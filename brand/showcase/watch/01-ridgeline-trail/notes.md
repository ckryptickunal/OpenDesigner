# 01 Fellrise: notes

Render: `shot.png` (205 x 251 CSS px at 3x, clipped to the display shape by `../render.py`). Page: `index.html`.

## Direction
Fellrise (called Ridgeline before round 3) is a trail-running app for people who race in the mountains. Mid-stride, with a heart rate of 170, the runner needs one number (pace) and one picture (where the climb is). Acid green on pure black, heavy italic numerals, cut corners like rock strata. Feel words: energetic, bold, futuristic.

## References (Mobbin, cited by link only; nothing saved)
- https://mobbin.com/screens/c9eb6b69-dd81-4527-97a5-84df9ab113c5: one gigantic slanted metric can own a running screen; everything else is small and grey.
- https://mobbin.com/screens/fba6c552-28f7-4783-89c2-d296f9a4ea2f: elevation reads instantly as a filled area with no axis; the fill does the work.
- https://mobbin.com/screens/943701a9-5313-45c4-8385-bf5f54734694: label-above-value rhythm with lots of air between metrics.

## Design system from the engine
Commands (full log with every output: `engine-log.txt`; decisions: `opendesigner/decisions.md`):

```
E=skills/opendesigner/scripts/engine.py; D=brand/showcase/watch/01-ridgeline-trail/opendesigner
python3 $E --dir $D sketch --name "Ridgeline" --brand "#C8FF2E" --audience large --platforms watch --feel energetic,bold,futuristic --delegated feel,audience,platforms
python3 $E --dir $D standard override STD-visual-details-24 --why "Brief: smartwatch app, black background edge-to-edge ..."
python3 $E --dir $D pick Q-theme-01 dark-only        # blocked until the standard is overridden
python3 $E --dir $D pick Q-color-21 black            # pure #000 page (OLED)
python3 $E --dir $D pick Q-plat-02 watch             # "recorded; the tokens already match this answer"
python3 $E --dir $D pick Q-plat-04 watch             # same: changes nothing
python3 $E --dir $D set raw.textFace '"Archivo"'
python3 $E --dir $D set raw.baseSize 17              # watchOS Body at xLarge (49 mm default), added after the owner's type rule
python3 $E --dir $D set dials.<id> <v> ...           # eight dials, values below
python3 $E --dir $D build
```

I kept the brand out of `--delegated`: with `--delegated all`, the first trial run of 01 swapped the hex I gave (#C8FF2E) for "#617f00, a readable shade".

Dial values and why:
- expression: 80, bold mid-run energy
- brandPresence: 85, the acid green is the identity
- density: 25, glanceable, few items
- energy: 90, race-day urgency
- roundness: 15, angular, cut corners
- depth: 10, flat OLED, no shadows on black
- colorfulness: 60, one loud accent plus status
- warmth: 35, cool neutrals so the green burns

## Fonts
Archivo (SIL OFL, Google Fonts link), one family. Width axis 62 to 125 and italic used for the pace numeral; the ticks of 4'52" are set at width 62 so the numeral fits.

## Type scale (watchOS text roles)
watchOS text styles at the xLarge size, the default for 44/45/49 mm (Apple HIG, Typography, watchOS Dynamic Type): Large Title 40, Title 1 38, Title 2 30, Title 3 20, Headline 17 semibold, Body 17, Caption 1 16, Caption 2 15, Footnote 1 14, Footnote 2 13; minimum 12.

Used here: Footnote 2 13 (`--ds-font-size-13`, caps labels), Body 17 (`--ds-font-size-17`, tag, clock, delta), Title 2 30 (`--ds-font-size-30`, +312 m), Display 68 (pace; outside the HIG styles on purpose: the one number read mid-stride). Four sizes. The summit value is Title 2 set Regular, not bold; only the pace numeral is heavy.

## Outside the tokens, on purpose
Pace numeral 68 px (data display). The terrain is SVG drawn in code: hatching, contour echoes and the runner marker are built from `--ds-color-brand-seed` and neutral tokens. Highlight by fill box (the KM 14.2 tag). The brand colour comes from `--ds-color-brand-seed` because the dark accent ramp has a dusty #b0d468 in place of the brand.
- Hardware: `--display-w/h/r` (205 x 251, 48 px corners) and the corner safe-area insets (22 to 28 px) are the device, not design tokens.

## Checks
validate: passes, 2 warnings, both about light mode, which a dark-only system never shows. preflight: ERROR M9 (false: the font comes from a Google Fonts link), WARN M5 tracking -0.045em on the 68 px numeral (intended display tracking). Font loaded, rendered sizes 13/17/30/68, all text 7:1 or more on black.

## Changes for the owner's type and colour rules
Owner type and colour rule: moved the tag, clock and delta from 16 to Body 17, the labels from 12 to Footnote 2 13, and the summit value from 21 bold to Title 2 30 regular. The 01 tokens changed from 12/16/21/28/38 to 13/17/23/30/40 after `raw.baseSize 17`.

## Process findings (this piece)
- `--delegated all` silently swapped the supplied brand hex for an olive (#617f00); recorded as a bug.
- Dark-only shows the brand only through `--ds-color-brand-seed`; every semantic accent role points at a desaturated step (#b0d468). Recorded.
- Watch answers change no tokens; recorded as a gap.
- Cross-piece findings are in `../PROCESS.md`; engine feedback is in `opendesigner/feedback.md` where this piece recorded one.

## Round 3 (2026-10-15): Fellrise, not Ridgeline
"Ridgeline" is a real product name (Honda sells the Ridgeline truck), and `NAMES.md` had marked it "may be real", so the app is now **Fellrise** (a web search found no app or product of that name; the nearest are the Lake District walking apps Fellbase and Fells). Changed: the page title and aria-label, this file's title, the engine system (`engine.py set name "Fellrise" --set-by delegated`, then `build`, which regenerated DESIGN.md, PRODUCT.md and the exports; logged in `engine-log.txt`), `../PROCESS.md`, `../sheet.html` (and `sheet.png`, re-rendered), the audit file's title, and the mockups that show it (`mockups/03-watch-trio`, `mockups/08-made-with-opendesigner`). The face shows no brand name, so `shot.png` is unchanged in pixels (re-rendered with `../render.py 01-ridgeline-trail`). The folder keeps its name so links do not break.
