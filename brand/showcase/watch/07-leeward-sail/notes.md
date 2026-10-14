# 07 Leeward: notes

Render: `shot.png` (205 x 251 CSS px at 3x, clipped to the display shape by `../render.py`). Page: `index.html`.

## Direction
Leeward is a sailing instrument for small keelboats: heading, apparent wind and speed at a glance from the helm. A compass card that runs off the display, bone linework on black, port red and starboard green as the only colour. Feel words: technical, classic, sober.

## References (Mobbin, cited by link only; nothing saved)
- https://mobbin.com/screens/792ecf30-b4d5-41fd-80f7-ddd7154392fd: degree plus cardinal readout under a dial.
- https://mobbin.com/screens/76bd3242-e04d-4bc0-b20a-305870075019: compass ticks with cardinal letters around a reading.
- https://mobbin.com/screens/0e7defa2-3205-4d83-a97c-7c118e60da43: tabular label and value rows in mono caps.

## Design system from the engine
Commands (full log with every output: `engine-log.txt`; decisions: `opendesigner/decisions.md`):

```
E=skills/opendesigner/scripts/engine.py; D=brand/showcase/watch/07-leeward-sail/opendesigner
python3 $E --dir $D sketch --name "Leeward" --brand "#EDE4CC" --audience large --platforms watch --feel technical,classic,sober --delegated feel,audience,platforms
python3 $E --dir $D standard override STD-visual-details-24 --why "Brief: smartwatch app, black background edge-to-edge ..."
python3 $E --dir $D pick Q-theme-01 dark-only        # blocked until the standard is overridden
python3 $E --dir $D pick Q-color-21 black            # pure #000 page (OLED)
python3 $E --dir $D pick Q-plat-02 watch             # "recorded; the tokens already match this answer"
python3 $E --dir $D pick Q-plat-04 watch             # same: changes nothing
python3 $E --dir $D set raw.textFace '"IBM Plex Mono"'
python3 $E --dir $D set raw.monoFace '"IBM Plex Mono"'
python3 $E --dir $D set raw.baseSize 17              # watchOS Body at xLarge (49 mm default), added after the owner's type rule
python3 $E --dir $D set dials.<id> <v> ...           # eight dials, values below
python3 $E --dir $D build
```

I kept the brand out of `--delegated`: with `--delegated all`, the first trial run of 01 swapped the hex I gave (#C8FF2E) for "#617f00, a readable shade".

Dial values and why:
- expression: 35, an instrument, not a poster
- brandPresence: 30, bone linework, no fills
- density: 60, several readings
- energy: 20, steady helm
- roundness: 30, hairlines and ticks
- depth: 0, flat chart
- colorfulness: 15 (tried 45: the status colours did not change, so it went back to 15)
- warmth: 45, chart paper

## Fonts
IBM Plex Mono (SIL OFL, Google Fonts link), one family for HTML and SVG text; set as both text and mono face in the engine.

## Type scale (watchOS text roles)
watchOS text styles at the xLarge size, the default for 44/45/49 mm (Apple HIG, Typography, watchOS Dynamic Type): Large Title 40, Title 1 38, Title 2 30, Title 3 20, Headline 17 semibold, Body 17, Caption 1 16, Caption 2 15, Footnote 1 14, Footnote 2 13; minimum 12.

Used here: Footnote 1 14 (`--ds-font-size-14`, labels, clock, card numerals), Body/Headline 17 (`--ds-font-size-17`, tack line, cardinal letters), Title 2 30 (HIG; AWS and SOG), Large Title 40 (HIG; heading, Regular). Four sizes.

## Outside the tokens, on purpose
Title 2 30 and Large Title 40 px. Port and starboard colours: the status tokens' hues pushed to signal chroma with relative oklch, because `--ds-color-danger-dark-11` #d78a81 and `--ds-color-success-dark-11` #6faa7b are too muted for side lights. Compass card is SVG drawn in code.
- Hardware: `--display-w/h/r` (205 x 251, 48 px corners) and the corner safe-area insets (22 to 28 px) are the device, not design tokens.

## Checks
validate: passes, 2 light-mode warnings. preflight: M9 false error, M5 tracking -0.04em on the heading (intended). Rendered sizes 14/17/30/40.

## Changes for the owner's type and colour rules
Owner rule: the degree sign was a superscript at another size; it is now inline at the heading size in secondary grey. Heading 46 medium to Large Title 40 regular; values 27 to Title 2 30 regular; labels 11 to Footnote 1 14 (shortened to 'AWS KN'); tack 18 to 17; port and starboard made vivid.

## Process findings (this piece)
- The Colorfulness dial does not reach the status colours on a near-neutral brand; recorded.
- The tick labels 210/240 run off the display edge on purpose: a card bigger than the screen.
- Cross-piece findings are in `../PROCESS.md`; engine feedback is in `opendesigner/feedback.md` where this piece recorded one.
