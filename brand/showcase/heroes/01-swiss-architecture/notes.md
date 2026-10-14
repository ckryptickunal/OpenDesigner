# 01 Halde Architekten: Swiss architecture hero

## Direction
Halde Architekten is a fictional studio of eleven architects in Zurich and Chur who design houses around the path of the sun ("Halde" is a hillside). The audience is private clients and juries who judge rigour before charm. The hero reads like an International Style poster: a visible 12-column grid, a numbered project index, a generated building section with a sun-path study, and an enormous tight grotesk headline. Feel words: **minimal, authoritative, bold**.

## References (Mobbin, structure only)
- Locomotive, project index: https://mobbin.com/sites/sections/280c1a2d-41d4-4495-a4bd-816763c93ad3 . Teaches column discipline: project, category and place each hold their own grid column, so a long list stays calm.
- Aino Agency, index: https://mobbin.com/sites/sections/aee9192a-eebd-4223-989c-64543cf5ec44 . Teaches density: tiny, uniform rows where the active item is marked by weight and color, not size.
- A24, title list: https://mobbin.com/sites/sections/b645a881-adf5-43f3-a86c-758cd54f0b72 . Teaches how far a tight grotesk can be pushed at display size before it stops reading.
- Studio Freight, approach: https://mobbin.com/sites/sections/37214c10-d891-48bc-a46e-6050033671b4 . Teaches the poster move: huge type is the layout, small labels sit in the corners.

## System (engine)
```
sketch --name "Kessler Wirth Architekten" --brand "#E8361E" --audience regular --platforms web --feel minimal,authoritative,bold --delegated all --surfaces persuade
set name "Halde Architekten"   set raw.brandColor "#E8361E" --set-by chosen   (sketch had darkened it, see findings)
set raw.textFace "Inter Tight"   set type.displayReach 14   set raw.fontLicence {web, app, selfHost: true}
```
The sketch first refused `--theme light-only` (house standard STD-visual-details-24), so the page supports light and dark through the tokens; the dark render works.

| Dial | Value | Why |
|---|---|---|
| roundness | 0 | square corners everywhere; the grid is the shape |
| depth | 0 | International Style is flat: rules, not shadows |
| colorfulness | 12 | black and off-white with one signal red |
| warmth | 70 | warm paper off-white (45 still gave a blue-white) |
| energy | 60 | heavy display type |
| expression | 55 | poster hero, quiet elsewhere |
| density | 40 | airy grid with dense small index text |

Fonts: Inter Tight (SIL OFL, Google Fonts link) for everything, tabular figures.

## Outside the tokens, on purpose
- **Page ground** uses `--ds-color-bg-neutral-subtle` (neutral step 3, #eeebe9), a fill role, because the base surface is always near-white and the engine has no way to set the light ground's lightness. It flips correctly in dark mode.
- **Headline size** `clamp(96px, 11.6vw, 168px)`: set to the column grid (about 10 columns). The scale jumps from 149 to 233 px after `displayReach 14`, and neither fits the grid width.
- **Headline tracking** -0.03em (system display value is -0.02em). Swiss display type is set tight; at -0.045 and -0.062 glyphs touched in the 200% crop, so it was loosened until they did not.
- **Line height** 0.84 on the headline: poster leading.
- **Section drawing** is generated SVG in code (deterministic, no randomness). Its colors are the tokens (`--ink`, `--ink-2`, `--signal` = `--ds-color-brand-seed`). Its labels are 11-11.5 px in a drawing that has a text alternative on the figure.

## Checks
- `engine.py validate`: passes, no errors, 0 warnings, 5 notes.
- `engine.py review`: first run found 22 hard-coded values and 8 standard breaks (px spacing, 100vh, ungated hover). All fixed; now "the code uses the tokens", DESIGN.md matches state.
- `preflight.py html`: 1 error, 1 warning. The error (M9, no @font-face for Inter Tight) is a false positive: the face loads from a Google Fonts link and `document.fonts.check` returned true in a test render. The warning (M7, `<br>` in the headline) is deliberate: the break is part of the poster.
- Checklist, type: tracking checked at 200% (glyphs no longer touch), heading weight 600, sizes 13/16/20 from the scale plus the one display size, no orphan words. Layout: every content edge snaps to the visible 12-column grid; no unplanned empty area over a quarter of the frame.
- Contrast: body #272421 on #eeebe9 about 13:1; secondary #5c5652 on #eeebe9 about 6:1; button white on #272421 about 15:1. Red is never used for text: the first render set the active index number in red (3.56:1, under the 4.5:1 floor), so it was changed to ink and the red square alone marks the row. Targets: nav and rows at least 24 px. Focus: 2 px ring from tokens.

## Type scale (named roles, 5 sizes, one face)
| Role | Size | Weight | Use |
|---|---|---|---|
| Display | 168 px (clamp, see above) | Inter Tight 600 | the poster headline |
| Title | 20 px (`--ds-font-size-20`) | 500 | the studio statement |
| Body | 16 px (`--ds-font-size-16`) | 400 | supporting copy, wordmark |
| Label | 13 px (`--ds-font-size-13`) | 400-600 | nav, index rows, meta, button, aside |
| Caption | 11 px (SVG) | 400-600 | drawing annotations (Material label minimum) |

## Changes for the owner's type and colour rules (mid-run)
- The supporting paragraph was 13 px, under the 14-16 px body minimum; it is now 16 px.
- Drawing labels were 11 and 11.5 px (within 10% of each other); all are 11 px now.
- The headline stays at weight 600 on purpose: the Swiss poster depends on a heavy grotesk. The only highlight is the red full stop, a colour mark, not an italic word.
- Colour unchanged: off-white ground, near-black text (13:1), one signal red that never carries text.

## Process findings (piece 01)
1. **Bug:** `sketch --brand --delegated all` silently replaced the given red with a darker one and stored it as the "exact" brand seed. Restored with `set raw.brandColor --set-by chosen`.
2. **Gap:** no control for the light page ground's lightness; off-white paper needed a borrowed fill role.
3. **Gap:** the typeface path (`raw.textFace`) is undocumented in the stage file; open Google faces outside a 40-name list are called licence risks.
4. **Bug:** house standard says spacing in rem, `review` flags px, but tokens.css itself is px.
5. **Bug:** `review` suggests wrong tokens for min-height, negative margin and line height; flags mask colors.
6. **Bug:** preflight errors on Google Fonts links and silently skips size checks because token sizes are rem.
7. **Gap:** single-mode marketing pages are refused by a house standard.
8. **Helped:** `type.displayReach` is exactly the right lever for poster type; `review` caught real drift fast; tokens made the dark version free.
All recorded with `engine.py feedback` in `opendesigner/feedback.md`.
