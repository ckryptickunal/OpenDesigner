# 06 Plumpot: playful fintech hero

**Direction.** Plumpot is a fictional money app for 13 to 17 year olds: pocket money, chore payments, savings jars that round up, a prepaid card, and a parent view that sees totals, not every purchase. The audience is teens first and their parents second. Mood: a sticker sheet that someone tidied. Feel words: **playful, cute, tidy**.

Render: 1440 x 900 at scale 2 (`shot.png`).

## References (Mobbin, cited by URL only)
| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/481d7e3c-d983-486f-a906-e8f003e52831 | Coins read as 3D from three things only: an elliptical face, a darker edge band with knurling, and a highlight. Drawn the coins in SVG on that recipe. |
| https://mobbin.com/sites/sections/55f5773f-00e6-4a59-b2fe-dec6be97b22b | Floating objects at different sizes and rotations create depth around a headline; keep each object simple. |
| https://mobbin.com/sites/sections/3a22f194-ecf5-49cd-8c51-5e0351313723 | Left-aligned oversized display type with rotated sticker badges overlapping the art. Took the sticker technique (white keyline, rotation), not the layout. |
| https://mobbin.com/sites/sections/38f98d17-c8cf-41d7-8da7-737c54b4217d | Scale contrast: a very large headline makes small UI fragments feel like toys. |

## System (engine)
```
init; standard override STD-visual-details-24 (light-only, single marketing page)
sketch --name Plumpot --brand #7B3FE4 --audience regular --platforms web --feel playful,cute,tidy --theme light-only --surfaces "landing page:persuade" --delegated all
```
| Dial | Value | Why |
|---|---|---|
| expression | 85 | Loud, toy-like, sticker energy |
| brandPresence | 80 | The purple should own the page |
| colorfulness | 85 | Several candy hues |
| roundness | 100 | Pills and inflated shapes everywhere |
| depth | 70 | Floating cards and coins need lift |
| energy | 75 | Heavy headings, springy entrance |
| density | 35 | A hero is airy |
| warmth | (default) | Cream page came from the warm neutral |

Other answers: Q-dir-01 `tonal`, Q-dir-02 `spacious`, `macros` = playful, friendly (dropped "minimal" that "tidy" mapped to), `raw.secondaryColors` = #FF6FB0 (candy pink) and #FFC83D (butter), `raw.fontLicence` all true (OFL).

**Fonts.** Display: Fredoka (SIL OFL, Google Fonts) at weight 700 and width 105-118 via `font-variation-settings`. Text: Figtree (SIL OFL). Both set through `raw.displayFace` / `raw.textFace`.

## Outside the tokens, on purpose
- Headline at 124px: the scale stops at 90px (display-sm).
- Plum-tinted soft shadows on the floating objects (`--shadow-plum`): the elevation tokens only carry a neutral shadow color.
- Butter yellow uses `accent3-light-9` (#fbc951) because the yellow tint steps are tan.
- The coin highlight #fff6d6 (marked `od-ignore`) and coin/blob geometry are art, not UI.
- Everything else (colors, radii, control heights, spacing, motion durations and the spring easing) uses `--ds-*` variables.

## Checks
- `engine.py validate`: no errors, 0 warnings, 3 notes.
- `preflight.py html`: 2 errors, both false (M9: Figtree and Fredoka "have no @font-face"; they load from a Google Fonts `<link>`). Fixed the real ones: an 11px label went to 12px, tracking went from -0.035em to -0.03em.
- `engine.py review`: it found 4 broken standards, all fixed. `100vh` became `100svh`. The infinite 5-7 s bob loops and the spinning badge became one staggered spring entrance. 32 raw values remain, most of them coin, blob and shadow art.
- Contrast: lede 6.5:1, "big plans." in plum ink on the pink fill box 8.2:1, primary button 5.7:1, badge text 8.1:1. The ghost button outline went from 1.5:1 to 3.6:1 (accent-light-8). White text on the card's lightest corner is 3.6:1; it is large and decorative (`aria-hidden`).
- Targets: nav links 40px, buttons 48-56px; focus ring from tokens.

## Process findings
1. **Light-only is blocked, and the fix is out of order.** `sketch --theme light-only` refuses (STD-visual-details-24). The suggested `standard override` fails until `init` has run. (feedback: bug)
2. **Typefaces can't be found from the CLI.** `set textFace` fails. `set raw.textFace '"Figtree"'` works, but only reading engine.py tells you that. (gap)
3. **"tidy" turns into minimal and conflicts with playful.** `set raw.feel` silently does nothing; `set macros` is the fix. (confusing)
4. **Fredoka (OFL) is shown as a "Licence risk"** because the open-font allowlist is short. (gap)
5. **The display weight token is 850, but Fredoka maxes at 700.** (bug)
6. **No display step above 90px for a persuade surface.** (gap)
7. **Yellow tint steps are tan.** Candy pastels needed `secondaryColors`, and even then the butter came from step 9. Pink worked well once seeded. (gap)
8. **`review` suggests tokens by numeric coincidence:** a 40px height maps to space-40, an inset border to an elevation. (bug) Still, it was the most useful check: it caught the vh unit and the ambient loops.
9. **Shadows are always neutral.** Playful systems want a tinted option. (idea)
10. **preflight M9 false error** for Google Fonts links. (bug)

What helped: the ramps for purple and pink were good straight away, the plum ink step 12 makes a lovely text color, and the radius roles (control = full, container = 28) were right for the brief on the first build.

## Owner type and color rules (applied after the first render)
- **Fonts:** two only. Fredoka is the display, Figtree the text. The coin "p" glyphs and the badge ring text are Fredoka inside the art.
- **Highlight:** the color-only "big" (purple) and the swoosh underline under "plans." were removed. "big plans." now sits in a candy-pink fill box with a white keyline, tilted -2°, like a sticker. Visual weight: the headline is the heaviest thing on the left, and the box ties it to the pink in the art on the right.
- **Weight:** chunky 700 display is kept on purpose; the direction is "chunky rounded".
- **Type scale (6 sizes, each at least 10% from the next):**

  | Role | Size | Use |
  |---|---|---|
  | Display | 124 | Headline |
  | Headline | 38 | Jar amount |
  | Title | 28 | Logo, card brand |
  | Body large | 21 | Lede, toast amount, sticker |
  | Body / label | 16 | Nav, buttons, badge ring |
  | Caption | 12 | Small card text, ring % |

  The minimum, 12, is above the 11pt/sp floors.
- **Color:** a light cream ground with plum ink at 11.4:1. No muddy mid-tones.

Replaced on 2026-10-14 by heroes/11-spend-platform after the Mobbin audit (score 2).
