# 01 · Phone trio: three evening apps

Render: `shot.png`, 1600 × 1200 at scale 2 (`brand/tools/shot.py`). Page: `index.html`.

## Direction
A case-study plate for three of the showcase's night-time apps: Lullwater (sleep), Undertow (podcast) and Halden Private (banking). Three generic phones float over one lilac mist field at slightly different heights, the middle one nearest the camera, each casting a long, soft, violet-tinted shadow. One caption line. Feel words: calm, premium, minimal.

Source renders (used as `<img>`, not redrawn): `app-screens/02-sleep-meditation`, `08-podcast-player`, `01-private-banking`.

## References (Mobbin, cited by link only)
- Sana, three phones: https://mobbin.com/sites/sections/cf567c70-dd59-4cc6-99c9-a8d4e761bb55 . The middle phone sits forward and larger; the trio reads as one object, not three screenshots.
- Slush, phones on a tinted field: https://mobbin.com/sites/sections/039d99ca-3adc-41ff-abff-661087ec40b8 . A pale field tinted from the product's own hue makes dark screens glow.
- Calm, three phones on a gradient: https://mobbin.com/sites/sections/aea0407a-ddaa-4cf2-ab72-3c1744dd9c71 . What to avoid: equal heights and no shadow read as a template.
- Analogue Agency, phone on a blue field: https://mobbin.com/sites/sections/c27f50ff-dd09-41f9-afc8-598c3ccae77a . One saturated field and nothing else is enough.

## System (engine, `systems.py`)
`sketch --name "Evening Apps Case Study" --brand "#5B4FC4" --audience regular --platforms web --feel calm,premium,minimal --surfaces "case study:experience" --delegated feel,audience,platforms`, then `raw.textFace "Manrope"`, `raw.fontLicence` (SIL OFL), `raw.neutralTint "brand"`, dials, `build`. Every command and its output is in `engine-log.txt`.

| Dial | Value | Why |
|---|---|---|
| expression | 45 | the work is the show; the scene stays quiet |
| brandPresence | 35 | violet only tints the field |
| density | 10 | three objects and one line of text |
| energy | 20 | floating, still |
| roundness | 80 | phones have big soft corners |
| depth | 85 | the idea is objects at different depths |
| colorfulness | 30 | one tinted field; the screens bring the colour |
| warmth | 35 | cool mist so the dusk screens glow |

Font: Manrope only (SIL OFL, Google Fonts link, variable 400–700).
Type scale used: one size, `body-md` 19 px (weight 600 for the title part, 400 for the names). The system's scale is 15 / 19 / 24 / 30 / 46 / 58 / 91 / 113; a caption-only scene needs one step.

## Outside the tokens, on purpose
- **Field colour.** `raw.neutralTint brand` barely tints the neutrals (step 3 is #ebebf0), so the field is built from `accent-light-2` to `accent-light-6`, not from a surface role.
- **Device geometry and metal.** Bezel width, corner radius, side keys, lens and the graphite edge gradient follow a phone's proportions, not UI spacing. Marked `od-ignore` in the page.
- **Shadows.** Four layers per phone (contact, near, mid, far), tinted with `accent-light-12` through `color-mix`. The elevation scale stops at `0 32px 64px`, too short for something floating this high.
- **Grain.** A deterministic canvas noise at 22% multiply, so the gradient reads as a lit surface.

## Look and fix
1. First render: phones small and high, a dead band above the caption, shadows almost invisible. Enlarged the phones (292/334 → 318/368 px wide), moved them down, made the middle shadow longer and softer than the outer two.
2. Second render: composition balanced; checked the shadow at 200% (soft, violet, no grey). Third pass after the checks: the names in `text-secondary` measured 4.36:1 on the lit field (5th percentile), so they now use the field's own deep ink `accent-light-12` (7.45:1 at the 5th percentile).

## Checks
- `engine.py validate`: passes, 0 warnings, 5 notes.
- `engine.py review --project .`: clean after the device-art lines were marked `od-ignore` (it first listed 17 values, all device materials and shadows).
- `preflight.py html --medium web`: 1 error, M9 "Manrope has no @font-face". False: the face is loaded by a Google Fonts `<link>`; `document.fonts.check` returned true in a browser check. It read no font sizes (`[]`), because the sizes come from the linked `tokens.css` in rem.
- Contrast, measured on the render: title 19 px `text-primary` on the field well above 7:1; names 7.45:1 after the fix.
- Checklist (type, layout): one family, one size, no italics, nothing within 10%; text at least 64 px from the edges; the work is untouched.

## Process findings
- There is no scene or mockup idea in the engine: the field colour, device geometry, materials and floating shadows all live outside the tokens (recorded with `engine.py feedback`, kind gap).
- A coloured page ground cannot be asked for; `neutralTint brand` is too faint to be a field (recorded, kind gap).
- `--surfaces "case study:experience"` worked: spacious density and display sizes came with it.

## Round 3 (2026-10-15): rebuilt as three dark interfaces
The sections above describe the round 1 plate (a lilac field, three dead-frontal phones with a round punch-hole camera, one caption line); this section replaces them where they differ. Two fresh audits before the rework scored it **3**: the phones were Android-style hardware around iOS screens, the plate read as Calm's three-flat-phones template, and the caption was a portfolio label.

**What changed** (`index.html`, `shot.png` 1600 × 1200 at 2×):
- **Hardware matches the screens.** The punch-hole is gone; each phone has a short camera pill centred in the status bar's gap (20% of the screen's width, not a copy of any brand's island). No logo, no camera bump.
- **Turned phones.** The middle phone is face-on and nearest; the outer two are turned 24° toward it (CSS 3D, one perspective). Their outer metal edges show as a crescent behind the front, the left one lit, with plain side keys (volume on the left phone, power on the right).
- **One light, from the upper left.** Lit rims; glass reflections of 2%, 4% and 6% (the right phone faces the light most); every shadow falls down and right on the wall. The shadows are drawn by a script over each phone's projected outline (its four corners as rendered), after a fresh audit found that shadows drawn inside the turned phones turned with them, and that bounding rectangles put shadow above the turned phones' far corners. Measured with and without the shadows: nothing above the far corners (5 to 6 levels at most, was up to 41).
- **The wall takes Undertow's colour.** The scene system's brand is now Undertow's periwinkle `#A9C4FF` (`engine.py set raw.brandColor`, logged in `engine-log.txt`), so the wall is that ramp's steps 2 to 6. `validate` now warns that the light action colour is faint on white (advisory; the scene has no buttons).
- **A case, not a label.** A 46 px heading, "Three dark interfaces", and one caption under each phone with one fact its screen shows: "Lullwater, a sleep app / Fades out by 23:40", "Undertow, a podcast player / Chapter 3 of 6, 17:05 in", "Halden Private, a bank for private clients / £150,000.00 to approve by Fri 16 Oct". Contrast against the darkest 5% of the wall behind each line: heading 11.9:1, names 7.6 to 9.1:1, facts 7.1 to 8.2:1.
- **Alt texts** rewritten for the changed screens (Undertow's square river-photo cover; Halden Private's pending £150,000.00 payment instead of a metal card; Lullwater at 23:22 with 16:52 left).
- **Lullwater's own data** was fixed in `app-screens/02` (clock 23:22, timer 16:52; see its notes).

**Fresh audit after the rework: 4 of 5**, against Sana (https://mobbin.com/sites/sections/cf567c70-dd59-4cc6-99c9-a8d4e761bb55), Bevel (https://mobbin.com/sites/sections/f324f5f1-a03a-4788-b1ef-9ddb8a4352c8) and Apple's "All in the family" section (structure only). Its one must-fix, the shadows above the far corners, was fixed after it (above); that fix has not been re-audited.

**Not done (nice-to-have from that audit):** a heading that makes a claim (for example "Three dark themes, each from its own design system", which is true: each app has its own `state.json`); a graphite left edge with one bright line instead of the silver band; more visible keys; a longer shadow for the nearer middle phone; captions 16 px lower; the camera pill centred on the clock's line; stronger reflections (at 2 to 6% they barely show).
