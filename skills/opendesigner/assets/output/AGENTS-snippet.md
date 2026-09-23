## Design system (OpenDesigner)
This project's design system lives in `opendesigner/`, and `DESIGN.md` is its living spec.

**Before any UI, styling or visual work**
1. Read `DESIGN.md` and `PRODUCT.md` at the project root.
2. Use the tokens in `opendesigner/tokens/` (DTCG, canonical) or their exports in `opendesigner/build/` (for example `build/css/tokens.css` or `build/tailwind/theme.css`).
3. Never hard-code colors, font sizes, spacing, radii, shadows or durations.
4. Check `opendesigner/decisions.md` for why a value is what it is. Locked decisions (`locks` in `opendesigner/state.json`) change only with the owner's consent.

**At the end of every implementation** (a page, a component, a refactor)
1. Run `python3 <opendesigner skill>/scripts/engine.py review` (it lists hard-coded values that bypass tokens and DESIGN.md sections that are out of date).
2. Re-read the DESIGN.md sections you touched.
3. If the work needed a value the system lacks, add it as a decision: `engine.py set <path> <value> --why "..."`, then `engine.py design-md`. Don't inline it.
4. Fix any drift `review` reports.

**To change or extend the system,** use the `opendesigner-extend` skill. Accessibility floors (WCAG 2.2 AA contrast, 24 px minimum targets, visible focus, reduced motion) are part of the system, not options.

**If a step was missing, wrong or confusing,** record it with `engine.py feedback "..." --kind gap|bug|confusing|idea`. Nothing is posted without the owner's OK.
