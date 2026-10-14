# 02 Thrum: notes

Render: `shot.png` (205 x 251 CSS px at 3x, clipped to the display shape by `../render.py`). Page: `index.html`.

## Direction
Thrum is a heart-rate trainer for interval sessions. The screen answers 'how hard am I working right now' with a huge BPM numeral and a five-step zone bar, warm reds from amber to crimson. Feel words: bold, warm, strong.

## References (Mobbin, cited by link only; nothing saved)
- https://mobbin.com/screens/eb5e7fd4-5d77-427f-9b49-99fa1b30b96c: a big BPM paired with a live trace; the trace explains the number.
- https://mobbin.com/screens/1881d8d9-7b6a-4b94-ace8-53ed3549453c: zones as a segmented track with a marker on the current segment.
- https://mobbin.com/screens/1a63990f-5793-4fb8-93e8-5827ed64982a: a five-step zone legend reads left to right, light to hot.

## Design system from the engine
Commands (full log with every output: `engine-log.txt`; decisions: `opendesigner/decisions.md`):

```
E=skills/opendesigner/scripts/engine.py; D=brand/showcase/watch/02-thrum-heart/opendesigner
python3 $E --dir $D sketch --name "Thrum" --brand "#FF5436" --audience large --platforms watch --feel bold,warm,strong --delegated feel,audience,platforms
python3 $E --dir $D standard override STD-visual-details-24 --why "Brief: smartwatch app, black background edge-to-edge ..."
python3 $E --dir $D pick Q-theme-01 dark-only        # blocked until the standard is overridden
python3 $E --dir $D pick Q-color-21 black            # pure #000 page (OLED)
python3 $E --dir $D pick Q-plat-02 watch             # "recorded; the tokens already match this answer"
python3 $E --dir $D pick Q-plat-04 watch             # same: changes nothing
python3 $E --dir $D set raw.textFace '"Bricolage Grotesque"'
python3 $E --dir $D set raw.baseSize 17              # watchOS Body at xLarge (49 mm default), added after the owner's type rule
python3 $E --dir $D set dials.<id> <v> ...           # eight dials, values below
python3 $E --dir $D build
```

I kept the brand out of `--delegated`: with `--delegated all`, the first trial run of 01 swapped the hex I gave (#C8FF2E) for "#617f00, a readable shade".

Dial values and why:
- expression: 70, big numerals are the show
- brandPresence: 70, warm red owns the status line
- density: 25, one number, one bar
- energy: 75, live data
- roundness: 55, soft but not bubbly
- depth: 20, flat
- colorfulness: 70, five zone colours
- warmth: 50 (was 90; lowered for the owner rule, because 90 tinted every grey brown)

## Fonts
Bricolage Grotesque (SIL OFL, Google Fonts link), one family; optical size 96 and width 78 for the numeral, optical size 13 to 30 for text.

## Type scale (watchOS text roles)
watchOS text styles at the xLarge size, the default for 44/45/49 mm (Apple HIG, Typography, watchOS Dynamic Type): Large Title 40, Title 1 38, Title 2 30, Title 3 20, Headline 17 semibold, Body 17, Caption 1 16, Caption 2 15, Footnote 1 14, Footnote 2 13; minimum 12.

Used here: Footnote 2 13 (zone numbers), Body/Headline 17 ('Threshold', clock, BPM, 'In zone'), Title 2 30 (12:40, Regular), Display 104 (BPM numeral, outside the HIG styles on purpose). Four sizes, all on engine tokens except the display size.

## Outside the tokens, on purpose
BPM numeral 104 px. The five zone colours are derived from `--ds-color-brand-seed` with relative oklch (`oklch(from var(--ds-color-brand-seed) L C calc(h + n))`): the generated dark ramps (accent2 #8c741b, accent3 #a45d9a, warning, danger) are too dusty for a luminous zone scale. The trace is SVG drawn in code.
- Hardware: `--display-w/h/r` (205 x 251, 48 px corners) and the corner safe-area insets (22 to 28 px) are the device, not design tokens.

## Checks
validate: passes, 2 warnings (the feel words 'warm' and 'strong' pull warmth and roundness in opposite directions). preflight: M9 false error (Google Fonts link), M5 tracking on the display numeral (intended). Rendered sizes 13/17/30/104; numeral is pure white on pure black.

## Changes for the owner's type and colour rules
Owner colour rule: removed the red radial glows (they made a brown-black haze around the number), removed the orange area fill under the trace, made inactive zone segments full colour but thin instead of 62% opacity (opacity over black made tan and brown), set the numeral to pure white, and lowered Warmth 90 to 50 through the engine. Type: 16 to Body 17, 12 to Footnote 2 13, 21 bold to Title 2 30 regular.

## Process findings (this piece)
- High Warmth makes brown neutrals with no warning; recorded.
- The dark ramps cannot give a vivid sequential data scale; recorded (with 07).
- Feel words 'strong' maps to authoritative, which fights 'warm'. The warning was clear.
- Cross-piece findings are in `../PROCESS.md`; engine feedback is in `opendesigner/feedback.md` where this piece recorded one.
