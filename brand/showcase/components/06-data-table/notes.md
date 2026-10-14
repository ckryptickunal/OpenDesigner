# 06 · Data table · Tarrow Freight

## Direction
Tarrow Freight is a fictional freight-operations platform. Dispatchers watch hundreds of live shipments a shift and need to scan, sort, filter and act on many rows at once. The table should feel like an engineered instrument: exact, compact and calm, with one signal colour (freight-label orange) for selection, sort state and the one primary action. Shape language is square (radius 0), rules instead of shadows, a faint manifest grid in the gutters.
Feel words: **technical, precise, dense** (the engine only knew "technical"; "precise" and "dense" were left out).

## References (Mobbin, cited by link only)
- Browserbase sessions table, https://mobbin.com/screens/7f018244-22df-44fb-832a-4f883773bb49 : filters as structured tokens ("Status is Completed ×") plus a "+" to add one. Taught me the key/operator/value filter chip.
- AirOps prompts table, https://mobbin.com/screens/dc762a82-155d-46c0-ac94-f48b0182a356 : a toolbar of labelled filter selects above a very even, rule-separated grid. Taught me the rhythm of one toolbar row, then the grid.
- DoorDash Merchant campaigns, https://mobbin.com/screens/5b7f8ac3-1059-401f-a3ee-88e553391166 : status shown as icon plus word, not colour alone, and a quiet "1–6 of 6" footer. Taught me status semantics and the footer.
- Shopify shipping labels, https://mobbin.com/screens/a695818f-5b4a-4c5c-a3ed-d6fb92be38c7 : two-line order cells and dense logistics columns. Taught me how much fits in a 32px row.

## System (engine)
`sketch --name "Tarrow Freight" --brand "#e8590c" --audience dense --platforms web --feel technical,precise,dense --theme system-light-dark --delegated all --surfaces operate`

| Dial | Value | Why |
|---|---|---|
| expression | 22 | dispatch tool: personality only in the accent and type |
| brandPresence | 40 | brand lives in the signal orange and wordmark, not in surfaces |
| density | 90 | 32px rows, 13px body; scanning 40+ shipments a screen |
| energy | 20 | calm, motion only confirms |
| roundness | 10 | gave radius 0 everywhere: freight-label squareness |
| depth | 15 | flat; borders model (all elevations become 0 shadows) |
| colorfulness | 30 | neutral slate, one accent plus status hues (brand floor kept it at 36) |
| warmth | 30 | cool slate neutrals against a warm accent |

Fonts through the engine: `raw.textFace "IBM Plex Sans"`, `raw.monoFace "IBM Plex Mono"` (SIL OFL, Google Fonts). The first version also had `raw.displayFace "IBM Plex Sans Condensed"`; removed under the owner's two-font rule (see below). `raw.fontLicence` recorded so DESIGN.md stops listing a licence risk.

Result used from tokens.css: every colour role (surfaces, text, border, accent, info/success/warning/danger subtle and text), spacing 2–32, `size.control.sm/md/lg` (24/32/40, used for rows and the density toggle), type styles body-md, label-sm/lg, code-sm/md, title-sm, the 12/14/20/24/35 sizes, focus ring width/offset, feedback and enter motion transitions (which switch under reduced motion).

## Where I stepped outside the tokens, and why
- **Row rule colour**: `--rule` = neutral ramp step 4. `color.border.subtle` is neutral 7 (#c4cad5), far too heavy for ten 32px row rules. There is no divider role. Components are told never to use ramps; I had to.
- **Selected-row rule**: accent ramp step 5 so the rule between two selected rows does not cut the band.
- **Lane progress marker colours**: warning and danger ramp step 9 for the truck marker on late and exception rows (no "marker" role).
- **Wordmark / sheet number sizes**: 19px and 32px tokens, but tracked 0.14em and condensed bold by hand.
- Bulk bar hover uses neutral ramp 11 on the inverse surface (no "inverse hover" role).

## Checks
- `engine.py validate`: no errors, 0 warnings, 5 notes (APCA advisory in dark mode, 24px smallest control, orphan steps, unasked asset hooks).
- `preflight.py html --medium web`: final run 1 error, a false positive: M9 says IBM Plex Mono has no @font-face, but it loads from a Google Fonts `<link>` (a Playwright check confirmed both faces loaded). Earlier run flagged a 9px carrier monogram (M8); raised it to the 11px token. After that "font sizes in px: []": preflight cannot see rem sizes, so it never checked the engine's 11px labels.
- Contrast: all text uses engine roles checked by validate (164 pairs). Stale rows in the error card use text-tertiary on a hatch of neutral 2 (about 5.4:1). Carrier monograms are decorative (`aria-hidden`), the carrier name beside them carries the meaning.
- Checklist (type, layout): one family per role, numbers tabular and right-aligned, one primary per header, status never colour alone (square, triangle, dashed outline), no text overlapping, captions not clipped (fixed in round 2).
- Interaction: real sorting on every sortable header (`aria-sort`), row selection with click, Space/Enter, Arrow keys and Shift+Arrow range, select-all with indeterminate state, removable filter chips, search (press `/`), density toggle switches `--row` between control md and lg, `:focus-visible` rings, transitions off under reduced motion.

## Rounds
1. First render: captions on the card edges were clipped (overflow hidden), the mode column truncated to "FTL…", the bulk bar covered the last row, the right rail had a dead 280px gap, the empty-state art was a weak doodle.
2. Fixed clipping, widened mode, 10 rows per page so the floating bulk bar sits in its own space, added lane-cell anatomy and density specimens to the rail, redrew the empty-state art (pallet, missing dashed container, lens).
3. Fixed the rail overflow, swapped the orange Retry (orange next to red read as a clash) for a bordered secondary, fixed the mode label baseline, removed a rule ("orange only for selection and focus") that the sheet itself contradicted.

## Process findings
1. **Engine and preflight disagree on the smallest web text.** Engine hard-codes `min_size = 11` and the dense scale emits 11px for body-sm, label-sm and code-sm; preflight errors below 12px on web and warns below 14px. No answer raises the floor. (feedback: gap)
2. **Preflight is blind to rem sizes** (all engine sizes are rem) and to Google Fonts links, so it reports false errors and misses real ones. (feedback: bug ×2)
3. **No component tokens for a table** (row height, header, cell padding, selected row); only `component.toast.*` exists. The engine gives good primitives, but the table is designed by hand. (feedback: gap)
4. **No divider role** lighter than border.subtle; dense UIs need one. (feedback: gap)
5. **Brand orange called "a brown"** in DESIGN.md and the sketch output. (feedback: bug)
6. **light-only refused** by a house standard; the brief's sketch command fails as written. Clear message, easy fix. (feedback: confusing)
7. Depth 15 removes even the ring from overlay elevation. (feedback: gap)
8. Helped: `dials` produced the right compact control sizes (24/32/40) and row height immediately; the `[data-density]` and reduced-motion transition tokens worked with no extra work; validate's contrast table meant I never had to hand-check a status colour.

## Owner type and color rules (applied after the first render)
- **Two fonts:** IBM Plex Sans (everything) and IBM Plex Mono (shipment IDs, lanes, weights, delta badges and the spec chips, which are all data). Dropped IBM Plex Sans Condensed: `engine.py set raw.displayFace '"=textFace"'`. Header cells are now Plex Sans 12/600 caps.
- **Type scale (5 sizes, none within 10%):** `engine.py set raw.baseSize 14` so body meets Material's 14 minimum. Caption/label 12 (header cells, chips, codes), body 14 (cells, controls), title 20 (wordmark), headline 24 ("Shipments", weight 500), display 35 (sheet number, weight 300). The scale went from 11/13/19/22/32 to 12/14/17/20/24/29/35; 17 and 29 are unused.
- **Weight on purpose:** the table title is 500, the sheet number is light 300; bold is kept for selected tab and the selected-count only.
- **Color:** light slate surface, near-black text, one orange for selection, primary action and sort state. No change needed.
- Knock-on fixes from the bigger body: widened the weight column (figures were truncating), shortened the Status filter value to "In transit, Delayed +1", search placeholder to "Search ID or lane", density specimens to ID and time.
