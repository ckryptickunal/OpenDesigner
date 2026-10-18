# 01 · Glassmorphism · Kadrel asset review

Kadrel, a brand-asset review tool: glass only on the controls that float over a campaign photo, which is the content. Fresh audit after the polish round: 4 of 5.

The "Round 3 (polish)" section of 2026-10-15, the last one, describes this page. The polish round of 2026-10-14 before it describes the version that round started from. The sections between record the first build, the Corvale revenue overview that the independent audit scored 3.

**Final score: 4 of 5** after three rounds (3, then 3.5, then 4). Render: 1440 x 900 at scale 2 (`shot.png`).

## Direction
Corvale is a fictional subscription-billing platform. This is the Revenue overview for one of its customers, Halyard Analytics: MRR, churn, failed-payment recovery and invoices, on the workspace backdrop the finance team chose (a mountain photograph at dusk). The audience is a finance lead or founder checking the month on a Tuesday morning. Mood: calm and expensive, like a good watch face at night.
Feel words: **premium, calm, precise** (the engine dropped "precise"; see findings).

## References (Mobbin, cited by link only)
Mobbin has no B2B product built in glassmorphism. The best glass examples are consumer iOS screens; the structure came from billing products.

| Reference | What it taught |
|---|---|
| Stripe billing overview, https://mobbin.com/screens/80db4fcd-360a-4ee9-8be0-f69f7edf83f8 | The vocabulary and structure of a billing overview: MRR with a growth chart, the movement categories (new, expansion, contraction, churn), "Updated" timestamps. |
| Xero sales overview, https://mobbin.com/screens/d0d03469-ccdc-45bc-989c-8d61fa34a943 | An invoice status strip (draft, awaiting payment, overdue) with counts and amounts, then "customers owing the most". Became the Invoices widget. |
| GOAT product detail (iOS), https://mobbin.com/screens/fcfcd85a-3191-4e0e-b0cb-02ac3f076210 | Real data on glass over a photo: a 3-cell stat grid in hairline boxes inside a frosted panel. Taught that the glass can carry numbers if the type is plain and the panel is dimmed. |
| Grok video settings (iOS), https://mobbin.com/screens/e3b57312-5759-4536-b0b8-c3ef7f967da6 | Dark smoked glass over a photo, with nested controls in a denser glass. Led to the tooltip using the engine's denser control glass rather than stacking two clear panes. |

## System (engine)
```
init; standard override STD-visual-details-24 --why "Style study: frosted glass shown only over one dark photographic backdrop"
sketch --name Corvale --brand #5CE1B4 --audience regular --platforms web --feel premium,calm,precise --theme dark-only --surfaces "billing app:operate" --delegated all
set raw.brandColor "#5CE1B4" + raw.flags.brandExact true   (sketch had swapped the mint for teal #008564)
pick Q-dir-01 glass; set raw.glass true
set raw.textFace "Manrope"; raw.displayFace "=textFace"; raw.monoFace "Manrope"; raw.numericStyles true; raw.fontLicence (all true)
build
```

| Dial | Value | Why | Expresses the style? |
|---|---|---|---|
| depth | 95 | Materials band: this is what turns on `material.glass.blur` and `surface.glass*` | Yes, the switch for glass |
| roundness | 78 | Widget corners like OS widgets | Partly: the roles stop at 24 px; the 28 px widget radius was taken from the scale by hand |
| colorfulness | 30 | The photograph carries the colour; the UI is white glass plus one mint | Yes |
| expression | 55 | A style study; the data stays plain | Indirectly |
| brandPresence | 35 | Mint only on positive movement and the one primary action | No |
| density | 45 | Gaps wide enough for the photo to show between widgets | No |
| energy | 30 | Calm money, no bounce | No |
| warmth | 20 | Cool neutrals under a teal photo | No |

**What the dials cannot express:** how clear the content glass is (the engine's glass is a 72% control material), the rim of light on the top-left edge, backdrop saturation, grain, the photograph itself and its crop, and text contrast over a backdrop that changes under every pane.

**Fonts.** Manrope only (SIL OFL, Google Fonts), tabular figures throughout. Weights: 300 for the big figures and the page title, 400 body, 500 to 600 labels.

**Type scale (6 sizes, none within 10%).**

| Role | Size | Use |
|---|---|---|
| Display | 56 (outside the scale) | MRR figure |
| Headline | 34 | Page title, recovery rate |
| Title | 27 | Churn and retention rates |
| Body large | 18 | KPI values, wordmark, invoice counts |
| Body | 14 | Rows, nav, buttons |
| Caption | 11 | Meta, axis labels, invoice ids |

## Where I stepped outside the tokens, and why
- **Content glass:** white 11% to 5% over the engine's 35% dimming token, with a 1 px rim gradient (white 42% top-left fading to 7%) and `saturate(160%)`. The blur is the engine's 24 px token.
- **Ink steps on glass:** white at 100 / 86 / 76%. The engine's text roles are solid hexes made for solid surfaces.
- **Photo treatment:** a real Unsplash photograph (photo-1485470733090), hotlinked as Unsplash asks, scaled 1.35x so the summit stands in the open band above the widgets and the ridge continues behind the glass. Side vignettes (black 62% to 0) keep the text on the open photo at 4.5:1.
- **Grain:** an SVG turbulence overlay at 14%, part of the frosted material.
- **56 px display figure** (the scale stops at 34).
- `review` still counts 41 hard-coded values, 23 of them the glass alphas above.

## Checks
- `engine.py validate`: no errors. Two warnings about **light** mode, a mode this dark-only system does not have (finding 5).
- `preflight.py html --medium web`: 1 error, M9 "Manrope has no @font-face". This is a false positive: it loads from a Google Fonts link.
- `engine.py review`: no standard breaks after round 3 (100vh → 100dvh, 1 to 3 px spacing moved onto tokens).
- **Contrast as rendered.** I wrote a check that hides all text, re-renders, and compares each text run with the brightest 5% of the pixels behind it.
  - Round 1: **13 failures**. The worst was 2.47:1, "Active subscriptions" over the snowy ridge.
  - Final: 119 runs, 0 failures. The lowest is 5.28:1 (an 11 px caption on glass).
  - `validate` and preflight passed all 13 failures, because neither tool can see a backdrop.
- **Facts.** The figures below were checked against each other:
  - MRR movements add up: 1,230,570 + 38,420 + 32,180 + 2,940 − 9,860 − 14,770 = 1,279,480.
  - Net new is 48,910, which is +4.0%.
  - ARR is 12 x MRR = $15.35M.
  - Average per account is 1,279,480 / 2,350 = $544.
  - Revenue churn is 14,770 / 1,230,570 = 1.20%.
  - Net retention is (1 + 0.614%)^12 = 107.6%.
  - Failed payments add up: 21,460 + 6,940 + 2,880 = 31,280, and 68.6% of that was recovered.
- Accessibility: a solid fallback under `prefers-reduced-transparency`, a visible focus ring (accent 11, 2 px), the chart and churn bars have text alternatives, and every control is at least 32 px.

## Self-audit (making.md sections 5 and 11)
Each round compared the render with Stripe, Xero and GOAT at the same width.

1. **Round 1 (score 3).** It read as a generic dark dashboard with slightly see-through cards. The photo was hidden behind the panes, so there was no glass moment. Other faults:
   - The search placeholder wrapped onto two lines.
   - The tooltip sat on the chart line.
   - The waterfall started from a cut-off base ($1.2M), so a 4% month drew the closing bar 2.6 times the height of the opening one.
   - The churn widget had empty bands.
   - "$1,279,<small>480</small>" read like cents.
2. **Round 2 (score 3.5 to 4).**
   - Recomposed around the photo: the summit stands in the open band and the ridge runs on behind the widgets. Now the blur shows a real shape continuing into the glass.
   - ARR, subscriptions and average per account moved onto the open photo as small true data.
   - The waterfall became a 5-cell MRR bridge with bars to one scale, and the MRR figure is set in one size.
   - Measured contrast as rendered and fixed all 13 failures (vignettes, ink steps, tile tint).
3. **Round 3 (score 4).**
   - A monotone curve replaced S-shaped wiggles that implied dips that never happened.
   - The tooltip moved above the end marker and is drawn after fonts load (it had drifted onto the headline).
   - The tooltip now uses the engine's denser control glass: the house rule says never to stack two clear panes.
   - Added a 1.50% target line to the churn bars.
   - Moved sizes and colours onto tokens.

**Tells from section 11, final state.**
- Glow with no job: removed the halo on the end marker. The only soft light is the rim, which is the material.
- Texture standing in for an asset: the grain stays, at 14%, over a real photograph.
- No decoration without data, no invented proof, and status is said once, as coral text.
- **Remaining weakness:** a real billing product would rarely put its numbers on a mountain photo. The "workspace backdrop" setting is the in-world reason, but it is still a showcase conceit. Also, the lower panes over the dark foreground read more like smoked plastic than glass.

## The style
- **Plain words:** panels look like frosted glass laid over a picture. You see a soft, blurred version of what is behind each panel, and the panel's edge catches light.
- **What defines it (checkable):**
  1. A real, varied backdrop behind the panels, either a photo or content, never an empty gradient.
  2. Panels fill at 5 to 20% white (or dimmed dark) with a `backdrop-filter` blur of 16 to 40 px and extra saturation.
  3. A 1 px rim brighter on the lit edge.
  4. A soft shadow that separates the pane from the backdrop.
  5. Shapes behind the glass continue visibly into it.
- **How it goes wrong:**
  - Coloured blobs painted only so the blur has something to show (section 11's top tell).
  - Glass on glass on glass.
  - Text contrast checked against the average backdrop instead of the brightest spot.
  - Every surface made of glass, so nothing is.
  - Glass on a flat colour, where it turns into plain grey.
- **How I kept it premium:**
  - One real photograph composed with the layout: the summit sits in the open, and the ridge crosses three panes.
  - One family (Manrope) at light weights for big figures.
  - One accent with one job: mint means money going up.
  - Data plain and dense enough to be a real product.
  - Contrast measured at the worst pixel, not the average.
  - A solid fallback for reduced transparency.

## Process findings
Each was recorded with `engine.py feedback` in `opendesigner/feedback.md`.
1. **(gap) Glassmorphism has no home.**
   - The glass preset is Apple's control material: `surface.glass` is 72% opaque, "controls and navigation only, never content".
   - The style puts content on clear glass. It needs a fill-opacity token, a rim, saturation, grain, and a contrast rule for a variable backdrop.
2. **(gap) Neither validate nor preflight can see a backdrop.** A rendered-pixel check found 13 failures (worst 2.47:1) that both tools passed.
3. **(bug) `sketch --delegated` swapped the brand mint #5CE1B4 for teal #008564** so that white text would pass, and said only "I picked a teal". On a dark system the mint carries dark text, so the swap was not needed. This is the same bug as Orbika's lime.
4. **(bug) `raw.monoFace "=textFace"` is written literally** into the CSS (`--ds-font-family-mono: =textFace, ui-monospace…`). `displayFace` accepts the alias; `monoFace` does not.
5. **(bug) A dark-only theme still writes a `[data-theme=light]` block,** and validate warns about light-mode contrast.
6. **(bug) DESIGN.md drops alpha in the dark column.** For example, `surface.glass` shows `#22252b` while the token is `rgb(34 37 43 / .72)`.
7. **(gap) The feel word "precise" is unknown,** and it is common for finance and tools.
8. **(repeat) Preflight M9** gives a false positive for Google Fonts links.
9. **What helped:**
   - `pick Q-dir-01 glass` plus depth 95 gave exactly the right blur, dimming and fallback tokens.
   - The 35% dimming rule (S-L15-073) was the right starting point for contrast over a photo.
   - The house standard "never stack translucent surfaces" caught the tooltip.

## Polish round 2026-10-14
**Fresh audit: 4 of 5.** Two fresh-context reviews both scored it 4. The independent audit had given the first build 3. Render: `shot.png`, 1440 x 900 at scale 2.

### What the audit asked for
- Glass on every reading surface, so the style disappeared, and a mountain photo standing in for content.
- A generic three-column widget dashboard.
- A euro invoice inside a USD total, and month-to-date churn labelled "Last 30 days".
- Corvale is one letter from Corvane (`product/03`), and Halyard was reused.

### What changed
- **A product whose content is the photograph.** Kadrel is a brand-asset review tool. The screen reviews one campaign photo for a fictional cabin company, Siljevik Cabins, shown whole at Fit (17%).
- **The one idea only this product has: placement crops.**
  - The selected crop (Web hero 21:9) is drawn on the photo. Outside it is dimmed, its headline zone is hatched, and the focal point is marked.
  - All four crops (Web hero 21:9, Billboard 3:1, Feed 4:5, Story 9:16) sit below the photo as thumbnails in their true ratios, each with its status.
- **Glass on one layer only,** as iOS does it. The controls that float over the photo are glass: the top bar, the tool palette, two crop labels and the zoom. The placements strip and the inspector are solid reading surfaces.
- **A real asset with true metadata.**
  - The photo is by Peter Schulz on Unsplash (photo-1754293193520, "Red shack on a lake with a pier", near Mora, Sweden, Unsplash Licence).
  - 6240 x 4160, Canon EOS 6D Mark II and the 8 Jul 2025 capture date come from the image's own metadata (`images.unsplash.com/...?fm=json`, DateTimeOriginal).
- **The glass recipe uses tokens where the engine has them:**
  - blur `--ds-material-glass-blur` (24 px);
  - tint is the engine's 35% dimming token;
  - fill white 12% to 4%, a rim and `saturate(180%)` are set by hand;
  - a solid fallback under `prefers-reduced-transparency`.
- **Names.**
  - Gone: Corvale, Halyard Analytics, Okapi Robotics, Lumenfield Health, Parcel & Pine, Ferro Labs.
  - New: Kadrel, Siljevik Cabins, Signe Aldén, Rhys Marsh.
  - The first name tried, Darkslide, was dropped: the first fresh audit found Darkslide Productions, a real stills and motion studio for brands. Kadrel, Siljevik Cabins, Signe Aldén and Rhys Marsh returned no match in the same field.
- **Fixes after the first fresh audit (4):**
  - The footer now acts on the selected crop ("Approve web hero"). It used to say "Approve story" while showing Web hero.
  - The comments no longer contradict each other. A right-aligned headline would have covered the lifebuoy that the next comment asks to keep. "The only red besides the shed" was false: there is a red barrel and a red mark on the trunk.
  - Added a Releases line, since no property release is on file and a building is visible.
  - Moved the tool palette off the brightest sky.
  - The strip now shows the go-live date, and a short History replaces an empty gap.
- **Fixes after the second fresh audit (4):**
  - "covers the shed" is now white at 700. It was pink, at about 4.6:1.
  - Pin 2 no longer covers the lifebuoy it is about.

### System (engine)
```
set name "Kadrel"; pick Q-scope-06 "asset review:operate"; pick Q-dir-01 glassmorphism
build
```
State now records `style: glassmorphism` on the glass preset. The dials are unchanged: depth 95, roundness 78, colorfulness 30.

### References (Mobbin, by link only)
| Reference | What it taught |
|---|---|
| Air asset viewer, https://mobbin.com/screens/98217c4d-ba19-4ef8-af76-7a4834172567 | The layout: a dark viewer, floating tools, and a solid Info and Comments panel. |
| Shopify focal point, https://mobbin.com/screens/06a322b7-84c5-4994-b3af-98443b6c3a76 | A focal-point dot with a hint chip, and an info card. Kadrel shows what the focal point does by placing four crops around it. |
| Frame.io review, https://mobbin.com/screens/79b23a07-f804-4e09-b554-f05ea13d814f | A breadcrumb, a comments panel and a status per asset. |

The fresh audits also compared it with Later (crop presets per placement, https://mobbin.com/screens/9af19631-f96d-418f-ae93-9d6d82bc5f39) and DoorDash Merchant (a crop with an as-it-appears preview, https://mobbin.com/screens/2afdeed5-654d-490d-b0f8-add960425f22).

### Checks
- **Contrast as rendered.** The check hides the text, renders again, and compares each run with the brightest or darkest 5% of the pixels behind it.
  - 73 runs, 0 below the floor. The lowest is 5.05:1, the breadcrumb slashes on the glass bar.
  - The same check passed with the engine's 35% dimming token, so the hand-set 44% tint was dropped.
- **Weekdays.** `check_dates.py --year 2026`: every weekday matches (Fri 9 Oct 2026, Mon 26 Oct 2026). Without the year written next to them, the tool took 2027 and 2025 from "Summer 2027" and the photo date nearby, and flagged both. That is a false positive of the tool.
- **Facts re-added from the page.**
  - The crops are 6240 x 2674 (21:9), 6240 x 2080 (3:1), 3328 x 4160 (4:5) and 2340 x 4160 (9:16). Each is big enough for its output size.
  - Zoom: 1060 / 6240 = 17%.
  - Counts: 2 of 4 crops approved; 3 comments on 2 pins.
  - 14 to 26 October is 12 days.
- **Tools.**
  - `engine.py validate`: no errors. The 2 light-mode warnings are on a dark-only system, as before.
  - `review`: 39 hard-coded values, mostly glass alphas and control sizes.
  - Preflight: M9 only. That is the known false positive for a Google Fonts link.

### Remaining weaknesses
- The overlay on the photo is busy: dimming, hatch, corner ticks, focal point, pins and chips. Every mark carries data, though.
- The inspector will crowd after three or four comments. A shipped tool would put Info and Comments on tabs.

## Round 3 (polish) 2026-10-15
**Fresh audit: 4 of 5** against the B2B product screens (`product/01`, `02`, `04`, `06`). Render: `shot.png`, 1440 x 900 at scale 2.

### Why this round
The piece still carried "Being rebuilt" on the public showcase. The owner's bar is the B2B product screens: one accent with one job, real dense content, exact spacing, legible type. The audit's own fixes were done in the polish round of 2026-10-14; this round closed what stood between that page and the bar.

### What changed
- **Captions moved from 11 px to 12 px, through the engine.** The 1.25 ratio on a 14 px body put 34 text runs at 11 px, below the 12 px the B2B screens use. `pick Q-type-09 1.2` rebuilt the scale as 12, 14, 17, 20, 24, 29, 35; the page now uses 12 (captions, labels), 14 (body) and 17 (the asset title). No size is outside the scale.
- **A quieter headline zone.** The hatch over the left 40% of the crop dropped from 1.2 px lines at 38% every 8 px to 1 px lines at 22% every 12 px, with a lighter tint. The dashed edge and the glass label still mark the zone; the shed under it reads again. This was the first "remaining weakness" of the last round (a busy overlay).
- **Two orphan wraps fixed** after the bigger captions: the camera line ("... Mark" / "II") and the footer ("... crops" / "approved.") are reworded to fit on one line each.
- **After the first fresh audit (4 for the source; the committed render was stale):**
  - The headline zone is a flat 15% tint with its dashed edge; the hatch lines read as scratches on the shed roof.
  - The focal point is a ring and a dot; its four arm ticks touched the zone's edge.
  - Both crop chips sit on the 16 px edge shared with the bar and the tool palette (they were at 12 and 80 px).
  - Small glass blurs less than big glass: chips and zoom at 14 px, the bar and palette at the engine's 24 px (`styles.md`: bigger surfaces, stronger blur). The engine has one blur token, so 14 px is set by hand.
  - The inspector's empty band moved: the reply box follows the comments, and History keeps to the bottom above the footer.
  - History reads like Rights: muted dates, ink events.
  - Copy labels instead of narrating: "4 crops, auto-placed around focal point 38%, 53%"; "Property release not on file"; "Approve Web hero", matching the placement's name.
- **After the second fresh audit (4):**
  - **The headline zone reads at a glance:** a 34% dark scrim over the left 40% of the crop, with the template's headline block ghosted in white (two lines and a button) where the layout would set it; the label sits on the zone's top edge and says "overlaps the shed", which is what the dashed edge shows.
  - **Even placements:** pictures 80 px tall with equal 48 px gaps; name, ratio and size, and status on three caption lines that may overhang into the gap, so a caption never widens its column.
  - **A footer that matches the state:** "Waiting on Rhys · due 14:00" with a Remind button, instead of offering Approve and Request changes on a crop whose changes are already requested.
  - **The inspector has no dead band:** History follows the comments and records the upload (Fri 9 Oct, 4 crops placed); the reply box is pinned above the footer.
  - **One edge:** the strip pads 16 px, like the glass overlays.
- **After the final fresh audit (4, "a low 4"):**
  - The ghost headline is 66% white, so it reads as a placeholder rather than a redaction bar, and pin 1 sits on the shed roof, clear of it.
  - The darkening outside the crop is 45% (was 58%), so the glass over it reads as glass, not grey pills.
  - Comments and Activity are tabs. The thread has two more true replies: Signe keeps the 21:9 crop; Rhys notes that Feed and Story cannot keep the lifebuoy (Feed spans 11 to 65% of the width, Story 19 to 57%; the buoy is near 90%). The reply box sits under the thread, and the history moved into the Activity tab.
  - Placement columns are at least 112 px with 32 px gaps, so no caption crowds the next picture; the selected picture has an inset ring on the 16 px edge.

- **After a last regression check (holds at 4):** no regression found; the lifebuoy claim was re-checked against the crop spans.

### System (engine)
```
pick Q-type-09 1.2 --why "captions at 12 px, as the B2B product screens"
build
```

### References (Mobbin, by link only)
| Reference | What it taught |
|---|---|
| Air, https://mobbin.com/screens/e2b11887-ecc9-4be2-abd8-ee714db2e7ae | Dark asset viewer with a solid info panel. |
| Higgsfield, https://mobbin.com/screens/ce861b55-1645-4413-8942-6f627d73b953 | Glass tools over media, reply box under the comments. |
| Ghost, https://mobbin.com/screens/092f62e5-6f39-4a6b-8189-934b7bab5a12 | Quiet darkening and handles in a crop editor. |

### Checks
- **Contrast as rendered** (text hidden, each run compared with the worst 5% of pixels behind it): 77 runs, 0 below the floor; lowest 4.99:1, the "Headline zone" label on its glass chip. The breadcrumb slashes went from 70% to 85% white when the darkening outside the crop was lightened (they had dropped to 4.55:1).
- **Weekdays:** `check_dates.py --year 2026` passes (Fri 9 Oct, Mon 26 Oct 2026).
- **Facts re-added:** crops 6240 x 2674 (21:9), 6240 x 2080 (3:1), 3328 x 4160 (4:5), 2340 x 4160 (9:16); zoom 1060 / 6240 = 17%; 2 of 4 crops approved; 5 comments on 2 pins; 14 to 26 October is 12 days.
- `engine.py validate`: no errors (the 2 light-mode warnings are on a dark-only system, as before). Preflight: no type or font errors.
