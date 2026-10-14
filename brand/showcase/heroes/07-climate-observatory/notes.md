# 07 Isobath Ocean Observatory: climate data hero

**Direction.** Isobath is a fictional ocean and climate data institute. It runs floats, moorings and gliders in the North Atlantic and publishes the readings openly. The audience is scientists, journalists and policy staff who want to trust the numbers before they read them. Mood: a chart room at night. Feel words: **calm, precise, technical**.

Render: 1440 x 900 at scale 2 (`shot.png`).

## References (Mobbin, cited by URL only)
| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/cb2e0ca2-02bf-4362-b00f-07f093c0766f | Line-drawn topographic forms in one accent on a deep ground, with hairline ticks on the frame edge. I took the single-color line art and the edge ticks. |
| https://mobbin.com/sites/sections/9b6f664a-b824-4de5-9b81-54126c6a391e | A large headline with one tinted phrase, and mono data used as texture. Here the tinted phrase is the italic "record". |
| https://mobbin.com/sites/sections/38d3c862-d84c-4840-9fd0-94002eaf5571 | Restraint: one drawing, small mono captions, lots of dark. It kept the readouts few and quiet. |
| https://mobbin.com/sites/sections/ecdffa16-f143-4fe1-9232-bc3cdb8a3665 | A scientific visualization can be the whole hero when its color stays inside the brand palette. |

## System (engine)
```
init; standard override STD-visual-details-24 (dark-only)
sketch --name Isobath --brand #3FC1D9 --audience regular --platforms web --feel calm,precise,technical --theme dark-only --surfaces "landing page:persuade" --delegated all
```
| Dial | Value | Why |
|---|---|---|
| expression | 45 | Art-led, but scientific restraint |
| brandPresence | 35 | Data and map lead; brand recedes |
| energy | 20 | Calm, no bounce |
| roundness | 0 | Instrument hairlines, square corners |
| depth | 10 | Lines and type, no shadows |
| colorfulness | 30 | Cyan plus one warm signal (tried 50: no change, reverted) |
| warmth | 10 | Cold neutrals |
| density | 55 | Readouts are dense |

Other: `raw.neutralBase` #0E2A4A (navy tint; barely moved the base), `raw.primaryActionColor` #3FC1D9 (fixed a muddy dark-mode button), Q-dir-02 `spacious`.

**Fonts (final).** IBM Plex Sans: display at Light 300, and all words. IBM Plex Mono: data only. Both SIL OFL. The first render used Source Serif 4 as a third face (see the owner rules below).

## Art
The bathymetry is generated on canvas. Seeded value-noise fBm, plus a seamount, a ridge and a trench, is contoured with marching squares at a 5 px grid. Every fifth line is an index contour. Lines are drawn into a white mask, then colored by position: cyan everywhere, `danger-dark-11` coral inside the marine heatwave. Depth labels sit on a few index contours. A float track ends in a crosshair. Latitude ticks run on the left edge.

## Outside the tokens, on purpose
- The navy background (#041120 to #082039) and the scrims behind the copy and rail: the neutral ramp's base step stays grey (#131519).
- Display weight 300 (Plex Sans Light): the lightest heading weight the engine makes is 600.
- Headline at 95px uses `--ds-font-size-95` (on scale). Line art colors come from tokens (`accent-dark-11/12`, `danger-dark-11`); alphas are art.

## Checks
- `engine.py validate`: no errors. The 2 warnings are about light mode, which this dark-only system does not ship (a bug, filed).
- `preflight.py html`: 2 errors, both false. They are M9 "no @font-face" for faces loaded from Google Fonts.
- `engine.py review`: 7 raw values remain (the 80px nav height, the live-dot halo, and sizes inside sparklines); 1 standard was fixed (2px became `--ds-space-2`).
- Contrast on navy: body/secondary 7.6:1, primary 14.4:1, cyan line labels 7.7:1, coral 7.7:1, the CTA's dark text on cyan 8.5:1, and the edge ticks 6.3:1. Canvas depth labels are 12px and decorative (`aria-hidden`).
- Targets: nav links 40px, buttons 48px; focus ring from tokens.

## Process findings
1. **Navy can't be made.** `neutralBase` is capped and the base step is forced near grey. (gap)
2. **Colorfulness doesn't reach a brand-seeded ramp,** and the dark-mode button became a muddy teal. Only `primaryActionColor` fixed it, and nothing in the output said this would happen. (confusing)
3. **validate checks light mode for a dark-only system.** (bug)
4. **No light display weight** (the minimum is 600). (gap)
5. **"precise" was silently dropped** from the feel words. (bug)
6. **The rem-spacing standard conflicts with the px space tokens.** (bug)
7. What helped: the dark ramps are well balanced. Secondary text at 7.6:1 on navy came free. `danger-dark-11` is a beautiful warm signal. Plex Mono with tabular numbers, read from the mono face token, made the rail look like an instrument at once.

## Owner type and color rules (applied after the first render)
- **Fonts:** two only. Source Serif 4 was dropped, using `engine.py set raw.displayFace "=textFace"`. IBM Plex Sans now carries the display (Light 300) and all words. IBM Plex Mono is kept only for data: readout values, deltas, the rail's live header, map tags, depth and latitude labels, and the position bar. Labels that were mono (eyebrow, readout names, the "Ocean Observatory" line) are now Plex Sans in caps.
- **Highlight:** the one-italic-word trick ("record." in italic serif) was removed. The headline has no highlight now. The heatwave on the map holds the screen's visual weight, and the light display headline is the calm second voice.
- **Weight:** Light 300 at 95px, chosen because a light display is more premium and calmer than the engine's 600.
- **Type scale (5 sizes):**

  | Role | Size | Use |
  |---|---|---|
  | Display | 95 | Headline |
  | Title | 25 | Readout values |
  | Body large | 20 | Lede |
  | Body / label | 16 | Nav, buttons |
  | Caption | 13 | Labels, data, canvas labels (were 12) |

- **Color:** deep navy with bright text (14.4:1) and one coral signal. Not brown, not muddy.

## Round 3 (owner review, 2026-10-15)

**What he said.** "Okay." It had to become clearly better, at the level of the B2B product screens and the Orbika hero. The earlier audit (score 4) named the SaaS skeleton under the science: headline left, four stacked readout cards of equal height with a sparkline each on the right, and two buttons; and called "The ocean keeps the record." a slogan.

**What changed.**
- **The map is a real chart.** Depth comes from one height field: 5,600 m on the plain, the seamount rising to about 2,400 m. Contours every 100 m, index lines every 500 m, labelled with their exact depth (3,500 m, 4,000 m), all in the one line colour. One convention: metres below the surface, positive, in the labels, the profile and the status bar ("Sea floor"). A true graticule: 1° of latitude = 164 px, 1° of longitude at 47.6° N = 110.6 px; every line drawn is labelled (longitude along the top, latitude in one column at the parallels' left end), above the scrim; a 50 km scale bar between two meridians. The radial background glow is gone.
- **One float tells the story, docked to the map.** The four-card rail is gone. Float 4917-B sits on the seamount's eastern flank at 47°36′N (sea floor 2,900 m, computed from the same field); its profile panel sits on the right margin with its header level with the float, joined by a short leader; the panel's top lines up with the eyebrow and its bottom with the button. The panel plots temperature against depth to 2,000 m (top 200 m stretched, marked on the axis), this cycle against the October mean for 1991–2020: the 38 m mixed layer is drawn in coral, +1.38 °C at the surface (15.98 against 14.60 °C). The panel header no longer repeats the status bar's coordinates. Three readings that appear nowhere else: salinity at 5 m 35.62 psu, O₂ at 400 m 246 µmol/kg, next profile in 10 days.
- **The warm water is its own shape.** A dashed coral outline of the +1 °C sea-surface temperature anomaly, irregular, with the float inside it near its south-east edge, and its own plain label inside it ("Surface +1 °C above normal"); it is no longer painted onto the sea-floor contours, and it is no longer called a marine heatwave (that term has its own definition: above the 90th percentile for five days or more). The float is a dot and one ring.
- **Copy.** The headline states the reach, not a slogan: "The North Atlantic, from the surface to 6,000 metres." Eyebrow "612 instruments at sea · open data" in secondary ink (4,112 was more than the world's whole Argo fleet; the second "North Atlantic" is gone). One button, "Explore the data"; "Data portal ↗" is a plain nav link. Sentence case everywhere except the wordmark.
- **Nav.** The active underline sits on the nav's bottom rule; links end on the 64 px margin.

**Type scale (round 3).** Display 64 px (outside the scale on purpose, between the 49 and 76 px steps, so the map leads; fluid below 1440) · Body large 20 px (lede, readings) · Body 16 px (eyebrow, nav, button, panel title) · Label 13 px (chart axes and labels, legend, status bar, graticule). Two faces: IBM Plex Sans, and IBM Plex Mono for numbers and coordinates only.

**Checks.** `engine.py review`: the code uses the tokens; DESIGN.md refreshed with `design-md`. `preflight.py html`: one warning, the 64 px display outside the scale (on purpose). `check_dates.py`: passes. Checked at 1280 × 800 as well.

**Fresh-eyes audit.** A fresh-context subagent scored it against the B2B screens, Orbika and three Mobbin references (Dub https://mobbin.com/sites/sections/c9831c1e-e14f-4ba8-9f87-c9bafeaddf2b, MOUTHWASH Studio https://mobbin.com/sites/sections/38d3c862-d84c-4840-9fd0-94002eaf5571, Dovetail https://mobbin.com/sites/sections/57c3f21b-b420-47cc-be74-8b45ab45aea5).
- Round 1, **3** (after a first rebuild that kept the old map): contours at an odd interval with rounded labels, unlabelled grid lines, ticks under the scrim at 1.35:1, the heatwave painted onto the isobaths, a reticle, a radial glow, the panel reading as a rail card, doubtful data (4,112 instruments, O₂ 168 µmol/kg, a deep profile equal to the mean).
- Round 2, **4** (low), after the chart rebuild: label collisions, "16° °C", unlabelled lines, near-miss alignments, a too-regular outline centred on the float, "marine heatwave" used loosely.
- Rounds 3 and 4, **4**: each round's slips fixed (one latitude column, outline clear of the panel, panel bottom on the button's bottom, scale bar between meridians); the last two (the label sitting on 47°N, the outline crossing the leader) were then fixed by moving the label inside the outline and casing the leader.
It recomputed the graticule (164 and 110.6 px per degree), the float's position (47.598° N, 32.2125° W), the sea floor at the float (2,900 m) and the contour labels against the height field, and measured all text at 5.8:1 or better on the pixels. What it says keeps the piece below 5: the copy-left, panel-right structure and a seamount generated in code.

**Still open.** `mockups/04-browser-cascade` and `mockups/08-made-with-opendesigner` embed this shot; their captions are unchanged.
