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

## Round 3 (owner review)
**What he said:** "needs work" (the independent auditor had scored it 5). Judged by his eye and the bar he set (the B2B product screens; the Brask, Keystrata and Rallo footers), the old page was warm cream paper with oxblood, italics almost everywhere, a 248 px italic numeral as a second hero, and dotted leaders: a costume of "editorial" rather than a quiet index.

**What changed (rebuilt in place):**
- Colour, through the engine: `set dials.warmth 12`, `set raw.neutralBase '"#e4ebf1"'` (cool neutrals), then the page uses neutral step 1 as near-white paper and step 12 as ink. The brand oxblood (#7a1f1f) is unchanged and now has one job: the current issue.
- Type, through the engine: `set raw.displayFace '"Newsreader"'`, `set raw.textFace '"Inter"'`. Newsreader (roman only, no italics) sets the masthead (51 px, weight 500, optical size 72), the issue title and the piece titles; Inter sets links, labels and data. One label style: 14 px semibold.
- Structure: masthead and one-line description; the current issue (No. 23, Thresholds, 168 pages, 7 contributors, £12) with one filled Subscribe action and the next issue's date; three pieces from it on three columns with page ranges and bylines, and a link to the full contents; the newsletter as one row; four link groups, the last three on the contents' columns.
- The one object only a print quarterly would have: **the shelf**. Every issue since spring 2021 stands at the foot as a spine as thick as its page count (128 to 168 pages), its theme printed down the spine top to bottom (the British convention) and its number at the foot. A wider gap and a year mark start each year. No. 23 is the one oxblood spine, 8 px taller; No. 24 is a dashed space marked "Out 4 Dec". Hovering a spine lifts it. Tablets show Nos. 13 to 24, phones 19 to 24.
- Facts: issue numbering runs No. 1 spring 2021 to No. 23 autumn 2026; pieces open on left-hand pages (fiction 38 to 61, field notes 62 to 83); 4 December 2026 is a Friday. The colophon names the printing city, the paper (100 gsm uncoated) and the typefaces. The ISSN was removed (its check digit was wrong).

**Drafts the fresh-eyes audits turned down (15 audits):** a contents list with a page ruler (3, read as a progress bar), a flatplan strip of page cells (3, a barcode), a flatplan grid with titles placed on it (3, a second hero), a proportional ink flatplan bar (3, an uptime bar). The shelf with ink spines scored 3 twice (too tall, three stacked indexes, a striped slab), then **4** once the footer was cut to three pieces, the spines unified in ink, the labels made one style and the columns aligned.

**Type scale used:** label 12 (year marks, counts, spine numbers), footnote 14 (labels, bylines, colophon), body 16, title 21 (piece titles), headline 38 (issue title; masthead on phones), display 51 (masthead). Six sizes.

**Outside the tokens, on purpose:** 14 px (footnote role; no step in this scale); the spine heights (168 px desktop, 160 tablet) and the 8 px year gap; the 2 px spine gaps.

**Checks:** `preflight.py html`: 0 errors, 1 warning (14 px off the scale, kept). `check_dates.py --year 2026`: passes. `engine.py validate`: no errors. Contrast measured on the pixels by the auditor: muted text 7.05:1, spine text 10.6:1, current-issue spine text 7.4:1 or more, dashed outline 3.56:1. No sideways scroll at 320 to 1440 px. No invented domains on the page.

**Fresh score: 4** (fifteenth audit, against the B2B screens and the three liked footers; Mobbin references: The New Yorker https://mobbin.com/sites/sections/84724b3c-961d-4245-a46a-f176fe4bec67, Readymag https://mobbin.com/sites/sections/5bc39154-2faf-4da2-8c59-b375379c1f7b). Its follow-up notes were applied afterwards and checked by eye, not re-audited: the shelf shortened to 168 px and the repeated "SL" initials removed, piece titles to 21 px, the hidden "from £12" price fixed, one year-range format, a visible focus ring on spines, unused CSS removed. Left open: the band above the shelf is still plainer than the bar (the shelf carries the brand), and about 150 px of paper sits under Subscribe at 1440.

**Process findings:**
- The engine has no "paper" tone: near-white with a hint of hue needed `raw.neutralBase` plus picking step 1 by hand.
- Twelve of the fifteen audit rounds turned on the one ownable object; the process has no step for proposing several candidate objects before building one.

## Round 4 (18 Oct 2026): quiet footer
This replaces the round-3 design described above. The round-4 audit (`brand/showcase/AUDIT-ROUND4.md`) and the owner called the footer studies cluttered; `brand/showcase/PRESENTATION.md` now sets the footer rules. Built from one shared generator so all four keep the PRESENTATION.md footer rules: link columns in one text size, one muted heading style, one rule, one legal line, at most one signature element, and the last row of the section above (one line of real copy) so the shot reads as the end of a page. No illustrations, charts, chips, badges or boxes.

- Issue promo, contents list, newsletter and the 24-spine shelf removed (audit round 4: 'nothing leads')
- The one signature element is the masthead fitted to the content width in oxblood, the brand colour's only job
- Warm uncoated-paper ground #f5f3ee, outside the tokens on purpose (the cool neutral step read as software grey)
- Prices taken out of the links; the fourth column renamed About; column headings aligned with the issue line

**Fresh audit:** 4 of 5. **Pairwise:** won against Legora by 1 (not blind). After the audit: heading alignment (6 px) fixed after the final audit, checked by eye.

**Checks:** `preflight.py html`: 0 errors, 0 warnings. `check_dates.py --year 2026`: passes. No invented domains on the page. Two typefaces at most, sizes on the token scale.
