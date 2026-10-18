# Mockups: process report

Eight presentation scenes that show the finished showcase work the way a studio presents it in a case study or a launch post. Each one uses the real renders from `heroes/`, `components/`, `app-screens/`, `watch/` and `footers/` (as `<img>`, as a cropped background, or as a live `index.html` in an iframe), never a redraw. Scenes 01 to 07 were made through OpenDesigner end to end: Mobbin references, an engine system for the scene's own presentation style (`systems.py` runs every command and logs it to each `engine-log.txt`), tokens in the HTML, at least two rounds of look and fix, then `validate`, `review` and `preflight`. Scene 08 uses OpenDesigner's own brand system in `brand/design-system/project/`.

## The pieces

| # | Folder | Direction | Palette | Type (sizes used) | Render |
|---|---|---|---|---|---|
| 01 | `01-phone-trio` | Lullwater, Undertow and Halden Private in three generic iOS phones (no punch-hole; a short camera pill), the middle one face-on, the outer two turned 24° toward it, one light from the upper left (round 3) | Pale periwinkle wall (accent-light 2 to 6 of Undertow's #A9C4FF), graphite phones, deep navy ink | Manrope only. 30 and 19 | 1600 × 1200 |
| 02 | `02-laptop-desk` | Halde Architekten's hero on a CSS 3D laptop on an oak table against grey plaster, matched to the photo's vanishing point | Photo (plaster, oak, graded cool), aluminium, one red dot | Inter only. 19 | 1600 × 1200 |
| 03 | `03-watch-trio` | Fellrise, Tidemark and Headway on generic graphite, silver and black cases, lit like a product shot | Near-black studio, cool rim light; colour from the screens | Sora only. 15 | 1600 × 900 |
| 04 | `04-browser-cascade` | Five hero sections stacked on an exact 24 × 104 px step with a numbered index and hairlines | Paper white, ink, one orange number, faint 12-column grid | Geist only. 13 / 16 | 1600 × 1200 |
| 05 | `05-components-board` | A studio components page: five components at their real size (1:1) in a bento on black | Black board, hairline tiles, one lime "1:1" tag | Instrument Sans only. 13 / 16 | 1600 × 1200 |
| 06 | `06-poster-street` | The Howl Hill hero printed on a roadside board at golden hour, mapped with a homography and multiplied into the photo | Photo (sky, eucalyptus, tarmac), festival yellow and blue | Archivo only. 19 | 1600 × 1200 |
| 07 | `07-tablet-clinic` | The Wardlight ward observations screen (was Vigil, a real company) on a generic tablet lying on a white table, a glass of water at the edge, window light | White table, cool shadow, teal mark | Source Sans 3 only. 16 | 1600 × 1200 |
| 08 | `08-made-with-opendesigner` | Launch post in OpenDesigner's brand: "Every piece has its own design system." over a mosaic of ten pieces | Light theme: #fcfdff, ink #222428, cobalt #2338FF once (the lockup's circle) | Hanken Grotesk only. 32 / 108 (300, phrase at 650) | 1600 × 900 |

Before building I wrote the eight directions side by side (field, palette, font, layout idea, mood). No two share a font or a layout idea. The closest pair is 02 and 07 (both a device in a real photograph); one is a frontal laptop at table height in afternoon light, the other a top-down tablet on white. 03 and 05 are both dark, but one is lit product photography and the other a flat board.

Photos (all free Unsplash licence, each checked on its photo page, hotlinked from `images.unsplash.com`, no people): Mark Huang (02), Charlie Deets (06, a shop name behind the fence is softened), NordWood Themes (07).

## Honest assessment
- Strongest: 06 (the print takes the corrugation, the tree shadow and the low sun; it reads as a real board), 04 (exact and calm, every window behind shows only its navigation), 07 (calm and believable), 01.
- 02 works at full view, but the drawn keyboard is its weakest detail: at 200% the keys look diagrammatic next to the photograph.
- 03's cases are convincing at a glance but flatter than real product photography (CSS gradients, no environment reflections).
- 05 is a strong board; the date-picker tile's thin cream strip at the top (the card's own top edge) is slightly awkward.
- 08 follows the brand README to the letter and is deliberately quiet. Next to 04 and 06 it may read plain; that is the brand's choice (one idea, generous space), not an accident.

## Process findings, most important first

### The engine or a skill is wrong or missing something

1. **There is no scene or mockup idea anywhere in OpenDesigner.**
   - A presentation scene needs a field colour, device geometry (bezel, corner radius, camera), materials (metal, glass) and long shadows for objects floating above or resting on a surface. None of these are tokens. The largest elevation step is `0 32px 64px`, too short for a phone floating over a field.
   - Evidence: `engine.py review --project <scene>` listed 17 hard-coded values in 01, 30 in 02, 29 in 03 and 24 in 07, every one a device material, bezel or shadow. Each was then marked `od-ignore` by hand.
   - Every builder of a device mockup will hand-write the same geometry and maths (vanishing points, homographies, shadow stacks). Recorded as a gap (01) and an idea for a mockup helper (02).
2. **Preflight's type checks cannot see what these pages render.**
   - M9 raised "font X is used but has no @font-face" on all 8 scenes. Every face loads through a Google Fonts `<link>`, as the brief allows, and a browser check (`document.fonts.check`) returned true for all eight.
   - For engine pages it printed `font sizes in px: []` (the sizes are rem in `tokens.css`). For 08 it did the opposite: it counted every size declared in the linked `tokens.css` and reported "13 distinct font sizes" and "sizes within 10%: (48, 51), (67, 72)", plus "Source Code Pro is used". The page renders two sizes (32 and 108, measured in the browser) and never uses Source Code Pro.
   - The checks that matter most for this test (fonts and scale discipline) said nothing true. Recorded (02, 08).
3. **`engine.py review` gives wrong advice for anything that is not UI.**
   - It proposed `var(--ds-radius-overlay)` (16 px) for a 46 px tablet corner, `--ds-elevation-raised` for a 1 px inset hairline (05, 07), and `--ds-color-text-on-action` for the `#000` inside a CSS mask gradient (06).
   - It also flags `padding: 2px` against the "spacing in rem" standard while every `--ds-space-*` token is in px (04, 05). Recorded (06, 07).
4. **Unknown feel words are dropped without a question when feel is delegated.**
   - `sketch --feel precise,editorial,minimal --delegated feel,...` printed "I don't know the feel word 'precise' yet, so I left it out" and the same for "editorial", then built 04 from "minimal" alone. 02 lost "precise" the same way.
   - These are everyday designer words. I re-ran with known words (sober, technical, refined). Recorded (04).
5. **Neutrals come out the same, and a coloured ground cannot be asked for.**
   - Four of seven systems got near-identical cool neutral ramps (step 3: #e8ecf1 in 02, #e7ecf4 in 03 and 04, #e8ecf3 in 07; step 12 #222428 in all four), despite different brands and feels.
   - `raw.neutralTint "brand"` in 01 moved step 3 only to #ebebf0, far from the lilac field the scene needed, so the field is built from `accent-light-2` to `-6`. There is no "page tone" or "field colour" answer (the footer builder found the same). Recorded (01).
6. **Validate warns about light-mode buttons in scenes that have no buttons and pin dark.** 03 and 05 pin `data-theme="dark"` and still get "In light mode, action primary background on base surface is too faint (1.849:1)". 04 and 06 get the same for colours that never become buttons. Recorded (03).
7. **Nothing helps with photographs, which the brief now allows.**
   - Unsplash search results mix free and Unsplash+ photos, so every candidate's photo page had to be opened to confirm the licence and the photographer.
   - The billboard photo had a legible business name on a sign behind the fence. Nothing would have caught it; I found it by zooming the render and softened it with a feathered blur.
   - `opendesigner-illustrate` covers open-licence SVG only. Recorded as a gap (06).

### Where I worked around something (recorded so the next builder knows)
- **`brand/tools/shot.py` has no reduced-motion option.** 06 shows the hero live in an iframe, and its marquee stopped at a different place on every render (once leaving an empty strip on the board). `render_still.py` in this folder is `shot.py` plus `reduced_motion="reduce"`; the final 06 render uses it.
- **Perspective was measured by hand.** 02's vanishing point came from the table's side edge (slope 0.70 through 1271,920 and 1557,1120, which passes through the image centre at 808,598). 06's four board corners were found by thresholding the photo and zooming each corner on a 10 px grid. 05's crop offsets came from each component page's DOM boxes via Playwright.
- **Work that should not appear in print:** the Howl Hill hero's on-screen pause button was pushed outside the print window by widening the iframe, and its navigation was scrolled out of frame.
- **Brand system (08):** the project ships no compiled `tokens.css` (the `_local/` copy is git-ignored), so `build_tokens.py` compiles one from `tokens.json` in the same format. The README has no rule for image tiles in a mosaic (I used `radius-container`, a 1 px `line`, no shadow) and nothing on colours inside showcased work that compete with cobalt (I swapped the Howl Hill tile out).
- **Mobbin:** searching "case study" returns case-study listing cards (logos and text), not device presentations, and there are no billboard, print or product-photography sections. Describing the layout instead ("three phone mockups at different heights", "stacked browser windows", "components at real size") found Sana, Readymag, Retool, Squarespace, Daylight and Oura, which taught the structures used here.
- **Contrast on photos and gradients** had to be measured on the render (5th-percentile background pixel). Two captions were fixed this way: 01's names were 4.36:1 on the lit field (now 7.45:1 in the field's deep ink), and 07's secondary caption was 4.59:1 in the darkened corner (now 4.87:1).

### What helped
- `--surfaces "case study:experience"` gave spacious density and marketing display sizes in one answer.
- Delegating with a list (`feel,audience,platforms`) kept every brand hex exact: `accent-light-9` equals the given hex in all seven systems.
- `systems.py` built all seven systems in seconds and kept a log of every decision; `decisions.md` in each system says why each dial moved.
- `review` plus `od-ignore` made every page end clean, with each deliberate raw value marked on its line.
- The brand README for 08 is precise enough to follow without guessing: styles with sizes, three highlight methods ranked by loudness, the one-accent rule and which lockup to use when the accent is spent.

## Checks (all scenes)
- `engine.py validate`: 01 to 07 pass with no errors. Warnings only in 03, 04, 05 and 06, all the light-mode button warnings in finding 6.
- `engine.py review --project <scene>`: clean for all seven after the fixes (`padding: 2px` to `space-2` in 04 and 05) and `od-ignore` on art lines.
- `preflight.py html --medium web`: the only errors are the false M9 font errors (finding 2). A browser check confirmed every face loaded and measured every rendered text size, listed in the table above.
- Contrast: measured on the renders. All caption text passes 4.5:1, most of it 7:1 or more.

## Feedback recorded
Each gap is in the `feedback.md` next to the system it came from (`engine.py feedback`, written locally, nothing posted): 01 has 2, 02 has 2, 03 has 1, 04 has 1, 06 has 2, 07 has 1, 08 has 1.

## Housekeeping
- `brand/.gitignore` still ignores the whole `showcase/mockups/` folder ("Unfinished mockups"). The scenes are finished, so the owner may want to narrow that rule to the PNGs. I did not edit it (it is outside this folder).
- The disk had about 350 MB free while rendering; one render failed with "No space left on device" and was re-run after I cleared my own scratch files.
- Renders: `shot.png` in each folder at scale 2 (git-ignored by design; the gallery makes thumbnails from them). 06 uses `render_still.py`; the rest use `brand/tools/shot.py`.
