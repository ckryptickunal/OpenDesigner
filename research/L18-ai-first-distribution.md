# L18: AI-first distribution (how an open-source design resource runs inside Claude, ChatGPT, Codex and other agents)

Lane L18, written 2026-09-23. Sources are in `traces/L18-trace.md` (S-L18-001 to 060 lane author; 100-142 helper H1, OpenAI; 200-265 helper H2, other hosts and standards; 300-351 helper H3, interview design and harmony). Every claim carries a source id or [inferred]. Related lanes, linked rather than repeated: L11 DC-L11-23/24 (agent-readable distribution, DESIGN.md, Storybook/shadcn/zeroheight MCPs, guardrails), L16 Parts A-B (Figma and Paper MCP tool lists, seats, limits), L17 (gstack, impeccable, frontend-design skill, reference intake).

## Lane overview

**Question.** OpenDesigner is a repo people load into their own AI. How can it be packaged for each host as of September 2026, what can each host render visually, and what layout works everywhere?

**Answer in seven points.**
1. **One skill format now runs almost everywhere.** The Agent Skills format (a folder with `SKILL.md`, name + description frontmatter, optional `scripts/ references/ assets/`) is loaded by Claude (app, Code, API), ChatGPT and Codex, Cursor, VS Code and every Copilot surface, Gemini CLI and about 40 other clients [S-L18-001, S-L18-050, S-L18-203, S-L18-106]. The skill is the core deliverable.
2. **Paths differ, so ship copies.** `.agents/skills/` is the cross-tool project path (Codex, Cursor, Copilot, Gemini CLI, Zed and more), but Claude Code reads only `.claude/skills/`, and Kiro only `.kiro/skills/` [S-L18-251, S-L18-106, S-L18-003, S-L18-212, S-L18-234]. Symlinks break on Windows and in zips [S-L18-211, S-L18-258].
3. **Two plugin formats wrap the skill.** Claude uses `.claude-plugin/plugin.json` plus marketplaces (Claude Code, Cowork, and plugin skills in Chat) [S-L18-004, S-L18-006, S-L18-045]. OpenAI, Cursor, VS Code, Copilot and Kiro use the vendor-neutral Agent Plugins 1.0 (`plugin.json` at the root, `skills/`, `mcp.json`, 6 Aug 2026) [S-L18-058, S-L18-059, S-L18-102]. Both put skills in `skills/`, so one folder serves both manifests [inferred].
4. **Custom GPTs are a dead end.** They retire on 11 Dec 2026 and migrate into plugins, with instructions becoming a skill [S-L18-118, S-L18-060]. ChatGPT Projects remain the no-install fallback [S-L18-126].
5. **Visual interviews have one portable standard: MCP Apps.** The extension (`io.modelcontextprotocol/ui`, stable spec 2026-01-26) renders server-supplied HTML in a sandboxed iframe inside Claude (web, desktop, mobile), ChatGPT, VS Code Copilot, Cursor, Microsoft 365 Copilot, Goose and others, and the widget can send the user's pick back as a message or tool call [S-L18-010, S-L18-011, S-L18-024, S-L18-055]. Terminal agents (Claude Code CLI, Codex CLI, Gemini CLI, Copilot CLI) do not render it [S-L18-044, S-L18-217].
6. **Without a server, Claude and Codex still have visual paths.** Claude's inline custom visuals send a follow-up prompt when clicked (web and desktop chat) [S-L18-041]; Claude artifacts and Claude Code artifacts render full HTML with a "copy as prompt" or comment-back loop [S-L18-027, S-L18-043]; the Codex desktop app's built-in browser renders local HTML and takes element comments [S-L18-115]. ChatGPT's code-block preview renders HTML/React but has no documented channel back to the model [S-L18-128].
7. **Harmony lives in files, not in the chat.** The evidence favors a closed, structured token source (DTCG 2025.10), retrievable examples, deterministic lint, and one short always-loaded context file that points to the rest [S-L18-324, S-L18-332, S-L18-323, S-L18-329]. Anthropic's own Claude Design works the same way: it builds the system from real code and files, then checks every output against it [S-L18-029, S-L18-032].

**Recommended architecture in one line:** a skills-first repo (one `skills/` source of truth, generated copies for `.agents/skills` and `.claude/skills`, AGENTS.md as the canonical entry file, two plugin manifests, chunked JSON knowledge, static visual templates), plus an optional stateless remote MCP server with MCP Apps widgets as phase 2 (Part I).

---

## Part A. Host capability matrix (verified 2026-09-23)

Y = verified, N = verified absent or not supported, ? = unverified. "Claude app" = claude.ai web, Claude Desktop chat and mobile (Cowork merged into it on 16 Sep 2026 [S-L18-038]).

| Capability | Claude app | Claude Code (CLI / desktop Code tab) | Claude API | ChatGPT web + mobile | ChatGPT desktop (Work + Codex) | Codex CLI / IDE | Cursor | VS Code + Copilot | Gemini CLI |
|---|---|---|---|---|---|---|---|---|---|
| **Loads SKILL.md** | Y: zip upload (Customize > Skills, all plans, code execution on), org-provisioned skills (Team/Ent), skills inside plugins [S-L18-002, S-L18-006, S-L18-045] | Y: `.claude/skills/`, `~/.claude/skills/`, plugins, synced from claude.ai; **not** `.agents/skills` [S-L18-003, S-L18-212] | Y: `/v1/skills` upload, runs in code-execution container, no network [S-L18-001] | Only inside a plugin (directory, workspace share, admin-imported GitHub marketplace) [S-L18-104, S-L18-106] | Y: standalone skills and plugins, `@skill` [S-L18-106] | Y: `.agents/skills` up to repo root, `~/.agents/skills`, `$skill` [S-L18-106] | Y: `.agents/skills`, `.cursor/skills` [S-L18-204] | Y: `.agents/skills`, `.github/skills`, `.claude/skills` [S-L18-205] | Y: `.agents/skills`, `.gemini/skills` [S-L18-207] |
| **Reads AGENTS.md** | N (not a repo host); Projects with a connected repo run Claude Code threads [S-L18-039, inferred] | Y only when no CLAUDE.md exists (v2.1.277+); otherwise via `@AGENTS.md` import in CLAUDE.md [S-L18-036, S-L18-211] | N [inferred] | N (not documented) [S-L18-112, inferred] | Y [S-L18-112] | Y: root-to-leaf concatenation, `AGENTS.override.md`, 32 KiB cap [S-L18-112] | Y: root and nested [S-L18-214] | Y (nested is experimental) [S-L18-210, S-L18-257] | N by default; `context.fileName` or a GEMINI.md with `@AGENTS.md` [S-L18-213] |
| **MCP local (stdio)** | Desktop only: `claude_desktop_config.json`, MCPB desktop extensions [S-L18-015, S-L18-049] | Y [S-L18-037] | N (remote only) [S-L18-048] | N; Secure MCP Tunnel in developer mode [S-L18-120] | Y (`config.toml`) [S-L18-113] | Y [S-L18-113] | Y [S-L18-221] | Y [S-L18-215] | Y [S-L18-224] |
| **MCP remote** | Y: custom connectors on Free/Pro/Max, owner-added on Team/Ent; OAuth (CIMD, DCR, own client), no-auth, request headers (beta) [S-L18-018] | Y: HTTP + OAuth, prompts as slash commands, resources via @, elicitation [S-L18-037] | Y, beta, tools only [S-L18-048] | Y via developer mode (docs: Plus, Pro, Business, Ent, Edu; help center: Business/Ent/Edu beta) or a published plugin [S-L18-119, S-L18-124] | Y [S-L18-113] | Y: streamable HTTP, `codex mcp login` [S-L18-113] | Y + OAuth, prompts, resources, elicitation [S-L18-221] | Y + OAuth, prompts, resources, sampling, elicitation [S-L18-256, S-L18-262] | Y + OAuth/DCR [S-L18-224] |
| **Interactive UI in chat** | Y: MCP Apps on web, desktop, mobile [S-L18-013]; custom visuals (web + desktop; click sends a follow-up) [S-L18-041]; artifacts with storage and connectors [S-L18-027]; Claude Design canvas [S-L18-029] | CLI: N for MCP Apps (falls back to text) [S-L18-044]; AskUserQuestion options [S-L18-304]; publishes claude.ai artifacts [S-L18-043]. Desktop Code tab: Y, MCP App widgets since 2026-09-02 [S-L18-045] | N (the integrator renders) [inferred] | Y: MCP Apps widgets ("fully compatible" 2026-02-22) with follow-up messages and tool calls; code-block previews of HTML/React/SVG with no channel back [S-L18-055, S-L18-121, S-L18-128] | Y: MCP App panels; built-in browser renders localhost and local HTML, users comment on elements [S-L18-109, S-L18-115] | N (image input only) [S-L18-137, S-L18-138] | Y: MCP Apps since 2.6 (2026-03-03) [S-L18-222, S-L18-062] | Y: MCP Apps since 1.109 (2026-02-04) [S-L18-220, S-L18-061] | N [S-L18-217] |
| **File / repo access** | Uploads, project library, connected GitHub repos in Projects (17 Sep 2026), code-execution sandbox [S-L18-039, S-L18-002] | Full local repo [S-L18-043] | Container files [S-L18-001] | Uploads, Project files (Free 5, Plus/Go 25, Pro 40), connected apps [S-L18-126] | Local folders [S-L18-113, inferred] | Local repo; cloud via GitHub/GitLab [S-L18-112, S-L18-139] | Local repo [inferred] | Local repo [inferred] | Local repo [inferred] |
| **Plugin / bundle format** | Claude plugins (skills + connectors; sub-agents greyed out in Chat) [S-L18-006] | `.claude-plugin/plugin.json`, marketplaces from GitHub, git, npm, zip [S-L18-004] | n/a | Agent Plugins (`plugin.json`, legacy `.codex-plugin/`) [S-L18-102] | Same [S-L18-102] | Same (IDE support conflicting) [S-L18-107, S-L18-109] | Agent Plugins [S-L18-058] | Agent Plugins [S-L18-058] | ? (Google reported joining Agent Plugins; snippet only) [S-L18-056] |
| **Writes to Figma** | Listed read + write in Figma's catalog; interactive Figma connector (FigJam diagrams) [S-L18-047, S-L18-013] | Y (remote server, Full seat) [L16 A1, S-L18-046] | ? | Catalog lists ChatGPT read + write, but Figma's write-to-canvas list omits it: conflicting [S-L18-244, S-L18-136] | Y via Codex [S-L18-135, S-L18-136] | Y [S-L18-136] | Y [S-L18-244] | Y [S-L18-244] | N (not listed) [S-L18-244] |
| **Writes to Paper** | Desktop only, through a local MCP entry (Paper's server runs in Paper Desktop at 127.0.0.1:29979) [L16 B2-B3, inferred] | Y (documented path) [L16 B3] | N [inferred] | N (local only) [inferred] | ? (localhost HTTP in config.toml should work) [inferred] | ? same [inferred] | ? [inferred] | ? [inferred] | ? [inferred] |

**Reading the matrix.**
- Only the MCP Apps row gives one visual implementation that works in both Claude and ChatGPT. Anthropic documents a single-codebase path (`registerAppTool`, `App.connect()` auto-detects the host) [S-L18-016].
- The terminal agents are where most engineers work, and none of them renders UI in chat. Their visual path is a file the agent writes and the user opens (a local HTML page, a published Claude artifact, Paper or Figma) [inferred from the UI row].
- Other hosts checked by H2: Copilot CLI (skills Y, AGENTS.md Y, MCP Y, no MCP Apps), Devin Desktop/ex-Windsurf (skills Y, no MCP Apps), Zed (reads only `.agents/skills`, MCP tools and prompts only), Goose (skills Y, MCP Apps Y), Kiro (`.kiro/skills` only, Figma write Y), Gemini consumer app (Gems + Canvas HTML/React preview, only fixed partner MCP connectors, no skills) [S-L18-243, S-L18-209, S-L18-230, S-L18-226, S-L18-235, S-L18-234, S-L18-254, S-L18-255, S-L18-260].

---

## Part B. Packaging formats (facts)

### B1. Agent Skills: the format and where Claude runs it
- **Format.** Required `name` (1-64 chars, lowercase letters, digits, hyphens, must match the folder; Claude also forbids "anthropic" and "claude") and `description` (1-1024 chars, what it does and when to use it). Optional `license`, `compatibility` (<=500 chars), `metadata`, `allowed-tools` (experimental) [S-L18-050, S-L18-001].
- **Budget.** Metadata costs about 100 tokens per skill at startup; the body loads on activation and should stay under 5k tokens and 500 lines; reference files load only when read, one level deep; scripts run and only their output enters context [S-L18-050, S-L18-001].
- **Claude surfaces do not sync.** A claude.ai upload, an API upload and a Claude Code folder are three separate installs [S-L18-001]. claude.ai skills need code execution; network access there varies by admin setting, the API has none, Claude Code has full network [S-L18-001, S-L18-002]. Claude Code syncs a signed-in user's claude.ai skills into `~/.claude/skills/synced/`, but shell injection and `${CLAUDE_*}` variables do not run in synced skills [S-L18-003].
- **Portable fields only.** Claude Code lists `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` as portable; fields like `context: fork`, `paths`, `arguments`, `model`, `hooks` are Claude Code-only and fail validation on claude.ai upload [S-L18-003].
- **Conflict noted.** The platform docs say claude.ai custom skills are per-user with no org distribution [S-L18-001]; the Help Center (updated 2026-09-23) and the Dec 2025 launch post say Team/Enterprise owners can provision skills for everyone [S-L18-002, S-L18-052]. The newer Help Center wins.
- **Standard.** Anthropic published Agent Skills as an open standard on 18 Dec 2025 [S-L18-052]. agentskills.io lists 46 clients, including ChatGPT and Codex [S-L18-203]. It is Apache-2.0 code and CC-BY-4.0 docs with no foundation governance [S-L18-248]. Skills over MCP (below) reuses the same format [S-L18-025].

### B2. Where skill folders live (why copies are needed)
The spec does not fix a location. The client-implementation guide calls `.agents/skills/` (project) and `~/.agents/skills/` (user) "a widely-adopted convention" [S-L18-251]. H2's per-tool check [S-L18-204 to S-L18-243]:
- **Read `.agents/skills`:** Codex, ChatGPT desktop, Cursor, VS Code and all Copilot surfaces, Gemini CLI (wins over `.gemini/skills`), Antigravity, Devin Desktop, Amp, Goose, OpenCode, Factory, Roo, Junie, Mistral Vibe, Zed (Zed reads only this path).
- **Do not:** Claude Code (`.claude/skills` only), Cline (`.cline/skills`, `.clinerules/skills`, `.claude/skills`), Kiro (`.kiro/skills`).
- A real copy in `.claude/skills` covers Claude Code and Cline. Clients that scan both folders may list the skill twice; per-client dedupe behavior is unverified [S-L18-251].

### B3. Instruction files
- **AGENTS.md** is stewarded by the Agentic AI Foundation (Linux Foundation, formed 9 Dec 2025 with MCP and goose) [S-L18-202, S-L18-261]. Nearest file wins [S-L18-202, S-L18-210]. Codex concatenates root to leaf with a 32 KiB default cap [S-L18-112].
- **Claude Code** reads AGENTS.md natively from v2.1.277, but only if no CLAUDE.md exists; it falls back to CLAUDE.md-only on Bedrock, with telemetry off, on older versions and in the first session after an upgrade. Anthropic's recommended bridge is a CLAUDE.md containing `@AGENTS.md`, and it says to prefer that import over a symlink on Windows [S-L18-036, S-L18-211].
- **Gemini CLI** reads GEMINI.md by default; a GEMINI.md with `@AGENTS.md` works because imports are supported [S-L18-213].
- **Cursor** reads AGENTS.md plus `.cursor/rules/*.mdc` (always, intelligent, glob, manual) [S-L18-214]. **Copilot** reads `.github/copilot-instructions.md`, path-scoped `*.instructions.md` (cloud agent and code review only) and AGENTS.md [S-L18-210].
- **Size guidance:** Claude under 200 lines, Cursor under 500 lines, Codex 32 KiB; longer files lower adherence [S-L18-329, S-L18-341, S-L18-112]. OpenAI's Sep 2026 guidance: lean router docs, prune AGENTS.md, over-specified recipes now hurt [S-L18-134].

### B4. Plugins and marketplaces
- **Claude.** A plugin is `.claude-plugin/plugin.json` plus `skills/`, `agents/`, hooks, `.mcp.json`. A repo becomes a marketplace with `.claude-plugin/marketplace.json`; one repo can be both. Users run `/plugin marketplace add owner/repo` then `/plugin install name@marketplace`. Sources can be GitHub, any git URL, a git subdirectory, npm or a zip [S-L18-004]. Anthropic's own `anthropics/skills` repo does exactly this: a root `marketplace.json` whose plugins point at `./skills/*` with `strict: false` [S-L18-034]. The official marketplace is `claude-plugins-official` (submit by PR); a community marketplace also exists [S-L18-004, S-L18-005].
- **Claude app.** Plugins are on all paid plans. Cowork runs everything; Chat runs plugin skills and connectors (sub-agents greyed out); Claude Code v2.1.273+ syncs account plugins [S-L18-006]. The Desktop changelog dates Chat support for org-provided plugin skills to 2026-09-02 [S-L18-045]. The claude.com docs page still says plugins "aren't used in Chat" [S-L18-007]; it is older. Limits: 200 MB per package, 5,000 files, 25 marketplaces per user [S-L18-007].
- **Agent Plugins 1.0** (6 Aug 2026; TSC from Amazon, Cursor, Microsoft, OpenAI, Vercel; not an AAIF project; no Anthropic involvement mentioned). Root `plugin.json` needs only `$schema` and `name`; fixed locations `skills/` and `mcp.json`; `${PLUGIN_ROOT}` and `${PLUGIN_DATA}` path variables; symlinks only inside the root; install mechanism left to clients. Compatible clients: VS Code, Cursor, GitHub Copilot, Codex, Kiro [S-L18-057, S-L18-058, S-L18-059].
- **OpenAI plugins.** The Apps SDK docs are now "Plugins": skills + optional MCP servers + optional ChatGPT UI, in one directory shared by ChatGPT and Codex; `.codex-plugin/plugin.json` still works as a fallback [S-L18-100, S-L18-102, S-L18-103]. Distribution: public submission, workspace sharing, admin import of a GitHub marketplace with daily sync, or a local marketplace in the desktop app. No documented path lets a Plus or Pro web user install an arbitrary GitHub repo [S-L18-102, S-L18-104].

### B5. ChatGPT-specific containers
- **Custom GPTs retire 11 Dec 2026** on all plans; Enterprise creation ends 26 Oct 2026 (planned). "Migrate to plugin" turns instructions into a skill and knowledge into reference files; custom actions do not carry over [S-L18-118, S-L18-060]. Current limit: 20 knowledge files of 512 MB [S-L18-127].
- **Projects** have instructions, files (Free 5, Plus/Go 25, Pro 40), project memory and apps, and can be shared on all plans [S-L18-126]. This is the only zero-install path for Free ChatGPT users [inferred].
- **Skills in ChatGPT** use SKILL.md; standalone skills work in the desktop app, Codex CLI and IDE; on web and mobile they arrive inside plugins [S-L18-106, S-L18-123].

### B6. Skills over MCP
- The official extension `io.modelcontextprotocol/skills` (SEP-2640, Final) lets an MCP server serve Agent Skills: `skills/list`, `skills/get`, and `resources/read` on `skill://` URIs, with a SHA-256 manifest per skill, host approval, and a 512-file / 16 MiB per-skill ceiling [S-L18-025].
- Host support is thin: ChatGPT (partial), fast-agent and MCP Inspector [S-L18-024]. OpenAI supports "a bounded, static subset": skills are snapshotted at plugin submission, not fetched at runtime [S-L18-120, S-L18-123]. Claude is not listed [S-L18-024], and Anthropic's 2026-07-28 post does not mention it [S-L18-028].
- Implication: a server-side skill copy is a nice-to-have for ChatGPT plugin submission, not a primary channel yet [inferred].

---
## Part C. MCP as the universal layer

### C1. Protocol state (Sep 2026)
- **Spec 2026-07-28** (final, published 28 Jul 2026; RC 21 May): stateless transport with no `initialize` handshake and no `Mcp-Session-Id`, so any server instance can answer any request; a first-class extensions framework with reverse-DNS ids; Tasks moved into an extension; elicitation now works by returning `InputRequiredResult` inside an active request; OAuth hardening; `server/discover` [S-L18-022, S-L18-023]. Anthropic is rolling it out across Claude products [S-L18-028]; Cloudflare's hosted servers already accept it [S-L18-054].
- **Official extensions:** MCP Apps (UI), OAuth Client Credentials, Enterprise-Managed Authorization, Skills over MCP [S-L18-024].
- **Elicitation** (2025-11-25 spec): form mode is flat fields, enums and defaults only, no nesting; URL mode sends the user to a page. OpenAI says use it for structured facts the user can reasonably supply and never for secrets [S-L18-301, S-L18-347, S-L18-120]. Claude Code, Cursor and VS Code support it [S-L18-037, S-L18-221, S-L18-262].
- **Claude-specific server rules.** Every tool must declare `readOnlyHint` and `destructiveHint` [S-L18-019]. Claude Code caps a tool result at 25k tokens by default, and a tool can raise its own cap with `_meta["anthropic/maxResultSizeChars"]` up to 500,000 chars [S-L18-037]. ChatGPT treats tools without `readOnlyHint` as writes that need confirmation [S-L18-119].

### C2. What an OpenDesigner MCP server would expose [inferred from C1 and the synthesis files]
| Primitive | Items | Why |
|---|---|---|
| Resources | `od://ontology`, `od://stage/{id}` (one questionnaire stage), `od://card/{DC-id}`, `od://levers`, `od://graph/fanout` | Chunked reads keep each result far below the 25k-token cap; the full `synthesis/QUESTIONNAIRE.md` is 267 KB and `cards.json` 826 KB (measured on disk) |
| Tools (read-only) | `od_next_questions(state)`, `od_explain(decision)`, `od_examples(decision)`, `od_check_coverage(state)` | Pacing and coverage computed from `decision-graph.json`, not from the model's memory |
| Tools (pure generators, no side effects) | `od_generate_palette(seed, options)`, `od_type_scale(base, ratio)`, `od_contrast(pairs)`, `od_export(state, format)` returning DTCG / CSS / Tailwind / DESIGN.md text | Deterministic math beats model arithmetic; returns text the agent writes into the user's repo |
| MCP Apps views | `ui://opendesigner/palette-picker`, `spacing-ruler`, `type-scale`, `radius-shape`, `component-preview`, `options-gallery` | The visual interview (Part D) |
| Prompts | `start-interview`, `extend-system`, `review-system` | Become slash commands in Claude Code, Gemini CLI and Cursor [S-L18-037, S-L18-224, S-L18-221] |
| Skills over MCP | the same `skills/opendesigner` folder | For ChatGPT plugin import (snapshot) [S-L18-120] |

State stays in the user's files (`opendesigner.state.json`, DESIGN.md, tokens), passed in on each call. That fits the stateless 2026-07-28 transport and means the server stores no user data [inferred from S-L18-022].

### C3. Hosting and auth options
- **No-auth public server.** Allowed by Claude custom connectors ("No sign-in") and ChatGPT developer mode ("No Auth") [S-L18-018, S-L18-119]. Suitable because the server holds only public knowledge and pure functions [inferred].
- **OAuth** only if accounts or saved projects are added later: Claude supports CIMD, DCR or a pre-registered client [S-L18-018]; Cloudflare Workers has OAuth templates (GitHub, Google, Auth0, WorkOS) [S-L18-054].
- **Local packaging** for offline or private use: stdio entry in `.mcp.json` / `config.toml` / `claude_desktop_config.json`, or an MCPB bundle for Claude Desktop [S-L18-037, S-L18-113, S-L18-049]. ChatGPT web cannot reach a local server except through Secure MCP Tunnel in developer mode [S-L18-120].
- **Directories.** Claude connectors directory (950+ servers; review criteria apply) [S-L18-028, S-L18-014]; official MCP Registry (preview since 8 Sep 2025, API frozen at v0.1) and GitHub MCP Registry (one-click into VS Code) [S-L18-246, S-L18-247]; OpenAI plugin directory [S-L18-103].
- **Security.** Skills and MCP servers are untrusted input: Anthropic warns that a malicious skill can exfiltrate data [S-L18-001]; the community's top MCP thread (2,269 points) is about a vendor connector injecting instructions [COMMUNITY-SIGNAL S-L00-050]. Keep the server read-only, return data rather than instructions, and ship scripts that need no network [inferred].

---

## Part D. Visual interviews: what each surface can show and how the choice comes back

Legend: Y = can show it; the last column is how the user's pick reaches the model.

| Surface (hosts) | Palette picker | Spacing ruler | Live component preview | Gallery of options | Choice returns via |
|---|---|---|---|---|---|
| **MCP App from an OpenDesigner server** (Claude web/desktop/mobile, ChatGPT web/desktop/mobile, VS Code, Cursor, Goose, M365 Copilot, Claude desktop Code tab, Codex app panels) | Y | Y | Y (real HTML/CSS) | Y (carousel 3-8 items) | `ui/message` (a chat turn), `tools/call`, `ui/update-model-context`; ChatGPT also `sendFollowUpMessage`, `setWidgetState` [S-L18-011, S-L18-121] |
| **Claude custom visuals** (model-written HTML inline; Claude web + desktop chat, all plans; not mobile) | Y | Y | Y | Y | A click sends a follow-up prompt in chat (not in Cowork); visuals are ephemeral, "Save as artifact" keeps one [S-L18-041, S-L18-042] |
| **Claude artifacts** (claude.ai conversations) | Y | Y | Y (HTML, React) | Y | No documented click-to-chat channel; the user reports the pick, or an AI-powered artifact calls Claude inside the page; persistent storage 20 MB [S-L18-027, inferred] |
| **Claude Code artifacts** (published claude.ai page from CLI or desktop) | Y | Y | Y | Y ("lay out several design options side by side") | "Copy as prompt" button pasted back; on Team/Ent, comments sent to Claude reach the session live (v2.1.221+) [S-L18-043] |
| **Claude Design canvas** (`/design`, Artifacts tab, any conversation; paid beta) | Y (Claude-made sliders) | Y (sliders for spacing) | Y | Y | Native: comments, chat and direct edits are all visible to Claude [S-L18-029, S-L18-033]. Closed product: OpenDesigner can hand off to it, not drive it [inferred] |
| **Codex desktop built-in browser** (local HTML the agent writes) | Y | Y | Y | Y | User comments on page elements go to the agent; the agent can also drive the page [S-L18-115] |
| **ChatGPT code-block preview** (canvas successor) | Y | Y | Y | Y | None documented; user types the choice [S-L18-128, inferred] |
| **Host question tools** (Claude AskUserQuestion; Codex `request_user_input`) | Text options (Agent SDK TS can attach HTML/markdown previews) | Text | Text | Up to 4 options per question (Claude) | Structured answer to the tool [S-L18-304, S-L18-109, S-L18-310] |
| **MCP elicitation form** (Claude Code, Cursor, VS Code) | Enum of named swatches only | Number field | N | Enum | Form result to the server [S-L18-301] |
| **Figma via MCP** (`use_figma`, remote, Full seat) | Y (variables + swatch frames) | Y | Y (frames, components) | Y (frames side by side) | User selects a frame; agent reads selection with `get_design_context`/`get_metadata` [L16 A1] |
| **Paper via MCP** (Paper Desktop, local) | Y | Y (on-canvas gap handles) | Y (real HTML/CSS via `write_html`) | Y | Agent reads `get_selection`; comments via `list_comment_threads` [L16 B2] |
| **Local HTML file** (any agent that writes files) | Y | Y | Y | Y | User copies a generated answer string back [inferred] |
| **Plain text** (everywhere) | Hex list + names | Numbered steps | ASCII sketch | Numbered list | Typed reply [S-L18-310, S-L18-322] |

**Constraints that shape the widget designs.**
- Claude inline cards auto-fit height, allow at most 2 actions and 4-5 data points, and forbid dropdowns and popovers (use segmented buttons, toggle chips). Carousels hold 3-8 items. Anything needing its own scroll goes fullscreen, where the composer stays visible [S-L18-017]. ChatGPT's guidelines match: 3-8 carousel items, at most 2 primary actions, fullscreen keeps the composer [S-L18-101, S-L18-122].
- Direct manipulation (sliders, toggles, selections) belongs in the widget; anything needing language goes to chat [S-L18-017]. A palette picker is therefore a widget; "why does this feel cold?" is a chat turn [inferred].
- Views must use host style tokens for structure and support light and dark; Claude publishes its token set (e.g. background `#FFFFFF`/`#30302E`, text `#141413`/`#FAF9F5`, radius 4-12 px, 0.5 px borders) [S-L18-017]. Preview panes showing the *user's* system should be visually fenced so host chrome and user tokens do not mix [inferred].
- `frameDomains` (nested third-party iframes) is restricted in Claude; external origins must be declared in `_meta.ui.csp` [S-L18-017, S-L18-011]. Claude Code artifacts load fonts only from Google Fonts and scripts from five CDNs [S-L18-043].
- MCP Apps explicitly names "configuring with many options" as a use case: a form showing all options with defaults beats a long back-and-forth [S-L18-021]. That matches the questionnaire's "one screen per cycle" rule (`synthesis/QUESTIONNAIRE.md`).

---

## Part E. "The design function of Claude": what Anthropic offers and what makes it good

### E1. The offering (verified)
| Piece | What it is | Evidence |
|---|---|---|
| **Claude Design** (Anthropic Labs) | Launched 17 Apr 2026 on Opus 4.7 as a research preview. Makes designs, prototypes, slides and one-pagers by conversation, inline comments, direct edits and "custom sliders (made by Claude)". Builds a team design system at onboarding from the codebase and design files; web capture; exports (Canva, PDF, PPTX, HTML); handoff bundle to Claude Code | [S-L18-033] |
| June 2026 update | DS import rebuilt (GitHub repo, design files, uploads); Claude "checks its output against your design system, and makes corrections before you see it"; admins lock one standard DS; new direct editor; `/design-sync` and `/design` in Claude Code; 1M+ users in week one (vendor figure) | [S-L18-032] |
| Sep 2026 integration | Claude Design works inside any conversation, Claude Code and the Artifacts tab; each design system becomes an artifact usable in any conversation; beta on Pro/Max/Team/Enterprise (off by default on Enterprise), not Free. Known issues: no version history, unreliable multi-editor, comments can vanish; no Figma export | [S-L18-029, S-L18-030, S-L18-031] |
| DS contents | UI kit of colors, typography, components, spacing/grid, extracted from code, screenshots, design files, PPTX/PDF brand docs, logos; "Published" toggle; "Let Claude clean it up" for migrated tokens; storage format not documented | [S-L18-031] |
| Built-in artifact design skill | When Claude Code builds an artifact it applies a design skill that first looks for the project's design system (CLAUDE.md or a theme file); precedence is prompt > project DS > Claude's own choices | [S-L18-043] |
| Public design skills | `anthropics/skills`: frontend-design (ground the design in the subject, confirm it with the client; plan, review against the brief, build, critique; a calibration list of generic AI looks), theme-factory, web-artifacts-builder, brand-guidelines, canvas-design | [S-L18-034, S-L18-035; L17 S-L17-021] |
| Visual surfaces | Custom visuals, artifacts (storage, connectors), MCP Apps with its own design guidelines and Figma UI kit | [S-L18-041, S-L18-027, S-L18-017] |
| Figma | Interactive Figma connector in Claude (Jan 2026); Figma partner skills in the directory (Dec 2025); Figma plugin for Claude Code (L16) | [S-L18-013, S-L18-052; L16 A2] |

### E2. What makes it good, and the open equivalent for OpenDesigner
1. **Starts from the user's real material, not a blank page.** Code, repos, design files and brand PDFs become the system [S-L18-031]. Open equivalent: an `extract` step that reads the user's repo, CSS variables, Figma variables (Figma MCP) or a reference URL before asking anything, matching H3's rule "look before you ask" [S-L18-310; L17 reference intake].
2. **Checks its own output against the system before showing it** [S-L18-032]. Open equivalent: deterministic validators (contrast, token references, spacing on-scale) run by a script after every generation step [S-L18-323, S-L18-332].
3. **Edit modes matched to the size of the change:** comments for a component, chat for structure, direct edits and generated sliders for visual tuning [S-L18-029, S-L18-033]. Open equivalent: the Part D ladder, with sliders in MCP Apps or artifacts, and chat for rationale.
4. **The system persists and is reusable everywhere** (an artifact in every conversation; admin lock) [S-L18-029, S-L18-032]. Open equivalent: DESIGN.md + DTCG tokens + a decision log in the user's repo, readable by any model; "locked" decisions flagged in state [inferred].
5. **Hands off to code** (bundle to Claude Code, `/design-sync`) [S-L18-032]. Open equivalent: exports to DTCG, CSS variables, Tailwind, Figma variables and a components spec (L07, L16).
6. **Taste guardrails** against generic AI looks [S-L18-035]. Open equivalent: ship a calibration list and "spend boldness in one place" rule (L17).

**Where an open resource can beat it** [inferred from E1]: it is closed, paid-only and Claude-only; its storage format is undocumented; it has no Figma export or version history; and nothing public says it teaches *why* a decision matters or spends more time on high fan-out decisions. OpenDesigner's differentiators are portability across models, an inspectable file format, the teaching layer, and fan-out-weighted pacing.

---
## Part F. Interview design for LLM-led elicitation (rules the skill should encode)

H3's synthesis, condensed. Rules marked [inferred] are this lane's reading, not a source's words.
1. **Look before you ask.** Read the repo, CSS, brand assets and any reference first; never ask what files can answer; if several candidates exist, list them and recommend one. OpenAI's Codex plan-mode prompt is the clearest statement: explore facts, ask only about taste and trade-offs [S-L18-310, S-L18-322, S-L18-302].
2. **Every question must change the system, lock an assumption, or pick a trade-off.** Clarifying questions cost the user effort, so ask for high-impact ambiguity and assume, with a label, for low-impact [S-L18-310, S-L18-307, S-L18-313].
3. **Offer 2-4 real options, mark one recommended with a one-line reason, always allow free text.** In a 2026 preprint, novices answering LLM-generated multiple-choice questions surfaced 47% more key design decisions in 73% less time [S-L18-310, S-L18-321, S-L18-304, S-L18-335]. State reasons as "X because Y"; Anthropic reports that explaining why improves instruction following [S-L18-309].
4. **One high-impact decision per turn; group up to 3 small related ones.** gstack asks one at a time, impeccable caps rounds at 3, AskUserQuestion allows 4 per call, GOV.UK defaults to one thing per page [S-L18-321, S-L18-322, S-L18-304, S-L18-319]; the split is [inferred].
5. **Order by downstream reach.** Product truth first (audience, the design's job, constraints), then one visual thesis or "memorable thing", then tokens, then components; no color or font questions during product intake [S-L18-322, S-L18-321, S-L18-303]. OpenDesigner already has the ordering data: stage order and fan-out in `synthesis/decision-graph.json` and the Quick/Standard/Expert modes in `synthesis/QUESTIONNAIRE.md`.
6. **Show, do not describe.** Prompt-only interfaces raise the "articulation barrier"; clickable, visual choices lower it [S-L18-315, S-L18-320, S-L18-311]. Use the Part D ladder.
7. **Ask for examples, including one the user dislikes.** A concrete reference carries its own don'ts; examples are among the most reliable ways to steer a model [S-L18-323, S-L18-309, S-L18-302].
8. **Word questions neutrally; put the recommendation in the option, not the question** [S-L18-317; placement inferred]. Closed questions for concrete choices, open ones only for vague starts [S-L18-318, S-L18-346].
9. **Record defaults honestly.** An unanswered or delegated question takes the default and is stored as `default` or `delegated`, never as confirmed: "A recommendation you made is not an answer you received" [S-L18-310, S-L18-322, S-L18-306].
10. **Play back before writing.** Summarize inferences, then a check-your-answers view with a change link per decision; give decisions stable ids so the user can say "change D3" [S-L18-343, S-L18-322, S-L18-312].
11. **Stay short.** Essential answer first, "more detail" on request; do not re-offer declined follow-ups [S-L18-313, S-L18-316].
12. **Interview in one session, build from the written spec in a fresh one**, so the transcript does not crowd the build context [S-L18-300, S-L18-309].
13. **Newer models need less scripting.** OpenAI's Sep 2026 guidance: the current model asks for clarification more readily, over-specified recipes hurt, and skills should say when to ask, stop or decline and which facts must not be inferred [S-L18-133, S-L18-134, S-L18-123]. So the skill should hold the decision data and the rules above, not a verbatim question script [inferred].

## Part G. Keeping harmony across sessions and models

Ranked by strength of evidence (H3) [S-L18-3xx as cited]:
1. **A closed, structured token source referenced by name.** DTCG 2025.10 is a stable W3C Community Group format with `$description` for intent and `$deprecated` instead of deletion [S-L18-324, S-L18-325]. In Sanity's eval of its own design-system docs (Aug 2026), JSON-structured docs plus 3 MCP tools took Sonnet 4.6 from 20% to 90% task success; retrievable code examples helped most, lint less [S-L18-332]. Anthropic reports models overwrite JSON less often than Markdown [S-L18-327]. Single-vendor eval, so treat the numbers as indicative.
2. **Retrievable component docs and code examples** (Storybook MCP, Figma Code Connect, shadcn registry) [S-L18-344, S-L18-337, S-L18-338].
3. **Deterministic gates, not advice.** DESIGN.md lint (broken refs, contrast, orphan tokens), stylelint strict-value, an audit script that exits 1, Claude Code hooks; Anthropic: CLAUDE.md is "context, not enforced configuration" [S-L18-323, S-L18-339, S-L18-334, S-L18-329].
4. **One short always-loaded context file that routes to granular files** (AGENTS.md; Figma Make's guidelines folder; skills; path-scoped rules) [S-L18-330, S-L18-336, S-L18-345, S-L18-341].
5. **Rationale plus an append-only decision log** (ADR style: superseded, not deleted; tagged confirmed / default / delegated) [S-L18-342, S-L18-323]. Logical rather than measured.
6. **A start-of-session routine:** read state, decision log and git log, run the checks, then work [S-L18-327, S-L18-326].
7. **Version-to-version drift checks** (`design.md diff`, upstream sync) [S-L18-323, S-L18-334].
8. **Fresh-context visual review** against the spec [S-L18-300].

What this means for OpenDesigner's outputs is DC-L18-10 to DC-L18-12.

---

## Part H. Decision Cards

Field names follow SCHEMA; for distribution decisions "Token encoding" means the files and schemas emitted, and "Platform notes" means host differences.

### DC-L18-01: Primary delivery unit
- **Block path:** Distribution > Packaging > Core unit
- **Questions the designer answers:** What does a person install to get OpenDesigner into their AI? Does it need a server? Does it work offline?
- **Options:** (a) **Agent Skill folder** (SKILL.md + references + scripts + assets): loads in Claude app/Code/API, ChatGPT (via plugin) and Codex, Cursor, Copilot, Gemini CLI and ~40 more [S-L18-001, S-L18-203, S-L18-106]. (b) **MCP server first**: one visual implementation for Claude + ChatGPT + VS Code + Cursor, but needs hosting and gives nothing visual in terminal agents [S-L18-024, S-L18-044]. (c) **Custom GPT**: retiring 11 Dec 2026 [S-L18-118]. (d) **Standalone web app**: full control, but not "load into your own AI" (BRIEF req. 6). (e) **Project knowledge bundle** (ChatGPT/Claude Projects): zero install, weakest structure [S-L18-126].
- **Visual effect:** (a) text-first with host-native visuals where present; (b) the same widget UI in every chat host that renders MCP Apps; (d) the richest UI but outside the user's AI [inferred].
- **Depends on (upstream):** BRIEF requirements 6-7.
- **Affects (downstream):** DC-L18-02 to 07; build order (Part I).
- **Token encoding:** `skills/opendesigner/SKILL.md` with portable frontmatter only (`name`, `description`, `license`, `compatibility`, `metadata`) [S-L18-003, S-L18-050].
- **Platform notes:** claude.ai needs code execution enabled; API skills have no network; ChatGPT web gets skills only inside plugins [S-L18-001, S-L18-106].
- **Accessibility constraints:** text fallback must be complete so screen-reader and terminal users lose nothing [inferred].
- **Default + heuristic:** **(a) skill first, (b) MCP server second, (e) as a documented fallback, never (c).** Heuristic: "If you're explaining how to do something, that's a skill; if you need access to something, that's MCP" [S-L18-053].
- **Evidence:** [S-L18-001, S-L18-003, S-L18-050, S-L18-053, S-L18-106, S-L18-118, S-L18-126, S-L18-203, S-L18-024, S-L18-044]

### DC-L18-02: Repo layout for multi-host discovery
- **Block path:** Distribution > Packaging > Discovery paths
- **Questions the designer answers:** Which folders must exist so each agent finds the skill and the instructions when the repo is cloned? Symlinks or copies?
- **Options:** (a) `skills/` source of truth + **generated real copies** in `.agents/skills/` and `.claude/skills/` (+ `.kiro/skills/` if wanted). (b) Symlinks `.claude/skills -> .agents/skills` (SSW's recommendation) [S-L18-258]. (c) Only `.agents/skills` (misses Claude Code, Cline, Kiro) [S-L18-212, S-L18-241, S-L18-234]. Instructions: (i) AGENTS.md canonical + `CLAUDE.md` and `GEMINI.md` each containing `@AGENTS.md` [S-L18-211, S-L18-213]; (ii) AGENTS.md alone (Claude Code reads it only without CLAUDE.md, and not on Bedrock or older versions) [S-L18-036].
- **Visual effect:** none; this decides whether the interview starts at all in a given tool [inferred].
- **Depends on (upstream):** DC-L18-01.
- **Affects (downstream):** release script, CI check that copies match, install docs.
- **Token encoding:** a `scripts/sync-skills` step that copies `skills/*` into discovery folders and fails CI on drift [inferred].
- **Platform notes:** Windows symlinks need admin or Developer Mode and Git checks them out as text files; Claude's Edit/Write refuse to write through symlinks; zip downloads and web uploads lose them [S-L18-211, S-L18-258, inferred]. Agent Plugins allows symlinks only inside the plugin root [S-L18-059].
- **Accessibility constraints:** n/a.
- **Default + heuristic:** **(a) + (i).** Keep AGENTS.md under ~200 lines (Claude) and far under Codex's 32 KiB; it routes to the skill and data rather than repeating them [S-L18-329, S-L18-112, S-L18-134].
- **Evidence:** [S-L18-036, S-L18-059, S-L18-112, S-L18-134, S-L18-211, S-L18-212, S-L18-213, S-L18-234, S-L18-241, S-L18-251, S-L18-258, S-L18-329]

### DC-L18-03: Plugin manifests and distribution channels
- **Block path:** Distribution > Channels
- **Questions the designer answers:** Through which stores and commands does each audience install it? Which manifests are needed?
- **Options:** (a) **Claude marketplace in the repo**: `.claude-plugin/marketplace.json` + `plugin.json`, installable with `/plugin marketplace add ckryptickunal/OpenDesigner` in Claude Code and via Customize > Plugins > Add marketplace in the Claude app; later a PR to `claude-plugins-official` [S-L18-004, S-L18-006, S-L18-007]. (b) **Agent Plugins `plugin.json`** at the root (+ optional `mcp.json`) for Codex, ChatGPT, Cursor, VS Code, Copilot, Kiro; submit to the OpenAI plugin directory for ChatGPT web users [S-L18-059, S-L18-102, S-L18-103]. (c) **Release zip of the skill** for claude.ai upload and org provisioning [S-L18-002]. (d) **MCP registries** for the server (official registry, GitHub registry, Claude directory) [S-L18-246, S-L18-247, S-L18-028]. (e) **ChatGPT Project starter** (instructions + at most 5 knowledge files, to fit Free) [S-L18-126].
- **Visual effect:** none directly; ChatGPT web users only get plugin UI and skills through (b) + directory approval [S-L18-104].
- **Depends on (upstream):** DC-L18-01, DC-L18-02, DC-L18-05.
- **Affects (downstream):** README install matrix; versioning (`version` in both manifests).
- **Token encoding:** Agent Plugins `plugin.json` needs `$schema` + `name` (1-64, lowercase, hyphens, periods); Claude `plugin.json` needs `name`; both find skills in `skills/` [S-L18-059, S-L18-004].
- **Platform notes:** No documented route lets a Plus/Pro ChatGPT web user install from GitHub directly [S-L18-104]; Codex IDE plugin support is contradictory [S-L18-107, S-L18-109]; the `anthropics/skills` repo is a working template for (a) [S-L18-034].
- **Accessibility constraints:** n/a.
- **Default + heuristic:** **(a) + (b) + (c) at launch; (d) with the server; (e) as a Free-tier fallback.** One `skills/` folder, two manifests, one version number [inferred].
- **Evidence:** [S-L18-002, S-L18-004, S-L18-006, S-L18-007, S-L18-028, S-L18-034, S-L18-059, S-L18-102, S-L18-103, S-L18-104, S-L18-107, S-L18-109, S-L18-126, S-L18-246, S-L18-247]

### DC-L18-04: Knowledge format and chunking
- **Block path:** Distribution > Knowledge > Format
- **Questions the designer answers:** How do 325 decision cards, the ontology and the questionnaire fit inside a model's context? Markdown or JSON?
- **Options:** (a) Ship the synthesis files as they are (QUESTIONNAIRE.md 267 KB, cards.json 826 KB, ontology.json 261 KB, measured on disk) and let the model read them. (b) **Chunk by stage and by card**: `references/stages/<nn>-<name>.md` (one screen each) + `data/*.json` indexes, loaded on demand. (c) Serve chunks only through MCP resources.
- **Visual effect:** (a) risks the model skimming or truncating; (b) keeps each step's facts in view [inferred].
- **Depends on (upstream):** `synthesis/QUESTIONNAIRE.md` stage structure; DC-L18-01.
- **Affects (downstream):** SKILL.md router, MCP resources, ChatGPT Project bundle.
- **Token encoding:** SKILL.md body under 5k tokens / 500 lines; references one level deep [S-L18-050]; JSON for data the model must not rewrite [S-L18-327, S-L18-332]; MCP results under Claude Code's 25k-token default [S-L18-037].
- **Platform notes:** ChatGPT Free Projects allow 5 files, so the Project bundle concatenates to <=5 files [S-L18-126]; Skills over MCP caps 512 files / 16 MiB per skill [S-L18-025].
- **Accessibility constraints:** n/a.
- **Default + heuristic:** **(b), with (c) as a mirror when the server exists.** Rule: the model should never need more than one stage file plus the state file to ask the next question [inferred].
- **Evidence:** [S-L18-025, S-L18-037, S-L18-050, S-L18-126, S-L18-327, S-L18-332]

### DC-L18-05: MCP server scope, hosting and auth
- **Block path:** Distribution > Live layer > MCP server
- **Questions the designer answers:** Should OpenDesigner run a server? Local or remote? Who pays for hosting? Does it need accounts?
- **Options:** (a) None (skill only). (b) **Remote, stateless, no-auth, read-only**: knowledge resources, pure generator tools, MCP Apps views, prompts (C2). (c) Local stdio package (`npx`, MCPB) for offline and for Claude Desktop, Codex, Cursor, VS Code [S-L18-049, S-L18-113]. (d) Remote with OAuth and saved projects.
- **Visual effect:** (b)/(c) unlock the widget interview in every MCP Apps host [S-L18-024].
- **Depends on (upstream):** DC-L18-01, DC-L18-04.
- **Affects (downstream):** DC-L18-06/07; directory listings; security review.
- **Token encoding:** tools carry `readOnlyHint: true`, `destructiveHint: false` [S-L18-019, S-L18-119]; views are `ui://` resources with `text/html;profile=mcp-app` and `_meta.ui.csp` [S-L18-011, S-L18-101].
- **Platform notes:** ChatGPT web cannot reach local servers except via Secure MCP Tunnel [S-L18-120]; Claude API connector is tools-only [S-L18-048]; the 2026-07-28 spec makes plain round-robin hosting possible [S-L18-022]; Cloudflare Workers supports it [S-L18-054].
- **Accessibility constraints:** views must meet WCAG AA, keyboard use and 44 pt targets per Claude's MCP Apps guidelines [S-L18-017].
- **Default + heuristic:** **(b) plus (c) from the same codebase; defer (d).** State stays in the user's files, so no user data is stored [inferred from S-L18-022].
- **Evidence:** [S-L18-011, S-L18-017, S-L18-019, S-L18-022, S-L18-024, S-L18-048, S-L18-049, S-L18-054, S-L18-101, S-L18-113, S-L18-119, S-L18-120]

### DC-L18-06: Visual surface ladder and capability detection
- **Block path:** Interview > Surface
- **Questions the designer answers:** On this host, right now, what is the best way to show a palette, a spacing scale or a component preview?
- **Options (ladder, best first):** 1 OpenDesigner MCP App view (if its tools are present) [S-L18-011]; 2 Claude Design canvas when the user already uses it (hand-off, not control) [S-L18-029]; 3 host-native model-written HTML: Claude custom visuals, Claude/Claude Code artifacts, Codex desktop browser [S-L18-041, S-L18-043, S-L18-115]; 4 Figma or Paper canvas via their MCPs (L16); 5 local HTML file opened by the user; 6 host question tool (AskUserQuestion, `request_user_input`) [S-L18-304, S-L18-310]; 7 plain text with hex values and numbered options.
- **Visual effect:** 1-5 show the real effect of the choice; 6-7 describe it [inferred].
- **Depends on (upstream):** DC-L18-05; host (Part A).
- **Affects (downstream):** `assets/templates/*.html` (one template per foundation: palette, type scale, spacing ruler, radius/shape, elevation, motion, component sheet, options gallery) reused by rungs 1, 3 and 5 [inferred].
- **Token encoding:** each template reads a JSON payload (candidate tokens + labels) so the same file renders in any rung [inferred].
- **Platform notes:** Claude inline cards: max 2 actions, no dropdowns, carousels 3-8; fullscreen for editors [S-L18-017]; custom visuals are not on mobile [S-L18-041]; ChatGPT code-block previews have no return channel [S-L18-128].
- **Accessibility constraints:** every visual carries text equivalents (hex, contrast ratio, px values) so rung 7 is the same content [inferred]; honor host light/dark tokens for chrome [S-L18-017].
- **Default + heuristic:** detect from the tools the model can see, pick the highest rung available, and say which rung is in use. Never block the interview on a visual [inferred].
- **Evidence:** [S-L18-011, S-L18-017, S-L18-029, S-L18-041, S-L18-043, S-L18-115, S-L18-128, S-L18-304, S-L18-310]

### DC-L18-07: How a visual choice returns to the model
- **Block path:** Interview > Return channel
- **Questions the designer answers:** After the user clicks a swatch, how does the model learn it, reliably and without retyping?
- **Options:** (a) MCP Apps `ui/message` (visible chat turn) or `tools/call` (`od_record_decision`) [S-L18-011]; (b) `ui/update-model-context` (silent context update) [S-L18-011]; (c) custom-visual click-to-prompt [S-L18-041]; (d) "Copy as prompt" string, e.g. `OD:set color.brand.seed=#3B5BDB` [S-L18-043]; (e) artifact comments sent to Claude (Team/Ent) [S-L18-043]; (f) Codex browser element comments [S-L18-115]; (g) typed reply.
- **Visual effect:** (a)/(c) feel like one continuous interview; (d)/(g) add a paste step [inferred].
- **Depends on (upstream):** DC-L18-06.
- **Affects (downstream):** state schema (every choice becomes a decision record).
- **Token encoding:** one compact grammar for all channels, `OD:<action> <token-path>=<value> [status]`, parsed identically whether it arrives by widget, click or paste [inferred].
- **Platform notes:** hosts can restrict which tools an app may call and may gate calls behind user approval [S-L18-021, S-L18-010].
- **Accessibility constraints:** every widget action also has a keyboard path and a text equivalent [S-L18-017].
- **Default + heuristic:** **(a) with a visible `ui/message`** so the choice appears in the transcript and survives a context reset; (b) only for high-frequency slider drags; (d) wherever no bridge exists [inferred].
- **Evidence:** [S-L18-010, S-L18-011, S-L18-017, S-L18-021, S-L18-041, S-L18-043, S-L18-115]

### DC-L18-08: Interview pacing (where the time goes)
- **Block path:** Interview > Pacing
- **Questions the designer answers:** Which decisions deserve three turns and a visual comparison, and which take a default and a confirm chip?
- **Options:** (a) Fixed script, same depth for every question. (b) **Fan-out-weighted**: depth set by each decision's fan-out and downstream reach in `synthesis/decision-graph.json` (e.g. personality DC-L06-02 fans out to 15 decisions and reaches 116), with Quick/Standard/Expert modes from the questionnaire. (c) User-chosen depth per stage.
- **Visual effect:** (b) spends the visual budget on the choices that change the most screens [inferred].
- **Depends on (upstream):** `synthesis/decision-graph.json`, `synthesis/QUESTIONNAIRE.md` (modes, cycles on one screen).
- **Affects (downstream):** SKILL.md pacing rules; `od_next_questions` logic.
- **Token encoding:** `pacing: {fanout_threshold_deep: 8, show_visual_if_reach_gt: 20}` in `data/pacing.json` (values to calibrate) [inferred].
- **Platform notes:** in terminal hosts, deep decisions get a local HTML or artifact preview; shallow ones stay in text [inferred].
- **Accessibility constraints:** accessibility floor decisions (contrast target, motion reduction) are always "deep" regardless of fan-out, because errors there are costly [inferred].
- **Default + heuristic:** **(b) with (c) as an override.** One high-impact decision per turn; group up to 3 low-impact ones; defaults recorded as `default` [S-L18-321, S-L18-322, S-L18-304, S-L18-310].
- **Evidence:** [S-L18-304, S-L18-310, S-L18-321, S-L18-322, S-L18-335; synthesis/DECISION-GRAPH.md]

### DC-L18-09: Question format
- **Block path:** Interview > Question anatomy
- **Questions the designer answers:** What does one well-formed OpenDesigner question look like in chat?
- **Options:** (a) Open question. (b) **Closed question with 2-4 options, one recommended with a reason, a visual per option, "other" allowed, and "what this changes downstream" in one line.** (c) A form with every option of a stage (MCP Apps "configuring with many options") [S-L18-021].
- **Visual effect:** (b) teaches while asking; (c) fits cycle screens where decisions constrain each other [inferred].
- **Depends on (upstream):** DC-L18-06, DC-L18-08.
- **Affects (downstream):** stage files format; widget templates.
- **Token encoding:** each question in `references/stages/*.md` carries `id`, `why_it_matters`, `options[] {label, value, effect, systems_using_it}`, `recommended`, `reason`, `affects[]` (from the cards' "Affects" fields) [inferred].
- **Platform notes:** AskUserQuestion takes up to 4 options per question [S-L18-304]; elicitation forms take enums only [S-L18-301].
- **Accessibility constraints:** neutral wording; recommendation in the option, not the stem [S-L18-317].
- **Default + heuristic:** **(b) per question; (c) for cycle screens.** Ask for 1-3 references the user likes and one they dislike at the start of each visual stage [S-L18-323, S-L18-302].
- **Evidence:** [S-L18-021, S-L18-301, S-L18-302, S-L18-304, S-L18-310, S-L18-317, S-L18-321, S-L18-323, S-L18-335]

### DC-L18-10: Durable outputs written to the user's repo
- **Block path:** Harmony > Outputs
- **Questions the designer answers:** What files let a later session, maybe a different model, extend the system without breaking it? What is canonical?
- **Options:** (a) DESIGN.md only (Stitch format, alpha, Apache-2.0; exports to DTCG) [S-L18-323, S-L18-350]. (b) **DTCG 2025.10 tokens as canonical + DESIGN.md as the readable view + `decisions.md` (ADR-style log) + `opendesigner.state.json` (answers, statuses, coverage against the ontology) + an AGENTS.md snippet pointing to them.** (c) Tokens only.
- **Visual effect:** (b) keeps colors, type and spacing identical across sessions because the values are read, not remembered [inferred from S-L18-332].
- **Depends on (upstream):** L07 token decisions; DC-L18-09.
- **Affects (downstream):** exports (CSS, Tailwind, Figma variables); DC-L18-11/12.
- **Token encoding:** `tokens/*.tokens.json` (DTCG, `$description` = intent, `$deprecated` instead of delete) [S-L18-325]; decision record `{id, question_id, value, status: confirmed|default|delegated|locked, reason, fanout, date, supersedes}` [S-L18-342, S-L18-310, inferred].
- **Platform notes:** Claude Code's artifact design skill already looks for a design system in CLAUDE.md or a theme file, so the AGENTS.md/CLAUDE.md pointer makes Claude's own visuals follow the user's system [S-L18-043].
- **Accessibility constraints:** store the contrast target and motion policy as locked decisions so later sessions cannot silently weaken them [inferred].
- **Default + heuristic:** **(b).** JSON for what must not drift, Markdown for why [S-L18-327, S-L18-323].
- **Evidence:** [S-L18-043, S-L18-310, S-L18-323, S-L18-325, S-L18-327, S-L18-332, S-L18-342, S-L18-350]

### DC-L18-11: Enforcement shipped with the system
- **Block path:** Harmony > Guardrails
- **Questions the designer answers:** How is "stay on system" checked rather than hoped for?
- **Options:** (a) Prose rules only. (b) **Validator script in the skill** (`scripts/od_validate.py`, stdlib only: token refs resolve, contrast pairs pass, spacing and radius on scale, no orphan tokens) run after every generation step. (c) Exported lint configs for the user's CI (stylelint strict-value, DESIGN.md lint) [S-L18-339, S-L18-323]. (d) Host hooks (Claude Code) [S-L18-329].
- **Visual effect:** off-system values are caught before the user sees them, the same promise Claude Design makes [S-L18-032].
- **Depends on (upstream):** DC-L18-10; L11 DC-L11-24.
- **Affects (downstream):** export bundle; review skill.
- **Token encoding:** `lint/` folder with configs generated from the tokens [inferred].
- **Platform notes:** API skills have no network and no package installs, and claude.ai network varies, so scripts must be dependency-free [S-L18-001].
- **Accessibility constraints:** contrast check against the chosen target (WCAG 2.2 AA default, per the questionnaire's pre-fills).
- **Default + heuristic:** **(b) + (c); (d) documented as optional.** Lint and autofix rated medium in Sanity's eval, so pair them with examples [S-L18-332].
- **Evidence:** [S-L18-001, S-L18-032, S-L18-323, S-L18-329, S-L18-332, S-L18-339]

### DC-L18-12: The "extend" session protocol
- **Block path:** Harmony > Later sessions
- **Questions the designer answers:** When someone returns months later, in another tool, what does the model do first?
- **Options:** (a) Start the interview again. (b) **Start-up routine:** read `opendesigner.state.json`, `decisions.md`, tokens and git log; run the validator; list locked decisions; ask only about what is new; flag any request that conflicts with a locked decision and ask before superseding it [S-L18-327, S-L18-326, S-L18-322]. (c) Free-form edits.
- **Visual effect:** new components inherit existing tokens instead of re-inventing values; community reports agents "reinvented existing components and hardcoded values" without context [L11 DC-L11-23, COMMUNITY-SIGNAL].
- **Depends on (upstream):** DC-L18-10, DC-L18-11.
- **Affects (downstream):** `skills/opendesigner-extend/SKILL.md`; team communication (decision log doubles as the explanation for teammates, BRIEF req. 10).
- **Token encoding:** superseding writes a new decision record with `supersedes`, never edits the old one [S-L18-342].
- **Platform notes:** works in any host that can read files; in chat-only hosts the user uploads the state and tokens files [inferred].
- **Accessibility constraints:** re-run contrast checks on every extension [inferred].
- **Default + heuristic:** **(b).** "A recommendation you made is not an answer you received": defaults stay marked so a later session can revisit them [S-L18-310].
- **Evidence:** [S-L18-310, S-L18-322, S-L18-326, S-L18-327, S-L18-342]

### DC-L18-13: Design-tool round trip and designer hooks inside AI hosts
- **Block path:** Distribution > Round trip
- **Questions the designer answers:** Can the interview write the result into Figma or Paper from the user's AI? Which hosts can?
- **Options:** (a) Skill instructions that call the Figma MCP (`use_figma` writes variables, styles, frames; remote only; Full seat; free beta) (L16 A1). (b) Paper MCP `write_html` / `create_tokens` (Paper Desktop, local) (L16 B2). (c) Export files only (Tokens Studio / Figma variables JSON) (L07).
- **Visual effect:** (a)/(b) give designers a native file to refine, keeping the "designer hooks" of BRIEF req. 2 [inferred].
- **Depends on (upstream):** DC-L18-10; L16 DC-L16-02 and DC-L16-13.
- **Affects (downstream):** `skills/opendesigner-export` sub-flows per tool.
- **Token encoding:** DTCG to Figma variables mapping (L07); DTCG to CSS variables for Paper, which has no modes yet (L16 B4).
- **Platform notes:** Figma write clients: Claude Code, Claude Desktop, Codex, Cursor, VS Code/Copilot and others; ChatGPT is listed in Figma's catalog but not its write matrix; Gemini CLI is not listed [S-L18-047, S-L18-136, S-L18-244; L16 A1]. Paper needs a host with local MCP [L16 B3].
- **Accessibility constraints:** n/a.
- **Default + heuristic:** **(c) always, (a)/(b) when the host has the MCP connected.** Detect the tools, offer the write, confirm before writing to a real file (Figma advises testing on a duplicate) [L16 A1].
- **Evidence:** [S-L18-047, S-L18-136, S-L18-244; L16 A1, B2-B4; L07]

### DC-L18-14: Trust and safety of the package
- **Block path:** Distribution > Security
- **Questions the designer answers:** How does an open-source skill and server stay safe to install and hard to hijack?
- **Options:** (a) No special handling. (b) **Least privilege:** no network in scripts, minimal `allowed-tools`, read-only server that returns data not instructions, signed releases, reference intake treats fetched pages as data. (c) Also Skills-over-MCP digests and pinned versions.
- **Visual effect:** none [inferred].
- **Depends on (upstream):** DC-L18-01, DC-L18-05.
- **Affects (downstream):** reference-intake flow (L17), MCP Apps CSP declarations.
- **Token encoding:** `_meta.ui.csp` with empty `connectDomains` unless needed [S-L18-011].
- **Platform notes:** Anthropic advises installing skills only from trusted sources; Enterprise can scan uploaded skills [S-L18-001]; Skills over MCP requires digest checks and approval [S-L18-025]; community flagged vendor MCP prompt injection [COMMUNITY-SIGNAL S-L00-050].
- **Accessibility constraints:** n/a.
- **Default + heuristic:** **(b), and (c) once hosts support it.** Rule: the package never asks the model to fetch and follow remote instructions [inferred].
- **Evidence:** [S-L18-001, S-L18-011, S-L18-025; COMMUNITY-SIGNAL S-L00-050]

---
## Part I. Recommended architecture for OpenDesigner

### I1. Repo layout (works in Claude, ChatGPT and Codex at once) [inferred from Parts A-H]
```
OpenDesigner/
├── AGENTS.md                  # canonical entry (<200 lines): what it is, start/extend commands, file map, rules
├── CLAUDE.md                  # "@AGENTS.md" + Claude notes (visual ladder: MCP App > custom visual/artifact > text)
├── GEMINI.md                  # "@AGENTS.md"
├── README.md                  # humans: one install section per host (Part A)
├── plugin.json                # Agent Plugins 1.0: $schema + name (+ version, license) -> Codex, ChatGPT, Cursor, VS Code, Copilot, Kiro
├── mcp.json                   # Agent Plugins MCP config (remote URL, optional)
├── .claude-plugin/
│   ├── plugin.json            # Claude plugin manifest
│   └── marketplace.json       # repo doubles as a Claude marketplace (pattern of anthropics/skills)
├── .mcp.json                  # Claude Code / VS Code project config (optional)
├── skills/                    # SOURCE OF TRUTH (Agent Skills format, portable frontmatter only)
│   ├── opendesigner/          # router skill: interview flow, modes, pacing, visual ladder, output contract
│   │   ├── SKILL.md           # <500 lines
│   │   ├── references/stages/ # one file per questionnaire screen (from synthesis/QUESTIONNAIRE.md)
│   │   ├── references/rules.md        # interview rules (Part F), taste calibration (L17)
│   │   ├── assets/templates/  # palette, type-scale, spacing-ruler, radius, elevation, motion, component-sheet, gallery (.html)
│   │   ├── assets/output/     # DESIGN.md, decisions.md, state.json, AGENTS-snippet.md templates
│   │   └── scripts/           # od.py: state, ramps, scales, contrast, validate, export (stdlib only, no network)
│   ├── opendesigner-extract/  # reference intake: repo CSS, URL, screenshot, Figma variables
│   ├── opendesigner-extend/   # later-session protocol (DC-L18-12)
│   └── opendesigner-export/   # DTCG, CSS vars, Tailwind, Figma (use_figma), Paper
├── .agents/skills/            # GENERATED copy of skills/ (Codex, Cursor, Copilot, Gemini CLI, Zed, ...)
├── .claude/skills/            # GENERATED copy (Claude Code, Cline)
├── data/                      # ontology.json, decision-graph.json, levers.json, questions/*.json, pacing.json
├── server/                    # phase 2: stateless MCP server + MCP Apps views (reuses assets/templates)
├── chatgpt-project/           # instructions.md + <=5 knowledge files (Free-tier Project fallback)
└── dist/                      # release zips: skill zip for claude.ai upload, plugin zip
```

### I2. Trade-offs
| Choice | Gains | Costs |
|---|---|---|
| Skills-first | No hosting; works offline and in terminals; one format across ~46 clients [S-L18-203] | Visuals depend on the host; ChatGPT web needs directory approval for plugins [S-L18-104] |
| Generated copies over symlinks | Works on Windows, zips and web uploads [S-L18-211] | A sync step and a CI drift check [inferred] |
| Two manifests | Covers Claude (Anthropic is not in Agent Plugins) and everyone else [S-L18-057, S-L18-004] | Two version fields to keep in step [inferred] |
| MCP server with MCP Apps | Same widget UI in Claude, ChatGPT, VS Code, Cursor, Goose, M365 Copilot [S-L18-024] | Hosting, directory review, CSP limits; nothing visual in CLIs [S-L18-017, S-L18-044] |
| Chunked JSON + Markdown | Fits skill budgets and tool-result caps; JSON resists rewriting [S-L18-050, S-L18-037, S-L18-327] | A build step from `synthesis/` into `skills/` and `data/` [inferred] |
| Custom GPT | none lasting | Retires 11 Dec 2026 [S-L18-118] |

### I3. What to build first
1. **Skill + chunked knowledge + text interview + output contract** (DESIGN.md, DTCG tokens, decisions log, state file, validator). This alone runs in Claude Code, Claude app (zip), Codex, ChatGPT desktop, Cursor, Copilot and Gemini CLI.
2. **Manifests and channels:** `.claude-plugin/marketplace.json`, Agent Plugins `plugin.json`, the claude.ai zip, the ChatGPT Project bundle; submit to the OpenAI plugin directory.
3. **Static visual templates** fed by JSON, used by Claude custom visuals and artifacts, Claude Code artifacts, the Codex browser and local files, with the `OD:` copy-back grammar (DC-L18-07).
4. **MCP server + MCP Apps views** reusing the same templates; test in Claude Desktop with a local stdio entry first, as Anthropic's getting-started guide does [S-L18-015]; then remote, stateless, no-auth.
5. **Round-trip writers** for Figma and Paper as export sub-flows (L16).

---

## Reconciliation with `sources/COMMUNITY-SIGNAL.md` (L00)
- **Agrees:** DESIGN.md is a draft, not a standard; treat it as a readable view with DTCG as canonical [COMMUNITY-SIGNAL; S-L18-323]. Figma MCP write features are client-dependent [S-L00-028; S-L18-136 vs S-L18-244]. MCP servers are an attack surface [S-L00-050; DC-L18-14].
- **Adds:** L00 predates the Agent Plugins 1.0 standard (6 Aug 2026), the custom GPT retirement notice, and the Claude/Cowork merge (16 Sep 2026) [S-L18-058, S-L18-118, S-L18-038].
- **No dispute found** on MCP Apps, Agent Skills or AGENTS.md in L00.

## Cross-lane notes
- **L11:** DC-L11-23 lists "Claude Design (17 Apr 2026)"; it is now integrated into every Claude conversation and Claude Code (Sep 2026), and design systems are artifacts [S-L18-029, S-L18-032]. OpenAI's plugins and Agent Plugins 1.0 are new distribution channels for DC-L11-23.
- **L16:** Claude's desktop Code tab now renders MCP App widgets (2026-09-02) [S-L18-045]; Codex desktop has a built-in browser with element comments [S-L18-115]; both are preview surfaces for DC-L16-06.
- **L17:** the Part F interview rules and DC-L18-08/09 are the AI-host form of L17's builder process; gstack and impeccable sequencing is re-cited only briefly [S-L18-321, S-L18-322].
- **Synthesis:** `QUESTIONNAIRE.md` (267 KB) and `cards.json` (826 KB) need a per-stage and per-card split before they can ship inside a skill (DC-L18-04).

## Open questions / gaps
- **ChatGPT web install path:** no documented way for a Plus/Pro web user to install a plugin straight from GitHub; directory approval timing unknown [S-L18-104, S-L18-103].
- **Developer mode plans:** developer docs (Plus/Pro included) and help center (Business/Ent/Edu beta) disagree [S-L18-119, S-L18-124].
- **Claude app plugins in Chat:** Help Center and changelog say plugin skills work in Chat; a claude.com docs page says they do not [S-L18-006, S-L18-045, S-L18-007].
- **Claude artifacts return channel:** no documented click-to-chat bridge for regular artifacts (custom visuals have one) [S-L18-027, S-L18-041].
- **MCP Apps with user-added remote connectors on claude.ai web:** Desktop local servers are documented [S-L18-015]; remote custom connectors rendering views is implied by the spec, not stated.
- **Paper from non-Claude hosts:** only the Claude Code path is documented [L16 B3].
- **Duplicate skill folders:** how each client dedupes a skill found in both `.agents/skills` and `.claude/skills` is unverified [S-L18-251].
- **Agent Plugins and Google:** Google's announced support is from secondary snippets only [S-L18-056].
- **Codex question tool scope** (plan mode only?) and **custom GPT instruction limit** unverified [S-L18-109, S-L18-141].
- **Evidence strength for harmony:** the only quantitative data is Sanity's eval of its own system and one preprint [S-L18-332, S-L18-335].
- **Not researched:** Google AI Studio, JetBrains Junie's AGENTS.md support (sources conflict), Windows behavior of each host's skill loader.

## Confidence
- **High (official docs or changelogs read today):** Agent Skills spec and Claude surfaces; Claude Code skill paths, AGENTS.md behavior, MCP features and artifacts; MCP Apps spec, client matrix and Claude/ChatGPT support dates; MCP 2026-07-28 changes; Agent Plugins 1.0 manifest; OpenAI plugins, skills and custom GPT retirement; Codex AGENTS.md, skills and MCP; Cursor, VS Code and Gemini CLI skill and MCP support; Claude Design timeline and features; custom visuals behavior.
- **Medium:** Figma catalog capability labels (JS-rendered page, fetch summary); plan eligibility where docs conflict; Codex desktop browser details; harmony mechanism rankings beyond items 1-2.
- **Inferred (labelled in text):** the repo layout, the `OD:` return grammar, pacing thresholds, the MCP server's tool list, and the build order. These are recommendations built from the verified facts, not facts.
