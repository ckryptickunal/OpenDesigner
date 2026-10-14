# 04 · Skeuomorphism · Fenmoor STEM-8 post console

**Final score: 5 of 5** after three rounds (4, then 4.5, then 5). Render: 1440 x 900 at scale 2 (`shot.png`).

## Direction
Fenmoor is a fictional maker of audio tools for post-production studios. STEM-8 is a plugin that puts a re-recording mixer's console in the session. It has eight stem channels (two dialogue mics, ADR, Foley, hard effects, backgrounds, score and a reverb return), each with trim, high-pass, presence and pan. The master section adds a broadcast loudness meter and a 5.1 bus. The scene: Episode 104, reel 3, mixed to a −24 LKFS delivery spec. The audience is re-recording mixers who have touched real consoles for twenty years. Mood: heavy, exact, quietly expensive, like machined aluminium in a dark room.
Feel words: **technical, premium, serious**.

## References (Mobbin, cited by link only)
Mobbin has no pro-audio plugin or console. The console layout and loudness metering come from first principles: the channel-strip order of large-format consoles and the BS.1770 readings (integrated, short-term, momentary, true peak, range).

| Reference | What it taught |
|---|---|
| [untitled] stem mixer (iOS), https://mobbin.com/screens/996916cd-2a7f-4d0c-ad28-d699736f8ee5 | Stems as side-by-side channel strips, tick-marked fader tracks, and the stem name at the foot of each strip. |
| Deezer equalizer (iOS), https://mobbin.com/screens/2d0034cc-3d4a-4052-af71-beafd7a9eaf7 | Faders against a printed dB scale (+12 / 0 / −12), with segmented level bars above. Taught the scale and its ticks beside the slot. |
| (Not Boring) Camera (iOS), https://mobbin.com/screens/1c45bdad-c58a-430b-ac9a-bf59021fcfb1 | Machined, knurled controls lit from one direction, in one body. The bar for the knobs and fader caps. |
| Once tape (iOS), https://mobbin.com/screens/a512d806-9250-4afa-8774-e1f187d15676 | A real object drawn straight: true proportions, small hardware detail (screws, windows), no cartoon. |

## System (engine)
```
init; standard override STD-visual-details-24 --why "a hardware console panel is one dark anodized appearance"
sketch --name Fenmoor --brand #38D5F2 --audience dense --platforms web,desktop --feel technical,premium,serious --theme dark-only --surfaces "plugin panel:operate" --delegated all
set raw.brandColor "#38D5F2" + flags.brandExact   (sketch had set #008195 and said "I picked a teal")
set raw.textFace "Barlow"; raw.displayFace "Barlow Condensed"; raw.monoFace "Barlow"; numericStyles true; fontLicence (all true)
build      (Q-dir-01 left unanswered: none of its six options is skeuomorphic)
```

| Dial | Value | Why | Expresses the style? |
|---|---|---|---|
| depth | 100 | Real light on real materials | Only partly: it gives a shadow ladder, not materials |
| roundness | 15 | Machined metal: 2 to 6 px radii, circles only on knobs | Yes |
| density | 85 | Eight strips and a master section in one window. This gave the dense scale 12/14/17/20/24/29/35 | Yes |
| colorfulness | 30 | Graphite and aluminium; LED colours only in meters and buttons | Yes |
| warmth | 15 | Cool anodized graphite, never brown | Yes |
| expression | 85 | The hardware metaphor is the point | Indirectly |
| brandPresence | 30 | Cyan only where an LCD is backlit | Yes |
| energy | 35 | Heavy, damped controls | No |

**What the dials cannot express:** brushed and anodized metal, knurled knob skirts, domed caps, fader caps with grip ridges, LCD glass with backlight, lit and unlit LEDs, screws, and one light direction across the panel.

**Fonts.** Barlow Condensed for silkscreened legends, the wordmark, the scribble strips and the channel plates (uppercase, tracked 0.06 to 0.32 em). Barlow, with tabular figures, for every value and readout. Both are SIL OFL from Google Fonts. Two fonts: legend and value, which is how hardware is lettered.

**Type scale (5 sizes, all from the engine's dense scale).**

| Role | Size | Use |
|---|---|---|
| Display | 35 | Integrated loudness −24.1 |
| Headline | 24 | FENMOOR wordmark |
| Title | 17 | Scribble-strip names, LCD readouts, channel plates, loudness stats |
| Body | 14 | Unit labels |
| Caption / legend | 12 | Silkscreen legends, knob values, scales |

## Where I stepped outside the tokens, and why
Every flat colour is a token: graphite is neutral dark 1 to 6, aluminium is 9 to 12, the LCD is accent dark 10 and 11, LEDs are success, warning and danger step 11, and mute and solo use danger and warning 9 and 10. What is hand-made is light and texture:
- hairline brushing (`repeating-linear-gradient`);
- knurling (`repeating-conic-gradient`);
- domed caps (`radial-gradient`);
- the inset of LCDs and slots;
- the 24 shadow stacks that make metal sit on metal.

`review` counts 64 hard-coded values, nearly all of them these shadows and the px sizes of hardware parts.

## Checks
- `engine.py validate`: no errors. Two warnings about light mode, which this dark-only system does not have.
- `preflight.py html`: 2 errors, M9 for Barlow and Barlow Condensed (false: Google Fonts link).
- `engine.py review`: no standard breaks.
- **Contrast as rendered:**
  - 287 runs, 0 failures.
  - Round 2 caught the LCD captions at 4.33 to 4.41:1 (accent dark 8 on black) and a graph label sitting on the line (1.03:1).
  - Both were fixed: captions moved to accent dark 10, graph labels moved to a right gutter.
- **Facts:**
  - Each fader cap sits at its dB on the console scale, and each plate shows the same number.
  - Each meter lights to its stated peak, with 2 dB segments and colour zones at −18 and −6 dBFS.
  - Integrated −24.1 is inside −24 ±2, so "In spec".
  - True peak −3.2 dBTP is under the −2.0 limit.
  - The loudness history ends at the short-term value (−22.8).
  - The 5.1 meters match their labels.
- **Accessibility:**
  - Every knob and fader has a role, a label and a value text.
  - Mute and solo are buttons with `aria-pressed`.
  - Targets are at least 30 px.
  - Focus ring is 2 px accent.
  - Status is shown by the LED colour plus the words "In spec", and by mute's red fill plus its label.

## Self-audit
Each round compared the render with the stem mixer, Deezer and (Not Boring) Camera at the same width.
1. **Round 1 (4).** It already read as a real plugin. But:
   - The BG scribble strip wrapped onto a third line.
   - The loudness history was a jagged 20-point zigzag.
   - The scribble-strip peak values had no unit or label.
2. **Round 2 (4.5).**
   - The history became 60 one-second readings with "−60 s" and "Now".
   - Peaks are labelled "pk".
   - Fixed LCD caption contrast and the graph label collision.
   - Renamed the BG stem to fit.
3. **Round 3 (5).**
   - Each strip meter got its own dBFS scale. Before, it sat beside the fader's gain scale, inviting a misread: a −12 dBFS peak looked like it lined up with the fader's "0".
   - True minus signs on every scale.
   - Spacing on tokens.

**Tells from section 11, final state:**
- Glow appears only on lit LEDs (a state).
- The screws are the only pure decoration: four, at the chassis corners.
- Every other mark is a value: ticks, LEDs, scales, plates.
- No device frame, no real brand's hardware.
- Light falls the same way on every part.

Why 5: put beside shipped audio tools, it passes as a real company's plugin, and the details are the ones a re-recording mixer checks (stem names, HPF corners, dialog gating, true peak, LRA, a 5.1 bus with LFE).

**Honest limit:** a working plugin would need resizing and a drag alternative for knobs. Here, focus plus arrow keys would set values (WCAG 2.5.7); that is noted but not wired.

## The style
- **Plain words:** the screen imitates a real object. This one is a console made of aluminium and anodized metal, with knobs you could grip, faders that slide in a slot, and lights behind glass.
- **What defines it (checkable):**
  1. Controls shaped like physical ones (knurled knobs with pointers, fader caps with ridges, keys that sink when on).
  2. One consistent light: highlights on top edges, shadows underneath, insets for windows and slots.
  3. Material textures that stay below notice (brushed hairlines at 3 to 12% alpha).
  4. Real proportions and real scales, printed like silkscreen.
  5. Backlit displays and LEDs with lit and unlit states.
- **How it goes wrong:**
  - Textures loud enough to fight the text.
  - Light from three directions.
  - Fake materials wrapped around what is really a form.
  - A copied real-brand device.
  - Gloss and glow everywhere.
  - Decoration (screws, rivets, wood) outweighing controls.
  - Scales that don't match the values.
- **How I kept it premium:**
  - Graphite and aluminium with colour only where a light would be lit.
  - Two typefaces in a hardware role split (condensed legends, tabular values).
  - Every scale computed from the same mapping as the control it labels.
  - Real post-production data and delivery spec.
  - The texture kept quieter than the type.

## Process findings
Each was recorded in `opendesigner/feedback.md`.
1. **(gap) No skeuomorphic option and no material tokens.** Metal, knurling, LCD glass and LEDs are all hand-made; 24 of the 64 hard-coded values are shadows that are the material.
2. **(gap) No lit and unlit indicator roles.** LEDs used status step 11 for lit and a 14% mix for unlit.
3. **(gap) No "secondary text in the accent colour" role for backlit displays.** Accent dark 8 gives 4.33:1 on step 1.
4. **(bug) `sketch --delegated` replaced the cyan brand #38D5F2 with teal #008195** (decisions.md D-0008) so white text would pass. This is the second time in these four pieces, after 01's mint. Light brands on dark need dark on-text, not a darker brand.
5. **(repeat) A dark-only theme still validates light mode.**
6. **(conflict) `references/styles.md` (untracked, from another session) gives skeuomorphism** roundness 48 to 80, density 30 to 50 and brandPresence 70 to 90. A professional hardware panel worked at 15, 85 and 30. Its ranges describe consumer skeuomorphism (wood, leather, a turntable), not machined pro tools.
7. **What helped:**
   - The dense audience produced exactly the type scale a console needs, with 12 px as the smallest step (preflight's web floor).
   - The neutral dark ramp gave a full graphite-to-aluminium range with no tinting.
   - The status ramps gave LED colours that already pass on black.
