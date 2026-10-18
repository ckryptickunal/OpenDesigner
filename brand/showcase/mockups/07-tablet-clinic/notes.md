# 07 · Tablet on the ward: Wardlight

Render: `shot.png`, 1600 × 1200 at scale 2. Page: `index.html`.

## Direction
The Vigil ward dashboard on a generic tablet lying on a white table, seen from above, with a glass of water half out of frame and soft window light falling across the table from the upper left. Calm and believable, nothing clinical-cliché (no stethoscope, no hands). Feel words: calm, trustworthy, clean.

Source render: `app-screens/10-clinical-vitals/shot.png` (1180 × 820 at 2x) inside the frame.

Photo: NordWood Themes on Unsplash, `images.unsplash.com/photo-1567011345445-fd175f248019`, free Unsplash licence (checked on the photo page), hotlinked and enlarged (2240 px wide) so the glass sits half out of frame.

## References (Mobbin, cited by link only)
- Daylight, device on a surface: https://mobbin.com/sites/sections/3ffb34f4-4713-4a4d-a05e-d18961771f0b . A tablet lying flat with window shadows crossing it; the light makes it real.
- Superpower, tablet dashboard: https://mobbin.com/sites/sections/4f2c6ee9-bebc-4c9b-82ef-15e8ba9f2a4f . Bezel proportion for a health dashboard on a tablet; nothing else on the plate.
- Ease, healthcare calm: https://mobbin.com/sites/sections/5a0b10db-4029-4d40-9eec-d3f3a58d9aa5 . One product surface on a soft field, generous space around it.

## System (engine)
`sketch --name "Vigil Ward Tablet" --brand "#127C7C" --feel calm,trustworthy,clean ...`, `raw.textFace "Source Sans 3"`, `raw.fontLicence`, dials, `build`. Log: `engine-log.txt`.

| Dial | Value | Why |
|---|---|---|
| expression | 35 | clinical calm |
| brandPresence | 30 | teal only in the caption mark |
| density | 15 | one tablet on a table |
| energy | 15 | night-shift quiet |
| roundness | 60 | tablet corners |
| depth | 55 | a device resting on a surface |
| colorfulness | 20 | white table, teal accent |
| warmth | 25 | clean daylight white |

Font: Source Sans 3 only. Type scale used: `body-md` 16 px (600 and 400).

## Outside the tokens, on purpose
Tablet geometry (46 px outer radius, 22 px bezel, 3 px aluminium rim, camera dot), its four-layer resting shadow cast down and right, and the window-light multiply layer. All marked `od-ignore`.

## Look and fix
1. First render: a mullion shadow crossed the screen's header and greyed "Find patient". Moved the window shadows to fall on the table and the tablet's lower-right corner only.
2. Second render: calm, readable; then the checks showed the secondary caption at 4.59:1 in the darkened bottom-right corner, so the edge falloff was lightened (alpha .6 → .42).

## Checks
- `validate`: passes, 0 warnings. `review`: clean after marking device art (it suggested `--ds-radius-overlay` 16 px for a 46 px tablet corner).
- `preflight`: M9 false error for Source Sans 3. Contrast: caption secondary 4.59:1 at the 5th percentile before the falloff fix, 4.87:1 after (dark ink on the white table).

## Process findings
- `review` treats device geometry as UI and proposes UI tokens for it (recorded, kind bug).

## Round 3 (2026-10-15): Wardlight, not Vigil
"Vigil" is a real company in this field (Vigil Health Solutions, nurse call and resident monitoring), and `app-screens/10-clinical-vitals` was rebuilt as **Wardlight**, an iPad split view. This scene shows that screen, so:
- **Renamed** in the page title ("Wardlight on the ward"), the top comment, the screen's alt text and the caption. The scene's engine system is now "Wardlight Ward Tablet" (`engine.py set name ... --set-by delegated`, then `build` and `design-md`; logged in `engine-log.txt`). The old export `opendesigner/build/dtcg/vigil-ward-tablet.resolver.json` was moved to the macOS Trash; the decision log keeps the reason for the rename.
- **New alt text**, from the new screen: Wardlight on Ward 4B at 02:16, patients sorted by NEWS2, Rosa Halvorsen in bed 7 at NEWS2 8, an emergency response called at 02:04, the registrar paged 12 minutes ago and not yet acknowledged, and her observation chart from 22:00 to 02:15.
- **Re-rendered** `shot.png` (1600 × 1200 at 2×) with the new screen; nothing else in the scene changed.

**Fresh audit, 4 of 5** for the render (a reviewer that did not build it), against Poly (https://mobbin.com/sites/sections/954077a6-b1a9-4625-8e1f-5e0d6fc7783d), Daylight (https://mobbin.com/sites/sections/7655435a-d6e7-4c7c-897a-5ddf03b3b015) and Superpower (https://mobbin.com/sites/sections/4f2c6ee9-bebc-4c9b-82ef-15e8ba9f2a4f). It re-scored NEWS2 for every column (2, 4, 5, 6, 7, 8, as shown). The window light only touches the Trend sparklines in the screen's lower right (at most 17/255) and no text. Caption contrast: "Wardlight" 10.8:1, "Ward 4B at night…" 5.1:1, "Tablet, 1180 × 820" 4.96:1 (it sits inside a window-shadow band, so its margin is thin).

**Still open:**
- The earlier audit's scene fixes were not part of this round: a matte graphite rim instead of the silver one (the silver rim, thin even bezel and long-edge camera read as today's iPad Pro), a shadow toward the lower left instead of the long lifted one, a reflection on the glass, and the right caption moved out of the shadow band.
- "Vigil" is still in the gallery (`brand/showcase/index.html` and the committed thumbnail `_thumbs/mockups--07-tablet-clinic--shot.jpg`, which also shows the old screen's wrong weekday for 14 Oct). The gallery takes its titles from each notes.md's first line, so this file's title must change before `build_gallery.py` runs (done below). Outside this folder: `app-screens/10`'s notes title, `app-screens/PROCESS-06-10.md`, and that piece's old `vigil.resolver.json` and `findings.measured*.json` still say Vigil.
