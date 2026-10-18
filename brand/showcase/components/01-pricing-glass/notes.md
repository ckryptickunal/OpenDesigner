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

## Round 3 (owner review, 2026-10-14)
**What Kunal said:** "can be better". The earlier audit named the hard-edged projector beam, the teal and amber corner blooms, the viewfinder marks and slate numbers, and the "$51 per seat, monthly … billed yearly" contradiction.

**What changed:** the piece is now Gloaming's pricing page at real size (1440 x 900), with the plan table in it, instead of a component sheet.
- **A plan table, not three cards.** A label column (with the billing toggle) and three plan columns of 300 px on a 1,200 px grid, then grouped rows with units: render-minutes, minutes past your plan, export resolution, finished film a month, longest clip, renders at once, licence, review links, single sign-on. The table runs on below the fold, as a real page does.
- **One idea, no light effects.** The beam, blooms, glass, grain, corner marks and slate numbers are gone. The plan most people pick is the one lit column (near-white, ink text) in a dark room; the filled button is its only other emphasis. No tag, no overhang (the first rebuild had both; the fresh audit counted four signals for one state).
- **Numbers re-added and made consistent.** Studio $19 yearly / $24 monthly, $228 a year, saves $60. Premiere is now $48 a seat yearly / $60 monthly, 1,800 render-minutes a seat pooled ($0.027 a minute yearly, $0.033 monthly) with extra minutes at $0.035, so extras never cost less than included minutes; 3 seats = $1,728 a year or $180 a month. Finished film: 20 / 4 = 5 min at 720p, 600 / 15 = 40 min, 1,800 / 15 = 120 min a seat. "Yearly saves 20%" holds (Studio 20.8%, Premiere 20.0%). The lead no longer claims "full quality" on every plan.
- **Type:** Instrument Serif (headline 51, prices 38, plan names 28) and Geist (lead 21, body and table 16, one caption 12). Six sizes, all at least 25% apart; weights 400 and 500. The billing lines and every number that matters are 16 px, not 12.
- **Engine:** `set dials.depth 35` (was 90, glass) and `build`. The rebuild also brought `accent.dark.9` to the exact brand #F2A93B (it was #e8ad5e). Brand colour checked: still #F2A93B.
- **States, one per frame:** `shot.png` (yearly, default), `shot-monthly.png`, `shot-hover.png` (the whole Premiere column tints), `shot-loading.png` (Studio's trial starting), `shot-current.png` (signed in as Odile Brenner: "412 of 600 used. Resets Nov 3." with a usage bar, a filled "Your plan", "Upgrade to Premiere", and the downgrade as a quiet link), `shot-focus.png` (keyboard focus on the toggle, amber ring 9.6:1). Render any of them with `--query state=<name>`.

**Checks:** rendered contrast (text hidden, each line against the pixels behind it): 67 runs, 0 below the floor, also in the current and loading states. Computed sizes 12, 16, 21, 28, 38, 51; two faces. `check_dates.py`: pass. `engine.py validate`: no errors. `preflight.py html`: 0 errors on the final page (the first rebuild drew a false "Geist has no @font-face" error; Geist loads from the Google Fonts link, and the finding is recorded from round 1). `engine.py review`: 33 notes, nearly all px values that equal a ladder step (`height: 32px`) plus the reduced-motion spinner at 2.4 s, which is deliberate.

**Fresh-eyes audit:** first pass 3/5 ("clean but the stock SaaS layout, no table, Premiere costs twice as much per minute, the lit plan flagged four ways"). After the table rebuild 4/5; its six remaining notes (header row shifting in the signed-in state, a missing resolution row, Premiere's overage below its included rate, tall blank group rows in the lit column, the empty top-left cell, square hover corners) were all fixed. References: Linear pricing comparison https://mobbin.com/sites/sections/0499d8f7-09b7-4022-afc1-4b63a4fabb00 (the label column with the billing toggle, a highlighted column), Linear cards joined by hairlines https://mobbin.com/sites/sections/5ffa41ef-e9a4-428b-921e-c13ad57b4873, Framer pricing https://mobbin.com/sites/sections/5da6c164-bbc2-4322-ac56-a6aed51c7369.

**Fresh score: 4.**

## Round 4 (owner review, 2026-10-15 to 2026-10-18)
**What Kunal said** (relayed by the coordinator): "most of the web components look absolutely rubbish"; "None of them should feel like they are from a vibe coded app or a cheap Chinese app." The round-4 audit (`AUDIT-ROUND4.md`) gave this piece 6: "a slider panel, a note line under each button and a footnote all stack up", "reads as a copy of the dark Linear or Vercel pricing style", tiny tick labels. This section replaces the descriptions above: the serif, the lit column and the nine-row table are gone.

**The idea, in one sentence:** you set how much finished 4K film you make a month, and the plans tell you which one covers it for least.

**What changed**
- One panel: the usage estimator spans the top, the three plans sit under it, and the slider runs from Studio's text edge to Premiere's. Each paid plan has a meter of your usage against its allowance; the plan that covers it for least says "Cheapest fit for 32 min" and carries the one filled button. The choice follows the slider and the billing toggle (Studio up to 240 min yearly, Premiere above).
- Prices are the one display size (43 px); the heading and the estimate are a step down (22 px). Instrument Sans replaces Geist (three audits read Geist on zinc as the stock dark template). Twilight blue-black surfaces (off-token, said in the CSS) with amber only for your usage.
- Cut: the subtitle, the footnote, the per-plan note lines, the ruler ticks, Spark's empty meter, "3 seats" said three times (now "3-seat minimum" once), "ProRes" (a real product name). Feature lists are three rows that differ by plan; a comparison table under the plans, on the plan columns, is cropped by the frame.
- Engine: displayFace `=textFace`, textFace Instrument Sans, base size 14, Q-color-09 cool, expression 45, colorfulness 40, energy 35, roundness 45, warmth 25, density 60. Brand #F2A93B unchanged. Stale extra frames (shot-current, shot-focus, shot-hover, shot-loading) deleted; shot-monthly.png re-rendered.

**Type scale:** 12 (slider ticks, comparison labels), 14 (body, meters, comparison heads), 18 (plan names), 22 (heading, estimate), 43 (prices). One face.

**Blind pairwise test** (opaque names, random sides, fresh judges), final version: Aside https://mobbin.com/sites/sections/de9e1a65-59c9-41f0-8c73-01df009482e1 reference better by 2; HoneyBook https://mobbin.com/sites/sections/e72ef239-29c4-45c5-b9b1-cd92db0a4173 ours better by 2; PamPam https://mobbin.com/sites/sections/67e0a61a-3431-44e4-9f2b-23e3477c87d5 ours better by 3. 2 of 3 better; worst margin 2. Earlier rounds: 3 of 3 better twice, 2 of 3 three times; never weaker by 3.

**Fresh-eyes audit: 3, in six rounds.** Every price and the estimator logic checked out each time. The audits kept naming the same thing: a generic dark three-plan layout that is sparser than the B2B product screens, with the estimator as the only original idea. The last round's concrete notes were fixed afterwards and checked by measurement, not re-audited: the comparison rows now sit on the plan columns under a plan-name header, the estimator and meter text are 14 px, nothing wraps at 240 or 320 minutes in either billing mode (buttons and lists align in all three states), Spark's reason moved into its bill line. **This piece did not reach 4.** It needs the owner's call: a light page in the B2B screens' manner, or a different presentation of the estimator.

**Checks:** check_dates pass; check_names 0 errors; preflight 0 errors; engine validate passes (2 light-mode warnings on a dark-only system, as recorded in round 1).
