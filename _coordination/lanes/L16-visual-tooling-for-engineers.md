# Lane L16 prompt: visual design tooling for engineers

Paste this into a Claude Code session opened in /Users/Kunal/Desktop/Design-System, after claiming L16 in `_coordination/BOARD.md` (see `_coordination/PROTOCOL.md`).

---

You are research lane L16 (VISUAL DESIGN TOOLING FOR ENGINEERS AND THE DESIGN <-> CODE ROUND TRIP) on a project in /Users/Kunal/Desktop/Design-System. Kunal is building a "design-system builder" whose aim is to make creating design systems, designs and visuals a beautiful, visual process for engineers and technical people, the way Figma makes it for designers. This lane studies the tools and interaction paradigms that already try to do this, so the builder can adopt what works and fill the gaps.

First read `_coordination/SCHEMA.md`, `_coordination/PROTOCOL.md` and `_coordination/BOARD.md`. Claim L16 in BOARD.md if it is still `open`, and message the session "Design system research and builder" that you claimed it. Follow SCHEMA exactly: source tiers, logging every source in `traces/L16-trace.md`, [S-id] or [inferred] tags. Read `sources/COMMUNITY-SIGNAL.md` before finalizing. Lane L11 reviews design-system builder products as competitors and L07 covers tokens and Figma's features; read `research/L11-process-governance.md` and `research/L07-tokens-figma.md` and link rather than duplicate. This lane's angle is the interaction model and the design<->code workflow.

Output: `research/L16-visual-tooling-for-engineers.md`.

Cover (verify every 2025-2026 claim against official docs, changelogs or launch posts, with dates):
- Figma for developers: Dev Mode, Code Connect, Figma Make, and the Figma MCP server. Establish exactly which MCP tools can READ designs and which can WRITE to the canvas as of September 2026, and on which plans and clients.
- Paper (paper.design): what it is, its MCP server, what an agent can read and write through it, and the exact documented way to connect it to Claude Code.
- Other code-native or dev-friendly visual tools: Penpot, Framer, Webflow, Subframe, Onlook, Builder.io (Visual Copilot/Fusion), Plasmic, Storybook (plus any Storybook MCP or AI features; verify), Chromatic, UXPin Merge, tldraw, Magic Patterns, v0, Lovable, Bolt, Figma-to-code and code-to-Figma plugins (e.g. html.to.design), and notable 2025-2026 entrants.
- Theme/foundation playgrounds engineers already use: Material Theme Builder, Radix Themes playground and Radix Colors, shadcn/ui themes and community generators (e.g. tweakcn), Realtime Colors, Adobe Leonardo, Huetone, Utopia, typescale tools, Tailwind's palette tooling.
- For each tool: target user, interaction model (canvas, sliders, live preview, direct manipulation, prompt/AI, code editor), source of truth (code, design file, JSON tokens), round-trip support (design->code, code->design), handling of tokens and components, what makes it feel good to use, and its gaps for engineers.
- Principles for creative tools that serve engineers: direct manipulation, immediate feedback and live programming (Bret Victor's "Inventing on Principle" and "Learnable Programming"), explorable explanations, multiplayer, keyboard-first and command palettes, undo/versioning, constraint-based layout, generative variation ("show me 6 options"), and visual diff/review. Cite the originals.
- Synthesis: the interaction patterns the builder should adopt, round-trip architecture options (Figma MCP read + Paper MCP write, tokens JSON as the hub, code as source of truth, and so on) with trade-offs, and the white space no current tool fills.

Use WebSearch, WebFetch and Perplexity. Today is 2026-09-23 and this space changes monthly, so do not rely on memory for any product claim. Write incrementally. When finished, set L16 to `done` in BOARD.md and message the orchestrator with the file path, exactly what Figma MCP and Paper MCP can read and write, the top 5 patterns to adopt, and the biggest gap.
