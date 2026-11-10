# Audit v1: opendesigner-explainer.mp4

Reviewed 2026-10-07 against `renders/opendesigner-explainer.mp4` (85 s, 1920x1080, 60 fps) and `index.html`. `index.html` was not edited.

**Evidence root:** `/private/tmp/claude-501/-Users-Kunal-Desktop-Design-System/85b89da4-acae-4311-8dc5-3178d29a0473/scratchpad/audit/`
- `f/f_NNN.png` holds one frame every 0.5 s. The frame for time t is `NNN = 2t + 1`, so 13.0 s is `f_027.png`.
- `sheet_00..08.png` are the same frames as labelled contact sheets.
- `t/t_<sec>.png` are frames 0.1 s apart around each scene start, tiled in `trans.png`.
- `c/full_<sec>.png` are full-resolution stills, and `c/crop_*.png` are zoomed crops.

**Method:**
- I looked at all 170 half-second frames and 60 frames around the transitions, and cropped the type at full resolution.
- `ffmpeg freezedetect` found the static stretches. It ran on the frame without the progress bar, with noise 0.0015 and a 1 s minimum.
- I checked the facts on screen against `skills/opendesigner/references/*.json`, `zoom.md`, `synthesis/standards.json`, `benchmarks/systems/`, `research/*.md`, `examples/*/tokens/` and `engine.py`.

**Verdict:** It looks cheap for three main reasons:
- **It is a slide deck with a fade between slides.** About 36 of the 85 seconds are frozen. Every scene enters and leaves the same way.
- **The type is broken in places.** Descenders are clipped, letters collide and word spaces collapse.
- **The design-system content contradicts itself.** The video claims DTCG but shows JSON that is not DTCG. A "ramp" mixes two hues, a radius labelled up to 32 animates past 32, and the "Zoom in" scene zooms out.

---

## Severity 1: broken or wrong (fix before anyone sees it)

### 1. Clipped descenders on the hero wordmark (twice)
- **Where:** 6.75 to 11.4 s (scene 2) and 81 to 85 s (end card).
- **What:** The "g" and "p" in "OpenDesigner" are cut flat along one horizontal line. The bowl of the g is sliced off.
- **Why it reads cheap:** It is the brand name, at its biggest size, on the two frames people screenshot. A cropped glyph looks like a bug, not a style.
- **Cause:** `.word` has `line-height: .9`, and each `.ch` mask has `overflow: hidden` with only `padding-bottom: .1em`. The Inter Tight g descender reaches lower than that box.
- **Evidence:** `c/crop_s2.png`, `c/crop_g.png`, `c/crop_end.png`, `f/f_020.png`, `f/f_167.png`.
- **Rule:** Any glyph inside an `overflow: hidden` reveal mask must fit the mask at rest. Render the resting frame, crop the lowest descender (g, j, p, q, y) and the highest ascender or accent at 200%, and check that no curve ends in a straight cut.

### 2. The "DTCG" token card is not DTCG, and its token names do not exist
- **Where:** 46.3 to 53.4 s.
- **What:** The card is labelled `opendesigner/tokens/ · DTCG` and shows `"color": {"accent": "#e4572e", "ink": "#121212"}, "radius": {"md": "12px"}, "space": {"base": "4px"}`. Three things are wrong:
  - **No DTCG keys.** There is no `$value` or `$type`. `engine.py` (lines 1256 to 1268) writes both.
  - **Wrong names.** The real output has `radius.0`, `radius.2` up to `radius.32`, plus semantic `radius.control`, `radius.container` and so on. Space uses numeric steps, and colour is ramps such as `color.neutral` and `color.brand`. There is no `radius.md`, `space.base` or `color.ink` (see `examples/public-service-accessible/tokens/primitives.tokens.json` and `semantic.tokens.json`).
  - **Not one file.** The tokens are 10 files: primitives, semantic, density and motion files, a resolver and a meta file.
- **Why it matters:** This is a design-system product. Anyone who knows DTCG will spot it, and it undermines the "built on research" scene that follows.
- **Evidence:** `c/crop_code.png`, `f/f_101.png`.
- **Rule:** Any code, file or schema on screen must be pasted from real output of the product, then trimmed. If it is labelled with a standard (DTCG, JSON Schema, OpenAPI), check the shown snippet against that standard's required keys.

### 3. The "color.ramp · 10 steps" mixes two hues
- **Where:** 27.2 to 38.6 s.
- **What:**
  - **Two hues.** The bar has nine warm neutrals and then an orange accent, but is labelled one 10-step ramp. A ramp is one hue stepped through lightness, and the product's own tokens keep `neutral` and `brand` as separate ramps.
  - **Invisible first step.** The first swatch, `#f3f2ee`, sits on the card colour `#fbfaf7` at a contrast of about 1.07:1, so the bar reads as nine steps.
  - **Copied from the README image.** The panel is lifted straight from `docs/assets/social-preview.png`, which has the same mistake.
- **Evidence:** `c/crop_sys.png`, `f/f_063.png`.
- **Rule:** A label must agree with what is drawn. Count the swatches, steps or items and compare them with the number in the label. A "ramp" must hold one hue, and every swatch must differ from its own background by at least 1.5:1 so you can see it.

### 4. The radius panel contradicts its label and its CODE caption
- **Where:** 28.4 to 33.6 s, with the caption at 34 to 38.6 s.
- **What:**
  - **Values outside the label.** The label says `0 → 32`, but the three squares animate to 12, 28 and **50 px**. On a 100 px box, 50 px is a full circle, which is `radius.full`, not 32. The second pass goes to 6, 20 and 38, and 38 is still above 32.
  - **No zero.** No square ever shows 0.
  - **Caption with nothing to point at.** The panel leaves at 33.6 s, but the PLAIN, DESIGNERS and CODE captions that follow are all about corners. They explain a thing that is no longer on screen.
- **Evidence:** `f/f_059.png`, `f/f_063.png` (circle), `f/f_071.png` (captions with no radius panel), `c/crop_voice.png`.
- **Rule:** Every animated value must stay inside the range its label states. An explanation must share the screen with the thing it explains.

### 5. "Zoom in" is shown as a zoom out
- **Where:** 39.8 to 45 s.
- **What:**
  - **Built inside out.** The boxes appear from the inside: 0 · Sketch first, then 1, 2 and 3 grow around it.
  - **Camera pulls back.** The whole nest scales from 1.35 down to 1, so you get bigger frames and more context, which is a zoom out.
  - **Says the opposite of the headline.** The headline is "Stop anywhere. Zoom in." The product's idea is to start at the sketch and go deeper, so the camera should push into a box, not pull back.
- **Evidence:** `sheet_04.png` (40.0 to 42.0), `f/f_081.png` to `f/f_085.png`.
- **Rule:** The direction of motion must match the verb on screen. Read the headline, then play the scene with the sound off and say what the camera did. If the two disagree, change one of them.

### 6. Collapsed word spaces and colliding letters in display type
- **Where:** All display lines. The worst are at 0.5 to 6 s, 16.7 to 25.6 s and the section heads.
- **What:**
  - **Collapsed spaces.** At -0.045em to -0.06em of tracking, the word space shrinks to about the size of a letter gap. "how it" reads as "howit", "What if" as "Whatif", and "A complete" as "Acomplete".
  - **Touching letters.** In "Five" (168 px at -0.06em), the dot of the i touches the arm of the F, and the v and e touch.
  - **Lines nearly touching.** In "Every app needs rules / for how it looks." (line-height .98), the tail of the y in "Every" nearly meets the f of "for".
  - **Not like the reference.** The social preview uses tight tracking only on one short wordmark, not on whole sentences.
- **Evidence:** `c/crop_s1a.png`, `c/crop_s1b.png`, `c/crop_five.png`, `c/crop_h2.png`.
- **Rule:** Negative tracking needs word spacing to make up for it. Under -0.03em, add about +0.05em to +0.1em of `word-spacing`. Crop each display line at 200% and check two things: no two glyphs touch, and every word space is clearly wider than the widest letter gap.

### 7. About 42% of the runtime is frozen
- **Where:** `freezedetect` (no change for more than 1 s, outside the progress bar) found these stretches:

| Start (s) | Length (s) | Scene |
|---|---|---|
| 1.15 | 1.1 | hook |
| 8.33 | 2.9 | title |
| 14.78 | 1.5 | hosts |
| 29.5 | 2.05 | system |
| 31.87 | 1.8 | system |
| **34.7** | **4.0** | system |
| 43.0 | 1.6 | zoom |
| **48.3** | **5.0** | exports |
| 56.3 | 2.45 | floors |
| **62.65** | **6.1** | stats |
| **72.25** | **5.0** | skills |
| 82.65 | 2.35 | end card |

  The total is about 35.8 s of 85 s. The drifting background grid (about 1 px/s) and the 85-second progress bar are the only things moving, and neither counts as motion.
- **Why it reads cheap:** The video has no audio, so a frozen frame has nothing holding attention. "Fast kinetic" (the brief) turns into a slide show.
- **Rule:** Run `freezedetect` before export. In a silent piece, no hold should last more than about 1.5 s unless it is the final end card. During a hold, keep a secondary action going (a highlight walking through a list, a value changing, a slow push-in) or cut sooner.

## Severity 2: reads as cheap (slide deck, monotony, weak composition)

### 8. Every scene uses the same entrance and exit
- **What:**
  - **One entrance.** Ten of the eleven scenes open with a headline whose words rise from a mask (expo.out), then a stack of cards that slide in by 60 to 90 px with an opacity fade and a stagger.
  - **One exit.** Every scene leaves with `y: -40, opacity: 0` over 0.32 s.
  - **Nothing carries across.** No element survives from one scene to the next: no shared object, no match cut, no camera move.
- **Evidence:** `sheet_00` to `sheet_08`. Compare the openings at 11.75, 26.25, 39.25, 45.75, 53.75, 59.25 and 69.25 in `trans.png`.
- **Rule:** List each scene's entrance, its main action and its exit in a table. If more than a third of the rows match, redesign the transitions. A video should have at least one carry-over (an object that moves from scene N into scene N+1) per act.

### 9. Blank frames between scenes, and an orange wipe that wipes nothing
- **Blank frames.** At six cuts the old scene fades out fully before the new one starts. That leaves 0.2 to 0.3 s of empty cream frames:
  - 11.55 to 11.65 s
  - 16.55 s
  - 39.05 to 39.15 s
  - 45.55 to 45.65 s
  - 53.55 s
  - 69.05 to 69.15 s
- **Wipe over nothing.** The orange wipe runs at only 4 of the 10 cuts (6.5, 26, 59 and 77.5 s). At each of them the old scene is already fading under the wipe, so it goes from almost blank to blank. At 26.05 and 59.05 s the wipe covers half the frame over empty cream. It decorates but does not join the scenes.
- **Evidence:** `trans.png`, `t/t_11.55.png`, `t/t_39.05.png`, `t/t_45.55.png`, `t/t_69.05.png`, `t/t_26.05.png`, `t/t_59.05.png`.
- **Rule:** Step through each cut 0.05 s at a time. No frame should show only the background. Use one transition grammar throughout, and only use a wipe if it actually covers the swap.

### 10. Grids of identical cards (scenes 4, 7, 8, 9 and 10)
- **What:** Five scenes are the same object: same-weight cards in a list or grid, each with a small mono label.
  - 5 question cards
  - 8 export pills
  - 4 lock rows, each with an identical LOCKED badge
  - 6 stat tiles in a 3x2 grid
  - 7 skill rows, each with an identical orange dot
- **What is missing:** Nothing in any of them is ranked, highlighted in order or linked to anything else. In scene 8, the same LOCKED badge four times adds nothing (a lock icon or one line saying "locked" would do).
- **Evidence:** `f/f_041.png`, `f/f_101.png`, `f/f_115.png`, `f/f_133.png`, `f/f_151.png`.
- **Rule:** No more than two scenes in a row should be "N identical cards". In any group of cards, one card needs a reason to be different (the one being talked about, the biggest, the one that changes).

### 11. Unbalanced compositions with large empty areas
- **Scene 3, 12 to 16 s:** All the content sits in the top 55% of the frame, and the bottom 40% is empty (`f/f_029.png`).
- **Scene 4, 22.8 to 25.6 s:**
  - **Empty frame.** The question list leaves and the principles bar appears at the bottom. "Five questions." sits alone top-left, and the right two thirds of the frame are empty for 2.8 s.
  - **Fake motion.** The only movement is the headline scaling from 1 to 1.02 over 3 s, which you cannot see (`f/f_048.png`).
- **Scene 5, 34 to 38.6 s:** The bottom row leaves, which opens a band about 250 px tall between the top panels and the captions (`f/f_071.png`).
- **Scene 6:** The nested boxes have 210 to 220 px side margins but only 30 px between their bottom edges. They pile up at the bottom (`c/crop_zoom.png`).
- **Scene 8, 54 to 58.6 s:** The lock list is fixed at 1300 px wide and left-aligned, so the right 500 px of the frame is empty (`f/f_115.png`).
- **Scene 10:**
  - **Wasted gutter.** The skill-name column is 560 px wide for names at most 260 px wide. That leaves a gap of about 300 px.
  - **Same colour as the background.** The rows' right halves are empty card fill (`c/crop_skills.png`).
- **Rule:** Look at every frame of a hold as a thumbnail. The content should sit inside an intended box, with roughly equal margins or a deliberate asymmetry. No empty area larger than about a quarter of the frame should appear unless it is the subject of the shot. Nested shapes need equal or proportional insets on all sides.

### 12. The type scale has no system
- **What:** I counted 27 distinct font sizes in the CSS:
  - **Labels and body:** 18, 20, 22, 24, 26, 30, 32, 34, 36, 38, 40, 44, 50, 56, 60
  - **Specimen sizes:** 47, 59, 73, 92
  - **Display:** 64, 96, 110, 150, 168, 200, 270, 420 (the 420 is the unused `.ghost` class)
- **Near-duplicates:** 18 and 20, 22, 24 and 26, 32 and 34, 36, 38 and 40.
- **Section heads disagree:** Scenes 3 and 8 use 110 px headings, centred vertically. Scenes 5, 6, 7, 9 and 10 use 96 px headings at the top, through inline `style="font-size:96px"` overrides.
- **Two families at nearly the same size:** In the skill rows, a 36 px mono name sits next to a 38 px sans description. They compete instead of setting a hierarchy.
- **The contradiction:** The video shows a "type.scale 1.25" panel but does not follow a scale itself.
- **Rule:** Before export, take every font size from the computed styles. There should be at most about 8 sizes in a video (display, heading, sub, body, label, plus the specimens), and each should be a step of one ratio. Two sizes within 10% of each other are a bug. Two type families next to each other need a clear size or weight gap.

### 13. Labels that cannot be read on a phone (and some barely at 1080p)
- **The small sizes:**
  - Scene tags (01 / WHY and so on) and the brand mark: 18 px
  - Dial labels: 18 px
  - Voice labels: 20 px
  - Panel labels: 22 px
  - Code: 24 px
  - LOCKED badges: 24 px
  - Answer pills: 26 px
  - Stat captions: 30 px
- **On a phone:** At about 390 px wide, which is how README and social viewers see it, the video is scaled to about 0.2x. These sizes become 3.7 to 6 px.
- **What you lose:** The scene tags, the code card, the dial labels and the skill descriptions (38 px becomes 7.7 px) cannot be read on a phone. The code card is the proof of "one source of truth", and it is 24 px in a small card in the middle of the frame.
- **Cryptic dial labels:** "Exp Brd Den Enr Rnd Dep Col Wrm" are shortened forms of `levers.json` dials. They are correct, but nobody can decode them.
- **Evidence:** `c/crop_sys.png`, `c/crop_code.png`, `c/crop_brand.png`.
- **Rule:** Text that carries meaning in a 1080p video for social or README use should be at least 40 px, which is about 8 px on a phone. Text below that size must be decoration that can be left unread. Downscale the frame to 390 px wide and read it. Never abbreviate a label the viewer needs.

### 14. Widows, orphans and bad rag
- **Scene 3 headline (11.8 to 16.4 s):** "It lives inside the AI you already / use." leaves a one-word widow. This is the main line of the scene (`f/f_027.png`).
- **Stat caption (60 to 68.6 s):** "famous design systems torn / down" breaks a phrasal verb across lines. The tile sits next to one-line captions, so the baselines do not match across the row (`c/crop_stats.png`).
- **Voices (34 to 38.6 s):**
  - "Corner radius, concentric when / nested." ends on a one-word orphan.
  - "border-radius · radius.0 → / radius.32" breaks a code expression at the arrow (`c/crop_voice.png`).
- **Scene 4 note:** It changes its break while it animates in. At 19.0 s "About three minutes, and you already" is followed by "have", and it later settles to another break (`f/f_039.png`).
- **Rule:** No line of display or caption text may end with a single word, or split a phrase, a number and its unit, or a code expression. Set `text-wrap: balance` on headings, and check every resting frame for one-word last lines.

### 15. A visible grid that nothing aligns to
- **What:**
  - **Visible lines.** The background draws a 96 px grid at 55% opacity, and it drifts 96 px over 85 s.
  - **Content off the grid.** The scene padding is 120 px and the brand sits at 72 px. Card gaps are 18, 22 and 26 px, and card paddings are 26 to 40 px. No edge of the content lands on a grid line.
  - **Pointless drift.** The grid's slow movement (about 1 px/s) adds nothing and looks like an encoding wobble.
- **Evidence:** any full frame, for example `c/full_31.0.png`.
- **Rule:** If a grid is visible, the content must snap to it (or the grid must go). Spacing values should come from one scale; here the product itself says the base is 4 px, so use 8, 16, 24, 32, 48 and so on. Gaps of 18, 22 and 26 are not on a 4 px scale.

### 16. The hosts copy repeats itself
- **What:** The scene 2 subtitle "Build a real design system **with the AI you already use**." is followed straight away by the scene 3 headline "It lives inside **the AI you already use**."
- **Rule:** Read every on-screen line in order as a script. No phrase longer than three words should appear twice within 10 s.

### 17. The skills list and the exports scene disagree
- **What:**
  - **The two lists.** Scene 7 lists Figma and Paper as export targets. The `-export` row in scene 10 says "ships it to CSS, Tailwind, Swift, Compose, Figma", which drops Paper and DTCG.
  - **Platforms or not.** Scene 7's "Every platform." also includes DESIGN.md and PRODUCT.md, which are documents, not platforms.
  - **Naming.** "SwiftUI" in scene 7 becomes "Swift" in scene 10.
- **Rule:** Any fact stated twice must be stated the same way. Grep the source for each product noun and check its spelling and list every time it appears.

### 18. Inconsistent casing and formatting
- **Hex case:** The colour is `#E4572E` in the scene 4 answer pill and `#e4572e` in the scene 7 code.
- **Voice labels:** PLAIN, DESIGNERS and CODE are an adjective, a plural noun and a noun. The glossary's voices are plain, designer and engineer.
- **Zoom details:** "1 · Broad" shows "8 questions · ~8 min" and "0 · Sketch" shows "5 questions · ~3 min". "2 · Defined" and "3 · Detailed" switch to descriptions with no counts.
- **Code in the wrong family:** The CODE voice is set in the sans, while every other code-like string is mono.
- **Unexplained highlights:** The first dial knob and the Claude chip get a highlight for no stated reason.
- **Rule:** Use one case convention per data type (hex, labels, file names). Parallel items must have parallel grammar and the same fields. Every highlight must have a reason the viewer can see.

### 19. Small motion-craft problems
- **Slot-machine words, 2.5 to 4.3 s:** Each of the five words gets 0.36 s, with no blur and no overlap. "Spacing." is barely readable (`f/f_007.png`, `sheet_00`).
- **Answer pills, 17.85 s on:** They pop in from scale 0.6. That is the only scale-from-small entrance in the piece, and it looks like a default.
- **Count-ups, 60 to 61.5 s:**
  - **Tilde too early.** The ~ prefix shows during the count ("~207").
  - **Plus sign pops in.** The + suffix appears only at the very end.
  - **Six numbers at once.** All six count together, so the eye reads none of them (`f/f_122.png`, `f/f_124.png`).
- **The prompt, 78 to 80.7 s:** The caret sits 26 px (the flex `gap`) away from the last letter, so it floats. Once typing finishes, the text uses only about 65% of a 1360 px box (`c/crop_prompt.png`).
- **The dial "second pass", 31.2 s:** The knobs move to new values, but the only visible effect is a change in the gap between type specimens. Changing the gap is not a type-scale change, so it implies a link that does not exist.
- **Rule:**
  - Give every word in a rapid sequence at least about 0.5 s on screen.
  - Count-ups should show their final affixes from the first frame.
  - One counting number should be the hero at a time.
  - A cursor must touch the glyph it follows.
  - Any "this control changes that" animation must change the thing the control names.

## Severity 3: facts to confirm or adjust

Checked against the repo on 2026-10-07.

| On screen | Repo | Status |
|---|---|---|
| 193 questions across 28 stages | `questions.json` has 193; there are 28 non-detailed stage files | Correct. AGENTS.md notes that 6 questions are planned and skipped, so "193 questions" is generous but matches the docs |
| 270+ building blocks | `ontology-slim.json` has 275 nodes (AGENTS.md says 271) | Correct as "270+" |
| 32 famous design systems torn down | `benchmarks/systems/` has 32 entries | Correct on disk, but AGENTS.md still says "Teardown of 25 famous design systems". That is a living doc to update; the video itself is fine |
| 500+ Decision Cards, "each with sources" | 519 `### DC-` headings in `research/*.md` | The count is correct. "Each with sources" is not verified: the rules allow `[inferred]` claims, so some cards may have none. Soften it to "with sources", or check every card first |
| 455 house standards from 46 sources | `standards.json` has 455 standards, `built_from` 46 | Correct |
| ~400 terms in 3 voices | `glossary.json` has 399 terms | Correct |
| Zoom 0 has 5 questions, about 3 min; zoom 1 has 8 questions, about 8 min | `zoom.md` says "up to 5 questions, about 3 minutes" and "8 questions, about 8 minutes" | Correct. The scene 4 copy "you already have a complete system" matches the zoom.md wording "complete but coarse" |
| The five questions and the answer "regular use" | They match `zoom.md` level 0 | Correct |
| Eight dials | `levers.json` has expression, brandPresence, density, energy, roundness, depth, colorfulness, warmth | Correct, but the abbreviations cannot be read (see finding 13) |
| "Free and open source · MIT" | Code is MIT; research and docs are CC BY 4.0 (`README.md` line 249) | Partly correct. Consider "MIT code · CC BY content", or keep it and accept the simplification |
| DTCG token snippet | Not DTCG, and the token names are invented | Wrong (see finding 2) |
| Mono font | `--mono: "JetBrains Mono"` has no `@font-face`, and the font is not installed in `~/Library/Fonts` | Risky. The render looks like JetBrains Mono, so the renderer probably resolved it itself [inferred]. Another renderer would fall back to the system mono. Bundle the woff2 the way Inter Tight is bundled |

---

## Check before export (reusable, deduplicated)

Run these on any video, page or deck before you call it done.

**Type**
1. **Mask fit.** Render the resting frame and crop the lowest descender and highest ascender of every masked or `overflow: hidden` line at 200%. No glyph may end in a straight cut.
2. **Tracking and word spacing.** At 200%, no two glyphs touch, and every word space is clearly wider than the largest letter gap. Negative tracking below -0.03em needs extra `word-spacing`.
3. **Line spacing.** With line-height under 1, check that the descenders of one line do not meet the ascenders of the next.
4. **Scale audit.** Take every font size from the computed styles. Use at most about 8 sizes, all from one ratio, with no two within 10% of each other. Do not override a heading size inline for one scene.
5. **Rag.** No one-word last lines, and no breaks inside a phrase, a number and its unit, or a code expression. Use `text-wrap: balance` on headings.
6. **Legibility.** Downscale a frame to 390 px wide. Meaning-bearing text must still be readable, which means at least about 40 px at 1080p. Never abbreviate a label the viewer needs.
7. **Fonts.** Load every `font-family` you use from a bundled file. Fail the build if a fallback face renders.

**Layout**

8. **Grid.** If a grid is visible, every content edge snaps to it. All spacing comes from one scale, such as a 4 or 8 px base.
9. **Balance.** On every hold, the content sits in an intended box. No unintended empty area is larger than about a quarter of the frame. Nested shapes have proportional insets on all sides.
10. **Variety.** No more than two scenes in a row are "N identical cards". Each group of cards has one with a visible reason to stand out.

**Motion**

11. **Freezes.** Run `ffmpeg -vf freezedetect=n=0.0015:d=1` on the frame without the progress bar. In a silent piece, no hold should last over about 1.5 s except the end card. Keep the total frozen time under 15%.
12. **Cuts.** Step through every cut 0.05 s at a time. No frame should show only the background. The transition must cover or carry the change, with one grammar throughout.
13. **Variety of motion.** Write each scene's entrance, main action and exit in a table. If more than a third match, redesign. Have at least one carry-over or match cut per act.
14. **Direction.** The motion's direction (in or out, up or down, toward or away) matches the verb on screen.
15. **Timing.** Rapid word swaps get at least about 0.5 s each. Count-ups show their final affixes from frame 1, with one hero number at a time. A cursor touches its glyph. A "control changes X" animation changes X.

**Truth**

16. **Labels match drawings.** Count the items, steps and swatches and compare them with the number in the label. Animated values stay inside the stated range. A "ramp" holds one hue, and each swatch differs from its background by at least 1.5:1.
17. **Real artefacts.** Code or files on screen are pasted from the product's real output. If a standard is named, check its required keys (for DTCG, `$value` and `$type`).
18. **Facts from the source.** Every number and claim is checked against the repo on the day of export, and every "each" or "all" claim is verified. A fact stated twice is stated the same way (lists, names, casing).
19. **Script read-through.** Read all on-screen text in order. No phrase longer than three words appears twice within 10 s. Parallel items use parallel grammar.
20. **Explanation and subject together.** A caption or explanation shares the screen with the thing it explains.
