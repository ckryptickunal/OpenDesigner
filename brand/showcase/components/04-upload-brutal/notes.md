# 04 · File upload, neo-brutalist (Halftone Yard)

## Direction
Halftone Yard is a fictional print shop for small runs: business cards, posters, zines. Customers upload print files and the shop checks them before they go to press. The look is the shop floor: newsprint paper, process inks (cyan, magenta, yellow, key black), thick black keylines, square corners, hard offset shadows that buttons slam into, registration marks, a halftone rosette and a colour control strip. The file rows read like job tickets. Feel words: **bold, loud, workmanlike** ("brutal" is not a word the engine knows).

## References (Mobbin, cited by link only)
- Whop bulk upload, https://mobbin.com/screens/80459def-95d4-4909-9e7b-8d47d7807147 : each file is its own boxed row with its state, and a finished row changes colour. Became the job-ticket rows.
- AWS S3 upload status, https://mobbin.com/screens/d0b2a1fa-99a9-4c29-ba83-f77a3f850d40 : a count of what succeeded and failed above the list, and a plain status word per file. Became "1 of 4 ready" and the status chips.
- Fireflies uploads, https://mobbin.com/screens/0e45d455-f884-44a9-8600-16830793250e : the dropzone states the accepted formats and the size limit in one line. Became the spec line under "Drop print files here".
- Figma's Shortcut editorial art, https://mobbin.com/sites/sections/d89d3841-aea4-4bc6-a310-075eb53e19db : flat process colours with black keylines and dot patterns. Taught the halftone dots and the keyline weight.

## System (engine)
- `sketch --name "Halftone Yard" --brand "#FFE500" --audience regular --platforms web --feel bold,loud,brutal --theme system-light-dark --surfaces "upload:operate" --delegated all`. Sketch turned the yellow into an olive (#847600) "so white text reads"; set back with `set raw.brandColor "#FFE500"` and `pick Q-color-01 keep-hex`. The engine then gave the yellow dark text by itself (`text.on-action` = neutral 12), which is right.
- `set raw.secondaryColors '["#00A0E3", "#E5007D"]'`: process cyan and magenta became exact `accent2` and `accent3` ramps. Found by reading engine.py; `pick Q-color-04 three` alone gave green and orange (its "triadic" is 60 degrees).
- Dials (all `delegated`): expression 90, density 55, energy 75, roundness 0, depth 8 (via Q-depth-01 borders), colorfulness 100, warmth 70 (with Q-color-09 warm, so the paper is newsprint, `accent.light.2` #f5f4eb).
- Type: `pick Q-type-08 16` (the 14 px base gave an 11 px small size again) and `set overrides.type.displayReach 5` (the operate surface capped the scale at 33 px).
- Faces: `raw.textFace Archivo` and `raw.displayFace Archivo` (one family; display uses its width axis at 125%), `raw.monoFace "Space Mono"`. Both OFL, from Google Fonts.

## Build
Everything uses `--ds-*`: inks (`accent`, `accent2`, `accent3`, `neutral.12`), paper, status colours, border widths (`border.width.4`), control sizes, type sizes, motion.

Outside the tokens on purpose:
- **The hard offset shadow** (`--hard: 6px 6px 0 0 ink`, `--hard-lg` 10 px). The engine's elevation is blurred shadows only.
- The control strip's 60% and 25% tints are `color-mix` of the inks with white: tints of real tokens, drawn as print furniture.
- The halftone rosette and registration marks are art.

Interaction: the dropzone is a focusable `role="button"` that opens a real file picker (Enter or Space), and accepts dragged files. Drag-over turns it solid yellow ("Release to upload"); a file of the wrong type turns it into a red hatch for 1.6 s, names the file in an `aria-live` message, and the good files in the same drop still upload. Uploads run on a timer one after another; each finished file says "Preflight passed". "Send to press" never disables: with a bad file it announces the reason and moves focus to "Replace file". Progress ticks redraw the list, so focus is put back on the button the keyboard was on. Buttons lift 2 px on hover and slam 6 px into their shadow on press (100 ms, enter curve); under reduced motion they do not move and the stripes stop. Render uses `?still` to freeze the timer.

## Revision for the owner's type and color rules (mid-run)
- **Two fonts, mono for data only.** The first version used Space Mono for every small label (tags, section titles, state names, chips, the shop's promise). Now Space Mono is kept only where the text is data: the job ticket (job number, quantity, paper, due time), the file spec line (formats, size limit, dpi, bleed) and each file's sizes, time left and preflight result. Every other label is Archivo 800 caps with tracking.
- **Weight on purpose.** It was Archivo 900 nearly everywhere (checklist M5, "black everywhere reads as shouting"). Now 900 is kept for the page title, the dropzone title, the ready count and the file badges; buttons and labels are 800, file names 700, body 400. The voice is still loud, but the eye now goes title, dropzone, error row, button.
- **Colour.** Already ink on newsprint with process colours at full strength; no change.
- **Type scale, named roles** (web px): label 12 (tickets, chips, data, state names), body 16 (file names, buttons), title 21 (ready count), headline 28 (wordmark, dropzone title), display 51 (page title). Five sizes, each at least 28% from the next.

## Checks
- First render: the card ran 90 px off the canvas. Fixed by making the title one line, putting the progress bar beside the name instead of under it, and fixing the row columns so every bar and chip lines up.
- Second look: the progress bars sat at different x positions (the last column changed width per row); fixed with fixed columns, and "Replace file" took the error row's status slot.
- Rag: "Drop print files / here" and "3 mm / bleed." left single words on a line; fixed with `text-wrap: balance` and non-breaking spaces between numbers and units.
- Rendered contrast: first pass 4 failures: ink on process magenta 3.37:1 (now white text, 4.52:1) and a state label hidden by a focus ring (moved down). Final: 69 text runs, 0 below 4.5:1.
- `preflight.py html`: 1 error, the same false positive as in 03: Archivo "has no @font-face" because it loads from Google Fonts and a `font-family` longhand is written (Space Mono was flagged too until its longhand class was removed). Not changed.
- `engine.py validate`: no errors, 2 warnings: yellow action colour on the paper is 1.25:1. Advisory only (WCAG 1.4.11 does not require it for a text-labelled button), and every button here has a 4 px ink border.
- Computed sizes: 12, 16, 21, 28, 51. Two faces, both loaded (Archivo variable 400 to 900, Space Mono 400/700).
- Playwright: Tab lands on the dropzone with a visible ring; a simulated drop of `cover-matte.tif` and `fonts.zip` shows drag-over, rejects the zip by name and queues the tif; "Send to press" with a bad file announces "Fix photo-lake.jpg first" and focuses "Replace file"; Replace swaps in a CMYK TIFF; focus stays on a Remove button across progress ticks; Remove updates the count.

## Process findings
1. **A yellow brand turns olive at sketch** (third piece with the brand rewrite; worst case). Bug.
2. **"Triadic" is 60 degrees.** `Q-color-04 three` on yellow gave green and orange. Bug.
3. **`raw.secondaryColors` is the right tool and nearly invisible** (one mention in zoom.md). Confusing.
4. **No hard offset shadow** in any depth model. Gap.
5. **Display reach is hidden**: poster sizes on an operate surface need `overrides.type.displayReach`, which no question asks. Confusing.
6. **11 px small size again** on an operate surface (same as 03).
7. Helped: once the brand was set right, every on-colour text came out correct by itself (`text.on-action` and `text.on-accent2` dark on yellow and cyan, `text.on-accent3` white on magenta; the badges now use those tokens), and the `border.width.4` token was exactly the keyline weight.

## Round 4 (owner review, 2026-10-15 to 2026-10-18)
**What Kunal said:** in round 3 "okay-ish, you can keep it"; on 2026-10-15, via the coordinator, "most of the web components look absolutely rubbish". The round-4 audit gave this piece 4 and "rebuild": half the frame was a spec sheet (dropzone in four states, button states, tag chips "04 · FILE UPLOAD · NEO-BRUTAL · CMYK"), crop marks, a halftone corner, a CMYK strip, offset shadows, and an error said four ways. This section replaces the neo-brutal descriptions above.

**The idea, in one sentence:** a print shop checks each artwork file against the order before it lets you send for a proof.

**What changed**
- One product moment: the "Upload artwork" dialog over order HY-4471 (500 business cards, 85 × 55 mm, 350 gsm silk, matt laminated, gold foil and spot UV on the front, $148.00 including foil), the order page behind under a light scrim and blur.
- Four files, each said once: front ready (CMYK, 342 dpi, 3 mm bleed), back uploading (64%, 11.5 of 17.9 MB), the foil layer ready with the choice to print in CMYK instead (−$38.00), and a spot UV mask that fails because it has no bleed (85 × 55 mm; it must be 91 × 61 mm). The footer says what blocks "Send for proof". `shot-ready.png` is the same dialog a minute later: all four ready, the yellow go-ahead enabled.
- Yellow (#FFE500) has one job: the go-ahead (and the logo). Removed: the spec sheet, the chips, crop marks, halftone corner, CMYK strip, offset shadows, the second face (JetBrains Mono was dropped; specs are Archivo with tabular figures). Coated profile (PSO Coated v3) to match the laminated stock, after an audit caught the uncoated profile and spot UV on uncoated board.
- Engine: monoFace `ui-monospace` (unused), base size 14, Q-color-09 cool (the yellow-tinted greys read beige), expression 35, colorfulness 30, energy 30, warmth 15, roundness 42 (6 px controls), depth 40, density 60. Brand #FFE500 unchanged.

**Type scale:** 12 (meta, tags), 14 (body, file names, buttons), 18 (dialog title), 27 (order title behind). Archivo only.

**Blind pairwise test** (opaque names, random sides, fresh judges), final version: Whop bulk upload https://mobbin.com/screens/03fc821c-eec1-4278-bf97-8f8ac202d34c ours better by 2; AirOps https://mobbin.com/screens/3c80b45c-6d21-4bd7-9e60-41ab67ef25e5 ours better by 3; Lindy https://mobbin.com/screens/7dcd57a7-d2e9-4742-bb0f-9e7b364c139b ours better by 3. 3 of 3 better. (One intermediate version lost to Whop by 3: the page behind showed through unblurred and the controls were square; both fixed.)

**Fresh-eyes audit:** 3, 3, then **4** twice ("everything round 4 flagged is gone"; "the print details are more specific than any of the three references"). Remaining notes, not fixed: the thumbnails are drawn glyphs rather than real tiny renders of the card; the blur turns the yellow logo into a soft disc; the folder name "upload-brutal" no longer describes the piece (kept, as the brief asks to rebuild in place).

**Checks:** check_dates pass; check_names 0 errors; preflight 0 errors; engine validate passes (2 warnings: the yellow primary on white has low boundary contrast, advisory for a text-labelled button).
