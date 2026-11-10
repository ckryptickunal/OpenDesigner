# 08 Onething: notes

Render: `shot.png` (205 x 251 CSS px at 3x, clipped to the display shape by `../render.py`). Page: `index.html`.

## Direction
Onething is a single-task focus timer: one task, one countdown, one pink ring. Everything else is grey or white. Feel words: minimal, focused, understated.

## References (Mobbin, cited by link only; nothing saved)
- https://mobbin.com/screens/08366dca-8bef-401f-a5d2-2514448fdf7d: a thin progress ring around a single time.
- https://mobbin.com/screens/8f41e7c5-7817-4dcc-97a5-bc0d9d9922d7: minute ticks around the timer as the track.
- https://mobbin.com/screens/620e1c4b-46e7-4ba7-936d-a2bded2de22e: one ring on pure black and nothing else.

## Design system from the engine
Commands (full log with every output: `engine-log.txt`; decisions: `opendesigner/decisions.md`):

```
E=skills/opendesigner/scripts/engine.py; D=brand/showcase/watch/08-onething-focus/opendesigner
python3 $E --dir $D sketch --name "Onething" --brand "#FF4F9A" --audience large --platforms watch --feel minimal,focused,understated --delegated feel,audience,platforms
python3 $E --dir $D standard override STD-visual-details-24 --why "Brief: smartwatch app, black background edge-to-edge ..."
python3 $E --dir $D pick Q-theme-01 dark-only        # blocked until the standard is overridden
python3 $E --dir $D pick Q-color-21 black            # pure #000 page (OLED)
python3 $E --dir $D pick Q-plat-02 watch             # "recorded; the tokens already match this answer"
python3 $E --dir $D pick Q-plat-04 watch             # same: changes nothing
python3 $E --dir $D set raw.textFace '"Geist"'
python3 $E --dir $D set raw.monoFace '"Geist Mono"'
python3 $E --dir $D set raw.baseSize 17              # watchOS Body at xLarge (49 mm default), added after the owner's type rule
python3 $E --dir $D set dials.<id> <v> ...           # eight dials, values below
python3 $E --dir $D build
```

I kept the brand out of `--delegated`: with `--delegated all`, the first trial run of 01 swapped the hex I gave (#C8FF2E) for "#617f00, a readable shade".

Dial values and why:
- expression: 30, nothing extra
- brandPresence: 35, one accent ring
- density: 20, one task
- energy: 30, steady
- roundness: 60, round ring and buttons
- depth: 0, flat black
- colorfulness: 15, monochrome plus pink
- warmth: 40, neutral

## Fonts
Geist (SIL OFL, Google Fonts link), one family. Geist Mono is still set as the engine's mono face but is no longer loaded or used on the screen (owner rule: at most two fonts; one is enough).

## Type scale (watchOS text roles)
watchOS text styles at the xLarge size, the default for 44/45/49 mm (Apple HIG, Typography, watchOS Dynamic Type): Large Title 40, Title 1 38, Title 2 30, Title 3 20, Headline 17 semibold, Body 17, Caption 1 16, Caption 2 15, Footnote 1 14, Footnote 2 13; minimum 12.

Used here: Caption 2 15 (HIG; clock, 'of 25 min'), Body 17 (`--ds-font-size-17`, task), Large Title 40 (HIG; timer, set Light 300). Three sizes.

## Outside the tokens, on purpose
Caption 2 15 and Large Title 40 px. The minute-tick track and the ring glow (drop-shadow of `--ds-color-brand-seed` at 55%).
- Hardware: `--display-w/h/r` (205 x 251, 48 px corners) and the corner safe-area insets (22 to 28 px) are the device, not design tokens.

## Checks
validate: passes, 0 warnings. preflight: M9 false error, M5 tracking on the timer (intended). Buttons are 44 px (`--ds-size-target-touch`) with a focus outline.

## Changes for the owner's type and colour rules
Owner rule: removed Geist Mono from the page; timer 46 light to Large Title 40 light; clock 16 and label 13 to Caption 2 15; task 16 to Body 17. The first version had a solid grey track and read as a default template; the minute-tick track replaced it.

## Process findings (this piece)
- The only piece with zero validate warnings: its brand passes contrast in both modes, so the light-mode noise disappears.
- Cross-piece findings are in `../PROCESS.md`; engine feedback is in `opendesigner/feedback.md` where this piece recorded one.
