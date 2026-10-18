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

## Round 4 (owner review, 2026-10-15)
**What he said:** on 2026-10-14 this screen was "good to go"; on 2026-10-15 he said all the app screens "look absolutely shit. None of them should feel like they are from a vibe coded app or a cheap Chinese app." `AUDIT-ROUND4.md` found it was Duolingo's structure tile for tile (mascot, word tiles, hearts, a "Perfetto!" sheet, +15 XP), and a blind judge named Duolingo at once.

**The idea in one sentence:** after the learner says a sentence aloud, the app shows the one word to fix and exactly what went wrong with it.

**What changed (a new exercise for the same product and the same sentence; structure only from shipped apps, no identity):**
- **A speaking exercise, after the attempt.** The prompt is "I'd like a coffee and a cornetto, please." The screen shows what was said, "Vorrei un caffè e un cornetto, per favore." (Spectral 22), with the one word to practise underlined, playback of the learner's take (3.4 s) and the native speaker's (2.6 s), "7 of 8 words clear · 1 to practise", and the fix, led by *caffè* at 34 pt: *caffè* /kafˈfɛ/ is stressed on the last syllable (the grave accent marks it), and the learner leaned on the first, as in English "coffee".
- **The object only this product has:** a loudness envelope of both recordings across the word, on one baseline, with each speaker's loudest moment marked: the learner's line is ink and peaks on *caf* (the vermilion dot) with a short f; the native speaker's line is grey and peaks on *fè* after a long double f.
- **Removed, so nothing names Duolingo:** the coffee-pot mascot, the word bank and tiles, hearts, XP, the result sheet, confetti, the dot grid, green, outlines and hard shadows. What is left is generic lesson structure: a close button, a progress bar and two actions.
- **One accent with one job, what to fix:** vermilion `#CC3B22` (4.98:1 on white) only under *caffè* and on the learner's peak. The primary button is ink, the secondary grey; playback is plain text buttons with a play glyph.
- **Type:** the Italian is set in Spectral (OFL) like a book; the interface is IBM Plex Sans (OFL), chosen because its capital I has serifs and its l a tail, so the lesson name "Al bar" could not read as "AI bar" (Plus Jakarta Sans and Inter could not); the lesson line was later cut to one prompt line. No-break spaces keep "un cornetto" and "per favore" together.
- **System through the engine:** `raw.textFace "IBM Plex Sans"` (Plus Jakarta Sans, then Inter, were tried), `raw.displayFace "Spectral"`, brand `#CC3B22`, `raw.accentCount 1`, `raw.secondaryColors []` (sunflower and tomato removed), `raw.neutralBase "#8A8F98"`, dials expression 40, brandPresence 40, energy 35, roundness 55, depth 15, colorfulness 30, warmth 35, density 45, `overrides.font.size` 11, 13, 15, 17, 22, 30, 34 and 48 (30 and 48 are no longer used); `build` passes. The cobalt close to Aerlo's blue (`app-screens/05`) is gone.
- **Tried and dropped:** syllable bar charts in cards (boxes inside boxes), stress marks over syllables, and a big "7/8" with an eight-segment meter (an auditor called it a repeated recipe).
- Status bar 07:48; exercise 6 of 10 (the bar is at 60%).

**Type roles (iOS):** Large Title 34 (*caffè*, Spectral) · Title 2 22 (the Italian sentence, Spectral) · Body 17 (the prompt, the score, the explanation, the IPA, the syllables, the buttons) · Subheadline 15 (playback) · Footnote 13 ("6 of 10", chart labels).

**References this round (Mobbin, structure only):** Speak https://mobbin.com/screens/3e01c79e-3175-4df8-9fc6-91966389ffb3 (a speaking prompt with a listen control and a record action), Duolingo https://mobbin.com/screens/35a6f682-bab6-4fc2-be70-b5fa58792795 (feedback that names one takeaway and then continues), Babbel https://mobbin.com/screens/3c8dc043-64d5-4ef3-b70c-5339053595a0 (correct and incorrect items with playback; also what to avoid: a three-line cheer and empty beige cards).

**Where I left the tokens, on purpose:** the iOS chrome, the 6 pt progress track, the close glyph's 4 pt inset that puts its ink on the text edge, and the envelope paths (data).

**Checks:** `engine.py build` and `validate` pass (1 warning: 13 text sizes in the scale). `preflight.py html`: 0 errors, 0 warnings (sizes 13, 15, 17, 22, 34). `check_dates.py --year 2026` passes. `check_names.py`: 0 errors; "English", "Italian", "I'd" and "Vorrei" are words, not invented names. Contrast against the rendered pixels: every grey label 7.3:1. Gallery copy at 192 px: the eye lands on the Italian sentence.

**Blind pairwise test (A)**, as for Lullwater: ours was judged more premium than all three references in every round: Speak +3, +3, +4, +4 and +3 on the final render; Duolingo +3, +3, +2, +3; Babbel +3, +3, +3, +3. No judge or auditor named Duolingo after the rebuild ("the close button, progress bar and count are generic lesson chrome"). **Passes.**

**Fresh-eyes audit (B), against the B2B screens:** 2, 3, 2.5, 2, 3 and 3 over six rounds: **does not pass**. The Italian, the stress, /kafˈfɛ/ and the counts were confirmed correct each time; the remaining verdict is weak craft around the idea (seven blocks at a similar volume, playback that looks like prototype links). Its chart was rebuilt three times (bars in cards, stress marks, smooth curves, then recording-like envelopes), and the asks reversed between rounds (smooth curves were called a maths diagram; the envelopes were then called randomly wiggly).

**After the last audit:** no change to Parlo; `shot.png` (22:27) is the audited page.
