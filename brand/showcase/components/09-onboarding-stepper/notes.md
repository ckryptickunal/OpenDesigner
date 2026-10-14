# 09 · Onboarding stepper · Mossby

## Direction
Mossby is a fictional plant-care app for first-time plant owners, many of whom have already killed a plant and feel a bit guilty about it. Onboarding has four short steps (your space, your plants, your rhythm, all set) and should feel like a friendly storybook: pastel sage, peach, lilac and butter; ink-line plant drawings on soft blobs; a progress line that is a growing vine and sprouts a leaf for each finished step; very round cards and pill buttons; a guilt-free "I'm not sure yet" on every question.
Feel words: **friendly, cheerful, gentle** (all three known: friendly; playful + friendly; friendly + deferential).

## References (Mobbin, cited by link only)
- Monzo home type question, https://mobbin.com/screens/1515fc78-f9a2-4d80-a446-dc3567901f5c : illustrated choice cards with an "I'm not sure" escape hatch in the corner. Taught me the escape hatch and illustrated options.
- Fiverr freelancer type, https://mobbin.com/screens/f052d523-3364-4a0a-a51f-19d832b87cfd : ink line drawings over a single colour blob in a card grid. Taught me the line-art-on-blob technique.
- Insight Timer goal step, https://mobbin.com/screens/580ddba5-e7ec-4532-8c2e-fa6077a2f2a5 : segmented progress bar at the top and calm option rows. Taught me the compact phone progress pattern.
- Public risk step, https://mobbin.com/screens/9be926dd-7e14-4401-84cd-522daa8ab6f3 : "Step 4 of 6" overline above the question, radio cards with a sub-line. Taught me the step overline and option anatomy.

## System (engine)
`sketch --name "Mossby" --brand "#5fae7d" --audience regular --platforms web,ios --feel friendly,cheerful,gentle --theme system-light-dark --delegated all --surfaces experience`, then `set raw.accentCount 3`, `set raw.secondaryColors ["#f08a63", "#9b7be8"]` (peach, lilac).

| Dial | Value | Why |
|---|---|---|
| expression | 66 | illustrated, a little storybook |
| brandPresence | 70 | sage, pastels and the rounded face carry it |
| density | 25 | one question per screen; controls 40/48/56 |
| energy | 55 | gentle lift on hover, calm otherwise |
| roundness | 95 | controls full pill, containers 20, overlays 28 |
| depth | 35 | soft raised / floating only |
| colorfulness | 62 | pastel family |
| warmth | 85 | warm neutrals, caring |

Typefaces: `raw.displayFace "Fredoka"` (rounded display), `raw.textFace "Nunito"` (rounded humanist text), SIL OFL, licence recorded.

Illustrations through **opendesigner-illustrate**: `search "potted house plant" --slot onboarding` (82 candidates), `rank --style flat`, `sheet --candidates`, `fetch` four CC0 CocoMaterial drawings, `recolor --variants themed,tint --tokens ...`, `apply --to art --as svg --variant themed`, `ledger` (ATTRIBUTION.md in opendesigner/illustrations/). The page inlines the four SVGs (built from a template so the SVG markup stays out of the source by hand) and sets `--od-illus-neutral-1` per card to a pastel ramp step, so each drawing's fills take its card's colour.

## Where I stepped outside the tokens, and why
- Pastel fills are ramp steps 3–4 of accent, accent2, accent3 and warning (butter). The semantic roles only expose `bg.*-subtle` (step 3) for accent and status; there is no role for "decorative pastel", so I used ramps on purpose and named them `--sage/--peach/--lilac/--butter`.
- The phone frame bezel is neutral 12 at 6px and 36px radius (a device, not UI).
- Vine leaves use accent step 8; the dashed upcoming vine uses border.subtle.
- Continue's count bubble is 22% white on the action fill.

## Checks
- `engine.py validate`: no errors, 0 warnings, 5 notes.
- `preflight.py html --medium web`: 0 errors, 0 warnings — but only because it can read nothing: every size is a rem token and every family comes through `var()`, so it extracted no sizes and no families (see findings).
- `illustrate.py check art/plant-3.svg`: warn, one leftover #000000 not in the palette (invisible here; the path is covered).
- Contrast: body and option text use text.primary / text.secondary roles (engine-checked). Warning message text on warning subtle is the engine's checked pair. The disabled Continue is exempt. Step states never rely on colour alone: check, number, "!" and arrow glyphs plus labels.
- Targets: picks are 150×262 buttons, options 52px tall, pills 40–56px: all over 44px.
- Interaction: plant cards are `role="checkbox"` buttons (click, Space, Enter) and update the Continue count; Continue is `aria-disabled` at zero and shows a saving spinner; phone options are a radiogroup; the finished step is a link back; `aria-current="step"` on the current step. Reduced motion stops the spinner and leaf drift and zeroes transitions.

## Rounds
1. Card blobs were clipped into octagons by the pot's overflow; the first step label sat 3px higher than the others because only it was a link with padding.
2. Freed the blob, aligned the labels. Looked again at full size: the composition holds; the hovered Snake plant reads as lifted.

## Process findings
1. **The illustrate skill worked end to end and the result is good**, but its `--dir` means something different from the engine's `--dir`; using the same folder dumped search files into opendesigner/ and made `palette` lose the tokens. (feedback: confusing)
2. **Search and rank quality**: "house" matched birdhouses and houses for sale; `--style flat` still ranked heavy line doodles; `fetch` exited 1 on success; `apply --label` left rows unassigned. (feedback: bug)
3. **Recolor for pastel line art**: mono drawings map to neutral 1 and 12 only. Overriding the CSS variable per card was easy and is the strongest part of the skill's output. (feedback: idea)
4. **Preflight passes a fully tokenised page by default**, because it reads only px sizes and literal families. (feedback: bug)
5. **Secondary accents**: three-accent harmony gave grey teal and khaki at 24/36 of the primary chroma; `raw.secondaryColors` fixed it, but no question asks for named secondary colours. (feedback: gap)
6. Helped: roundness 95 gave pill controls and 20/28 containers that matched the direction exactly; density 25 gave 40/48/56 controls; Fredoka/Nunito went in through `raw.*Face` with no friction.

## Owner type and color rules (checked after the rule arrived)
- **Two fonts:** Fredoka (display: questions, step numbers, card names) and Nunito (everything else). Already compliant.
- **Type scale (6 sizes):** caption 13 (step labels, card hints, error text), body 16 (buttons, options), body-large 20 (lede, card names), title 25 (phone question, "Your jungle is set"), headline 39 (sheet number), display 49 (the step question). Adjacent steps are at least 20% apart.
- **Weight:** the question is Fredoka 600, chosen because the rounded face looks thin and timid at 400 on pastel; card names 600, body 400-700 Nunito.
- **No highlight trick** in any heading. **Color:** light warm-white background with near-black text and pastel fills; Warmth 85 tinted the neutrals slightly pink-cream, not brown, so no change.
