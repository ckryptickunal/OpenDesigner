# 09 Kumo Kōbō: Japanese ceramics workshop hero

**Direction.** Kumo Kōbō (雲工房, "cloud workshop") is a fictional two-person ceramics workshop with one wood-burning kiln. It sells tea bowls and tableware twice a year, after each kiln opening. The audience is collectors and people planning a visit. Mood: a scroll painting in a quiet room. Feel words: **calm, traditional, understated**.

Render: 1440 x 900 at scale 2 (`shot.png`).

## References (Mobbin, cited by URL only)
| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/dfb1f238-01a9-4866-afae-db35c7863ae8 | Ceramic objects as the whole art direction, with the headline kept small and wide margins around everything. |
| https://mobbin.com/sites/sections/37214c10-d891-48bc-a46e-6050033671b4 | An asymmetric serif headline with one inset artwork; tiny text pinned to the corners. I took the corner-pinned micro type: date, counter, caption. |
| https://mobbin.com/sites/sections/1fcb7257-0639-4121-b5c3-74491b005663 | Monochrome restraint with a small information block in a corner. |
| https://mobbin.com/sites/sections/a87f2a50-8a78-4193-b491-5589059041fa | A warm, quiet palette, and type that whispers next to the object. |

## System (engine)
```
init; standard override STD-visual-details-24 (one light page)
sketch --name "Kumo Kobo" --brand #A23A2A --audience regular --platforms web --feel calm,traditional,understated --theme light-only --surfaces "landing page:persuade" --delegated all
```
| Dial | Value | Why |
|---|---|---|
| expression | 55 | Art-led, but quiet |
| brandPresence | 20 | Only the seal carries color |
| energy | 10 | Still |
| roundness | 0 | No boxes, no pills |
| depth | 0 | Paper is flat |
| colorfulness | 10 | Ink, paper, one red |
| warmth | 80 | Warm paper |
| density | 15 | Lots of air |

Other settings:
- `raw.neutralBase` #D9C9A8 moved the neutrals from pinkish grey to washi beige (#f1ebde). It worked well in light mode.
- `raw.scripts` ["Latn","Jpan"] gives `:lang(ja)` a 1.133 line-height scale.
- Q-dir-02 `spacious`.
- `raw.fontLicence` all true.

**Fonts.** Display, Japanese and English: Shippori Mincho. Text: Zen Kaku Gothic New. Both SIL OFL, from Google Fonts, both covering Latin and Japanese.

## Art
`opendesigner-paint brief --slot hero` ran. It recommended sketch, watercolour or charcoal, and its "archival-ink" palette family is the one used.

The film engine needs npm, Playwright and ffmpeg installed with the owner's yes, so the painting is done in canvas instead:
- **Washi paper:** a base color, a soft light falloff, 2,600 fibres and grain.
- **The tea bowl, painted per pixel as ink density:**
  - pale ash glaze over a dark iron glaze, with a wavy boundary
  - streaks that follow the form (noise in a curve-following coordinate)
  - the right side running dry where the light falls
  - 13 ash runs dragged down into the dark
  - ink pooling at the edges, and a darker lip at the front
- **Finishing:** a thin far rim, a foot ring, a cast-shadow wash, a pale moon wash and a few spatters. All of it is multiplied into the paper.
- **The seal (落款):** red with an SVG turbulence edge.

## Outside the tokens, on purpose
- Display at weight 400: the engine's lightest heading weight is 600, too heavy for Mincho at this mood.
- Canvas art: all colors come from neutral tokens (`--ds-color-neutral-light-*`) with alpha; the geometry and densities are art.

## Checks
- `engine.py validate`: no errors, 0 warnings.
- `preflight.py html`: 1 error, false (M9 Google Fonts). The `<br>` was fixed.
- `engine.py review`: 4 raw sizes left (seal, label rule, counter rule); no standards broken.
- Contrast:
  - ink on washi: 13:1
  - secondary text: 6.0:1 (7.0:1 at the light spot)
  - seal character: 6.0:1
  - The quiet link underline moved to `border-strong` (3.2:1).
- Japanese text is marked `lang="ja"`. Art is `aria-hidden`.

## Process findings
1. **Low colorfulness turns the ramp around the pinned red grey.** Hover and link colors lose the brand hue. (bug)
2. **No light path in the paint skill for a single painted still,** and no ink-wash style. (gap)
3. **The paint brief's "brand-tint" family uses a grey accent tint** instead of the washi neutral. (bug)
4. **The display weight floor of 600** (also in 07).
5. What helped:
   - `neutralBase` gave a true washi beige at once.
   - The CJK script setting produced a `:lang(ja)` line-height rule.
   - The paint brief's families and its "accent mark" idea (the brand red used once, as the seal) shaped the whole page.
   - `review` came back nearly clean, because the art reads its colors from tokens.

## Owner type and color rules (applied after the first render)
- **Fonts:** already two (Shippori Mincho, Zen Kaku Gothic New).
- **Highlight:** none in the headline. The bowl and the red seal carry the visual weight, and the headline stays a quiet regular 400.
- **Color:** the warm neutrals were drifting brown-olive (secondary text #63563c). `raw.neutralBase` moved to #DCD3C1 and warmth from 80 to 60. Paper is now #efebe4 and secondary text #5d5648 (6.1:1). The page is still clearly light ground with dark ink.
- **Type scale (5 sizes):**

  | Role | Size | Use |
  |---|---|---|
  | Headline | 39 | Headline |
  | Title | 25 | Vertical inscription |
  | Body large | 20 | Wordmark |
  | Body | 16 | Lede, links, caption title |
  | Caption | 13 | Nav, labels, caption, footer |

  The seal character is part of the SVG art.
