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

## Round 3 (owner review, 2026-10-15)

**What he said.** "Okay." It had to become clearly better, at the level of the B2B product screens and the Orbika hero. The audit also flagged the palette as the brown + orange + cream combination he bans, plus a sage pill behind "steep", two buttons and a three-item reassurance row, an illustration assembled from a sun disc, moon, sparkles, flowers, tin, cup and hill, and the stock DTC layout.

**Palette, re-cut through the engine.**
```
set raw.brandColor "#3D5A47" --set-by chosen      (was clay #B8643F)
set raw.neutralBase "#E8ECE4" --set-by chosen     (was cream #EADBC4)
set raw.secondaryColors ["#E2B23A"] --set-by chosen   (chamomile yellow, flower hearts only; was sage)
set dials.warmth 30                                (was 85, which made the neutrals brown)
build
```
Result: cool green-grey paper (#eaece9), green-black ink (#232521, about 14:1), one deep sage green (#3d5a47) for the tin, the button and the blend's percentages, and yellow only inside the chamomile flowers. No brown, no orange, no cream. The engine kept the brand and the yellow exactly as typed.

**What changed.**
- **Layout: the plate is a horizon, the copy sits above it.** The headline runs as one line across the page; under it the lede and the one button on the left, and the spec as a small 2 x 2 strip on the right (steep 5 minutes at 95 °C, 2 g per cup, a 40 g tin makes about 20 cups, no caffeine). The left-text, right-picture DTC split is gone.
- **One object: the blend as a botanical plate.** A tea caddy stands on a shelf line that runs the width of the grid, in front of the three plants it is made of, each labelled with its share, its Latin name and the part that goes in the tea: chamomile 50% (*Matricaria chamomilla*, the flowers), lemon balm 30% (*Melissa officinalis*, the leaves), valerian 20% (*Valeriana officinalis*, the root, in a dish on the shelf). The tin's label prints the same 50 / 30 / 20 as one bar in three inks. The sun disc, moon, sparkles, cup and hill are gone.
- **The tin, drawn with care.** An opaque slip lid in the body green, one light from the left across the cylinder, a contact shadow and a cast shadow on the shelf. Chamomile heads have domed, shaded centres; two are seen from the side with their rays hanging all round the cone. Valerian flowers are a branching cluster of florets; its root is shown as cut, dried pieces with ringed faces in a small dish. Lemon balm leaves have rounded teeth and veins, each leaf drawn in its own layer. No blurred shadow discs.
- **Copy and type.** No pill behind "steep". Percentages are ink; green is the tin and the button.
- **One action.** "Add to bag · £14". The quiz button, the "Find your blend" pill and the pill-shaped nav are gone; the bag is a text link.

**Type scale (round 3).** Display 90 px (`--ds-font-size-90`, Fraunces 340, one line) · Title 28 px (wordmark, Fraunces italic) · Body large 21 px (lede) · Body 16 px (nav, spec, button, plant names) · Label 12 px (Latin names, the plate caption, the tin's small lines). Two faces: Fraunces and Instrument Sans. The plate is drawn at 1 : 1.2 scale onto the page's shelf.

**Checks.** `engine.py build`: passes, 0 warnings. `engine.py review`: the code uses the tokens. `preflight.py html`: no errors or warnings. `check_dates.py`: passes. The plate is drawn at 1 : 1.2, so its type is set at 10 in the source to render at 12 px.

**Fresh-eyes audit.** A fresh-context subagent scored it against the B2B screens, Orbika and three Mobbin references (Yellowbird https://mobbin.com/sites/sections/52ad00dc-133b-4d95-8b9a-c3c7bde88887, MANA Yerba Maté https://mobbin.com/sites/sections/35a3baf2-74ae-4890-b2a1-7573e0585652, Eat Hungry Tiger https://mobbin.com/sites/sections/0a65ae4c-404c-4d2d-bc70-bef248345510).
- Round 1, **3**: palette passed the ban, but the layout was still the DTC split; the tin's see-through lid, a seam, a supplement-tub look, floating above the shelf; loose daisies; washed-out white petals; the valerian label pointed at a flower though the tea uses the root.
- Round 2, **3** (upper): layout, palette, type and data passed; the art still had faults at full size (a broom-like root, offset floret outlines, blurred discs, floating side flowers, veins past leaf edges, tin type rendering at 14.4 px, labels 13 px off the spec column).
- Round 3, **4**: all fixed and checked on the pixels (labels on the spec's column at 1135, 40 px spec rows, shared baseline, 12 px tin type, 32 px caption margin). Its last small notes (root pieces reading as gravel, side heads fanning one way, the valerian label aligned to nothing) were then fixed: ringed cut faces and rootlets, rays all round the cone, the label on grid column 4's edge.
Contrast measured on the pixels: ink on the ground 13.0:1, secondary and the 12 px Latin names 6.09:1, button 7.63:1, "40 g" on the tin green 7.4:1 or more.

**Still open.** Lullwort shares the "Lull" stem with Lullwater (`app-screens/02`), a sleep app; not one letter apart, and no real tea company called Lullwort was found, so it is kept.
