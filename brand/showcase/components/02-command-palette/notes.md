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
