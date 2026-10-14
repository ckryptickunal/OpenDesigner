# 05 Maison Auberval: luxury maison hero

## Direction
Maison Auberval is a fictional Paris fashion house. Its audience reads fashion as culture and expects the site to behave like a printed lookbook: very little on the page, all of it exact. The hero is mostly empty ivory paper with tiny tracked caps, a hairline didone headline, and a tall plate of painted black silk cropped off-centre and bleeding off the top edge. The second line of the headline runs onto the plate, and where it crosses, it turns ivory. Feel words: **luxurious, timeless, understated**.

## References (Mobbin, structure only)
- In Common With: https://mobbin.com/sites/sections/a87f2a50-8a78-4193-b491-5589059041fa . Teaches scale contrast: one image owns the frame and the type is tiny, placed in its quiet corners.
- Face Formula: https://mobbin.com/sites/sections/b266b4bd-2c02-4ac4-afb3-9b9efea2c39d . Teaches the split: a wordmark that runs across two different grounds and stays one word.
- SSENSE editorial: https://mobbin.com/sites/sections/4de98a06-dbff-4e54-83c6-a301c519bba0 . Teaches the pairing of plain uppercase sans with a large serif line.
- Studio Freight: https://mobbin.com/sites/sections/c88d7a4b-61f2-4217-8818-80213f9cd809 . Teaches how much empty page a confident layout can leave, with labels pinned to the edges.

## System (engine)
```
sketch --name "Maison Auberval" --brand "#3A2418" --audience regular --platforms web --feel luxurious,timeless,understated --delegated all --surfaces persuade
   (here --delegated kept the espresso: white text already passes on it)
set raw.displayFace "Bodoni Moda"   set raw.textFace "Jost"   set raw.fontLicence {web, app, selfHost}
set raw.neutralBase "#EFE6D6"      (ivory paper)
set type.headingWeight 400          set type.displayReach 9.5
```
| Dial | Value | Why |
|---|---|---|
| roundness | 0 | couture is cut square: hairlines only |
| depth | 5 | no shadows |
| colorfulness | 8 | ivory and near-black |
| warmth | 72 | ivory, never white |
| energy | 10 | slow, hushed |
| expression | 85 | editorial, image-led |
| density | 30 | first 5, which raised body text to 19 px and labels to 14 px (see findings); 30 gives 16 / 12 |

Fonts (two): Bodoni Moda (SIL OFL, optical size 96 for hairlines) and Jost (SIL OFL), Google Fonts link.

## Type scale (named roles, 4 sizes)
| Role | Size | Face, weight | Use |
|---|---|---|---|
| Display | 160 px (`--ds-font-size-160`) | Bodoni Moda 400 | the headline, two roman lines |
| Title | 28 px (`--ds-font-size-28`) | Bodoni Moda 400 | wordmark, chapter title |
| Body | 16 px (`--ds-font-size-16`) | Jost 300; Bodoni italic for the plate caption and index numerals | intro copy, caption |
| Label | 12 px (`--ds-font-size-12`) | Jost 400, caps, +0.24em | nav, season, index, footer |

## Changes for the owner's type and colour rules (mid-run)
- The headline's second line was italic Bodoni; it is now roman, so nothing is highlighted by italics. The emphasis comes from where the line goes: it crosses the plate and turns ivory.
- The chapter title was italic; now roman.
- The plate was espresso, camel and ivory: ivory type over brown. It is now black silk, painted only from the system's ink (neutral 12), black and ivory, so the crossing reads as ivory on near-black. Measured under the crossing letters: 7.5:1 at the 95th percentile of background lightness, 16:1 median.
- The brand espresso now appears only in hover states; the page is ivory and ink.

## Art
The plate is painted in canvas by code: a height field of folds that converge on one pin above the crop, a second set of arcs where the cloth turns, satin lighting (diffuse plus two sheen lobes), a soft "settling" blur and faint brush variation. Colours come from three tokens, mixed in OKLab. Seeded, so every render is the same. First version looked like a metal sunburst (too many thin folds, a pinstripe grain); the second like a pleated curtain; the third softens it into a painted study.

## Outside the tokens, on purpose
- Plate position and size (868 px, 296 x 792 px) and the headline indent (2 x space-96 + space-40): composition, not spacing.
- Ground is `surface.sunken` (neutral step 2) for ivory; the base surface is near-white.
- Wordmark tracking 0.42em and caps tracking 0.24em; headline tracking is the system's -0.02em.

## Checks
- `engine.py validate`: passes, 0 warnings. `engine.py review`: first run found 96 px, 232 px and a `transition: width`; now "the code uses the tokens" (the link line grows with `transform: scaleX`).
- `preflight.py html`: 2 errors, both M9 false positives (Google Fonts). No size warnings, but only because it cannot read rem token sizes.
- Contrast (computed): body #5d564a on #f6f4ef 6.6:1; labels and headline #262420 on #f6f4ef 14.1:1; ivory on the plate 7.5:1 or more. Targets: nav and links 24 px or more. Dark mode renders correctly (ink ground, ivory type; checked).

## Process findings (piece 05)
1. **Gap:** a very dark brand seed makes a colourless accent ramp (steps 1-8 are greys).
2. **Confusing:** the Density dial changes text size, so "lots of whitespace" made the type bigger.
3. **Gap:** nothing warns that high Warmth plus a warm brand makes a brown-black dark mode with orange (seen in piece 03).
4. **Helped:** `type.headingWeight 400` and `displayReach` gave a 160 px regular display step straight from the engine; two tokens (ink and ivory) were enough to paint the plate.
