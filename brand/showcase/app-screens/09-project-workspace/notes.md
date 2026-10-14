# 09 · Quarry: project workspace (desktop, 1440×900 @2x)

## Direction
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
