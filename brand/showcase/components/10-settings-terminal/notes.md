# 10 · Settings panel · rackhound

Gallery: Ackwire is a fictional on-call paging tool; an engineer drags the end of his quiet hours from 07:00 to 08:30.

## Direction
rackhound is a fictional self-hosted console for people who run a small server rack at home. Its settings panel lives in the browser but feels like a 1980s amber-phosphor terminal: mono everything, box-drawing frames, block-character switches and sliders, a tmux-style status line top and bottom, a pixel display face for titles and readouts, scanlines and a soft phosphor glow. It must still be a real, accessible settings UI: switches, segmented controls, sliders, an input, apply and revert.
Feel words: **retro, technical, nerdy** (engine: retro → heritage + playful, technical → modern + serious, nerdy → modern + playful).

## References (Mobbin, cited by link only)
- Mintlify add-ons settings, https://mobbin.com/screens/dfc67d57-50f5-473e-8567-7c1f11332e0b : group title and description on the left, rows of controls on the right, a three-state select with explanations. Taught me the label-left, control-right row with a one-line description.
- Replit user settings, https://mobbin.com/screens/093752e0-185b-45e6-b6b9-10ae944810a2 : collapsible groups, switches and a Light/Dark/System segmented control in one list. Taught me mixing switch, select and segmented rows at one rhythm.
- Customer.io experimental features, https://mobbin.com/screens/a1452449-634b-45f7-8340-447391cf7577 : each setting explains what happens when it is on. Taught me the descriptive second line under every setting.
- Magnific settings dialog, https://mobbin.com/screens/95dbaf70-750c-4ff7-bfc1-ad67e0a1c60d : a left section list with a dense right pane. Taught me the section rail.

## System (engine)
`sketch --name "rackhound" --brand "#ffb000" --audience dense --platforms web --feel retro,technical,nerdy --theme system-light-dark --delegated all --surfaces operate`, rendered with `data-theme="dark"`. Then, to get the amber back (see findings): `set dials.colorfulness 85`, `pick Q-color-01 keep-hex`, `set raw.brandColor "#ffb000" --set-by chosen`, `set raw.accentCount 1`.

| Dial | Value | Why |
|---|---|---|
| expression | 70 | a stylised terminal |
| brandPresence | 80 | the phosphor is the brand |
| density | 72 | terminal-dense rows; controls 32/40/48 |
| energy | 40 | only the cursor blinks and "applying" pulses |
| roundness | 0 | square cells, box-drawing borders |
| depth | 10 | no shadows; glow instead |
| colorfulness | 85 | needed for chroma (22 turned the amber brown) |
| warmth | 58 | warm amber |

Typefaces: `raw.textFace` and `raw.monoFace` "JetBrains Mono", `raw.displayFace "VT323"` (SIL OFL, Google Fonts), licence recorded.

## Where I stepped outside the tokens, and why
- **Phosphor colour** `--ph` is the accent ramp's LIGHT step 9 (exactly #ffb000) used in the dark theme. The dark ramp desaturates the accent to #eeb763 at step 9, which reads as beige, not phosphor.
- Secondary text is `accent-dark-solid-pressed` (#c6913a, 6.5:1) and hints/borders `accent-dark-8` (#a67931, 4.7:1): ramp steps, because the semantic text roles in dark mode are neutral greys and the whole UI is amber.
- Unlit blocks, rules and hover wash use neutral dark 6 and 3 (grey), not the brown accent steps.
- Header title VT323 at 76px and readouts at 29px: VT323 has a small x-height, so it is set larger than a sans would be; 76 is off the scale on purpose (a display moment).
- Scanlines, vignette and text glow are decorative overlays.

## Type scale (6 sizes, no two within 10%)
caption/label 12 (status lines, chip labels, hints), body 14 (setting names and descriptions, controls), unit 20 (the °C/W beside readouts), title 24 (box legends, VT323), headline 29 (slider readouts, VT323), display 76 (the "settings" title, VT323, off-token). Two fonts only: JetBrains Mono for every piece of UI text (it is all settings data and log output) and VT323 for titles and readouts.

## Owner type and color rules (checked after the rule arrived)
- Two fonts: compliant (JetBrains Mono + VT323).
- Weight: titles in VT323 regular (the face has one weight); setting names JetBrains Mono 500, selected items 700 in the inverted fill box; no bold headings.
- Highlight: the selected section and selected segment use a filled amber box with black text, not a different face.
- **Color change:** the first render used the accent's dark steps 3 and 7 (#2f2618, #614208, brown) for unlit slider blocks, the OFF switch thumb, rules and hover wash. Those were the muddy brown-on-black the rule warns about. They are now neutral dark 6 (#403f3e) and 3 (#262524), so the screen is black, grey (unlit) and bright amber (lit), with clear tonal contrast. Background is neutral dark 1 (#151515), not a warm brown-black.

## Checks
- `engine.py validate`: no errors, 7 warnings, 5 notes. Warnings: light-mode action fill #ffb000 is 1.8:1 against the base surface (advisory; it is a text-labelled button and dark text on it is 10:1), "vivid colour on a dense layout" (intended), and four "playful, serious pull X in opposite directions" macro conflicts that do not clear after setting every dial (see findings).
- `preflight.py html --medium web`: 1 error, a false positive (M9: VT323 loads from the Google Fonts link; a Playwright check confirmed both faces loaded). Two earlier warnings fixed: a `<br>` in the rack label, and −0.05em tracking on block characters.
- Contrast: phosphor #ffb000 on #151515 is 10:1, secondary 6.5:1, hints and control borders 4.7:1, danger #f19288 8:1. Unlit blocks and disabled controls are exempt (inactive). The focus ring is the token focus colour (#eeb763, 10:1).
- Targets: switches 60×28, segments 32 tall, buttons 32, inputs 36, sliders 28; all over 24px for pointer.
- Interaction: switches are `role="switch"` buttons that update their ON/OFF word and mark the row unsaved (`*`); segmented controls are radiogroups with Arrow keys; sliders are native ranges with live readouts and `aria-valuetext` ("62 degrees"); apply clears the unsaved marks. Reduced motion stops the cursor blink and the applying pulse and zeroes transitions.

## Rounds
1. The ASCII rack drawing in the header misaligned (some block glyphs fell back to another font), "10/10" read like a score, and the bottom third of the nav and settings boxes was empty.
2. Replaced the ASCII rack with a CSS rack (bays with LEDs), changed the number to "#10", added a fan-curve preview (target and current temperature marked on the curve) and UPS and config readouts to the nav.
3. Aligned the curve's axis labels to their real temperatures, stretched the log box to match the column bottoms, removed the `<br>` and the tight tracking. After the owner's colour rule: swapped brown dims for neutral greys.

## Process findings
1. **`--brand` plus `--delegated all` replaced my brand.** The sketch swapped #ffb000 for #9e6b00 ("a readable shade … (an olive)") so white text would pass, and DESIGN.md said "Picked for you, not chosen by you". The same thing changed #e8590c, #ff3d81 and #5fae7d in pieces 06, 08 and 09. Only `set raw.brandColor ... --set-by chosen` restored it, with dark text. (feedback: bug)
2. **Colorfulness mixes "how many hues" with "how saturated".** A one-hue, full-chroma brand needed colorfulness 85 plus `accentCount 1`. (feedback: gap)
3. **The dark ramp always desaturates the accent**; no option keeps brand chroma in dark mode, which neon, CRT and phosphor looks need. (feedback: gap)
4. **Macro-conflict warnings never clear** and name no command. (feedback: confusing)
5. **The light-mode contrast warning's fix would undo the brand pin.** (feedback: idea)
6. Helped: roundness 0 and depth 10 gave exactly the square, shadowless system; density 72 gave 32/40/48 controls; the reduced-motion transition tokens and focus tokens worked unchanged in a very unusual look.

## Round 3 (owner review, 2026-10-14)
**What Kunal said:** "okay, but I don't know who will use it." The earlier audit: phosphor glow and scanlines on every line, a 76 px pixel "settings" title with a cursor block, and a "#10" numeral louder than the panel.

**Who it is for now:** rackhound is the web console an ML infrastructure team uses for the GPU servers it keeps in a colocation cage. This page is the power and thermal policy for one pool (train-a: rack B2, 8 nodes, 4 GPUs each). The job is real and specific: keep the rack under the power the cage is contracted for (12.5 kW), so the team caps every GPU's power, sets the fan target, staggers power-on after an outage so the inrush stays under the breaker, and sets a lower cap for when one of the rack's two feeds drops.

**What changed:**
- **Kept:** label-left/control-right rows with a one-line consequence, block sliders and switches, the fan-curve preview, the change log, the unsaved `*` marks, the JetBrains Mono + VT323 pair, the amber brand.
- **Quieter costume:** grey text and grey frames; amber only for what is live, changed or chosen (readouts, `*`, the selected section and segments, the on switch, apply, nodes above the fan target); red only for what is over the contract or failed. The top status bar is dark with only the rackhound tag in amber; no mode line, no "tail -f", no cursor, no glow, no scanlines. VT323 is kept only for the page title (29) and the readouts (29, and the 56 px budget figure); box legends are JetBrains Mono 500 at 17. The first rebuild in this round kept the full amber costume and scored 3 ("the chrome is louder than the data").
- **Real data that re-adds:** node draws 1.48 + 1.46 + 1.49 + 1.31 + 1.47 + 1.45 + 1.28 + 1.46 = 11.40 kW. Full load = 8 x (4 x W + base), where base (CPU, memory, NICs and fans) is 290 W a node with fans at the new 62 °C target and 280 W at the old 66 °C: 11.92 kW at 300 W, 12.80 kW live now (330 W, 66 °C), 13.20 kW at 340 W. The most that fits is 318 W, so 310 W on the slider's 10 W step (12.24 kW). One alert rule: full load above 12.0 kW; it fired at 13:58 (12.8) and fires again in the error frame. If gpu-07 keeps 330 W and 66 °C after a partial apply: 7 x 1,490 + 1,600 W = 12.03 kW. Single-feed cap: one feed carries 10.5 kW; at 250 W the pool needs 8 x 1,290 W = 10.32 kW. Max fans add about 180 W across the pool. The budget meter is a continuous block bar on a 0 to 15.5 kW scale with ticks at the alert and the contract; the cage holds three racks, 12.5 + 12.5 + 6 = 31 kW contracted.
- **People and pools:** Noa Brekke is on call and named in the log, beside rackhound and the alert; pools each have their own rack and contract (train-b rack B3, infer rack B4). "Drain before maintenance" was replaced by the single-feed cap (it belongs under the scheduler).
- **Engine:** `set raw.domain "ML infrastructure: GPU servers in a colocation cage"`, `set dials.depth 4` (no glow or scanlines), rebuilt; brand #ffb000 checked. Sizes 12, 14, 17, 24 (readout units), 29, plus the 56 px VT323 budget readout (off-token on purpose: VT323 runs small). Body copy is 14 px mono: the auditor measured it legible at 13:1, below the brief's 15-17 px web body; a terminal-dense console is the exception, recorded here.
- **States, one per frame:** `shot.png` (3 unsaved changes), `shot-drag.png` (dragging the limit to 340 W: the overage is drawn red past the contract and apply is disabled with "310 W is the most that fits"), `shot-applying.png` (5 of 8 nodes done; apply and revert disabled), `shot-error.png` (7 of 8 set, gpu-07 did not answer and keeps 330 W, full load 12.03 kW trips the alert; "retry gpu-07" and "undo all"). Render with `--query state=<name>`.

**Checks:** rendered contrast: no live text below the floor (disabled buttons exempt). `check_dates.py`: pass. preflight: 0 errors, 1 warning (the 56 px readout, on purpose). `engine.py validate`: no errors (the light-mode warnings do not apply to this dark-only page).

**Fresh-eyes audit:** 3/5 ("believable job, but the costume is louder than the data, and the rack does not add up"), then 4/5 (low 4: "a believable ML-infra console; the numbers check out"); its last notes (a white over-contract figure, fan watts not counted, no feed capacity, an unclear alert rule, an empty pools box, pixel-face legends, a pale drag handle, unit spacing, "the old 330 W", the "rh" actor, a red "danger zone", the missing name) were fixed. References: Linear settings rows https://mobbin.com/screens/c968b3b2-82a5-4044-8e4a-0bec5683dec5, Dropbox Dash dark settings https://mobbin.com/screens/f2c6abf3-905c-444a-af3d-33088030cb89, Modal developer settings https://mobbin.com/screens/87b2d397-bbe1-4398-ad00-f8143c60f24f.

**Fresh score: 4.**

## Round 4 (owner review, 2026-10-15)

**What he said.** Most of the web components "look absolutely rubbish", and none should "feel like they are from a vibe coded app or a cheap Chinese app". Margin (02) is the only component he does not call ugly; the B2B product screens are the bar. In round 3 he had said of this piece: "okay, but I don't know who will use it".

**The idea in one sentence:** an on-call engineer sets how Ackwire reaches him, and sees tonight's quiet hours against his shift.

**What changed: a new concept, rebuilt in place.** The rackhound GPU-rack console answered "who uses it" for very few people, and the terminal look was optional. The folder now holds a settings dialog most engineering teams know:
- **Ackwire**, a fictional on-call paging tool, with its settings open over the incidents page (dimmed), for **Tomas** at **Fernbank Grocery**, a grocer whose services (checkout-svc, basket-api, picking-queue) page their engineers.
- The dialog (1120 × 656): the section list (your account; the team) and *Notifications*. *When you're paged*: push to your phone, a phone call after 5 minutes if a page is still open, a text message to +1 (503) 555-0148, a daily email summary to tomas@fernbank.example. *Schedule*: quiet hours on weeknights from 22:00 to 07:00, a strip from Thu 07:00 to Fri 12:00 with now (13:52) and tonight's quiet hours, and one line on the shift: Tomas is primary for checkout-svc until Mon, Oct 19 at 09:00, and after 10 minutes the policy pages Bea Ashby.
- Green (#3DD68C) means on: the switches (deeper accent step, white knob) and the quiet-hours block in the strip, which is the "on" period of the quiet-hours switch. The auditor counts that as a second job.
- Removed after the audits: an icon tile on every row, the open select menu (it hid two controls), the second strip for the on-call shift, the boxed callout, the save footer and its test-page button (settings save as they change), the pane's subtitle, the second lines on the text and email rows, the dialog's shadows (one hairline is its only depth now), the incidents column that showed past the dialog, and a to-do style check-mark logo.
- Two names changed: "Wen Ashby" became Bea Ashby ("Wen" is in `app-screens/09`), and "now" moved from 14:06 to 13:52 (14:06 is in `components/06`).

**References (Mobbin, cited by link only).**
- Notion preferences (dark), https://mobbin.com/screens/d138214d-5351-4bd6-a2bb-c7b3648ea6a5 : a dialog with grouped section nav over the dimmed app. Taught the shell.
- Perplexity preferences, https://mobbin.com/screens/27ad8f42-8906-4552-a56d-01c4c15e69dd : label and description left, control right, plain section headings. Taught the row.
- Replit settings, https://mobbin.com/screens/e2c001c6-04fa-4162-aa16-a3f89d7c7d8d : a long run of identical toggles. Taught what to avoid.

**System (engine).** Re-sketched (git keeps the old state):
`sketch --name Ackwire --brand "#3DD68C" --audience dense --platforms web --feel calm,technical,reliable --theme system-light-dark --delegated all --surfaces "console:operate"`, then `set raw.textFace "Mona Sans"`, `raw.neutralTint pure`, `raw.brandColor "#3DD68C" --set-by chosen`; dials roundness 40, depth 40, warmth 8, colorfulness 20, expression 25, energy 15 (all `delegated`); `build`. Rendered with `data-theme="dark"` (dark-only is refused by a house standard).
- Face: Mona Sans (SIL OFL), one family.
- Type scale, named roles (web px): label 12 (section labels in caps, ticks, note), body 14, title 20 (semibold). Weights 400, 500, 600.
- Outside the tokens on purpose: the 36 × 20 switch, the hatched quiet block and its 32 px strip, the scrim at 60%. The dialog's only depth is one hairline.

**Checks (final render).**
- Dates and times: Thu Oct 15 is today; Mon, Oct 19 is a Monday; the strip runs 29 hours, so now (13:52) sits at 23.7%, 22:00 at 51.7% and Fri 07:00 at 82.8%; the incident list behind runs from 13:48 today back to Oct 8. `check_dates.py --year 2026` passes.
- `check_names.py`: no collisions. New: Ackwire, Fernbank Grocery (web search found neither), Tomas, Bea Ashby. The phone number is in the 555-01xx range kept for fiction.
- `preflight.py html`: 0 errors, 0 warnings; sizes 12, 14, 17, 20.
- `engine.py validate`: no errors; 2 warnings, both for light mode (a light green button is faint on white). The piece is shown dark; recorded with `engine.py feedback`.
- Computed contrast: 45 runs, lowest 5.12:1. The app behind the scrim is context (`aria-hidden`).
- Gallery size (337 px): the eye lands on the dialog's switches and title.

**Blind pairwise test** (ours against a shipped settings dialog, sides random, fresh judges):

| Round | Version | Notion | Perplexity | Replit |
|---|---|---|---|---|
| 1 | first build | ours +1 | 0 | +3 |
| 2 | Schedule heading, labels out of the strip | +1 | −1 | +3 |
| 3 | no icon tiles, 14 px descriptions, no open menu | +1 | −2 | +3 |
| 4 | blurred backdrop, one strip, white knobs | +1 | +1 | +3 |
| 5 | no save footer | +2 | +1 | +3 |
| 6 | one hairline, fewer second lines; one judge, one pair | | +1 | |
| 7 | final (larger dialog, semibold title, destinations named, green quiet block); one judge | +2 | +1 | |

It passed every round by the rule (never weaker by 3, equal or better at least twice), but it was the closest piece: Perplexity beat it twice, on weak separation from the page behind and a timeline of flat grey slabs. Both were fixed in round 4.

**Fresh-eyes audit:** round 1, 3 (icon tile on every row, 12 px descriptions, the menu hiding two controls); round 2, 3 (flat hierarchy, an on-call bar with no information, dark switch knobs); round 3, 3 (three heading levels, four depth effects on the dialog, the strip repeating its row; addressed); round 4, 3 ("the closest to a 4": stock dark dialog, dialog about 52% of the frame, title outweighed by the section headings; addressed); final, **3.5**, still the closest to the bar.

**Result: fails the fresh-eyes bar after four rounds, honestly reported.** It wins or ties every blind pairing except two narrow losses to Perplexity (by 1 and 2, both before round 4), and the final auditor scores it 3.5: a resting state with nothing being changed, the dimmed page shows no useful context (the acknowledged #2214 sits behind the dialog), and green does two jobs. Next steps: show one setting mid-change (the quiet-hours end time being dragged on the strip), and place the dialog so the acknowledged incident stays visible.

## Round 5 (owner hid it until better, 2026-10-18)
**What Kunal did:** he hid the piece "until better": it had won its blind test in round 4, but the fresh reviewer stayed at 3.

**The idea, in one sentence:** an on-call engineer is dragging the end of his quiet hours from 07:00 to 08:30, and sees what that changes.

**What changed**
- The settings page itself, not a dialog over a dimmed incidents page: a settings sidebar (back to Incidents, your account, Fernbank Grocery) and the Notifications pane, so there is no context that adds nothing.
- Mid-change: quiet hours come first. The strip (Thu 07:00 to Fri 12:00, now 13:52) shows the end handle held at Fri 08:30 with its tooltip, the old end as a dashed line at 07:00, the heading "Weeknights 22:00 to 08:30, was 07:00", and what it changes: "90 more quiet minutes each weekday morning: low-urgency pages from 07:00 wait until 08:30. Last week, 4 did."
- Green has one job: the 90 minutes being added. Switches are monochrome (white when on); the quiet block, the handle and the logo are neutral (the logo's green dot is gone).
- Small fixes: the email summary moved to 09:00 (08:00 would fall in the new quiet hours); the on-call line is one sentence; Bea Ashby is never split across lines.

**Type scale:** 12 (ticks, group labels), 14 (body; section headings semibold), 20 (title). One face, Mona Sans. A 16 px heading was tried, but the system has no 16 px token, so the CSS now says the 14 px that renders.

**References (Mobbin, cited by link only; used for the blind test):**
- Devin settings, https://mobbin.com/screens/93170d84-7435-4c89-82b5-647330913aba : a dark settings page with a back-to-app sidebar; taught the page shell.
- Buffer notification settings, https://mobbin.com/screens/212b19ca-47d0-4574-aa67-6de419f6eb94 : grouped settings nav and rows with switches; what a long run of toggles looks like.
- hilos preferences, https://mobbin.com/screens/2d37f928-46b4-47e7-98e2-434cb772354c : a settings dialog over the app; what the dimmed context costs.

**Blind pairwise test** (ours minus shipped, 1 to 5; neutral file names, random sides, no labels; one fresh judge saw all the round's pairs):

| Round | Version | Devin | Buffer | hilos |
|---|---|---|---|---|
| 1 | settings page, quiet hours being dragged, neutral hatch, green switches | +1 | +1 | +1 |
| 2 | green only for the added 90 minutes, white switches, flat quiet block | +1 | +1 | +1 |

**Fresh-eyes audit:** round 1, 3.5 (green on the switches instead of the change, the change not drawn, low tonal contrast; addressed); round 2, **4** (the eye lands on the "Fri 08:30" tooltip and handle; remaining: the empty daytime part of the strip, the added 90 minutes could be louder, three white switches). Stopped after round 2.

**Result: 4 from the round 2 fresh auditor, and it passes the blind test (+1, +1, +1); stopped at round 2.** All dates check: Thu Oct 15, Fri Oct 16, Mon Oct 19, 2026, and the strip positions match their times.

**Checks (final render):** check_dates `--year 2026` passes; check_names 0 errors (the NEW words it lists are dictionary words, key names or the typed query); preflight 0 errors, 0 warnings; engine validate no errors (light-mode warnings as before); computed contrast of every HTML text run 4.6:1 or more.
