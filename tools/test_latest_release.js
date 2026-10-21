"use strict";

const assert = require("node:assert/strict");
const { test } = require("node:test");
const { refreshRelease, artifacts, requestTimeoutMs } = require("../assets/latest-release.js");

const digest = "a".repeat(64);
const release = (overrides = {}) => ({
  tag_name: "v1.2.3",
  html_url: "https://github.com/olbrichattila/lazycodingagent/releases/tag/v1.2.3",
  assets: artifacts.map((artifact) => ({
    name: `LazyCodingAgent-1.2.3-${artifact.suffix}`,
    browser_download_url: `https://github.com/olbrichattila/lazycodingagent/releases/download/v1.2.3/LazyCodingAgent-1.2.3-${artifact.suffix}`,
    digest: `sha256:${digest}`,
  })),
  ...overrides,
});

function element(extra = {}) {
  return { textContent: "", hidden: false, href: "", ...extra };
}

function makeDocument({ malformedChecksum = false } = {}) {
  const elements = {
    "[data-release-version]": [element({ textContent: "0.1.15" })],
    "[data-release-page]": [element({ href: "https://github.com/olbrichattila/lazycodingagent/releases/tag/v0.1.15" })],
    "[data-checksum-version]": [element({ textContent: "SHA-256 checksums (0.1.15)" })],
    "[data-release-status]": [element({ textContent: "fallback status" })],
    "[data-checksum-status]": [element({ textContent: "fallback digest notice" })],
  };
  for (const artifact of artifacts) {
    elements[`[data-release-asset="${artifact.id}"]`] = [element({
      href: `https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.15/LazyCodingAgent-0.1.15-${artifact.suffix}`,
    })];
    elements[`[data-asset-status="${artifact.id}"]`] = [element({
      textContent: "fallback availability",
      hidden: true,
    })];
    const codes = malformedChecksum && artifact.id === "windows"
      ? [element({ textContent: `LazyCodingAgent-0.1.15-${artifact.suffix}` })]
      : [
          element({ textContent: `LazyCodingAgent-0.1.15-${artifact.suffix}` }),
          element({ textContent: "b".repeat(64) }),
        ];
    elements[`[data-checksum="${artifact.id}"]`] = [element({
      hidden: false,
      querySelectorAll: (selector) => selector === "code" ? codes : [],
    })];
  }
  return {
    elements,
    querySelectorAll(selector) { return elements[selector] || []; },
  };
}

function fetchOk(body) {
  return async () => ({ ok: true, json: async () => body });
}

test("successful metadata refreshes version, release page, explicit asset links and valid digests", async () => {
  const document = makeDocument();
  await refreshRelease(document, fetchOk(release()), undefined, 100);
  assert.equal(document.elements["[data-release-version]"][0].textContent, "1.2.3");
  assert.equal(document.elements["[data-release-page]"][0].href, release().html_url);
  assert.match(document.elements['[data-release-asset="windows"]'][0].href, /v1\.2\.3/);
  assert.equal(document.elements['[data-checksum="windows"]'][0].querySelectorAll("code")[1].textContent, digest);
  assert.match(document.elements["[data-release-status]"][0].textContent, /latest published release, 1\.2\.3/);
});

test("fetch failure leaves all checked-in fallback values intact", async () => {
  const document = makeDocument();
  await refreshRelease(document, async () => { throw new Error("offline"); }, undefined, 100);
  assert.equal(document.elements["[data-release-version]"][0].textContent, "0.1.15");
  assert.match(document.elements['[data-release-asset="windows"]'][0].href, /v0\.1\.15/);
  assert.equal(document.elements['[data-checksum="windows"]'][0].querySelectorAll("code")[1].textContent, "b".repeat(64));
});

test("a stalled fetch is bounded and does not mutate fallbacks", async () => {
  const document = makeDocument();
  await refreshRelease(document, () => new Promise(() => {}), undefined, 10);
  assert.equal(document.elements["[data-release-version]"][0].textContent, "0.1.15");
  assert.ok(requestTimeoutMs <= 10000);
});

test("malformed release metadata is rejected without partial updates", async () => {
  const document = makeDocument();
  await refreshRelease(document, fetchOk({ tag_name: "not-a-version", assets: [] }), undefined, 100);
  assert.equal(document.elements["[data-release-version]"][0].textContent, "0.1.15");
  assert.equal(document.elements["[data-release-status]"][0].textContent, "fallback status");
});

test("digest-less assets keep their download but do not expose a stale checksum", async () => {
  const document = makeDocument();
  const data = release();
  data.assets.find((asset) => asset.name.endsWith("win64-Setup.exe")).digest = null;
  await refreshRelease(document, fetchOk(data), undefined, 100);
  assert.equal(document.elements['[data-release-asset="windows"]'][0].hidden, false);
  assert.equal(document.elements['[data-checksum="windows"]'][0].hidden, true);
  assert.match(document.elements["[data-checksum-status]"][0].textContent, /No digest was published/);
});

test("missing assets disable only matching fallback buttons and explain availability", async () => {
  const document = makeDocument();
  const data = release();
  data.assets = data.assets.filter((asset) => !asset.name.endsWith("arm64.deb"));
  await refreshRelease(document, fetchOk(data), undefined, 100);
  assert.equal(document.elements['[data-release-asset="linux-arm64"]'][0].hidden, true);
  assert.equal(document.elements['[data-asset-status="linux-arm64"]'][0].hidden, false);
  assert.match(document.elements['[data-asset-status="linux-arm64"]'][0].textContent, /not available/);
  assert.equal(document.elements['[data-release-asset="windows"]'][0].hidden, false);
});

test("a malformed checksum row cannot interrupt processing other artifacts", async () => {
  const document = makeDocument({ malformedChecksum: true });
  await refreshRelease(document, fetchOk(release()), undefined, 100);
  assert.equal(document.elements['[data-checksum="windows"]'][0].hidden, true);
  assert.equal(document.elements['[data-checksum="linux-amd64"]'][0].hidden, false);
  assert.equal(document.elements['[data-release-asset="linux-amd64"]'][0].hidden, false);
});
