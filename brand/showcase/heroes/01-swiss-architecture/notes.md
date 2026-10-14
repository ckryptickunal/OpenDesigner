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

## Round 3 (owner review, 2026-10-14)

**What he said.** "Okay." It had to become clearly better, at the level of the B2B product screens and the Orbika hero. The earlier audit (score 4) named three competing centres (the project index, the drawing and the giant headline), the stock filled-plus-underlined button pair, and a drawing that read as a diagram.

**What changed.**
- **One object.** The building section is now the hero: about 680 px tall at 1 m = 32 px, across all twelve columns. The project index and the visible column guides are gone; the index survives as "Work 24" in the nav and "01 of 24" in the title block.
- **The drawing, redrawn as an architect would.** Three storeys, each 12 m deep, step back 8 m up a 38% slope, with poché slabs, 0.4 m retaining walls, 1.40 m overhangs, glass balustrades, a garden wall and level marks (±0.00, +3.60, +7.20). The cut earth is a 0.8 m band of 45° hatch along the cut ground (a flat grey tone read as a shadow of the building). Real dimension lines with extension lines: an outer chain 8.00 / 8.00 / 12.40 (glass to glass, then glass to the outer wall face), an inner 1.40 for the overhang and 7.24 under the lowest floor. The angles 19.7° and 66.6° are marked where the rays land. A title block on columns 10 to 12 stands on the band's rule: project, year, "Section A–A, looking west", "01 of 24", "±0.00 = 1,081.40 m above sea level", a 0–5 m scale bar and S → N. Entourage at 1:200: outline figures (1.75 m) and a bare winter tree with its summer crown dashed.
- **The sun, computed.** Flims, 46.83° N: 19.7° at solar noon on 21 December and 66.6° on 21 June. Under a 1.40 m overhang and 3.10 m clear height the winter ray lands 7.24 m inside; the summer ray lands 0.06 m short of the glass. Winter light is shown once outside (a dashed ray drawn 6 m back from each overhang, so all three start alike and none crosses a dimension) and once inside (a tinted wedge); the red never sets text (3.6:1 on the paper).
- **Headline.** One line, 88 px, Inter Tight 500 (was 168 px / 600 over two lines), in a band ruled off from the drawing. The red full stop stays: it is the sun.
- **One action.** "Start a project →" as an underlined link; the filled button is gone.
- **Facts.** Sunrise in Zurich on 14 Oct 2026 is 07:41 CEST (was 07:38).
- **Key.** 16 px, on the paper at bottom left; it names the two days and does not repeat the drawing's numbers. The statement no longer repeats "Zurich and Chur" from the header.

**Type scale (round 3).** Display 88 px at 1440 wide, `min(88px, 6.1vw)` below it (outside the scale, `od-ignore`: one line across nine columns; checked at 1280 x 800) · Body 16 px · Label 13 px (bar, drawing labels, title block). One face, Inter Tight.

**Checks.** `check_dates.py`: passes. `preflight.py html`: one warning, the 88 px display outside the scale (on purpose). `engine.py review`: the code uses the tokens; DESIGN.md refreshed with `design-md`.

**Fresh-eyes audit.** A fresh-context subagent scored it against the B2B screens, Orbika and three Mobbin references (Heron AI https://mobbin.com/sites/sections/76dab96c-c33d-4d52-944b-7d32dc2274fa, Waka Waka https://mobbin.com/sites/sections/082e8338-c62d-4080-a4a0-a5a8a8caa6ac, MOUTHWASH Studio https://mobbin.com/sites/sections/38d3c862-d84c-4840-9fd0-94002eaf5571).
- Round 1, **3**: still an explainer diagram; winter light shown six ways; gradient fades; a fractal tree and pictogram figures; "looking east" was wrong (south left, north right faces west); a 13 px key.
- Round 2, **4** (low): a ray crossing a dimension tick, rays starting differently, a flat grey earth mass with a seam, tree limbs outside the crown, 12.00 measured to a hidden face, a split link underline, repeated numbers.
- Round 3, **4**: all fixed; the new grey earth band read as a drop shadow.
- Round 4, **4**: the hatched band reads as cut earth; nothing new broken. Optional nits left: the band's lower edge notches under the garden, and the hatch ends in a sliver at the right margin.
It recomputed the sun angles, the 7.24 m and the 0.06 m, measured the chains on the render (257 / 256 / 384 px at 32 px per metre) and measured text contrast on the pixels (key 6.1:1 on the paper, "19.7°" 10.2:1 on the wedge).

**Still open.** "Halde" is one letter from "Halden" (`app-screens/01`, `components/06`); NAMES.md lists it as unresolved. Renaming this brand would also change `mockups/02` and `mockups/08`, so it is left to the orchestrator. `mockups/02-laptop-desk` alt text still describes the old project index.
