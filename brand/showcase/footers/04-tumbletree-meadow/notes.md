# 04 Tumbletree: playful illustrated footer with a meadow and a mascot

## Direction
Tumbletree is a fictional learning app for children aged 4 to 8 (reading, numbers, ten minutes a day). The footer is read by parents and teachers, but it should make a child smile if they are on the lap: a meadow at the end of the page, a rising sun, and Pip, a round tangerine creature with a sprout, waving with one hand and flying a kite with the other, saying "See you tomorrow!". Chunky rounded type, thick ink outlines, "sticker" buttons with a hard drop.
Feel words: playful, cheerful, warm.

## References (Mobbin, structure only)
- https://mobbin.com/sites/sections/0cc6183c-2921-48ea-bfe9-d7c3d60bfed4 — a line-art scene along the bottom edge that the link grid sits above; the scene is the reward for scrolling to the end.
- https://mobbin.com/sites/sections/63e60bfc-1a20-41d0-a3b3-2da8a43a3723 — a landscape as the ground of the footer, with legal text standing on it.
- https://mobbin.com/sites/sections/9ee9d990-cbe1-40fe-b2ca-03ae743e3f0a — a warm footer that puts links in a rounded panel with a thick border and lets a mascot and a speech bubble carry the voice.

## System (engine)
```
python3 $E --dir .../04-tumbletree-meadow/opendesigner sketch --name "Tumbletree" --brand "#ffc83d" --audience large --platforms web \
  --feel playful,cheerful,warm --theme system-light-dark --delegated feel,audience,platforms,theme,surfaces --surfaces "family site:persuade"
```
- Dials: expression 90 (a whole illustrated world), brandPresence 80 (sun yellow and the mascot are the brand), density 28 (big targets, few links), energy 80 (bouncy), roundness 100 (pills and blobs), depth 35 (chunky drop on the panel and buttons), colorfulness 95, warmth 90.
- `raw.accentCount 3`, `raw.secondaryColors '["#3fb6f2","#3fb86a"]'`: sky (accent2) and grass (accent3) ramps.
- Faces: `raw.textFace "Nunito"`, `raw.displayFace "Fredoka"` (both SIL OFL). DESIGN.md flagged Fredoka as a licence risk, so I recorded `raw.fontLicence {"web":true,"app":true,"selfHost":true}`.
- Build: no errors, 1 warning (2 after the warmth change, base and raised surface): the yellow action colour against a white surface is 1.5:1. Correct and useful; the buttons get a 3 px ink border so the edge passes.
- `--audience large` did not raise body size (still 16 px; see findings).

## Build
- Type, spacing, radii, motion, focus and all UI colours are tokens. The meadow uses the ramps: sky accent2 steps 2 and 4, hills accent3 steps 4, 6, 9 and 11, sun accent step 9, path accent step 3.
- Outside the tokens, on purpose: Pip's tangerine, belly and cheek colours (a brand character, the "illustration, characters" asset the engine lists as a designer hook); the ink outline uses the darkest neutral token; white clouds and flowers; the 56 px button height and 3 px outlines (sticker style); the hard 5 to 8 px drops.
- Art made in SVG by hand: hills, trees, path, sun, kite, birds, clouds, Pip. The speech bubble's words are inside the art, so the SVG is `aria-hidden` and nothing it says is needed.
- Accessibility: white legal text on accent3 step 11 is 5.9:1; chips' green text on white 5.9:1; the blue "big curiosity." 5.4:1 on the sky; buttons are 56 px tall; links 36 px; 3 px focus ring in sky step 11; clouds stop drifting with reduced motion.

## Renders
- `shot.png`: 1440 wide, full height (836 px after the type changes), scale 2. `shot-mobile.png`: 390 wide.
- Round 1: clouds sat behind the logo and inside the link panel, "Lesson plans" wrapped beside its "New" pill, the speech bubble tail was a patched shape. Moved clouds into the empty sky, made links nowrap with auto columns, drew the bubble and tail as one path, added birds.
- Round 2 (mobile): the legal links sat on the bright near hill (white on #00bc5f is 2.5:1, a fail), the kite was cut off and a cloud covered a chip. Moved the legal row into its own dark green band below the scene, reframed the SVG on phones (`viewBox 600 0 520 380`) so Pip and the kite stay in view, hid two clouds.

## Checks
- `preflight.py html`: 1 error, the Google Fonts false positive (Fredoka).
- `engine.py validate`: passes with the advisory yellow-on-white warning (handled by the border).
- `engine.py review`: 25 raw values, 16 of them colours: the mascot, white art, rgb() whites for translucent panels. All in the art layer.
- Checklist: sizes 12, 16, 21, 28, 38 (phone), 51 from one scale; heading weight 600 (lighter than the system's 750, because Fredoka at 750 reads as shouting); the panel, chips and buttons stay on one line where they should.

## Owner type and color rules (applied mid-run)
- Fonts: two (Fredoka for display and the speech bubble, Nunito for text).
- Type scale (named roles): label 12 ("New" pill), body 16, title 21 (link headings, buttons, lede), headline-sm 28 (wordmark), display 51 (headline; 38 on phones). Five steps.
- Changed: "big curiosity." was highlighted by colour only (sky blue). Now it sits in a rounded sun-yellow fill box with ink text, which matches the sticker style and the yellow button. Headline leading went from 1.04 to 1.14 so the box does not touch the line above.
- Changed: warmth 90 to 55 (`set dials.warmth 55`). At 90 the ink and grey text were brown (#282321, #605551) on a sky-blue page; now a clean ink (#252423) and grey (#595756).

## Process findings
1. `--audience large` promises 17 px body in the stage file but leaves it at 16 (feedback: bug).
2. The open-font list misses common OFL faces, so DESIGN.md warns about licences that are free (feedback: bug).
3. No saturated mid-tones for illustration in the ramps (feedback: gap).
4. The illustrate skill cannot run without a person to say yes to fetching (feedback: confusing).
- Helped: the yellow-on-white warning caught a real problem with a chunky yellow button.

## Round 3 (owner review)
**What he said:** "needs work". He likes the Brask, Keystrata and Rallo footers and the B2B product screens: quiet, exact, real, one accent. The independent audit had listed the hero stack in a footer (highlight block, two sticker buttons, three check pills), stock scenery (clouds, sun, birds, lollipop trees) and a generic blob mascot.

**What changed (rebuilt in place):**
- Everything decorative is gone: the meadow, sun, clouds, birds, trees, kite, speech bubble, the mascot Pip, the headline with its highlight block, both buttons and the check pills.
- A quiet index on a flat night ground (accent2 dark step 3): the wordmark, two short paragraphs with facts (ages 4 to 7, England's EYFS framework and the Key Stage 1 national curriculum, the app locks until 6.30am, 31 people of whom nine are former teachers), and four link columns. The Lessons column carries lesson counts and a total (380 + 240 + 300 + 90 + 26 = 1,036).
- The one detail only this brand would have: a handwriting-formation specimen of the first eight Phase 2 phonics sounds, Set 1 s a t p and Set 2 i n m d, on four writing lines. Single-line letters in white; sun yellow has one job: the start dot, the first-direction arrow and the stroke numbers of the two-stroke letters t and i. It is drawn by a small script inside the grid columns, so it fits every width; below 480 px the two sets go on two rows.
- Text is white at 68% (7.5:1) instead of the pale cyan the first draft used; all rules are white at 14%, the writing lines 40% and 50% (3.5:1 and 4.7:1).
- Legal row: "© 2026 Tumbletree Learning Ltd, Bristol · Registered in England and Wales", with five legal links aligned to the index column.

**Drafts the fresh-eyes audits turned down (16 audits in all):** a sleeping mascot on a green hill (3: still a hero band, and close to Duolingo's footer), a night bed with an alphabet quilt (3: clip-art, Duolingo's silhouette), a patchwork quilt of felt letters (3: texture standing in for an asset), large dotted tracing letters across the page (3: worksheet-generator look, wrong dot ends), and a small specimen beside the about text (3: too small and fussy). The fixes that moved it to 4: the specimen moved under the index at about 75 px x-height with a 3 px stroke, marks that scale with the letters, each downstroke arrow inside its own letter, one arrow length, and layouts checked at 1440, 1240, 1100, 960 and 390 px.

**Type scale used:** label 12 (set labels), footnote 14 (legal, counts, stroke numbers), body 16, title 28 (wordmark). Fredoka for the wordmark only, Nunito for everything else.

**Outside the tokens, on purpose:** 14 px (no 14 step in this scale; footnote role), white-alpha text and rule colours (`rgb(255 255 255 / .68)` and `/ .14`, `/ .4`, `/ .5`), a 56 px row gap, and the 5 px and 13 px baseline nudges that put the column headings on the wordmark's baseline.

**Checks:** `preflight.py html`: 0 errors, 1 warning (14 px is off the token scale, kept on purpose). `check_dates.py --year 2026`: passes. `engine.py validate`: no errors. Names: Tumbletree and Tumbletree Learning Ltd are this piece's only names (NAMES.md); no new names. No invented domains on the page.

**Fresh score: 4** (sixteenth audit, against the B2B screens and the Brask, Keystrata and Rallo footers, with Opennote and Clay footers on Mobbin as references: https://mobbin.com/sites/sections/3dbc7c17-d1c9-4490-a394-33c61e52f471, https://mobbin.com/sites/sections/9ee341c1-9b8d-4389-9899-62f10bfaa78b). Its remaining notes (arrow lengths, arrows sitting in the gaps, the note far from the drawing at mid widths, the i's stacked numbers, the d's cap above the top line, a lone "Bristol" on phones) were fixed afterwards and checked by eye at 1440, 1100 and 390 px; that last pass was not re-audited.

**Process findings:**
- The engine's type scale has no 14 px step, but footers need a footnote size between 12 and 16.
- Nothing in the process checks a layout between breakpoints; three of the audit rounds found faults only at 960 to 1240 px.

## Round 4 (18 Oct 2026): quiet footer
This replaces the round-3 design described above. The round-4 audit (`brand/showcase/AUDIT-ROUND4.md`) and the owner called the footer studies cluttered; `brand/showcase/PRESENTATION.md` now sets the footer rules. Built from one shared generator so all four keep the PRESENTATION.md footer rules: link columns in one text size, one muted heading style, one rule, one legal line, at most one signature element, and the last row of the section above (one line of real copy) so the shot reads as the end of a page. No illustrations, charts, chips, badges or boxes.

- Round-3 writing specimen, lesson counts and second paragraph removed (audit round 4: 'letter-formation diagram with numbered yellow arrows', 'corporate navy')
- Pale sky ground (accent2 step 2) instead of navy; the one signature element is the product's rule in Fredoka: 'Ten minutes a day, then the app locks until morning.'
- Four link columns of four links, one muted heading style, one rule, one legal line; a placeholder logo square removed after the fresh audit
- The last row of the FAQ above as the top sliver

**Fresh audit:** 4 of 5. **Pairwise:** won against Loom by 1 (not blind: the judge knew which side came from Mobbin). After the audit: placeholder mark removed and the about text cut to one line (both from the final audit, checked by eye).

**Checks:** `preflight.py html`: 0 errors, 0 warnings. `check_dates.py --year 2026`: passes. No invented domains on the page. Two typefaces at most, sizes on the token scale.
