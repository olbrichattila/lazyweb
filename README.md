# Lazy Coding Agent website

A framework-free static website for Lazy Coding Agent, built with HTML and CSS only. Product details are deliberately evidence-gated: the workspace did not include application source or product documentation, so no feature, release, platform, roadmap, or license claims are verified. See the evidence ledger and content plan before changing public product copy.

## Structure

- `index.html`, `features.html`, `agents.html`, `download.html`, `roadmap.html`, `community.html`, `privacy.html`, `404.html` — root pages
- `docs/index.html` — documentation status landing page
- `docs/PRODUCT_FEATURE_INVENTORY.md` — evidence ledger and verification criteria
- `docs/WEBSITE_CONTENT_PLAN.md` — canonical content truth and page plan
- `blog/index.html` — empty blog listing; no history fabricated
- `assets/site.css`, `assets/owl-mark.png` — shared styling and derived copy of provided brand art
- `robots.txt`, `sitemap.xml` — root-domain crawl metadata
- `tools/check_site.py` — dependency-free basic metadata, landmark, local-link and CSS check
- `DEPLOYMENT.md` — conditional DigitalOcean App Platform setup guidance

## Editing

Edit each page's semantic HTML directly and keep the shared header/footer, skip link, page title, description, canonical, Open Graph metadata, active navigation and disclosure copy consistent. Use `assets/site.css` (from the root page) for shared styles. Internal page and asset links are document-relative so they work both under `file://` and when deployed at the domain root. Navigation is plain HTML with a native `<details>` menu for narrow layouts; no script or build process is needed.

Keep product assertions tied to the inventory. Before changing `Unverified` to a product status, obtain an authorized source snapshot and record file-level evidence, UI wiring and tests where possible. Do not add download links, versions, platform support, roadmap dates, or community features until checked.

## Documentation and blog

Add documentation pages only when grounded in actual help/source and verified installation instructions. Link them from `docs/index.html`, maintain accessible headings and navigation, and add each public page to `sitemap.xml`.

The blog currently has no articles. When approved content exists, create a static article page with an accurate title, date, tags, reading time and body; link it from `blog/index.html` and the sitemap. Never create fake past dates/posts. Label unapproved vision material as draft.

## Downloads

Update `download.html` only after checking the canonical repository/release page and actual release assets, checksums/signatures if supplied, installation documentation, and platform support. Include no guessed version, binary URL, checksum, date, or prerequisites. Update related evidence in the inventory and content plan simultaneously.

## Local preview

No production runtime or local server dependency is required. Open `index.html` directly in a browser to preview the pages and assets; document-relative links work from disk as well as from a domain-root deployment. `tools/check_site.py` also checks local links and referenced assets.

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md). Repository, branch, output/source directory, domain, HTTPS, and 404 routing need owner confirmation against the current DigitalOcean App Platform UI. The workspace is not currently a Git repository.
