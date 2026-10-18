# 03 · Watch trio: three faces on generic cases

Replaced on 2026-10-14 by mockups/10-multi-device after the Mobbin audit (score 2).

Render: `shot.png`, 1600 × 900 at scale 2. Page: `index.html` (dark theme pinned with `data-theme="dark"`).

## Direction
Product photography in CSS: three generic watch cases in graphite, silver and black, close up, lit by one soft key light from above and a cool rim light from the left, falling off into black at the top and bottom. The middle case is nearest the camera. Bands are plain straps with pin holes. No real device shape copied beyond what every watch has (a rounded case, a crown, a side button). Feel words: premium, sleek, bold.

Source renders: `watch/01-ridgeline-trail`, `03-tidemark-face`, `04-headway-transit` (the renders already carry rounded display corners).

## References (Mobbin, cited by link only)
- Oura, ring line-up: https://mobbin.com/sites/sections/4f570743-322c-4f19-8ef0-961c70f2b6d7 . Products in one row under one light, each finish different; the light and the falloff do the selling.
- Apple, three phones on black: https://mobbin.com/sites/sections/fae8666e-aa8f-401c-8456-63eea00ed5d9 . Devices on black with a thin rim light; the middle one faces the camera.
Mobbin has no watch platform and no product-photography sections as such; these two were the closest.

## System (engine)
`sketch --name "Wrist Studio" --brand "#5CC8FF" --feel premium,sleek,bold ...`, `pick Q-color-21 near-black`, `raw.textFace "Sora"`, dials, `build`. Log: `engine-log.txt`.

| Dial | Value | Why |
|---|---|---|
| expression | 60 | light is the drama |
| brandPresence | 25 | blue only in the screens |
| density | 10 | three objects |
| energy | 35 | still, but crisp highlights |
| roundness | 70 | rounded square cases |
| depth | 90 | speculars, rim light, deep shadows |
| colorfulness | 25 | graphite; the screens bring colour |
| warmth | 20 | cool studio grey |

Font: Sora only. Type scale used: one size, `body-sm` 15 px (650 title, 400 names). At 1600 × 900 the caption is small on purpose: the faces are the subject.

## Outside the tokens, on purpose
- Backdrop light uses `neutral-dark-3/5` and `accent-dark-6` (tokens); case metal, glass, crown knurling, band shading and pin holes are art (`od-ignore`).
- Case geometry is the display (205 × 251 at 1.42–1.6×) plus a 13 px black glass ring and a 9 px metal rim; radius follows the render's 48 px display corner.

## Look and fix
1. First render: bands as wide as the case looked like flat curtains, the right band read brown, the metal looked like plastic. 
2. Second render: bands narrowed to 60% of the case, rounded, shaded darker under the case, pin holes on the lower strap, the brown band replaced by near-black; the cases got a top-left specular and a cool left rim. Checked at 200%: crown and button sit on the right edge, no hard seams.

## Checks
- `validate`: passes; 2 warnings that do not apply ("in light mode, action primary background is too faint", but this scene pins dark and has no buttons).
- `review`: clean after marking case, band and crown art (23 lines).
- `preflight`: M9 false error for Sora. Caption contrast: `text-primary` and `text-secondary` on near-black, above 7:1.

## Process findings
- Light-mode warnings on a pinned dark scene (recorded, kind confusing).
- A watch platform and a product-photography reference pool are both missing (see the watch category report).

## Round 3 (2026-10-15)
Re-rendered `shot.png` (1600 × 900 at 2×) because `watch/03-tidemark-face` now reads "WED 14" (it said "TUE 14"; 14 Oct 2026 is a Wednesday). The pixel change is confined to the middle watch's date; nothing else in the scene changed. `check_dates.py --year 2026` passes.
Later the same day: the trail app was renamed **Fellrise** (Ridgeline is a real product name), so the caption and the first watch's alt text say Fellrise; re-rendered again. A fresh check confirmed both changes and found no regression, but kept the score at **2**: the earlier audit's reasons (an Apple Watch-shaped case, flat straps with dots, lit bands in the background) are still there, and `mockups/10-multi-device` replaced this piece. The 14 px lower position set for the two side watches never applies, because each watch's inline `margin:0` overrides it.
