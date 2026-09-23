## Design system (OpenDesigner)
This project's design system lives in `opendesigner/`. Before any UI, styling or visual work:
1. Read `opendesigner/DESIGN.md`. Use the tokens in `opendesigner/tokens/` (DTCG, canonical) or their exports (`opendesigner/css/tokens.css`, `opendesigner/tailwind/theme.css`). Do not hard-code colors, font sizes, spacing, radii, shadows or durations.
2. Check `opendesigner/decisions.md` for why a value is what it is. Decisions listed under `locks` in `opendesigner/state.json` change only with the owner's explicit consent.
3. To change or extend the system, use the `opendesigner-extend` skill. Without it: read `state.json`, `decisions.md` and the tokens first, change one decision at a time with `engine.py set` or `engine.py pick` and a `--why`, then run `engine.py generate` and `engine.py validate`.
4. New components reuse existing tokens. If a value is missing, add a token through the engine instead of inventing one inline.
5. Accessibility floors (WCAG 2.2 AA contrast, 24 px minimum targets, visible focus, reduced motion) are part of the system, not options.
