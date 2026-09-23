# Lane L15 prompt: visual design principles

Paste this into a Claude Code session opened in /Users/Kunal/Desktop/Design-System, after claiming L15 in `_coordination/BOARD.md` (see `_coordination/PROTOCOL.md`).

---

You are research lane L15 (VISUAL DESIGN PRINCIPLES: WHAT MAKES AN INTERFACE LOOK GOOD, AND WHY) on a project in /Users/Kunal/Desktop/Design-System. Kunal is building a "design-system builder": a product that makes creating design systems, designs and visuals a beautiful, visual process for engineers and technical people, the way Figma makes it for designers. Engineers often lack visual-design training, so this lane decides which principles the builder should make automatic, which it should teach, and which controls it should expose. It is central to the question "what would make it look which way".

First read `_coordination/SCHEMA.md`, `_coordination/PROTOCOL.md` and `_coordination/BOARD.md`. Claim L15 in BOARD.md if it is still `open`, and message the session "Design system research and builder" that you claimed it. Follow SCHEMA exactly: source tiers, logging every source in `traces/L15-trace.md`, Decision Card format, [S-id] or [inferred] tags. Read `sources/COMMUNITY-SIGNAL.md` before finalizing. Related lanes: L01 color, L02 typography, L03 space/layout, L06 brand, L13 UX laws. Link to their files rather than duplicating token-level detail.

Output: `research/L15-visual-design-principles.md`.

Sources to prioritize: NN/g visual design articles (principles of visual design, visual hierarchy, aesthetic-usability), The Futur (thefutur.com and its YouTube channel, Chris Do; Kunal referred to it as "futur", so confirm that is the right source and note any other likely match), Figma's resource library and blog, the Interaction Design Foundation, Refactoring UI (Adam Wathan and Steve Schoger), Google Design, Apple's HIG foundations, Smashing Magazine, and classic texts (Robin Williams' CRAP principles, Josef Müller-Brockmann on grids, Gestalt psychology).

Cover:
- Hierarchy and emphasis: size, weight, color, contrast, position, whitespace, and de-emphasis as a tool; focal points; scanning order.
- Contrast, alignment, repetition/consistency, proximity (CRAP); balance, rhythm, unity, scale, proportion.
- Gestalt principles in UI: proximity, similarity, closure, continuity, figure-ground, common region, uniform connectedness, Prägnanz, common fate.
- Whitespace and density as a visual voice; grids and composition in UI.
- Color theory for UI (harmonies, the 60-30-10 rule and whether it is evidence-based, temperature, saturation, restraint), and type pairing and typographic hierarchy at the principle level.
- Visual weight, optical adjustments (optical alignment, overshoot, optical sizing of icons, nested radii), depth cues, and polish details that separate good from great.
- Refactoring UI-style tactics, listed with their rationale.
- The aesthetic-usability effect and its evidence.
- Visual styles and trends: flat, material, neumorphism, glassmorphism, neo-brutalism, bento grids, skeuomorphism's return, Liquid Glass. For each: its defining levers, durable vs fashionable, accessibility risks.
- Critique vocabulary designers use to explain why something looks off, which the builder could use to give feedback.

For each principle give: what it is, evidence strength, the concrete levers/tokens it maps to, and the builder's stance: **automate** (enforce by construction), **guide** (warn or suggest), or **expose** (give the user a control). Add Decision Cards where the designer makes a real choice (style direction, density voice, hierarchy strength). Use WebSearch, WebFetch and Perplexity. Today is 2026-09-23; verify recent trend claims against live sources. Write incrementally. When finished, set L15 to `done` in BOARD.md and message the orchestrator with the file path, what "futur" resolved to, and your top 5 findings.
