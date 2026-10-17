# Static deployment guide (DigitalOcean App Platform)

This site consists of static HTML, CSS and image assets. It has no build step, server runtime, Dockerfile, or package dependency. These instructions are conditional because the actual website GitHub repository and current App Platform UI/configuration have not been inspected.

## Before setup

1. Put this website project in the intended GitHub website repository; verify the repository and branch are the ones the owner intends to publish. This workspace is not currently a Git repository.
2. Confirm that the repository root contains `index.html`, all root pages, `assets/`, `docs/`, and `blog/`. If the site is nested in a subdirectory, select that actual source directory instead.
3. In DigitalOcean App Platform, create an app and connect the website repository/branch. Select a **Static Site** component (not a service/container).
4. In the current component settings, set the source directory to the directory containing `index.html`. Set the output directory to that same directory if the UI requests it; this project has no separate generated output. Leave build command blank/not configured when permitted. Confirm the current UI's accepted values and behavior rather than assuming a setting.
5. Deploy, then test `/`, each HTML page, `/docs/`, `/blog/`, CSS/image URLs, and an unknown route. The repository includes `404.html`; verify whether the selected App Platform static site configuration serves it for unknown paths and configure routing only as supported by current platform documentation/UI.

## Domain and HTTPS

Add `lazycodingagent.com` (and `www` only if intended) in the App Platform domain settings. Follow the DNS records and verification instructions shown by DigitalOcean for this app and registrar; do not copy generic record values from this document. Allow DNS propagation, verify domain ownership, and confirm the platform reports HTTPS/certificate readiness. Test both intended hostnames over HTTPS and decide/verify a canonical redirect if required.

## Updates and smoke checks

Push reviewed website changes to the connected branch. Confirm the platform's automatic deployment behavior in the app settings, check deployment logs/status, and smoke-test changed pages/assets afterward. Keep release facts and platform configuration current; do not publish unverified application downloads.

## Owner confirmation / readiness blockers

- Confirm website repository, branch, source directory and current App Platform build/output settings.
- Confirm custom 404 behavior and domain-root hosting at the canonical domain; internal site URLs are document-relative and work at the root.
- Confirm domain/DNS ownership, `www` policy, HTTPS, and redirects.
- Confirm production host behavior for the privacy notice.
- Product release readiness is **unverified**: source/help were reviewed, but owner confirmation of the README integration status, live build/runtime verification, release assets, privacy contact/hosting behavior, and direct community/license verification remain outstanding.

No claim is made here about DigitalOcean requirements beyond the conditional operational steps above. Check current DigitalOcean documentation and the selected app's settings before deployment.
