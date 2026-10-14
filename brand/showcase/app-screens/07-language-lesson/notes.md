# 07 · Parlo: Italian lesson (phone, 390×844 @3x)

## Direction
Parlo is a fictional language app that teaches Italian in five-minute lessons. The screen is a "translate this sentence" exercise just after a correct answer: tiles placed, the result sheet up, and the mascot Moka (an enamel coffee pot drawn in SVG) saying the sentence. It should feel like a toy: thick ink outlines, hard bottom edges that read as pressable, and bright primaries (cobalt, sunflower, tomato) on white. Feel words: **playful, bold, cheerful**.

## References (Mobbin, structure only)
- [Duolingo, translate exercise](https://mobbin.com/screens/bb075437-bdb1-4c18-ab7b-fdeb460bf3dd): the order of the exercise, from prompt to character and bubble, answer lines, word bank and a bottom action.
- [Duolingo, early lesson](https://mobbin.com/screens/c1d0e1c6-2633-4424-ab10-d5b18f197cc5): used tiles leave empty slots in the bank, so the bank never reflows.
- [LinkedIn games, Wend](https://mobbin.com/screens/9875e8a8-8b78-409d-9c6e-d6e97571748a): hard-edged tiles and a hint banner on a tile grid.
- [Chick-fil-A, game](https://mobbin.com/screens/0520584e-bb07-4c66-ac6c-d232a0c87f74): thick ink line work with flat primaries, which became the mascot style.

I kept the identity apart from the obvious reference: no green, no owl, an ink-outline style and a coffee-pot mascot.

## System (engine)
```
sketch --name "Parlo" --brand "#2A5BD7" --audience regular --platforms ios --feel playful,bold,cheerful --delegated all
set raw.accentCount 3 · set raw.secondaryColors ["#FFC531", "#F2493B"]   sunflower and tomato
set raw.textFace Nunito · set raw.displayFace Fredoka · set raw.fontLicence {...}   both OFL
pick Q-scope-06 experience            (body went 14 → 16)
set raw.baseSize 17                   (body 17, labels 13: iOS sizes; see findings)
pick Q-dir-01 neo-brutalist           (changed nothing; see findings)
build → Passes: no errors, 0 warnings
```
| Dial | Value | Why |
|---|---|---|
| expression | 90 | a game-like lesson |
| brandPresence | 85 | the lesson is the brand moment |
| density | 40 | one exercise per screen, big tiles |
| energy | 85 | snappy feedback (heading weight 750, display 850) |
| roundness | 75 | toy corners (control 12, container 16, overlay 24) |
| depth | 60 | pressable tiles |
| colorfulness | 95 | primaries |
| warmth | 60 | warm white under the primaries |

## Fonts and type scale (two faces)
Fredoka (display, OFL) and Nunito (text, OFL). The iOS Dynamic Type roles from the engine's scale (13, 17, 23, 30) use 4 sizes, none within 10%:

| Role | Size / weight | Used for |
|---|---|---|
| Title 1 | 30 Fredoka 600-700 | "Translate this sentence", "Perfetto!" |
| Title 2 | 23 Fredoka 600 | the Italian sentence, the Continue button |
| Body | 17 Nunito 600-800 | tiles, explanation, tooltip |
| Footnote | 13 Nunito 800-900 | eyebrow chip, XP chip, gender hint |

Fredoka stops at 700, but the engine asks for 750 (heading) and 850 (display). I set weights by hand, up to 700.

## Highlight and color
- The new word "cornetto" is marked with a **sunflower fill box**, and the matching answer tile is sunflower too. No italics anywhere.
- White page, cobalt ink outlines (`accent-12`), one sunflower sheet, a tomato mascot and chip. The text is strong ink on white or on sunflower (`text-on-accent2`).

## Where I left the tokens, on purpose
- **The hard offset shadow** (`0 4px 0 ink` and `0 3px 0 ink`) and the 2 px ink outlines. The engine's neo-brutalist preset promises "4px solid offset shadow, thick borders" but emits neither.
- The mascot, confetti and dot grid are SVG and CSS art. Their colors come from tokens.
- A −10 px margin on the close button aligns its 44 pt hit area optically.

## Changes for the owner's type and color rules
None were needed. It already used two faces, a fill-box highlight and 4 sizes. I wrote the scale down here and kept the yellow highlight at step 9, because the lighter yellow steps are beige.

## Checks
- `engine.py validate`: Passes, 0 warnings.
- `preflight.py html`: 0 errors and 0 warnings. That is because it saw no sizes at all ("font sizes in px: []"): every size is a rem token, so its type checks did not run.
- Review probe: 0 errors and 0 warnings. Info only: weight 800 is outside the system's weights, and 3 px gaps.

## Process findings
- **Bug:** `pick Q-dir-01 neo-brutalist` reports "tokens already match". The preset's `extra` (offset shadow, thick borders) is never read by the engine, and its dials are ignored because the dials were set explicitly. (feedback recorded)
- **Gap:** with Brand presence above 50 on iOS, body text drops from 17 pt to 14 px and labels to 11 px. The surface mode only reaches 16/12; I had to set `raw.baseSize 17`. (feedback recorded)
- **Gap:** the light steps of a yellow accent are beige (`#f3ebd9` … `#e3c68a`). (feedback recorded)
- **Gap:** the engine sets weights the face does not have (Fredoka 750 and 850). (feedback recorded)
- **Note:** piece 05 (travel) also leads with a blue near `#2A5BD7`. This piece differs in mood, type and shape, but the hue is close.
