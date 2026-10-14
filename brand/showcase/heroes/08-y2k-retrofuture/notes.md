# 08 Orbika SR-1: Y2K retro-future hardware hero

**Direction.** Orbika is a fictional maker of a pocket satellite radio. The SR-1 receives about 2,400 stations from orbit, with no towers and no account. The audience is travellers and gadget lovers who miss physical buttons. Mood: a chrome toy from 2001 that still works, played straight. Feel words: **playful, futuristic, techy**.

Render: 1440 x 900 at scale 2 (`shot.png`).

## References (Mobbin, cited by URL only)
| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/9f0e3e90-1f2c-4e81-a719-0f0ca5a2063a | A very wide display word spanning the full width as the anchor of the page. Here that is the headline, not the logo. |
| https://mobbin.com/sites/sections/cac5c6fe-01b5-4769-8972-a2d70c190673 | Pixel type next to plain type, and a bright block behind one word. I took the lime block behind "SKY.". |
| https://mobbin.com/sites/sections/acc902bb-ea91-4876-ad44-a2378a7c778e | CRT details: scanlines, slight curvature darkening at the edges, color fringing. Used on the LCD, the ticker and "SKY.". |
| https://mobbin.com/sites/sections/2e285ad6-ea7e-404a-9849-61c2bc6654e2 | The device on a stage as the hero, with the copy kept small beside it. |

## System (engine)
```
init; standard override STD-visual-details-24 (light only)
sketch --name Orbika --brand #B8F400 --audience regular --platforms web --feel playful,futuristic,techy --theme light-only --surfaces "landing page:persuade" --delegated all
set raw.brandColor "#B8F400"   (sketch had swapped it for olive #5f8000)
```
| Dial | Value | Why |
|---|---|---|
| expression | 90 | Y2K maximal product hero |
| brandPresence | 75 | Lime marks every key moment |
| energy | 80 | Punchy display |
| roundness | 70 | Pill bezels (buttons use `radius-full`) |
| depth | 85 | Chrome needs depth |
| colorfulness | 55 | Chrome greys plus one acid lime |
| warmth | 25 | Cool metal |
| density | 40 | Roomy product page |

Q-dir-01 `soft`: the nearest material to chrome; it warns that soft fails 3:1 edges by design. `raw.fontLicence` is all true (OFL).

**Fonts (final).** Michroma (display) and Space Grotesk (text), both SIL OFL. The first render also used Silkscreen for LCD and labels; it was removed under the owner rules (see below).

## Art
- The receiver is pure CSS:
  - a chrome capsule made of banded gradients from the neutral ramp
  - a speaker grille drawn with a radial-gradient dot pattern
  - a lime LCD with scanlines and a pixel spectrum
  - a knurled tuning dial (repeating-conic-gradient)
  - pill keys and a telescopic antenna
- A canvas draws a faint dot-matrix grid. Pixel radio arcs come off the antenna tip: each circle is walked and the cell under it lit, like Bresenham's algorithm in pixel art.

## Outside the tokens, on purpose
- 104px headline (the scale stops at 90).
- Specular white bands and deep shadow tones in the chrome. The chrome color stops are neutral tokens; the alphas and blend are by hand.
- The chromatic fringe on "SKY." (decorative 18% magenta and cyan).

## Checks
- `engine.py validate`: no errors. Warnings: lime action on a light surface is 1.29:1 (advisory, a labelled button), so every lime button got a 2px ink outline and an ink drop edge. Soft preset edges also warn.
- `preflight.py html`: 3 errors, all false (M9 Google Fonts). The `<br>` warning was fixed.
- `engine.py review`: 1 standard was fixed (a 3px gap). 29 raw values are left; 18 of them are chrome shadows.
- Contrast:
  - ink on lime: 11.8:1
  - LCD text: 9.5:1
  - lede on silver: 5.2-6.1:1
  - The chrome under the nav and button text failed at the darkest band (4.3:1). It now uses a softer chrome behind text, with a minimum of 11:1.
- The device, sticker and canvas are `aria-hidden`. The ticker is labelled "Now playing".

## Process findings
1. **`--delegated` swapped the brand hex.** Acid lime became olive (#5f8000) so white text would pass, and the sketch output only said "I picked a green". For a neon brand, this destroys the identity. (bug)
2. **No chrome or metal material.** Soft/neumorphic was the nearest option. (gap)
3. **Only three face roles,** so the pixel face first had to replace mono. Under the two-font rule it went entirely, and the LCD became drawn art. (idea)
4. Same as 06: the display weight token is 850 (Michroma has one weight), the scale stops at 90px, and the yellow-green tint steps are sage, not lime.
5. What helped: the brand-exact pin at step 9 with dark on-text was exactly right once the hex was restored. The validate warning about a lime button on a light surface was a real catch; it led to the ink outline, which also looks more Y2K.

## Owner type and color rules (applied after the first render)
- **Fonts:** two only. The pixel face (Silkscreen) was dropped, using `engine.py set raw.monoFace "ui-monospace"`. Michroma is the display: headline, wordmark, tagline, spec values, sticker number and the ticker. Space Grotesk handles everything else, in caps with tracking for labels and with tabular numbers for the RX/SATS/SIGNAL data.
- **LCD:** the screen is now dot-matrix art drawn on canvas from a hand-made 5 × 7 bitmap, with ghosted unlit dots and a spectrum. It is part of the device illustration (`aria-hidden`), not a font.
- **Highlight:** "SKY." in a lime fill box with an ink keyline, which is the allowed fill-box form. Michroma has one weight (400), so the headline is regular by design.
- **Type scale (5 sizes):**

  | Role | Size | Use |
  |---|---|---|
  | Display | 104 | Headline |
  | Headline | 28 | Sticker number |
  | Title | 21 | Wordmark, tagline, spec values |
  | Body / label | 16 | Body, buttons, nav, ticker |
  | Caption | 12 | Labels, keys |

  The 51px LCD channel size is gone; it is now art.
- **Color:** silver with black ink, and lime only with ink on it (11.8:1).
