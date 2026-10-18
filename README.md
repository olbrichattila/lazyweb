# Lazy Coding Agent website

A framework-free static website for Lazy Coding Agent, built with HTML and CSS only. Product copy summarizes reviewed application README, help and source. Installers and packages are advertised on [download.html](download.html) from GitHub Releases (currently **v0.1.11**). The application README still describes AI/model execution as in active integration—public copy retains that maturity caveat. See the evidence ledger and content plan before changing public claims.

## Structure

- `index.html`, `features.html`, `agents.html`, `download.html`, `roadmap.html`, `community.html`, `privacy.html`, `404.html` — root pages
- `docs/index.html` — documentation hub; `docs/*.html` topic guides adapted from reviewed application `help/`
- `docs/PRODUCT_FEATURE_INVENTORY.md` — source-evidence ledger, safe status distinctions and launch gates
- `docs/WEBSITE_CONTENT_PLAN.md` — canonical publishable facts, per-page guidance and owner confirmations
- `blog/index.html` — empty blog listing; no history fabricated
- `assets/site.css`, `assets/owl-mark.png`, `assets/neon-owl-emblem.png`, `assets/workspace-screenshot.webp` — shared styling and brand/UI artwork
- `robots.txt`, `sitemap.xml` — root-domain crawl metadata
- `tools/check_site.py` — dependency-free basic metadata, landmark, local-link and CSS check
- `DEPLOYMENT.md` — conditional DigitalOcean App Platform setup guidance

## Evidence and public claims

“Implemented in reviewed source/docs” is not equivalent to user-tested on every platform or fully mature. Current website descriptions cover the documented workspace/editor, modes and tool boundaries, sessions and execution detail, model/image examples, terminal caveats, themes and project rules. Multi-agent collaboration, execution plans, workspace knowledge/RAG, The Brain and embedded SQLite/vector retrieval remain planned/future work, not current features.

Do not claim overall product readiness until the owner confirms the README integration status. Release assets on GitHub are listed on `download.html` with version-specific URLs and SHA-256 digests; update that page when the application repository tags a new release. Do not add unverified legal/license statements, community features or hosting/privacy guarantees. See `docs/PRODUCT_FEATURE_INVENTORY.md` for citations and `docs/WEBSITE_CONTENT_PLAN.md` for remaining launch gates.

## Editing

Edit each page's semantic HTML directly and keep the shared header/footer, skip link, page title, description, canonical, Open Graph metadata, active navigation and disclosure copy consistent. Use `assets/site.css` for shared styles. Internal page and asset links are document-relative so they work under `file://` and when deployed at the domain root. Navigation uses native `<details>` on narrow layouts; no script or build process is needed.

## Documentation and blog

The product help topics were reviewed in the separate application repository's `help/` directory. This website does not link to missing local help files or copy them wholesale. The owner must confirm a public source destination and publication rights before adding links or curated guides. Keep the blog empty until approved posts exist; never create fake past dates/posts.

## Downloads

[download.html](download.html) links to GitHub Releases (`https://github.com/olbrichattila/lazycodingagent/releases`) with per-platform buttons for the current release (**0.1.11** as of the last site update): Windows installer, Linux `.deb` (amd64 and arm64), AppImage, and macOS disk images (Intel and Apple Silicon).

When the application repository publishes a new tag, update on `download.html`:

1. Version string in the page head, lead, and checksum section title
2. All six `releases/download/vX.Y.Z/...` asset URLs (filenames include the version)
3. SHA-256 digests from the GitHub release assets (authoritative on the release page)

The header **Download** button continues to point at the releases index. Build-from-source remains documented separately via the app repository README.

## Local preview and validation

No production runtime or local server dependency is required. Open `index.html` directly in a browser to preview pages/assets; document-relative links work from disk and domain root. Run the dependency-free integrity checker with:

```sh
python3 tools/check_site.py
```

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md). Website repository, branch, source/output directory, domain, HTTPS, redirects and 404 routing need owner confirmation in the current DigitalOcean App Platform UI and actual configuration. No deployment has been verified.
