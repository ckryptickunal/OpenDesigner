# 05 Salt Ledger: editorial magazine index footer

## Direction
Salt Ledger is a fictional independent print quarterly from Leith, Scotland: essays, fiction and field notes about place, work and weather. Its website footer is set like the contents page of the printed issue: a double rule, a running head, a huge italic issue number in oxblood, and the site's sections as a numbered table of contents with dotted leaders and page numbers. One serif family, warm uncoated-paper ground, ink and one oxblood.
Feel words: classic, literary, refined.

## References (Mobbin, structure only)
- https://mobbin.com/sites/sections/84724b3c-961d-4245-a46a-f176fe4bec67 — a magazine footer groups its sections under one small label and keeps the seal or masthead to one side; type does all the work.
- https://mobbin.com/sites/sections/3ecc4297-ecf4-443f-b298-99eb8a972b6c — an index set as dense lists still reads calmly when the rhythm (label, entries, gap) is strict.
- https://mobbin.com/sites/sections/5bc39154-2faf-4da2-8c59-b375379c1f7b — thin rules under each column label instead of boxes.
- Mobbin had no real contents-page footer; the dotted leaders, roman section numbers and page numbers come from print practice, not from a reference.

## System (engine)
```
python3 $E --dir .../05-salt-ledger-index/opendesigner sketch --name "Salt Ledger" --brand "#7a1f1f" --audience regular --platforms web \
  --feel classic,literary,refined --theme system-light-dark --delegated feel,audience,platforms,theme,surfaces --surfaces "magazine:read"
```
- "literary" is not a known feel word and was left out.
- Dials: expression 72 (the numeral and the contents list are the art), brandPresence 55 (masthead and oxblood only), density 58 (a contents page is dense but orderly), energy 22 (slow), roundness 0 and depth 0 (print: rules, no shadows), colorfulness 18 (ink, paper, one oxblood), warmth 72 (warm paper).
- `set raw.neutralBase '"#efe6d4"'` for paper-tinted neutrals; the page uses neutral step 3 (#efebe4).
- `set raw.marketingSurfaces true` (a "read" surface again capped type at 38 px).
- `set raw.textFace '"Newsreader"'` (SIL OFL, optical sizes 6 to 72) and `raw.fontLicence` recorded.
- Build: no errors, 0 warnings.

## Build
- All colours, spacing, sizes, rules, focus and motion are tokens. Entries are `--ds-font-size-21`, notes and page numbers 16, labels 12 tracked uppercase, theme 38.
- Outside the tokens, on purpose: the issue numeral at 248 px (180 on phones), weight 250, tracking -0.04em (marked `od-ignore`); old-style figures and tracked labels (`font-variant-numeric`, letter-spacing), since there is no token for figure style; the dotted leader is a 6 px radial-gradient pattern in neutral step 9.
- The theme title "Thresholds" uses weight 400 italic, not the 600 heading weight: editorial italics carry the voice.
- Accessibility: contrast on #efebe4: ink 13:1, secondary #5d5649 6.1:1, tertiary 5.0:1, oxblood 8.7:1. Each entry is a link at least 40 px tall (36 px on phones). The numeral is `aria-hidden` with an aria-label on its paragraph.

## Renders
- `shot.png`: 1440 wide, natural height (661 px), scale 2. `shot-mobile.png`: 390 wide.
- Round 1: rendered at an 800 px viewport, which left 160 px of empty paper; the colophon's ISSN wrapped onto its own line, and the copyright sat higher than the legal links. Rendered at natural height, moved the copyright into the colophon sentence, removed a stray max-width.
- Round 2 (mobile): the Fiction subtitle wrapped and squeezed its leader to four dots. Subtitles are hidden on phones.

## Checks
- `preflight.py html`: 1 error (the Google Fonts false positive), 1 warning (-0.04em on the numeral; at 200% the 2 and 3 do not touch). It read only the two px numeral sizes.
- `engine.py validate`: passes. `engine.py review`: clean after `od-ignore` on the two numeral sizes.
- Checklist: sizes 12, 16, 21, 28, 38 plus the numeral; every edge on the 12-column grid; the vertical rule ends with the content; no wraps at 390.

## Owner type and color rules (applied mid-run)
- Fonts: one (Newsreader).
- Type scale (named roles): label 12 (tracked uppercase), body 16, title 21 (contents entries, masthead, subscribe), headline-sm 28 ("No."), headline 38 (issue theme), display 248 (the issue numeral, art; 180 on phones). Six steps.
- Italics reviewed: no heading uses the one-italic-word trick. The whole issue theme ("Thresholds") and the masthead are italic as a style, and the italic subtitles in the contents are titles of works (a print convention). No change.
- Color: warm paper with near-black ink (13:1) and oxblood (8.7:1); no light-on-brown. No change.

## Process findings
1. "literary" is not a feel word (feedback: idea).
2. `raw.neutralBase` sets only hue; no "page tone" answer for paper or cream grounds (feedback: gap).
3. No token for figure style or small caps (feedback: gap).
- Helped: `od-ignore` is a clean way to keep a deliberate raw value and still get a clean `review`.
