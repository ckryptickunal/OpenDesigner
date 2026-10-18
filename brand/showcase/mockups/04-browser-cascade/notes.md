# 04 · Browser cascade: five heroes, one index

Render: `shot.png`, 1600 × 1200 at scale 2. Page: `index.html`.

## Direction
An editorial index page: five hero sections as browser windows stacked on an exact step (24 px across, 104 px down), so every window behind shows only its address bar and navigation, and the front one shows its whole hero. A numbered index on the left joins each name to its window with a hairline. Paper white, ink, a faint 12-column grid, one orange number for the window in front. Feel words: minimal, technical, refined (first run: precise, editorial, minimal).

Source renders: `heroes/09-japanese-ceramics`, `06-playful-fintech`, `08-y2k-retrofuture`, `02-luminous-devtool`, `07-climate-observatory` (front).

## References (Mobbin, cited by link only)
- Readymag, stacked sites: https://mobbin.com/sites/sections/0df56e85-333b-49b0-b2e3-0c500a699fcc . Each sheet behind shows only its top strip, so many sites read at once without clutter.
- Cosmos, stacked cards: https://mobbin.com/sites/sections/8e070129-3de0-457a-b6a0-39ace1cc6015 . One item in front, the others offset behind it.
- Mailchimp, browser frame: https://mobbin.com/sites/sections/406a32a0-f61e-4f4c-b976-63e4a99fccdd . Window chrome kept quiet so the page inside leads.

## System (engine)
`sketch --name "Index of Heroes" --brand "#FF4F00" --feel minimal,technical,refined ...`, `raw.textFace "Geist"`, dials, `build`. Log: `engine-log.txt`.

| Dial | Value | Why |
|---|---|---|
| expression | 55 | editorial: a numbered index, exact steps |
| brandPresence | 30 | one orange number |
| density | 35 | five windows, five labels |
| energy | 25 | precise, not lively |
| roundness | 25 | small window radii |
| depth | 55 | stacked windows need shadow to separate |
| colorfulness | 15 | paper and ink; the heroes bring colour |
| warmth | 20 | cool paper white |

Font: Geist only (tabular figures on). Type scale used: `body-sm` 13 px (address bars), `body-md` 16 px (index, caption). Two sizes, 23% apart.

## Outside the tokens, on purpose
Window shadows are four layers built from `shadow-key` and `shadow-ambient` (the elevation steps do not describe stacked sheets). Everything else (colours, radii, spacing, type) is a token.

## Look and fix
1. First render: a 90 × 118 px diagonal step left letter-fragments of every hero showing ("S m b", "Sear at th") and read messy. 
2. Second render: the step changed to 24 × 104 px with wider windows, so each window behind shows only its chrome and navigation; the index rows line up with each address bar.

## Checks
- `validate`: passes; 1 warning (orange action colour on white 2.994:1; no buttons here).
- `review`: one real finding, `padding: 2px` on the address pill, fixed to `var(--ds-space-2)`. Clean after.
- `preflight`: M9 false error for Geist. Contrast: 13 px address text `text-secondary` on white about 7:1; caption 5.66:1 at the 5th percentile.

## Process findings
- "precise" and "editorial" were unknown feel words and were dropped without a question because feel was delegated (recorded, kind confusing).
- `review` flags 2 px against the rem standard while every spacing token is in px (also found by the watch builder).

## Round 3 (2026-10-15)
- **Nearmost, not Orrery.** Hero 02's brand was renamed (Orrery is a real open-source tool in the same field), so the index row, the address bar and the alt text changed. Heroes 02 and 07 were rebuilt, and the windows show the new renders.
- **`.example` domains** (the showcase's new rule, RFC 2606): kumokobo.example, plumpot.example, orbika.example, nearmost.example, isobath.example. They were .jp, .app, .radio, .dev and .org.
- **The audit's two old must-fixes, now done:** the 12-column background grid ("the editor's paper" above) is gone, since it was decoration with no data; and every connector line ends at the same 12 px before the stack (they used to end at each window's own edge, which the windows in front covered, so they read as five lengths).
- **Accessibility:** the index is an `ol`, and the five alt texts follow one pattern ("Plumpot, a money app for teens: hero section"); the front window's alt adds its headline.
- Re-rendered `shot.png` (1600 × 1200 at 2×, `../render_still.py`).

**Fresh audit: 4 of 5**, against Readymag (https://mobbin.com/sites/sections/0df56e85-333b-49b0-b2e3-0c500a699fcc), Phantom (https://mobbin.com/sites/sections/27513f15-796b-4e65-bb7b-443364e226d9) and Webflow (https://mobbin.com/sites/sections/f0b2cf3b-c4b7-44bf-9e3d-e104422ef914). Caption 6.5:1, the orange "05" 5.4:1, address bars 6.7:1 or better. **Still open:** the 24 px strips of the back windows show fragments of their heroes (the curve of Nearmost's "8.7 ms" and a teal button edge); filling each back window below its navigation with its page colour would remove them.
