# 07 · AI composer · Oriel

Gallery: Oriel is a fictional research assistant for historians; typing @harb opens its source picker mid-question.

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

## Round 4 (owner review, 2026-10-15)

**What he said.** Most of the web components "look absolutely rubbish", and none should "feel like they are from a vibe coded app or a cheap Chinese app". Margin (02) is the only component he does not call ugly; the B2B product screens are the bar. The round 3 audit had scored this piece 4; his verdict overrules it.

**The idea in one sentence:** a historian cites a source mid-question by typing "@harb" and choosing the harbour board minutes.

**What changed.** The brand and its job stay (Oriel reads your sources and cites every claim). The presentation was rebuilt three times in this round:
1. The component sheet went: the "NO. 07 Composer" masthead, "COMPONENTS · AUTUMN 2026", the grid of six send-button states, the italic serif state labels and the empty, streaming, error and drop panels.
2. First rebuild: a new thread with the composer centred and the model menu open. Judges preferred it to every reference, but the fresh audit (3) called it the stock AI start page with an empty top third, and AUDIT-ROUND4 named Claude Projects as the look it echoed.
3. Second rebuild: the thread with the composer docked. The audit (3) said the 17 px serif answer, not the composer, drew the eye.
4. Now: yesterday's question and the end of its answer as quiet context (body size, secondary ink, one line naming its sources), and the composer as the subject: "Who did the board let dredge the flats, and when? Quote each minute with its date from the @harb", with the source picker open at the @ (three matching sources, with pages and whether Oriel has read them; the chosen one tinted), two attached sources under the text, the reading depth ("Careful reading") and send. One secondary state, in place.
- One typeface (Onest); Source Serif 4 is gone, because a serif answer is another product's signature and it was used for one element.
- Ink blue keeps one meaning, a source, and appears only on the typed "@harb" and the chosen picker row (tinted). Citations, chips and every action are grey or ink.
- Depth: one technique, a soft shadow, on the two floating parts only (the composer and the picker). Everything else is flat fills: no borders on the sidebar, top bar, search, chips or buttons. Icon tiles are gone; icons stand alone.
- Removed as clutter: the Copy and Add to notes row, the footnote under the composer, the "Research" mode (it did the same job as the reading depth), the hint line, the project name repeated in the top bar.
- Fixed facts: the answer's last claim now carries its citation (Keller, p. 112, in a 248-page book); sources keep one name everywhere (Tidal Commons, Saltings interviews); the 24-page minutes became 212 pages; "Kestrel" (also a workspace in `app-screens/09`) is no longer used; "Fisheries Act 1951" became "Harbour by-laws, 1929", so no real law is named.

**References (Mobbin, cited by link only).**
- Dropbox Dash, https://mobbin.com/screens/536f1280-e59b-43c4-8dd0-3f0e91e15695 : attachments and a menu tied to the composer. Taught how a menu opens without hiding the prompt.
- Langdock, https://mobbin.com/screens/e8b4319b-3d79-4dcd-b49f-7370ccf89b29 : one toolbar row (add, tools, model, send). Taught the toolbar order.
- Notion AI, https://mobbin.com/screens/58188761-2d93-43a2-be51-df5fee96707a : the composer as the calm centre of the page. Also showed what to avoid: a duplicated model list and a logo strip.

**System (engine).** Re-sketched for a dense work tool (git keeps the old state):
`sketch --name Oriel --brand "#2B4C8C" --audience dense --platforms web --feel calm,focused,refined --theme system-light-dark --delegated all --surfaces "app:operate"`, then `set raw.textFace "Onest"`, `raw.displayFace "Onest"`, `raw.neutralTint pure`, `raw.brandColor "#2B4C8C" --set-by chosen`; dials roundness 50, depth 28, warmth 12, colorfulness 22, expression 30, energy 18, brandPresence 35 (all `delegated`); `pick Q-ai-01 chat`; `build`.
- Type scale, named roles (web px): label 12, body 14, prompt 17. Weights 400, 500, 600.
- Outside the tokens on purpose: the two shadows (the engine's elevation tokens pair a ring with the shadow), the text caret, the picker's position at the @.
- Tabular figures were removed: in Onest they spaced every "1" (recorded with `engine.py feedback`).

**Checks (final render).**
- `check_dates.py --year 2026`: passes (no weekdays; "Read Oct 9" and "Read Oct 2" are before today).
- `check_names.py`: no errors. New titles: Saltings estuary study, the five recent threads, Harbourmaster's day book and Harbour by-laws, 1929 (added to NAMES.md). The reading models Wren and Heron are no longer on the page. "Harb" and "Esc" are a query and a key.
- `preflight.py html`: 0 errors, 0 warnings; sizes 12, 14, 17; one face.
- `engine.py validate`: no errors, 0 warnings.
- Computed contrast of every text run: 58 runs, lowest 4.96:1.
- Gallery size (337 px): my eye lands on the picker and the composer; the final auditor's landed on the black send button and the logo (see the result below).

**Blind pairwise test** (ours against a shipped composer, sides random, fresh judges with no context; each judge saw one pair per piece):

| Round | Version | Dropbox Dash | Langdock | Notion |
|---|---|---|---|---|
| 1 | centred composer, model menu | ours +2 | +2 | +2 |
| 2 | same, stage raised | +3 | +2 | +2 |
| 3 | thread with docked composer | +3 | +2 | +2 |
| 4 | answer tail, source picker open | +3 | +2 | +3 |
| 5 | one face, clutter removed | +2 | +2 | +2 |
| 6 | sources as one line, no tiles; one judge, one pair | +2 | | |
| 7 | final (one depth technique, tinted picker row); one judge | | +2 | +2 |

Passes in every round: never clearly weaker, better in all three.

**Fresh-eyes audit:** round 1, 3 (empty start page, two controls for one job, mixed units); round 2, 3 (composer not the subject, accent used eight times, serif answer); round 3, 3 (a page-count contradiction, sources shown twice, grey tiles everywhere; fixed); round 4, 3 (component about 23% of the frame, popover white on white with two depth effects, accent nearly gone; addressed); final, **3** (the composer and picker still fill about a quarter of the frame, the stock AI-app layout, a prompt that compared the minutes with themselves, now reworded).

**Result: fails the fresh-eyes bar after four rounds, honestly reported.** It wins every blind pairing in seven rounds, but the fresh auditors score it 3 four times running: at 1× the composer and picker fill about a quarter of a 1440 × 900 frame, and the layout (sidebar, thread, rounded composer, round send) reads as the stock AI-app pattern. More polish is not moving it. What would: a crop to a smaller viewport so the composer fills the frame, or a structure of its own (for example the source picker as a side panel with the page being cited).

## Round 5 (owner hid it until better, 2026-10-18)
**What Kunal did:** he hid the piece "until better": it had won its blind test in round 4, but the fresh reviewer stayed at 3.

**The idea, in one sentence:** a historian cites a source mid-question by typing "@harb" and choosing the harbour board minutes.

**What changed**
- A tighter viewport: the page is shown in a 960 × 600 window rendered at 3× (`shot.py ... --w 960 --h 600 --scale 3`, so shot.png is still 2880 × 1800). At this width the sidebar folds into a button, and the composer and its picker fill most of the frame at their real size (PRESENTATION rule 4: render a smaller viewport rather than shrink).
- A structure of its own: the source picker has two panes. The matches for "harb" on the left (three sources, with pages and whether Oriel has read them); on the right, the chosen source as the record office lists it: "Minutes of the harbour board, 1931 to 1938", its catalogue entries that mention dredging (12 Mar 1931, p. 14; 3 Oct 1934, p. 96, the minute Keller cites; 9 May 1936, p. 141), and "Not read yet: about 2 minutes to read all 212 pages."
- Context reduced to one dimmed line of the last answer (secondary grey, 4.6:1); the question bubble, the sources line and the sidebar are gone; Share is an outline button.
- Ink blue still means a source: the typed @harb, the chosen row and the 1934 entry. A pages-by-year bar chart was tried in round 1 and replaced (auditors read it as decoration, then as loading placeholders).
- Fixes: the citation in the tail is numbered 1 (it read 2 before 1); its chip text is secondary grey (the dimmed grey was 3.9:1); the caret blinks only after 3 s, so renders always show it.

**Type scale:** 12 (labels, meta), 14 (body), 17 (prompt). One face, Onest.

**References (Mobbin, cited by link only; used for the blind test):**
- Dropbox Dash, https://mobbin.com/screens/536f1280-e59b-43c4-8dd0-3f0e91e15695 : a menu tied to the composer that does not hide the prompt.
- Gumloop model picker, https://mobbin.com/screens/a3f8b130-cfc5-4ddc-8fd9-b95a4a6927bf : a picker with a detail pane beside the list; taught the two panes.
- Microsoft Copilot composer, https://mobbin.com/screens/2ff3d94d-adb2-4937-818d-de633b9757c3 : attachments as cards above the prompt; what the stock composer looks like.

**Blind pairwise test** (ours minus shipped, 1 to 5; neutral file names, random sides, no labels; one fresh judge saw all the round's pairs):

| Round | Version | Dropbox | Gumloop | Microsoft |
|---|---|---|---|---|
| 1 | 960 × 600 at 3×, two-pane picker with pages by year | +2 | +2 | +1 |
| 2 | dimmed tail, tinted bars | +2 | +3 | +1 |
| 3 | catalogue entries instead of the chart | +2 | +2 | +1 |

**Fresh-eyes audit:** round 1, **4** (the blue bar outshouts the idea, the context not dimmed, everything labelled; addressed); round 2, 3.5 (the 3× render reads larger than its siblings, bars like loading placeholders, a stock composer; the chart replaced); round 3, **4** (passes, narrowly: a dead band under the one-line tail, three depth cues, why 1934 is blue is not said).

**Result: 4 from the final fresh auditor; passes both tests.** Two of three auditors scored 4; the one at 3.5 objected mainly to the 3× render (one presentation per category, rule 8), which the owner asked for. It wins every blind pairing in all three rounds. Not changed after the last audit: the gap under the tail and the stock composer chrome.

**Checks (final render):** check_dates `--year 2026` passes; check_names 0 errors (the NEW words it lists are dictionary words, key names or the typed query); preflight 0 errors, 0 warnings; engine validate no errors (light-mode warnings as before); computed contrast of every HTML text run 4.6:1 or more.
