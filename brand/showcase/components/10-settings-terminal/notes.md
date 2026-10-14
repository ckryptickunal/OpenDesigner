# 10 · Settings panel · rackhound

## Direction
rackhound is a fictional self-hosted console for people who run a small server rack at home. Its settings panel lives in the browser but feels like a 1980s amber-phosphor terminal: mono everything, box-drawing frames, block-character switches and sliders, a tmux-style status line top and bottom, a pixel display face for titles and readouts, scanlines and a soft phosphor glow. It must still be a real, accessible settings UI: switches, segmented controls, sliders, an input, apply and revert.
Feel words: **retro, technical, nerdy** (engine: retro → heritage + playful, technical → modern + serious, nerdy → modern + playful).

## References (Mobbin, cited by link only)
- Mintlify add-ons settings, https://mobbin.com/screens/dfc67d57-50f5-473e-8567-7c1f11332e0b : group title and description on the left, rows of controls on the right, a three-state select with explanations. Taught me the label-left, control-right row with a one-line description.
- Replit user settings, https://mobbin.com/screens/093752e0-185b-45e6-b6b9-10ae944810a2 : collapsible groups, switches and a Light/Dark/System segmented control in one list. Taught me mixing switch, select and segmented rows at one rhythm.
- Customer.io experimental features, https://mobbin.com/screens/a1452449-634b-45f7-8340-447391cf7577 : each setting explains what happens when it is on. Taught me the descriptive second line under every setting.
- Magnific settings dialog, https://mobbin.com/screens/95dbaf70-750c-4ff7-bfc1-ad67e0a1c60d : a left section list with a dense right pane. Taught me the section rail.

## System (engine)
`sketch --name "rackhound" --brand "#ffb000" --audience dense --platforms web --feel retro,technical,nerdy --theme system-light-dark --delegated all --surfaces operate`, rendered with `data-theme="dark"`. Then, to get the amber back (see findings): `set dials.colorfulness 85`, `pick Q-color-01 keep-hex`, `set raw.brandColor "#ffb000" --set-by chosen`, `set raw.accentCount 1`.

| Dial | Value | Why |
|---|---|---|
| expression | 70 | a stylised terminal |
| brandPresence | 80 | the phosphor is the brand |
| density | 72 | terminal-dense rows; controls 32/40/48 |
| energy | 40 | only the cursor blinks and "applying" pulses |
| roundness | 0 | square cells, box-drawing borders |
| depth | 10 | no shadows; glow instead |
| colorfulness | 85 | needed for chroma (22 turned the amber brown) |
| warmth | 58 | warm amber |

Typefaces: `raw.textFace` and `raw.monoFace` "JetBrains Mono", `raw.displayFace "VT323"` (SIL OFL, Google Fonts), licence recorded.

## Where I stepped outside the tokens, and why
- **Phosphor colour** `--ph` is the accent ramp's LIGHT step 9 (exactly #ffb000) used in the dark theme. The dark ramp desaturates the accent to #eeb763 at step 9, which reads as beige, not phosphor.
- Secondary text is `accent-dark-solid-pressed` (#c6913a, 6.5:1) and hints/borders `accent-dark-8` (#a67931, 4.7:1): ramp steps, because the semantic text roles in dark mode are neutral greys and the whole UI is amber.
- Unlit blocks, rules and hover wash use neutral dark 6 and 3 (grey), not the brown accent steps.
- Header title VT323 at 76px and readouts at 29px: VT323 has a small x-height, so it is set larger than a sans would be; 76 is off the scale on purpose (a display moment).
- Scanlines, vignette and text glow are decorative overlays.

## Type scale (6 sizes, no two within 10%)
caption/label 12 (status lines, chip labels, hints), body 14 (setting names and descriptions, controls), unit 20 (the °C/W beside readouts), title 24 (box legends, VT323), headline 29 (slider readouts, VT323), display 76 (the "settings" title, VT323, off-token). Two fonts only: JetBrains Mono for every piece of UI text (it is all settings data and log output) and VT323 for titles and readouts.

## Owner type and color rules (checked after the rule arrived)
- Two fonts: compliant (JetBrains Mono + VT323).
- Weight: titles in VT323 regular (the face has one weight); setting names JetBrains Mono 500, selected items 700 in the inverted fill box; no bold headings.
- Highlight: the selected section and selected segment use a filled amber box with black text, not a different face.
- **Color change:** the first render used the accent's dark steps 3 and 7 (#2f2618, #614208, brown) for unlit slider blocks, the OFF switch thumb, rules and hover wash. Those were the muddy brown-on-black the rule warns about. They are now neutral dark 6 (#403f3e) and 3 (#262524), so the screen is black, grey (unlit) and bright amber (lit), with clear tonal contrast. Background is neutral dark 1 (#151515), not a warm brown-black.

## Checks
- `engine.py validate`: no errors, 7 warnings, 5 notes. Warnings: light-mode action fill #ffb000 is 1.8:1 against the base surface (advisory; it is a text-labelled button and dark text on it is 10:1), "vivid colour on a dense layout" (intended), and four "playful, serious pull X in opposite directions" macro conflicts that do not clear after setting every dial (see findings).
- `preflight.py html --medium web`: 1 error, a false positive (M9: VT323 loads from the Google Fonts link; a Playwright check confirmed both faces loaded). Two earlier warnings fixed: a `<br>` in the rack label, and −0.05em tracking on block characters.
- Contrast: phosphor #ffb000 on #151515 is 10:1, secondary 6.5:1, hints and control borders 4.7:1, danger #f19288 8:1. Unlit blocks and disabled controls are exempt (inactive). The focus ring is the token focus colour (#eeb763, 10:1).
- Targets: switches 60×28, segments 32 tall, buttons 32, inputs 36, sliders 28; all over 24px for pointer.
- Interaction: switches are `role="switch"` buttons that update their ON/OFF word and mark the row unsaved (`*`); segmented controls are radiogroups with Arrow keys; sliders are native ranges with live readouts and `aria-valuetext` ("62 degrees"); apply clears the unsaved marks. Reduced motion stops the cursor blink and the applying pulse and zeroes transitions.

## Rounds
1. The ASCII rack drawing in the header misaligned (some block glyphs fell back to another font), "10/10" read like a score, and the bottom third of the nav and settings boxes was empty.
2. Replaced the ASCII rack with a CSS rack (bays with LEDs), changed the number to "#10", added a fan-curve preview (target and current temperature marked on the curve) and UPS and config readouts to the nav.
3. Aligned the curve's axis labels to their real temperatures, stretched the log box to match the column bottoms, removed the `<br>` and the tight tracking. After the owner's colour rule: swapped brown dims for neutral greys.

## Process findings
1. **`--brand` plus `--delegated all` replaced my brand.** The sketch swapped #ffb000 for #9e6b00 ("a readable shade … (an olive)") so white text would pass, and DESIGN.md said "Picked for you, not chosen by you". The same thing changed #e8590c, #ff3d81 and #5fae7d in pieces 06, 08 and 09. Only `set raw.brandColor ... --set-by chosen` restored it, with dark text. (feedback: bug)
2. **Colorfulness mixes "how many hues" with "how saturated".** A one-hue, full-chroma brand needed colorfulness 85 plus `accentCount 1`. (feedback: gap)
3. **The dark ramp always desaturates the accent**; no option keeps brand chroma in dark mode, which neon, CRT and phosphor looks need. (feedback: gap)
4. **Macro-conflict warnings never clear** and name no command. (feedback: confusing)
5. **The light-mode contrast warning's fix would undo the brand pin.** (feedback: idea)
6. Helped: roundness 0 and depth 10 gave exactly the square, shadowless system; density 72 gave 32/40/48 controls; the reduced-motion transition tokens and focus tokens worked unchanged in a very unusual look.
