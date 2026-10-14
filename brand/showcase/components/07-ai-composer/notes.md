# 07 · AI composer · Oriel

## Direction
Oriel is a fictional research assistant for historians and long-form writers: you bring PDFs, field data and archive links, and it reads them with you and cites every claim. The composer should feel like a reading room, not a chatbot: parchment, brown-black ink, one terracotta accent, an editorial serif (Newsreader) for the answer, the mode names and the small italic notes, and a warm grotesque (Instrument Sans) for the controls and what you type. Soft paper-card corners and pill controls. The page is set like a journal: a double-ruled masthead, small-caps labels, an issue number.
Feel words: **warm, editorial, refined** (engine: warm → friendly, refined → premium, "editorial" unknown).

## References (Mobbin, cited by link only)
- Microsoft Copilot home composer, https://mobbin.com/screens/2ff3d94d-adb2-4937-818d-de633b9757c3 : attachments as cards above the text, a small mode pill and a round send in one footer row. Taught me the composer's anatomy and vertical order.
- Gumloop model picker, https://mobbin.com/screens/a3f8b130-cfc5-4ddc-8fd9-b95a4a6927bf : models described by what they are good at ("Recommended", "Smartest", "Fastest") instead of version numbers. Taught me to name models by behaviour and say speed in words.
- Unify chat while thinking, https://mobbin.com/screens/09c29920-400c-4d21-9eba-b057f8759c50 : the send button becomes a square stop while the agent works, with a visible "Thinking 7s". Taught me the send/stop swap and showing elapsed time.
- Dropbox Dash, https://mobbin.com/screens/536f1280-e59b-43c4-8dd0-3f0e91e15695 : model menu rows with a one-line description and a check for the selected one. Taught me the menu row structure.

## System (engine)
`sketch --name "Oriel" --brand "#b4532a" --audience regular --platforms web --feel warm,editorial,refined --theme system-light-dark --delegated all --surfaces read`, then `pick Q-color-09 warm`, `pick Q-ai-01 chat`.

| Dial | Value | Why |
|---|---|---|
| expression | 62 | editorial voice, generous serif in the answer |
| brandPresence | 62 | terracotta and the serif carry the brand |
| density | 32 | a reading product: airy, unhurried |
| energy | 30 | calm; only send and streaming move |
| roundness | 64 | radius control 12, container 16, overlay 24, pills full |
| depth | 45 | cards lift slightly off the paper (floating, overlay shadows) |
| colorfulness | 38 | warm neutrals, one terracotta |
| warmth | 88 | cream paper, brown-black ink |

Typefaces: `raw.textFace "Instrument Sans"`, `raw.displayFace "Newsreader"` (both SIL OFL, Google Fonts), `raw.fontLicence` recorded. Neutral: `raw.neutralBase "#e8dcc5"` (parchment; see findings).

## Where I stepped outside the tokens, and why
- Serif display weight: I used `font.weight.body` (400) and 500 for the serif because the engine's heading weight (600) is too heavy for an editorial serif; there is no display-only weight.
- Mention chip, drop zone and suggestion hover use accent ramp step 2 (lighter than `bg.accent-subtle`) because the subtle role was too pink against parchment.
- Paper grain is a decorative SVG noise at 5% (art, not a token).
- The masthead "Oriel" (39px italic) and issue number use the 39px token; the answer is set in the serif at the 20px token with `opsz 20`.
- Citation chip lifted 3px off the baseline by hand.

## Checks
- `engine.py validate`: no errors, 0 warnings, 5 notes (APCA advisory in dark mode, orphans, asset hooks).
- `preflight.py html --medium web`: 1 error, a false positive: M9 "Newsreader has no @font-face" (it loads from the Google Fonts link). "font sizes in px: []" because every size is a rem token; smallest text here is the 13px token.
- Contrast: tertiary text #6d634f on paper #f7f4ed is about 5.6:1; italic notes use it. Disabled send icon is exempt (disabled control). The drop state's light accent fill keeps accent text at the engine-checked text.accent role.
- Checklist (type, layout): two families plus system mono (unused), serif only for reading and labels of intent, sans for controls; captions never clipped; one filled action per area (send); no orphaned single words in the hero prompt.
- Interaction: real contenteditable textbox with a non-editable mention chip; Enter sends, Shift+Enter breaks a line; send turns into a stop square for 4s, Esc stops; send disabled when empty; Mode is a radiogroup with Arrow keys; the model pill opens a real menu (a live copy of the spec) and updates the pill; attachment remove buttons; drag-over turns the composer into the dashed drop target; reduced motion stops the caret blink and pulse and zeroes transitions.

## Rounds
1. First render was close. Problems: keyboard hint "Enter send" read as a label, the streaming line had a broken space around the italic title, the third suggestion wrapped alone, and the right column ended 100px early.
2. Rewrote the hint, fixed the streaming line, shortened suggestions, added the drop-target state.
3. The new state pushed the right column off the canvas; shortened the error copy and tightened padding.

## Process findings
1. **No way to get cream/parchment through the documented questions.** Warmth 88 tinted the grays pink (toward the brand hue). `pick Q-color-09 warm` then made them nearly gray (chroma 0.010). `raw.neutralBase` fixes it but is only discoverable by reading engine.py. (feedback: gap)
2. **"editorial" is not a feel word** the engine knows. (feedback: idea)
3. **The heading weight is shared by sans titles and the serif display**, so the serif came out at 600. (feedback: gap)
4. **AI composer has no component support.** `pick Q-ai-01 chat` adds `prompt-input` to the inventory, and DESIGN.md calls it "planned (tokens ready)", but there are no composer tokens or state guidance (send, stop, streaming, queue, error that keeps the draft). (feedback: gap, idea)
5. Helped: the motion feedback and enter transitions, `motion.scale.press` and `motion.scale.enter` gave the send press and the attachment × reveal for free; elevation floating and overlay at depth 45 looked right on paper without tuning; the house standard for focus (outer 2px, 2px gap) worked on the round send.

## Owner type and color rules (applied after the first render)
- **Two fonts:** Newsreader (serif: answer prose, masthead, small notes, mode names) and Instrument Sans (controls, input, labels). No mono is used anywhere.
- **No italic-word highlight:** the masthead was "N° 07 · *Composer*" with the last word in italic terracotta, which is the banned trick. Now "Composer" is regular serif in ink, and "No. 07" sits in a filled ink box in the sans. The "Oriel" wordmark is upright now. The @mention chip is the sans in a fill box (it was italic serif inside sans text, two faces in one line). Model descriptors ("quick", "careful") are the sans, not italic serif. The italic *common pool* in the answer stays: it marks a quoted term in running prose, not a headline highlight.
- **Type scale (4 sizes):** caption/label 13 (small caps labels, notes, file meta), body 16 (controls, buttons), body-large 20 (answer prose, the prompt), display 39 (masthead). Weight: display and answer at regular 400; labels 500-600.
- **Color:** light parchment with near-black ink (about 14:1) and one terracotta. To avoid muddy mid-tones, the small italic notes and captions moved from text.tertiary (#6d634f) to text.secondary (#5f5644).

## Round 3 (owner review, 2026-10-14)
**What Kunal said:** "very good, but the colours need work. Keep everything else; fix the palette only, and keep it harmonious." So the layout, type, copy, masthead and the component sheet were kept as they were; only colour (and the paper grain, which belonged to the parchment) changed. Earlier audit: cream parchment, terracotta and brown-black ink were the forbidden warm trio; tertiary text was brown; a 5% grain sat on the paper.

**What changed (palette only):**
- **Through the engine:** `set raw.brandColor "#2B4C8C"` (an ink blue, `--set-by chosen`), `set raw.neutralBase null` (no parchment), `set raw.neutralTint "pure"` and `pick Q-color-09 pure` (true greys; the first try, "neutral", came out blue-grey and made the page monochrome blue), `set dials.warmth 20`, `set raw.focusColor "#242424"`, then `build`. Why blue and not a cleaner terracotta: terracotta and a serif on ivory sits close to a real AI assistant's own look, and Wayfern (03) now owns terracotta in this set.
- **One job per colour.** Blue means "a source": citation chips and source numbers, the @mention, the drop target's dashed border, icon and title, and the logo. Every action and state is ink: the five send states, the caret, the menu check, the byline dot, the streaming pulse and bar, the upload arc, the focused composer (a 1 px ink border, no halo). Red is only on the error icon, the error title and the oversize file's size; borders around errors are grey and Retry is a neutral button. Source-type tiles are one grey; "a few minutes" is plain grey text.
- **Surfaces:** the page is `neutral.light.2` (#f4f4f4); the composer, the small cards, the menu, the error box and the drop zone are white, so the working surfaces are the brightest again.
- **Copy that named a colour:** "focus ring is the soft terracotta halo" became "focus is a 1 px ink border".
- Page-level: a `[data-theme="dark"]` override sets the focus colour to `neutral.dark.12`, because `raw.focusColor` is one value for both themes and #242424 is 1.09:1 on the dark surface (recorded as engine feedback).

**Checks:** rendered contrast 113 runs, 0 below the floor (ink 14.1:1, white on send 15.5:1, blue on its chips 9.2:1, red on white 7.2:1). Two faces as before (Newsreader, Instrument Sans), sizes 13/16/20/39. `engine.py validate`: no errors. `check_dates.py`: pass. preflight: 0 errors.

**Fresh-eyes audit:** first pass 3/5 (the composer had lost its lift, blue had about ten jobs, a periwinkle border and an invisible halo, salmon error outlines, a tinted drop zone, DESIGN.md still said "Warm tint"). Second pass 4/5 ("premium and believable, now in Margin's family"; two hues only, blue pixels down from 24,440 to 8,056); its last four notes (dark focus, the heavy 2 px ring, the blue upload arc, one periwinkle icon outline) were fixed. References: Langdock https://mobbin.com/screens/b66870ae-8d47-493d-b1b6-e6c01173ad96, Dropbox Dash https://mobbin.com/screens/536f1280-e59b-43c4-8dd0-3f0e91e15695, Google Gemini https://mobbin.com/screens/057d8ba8-d787-4612-b7ce-ea3595a984ed.

**Fresh score: 4.**
