# Watch screens: process report

Eight fictional watch apps, each made through OpenDesigner end to end: Mobbin references, a system from `engine.py`, a page that reads the generated `--ds-*` tokens, renders at 205 x 251 CSS px (49 mm class) at 3x, checks, notes. The board is `sheet.png` (1600 x 1000 at 2x).

Files: each piece has `index.html`, `shot.png`, `notes.md`, `engine-log.txt` (every engine command and its output), `opendesigner/` (state, decisions, tokens, builds) and `DESIGN.md`. `render.py` renders and clips a piece to the display shape. `systems.py` re-creates the eight systems (it deletes each `opendesigner/` first).

## The pieces

| # | Brand, domain | Palette | Type (one family each) and roles used | Shape idea | Render |
|---|---|---|---|---|---|
| 01 | Fellrise (was Ridgeline), trail pace and climb | acid green #C8FF2E on black | Archivo: 13 / 17 / 30 / 68 display | slanted heavy numeral, hatched ridge, cut-corner tag | 205 x 251 @3x |
| 02 | Thrum, heart-rate zones | warm red #FF5436, amber-to-crimson zones | Bricolage Grotesque: 13 / 17 / 30 / 104 display | one giant numeral, segmented zone bar, live trace | 205 x 251 @3x |
| 03 | Tidemark, dawn tide face | sky blue #5CC8FF, navy sky | Sora: 14 / 17 / 20 / 72 display | generative dawn sky, tide sine on the sea | 205 x 251 @3x |
| 04 | Headway, transit countdown | signal yellow #FFCC1A on black | Big Shoulders Display: 14 / 17 / 20 / 30 / 114 display | signage: square badges, hard rules, vertical MIN | 205 x 251 @3x |
| 05 | Nook, home scenes | lamp amber #FFB54A, neutral tiles | Nunito: 15 / 17 / 30 | pillowy tiles, one lit | 205 x 251 @3x |
| 06 | Hush, breathing | lavender #B9A6FF | Fraunces (upright): 15 / 17 / 30 | grainy orb, ripples, phase arc | 205 x 251 @3x |
| 07 | Leeward, sailing heading and wind | bone #EDE4CC, port red, starboard green | IBM Plex Mono: 14 / 17 / 30 / 40 | compass card larger than the screen | 205 x 251 @3x |
| 08 | Onething, focus timer | monochrome plus pink #FF4F9A | Geist: 15 / 17 / 40 | one ring on a minute-tick track | 205 x 251 @3x |

Directions were written side by side before building. Each has its own hue, family and shape language. The closest pair is 06 and 08 (both a circle in the middle); one is a soft light, the other a hard ring with ticks.

Type follows the watchOS text styles at xLarge, the default for 44/45/49 mm (Apple HIG, Typography): Large Title 40, Title 1 38, Title 2 30, Title 3 20, Headline and Body 17, Caption 1 16, Caption 2 15, Footnote 1 14, Footnote 2 13, minimum 12. Each piece uses three to five sizes, none within 10% of another. Data numerals (pace, BPM, countdown, the face's time) are a deliberate display size above the HIG styles. All text is at least 13 px.

## Honest assessment

- Strongest: 03 (the generated sky looks painted, not templated), 04 (pure signage), 01 and 02 (one loud number each, very legible).
- 07 works as an instrument, but its compass labels run off the display edge on purpose. Some viewers may read that as cropping.
- 05 is clean but closest to a platform default; the lit hero tile carries it.
- 08 is the most conventional idea (a ring timer). The minute-tick track and the restraint save it, but it would not lead a post.
- 04's list rows are 42 px, under the 44 pt touch target, so they are read-only rows here.

## Findings: the engine or skill is wrong or missing something

Most important first.

1. **Watch is not a real platform in the engine.**
   - Evidence, command: `sketch --platforms watch`. The `--help` lists only `web,ios,android,desktop,secondary`, but the value is accepted silently. `decisions.md` D-0006 says "watch is not one of the listed options for Q-plat-01; kept as your own answer".
   - Evidence, answers: `pick Q-plat-02 watch` and `pick Q-plat-04 watch` each print "recorded; the tokens already match this answer". Nothing changes.
   - Evidence, levers: `levers.json` has `platformBase: {"watchos": 16}`, but the engine's platform id is `watch`, so the native body size never applies. Even with a matching id, it applies only when Brand presence is under 50.
   - Evidence, targets: `tokens.css` lines 800-801 hold `@media (pointer: fine) { --ds-size-target-min: 24px }`, so a watch-only system drops its target floor to 24 px under a mouse.
   - What a watch should imply: dark-only, a pure black page, the watchOS text styles, a 44 pt target floor and a corner safe area. Recorded in `01/opendesigner/feedback.md`.
2. **No watchOS type roles, and the dials can push type under the watch floor.**
   - The engine's scale is a modular web scale.
   - Evidence, before any fix: with `--audience large` and Density 45 to 60, the scales for 03, 04 and 07 were 11/14/18/22/27/34. Body was 14, under the watch's 16 to 17.
   - The fix a user can make through the engine: `set raw.baseSize 17`. That gives 14/17/21/27/33/42, and only 14 and 17 land on HIG sizes.
   - Six of eight pieces still needed literal HIG sizes (Title 3 20, Title 2 30, Caption 2 15, Large Title 40). Each one is commented in its page. Recorded in `03/opendesigner/feedback.md`.
3. **Dark-only never shows the exact brand colour.**
   - `brandExact` pins the hex only in the light ramp. The dark ramp lowers chroma by 26/32.
   - Evidence from `tokens.css`: `--ds-color-brand-seed` against `--ds-color-accent-dark-9` reads #c8ff2e against #b0d468 (01), #ff5436 against #e86d55 (02), and #ffcc1a against #e0c16c (04).
   - Every semantic role (`bg-action-primary`, `bg-brand`, `text-accent`) points at the dusty step. Every piece used `--ds-color-brand-seed` directly. Recorded in `01/opendesigner/feedback.md`.
4. **Dark-only is hard to choose and then half-ignored.**
   - Evidence, blocked: `sketch --theme dark-only` stops with "Nothing was written: the theme dark-only breaks a standard" (STD-visual-details-24). Stage 07 itself names dark-only as the option for watch, TV and car. Every watch needed `standard override` first.
   - Evidence, still validated: after dark-only, `validate` still checks light mode. 6 of 8 systems warn "In light mode, action primary background on base surface is too faint" (see each `engine-log.txt`).
   - Evidence, DESIGN.md: the front matter of all 8 lists a light `surface` (#fcfdff and similar). Recorded in `02/opendesigner/feedback.md`.
5. **Colour on black: three ways the generated colours go muddy.**
   - Warmth: Warmth 90 to 95 tints the dark neutrals brown, for example the 05 tile at `neutral-dark-5` #261f1c and secondary text #a29590. That is the owner's "brown-black with orange" case, and nothing warns.
   - Status colours: Colorfulness does not reach them on a near-neutral brand. In 07, raising it from 15 to 45 left `success-dark-11` #6faa7b and `danger-dark-11` #d78a81 unchanged (decisions D-0025 and D-0026).
   - Data scales: the dark ramps give dusty mid-tones, such as `accent2-dark-9` #8c741b and `accent3-dark-9` #a45d9a, so there is no vivid sequential scale for heart-rate zones.
   - Worked around: Warmth lowered to 50 through the engine, and colours derived from tokens with relative oklch. Recorded in the 05 and 07 feedback.
6. **`--delegated all` changed a brand hex I typed.**
   - Evidence: the first sketch of 01 logged "D-0005 raw.brandColor = '#617f00' ... a readable shade of #c8ff2e". It assumed white text on the brand.
   - With the brand not delegated, the same hex was kept exactly with dark text. Recorded in `01/opendesigner/feedback.md`.
7. **Preflight gives a false error and misses token sizes.**
   - False error: `preflight.py html` reports "ERROR font "X" is used but has no @font-face" (M9) on all 8 pages. Each loads its font with a Google Fonts `<link>`, the way the brief allows. A browser check confirmed every font loaded.
   - Blind size check: M8 cannot see sizes that come from the linked `tokens.css` (rem), so it checked only the few px literals.
   - Tracking: M5 warns on -0.045em tracking even on a 68 px numeral, where that is normal.
   - Missing: there is no `--medium watch`. Recorded in `08/opendesigner/feedback.md`.
8. **The review and a house standard contradict each other.**
   - `engine.py review` says "gap: 6px -> use var(--ds-space-6)". In the same output it cites STD-accessibility-motion-13 (must): "Write spacing in rem or em".
   - Every `--ds-space-*` token is itself in px. Recorded in `02/opendesigner/feedback.md`.
9. **Smaller issues**
   - DESIGN.md describes every watch system's audience as "people who use it now and then, often on a phone" (the plain words for `--audience large`).
   - DESIGN.md asks to "confirm the web licence" for Archivo, Bricolage Grotesque, Big Shoulders Display and Fraunces, which are all SIL OFL.
   - The feel words "technical" (modern and serious) and "strong" (bold and authoritative) fight common partners such as "energetic" and "warm". The warnings were clear.

## Findings: places I worked around something (not engine bugs)

- **Mobbin has no watch platform** (only `ios` and `web`). The references are phone workout screens, small widgets (the nearest thing to a complication) and compass and timer screens. The skill could say this for watch, TV and car work. Recorded as an idea in `04/opendesigner/feedback.md`.
- **shot.py cannot clip or make a transparent background.** `render.py` runs `shot.py` and then cuts the 48 px display corners with an anti-aliased alpha mask.
- **The owner's type and colour rules arrived mid-run.** All 8 pieces and the sheet were revised. Details are in each `notes.md` under "Changes for the owner's type and colour rules":
  - one family per piece (08 dropped Geist Mono);
  - italics removed from 06;
  - watchOS roles everywhere;
  - Warmth 90/95 lowered to 50 in 02 and 05;
  - glows and opacity tints that made brown-black removed;
  - port and starboard made vivid;
  - the sheet's italic-serif highlight replaced by a weight highlight in one family (Inter).
- **Spacing tokens:** 36 spacing declarations were moved to `--ds-space-*` after `engine.py review` listed the raw values. Positions such as `top: 146px` and the corner safe-area insets (22 to 28 px) stay raw: they are device layout, not rhythm.

## What helped

- `sketch` gives a complete, valid system in one command. Each full piece setup (sketch, override, 4 picks, faces, base size, 8 dials, build) took a few seconds. `build` alone takes about 0.3 s.
- `standard override` explains itself: it records the person's words and names the restore command.
- `Q-color-21 black` exists and produces a true #000 page. `--ds-color-brand-seed` keeps the exact hex available.
- `decisions.md` made every change traceable. The Colorfulness test in 07 is visible as D-0025 and D-0026.
- `engine.py review` found real raw spacing values quickly.

## Checks (all pieces)

- `engine.py validate`: all 8 pass with no errors. The warnings are the light-mode noise above (6 pieces), feel-word conflicts (02), and none at all (08).
- `preflight.py html`: the only error is the false M9 on every page. M5 tracking warnings appear only on display numerals (01, 02, 03, 07, 08).
- A browser check (Playwright) confirmed every web font loaded and read the rendered sizes listed in the table.
- The same check found no hex or rgb text colour under 4.5:1 against its background.
- Colours written in oklch were checked by hand against black:
  - port red 6.7:1 and starboard green 12.1:1;
  - zones 1 to 5 from 13.8:1 down to 5.1:1;
  - the brand red 6.6:1;
  - black on the amber tile 12.0:1.

Mobbin printed a usage notice on every search ("Your Mobbin AI usage is high this month"; credits used reached 460).
