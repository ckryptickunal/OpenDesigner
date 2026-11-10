# 05 · Components board: five components at their real size

Render: `shot.png`, 1600 × 1200 at scale 2. Page: `index.html` (dark theme pinned).

## Direction
A studio's components page: a black board with a bento of five tiles, each a window onto a finished component render shown at 1:1 (one CSS pixel of the component is one CSS pixel here). Light and dark components side by side, hairline tile edges, one lime "1:1" tag as the only accent. Feel words: techy, minimal, bold.

Source renders (each `shot.png` drawn as a background at 1440 × 900, offset to the component's own layout box): `components/02-command-palette` (Margin), `08-music-player` (Calamondin Tapes; Pomelo Tapes before round 3), `01-pricing-glass` (Gloaming), `05-toast-stack` (Kinroom; Chorus before round 3), `03-date-range-picker` (Wayfern). Crop offsets were measured from each page's DOM boxes with Playwright, not guessed.

## References (Mobbin, cited by link only)
- Retool, components field: https://mobbin.com/sites/sections/2516034c-7096-4637-80c6-424444c9d100 . Real components at real size on one plain field read as a kit.
- Framer, resources: https://mobbin.com/sites/sections/aca5d0bf-a0de-4105-933d-b0e993d85024 . A dark board with rounded tiles that crop each preview.
- Retool, bento: https://mobbin.com/sites/sections/0daad8f7-cdde-4ef2-a454-2a26d2bbe0a5 . Mixed-width tiles in two rows keep a grid without a uniform rhythm.

## System (engine)
`sketch --name "Components Board" --brand "#C6F432" --feel techy,minimal,bold ...`, `pick Q-color-21 near-black`, `raw.textFace "Instrument Sans"`, dials, `build`. Log: `engine-log.txt`.

| Dial | Value | Why |
|---|---|---|
| expression | 50 | a studio components page |
| brandPresence | 25 | lime only marks scale |
| density | 40 | five tiles in a bento |
| energy | 30 | calm board |
| roundness | 55 | tiles with medium corners (20 px) |
| depth | 20 | flat tiles, hairline borders |
| colorfulness | 20 | black board; components bring colour |
| warmth | 35 | neutral black, no brown |

Font: Instrument Sans only. Type scale used: `label-md` 13 px (the tag), `body-md` 16 px (caption).
Grid (round 3): columns 344 / 240 / 48 / 792, rows 556 / 304 / 144, gap `space-16`, margins `space-64`. Row 1: palette 600 and music 856, as before. Row 2: pricing (664 × 304) over the toasts (664 × 144), beside the whole calendar (792 × 464). Before round 3: columns 360 / 224 / 200 / 640, rows 556 / 464.

## Outside the tokens, on purpose
Only the crop offsets (measured numbers). Tile borders are inset hairlines from `border-subtle` and white at 9% (`od-ignore`: review reads an inset 1 px line as elevation).

## Look and fix
1. First render: the palette tile showed the spec sheet's numbered callout dots on its right edge, the toast tile cut the message field mid-word, the date tile cut a calendar row in half.
2. Second and third renders: the palette tile now stops 8 px short of the palette's right edge (the dots sit exactly on it), the toast tile is cropped to the app panel with the field out of frame, the date tile ends between rows 3 and 4 and shows the card's top edge. "CHAPTER 3" no longer clipped.

## Checks
- `validate`: passes; 2 light-mode warnings that do not apply (dark pinned, no buttons).
- `review`: `padding: 2px` fixed to `space-2`; two hairline shadows marked. Clean.
- `preflight`: M9 false error. Contrast: lime tag text 13 px dark ink on lime above 12:1; caption secondary on black above 7:1.

## Process findings
- `review` maps any `inset 0 0 0 1px` to `--ds-elevation-raised`; a hairline is a border, not elevation (recorded with the 07 bug).

## Round 3 (2026-10-15): new layouts, new names, new crops
Components 01, 03, 05 and 08 were rebuilt with new layouts, and two were renamed because their names were close to real companies: **Chorus is now Kinroom** (`components/05`) and **Pomelo Tapes is now Calamondin Tapes** (`components/08`, catalogue prefix CLMD). The crop offsets were set for the old layouts, so they were measured again from each page's DOM boxes at 1440 × 900 (the page's top comment lists each one), and the board was re-gridded after a fresh audit (score 3) found tiles that cut content badly:
- **Pricing** (664 × 304): the Spark and Studio plan heads side by side, ending at the bottom of the Studio head, so no table values appear without their row labels.
- **Toasts** (664 × 144): Kinroom's stack of three toasts with the composer's Send button whole.
- **Dates** (792 × 464): Wayfern's whole calendar width, month labels to Sunday, from the heading to the end of the fifth week, so the stay Fri 23 to Tue 27 Oct shows whole.
- **Music**: the player card with the start of the track list, stopping before the release column.
- Aria-labels rewritten from the new pages; the caption now reads "Margin, Calamondin Tapes, Gloaming, Kinroom, Wayfern". Re-rendered `shot.png` (1600 × 1200 at 2×).

**Fresh audit after the re-grid: still 3 of 5**, against Retool (https://mobbin.com/sites/sections/2516034c-7096-4637-80c6-424444c9d100), Chronicle (https://mobbin.com/sites/sections/d56f6dd4-a959-448d-a7cc-c0c2f145fce4) and Base (https://mobbin.com/sites/sections/d4f3d376-5f46-430f-b7f6-0b3d82a90917). The three earlier must-fixes are fixed (pricing labels, the calendar's Monday and November label, the Send button), but every tile still cuts something at an edge, so the board reads as windows onto pages rather than whole components, and there is one caption for the board instead of one per tile. The "Look and fix" section above describes round 2.

**For Kunal: the board's idea needs a decision.** "Windows onto pages at 1:1" will always cut something; the references frame each component whole and name each tile. Either keep the windows idea and accept 3, or rebuild it as framed components with a label on each tile (the next step to 4).
