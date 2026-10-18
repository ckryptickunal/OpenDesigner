# 02 · Command palette (Margin)

## Direction
Margin is a fictional writing tool for novelists: one long manuscript, many drafts, a lot of keyboard. The palette is the fastest way around, so it is quiet, exact and monochrome: paper, ink and 1 px rules, no hue at all. The sheet is drawn like a manuscript page with margin notes, because the brand is about margins. Feel words: **minimal, quiet, literary**.

## References (Mobbin, cited by link only)
- Juicebox command menu, https://mobbin.com/screens/2af813bf-0129-45d1-81ed-069edee76e16 : a 2 px bar on the left edge marks the selected row, and the footer names each key in a keycap. Both kept, in ink instead of colour.
- Supabase command menu, https://mobbin.com/screens/9b4725f5-e038-4fc7-98ad-64a59f74b4d7 : spaced caps group labels and small keycaps on the right. Taught the label rhythm.
- Evernote quick search, https://mobbin.com/screens/46926538-2111-4bed-8396-4db69c067660 : the matched part of each title in bold and a quiet location label after the title. Became the match style and the "Salt Road / Ch. 3" path.
- Langdock search, https://mobbin.com/screens/9c45e8ef-bc96-4b1c-bd22-f49b9118a7c3 : groups with a count. Kept the count on the right of each group label.

## System (engine)
- `sketch --name Margin --brand "#1A1A1A" --audience regular --platforms web --feel minimal,quiet,literary --theme light-dark-toggle --surfaces "editor:operate" --delegated all`.
- Dials (all `delegated`): expression 22 (a tool, no hero), density 62 (14 px body, 44 px rows), energy 15 (still), roundness 22 (2 px controls, 12 px panel), depth 22 (hairline ring plus one soft shadow), colorfulness 0 (monochrome), warmth 40.
- Q-color-09 pure (no tint).
- Faces: `raw.textFace "IBM Plex Sans"`, `raw.displayFace Newsreader`, both SIL OFL from Google Fonts. `raw.monoFace "IBM Plex Mono"` was set and used at first; removed from the page after the owner's two-font rule (see below).
- The scale came out 12 / 14 / 17 / 20 / 24 / 29 / 35, which is right for a dense tool.

## Build
`index.html` uses `--ds-*` for every colour, size, radius, shadow and focus value in the palette. The dark sample is the same markup inside `data-theme="dark"`, so the tokens switch on their own.

Outside the tokens on purpose:
- The paper veil over the manuscript (`rgb(253 253 253 / .72)`): the alpha neutrals are all ink-tinted, so there is no white veil.
- One extra shadow layer under the palette (`0 32px 64px -24px`) on top of `elevation.overlay`, so it lifts off a white page.
- The sheet's layout (absolute positions of the editor, notes and states column) is presentation, not component.

Interaction: the input is a combobox with `aria-activedescendant`; arrow keys move the selection, Enter runs, Escape clears. Matching is a real fuzzy match (best placement of the letters, rewarding word starts and runs), so the highlights on screen come from the code. Nothing animates: the house standards say a palette opened 100+ times a day, and keyboard moves, get no motion (STD-when-to-animate-05, -06). The settings row is a switch that flips with Enter.

## Revision for the owner's type and color rules (mid-run)
- **Two fonts.** The first version used three: IBM Plex Sans, IBM Plex Mono (group labels, paths, keycaps, margin notes) and Newsreader (manuscript, wordmark). The mono text was labels, not code, so it is now Plex Sans: group labels in 600 spaced caps, keycaps in 500, numbers with tabular figures. Newsreader stays because the page behind the palette must read as a manuscript.
- **Highlight by weight.** The fuzzy match was already weight 600 plus a hairline underline, which the new rule allows; no change.
- **Colour.** Monochrome ink on paper already has the strongest tonal contrast; no change.
- **Type scale, named roles** (web px, Material 3 names): label 12 (group labels, keycaps, paths, notes), body 14 (result rows), body-lg 17 (the query input), title 20 (manuscript text), headline 24 (wordmark), display 35 (chapter title). Six sizes, each at least 16% from the next. Titles are regular weight on purpose: the chapter title is Newsreader 400 and the wordmark 500; a quiet writing tool should not shout.

## Checks
- `preflight.py html`: first run 1 error (10 px digits in the note markers), fixed to 12 px. Now 0 errors, 0 warnings.
- `engine.py validate`: no errors, no warnings.
- Rendered contrast (text hidden, background measured): 126 text runs, 2 below 4.5:1, both in the "disabled" sample row (3.55:1). Inactive controls are exempt under WCAG 1.4.3; said here on purpose. The manuscript under the veil is decorative (`aria-hidden`) and also exempt.
- Computed sizes: 12, 14, 20, 24, 35 on text, plus 17 in the input (all from the scale). Two faces, both loaded (Plex Sans 400/500/600, Newsreader 400/500).
- Keyboard test (Playwright): focus starts in the input; "shrev" gives 5 results; two ArrowDowns select the third row and set `aria-activedescendant`; Enter on the switch row turns it off; "qzxv" shows the empty state; Escape restores all 13 rows.
- `review`: 42 findings, almost all the sheet's absolute layout (left: 48px, top: 80px) mapped to space tokens; 2 ask to rebuild the dialog on base-ui or Radix (this page has no stack).

## Process findings
1. **The house standards did the motion design.** STD-when-to-animate-05 and -06 settled "no motion" for a palette at once; without them I would have added a 150 ms scale-in. This is the process at its best.
2. **The scale was right for once.** Expression 22 and density 62 gave 12 / 14 / 17 / 20, exactly what a dense palette wants (compare 01, which had no 14).
3. **Near-black brand collapses the ramp:** accent 10, 11 and 12 are all black. Bug, recorded.
4. **No white veil token** for light-mode overlays. Gap, recorded.
5. **review pushes React libraries on a plain-HTML page**, and cannot tell page layout from component CSS. Recorded.
6. The feel word "literary" was unknown; the engine said so and carried on, which is the right behaviour.

## Round 4 (owner review, 2026-10-15)

**What he said.** Most of the web components "look absolutely rubbish"; Margin is the only one he does not call ugly. The brief for this round: don't rebuild it, run the blind pairwise test, and if it shows spec-sheet framing or fails, polish only what is needed and keep what he liked. AUDIT-ROUND4 also asked whether it should be cropped to the palette in its app.

**The idea in one sentence:** a novelist types "shrev" and the palette finds both commands and drafts.

**Blind pairwise test on the piece as it was** (ours against a shipped command palette, sides random, fresh judges): Magnific, ours weaker by 3; Mintlify, ours better by 2; v0, ours weaker by 2. It failed (clearly weaker once, equal or better once). Every judge named the cause: it read as a spec sheet. Two judges also said the palette itself was the better-made one.

**What changed (the framing, and small polish to the palette).**
- Removed: the header tags ("02 · Command palette · ⌘K anywhere · Monochrome · 1 px rules · 2 faces"), the five numbered margin notes with leader lines, the states column (row, query, keycaps, footer, dark) and the footnote citing STD-when-to-animate. Their CSS went with them; the old sheet stays in git.
- Added: Margin's own chrome. The binder on the left (the mark, *The Salt Road · draft 4*, chapters 1 to 5 with word counts, two notebook pages) and chapter 3 filling the editor. A white veil at 64% covers the whole window, so the palette reads first.
- The palette: 640 px wide (was 560), placed over the manuscript column so no line peeks out beside it, and its bottom edge falls between two paragraphs.
- Kept exactly: the scope chip, "shrev", the spaced-caps group labels with counts, the 2 px ink rule on the selected row, the switch row, the footer with every key in a keycap, "5 results", IBM Plex Sans with Newsreader, monochrome, and every behaviour in the script.
- Polished after the fresh audit: matched letters are marked by weight only (the underline went); row shortcuts are set as quiet glyphs (⌥⌘R), so only the footer and esc carry keycaps; ⌥⌘H, which clashes with macOS Hide Others, became ⌥⌘R; section break moved to ⇧⌘↵ so ⌘↵ means only "open beside"; the drafts show word counts (640 w, 1,312 w) instead of "edited 2 d" and a count equal to the whole chapter; "Shipwreck scene" became "Shore lamp scene" so it no longer sits in chapter 3 while chapter 4 is "Wreck season"; the revision rule on the first paragraph went, because it peeked out beside the palette.

**Checks (final render).**
- `check_dates.py --year 2026`: passes.
- `check_names.py`: no errors. New titles: Low water, The salt pans, Wreck season, Lamps out (chapters), Workshop comments (a notebook page), Shore lamp scene (a draft). ArrowDown, ArrowUp, Bible and The are words or key names.
- `preflight.py html`: 0 errors, 0 warnings; sizes 12, 14, 17, 20, 35.
- Computed contrast: 38 runs outside the decorative manuscript, lowest 5.92:1. The manuscript and binder are context behind an open dialog (`aria-hidden`).
- Gallery size (337 px): the eye lands on the palette and its selected row.

**Blind pairwise test after the polish:**

| Round | Magnific | Mintlify | v0 |
|---|---|---|---|
| 1 (the spec sheet) | ours −3 | +2 | −2 |
| 2 (in its app) | +3 | +2 | +2 |
| 3 (veil over the window, glyph shortcuts) | +2 | +3 | +2 |
| 4 (final) | +2 | +3 | +2 |

**Fresh-eyes audit:** round 1, 3.5 (half-window veil, keycap clutter, match marked twice, off-centre); round 2, 4; round 3, **4**. Remaining notes from that audit, left for the owner because they touch what he liked: the palette covers about 22% of the frame, the black switch outweighs the selected row, and the query has no visible caret.

**Result: passes both tests.**
