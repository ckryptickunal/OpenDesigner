# OpenDesigner film: preflight audit v2

- **Video:** `renders/opendesigner-film.mp4` (1920 x 1080, 60 fps, 129.0 s, -14.2 LUFS, peak -1.4 dB)
- **Source:** `index.html`
- **Skill:** `skills/opendesigner-preflight` (checklist items are shown as C1 to C30, mistakes as M1 to M29)
- **Reviewer:** a fresh-eyes subagent, 2026-10-07. Report only: no project file was changed.
- **Scope:** the slop act (0 to 17 s) is judged only on legibility and on whether it reads as intentional. Everything after it is judged at full strictness.

Evidence lives in the scratchpad `/private/tmp/claude-501/-Users-Kunal-Desktop-Design-System/85b89da4-acae-4311-8dc5-3178d29a0473/scratchpad/audit2/` (shortened to `A/` below):
- `A/frames/full` and `A/frames/phone`: the helper's frames, one per second. Frame k is at about (k - 0.5) s; see the feedback section.
- `A/t/tNN.png`: exact frames taken at NN seconds.
- `A/cut/`: crops at 200%, 0.05 s step-throughs, and phone-size strips.

## Helper results

- `preflight.py html --medium video`: 0 errors and 4 warnings.
  - 14 font sizes, 4 pairs of them within 10% of each other, text under 40 px (28, 32, 34) and tracking of -0.04em.
  - Most of these sizes come from the slop act on purpose. After the slop act the film uses 6 sizes: 32, 40, 50, 62, 122 and 220.
- `preflight.py video`: 1 warning. 31.0 s is frozen (24%), in 17 holds of 1.5 s or longer, all between 54 and 129 s.
- Narration was checked against `audio/lines.json`:
  - Lines with an existing transcript in `audio/words/` were compared directly.
  - The 6 lines without one (v01, v03, v04, v06, v07, v17) were transcribed with `whisper-cli` (small.en).
  - All 18 match the script. No style directions were read aloud (C25 / M24: pass).

## Severity 1 (must fix before sharing)

**1. Act 2 text cannot be read on a phone, which contradicts the film's own premise.** 20 to 113 s. C9 / M8.
- The film says "People watching on a phone. So the type gets bigger." Yet almost every label that carries meaning in act 2 is set at `--t-label` 32 px, which is below the skill's 40 px floor. That covers:
  - token names and values
  - dial names and values
  - the lock-row subtitles
  - the research captions
  - every file name
  - the pane headers
  - `film.html · 1920 × 1080` and the status pill
- The canvas is drawn at a scale of 0.54, so the text inside it gets smaller again:
  - card titles end up at about 27 px and card bodies at about 17 px
  - the `13.8 : 1` contrast tag is about 17 px (75 s)
  - the grid label `space · 4 px base · 160 px margins` is about 17 px (62 s)
- At 390 px wide, all of this is 3 to 6 px tall and unreadable.
- Evidence: `A/cut/phone4.png` (frames at about 66, 75, 95 and 116 s), `A/t/t64.png`, `A/t/t75.png`, `A/t/t62.6.png`.

**2. "Seven skills" is wrong: the repo has eight.** 102.4 to 113.6 s. C22 / M21.
- The narration, the caption, the pane header `SEVEN SKILLS` and its 7-item list all say seven.
- The repo has 8 skill folders in `skills/`, including `opendesigner-preflight`.
  - `.claude-plugin/marketplace.json` says "Eight skills".
  - `AGENTS.md` on disk lists `opendesigner-preflight`.
- The line "Seven skills cover the rest" is also wrong on its own terms. The list includes `opendesigner` itself, so only six skills "cover the rest".
- Evidence: `A/t/t107.2.png`, `A/t/t112.9.png`, and `ls skills/`.

## Severity 2 (visibly cheap or misleading)

**3. Captions sit on the content in act 3.** 113.6 to 117.7 s. C26 / M25.
- The card bottoms reach about y = 932 and the caption text starts at about y = 965.
- The caption scrim (from y = 900) darkens the lower part of all three cards.
- The caption zone is not kept free of other content.
- Evidence: `A/t/t116.png`.

**4. Card text overflows the card padding.** About 49 to 118 s, and worst at full frame from 113.6 s. C14 / M13.
- The two-line title plus the two-line body is about 220 px tall in a 230 px card that has 50 px of padding.
- The title sits about 14 px below the top edge while the left padding is 50 px. It reads as cramped and clipped.
- Evidence: `A/cut/card200.png` (200% crop of `A/t/t116.png`).

**5. Skill highlights drift from the voice.** 102.4 to 112.5 s. C26 / C18.
- The highlight times come from `audio/words/v16.json`, whose timestamps drift. Its last words land at 11.03 s and 11.36 s, but `v16.wav` is only 10.09 s long.
- Silence detection on the wav puts the phrases at:

  | Spoken words | Time in the wav |
  |---|---|
  | "illustrate it" | 6.40 s |
  | "review it" | 7.42 to 8.16 s |
  | "even paint with it" | 8.47 to 9.68 s |

- So `illustrate` lights up 0.56 s early, `review` lights up after the phrase has ended (8.26 s), and `paint` lights up at 9.79 s, after the narrator has finished.
- The other sync points checked are within 0.1 s of the voice: the caption splits in v02, v05, v13, v14, v15, v16 and v18.

**6. 24% of the runtime is frozen.** 54 to 129 s. C15 / M14.
- There are 17 holds of 1.5 s or longer. Some of them:
  - 69.7 to 72.0 s
  - 104.9 to 112.5 s (four holds back to back)
  - 114.9 to 117.7 s
  - 119.0 to 124.8 s
- The camera push (`#cam`, scale 1 to 1.04 over 92 s) is too slow to see, and freeze detection does not register it either.
- From about 64 to 113 s the canvas does not change at all.
- Evidence: the `freezedetect` output from the helper's video mode.

**7. Slide-deck grammar: one entrance for everything.** 20 to 113 s. C13, C17 / M12, M16.
- All 8 panel panes enter and leave the same way, through `pane()`: fade in with a 24 px rise, then fade out with a 16 px lift.
- Every row inside them uses the same 20 px rise (`rise()`).
- Six panes in a row (tokens, dials, locks, research, files, skills) have the same shape: a mono header, then N identical rows.
- The canvas is the one object carried across the cuts, which is good, but nothing else varies.

**8. Three oranges in 10 seconds, and contrast claims that don't name their pair.** 50.9 to 65 s. C23 / M22.
- The panel shows `#E4572E`, then `#D04418` ("white text 4.64 : 1"), then `dark theme #D16445 · 4.88 : 1`. The next pane says `color.action #D16445`.
- The numbers are correct:
  - #E4572E with white is 3.68 : 1
  - #D04418 with white is 4.64 : 1
  - #D16445 with #161514 is 4.88 : 1
  - #ECE8E6 on #1E1D1C is 13.8 : 1
- But the dark-theme line does not say its text is dark (#161514) rather than white. The canvas button beside it is #D16445 with dark text, sitting under a heading that says "white text".
- `13.8 : 1` floats beside the headline without naming the pair.
- Evidence: `A/t/t56.5.png`, `A/t/t64.png`, `A/t/t75.png`.

**9. A repeated phrase, the same mistake as M26 in the last film.** C27 / M26.
- 21.9 to 27.8 s: the pane title "Inside the AI you already use." and the caption "I live inside the AI you already use." are on screen together while the voice says it. Evidence: `A/t/t26.png`.
- 121.3 to 125.4 s: the prompt pill and the caption both say "create a design system for this project" at the same time.

**10. A grid that most of the content misses.** 61.5 to 64 s. C11 / M10.
- The drawn grid has a 140 px pitch from x = 160, so its lines fall at 160, 300, 440, 580, 720, 860 and so on.
- Only the left edges snap (x = 160). Card 2 starts at 700 and card 3 at 1240, and no right edge lands on a line.
- The label says "4 px base". That does not describe a 140 px column pitch.
- Evidence: `A/t/t62.6.png`.

## Severity 3 (polish)

11. **The transitional headline collides with things.** 37.6 to 49.6 s. C14.
    - The scaled `#h2` runs edge to edge across the canvas, and its second line touches the subtitle.
    - A sparkle sits on the "o" of "Your", and the NEW!! sticker covers "built".
    - This stage is still meant to look broken, but it is past 17 s, and here the collisions look accidental rather than designed.
    - Evidence: `A/t/t40.png`, `A/t/t46.png`.
12. **Captions double-expose for one beat.** C16 / M15.
    - At every back-to-back caption change, both captions show for about 0.05 s (3 frames).
    - The outgoing caption fades out from b - 0.15 for 0.2 s, while the incoming one starts at b.
    - Evidence: `A/cut/cap84.png` (84.2 to 84.7 s in 0.05 s steps).
13. **Empty frames at transitions.** C16 / M15.
    - About 118.2 to 118.3 s: almost nothing but background shows, between the cards leaving and the wordmark rising (`A/cut/end.png`).
    - About 19.6 to 20.5 s and 113.4 s: the panel shell is shown empty (`A/t/t19.5.png`, `A/cut/grow.png`).
14. **Values outside the system.** C2 / M2.
    - Every exit uses `power2.in` with 0.25 s. The tokens say exit easing `cubic-bezier(0.23, 1, 0.32, 1)` and 160 to 200 ms.
    - About 15 spacing and size values are not on the x2.5 scale: 8, 12, 14, 18, 22, 26 and 66 px, the radii of 24 px on `#frame` and `#realwin`, and 5 and 6 px on the brand marks.
    - `#fb9073` and `#e4572e` are hard-coded instead of token variables.
15. **The file paths are not the real paths.** 92 to 102 s. C21.
    - The header says `WRITTEN TO opendesigner/`, but the files are in `opendesigner/build/css/tokens.css` and so on.
    - `DESIGN.md` is written at the project root, not inside `opendesigner/`.
16. **The same count is stated three ways.** C22, C23.
    - The voice says "nearly two hundred", the panel says 193, and the caption says "193".
    - 193 includes 6 questions marked planned and not built (`pacing.json` counts).
    - The card says "Five plain questions" while the pane says "A few plain questions". Inside the repo, `zoom.md` says "up to 5", but `pacing.json` lists 7 question ids for zoom 0.
17. **Some token rows change nothing on screen.** 59.7 to 61.4 s. C18 / M17.
    - The `color.action` and `text.display` rows land while the canvas stays the same, because the button and the headline had already changed earlier.
    - The source comment "type: tracking settles" only moves the headline 12 px.
18. **The caret looks like a typed space.** 121 to 124.5 s.
    - The caret sits 30 px after the typed text (the flex gap), so it reads as a trailing space.
19. **Slop act legibility.** About 1.4 to 17 s.
    - The NEW!! sticker is mostly hidden behind "Design" and reads as a layering bug, not as a deliberate joke.
    - Everything else in the slop act is legible, and it reads as intentional from the first caption ("This video has no design system yet. You can tell.").

## Checks that passed

- **Fonts (C10):** every family has an `@font-face` that points to a shipped file.
- **Mask fit (C4):** the wordmark's "p" and "g" at rest are not cut (`A/cut/word200.png`).
- **Tracking (C5):** the premium headline uses -0.02em and its word spaces are clear at 200% (`A/cut/h3_200.png`).
- **Real output (C21):** the preview window shows the engine's real `preview.html`.
- **Facts confirmed against the repo:**
  - 32 teardown files in `benchmarks/systems/` (25 in the matrix plus 7 extended)
  - 193 questions and 28 stages
  - 519 unique Decision Cards in `research/`, each citing at least one source
  - 8 dials, whose values match `state.json`
  - 9 `.tokens.json` files
  - `radius.overlay` 12 px, motion.enter `.23, 1, .32, 1`, 3 elevation layers, heading weight 650, display tracking -0.02em
  - "About three minutes" (from `zoom.md`)
  - the GitHub URL matches `origin`
- **Licence (C24):** "Free and open source" fits the repo (MIT code, CC BY 4.0 docs).

## Could not check

- **Reference research (C3):** no notes for this film were found on disk.
- **Every sync point:** only spot checks were made. Highlight sync for v11 to v15 depends on word timestamps that may drift the same way as v16.
- **Contrast inside the video:** taken from the token math, not measured on decoded frames.
- **Motion smoothness:** not measured.

## Feedback on the preflight skill itself

1. **The x2.5 mapping contradicts the 390 px phone premise.**
   - A 1920 px frame watched 390 pt wide is shown at about 0.2 scale. Under the x2.5 rule, 16 px body text becomes 40 px, which is about 8 pt on the phone. Captions and labels built "correctly" from the rule are therefore too small.
   - Keeping UI sizes (16 pt body) needs about x4.9. A defensible floor is about 54 px for meaningful text, which gives about 11 pt.
   - The SKILL's "about 2.5" and the checklist's "at least about 40 px" need to be reconciled.
2. **Legibility checks ignore transforms.**
   - The `html` check reads CSS `font-size` only. It cannot see that a scene is drawn at `scale(0.54)`, which is the main legibility failure in this film.
   - C9 / M8 should say "effective size after transforms". The helper could warn when an ancestor has `scale` below 1, or measure text in rendered frames.
3. **The helper's frame timestamps are off by half an interval.**
   - `frames` prints "Frame k is at about (k-1) x every". With ffmpeg's `fps` filter, frame k is nearer (k - 0.5) x every: helper frame 0067 matched 66.49 s exactly, with a PSNR of 64.7.
   - Either print the true times or extract with `-ss` per timestamp.
4. **There is no way to scope a deliberately bad section.**
   - The `html` check counts the slop act's sizes and tracking, so its M6, M8 and M5 warnings were mostly noise.
   - An `--ignore` selector, or a `data-preflight-ignore` attribute, would make the warnings useful.
5. **The video check reports totals, not locations.**
   - It says "31 s frozen" but not where. Printing each freeze range, and black-frame ranges, would save a rerun.
   - The 15% threshold, and C15's "silent piece" clause, don't say what applies to narrated pieces. This film is narrated, so it is unclear whether 24% is acceptable.
6. **Missing checklist items:**
   - **Highlight-to-voice sync:** word-timestamp files can drift past the clip length. Catch it by checking the last word time against the wav length, or with silence detection.
   - **Caption double exposure at back-to-back caption changes.**
   - **Caption safe zone in each layout state:** the zone was clear in act 2 and occupied in act 3.
   - **Content inside a card overflowing its own padding:** C14 only covers wrapping and overflow of pills and paths.
   - **Facts against the working tree, including uncommitted files:** "seven skills" was true at the last commit and false on disk.
   - **A contrast claim must also say which text color it uses:** C23 says "next to the exact pair", but the failure here was a pair that was never named.
7. **A known mistake recurred anyway.**
   - M26 ("the AI you already use" repeated) is the catalog's own example, and it came back in v2. Reading the text out loud was not enough.
   - The helper could list on-screen strings and captions that are visible at the same time and flag shared runs of 3 or more words. Most strings are in the HTML, and the caption times are in the script.
8. **There is no severity scale and no report template.**
   - SKILL.md section 5 asks for time, evidence and rule, but not for a severity. Reviewers will each invent their own.
   - A 3-level definition would make audits comparable. For example: 1 is wrong or unreadable, 2 looks cheap or misleads, 3 is polish.
9. **Small items:**
   - C17 says "list each scene's entrance" but gives no output format.
   - C22 says "check every number against the source" but doesn't say which source wins when the repo disagrees with itself (`zoom.md` "up to 5" versus `pacing.json` with 7 ids).
   - The `video` mode could also print peak level and true-peak, not only LUFS.
