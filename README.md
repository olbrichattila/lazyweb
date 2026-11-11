# Lazy Coding Agent website

A framework-free static website for Lazy Coding Agent, built with HTML, CSS, and one small optional release-refresh script. The site has no build step or package dependency. Product copy summarizes reviewed application README, help and source. The download page uses GitHub's latest-release API in the browser when available; its checked-in fallback is v0.1.0, based on the GitHub release metadata snapshot checked on 2026-11-11. The release was published, not a draft or prerelease, at 2026-11-11T22:13:18Z. Release evidence and all six GitHub-published asset digests are recorded below and on the download page. The release body links the first-release changelog `https://github.com/attilaolbrich/lazycodingagent/commits/v0.1.0`. These are source/release context, not proof of runtime quality or a claim of broader capability. This checked-in data is a fallback, not a guarantee of the latest release at viewing time. Browser/API behavior and deployment remain unverified. The application README still describes AI/model execution as in active integration—public copy retains that maturity caveat. See the evidence ledger and content plan before changing public claims.

## Structure

- `index.html`, `features.html`, `agents.html`, `download.html`, `roadmap.html`, `community.html`, `privacy.html`, `404.html` — root pages
- `docs/index.html` — documentation hub; `docs/*.html` topic guides adapted from reviewed application `help/`
- `docs/PRODUCT_FEATURE_INVENTORY.md` — source-evidence ledger, safe status distinctions and launch gates
- `docs/WEBSITE_CONTENT_PLAN.md` — canonical publishable facts, per-page guidance and owner confirmations
- `blog/index.html` — empty blog listing; no history fabricated
- `assets/site.css`, `assets/owl-mark.png`, `assets/neon-owl-emblem.png`, `assets/workspace-screenshot.webp` — shared styling and brand/UI artwork
- `assets/latest-release.js` — optional browser-side release and asset metadata refresh on the download page
- `robots.txt`, `sitemap.xml` — root-domain crawl metadata
- `tools/check_site.py` — dependency-free page, release-fallback, local-link and CSS checks
- `tools/test_latest_release.js` — dependency-free mocked updater regression tests (Node.js)
- `DEPLOYMENT.md` — conditional DigitalOcean App Platform setup guidance

## Evidence and public claims

“Implemented in reviewed source/docs” is not equivalent to user-tested on every platform or fully mature. Current website descriptions cover the documented workspace/editor, modes and tool boundaries, sessions and execution detail, model/image examples, terminal caveats, themes and project rules. Multi-agent collaboration, execution plans, workspace knowledge/RAG, The Brain and embedded SQLite/vector retrieval remain planned/future work, not current features.

Do not claim overall product readiness until the owner confirms the README integration status. The download page optionally requests GitHub's latest-release API in the browser and may update known asset links and valid published digests when its response is usable. Its checked-in v0.1.0 snapshot remains available if the request fails. The first-release commit list is linked as changelog context; no broader product capability claim is inferred from release metadata. No deployed-site, browser/API refresh, installation, or product maturity test was performed. Do not add unverified legal/license statements, community features or hosting/privacy guarantees. See `docs/PRODUCT_FEATURE_INVENTORY.md` for citations and `docs/WEBSITE_CONTENT_PLAN.md` for remaining launch gates.

## Editing

Edit each page's semantic HTML directly and keep the shared header/footer, skip link, page title, description, canonical, Open Graph metadata, active navigation and disclosure copy consistent. Use `assets/site.css` for shared styles. Internal page and asset links are document-relative so they work under `file://` and when deployed at the domain root. Navigation uses native `<details>` on narrow layouts. Only the download page loads a small optional script; its checked-in release links work without JavaScript.

## Documentation and blog

The product help topics were reviewed in the separate application repository's `help/` directory. This website does not link to missing local help files or copy them wholesale. The owner must confirm a public source destination and publication rights before adding links or curated guides. Keep the blog empty until approved posts exist; never create fake past dates/posts.

## Downloads

[download.html](download.html) contains checked-in v0.1.0 fallback links and GitHub-published SHA-256 digests for Windows, Linux `.deb` (amd64 and arm64), AppImage, and macOS disk images (Intel and Apple Silicon). The canonical latest-release API `https://api.github.com/repos/attilaolbrich/lazycodingagent/releases/latest` was checked on 2026-11-11; it identified tag `v0.1.0`, published at `2026-11-11T22:13:18Z` with `draft: false` and `prerelease: false`. The tag API is `https://api.github.com/repos/attilaolbrich/lazycodingagent/releases/tags/v0.1.0`; release page: `https://github.com/attilaolbrich/lazycodingagent/releases/tag/v0.1.0`. The release body links the first-release changelog `https://github.com/attilaolbrich/lazycodingagent/commits/v0.1.0`. Release notes and source comparisons are context, not independently validated runtime claims.

The six uploaded assets and SHA-256 digests below are GitHub API-published metadata; the files were not downloaded or independently hashed. Direct URLs follow the v0.1.0 release-download path:

| Platform artifact | Filename | Direct URL | GitHub-published SHA-256 |
|---|---|---|---|
| Windows installer | `LazyCodingAgent-0.1.0-win64-Setup.exe` | [Download](https://github.com/attilaolbrich/lazycodingagent/releases/download/v0.1.0/LazyCodingAgent-0.1.0-win64-Setup.exe) | `edf9ba9bfebd8135554a679afdf3d48f4c3ca52691d18950d24f2dfccff73330` |
| Linux amd64 Debian | `LazyCodingAgent-0.1.0-amd64.deb` | [Download](https://github.com/attilaolbrich/lazycodingagent/releases/download/v0.1.0/LazyCodingAgent-0.1.0-amd64.deb) | `5b9e632a6c921a8c33b524e6af28c549d13c15a46573009022d681d9fec5930b` |
| Linux arm64 Debian | `LazyCodingAgent-0.1.0-arm64.deb` | [Download](https://github.com/attilaolbrich/lazycodingagent/releases/download/v0.1.0/LazyCodingAgent-0.1.0-arm64.deb) | `de270a7f1f36b337730cc7a35fb562f2d7e4a6c7ad9a7b2d68227af6558d3967` |
| Linux x86_64 AppImage | `LazyCodingAgent-0.1.0-x86_64.AppImage` | [Download](https://github.com/attilaolbrich/lazycodingagent/releases/download/v0.1.0/LazyCodingAgent-0.1.0-x86_64.AppImage) | `5899b70e9f329b3752226b220fd64742f98db7f3b0b76d91807f22f25569dc5c` |
| macOS Intel disk image | `LazyCodingAgent-0.1.0-x86_64.dmg` | [Download](https://github.com/attilaolbrich/lazycodingagent/releases/download/v0.1.0/LazyCodingAgent-0.1.0-x86_64.dmg) | `083c372445fff516b25387d5d3447d9c5116debd26fd0cafbcf3943f28cb28d8` |
| macOS Apple Silicon disk image | `LazyCodingAgent-0.1.0-aarch64.dmg` | [Download](https://github.com/attilaolbrich/lazycodingagent/releases/download/v0.1.0/LazyCodingAgent-0.1.0-aarch64.dmg) | `40c848c0569c35f34a2cb91d2f14c3da32c22e494cb6e9ea8440b36591a278ac` |

The fallback is a dated snapshot, not a guarantee of the latest version at viewing time. On page load, `assets/latest-release.js` optionally requests the latest-release API with a bounded timeout. On a complete response it updates the version, release-page link, supported asset URLs and valid SHA-256 digests. Missing artifacts disable only their corresponding buttons and are explained; a digest is replaced only with a valid 64-hex SHA-256 value. API failure, timeout, malformed metadata, and digest-less assets do not erase the static fallback. Browser/API refresh and deployed-site behavior remain unverified. The listed digests are supplied by GitHub release metadata and were not independently recalculated; independent verification requires downloading each exact file and hashing it.

When publishing a release, query the canonical GitHub Releases API and confirm the release is published (not draft or prerelease). Record verification date, source, tag, each asset filename/direct URL and its SHA-256 digest. Prefer the API-published digest; if absent, independently download and hash the exact artifact, or omit that fallback digest rather than carrying a stale value. Update the checked-in fallback version, release link, asset links, filenames and digests together in `download.html` so the page works without JavaScript/API access. Keep artifact suffixes in `assets/latest-release.js` aligned with verified release naming. Run both checks below and manually preview API-success/API-failure and responsive page behavior; do not claim API/browser or deployment verification unless actually tested.

The header **Download** button continues to point at the releases index. Build-from-source remains documented separately via the app repository README.

## Local preview and validation

No production runtime, build step, or package dependency is required. Open `index.html` directly in a browser to preview pages/assets; document-relative links work from disk and domain root. Run the dependency-free integrity checker and updater tests with Python 3 and Node.js:

```sh
python3 tools/check_site.py
node --test tools/test_latest_release.js
```

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md). Website repository, branch, source/output directory, domain, HTTPS, redirects and 404 routing need owner confirmation in the current DigitalOcean App Platform UI and actual configuration. No deployment has been verified.
