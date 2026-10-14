# 07 Isobath Ocean Observatory: climate data hero

**Direction.** Isobath is a fictional ocean and climate data institute. It runs floats, moorings and gliders in the North Atlantic and publishes the readings openly. The audience is scientists, journalists and policy staff who want to trust the numbers before they read them. Mood: a chart room at night. Feel words: **calm, precise, technical**.

Render: 1440 x 900 at scale 2 (`shot.png`).

## References (Mobbin, cited by URL only)
| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/cb2e0ca2-02bf-4362-b00f-07f093c0766f | Line-drawn topographic forms in one accent on a deep ground, with hairline ticks on the frame edge. I took the single-color line art and the edge ticks. |
| https://mobbin.com/sites/sections/9b6f664a-b824-4de5-9b81-54126c6a391e | A large headline with one tinted phrase, and mono data used as texture. Here the tinted phrase is the italic "record". |
| https://mobbin.com/sites/sections/38d3c862-d84c-4840-9fd0-94002eaf5571 | Restraint: one drawing, small mono captions, lots of dark. It kept the readouts few and quiet. |
| https://mobbin.com/sites/sections/ecdffa16-f143-4fe1-9232-bc3cdb8a3665 | A scientific visualization can be the whole hero when its color stays inside the brand palette. |

## System (engine)
```
init; standard override STD-visual-details-24 (dark-only)
sketch --name Isobath --brand #3FC1D9 --audience regular --platforms web --feel calm,precise,technical --theme dark-only --surfaces "landing page:persuade" --delegated all
```
| Dial | Value | Why |
|---|---|---|
| expression | 45 | Art-led, but scientific restraint |
| brandPresence | 35 | Data and map lead; brand recedes |
| energy | 20 | Calm, no bounce |
| roundness | 0 | Instrument hairlines, square corners |
| depth | 10 | Lines and type, no shadows |
| colorfulness | 30 | Cyan plus one warm signal (tried 50: no change, reverted) |
| warmth | 10 | Cold neutrals |
| density | 55 | Readouts are dense |

Other: `raw.neutralBase` #0E2A4A (navy tint; barely moved the base), `raw.primaryActionColor` #3FC1D9 (fixed a muddy dark-mode button), Q-dir-02 `spacious`.

**Fonts (final).** IBM Plex Sans: display at Light 300, and all words. IBM Plex Mono: data only. Both SIL OFL. The first render used Source Serif 4 as a third face (see the owner rules below).

## Art
The bathymetry is generated on canvas. Seeded value-noise fBm, plus a seamount, a ridge and a trench, is contoured with marching squares at a 5 px grid. Every fifth line is an index contour. Lines are drawn into a white mask, then colored by position: cyan everywhere, `danger-dark-11` coral inside the marine heatwave. Depth labels sit on a few index contours. A float track ends in a crosshair. Latitude ticks run on the left edge.

## Outside the tokens, on purpose
- The navy background (#041120 to #082039) and the scrims behind the copy and rail: the neutral ramp's base step stays grey (#131519).
- Display weight 300 (Plex Sans Light): the lightest heading weight the engine makes is 600.
- Headline at 95px uses `--ds-font-size-95` (on scale). Line art colors come from tokens (`accent-dark-11/12`, `danger-dark-11`); alphas are art.

## Checks
- `engine.py validate`: no errors. The 2 warnings are about light mode, which this dark-only system does not ship (a bug, filed).
- `preflight.py html`: 2 errors, both false. They are M9 "no @font-face" for faces loaded from Google Fonts.
- `engine.py review`: 7 raw values remain (the 80px nav height, the live-dot halo, and sizes inside sparklines); 1 standard was fixed (2px became `--ds-space-2`).
- Contrast on navy: body/secondary 7.6:1, primary 14.4:1, cyan line labels 7.7:1, coral 7.7:1, the CTA's dark text on cyan 8.5:1, and the edge ticks 6.3:1. Canvas depth labels are 12px and decorative (`aria-hidden`).
- Targets: nav links 40px, buttons 48px; focus ring from tokens.

## Process findings
1. **Navy can't be made.** `neutralBase` is capped and the base step is forced near grey. (gap)
2. **Colorfulness doesn't reach a brand-seeded ramp,** and the dark-mode button became a muddy teal. Only `primaryActionColor` fixed it, and nothing in the output said this would happen. (confusing)
3. **validate checks light mode for a dark-only system.** (bug)
4. **No light display weight** (the minimum is 600). (gap)
5. **"precise" was silently dropped** from the feel words. (bug)
6. **The rem-spacing standard conflicts with the px space tokens.** (bug)
7. What helped: the dark ramps are well balanced. Secondary text at 7.6:1 on navy came free. `danger-dark-11` is a beautiful warm signal. Plex Mono with tabular numbers, read from the mono face token, made the rail look like an instrument at once.

## Owner type and color rules (applied after the first render)
- **Fonts:** two only. Source Serif 4 was dropped, using `engine.py set raw.displayFace "=textFace"`. IBM Plex Sans now carries the display (Light 300) and all words. IBM Plex Mono is kept only for data: readout values, deltas, the rail's live header, map tags, depth and latitude labels, and the position bar. Labels that were mono (eyebrow, readout names, the "Ocean Observatory" line) are now Plex Sans in caps.
- **Highlight:** the one-italic-word trick ("record." in italic serif) was removed. The headline has no highlight now. The heatwave on the map holds the screen's visual weight, and the light display headline is the calm second voice.
- **Weight:** Light 300 at 95px, chosen because a light display is more premium and calmer than the engine's 600.
- **Type scale (5 sizes):**

  | Role | Size | Use |
  |---|---|---|
  | Display | 95 | Headline |
  | Title | 25 | Readout values |
  | Body large | 20 | Lede |
  | Body / label | 16 | Nav, buttons |
  | Caption | 13 | Labels, data, canvas labels (were 12) |

- **Color:** deep navy with bright text (14.4:1) and one coral signal. Not brown, not muddy.
