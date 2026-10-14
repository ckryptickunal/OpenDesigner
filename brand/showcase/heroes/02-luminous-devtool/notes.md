# 02 Orrery: luminous dev-tool hero

## Direction
Orrery is a fictional open-source vector database. Its audience is backend and ML engineers who judge a tool by its numbers and its code sample before its adjectives. The hero is a night sky: an embedding "galaxy" drawn in canvas, a bright query star joined to its 8 nearest neighbours inside orrery rings, and the product floating in front with real depth (a results table, the query in code, a latency chip), each panel at a different distance. Feel words: **techy, futuristic, precise** ("precise" is not in the engine's word list; it asked, which is the designed behaviour).

## References (Mobbin, structure only)
- Customer.io developers hero: https://mobbin.com/sites/sections/cbac56f2-5cdf-45a1-814d-83c855d8f552 . Teaches the overlap: a code card in front of a chart card with a floating stat chip, so the product reads as layers.
- Shopify Editions developer platform: https://mobbin.com/sites/sections/1a1c2145-71da-40a3-9e78-56b515a907e8 . Teaches rim light: a coloured glow around the product window lifts it off a dark page.
- Retool: https://mobbin.com/sites/sections/dcbd55be-58cb-4e0e-9b70-cb4d184fa30a . Teaches the split: a calm text column left, the product bleeding toward the right edge.
- Railway: https://mobbin.com/sites/sections/087ce883-5976-4533-bd70-0e050800f938 . Teaches restraint: one deep ground, thin hairline panels, the colour reserved for live state.

## System (engine)
```
sketch --name "Orrery" --brand "#46E0D3" --audience dense --platforms web --feel techy,futuristic,precise --delegated all --surfaces persuade
standard override STD-visual-details-24 --why "Art direction for this marketing hero is dark-only"
pick Q-theme-01 dark-only
set raw.brandColor "#46E0D3"        (sketch had changed it to #00837b, a dark teal for white text)
set raw.textFace "Geist"   set raw.monoFace "Geist Mono"   set raw.fontLicence {web, app, selfHost}
set raw.darkBase "black"   set raw.neutralTint "cool"
set raw.secondaryColors ["#8B6CFF", "#3D63FF"]   set raw.accentCount 3
set type.displayReach 5
```
| Dial | Value | Why |
|---|---|---|
| depth | 85 | the product floats with real depth |
| colorfulness | 55 | one luminous accent plus the halo hues |
| warmth | 15 | cool night-sky neutrals |
| roundness | 40 | panels 12 px, controls 6 px |
| energy | 65 | fast, confident |
| expression | 75 | marketing hero with a generative light field |
| density | 55 | engineers read dense code and numbers |

Fonts: Geist and Geist Mono (SIL OFL), Google Fonts link.

## Outside the tokens, on purpose
- **Glow and the deep drop shadow.** On a black ground the engine's elevation shadows (depth 85) are invisible, and there are no glow tokens. I defined `--glow-sm`, `--glow-md` and `--drop` at the top of the page from token colours and token sizes. `--drop` is marked `od-ignore`.
- **Panel fill** mixes `neutral-dark-4` and `neutral-dark-3` with transparency, because surface.raised and surface.overlay are #010101 and #050608 with the black base: too close to black to separate.
- **The light field** (canvas) reads every colour from the tokens at run time (`brand-seed`, accent, accent2, accent3, neutral dark 1, white) and is seeded, so every render is identical. Its washes, rings and grain are art, not UI.
- **Headline** tracking -0.035em (system -0.02em) and line-height 1.02: checked at 200%, no glyphs touch.
- **Code sample** is 12 px mono inside the product picture (aria-hidden). Line numbers are 1.8:1 and decorative.

## Checks
- `engine.py validate`: no errors; 2 warnings, both about the light mode this dark-only system does not use (see findings).
- `engine.py review`: first run 37 hard-coded values (glows, white alphas, pixel heights). Moved onto tokens (alpha neutrals, control sizes, border widths); final run: "the code uses the tokens".
- `preflight.py html`: 2 errors (M9 for Geist and Geist Mono loaded from Google Fonts: false positive) and 1 warning (tracking -0.035/-0.04, checked at 200%: no glyphs touch). Before the owner's rules it also warned about the 13 px code (now 12 px, a token). After that change it reported `font sizes in px: [22]`: it read the 22 px line height in `font: 400 var(--ds-font-size-12)/22px ...` as a font size.
- Contrast (computed): lede #94989f on #000 7.25:1; labels #7b8087 on #000 5.28:1 and on the panel #111315 4.68:1; primary button black on #67dacf 12.5:1; headline #d7dadf on #000 15:1. Targets: nav links 24 px minimum, buttons 40-48 px. Focus: token ring.

## Type scale (named roles, 5 sizes, two faces)
| Role | Size | Face, weight | Use |
|---|---|---|---|
| Display | 67 px (`--ds-font-size-67`) | Geist 300, the phrase in 600 | headline |
| Title | 28 px (`--ds-font-size-28`) | Geist Mono 500 | the latency figure (data) |
| Body large | 21 px (`--ds-font-size-21`) | Geist 400; Geist Mono 500 for figures | lede, stat figures |
| Body | 16 px (`--ds-font-size-16`) | Geist 400-500; Geist Mono for the install command | nav, buttons |
| Label | 12 px (`--ds-font-size-12`) | Geist; Geist Mono only for code and scores | chip, stat labels, table, code |

## Changes for the owner's type and colour rules (mid-run)
- Headline was 600 throughout with a gradient-filled phrase. Now the first line is light (300) and "at the speed of memory." is 600 in the same colour: the highlight is weight, and the visual weight sits on the promise, while the light field carries the colour.
- Mono was also used for small labels (stat captions, panel labels, tab names, one customer wordmark). Those are Geist now; mono is left only for code, the install command and figures.
- Code went from 13 px to 12 px (13 and 12 were within 10%).
- Colour unchanged: black ground with bright text (lede 7.25:1, headline 15:1).

## Process findings (piece 02)
1. **Bug:** sketch rewrote the luminous aqua into a dark teal for white text, even though a dark UI wants dark text on the aqua.
2. **Bug:** dark-only still validates and exports light mode.
3. **Gap:** a black dark base collapses surface steps; depth in dark mode means shadows only; no glow or rim-light tokens.
4. **Confusing:** secondary colours are ignored silently until `accentCount` is raised.
5. **Bug:** review calls hairline inset borders shadows; radius suggestions are inconsistent.
6. **Helped:** `secondaryColors` plus `accentCount 3` gave real violet and indigo ramps that the canvas and syntax colours could read, so the art and the UI share one palette. `darkBase` and `neutralTint` are good levers once found.
