# 03 Lullwort: organic wellness hero

## Direction
Lullwort is a fictional maker of loose-leaf sleep teas (chamomile, lemon balm, valerian). The audience is adults who want a wind-down ritual, not a supplement. The hero is a painted dusk: a clay sun, a sage meadow, a tin and a cup among chamomile and valerian, all in pen and watercolour on cream paper. A soft serif headline does the talking. Feel words: **calm, cozy, natural** ("natural" is not in the engine's list; it asked).

## References (Mobbin, structure only)
- Eat Hungry Tiger: https://mobbin.com/sites/sections/0a65ae4c-404c-4d2d-bc70-bef248345510 . Teaches the pill-shaped nav and small, quiet copy in the corners, so the hero image and headline own the frame.
- MANA Yerba Maté: https://mobbin.com/sites/sections/35a3baf2-74ae-4890-b2a1-7573e0585652 . Teaches the product as the subject, with small hand-drawn sparkles around it.
- Yellowbird: https://mobbin.com/sites/sections/52ad00dc-133b-4d95-8b9a-c3c7bde88887 . Teaches art as a horizon: the illustration sits on the bottom edge and the copy floats above.

## System (engine)
```
sketch --name "Lullwort" --brand "#B8643F" --audience regular --platforms web --feel calm,cozy,natural --surfaces persuade
   (run without --delegated to test the difference: the exact clay was kept and only the button got a darker shade)
set raw.displayFace "Fraunces"   set raw.textFace "Instrument Sans"   set raw.fontLicence {web, app, selfHost}
set raw.secondaryColors ["#7E9475"]   set raw.accentCount 2
set raw.neutralBase "#EADBC4"         (cream paper hue)
set type.headingWeight 400            (a soft serif reads hushed at regular weight)
set type.displayReach 7               (120 px display step)
paint.py brief --slot hero --message "Let the day steep out of you"   (offline: recommends watercolour, writes 8 palette families)
```
| Dial | Value | Why |
|---|---|---|
| roundness | 92 | blobs, pills, soft corners |
| warmth | 85 | cream and clay, never blue-grey |
| colorfulness | 42 | earthy and muted |
| depth | 15 | flat print feel, paper grain instead of shadows |
| energy | 15 | slow, hushed |
| expression | 70 | illustrated, characterful hero |
| density | 25 | lots of air |

Fonts: Fraunces (SIL OFL; SOFT 100, opsz 144, weight 300-340) and Instrument Sans (SIL OFL), Google Fonts link.

## Art
Painted in SVG by code, following the paint brief's style (watercolour) and its "brand-paper" family. Turbulence displacement gives wobbly wash edges, a second noise gives pigment granulation, an eroded copy gives the darker drying rim, and a pen layer adds the line work. The paint engine itself was not run: it needs npm and Chromium installs, which need the person's yes. Every colour is a token.

## Outside the tokens, on purpose
- **Ground** is `bg.neutral.subtle` (neutral step 3, #f1ebe1): the base surface is always near-white.
- **Sage** is mixed back toward the warm neutral (`color-mix`, 62%), because the engine raised the given sage #7E9475 to a bright #6c9c57.
- **Pigments stay fixed across themes** (`--art-paper` = neutral light 1, `--art-ink` = neutral light 12). Bound to UI roles, the first dark render turned the white chamomile petals black.
- **Headline** 120 px token with -0.03em tracking and line-height .95 (system: -0.02em). Checked at 200%.

## Checks
- `engine.py validate`: passes, 0 warnings.
- `engine.py review`: 2 hard-coded sizes, fixed; final "the code uses the tokens".
- `preflight.py html`: 2 errors, both M9 false positives (Fraunces and Instrument Sans load from Google Fonts). "font sizes in px: []" again: token sizes are rem and the script cannot see them.
- Contrast (computed): body #615544 on #f1ebe1 6.13:1; "steep" #262420 on its sage pill (#abb293, sampled) 7.0:1; button white on #b15f3b 4.6:1; bag count #874528 on #f4c9b7 4.77:1. Targets 40-48 px pills. Dark mode renders without broken art (checked), but its brown-black ground with terracotta breaks the owner's later colour rule, so only the light render is shown.

## Type scale (named roles, 5 sizes, two faces)
| Role | Size | Face, weight | Use |
|---|---|---|---|
| Display | 120 px (`--ds-font-size-120`) | Fraunces 340, SOFT 100 | headline |
| Title | 28 px (`--ds-font-size-28`) | Fraunces italic 400 | wordmark only |
| Body large | 21 px (`--ds-font-size-21`) | Instrument Sans 400 | lede |
| Body | 16 px (`--ds-font-size-16`) | Instrument Sans 400-500 | nav, kicker, buttons, facts |
| Label | 12 px (`--ds-font-size-12`) | Instrument Sans 600 | bag count, tin label lines |

## Changes for the owner's type and colour rules (mid-run)
- "steep" was an italic clay word: the banned one-italic-serif-word trick. It is now set like the rest of the line, on a sage pill (a fill box) in the same ink colour. The pill echoes the blob shapes of the painting and puts a small weight on the left to answer the large painting on the right.
- The tin label's small lines were 9.5 px, under the 11 px minimum; now 12 px, shortened to "chamomile, valerian".
- Colour in light mode: cream ground, near-black text 13:1, clay button 4.6:1. **Dark mode now breaks the new colour rule**: Warmth 85 plus a clay brand gives a brown-black ground (#171512) with terracotta. The showcase uses the light render only; see the finding below.

## Process findings (piece 03)
1. **Bug:** secondary colours are re-saturated to the brand's chroma and have no seed token.
2. **Gap:** no illustration palette; light accent steps drift pink; art bound to UI roles inverts in dark mode.
3. **Bug:** the paint brief ignores the recorded font licence.
4. **Gap:** the paint skill cannot paint without installs, so an unattended agent only gets the brief.
5. **Gap:** "natural" and "organic" are not feel words.
6. **Gap:** high Warmth plus a warm brand gives a muddy brown-black dark mode with no warning (recorded in 05's feedback).
7. **Helped:** without `--delegated`, sketch kept the exact clay and explained the darker button shade in one plain sentence. `neutralBase` and `type.headingWeight` were the right levers. The paint brief's palette families were a good art guide.
