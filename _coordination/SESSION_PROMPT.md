# Prompts for extra Claude sessions

Paste one of these into a new Claude Code session opened in `/Users/Kunal/Desktop/Design-System`. Each session coordinates through the files in `_coordination/` and can message the orchestrator session by name.

---

## Prompt A: join the research as a new lane

```
You are joining a multi-session research project in /Users/Kunal/Desktop/Design-System. I am building a "design-system builder": a product that helps people create their own design system from building blocks. Several Claude sessions and subagents are already working here.

1. Read _coordination/PROTOCOL.md, _coordination/SCHEMA.md and _coordination/BOARD.md before doing anything else.
2. Claim the lane I name below (or, if I name none, the first lane marked `open`) by editing only that lane's row in BOARD.md to `claimed by <your session title>`.
3. Send one message with SendMessage to the session named "Design system research and builder" (find it with ListAgents) saying which lane you claimed.
4. Research according to SCHEMA.md: Tier A official sources first, log every source you open in traces/<LANE>-trace.md, write Decision Cards in research/<LANE>-<slug>.md, and tag every claim with a source id or [inferred]. Read sources/COMMUNITY-SIGNAL.md before you finalize.
5. When you finish, set your row in BOARD.md to `done` and message the orchestrator with the file path and your top 5 findings.
Never edit another lane's files. Today's date matters: verify anything from 2025-2026 against live sources.

Lane: <fill in, e.g. "L13 accessibility deep dive" or leave blank>
```

---

## Prompt B: the Figma MCP hands-on lane (L12)

Before using this prompt, turn on Figma's MCP server. Either:
- **Figma desktop app:** open a design file, open the Figma menu > Preferences > "Enable Dev Mode MCP Server" (the menu wording may differ in newer versions), then restart the Claude desktop app. Or:
- **claude.ai Figma connector:** authorize it in your claude.ai connector settings.

Then duplicate these community files into your Figma drafts (so the MCP can read them): Figma's "Simple Design System", Google's "Material 3 Design Kit", Apple's "iOS and iPadOS 26" UI kit, and optionally Microsoft's "Fluent 2 Web" kit.

```
You are taking lane L12 (Figma MCP hands-on) in /Users/Kunal/Desktop/Design-System. First read _coordination/PROTOCOL.md, _coordination/SCHEMA.md and _coordination/BOARD.md, then claim L12 in BOARD.md and message the session "Design system research and builder" that you claimed it.

Goal: inspect real design-system files through the Figma MCP tools (get_metadata, get_variable_defs, get_design_context, get_screenshot) and record how professional systems are actually structured inside Figma. For each file I have open (Simple Design System, Material 3 Design Kit, iOS 26 UI kit, Fluent 2 kit), document:
- variable collections, their modes, variable types and counts, naming conventions, aliasing chains (primitive to semantic to component), scoping, and code syntax if set
- text/color/effect styles still in use alongside variables
- component structure: how variants and component properties (boolean, instance swap, text, variant) are set up for Button, Text field, Checkbox, Dialog and Navigation, including how states are modeled
- page and file organization (cover, foundations, components, patterns)
Save screenshots of key frames to research/L12-assets/. Write research/L12-figma-mcp-handson.md using the Decision Card format where it fits, and log every file and node inspected in traces/L12-trace.md. When done, set L12 to done in BOARD.md and message the orchestrator with the path and your top 5 findings.
```
