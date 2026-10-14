# 06 Knurl Supply: neo-brutalist footer

## Direction
Knurl Supply is a fictional streetwear label from Rotterdam that sells in timed drops and never restocks. Its footer is a poster wall: a black marquee announcing the next drop, then a grid of hard-edged blocks with 4 px ink borders and 6 px zero-blur offset shadows: acid lime newsletter block with a drop countdown, white link blocks, a black flagship-store block, and a knurled (diamond cross-hatch) block carrying a round stamp. Condensed black display type against a blunt mono.
Feel words: bold, edgy, loud.

## References (Mobbin, structure only)
- https://mobbin.com/sites/sections/091c7a61-be44-4c2d-bafa-fa3afe0da71c — a marquee band as the divider between newsletter and links, and a footer built from bordered cells instead of columns.
- https://mobbin.com/sites/sections/ab88d658-db2f-4436-b63e-f4a441f63b76 — each group of links is its own cell; the cell edges are the grid.
- https://mobbin.com/sites/sections/5cc26aaf-f102-42e9-984a-3c8768918494 — one cell can be pure graphic texture (there a dot matrix; here a knurl pattern) to give the eye a rest from type.
- Mobbin had no true neo-brutalist footer for the words I tried; the hard shadows and countdown come from the direction, not a reference.

## System (engine)
```
python3 $E --dir .../06-knurl-brutalist/opendesigner sketch --name "Knurl Supply" --brand "#c8ff00" --audience regular --platforms web \
  --feel bold,edgy,loud --theme system-light-dark --delegated feel,audience,platforms,theme,surfaces --surfaces "shop:persuade"
```
- Dials: expression 95 (a poster), brandPresence 90 (lime and black everywhere), density 60 (blocks packed edge to edge), energy 95 (marquee, loud type), roundness 0, depth 40 (meant as hard shadows; the engine made soft ones), colorfulness 70, warmth 35 (blunt, cool concrete).
- Faces: `raw.displayFace "Big Shoulders Display"`, `raw.textFace "Space Mono"`, `raw.monoFace "Space Mono"`, `raw.fontLicence` recorded (all SIL OFL).
- Build: no errors, 2 advisory warnings (lime action colour on white and on the base surface, 1.07 to 1.16:1). Every lime control here has a 4 px ink border, so the edge passes.

## Build
- Colours, type sizes, spacing, border widths (`--ds-border-width-4`, `-2`), focus and durations are tokens. Headline 90, block titles and countdown 51, marquee and button 28, links 16, labels 12 (after the owner's type rule; see below).
- Outside the tokens, on purpose: the hard shadow (`6px 6px 0` ink; there is no zero-blur depth style); 64 px control height (bigger than the system's control sizes, for the poster scale); the knurl pattern and stamp are SVG.
- Accessibility: ink on lime is 13:1, lime on ink the same; buttons 64 px, links 40 px; focus is a 4 px ring in accent step 11; the marquee has an aria-label with the full sentence and stops with reduced motion; the countdown has a role and label; decorative pattern and stamp are `aria-hidden`.

## Renders
- `shot.png`: 1440 wide, natural height (758 px after the type changes), scale 2. `shot-mobile.png`: 390 wide.
- Round 1: the black highlight behind "BEFORE" cut into the line above (line-height 0.86), the stamp's ring text overran and collided ("ESTKNURL"), and the lime block had a dead middle. Made the highlight an inline block, fitted the ring text with `textLength`, added a drop countdown.
- Round 2 (mobile): in a column the email field collapsed to a sliver (`flex: 1` in a column) and the base bar left an empty cell and a stray right border. Fixed both.

## Checks
- `preflight.py html`: 2 errors (Google Fonts false positives), 1 warning (`<br>` in the store address, which is an address, not a heading).
- `engine.py validate`: passes with the two advisory warnings above.
- `engine.py review`: 5 raw values (control heights and the hover shadow). It suggested `var(--ds-elevation-raised)` for the `3px 3px 0` hover shadow, which is a soft zero-size shadow in this system, so the wrong replacement.
- Checklist: sizes 12, 16, 28, 38, 51, 67, 90 from one scale; heading weight 900 on purpose (display only, the style demands it); every block edge on the 12-column grid; pills and labels stay on one line at 390.

## Owner type and color rules (applied mid-run)
- Fonts: two (Big Shoulders Display, Space Mono). Space Mono is the text face for everything small, not an extra label face.
- Changed: the piece used eight sizes (12, 16, 21, 28, 38, 51, 67, 90). Now five: label 12, body 16, title 28 (marquee, button), headline 51 (block titles, countdown), display 90 (newsletter headline; 67 on phones). The store handle dropped from 21 to 16 bold, the marquee from 38 to 28, the countdown from 67 to 51.
- Highlight: "BEFORE" in a black fill box, the rest plain. Kept.
- Color: acid lime, black and white, 13:1. No change.

## Process findings
1. No hard offset shadow style, and the stage file calls it dated (feedback: gap).
2. The contrast fix suggested for a pale brand action colour would lose the brand; a border is the real fix (feedback: idea).
- Helped: border-width tokens (1, 2, 4) were exactly what this style needs.
