# VERIFICATION-a: time-sensitive platform and tool claims

Verifier V1a, fresh context, 2026-09-24. Every source opened is logged in `traces/V1-trace.md` as S-V1a-001 to S-V1a-086. Tiers follow `_coordination/SCHEMA.md`. A claim counts as **confirmed** only when an official page (Tier A: vendor docs, changelog, launch post, repo or registry) says it today. Secondary articles were not used to confirm anything.

**Scope.** Claims about AI platforms and design tools in `synthesis/OPENDESIGNER-SPEC.md`, `docs/`, `README.md`, `AGENTS.md`, `research/L11`, `L16`, `L17`, `L18`, `benchmarks/L09-benchmark-matrix.md` and `sources/COMMUNITY-SIGNAL.md`. Where the same claim also sits in another lane file (L05, L07, L08), that location is listed too. `docs/SPEC.md` is a copy of `synthesis/OPENDESIGNER-SPEC.md` shifted by two lines: SPEC line *n* is `docs/SPEC.md` line *n*+2, and every SPEC fix applies to both files.

**Verdicts.** 78 claims checked: **65 confirmed, 11 partly right, 1 wrong, 1 unverifiable.**

## Results

| # | Claim | Where | Verdict | Correct statement (when not confirmed) | Source | Checked |
|---|---|---|---|---|---|---|
| **Claude Design and the Claude app** |||||||
| 1 | Claude Design is an Anthropic Labs product, launched 17 Apr 2026 on Opus 4.7 as a research preview for Pro, Max, Team and Enterprise | L18:148; L11:408; FAQ:130 | confirmed | | S-V1a-001 | 2026-09-24 |
| 2 | Claude Design offers "custom sliders (made by Claude)" / "adjustment sliders Claude creates to tune spacing and color" | L18:148; L16:176 | confirmed | | S-V1a-001, S-V1a-083 | 2026-09-24 |
| 3 | June 2026 update: Claude checks its output against the design system before you see it; an admin can approve one system and lock it; over 1M users in week one | L18:149; SPEC:730 | confirmed | | S-V1a-004 | 2026-09-24 |
| 4 | Sep 2026: Claude Design works in any conversation, in Claude Code and in the Artifacts tab; beta on Pro, Max, Team, Enterprise; off by default on Enterprise; not on Free | L18:150 | confirmed | | S-V1a-003, S-V1a-004 | 2026-09-24 |
| 5 | Claude Design is "now integrated into every Claude conversation and Claude Code" / "since Sep 2026 inside any Claude conversation and Claude Code" | L18:447; L16:176 | partly right | It works inside conversations and Claude Code, but in beta, on paid plans only (not Free), and off by default on Enterprise until an owner turns it on. "Every conversation" overstates it | S-V1a-003, S-V1a-002 | 2026-09-24 |
| 6 | Each design system becomes an artifact Claude can use in any conversation | L18:150; SPEC:730 | confirmed | (Stated on the product page. The Help Center adds that systems are managed in Settings > Design systems) | S-V1a-083, S-V1a-005 | 2026-09-24 |
| 7 | Known issues: no version history, unreliable multi-person editing, inline comments can go missing | L18:150; SPEC:730 | confirmed | | S-V1a-003 | 2026-09-24 |
| 8 | No Figma export | L18:150; L16:176; SPEC:730 | confirmed (by omission) | Official export lists name Canva, PDF, PPTX, HTML, a folder and a URL; Figma is not listed | S-V1a-001, S-V1a-083 | 2026-09-24 |
| 9 | Claude Design status: "research preview" | L11:455 | partly right | It launched as a research preview; since Sep 2026 the Help Center calls it a beta | S-V1a-001, S-V1a-003 | 2026-09-24 |
| 10 | Cowork merged into the Claude app on 16 Sep 2026 | L18:24; L18:443 | partly right | Announced and started on 16 Sep 2026. It is rolling out to Pro and Max first "over the coming weeks"; Team and Free follow, and Enterprise admins get notice first | S-V1a-002 | 2026-09-24 |
| 11 | Claude custom visuals: web and desktop chat, all users; a click sends a follow-up prompt in chat but not in Cowork; not on mobile | SPEC:177-178; L18:32; L18:121 | confirmed | (Beta. "Not on mobile" is by omission: the page lists web and desktop only) | S-V1a-072 | 2026-09-24 |
| 12 | Claude app skills: zip upload in Customize > Skills, all plans, code execution must be on | README:30; FAQ:87; L18:28 | confirmed | | S-V1a-070 | 2026-09-24 |
| **Agent Skills** |||||||
| 13 | About 46 clients read the Agent Skills format | SPEC:29; L18:53; L18:425 | confirmed | (46 entries on agentskills.io; "ChatGPT & Codex" is one entry) | S-V1a-007 | 2026-09-24 |
| 14 | ChatGPT, Codex, Cursor, VS Code/Copilot and Gemini CLI load SKILL.md; Codex, Cursor, VS Code and Gemini CLI read `.agents/skills/` | L18:10; L18:28; L18:57; README:37; README:66; FAQ:100; FAQ:104 | confirmed | (ChatGPT: standalone skills only in the desktop app; on web and mobile, skills arrive inside plugins) | S-V1a-011 to S-V1a-014 | 2026-09-24 |
| 15 | Claude Code reads `.claude/skills/`, not `.agents/skills/` | L18:11; L18:28; L18:58 | confirmed | | S-V1a-076, S-V1a-075 | 2026-09-24 |
| 16 | SKILL.md `description` is 1-1024 characters | L18:48 | partly right | The open spec and the Claude API allow 1,024 characters, but the claude.ai Help Center states a 200-character maximum for skills uploaded to the Claude app. Keep descriptions at or under 200 characters to be portable (the repo already does this: `tools/build_dist.py`, DECISIONS 2026-09-23) | S-V1a-006, S-V1a-010, S-V1a-009 | 2026-09-24 |
| 17 | Anthropic published Agent Skills as an open standard on 18 Dec 2025 | L18:53 | confirmed | | S-V1a-077 | 2026-09-24 |
| **Agent Plugins 1.0** |||||||
| 18 | Agent Plugins 1.0, 6 Aug 2026; TSC from Amazon, Cursor, Microsoft, OpenAI, Vercel; not an AAIF project | L18:72; L18:443 | confirmed | | S-V1a-016, S-V1a-017 | 2026-09-24 |
| 19 | No Anthropic involvement | L18:72 | confirmed | (Anthropic is absent from the TSC, the launch post and the compatible-clients page) | S-V1a-016, S-V1a-017, S-V1a-081 | 2026-09-24 |
| 20 | Root `plugin.json` needs only `$schema` and `name`; fixed `skills/` and `mcp.json`; `${PLUGIN_ROOT}` and `${PLUGIN_DATA}`; symlinks only inside the root | L18:72 | confirmed | (The repo's root `plugin.json` validates against the official 1.0.0 schema) | S-V1a-018, S-V1a-019 | 2026-09-24 |
| 21 | Compatible clients: VS Code, Cursor, GitHub Copilot, Codex, Kiro | L18:12; L18:72; README:37 | confirmed | | S-V1a-017, S-V1a-081 | 2026-09-24 |
| 22 | Google reported joining Agent Plugins | L18:34 (already marked "?") | unverifiable | Not on the official compatible-clients page or in the launch post | S-V1a-081, S-V1a-017 | 2026-09-24 |
| **MCP Apps** |||||||
| 23 | MCP Apps is an official extension, `io.modelcontextprotocol/ui`, stable spec 2026-01-26 | L18:14 | confirmed | | S-V1a-025, S-V1a-023 | 2026-09-24 |
| 24 | Claude web, desktop and mobile render MCP Apps (launched 26 Jan 2026, Free to Enterprise) | L18:32; SPEC:177-178 | confirmed | | S-V1a-020 | 2026-09-24 |
| 25 | ChatGPT "fully compatible" with MCP Apps on 2026-02-22 | L18:32; SPEC:181 | confirmed | | S-V1a-021 | 2026-09-24 |
| 26 | Claude desktop Code tab renders MCP App widgets "since 2026-09-02" | L18:32; L18:448; SPEC:180 | **wrong** | The Code tab does render MCP App widgets, but not "since 2026-09-02". The desktop changelog's only mention is v1.37937.0 (2026-08-25), in the 3P (third-party platform) section, which adds Code tab features "already available in the standard app". The standard app's date is not documented | S-V1a-022 | 2026-09-24 |
| 27 | Desktop changelog dates Chat support for skills from org-provided plugins to 2026-09-02 | L18:70 | partly right | The 2026-09-02 entry (v1.44121.4) is in the 3P section, so it dates the feature for third-party-platform builds, not for the standard app | S-V1a-022 | 2026-09-24 |
| 28 | Cursor renders MCP Apps since 2.6 (2026-03-03); VS Code since 1.109 (2026-02-04) | L18:32; SPEC:184 | confirmed | | S-V1a-074, S-V1a-073 | 2026-09-24 |
| **ChatGPT and Codex** |||||||
| 29 | Custom GPTs retire on 11 Dec 2026 on all plans; Enterprise creation of new GPTs ends 26 Oct 2026 (planned); "Migrate to plugin" turns instructions into a skill and knowledge into reference files; custom actions do not transfer | FAQ:96; L18:13; L18:75; L18:430 | confirmed | | S-V1a-026 | 2026-09-24 |
| 30 | Developer-mode plans conflict: developer docs say Pro, Plus, Business, Enterprise, Edu; Help Center says Business, Enterprise, Edu (beta) | L18:31; L18:454 | confirmed | (The conflict between the two official pages is real) | S-V1a-027, S-V1a-028 | 2026-09-24 |
| 31 | Codex caps concatenated AGENTS.md at 32 KiB (`project_doc_max_bytes`) and reads root to leaf with `AGENTS.override.md` | L18:29; L18:62; L18:66; L18:228 | confirmed | | S-V1a-015 | 2026-09-24 |
| 32 | ChatGPT standalone skills in the desktop app; plugin skills on web and mobile | FAQ:93; L18:77 | confirmed | | S-V1a-014 | 2026-09-24 |
| 33 | ChatGPT Projects work on the Free plan; Free allows 5 files (Plus/Go 25, Pro 40) | README:45-48; FAQ:92; L18:76 | confirmed | | S-V1a-071 | 2026-09-24 |
| 34 | OpenAI plugin directory: identity verification; a skills-only plugin is allowed | SPONSORSHIP:93 | confirmed | | S-V1a-084 | 2026-09-24 |
| **Claude Code** |||||||
| 35 | `/plugin marketplace add ckryptickunal/OpenDesigner` then `/plugin install opendesigner@opendesigner` | README:26-27; FAQ:83-84; AGENTS.md (Installing table) | confirmed | (The public repo's marketplace is named `opendesigner` and lists plugin `opendesigner` with source `./`) | S-V1a-029, S-V1a-031 | 2026-09-24 |
| 36 | Claude plugin layout: `.claude-plugin/plugin.json`, `marketplace.json`; sources GitHub, git, git subdirectory, npm, zip | L18:69 | confirmed | | S-V1a-031, S-V1a-032 | 2026-09-24 |
| 37 | The Claude manifests pass `claude plugin validate` | README:52; README:203 | confirmed | (The marketplace passes. The plugin passes with one warning: a `CLAUDE.md` at the plugin root is not loaded as context for plugin users) | S-V1a-030 | 2026-09-24 |
| 38 | Claude Code reads AGENTS.md natively from v2.1.277 only when there is no CLAUDE.md, and falls back to CLAUDE.md-only on Bedrock and with telemetry off | L18:29; L18:63 | partly right | v2.1.277 and the no-CLAUDE.md rule are correct. The Bedrock and telemetry-off fallback applies only before v2.1.281. A "Project instructions" setting can also load both files | S-V1a-075 | 2026-09-24 |
| 39 | Claude plugin directory: public repo, run `claude plugin validate`, individuals submit through Console; listing in Claude Code's official marketplace and in Cowork | SPONSORSHIP:92 | confirmed | | S-V1a-079 | 2026-09-24 |
| 40 | Figma write access via `claude plugin install figma@claude-plugins-official` | SPEC:652; L16:70; L16:610 | confirmed | | S-V1a-082 | 2026-09-24 |
| **Figma** |||||||
| 41 | `use_figma` and `generate_figma_design` are write tools that exist only on the remote server | L16:15; L16:48-49; L16:69; SPEC:649 | confirmed | | S-V1a-033 | 2026-09-24 |
| 42 | Writing to the canvas needs a Full seat | FAQ:116; L16:16; L16:59; SPEC:649; L18:129 | confirmed | (Precisely: a Full seat to write outside drafts; Dev seats are read-only outside their drafts) | S-V1a-034, S-V1a-036 | 2026-09-24 |
| 43 | Write to canvas is free during the beta and will become a usage-based paid feature | L16:60; L11:356; COMMUNITY-SIGNAL:72; COMMUNITY-SIGNAL:248; L18:364 | confirmed | | S-V1a-035, S-V1a-036 | 2026-09-24 |
| 44 | The remote server is on all seats and plans; the desktop server needs a Dev or Full seat on a paid plan | L16:31; L11:356; COMMUNITY-SIGNAL:72 | confirmed | | S-V1a-035 | 2026-09-24 |
| 45 | `create_design_system_rules` is an MCP prompt, not a tool | L16:56 | confirmed | | S-V1a-033 | 2026-09-24 |
| 46 | Figma Motion (Config 2026) brought timing and easing variables and animated components; rolling out from 24 Jun 2026; open beta on all plans, not GA | L07:110; L07:139; L11:409; L11:645; COMMUNITY-SIGNAL:159; COMMUNITY-SIGNAL:168; COMMUNITY-SIGNAL:232 | confirmed | | S-V1a-040 | 2026-09-24 |
| 47 | Figma has six variable types: color, number, string, boolean, timing, easing | L07:14; L07:110 | confirmed | | S-V1a-037 | 2026-09-24 |
| 48 | Modes per collection: Professional 10, Organization 20, Enterprise unlimited with extended collections | L07:14; L07:112; L17:200; L17:955; SPEC:533 | confirmed | | S-V1a-039 | 2026-09-24 |
| 49 | Extended collections are Enterprise-only | L17:200; L17:955; SPEC:533; COMMUNITY-SIGNAL:75 | confirmed | | S-V1a-041 | 2026-09-24 |
| 50 | Extended collections need "Enterprise, Full seat" | L07:120 | partly right | Enterprise plan is correct; the Help Center says anyone with can-edit access can extend a collection and names no seat type | S-V1a-041 | 2026-09-24 |
| 51 | Native DTCG import: one mode per file; colors sRGB or HSL only; dimensions px only; durations in seconds; no composite tokens | FAQ:74; SPEC:534; SPEC:661; L07:119 | confirmed | ("A new mode will be created for each file you import"; only the listed `$type`s import, so composites are skipped) | S-V1a-038 | 2026-09-24 |
| 52 | A Make kit packages a design system as an npm package plus guidelines; Make needs a Full seat on paid plans | FAQ:142; SPEC:731; L17:237 | confirmed | | S-V1a-042 | 2026-09-24 |
| **Paper** |||||||
| 53 | Paper MCP runs in Paper Desktop at `127.0.0.1:29979`; the live server exposes 34 tools (incl. `create_tokens`, `set_tokens`), 21 are documented | L16:17; L16:108-121; SPEC:654 | confirmed | | S-V1a-044, S-V1a-045 | 2026-09-24 |
| 54 | Paper Free: 100 MCP calls a week; Pro 1M a week | L16:143; L16:213; L16:539 | confirmed | | S-V1a-043 | 2026-09-24 |
| **Component and token ecosystem** |||||||
| 55 | shadcn/ui made Base UI its default in July 2026; Radix still supported | FAQ:112; SPEC:285; L08:60; COMMUNITY-SIGNAL:149; COMMUNITY-SIGNAL:254 | confirmed | | S-V1a-046 | 2026-09-24 |
| 56 | shadcn switched to Base UI on 2026-07-02 | L09:16; L09:674 | confirmed | (The changelog entry is dated 2026-07-02; the CLI release shadcn@4.13.0 followed on 2026-07-03 UTC) | S-V1a-086, S-V1a-047 | 2026-09-24 |
| 57 | Radix resumed releases in June 2026 after a gap from 13 Aug 2025 (about 10 months) | L08:56; L08:533; L09:676 | confirmed | (L08's release list omits 1.6.0 on 15 Jun and the 1.6.4-1.6.7 releases of 20-24 Jul) | S-V1a-048 | 2026-09-24 |
| 58 | Tailwind Labs is joining Shopify (2026-09-09); Tailwind stays MIT | L09:17; L09:45; L09:645; L09:676 | confirmed | | S-V1a-049 | 2026-09-24 |
| 59 | Twilio retired the Paste docs site on 2026-07-31; docs live on in GitHub; no npm release since 2025-08-25 | L09:18; L09:36; L09:70; L09:676; COMMUNITY-SIGNAL:289 | confirmed | (paste.twilio.design now redirects to the GitHub repo) | S-V1a-050, S-V1a-051, S-V1a-053 | 2026-09-24 |
| 60 | "paste.twilio.design redirects to the GitHub repo; the repo's homepage is now paste-dsys.com (live)" | COMMUNITY-SIGNAL:261 | partly right | Both facts are true, but paste-dsys.com is an independent fork "not affiliated with, endorsed by, or sponsored by Twilio". It is not Paste's new home | S-V1a-050, S-V1a-052 | 2026-09-24 |
| 61 | Polaris React is deprecated and archived; Polaris moved to web components (released 2025-10-01) | L09:12; L09:674; L08-component-catalog:8 | confirmed | (The repo is now `Shopify/polaris-react-archive`, archived 11 Sep 2026; polaris.shopify.com redirects to shopify.dev/docs/api/polaris) | S-V1a-055, S-V1a-056 | 2026-09-24 |
| 62 | Polaris Viz deprecated; repo archived 2026-07-29 | L05:524 | confirmed | | S-V1a-054 | 2026-09-24 |
| 63 | Lovable removed Themes on 16 Mar 2026 | L17:953; L17:233 | confirmed | | S-V1a-057 | 2026-09-24 |
| 64 | Lovable "made design systems a paid feature on 19 Aug 2026" | L17:953 | partly right | On 19 Aug 2026 design systems became available on all paid plans (an expansion); wrapping an existing npm package stays Enterprise-only | S-V1a-057 | 2026-09-24 |
| 65 | Lovable replaced Visual Edits with the preview toolbar on 10 Jun 2026 | L16:172; L16:602 | confirmed | | S-V1a-057 | 2026-09-24 |
| 66 | Motiff is discontinued; data export until 31 Oct 2026 | L17:221; L17:953; SPEC:734 | confirmed | | S-V1a-058 | 2026-09-24 |
| 67 | Specify shut down: announced 25 Oct 2024, ended 15 Nov 2024 | L07:16; L07:184 | confirmed | | S-V1a-060 | 2026-09-24 |
| 68 | Material Theme Builder's GitHub repo was archived on 23 Jul 2026 | L11:625; L11:643 | confirmed | | S-V1a-061 | 2026-09-24 |
| 69 | Style Dictionary v5 supports DTCG 2025.10 colors and dimensions but not resolvers (no built-in themes) | L07:16; L07:584 | confirmed | (Issue #1590 still open on 2026-09-18; resolver design under discussion; latest release v5.5.5, 2026-09-20) | S-V1a-062 | 2026-09-24 |
| 70 | Terrazzo 2.x fully supports DTCG 2025.10 including resolvers | L07:16; L07:585 | confirmed | | S-V1a-063 | 2026-09-24 |
| 71 | Builder.io renamed Fusion to Builder Code on 10 Sep 2026 | L16:161; L16:216; L16:603 | confirmed | | S-V1a-059 | 2026-09-24 |
| **Standards and other claims in README.md and docs/** |||||||
| 72 | DTCG 2025.10 was published as stable on 28 Oct 2025; modes live in its Resolver module | FAQ:68; README:147 | confirmed | ("Final Community Group Report"; modules Format, Color, Resolver) | S-V1a-064 | 2026-09-24 |
| 73 | WCAG 3 is still a draft | FAQ:187 | confirmed | (W3C Working Draft of 10 Sep 2026) | S-V1a-065 | 2026-09-24 |
| 74 | tweakcn: open-source shadcn theme editor with about 40 token inputs, AI generation from text or an image, Tailwind v3 and v4 output, a contrast checker | FAQ:146; L16:230 | partly right | Every feature is confirmed. The count is about 46 controls: 32 color tokens, 3 font pickers, letter spacing, and 10 sliders under "Other" | S-V1a-066, S-V1a-067 | 2026-09-24 |
| 75 | "NN/g's study of 10 AI design tools" | FAQ:152; L17:17; L17:131; L17:234 | partly right | NN/g's methodology page lists 14 tools tested in 3 categories; the Oct 2025 article shows outputs from 10 of them. The generic-look finding is confirmed | S-V1a-069, S-V1a-068 | 2026-09-24 |
| 76 | Gemini CLI reads GEMINI.md by default; AGENTS.md through an `@AGENTS.md` import or `context.fileName` | FAQ:104; L18:29; L18:64 | confirmed | (The repo ships a GEMINI.md containing `@AGENTS.md`) | S-V1a-078 | 2026-09-24 |
| 77 | Gemini CLI extension gallery: public repo, `gemini-cli-extension` topic, `gemini-extension.json` at the root, crawled daily | SPONSORSHIP:94 | confirmed | | S-V1a-085 | 2026-09-24 |
| 78 | Claude Design is a closed product on paid Claude plans | FAQ:130; SPEC:730 | confirmed | | S-V1a-003, S-V1a-083 | 2026-09-24 |

## Corrections to make, by file

**research/L18-ai-first-distribution.md** (owner: L18)
- Line 32, Claude Code column: "Desktop Code tab: Y, MCP App widgets since 2026-09-02 [S-L18-045]" should read "Desktop Code tab: Y, renders MCP App widgets (already in the standard app when the changelog added it to third-party-platform builds on 2026-08-25; the standard-app date is not documented) [S-V1a-022]". Make the same fix at line 448.
- Line 70: say that the 2026-09-02 changelog entry for org-provided plugin skills in Chat is in the 3P section.
- Line 24: "Cowork merged into it on 16 Sep 2026" should read "Cowork and chat began merging on 16 Sep 2026, rolling out to Pro and Max first, then Team and Free" [S-V1a-002].
- Line 447: "integrated into every Claude conversation" should add "in beta on paid plans; off by default on Enterprise" [S-V1a-003].
- Line 48: add that the claude.ai Help Center caps `description` at 200 characters for uploaded skills [S-V1a-009].
- Line 63: the Bedrock and telemetry-off CLAUDE.md-only fallback applies only before v2.1.281 [S-V1a-075].

**synthesis/OPENDESIGNER-SPEC.md and docs/SPEC.md** (orchestrator; docs/SPEC.md at +2 lines)
- Line 180 (docs 182): replace "MCP App widgets since 2026-09-02 [S-L18-045]" with "MCP App widgets (date not documented for the standard app) [S-V1a-022]".

**docs/FAQ.md** (R1 docs owner)
- Line 152: "NN/g's study of 10 AI design tools" should read "NN/g's evaluation of AI prototyping tools (14 tested)" [S-V1a-069].
- Line 146 (optional): "about 40 token inputs" could read "about 45 controls" [S-V1a-067].

**research/L16-visual-tooling-for-engineers.md** (owner: L16)
- Line 176: after "since Sep 2026 inside any Claude conversation and Claude Code", add "(beta, paid plans)" [S-V1a-003].
- Line 230 (optional): the tweakcn count is about 46 controls [S-V1a-067].

**research/L17-how-systems-get-made.md** (owner: L17)
- Lines 17, 131 and 234: the NN/g study tested 14 tools; the article shows outputs from 10 [S-V1a-069].
- Line 953: "made design systems a paid feature on 19 Aug 2026" should read "made design systems available on all paid plans on 19 Aug 2026 (npm-package wrapping stays Enterprise-only)" [S-V1a-057].

**research/L11-process-governance.md** (owner: L11)
- Line 455: "research preview" should read "research preview at launch (Apr 2026); beta since Sep 2026" [S-V1a-003].

**research/L07-tokens-figma.md** (owner: L07)
- Line 120: "Enterprise, Full seat" should read "Enterprise plan; anyone with can-edit access (no seat type stated)" [S-V1a-041].

**sources/COMMUNITY-SIGNAL.md** (owner: L00)
- Line 261: add that paste-dsys.com is an independent fork that is not affiliated with Twilio, so it is not Paste's new home [S-V1a-052].

**research/L08-components-patterns.md** (owner: L08; optional)
- Line 56: the Radix release list can add 1.6.0 (15 Jun 2026) and 1.6.4-1.6.7 (20-24 Jul 2026) [S-V1a-048].

**Plugin packaging** (optional; no factual error)
- `claude plugin validate .claude-plugin/plugin.json` warns that a root `CLAUDE.md` is not loaded as context for plugin users. This is expected, because the skills carry the guidance, but maintainers should know about it [S-V1a-030].

## Not checked, and caveats
- `docs/SPONSORSHIP.md`: the funding-program rows (grants, credit programs, windows) were not checked. Only the three distribution rows (Claude plugin directory, OpenAI plugin directory, Gemini extension gallery) were.
- Claims in L18 that were not on the task list (Codex CLI UI, Kiro and Zed paths, Skills over MCP, MCP 2026-07-28 spec details, Figma rate limits, `use_figma` payload limits) were not re-checked.
- The Figma desktop MCP server did not connect in this session (ECONNREFUSED), so the "6 read-only tools on this machine" observation (SPEC:648; L16:16, L16:68) could not be re-observed.
- The local Claude Code CLI is 2.1.238, which is older than the v2.1.277 AGENTS.md support described in row 38. The validation result in row 37 comes from that version.
- help.openai.com returns HTTP 403 to scripts, so rows 29, 30 and 33 were read in the built-in browser pane.
