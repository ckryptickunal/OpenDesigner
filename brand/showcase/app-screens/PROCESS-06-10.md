# App screens 06–10: process report

Five app screens, each made through OpenDesigner end to end. For each one I ran Mobbin references, then `engine.py sketch`, dials and answers, `build`, then the build, the render, `validate`, `preflight` and the review probe, then notes. A second builder made 01–05 at the same time. After the owner's mid-run type and color rules, I revisited all five screens; each `notes.md` has a section on what changed.

## Directions side by side (written before building, adjusted after checking 01–05)

| | 06 Loam | 07 Parlo | 08 Undertow | 09 Quarry | 10 Vigil |
|---|---|---|---|---|---|
| Domain | plant care diary | Italian lesson | podcast now playing | project workspace | ward vitals |
| Device | phone 390×844 @3x | phone 390×844 @3x | phone 390×844 @3x, dark | desktop 1440×900 @2x | tablet 1180×820 @2x |
| Palette | moss `#4E6E48`, clay `#B85B36`, warm paper | cobalt `#2A5BD7`, sunflower, tomato on white | night navy, ice blue `#A9C4FF`, ultramarine duotone | cool greys plus vermilion `#D93900` | cool greys, teal `#0B7A84`, status colors |
| Type | Alegreya + Figtree | Fredoka + Nunito | Newsreader (light) + Hanken Grotesk | Geist + Geist Mono | Atkinson Hyperlegible Next + Mono |
| Shape | arches, pills, radius 16–32 | chunky tiles, ink outlines, hard offset shadow | radius 0, hairlines | radius 4–8, hairlines | radius 6–12, flat tiles |
| Imagery | CC0 line plants recolored (opendesigner-illustrate) | mascot drawn in SVG | generated contour-map canvas | none (data) | live SVG traces |
| Mood | gentle, cozy | playful, bold | moody, editorial | focused, calm | trustworthy, clear |

Collisions with 01–05 that I fixed: 08 used Instrument Serif with peach on dark indigo, like 02, so it moved to Newsreader with navy and ice. 06 used Fraunces, like 03, so it moved to Alegreya. 09's workspace was called "Halden", like 01, so it became Kestrel. One remains: 07's cobalt is close to 05's blue, though the mood, type and shape are far apart.

## Pieces

| Piece | Shot | Verdict |
|---|---|---|
| 06 plant care | `06-plant-care/shot.png` | Strong. The line drawings with clay "printed" pots give it its own voice. |
| 07 language lesson | `07-language-lesson/shot.png` | Strong. Toy-like and clearly its own product, not a copy of the reference app. |
| 08 podcast player | `08-podcast-player/shot.png` | Strongest. The generated night map and the light serif title. |
| 09 project workspace | `09-project-workspace/shot.png` | Polished but the least distinctive. It reads as a well-made member of a familiar genre; the diamond status icons and the single accent are its only marks. |
| 10 clinical vitals | `10-clinical-vitals/shot.png` | Clear and safe. Plain by design; its strength is the status language, not beauty. |

## Process findings, most important first

### The engine or a skill is wrong or missing something

1. **`sketch --delegated all` silently rewrites an explicit brand color.** The brief's recipe passes `--delegated all`, and the sketch then treats `--brand` as "picked for them" and darkens it until white text passes (`engine.py` cmd_sketch, the `readable_shade` branch). Apricot `#E8946A` became brown `#AF6037` in `08-podcast-player/opendesigner/state.json`, and vermilion `#F04A1A` became `#D93900`. Apricot was meant to carry dark text on a dark player, so the brand's character was lost and nothing was flagged. Fix used: `set raw.brandColor '"#E8946A"' --set-by chosen`. Pieces 01, 02 and 04 hit the same problem ("restored" in their notes).
2. **`preflight.py html` cannot see a token-based page.** It reads only px font sizes and local `@font-face`. On these pages it printed `font sizes in px: []`, so no small-text check ran (07, 08, 09, 10), and it raised M9 errors for every face loaded through the Google Fonts `<link>` the brief allows (06, 10). The review probe (`opendesigner-review/scripts/probe.js` + `review.py check`) was what found the real problems: 4 real contrast failures (06 `· 400 ml`, 09 key cap, weekend labels, breadcrumb slash), 9–10 px text, heading skips and an endless animation. It also reported 2 contrast misreads (finding 11).
3. **The neo-brutalist style does nothing.** `pick Q-dir-01 neo-brutalist` answers "tokens already match". The preset's `extra` (`offsetShadow: "4px solid"`, `borderWidth: "thick"` in `levers.json`) is never read by `engine.py` (no `offsetShadow` anywhere), and its dials are ignored once dials are set by hand. The hard shadow in 07 is hand-written.
4. **iOS type depends on Brand presence.** With `brandPresence` 85, iOS body text became 14 px and labels 11 px (07, before the fix). The native 17 pt base is kept only below 50. `Q-scope-06 experience` reached only 16/12, so I set `raw.baseSize 17` by hand. 08 had the same problem.
5. **The font list and weights are thin.** `OPEN_FONTS` does not include Fraunces, Fredoka, Instrument Serif, Newsreader, Alegreya or Atkinson Hyperlegible Next and Mono (all OFL). Validate warns "no recorded app licence" until `raw.fontLicence` is set by hand. The engine also assigns weights the face lacks: Fredoka (max 700) gets 750 and 850; Instrument Serif (400 only) gets 650 and 750. Nothing lets you ask for light display titles; weight comes only from Energy.
6. **Color inputs that cannot reach the result.** (a) Status colors cannot be pinned and barely follow Colorfulness: danger stays a muted `#be544b` at 35 and 55 (10). (b) Yellow light steps are beige (`#f3ebd9` to `#e3c68a`, 07). (c) Warmth does nothing once `neutralBase` is set: identical ramps at 82, 60 and 45 (06). A warm base also makes secondary text brown, which the owner's rule forbids. (d) A navy `neutralBase` gives a near-grey dark ramp (`#131519`, 08).
7. **The macro-conflict warning persists** after the conflicting dial is set explicitly (10 validate: "serious, minimal, everyday pull colorfulness in opposite directions" with colorfulness set to 35).
8. **`light-only` and `dark-only` are refused** by STD-visual-details-24 with no next step (08). Keeping both modes was fine, but the refusal should say "keep both, set the default theme to dark".
9. **opendesigner-illustrate:** each `search` overwrites `candidates.json`, so the first query's candidates are gone and `fetch` fails for them. Commons matched "monstera" to Mönsterås municipal arms. Recolor cannot split one fill into two regions (leaves and pot), so the clay pots in 06 are a CSS multiply clip.
10. **`engine.py review` is noisy on real UI.** It reported 78 hits on 09 and 33 on 06, mostly icon and avatar sizes mapped to spacing tokens and 1 px inset rings called "shadows". Real spacing literals were a minority (fixed).
11. **The review probe misreads stacked backgrounds.** It measures contrast against the nearest ancestor, so white text over a sibling progress fill or an SVG shape scored 1.29:1 and 1:1. Both were readable; I changed the markup so the check could see the real background.

### Worked around, and nothing in OpenDesigner needs changing
- Mobbin has no clinical software (10); references came from health trackers and monitoring tools, and the NEWS2 structure is my own knowledge (flagged in notes).
- The brief's render line says `--scale 2`; phones were rendered at `--scale 3`, as asked for this category.
- My own class clash (`.pri`) shrank 09's primary button. The probe did not see it; only looking at the render did. This is the reason to keep "look at every render at full size" in the brief.

### What helped
- `sketch` plus dials gave a complete, contrast-checked token set in seconds, and the dials visibly changed shape (radius 0 in 08, chunky radii in 07, compact 12/14 type in 09).
- `secondaryColors`, `neutralTint`, `chartPalette` and `Q-scope-06` did what they say.
- The illustrate pipeline (search, sheet, fetch, recolor with `--map`, themed apply with `:where()` classes and a licence ledger) was the smoothest part of the process.
- The review probe with `review.py check` was the most useful check. It caught real contrast, size, heading and motion problems with exact elements.

All feedback was recorded locally with `engine.py feedback` in each piece's `opendesigner/feedback.md`; nothing was posted.
