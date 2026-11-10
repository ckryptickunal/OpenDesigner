# 04 Howl Hill Weekender: neo-brutalist festival hero

## Direction
Howl Hill Weekender is a fictional three-day indie music festival on a small hill: 41 loud bands, three tiny stages, camping, no VIP. The audience is 18-40 gig-goers who buy on a phone in the week tickets drop. The hero is a gig poster that works as a page: huge condensed type with a hard shadow, bordered cells for the nav, stickers slapped on top, a poster card with the moon and the hill, and two crossing tickers carrying the lineup. Feel words: **loud, playful, retro**.

## References (Mobbin, structure only)
- Eventbrite, Reconvene Summit: https://mobbin.com/sites/sections/d2ac77c3-af65-4cfb-9f59-227d98a51578 . Teaches scale: a condensed display face can fill the width at one line, with the date set small above it.
- Maze, Disco Conf: https://mobbin.com/sites/sections/a77d89bd-bdc0-4fd5-a618-c7b38671c9f2 . Teaches the marquee band crossing the page with an object sitting on top of it, and the date as a rotated sticker.
- Yellowbird: https://mobbin.com/sites/sections/52ad00dc-133b-4d95-8b9a-c3c7bde88887 . Teaches the flat yellow ground with thick black outline art and a bordered, cell-like header.
- Mobbin had little true neo-brutalism: two searches mostly returned polished SaaS heroes (a finding about the reference pool, not the tool).

## System (engine)
```
sketch --name "Howl Hill Weekender" --brand "#2433FF" --audience large --platforms web --feel loud,playful,retro --delegated all --surfaces experience
standard override STD-visual-details-24 --why "a single light poster-yellow festival page"   pick Q-theme-01 light-only
set raw.secondaryColors ["#FFD60A"]   set raw.accentCount 2
set color.accent2.light.9 {srgb #ffd60a}       (the ramp had muted the poster yellow to #f8d756)
set elevation.raised  [{0 offset 6px 6px, blur 0, color {color.neutral.light.12}}]
set elevation.floating [{10px 10px, blur 0}]      (hard offset shadows, see findings)
set raw.displayFace "Big Shoulders Display"   set raw.textFace "Space Grotesk"   set raw.fontLicence {...}
set type.displayReach 20                        (283 px display step)
```
`--audience large` was my misreading: I took it as "big type". It recorded "people who use it now and then, often on a phone" and did not change the body size (16 px). It fits a festival audience anyway, so I kept it.

| Dial | Value | Why |
|---|---|---|
| roundness | 10 | square boxes (radius tokens became 0) |
| depth | 70 | every card and button lifts on a hard shadow |
| colorfulness | 95 | saturated poster colours |
| energy | 95 | loud, fast |
| expression | 95 | a poster, not an app |
| density | 45 | packed but readable |
| warmth | 55 | neutral |

Fonts: Big Shoulders Display 800-900 and Space Grotesk 400-700 (both SIL OFL), Google Fonts link.

## Outside the tokens, on purpose
- **Headline stroke and text shadow**: a 4 px ink stroke (border-width token) and a 12 px hard text shadow from space tokens. Text-shadow cannot use the elevation tokens (they carry a spread), so it is marked `od-ignore`.
- **Rotations** of stickers and bands (-5 to 14 degrees) and the dot-grid ground: poster devices with no token equivalent.
- **Button press** moves 6 px to sit on its shadow (the raised offset).

## Checks
- `engine.py validate`: passes, 0 warnings.
- `engine.py review`: 4 hard-coded values, fixed; the text-shadow advice was wrong (see findings). Final: "the code uses the tokens".
- `preflight.py html`: 1 error, M9 false positive for Space Grotesk (Google Fonts link). It did not notice the infinite ticker animation; I added a pause button (WCAG 2.2.2) by hand, and the tickers stop under reduced motion.
- Contrast (computed): ink #252423 on yellow #ffd60a 10.98:1; white on ultramarine #2433ff 7.02:1; yellow on ink band 10.98:1. Nav links and buttons at least 44 px tall; pause button 40 px. Focus: 4 px ultramarine outline.

## Type scale (named roles, 6 sizes, two faces)
| Role | Size | Face, weight | Use |
|---|---|---|---|
| Display | 283 px (`--ds-font-size-283`) | Big Shoulders Display 900 | HOWL HILL |
| Headline | 90 px (`--ds-font-size-90`) | Big Shoulders 900 | dates, "41" |
| Headline small | 67 px (`--ds-font-size-67`) | Big Shoulders 900 | the Weekender sticker |
| Title | 38 px (`--ds-font-size-38`) | Big Shoulders 800-900 | logo, buttons, tickers, sticker words |
| Body | 21 px (`--ds-font-size-21`) | Space Grotesk 500 | lede; Big Shoulders for the nav button and small sticker lines |
| Label | 16 px (`--ds-font-size-16`) | Space Grotesk 500-700 | nav links, tag, price, captions |

## Changes for the owner's type and colour rules (mid-run)
- Buttons used 28 px, which is not on this system's scale (the token did not exist and the fallback literal was used): a seventh size. They are now 38 px (Title), with shorter labels ("Get tickets", "Play lineup") so each stays on one line.
- Weight is 800-900 everywhere on purpose: the genre is a gig poster. The one highlight in copy, "No VIP. Ever.", is a fill box in bold.
- Colour unchanged: yellow ground with near-black text (11:1), white on ultramarine (7:1).

## Process findings (piece 04)
1. **Gap:** no hard offset shadow option, and the depth stage tells people to avoid it; fixed by overriding elevation tokens through the engine.
2. **Bug:** `set` accepted a malformed shadow value and `build` then crashed with a Python traceback.
3. **Bug (again):** secondary colours are changed (the poster yellow came back muted); a token override fixed it and validation still passed.
4. **Gap:** preflight misses infinite animations without a pause control.
5. **Bug:** review suggests a box-shadow token for a text-shadow.
6. **Confusing:** `--audience large` is not what it sounds like.
7. **Helped:** overriding single tokens in DTCG form (`set elevation.raised [...]`, `set color.accent2.light.9 {...}`) is a strong escape hatch: decisions are logged and validation re-checks contrast.
