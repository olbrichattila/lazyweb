# Website content plan — canonical publishable facts

## Evidence boundary and maturity

The website team reviewed the designated application repository, including its README, selected implementation units, user help, CI workflow and future-plan documents. See [`PRODUCT_FEATURE_INVENTORY.md`](PRODUCT_FEATURE_INVENTORY.md) for claim-by-claim repository-relative citations.

Use **Implemented in reviewed source/docs** only to mean the source/help describe and wire the behavior. It does not mean released, tested in a live run, or available to download. The application README currently says: “Multi-window workspace layout implemented. AI/model execution is in active integration.” That status has not been owner-confirmed as current. Do not call the product release-ready, fully integrated or generally available until the owner confirms maturity and an actual build/runtime/release has been checked.

No live application run, external GitHub community verification, installation/runtime test, or current DigitalOcean configuration/deployment check was performed. On 2026-11-24, the canonical latest-release API `https://api.github.com/repos/attilaolbrich/lazycodingagent/releases/latest` identified published, non-draft/non-prerelease release v0.1.2 (`published_at: 2026-11-24T21:20:02Z`). The tag API is `https://api.github.com/repos/attilaolbrich/lazycodingagent/releases/tags/v0.1.2`; release page: `https://github.com/attilaolbrich/lazycodingagent/releases/tag/v0.1.2`; full changelog comparison: `https://github.com/attilaolbrich/lazycodingagent/compare/v0.1.1...v0.1.2`. Six uploaded asset names and GitHub-published SHA-256 digests are recorded in `README.md` and `download.html`; assets were not downloaded and independently hashed. This dated v0.1.2 API snapshot is the checked-in fallback, not a guarantee it remains latest. The latest-release API still provides optional browser-time refresh, but live browser/API behavior has not been tested. This website uses conservative product descriptions and retains the remaining gates below.

## Publishable facts and qualified language

- **Product type:** A desktop coding workspace built with Free Pascal, Lazarus and LCL; do not call it a browser or web application. (App `README.md` “Technology Stack”; `lazycodingagent.lpr`; `mainunit.pas`.)
- **Workspace:** Source/help describe navigation, project tree, chat, a single-file editor, Markdown preview, guidelines/utility panels and integrated terminal. Phrase as present in reviewed source/docs. (App `README.md` §§ 3–5; `mainunit.pas`; `uNavigationPanel.pas`; `uMainFileEditor.pas`; `help/workspace-layout.md`.)
- **Modes and permissions:** Ask is read-oriented; Plan can save plans; Agent exposes write/patch/shell tools. By default writes and shell working directories are restricted to the open workspace; per-session opt-in permits modifications outside it. Do not call this an OS-level sandbox or risk-free. (App `help/chat-and-modes.md`; `help/how-the-agent-works.md`; `help/tools-reference.md`; `uAgentTypes.pas`; `uAgentTools.pas`; `uToolWriteFile.pas`; `uToolRunProcess.pas`.)
- **Agent behavior:** One engine per chat session runs the model/tool loop asynchronously. The app records visible actions/tool I/O in its execution detail/log UI; do not present this as private hidden chain-of-thought, a guaranteed replay, or a sanitized export. (App `uAgentEngine.pas`; `uAgentRunThread.pas`; `uChatSessionHub.pas`; `uAgentExecutionLog.pas`; `help/how-the-agent-works.md`; `help/chat-and-modes.md`.)
- **Provider/model and image support:** Only cite examples and constraints directly in app `README.md` and `help/chat-and-modes.md`. Provider availability, price, API behavior, model capability and vision support depend on configuration and third parties. (App `uAgentTypes.pas`; `uLlmClient.pas`; `uChatImageStore.pas`; `frmSettings.pas`.)
- **Terminal:** State the app has an integrated PTY terminal in reviewed docs/source, with Windows 10 1809+ ConPTY and Linux PTY/libutil caveats. Do not promise universal runtime support. (App `README.md` “Integrated terminal”; `uTerminalPanel.pas`; `help/workspace-layout.md`.)
- **Customization:** Dark/light theme, project rules under `.rules/*.md`, debugging and Learn options are documented. Do not broaden this into plugin/extensibility claims. (App `README.md` “Modern Dark-First Design” and “Debugging mode and project rules”; `help/chat-and-modes.md`.)
- **Build targets:** Repository build configuration includes Linux, Windows and macOS jobs. Label as configured targets; CI configuration alone is not proof of current passing CI or runtime parity. (App `.github/workflows/build.yml`; app `README.md` “Building & Running”.)
- **Planned:** Multi-Agent Workspace, Execution Plans, Workspace Knowledge Base/RAG and The Brain are explicitly roadmap placeholders with no backend. Embedded SQLite/vector retrieval is a future plan, not implemented. No delivery dates or commitments. (App `help/workspace-layout.md` “Future Features”; `future-plan/Lazarus_AI_Agent_Future_Plan.md`; `future-plan/Lazarus_Embedded_Storage_and_Vector_Plan.md`.)
- **Downloads:** `download.html` has a checked-in v0.1.2 fallback covering Windows 64-bit installer, Linux amd64 `.deb`, x86_64 AppImage, arm64 `.deb`, and macOS Intel and Apple Silicon `.dmg`. The canonical latest-release API `https://api.github.com/repos/attilaolbrich/lazycodingagent/releases/latest` was checked on 2026-11-24 and identified published, non-draft/non-prerelease tag v0.1.2 (`published_at: 2026-11-24T21:20:02Z`). Tag API: `https://api.github.com/repos/attilaolbrich/lazycodingagent/releases/tags/v0.1.2`; release page: `https://github.com/attilaolbrich/lazycodingagent/releases/tag/v0.1.2`; full changelog comparison: `https://github.com/attilaolbrich/lazycodingagent/compare/v0.1.1...v0.1.2`. Six uploaded asset filenames, direct URLs, and GitHub-published SHA-256 digests are recorded in `README.md` and `download.html`; no independent download/hash was performed. This is dated fallback evidence, not assurance of the latest version now. The latest-release API still handles optional browser-time refresh, but browser/API, installation/runtime, and deployment remain unverified. Link build-from-source to the app README separately. Retain README active-integration maturity caveat.

### v0.1.2 GitHub-published asset digests

The 2026-11-24 release metadata snapshot lists the following SHA-256 values. These are GitHub-published metadata; no file was downloaded or independently hashed. Direct asset URLs use `https://github.com/attilaolbrich/lazycodingagent/releases/download/v0.1.2/<filename>`.

| Platform artifact | Filename | GitHub-published SHA-256 |
|---|---|---|
| Windows installer | `LazyCodingAgent-0.1.2-win64-Setup.exe` | `496b8a9ef5b42a2dc9acf435bf530c23382b41a6c2b71d6a4a0ca1b343d5414e` |
| Linux amd64 Debian | `LazyCodingAgent-0.1.2-amd64.deb` | `f77b14bfe7e7ae79b4cb730d775969552505226f8811616716f746452f6e2487` |
| Linux arm64 Debian | `LazyCodingAgent-0.1.2-arm64.deb` | `cffbb4e9ffe1cbca981cfaafdd378d3da2193c60f95df1125b4c114d7f69008e` |
| Linux x86_64 AppImage | `LazyCodingAgent-0.1.2-x86_64.AppImage` | `4210813a113cbc0b966e67a2a2a6c35039242e79be65ddf8efbdd9b9c37608c6` |
| macOS Intel disk image | `LazyCodingAgent-0.1.2-x86_64.dmg` | `9d680fd23dd4e80d1e918dc9ab54df6c4e273960a3acc54c0327044240cdf1b6` |
| macOS Apple Silicon disk image | `LazyCodingAgent-0.1.2-aarch64.dmg` | `30602f2f1818f52d9d33d762b3ad256ab305068c452880f3849c0ef791e91e49` |

- **Unverified:** Per-user install/runtime testing on every platform, current GitHub license/community features, owner-approved current maturity wording, production hosting/privacy behavior and deployment settings. Do not invent answers.

## Page-by-page content rules

| Page | Publishable content | Qualification / source |
|---|---|---|
| `/` | Restrained desktop-app description; highlights for workspace/editor, mode-gated tools and execution detail. | Nearby maturity and release caveat. “Plan. Build. Review. Learn.” is positioning only, not proof of multi-agent workflow. Citations: inventory; app README; app help and units above. |
| `/features.html` | Workspace/editor/panels, Ask/Plan/Agent boundaries, sessions and recorded execution detail, documented model/image scope, terminal caveats, documented themes/rules. | Each section links to the local website documentation index; maintainer citations remain in inventory. Explicitly label RAG/Brain/multi-agent/plans as planned. |
| `/agents.html` | Actual single-agent ReAct/tool loop and per-session background engine; explain application-recorded context/tool I/O. | Cite app `uAgentEngine.pas`, `uAgentRunThread.pas`, `uChatSessionHub.pas`, `uAgentExecutionLog.pas`, `help/how-the-agent-works.md`. No operational multi-agent diagram. |
| `/download.html` | Platform cards with checked-in v0.1.2 fallback direct links, primary “All releases on GitHub” CTA, install notes, fallback SHA-256 list, build-from-source pointer, maturity notice. Browser refresh may update known release data; missing assets must not appear active without explanation. | The 2026-11-24 GitHub latest-release API snapshot confirmed v0.1.2 and six uploaded asset names/URLs/published digests; evidence is in `README.md` and the page. The changelog comparison is `v0.1.1...v0.1.2`. Recheck before future edits. Test live/deployed API behavior before claiming it. Do not claim full product maturity while README says active integration. |
| `/roadmap.html` | Multi-agent, execution-plan tracker, workspace knowledge/RAG, Brain, and SQLite/vector retrieval as planned/future planning. | Cite app `help/workspace-layout.md` and future-plan files. No dates, commitments, or current-feature ambiguity. |
| `/docs/` | Hub at `docs/index.html` with category cards and anchor sections (`#workspace`, `#modes`, `#chat`, `#rules`, `#agent-loop`) for inbound links from features/agents pages. Six static topic guides (`getting-started`, `workspace-layout`, `chat-and-modes`, `project-rules`, `how-the-agent-works`, `tools-reference`) derived from reviewed application `help/` with maturity qualifiers (active integration, application-level sandbox, execution detail limits). Maintainer evidence remains in `PRODUCT_FEATURE_INVENTORY.md`. |
| `/community.html` | Canonical repository URL `https://github.com/attilaolbrich/lazycodingagent`. | No license, open-source, Issues/PRs/Discussions or contribution assertions without direct verification. |
| `/privacy.html` | Observed authored-source behavior and limits, including the optional GitHub latest-release API request on the download page and fallback behavior. | No guarantees about host, GitHub data handling, logs, cookies, network intermediaries or contact. Recheck after scripts, embeds, analytics, or hosting changes. |
| `/404.html`, `/blog/` | Truthful recovery links and empty blog. | Do not invent posts, dates, assets or deployment 404 behavior. |

## Editorial and technical requirements

- Keep static, framework-free HTML/CSS with no build step or package dependency. The download page alone uses a small optional script; checked-in links work without JavaScript. Keep native `<details>` mobile navigation, skip links, landmarks, semantic headings, visible focus and reduced-motion handling.
- Preserve document-relative internal URLs and root-domain canonical URLs. Update sitemap only for URL changes; do not include the 404 page as a sitemap destination. Leave the blog empty until approved posts exist.
- No fabricated screenshots. Use local owl artwork only where appropriate and publication rights are confirmed.
- Keep direct citations for all material claims in `PRODUCT_FEATURE_INVENTORY.md`; source documents support descriptions but do not replace release verification.
- Keep `DEPLOYMENT.md` conditional. Website repository/branch, source/output directory, canonical domain, HTTPS, redirects and 404 behavior must be confirmed in current DigitalOcean UI/configuration.

## Owner confirmations and launch blockers

1. Is README's “AI/model execution is in active integration” status current? What precise maturity wording is approved?
2. Recheck the current GitHub latest release, artifact names/download URLs and SHA-256 digest values before future fallback changes, then test deployed page/API behavior. The v0.1.2 fallback is a dated GitHub API snapshot from 2026-11-24, not proof it remains latest or that browser refresh, installation/runtime, or deployment work.
3. What license, contribution instructions and GitHub community channels are actually present/enabled?
4. May concise descriptions or derived documentation/artwork be republished on this site? May original help be linked or summarized?
5. Who is the privacy contact, and what do production host/CDN/logging settings do?
6. Which DigitalOcean repository/branch, source/output directory, canonical host, HTTPS/redirect and 404 settings are configured?

No application source was changed for this site work. Do not treat the website copy or repository build matrix as proof of product release, current successful build, external availability, or deployment state. Keep gates open until dated evidence with scope is actually recorded.
