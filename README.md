# Lazy Coding Agent website

A framework-free static website for Lazy Coding Agent, built with HTML, CSS, and one small optional release-refresh script. The site has no build step or package dependency. Product copy summarizes reviewed application README, help and source. The download page uses GitHub's latest-release API in the browser when available; its checked-in fallback is v0.1.17, verified against the published GitHub release API on 2026-10-25 (release tag, six asset names/URLs, and all six published SHA-256 digests). This checked-in data is a fallback, not a guarantee of the latest release at viewing time. API/browser behavior and deployment remain unverified. The application README still describes AI/model execution as in active integration—public copy retains that maturity caveat. See the evidence ledger and content plan before changing public claims.

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

Do not claim overall product readiness until the owner confirms the README integration status. The download page checks GitHub's latest-release API in the browser and updates known asset links and valid published digests when the response is usable. Its checked-in v0.1.17 data remains available if the request fails; release metadata and all six published asset digests were checked against the canonical GitHub Releases API on 2026-10-25. No deployed-site, live browser/API refresh, installation, or product maturity test was performed. Do not add unverified legal/license statements, community features or hosting/privacy guarantees. See `docs/PRODUCT_FEATURE_INVENTORY.md` for citations and `docs/WEBSITE_CONTENT_PLAN.md` for remaining launch gates.

## Editing

Edit each page's semantic HTML directly and keep the shared header/footer, skip link, page title, description, canonical, Open Graph metadata, active navigation and disclosure copy consistent. Use `assets/site.css` for shared styles. Internal page and asset links are document-relative so they work under `file://` and when deployed at the domain root. Navigation uses native `<details>` on narrow layouts. Only the download page loads a small optional script; its checked-in release links work without JavaScript.

## Documentation and blog

The product help topics were reviewed in the separate application repository's `help/` directory. This website does not link to missing local help files or copy them wholesale. The owner must confirm a public source destination and publication rights before adding links or curated guides. Keep the blog empty until approved posts exist; never create fake past dates/posts.

## Downloads

[download.html](download.html) contains checked-in v0.1.17 fallback links and GitHub-published SHA-256 digests for Windows, Linux `.deb` (amd64 and arm64), AppImage, and macOS disk images (Intel and Apple Silicon). The verified release tag is `v0.1.17`, published 2026-10-25; source: `https://api.github.com/repos/olbrichattila/lazycodingagent/releases/latest` (HTTP 200; release page `https://github.com/olbrichattila/lazycodingagent/releases/tag/v0.1.17`). Verified assets, direct URLs, and GitHub-published digests: `LazyCodingAgent-0.1.17-win64-Setup.exe` — `https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.17/LazyCodingAgent-0.1.17-win64-Setup.exe` — `84e17ccbdf7b8a77e215bd58a4cf4bc253cdfa2fa9e9089e0afb981e1d7405be`; `LazyCodingAgent-0.1.17-amd64.deb` — `https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.17/LazyCodingAgent-0.1.17-amd64.deb` — `ecd9b2892814d1583d5900406cd281c40d71a065d726eecfba71ce15ddb7e575`; `LazyCodingAgent-0.1.17-arm64.deb` — `https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.17/LazyCodingAgent-0.1.17-arm64.deb` — `08a6924eebb8d58e430af9d69ced03189744884f7108d40c45bc441d212d4919`; `LazyCodingAgent-0.1.17-x86_64.AppImage` — `https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.17/LazyCodingAgent-0.1.17-x86_64.AppImage` — `6d1d72af31b18872fa1b81c24fe82b3e0a3f93d24754284e1e0223a4aa9d80b2`; `LazyCodingAgent-0.1.17-x86_64.dmg` — `https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.17/LazyCodingAgent-0.1.17-x86_64.dmg` — `f10615bbb4bfc6576b65c25c9a3c14ff28e62af7022af46d179276dcd9bfdb30`; `LazyCodingAgent-0.1.17-aarch64.dmg` — `https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.17/LazyCodingAgent-0.1.17-aarch64.dmg` — `0ddaaa95a4a38ed3784fea546cb0de927b09029cdfe197a0245d2514cae26990`. On page load, `assets/latest-release.js` requests the latest GitHub release API with a bounded timeout. On a complete response it updates the version, release-page links, supported asset URLs and valid SHA-256 digests. A missing artifact disables only its corresponding button and is explained; a digest is replaced only with a valid 64-hex SHA-256 value. API failure, timeout, malformed metadata, and digest-less assets do not erase the static fallback. The API refresh/browser behavior and deployed site were not manually tested.

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
