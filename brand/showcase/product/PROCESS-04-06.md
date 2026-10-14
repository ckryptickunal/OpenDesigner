# Product screens 04-06: process report

I built three B2B product screens through OpenDesigner from `brand/showcase/b2b-study/product-ui.md` section 5, aiming for the bar "passes as a real top-tier B2B product". Each was:
- rendered at 1440 × 900 (scale 2) with `brand/tools/shot.py`
- opened at full size and compared with three or four shipped products on Mobbin at the same width
- fixed over three or four rounds

Notes per piece are in each folder's `notes.md`. Audit records are in `brand/showcase/audit/product--0N-*.json`.

| Piece | Screen | Accent and its one job | Type and sizes | Frames | Final score |
|---|---|---|---|---|---|
| [04-sounding-observability](04-sounding-observability/) | API service overview: environment, range and comparison row; KPI text row; four chart cards with the previous day dashed, the last hour dotted, deploy markers and a hatched no-data gap; one honest empty card; endpoints table with p95 sparklines | Amber `#c97a06`, only on the alerting series and the words that point to it. Near-black primary | Inter + JetBrains Mono (routes, versions, latencies); 12/14/20/24 | `shot.png` | 4 |
| [05-kilnworks-billing](05-kilnworks-billing/) | Usage and billing: one-line plan, budget/seat/credit meters, spend against budget with forecast, likely range and crossing, receipt ledger, invoices, usage by product with daily bars | Burnt orange `#c24e14`, only on "Edit budget" and the forecast crossing | Public Sans + Source Code Pro (invoice references); 12/14/17/20/24 | `shot.png` | 4 |
| [06-ferrule-security](06-ferrule-security/) | Security settings: auth-method rows with consequences, a SAML panel waiting on domain verification, SCIM "Available on Enterprise", sessions, danger zone; plus the audit log with filters, a UTC/Local switch and one expanded entry | Plum `#7b3577`, only on switches and focus. Near-black primary | Red Hat Text + Red Hat Mono (SP values, event codes, IPs, IDs); 12/14/20 | `shot.png`, `shot-audit.png` (`?frame=audit`) | 4 (the audit frame alone: 5) |

**What all three share:**
- light theme, 6/8/12 corners, borders on static surfaces
- one shadow at most, and only on a floating layer or a switch knob
- weights 400/500/600, tabular digits, 36 px single-line rows
- no gradients, glass, emoji or illustrations
- invented brands, people, companies and IPs (from the RFC 5737 documentation ranges)
- figures that add up; the totals and their arithmetic are in each `notes.md`

**Round scores:**
- Sounding: 3, then 4, then 4.
- Kilnworks: 3, then 4, then 4, then 4 (a typeface change).
- Ferrule: 3 (security frame) and 4 (audit frame), then 4, then 4.

**How sure the scores are.** They are my own judgement against the references in each `notes.md`. The rendered measurements were checked with a Playwright script: loaded faces and weights, sizes in use, row heights, contrast for the hand-picked pairs. Nobody else has reviewed them. I scored 4, not 5, where I could still name a weakness, and each audit file lists those weaknesses.

## Process findings, most important first

### The engine is wrong or missing something

1. **A near-black primary next to a chromatic accent can't be made, and the obvious attempt produces the wrong color.**
   - What happened: `raw.primaryActionColor "#17181c"` produced a periwinkle `#5f6dcc` primary. The action ramp keeps only the seed's hue and applies the accent's chroma and step-9 lightness (04 `DESIGN.md` before the fix: `color.bg.action.primary #5f6dcc`).
   - No question offers "near-black primary plus one chromatic color for data, selection or focus", which is study proposal P5 and the Vercel/Linear pattern.
   - Workaround: 04 and 06 alias the primary to `color.bg.inverse` by hand.
   - Feedback: 04 F-001, 06 F-002.
2. **The dense work-tool profile (P1) still has to be set by hand, about 10 commands per piece.**
   - All three sketches started from roundness 20 (2 px controls), depth 30 (a shadow on static cards) and two weights.
   - I set roundness 42, depth 10, expression 25, `weightCount 3`, `numericStyles`, `Q-color-19 brand-gray`, `focusColor` and the faces by hand.
   - After that, the engine produced exactly the evidence values: 6/8/12 corners, a 500 label weight and `text.numeric.*` styles. So the profile only needs to be the default for `--audience dense`.
   - This agrees with PROCESS-01-03 finding 1. Feedback: 05 F-003.
3. **The sketch overrides or mislabels the brand color.**
   - With `--delegated all`, an amber `#e5a00d` meant for one alerting chart series was swapped for "a readable shade" `#9c6b00` and called "an olive" (04 sketch output, decision D-0005).
   - The burnt orange `#c24e14` was called "a brown" (05 `DESIGN.md`). This repeats the components/06 finding, and the owner's rules ban brown palettes, so the label misleads.
   - Feedback: 04 F-002, 05 F-001.
4. **There is no chart grammar beyond categorical, sequential and neutral.**
   - Hand-made in 04: the comparison series dashed, the partial period dotted, the no-data hatch, the objective line and the deploy markers.
   - Hand-made in 05: the forecast, the likely-range band, the budget line and the today line.
   - P7 asks for these as tokens. Feedback: 04 F-003.
5. **Table and settings primitives are missing.**
   - There are no row-height tokens. All three pieces set `--row: 36px`.
   - There is no separator role. `border.subtle` is neutral step 6, about 1.5:1, which is too heavy for row hairlines, so all three alias steps 4 and 5.
   - There are no tokens for a switch, badge, status dot or setting row. The 32 × 18 switch needed neutral 8 for its off track to reach 3:1, and no "control-off" role exists.
   - `engine.py review` then reports these hand-made sizes as "hard-coded values" (34, 18 and 27 remain in the three pieces). It can't tell "no token exists" from "you skipped a token".
   - Feedback: 05 F-002, 06 F-001.
6. **Depth 10 zeroes the overlay elevation.** A floating chart tooltip (04) gets `0 0 0 0` from `elevation.overlay`. This is the same as PROCESS-01-03 finding 2. Feedback: 04 F-004.
7. **Reserving the accent for data has no switch.**
   - `text.link` and `border.focus` default to the accent, so 04's links would have been amber.
   - `raw.focusColor` takes one value for both modes, so an ink focus color is 1.05:1 in dark mode. Validate notes it, and the inner ring rescues it.
   - Feedback: 04 F-005, F-006.
8. **The feel word "precise" is unknown in all three sketches, and "quiet" maps only to deferential.** This is P10. Feedback: 05 F-004.

### I worked around it

9. **Preflight false positives and a parser bug.**
   - M9 reports every Google Fonts face as missing. The faces load from a `<link>`, and Playwright confirmed every face and weight.
   - Preflight read the line-height in `font: 500 var(--x)/32px …` as a 32 px font size (04 F-007).
   - It still caught real problems: 10 px and 11 px text in 04 and 06, 13 px mono within 10% of 12, and `<small>` at 11.67 px in 05. I fixed them all.
10. **Nothing shows what parallel builders already chose.** My first Kilnworks pair, Instrument Sans + DM Mono, was the same pair as `02-fennick`. I found it only when reading PROCESS-01-03 at the end, and changed to Public Sans + Source Code Pro through `engine.py set`. A per-category list of faces and accents would prevent this.
11. **A shell slip touched another builder's files.** A `sed` over `brand/showcase/product/*/index.html`, meant for my three pieces, also rewrote one CSS line in 01-quoin, 02-fennick and 03-corvane: `svg.i` width and height went from `16px` to `var(--ds-size-icon-sm)`, which is the same value. I reverted those three lines straight away with the exact reverse substitution, and checked that each file again reads `svg.i { width: 16px; height: 16px; …`. Nothing else in those folders was touched. The lesson for builders: in a shared category folder, always name your own piece folders explicitly.

### What helped

- Once set, `dials.roundness 42` gave exactly 6 / 8 / 12 corners, `depth 10` gave a borders model, and `weightCount 3` gave a 500 label weight. The levers work; only the defaults are off.
- `chart.categorical.1` gave the alerting series a real token. `bg.action.primary` became the orange in 05 with no aliasing. `text.danger` on `bg.danger.subtle` gave the danger-zone button. `border.input` gave fields a 3:1 edge.
- Validate's 164-168-pair contrast tables meant no status color needed checking by hand. Validate also caught the dark-mode focus problem, which a light-only render never shows.
- `engine.py set raw.textFace` plus `build` swapped a typeface in seconds, with the reason recorded.

## Checks run

| Check | 04 Sounding | 05 Kilnworks | 06 Ferrule |
|---|---|---|---|
| `engine.py validate` | No errors or warnings; 10 notes (5 about dark-mode focus) | No errors or warnings; 10 notes (same) | No errors or warnings; 5 notes |
| `preflight.py html --medium web` | 2 errors, both M9 false positives; 1 warning (12 px meta text, by design) | 1 error, an M9 false positive | 1 error, an M9 false positive |
| `engine.py review` | 34 hard-coded values left: component sizes with no token | 18 left | 27 left |
| Measured in the DOM | Sizes 12/14/20/24, weights 400/500/600, rows 36 px | Sizes 12/14/17/20/24, weights 400/500/600, rows 36 px and group rows 32 px | Sizes 12/14/20, weights 400/500/600 |

On-scale spacing in all three files was replaced with `--ds-space-*` after the first review run, and each `DESIGN.md` was refreshed with `engine.py design-md`.

**Not done:** dark-mode renders. The engine validates dark mode, but none of the pages was rendered dark. No Mobbin images were saved; the references are cited by `mobbin_url` only. The scratch crops were deleted.
