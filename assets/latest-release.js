/* Refresh explicit download-page fallbacks from GitHub Releases when available. */
(function (root) {
  "use strict";

  const repository = "olbrichattila/lazycodingagent";
  const releaseApi = `https://api.github.com/repos/${repository}/releases/latest`;
  const requestTimeoutMs = 8000;
  const artifacts = [
    { id: "windows", suffix: "win64-Setup.exe", label: "Windows installer" },
    { id: "mac-intel", suffix: "x86_64.dmg", label: "macOS Intel disk image" },
    { id: "mac-arm", suffix: "aarch64.dmg", label: "macOS Apple Silicon disk image" },
    { id: "linux-amd64", suffix: "amd64.deb", label: "Linux amd64 Debian package" },
    { id: "linux-appimage", suffix: "x86_64.AppImage", label: "Linux x86_64 AppImage" },
    { id: "linux-arm64", suffix: "arm64.deb", label: "Linux arm64 Debian package" },
  ];

  function safeRun(action) {
    try { action(); } catch (_) { /* A damaged optional element must not block other assets. */ }
  }

  function usableUrl(value) {
    try {
      const url = new URL(value);
      return url.protocol === "https:" && url.hostname === "github.com";
    } catch (_) {
      return false;
    }
  }

  function usableDigest(value) {
    const digest = typeof value === "string" ? value.replace(/^sha256:/i, "") : "";
    return /^[a-f\d]{64}$/i.test(digest) ? digest.toLowerCase() : "";
  }

  function releaseDetails(release) {
    if (!release || typeof release !== "object" || !Array.isArray(release.assets)) return null;
    const tag = typeof release.tag_name === "string" ? release.tag_name : "";
    const version = tag.replace(/^v/, "");
    if (!/^\d+\.\d+\.\d+(?:[-+][\w.-]+)?$/.test(version)) return null;

    const releasePage = usableUrl(release.html_url)
      ? release.html_url
      : `https://github.com/${repository}/releases/latest`;
    const byId = new Map();
    for (const artifact of artifacts) {
      const asset = release.assets.find((candidate) =>
        candidate && typeof candidate.name === "string" && candidate.name.endsWith(`-${artifact.suffix}`));
      if (!asset || !usableUrl(asset.browser_download_url)) continue;
      byId.set(artifact.id, {
        name: asset.name,
        url: asset.browser_download_url,
        digest: usableDigest(asset.digest),
      });
    }
    return { version, releasePage, byId };
  }

  function refreshRelease(document, fetchFunction, AbortControllerClass, timeoutMs = requestTimeoutMs) {
    if (!document || typeof fetchFunction !== "function") return Promise.resolve();
    let timer;
    let controller;
    let timedOut = false;
    const requestOptions = {
      headers: { Accept: "application/vnd.github+json" },
      cache: "no-cache",
    };
    if (typeof AbortControllerClass === "function") {
      controller = new AbortControllerClass();
      requestOptions.signal = controller.signal;
    }

    const timeout = new Promise((_, reject) => {
      timer = setTimeout(() => {
        timedOut = true;
        if (controller) safeRun(() => controller.abort());
        reject(new Error("GitHub release request timed out"));
      }, timeoutMs);
    });

    const request = Promise.resolve()
      .then(() => fetchFunction(releaseApi, requestOptions))
      .then((response) => {
        if (!response || !response.ok) throw new Error("GitHub release request failed");
        return response.json();
      });

    return Promise.race([request, timeout])
      .then((release) => {
        const details = releaseDetails(release);
        if (!details) throw new Error("GitHub release metadata is incomplete");

        // All response data is validated before any fallback content is changed.
        for (const label of document.querySelectorAll("[data-release-version]")) {
          safeRun(() => {
            if (label.tagName === "META") {
              label.content = label.content.replace(/(Lazy Coding Agent )\d+\.\d+\.\d+/, `$1${details.version}`);
            } else label.textContent = details.version;
          });
        }
        for (const link of document.querySelectorAll("[data-release-page]")) {
          safeRun(() => { link.href = details.releasePage; });
        }

        const unavailable = [];
        const digestUnavailable = [];
        for (const artifact of artifacts) {
          const asset = details.byId.get(artifact.id);
          for (const link of document.querySelectorAll(`[data-release-asset="${artifact.id}"]`)) {
            safeRun(() => {
              if (asset) {
                link.href = asset.url;
                link.hidden = false;
              } else {
                link.hidden = true;
              }
            });
          }
          for (const filename of document.querySelectorAll(`[data-release-filename="${artifact.id}"]`)) {
            safeRun(() => {
              filename.hidden = !asset;
              if (asset) filename.textContent = asset.name;
            });
          }
          for (const status of document.querySelectorAll(`[data-asset-status="${artifact.id}"]`)) {
            safeRun(() => {
              status.textContent = asset ? "" : `${artifact.label} is not available in this release.`;
              status.hidden = Boolean(asset);
            });
          }
          for (const row of document.querySelectorAll(`[data-checksum="${artifact.id}"]`)) {
            safeRun(() => {
              const codes = row.querySelectorAll("code");
              if (!asset || !asset.digest || codes.length !== 2) {
                row.hidden = true;
                return;
              }
              codes[0].textContent = asset.name;
              codes[1].textContent = asset.digest;
              row.hidden = false;
            });
          }
          if (!asset) unavailable.push(artifact.label);
          else if (!asset.digest) digestUnavailable.push(artifact.label);
        }

        for (const heading of document.querySelectorAll("[data-checksum-version]")) {
          safeRun(() => { heading.textContent = `SHA-256 checksums (${details.version})`; });
        }
        for (const note of document.querySelectorAll("[data-release-status]")) {
          safeRun(() => {
            note.textContent = unavailable.length
              ? `Showing ${details.version}. Not included in this release: ${unavailable.join(", ")}.`
              : `Showing the latest published release, ${details.version}.`;
          });
        }
        for (const note of document.querySelectorAll("[data-checksum-status]")) {
          safeRun(() => {
            note.textContent = digestUnavailable.length
              ? `Only validated published SHA-256 digests are shown. No digest was published for: ${digestUnavailable.join(", ")}.`
              : "Only SHA-256 digests published and validated for these assets are shown.";
          });
        }
      })
      .catch((error) => {
        // Do not mutate the checked-in version, direct links, or checksum fallbacks on failure.
        if (!timedOut) console.warn("Could not refresh the latest release details from GitHub.", error);
      })
      .finally(() => clearTimeout(timer));
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { refreshRelease, releaseDetails, artifacts, requestTimeoutMs };
  }
  if (root && root.document && typeof root.fetch === "function") {
    refreshRelease(root.document, root.fetch.bind(root), root.AbortController);
  }
})(typeof globalThis === "undefined" ? this : globalThis);
