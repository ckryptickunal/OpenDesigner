# 03 Tidemark: notes

Render: `shot.png` (205 x 251 CSS px at 3x, clipped to the display shape by `../render.py`). Page: `index.html`.

## Direction
Tidemark is a watch face for sea swimmers and kayakers on a cold coast. At dawn it shows the time, the weather and where the tide is in its cycle, over a sky generated in code. Cool blues, light geometric numerals, round complication shapes. Feel words: calm, fresh, sleek.

## References (Mobbin, cited by link only; nothing saved)
- https://mobbin.com/screens/689e95c1-61af-4914-9821-860cade5109f: the tide as one sine curve with a 'now' dot and labels sitting on the curve.
- https://mobbin.com/screens/a9580790-ccec-4905-8b5a-3e1580c4a7d4: the smallest widget is the nearest thing to a complication: what survives at tiny size.
- https://mobbin.com/screens/6c285ffd-a76e-4528-a227-7ca21df20cd8: sky and light as data on a dark navy ground.

## Design system from the engine
Commands (full log with every output: `engine-log.txt`; decisions: `opendesigner/decisions.md`):

```
E=skills/opendesigner/scripts/engine.py; D=brand/showcase/watch/03-tidemark-face/opendesigner
python3 $E --dir $D sketch --name "Tidemark" --brand "#5CC8FF" --audience large --platforms watch --feel calm,fresh,sleek --delegated feel,audience,platforms
python3 $E --dir $D standard override STD-visual-details-24 --why "Brief: smartwatch app, black background edge-to-edge ..."
python3 $E --dir $D pick Q-theme-01 dark-only        # blocked until the standard is overridden
python3 $E --dir $D pick Q-color-21 black            # pure #000 page (OLED)
python3 $E --dir $D pick Q-plat-02 watch             # "recorded; the tokens already match this answer"
python3 $E --dir $D pick Q-plat-04 watch             # same: changes nothing
python3 $E --dir $D set raw.textFace '"Sora"'
python3 $E --dir $D set raw.baseSize 17              # watchOS Body at xLarge (49 mm default), added after the owner's type rule
python3 $E --dir $D set dials.<id> <v> ...           # eight dials, values below
python3 $E --dir $D build
```

I kept the brand out of `--delegated`: with `--delegated all`, the first trial run of 01 swapped the hex I gave (#C8FF2E) for "#617f00, a readable shade".

Dial values and why:
- expression: 60, the sky is the art
- brandPresence: 50, blue in the sky, not the chrome
- density: 45, a face carries several complications
- energy: 30, slow tides
- roundness: 70, round complications
- depth: 35, layered sky
- colorfulness: 55, a cool family of blues
- warmth: 15, cold sea air

## Fonts
Sora (SIL OFL, Google Fonts link), one family; weight 200 for the time, 500 to 600 for complications.

## Type scale (watchOS text roles)
watchOS text styles at the xLarge size, the default for 44/45/49 mm (Apple HIG, Typography, watchOS Dynamic Type): Large Title 40, Title 1 38, Title 2 30, Title 3 20, Headline 17 semibold, Body 17, Caption 1 16, Caption 2 15, Footnote 1 14, Footnote 2 13; minimum 12.

Used here: Footnote 1 14 (`--ds-font-size-14`, HIGH), Body 17 (`--ds-font-size-17`, date, temperature, 'rising', 9:42), Title 3 20 (HIG value; the engine steps 17 to 21), Display 72 (the face's time). Four sizes.

## Outside the tokens, on purpose
Time 72 px. Title 3 20 px. The sky (gradient, horizon glow, 120 seeded stars, crescent, cloud strata, glints) and tide curve are canvas 2D, coloured from `--ds-color-accent-dark-5/7/11` and `--ds-color-brand-seed` plus light blue rgba tints for glow.
- Hardware: `--display-w/h/r` (205 x 251, 48 px corners) and the corner safe-area insets (22 to 28 px) are the device, not design tokens.

## Checks
validate: passes, 2 light-mode warnings (never shown). preflight: M9 false error, M5 tracking on the 72 px time. Rendered sizes 14/17/20/72, text 7:1 or more.

## Changes for the owner's type and colour rules
Owner rule: complications and labels from 18 to Body 17, '2.1 m' from 22 to Title 3 20, HIGH from 11 to Footnote 1 14, the time to pure white. Before `raw.baseSize 17`, this system's scale was 11/14/18/22/27/34 (density 45 pushed the body to 14 px).

## Process findings (this piece)
- Before the base size was set, the density dial lowered the type below the watch floor even with `--audience large`; recorded with the missing watchOS roles.
- Q-color-21 'black' exists and works, but the stage file warns against bright objects on pure black, which is exactly the watch convention.
- Cross-piece findings are in `../PROCESS.md`; engine feedback is in `opendesigner/feedback.md` where this piece recorded one.
