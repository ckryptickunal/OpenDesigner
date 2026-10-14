# 03 · Larder: recipe detail

## Direction
Larder is a fictional cooking quarterly turned into an app: recipes read like a magazine spread, with one big plate image, a strong serif headline, and the practical parts (ingredient checklist, step timer) set like good print furniture. Warm off-white paper, ink, tomato red, an olive check. Feel words: **warm, editorial, rich** ("editorial" is not in the engine's feel list).

Shape language: printed rules (a 2 px + 1 px double rule, hairline table rules), 2 px corners, round checkboxes, one red "ticket" pinned at the bottom. Type: Fraunces (display) and Libre Franklin (text). Two fonts.

## References (Mobbin, structure only)
- https://mobbin.com/screens/ad8755f7-d3fe-42c4-a57c-dd23175e6635 (a recipe app): serif title, then a row of four facts (skill, time, ingredients, calories), then ingredients. Taught the order and the fact row.
- https://mobbin.com/screens/0555a2ce-5562-4509-b1f2-c8cc33adb9ac (a fitness app's recipe): quantity first, the ingredient, then a prep note, with hairline rows. Taught the ingredient line.
- https://mobbin.com/screens/6a2dec2a-8492-4e64-bcda-12ac62d57c30 (a recipe app): the servings stepper sitting on the ingredients header line.
- https://mobbin.com/screens/85a4ace6-390e-40b5-a231-14f134af1752 (a recipe app, cooking mode): a running step timer that stays on screen while you read. Taught the pinned timer.

## System (engine)
```
sketch --name "Larder" --brand "#C8401F" --audience regular --platforms ios --feel warm,editorial,rich --theme system-light-dark --delegated all
pick Q-color-01 keep-hex · pick Q-color-09 warm · pick Q-color-14 alternating · set raw.neutralBase "#958A78" (first "#8B6B3D", see revision)
pick Q-color-04 three · set raw.secondaryColors ["#5F6B2E", "#E2B44C"]
pick Q-depth-01 borders
pick Q-type-01 brand-display · raw.displayFace "Fraunces" · raw.textFace "Libre Franklin" · pick Q-type-02 yes · pick Q-type-08 17
set overrides.type.displayReach 3.2 · HIG type scale (Q-type-10 named, Q-type-09 hand-tuned, font.size steps, text-style overrides)
```
Dials: expression 70, brandPresence 75, density 45, energy 35, roundness 20 (2 px controls, 8 px containers), colorfulness 65, warmth 55 (was 85, see revision); depth 8 from Q-depth-01 `borders`.

The brand red was kept by the sketch this time: it already carries white text (4.99:1). Rendered in the light mapping.

## Type scale (Apple HIG roles)
| Role | Size / line | Used for |
|---|---|---|
| Large Title | 34 / 37, Fraunces 350 with the phrase at 650 | the recipe title |
| Title 1 | 28, Fraunces 500 | the step timer's clock |
| Title 2 | 22 / 28, Fraunces 600-700 | masthead "Larder", "Ingredients" |
| Body | 17 / 22 | ingredient rows, fact values, the step instruction, status bar |
| Footnote | 13 / 18 | folio, kicker, fact labels, caption, stepper, step label |

Five sizes, nothing under 13.

## Image
Photograph by Kerri Leung on Unsplash (`images.unsplash.com/photo-1715216553304-4960f95dfff2`, hotlinked and cropped with Unsplash's own crop parameters to the pot; free Unsplash licence, not an Unsplash+ image). Credited in the figure caption.

The first version used a still I painted in canvas 2D from `paint.py brief --slot hero` (watercolour recommended, nine palette families from the tokens). The paint skill's own engine needs an npm project and a Chromium download, which needs the person's yes, so I did not run it. That version is kept as `shot-painted-v1.png`. The photograph replaced it when the owner allowed Unsplash: it is more appetising, and the recipe was renamed to match what is in the pot.

## Where I went outside the tokens, and why
- Fraunces axes (`opsz`, `SOFT`, `WONK`) are set per element; the tokens have no place for variable-font axes.
- The pause button is white with a red icon on the red ticket (`--ds-color-white` and `text.accent`); there is no "on-accent secondary button" role.

## Revision for the owner's type and color rules (mid-run)
- **Headline:** it was "Burnt tomatoes *&* butter beans" with an italic red ampersand, the trick the rule forbids. Now "**Burnt tomatoes** and butter beans": the phrase in bold, the rest light, at Large Title 34 instead of 40. The photo above is the heaviest thing on screen, so the title stays dark and calm and the only other strong color is the timer at the bottom.
- **Color:** Warmth 85 with a brown neutral base made secondary text brown (#67543b) and the timer a brown-black (#272420) with salmon and red-orange on it. Now Warmth 55 and a greyer base (#958A78): paper #f7f4ee, ink #262420, secondary #5f5647 (6.58:1). The timer is tomato red with white text (4.99:1) and a white pause button.
- **Italics:** the masthead "no. 14", "Ingredients" and the ingredient notes were italic serif; now roman ("No. 14" in small Fraunces capitals, "Ingredients" in Fraunces 600, notes in the text face in secondary color). Only the figure caption stays italic.
- **Two fonts:** the status bar used the system font; it now uses Libre Franklin.
- Sizes 23, 30 and 40 became 22, 28 and 34.

## Checks
- `engine.py validate`: 0 errors, 1 warning ("12 text sizes", the formula steps that cannot be removed after hand-tuning).
- `engine.py review`: 10 findings, all element sizes plus the ticket shadow.
- `preflight.py html --medium web`: 1 error, "Fraunces has no @font-face" (Google Fonts `<link>`; Libre Franklin, loaded the same way, is not flagged). No text under 12 px, no tracking or `<br>` warnings.
- Contrast (computed): ink on paper 14.11:1; secondary 6.58:1; tertiary (struck-through) #6d6352 5.38:1; white on the red ticket 4.99:1.
- Targets: nav buttons 44; checkboxes 24 with a 44 hit area; stepper buttons 40 × 44 hit; pause 44.
- Full-size rounds: three on the painted version (clip-art beans, a disconnected spoon, a cut-off timer line, a rotated icon), then two after the rules (the photo crop and the final type).

## Process findings
1. **Gap: "editorial" is not a feel word.**
2. **Bug: secondary colors are not kept exact** under keep-hex: olive `#5F6B2E` became `#6c7d00`, much more acid, because the ramp peak takes the dial's chroma when it is higher.
3. **Gap: the paint skill has no in-app imagery slot and no still-only path.** Every slot is a 16:9 film size and painting needs an npm project.
4. **Gap: warm neutrals turn brown with no warning.** The neutral chroma curve is highest at the text steps and lowest at the paper steps, the opposite of "cream paper, neutral ink".
5. **Helped:** Q-color-14 `alternating` with a warm neutral base gave a real paper page with white cards; the paint brief's palette families were a ready list of in-system pigments.
