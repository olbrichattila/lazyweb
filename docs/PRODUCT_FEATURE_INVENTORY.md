# Product feature inventory and evidence ledger

> **Evidence gap — no application source snapshot was provided.** The accessible website workspace was inspected and contained only the implementation plan and four image assets under `temp/`. No Lazarus/Pascal/LFM application source, README, help files, tests, roadmap, release artifacts, workflows, license, or contribution guidance were available. Do not interpret `Unverified` as “not implemented” or as a development status. Nothing here is advertised as a released capability.

## Inventory

| Feature / evidence area | Status in this inventory | Evidence reviewed | Verification required | Website location |
|---|---|---|---|---|
| Workspace and session behavior | Unverified | No app source, UI implementation, tests, or product docs in workspace | Review relevant implementation, UI wiring, behavior tests and help content | `/features.html`, `/agents.html` |
| AI coding, providers, and models | Unverified | No provider/settings/tool implementation or user documentation supplied | Inspect integrations, settings UI, request paths, error handling and tests | `/features.html`, `/agents.html` |
| Editing, tools, terminal, permissions | Unverified | No editor, tool execution, terminal, permission or safety source supplied | Trace UI actions through implementation; review tests, limits and documentation | `/features.html`, `/docs/` |
| Customization and themes | Unverified | No settings/design system or theme source supplied | Verify user-accessible options and persisted behavior | `/features.html`, `/docs/` |
| Platform support and build prerequisites | Unverified | No project manifest, build instructions, workflow or platform test evidence | Review build setup, CI matrix and documented requirements | `/features.html`, `/download.html` |
| Agent workflow / planning / review / specialists | Unverified | No architecture sources or plans (apart from this website plan's topic list) supplied; this plan is not application evidence | Verify each stage from implementation, UI wiring, behavior and approved plans | `/agents.html` |
| Release availability and installation | Unverified | No release page snapshot, release assets, checksums, or install instructions reviewed | Confirm canonical repository/releases, actual assets, platform and prerequisites | `/download.html` |
| Roadmap items | Unverified | No product roadmap or approved planning documents supplied | Review owner-approved plans; separate Released, In Development, Planned, Exploring; cross-check releases | `/roadmap.html` |
| License and contribution/community options | Unverified | No LICENSE, contribution guide, or GitHub feature state inspected | Verify repository contents and enabled Issues/PRs/Discussions directly | `/community.html` |
| Website privacy and hosting | Partially observed; host unverified | Authored static files contain HTML/CSS and local artwork; no form or authored analytics/cookie JavaScript present. Production host and request handling unknown. | Inspect deployed host, DNS/CDN, logs, third-party resources and applicable policy needs | `/privacy.html` |

## Status meanings

- **Available** — verified in shipped, user-reachable implementation, with supporting behavior/UI and preferably test or documentation evidence.
- **In Development** — evidence shows active implementation, not release availability.
- **Planned** — owner-approved plan; not a shipped capability.
- **Exploring** — explicitly exploratory work; not a commitment or release claim.
- **Unverified** — evidence was not available or insufficient. This is the current evidence status for product capabilities, not a claim about actual implementation.

## Verification criteria

A Pascal class, menu caption, placeholder, plan entry, or isolated routine alone is not sufficient proof. For each capability, record direct file paths and relevant symbols/sections, establish that the UI exposes the behavior, check tests or documented behavior/limitations, and verify whether the functionality exists in an actual release. Link roadmap statuses to dated/approved planning evidence; do not invent dates. Downloads require checking real artifacts and installation requirements, not merely a repository link.

## Unresolved owner inputs

Please provide an authorized **in-workspace** source snapshot for review, ideally including `README.md`, `future-plan/`, relevant `.plan/` and help files, key Pascal/LFM units, tool/provider/settings/workspace units, package design system, tests, GitHub workflows, release artifacts, license, and contribution guidance. Also confirm which files may be published, canonical release/repository URLs, product-owner contact for privacy, and any approved product description. No external application paths were scanned.
