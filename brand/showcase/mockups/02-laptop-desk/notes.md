# 02 · Laptop on a desk: Halde Architekten

Replaced on 2026-10-14 by mockups/09-laptop-dashboard after the Mobbin audit (score 2).

Render: `shot.png`, 1600 × 1200 at scale 2. Page: `index.html`.

## Direction
The Halde Architekten hero shown the way an architecture studio would present its own site: on a laptop standing on an oak table against a grey plaster wall, in soft afternoon light. The laptop is generic and drawn in CSS 3D; the room is a real photograph. One credit line on the wall, with the studio's red as a single dot. Feel words: calm, sober, understated.

Source render: `heroes/01-swiss-architecture/shot.png` inside the laptop screen.

Photo: Mark Huang on Unsplash, "a wooden table with a white wall in the background", `images.unsplash.com/photo-1717911100016-17d359d902da`, free Unsplash licence (checked on the photo page), hotlinked, no people, no brand names.

## References (Mobbin, cited by link only)
- Squarespace, laptop on a table: https://mobbin.com/sites/sections/c933603d-46cb-4b6f-b166-3973ca7bd660 . A frontal laptop on a table against a textured wall, camera just above the table: the keyboard deck shows as a thin band.
- Squarespace, monitor on a desk: https://mobbin.com/sites/sections/563c7e39-871d-485e-b254-eff34fef7bf7 . Props stay small and at the edge; the screen is the brightest thing in the room.
- Riverside, devices: https://mobbin.com/sites/sections/601ce269-1efe-407c-9fb5-7272f7504f43 . Laptop proportions: a thin black bezel and a slab base wider than the lid.

## System (engine)
`sketch --name "Halde Studio Desk" --brand "#D7351F" --feel calm,sober,understated ...` (first run used "precise", which the engine does not know and dropped; see findings), `raw.textFace "Inter"`, dials, `build`. Log: `engine-log.txt`.

| Dial | Value | Why |
|---|---|---|
| expression | 35 | the photograph carries the mood; type is a credit line |
| brandPresence | 20 | red appears only as one dot |
| density | 10 | one object on a table |
| energy | 15 | afternoon light |
| roundness | 20 | machined aluminium, tight radii |
| depth | 60 | a real object casting a real shadow |
| colorfulness | 15 | plaster grey, oak, aluminium |
| warmth | 30 | cool grade on the photo |

Font: Inter only (SIL OFL). Type scale used: one size, `body-md` 19 px (600 and 400).

## Outside the tokens, on purpose
- **Perspective.** The 3D stage uses the photo's vanishing point (808, 598): the image centre, which the table's receding side edge passes through (measured on the render: slope 0.70 through 1271,920 and 1557,1120). `perspective: 4000px`; deck 1190 × 833 units, front edge 577 units behind the picture plane, lid tilted 13°.
- **Laptop materials and shadow.** Aluminium gradients, keyboard well and a projected 2D footprint shadow (the same vanishing point) are art, marked `od-ignore`.
- **Photo grade.** `saturate(.62) brightness(1.03) contrast(1.04)` so the oak loses its orange, plus a soft window gradient from the left. This keeps the owner's colour rule (no warm brown mid-tones) without hiding the material.

## Look and fix
1. First render: the scene worked but the laptop floated (its 3D shadow plane did not render), the keyboard read as one row of tall bars, and the deck sides did not follow the table edge. Measured the table edge and corrected the vanishing point from my first guess (803, 563) to (808, 598); replaced the 3D shadow with a projected 2D one; widened the key gaps so rows survive the foreshortening.
2. Second render: shadow visible under the front edge and falling right, away from the window; deck shaded darker toward the hinge. Checked at 200%.

## Checks
- `validate`: passes, 0 warnings. `review`: clean after marking device and shadow art (first run listed 30 values, all laptop materials, plus three SVG shadow fills).
- `preflight`: M9 false error for Inter (Google Fonts link; loaded in the browser check). No sizes read.
- Contrast of the credit on the plaster wall, 5th-percentile background pixel: 4.83:1 (19 px, dark ink). Passes 4.5:1 with a small margin.

## Process findings
- Unknown feel words are silently dropped when feel is delegated ("precise"), see 04.
- No help for photo-based mockups: vanishing point, perspective and shadow had to be measured and hand-written (recorded as an idea: a mockup helper).

## Round 3 (2026-10-15)
Hero 01 was rebuilt (its project index was removed; it is now one building section with sun angles), so the screen's alt text was rewritten: a section through Haus am Hang in Flims with the solar-noon sun angles for 21 December and 21 June, and the headline "Houses that follow the sun". Re-rendered `shot.png`. A fresh audit scored the scene **2 of 5**, as before: the CSS laptop still has a legend-less keyboard, a MacBook outline with its thumb notch, no hinge and flat lighting. This piece was replaced by `mockups/09-laptop-dashboard` and is out of the gallery; Kunal to decide whether to keep or remove it.
