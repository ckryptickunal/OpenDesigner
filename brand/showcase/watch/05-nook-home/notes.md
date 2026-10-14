# 05 Nook: notes

Render: `shot.png` (205 x 251 CSS px at 3x, clipped to the display shape by `../render.py`). Page: `index.html`.

## Direction
Nook is a smart-home remote for the evening: scenes, not devices. One lit tile for the active scene, two quiet tiles for the others. Lamp-light amber, pillowy radii, rounded type. Feel words: warm, cozy, gentle.

## References (Mobbin, cited by link only; nothing saved)
- https://mobbin.com/screens/099d8bfc-4a2a-44e2-b1fa-a5f0266e2208: scene tiles: icon chip top-left, name bottom-left.
- https://mobbin.com/screens/810de075-3035-4f04-9118-505991f0ec3f: the active thing is a filled warm tile; off things stay neutral.
- https://mobbin.com/screens/a255c56f-2d49-4ce5-86d4-58e929052ab4: large-radius dark tiles on pure black.

## Design system from the engine
Commands (full log with every output: `engine-log.txt`; decisions: `opendesigner/decisions.md`):

```
E=skills/opendesigner/scripts/engine.py; D=brand/showcase/watch/05-nook-home/opendesigner
python3 $E --dir $D sketch --name "Nook" --brand "#FFB54A" --audience large --platforms watch --feel warm,cozy,gentle --delegated feel,audience,platforms
python3 $E --dir $D standard override STD-visual-details-24 --why "Brief: smartwatch app, black background edge-to-edge ..."
python3 $E --dir $D pick Q-theme-01 dark-only        # blocked until the standard is overridden
python3 $E --dir $D pick Q-color-21 black            # pure #000 page (OLED)
python3 $E --dir $D pick Q-plat-02 watch             # "recorded; the tokens already match this answer"
python3 $E --dir $D pick Q-plat-04 watch             # same: changes nothing
python3 $E --dir $D set raw.textFace '"Nunito"'
python3 $E --dir $D set raw.baseSize 17              # watchOS Body at xLarge (49 mm default), added after the owner's type rule
python3 $E --dir $D set dials.<id> <v> ...           # eight dials, values below
python3 $E --dir $D build
```

I kept the brand out of `--delegated`: with `--delegated all`, the first trial run of 01 swapped the hex I gave (#C8FF2E) for "#617f00, a readable shade".

Dial values and why:
- expression: 45, calm controls
- brandPresence: 55, amber is lamp light
- density: 20, three big tiles
- energy: 25, unhurried
- roundness: 95, pillowy tiles
- depth: 55, the lit tile lifts by colour
- colorfulness: 50, amber plus neutrals
- warmth: 50 (was 95; lowered for the owner rule: it turned the tiles brown-black #261f1c)

## Fonts
Nunito (SIL OFL, Google Fonts link), one family; 600 to 750.

## Type scale (watchOS text roles)
watchOS text styles at the xLarge size, the default for 44/45/49 mm (Apple HIG, Typography, watchOS Dynamic Type): Large Title 40, Title 1 38, Title 2 30, Title 3 20, Headline 17 semibold, Body 17, Caption 1 16, Caption 2 15, Footnote 1 14, Footnote 2 13; minimum 12.

Used here: Caption 2 15 (HIG; tile captions), Body/Headline 17 (`--ds-font-size-17`, room, clock, tile names, hero caption), Title 2 30 (HIG; 'Wind down'). Three sizes.

## Outside the tokens, on purpose
Title 2 30 and Caption 2 15 px. Hero tile gradient (two radial lights over `--ds-color-brand-seed`, using `--ds-color-accent-dark-12` and `--ds-color-warning-dark-9`). Tile radius uses `--ds-radius-28` directly, not the semantic `--ds-radius-container` (20), for a softer watch tile.
- Hardware: `--display-w/h/r` (205 x 251, 48 px corners) and the corner safe-area insets (22 to 28 px) are the device, not design tokens.

## Checks
validate: passes, 2 light-mode warnings. preflight: M9 false error only. Rendered sizes 15/17/30; dark text on amber, light text on #202020 tiles. Tiles are buttons, at least 44 px tall, with a visible focus outline.

## Changes for the owner's type and colour rules
Owner colour rule: Warmth 95 to 50 through the engine (tiles now neutral #202020, secondary text neutral #979797), removed the amber halo around the hero tile, icon chips from brown accent-dark-4 to neutral-dark-7 with an amber glyph, hero caption from brown mix to the on-brand black. Type: 16 to 17, 25 to Title 2 30 (weight 900 to 750), 13 and 16 captions to Caption 2 15.

## Process findings (this piece)
- This was the clearest case of the Warmth dial producing the muddy brown-black look; recorded as a gap.
- Cross-piece findings are in `../PROCESS.md`; engine feedback is in `opendesigner/feedback.md` where this piece recorded one.
