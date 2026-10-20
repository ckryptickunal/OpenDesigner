# 09 · Soffit: roadmap forecast (desktop, 1440×900 @2x)

Gallery: Soffit is a fictional roadmap planner; Christmas slot booking opens in place on the timeline, forecast 8 days past its target, with the choice to cut or move.

Soffit is a fictional roadmap planner that forecasts each project's finish from its own pace. The screen is the H2 2026 roadmap of Whinberry, a fictional UK online grocer: 14 projects in five teams, each with closed issues, target, forecast and how far the forecast lands from the target, and Christmas slot booking open in the side panel because it will finish 8 days late. Rebuilt in round 4 (see the end of this file); the sections from "Direction" to "Process findings" describe the Quarry board it replaced.

## Direction (rounds 1 to 3: the Quarry board, replaced in round 4)
Quarry is a fictional project tool for product teams. The fictional company is "Kestrel", and its project is a field-service app. The screen is the board for Cycle 14: sidebar, header, view tabs with keyboard numbers, a two-week timeline strip with a today line and a release milestone, five status columns with one card being dragged, and a footer of shortcuts. It should be dense but calm, with crisp cool greys and one vermilion accent used only for today, the primary action, the focused card, urgent priority and "due soon". The status icons are diamonds, a cut-stone motif for "Quarry". Feel words: **focused, calm, technical**.

## References (Mobbin, structure only)
- [Linear, board](https://mobbin.com/screens/29621c0a-9946-46aa-9d39-6d5f4f578b21): card density (id, title, label chips, avatar) at about 120 px a card.
- [Linear, project timeline](https://mobbin.com/screens/64119b7d-8337-4873-8794-1ead1cba2618): day columns with a today marker over the bars.
- [Jira, timeline](https://mobbin.com/screens/45d3b32a-ed07-481f-bb37-8712b7cd546c): a today line, shaded weekends and view tabs above the canvas.
- [Height, kanban](https://mobbin.com/screens/4da1ccac-3d97-4b47-9399-296086983c30): a sidebar in sections (inbox, projects, views) and a quiet workspace switcher.

## System (engine)
```
sketch --name "Quarry" --brand "#F04A1A" --audience dense --platforms web --feel focused,calm,technical --delegated all
   (stored brand became #D93900: the sketch picked a white-text shade; I kept it, it is crisper)
set raw.neutralTint cool · set raw.textFace Geist · set raw.monoFace "Geist Mono"
build → Passes: no errors, 0 warnings
```
| Dial | Value | Why |
|---|---|---|
| expression | 25 | daily tool, calm chrome |
| brandPresence | 18 | one accent, used sparingly |
| density | 82 | people live in it all day (compact density) |
| energy | 40 | quick, no bounce |
| roundness | 28 | small crisp corners (control 4, container 8, overlay 12) |
| depth | 15 | hairlines over shadows |
| colorfulness | 15 | greys plus one accent |
| warmth | 35 | slightly cool |

## Fonts and type scale (two faces)
Geist (text, OFL) and Geist Mono (OFL), the mono only for real data: issue ids, dates, day labels, percentages and key caps. It follows desktop and Material 3 conventions, with 2 sizes for a dense tool:

| Role | Size / weight | Used for |
|---|---|---|
| Title small | 14 Geist 600 | page title (h1 "Cycle 14"), column heads, cycle title |
| Body | 14 Geist 400-500 | card titles, navigation, buttons, chips |
| Label | 12 Geist / Geist Mono 400-600 | ids, labels, dates, key caps, footer, avatar initials |

No display sizes. The board itself is the page, as in the references.

## Where I left the tokens, on purpose
- Weekend hatching in the timeline is a CSS gradient. The dragged card is rotated 2.2°.
- The milestone tag is positioned with `calc()` from the timeline geometry.
- The timeline bars use `neutral` steps. Only the today line is vermilion.

## Changes for the owner's type and color rules
- The workspace was renamed "Halden" → "**Kestrel**", because piece 01's brand is "Halden Private".
- The cycle summary ("Day 8 of 14 · 61% done") moved from mono to Geist, because it is a sentence, not data.
- The scale is written down here: two sizes, Material label minimum 12.

## Checks
- `engine.py validate`: Passes, 0 warnings.
- `preflight.py html`: 0 errors, but only because it saw no px sizes. Earlier it caught 9 to 10 px avatar initials (fixed to 12).
- Review probe: it caught 4 real or likely problems, now fixed: the kbd in the primary button (3.44:1), weekend day labels on `neutral-8` (3.56:1), the breadcrumb slash (1.62:1) and white initials on a bar, which the probe misread (see findings). It also caught a missing h1 and skipped heading levels. Now: 0 errors and 0 warnings. Hover styles were added for every pointer control.
- `engine.py review`: 78 "hard-coded values", mostly icon and avatar sizes mapped to spacing tokens, and 1 px inset rings it calls shadows. The real spacing values were moved to tokens.

## Process findings
- **Bug in my own build, worth noting:** a `.pri` priority-icon class clashed with `.btn.pri` and shrank the "New issue" button to a 30 px pill. The probe did not catch it; only looking at the render did.
- **Confusing:** `engine.py review` is noisy on a dense UI: 78 hits, most of them sizes or hairlines. (feedback recorded)
- **Bug (review skill):** the probe measures contrast against the nearest ancestor background, not what is painted behind (a sibling progress fill, an SVG shape). (feedback recorded)
- **Helped:** compact density and the cool tint gave good dense defaults (12/14 type, 4/8 radii) with no hand-tuning.

## Round 4 (owner review, 2026-10-15)
**What the owner said.** About all the app screens, the desktop ones included: they "look absolutely shit. None of them should feel like they are from a vibe coded app or a cheap Chinese app." The orchestrator's notes on this piece: a close copy of Linear (cycle header, board, keyboard bar); heavy dark timeline slabs with large knobs; a tilted mid-drag card that looks broken in a still; an orange "New issue" fighting the red today line and due dates; type a little large; "Tu 14" was the wrong weekday (14 Oct 2026 is a Wednesday); and "Kestrel" was also used by `components/07`.

**What changed: a new piece, not a repaint.**
- **One idea:** a head of product sees that Christmas slot booking will finish 8 days after its target, and must decide what to cut or move. The way it knows: every project on the roadmap carries a forecast from its own pace.
- **Product and names:** Soffit (roadmap planner) for Whinberry (UK online grocer). Quarry, Kestrel and every old name are gone (see `NAMES.md`, appended 2026-10-18).
- **Screen:** H2 2026 roadmap, grouped by team, 14 scheduled projects. Columns: Closed, Target, Forecast and "vs target" (for example "8d late" or "3d early"). Bars show plan span and closed issues; a red block shows where a forecast passes its target; the 14 Dec peak freeze is hatched; a legend sits in a footer. The side panel holds the project with one display figure (Tue 8 Dec, "8 days past the 30 Nov target"), closed and pace, checkpoints worked in order with due and forecast dates, the week 42 check-in, and a decision bar: cut 7 issues to keep 30 Nov, or move the target to 8 Dec.
- **Colour jobs:** petrol `#136f8a` only for today (the "15 Oct" marker and line, and focus). Red only where a forecast lands after its target. Neutral selection. One dark button on the screen ("Choose 7 to cut"). Hairlines only, no shadows.
- **Type:** IBM Plex Sans (OFL), one face. 12 (labels, dates, counts, legend), 14 (body), 17 (project title), 29 (the forecast figure). Weights 400/500/600. The 14/12 pair follows the B2B product screens; the brief's 15–17 px body floor is not met, on purpose, because the bar screens use 14.
- **Dates:** British (`en-GB`: "8 Dec", "Wed 14 Oct"), since the grocer is in the UK.

**References (Mobbin, structure only; also the three blind-test references):**
- [Linear, project timeline with side panel](https://mobbin.com/screens/c1cc22aa-69de-468c-b200-cf80f05ac1c7): a timeline beside a project panel.
- [Linear, project page](https://mobbin.com/screens/9c8e3907-b7af-48d6-ae2d-9b4ff700d433): properties, milestones and an update in one panel.
- [Wrike, Gantt with task table](https://mobbin.com/screens/309ce63c-f7a7-4f54-93a0-16a72d3181c2): a table of columns beside the bars.
- Its own: forecast and "vs target" on every row, red overruns, checkpoint forecasts in order ending in the target, the freeze band and the decision bar.

**System (engine; the folder was re-sketched, old feedback F-001 and F-002 kept):**
```
sketch --name "Soffit" --brand "#3358D4" --audience dense --platforms web --feel calm,technical,serious --delegated all
set dials.warmth 30 · raw.neutralTint cool · dials.depth 10 · dials.roundness 42 · dials.colorfulness 20 · dials.expression 15
set raw.brandColor "#136F8A"   (petrol; an audit called Inter with cobalt "the most default palette")
set raw.textFace "IBM Plex Sans"
build → Passes: no errors, 0 warnings
```
`light-only` was refused by house standard STD-visual-details-24, so the page sets `data-theme="light"` on a light-and-dark system.

**Outside the tokens, on purpose:** the timeline scale (31 px weeks, 8 px inset), the freeze hatch, the red overrun blocks, the today marker, white rings on checkpoint dots, and 28 px icon buttons (no token). `--primary` aliases `bg.inverse` (the engine has no near-black primary role).

**Figures, re-added from the page:**
- Projects: 4 + 3 + 3 + 2 + 2 = 14 scheduled, and 5 with no dates, which makes 19 (the sidebar). 2 forecast late.
- Christmas slot booking: 41 of 89 closed. The 48 open are 11 for the load test, 22 for members first and 15 for everyone else. The pace is 25 issues in 28 days. Each forecast is rounded up to a working day:
  - load test: 11 issues take 12.3 days, so Wed 28 Oct (due Thu 22 Oct);
  - members first: 33 issues take 37 days, which lands on Sat 21 Nov and rounds to Mon 23 Nov (on time);
  - everyone else: 48 issues take 53.8 days, so Tue 8 Dec, 8 days after Mon 30 Nov.
- To keep 30 Nov, the 46 days left close about 41 issues, so 7 of the 48 must be cut.
- The other forecasts use each project's pace since it started; "vs target" is the forecast minus the target. Cold-chain scan has no forecast in its first week.
- Check-in: 7,400 × 1.22 = 9,028, so "about 9,000". Wed 14 Oct is in ISO week 42.

**Checks:**
- `check_dates.py --year 2026`: every weekday matches.
- `check_names.py`: 0 errors. The 7 "new" words are UI words, plus "Eze" (part of Ngozi Eze, which is listed).
- `preflight.py html`: 0 errors and 0 warnings; sizes 12/14/17/29.
- `engine.py validate`: passes. `engine.py review`: 0 lines break a standard.
- Contrast: the lowest text pair is 4.96:1 (tertiary on the selected row). Bar edges and closed fill are 3.62:1 (3.05:1 on the selected row). Red blocks are 4.6:1.

**Round 4 test**
- **A. Blind pairwise** (sides random, no labels, same height). Ours won every pair in every round except one:

  | Round | vs Linear timeline | vs Linear project page | vs Wrike Gantt |
  |---|---|---|---|
  | A | won by 4 | won by 2 | won by 4 |
  | B | won by 3 | won by 2 | won by 4 |
  | C | won by 3 | won by 2 | won by 4 |
  | D | won by 3 | **lost by 2** | won by 4 |
  | E | won by 4 | won by 2 | won by 4 |
  | F | won by 4 | won by 2 | won by 4 |
  | Final render | won by 3 | won by 2 | won by 4 |

  In the final round one judge saw all three pairs. It passes rule 1.
- **B. Fresh-eyes audit:** 3, 3, 3, 4, 3, 3 and 3 across seven rounds. It reached 4 once (round E) and the latest round scored 3, so it has **not reliably passed** B after more than four rounds.
  - The last rounds found no factual errors; every figure checked out.
  - Their objections disagreed with each other from round to round:
    - bar edges were a must-fix in one round and "remove the outline" in the next;
    - the today pill was asked for in round D and called a Linear signature in the last round;
    - a checkpoint slip line was asked for, then called an unexplained mark.
  - The steady complaints were three:
    - it is mostly grey and can read as a wireframe;
    - its family resemblance to Linear (the ⌘K sidebar, the Teams list, the side panel);
    - small type in a dense panel.

**Process findings (round 4)**
- **F-003 (gap):** the Mobbin references for this kind of screen are demo accounts with empty data, so the blind test mostly measures data richness; ours won it from round A while the strict audit stayed at 3.
- **F-004 (bug):** the warning role reads as brown (`#845d00` text on a cream `#f8f4ed`), the owner's banned combination, even with cool neutrals; the late state uses the danger role instead.
- Fresh audits do not converge after about four rounds: each finds new nits and some reverse earlier ones. A score from an AI reviewer can only rule work out, and the owner's eye has to decide this one.

## Round 5 (owner hid it until better, 2026-10-18)
**What he said:** hide it until it passes at 4; it won the blind test, but the fresh reviewer stayed at 3: mostly grey so it could read as a wireframe, a family resemblance to Linear (the ⌘K sidebar, the Teams list, the side panel), and small type in a dense panel.

**The idea in one sentence:** the head of product sees Christmas slot booking open in place on the roadmap, forecast 8 days past its target, and chooses whether to cut 7 issues or move the date.

**What changed (its own structure):**
- **No sidebar, no side panel.** A top bar with the workspace and the product's own tabs (Roadmap, Projects, Check-ins, Capacity), a page head with the one summary line ("14 scheduled projects in 5 teams · 2 forecast late"), and the roadmap at full width.
- **The project being decided opens in place,** as a band inside the timeline: on the left, Tue 8 Dec at 29 px with "8 days past the 30 Nov target", 41 of 89 closed and the pace, and the decision ("To keep 30 Nov, cut 7 of 48 open issues": Move target, Choose 7 to cut); on the right, its own bar with its checkpoints, only the two late ones labelled (Load test, 9,000 bookings/min: due 22 Oct, forecast 28 Oct; Open to all customers: due 30 Nov, forecast 8 Dec). The check-in text and the legend footer are gone.
- **Every bar runs from its start to its forecast:** solid petrol up to today, petrol tint after today, red past the target; a tick marks each target, so slack and overrun read on a date axis. A project with no forecast shows its plan as a dashed outline; Cold-chain scan says "Too early". The issues-closed fill is gone (an auditor noted it ran past today on a date axis).
- **Colour jobs:** petrol for work, red for late, ink for the one primary action and the today pill; the today line is 1 px secondary ink.
- **Type up:** IBM Plex Sans 13 / 15 / 17 / 24 / 29 (was 12 / 14 / 17 / 29). Months sit at their first Monday; one line per week.

**Engine:** `set overrides.font.size.15` and `overrides.font.size.13` (both `--set-by delegated`), then `build`: passes, 0 warnings.

**Figures, re-added from the page:** 4 + 3 + 3 + 2 + 2 = 14 scheduled (Loyalty and Payments are cropped at the bottom, through repetition); 2 forecast late (Christmas slot booking 8d, Offline delivery proof 11d). Every "vs target" is forecast minus target (26 Oct − 29 Oct = 3d early … 23 Nov − 12 Nov = 11d late). From 15 Oct to 30 Nov is 46 days; at 25 issues in 28 days that closes 41, so 7 of the 48 open must go; the 48 take 54 days at that pace, which lands on Tue 8 Dec.

**References (Mobbin, structure only; also the blind-test references):** Linear project timeline https://mobbin.com/screens/c1cc22aa-69de-468c-b200-cf80f05ac1c7 (the structure to move away from: sidebar, side panel), Jira timeline https://mobbin.com/screens/45d3b32a-ed07-481f-bb37-8712b7cd546c (a work column beside bars and a today line), Productboard roadmap https://mobbin.com/screens/89e63446-9567-41d3-bdc2-f7d6aa88e394 (items placed by time in swimlanes; also what to avoid: cards and chrome with nothing leading).

**Contrast:** petrol 5.7:1 on white, the tint bars' edge 3.7:1, red marks 4.6:1, grey and red text on the open band 6.5:1.

**A. Blind pairwise:** Linear +2, +3, +2; Productboard +3, +3, +3; Jira +2, +2, +3. **Passes.** The judges' one steady complaint was small, dense table type.

**B. Fresh-eyes audit:** **3.5, 4, 3.5. Does not reliably reach 4 after three rounds.**
- Round 1 (3.5): the axis read "Sep 31" and "Dec 30"; the closed fill ran past today; two forecast markers; the freeze hatch broke across the band.
- Round 2 (4): "it no longer reads as Linear"; plan-only bars looked like tinted ones (now dashed); too many callouts (now only the late ones); projects not indented under teams; "–" with no reason.
- Round 3 (3.5): "the Linear look is gone"; the open band is the new dense panel (five markers, two callouts, target tick and ring on one x); the 2 px black today line outranked the forecast; "Everyone else" unclear; an orphaned "open issues". Applied after it, not audited again: the today line is 1 px secondary ink, the checkpoint is "Open to all customers", and "open issues" stays together. Not applied: fewer markers on the open bar (round 2 asked to keep them as plain rings).

**Checks:** `check_dates.py --year 2026`: every weekday matches. `check_names.py`: 0 errors ("Check-ins", "Roadmap" are UI words). `preflight.py html`: 0 errors, 0 warnings (13/15/17/24/29). `engine.py validate` passes. Gallery copy at 337 px: the eye lands on the long petrol bar ending in red, then Tue 8 Dec.
