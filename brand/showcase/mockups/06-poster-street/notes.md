# 06 · Roadside board: Howl Hill Weekender

Render: `shot.png`, 1600 × 1200 at scale 2, made with `../render_still.py` (reduced motion; see below). Page: `index.html`.

## Direction
The Howl Hill festival hero printed on a large roadside board at golden hour, in a car park lined with eucalyptus. The print is perspective-matched to the board and multiplied into the photo, so the corrugated metal, the tree shadow on its top left and the low sun stay on top of the ink. One caption line in white over the dark tarmac. Feel words: bold, energetic, playful.

Source: the hero's own `heroes/04-neobrutalist-festival/index.html` in an iframe (1760 × 880 viewport; navigation scrolled out of frame; the hero's on-screen pause button left outside the 1680 × 784 print window, because a web control means nothing on paper).

Photo: Charlie Deets on Unsplash, `images.unsplash.com/photo-1599803654935-5b9d1c93578c`, free Unsplash licence (checked on the photo page), hotlinked. The board is blank in the original; there are no people. Shop signs behind the fence carried a legible business name, so a feathered `backdrop-filter: blur(2.4px)` band softens only that strip, like a shallow depth of field.

## References (Mobbin, cited by link only)
- Büro, brand in a real room: https://mobbin.com/sites/sections/b9ad8a1e-9770-4af9-b381-83ee5ac777f6 . The brand shown as it lives in a photographed place, at the place's own light.
- Analogue Agency, type over photo: https://mobbin.com/sites/sections/ce6ec47f-9562-4469-88db-1d1abeb05ccf . Big flat type on a real photograph stays believable when the photo keeps its texture.
Mobbin has no billboard or print mock-ups; two searches returned web pages about campaigns.

## System (engine)
`sketch --name "Howl Hill Billboard" --brand "#FFD400" --feel bold,energetic,playful ...`, `raw.textFace "Archivo"`, `raw.fontLicence` (Archivo is SIL OFL but not in the engine's open-font list), dials, `build`. Log: `engine-log.txt`.

| Dial | Value | Why |
|---|---|---|
| expression | 70 | a festival board at golden hour |
| brandPresence | 60 | festival yellow on the board |
| density | 10 | one board |
| energy | 55 | summer evening |
| roundness | 10 | square board edges |
| depth | 40 | shadows come from the sun in the photo |
| colorfulness | 55 | sky and yellow print |
| warmth | 45 | warm light stays in the photo, not in the neutrals |

Font: Archivo only. Type scale used: `body-md` 19 px (650 and 400).

## Outside the tokens, on purpose
- The homography: four corners measured on the placed photo (TL 223,206 · TR 1368,131 · BR 1386,709 · BL 202,730) solved into a `matrix3d` in the page.
- Two multiply layers (the print, and a warm falloff across it) and the feathered blur band. The caption is white on the tarmac, 14:1 or more.

## Look and fix
1. First render: convincing at once, but the hero's pause button showed on the board, a black nav border ran along the top edge, a strip of bare board showed above the print on the right, and a shop name behind the fence was legible.
2. Second and third renders: wider iframe so the pause button falls outside the print, offset 96 px instead of 88 to drop the nav border, top-right corner moved up 4 px, background signs softened. The marquee stopped at a different place on every render, so the final render uses reduced motion.

## Checks
- `validate`: passes; 2 light-mode warnings about yellow buttons that are not in this scene.
- `review`: it listed the mask gradients' `#000` as colours and suggested `--ds-color-text-on-action`. Marked `od-ignore` and recorded as a bug.
- `preflight`: M9 false error for Archivo.

## Process findings
- `brand/tools/shot.py` has no reduced-motion option, so animated work inside an iframe is captured mid-animation; `render_still.py` in this folder adds it.
- Nothing helps source photos (licence, credit, background brand names); recorded as a gap.
