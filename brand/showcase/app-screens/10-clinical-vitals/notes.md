# 10 · Vigil: ward vitals (tablet, 1180×820 @2x)

## Direction
Vigil is a fictional ward dashboard for the nurse in charge on a night shift, used on an iPad at the nurses' station. The screen shows Ward 4B: a patient list sorted by early-warning score (NEWS2), the selected patient (bed 7, NEWS2 7, urgent review), an escalation banner with a response countdown, six vital-sign tiles with 2-hour traces against the usual range, and a 12-hour NEWS2 strip. Clinical clarity comes first. **Status never relies on color alone**: every state has a shape and a word (green circle with a check and "In range" or "Low", amber triangle and "Watch" or "Medium", red octagon and "Urgent" or "High"), plus the score as a number. Feel words: **trustworthy, clean, accessible**. All patients and staff are fictional.

## References (Mobbin, structure only)
- [Google Health, heart-rate zones](https://mobbin.com/screens/53fdd39a-62b9-4048-a26a-8b6bb27976c5): threshold lines on a trace, so a value reads against its limits.
- [The Outsiders, heart rate](https://mobbin.com/screens/759363a4-d740-46ac-b90e-84020a56990f): a big value, then one sentence about the normal range, then the band.
- [Better Stack, monitor](https://mobbin.com/screens/b677964b-252f-47a8-8495-40501138635c): status tiles above live charts.
- [OpenAI, service health](https://mobbin.com/screens/d605f83d-3869-4ecc-8874-b913e09e2930): a status row as icon plus word, and an incident list.

Mobbin has no clinical or ward software, so the references are health trackers and monitoring dashboards. The clinical structure (NEWS2 scoring, escalation, observation timing) follows the public NEWS2 scheme. The values are invented and only meant to be plausible.

## System (engine)
```
sketch --name "Vigil" --brand "#0B7A84" --audience regular --platforms ios --feel trustworthy,clean,accessible --delegated all
set raw.neutralTint cool · set raw.chartPalette categorical-8
set raw.textFace "Atkinson Hyperlegible Next" · set raw.monoFace "Atkinson Hyperlegible Mono" · set raw.fontLicence {...}
build → Passes: no errors, 1 warning (a macro conflict that persists after the dial was set; an engine bug)
```
| Dial | Value | Why |
|---|---|---|
| expression | 18 | nothing decorative |
| brandPresence | 22 | the data leads |
| density | 66 | 13 patients and 6 vitals on one tablet screen |
| energy | 28 | calm; only alerts stand out |
| roundness | 40 | control 6, container 8, overlay 12 |
| depth | 20 | flat tiles with borders |
| colorfulness | 35 | color is kept for status |
| warmth | 30 | cool, clinical |

## Fonts and type scale (two faces)
Atkinson Hyperlegible Next (text, OFL; designed so 1/l/I and 0/O never confuse, which matters for doses and vitals) and Atkinson Hyperlegible Mono (OFL), used only for data: bed numbers, scores, clock times, the countdown and the NEWS2 cells. iPadOS roles, 5 sizes:

| Role | Size / weight | Used for |
|---|---|---|
| Large title | 42 Next 700 | vital values, NEWS2 octagon |
| Title 1 | 29 Next 700 | patient name |
| Title 2 | 24 Next 700 / Mono 600 | brand, "Patients", countdown |
| Body / headline | 17 Next 400-700 | names, banner, buttons, NEWS badges |
| Footnote | 14 Next / Mono | ranges, sublines, chips, hour labels |

## Color
Cool light greys, near-black ink and one teal for selection and the brand. The status colors come from the engine: success `#208643`, warning `#e9b452` (dark text on it), danger `#be544b`. Chart lines use `chart.categorical` steps; the usual-range band uses `bg.success.subtle`.

## Where I left the tokens, on purpose
- The traces are SVG built in script from token colors. The live dot pulses 6 times and then stops (no endless loop; still under reduced motion).
- The octagon is a CSS `clip-path` shape. As an SVG behind the number, it read as 1:1 contrast to the probe.

## Changes for the owner's type and color rules
- The scale went from 7 sizes (14, 17, 20, 24, 29, 35, 42) to 5. The brand and "Patients" moved from 20 to 24, and the octagon number from 35 to 42.
- Big values moved from the mono to the text face, with tabular figures, so mono is kept for data labels.
- The patient-row gap was tightened so names are never cut with an ellipsis. A cut patient name is a safety issue, not just style.

## Checks
- `engine.py validate`: no errors; 1 warning (the macro-conflict bug, below).
- `preflight.py html`: 1 error, M9, a false positive. Atkinson Hyperlegible Mono loads through the Google Fonts link; the browser reports both faces `loaded`.
- Review probe: it caught the octagon contrast misread, an h1 → h3 skip (fixed with h2), an endless pulse animation (fixed: 6 beats) and a truncated name (fixed). Now: 0 errors and 0 warnings. Hover styles were added.

## Process findings
- **Bug:** the macro-conflict warning ("serious, minimal, everyday pull colorfulness in opposite directions") stays after `dials.colorfulness` is set explicitly. (feedback recorded)
- **Gap:** status colors cannot be pinned. Danger is a muted brick `#be544b` at Colorfulness 35 and 55 (`#c94c43` at 75). A clinical product needs a crisp alarm red without saturating the brand. (feedback recorded)
- **Gap:** there are no Mobbin references for clinical software, so the domain structure came from my own knowledge of NEWS2. It is flagged here as not checked against a live clinical source.
- **Helped:** `chartPalette categorical-8` gave six distinguishable trace colors; `neutralTint cool` and the status set worked with no hand-tuning.
