# 07 Sasame: Japanese-minimal tea house footer

## Direction
Sasame (茶房 ささめ) is a fictional eight-seat tea house in Kanazawa's old quarter. The footer is quiet and mostly paper: on the left, the name, one sentence, and three small notes (visit, hours, a seasonal note for October about the first hōjicha roast); on the right, a hanging-scroll moment: a brush ensō, a vertical line of place names, and a vertical phrase, 一服の、静けさを。("a bowl's worth of stillness"), signed with a vermilion seal. A pale celadon paper ground with a faint fibre texture (first warm washi; changed under the owner colour rule), sumi ink, matcha for the kanji labels, one red seal.
Feel words: calm, quiet, timeless.

## References (Mobbin, structure only)
- https://mobbin.com/sites/sections/471f17eb-e5b3-4785-8cd9-333119653eac — a Japanese brand footer that is almost empty: tracked small capitals, a JA / EN switch, no boxes.
- https://mobbin.com/sites/sections/6ecba422-fe26-482b-8225-8e24ec959d84 — a café footer led by contact, hours and "find us", plus one hand-drawn mark as the only image.
- https://mobbin.com/sites/sections/e4b43a6b-b75a-4564-8573-10742b5e5911 — one calligraphic line carries the whole footer's character; everything else steps back.

## System (engine)
```
python3 $E --dir .../07-sasame-tea/opendesigner sketch --name "Sasame Tea House" --brand "#5f6b3d" --audience regular --platforms web \
  --feel calm,quiet,timeless --theme system-light-dark --delegated feel,audience,platforms,theme,surfaces --surfaces "tea house site:experience"
```
- Dials: expression 55 (one scroll-like moment, otherwise silence), brandPresence 35 (a small seal), density 12 (ma, generous air), energy 8 (still), roundness 0, depth 0, colorfulness 18 (sumi, matcha, one red), warmth 70 (washi).
- `raw.neutralBase "#ece4d3"` (washi), `raw.accentCount 2` + `raw.secondaryColors ["#b4432c"]` (seal vermilion as accent2), `raw.textFace "Shippori Mincho"` (SIL OFL), `raw.scripts ["Latn","Jpan"]` (added a `:lang(ja)` line-height scale), `raw.fontLicence` recorded.
- Build: no errors, 0 warnings.

## Build
- Tokens for colour (neutral step 3 washi, step 12 sumi, accent 9 matcha, accent2 9 seal), sizes (13, 16, 25, 39, 49), spacing, focus.
- Outside the tokens, on purpose: a Japanese serif fallback stack added by hand (the engine's stack falls back to sans and has no Japanese faces); `writing-mode: vertical-rl` and the vertical tracking (no token for vertical text); the seal's 3 px corner and double inner edge (`od-ignore`); the 6 px seasonal dot; the washi texture and the brush ensō are SVG (the ensō is a generated tapered path with a turbulence displacement and a dry-brush layer).
- Accessibility (first version, warm washi): sumi 13:1, secondary 6.1:1, matcha labels 4.8:1, white on the seal 4.6:1; see the owner-rules section for the celadon values. Japanese runs carry `lang="ja"`; the poem has an English aria-label; the seal and ensō are decorative. Links are at least 24 px tall.

## Renders
- `shot.png`: 1440 wide, natural height (725 px), scale 2. `shot-mobile.png`: 390 wide.
- Round 1: the small vertical place-name line ran through the ensō's stroke, and the poem's wide tracking made the footer taller than its content, leaving a dead band above the legal row. Put ensō, place names and poem in one row with fixed gaps; tightened the poem's tracking from 0.32em to 0.2em.
- Round 2: the ensō was an even ring with two round caps, which read as a drawn circle, not a brush. Replaced it with a tapered path (swells, then thins to a dry tail). On phones the ring overlapped the poem; it now sits on the left and the poem on the right.

## Checks
- `preflight.py html`: 1 error (Google Fonts false positive), 1 warning (`<br>` in the address and hours, which are addresses, not headings).
- `engine.py validate`: passes. `engine.py review`: 2 raw values left (the 6 px dot).
- Checklist: sizes 13, 16, 25, 39, 49 from one scale; the left block and the scroll each sit in a clear box; the empty space is deliberate and under a quarter of the frame.

## Owner type and color rules (applied mid-run)
- Fonts: one (Shippori Mincho, with Japanese system Mincho fallbacks).
- Type scale (named roles): label 13 (tracked uppercase), body 16, title 25 (kanji labels), headline 39 (wordmark), display 49 (vertical phrase). Five steps.
- Titles are not bold: the wordmark is 500 and the phrase 500. No highlight is used.
- Changed (colour): the warm washi ground (neutralBase #ece4d3, warmth 70) made this piece read as a sibling of piece 05 (cream paper, dark serif, red accent), and its greys were brownish. Now `set raw.neutralBase '"#d9e2cf"'` and `set dials.warmth 45`: a pale celadon ground (neutral step 4, #e0e4db) that belongs to tea, with sumi at 12:1 and secondary text at 5.6:1. Matcha is 4.5:1 on the new ground, so it stays on the 25 px kanji labels (large text) and the "Directions" link moved to accent step 11. The paper texture was re-tinted green-grey.

## Process findings
1. The fallback stack ignores the face's class and the page's scripts (feedback: bug).
2. No vertical writing support (feedback: gap). The `:lang(ja)` line-height scale is a good start.

## Round 4 (18 Oct 2026): quiet footer
This replaces the round-3 design described above. The round-4 audit (`brand/showcase/AUDIT-ROUND4.md`) and the owner called the footer studies cluttered; `brand/showcase/PRESENTATION.md` now sets the footer rules. Built from one shared generator so all four keep the PRESENTATION.md footer rules: link columns in one text size, one muted heading style, one rule, one legal line, at most one signature element, and the last row of the section above (one line of real copy) so the shot reads as the end of a page. No illustrations, charts, chips, badges or boxes.

- The tea-year Gantt, seal, today line and every chart label removed
- The one signature element is a seasonal sentence in Shippori Mincho beside the name, at 49 px so it reads at gallery size
- Visit, Hours, Seats and More as four quiet columns; headings muted, links no longer underlined, the address reduced to 'Higashiyama 2-chome' so it cannot match a real house
- Last row of the section above: 'Ask for a seat'

**Fresh audit:** 3 of 5. **Pairwise:** lost to VanMoof by 2 (not blind); the earlier blind test lost to Legora by 4. After the audit: all four of the final audit's Sasame fixes (muted headings, no underlines, 49 px statement, address) were applied after it scored 3 and were checked by eye, not re-judged; the score stays 3 until it is.

**Checks:** `preflight.py html`: 0 errors, 0 warnings. `check_dates.py --year 2026`: passes. No invented domains on the page. Two typefaces at most, sizes on the token scale.

## Round 5 (owner review, 2026-10-18)
The owner hid this footer until it passes at 4 (round 4 scored 3; an earlier blind test lost to Legora by 4). This replaces the round-4 layout; the ensō, seal and vertical type described in the first sections are long gone.

**One idea:** a tea house ends its page with one quiet note from the back room.

**Changed:**
- Ground changed from pale celadon to sumi ink (neutral-dark-2) with the paper-white section above, for strong tonal contrast
- One signature element: 'Hojicha is roasting in the back room.' in Shippori Mincho at 76 px; the second sentence and the about paragraph removed
- Name and 茶房ささめ (both in the Mincho) lead the column row; Visit, Hours, Seats and More in one text size, information muted, links in ink, headings 13 px
- One rule above the columns, one legal line; the sliver above lists the five sittings

Type: Shippori Mincho (name and note) and Zen Kaku Gothic New; sizes 13, 16, 25 and 76 from the token scale (39 on phones). Contrast on sumi: text 14:1, muted text 7.5:1. Renders: `shot.png` 1440 wide, natural height, scale 2; `shot-mobile.png` 390 wide. The 337 px gallery copy was checked first.

**Blind pairwise (18 Oct, fresh judge, no labels, random sides; Mobbin footer sections, kept in scratch and deleted):** lost 1 vs MOUTHWASH Studio, won 3 vs Monte, won 2 vs In Common With (tested with the longer first version of the note).

**Fresh-eyes audit:** 4 (18 Oct), 4 (20 Oct). Final: 4 of 5.

**Checks:** `check_dates.py --year 2026` passes; `check_names.py` 0 errors (Kanazawa, Higashiyama, Ishikawa and English are false positives); `preflight.py html` 0 errors, 0 warnings. The five sittings from 10:00 end at the 17:30 close.
