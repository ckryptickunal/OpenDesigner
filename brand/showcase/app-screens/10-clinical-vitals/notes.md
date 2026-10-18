# 10 · Vigil: ward vitals (tablet, 1180×820 @2x)

Gallery: Wardlight is a fictional ward dashboard for the nurse in charge on a night shift, on an iPad at the nurses' station.

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

## Round 3 (owner review, 2026-10-14): rebuilt as Wardlight
**What he said:** "needs a lot of work." The brief asked to study shipped clinical and dense monitoring screens and rebuild properly.

**Research.** Mobbin has almost no clinical software (searches for EHR, ward and patient monitoring returned scribes, HR and analytics tools), so the structure comes from the Royal College of Physicians' NEWS2 observation chart, where each value's cell is shaded by its parameter score, and the dense parts from monitoring tools: Bevel https://mobbin.com/screens/cf175d8e-0c46-4461-90cb-3c5163d9349a (each vital as a value with its normal range and a trend), PlanetScale https://mobbin.com/screens/ef455d28-04ea-46f4-a289-cb6c283ea929 (a dense table with a sparkline per row), incident.io https://mobbin.com/screens/4998988c-03a6-4a50-85f4-1ba0d6b9bca3 (an alert with its escalation and acknowledgement state).

**What changed:**
- **Name.** "Vigil" is a real company in this field (Vigil Health Solutions, nurse call and resident monitoring), so the product is now **Wardlight** (`set name`; a web search found no product of that name). Surnames shared with other pieces (Lindqvist, Nakamura, Ferreira, Adeyemi) were replaced.
- **The NEWS2 maths was wrong before.** The old tiles scored 7 while their own sub-scores (with 2 for oxygen) added to 11. Every value is now re-scored against the RCP 2017 thresholds: totals 2, 4, 5, 6, 7, 8 for 22:00 to 02:15, each cell shaded by its parameter score, checked twice by the fresh-eyes auditor.
- **The scene holds together:** status bar 02:16 Wed 14 Oct (it said 9:41 Tue 14 Oct); NEWS2 7 at 02:00 led to an emergency call at 02:04; the registrar paged 02:04 (12 min, not acknowledged) and critical care outreach paged automatically at 02:14; obs every 15 min with a live 02:15 column; the sepsis screen (positive 01:05) and a non-penicillin antibiotic (patient is penicillin-allergic) are in the timeline.
- **Layout:** an iPad split view. The sidebar is "Ward 4B" with search, "Needs action · 3" (two-line rows) and "Low risk, 0–4 · 10" (one-line rows), 13 patients in 14 beds with bed 3 free. The detail is the patient header (NEWS2 said once in text), an escalation card (one line per page, a timeline of actions, one filled button), and the observation chart with a trend per row.
- **Status said once, colour with one job:** six vital tiles with borders, badges, dots and categorical trace colours are gone. A three-step ramp marks parameter scores 1, 2, 3; totals 5–6 get a thin amber bar and 7 or more a red chip; teal is selection and the one filled action.
- **Type:** one app face, Atkinson Hyperlegible Next, regular weight except the score that matters and the time since paging; the status bar is in the system face. Roles: Title 1 28 · Title 3 20 · Body 17 (every value) · Subheadline 15 · Footnote 13. The mono face is no longer used. `overrides.font.size` 13/15/17/20/28/34 and `dials.density` 60 through the engine.

**Fresh-eyes audit** (fresh-context agent, against the B2B product screens and the three references, re-scoring NEWS2 from the RCP sources): **3/5** for the first rebuild (a 30-minute emergency window, score said five ways, bold everywhere, 15 pt values, the timeline missing), then **4/5** after the second, with five items (score-2 amber too loud, NEWS2 repeated in the timeline, sepsis screen late not due, pages without their own status, outlined chips), all applied after it. A final check kept **4/5** with three small items, also applied: score-1 cells got a hairline so they hold on a dimmed screen, "01:20 FY1 review" joins the timeline before the antibiotic, and T. Oyelaran is in NAMES.md.

**Checks:** `engine.py build` passes (1 warning: text sizes from the old formula steps). `preflight.py html`: no errors after the mono face was dropped. `check_dates.py --year 2026`: passes.

**Outside this folder:** `mockups/07-tablet-clinic/index.html` still says "Vigil" (title, comment, alt text, caption) and shows this shot.png; it needs the new name and a re-render.

## Round 4 (owner review, 2026-10-15)
**What he said:** "needs a lot of work" (earlier), and about the app screens now: "None of them should feel like they are from a vibe coded app or a cheap Chinese app." AUDIT-ROUND4 scored the round 3 shot 4/10: caramel and beige boxes on every value, slashed zeros, three bordered boxes stacked at the top.

**The one idea:** at 02:16 the nurse in charge sees that bed 7's emergency page has gone unanswered for 12 minutes.

**Device (needs the owner):** the round 4 brief asked for iPhone frames, and PRESENTATION.md wants one canvas per category. Wardlight is the nurses'-station iPad app and `mockups/07-tablet-clinic` shows it in a tablet, so it stays iPad landscape, 1180 × 820 pt at 2x, with iPadOS chrome (24 pt status bar with full battery, home indicator, 17 pt body, 44 pt targets).

**What changed (rebuilt in place):**
- **One face:** IBM Plex Sans (`raw.textFace`), tabular figures, no slashed zeros.
- **Red has one job, clinical risk.** Ink is the brand and action colour (`raw.brandColor` #1E2833). A NEWS2 parameter score is counted in dots beside the value (one for 1, two for 2; a 3 would be a solid cell); a total of 5 to 6 is outlined and 7 or more is solid, in the table, the sidebar and the header tile alike. Most cells stay white. The first rebuild filled every scored cell and blind judges called it "flooded with salmon".
- **The score sits with the patient** (a solid NEWS2 8 tile beside the name; "Up from 7 at 02:00" leads the facts line) and the penicillin allergy is a red-outlined chip.
- **Escalation:** the registrar and critical care outreach, both paged at 02:04, "No reply", 12 min (said once more in the card's subtitle, in ink); the filled action is "Page again". The card's last row is one line of what happened earlier: 01:05 sepsis screen positive, 01:20 FY1 review, 01:30 IV levofloxacin given (she is penicillin-allergic), 01:40 oxygen 2 L/min.
- **The table:** right-aligned values at 17 pt, the live 02:15 column marked by a 2 pt ink rule under its head, "Continuous · manual every 15 min" (RCP: continuous monitoring at 7 or more), and a key that lists only what is drawn. The trend column is gone: each sparkline had its own scale and even spacing over uneven times, which misled.
- **Sidebar:** the Wardlight mark with search and the sidebar toggle, Ward 4B, three "Needs action" rows with a status glyph (bell, clock, repeat), then the 10 low-risk patients with their next obs time; selection is white on grey with a hairline ring; every row 44 pt or more.
- Icons at one 1.5 pt stroke.

**NEWS2, re-scored against RCP 2017 (SpO₂ scale 1):** respiration, SpO₂, air or oxygen, systolic, pulse, consciousness, temperature.
- 22:00: 20 (0), 95 (1), air (0), 122 (0), 94 (1), A (0), 37.8 (0) = 2
- 00:00: 21 (2), 95 (1), air (0), 120 (0), 96 (1), A (0), 37.9 (0) = 4
- 01:00: 21 (2), 94 (1), air (0), 118 (0), 98 (1), A (0), 38.1 (1) = 5
- 01:30: 22 (2), 93 (2), air (0), 116 (0), 104 (1), A (0), 38.2 (1) = 6
- 02:00: 23 (2), 94 (1), oxygen (2), 112 (0), 108 (1), A (0), 38.3 (1) = 7
- 02:15: 23 (2), 95 (1), oxygen (2), 110 (1), 110 (1), A (0), 38.4 (1) = 8

Ward: 3 needing action + 10 at 0 to 4 = 13 patients. Next obs for the low-risk patients follow RCP minimum frequencies (4-hourly at 1 to 4, 12-hourly at 0).

**Type scale (iPadOS roles):** Large Title 34 (the score) · Title 1 28 (patient) · Title 3 20 (ward, section head, minutes since paging) · Body 17 (names, values, escalation title) · Subheadline 15 (sublines, labels, buttons, timeline) · Footnote 13 (column heads, bed numbers, times, key). Six sizes.

**Engine (this round):** `set raw.textFace "IBM Plex Sans"`, `set raw.brandColor "#1E2833"`, `dials.colorfulness 20`, `overrides.font.size.22` (the step was missing, so the ward title had silently fallen back to 17 px; now spare) and `.48` (spare), then `build` (passes; 1 warning: 13 text sizes from old formula steps). `preflight.py html`: 0 errors, 0 warnings. `check_dates.py` flags only "2017" (the RCP edition) in this file: false positives.

**Blind pairwise test** (same method; no ward-observation app is on Mobbin, so the nearest shipped work of the same shape: an alert with its escalation and a data view). References: incident.io https://mobbin.com/screens/16809a67-3ba1-423b-92a1-63c8eea209d5, Perplexity Health https://mobbin.com/screens/7e1d573a-6062-4c81-b4e9-b5d6a9fe46db, Sentry https://mobbin.com/screens/44f8570c-f154-4173-a40b-06d1adba7f00.
- First rebuild: ours won by 3 against Perplexity and Sentry; incident.io won by 2.
- With filled score cells: incident.io and Perplexity each won by 2 ("flooded with salmon"), so the score ramp became dots and outlines.
- Rounds after that, and the final round: ours won against Perplexity and Sentry by 2 to 3; incident.io won by 1 or 2, never by 3. Passes the rule.

**Fresh-eyes audit:** **3, 3, 4, 3** over four rounds. Every round re-scored NEWS2 and found it right. It caught misleading sparklines, the pink-tile table, a key that showed a score no cell had, the wrong button filled, red doing too many jobs, outreach paged 10 minutes late, a first-dose antibiotic on day 2, and a clipped last bed. The last round's items (one line of earlier events inside the card, "No reply" said once in ink, a rule instead of the tint on the live column, the key, the monitoring wording, a ring-only selection) were applied after it and audited in the focused pass below. The fourth audit scored 3; the focused pass below scored 4.

**Checks:** `check_dates.py --year 2026`: the page passes. `check_names.py`: 0 errors. Shot re-rendered at 1180 × 820, 2x.

**Outside this folder:** `mockups/07-tablet-clinic` shows this shot.png and needs a re-render; its alt text (NEWS2 8, the 02:04 call, the registrar unanswered for 12 minutes, the 22:00 to 02:15 chart) still holds.

**Focused pass (2026-10-18).** After the polish above: blind test, ours won against incident.io by 1, Perplexity Health by 2 and Sentry by 3. **Fresh-eyes audit: 4** ("the closest piece to the B2B bar: dense, mid-task, one face, edges aligned"), with every NEWS2 value and all 32 dots re-scored correct. Two of its items were applied after it: "Bed 7" leads the facts line (no "7 · 7" side by side) and rows sit on 40 pt and 56 pt pitches. Not applied: replacing the dots with a points column, an "Escalate to consultant" primary action, a grey allergy chip; the auditor marked the escalation one as its own judgment, not RCP text.
