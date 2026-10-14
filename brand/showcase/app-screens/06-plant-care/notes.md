# 06 · Loam: plant care diary (phone, 390×844 @3x)

## Direction
Loam is a fictional plant care diary for people with a dozen houseplants and no green thumb. The "Today" screen answers one question: who needs water this morning? It has a week of watering, one hero plant with soil moisture and a big log button, and the rest of the day's tasks. The mood is a potting-shed notebook: paper, moss, clay pots and line drawings. Feel words: **gentle, cozy, natural** (the engine knew gentle and cozy; it did not know "natural" and left it out).

## References (Mobbin, structure only)
- [Future Pro, challenge card](https://mobbin.com/screens/609b81b8-53ab-4bac-aa1a-2e7eb1ef7703): a seven-day strip with today filled. It sets the rhythm for the watering week.
- [Insight Timer, streak card](https://mobbin.com/screens/059e3d86-ddb6-498c-b0cc-33afba20b190): checked past days and a quiet serif line. Past days can recede while today leads.
- [Greg, plant detail](https://mobbin.com/screens/caee6c2a-1f6f-48d0-bc7e-ebb9d10c2576): a plant portrait in a frame with one big water action. I used the same idea of one hero plant and one action.
- [Lifesum, diary](https://mobbin.com/screens/7f1180e8-1839-4859-90cc-96b966c08c77): a tab bar floating over content that scrolls under it.

## System (engine)
```
sketch --name "Loam" --brand "#4E6E48" --audience regular --platforms ios --feel gentle,cozy,natural --delegated all
set raw.accentCount 2 · set raw.secondaryColors ["#C0603A"]        terracotta, the clay-pot color
set raw.neutralBase "#E6E0D2"   (first "#E8DCC6"; changed for the owner's color rule, see below)
set raw.textFace Figtree · set raw.displayFace Alegreya   (first Fraunces; changed, see below)
set raw.fontLicence {"web":true,"app":true,"selfHost":true}   both OFL; the engine did not know them
build → Passes: no errors, 0 warnings
```
Dials, all `--set-by delegated`:

| Dial | Value | Why |
|---|---|---|
| expression | 55 | the drawings carry the personality, the chrome stays calm |
| brandPresence | 45 | below 50, so iOS keeps its 17 pt body |
| density | 38 | a slow daily ritual, one task per row |
| energy | 30 | nothing shouts |
| roundness | 82 | leaves, pots and arches (control 16, container 24, overlay 32) |
| depth | 25 | paper-flat, a soft lift on the hero card |
| colorfulness | 45 | moss and clay; the rest is neutral |
| warmth | 82 | (it has no effect once `raw.neutralBase` is set: a finding) |

## Fonts and type scale (two faces)
Alegreya (display, OFL) and Figtree (text, OFL), both from Google Fonts. The scale follows iOS Dynamic Type roles, 6 sizes, none within 10%:

| Role | Size / weight | Used for |
|---|---|---|
| Display | 42 Alegreya 400 | plant name "Monty" |
| Large title | 33 Alegreya 400, phrase in 700 | greeting; soil moisture figure (Figtree 700) |
| Title 3 | 21 Alegreya 700 | wordmark |
| Body / headline | 17 Figtree 400-600 | buttons, plant names, section heads |
| Footnote | 14 Figtree 400-500 | labels, tasks, species names |
| Caption | 12 Figtree 600 | tab labels (below the 14 token step on purpose; iOS uses 10-11 pt here) |

Species names are in Figtree italic, by botanical convention; no headline uses an italic word.

## Art
Three CC0 line drawings from CocoMaterial, found and recolored with **opendesigner-illustrate** (`search`, `rank`, `sheet --candidates`, `fetch`, `recolor --map "#030303=accent-12" --map "#fff=accent-4"`, `apply --as svg --variant themed`). The ledger and `ATTRIBUTION.md` are in `opendesigner/illustrations/` (no credit required). The clay pots are a multiply-blended clip shape laid over each drawing's pot, because the source has one white fill for leaves and pot.

## Where I left the tokens, on purpose
- Arch windows: the top radius is half the width (78 px and 30 px). They are art shapes, not UI radii.
- Paper grain: an SVG noise texture at 50% multiply, decorative.
- Tab labels at 12 px (see the scale).
- The clay pot overlays use `mix-blend-mode: multiply` with hand-measured clip polygons.

## Changes for the owner's type and color rules (mid-run)
- **Italic-word highlight removed.** "thirsty" was Fraunces italic in clay. It is now Alegreya 700 in the same ink as the rest of the line. The hero card stays the focal point.
- **Display face changed** from Fraunces to Alegreya, because piece 03 already uses Fraunces. Alegreya also has the bold weight the highlight needs.
- **Fewer sizes.** The 27 px step is gone; 7 sizes became 6.
- **Calmer neutrals.** The cream base `#E8DCC6` made secondary text brown (`#5f5645`). `#E6E0D2` gives `#5c574c` and a cleaner paper (`#f6f4f0`). Moving the Warmth dial from 82 to 45 changed nothing while `neutralBase` was set.

## Checks
- `engine.py validate`: Passes, no errors, 0 warnings.
- `preflight.py html`: 1 error and 1 warning, both judged not real. M9 "Figtree has no @font-face" is a false positive: the face loads through a Google Fonts `<link>` (the browser reports Figtree and Alegreya `loaded`). M8 flags the 12 px tab labels, which are intended.
- Review probe (`opendesigner-review/scripts/probe.js` + `review.py check`): it caught a real contrast failure, `· 400 ml` at 80% opacity on moss (3.69:1). Fixed. It now reports 0 errors and 1 warning (the arch radii, intended).
- `engine.py review`: 33 "hard-coded values". Most are icon and avatar sizes it maps to spacing tokens. The real spacing values were moved to `--ds-space-*`.

## Process findings
- **Helped:** `sketch` gave a working, contrast-checked system in seconds. `secondaryColors` produced a proper clay ramp. The illustrate pipeline (search, sheet, fetch, recolor with `--map`, themed apply) worked end to end, and its `:where()` classes made the art easy to restyle.
- **Bug:** each `illustrate.py search` overwrites `candidates.json`, so the first query's results are lost. I had to back up and restore the file to fetch them. Commons matched "monstera" to Mönsterås municipal arms. (feedback recorded)
- **Idea:** recolor cannot split one fill into two regions (leaves and pot). (feedback recorded)
- **Gap:** the Warmth dial does nothing once `raw.neutralBase` is set, and nothing says so.
- **Bug:** `preflight.py html` misses Google Fonts links and rem sizes. (feedback recorded)
