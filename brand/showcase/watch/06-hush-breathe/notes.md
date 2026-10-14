# 06 Hush: notes

Render: `shot.png` (205 x 251 CSS px at 3x, clipped to the display shape by `../render.py`). Page: `index.html`.

## Direction
Hush is a one-minute breathing break. The interface is a slow orb and one instruction; nothing to tap. Lavender light, film grain, a soft optical-size serif. Feel words: calm, gentle, elegant.

## References (Mobbin, cited by link only; nothing saved)
- https://mobbin.com/screens/a7726922-7009-4136-ad66-f22affa3077e: concentric rings read as breath ripples.
- https://mobbin.com/screens/35fce318-4db6-40d2-bdab-342d4ec900ca: one instruction line under one ring; hairline rings.
- https://mobbin.com/screens/a9c8abcf-2dfe-49e1-a5da-0cc11d636ab5: a serif instruction and a lot of black.

## Design system from the engine
Commands (full log with every output: `engine-log.txt`; decisions: `opendesigner/decisions.md`):

```
E=skills/opendesigner/scripts/engine.py; D=brand/showcase/watch/06-hush-breathe/opendesigner
python3 $E --dir $D sketch --name "Hush" --brand "#B9A6FF" --audience large --platforms watch --feel calm,gentle,elegant --delegated feel,audience,platforms
python3 $E --dir $D standard override STD-visual-details-24 --why "Brief: smartwatch app, black background edge-to-edge ..."
python3 $E --dir $D pick Q-theme-01 dark-only        # blocked until the standard is overridden
python3 $E --dir $D pick Q-color-21 black            # pure #000 page (OLED)
python3 $E --dir $D pick Q-plat-02 watch             # "recorded; the tokens already match this answer"
python3 $E --dir $D pick Q-plat-04 watch             # same: changes nothing
python3 $E --dir $D set raw.textFace '"Fraunces"'
python3 $E --dir $D set raw.baseSize 17              # watchOS Body at xLarge (49 mm default), added after the owner's type rule
python3 $E --dir $D set dials.<id> <v> ...           # eight dials, values below
python3 $E --dir $D build
```

I kept the brand out of `--delegated`: with `--delegated all`, the first trial run of 01 swapped the hex I gave (#C8FF2E) for "#617f00, a readable shade".

Dial values and why:
- expression: 65, the orb is the interface
- brandPresence: 40, quiet presence
- density: 10, one word on screen
- energy: 10, slow breath
- roundness: 100, everything is a circle
- depth: 30, glow, not shadow
- colorfulness: 35, lavender only
- warmth: 55, soft dusk

## Fonts
Fraunces (SIL OFL, Google Fonts link), one family, upright only; optical size 14 to 72 and the SOFT axis at 100.

## Type scale (watchOS text roles)
watchOS text styles at the xLarge size, the default for 44/45/49 mm (Apple HIG, Typography, watchOS Dynamic Type): Large Title 40, Title 1 38, Title 2 30, Title 3 20, Headline 17 semibold, Body 17, Caption 1 16, Caption 2 15, Footnote 1 14, Footnote 2 13; minimum 12.

Used here: Caption 2 15 (HIG; clock, '4 of 7'), Headline 17 (`--ds-font-size-17`, 'Hush'), Title 2 30 (HIG; 'Breathe in', weight 300). Three sizes.

## Outside the tokens, on purpose
Title 2 30 and Caption 2 15 px. The orb (feathered radial light, inner bloom, grain, ripples, phase arc) is canvas 2D coloured from `--ds-color-brand-seed` and `--ds-color-accent-dark-7/12`.
- Hardware: `--display-w/h/r` (205 x 251, 48 px corners) and the corner safe-area insets (22 to 28 px) are the device, not design tokens.

## Checks
validate: passes, 2 light-mode warnings. preflight: M9 false error only. Rendered sizes 15/17/30.

## Changes for the owner's type and colour rules
Owner rule: the cue and the app name were italic Fraunces; both are now upright (the cue at weight 300, white), the italic axis was removed from the font link. Clock and count 15, app name 17, cue 30 (was 30 italic). The first orb looked like a glossy ball; it is now a feathered, diffuse light.

## Process findings (this piece)
- The engine has no motion guidance for a 4 s in / 6 s out breathing rhythm; the motion tokens are UI durations (100 to 660 ms). Not recorded as a gap: out of scope for a still.
- Cross-piece findings are in `../PROCESS.md`; engine feedback is in `opendesigner/feedback.md` where this piece recorded one.
