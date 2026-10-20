# 04 Headway: notes

Render: `shot.png` (205 x 251 CSS px at 3x, clipped to the display shape by `../render.py`). Page: `index.html`.

## Direction
Headway is a transit countdown for commuters on a city tram and train network. Lifted from station signage: yellow on black, condensed caps, square line badges, hard rules, one huge countdown. Feel words: bold, practical, authoritative.

## References (Mobbin, cited by link only; nothing saved)
- https://mobbin.com/screens/817f224d-319c-4a04-9302-d4e82611dc0b: row rhythm: line badge, destination, minutes right-aligned.
- https://mobbin.com/screens/6019ffc7-071d-4e27-b0cc-c9ceaeea8c45: a stop line with a you-are-here dot explains 'how far away' without words.

## Design system from the engine
Commands (full log with every output: `engine-log.txt`; decisions: `opendesigner/decisions.md`):

```
E=skills/opendesigner/scripts/engine.py; D=brand/showcase/watch/04-headway-transit/opendesigner
python3 $E --dir $D sketch --name "Headway" --brand "#FFCC1A" --audience large --platforms watch --feel bold,practical,authoritative --delegated feel,audience,platforms
python3 $E --dir $D standard override STD-visual-details-24 --why "Brief: smartwatch app, black background edge-to-edge ..."
python3 $E --dir $D pick Q-theme-01 dark-only        # blocked until the standard is overridden
python3 $E --dir $D pick Q-color-21 black            # pure #000 page (OLED)
python3 $E --dir $D pick Q-plat-02 watch             # "recorded; the tokens already match this answer"
python3 $E --dir $D pick Q-plat-04 watch             # same: changes nothing
python3 $E --dir $D set raw.textFace '"Big Shoulders Display"'
python3 $E --dir $D set raw.baseSize 17              # watchOS Body at xLarge (49 mm default), added after the owner's type rule
python3 $E --dir $D set dials.<id> <v> ...           # eight dials, values below
python3 $E --dir $D build
```

I kept the brand out of `--delegated`: with `--delegated all`, the first trial run of 01 swapped the hex I gave (#C8FF2E) for "#617f00, a readable shade".

Dial values and why:
- expression: 55, signage, not decoration
- brandPresence: 75, yellow is wayfinding
- density: 50, a departure board needs rows
- energy: 50, urgency without panic
- roundness: 0, hard signage edges
- depth: 0, flat enamel
- colorfulness: 30, yellow, white, one alert
- warmth: 55, sodium-lamp yellow

## Fonts
Big Shoulders Display (SIL OFL, Google Fonts link), one family; 500 to 900.

## Type scale (watchOS text roles)
watchOS text styles at the xLarge size, the default for 44/45/49 mm (Apple HIG, Typography, watchOS Dynamic Type): Large Title 40, Title 1 38, Title 2 30, Title 3 20, Headline 17 semibold, Body 17, Caption 1 16, Caption 2 15, Footnote 1 14, Footnote 2 13; minimum 12.

Used here: Footnote 1 14 (`--ds-font-size-14`, MIN units), Body/Headline 17 (`--ds-font-size-17`, station, clock, '2 stops out'), Title 3 20 (HIG; destinations, badges, vertical MIN), Title 2 30 (HIG; list minutes), Display 114 (the countdown). Five sizes.

## Outside the tokens, on purpose
Countdown 114 px; Title 3 20 and Title 2 30 px (the engine steps 17, 21, 27, 33). The vertical MIN is a signage move, set in the same family.
- Hardware: `--display-w/h/r` (205 x 251, 48 px corners) and the corner safe-area insets (22 to 28 px) are the device, not design tokens.

## Checks
validate: passes, 2 light-mode warnings. preflight: M9 false error only. Rendered sizes 14/17/20/30/114. Rows are 42 px tall: tappable rows would need 44, so they are read-only here, a known compromise.

## Changes for the owner's type and colour rules
Owner rule: station and clock 18 to Body 17, destinations 22 to Title 3 20 (weight 700 to 600 in the list), list minutes 27 to Title 2 30.

## Process findings (this piece)
- The first two layouts collided (numeral over badge, MIN over the stop line); the engine has no layout help for a 205 x 251 canvas, as expected.
- Mobbin has no watch platform; recorded as an idea for the skill.
- Cross-piece findings are in `../PROCESS.md`; engine feedback is in `opendesigner/feedback.md` where this piece recorded one.

## Round 4 (owner review, 2026-10-18)
The owner called the showcase "very very very cluttered and very unprofessional". The round-4 audit (`../../AUDIT-ROUND4.md`) and `../../PRESENTATION.md` set the watch rules: one glanceable thing, the time top right, colour only when it carries information.

**One idea:** The next tram to Saltgrove leaves Wharf Rd in 2 minutes.

**Changed:**
- Face changed through the engine from Big Shoulders Display to Overpass (an open highway-sign face)
- Yellow route squares, stop line, rule, rotated 'MIN' and the departure rows removed: one countdown, one route line, one 'Then 9 and 14 min' line
- Yellow only on the countdown; the stop name in grey
- Destination Northgate renamed Saltgrove (check_names.py: two letters from Northcote and Northvale); 'Harbour', shared with components/07, no longer shown

Common to all seven: black ground, the title and clock in Inter (SIL OFL) as the stand-in for San Francisco, which watchOS draws itself; the app's own face for everything else (two typefaces); sizes from the watchOS roles (Caption 2 15, Headline 17) plus one data numeral. Rendered with `../render.py` at the existing size, 205 x 251 pt at 3x (615 x 753), clipped to the display; the gallery copy (192 px) was checked first.

**Blind pairwise (18 Oct, fresh judge, no labels, random sides; tested the first round-4 render, before the audit fixes):** lost 2 vs Transit (nearby list), won 4 vs Citymapper, won 2 vs Transit (route). References were App Store Apple Watch screenshots, kept in scratch and deleted.

**Fresh-eyes audit:** 4 (18 Oct), 4 (20 Oct). Final: 4 of 5.

**Checks:** `check_dates.py --year 2026` passes; `check_names.py` 0 errors; `preflight.py html` only warns about the HIG sizes and the display numeral outside the token scale (both on purpose, commented in the page).
