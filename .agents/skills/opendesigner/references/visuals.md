# Showing the system: the overview, the templates and Copy my choice

SKILL.md ("Show, then ask: the visual ladder") picks the surface. This file says what to show on it.

## The overview
**The overview** (`opendesigner/overview.html`, rebuilt by every `build`) is the person's own design-system page: cover, brand book, colors per theme, headings h1 to h6, spacing, corners, depth, motion, components, brand assets and how it grew. Each area says Chosen, Picked for you or Default, and anything only a person can give (a logo, a voice guide, what the product is for) shows as **Not enough information**, with the question that fills it. Show it after the sketch and after each zoom. In Claude Code, also offer to keep it as a Design System artifact: `build` writes its files to `opendesigner/build/artifact/project/`; create one with the Artifact tool (quickstart, the Design System type) and publish that folder as its `root`, uploading the logo files the README lists. Republish after later builds.

## The templates
Templates: `palette` (color, light and dark), `type-scale` (text), `spacing-ruler` (spacing and density), `radius` (corners), `elevation` (depth), `motion`, `component-sheet` (components and states), `option-gallery` (3 to 8 directions side by side), `direction-board` (the project's three directions, with photos; `engine.py research directions board` fills it), `audit` (the system as the code builds it; `engine.py audit-page` fills it) and `adapt` (a reference's changes beside the current system; `engine.py adapt` fills it). `engine.py show <template>` fills one with real values, plus what-if options for its question, without changing any choice. It writes `opendesigner/preview/<template>.html` (`--open` opens it); `build` refreshes all of them, so the person always sees their own system, never sample data. Never fill a template with invented values.

## Copy my choice
Each template has a **Copy my choice** button that produces `OD:` lines. When the person pastes them back, run each line with the engine (`rules.md` section 9) and confirm in one sentence. Record how each answer was set with `--set-by` (`rules.md` section 5).
