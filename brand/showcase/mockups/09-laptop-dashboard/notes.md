# 09 · Quoin payments on a laptop

Replaces `mockups/02-laptop-desk` (audited 2 of 5, "remake"). Render: `shot.png`, 1600 x 1200 at scale 2 (3200 x 2400), made with `../render_still.py --wait 2500`. Page: `index.html`.

## Direction
The new B2B product screen `../../product/01-quoin-payments/shot.png` (Quoin, the payments table of Tamsin & Rowe, a tableware and kitchen supplier: 2,418 payments in the last 7 days, the newest rows from the last two hours, three rows selected for export) on a real laptop on a dark wooden table by a window, afternoon daylight. The scene must look photographed: the screen sits in the photo's own display, in its perspective and its light. Feel words: **calm, sober, technical**.

What the old piece did that this one must not (`../../audit/mockups--02-laptop-desk.json`): a CSS laptop with a legend-less keyboard pasted on a photo, no contact shadow, a full-brightness screen with no glass, a MacBook outline drawn as "generic", and a laptop filling a quarter of the frame. Here the laptop is real (keys, hinge, shadow and table reflection all photographed), only the screen is placed, and the laptop fills about 80% of the width.

## Photo
Dillon Shook on Unsplash, "photo of black MacBook Pro on table", https://unsplash.com/photos/xbFX7qCoAqI, free Unsplash licence ("Free to use under the Unsplash License", checked on the photo page). Hotlinked from `images.unsplash.com/photo-1515803171005-2d5e90f7b4d3` at 3600 px; no copy is kept in the repo. No people. The display was off, which is what makes a clean placement possible.
- **Brand mark removed:** the bezel under the display carries a printed model name. A clone of the plain bezel 250 source px to its left (same band, same slope) is laid over it with a clip path; at 200% the band shows no seam. No logo is visible anywhere else (the lid's back faces away).
- **Residual risk, said plainly:** the machine is a real 15-inch laptop of one brand. Its name is gone, but its shape is that brand's. The audit rule was about devices we draw; a photographed product is that product.

## References (Mobbin; cited by link only, nothing saved)
| Reference | What it taught |
|---|---|
| Legora, product hero: https://mobbin.com/sites/sections/de997de8-3e43-4060-a258-2b2e10dea2ca | A B2B product on a photographed laptop in window light: the screen is a little dimmer than the room and shares its light. |
| Craft, hero video still: https://mobbin.com/sites/sections/58c31ff2-407c-4d33-933f-3b0a08528728 | A photographed laptop whose UI is lit like the room rather than pasted at full brightness. |
| Mailchimp, workspace section: https://mobbin.com/sites/sections/6f6f0323-3daa-4130-a9dc-03ca1bf8a988 | A dashboard on a real laptop inside a real scene, cropped close (that one has a person; ours keeps none). |

## How the screen was placed
1. Downloaded the 4000 px original to a scratch folder outside the repo (deleted afterwards) to measure.
2. Fitted straight lines to the lid's black glass on four sides (top and sides by thresholding against the wall and window; bottom by a luminance profile across the bezel band, which steps from 3 to 24 at one line, `y = 0.185x + 1473`).
3. Solved the camera's focal length from the two vanishing points (f = 6638 px, about a 60 mm lens on full frame), which gives the black glass a true aspect of 1.573:1. An estimate from the published 15.4-inch 16:10 panel plus even bezels gives 1.563:1, so the two agree within 1% [the bezel widths are inferred].
4. Inset a 16:10 active area (7.2 mm sides and top, 5.6 mm bottom in lid millimetres) through that homography and mapped the 1440 x 900 screen onto it with `matrix3d`. Measured on the render, the right bezel grows from 34 to 37 px toward the camera, as it should.
5. Light: the panel at `brightness(0.9) contrast(0.95) saturate(0.95)` so its white sits just under the wall's; a multiply falloff toward the far (left) edge for viewing angle; one broad 3-7% white sheen from the upper left; a 6 px inner edge darkening where the panel meets the black glass; 7% photographic grain so the screen shares the photo's texture.

## System (engine)
Full log: `engine-log.txt`.
```
sketch --name "Quoin Desk Scene" --brand "#0f6b66" --audience regular --platforms web --feel calm,sober,technical --surfaces "case study:experience" --delegated feel,audience,platforms
set raw.textFace "Geist"; set raw.fontLicence {...}; set dials.* (below); build; design-md
```
| Dial | Value | Why |
|---|---|---|
| expression | 30 | the photograph does the mood; type is one credit line |
| brandPresence | 20 | teal lives only inside the product screen |
| density | 10 | one object on a table |
| energy | 15 | quiet daylight |
| roundness | 30 | the product's own 6 px controls |
| depth | 50 | a real object in real light; the photo carries it |
| colorfulness | 10 | grey wall, dark wood, space-grey metal |
| warmth | 30 | cool daylight, no brown cast |

## Font and type scale
One family, **Geist** (SIL OFL, Google Fonts), the product's own face, so the scene adds no second one. One size: `body-sm` 16 px, weights 500 (left) and 400 (right). The product screen inside is the product's own render.

## Outside the tokens, on purpose
The photo, the four measured corners and the solved homography, the clone-stamp clip path, the falloff and sheen gradients (marked `od-ignore`), the grain filter.

## Look and fix (rounds, scores)
1. **Round 1, score 4.** Convincing at full view. At 200% I checked every corner: the bezel is even, the clone stamp is invisible, the screen's bottom edge cuts the product's floating bulk bar the way a real viewport does.
2. **Round 2, score 4.** Measured the caption on the render: the white left caption sat on the window's reflection in the table and measured **1.6:1** (the 1600 px preview hid it). The caption moved to the top, in ink, over the bright window and wall: 9.0 to 10.0:1. The grey right half measured 4.2:1 on the wall, so both halves are now ink, told apart by weight.
3. Considered and rejected: a light spill from the screen onto the keys near the hinge. In this exposure it would be a few percent and risked reading as a painted glow.
4. **Round 3 (B2B fix round), score 4.** Quoin's screen was re-rendered: the merchant is now a tableware and kitchen supplier, the rows cover the last two hours, and the Edit columns popover moved to its own frame (`shot-columns.png`). The page links the product's `shot.png`, so the new screen dropped into the same measured corners and the same light with no change to the perspective; I updated the alt text and the right caption ("A tableware supplier's finance team, 2,418 payments in 7 days", 8.9:1 measured) and re-rendered.

Final score **4 of 5**. Compared at the same size with Legora and Craft: the light and perspective hold, and the screen is readable (the status tiles, the selected rows and the bulk bar read at 100%). Below 5 because the screen is a touch cleaner and brighter than Legora's, and because the laptop is recognisably one brand's shape.

## Checks
- `validate`: passes, 0 warnings. `review --project`: clean. DESIGN.md refreshed.
- `preflight --medium web`: M9 false error only (Geist loads through a Google Fonts link).
- Caption contrast measured on the render (5th-percentile background pixel): 8.9:1 or more for both halves.
- `brand/tools/check_dates.py brand/showcase/mockups --year 2026`: every weekday matches its date. The scene adds no names of its own; Tamsin & Rowe and Quoin are listed with this piece in `../../NAMES.md`.

## Process findings (this piece)
- **The display's active area is invisible when the screen is off,** which is exactly the photo you want. Finding it took line fitting, a focal-length solve and a lid spec. A helper that takes four corners and a target aspect would make every photo mockup honest. Recorded (idea).
- **A preview at 50% hides contrast failures on photos.** The left caption looked fine at 1600 px and measured 1.6:1. The check that caught it was a pixel measurement, which nothing in the process asks for on photo pages.
- The scene's own system adds little: one caption in one size. The work is photo measurement and light matching, which OpenDesigner has no step for (the same finding as `PROCESS.md` item 1).

## Rework 2026-10-14
After the independent audit (`../../audit/mockups--09-laptop-dashboard.json`, 3 of 5). It found the photographed laptop was a real Apple MacBook Pro with a Touch Bar (removing the printed name did not make it generic), the screen was a near copy of Stripe's Transactions page, and the left caption described the device size, not the product. The sections above describe the earlier photo and are kept as its record; this section replaces them where they differ. Render: `shot.png`, 1600 × 1200 at 2×, made with `../render_still.py --wait 2500`.

**Photo.** "a laptop on a desk" by Windows (@windows) on Unsplash, https://unsplash.com/photos/a-laptop-on-a-desk-FV6Pma5U_98, free Unsplash License (not Unsplash+; the photo's API record says `premium: false`, `plus: false`), checked 2026-10-15. Hotlinked from `images.unsplash.com/photo-1664575196412-ed801e8333a1` at its full 5504 px; no copy is kept in the repo. Credited here and in the page's top comment, the way `mockups/06` and `mockups/07` credit their photos; nothing in a mockup scene carries an on-page credit.
- **What is in frame:** a small sage laptop on a white desk by a window, with a mug, an envelope, a notebook and a calculator. No logo or brand text is visible: the lid's back faces away, the bezel and deck are plain, and the Windows key's printed glyph is a blurred patch a few pixels wide. No clone stamp was needed.
- **Owner decision pending: the device is recognisable.** It is a Microsoft Surface Laptop Go (sage, 3:2 panel, USB-A, USB-C and headphone jack on the left), in Microsoft's own photo posted by its Windows account. It meets the brief as written ("a current non-Apple laptop", no logo), but anyone who knows laptops will name it, which is the same kind of problem the MacBook was. The Unsplash License covers the photo, not Microsoft's trademarks or product design. Kunal to decide: keep it, or re-source a photo where the laptop is unbranded or incidental to a person working (as Mailchimp's and Deel's sections are).
- **The photo is widely used:** 6.7 million views and 57,822 downloads (against 12,445 for the old one), so the scene is not ownable. Every less-used free photo of a non-Apple laptop the builder found had a printed logo, or was a manufacturer's shot with the screen lit.

**Screen.** The display is a 3:2 panel, so the page frames the live product page (`../../product/01-quoin-payments/index.html`) at 1440 × 960 in an iframe instead of the 16:10 `shot.png`, which would have needed cropping. It shows the product's default state (the To match queue, three suggestions selected) with one more table row than `shot.png`, and it follows the product page on every render. The screen is the reworked Receipts view, so the Stripe-like screen is gone (see `product/01`'s notes).

**How the screen was placed.** The photo was rendered at its full 5504 px in a scratch folder (deleted afterwards). Straight lines were fitted to all four edges of the lit display with sub-pixel crossings at about 60 points per edge (fit error 0.11 to 0.21 px); the corners are their intersections. In page px (photo at 0.6, shifted −1020, −750): [291.83, 162.37], [818.57, 85.43], [903.28, 530.13], [376.32, 650.96], mapped with a homography (`matrix3d`). The corners fit a true 3:2 rectangle at 90° with a focal length of about 8,500 px; the photo's EXIF focal length does not, which suggests the photo was cropped. The fresh audit laid the corners over the bare photo: they sit on the lit area to about 1 px, and none of the original wallpaper or taskbar shows at the edges.

**Light.** A multiply of `rgb(164 168 172)`: the photo's lit taskbar reads (153, 157, 160) beside a desk at (241, 243, 245), so the panel's white maps to a slightly cool 164. A faint screen-blend sheen from the window side (6% to 1.2%), a 4 px inner edge darkening at 30%, a 0.35 px blur and an overlay grain at 22%. All marked `od-ignore: device or photo art`.

**Captions.** On the flat desk top at the lower right, in ink, weight 500 then 400: "Quoin · Matching each customer payment to the invoice it pays" (what the team does, as the audit asked) and "Tamsin & Rowe, tableware wholesaler · 2,418 receipts, Oct 1–14" (the screen's period; "this week" was looser than the screen's filter). Measured at full size with the captions hidden, against the darkest 5% of the desk behind each line: 12.5:1 and 12.4:1 (the fresh audit measured 12.35:1 and 12.16:1). The alt text names the same facts: 2,418 payments received 1 to 14 October, 192 waiting to be matched, three suggested matches selected.

**Fresh audit (a reviewer that did not build it), 4 of 5,** against Legora (https://mobbin.com/sites/sections/de997de8-3e43-4060-a258-2b2e10dea2ca), Mailchimp (https://mobbin.com/sites/sections/6f6f0323-3daa-4130-a9dc-03ca1bf8a988) and Deel (https://mobbin.com/sites/sections/2b9279ed-4c25-4c50-84f2-5c23af38b44e). The photo work and the screen pass; what keeps it from 5 is the device (above) and a scene that reads as stock next to Legora's single quiet laptop. Its must-fixes were the credit (now here) and the owner decision (pending, above).

**Not done, from the audit's list** (small, each visible only at 200%): the photo's own display brightens about 12% from top to bottom and the composite is flat, so a top-to-bottom falloff would match it; the screen's grain varies about 1.1 levels against 1.6 to 2.1 in the photo (an opacity of about 0.33 instead of 0.22); a 0.5 px blur instead of 0.35 would match the photo's softness at 2×. The calculator in the foreground is a finance cliché, which only a different photo fixes.

**Checks.** `check_dates.py --year 2026` passes for this folder and for the product page. `engine.py review` and preflight are clean (M9's Google Fonts false error aside). The scene adds no names of its own; the customers visible on the screen are listed with this piece in `../../NAMES.md`.
