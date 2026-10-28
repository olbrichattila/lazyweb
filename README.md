# Lazy Coding Agent website

A framework-free static website for Lazy Coding Agent, built with HTML, CSS, and one small optional release-refresh script. The site has no build step or package dependency. Product copy summarizes reviewed application README, help and source. The download page uses GitHub's latest-release API in the browser when available; its checked-in fallback is v0.1.38, based on the GitHub release metadata snapshot dated 2026-10-28. The release was published, not a draft or prerelease. Release evidence and all six API-published asset digests are recorded below and on the download page. The comparison from v0.1.37 to v0.1.38 records a maintenance fix; no broader user-facing feature claims are inferred. This checked-in data is a fallback, not a guarantee of the latest release at viewing time. Browser/API behavior and deployment remain unverified. The application README still describes AI/model execution as in active integration—public copy retains that maturity caveat. See the evidence ledger and content plan before changing public claims.

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

Do not claim overall product readiness until the owner confirms the README integration status. The download page checks GitHub's latest-release API in the browser and updates known asset links and valid published digests when the response is usable. Its checked-in v0.1.38 snapshot remains available if the request fails. The comparison from v0.1.37 to v0.1.38 records maintenance/fix context only; no wider product claims are inferred. No deployed-site, browser/API refresh, installation, or product maturity test was performed. Do not add unverified legal/license statements, community features or hosting/privacy guarantees. See `docs/PRODUCT_FEATURE_INVENTORY.md` for citations and `docs/WEBSITE_CONTENT_PLAN.md` for remaining launch gates.

## Editing

Edit each page's semantic HTML directly and keep the shared header/footer, skip link, page title, description, canonical, Open Graph metadata, active navigation and disclosure copy consistent. Use `assets/site.css` for shared styles. Internal page and asset links are document-relative so they work under `file://` and when deployed at the domain root. Navigation uses native `<details>` on narrow layouts. Only the download page loads a small optional script; its checked-in release links work without JavaScript.

## Documentation and blog

The product help topics were reviewed in the separate application repository's `help/` directory. This website does not link to missing local help files or copy them wholesale. The owner must confirm a public source destination and publication rights before adding links or curated guides. Keep the blog empty until approved posts exist; never create fake past dates/posts.

## Downloads

[download.html](download.html) contains checked-in v0.1.38 fallback links and GitHub-published SHA-256 digests for Windows, Linux `.deb` (amd64 and arm64), AppImage, and macOS disk images (Intel and Apple Silicon). The canonical latest-release API `https://api.github.com/repos/olbrichattila/lazycodingagent/releases/latest` was checked on 2026-10-28; it identified tag `v0.1.38`, published at `2026-10-28T18:27:49Z` with `draft: false` and `prerelease: false`. The tag API is `https://api.github.com/repos/olbrichattila/lazycodingagent/releases/tags/v0.1.38`; release page: `https://github.com/olbrichattila/lazycodingagent/releases/tag/v0.1.38`. The release body links the comparison/changelog `https://github.com/olbrichattila/lazycodingagent/compare/v0.1.37...v0.1.38`. Its single commit, “Fix rules content fingerprint to use stable file timestamps,” describes using raw `FindFirst` time, adding a unit test, and refreshing main-form designer PPI scaling. This is maintenance/fix context, not a broader product capability claim.
The six uploaded assets and SHA-256 digests below are GitHub API-published metadata; the files were not downloaded or independently hashed. Direct URLs follow the v0.1.38 release-download path:
| Platform artifact | Filename | Direct URL | GitHub-published SHA-256 |
|---|---|---|---|
| Windows installer | `LazyCodingAgent-0.1.38-win64-Setup.exe` | [Download](https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.38/LazyCodingAgent-0.1.38-win64-Setup.exe) | `c3e4333e12c9e8c4979ea5d531ad9b42f2905b224b28e483984c59b6fec8596a` |
| Linux amd64 Debian | `LazyCodingAgent-0.1.38-amd64.deb` | [Download](https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.38/LazyCodingAgent-0.1.38-amd64.deb) | `6270b1b01a312b265ea780134cf8cf7debbfb7627a7323c97fbb319232729db5` |
| Linux arm64 Debian | `LazyCodingAgent-0.1.38-arm64.deb` | [Download](https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.38/LazyCodingAgent-0.1.38-arm64.deb) | `579bf9bf92fd920dea2448435df31a97aa151cfc5f608ebdcea9e9604fff509f` |
| Linux x86_64 AppImage | `LazyCodingAgent-0.1.38-x86_64.AppImage` | [Download](https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.38/LazyCodingAgent-0.1.38-x86_64.AppImage) | `e2bf3d7cf74309b6eada64fc211cdf71a35ecf5feff7740e1b84e12f4c273de0` |
| macOS Intel disk image | `LazyCodingAgent-0.1.38-x86_64.dmg` | [Download](https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.38/LazyCodingAgent-0.1.38-x86_64.dmg) | `c02271ee0c1340a539f0f6e5d2baf6c623f43e4a38ca20821ea403ae1ea9e7a7` |
| macOS Apple Silicon disk image | `LazyCodingAgent-0.1.38-aarch64.dmg` | [Download](https://github.com/olbrichattila/lazycodingagent/releases/download/v0.1.38/LazyCodingAgent-0.1.38-aarch64.dmg) | `9cfb7b70737cfa88499ea1acc3178bfd76800e065c18fd7376b775fc049f64f9` |

The fallback is a dated snapshot, not a guarantee of the latest version at viewing time. On page load, `assets/latest-release.js` requests the latest-release API with a bounded timeout. On a complete response it updates the version, release-page link, supported asset URLs and valid SHA-256 digests. Missing artifacts disable only their corresponding buttons and are explained; a digest is replaced only with a valid 64-hex SHA-256 value. API failure, timeout, malformed metadata, and digest-less assets do not erase the static fallback. Browser/API refresh and deployed-site behavior remain unverified.
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
