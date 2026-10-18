# 02 · Neumorphism · Ostwell floor plan and zone dial

Ostwell, a building-management system: a flat Level 6 floor plan with live desks and one fault, and one soft object, the zone dial. Fresh audit after the polish round: 4 of 5.

The "Round 3 (polish)" section of 2026-10-15, the last one, describes this page. The polish round of 2026-10-14 before it describes the version that round started from. The sections between record the first build, the Ouvra climate panel that the independent audit scored 3.

**Final score: 4 of 5** after three rounds (3.5, then 4, then 4). Render: 1440 x 900 at scale 2 (`shot.png`).

## Direction
Ouvra is a fictional building-management system. The screen is the climate panel a facility manager uses for one zone: Level 6 East open office in Tessaly House, a 12-floor office building. The panel holds the zone dial, the set point, the mode, airflow and dampers, desk occupancy, the other zones on the floor and the occupied-hours schedule. The audience is facilities staff at a desk or on a wall tablet. Mood: quiet, tactile, engineered, like a well-made thermostat.
Feel words: **soft, calm, technical**.

## References (Mobbin, cited by link only)
Mobbin has no true neumorphic product screen and no building-management system. The material came from first principles (one light source, paired shadows, pressed equals on); the structure came from climate and device controls.

| Reference | What it taught |
|---|---|
| MyDyson controls (iOS), https://mobbin.com/screens/d720c97a-7732-438d-a09d-a41e30bb745a | A grid of round controls, each with an icon or value plus a label ("Airflow speed 4", "Oscillation OFF"). Became the fan-speed keys with their percentages. |
| Starlink sleep schedule (iOS), https://mobbin.com/screens/bc087b84-b872-4048-acfb-f9c8bfa44a18 | A dial with fine ticks, labelled major ticks and a handle riding the ring. Became the 16 to 28 °C zone dial with its set-point handle. |
| Eight Sleep temperature (iOS), https://mobbin.com/screens/68cf6abd-1b32-49c1-94b1-8d5744d3acef | Set-point steppers, − value +, with the value between the buttons. Became the set-point row under the dial. |
| Bump settings (iOS), https://mobbin.com/screens/d5d47d2b-9e60-4c5e-9863-590990ac9527 | Soft light-grey controls: a recessed track with a raised selection, the nearest shipped soft UI. |

## System (engine)
```
init; standard override STD-visual-details-24 --why "neumorphism is a light, same-colour material; one light appearance"
sketch --name Ouvra --brand #2F5BEA --audience regular --platforms web --feel soft,calm,technical --theme light-only --surfaces "building controls:operate" --delegated all
pick Q-dir-01 soft
set raw.textFace "Outfit"; displayFace "=textFace"; monoFace "Outfit"; numericStyles true; fontLicence (all true)
build
```

| Dial | Value | Why | Expresses the style? |
|---|---|---|---|
| depth | 70 | Extrusion is the whole style | Only in name: the soft preset emits the same one-way drop shadows as flat |
| roundness | 85 | Pillowy shapes: circles and 16 to 24 px radii | Yes (control 16, container 24) |
| colorfulness | 18 | Monochrome surface, one cobalt, status hues only for alarms | Yes |
| warmth | 22 | Cool grey-blue. The feel word "soft" had pushed warmth to 80, which turns the neutrals beige | Yes, and protects the owner's colour rule |
| expression | 45 | A quiet tool; the material is the personality | Slightly |
| brandPresence | 30 | Cobalt marks only the active mode and the selected control | No |
| density | 50 | Readings and controls at arm's length | No |
| energy | 25 | Calm, damped motion | No |

**What the dials cannot express:**
- The paired highlight and shade (light top-left, dark bottom-right).
- The inset "pressed" state.
- Elements being the same colour as the page.
- The 3:1 rim on controls whose shape is their only cue.

**Fonts.** Outfit only (SIL OFL, Google Fonts), with tabular figures. Weights: 300 for the big reading and the occupancy figure, 400 and 500 elsewhere, 600 for selected keys.

**Type scale (6 sizes).**

| Role | Size | Use |
|---|---|---|
| Display | 72 (outside the scale) | Zone reading 22.4 |
| Headline | 34 | Occupancy figure |
| Title | 22 | Zone name, set point |
| Body large | 18 | Readings, zone temperatures, building name |
| Body | 14 | Labels, keys, rows |
| Caption | 11 | Meta, ticks, hours |

## Where I stepped outside the tokens, and why
- **The extrusion.** The engine's soft preset gave the flat preset's shadows and a white `surface.raised`. I built every shadow from ramp steps:
  - `--neu-bg` is neutral step 3; the highlight is step 1; the shade is step 12 at 22% (12% on panels).
  - `--raise-sm/md/lg`, `--raise-panel`, `--press` and `--press-sm` are hand-made.
- **72 px reading.** Larger than the scale; it is the one thing to read from across a room.
- `review` counts 28 hard-coded values, mostly px sizes for round controls (48, 56 px) where the engine suggests spacing tokens.

## How the contrast problem is solved
Neumorphism's known failure is low contrast: edges and states drawn only by shadows on a same-colour page. Here:
1. **Text never uses the surface family.** Primary ink (neutral 12) is 13.1:1 on the page, secondary (11) 6.1:1, tertiary (10) 5.0:1. The darker text tone is what makes the panel readable.
2. **State is never carried by shadow depth alone.** "On" is always pressed in **plus** cobalt text, or a cobalt fill (toggle, slider, today's schedule bar). Cobalt is 4.65:1 against the page; white on cobalt is 5.52:1. One rule for the whole panel: pressed in means on (mode keys, fan keys, rail item, selected zone).
3. **A 3:1 rim where the shape is the only cue.** Toggle tracks, the slider track and thumb, the set-point handle and the empty toggle carry a 1 px rim in neutral step 8: **3.05:1** against the page. Buttons with a text or icon label keep the pure soft look, because their ink label (13.1:1) identifies them.
4. **Focus** is a 2 px cobalt ring, never a shadow change.
5. **Measured as rendered:** 116 text runs, 0 below 4.5:1. The lowest is 4.87:1, on scale labels marked decorative.

## Checks
- `engine.py validate`: no errors. Two warnings, both unanswerable:
  - "Soft fails 3:1 by design" cannot be cleared even with the rims in place.
  - The "friendly vs serious roundness" conflict stays after roundness was set by hand.
- `preflight.py html`: 1 error, M9 for Outfit (false: Google Fonts link). The earlier `<br>` warning is fixed.
- `engine.py review`: no standard breaks after round 3 (100dvh; 2 px gaps on tokens).
- **Facts:**
  - The dial, set point and zone list agree (22.4 now, 21.5 set).
  - 38 of 64 desks matches the 10:00 bar.
  - Yesterday's 11:00 bar is the stated peak of 52.
  - The fan runs at 58% and the dampers average 62% (round 3 fixed a duplicated 62%).
  - The building area is plausible for 12 floors (18,400 m²).

## Self-audit
Each round compared the render with MyDyson, Starlink and Eight Sleep at the same width.
1. **Round 1 (3.5).** Real neumorphism and readable, but:
   - The −/+ buttons overlapped the dial's edge.
   - The set-point handle crowded the 22 label.
   - Big dead bands sat under the mode keys, under the airflow toggle and under the zone list.
   - Selected was said two ways: the mode thumb was raised, while the fan, rail and zone were pressed.
   - "2 open alarms" appeared both in the header and on the rail badge.
2. **Round 2 (4).**
   - Rebuilt the dial (400 px, ticks outside the labels, handle on the tick band).
   - Put the set point between − and + under the dial.
   - Turned the mode control into keys with one rule: pressed in means on.
   - Removed the header alarm, so the rail badge and the zone row each say it once.
   - Filled the gaps with true data: a 64-desk capacity line, a caption explaining raised (today) against pressed (yesterday), the pre-cool rule and the next set-back exception.
3. **Round 3 (4).**
   - Panels drop to a softer extrusion (12% shade) so the strongest depth is spent on what you can press.
   - Fixed data clashes.
   - Moved spacing onto tokens.

**Tells from section 11, final state.** No glow, no decoration without data, and every state said once plus text.

**Remaining weakness:** every panel still uses the same soft radius and treatment ("one bubbly radius on every element"). A shipped building-management system would also be denser and flatter, so this is a premium concept more than a product a facility team runs all day.

## The style
- **Plain words:** everything looks molded from one soft material. Controls bulge up out of the page or press into it, lit from one side.
- **What defines it (checkable):**
  1. Elements are the same colour as the page (here neutral step 3, #e7ecf4).
  2. Two shadows on opposite sides: light up-left, dark down-right, offset 3 to 10 px with a blur of 7 to 24 px.
  3. Pressed or on states swap to inset shadows.
  4. Large radii and circles.
  5. A muted palette with at most one accent.
  6. Few borders.
- **How it goes wrong:**
  - Grey text on grey, so nothing reads.
  - State shown only by a shadow nobody can see.
  - Every element extruded the same amount, so nothing reads as pressable.
  - The paired shadows copied onto tables, inputs and text.
  - Warm neutrals sliding into beige.
- **How I kept it premium:**
  - Dark ink text (13:1).
  - One cobalt with one job (on and selected).
  - One rule for state (pressed means on).
  - Rims only where the shape is the only cue.
  - The strongest depth spent on the dial and keys.
  - Real BMS data (AHU and VAV ids, L/s, ppm, set-back hours).

## Process findings
Each was recorded in `opendesigner/feedback.md`.
1. **(gap) The soft preset emits no neumorphic tokens.** Elevation is identical to flat (one-way drop shadows), `surface.raised` is white, and the preset only adds a warning. It needs paired highlight and shade tokens, an inset pressed token, a same-colour surface rule and a 3:1 rim role.
2. **(bug) Picking soft left depth at 15** (coupled to expression 0 through the feel macros): the flattest depth for the one style that is all depth.
3. **(bug) The feel word "soft" maps to friendly,** whose macro pushed warmth to 80 (beige neutrals). A material word is read as a personality word.
4. **(bug) The macro-conflict warning stays** after the dial is set by hand.
5. **(confusing) The neumorphic contrast warning cannot record its mitigation,** so it stays even when every edge passes.
6. **(bug) `review` suggests the wrong tokens:** `radius-container` (24 px) for 3 to 6 px radii, and spacing tokens for control sizes.
7. **(conflict) `references/styles.md` disagrees with this result in two places.** That file was written during this run by another session and is untracked; nothing in the engine reads it.
   - It lists "no borders and no outlines" as a defining trait. Accessibility needs rims on shape-only controls, and this piece shows the look survives them.
   - It suggests warmth 40 to 60. I tested this on a copy of this state: neutral step 3 goes from #e7ecf4 at warmth 22, to #eaebee at 40, #ebebeb at 50, #edebea at 60 and #efebe8 at 80. So 40 to 60 gives a flat grey, 80 gives beige, and the crisp blue-grey this piece uses needs about 20.
8. **What helped:**
   - Validate's neumorphic lint and the stage file's warning ("every clickable part needs added borders") pointed straight at the real problem.
   - The status ramps gave a warning text colour at 4.99:1 with no work.

## Polish round 2026-10-14
**Fresh audit: 4 of 5.** Two fresh-context reviews both scored it 4. The independent audit had given the first build 3. Render: `shot.png`, 1440 x 900 at scale 2.

### What the audit asked for
- The same soft extrusion was on every panel, key, row and bar, so nothing read as the thing to press.
- Raised against pressed bars could not show today against yesterday.
- A generic icon rail and an "IV" avatar.
- A 2020 smart-home layout: one dial card plus four widget cards.
- The header put a Tuesday on 14 October, which is a Wednesday in 2026.
- VAV-6.03 served two zones.
- Tessaly was reused.

### What changed
- **A layout built on the one idea only a building-management system has: the floor plan.** Level 6 is drawn as a 64 x 34 m plate. It shows:
  - each zone's temperature against its set point;
  - live desk sensors (38 of 64 desks in use east, 27 of 48 west);
  - each VAV box in the zone it serves;
  - the one fault, said once next to the box that causes it: V-6.06 is stuck at 10%, so rooms 6.24 to 6.26 run at 23.1°.
- **The soft look is on one control only: the zone dial.**
  - It uses the engine's new extruded elevation tokens: overlay for the ring, pressed for the well, raised for the handle and the − and +.
  - The handle is the control. It is a slider: arrow keys, drag along the ring, 0.5 °C steps. The − and + sit on the dial.
  - Everything else is flat, with hairlines.
- **Today against yesterday uses a real second signal:** bars for today, a dashed line for yesterday.
- The icon rail and the avatar are gone.
- **Facts.**
  - The date is Wed 14 Oct.
  - Each VAV box serves one zone: 6.01 to 6.04 east, 6.05 and 6.06 the meeting rooms, 6.07 to 6.09 west, 6.10 the kitchen.
  - A damper stuck at 10% starves its rooms of cool air, so they run warm. The first build said "stuck open", which would make them cold.
  - Cooling comes from outside air at 11.8 °C, and the chiller is locked out below 12 °C outside. That is why the zone is still 0.9° over set point 82 minutes after cooling started. Dampers 86% open and 2,580 L/s of 3,000 design agree with it.
- **Names.**
  - Ouvra is a real French software for plumbing and heating firms. It became Kelvane, which the second fresh audit found as a live Framer template for HVAC contractors. The name is now **Ostwell**, which returned no company in building controls.
  - Tessaly House is now Fenwold House.
- **Fixes after the first fresh audit (4):**
  - The fault has one signal plus its text; the pink room fill is gone.
  - VAV labels carry a "V-" prefix, so they cannot be read as room numbers.
  - The outer wall is lighter.
  - The chart titles name the zone.
  - The set-back line gives both limits (16 / 26 °C).
  - The CO₂ copy is fixed.
  - The comms room shows its set point.
- **Fixes after the second fresh audit (4):**
  - The in-use desks are lighter, so the temperatures and the fault lead.
  - Labels moved off the walls.

### System (engine)
```
set name "Ostwell"; pick Q-dir-01 neumorphism; build
```
- Picking neumorphism left the dials as they were, because they had been set earlier: depth 70, warmth 22.
- The build now writes `elevation.raised`, `floating` and `overlay` as paired highlight and shade, and `elevation.pressed` as an inset pair. The first build had to hand-make all six shadows.

### References (Mobbin, by link only)
| Reference | What it taught |
|---|---|
| Airbnb dial, https://mobbin.com/screens/5c40f106-f3d9-442a-b651-a885faa0ec83 | One soft control on an otherwise flat screen, and the knob is the control. |
| Rivian climate, https://mobbin.com/screens/d217e8a1-3cf7-44b4-be12-5937efd5ee13 | Set temperature against cabin temperature, with flat steppers. |
| Zillow floor plan, https://mobbin.com/screens/887b121b-4662-4fcb-9599-d6fef699b07d | A plan in one line weight with markers and a floor picker. Mobbin has no real building-management screen. |

### Checks
- **Contrast as rendered** (text hidden, then each run compared with the darkest 5% behind it): 124 runs, 0 below the floor. The lowest is 5.22:1, "Core" on the core fill.
- **Control edges.** The rims on the handle and on − and + use `border.strong` (neutral 8) at 3.05:1. Free desks have a neutral 8 outline; desks in use have a neutral 8 fill.
- **Weekdays.** `check_dates.py --year 2026`: every weekday matches.
- **Tools.**
  - `validate`: no errors. One warning remains, the neumorphic 3:1 note, which the rims answer.
  - `review`: 11 hard-coded values, mostly control sizes.
  - Preflight: M9 (the false positive for Google Fonts) and an M8 warning for 12 px chart and dial labels. The plan's 11-unit labels render at about 12 px, because the plan scales by 1.095.
- **Recorded with `engine.py feedback`:**
  - Preflight's 12 px floor for web text conflicts with the engine's own 11 px caption step.
  - What helped: the new extruded tokens.

### Remaining weaknesses
- The dial spends 340 px on a 0.9° gap. A shipped system would give the plan more room.
- The meeting rooms count as one zone although they show two temperatures on two VAV boxes.

## Round 3 (polish) 2026-10-15
**Fresh audit: 4 of 5** against the B2B product screens (`product/01`, `02`, `04`, `06`). Render: `shot.png`, 1440 x 900 at scale 2.

### Why this round
The piece still carried "Being rebuilt" on the public showcase. The owner's bar is the B2B product screens: one accent with one job, real dense content, exact spacing, legible type. The audit's fixes were done in the polish round of 2026-10-14; this round closed what stood between that page and the bar.

### What changed
- **One type scale, through the engine.** The page used eight sizes, three pairs within 10% of each other (11 and 12, 14 and 15.3, 22 and 24). `pick Q-type-09 1.2` rebuilt the scale as 12, 14, 17, 20, 24, 29, 35. The page now uses five sizes:

| Role | Size | Use |
|---|---|---|
| Caption | 12 | Legends, plan labels, chart axes, set points |
| Body | 14 | Header, readings, nav |
| Title | 17 | The wordmark |
| Headline | 24 | Zone name, zone temperatures on the plan |
| Display | 56 (outside the scale) | The reading inside the dial |

  The plan is an SVG drawn in metres and scaled to the column, so its labels are now sized by the plan's own zoom and render at 12 and 24 px. Comms uses the same zone tag as the other rooms (it was 15.3 px).
- **The mode switch is the second soft part.** It was a bordered row with a solid cobalt segment, the loudest block on the right. It is now a track pressed into the page (the engine's pressed elevation) with the chosen mode raised out of it (the raised elevation), so the page shows both halves of the style: raised and pressed. State is never shadow alone: the raised mode is also cobalt, heavier, and keeps the 3:1 rim, as the engine's neumorphic warning asks.
- **Spacing.** The bigger zone title pushed the schedule note into the last reading row; the dial and switch gaps went from 32 and 24 to 20 px, so the note has 16 px of air again.
- **After the first fresh audit (3):**
  - **Soft parts without outlines.** The dial, its handle, − and +, and the mode track carry no rim; their cobalt dot and ink glyphs give the 3:1 cue. Only the chosen mode keeps a rim, as its state cue.
  - **The fault is on the plan.** Rooms 6.24 to 6.26 are tinted, VAV-6.06 is drawn in red, each meeting room shows its own reading (21.5, 21.7, 21.6; 23.0, 23.3, 23.0, averaging 21.6° and 23.1°), and the fault line is 14 px: "1.6° over in 6.24 to 6.26: V-6.06 stuck at 10%".
  - **The core says what it is:** lifts, stair, WC and risers in hairline cells on the plate colour, instead of the darkest grey block on the plan.
  - **Selection on the walls.** The east zone's own walls are drawn in cobalt, with a 5% cobalt fill; the inset outline doubled the grey wall on three sides.
  - **Edges.** The plan's viewBox starts at the wall, so the plan lines up with the header, legend and charts on the 32 px edge.
  - **One time axis.** Both charts run 06 to 19, and both carry the 10:42 line.
  - **VAV boxes off the walls:** V-6.05 and V-6.06 sit over the middle room of the three each serves, labelled below.
  - **Cobalt has one job,** the selected zone and its control: the logo is ink now.
  - **4/8 rhythm:** the reading rows are back to 8 px, gaps of 2 px are 4. The dial went from 340 to 320 px to make the room.
- **After the second fresh audit (3, "close to 4"):**
  - **The arc owns its track:** the ticks under the set-point arc are masked, so no tick crosses it.
  - **Cobalt has one meaning,** the selected zone and its control: the temperature chart draws today in ink and yesterday dashed.
  - **No soft part has a rim.** The chosen mode is raised, cobalt and heavier; the handle's dot and the ink − and + are the 3:1 cues.
  - **A plan, not a wireframe:** glazing on a 2.4 m module along the outer walls, a door for each meeting room, a temperature sensor in each zone (and in the legend), and the riser cell tagged AHU-2.
  - **The fault is said twice, not four times:** the tinted rooms show where; the sentence says why. V-6.06's box and label are neutral.
  - **Charts:** desk bars in the plan's desk grey; legends on one line height; short titles ("Temperature", "Desks in use") so neither header wraps.
  - **Readings:** airflow 2,160 of 3,000 L/s (72%), no longer equal to the 86% damper average; the panel says V-6.01 to 6.04, as the plan does.
- **After the final fresh audit (4):**
  - The charts sit under one heading, "East open office, today", so they say which zone they show.
  - The set-point arc and its handle ride outside the tick ring (radius 152), so no tick is hidden or crossed.
  - The selection is 3.5 px, wide enough to cover the glazing lines on the zone's walls; the east wall is glazed its full height.
  - The temperature curve levels off after cooling starts at 09:20 (22.05, 22.24, 22.36, 22.42, 22.4 now).
  - "Set 21.5°" on the meeting-rooms strip, as everywhere else.

- **After a last regression check (holds at 4):** the selection moved 3 px inside the zone's walls so their glazing shows (drawn on the walls, it hid the panes), and the ticks end at radius 144 so the handle covers the half-degree tick under it.

### System (engine)
```
pick Q-type-09 1.2 --why "one scale, captions at 12 px, as the B2B product screens"
build
```

### References (Mobbin, by link only)
| Reference | What it taught |
|---|---|
| Rivian, https://mobbin.com/screens/d217e8a1-3cf7-44b4-be12-5937efd5ee13 | Chosen segment raised out of a track; set point against the reading. |
| MyDyson, https://mobbin.com/screens/4b8af8cf-12b8-45a1-a2be-40f6e33cd0f6 | Round soft controls whose glyph is the cue. |
| Tripadvisor, https://mobbin.com/screens/33957d93-1613-4b44-af7d-a07f32ff16ff | A plan with state in room fills and one clean selection edge. |

### Checks
- **Contrast as rendered:** 131 runs; the only flag is the white "1" on the red alarm pill, where the measuring box takes in the page behind the pill's rounded ends. The pair itself (white on `#a82321`) is 7.17:1. Every other run passes.
- **Weekdays:** `check_dates.py --year 2026` passes (Wed 14 Oct).
- **Facts re-added:** desks 38 + 27 = 65 of 64 + 48 = 112; plate 64 x 34 = 2,176 m²; meeting rooms 21.5, 21.7, 21.6 average 21.6° and 23.0, 23.3, 23.0 average 23.1°, 1.6° over 21.5°; zone 22.4° against 21.5° is 0.9° over; outside 11.8 °C is under the 12 °C chiller lockout.
- `engine.py validate`: no errors, 1 warning (the neumorphic edge-contrast warning; every soft control has a 3:1 glyph or label). Preflight: one warning, the 56 px dial figure outside the scale, on purpose.
