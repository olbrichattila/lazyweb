/* Keep versioned release links and checksum details in sync with GitHub Releases. */
(() => {
  "use strict";

  const repository = "olbrichattila/lazycodingagent";
  const releaseApi = `https://api.github.com/repos/${repository}/releases/latest`;
  const suffixes = [
    "win64-Setup.exe",
    "x86_64.dmg",
    "aarch64.dmg",
    "amd64.deb",
    "x86_64.AppImage",
    "arm64.deb",
  ];

  function replaceVersion(value, oldVersion, newVersion) {
    return value.split(oldVersion).join(newVersion);
  }

  async function updateLatestRelease() {
    const versionLabel = document.querySelector(".page-head .lead strong");
    if (!versionLabel) return;

    try {
      const response = await fetch(releaseApi, {
        headers: { Accept: "application/vnd.github+json" },
        cache: "no-cache",
      });
      if (!response.ok) throw new Error(`GitHub API returned ${response.status}`);

      const release = await response.json();
      const version = (release.tag_name || "").replace(/^v/, "");
      if (!version || !Array.isArray(release.assets)) throw new Error("Latest release data is incomplete");

      const oldVersion = versionLabel.textContent.trim();
      if (oldVersion !== version) {
        const walker = document.createTreeWalker(document, NodeFilter.SHOW_TEXT);
        while (walker.nextNode()) {
          walker.currentNode.nodeValue = replaceVersion(walker.currentNode.nodeValue, oldVersion, version);
        }
        for (const element of document.querySelectorAll("meta[content], a[href]")) {
          for (const attribute of ["content", "href"]) {
            if (element.hasAttribute(attribute)) {
              element.setAttribute(attribute, replaceVersion(element.getAttribute(attribute), oldVersion, version));
            }
          }
        }
      }

      const assetBySuffix = new Map();
      for (const suffix of suffixes) {
        const asset = release.assets.find((item) => item.name.endsWith(`-${suffix}`));
        if (asset) assetBySuffix.set(suffix, asset);
      }

      for (const link of document.querySelectorAll('a[href*="/releases/download/"]')) {
        const suffix = suffixes.find((item) => link.href.endsWith(`-${item}`));
        const asset = suffix && assetBySuffix.get(suffix);
        if (asset) {
          link.href = asset.browser_download_url;
          link.hidden = false;
        } else {
          link.hidden = true;
        }
      }

      const releasePage = release.html_url || `https://github.com/${repository}/releases/latest`;
      for (const link of document.querySelectorAll('a[href*="/releases/tag/"]')) {
        link.href = releasePage;
      }

      for (const item of document.querySelectorAll(".checksum-list li")) {
        const codes = item.querySelectorAll("code");
        if (!codes.length) continue;
        const suffix = suffixes.find((candidate) => codes[0].textContent.endsWith(`-${candidate}`));
        const asset = suffix && assetBySuffix.get(suffix);
        if (!asset) {
          item.hidden = true;
          continue;
        }
        codes[0].textContent = asset.name;
        codes[1].textContent = asset.digest
          ? asset.digest.replace(/^sha256:/i, "")
          : "SHA-256 digest not published for this asset";
      }
    } catch (error) {
      // The page's checked-in links remain usable if GitHub or its API is unavailable.
      console.warn("Could not refresh the latest release details from GitHub.", error);
    }
  }

  updateLatestRelease();
})();
