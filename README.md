# Lazy Coding Agent website

A framework-free static website for Lazy Coding Agent, built with HTML and CSS only. Product copy now summarizes reviewed application README, help and source while distinguishing implementation evidence from release/runtime verification. The application README says multi-window layout is implemented and AI/model execution is in active integration; the currency of that status needs owner confirmation. No live application run, release assets, external GitHub state, or current DigitalOcean deployment was verified. See the evidence ledger and content plan before changing public copy.

## Structure

- `index.html`, `features.html`, `agents.html`, `download.html`, `roadmap.html`, `community.html`, `privacy.html`, `404.html` — root pages
- `docs/index.html` — help topic index (help files are in the separate application repository, not copied here)
- `docs/PRODUCT_FEATURE_INVENTORY.md` — source-evidence ledger, safe status distinctions and launch gates
- `docs/WEBSITE_CONTENT_PLAN.md` — canonical publishable facts, per-page guidance and owner confirmations
- `blog/index.html` — empty blog listing; no history fabricated
- `assets/site.css`, `assets/owl-mark.png` — shared styling and local brand artwork
- `robots.txt`, `sitemap.xml` — root-domain crawl metadata
- `tools/check_site.py` — dependency-free basic metadata, landmark, local-link and CSS check
- `DEPLOYMENT.md` — conditional DigitalOcean App Platform setup guidance

## Evidence and public claims

“Implemented in reviewed source/docs” is not equivalent to released, live-tested, user-tested, or available to download. Current website descriptions cover the documented workspace/editor, modes and tool boundaries, sessions and execution detail, model/image examples, terminal caveats, themes and project rules. Multi-agent collaboration, execution plans, workspace knowledge/RAG, The Brain and embedded SQLite/vector retrieval remain planned/future work, not current features.

Do not claim overall product readiness until the owner confirms the README integration status and the product has been checked in a runnable build. Do not add download links, versions, checksums, legal/license statements, community features or hosting/privacy guarantees until verified. See `docs/PRODUCT_FEATURE_INVENTORY.md` for direct application-relative citations and `docs/WEBSITE_CONTENT_PLAN.md` for launch gates.

## Editing

Edit each page's semantic HTML directly and keep the shared header/footer, skip link, page title, description, canonical, Open Graph metadata, active navigation and disclosure copy consistent. Use `assets/site.css` for shared styles. Internal page and asset links are document-relative so they work under `file://` and when deployed at the domain root. Navigation uses native `<details>` on narrow layouts; no script or build process is needed.

## Documentation and blog

The product help topics were reviewed in the separate application repository's `help/` directory. This website does not link to missing local help files or copy them wholesale. The owner must confirm a public source destination and publication rights before adding links or curated guides. Keep the blog empty until approved posts exist; never create fake past dates/posts.

## Downloads

`download.html` remains release-pending. Update it only after confirming the canonical release destination, inspecting actual release assets and any supplied checksums/signatures, verifying install requirements and testing a distributable package. Build instructions and CI configuration are developer evidence, not consumer release proof.

## Local preview and validation

No production runtime or local server dependency is required. Open `index.html` directly in a browser to preview pages/assets; document-relative links work from disk and domain root. Run the dependency-free integrity checker with:

```sh
python3 tools/check_site.py
```

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md). Website repository, branch, source/output directory, domain, HTTPS, redirects and 404 routing need owner confirmation in the current DigitalOcean App Platform UI and actual configuration. No deployment has been verified.
