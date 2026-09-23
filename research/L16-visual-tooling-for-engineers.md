# L16: Visual design tooling for engineers and the design <-> code round trip

Lane: L16. Author: orchestrator subagent L16 (with helper subagents H1, H2, H3 whose sources are re-logged in the trace). Written 2026-09-23.
Trace: `traces/L16-trace.md`. Every claim is tagged `[S-L16-xxx]` or `[inferred]`. `S-L16-000` is the orchestrator's own observation of the local MCP servers on 2026-09-23.
Status: done (2026-09-23). 43 tools reviewed (Part A-D), 15 principles with originals (Part E), 15 Decision Cards (Part F), synthesis (Part G). Trace: 323 source rows (19 rejected) plus 11 search-log rows.

Related lanes (linked, not repeated): L07 owns tokens, DTCG and Figma's variable and component features (`research/L07-tokens-figma.md`, tables A6, A7, A9 and DC-L07-24). L11 owns the competitor review of design-system builder products and agent-readable distribution (`research/L11-process-governance.md`, Part G and DC-L11-16, DC-L11-23). This lane's angle is the **interaction model** and the **design <-> code workflow**.


## Lane overview

**What this lane covers.** How engineers operate visual design tools today, and how designs, tokens and components move between canvases and code. It covers Figma's developer surfaces and MCP server, Paper and its MCP server, 12 code-native editors, 13 AI builders and agent canvases, 3 Figma/code bridges, 15 theme and foundation playgrounds, and the design principles behind creative tools. It ends with patterns to adopt, round-trip architectures and the white space.

**Seven things that matter most for the builder**
1. **Figma MCP: reading works everywhere; writing needs the remote server.** Read tools (design context, variables, screenshots, metadata, motion, FigJam) are on both servers. Every write tool is on the remote server only (`https://mcp.figma.com/mcp`): `use_figma` (Plugin API JavaScript that creates frames, components, variants, variables, styles and auto layout), `generate_figma_design` (captures live UI), `create_new_file`, `upload_assets`, `generate_diagram`. Writing needs a Full seat and a catalog client. It is a free beta that will become usage-priced [S-L16-001] [S-L16-002] [S-L16-003] [S-L16-007] [S-L16-022].
2. **This machine can only read from Figma.** It has only the desktop server (6 read-only tools). The fix is Figma's Claude Code plugin or the remote server plus OAuth, with a Full seat [S-L16-000] [S-L16-004] [S-L16-008].
3. **Paper reads and writes HTML/CSS, including tokens, but has no modes yet.** Paper is an HTML/CSS canvas whose local MCP (Paper Desktop, `127.0.0.1:29979`) exposes 34 tools: reads (tree, JSX, computed styles, screenshots, tokens, comments) and writes (`write_html`, `update_styles`, `create_tokens`/`set_tokens`, files, pages, nodes). Its tokens are CSS variables with **no modes, no libraries and no DTCG** yet. Free is 100 MCP calls a week [S-L16-009] [S-L16-010] [S-L16-018] [S-L16-020].
4. **Direct manipulation has converged on one pattern:** select in a live preview, edit a scoped property panel, batch the edits, commit as a reviewable change (v0, Bolt, Figma Make, Subframe, Tempo). AI now shows up as "show me N" variations and model-generated sliders rather than as the only input [S-L16-242] [S-L16-253] [S-L16-026] [S-L16-293] [S-L16-299] [S-L16-264] [S-L16-269].
5. **Theme playgrounds share a strong interaction grammar and one hole.** The grammar: lock + shuffle, a seed or preset code that round-trips between URL, CLI and repo, outcome-first color (contrast targets), and previews on real components. The hole: none of the 16 examined shows a before/after diff, branches or light and dark side by side [S-L16-327] [S-L16-328] [S-L16-337] [S-L16-390].
6. **No tool found does deterministic two-way token sync between a canvas and git,** and only Penpot imports and exports DTCG natively. Two-way flows run through agents or manual git syncs (Part C4) [S-L16-113].
7. **Recommended architecture** [inferred]: the builder is itself the visual tool. It renders real HTML/CSS components from its own model. Direct manipulation writes deterministic patches to that model, which compiles to DTCG 2025.10 and to code. Figma (`use_figma` or DTCG import) and Paper (`write_html`, `create_tokens`) are one-click mirrors, with capture back only for review (Part G2).

**How to read this file.** Part A: Figma. Part B: Paper. Part C: tool-by-tool review. Part D: playgrounds. Part E: principles. Part F: Decision Cards DC-L16-01 to 15. Part G: synthesis (G1 patterns, G2 architectures, G3 white space). Then reconciliation with L00, cross-lane notes, gaps and confidence.

---

## Part A. Figma for developers (verified 2026-09-23)

### A1. The Figma MCP server: what an agent can read and write

Figma runs two MCP servers. The **remote** server (`https://mcp.figma.com/mcp`, OAuth) is available on all seats and plans. The **desktop** server runs inside the Figma desktop app at `http://127.0.0.1:3845/mcp` and needs a Dev or Full seat on a paid plan. Figma calls the remote server "preferred" and says the desktop server is "primarily for specific use cases for organizations and enterprises" [S-L16-007] [S-L16-005]. Only clients listed in Figma's MCP Catalog can connect [S-L16-004] [S-L16-006].

Every write-to-canvas and code-to-canvas tool is **remote-only** [S-L16-001] [S-L16-003].

| Tool | Reads or writes | Remote only? | What it does | Evidence |
|---|---|---|---|---|
| `get_design_context` | read | no | Design context for a layer or selection. Output is React + Tailwind by default; the prompt can ask for Vue, HTML/CSS or iOS, or for the project's own components. Uses Code Connect mappings when present | [S-L16-001] |
| `get_metadata` | read | no | Sparse XML outline (ids, names, types, position, size); lists pages when called without a node | [S-L16-001] |
| `get_screenshot` | read | no | PNG of a selection | [S-L16-001] |
| `get_variable_defs` | read | no | Variables and styles used in a selection (names and values) | [S-L16-001] |
| `get_motion_context` | read | no | Keyframe tracks, easing, precomputed CSS `@keyframes` and motion.dev snippets | [S-L16-001] |
| `get_figjam` | read | no | FigJam diagram as XML plus screenshots | [S-L16-001] |
| `get_code_connect_map` | read | no | Figma node id to code component (name, source path, snippet, framework label) | [S-L16-001] |
| `download_assets` | read | yes | Exports (PNG/JPG/SVG/PDF) and original source images, up to 20 nodes | [S-L16-001] |
| `get_libraries`, `search_design_system` | read | yes | List subscribed/available libraries; search components, variables and styles by text | [S-L16-001] |
| `get_code_connect_suggestions`, `get_context_for_code_connect` | read | mixed (the second is remote-only) | Figma-prompted steps of the Code Connect skill | [S-L16-001] |
| shader and generative-plugin readers (`list_shaders`, `get_shader`, `list_file_shaders`, `list_generative_plugins`, `get_generative_plugin`), `whoami` | read | yes | Source of shaders and generative plugins; identity and plans | [S-L16-001] |
| **`use_figma`** | **write** (and inspect) | **yes** | General-purpose create, edit, delete and inspect in Figma Design, FigJam and Slides: frames, components, variants, **variables**, styles, text, auto layout. It runs agent-written JavaScript against the **Plugin API** | [S-L16-001] [S-L16-002] [S-L16-022] |
| **`generate_figma_design`** | **write** | **yes** | "Code to canvas": captures live browser UI (localhost, staging or production) into a new file, an existing file or the clipboard as editable layers; auto-binds library variables | [S-L16-003] [S-L16-024] |
| `create_new_file` | write | yes | Blank Design, FigJam or Slides file in drafts | [S-L16-001] |
| `upload_assets` | write | yes | PNG/JPG/GIF/WebP up to 10 MB into a file or node fill | [S-L16-001] |
| `generate_diagram` | write | yes | FigJam diagram from Mermaid or plain language | [S-L16-001] |
| `add_code_connect_map`, `send_code_connect_mappings` | write (metadata only) | no | Map a Figma node to a code component; confirm suggested mappings | [S-L16-001] |
| `create_/update_generative_plugin`, `create_/update_shader` | write (code resources) | yes | Scaffold and update generative plugins and shaders; each needs a skill | [S-L16-001] |
| `weave_*` (6 tools) | run paid Weave workflows | n/a | Needs a paid Figma Weave account; spends Weave credits | [S-L16-001] |
| `create_design_system_rules` | **MCP prompt**, not a tool | n/a | Generates a rules file for codebase-aware code generation | [S-L16-001] |

**Plans, seats and limits.**
- **Writing to the canvas needs a Full seat** and edit permission on the file. Dev seats are read-only outside their own drafts. Code to canvas works on any seat in drafts, but a Full seat is needed for files outside drafts [S-L16-002] [S-L16-022] [S-L16-003].
- Write to canvas is a **free beta** that "will eventually be a usage-based paid feature" [S-L16-007] [S-L16-022].
- Read-tool rate limits: View and Collab seats get 20 calls a month on Starter and 6 a month on paid plans. Dev and Full seats get 200 a day (Professional, 10 a minute), 200 a day (Organization, 15 a minute) or 600 a day (Enterprise, 20 a minute). Some write tools are exempt [S-L16-006] (matches L07 A6).
- `use_figma` limits today: 20 KB response per call, no image assets, only fonts uploaded to the account, and components must be published by hand before Code Connect completes. Figma recommends testing on a duplicate file first [S-L16-002] [S-L16-022].
- Clients that can write to the canvas, per the Help Center matrix: Augment Code, Claude Code, Claude Desktop, Codex, Copilot CLI, Cursor, Factory, Firebender, Kiro, VS Code, Warp and Xcode (beta, remote only). Clients that connect but cannot write: Gemini CLI, Android Studio, Replit (remote only), Amazon Q and OpenHands (desktop only) [S-L16-007] [S-L16-002].
- Timeline: remote MCP server guide first published 15 May 2025. `use_figma` launched on **24 Mar 2026** (Figma blog). The in-canvas Figma agent was announced on 20 May 2026 and listed as open beta in the Config 2026 notes (rollouts from 24 Jun 2026) [S-L16-007] [S-L16-030] [S-L16-031] [S-L16-033]. A WebSearch summary gave 7 Jul 2026 for the write-to-canvas post; that is the page's modified date, not its publish date [S-L16-029].

### A2. What is connected on this machine, and why it cannot write

- **Observed:** the connected Figma server is `figma-desktop` at `http://127.0.0.1:3845/mcp`. It exposes only `get_design_context`, `get_figjam`, `get_metadata`, `get_motion_context`, `get_screenshot` and `get_variable_defs`, all read-only [S-L16-000] [S-L16-008] [S-L16-020]. A second connection named "Figma" shows 7 tools in this session (`get_design_context`, `get_metadata`, `get_screenshot`, `get_variable_defs`, `get_code_connect_map`, `add_code_connect_map`, and `create_design_system_rules` as a tool rather than a prompt). None of them can write to the canvas [S-L16-020]. There is no `mcp.figma.com` entry in `claude mcp list`, and the session reports that a plugin-provided Figma server needs OAuth first [S-L16-008].
- **Why:** Figma documents exactly this situation. `use_figma` and `generate_figma_design` exist only on the remote server. The desktop server "doesn't provide them", and a desktop entry can even shadow the remote tools because the names overlap [S-L16-003].
- **How to get write access (for Kunal, in an interactive session):** run `claude plugin install figma@claude-plugins-official`, which bundles the remote server and Figma's skills. The manual alternative is `claude mcp add --scope user --transport http figma https://mcp.figma.com/mcp`. Then choose /mcp, then Authenticate (OAuth) [S-L16-004]. Keep the desktop server under its own id (`figma-desktop`), or remove it, and name the remote server explicitly in prompts [S-L16-003]. Writing needs a Full seat [S-L16-002].
- **Is the Figma plugin route a separate write path?** Yes, in principle. `use_figma` is itself a thin wrapper that runs Plugin API JavaScript [S-L16-002], so a custom Figma plugin could also create variables, components and frames. That path runs inside Figma with a human present, not from an agent [inferred]. For variables specifically, the REST API can write them only on Enterprise with a Full seat (L07 A6).

### A3. Figma's developer surfaces, as interaction models

| Surface | Interaction model | Source of truth | Round trip | What feels good | Gaps for engineers | Evidence |
|---|---|---|---|---|---|---|
| **Dev Mode** | Inspect panel on the design canvas (Shift D); "ready for dev" statuses; compare changes (frame version history, compare with main component); dev resource links; Figma for VS Code | Figma file | Design to code: read-only inspection and code snippets | Specs, variables with code syntax and alias chains, and version compare in one place | Needs a paid Dev or Full seat; you inspect, you do not author; no code-to-design path | [S-L16-023] (variable details: L07 A6) |
| **Code Connect** | Mapping UI in Figma, or CLI templates in the repo | Code components, linked to Figma components | Tells `get_design_context` to emit your real components | Generated code reuses your components | Organization and Enterprise only; one repo per library file; mappings are manual work | L07 DC-L07-24, [S-L16-001] |
| **Figma Make** | Chat with an agent plus a live app preview; an edit tool with a Figma-style properties panel; draw-on-preview; annotations "for agent"; version history; direct code editing | The generated code | Figma frames go in as context; Make layers can be copied back to Design; published as a site | Point at the running UI and tweak properties; parallel chats | Full seat on paid plans. Direct edits are **staged and applied by the agent**, costing AI credits, instead of being written straight to code. Community verdict: "Ideation and concepts. Nothing actually usable" (Tier C) | [S-L16-025] [S-L16-026] [COMMUNITY-SIGNAL c] |
| **Figma agent** (in canvas) | Cmd/Ctrl+Enter prompt on any layer; parallel prompts with on-canvas progress; @-mention components and variables; undo in chat | Figma file and connected libraries | Stays inside Figma; hands off to Make or to MCP | "Go wide" (several distinct directions at once) or "go deep"; direct manipulation stays available alongside | Designer-facing; free beta; edit rights need a Full seat | [S-L16-027] [S-L16-031] |
| **Code to canvas** (`generate_figma_design`, Chrome extension, copy from Make) | Toolbar injected into the running app: "Entire screen" or "Select element" capture | Code (the running UI) | **Code to design.** Variables are bound on paste by matching page CSS variable names to Figma **code syntax**, then to variable names, then by best-matching scope | Real UI lands as editable layers; multi-step flows side by side | Output is flat layers with no library components; some properties are not bound; Check designs (Org/Ent) is needed to find misses | [S-L16-003] [S-L16-024] [S-L16-022] |
| **Write to canvas** (`use_figma`) | An agent in the IDE or CLI builds native Figma structure from a prompt plus a file link | Figma file, built from the existing library | Code or tokens to design, structurally: variables, components, variants, auto layout | Output is editable, library-linked Figma content, not a picture | Beta quality, 20 KB per call, no images, Full seat, future usage pricing | [S-L16-002] [S-L16-022] [S-L16-030] |

| **Code layers** (Config 2026) | Working code as a new kind of layer on the design canvas; convert code layers to design layers and back; start from an uploaded codebase or a cloned GitHub repo | Code, inside a Figma file | Both directions, inside Figma | Design and code side by side on one canvas | **Still closed beta** on 2026-09-23 (waitlist). Community pushback: "I don't want code layers. I want to design things" (Tier C) | [S-L16-033] [COMMUNITY-SIGNAL c] |

**Figma's own "design-system builder" recipe.** Figma ships an agent skill, `figma-generate-library`, described as a way to "Build or update a professional-grade design system in Figma from a codebase" [S-L16-039]. Its phases are:
0. Discovery, with no writes. It ends with a printed **gap analysis**: what is in code but not Figma, what is in Figma but not code, and every conflict with its resolution.
1. Foundations: collections and modes, primitives, semantic aliases, scopes on every variable (never `ALL_SCOPES`), code syntax on every variable, then text and effect styles.
2. File structure, plus foundation documentation pages, then a visual review.
3. Components, in dependency order.
4. Code Connect, then accessibility, naming and unbound-value audits.

The skill keeps a state ledger on disk. It also defines "decision forks": when code and Figma disagree, the agent shows both values with their provenance and asks the user which wins [S-L16-039]. This is the closest existing thing to Kunal's builder. It runs through an agent in a chat, not a visual UI, and it assumes the system already exists in code [inferred].

**Key lesson for the builder** [inferred from S-L16-024 and L07 DC-L07-20]: Figma's code-to-design binding uses a variable's **code syntax** as the join key between a CSS custom property and a Figma variable. If the builder writes code syntax (`--color-bg-surface` and so on) onto every Figma variable it creates, later captures and round trips bind automatically.

---

## Part B. Paper (paper.design), verified 2026-09-23

### B1. What Paper is
- Paper describes itself as "the connected canvas for teams shipping with agents": a professional design tool whose canvas **is real HTML and CSS**, available on the web and as Paper Desktop [S-L16-012] [S-L16-015].
- The March 2026 build log records "Launched Paper Desktop with MCP server support" [S-L16-014]. The Series A post (22 Jul 2026: $34M from Accel and ICONIQ, $38.5M in total) says ARR grew 25x in the month after the Desktop launch. That is a vendor claim. The post names Ramp, Lovable and Harvey as customers and says engineers, sales and growth teams also use Paper [S-L16-013].
- Paper's stated vision is that "Your CI pipeline will create canvases with visual diffs" and that custom harnesses will embed Paper [S-L16-013].
- Interaction model: a Figma-like direct-manipulation canvas (flex layouts, a Constraints panel, on-canvas gap and padding handles, on-canvas gradient handles, a pen tool, text hotkeys) plus agents working through MCP, with "agent presence" and working indicators shown on the canvas [S-L16-014]. Code export includes Copy as React CSS (⌥R) and Copy as Tailwind (⌥T) [S-L16-014].
- Pricing: Free gives unlimited viewers and editors and **100 MCP tool calls a week**. Pro costs $20 per editor per month ($16 billed yearly) and gives **1M MCP tool calls a week** [S-L16-010].

### B2. Paper MCP: what an agent can read and write

The MCP server starts when a file is opened in **Paper Desktop**; the web app does not host it [S-L16-009]. Paper's own guide calls the Figma MCP "read only" and warns that "The Paper MCP can read and write" [S-L16-009].

| Group | Tools (live server, 2026-09-23) | Documented on paper.design/docs/mcp? | Evidence |
|---|---|---|---|
| **Read: file and structure** | `get_basic_info` (file, page, node count, artboards), `get_selection`, `get_node_info`, `get_children`, `get_tree_summary`, `find_nodes`, `list_files` | yes, except `find_nodes` and `list_files` | [S-L16-009] [S-L16-000] [S-L16-020] |
| **Read: visuals and code** | `get_screenshot` (1x or 2x), `get_jsx` (Tailwind or inline styles), `get_computed_styles` (batch CSS), `get_fill_image`, `get_font_family_info`, `get_tokens` | yes, except `get_tokens` | [S-L16-009] [S-L16-020] |
| **Read: guidance and comments** | `get_guide` (e.g. `figma-import`, `paper-mcp-instructions`), `list_comment_threads`, `get_comment_thread`, `list_comment_thread_authors` | `get_guide` only | [S-L16-009] [S-L16-020] |
| **Export** | `export` (PNG, JPG, SVG, MP4 with per-node scale), `export_combined_pdf` | `export` only | [S-L16-009] [S-L16-020] |
| **Write: files and pages** | `create_file`, `create_page`, `open_file`, `create_artboard` | `create_artboard` only | [S-L16-009] [S-L16-020] [S-L16-014] |
| **Write: content** | `write_html` (parse HTML into nodes; insert-children or replace), `update_styles` (CSS on many nodes), `set_text_content`, `rename_nodes`, `duplicate_nodes`, `move_nodes` (reorder or reparent, ids preserved), `delete_nodes` | yes | [S-L16-009] |
| **Write: tokens** | `create_tokens`, `set_tokens` | no (the build log says tokens can be added "using the MCP" since June 2026) | [S-L16-020] [S-L16-014] [S-L16-018] |
| **Write: comments and session** | `set_comment_thread_status`, `finish_working_on_nodes` (clears the on-canvas working indicator) | `finish_working_on_nodes` only | [S-L16-009] [S-L16-020] |

The live server exposes **34 tools**, 13 more than the 21 documented; the docs lag the build log [S-L16-020] [S-L16-009] [S-L16-014].

### B3. The documented way to connect Paper to Claude Code
1. Install **Paper Desktop** and open a file; the server starts in the background at `http://127.0.0.1:29979/mcp` [S-L16-009].
2. Recommended: add Paper's plugin marketplace and install the plugin: `/plugin marketplace add paper-design/agent-plugins`, then `/plugin install paper-desktop@paper` [S-L16-009].
3. Manual alternative (the one used on this machine): `claude mcp add paper --transport http http://127.0.0.1:29979/mcp --scope user` [S-L16-009] [S-L16-000].
4. Verify: ask the agent to "create a red rectangle in Paper" [S-L16-009]. Paper's server instructions also require the agent to load `get_guide({topic: "paper-mcp-instructions"})` first, to call `get_font_family_info` before styling type, and to call `finish_working_on_nodes` when done (session MCP instructions, observed 2026-09-23) [S-L16-020].
5. Troubleshooting: restart long agent sessions. On WSL, use mirrored networking [S-L16-009].

### B4. Paper tokens and round trip
- Tokens are "also known as CSS variables" and map directly onto Tailwind. Supported types are color, radius, spacing, container, breakpoint, font family, font weight, font size, line height and letter spacing [S-L16-018].
- Tokens can be created three ways: in the Theme tab; through MCP from a design on the canvas; or through MCP **from a codebase's CSS variables** [S-L16-018].
- **No theme modes yet.** Multiple modes (dark, compact) and grouped "theme classes" are on the roadmap. There are **no shared libraries yet**: tokens are copied and pasted between files and do not update across files [S-L16-018].
- Paper's docs do not mention DTCG [S-L16-018]. The builder would therefore translate DTCG into CSS variables for Paper [inferred].
- The roadmap lists "use your code components" (in progress), native Tailwind (in progress, with the Tailwind team), components with props and slots (coming soon), a Base UI component kit (coming soon), and "Right click → Remix" for "fast variations, font pairings, and color scales" (planned) [S-L16-016].
- Figma to Paper: via Figma copy-paste (May 2026) or an agent using both MCPs. Known losses: SVG fills arrive as images, spacer elements are ignored, inset borders are not converted, and Code Connect components do not carry over reliably [S-L16-014] [S-L16-009].

### B5. Why Paper matters for this builder [inferred from B1-B4]
- It is currently the only mainstream canvas whose agent write path is **HTML/CSS in, HTML/CSS out** (`write_html`, `update_styles`, `get_jsx`, `get_computed_styles`). An engineer-facing builder that renders CSS tokens can therefore push specimens and component sheets to a canvas without a translation layer.
- Its weaknesses are exactly where a design-system builder is strong: no modes, no libraries, and no DTCG. Paper is a good **write target and visual review surface**, not a system of record.
- Caveats: the MCP needs the desktop app running (local only), and the free plan's 100 calls a week is tight for token syncs [S-L16-009] [S-L16-010].

---
## Part C. Tool-by-tool review: interaction model and round trip (verified 2026-09-23)

Vendor descriptions of "what feels good" are vendor claims unless a row says otherwise. L11 Part G reviews many of the same products as design-system competitors; this part covers how they are operated and how design and code move between them.

### C1. Code-native visual editors and design tools

| Tool | Target user | Interaction model | Source of truth | Round trip | Tokens and components | AI / MCP (read vs write) | What feels good | Gaps for engineers | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| **Figma** | Designers; engineers through Dev Mode and MCP | See Part A | Figma file | See Part A | L07 A6 | See A1 | Multiplayer canvas; agent plus direct manipulation | Write needs remote MCP and a Full seat | Part A |
| **Paper** | Design teams shipping with agents; engineers through MCP | See Part B | Paper file (HTML/CSS) | See Part B | CSS-variable tokens; no modes or libraries yet | See B2 | Canvas is HTML/CSS | Desktop app must run; no modes | Part B |
| **Penpot** | Product designers and DS teams wanting open source and self-hosting | Browser canvas with CSS Grid and Flex, components and variants, Tokens panel, Inspect code tab; agents via MCP | Penpot file | Design to code: Inspect gives HTML/SVG + CSS. Code to design: MCP agents create and modify elements, tokens and components | **Native DTCG tokens** (import and export without conversion), sets, multidimensional themes, math; `$` keys since 2.17.0 (22 Jul 2026) | MCP (remote or `npx @penpot/mcp`): `execute_code` (Plugin API, read and write), `high_level_overview`, `penpot_api_info`, `export_shape`, `import_image`; needs the plugin open in a browser tab; focused page only | Open standards; token pills in numeric fields | No React export; MCP bound to one open tab; plugin tokens API "coming soon" | [S-L16-111] [S-L16-112] [S-L16-113] [S-L16-114] [S-L16-117] |
| **Framer** | Website teams; engineers secondary | Canvas with breakpoints; in-canvas Agents ("Cursor for design", Framer 3.0, 16 Jun 2026); External Agents from a terminal | Hosted Framer project | Code components live inside Framer; React export only through a paid third-party plugin; no git sync; every external-agent change lands on a Framer branch | Color styles (light plus optional dark) and text styles; no DTCG or CSS-variable export found | **Official:** `npx @framer/agent setup` (skills + CLI on the Server API; "doesn't require a separate MCP server"). **This machine's Framer MCP is third-party** (Unframer; "This is not an official Framer plugin"): reads project XML, code files, CMS; writes nodes (`updateXmlForNode`), pages, color and text styles, code files, CMS | Live light/dark toggle on canvas; branch per agent change | Proprietary styles; no repo round trip | [S-L16-100] [S-L16-102] [S-L16-104] [S-L16-106] [S-L16-107] [S-L16-109] [S-L16-110] |
| **Webflow** | Marketing-site teams; front-end devs via DevLink and code components | Visual Designer (classes, breakpoints, variables panel, components with props, variants, slots); agents via MCP | Hosted Webflow site | React components in via DevLink/code components (Shadow DOM); Webflow components out as React (paid) | **Variables** (color, font family, number, percentage, size) in collections with **modes** (can tie to breakpoints); exposed as CSS custom properties; DTCG not documented | Official remote MCP (`mcp.webflow.com/mcp`, OAuth, owners/admins authorize), each tool labelled read or write: `data_variable_tool` (create/update/rename/delete variables, collections, modes), `data_style_tool`, `data_component_tool`, props and variants tools; Designer-session tools need a Bridge App; activity log | The most complete token **write** surface found (variables + modes + style bindings); "Variables Refactor" prompt recipe | Hosted, proprietary source of truth; React round trip paid and not git-based | [S-L16-152] [S-L16-153] [S-L16-154] [S-L16-156] [S-L16-158] [S-L16-159] |
| **Subframe** | Product engineers on React + Tailwind | Infinite canvas on HTML/CSS primitives (stacks, variants, states, breakpoints); built-in browser that previews the local app with visual Inspect edits and "capture as design"; agent panel | Subframe ("single source of truth"); CLI pushes components and theme into the repo | CLI `sync` is one-way (overwrites local edits unless opted out); code to design by capturing a live page, theme import, importing React components (Custom plan) | Theme tokens (colors, type, borders, corners, shadows), multiple themes; imports Tailwind v3/v4, CSS variables, DTCG (**colors only**); exports **Tailwind only** | Remote MCP (`mcp.subframe.com/mcp`, OAuth) + Claude Code plugin with 3 skills. Read: projects, pages (returns React + Tailwind), components, screenshots, theme. Write: `design_page`, `edit_page`, `update_node_styles`, `design_component`, `edit_component`, `edit_theme`, and more; **viewers read-only** | Designing with web primitives means the design is already code | One-way sync; Tailwind-only export; React/Tailwind/Radix lock-in | [S-L16-141] [S-L16-142] [S-L16-143] [S-L16-144] [S-L16-145] [S-L16-146] [S-L16-147] |
| **Onlook** | Designers working inside a React codebase | Figma-like editor over a live iframe of the running app; Tailwind toolbar, layers, side-by-side code, AI chat | Code (Next.js + Tailwind) | Two-way by construction: DOM edits map back to source locations; branches and checkpoints | "Manage brand assets and tokens" shipped; format not documented | No MCP (on the roadmap) | Canvas is the code | Next.js + Tailwind only; OSS releases stopped at v0.2.32 (17 Jul 2025) as the company moves to a hosted product | [S-L16-149] [S-L16-150] [S-L16-151] |
| **Builder.io** (Visual Copilot; Fusion renamed **Builder Code** on 10 Sep 2026) | Cross-functional teams on an existing codebase | "Visual IDE": prompt agent plus a Figma-like visual editor over a live preview of the real app; multiplayer; Figma plugin; VS Code extension | The customer's git repo (changes arrive as PRs) | Strongest git round trip found: push a branch, others edit visually, Builder commits back, engineer reviews the diff; Figma to code via Visual Copilot | "Design system intelligence" indexes components and tokens from repos, npm or Figma (Enterprise); **Style Strict Mode** limits visual edits to tokens | Three MCP servers (CMS, Code, local), described but without published tool identifiers; local MCP writes files and pushes branches (Enterprise) | "Push your branch, let your team take over" (vendor framing) | DS intelligence Enterprise-only; credits; frequent renames | [S-L16-129] [S-L16-130] [S-L16-131] [S-L16-132] [S-L16-134] [S-L16-135] [S-L16-136] [S-L16-138] [S-L16-139] [S-L16-140] |
| **Plasmic** | React teams where non-developers build pages | Plasmic Studio canvas (components, variants, breakpoints, tokens), can run inside your app host | Plasmic project; consumed at runtime or via codegen | Code components and tokens registered from the app host; output via loader or `plasmic sync` | Tokens as CSS custom properties; codegen exports Salesforce **Theo** JSON, not DTCG | No first-party MCP; Chrome DevTools MCP drives Studio via a browser-side API and a `plasmic-designer` skill ("early stage", 27 May 2026) | Studio renders your real components with real data | Browser-automation agent path is fragile [inferred]; Theo export | [S-L16-161] [S-L16-162] [S-L16-163] [S-L16-164] [S-L16-165] |
| **Storybook** (incl. `@storybook/addon-mcp`) | Front-end and DS engineers | Stories in code plus a browser workshop (Controls, Docs); agents via MCP | Component code and stories; a generated components manifest | Code to docs and preview only | Real framework components; no token management | MCP at `localhost:6006/mcp` (10.6.0, 2 Sep 2026; AI features "in preview"). Read: `stories-changed`, `stories-find-by-component`, `stories-preview` (live previews in chat via MCP Apps), `docs-list`, `docs-show`, `docs-show-story`. Run: `test-run` (incl. accessibility). "Write-ish": `review-create`. The agent writes files itself | Self-healing loop: agent writes a story, previews it, runs tests, fixes | No visual editing or token authoring | [S-L16-118] [S-L16-120] [S-L16-121] [S-L16-122] [S-L16-124] [S-L16-125] |
| **Chromatic** | FE and DS teams doing visual and accessibility testing | CI-triggered snapshots; web UI Review of diffs; PR checks | Git repo + Storybook; baselines per branch | Visual diffs gate PRs | Consumes whatever Storybook renders | Auto-publishes the Storybook MCP with each build at `<storybook-url>/mcp` (docs tools only, read-only) | TurboSnap tests only affected stories | Snapshot-priced (Free 5,000/month; Starter $179; Pro $399) | [S-L16-126] [S-L16-128] |
| **UXPin Merge** (+ Forge AI, Wire) | Enterprise DS teams prototyping with production components | Drag-and-drop canvas of real React components with a props panel; Forge prompt generation (launched 11 Feb 2026) | The code component library (Git, Storybook, npm) | Code to design via Merge sync (CLI or CI); design to code as JSX using the same components | Real components; native token management listed as "Soon" | No MCP server found | Designers cannot drift from code | No MCP; tokens not first-class | [S-L16-166] [S-L16-167] [S-L16-168] [S-L16-169] |

### C2. AI builders and agent canvases (interaction and round trip; L11 Part G covers their design-system inputs)

| Tool | Target user | Interaction model | Source of truth | Round trip | Tokens and components | AI / MCP (read vs write) | What feels good | Gaps for engineers | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| **v0** (Vercel) | Developers shipping Next.js to Vercel | Chat + live preview. **Design mode**: select an element, tune type, color, spacing, radius, shadow in a panel; pending edits with undo, redo, reset and a before/after toggle; **Apply creates a new diffable version** | The GitHub repo once connected | Branch per chat, PRs, pull from base. Figma in (variables, styles, auto layout; paid plans) and **Paper links in** (1 Sep 2026). No export to Figma | Tailwind values surfaced "where appropriate" | Ships `v0.app/api/mcp` (OAuth) to create and manage chats; consumes MCP | At launch (12 Jun 2025), design-mode edits cost no credits and needed no LLM round trip (vendor claim) | Design mode only on the latest preview and version | [S-L16-242] [S-L16-243] [S-L16-244] |
| **Lovable** | Non-engineers and teams building apps by prompt | Chat + preview. On 10 Jun 2026 the property-panel Visual Edits were **replaced** by Select-then-describe (credits), inline text edit, draw annotations and comments. Three rendered directions before the first build | Lovable project, two-way synced to one git branch | Git two-way sync (GitHub, GitLab, Bitbucket). Figma in (plugin, MCP, .fig). No code to Figma found | Themes (Nov 2025); design systems on paid plans (Aug 2026) | Ships `mcp.lovable.dev` on all plans, scoped to the whole account | Pointing and drawing beat describing (vendor) | Most visual edits now go through the model and cost credits [inferred from S-L16-246] | [S-L16-245] [S-L16-246] [S-L16-247] [S-L16-248] [S-L16-249] [S-L16-250] [S-L16-251] |
| **Bolt** | Builders creating web apps by prompt | Chat + preview. Select tool with hover, arrow keys to walk the DOM tree, a contextual toolbar showing only valid properties; **edits batch above the chat; editing is free, tokens are spent only on "Save changes"** | Bolt project, optionally GitHub | GitHub auto-sync. Figma in (via Anima) and Stitch in. No code to Figma found | Design-system agent reuses DS components only on Screenshot import; Storybook view | Consumes MCP; no Bolt-hosted MCP found | A clear cost model: free tweaks, pay once on save [inferred] | Figma "Code" import is not DS-aware | [S-L16-252] [S-L16-253] [S-L16-254] [S-L16-255] [S-L16-256] [S-L16-257] [S-L16-258] |
| **Magic Patterns** | Product teams prototyping with their real DS | Prompt + multiplayer canvas; Visual Edit for direct element edits; **Controls panel (sliders) for 2-3 structural decisions**, local until "Make defaults" writes them into a prompt; an inspiration skill giving four bold directions on a comparison link; plan mode, fork, merge | Magic Patterns artifacts (React + Vite) and **immutable DS versions** | Manual two-way GitHub sync into a new repo; Figma export is a static clipboard snapshot; Figma import | Color, spacing, typography tokens; DS edits persist to all designs | Ships MCP (paid): `create_design`, `read/write_artifact_files`, `list/create/get_design_system`, `read/write_design_system_files`, `publish_design_system`, inspiration tools | Controls turn "regenerate and wait" into instant local exploration (vendor guidance) | Sync creates a new repo instead of attaching to an existing one | [S-L16-235] [S-L16-236] [S-L16-237] [S-L16-238] [S-L16-239] [S-L16-240] [S-L16-241] |
| **Google Stitch** | Designers exploring variations; founders | AI-native infinite canvas (18 Mar 2026); project-wide agent and parallel agents; voice ("give me three different menu options"); streaming generation you can steer mid-way (May 2026). SDK variants: 1-5 per call, `creativeRange` REFINE / EXPLORE / REIMAGINE, `aspects` LAYOUT / COLOR_SCHEME / IMAGES / TEXT_FONT / TEXT_CONTENT | Stitch project; rules portable as DESIGN.md | Out: Paste to Figma, HTML/CSS, AI Studio, Bolt. In: codebases and design files; DS extraction from a URL | Design systems (fonts, colors, button styles); DESIGN.md spec | Ships `stitch.googleapis.com/mcp` (API key or OAuth) with `create_project`, `generate_screen_from_text`, `get_screen`; SDK | "Diverge and converge" (vendor) | Output is HTML/CSS screens, not a component library; docs are JavaScript-only | [S-L16-256] [S-L16-259] [S-L16-260] [S-L16-261] [S-L16-262] [S-L16-263] [S-L16-264] [S-L16-265] |
| **Claude Design** (Anthropic Labs) | Designers exploring; founders, PMs, marketers | Conversation beside a canvas; inline comments; direct edits (a new editor with drag, resize, align, June 2026); **"adjustment sliders Claude creates to tune spacing and color"**; since Sep 2026 inside any Claude conversation and Claude Code (`/design`; beta, paid plans only, off by default on Enterprise [S-V1a-003]) | Design project plus an org DS built from code and design files | In: codebase, GitHub, design files, web capture. Out: handoff bundle to Claude Code, `/design-sync` from local code, PDF, PPTX, HTML, Canva and connectors; no Figma export named | Builds with real DS components and self-checks against the DS | No public MCP tool list found | Model-generated sliders scoped to the current design | Comments can vanish before Claude reads them (known issue); no token export format documented | [S-L16-266] [S-L16-267] [S-L16-268] [S-L16-269] |
| **pen.dev** (formerly Pencil) | Engineers and design engineers in the repo | WebGL canvas with Figma-like shortcuts, symbols with overrides; **Script nodes whose `@input` lines become property-panel controls** that re-run the script live; browser import | **`.pen` JSON files committed next to code**; text diffs, branch and merge with code | Two-way through the agent (recreate a component from `src/…`, export HTML/Tailwind); CSS variables to and from pen variables | Typed variables (color, number, string, boolean), theme columns and extra theme axes with inheritance; components with overrides | Local MCP: `get_style`, `read_skill`, `get_app_state`, `execute`, `browser`, `spawn_agents`; currently free | Script-driven parametric components are unusually engineer-native [inferred] | `.pen` format may break between versions; sync is agent-mediated, not deterministic | [S-L16-271] [S-L16-272] [S-L16-273] [S-L16-274] [S-L16-275] [S-L16-276] [S-L16-277] [S-L16-278] [S-L16-279] |
| **Tempo** (Tempo Labs) | Product teams on a real repo in one desktop app | Figma-style canvas where **every frame is a live iframe of a route or React component**; a Style Panel that writes to source; drag repo components; chat agents in isolated worktrees | **Code**: storyboards are typed React exports in `index.canvas.tsx`, committed | Canvas edits write code; **visual review pixel-diffs tracked storyboards on every PR** and blocks until a human approves | Repo components; canvas Variables (Sep 2026) | Ships `@tempo-ai/mcp` (stdio) and a hosted MCP | "Your designs are your code" (vendor) | GitHub Actions only; storyboards must render deterministically | [S-L16-298] [S-L16-299] [S-L16-400] [S-L16-401] [S-L16-402] |
| **Kombai** | Front-end developers in IDEs | Agent modes; infinite canvases with parallel agents; **one-click variation verbs** (Surprise me, Rearrange layout, Simplify, Enrich, Fix hierarchy, Adjust density); select, snip-to-chat, edit, draw, comment | Repo (canvases stored in project folders) | Figma to code natively; reuses existing UI through "Context Graphs" | Indexes components, hooks and tokens from workspace, npm or Storybook | Local MCP that auto-configures many clients and installs skills | Named design decisions surfaced per task (vendor) | Vendor benchmarks only | [S-L16-295] [S-L16-296] |
| **Polymet** | Product teams wanting pages plus front-end code | Prompt + canvas and focus mode; variations; visual editor with per-side spacing, drag-to-adjust values, a Theme tab, a layers panel that labels repeated items ("2 of 5") | Polymet project with git history | Figma in (up to 8 frames) and out (Export ID); export repo; MCP hands a canvas link to a coding agent and pulls code back | Theme editor (palettes, type, tokens); token extraction from a URL | Ships `polymet.ai/api/mcp` | Thoughtful layer details [inferred] | No MCP tool list published | [S-L16-405] [S-L16-406] [S-L16-407] |
| **tldraw** | Developers embedding canvases; people working with local agents | Infinite canvas SDK; agent starter kit; multi-agent "Fairies"; comments as the agent channel (SDK 5.3); **MCP App** (a live canvas inside the chat, 3 Mar 2026); tldraw offline (agents write JavaScript against the live editor, 16 Jul 2026) | tldraw document / `.tldraw` file | Not a design-to-code tool; "make real" (sketch to HTML) is archived | Canvas themes only | MCP App tools create, edit and delete shapes | Canvas makes multi-agent work legible (vendor) | No bridge to tokens or components; SDK needs a paid license key in production | [S-L16-200] [S-L16-201] [S-L16-202] [S-L16-203] [S-L16-204] [S-L16-205] [S-L16-206] [S-L16-207] [S-L16-209] [S-L16-210] [S-L16-211] |
| **Superdesign** | Developers and designers inside coding agents | Skill + CLI; infinite canvas of **branchable drafts** | superdesign.dev projects | Reads the codebase; drafts refined, then implemented | Sets up design systems (details not verified) | Skill for 70+ agents; Claude Code plugin in the official marketplace | Branching as the exploration primitive | Not verified beyond README | [S-L16-037] [S-L16-040] |
| **Variant** | Anyone starting a UI from zero | Type an idea, scroll an endless feed of full designs; "Style Dropper" copies one design's style to another | Generated designs | HTML or React export per press only | not verifiable | not verifiable | "Exploration at the speed of scrolling" (press opinion) | Vendor docs behind sign-in | [S-L16-403] [S-L16-404] |

### C3. Figma <-> code bridges and plugins

| Tool | Direction | How | Tokens and components | MCP | Gaps | Evidence |
|---|---|---|---|---|---|---|
| **Figma code to canvas** (`generate_figma_design`; Chrome extension; copy from Make) | code to design | Capture toolbar on the running app; Claude Code support from 17 Feb 2026, VS Code/Copilot from 6 Mar 2026 | Auto-binds color, number and string variables by code syntax, then name, then scope | Remote MCP | Flat layers, no components | [S-L16-003] [S-L16-024] [S-L16-214] [S-L16-219] |
| **html.to.design** (divRIOTS) | code to design | Figma plugin (URL, pasted HTML, zip) and a Chrome extension for logged-in pages; viewport and theme chosen before import | Creates text and color local styles; "components with all variants"; auto layout; light and dark | Remote MCP `mcp.to.design` (`import-html`, `import-url`), relayed through the open Figma plugin | One-way; free-tier count conflicts between its own pages | [S-L16-220] [S-L16-221] [S-L16-222] [S-L16-223] [S-L16-224] [S-L16-225] |
| **Anima** | both | Figma plugin, Playground (each artifact is a real git repo), "Copy to Figma" | Figma DS import creates a live Storybook from variables and components | Remote MCP (`artifact-create`, `codegen-figma_to_code`, `artifact-publish` and more); DS publish over MCP needs Enterprise | Generated file sets are filtered, so the agent must merge | [S-L16-226] [S-L16-227] [S-L16-228] [S-L16-229] |
| **Locofy** | design to code | Figma or Penpot plugin, CLI, MCP | Honours "use tokens from src/tokens.ts"-style instructions | `@locofy/mcp` (`convertDesignToCode`, `getLatestComponentAndDependencyCode` and more) | No code-to-design path | [S-L16-230] [S-L16-232] |
| **Builder.io Figma plugin** (Visual Copilot) | both | Figma to React/Vue/Tailwind; export from a Builder project back into Figma | not stated | none on the page | brief review only | [S-L16-234] (and H1 rows in C1) |
| **Figma Make to GitHub** | design to code | One-way push to a repo Make created; default branch only | n/a | n/a | GitHub edits are overwritten on the next push | [S-L16-282] |

### C4. Cross-tool patterns [inferred from the rows cited]
- **Three source-of-truth models.**
  - The tool's own file is canonical and code is exported: Figma, Framer, Webflow, Penpot, Plasmic, Subframe, Paper [S-L16-143] [S-L16-163] [S-L16-113] [S-L16-018].
  - The repo is canonical and the visual layer edits it: Builder.io (PRs), Onlook (DOM mapped to source), Tempo (storyboards in git), UXPin Merge (renders synced components), v0 (repo as source of truth once connected) [S-L16-135] [S-L16-149] [S-L16-299] [S-L16-169] [S-L16-242].
  - The repo is canonical and the tool documents or tests it: Storybook, Chromatic [S-L16-122] [S-L16-126].
  - A design file lives in the repo: pen.dev `.pen` JSON [S-L16-272].
  - **No tool found does deterministic two-way sync of tokens between a canvas file and a git repo.** Two-way flows go through an agent (pen.dev, Paper) or through git (Lovable, Magic Patterns manual sync) [S-L16-273] [S-L16-012] [S-L16-249] [S-L16-239].
- **Token portability is weak.** Only Penpot imports and exports DTCG natively [S-L16-113]. Subframe imports DTCG colors only and exports Tailwind [S-L16-144] [S-L16-145]. Plasmic exports Theo JSON [S-L16-163]. Webflow and Framer keep proprietary variables and styles [S-L16-153] [S-L16-109]. Paper uses CSS variables with no modes [S-L16-018]. UXPin lists tokens as "Soon" [S-L16-168].
- **Direct manipulation has converged on one pattern.** Select an element in a live preview, edit a scoped property panel, batch the edits, then commit them as a reviewable change. Examples: v0 Apply creates a new version; Bolt batches edits and charges only on save; Figma Make stages edits until Apply; Subframe's change tray; Tempo's Style Panel writes to source [S-L16-242] [S-L16-253] [S-L16-026] [S-L16-293] [S-L16-299]. Lovable went the other way, replacing its panel with select-and-describe [S-L16-246].
- **"Show me N" is a first-class primitive.** Stitch variants with `creativeRange` and `aspects`; Magic Patterns' four directions; Lovable's three directions; Kombai's variation verbs; the Figma agent's parallel prompts; Superdesign's branchable drafts; Variant's endless feed [S-L16-264] [S-L16-237] [S-L16-251] [S-L16-295] [S-L16-031] [S-L16-040] [S-L16-404].
- **Generated controls are the new slider.** Claude Design builds sliders for the current design; Magic Patterns Controls; pen.dev `@input` script controls; Figma parameterized shaders; Framer property controls on generated components [S-L16-269] [S-L16-238] [S-L16-275] [S-L16-281] [S-L16-283].
- **MCP write surfaces differ in shape.**
  - Typed tools labelled read or write: Webflow, Subframe, Paper, Magic Patterns [S-L16-153] [S-L16-142] [S-L16-009] [S-L16-237].
  - Code execution against a plugin API: Figma `use_figma`, Penpot `execute_code`, pen.dev `execute`, Framer's official CLI [S-L16-002] [S-L16-111] [S-L16-276] [S-L16-102].
  - Read plus test only: Storybook, Chromatic [S-L16-120] [S-L16-126].
  - Browser automation: Plasmic [S-L16-161].
  - None: Onlook, UXPin [S-L16-149] [S-L16-168].
  - Write access is gated by seat (Figma Full seat; Subframe editors; Webflow owners and admins authorize) or by quota (Paper Free 100 calls a week) [S-L16-002] [S-L16-142] [S-L16-154] [S-L16-010].
- **Skills ship next to (or instead of) MCP.** Figma, Framer ("doesn't require a separate MCP server"), Subframe, Webflow, Plasmic, Kombai and Superdesign all ship agent skills [S-L16-038] [S-L16-102] [S-L16-142] [S-L16-154] [S-L16-161] [S-L16-296] [S-L16-040].
- **Safety patterns worth copying.** A branch per agent change (Framer); an activity log plus roles (Webflow); `dry_run` on destructive actions (Webflow); read-only MCP for viewers (Subframe); pixel-diff visual review that blocks a PR (Tempo, Chromatic); immutable DS versions (Magic Patterns) [S-L16-102] [S-L16-154] [S-L16-153] [S-L16-142] [S-L16-400] [S-L16-128] [S-L16-237].
- **Tool names churn.** Storybook renamed its docs tools within 2026; Webflow publishes a "Skill Migration" page; Builder renamed Fusion to Builder Code on 10 Sep 2026; Paper's docs list 21 tools while its server exposes 34 [S-L16-174] [S-L16-152] [S-L16-140] [S-L16-020]. Integrations must pin versions and re-check tool lists at runtime [inferred].

---

## Part D. Theme and foundation playgrounds engineers already use (interaction model)

L11 Part G lists their inputs and outputs. This table covers how they are operated [S-L16-300 to S-L16-350, S-L16-390 as cited].

| Tool | Controls | Preview | Feedback, undo, share | Export | Feel / gaps | Status | Evidence |
|---|---|---|---|---|---|---|---|
| **Material Theme Builder** (web + Figma plugin) | Source image or core colors; HCT picker; **Shuffle** (no locks); extended colors with harmonize; fonts | Web sample UI; in Figma, your own design with live Swap and a sun/moon light/dark toggle | An explicit **Update** press after color changes; no documented undo or share URL | Android Views XML, Compose, DSP tokens (2021); JSON between web and Figma | Correct M3 role mapping. No M3 Expressive tokens (issue open since Jun 2025). **Repo archived 23 Jul 2026**, no successor named, web app still served | archived | [S-L16-300] [S-L16-316] [S-L16-317] [S-L16-318] [S-L16-319] [S-L16-324] [S-L16-389] |
| **Radix Themes playground + ThemePanel** | Floating panel toggled with **T**: accent, gray, appearance, radius, scaling, panel background | Every component as a variant-by-color matrix | No undo or share in the panel source | "Copy Theme" writes `<Theme …>` JSX with only non-default props | Curated choices make broken results hard; a shippable dev overlay | Themes 3.3.0 (31 Jan 2026) | [S-L16-302] [S-L16-322] [S-L16-323] |
| **Radix Colors custom palette** | Accent, Gray, Background (any CSS color incl. P3) + a light/dark switch | 12 steps labelled by job, beside real Radix components | URL generated on demand (`accent-light`, …) plus a 2-hour cookie | CSS (steps, alpha, P3, surface), SVG, URL | Three inputs yield a whole system and teach step roles | folder commits Jun 2026 | [S-L16-320] [S-L16-321] |
| **shadcn create** (and typeset) | Pickers with a **Lock** each; **Shuffle** (button or **R**) with curated biases; Cmd+Z/Shift+Z | Real components in sample screens | `?preset=<code>` updates live; the CLI can decode, resolve, url and open presets | `shadcn init --preset`, `shadcn apply --preset` (full, theme only, fonts only), globals.css | The preset code is a seed that moves between browser, URL, CLI and repo. Typeset reuses the pattern for type and adds a "Prompt" tab for agents | CLI 4.21.0 (4 Sep 2026) | [S-L16-305] [S-L16-326] [S-L16-327] [S-L16-328] [S-L16-331] [S-L16-390] |
| **tweakcn** | ~46 controls: 32 color tokens (hex or Tailwind names), 3 font pickers, letter spacing and 10 sliders [S-V1a-067]; an AI Generate tab (text or image) | Real shadcn components in 5 contexts | **Undo stack of 30 entries; edits within 500 ms coalesce**; checkpoints; share | Tailwind v3/v4 CSS; `npx shadcn add https://tweakcn.com/r/themes/<id>`; Figma via a third-party kit | Full control; the flat list of ~46 fields is the cost; WCAG AA checker | commits to 3 Sep 2026 | [S-L16-306] [S-L16-332] [S-L16-333] |
| **Realtime Colors** | 5 roles + 2 fonts; **Spacebar** randomizes; lock up to 4 | A full sample landing page, recolored in place | Cmd+Z/Y or arrows; **the URL always mirrors state**; Cmd+S copies it; QR to phone | Cmd+E: CSS, Tailwind, SCSS, OKLCH and more; Figma plugin reads the share URL | The fastest keyboard loop; only 5 colors, HSL randomizer; repo dormant since Oct 2023 | docs 2023 | [S-L16-312] [S-L16-334] [S-L16-335] |
| **Adobe Leonardo** | Global Brightness/Contrast/Saturation sliders; **target contrast ratios per step**; WCAG 2 or APCA; interpolation space | Chromaticity, lightness, 3D and wheel charts; analysis panel | Share URL `?name=&config=` | CSS, parameters, tokens with `$value`/`$type`; **`@adobe/leonardo-mcp` `generate-theme`** (Feb 2026) | Outcome-first color; steep learning curve | repo active Jul 2026 | [S-L16-307] [S-L16-336] [S-L16-337] [S-L16-338] |
| **Huetone** | Hue-by-tone grid; numeric L/C/H; **keyboard-first** (arrows, L/C/H nudges, duplicate rows) | Per-cell APCA or WCAG contrast; LCH charts; hold **B** for greyscale | Copy link | Figma Tokens JSON, CSS variables | The most spreadsheet-like, engineer-native tool; no component preview; dormant since Nov 2023 | dormant | [S-L16-308] [S-L16-339] [S-L16-340] |
| **Utopia** | Two "keyframes" (min and max viewport: width, base size, ratio); space multipliers and pairs | Table, graph, visualiser; value at any width | Config URL; **generated CSS starts with an `@link` back to the tool** | CSS, SCSS, PostCSS (clamp or locks); `utopia-core` on npm | Scales as functions of viewport; no component preview | core 1.6.0 (Sep 2024) | [S-L16-341] [S-L16-342] [S-L16-343] |
| **Typescale.com** | Base size + ratio; responsive breakpoint | Templates, mobile/desktop | account boards | CSS export is Pro-gated | no owner or date found | unknown | [S-L16-344] |
| **Tailwind v4 palette / uicolors.app / tints.dev** | Tailwind: 26 families x 11 OKLCH stops set via `@theme`, no official generator. uicolors: lock per stop, Spacebar random. tints.dev: hue shift, saturation shift, lightness distribution curves with nudges | uicolors: shadcn and dashboard previews (many Pro) | URL state (uicolors path; tints.dev base64); tints.dev public API | Tailwind 3/4, CSS, W3C tokens (uicolors, paid) | tints.dev comes closest to "handles on curves" | Tailwind v4.3.3 (16 Jul 2026) | [S-L16-311] [S-L16-315] [S-L16-345] [S-L16-346] [S-L16-347] |
| **oklch.com / Harmonizer** (Evil Martians) | oklch.com: L/C/H/A with gamut slice charts. Harmonizer: hue-by-level grid where **each level holds an APCA target** and a chroma; a drag handle sets where light mode starts | gamut views; both backgrounds in one view | URL hash | Tailwind, CSS variables, JSON; a Figma plugin creates variables | Contrast as a column property, so swapped colors keep text contrast | repos active Aug-Sep 2026 | [S-L16-309] [S-L16-310] [S-L16-348] [S-L16-349] [S-L16-350] |

**Patterns across the playgrounds** [inferred from the rows above]:
- **Lock + Shuffle + seed** is now standard (shadcn, Realtime Colors, uicolors; MTB shuffles without locks).
- **The URL is the save file** (Realtime Colors, tints.dev, oklch.com, Harmonizer, shadcn presets, Utopia, Leonardo). Some tools also make the code point back to the tool: Utopia's `@link`, shadcn `preset open`, and the Realtime Colors Figma plugin.
- **Outcome-specified color** (contrast targets): Leonardo, Harmonizer, Huetone.
- **Previews on real components**: Radix, shadcn, tweakcn, uicolors.
- **Export by CLI or registry URL**: shadcn, tweakcn.
- **Missing everywhere**: before/after diffs of a theme edit, branches, multi-user editing, and light and dark side by side (most tools toggle). None of the 16 tools H3 examined has review or branching [S-L16-390] [S-L16-333] [S-L16-387].

---

## Part E. Principles for creative tools that serve engineers (originals cited)

| Principle | Original source | What it says (paraphrase) | What it implies for the builder [inferred] | Evidence |
|---|---|---|---|---|
| Immediate connection | Bret Victor, "Inventing on Principle", CUSEC talk, 20 Jan 2012 | "Creators need an immediate connection to what they create": no compile-and-look gap | Every token edit re-renders real components in the same frame; numbers are scrubbable | [S-L16-355] [S-L16-356] [S-L16-358] |
| Learnable environments | Bret Victor, "Learnable Programming", Sep 2012 | Read the vocabulary, follow the flow, see the state, create by reacting, create by abstracting | Hover a token to see its meaning and usage; trace primitive to alias to component; start from a working preset; restyle one button, then promote the change to a token | [S-L16-353] |
| Explorable explanations | Bret Victor, "Explorable Explanations", 10 Mar 2011 | Reactive documents let readers change assumptions and see consequences | The generated docs site is itself explorable (drag the ratio in the docs) | [S-L16-354] |
| Direct manipulation | Ben Shneiderman, IEEE Computer 16(8), Aug 1983 (paywalled; cited via NN/g restatement) | Visible objects; physical actions instead of syntax; rapid, incremental, reversible actions with immediate feedback | Tokens as objects you grab; curves with handles; every operation small and undoable | [S-L16-359] [S-L16-363] [S-L16-364] |
| Gulfs of execution and evaluation | Hutchins, Hollan and Norman, "Direct Manipulation Interfaces", HCI 1(4), 1985 | Directness comes from shrinking the distance between intention and the system | Let engineers state intent ("text on primary passes AA") and compute values (the Leonardo and Harmonizer model) | [S-L16-366] |
| Response time | Doherty and Thadani, IBM, Nov 1982 | Productivity rose steeply as response time fell from 3.0 s to 0.3 s; sub-second response let novices perform like experts. "400 ms" is a later restatement | A hard latency budget; slow work asynchronous and non-blocking | [S-L16-368] [S-L16-369] [S-L16-370] |
| Multiplayer | Evan Wallace, "How Figma's multiplayer technology works", 16 Oct 2019 | Central server, last-writer-wins per object property; undo must not clobber others | Model the system as objects with properties; sync per property | [S-L16-372] |
| Local-first | Kleppmann et al., Ink & Switch, Apr 2019 (Onward! 2019) | Seven ideals starting with "No spinners"; user owns the data | The source of truth is a file in the user's repo; the cloud is a copy | [S-L16-373] |
| Versioning for creative work | Ink & Switch, Upwelling (Mar 2023) and Patchwork (from Feb 2024) | Private drafts that merge; always-on change tracking; diffs and branches for non-code work; AI suggestions as edits on a branch | Theme branches; visual diffs before merge; AI proposals as reviewable branches | [S-L16-374] [S-L16-375] |
| Command palette | Sublime Text 2 beta (1 Jul 2011); Superhuman, "How to build a remarkable command palette" (12 Oct 2021) | One shortcut for every command; fuzzy matching with synonyms; context-aware; teaches shortcuts | Cmd+K reaches every action and token, with synonyms in engineer vocabulary | [S-L16-376] [S-L16-378] |
| Constraint-based layout | Badros, Borning and Stuckey, Cassowary, ACM TOCHI 8(4), Dec 2001; Apple Auto Layout Guide | Declare relationships as requirements or preferences; a solver keeps them true incrementally | Express system rules as constraints (required: contrast ≥ 4.5:1; preferred: hue near brand); show which constraint binds | [S-L16-379] [S-L16-380] [S-L16-381] |
| Design galleries | Marks et al., SIGGRAPH 1997 | For nonlinear parameter spaces, generate a perceptually dispersed set of outputs to browse instead of manual tweaking | A gallery of variants spread across the parameter space, then refine | [S-L16-382] [S-L16-384] |
| Parallel prototyping | Dow et al., ACM TOCHI 17(4), Dec 2010 | Parallel prototypes before feedback gave better, more diverse results and more confidence than serial iteration | Side-by-side A/B/C themes on the same component page as the default | [S-L16-385] |
| User control and freedom | Nielsen, "10 Usability Heuristics", NN/g, 1994 (reviewed 2024) | Emergency exits; support undo and redo; visibility of system status; accelerators | One global undo history covering manual edits, shuffles and AI generations | [S-L16-386] |
| Visual review | Chromatic docs (UI Tests, UI Review); Figma "Create branches and merge changes" | Snapshot diffs against per-branch baselines; side-by-side and overlay review before merge | A token change produces a visual changeset across the component gallery | [S-L16-387] [S-L16-388] |

---

## Part F. Decision Cards: the builder's interaction model and round trip

These cards describe decisions about **the builder itself**, not decisions a designer makes inside a design system. The template fields keep their SCHEMA names. "Visual effect" here means how each option makes the tool feel to an engineer. "Token encoding" means how the decision shows up in the builder's data.

### DC-L16-01: Primary interaction model
- **Block path:** Builder > Interaction model > Primary surface
- **Questions the designer answers:** Where does an engineer spend most of their time: on a canvas, in a panel of controls with a live preview, in a chat with an agent, or in code? Which surface is primary for foundations, and which for composing components and screens?
- **Options:**
  1. **Freeform canvas** (Figma, Penpot, Paper, Framer): direct manipulation of frames and layers [S-L16-023] [S-L16-014] [S-L16-111] [S-L16-106].
  2. **Control panel plus live preview on real components** (Radix Themes playground and custom colors, tweakcn, shadcn create and typeset, Realtime Colors, Leonardo, Utopia): a small set of controls drives a rendered specimen of real UI [S-L16-320] [S-L16-322] [S-L16-327] [S-L16-331] [S-L16-332] [S-L16-334] [S-L16-337] [S-L16-341].
  3. **Prompt or agent first** (Figma Make, the Figma agent, v0, Lovable, Bolt, Stitch, Magic Patterns): describe, then iterate in chat, with point-and-edit bolted on [S-L16-025] [S-L16-027] [S-L16-242] [S-L16-246] [S-L16-261] [S-L16-235].
  4. **Visual editor over the running app** (Builder.io Visual IDE, Onlook, Tempo, v0 Design mode, Bolt visual edits, Subframe's browser; Figma Make's edit tool): select elements in a live preview of real code and edit properties [S-L16-136] [S-L16-149] [S-L16-299] [S-L16-242] [S-L16-253] [S-L16-293] [S-L16-026].
  5. **Code plus workshop** (Storybook): stories in code, a browser UI for controls, docs and tests [S-L16-121].
- **Visual effect:** A canvas feels creative but pushes an engineer into designer vocabulary (frames, layers). A panel plus live preview feels instant and safe, because every control maps to a token. Prompt-first feels fast at first and loses precision over time; Figma frames the dilemma as "Speed or precision? AI generation or direct manipulation?" [S-L16-031]. A visual editor over live code feels truthful but is bound to one app's DOM.
- **Depends on (upstream):** the source-of-truth choice (DC-L16-02) and the target platforms (L10).
- **Affects (downstream):** every other card in this part; the export channels (DC-L16-12).
- **Token encoding:** each control binds to one token path, or to one generator parameter that derives many tokens (for example a Radix accent seed, a Leonardo contrast target or a Utopia min/max pair) [S-L16-321] [S-L16-338] [S-L16-341] [inferred].
- **Platform notes:** Live previews of real components are easy on the web. For iOS and Android the preview is a web approximation unless the builder renders native previews [inferred].
- **Accessibility constraints:** The preview must show contrast results in place (Realtime Colors traffic light, tweakcn AA checker, Leonardo ratio targets, Huetone per-cell APCA/WCAG) rather than on a separate audit screen [S-L16-335] [S-L16-333] [S-L16-337] [S-L16-340].
- **Default + heuristic:** **Default: panel plus live preview for foundations and tokens; a canvas for composing components and screens; the agent as an accelerator inside both, never the only path; code always one click away.** Heuristic: if a decision has a small number of continuous parameters, use controls with a live preview; if it is spatial composition, use a canvas [inferred].
- **Evidence:** [S-L16-014] [S-L16-025] [S-L16-026] [S-L16-027] [S-L16-031] [S-L16-121] [S-L16-136] [S-L16-149] [S-L16-235] [S-L16-242] [S-L16-246] [S-L16-253] [S-L16-261] [S-L16-293] [S-L16-299] [S-L16-320] [S-L16-322] [S-L16-327] [S-L16-332] [S-L16-334] [S-L16-337] [S-L16-341]

### DC-L16-02: Source of truth and round-trip direction
- **Block path:** Builder > Data > Source of truth
- **Questions the designer answers:** What is canonical: the builder's token and component model, the code repository, or a design file? Which directions sync automatically, which are one-shot exports, and which are manual?
- **Options (L07 DC-L07-08 and L11 DC-L11-16 cover the governance side; this card covers the mechanics):**
  1. **Design file canonical** (Figma variables and components; Penpot; Framer styles): code reads through Dev Mode, MCP or exports [S-L16-001] [S-L16-113] [S-L16-109].
  2. **Code canonical** (Storybook, Builder.io, Onlook-style tools): design tools mirror the code through capture (`generate_figma_design`, Paper Snapshot) [S-L16-121] [S-L16-135] [S-L16-003] [S-L16-014].
  3. **Token file canonical** (DTCG JSON plus a Resolver in git; Penpot and Tokens Studio write DTCG): both code and design tools are generated from it (L07 A9) [S-L16-113].
  4. **The builder's own model canonical**, compiled to DTCG, CSS, native code, Figma and Paper [inferred].
- **Visual effect:** Design-canonical keeps designers happy and engineers reading specs. Code-canonical matches the 2026 practitioner majority ("Code is the source of truth") but makes visual exploration a second-class copy [COMMUNITY-SIGNAL a, c]. Token-canonical makes foundations portable but says nothing about components.
- **Depends on (upstream):** team shape (L11), platforms (L10).
- **Affects (downstream):** which MCP write paths the builder needs (Part G2), versioning and review (DC-L16-08, DC-L16-09).
- **Token encoding:** DTCG 2025.10 plus Resolver as the interchange (L07 Part C). Every token also carries its **code syntax** (the CSS variable name, Swift and Kotlin names), because Figma binds captured CSS to variables by code syntax first [S-L16-024].
- **Platform notes:** Only code-canonical setups can be tested in CI with real components (Storybook tests, Chromatic diffs) [S-L16-120] [S-L16-128].
- **Accessibility constraints:** Contrast and target-size checks run best on the canonical model, once per mode combination (L07 Part C "Permutation") [inferred].
- **Default + heuristic:** **Default: the builder's model is canonical and compiles to DTCG and to code in one step. Design tools are push targets, with capture back for review, never a second source of truth.** Heuristic: automate one direction completely before you offer a second one; zeroheight's 2026 survey found only 5% of teams run a bi-directional sync (L11 DC-L11-16).
- **Evidence:** [S-L16-001] [S-L16-003] [S-L16-014] [S-L16-024] [S-L16-109] [S-L16-113] [S-L16-120] [S-L16-121] [S-L16-128] [S-L16-135] [COMMUNITY-SIGNAL]

### DC-L16-03: Canvas rendering substrate
- **Block path:** Builder > Canvas > Renderer
- **Questions the designer answers:** Does the builder draw with real HTML and CSS (or real components), or with its own scene graph? Can an agent read and write that substrate in a language it already knows?
- **Options:**
  1. **Real HTML/CSS canvas** (Paper): the MCP writes HTML (`write_html`) and CSS (`update_styles`) and reads JSX and computed styles [S-L16-009] [S-L16-015].
  2. **Proprietary scene graph plus a code generator** (Figma: Plugin API, with `get_design_context` emitting React + Tailwind; Penpot: Plugin API code execution) [S-L16-001] [S-L16-111].
  3. **The real application's DOM** (Builder.io Visual IDE, Onlook; Figma Make's preview) [S-L16-136] [S-L16-026].
  4. **Design files in git, or canvases made of code files**: pen.dev `.pen` JSON with text diffs, branch and merge next to code [S-L16-272] [S-L16-277]; Tempo storyboards as typed React exports whose frames are live iframes [S-L16-299].
- **Visual effect:** An HTML/CSS canvas means what you see is exactly what ships on the web, including flexbox, `oklch()` and P3 per element (Paper's claims) [S-L16-015]. A scene graph gives tighter vector control but always needs a translation step, and translation is where fidelity is lost [S-L16-009] [inferred].
- **Depends on (upstream):** DC-L16-01, platforms (L10).
- **Affects (downstream):** agent reliability, export fidelity, native previews.
- **Token encoding:** On an HTML/CSS canvas, tokens are simply CSS custom properties, and modes are selectors or `@media` blocks (Paper tokens are CSS variables [S-L16-018]).
- **Platform notes:** No substrate renders SwiftUI or Compose natively on a shared canvas. Native output is always a transform from the model [inferred].
- **Accessibility constraints:** A DOM substrate lets the builder run real accessibility checks (roles, focus order) on previews; a scene graph cannot [inferred].
- **Default + heuristic:** **Default: render previews and specimens as real HTML/CSS (ideally the real component library); keep native platforms as compiled outputs with their own preview images.** [inferred]
- **Evidence:** [S-L16-001] [S-L16-009] [S-L16-015] [S-L16-018] [S-L16-026] [S-L16-111] [S-L16-136] [S-L16-272] [S-L16-277] [S-L16-299]

### DC-L16-04: How AI participates in editing
- **Block path:** Builder > AI > Edit model
- **Questions the designer answers:** Does a slider drag go through an LLM? When the agent proposes changes, does it apply them directly, or stage them for review? What happens when two sources disagree?
- **Options:**
  1. **Deterministic direct manipulation; AI only proposes** (Paper and Figma canvases with agents alongside; the Figma agent "built for direct manipulation so you can stay in control") [S-L16-031] [S-L16-014].
  2. **Direct edits staged, then committed as a reviewable change.** Figma Make queues property-panel and annotation edits above the prompt and commits them on Apply, using AI credits [S-L16-026]. v0 Design mode keeps pending edits with undo, reset and a before/after toggle, and Apply creates a new diffable version; at launch it needed no credits and no LLM round trip [S-L16-242] [S-L16-243]. Bolt batches visual edits for free and spends tokens only on "Save changes" [S-L16-253]. Lovable went the other way in June 2026: select-then-describe, which consumes credits [S-L16-246].
  3. **Agent applies directly with undo** (Figma agent: Undo in chat or Cmd+Z) [S-L16-027].
  4. **Agent changes land on a branch** (Framer 3.0 External Agents; Builder.io pushes commits to a branch or PR) [S-L16-102] [S-L16-106] [S-L16-139].
  5. **Decision forks** (Figma's `figma-generate-library` skill: when code and Figma disagree, show both values with provenance and ask) [S-L16-039].
- **Visual effect:** Routing deterministic edits through an LLM adds latency, cost and nondeterminism to what should feel like a knob [inferred from S-L16-026]. Branch- or diff-based agent output feels safe to engineers because it looks like a pull request [S-L16-139].
- **Depends on (upstream):** DC-L16-02, DC-L16-08.
- **Affects (downstream):** latency budget (DC-L16-07), review (DC-L16-09), cost model.
- **Token encoding:** agent proposals stored as a patch against the model: `{op, path, from, to, rationale, provenance}` [inferred].
- **Platform notes:** n/a.
- **Accessibility constraints:** The agent's proposals should be checked by the same contrast gates as human edits before they can be accepted [inferred].
- **Default + heuristic:** **Default: every human edit is deterministic and instant. Every agent edit arrives as a reviewable patch (a diff card with before and after previews), and conflicts arrive as decision forks.** [inferred from S-L16-026, S-L16-039]
- **Evidence:** [S-L16-014] [S-L16-026] [S-L16-027] [S-L16-031] [S-L16-039] [S-L16-102] [S-L16-106] [S-L16-139] [S-L16-242] [S-L16-243] [S-L16-246] [S-L16-253]

### DC-L16-05: Generative variation ("show me 6 options")
- **Block path:** Builder > Exploration > Variation
- **Questions the designer answers:** How does an engineer explore options they would not have thought of? Which parameters stay fixed while others vary? How do they compare options, and how do they keep one?
- **Options:**
  1. **Lock + Shuffle** over discrete properties: shadcn create and shadcn typeset (a lock toggle on every picker; Shuffle randomizes the unlocked ones and updates the `?preset=` URL) [S-L16-327] [S-L16-331]; Realtime Colors (Spacebar randomizes; lock up to 4 colors) [S-L16-335]; Material Theme Builder's Shuffle [S-L16-300].
  2. **Go wide with parallel generation**: the Figma agent runs several prompts at once and "Quickly generate distinct stylistic approaches" [S-L16-027] [S-L16-031]; Figma Make runs parallel chats [S-L16-025]; Stitch's SDK returns 1-5 variants with a `creativeRange` (REFINE, EXPLORE, REIMAGINE) and chosen `aspects` (layout, color scheme, images, font, content) [S-L16-264]; Magic Patterns gives four bold directions on a comparison link and Lovable three before the first build [S-L16-237] [S-L16-251]; Kombai offers one-click variation verbs (Surprise me, Simplify, Enrich, Adjust density) [S-L16-295].
  2b. **Generated controls**: Claude Design builds adjustment sliders for spacing and color in the current design; Magic Patterns Controls expose 2-3 structural decisions locally until "Make defaults"; pen.dev turns `@input` lines in a script into panel controls [S-L16-269] [S-L16-238] [S-L16-275].
  3. **Branchable drafts** on an infinite canvas (Superdesign) [S-L16-040]; Framer branches [S-L16-106].
  4. **Planned "Remix"** for variations, font pairings and color scales (Paper roadmap, not shipped) [S-L16-016].
  5. **Parametric sweep**: move one generator parameter (contrast multiplier, scale ratio) and watch every derived value move (Leonardo global sliders; Utopia) [S-L16-337] [S-L16-341].
- **Visual effect:** Lock + Shuffle feels playful and keeps the engineer in control of what varies. Parallel generation feels like a creative partner but produces many near-duplicates unless the prompts force distinct directions [inferred]. Dow et al. (2010) found that designers who made several prototypes in parallel before feedback produced better and more diverse results than those who iterated serially [S-L16-385]. Marks et al.'s Design Galleries (1997) generated a perceptually dispersed set of outputs to browse, instead of manual parameter tweaking [S-L16-384].
- **Depends on (upstream):** DC-L16-01; a model with named, lockable parameters.
- **Affects (downstream):** undo and history (every shuffle is an undoable step), sharing (every variant needs a URL).
- **Token encoding:** a variant is a set of parameter values plus a seed; the builder stores `{seed, locked[], params}` so any variant can be regenerated exactly [inferred from S-L16-328].
- **Platform notes:** n/a.
- **Accessibility constraints:** Random generation must be constrained so every variant passes the contrast target; filter or repair failing variants before showing them [inferred from S-L16-337].
- **Default + heuristic:** **Default: Lock + Shuffle on every foundation parameter, a "show 6" grid that renders the same real-component specimen once per variant, and pinning to keep one.** Heuristic: vary what the user has not locked, never what they have [inferred].
- **Evidence:** [S-L16-016] [S-L16-025] [S-L16-027] [S-L16-031] [S-L16-040] [S-L16-106] [S-L16-237] [S-L16-238] [S-L16-251] [S-L16-264] [S-L16-269] [S-L16-275] [S-L16-295] [S-L16-300] [S-L16-327] [S-L16-328] [S-L16-331] [S-L16-335] [S-L16-337] [S-L16-341] [S-L16-384] [S-L16-385] [S-L16-390]

### DC-L16-06: Preview surface (what the engineer looks at while deciding)
- **Block path:** Builder > Feedback > Preview
- **Questions the designer answers:** Does the preview show swatches and specimens, real components, or a whole sample product? Are light and dark (and other modes) visible at once? Do contrast results appear in the preview itself?
- **Options:**
  1. **Component matrix**: the Radix Themes playground renders every component with tabs for theme colors, all colors, all sizes and weights [S-L16-322].
  2. **Sample screens**: tweakcn previews Cards, Dashboard, Application and Marketing with real shadcn components [S-L16-332]; shadcn create switches between sample screens [S-L16-327]; Realtime Colors renders a full landing page [S-L16-334].
  3. **Scale specimens and graphs**: Utopia's table, graph and visualiser views, including interpolated values at any viewport width [S-L16-341]; Leonardo's chromaticity, lightness, 3D and wheel charts [S-L16-337]; Huetone's hue-by-tone grid with per-cell contrast [S-L16-340].
  4. **The user's own product**: Builder.io and Onlook edit the live app; Figma code to canvas captures it [S-L16-136] [S-L16-003].
- **Visual effect:** Real components answer "what will my product look like"; graphs answer "why". Tools that show only swatches force the engineer to imagine the result [inferred].
- **Depends on (upstream):** DC-L16-03 (a DOM substrate makes real-component previews cheap).
- **Affects (downstream):** perceived quality of every foundation decision; causal explanation (L01-L05 "Visual effect" fields become preview states) [inferred].
- **Token encoding:** each preview binds to semantic tokens only, so swapping modes or brands re-renders without code changes [inferred].
- **Platform notes:** Show a device frame per platform (web, iOS, Android) when platform tokens differ (L10) [inferred].
- **Accessibility constraints:** Show light and dark side by side (Material Theme Builder's sun/moon toggle and Realtime Colors' Alt+T toggle show one at a time) [S-L16-318] [S-L16-335]; show a greyscale preview (Huetone: hold B) [S-L16-340]; show contrast per pairing [S-L16-333] [S-L16-335].
- **Default + heuristic:** **Default: split the view. Graphs and specimens explain the scale; a component matrix and 2-4 sample screens show the result; every mode is visible at once or one keystroke away.** [inferred]
- **Evidence:** [S-L16-003] [S-L16-136] [S-L16-318] [S-L16-322] [S-L16-327] [S-L16-332] [S-L16-333] [S-L16-334] [S-L16-335] [S-L16-337] [S-L16-340] [S-L16-341]

### DC-L16-07: Feedback latency budget
- **Block path:** Builder > Feedback > Latency
- **Questions the designer answers:** How fast must the preview respond to a drag? Which operations may be slow (AI generation, exports), and how is slowness shown?
- **Options:** (a) continuous feedback during a drag, re-rendering on every frame, as in Bret Victor's demos ("Creators need an immediate connection to what they create" [S-L16-358]) and in slider-driven tools such as Leonardo and Utopia [S-L16-337] [S-L16-341]; (b) update on release; (c) an asynchronous agent with visible progress, such as the Figma agent's on-canvas loading indicators and Paper's agent working indicator [S-L16-027] [S-L16-009].
- **Visual effect:** Continuous feedback turns a parameter into something you can feel; update-on-release turns it into guess-and-check. Material Theme Builder's explicit Update button is an example of the second [S-L16-300] [inferred].
- **Depends on (upstream):** DC-L16-03, DC-L16-04 (an LLM in the loop breaks the budget).
- **Affects (downstream):** architecture: the token resolver and preview must run client-side [inferred].
- **Token encoding:** n/a (engine concern).
- **Platform notes:** Native previews (simulators) cannot meet a per-frame budget; show a web proxy while dragging and refresh native previews on release [inferred].
- **Accessibility constraints:** Honour reduced motion in the builder's own UI [inferred].
- **Default + heuristic:** **Default: every deterministic control re-renders the preview within one frame while dragging. Anything slower than a few hundred milliseconds shows progress and never blocks further editing.** Doherty and Thadani (IBM, 1982) found that productivity rose steeply as response time fell from 3.0 s to 0.3 s [S-L16-369]. The popular "400 ms Doherty threshold" is a later restatement (Laws of UX); it does not appear in the 1982 text [S-L16-370].
- **Evidence:** [S-L16-009] [S-L16-027] [S-L16-337] [S-L16-341] [S-L16-353] [S-L16-358] [S-L16-369] [S-L16-370]

### DC-L16-08: State, undo, versioning and sharing
- **Block path:** Builder > State > History
- **Questions the designer answers:** How far back can I undo? Can I share exactly what I see with a link? Can I branch an experiment and merge it back?
- **Options:**
  1. **Undo stack with coalescing**: tweakcn keeps 30 steps and merges edits made within 500 ms into one entry [S-L16-333]; Realtime Colors uses Cmd+Z/Y and arrow keys, with history in localStorage [S-L16-335].
  2. **State in the URL**: Radix custom palettes (`accent-light`, `accent-dark`, `gray-*`, `bg-*` params) [S-L16-321]; shadcn preset codes that the CLI can decode, resolve and open [S-L16-328]; Realtime Colors `?colors=&fonts=` [S-L16-334]; Leonardo and Utopia config URLs (Utopia even writes the URL into the generated CSS as an `@link` comment) [S-L16-338] [S-L16-341].
  3. **Automatic versions**: Figma Make versions every human or AI edit [S-L16-026].
  4. **Branches**: Framer 3.0 branching, with every external-agent change on a branch [S-L16-106] [S-L16-102]; Builder.io branches and PRs [S-L16-139]; Figma branching needs Organization or Enterprise (L07 A6).
- **Visual effect:** A URL that reproduces the exact state makes every experiment shareable in chat, and turns a playground into a collaboration tool at no infrastructure cost [inferred].
- **Depends on (upstream):** DC-L16-02.
- **Affects (downstream):** review (DC-L16-09), multiplayer (DC-L16-11).
- **Token encoding:** a compact, versioned encoding of the model or of the generator parameters (the shadcn preset pattern), plus a full DTCG snapshot per saved version [S-L16-328] [inferred].
- **Platform notes:** n/a.
- **Accessibility constraints:** n/a.
- **Default + heuristic:** **Default: unlimited coalesced undo; the URL always encodes the current state; named versions; experiments as branches that merge through a diff view.** [inferred]
- **Evidence:** [S-L16-026] [S-L16-102] [S-L16-106] [S-L16-139] [S-L16-321] [S-L16-328] [S-L16-333] [S-L16-334] [S-L16-335] [S-L16-338] [S-L16-341]

### DC-L16-09: Review and visual diff
- **Block path:** Builder > Governance > Review
- **Questions the designer answers:** When a token changes, how do I see everything it affects before merging? Who approves, and where?
- **Options:**
  1. **Snapshot diffs in CI**: Chromatic UI Review on Storybook, with baselines per branch [S-L16-128] [S-L16-387]; Tempo pixel-diffs tracked storyboards on every PR and blocks until a human approves [S-L16-400]; Figma branching reviews side by side or as an overlay (Organization and Enterprise) [S-L16-388].
  2. **Agent-created review links** (Storybook MCP `review-create` pushes a curated review of the current changes) [S-L16-121].
  3. **Design-file compare** (Dev Mode compare changes and compare with main component) [S-L16-023].
  4. **Code diff in a PR** (Builder.io) [S-L16-139].
  5. **Captured flows on a canvas** (Figma code to canvas puts multi-step flows side by side) [S-L16-003]; Paper's stated goal of CI pipelines that "create canvases with visual diffs" [S-L16-013].
- **Visual effect:** A token diff shown as before and after renders of affected components is understandable to designers and engineers alike; a JSON diff is not [inferred].
- **Depends on (upstream):** DC-L16-02, DC-L16-08.
- **Affects (downstream):** governance (L11 DC-L11-12), release notes.
- **Token encoding:** a change set lists changed tokens, then resolves the downstream dependency graph to the affected components and screens (L07 aliasing) [inferred].
- **Platform notes:** Per-platform renders in the diff when platform outputs differ [inferred].
- **Accessibility constraints:** The diff must flag any pairing whose contrast drops below the target [inferred].
- **Default + heuristic:** **Default: every change set gets a visual diff page (affected components, before and after, per mode) plus the code diff, and exports to a PR.** [inferred]
- **Evidence:** [S-L16-003] [S-L16-013] [S-L16-023] [S-L16-121] [S-L16-128] [S-L16-139] [S-L16-387] [S-L16-388] [S-L16-400]

### DC-L16-10: Keyboard-first operation and command palette
- **Block path:** Builder > Input > Keyboard
- **Questions the designer answers:** Can an engineer drive the whole tool from the keyboard? Is there one searchable command surface for every action?
- **Options:** (a) single-key toggles: Radix's "T" key toggles the theme panel [S-L16-323]; Realtime Colors uses Spacebar to randomize and Cmd+E to export [S-L16-335]; (b) fine-grained nudge keys: Huetone uses L/C/H plus arrow keys, and Paper has type-size and weight hotkeys [S-L16-340] [S-L16-014]; (c) a prompt summoned by keyboard: the Figma agent opens with Cmd/Ctrl+Enter on any layer [S-L16-027]; (d) a command palette: Sublime Text 2 introduced it in 2011 for commands that do not merit a key binding [S-L16-378]; Superhuman's guidance is one Cmd+K shortcut, fuzzy matching with synonyms, context awareness, and teaching each command's own shortcut [S-L16-376]; shadcn create uses R to shuffle [S-L16-390].
- **Visual effect:** Keyboard nudging of perceptual parameters (for example OKLCH lightness in fixed steps) is faster and more precise than dragging, and feels like an editor, which engineers already know [inferred].
- **Depends on (upstream):** DC-L16-01.
- **Affects (downstream):** accessibility of the builder itself.
- **Token encoding:** n/a.
- **Platform notes:** Respect platform modifier conventions (Cmd on macOS, Ctrl elsewhere) [inferred].
- **Accessibility constraints:** Full keyboard operability also makes the builder WCAG-conformant [inferred].
- **Default + heuristic:** **Default: a Cmd+K palette for every action and token; single keys for view toggles (theme panel, light/dark, greyscale); arrow-key nudging with Shift for big steps.** [inferred]
- **Evidence:** [S-L16-014] [S-L16-027] [S-L16-323] [S-L16-335] [S-L16-340] [S-L16-376] [S-L16-378] [S-L16-390]

### DC-L16-11: Multiplayer and agent presence
- **Block path:** Builder > Collaboration > Presence
- **Questions the designer answers:** Can designers, engineers and agents work in the same system at the same time? Can I see what an agent is touching?
- **Options:** (a) real-time multiplayer (Figma; Paper, with teammate and agent presence and "follow a teammate's cursor"; Builder.io) [S-L16-014] [S-L16-136]; (b) comments addressed to people and agents (Paper, Aug 2026) [S-L16-014]; (c) single-user local tools (most playgrounds; Pencil per Paper's comparison) [S-L16-019]; (d) local-first sync, where the file lives on the user's machine and the cloud is a copy (Ink & Switch, 2019) [S-L16-373]; Figma syncs at object-property granularity with last-writer-wins on a central server [S-L16-372].
- **Visual effect:** Visible agent presence (Paper's working indicator, cleared by `finish_working_on_nodes`) makes an agent feel like a teammate rather than a black box [S-L16-009] [inferred].
- **Depends on (upstream):** DC-L16-02, DC-L16-08.
- **Affects (downstream):** infrastructure cost; governance.
- **Token encoding:** edits as operations (CRDT or operational transform), which also give undo and history [inferred].
- **Platform notes:** n/a.
- **Accessibility constraints:** n/a.
- **Default + heuristic:** **Default for v1: single-user, local-first, with state in the URL and git; add presence for agents first (they are the most frequent co-editors), then human multiplayer.** [inferred]
- **Evidence:** [S-L16-009] [S-L16-014] [S-L16-019] [S-L16-136] [S-L16-372] [S-L16-373]

### DC-L16-12: Export and handoff channels
- **Block path:** Builder > Output > Channels
- **Questions the designer answers:** How does the result leave the builder: copy and paste, a CLI install, a file, a pull request, a push to a design tool, or an MCP server?
- **Options:**
  1. **Copy snippets**: Radix "Copy Theme" writes `<Theme ...>` JSX with only non-default props [S-L16-323]; Radix custom colors copies CSS, SVG or a URL [S-L16-320]; Utopia generates CSS, SCSS or PostCSS [S-L16-341].
  2. **CLI install from a URL**: tweakcn `npx shadcn@latest add https://tweakcn.com/r/themes/<id>` [S-L16-333]; shadcn presets [S-L16-328].
  3. **Token files**: Leonardo "Copy Tokens" with `$value` and `$type` [S-L16-338]; Huetone JSON for the Figma Tokens plugin and CSS variables [S-L16-340].
  4. **Design-tool pushes**: tweakcn "Export to Figma" (through a third-party UI kit) [S-L16-333]; Material Theme Builder Figma plugin "swap" [S-L16-318]; Realtime Colors Figma plugin that ingests the share URL [S-L16-335]; agents pushing to Figma (`use_figma`) and Paper (`write_html`, `create_tokens`) [S-L16-002] [S-L16-020].
  5. **MCP servers**: Adobe Leonardo ships `@adobe/leonardo-mcp` with a `generate-theme` tool [S-L16-338]; Storybook MCP [S-L16-121]; agent-readable formats (L11 DC-L11-23).
  6. **Pull requests** (Builder.io) [S-L16-135].
- **Visual effect:** One-line installs feel native to engineers; copy-paste feels fragile; PRs feel reviewable [inferred].
- **Depends on (upstream):** DC-L16-02.
- **Affects (downstream):** adoption; L11 distribution.
- **Token encoding:** DTCG canonical; CSS custom properties; Tailwind v4 `@theme`; a shadcn registry item; Swift and Kotlin (L07 A9) [inferred].
- **Platform notes:** Native outputs need their own channel (a Swift package, Compose theme objects) (L10) [inferred].
- **Accessibility constraints:** Ship contrast results with the export (a report file) [inferred].
- **Default + heuristic:** **Default: every state exports in five ways from one menu: copy CSS, a CLI/registry URL, a DTCG file, a PR, and a push to Figma or Paper through MCP. Also expose the builder's generator as an MCP tool, following Leonardo's example.** [inferred from S-L16-338]
- **Evidence:** [S-L16-002] [S-L16-020] [S-L16-121] [S-L16-135] [S-L16-318] [S-L16-320] [S-L16-323] [S-L16-328] [S-L16-333] [S-L16-335] [S-L16-338] [S-L16-340] [S-L16-341]

### DC-L16-13: Design-tool interop strategy
- **Block path:** Builder > Interop > Design tools
- **Questions the designer answers:** Which design tools does the builder read from and write to, through which path, and with what losses?
- **Options (see the table in Part G2):** Figma remote MCP (`use_figma`), Figma native DTCG import, Figma REST (Enterprise), a custom Figma plugin; Paper MCP; Penpot MCP (`execute_code`) and DTCG import; Framer (official skills and CLI, or the third-party MCP) [S-L16-002] [S-L16-020] [S-L16-111] [S-L16-113] [S-L16-102] [S-L16-104].
- **Visual effect:** Pushing a complete, correctly named library into a designer's own tool is the moment a builder earns designers' trust [inferred].
- **Depends on (upstream):** DC-L16-02; plan and seat gates (Figma write needs a Full seat [S-L16-002]; variables REST needs Enterprise, L07 A6).
- **Affects (downstream):** onboarding, token naming (code syntax), mode mapping.
- **Token encoding:** Figma: collections x modes with scopes and code syntax set on every variable (Figma's own skill requires both) [S-L16-039]. Paper: CSS variables, no modes yet [S-L16-018]. Penpot: DTCG sets and themes [S-L16-113].
- **Platform notes:** n/a.
- **Accessibility constraints:** n/a.
- **Default + heuristic:** **Default: write to Figma through the remote MCP (`use_figma`) when a Full seat is present; otherwise emit a DTCG file per mode that Figma imports natively. Write to Paper through its MCP. Treat both as mirrors.** [inferred]
- **Evidence:** [S-L16-002] [S-L16-018] [S-L16-020] [S-L16-039] [S-L16-102] [S-L16-104] [S-L16-111] [S-L16-113]

### DC-L16-14: Controls for foundation parameters
- **Block path:** Builder > Controls > Parameter widgets
- **Questions the designer answers:** Is color chosen with a hex field, a perceptual picker, or contrast targets? Is type set with a ratio or with min and max viewport keyframes? Which controls are presets and which are continuous?
- **Options:**
  1. **Perceptual color controls**: numeric L/C/H nudging (Huetone), OKLCH pickers (oklch.com), HCT (Material) [S-L16-340] [S-L16-309] [S-L16-300].
  2. **Contrast-target generation**: Leonardo takes target ratios per scale step (default 4.5) and regenerates the ramp, with global Brightness, Contrast and Saturation sliders and a choice of WCAG 2 or APCA [S-L16-337].
  3. **Seed-color generation**: Radix custom palette from Accent, Gray and Background into 12 steps plus alpha and P3 [S-L16-320] [S-L16-321].
  4. **Two-keyframe fluid scales**: Utopia uses min and max viewport, each with base size and ratio, then interpolates [S-L16-341] [S-L16-342].
  5. **Named presets plus overrides**: shadcn styles, Utopia ratio presets, Radix radius (none..full) and scaling (90-110%) [S-L16-327] [S-L16-341] [S-L16-322].
- **Visual effect:** Contrast-target and perceptual controls make "correct" the default, so engineers without color training still get accessible ramps. Hex fields invite arbitrary, inaccessible values [inferred from S-L16-337].
- **Depends on (upstream):** L01 (color method), L02 (type scale), L03 (space).
- **Affects (downstream):** every derived token.
- **Token encoding:** store the **generator parameters** as the source (seed, targets, ratios) and the generated values as derived tokens, with provenance in `$extensions` [inferred].
- **Platform notes:** P3 and OKLCH need sRGB fallbacks for Figma import (L07 A7).
- **Accessibility constraints:** Default to targets that guarantee WCAG AA for text pairings (4.5:1) [S-L16-333] [S-L16-337].
- **Default + heuristic:** **Default: generator-first controls (seed + contrast targets for color; min/max keyframes for type and space); raw value editing as an explicit "detach" (as Paper does for tokens [S-L16-018]).** [inferred]
- **Evidence:** [S-L16-018] [S-L16-300] [S-L16-309] [S-L16-320] [S-L16-321] [S-L16-322] [S-L16-327] [S-L16-333] [S-L16-337] [S-L16-340] [S-L16-341] [S-L16-342]

### DC-L16-15: Guardrails inside the editing loop
- **Block path:** Builder > Governance > Guardrails
- **Questions the designer answers:** Can someone (or an agent) apply a raw value where a token exists? Where are violations caught: while editing, at export, or in CI?
- **Options:** (a) **token-only styling modes**: Builder.io "Style Strict Mode" restricts Design Mode edits to design-system tokens [S-L16-132]; (b) **scoping**: Figma variable scopes limit where a token appears (L07 DC-L07-19), and Figma's skill forbids `ALL_SCOPES` [S-L16-039]; (c) **lint after the fact**: Figma Check designs (Org/Ent), unbound-value audits [S-L16-024] [S-L16-039]; (d) **agent rules**: Storybook's recommended "Never hallucinate component properties" rule [S-L16-121]; (e) **tests in the loop**: Storybook MCP `test-run` with accessibility checks [S-L16-120].
- **Visual effect:** Guardrails inside the editor feel like autocomplete; guardrails in CI feel like a scolding [inferred].
- **Depends on (upstream):** DC-L16-02, DC-L16-04.
- **Affects (downstream):** L11 DC-L11-24 (lint export).
- **Token encoding:** per-token scopes and per-component allowed-token lists [inferred].
- **Platform notes:** n/a.
- **Accessibility constraints:** Contrast gates run on every edit, not only at export [inferred].
- **Default + heuristic:** **Default: in the builder, raw values are possible only through an explicit detach; agents get the same scopes as humans; exports ship lint rules (L11 DC-L11-24).** [inferred]
- **Evidence:** [S-L16-024] [S-L16-039] [S-L16-120] [S-L16-121] [S-L16-132]

---
## Part G. Synthesis

### G1. Interaction patterns the builder should adopt (ranked)

1. **The same-frame live preview on real components, with every mode visible.** Every control re-renders real components (a matrix plus 2-4 sample screens) within the frame, and light, dark and other modes sit side by side instead of behind a toggle. Sources: Victor's immediate connection [S-L16-358]; Radix, tweakcn and shadcn previews [S-L16-322] [S-L16-332] [S-L16-327]; Tempo's live-iframe frames [S-L16-299]. Side-by-side modes are missing from almost every playground [S-L16-390]. (DC-L16-06, DC-L16-07)
2. **Outcome-first generator controls.** Engineers state intent (contrast targets per step, min and max viewport keyframes, a seed color) and the tool computes the values, with raw editing as an explicit detach. Sources: Leonardo, Harmonizer, Huetone, Utopia, Radix custom palettes [S-L16-337] [S-L16-349] [S-L16-340] [S-L16-341] [S-L16-321]; Hutchins, Hollan and Norman's gulfs [S-L16-366]; Cassowary-style required and preferred constraints [S-L16-380]. (DC-L16-14)
3. **Lock + Shuffle + a "show 6" gallery, with a seed code that round-trips between URL, CLI and repo.** Sources: shadcn presets (`init --preset`, `apply --preset`, `preset open`) [S-L16-328] [S-L16-390]; Design Galleries and parallel prototyping [S-L16-384] [S-L16-385]; Stitch's `creativeRange` [S-L16-264]. (DC-L16-05, DC-L16-08)
4. **Deterministic direct manipulation, with agents limited to reviewable patches.** Human edits never wait on an LLM. Agent output arrives as a staged batch or a branch with before/after previews, and code-versus-design conflicts arrive as "decision forks" with provenance. Sources: v0 Apply, Bolt's free batch, Framer's branch per agent change, Figma's decision forks, Ink & Switch Patchwork [S-L16-242] [S-L16-253] [S-L16-102] [S-L16-039] [S-L16-375]. (DC-L16-04)
5. **A visual diff for every change set.** A token edit resolves its downstream graph and shows before, after and overlay renders of the affected components in every mode, then exports as a PR. Sources: Chromatic, Tempo, Figma branching [S-L16-387] [S-L16-400] [S-L16-388]. No playground has this today [S-L16-390]. (DC-L16-09)
6. **Code syntax as the join key, push-to-canvas adapters, and capture back for review.** Write code syntax on every variable, so Figma's capture binds CSS variables automatically [S-L16-024] [S-L16-039]. Push to Figma through `use_figma` or DTCG import and to Paper through `write_html` and `create_tokens` [S-L16-002] [S-L16-020]. (DC-L16-13)
7. **Keyboard-first operation.** Cmd+K for every action and token; single-key view toggles; arrow-key nudging of perceptual values; coalesced unlimited undo; the URL as the save file. Sources: [S-L16-376] [S-L16-323] [S-L16-340] [S-L16-333] [S-L16-334]. (DC-L16-08, DC-L16-10)
8. **The builder's generator exposed as an MCP tool plus skills,** so agents call the same generator the UI uses, not a prose description of it. Sources: Leonardo's `generate-theme` MCP; Figma's skills [S-L16-338] [S-L16-038]. (DC-L16-12)

### G2. Round-trip architecture options (with trade-offs)

Write paths available on 2026-09-23 [S-L16-002] [S-L16-003] [S-L16-020] [S-L16-036] [S-L16-111] [S-L16-113] [S-L16-102] [S-L16-104] [S-L16-129] [S-L16-130], plus L07 A6 and A9:

| Target | Read path | Write path | Gate | Main loss or risk |
|---|---|---|---|---|
| Figma | desktop MCP (6 read tools here) or remote MCP (all read tools) | remote MCP `use_figma` (Plugin API JavaScript); `generate_figma_design` (captures live UI); native DTCG import in the UI (one file per mode); REST variables API; a custom plugin | `use_figma`: remote server, catalog client, **Full seat**, beta that will become usage-priced. REST writes: Enterprise. DTCG import: manual, all plans with modes | DTCG import takes only sRGB/HSL, px and seconds, and no composites (L07 A7). `use_figma` has a 20 KB response cap and no images. Captures are flat layers |
| Paper | Paper MCP (read tools) | Paper MCP `write_html`, `update_styles`, `create_tokens`/`set_tokens`, `create_file`/`create_page` | Paper Desktop running locally; Free 100 calls a week, Pro 1M | No modes, no shared libraries, no DTCG. Tokens are per file |
| Penpot | MCP `high_level_overview`, `export_shape` | MCP `execute_code` (Plugin API); DTCG token import | a browser tab with the plugin open; MCP key | Acts only on the focused page; no React export |
| Framer | official `@framer/agent` CLI and skills, or the third-party Unframer MCP | same (the Unframer MCP writes styles, nodes, code files and CMS) | Framer plugin open (Unframer); API key (official) | No DTCG or CSS-variable export; changes land on Framer branches |
| Code repo | files | files, PRs (Builder.io pushes branches and PRs; Storybook MCP only reads and tests) | none | the builder must own transforms (L07 A9) |

**Option 1. Figma MCP read + Paper MCP write (the setup on this machine today).** Figma is the input (variables and components read via `get_variable_defs` and `get_design_context`); Paper is the visual output where agents compose specimens in HTML/CSS [S-L16-000] [S-L16-009].
- For: works today with no extra accounts; Paper's own guide documents the Figma-to-Paper token sync [S-L16-009].
- Against: Figma stays read-only here, so nothing flows back into Figma. Figma-to-Paper is lossy (SVG fills become images, spacers are dropped, Code Connect components do not carry over) [S-L16-009]. Paper has no modes, so a light/dark system cannot be represented as one token set [S-L16-018]. Both desktop apps must be open.
- Verdict: good for a demo; not an architecture [inferred].

**Option 2. The token file (DTCG 2025.10 + Resolver) as the hub; adapters in and out.** The builder writes DTCG; adapters push to Figma (DTCG import or `use_figma`), Paper (`create_tokens`), Penpot (native DTCG), and code (Terrazzo or Style Dictionary) (L07 A9) [S-L16-113] [S-L16-020].
- For: standard, diffable, reviewable in git; Penpot imports it natively; matches L07's recommended data model.
- Against: DTCG has no component model; each adapter loses something (Figma composites and color spaces, Paper modes); mode combinations must be flattened per target (L07 A7).
- Verdict: the right **interchange**, but not enough on its own for components [inferred].

**Option 3. Code as source of truth; design tools as mirrors.** Components and CSS variables live in the repo. Storybook is the workshop, Chromatic reviews diffs, and captures (`generate_figma_design`, Paper Snapshot) refresh the design tools [S-L16-121] [S-L16-128] [S-L16-003] [S-L16-014].
- For: the practitioner majority view in 2026; CI-testable; agents build with real components [COMMUNITY-SIGNAL a].
- Against: exploration happens in code, which is slow for visual decisions; captures arrive as flat layers without library links [S-L16-022]; designers lose authorship.
- Verdict: correct for mature systems; wrong as the starting experience for creating a system [inferred].

**Option 4. The builder is the visual tool.** The builder's own canvas renders real HTML/CSS components, driven by its own model. Direct manipulation writes deterministic patches to that model; the model compiles to DTCG and code; Figma and Paper are one-click mirrors; captures come back only for review [inferred].
- For: it is the only option where visual editing and the source of truth are the same thing, which makes the "Figma for engineers" experience possible.
- Against: the most engineering (canvas, undo, variation, diffs), and multiplayer later.
- Verdict: **recommended**, built on Option 2 as the interchange and with Option 3's review loop (Storybook/Chromatic-style visual diffs) for systems that graduate into a repo [inferred].

### G3. The white space no current tool fills

**The biggest gap:** no tool lets an engineer *author the decisions* of a design system on a visual surface where each of the following holds together:
- every change shows its downstream effect on real components, in every mode, before it is committed;
- the change lands as a reviewable diff to a portable source (DTCG plus code);
- the same source pushes to Figma, Paper and code in one step.

That judgement is [inferred] from the pieces that exist separately:

| Piece | Who has it | Who lacks it | Evidence |
|---|---|---|---|
| Live preview of real components while tuning | Radix, shadcn, tweakcn, Tempo | Figma variables (no live component matrix per mode), Paper (no modes) | [S-L16-322] [S-L16-327] [S-L16-332] [S-L16-299] [S-L16-018] |
| Causal "what does this change affect" view before commit | Chromatic and Tempo (after the change is in code) | Every theme playground; every canvas | [S-L16-387] [S-L16-400] [S-L16-390] |
| Modes side by side | Harmonizer (both backgrounds) | Most playgrounds toggle | [S-L16-349] [S-L16-390] |
| Deterministic two-way token sync between canvas and git | nobody | all (two-way flows go through agents or manual git syncs) | Part C4 |
| Portable tokens (DTCG in and out, with modes) | Penpot | Subframe (Tailwind out), Plasmic (Theo), Paper (CSS variables, no modes), Figma (import subset) | [S-L16-113] [S-L16-145] [S-L16-163] [S-L16-018] (L07 A7) |
| Explanation of *why* a choice matters | none | all (L11's finding for builders; Victor's explorable explanations show the form) | L11 Part G, [S-L16-354] |
| A component layer tied to the token model with precise control | Figma, Webflow, Subframe (each in its own format) | playgrounds stop at the theme; agent builders trade precision for prompts | [S-L16-153] [S-L16-142] (L07 A6) |
| Native platforms in the loop | none (all web-first; native only as generated output) | all | [inferred] |

The builder's opening: combine patterns 1-5 from G1 on the Option 4 architecture from G2. That gives outcome-first controls, live multi-mode previews, variation galleries, reviewable diffs, and one-click mirrors to Figma and Paper. It would also be the first tool that explains each decision as it is made [inferred].

---

## Reconciliation with `sources/COMMUNITY-SIGNAL.md` (L00)
- **"Code is the source of truth" (majority view, Tier C).** Consistent with Part C4: the most engineer-friendly tools (Tempo, Onlook, Builder.io, v0 with a repo) keep code canonical. The recommendation (G2 Option 4) compiles to code, so it does not contradict this. It adds a visual authoring layer *before* code exists [COMMUNITY-SIGNAL a] [S-L16-299] [S-L16-149] [S-L16-135].
- **"Figma Make ... nothing actually usable" (Tier C).** Not contradicted by official docs. Make's direct edits are staged and applied by the agent at a credit cost, and GitHub sync is one-way [S-L16-026] [S-L16-282].
- **"I don't want code layers" (Tier C).** Code layers are still closed beta, so there is no evidence either way on adoption [S-L16-033].
- **"MCP write features are client-dependent"; a forum report that `generate_figma_design` was missing in Claude Code.** Explained by Figma's own docs: both write tools are remote-only, and a desktop-server entry can shadow them. That is exactly this machine's state [S-L16-003] [S-L16-008].
- **"Figma MCP + Claude + shadcn is how people build systems now."** Matches Figma's own `figma-generate-library` skill, which builds a Figma library from a codebase [S-L16-039].
- **shadcn "lint" (YouTube, Tier C).** Not found on the shadcn changelog; unverified [S-L16-034] [S-L16-035].
- **Disputed or stale items.** A WebSearch summary dated Figma's write-to-canvas post 7 Jul 2026; the real publish date is 24 Mar 2026 [S-L16-029] [S-L16-030]. Helper H2 summarised Paper tokens as having "multiple modes"; the tokens page lists modes and theme classes under **Roadmap**, so this file treats them as not shipped [S-L16-018].

## Cross-lane notes
(Kept here, not in BOARD.md, as the orchestrator instructed.)
- [L16 -> L07] Figma binds captured CSS to variables by **code syntax first**, then name, then scope, so the builder should set code syntax on every variable it writes. Figma's `figma-generate-library` skill requires scopes (never `ALL_SCOPES`) and code syntax on all variables [S-L16-024] [S-L16-039]. Paper tokens are CSS variables with no modes and no DTCG [S-L16-018]. Webflow's MCP can create variable collections and modes [S-L16-153].
- [L16 -> L11] Updates to L11 Part G:
  - shadcn now ships "eight styles" (Aug 2026 changelog), and `/themes` redirects to `/create` [S-L16-035] [S-L16-330].
  - Lovable replaced its property-panel Visual Edits with select-and-describe on 10 Jun 2026 [S-L16-246].
  - Builder.io renamed Fusion to Builder Code on 10 Sep 2026 [S-L16-140].
  - The Framer MCP on this machine is third-party (Unframer); Framer's official agent path is `npx @framer/agent` [S-L16-100] [S-L16-102].
  - Figma's `figma-generate-library` skill is a direct competitor workflow for "build a DS from code" [S-L16-039].
  - Leonardo ships an MCP server [S-L16-338].
- [L16 -> L01] The best color tools are outcome-first: Leonardo target ratios, Harmonizer APCA per level, Huetone per-cell contrast, Radix 12-step custom palettes with P3 [S-L16-337] [S-L16-349] [S-L16-340] [S-L16-321]. Paper mixes sRGB, P3 and OKLCH per element (vendor claim) [S-L16-015].
- [L16 -> L02, L03] Utopia models fluid type and space as two viewport keyframes with interpolation, and its CSS carries an `@link` back to the config [S-L16-341] [S-L16-342]. shadcn typeset applies lock and shuffle to typography [S-L16-331].
- [L16 -> L04] Figma's `get_motion_context` returns keyframes plus CSS `@keyframes` and motion.dev snippets [S-L16-001].
- [L16 -> builder/implementation] To let an agent write to Figma, add the remote server (`claude plugin install figma@claude-plugins-official`, or `claude mcp add --scope user --transport http figma https://mcp.figma.com/mcp`), authenticate interactively, and use a Full seat. Keep the desktop server under a distinct id [S-L16-004] [S-L16-003]. Enumerate MCP tools at runtime rather than trusting docs: Paper's server exposes 34 tools against 21 documented [S-L16-020].

## Open questions / gaps
- **No write tool was exercised** (by instruction). `use_figma` behaviour on a real library, and the input schemas of Paper's `create_tokens` and `set_tokens`, are unverified hands-on [S-L16-020].
- **Figma's usage-based price** for write to canvas is not announced; the date write to canvas leaves beta is unknown [S-L16-007].
- **Code layers** GA date unknown (closed beta on 2026-09-23) [S-L16-033].
- **Could not read:** Stitch's MCP tool reference (JavaScript-only docs); Builder.io's MCP tool identifiers; Plasmic's browser AI tool names; Variant's product pages (sign-in); Onlook's hosted product (waitlist); Material Theme Builder's web UI (Flutter canvas) [S-L16-259] [S-L16-129] [S-L16-161] [S-L16-403] [S-L16-149] [S-L16-317].
- **Latency** is not published by any tool and was not measured; "instant" in Part D means no visible delay during DOM inspection [inferred].
- **Unverified dates:** pen.dev's rename from Pencil; Claude Design's September 2026 integration day; Harmonizer's launch date; Typescale's owner [S-L16-271] [S-L16-267] [S-L16-350] [S-L16-344].
- **Doherty's "400 ms"** is not in the 1982 text read; only 3.0 s vs 0.3 s data is [S-L16-369] [S-L16-370].
- **Tier C coverage is thin.** Only L00's Reddit, HN and YouTube pulse is used; X and LinkedIn, where designers are most active, were unavailable.
- **Local scratch loss.** Mid-run, some helper and lane scratch files were deleted from the shared scratch folder. Helpers H2 and H3 rebuilt their notes from their own session records, and their row times are approximate. Every source row was re-logged in the trace.

## Confidence
- **Confirmed from Tier A primary sources (high):**
  - The Figma MCP tool list, the read/write split, remote-only status, seat gates, rate limits, supported clients and setup commands [S-L16-001] to [S-L16-007] [S-L16-022].
  - The Figma launch dates (from JSON-LD) [S-L16-030] [S-L16-031].
  - Paper MCP setup, documented tools, pricing, tokens and build-log dates [S-L16-009] [S-L16-010] [S-L16-014] [S-L16-018].
  - The live tool lists of the local Figma and Paper servers (direct observation) [S-L16-000] [S-L16-020].
  - The MCP tool lists of Webflow, Subframe, Storybook, Penpot, Magic Patterns and Tempo (vendor docs) [S-L16-153] [S-L16-142] [S-L16-120] [S-L16-111] [S-L16-237] [S-L16-401].
  - Playground controls read from live DOMs and source code (shadcn, tweakcn, Radix, Leonardo) [S-L16-327] [S-L16-333] [S-L16-323] [S-L16-338].
  - The principle originals, with bibliographic data from Crossref, ACM, SIGGRAPH and author sites [S-L16-353] to [S-L16-385].
- **Medium (vendor claims or secondary):** every "what feels good" statement unless labelled; Paper's growth figures; Variant (press only); Claude Design integration timing; the Shneiderman properties (via an NN/g restatement).
- **Inferred (marked `[inferred]`):** every "Default + heuristic", the Part G architecture recommendation, the white-space analysis, and the "missing everywhere" judgements (absence of evidence across the pages read, not proof of absence).
