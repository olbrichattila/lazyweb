# Website content plan (canonical source)

## Evidence boundary

The only product-specific evidence reviewed in this workspace is the supplied website implementation plan and four brand-image files. No application source, README/help, roadmap, releases, CI, license, or community settings were supplied. Product behavior, status, operating-system support, prerequisites, and actual download URLs are therefore **unverified**. The absence of evidence is not proof of absence. Pages must keep this distinction visible until an authorized source snapshot is reviewed.

## Approved/pending overview and proposed copy

- **Proposed hero line from the website plan:** “Your AI Engineering Workspace” and “Plan. Build. Review. Learn.” These are positioning copy, not verified descriptions of delivered functionality; preserve the contextual disclosure.
- **Verified capabilities:** None verified from application sources.
- **Differentiators:** None substantiated; do not claim.
- **Architecture:** Unknown. Do not portray planning, execution, review, approval, specialists, or “The Brain” as operational.
- **Open-source/license status:** Unverified. Do not assert open-source status until the actual license and repository are checked.
- **Platforms and prerequisites:** Unknown. Do not assert support for Windows, Linux, or macOS or provide build-from-source guidance without repository/build evidence.
- **Downloads/releases:** No assets or canonical releases URL verified. No version/date/checksum or download CTA/link.
- **Roadmap:** No product roadmap files available. Do not infer entries from the website implementation plan. Publish a clearly labeled evidence-pending state only.
- **Documentation topics:** No product help/source documentation available. Installation, workspaces, sessions, modes, providers, editing, tools, terminal, panels, themes, rules, troubleshooting, and building remain pending.
- **Community:** The plan supplies `https://github.com/olbrichattila/lazycodingagent` as the canonical repository URL; current existence, access, license, contribution guide, Issues, pull requests, Discussions, and releases have not been checked.
- **Privacy:** Authored website files are static HTML/CSS and local artwork, with no forms or authored analytics/cookie JavaScript. Hosting provider, logs, intermediaries, DNS/CDN, and production runtime behavior are unverified. State no blanket collection/cookie guarantees.

## Page structure and content rules

| Page | Content | Truth/safety rule |
|---|---|---|
| `/` | Hero, artwork, verification disclosure, links to status | Hero is positioning only; no feature/release promises |
| `/features.html` | Capability categories with evidence status | Mark unverified rather than inventing or claiming unavailable |
| `/agents.html` | Architecture evidence requirement | No operational workflow diagram until evidenced |
| `/download.html` | Release status and requirements needed | No versions, binaries, OS support, checksum, or direct release link until checked |
| `/roadmap.html` | Separate status categories | No fabricated roadmap items or dates |
| `/docs/` | Documentation status and evidence docs | No invented product instructions |
| `/blog/` | Empty listing with publishing guidance | No fabricated historical articles; draft vision needs approval |
| `/community.html` | Plan-provided repository address with availability caveat | Verify destination and each community feature before claims |
| `/privacy.html` | Authored site behavior and explicit host limits | Recheck against deployed config before launch |
| `/404.html` | Accessible recovery links | Host-specific error routing must be tested |

## Evidence-gated follow-up

Once the owner provides a source snapshot: build the ledger in `PRODUCT_FEATURE_INVENTORY.md`; use direct paths and references; confirm shipped status using UI/test/release evidence; then update feature, architecture, docs, download, roadmap, community, and privacy copy in one consistency pass. All content stays framework-free, static, and deployable at the canonical domain root. Deployment settings must be confirmed against the current DigitalOcean Static Site UI and actual repository configuration; do not assert a special output directory or 404 setting without that check.
