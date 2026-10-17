# Website content plan — canonical publishable facts

## Evidence boundary and maturity

The website team reviewed the designated application repository, including its README, selected implementation units, user help, CI workflow and future-plan documents. See [`PRODUCT_FEATURE_INVENTORY.md`](PRODUCT_FEATURE_INVENTORY.md) for claim-by-claim repository-relative citations.

Use **Implemented in reviewed source/docs** only to mean the source/help describe and wire the behavior. It does not mean released, tested in a live run, or available to download. The application README currently says: “Multi-window workspace layout implemented. AI/model execution is in active integration.” That status has not been owner-confirmed as current. Do not call the product release-ready, fully integrated or generally available until the owner confirms maturity and an actual build/runtime/release has been checked.

No live application run, release-page/assets/checksum inspection, external GitHub verification, or current DigitalOcean configuration/deployment check was performed. This website uses conservative product descriptions and retains the remaining gates below.

## Publishable facts and qualified language

- **Product type:** A desktop coding workspace built with Free Pascal, Lazarus and LCL; do not call it a browser or web application. (App `README.md` “Technology Stack”; `lazycodingagent.lpr`; `mainunit.pas`.)
- **Workspace:** Source/help describe navigation, project tree, chat, a single-file editor, Markdown preview, guidelines/utility panels and integrated terminal. Phrase as present in reviewed source/docs. (App `README.md` §§ 3–5; `mainunit.pas`; `uNavigationPanel.pas`; `uMainFileEditor.pas`; `help/workspace-layout.md`.)
- **Modes and permissions:** Ask is read-oriented; Plan can save plans; Agent exposes write/patch/shell tools. By default writes and shell working directories are restricted to the open workspace; per-session opt-in permits modifications outside it. Do not call this an OS-level sandbox or risk-free. (App `help/chat-and-modes.md`; `help/how-the-agent-works.md`; `help/tools-reference.md`; `uAgentTypes.pas`; `uAgentTools.pas`; `uToolWriteFile.pas`; `uToolRunProcess.pas`.)
- **Agent behavior:** One engine per chat session runs the model/tool loop asynchronously. The app records visible actions/tool I/O in its execution detail/log UI; do not present this as private hidden chain-of-thought, a guaranteed replay, or a sanitized export. (App `uAgentEngine.pas`; `uAgentRunThread.pas`; `uChatSessionHub.pas`; `uAgentExecutionLog.pas`; `help/how-the-agent-works.md`; `help/chat-and-modes.md`.)
- **Provider/model and image support:** Only cite examples and constraints directly in app `README.md` and `help/chat-and-modes.md`. Provider availability, price, API behavior, model capability and vision support depend on configuration and third parties. (App `uAgentTypes.pas`; `uLlmClient.pas`; `uChatImageStore.pas`; `frmSettings.pas`.)
- **Terminal:** State the app has an integrated PTY terminal in reviewed docs/source, with Windows 10 1809+ ConPTY and Linux PTY/libutil caveats. Do not promise universal runtime support. (App `README.md` “Integrated terminal”; `uTerminalPanel.pas`; `help/workspace-layout.md`.)
- **Customization:** Dark/light theme, project rules under `.rules/*.md`, debugging and Learn options are documented. Do not broaden this into plugin/extensibility claims. (App `README.md` “Modern Dark-First Design” and “Debugging mode and project rules”; `help/chat-and-modes.md`.)
- **Build targets:** Repository build configuration includes Linux, Windows and macOS jobs. Label as configured targets; CI configuration alone is not proof of current passing CI or runtime parity. (App `.github/workflows/build.yml`; `README.md` “Building & Running”.)
- **Planned:** Multi-Agent Workspace, Execution Plans, Workspace Knowledge Base/RAG and The Brain are explicitly roadmap placeholders with no backend. Embedded SQLite/vector retrieval is a future plan, not implemented. No delivery dates or commitments. (App `help/workspace-layout.md` “Future Features”; `future-plan/Lazarus_AI_Agent_Future_Plan.md`; `future-plan/Lazarus_Embedded_Storage_and_Vector_Plan.md`.)
- **Unverified:** Releases/assets, installation prerequisites as distributable package, current GitHub availability/license/community features, owner-approved current maturity, production hosting/privacy behavior and deployment settings. Do not invent answers.

## Page-by-page content rules

| Page | Publishable content | Qualification / source |
|---|---|---|
| `/` | Restrained desktop-app description; highlights for workspace/editor, mode-gated tools and execution detail. | Nearby maturity and release caveat. “Plan. Build. Review. Learn.” is positioning only, not proof of multi-agent workflow. Citations: inventory; app README; app help and units above. |
| `/features.html` | Workspace/editor/panels, Ask/Plan/Agent boundaries, sessions and recorded execution detail, documented model/image scope, terminal caveats, documented themes/rules. | Each section links to the local website documentation index; maintainer citations remain in inventory. Explicitly label RAG/Brain/multi-agent/plans as planned. |
| `/agents.html` | Actual single-agent ReAct/tool loop and per-session background engine; explain application-recorded context/tool I/O. | Cite app `uAgentEngine.pas`, `uAgentRunThread.pas`, `uChatSessionHub.pas`, `uAgentExecutionLog.pas`, `help/how-the-agent-works.md`. No operational multi-agent diagram. |
| `/download.html` | Release pending. A concise developer-build note may refer to README build guidance. | No release URL/assets/version/checksum or promise. Clearly distinguish CI/build configuration from a published application. |
| `/roadmap.html` | Multi-agent, execution-plan tracker, workspace knowledge/RAG, Brain, and SQLite/vector retrieval as planned/future planning. | Cite app `help/workspace-layout.md` and future-plan files. No dates, commitments, or current-feature ambiguity. |
| `/docs/` | Accessible topic index for getting started, workspace, chat/modes, agent loop, tools and project rules. | These original help files are in a separate codebase and have not been copied. Provide source availability instructions/link only if destination confirmed; do not link to missing local guide pages or reproduce wholesale without publication approval. |
| `/community.html` | Owner-provided repository URL, clearly noting external availability is unchecked. | No license, open-source, Issues/PRs/Discussions or contribution assertions without direct verification. |
| `/privacy.html` | Observed authored-source behavior and limits. | No guarantees about host, logs, cookies, network intermediaries or contact. Recheck after scripts, embeds, analytics, or hosting changes. |
| `/download.html`, `/404.html`, `/blog/` | Keep release-pending, truthful recovery links and empty blog. | Do not invent posts, dates, assets or deployment 404 behavior. |

## Editorial and technical requirements

- Keep static, framework-free HTML/CSS, no runtime/build dependency, native `<details>` mobile navigation, skip links, landmarks, semantic headings, visible focus and reduced-motion handling.
- Preserve document-relative internal URLs and root-domain canonical URLs. Update sitemap only for URL changes; do not include the 404 page as a sitemap destination. Leave the blog empty until approved posts exist.
- No fabricated screenshots. Use local owl artwork only where appropriate and publication rights are confirmed.
- Keep direct citations for all material claims in `PRODUCT_FEATURE_INVENTORY.md`; source documents support descriptions but do not replace release verification.
- Keep `DEPLOYMENT.md` conditional. Website repository/branch, source/output directory, canonical domain, HTTPS, redirects and 404 behavior must be confirmed in current DigitalOcean UI/configuration.

## Owner confirmations and launch blockers

1. Is README's “AI/model execution is in active integration” status current? What precise maturity wording is approved?
2. Which canonical release page/assets/prerequisites are intended, and have they been tested?
3. What license, contribution instructions and GitHub community channels are actually present/enabled?
4. May concise descriptions or derived documentation/artwork be republished on this site? May original help be linked or summarized?
5. Who is the privacy contact, and what do production host/CDN/logging settings do?
6. Which DigitalOcean repository/branch, source/output directory, canonical host, HTTPS/redirect and 404 settings are configured?

No application source was changed for this site work. Do not treat the website copy or repository build matrix as proof of product release, current successful build, external availability, or deployment state.
