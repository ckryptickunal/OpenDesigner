# 01 · Pricing table, glass (Gloaming)

## Direction
Gloaming is a fictional AI video studio that renders short films from scripts. The page sells three plans to creators and small studios. The idea: the plans sit in a dark screening room and a projector beam falls on the plan most people pick. Teal-and-amber film grade, frosted glass cards, a film-title serif for names and prices. Feel words: **cinematic, sleek, vivid**.

## References (Mobbin, cited by link only)
- Chronicle pricing, https://mobbin.com/sites/sections/af28a0bd-bca7-461c-881b-23e85ec3c674 : a single warm light source behind the cards carries the whole mood; the cards stay almost black. Taught me to light the backdrop, not the cards.
- Framer pricing, https://mobbin.com/sites/sections/5da6c164-bbc2-4322-ac56-a6aed51c7369 : the highlighted plan is tinted from the inside with a top-down gradient, the others stay neutral. Taught me the inner radial glow on the featured card.
- Air pricing, https://mobbin.com/sites/sections/9e00570d-8572-4630-a99a-54974bb02ee3 : translucent cards, an italic display face for plan names against a plain sans, and the "Most popular" tab sitting on the card's top edge.
- Save.design membership, https://mobbin.com/sites/sections/8310aad8-6473-4310-9b07-85251a7623b5 : mono metadata and corner marks on the chosen plan. Became the viewfinder corners and the "SC 01" slate numbers.

## System (engine)
- `init`, then `standard override STD-visual-details-24` (dark-only breaks it; the brief asks for dark), then `sketch --name Gloaming --brand "#F2A93B" --audience regular --platforms web --feel sleek,vivid,cinematic --theme dark-only --surfaces "pricing page:persuade" --delegated all`.
- Dials (all `delegated`): expression 85 (persuasive page, one hero moment), density 35 (spacious cards), energy 55 (composed, glow not bounce), roundness 62 (soft glass corners, pill toggle), depth 90 (set by Q-depth-01 glass), colorfulness 82 (the amber has to glow), warmth 62 (warm light on cool shadows).
- Answers: Q-color-01 keep-hex, Q-color-09 cool, Q-depth-01 glass, Q-color-21 near-black, Q-color-10 alpha.
- `set raw.brandColor "#F2A93B"` by hand, because sketch had replaced it (see findings).
- Fonts through the engine: `raw.textFace Geist`, `raw.displayFace "Instrument Serif"` (both SIL OFL, from Google Fonts). `raw.monoFace "Geist Mono"` was set too, but after the owner's two-font rule the page no longer uses it; numbers use Geist with tabular figures.

## Build
`index.html` links `opendesigner/build/css/tokens.css` and uses `--ds-*` for colour, space, radius, type sizes, motion, focus, glass blur and the alpha neutrals.

Outside the tokens on purpose:
- `--grade-teal` (18 96 104): the cool half of the film grade, only in backdrop light. The system has one accent and cool grays; a teal ramp would be a second brand hue it does not need.
- Amber light uses the brand seed as channels (`--amber-rgb`) so it can be layered at many alphas. The projector light (`--light-rgb` 255 236 204) is the amber pushed almost to white, so the beam reads as light, not as an orange smear.
- The lit plan (`--screen` #fff6e9 to #fbe9cf) is `accent.dark.12` pushed to near-white: a light surface for ink text inside a dark page.
- The glass is the token `color.surface.glass` mixed at 55%: at the token's 72% the backdrop light never shows through.
- Display text is weight 400 with `font-synthesis: none`: Instrument Serif ships one weight, and the token weights (650 heading, 750 display) would fake a bold.
- Card padding and the card gap were 28 px at first; moved to the 24 / 32 ladder after `review`.

Interaction: the billing toggle is a radiogroup with roving tabindex and arrow keys. A pointer switch crossfades the prices in 150 ms with the token blur (2 px); a keyboard switch is instant (STD-when-to-animate-06). Cards lift 4 px on hover (200 ms, enter curve), and only change border under reduced motion. Reduced transparency and more-contrast make the glass solid.

## Revision for the owner's type and color rules (mid-run)
What changed and why:
- **Two fonts.** The first version used three (Instrument Serif, Geist, Geist Mono for small labels). The mono labels were not code, so they are now Geist; prices and minutes keep tabular figures.
- **No italic-serif highlight.** The headline was "Light every *frame.*" with the last word in italic serif and an amber gradient, which is the forbidden trick. The visual weight of this screen belongs to the lit plan, so the headline is now one plain line in Instrument Serif regular with no highlight. Plan names are upright too.
- **Tonal contrast, no cream on brown.** Before, the featured card was dark glass lit amber from behind, so its text was cream on a brown mid-tone (it needed a warm text colour to pass at all), and an orange glow at the bottom right muddied the teal. Now the lit plan is a near-white screen with ink text (about 17:1) and an ink button, the two other plans stay dark glass with light text, the beam is whiter, and the orange glow is gone. The page reads as dark with one bright object, which is the point.
- **Type scale, named roles** (Material 3 names, web px): caption 12 (labels, billing notes), body 16 (copy, features, buttons), title 28 (wordmark, currency sign), headline 38 (plan names), display-md 67 (page title), display-lg 90 (prices). Six sizes, each at least 10% from the next. Titles are regular weight on purpose: Instrument Serif has one weight and large regular serif reads more premium than a faked bold.

## Checks
- `preflight.py html`: 0 errors, 0 warnings after replacing two `<br>` with `max-width`. It reported "font sizes in px: []" because every size is a `var(--ds-font-size-*)`: it cannot see token sizes.
- `engine.py validate`: no errors, 3 warnings. Two are light-mode warnings on a dark-only system (a bug), one is the feel-word conflict.
- Rendered contrast (my own script: computed text colour against the dominant pixels behind each text box, text hidden): first pass 10 failures, all secondary or tertiary text on the lit glass (worst 2.88:1). Fixed with a warm light text (`accent.dark.12`) inside the featured card (STD-visual-details-13) and a dimmer bloom. After the colour revision: 92 text runs, one below 4.5:1, the "Current plan" disabled sample (3.15:1, inactive and exempt).
- `engine.py review`: 103 findings at first, 41 after moving hairlines to the alpha neutrals and spacing onto the ladder. What is left is the art light (teal, amber glows, glow shadows), on purpose.
- Keyboard test (Playwright): first Tab lands on the checked radio with a visible ring; ArrowLeft switches to monthly instantly ($24, "Billed monthly"); ArrowRight back to $19.
- Checklist: computed styles show 6 sizes, all from the scale (12, 16, 28, 38, 67, 90); two faces, both loaded (Geist 400/500, Instrument Serif 400), no fallback renders; headings balanced; no pills wrap.

## Process findings
1. **Sketch replaced the brand colour.** `sketch --brand "#F2A93B"` printed "I picked a brown for buttons ... with white text" and stored #a16900 as `raw.brandColor`. Stage 08 says a light brand colour should switch its button text to dark instead. Recorded as a bug.
2. **keep-hex lied.** `pick Q-color-01 keep-hex` said "the tokens already match this answer" while #F2A93B was in no ramp. Bug.
3. **Dark-only needs a hidden order.** `sketch --theme dark-only` refuses and says to run `standard override`, which fails with "no state" until `init`. Confusing.
4. **Dark-only still checks and documents light mode.** Bug.
5. **Weights do not know the face.** Instrument Serif has one weight; the tokens ask for 650 and 750. Gap.
6. **No 14 px step** at expression 85. Gap.
7. **Glass over art is never contrast-checked**, and the glass token is too opaque to show the art. Gap.
8. **The alpha neutral ramp exists but is undocumented.** Confusing.
9. **review is noisy and sometimes wrong** (a backdrop colour mapped to `text-on-action`, `width: 80px` to `space-80`). Bug.
10. Helped: `standards` gave clear rules I would not have remembered (instant keyboard changes, glass needs a reduced-transparency fallback, warmer text on glass). The `--ds-motion-blur-crossfade` token made the price swap feel right with no guessing.
