# 12 · Pixel art · Lampwright

**Final self-audit score: 4 / 5** (3 rounds). Render: `shot.png`, 1440 x 900 at scale 2, dark theme.

## Direction
Lampwright is the live-ops console of a fictional studio's game, Mossbank (a cosy lakeside game drawn in pixel art). Live ops is the work of running a game after launch: events, offers, experiments. The screen is the Overview on day 3 of the seven-day Lantern Festival event: an event header with the game's own pixel key art, a strip of six KPIs, revenue per hour against last year's festival, and the live offers with their item sprites. Feel words: **playful, technical, calm**.

## The style
- **In plain words:** pixel art is a picture built from a small grid of square dots, each placed on purpose, then enlarged without smoothing so every square stays sharp. Pixel type is a typeface drawn on the same kind of grid.
- **What defines it (checkable):**
  1. A low-resolution grid scaled by a whole number (here 328 x 70 art pixels at 4x, `image-rendering: pixelated`), so no square is blurred or uneven.
  2. A limited palette with deliberate shading steps, and ordered dithering (a checker pattern) instead of smooth gradients.
  3. Shapes readable at tiny sizes: a lantern is 5 x 6 squares near the pier, 3 x 4 further up, 2 x 2 and then 1 square as they rise.
  4. Pixel type only at sizes on its own grid (Silkscreen at 16 and 32 px).
  5. Everything else on the grid too: the event's day bar uses the same 4 px unit as the art.
- **How it goes wrong ("with restraint" is the hard part):** pixel fonts on numbers and tables, so the data becomes hard to read; pixel borders and pixel buttons everywhere (a retro costume over the whole app); blurry scaling at non-integer sizes; random noise sold as pixel art; stars and sparkles as confetti.
- **How I kept it premium and restrained:** pixel art appears in exactly the places a real live-ops tool would show the game's art: the event's key art, the item thumbnails beside offers, the logo and the user's avatar. Every number, label and control is Onest, with tabular figures. The scene is composed (a plume of lanterns rising from the pier and drifting right on the wind, a quiet sky behind the title, the moon and its reflection), not scattered.

## References (Mobbin, cited by URL only)
| Reference | What it taught |
|---|---|
| General Intelligence Company, sunflower hero: https://mobbin.com/sites/sections/1d8f67c5-b815-4397-a516-9fb82198dac5 | A rich pixel scene as the banner, with clean modern type and UI over it |
| Equals, pixel magnifier: https://mobbin.com/sites/sections/71913350-1721-470b-8e68-99818ad75518 | Restraint: one pixel object beside plain text is enough |
| Lightdash, pixel team avatars: https://mobbin.com/sites/sections/94e68245-62cd-44e2-b7b9-c956cb47c511 | Pixel art at one small size inside a clean data brand |
| Arcade, insights KPIs: https://mobbin.com/screens/3cb8ac4e-d57c-444c-a061-e936dd2b28ba | The KPI strip: value, comparison, delta |
| StackAI, project analytics: https://mobbin.com/screens/03fb91f0-89d0-45e6-ada1-34d533a3febf | Dark analytics density: tiles, small charts, a table |

## System (engine)
```
sketch --name Lampwright --brand #FFC24B --audience dense --platforms web --feel playful,technical,calm --theme system-light-dark --surfaces "app:operate" --delegated all
set raw.brandColor "#FFC24B" --set-by chosen      (the sketch had swapped lantern gold for #996d00, a brown olive)
set raw.textFace "Onest"; set raw.displayFace "Silkscreen"; set raw.fontLicence {...}
```
Rendered with `data-theme="dark"`.

| Dial | Value | Why, and what it expresses of the style |
|---|---|---|
| roundness | 15 | **Pixel:** small UI corners (4 to 6 px) next to square art |
| expression | 55 | **Pixel with restraint:** art and pixel type in the header only |
| depth | 15 | Flat surfaces separated by tone |
| density | 65 | A dashboard: compact tiles and rows |
| brandPresence | 45 | Gold marks the live event and nothing else |
| colorfulness | 50 | Night indigo art, lantern gold, semantic green and red |
| energy | 35 | Still art; only the Live dot pulses (off under reduced motion) |
| warmth | 5 | 40 gave pure grey; 0 to 5 is the coolest the dial goes (slate #191d23), never indigo |

**What the dials cannot express:** the pixel grid and integer scale, the art palette and dithering, the size grid of the pixel face, and the rule "pixel art only where the game's own art would appear". The scene, sprites and palette live in `index.html`.

## Type
**Onest** (UI and every number) and **Silkscreen** (event kicker and title only), both SIL OFL, Google Fonts.

| Role | Size | Use |
|---|---|---|
| Pixel display | 32 (off-scale, Silkscreen grid) | "LANTERN FESTIVAL" |
| Headline | 27 (`font-size-27`) | KPI values |
| Pixel label | 16 (off-scale, Silkscreen grid) | "LIVE EVENT · DAY 3 OF 7" |
| Body / label | 14 (`font-size-14`) | Everything else, chart axes |

Silkscreen is crisp only at multiples of 8 px; the generated scale (11, 14, 18, 22, 27, 34) has none, so both pixel sizes are off-scale on purpose.

## Outside the tokens, on purpose
- The art palette (sky, hills, water, lantern, moon) and the item sprites: `review` lists 96 raw values, 68 of them colours, nearly all from the art and sprite palettes.
- Lantern gold uses `--ds-color-brand-seed` directly: the dark ramp turns it beige (#e6bd77 at accent-dark-9).
- Banner text colours (#fff, #d6dcf5) sit on the art, not on a surface token.
- 38 on-ladder spacings converted to tokens (render pixel-identical); the chart and sparkline SVG colours now come from tokens too.

## Checks
- `engine.py validate`: no errors. Warnings: gold on light surfaces 1.6:1 (light mode is never shown; advisory) and four macro conflicts from "playful" against "technical".
- `preflight.py html`: 2 errors, M9 for Onest and Silkscreen, false positives (the browser loaded both). No size or tracking warnings.
- `engine.py review`: 3 false hits (sprite rows like `'...w....w...'` read as "three periods in UI text"); the pulse animation's `ease-in-out` replaced with the standard easing token.
- Contrast on the cards (#191d23): primary 13.9:1, secondary 7.4:1, tertiary 5.7:1, gold 10.5:1, green 7.4:1, red 7.5:1. On the art: sub-line 9.9:1, gold kicker 10.8:1; ink on the gold button 11.4:1.
- Targets: tabs 32 px, buttons 36 px, range and game switchers 32 px.

## Rounds and self-audit
Compared at 768 px width with General Intelligence Company, Arcade and StackAI (scratchpad sheet, deleted). Early-round scores were given afterwards from what each render showed.
1. **Round 1 (about 3):** the dashboard worked, but the sky had 46 stars and 42 same-size lanterns on an even scatter (confetti, an audited tell), the gold area fill under the chart turned olive-brown on the dark card, and the event tile said "this is the event" three ways (gold border, value, line).
2. **Round 2 (3.5):** lanterns rebuilt as a plume with four sizes and halos, stars cut to 26 and kept out of the title's sky, area fill and extra border removed. The two buttons now covered the moon's reflection.
3. **Round 3 (4):** event actions moved into the copy column, day labels inline with the day bar; SVG colours tokenised.

**Tells from section 11 still present:** stars are decoration inside the scene (kept few and dim). No glow blobs, no invented proof, status shown once with text.
**Why not 5:** the scene is clean but less richly shaded than the sunflower reference; hand-placed shading on the near lanterns and pier would close the gap.

## Process findings
1. **The delegated sketch swapped the brand again**, here to a brown olive (#996d00), the exact colour family the owner rules forbid. Recorded (bug, with 09).
2. **The dark ramp desaturates a warm brand** (gold to beige). Recorded (gap).
3. **No size grid for pixel faces.** Recorded (gap).
4. **Warmth cannot reach a tinted dark** (indigo shell); a neutral-hue input would. Recorded (idea).
5. **`review` false positives** on sprite strings, and its rem-spacing standard contradicts its own px space tokens. Recorded (bug, confusing).
6. Helped: Onest on the generated 14/27 steps made the KPI strip look shipped with no tuning; semantic green and red in dark mode passed contrast first time.

## Polish round 2026-10-14
After the independent audit (score 3). **Renamed Signalfire to Lampwright.** SignalFire is a San Francisco venture capital firm. A web search found no games, analytics or live-ops company called Lampwright; the nearest is Lampright, an Australian lighting supplier. Mossbank is a village in Shetland, not a game. Name mentions above are updated; the rest of the text above describes the version before this round. A fresh-context reviewer re-audited it twice; final score **4**, with no fact errors left.

**What changed: the pixel art now runs through the data**
- **The event chart is the game's own night sky.** Each 3-hour slot from Mon 12 to Sun 18 is a column of pixel lanterns, one per 25,000 released. Last year is a pale stepped line in every slot. A dotted line marks now (Wed 13:47).
  - 92 lanterns this year against 80 last year at the same hours is +15%, matching "2.31M so far" against 2.01M.
  - The busiest slot is Monday 18:00 to 21:00, at 12 lanterns (300,000).
- **The goal is a pixel progress bar:** 2.31M of 5M, 23 of 50 blocks, on pace for Sat Oct 17.
- **Every KPI has stepped 4 px bars.** The offers carry their item sprites and $10K blocks. The banner and the smooth line chart are gone.
- **Facts.**
  - "Ends Sun Oct 18", which was "Sat".
  - Gross revenue is $706.2K, and the four offers make $554.9K of it (79%, prices before store fees). Before, the offers grossed more than the revenue.
  - Kite 0.6%. Every KPI is measured against the same 24 h a week ago.
  - D1 retention names its install day.
  - The time 14:06 and 1.84M, both used in other pieces, became 13:47 and 1.87M.
- **Sprites.** A folded paper boat replaces the crane that did not read, and the pass is a ticket stub. The hills are gone.
- **Engine.** `pick Q-dir-01 pixel-art`; the name is set; the stale build file `signalfire.resolver.json` is removed.

**References used by the re-audit:** Unity Gaming Services (https://mobbin.com/screens/8a4c6a9b-2cc5-48a0-a4b7-66f3b7754920), SoundCloud Insights (https://mobbin.com/screens/81f4a402-c167-4470-ab5d-23a892be6a5a), Lightdash (https://mobbin.com/sites/sections/86246cd3-0c0a-4ee0-bb8f-7e4e6a24b375).

**Left:** the dithered sky is a backdrop with no data, and the lower half is still the familiar list of numbers beside a table.
