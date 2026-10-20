# 08 weir: a Bauhaus hero for a data-pipeline company

Gallery: weir is a fictional data-pipeline company; its hero is a Bauhaus diagram, each source shape sized by rows a day.

**This page now:** the "Round 4 (owner review, 2026-10-18)" section, the last one, describes it. The sections between record earlier versions.

**Direction.** weir is a fictional ETL company: it copies data from 312 kinds of source into a customer's warehouse and checks every row against where it came from. The hero is a Bauhaus poster in which the geometry *is* the pipeline diagram: three sources as the three elementary shapes, sized by rows a day; black bars as flows, weighted by rows a second; the weir itself as a vertical black bar with its job set along it; the warehouse as a black square. All type is lowercase, after Herbert Bayer's universal alphabet. Feel words: **bold, technical, clean**.

Render: 1440 x 900, scale 2 (`shot.png`), light by design (`data-theme="light"`).

## References (Mobbin, cited by URL only)
Mobbin has no true Bauhaus page; the shapes, Kandinsky's colour pairing and the lowercase type come from Bauhaus practice. Mobbin gave the hero structure and the pipeline diagram.

| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/6e31f38b-b744-4dbf-9369-7e7e3205c19a (Customer.io, data pipelines) | The diagram every ETL buyer knows: sources on the left, a hub, destinations on the right. Ours keeps the order and drops the logos and glow. |
| https://mobbin.com/sites/sections/ee5646ad-4ed5-4561-bb59-15de0e1e5b17 (Shopify, commerce components) | Enterprise hero with a regular-weight headline on the left and a flat geometric composition on the right; geometry can be the whole visual. |
| https://mobbin.com/sites/sections/199259c8-fe79-4eb8-8487-77464c455ebb (Figma, enterprise) | Flat polygons joined by lines read as a system diagram, not decoration. |
| https://mobbin.com/sites/sections/9cb511d3-6877-41db-ae13-07ac364164e7 (Figma, "make design accessible") | One huge circle can carry a page; it led to the 300 px databases disc. |

## System (engine)
```
sketch --name Weir --brand "#D7261E" --audience regular --platforms web --feel bold,technical,clean --theme system-light-dark --surfaces "landing page:persuade,pipeline console:operate" --delegated all
set raw.secondaryColors ["#1E4AA8", "#F2C200"]; raw.accentCount 3
set answers.Q-dir-01 "flat2"; raw.textFace "Jost"; raw.displayFace "=textFace"; raw.fontLicence all true; raw.marketingSurfaces true
build -> no errors, 0 warnings
```
The brand red was kept exactly (pinned at step 9). The two secondaries were not: ultramarine #1E4AA8 came out as **#256aff** at accent2 step 9 (an electric blue, wrong for Bauhaus) and appears in no step; yellow #F2C200 came out as #edc343. Both are set by hand as `--blue` and `--yellow` (recorded as a bug).

| Dial | Value | How it expresses Bauhaus |
|---|---|---|
| expression | 75 | The geometry is the poster and the diagram |
| brandPresence | 65 | Red on the action and the mark |
| density | 42 | A poster: few elements, large |
| energy | 50 | Static, balanced asymmetry |
| roundness | 0 | Square corners; the only curve is the circle |
| depth | 0 | Flat |
| colorfulness | 72 | Three primaries plus black |
| warmth | 40 | White paper, not cream |

**What the dials cannot express:** the shape vocabulary and Kandinsky's pairing (yellow triangle, red square, blue circle, from his 1923 Bauhaus questionnaire), the grid (no grid tokens exist; a 12-column grid with 84.67 px columns, 24 px gutters and 80 px margins is set by hand and written in a comment), lowercase as a typographic rule, vertical type, and bar weights as data.

**The geometry is data.** Area is 44,000 px² per billion rows a day: databases 1.6 b = circle r 150; event streams 0.62 b = triangle, side 251; SaaS apps 0.18 b = square, side 89. Bar thickness is rows a second: 16, 6 and 2 px in, 24 px out (18,500 + 7,200 + 2,100 = 27,800 rows/s).

## Fonts and type scale
Jost only (SIL OFL; geometric, in the Futura tradition).

| Role | Size | Use |
|---|---|---|
| Headline | 67 | "every row in." 400, "none lost." 600 (highlight by weight) |
| Title | 38 | Facts, warehouse volume |
| Body large | 21 | Lede, "databases", "warehouse" |
| Body | 16 | Nav, button, shape labels, the weir's vertical line |
| Label | 12 | Rates, captions |
Plus the 28 px wordmark (title-small step). Five text sizes plus the wordmark.

## Outside the tokens, on purpose
- `--blue` #1E4AA8 and `--yellow` #F2C200 (the engine moved both).
- Diagram geometry in an absolutely positioned SVG on the 1440 x 900 frame.
- `engine.py review`: raw values left are the 80 px margins and the frame; the "#256aff" it flags is in a CSS comment.

## Checks
- `engine.py validate`: no errors, 0 warnings.
- `preflight.py html`: 1 error (M9 Google Fonts false positive); the `<br>` warning was fixed with block spans; it read no font sizes.
- Contrast: ink on paper 15.2:1; white on red button 5.0:1; white on ultramarine 7.9:1; ink on yellow 9.2:1. The SVG has one `aria-label` that states every number in words.

## Self-audit
Compared at 1440 with Customer.io's pipeline section, the Shopify enterprise hero and the Figma enterprise hero.
- **Round 1, score 3.5.** Red circle, blue square (Kandinsky reversed); a CSS selector put a second 4 px rule inside each fact ("double line" bug); the black CTA left all colour on the right; the warehouse block had a hole between its title and numbers; a "0 rows lost across 41 customer warehouses" fact was a customer count (invented proof, section 11).
- **Round 2, score 4.** Kandinsky pairing; shapes centred on columns 7 and 8, the weir on the right edge of column 10, the warehouse across 11 and 12; rate labels clear of the circle; red CTA balancing the blue disc; selector fixed.
- **Round 3, score 4.** Warehouse shows "2.4 b" as the number with "rows a day, 0 lost" under it; facts now 312 connectors, 4 min p95 lag, eu · us residency (no customer count); `<br>` replaced.
- **Tells left:** the composition is calm and evenly spaced; a stronger Bauhaus poster would add tension (an overlap, a diagonal, type locked to a bar). **Final score: 4.**

## The style: Bauhaus
- **Plain words.** The look of the 1920s German design school: elementary shapes, primary colours and plain geometric type, arranged so that form follows function.
- **What defines it (checkable).** Circle, square and triangle in flat red, yellow and blue with black; a geometric sans (Futura-like), often lowercase; asymmetric balance on a grid; thick black bars and rules; type set vertically or along bars; no ornament, gradient or shadow.
- **How it goes wrong.** A Mondrian grid pasted behind a SaaS page; the three shapes as random confetti; red, yellow and blue at equal weight everywhere; fake "Bauhaus" display fonts; distressed paper textures; geometry that means nothing.
- **How I kept it premium.** Every shape and bar is a number (rows a day, rows a second); the colour pairing is Kandinsky's own; one family, lowercase, regular weight with one bold phrase; one red action; facts with units.

## Process findings
1. **Secondary colours are not pinned** (ultramarine to #256aff, yellow nudged) (feedback: bug).
2. **No grid tokens** for a grid-led style (feedback: gap).
3. **No style catalogue** (feedback: idea): each builder writes the traits, dial mapping and failure modes by hand.
4. Helped: the brand pin kept vermilion exact; `accentCount 3` with `secondaryColors` gave three ramps in one step; the warmth dial at 40 gave clean white paper.

## Polish round 2026-10-14
After the independent audit (score 3: the hero recipe, shapes floating apart at even spacing, and a vertical label that was hard to read). **Rebuilt as a poster with tension.** The text above describes the version before this round: its 312 connectors, 44,000 px² per billion and r 150 are now 287, 80,000 and r 202. A fresh-context reviewer re-audited it twice; final score **4**, with no fact errors left.

**What changed**
- **The weir is the structure.** A black crest bar bleeds off the left edge and joins the vertical weir bar, which bleeds off the top and bottom. The headline sits inside the crest: one line, one weight.
- **The shapes interlock, still sized by rows a day (80,000 px² per billion).**
  - The databases circle (1.6 b, r 202) sends its 16 px flow straight through the weir.
  - The saas square (0.18 b, side 120) sits over the circle's shoulder.
  - The event-streams triangle (0.62 b, side 338.5) stands on the bottom edge over the circle's flank.
  - The warehouse square (2.4 b, side 438) is whole and sits flush in the bottom-right corner.
  - The bars are weighted by rows a second: 16 + 6 + 2 = 24 px, or 18,500 + 7,200 + 2,100 = 27,800, which matches 2.4 b over 86,400 s. The databases bar has a paper edge where it crosses the blue. The square and the triangle are drawn over the ends of their own bars.
- **The weir's job is set across beside the bar.** The three-stat row is folded into it (287 source connectors, eu or us) and into the warehouse (p95 4 min behind the source).
- **One action, in black.** Apart from the logo mark and the focus ring, red marks only the saas-apps square. The square's top lines up with the button's bottom.
- **312 became 287.** 312 is used by other showcase pieces.
- **Accessibility.** The SVG comes after the copy in the source and ignores pointer events. Its aria-label states every number.
- **Engine.** `pick Q-dir-01 bauhaus`; build passes.

**References used by the re-audit:** Friends of Figma (https://mobbin.com/sites/sections/d07a48ba-b906-4fac-a94c-4506459d69d1), Figma Enterprise (https://mobbin.com/sites/sections/199259c8-fe79-4eb8-8487-77464c455ebb), Customer.io data pipelines (https://mobbin.com/sites/sections/6e31f38b-b744-4dbf-9369-7e7e3205c19a).

**Left:** the composition is calmer than a full Friends-of-Figma frame (only the crest, the weir, the triangle and the warehouse touch the edges), and the copy stack on the left is conventional.

## Round 3 (polish) 2026-10-15
**Fresh audit: 4 of 5** against the B2B product screens and Orbika (`heroes/08`). Render: `shot.png`, 1440 x 900 at scale 2.

### Why this round
The piece still carried "Being rebuilt" on the public showcase. The poster held, but its right column, "the weir", said what the weir does and then stood empty for 200 px above the warehouse. The B2B screens persuade with specific numbers, not claims.

### What changed
- **The weir shows its count.** The column under the weir's line held a two-item list (287 connectors, which the lede already says, and a region line). It now holds a three-row ledger for today to 14:00 UTC. The first version showed rows at source and "missing 0"; the audit below changed it to at source against landed.
- **After the first fresh audit (3):**
  - **The ledger shows the count:** rows at source against rows landed for each kind of source, and a footnote: "the gap is 2,482,309 rows in flight, none older than 4 min. missing: 0." (Databases 1,665,288, event streams 647,823, SaaS apps 169,198 in flight; about 90 s of each rate.) The "eu or us" line, unrelated to the count, is gone.
  - **The out-flow enters the warehouse** with a paper edge, as the databases flow crosses the blue. The warehouse text sits in two groups: the name and 2.4 b at the top, the rate and lag at the bottom on the same baselines as the event-streams label.
  - **The red square has room:** the button moved up 28 px; the source comment that said the square's base lined up with the button was wrong and is fixed.
  - **The event-streams flow is visible:** raised from the bottom edge to y 800, with a paper edge where it crosses the blue.
  - **"databases" is centred** on the circle.
  - **Labels at 16 px:** flow rates, rows-a-day lines, ledger headers and footnote (they were 12).
- **After the second fresh audit (4, "only just"):**
  - **The out-flow stops at the warehouse's edge,** on the databases axis, and its rate is labelled where it arrives ("27,800 rows/s in", "p95 4 min behind the source").
  - **The databases bar starts clean** at the circle's centre: paper edges run along its top and bottom only.
  - **The triangle's apex sits on the square's left edge** (moved 10.75 px), and **the circle sits on the page's bottom edge** like the triangle (centre moved 28 px down; the flow and labels with it).
  - **A heavier headline:** 80 px at weight 500, outside the scale (67 and 90) on purpose: 90 runs into the weir, 67 left the crest empty. Glyphs measured inside the crest bar (y 136 to 216 of 118 to 222).
  - **The footnote agrees with the lag:** "none older than 6 min", since p95 is 4 min.
- **After the final fresh audit (4):**
  - The red square is set clearly into the circle's shoulder (it grazed it), and its flow leaves flush with its top.
  - The weir's line no longer promises "in seconds" while rows can be minutes in flight: "if one runs late, you hear at once."
  - The headline is 76 px, balanced in the crest (80 px left, 70 px before the weir); "the weir" sits on the crest's top line.

- **After a last regression check (holds at 4):** the square and the triangle moved 40 px right together: the square overlaps the circle clearly and the triangle's apex now sits 51 px under the square's corner, a clear gap instead of an 11 px near miss; the SaaS flow still leaves flush with the square's top.

### Arithmetic
- 14 hours is 50,400 s. 931,872,406 / 50,400 = 18,490 rows/s (the poster's average: 18,500); 362,509,877 / 50,400 = 7,193 (7,200); 106,114,239 / 50,400 = 2,105 (2,100). The order of the rows follows the shapes, largest first.

### References (Mobbin, by link only)
| Reference | What it taught |
|---|---|
| Customer.io, https://mobbin.com/sites/sections/6e31f38b-b744-4dbf-9369-7e7e3205c19a | Many sources drawn into one hub. |
| Figma Enterprise, https://mobbin.com/sites/sections/199259c8-fe79-4eb8-8487-77464c455ebb | A geometric figure that does a job beside a heavy headline. |
| Shopify, https://mobbin.com/sites/sections/ee5646ad-4ed5-4561-bb59-15de0e1e5b17 | Flat shapes that interlock firmly instead of grazing. |

### Checks
- **Contrast as rendered:** 39 runs. The only flag is the headline: an upright 76 px text box is taller than the 104 px crest bar, so it takes in paper above and below. Measured with canvas text metrics, the glyphs sit inside the bar. Every other run passes; lowest 7.93:1.
- **Weekdays:** `check_dates.py --year 2026` passes (no weekdays on the page).
- Preflight: one warning, the 76 px headline outside the scale, on purpose (90 px runs into the weir, 67 px left the crest empty).

## Round 4 (owner review, 2026-10-18)
**This section describes the page now.** Rebuilt after the round-4 audit scored it 5 of 10 (rebuild). Render: `shot.png`, 1440 x 900 at scale 2.

**One idea:** Three sources, a square, circle and triangle sized by rows a day, flow through the weir into one warehouse, every shape whole inside the frame.

**Why:** The round-4 audit: the shapes carried data but bled off the bottom, so the page looked cropped, not composed; the black data panel was a second design bolted on; the all-lowercase headline and nav felt affected.

### What changed
- **Composed, not cropped:** the diagram is a 752 x 744 field inside the margins. The three sources stand in one column, 64 px apart (square, circle, triangle; areas 7,921, 70,686 and 27,498 px² for 0.18, 1.6 and 0.62 billion rows a day), each with a black bar to the weir weighted by rows a second; the weir bar ends at the last input.
- **No bolted-on panel:** the ledger table and the black side panel are gone. The day's count is set beside the weir, where it is taken ('2,482,309 rows in flight, none older than 6 min, 0 missing'), and the warehouse is a slimmer black square at the end of the flow (not to scale; it is the destination).
- **Sentence case:** headline, nav, labels and the lede ('Copy data from 287 kinds of source…'); the wordmark stays lowercase as a logotype. 'billion' is spelled out.
- The hero is the rule's minimum: headline, one line, one action, one subject; the copy column is centred against the diagram.
- After the fresh audits: the stacked column, the table removed, the lede rewritten to two lines, the bar trimmed. **After the third audit:** the warehouse box narrowed to 152 px and the weir note given 24 px of room.

### Type scale
Jost only. 16 labels and nav, 21 lede and source names, 28 the wordmark and '2.4 billion', 67 the headline.

### Blind pairwise test
Three shipped references (Mobbin, cited by link only; images were kept in scratch and deleted). Each pair at the same height, sides random, no labels; fresh judges saw several pairs at once (four sets: 15, 9, 6 and 6 pairs, a new judge each time) and were told to weigh craft, not content. The table gives the result for the final render.

| Reference | Result |
|---|---|
| Mixpanel, https://mobbin.com/sites/sections/f23d55dd-c491-4722-9530-ce6deeebdca9 | ours better by 2 |
| Customer.io, https://mobbin.com/sites/sections/6e31f38b-b744-4dbf-9369-7e7e3205c19a | ours worse by 2 |
| Airtable, https://mobbin.com/sites/sections/56f4e48d-280e-40d2-bbe9-9afd7d3e55ad | ours better by 3 |

**Pass rule:** never lose by 3 or more, and equal or better in at least 2 of 3. Passes. The judges' flaw for ours on the final render: flat primary shapes with plain black bars read as a classroom diagram or a toy.

### Fresh-eyes audit
Round 1 was a fresh-context auditor given PRESENTATION.md, ROUND3-BRIEF.md, the owner's note, the B2B product screens (product/01, 02, 04, 06), Orbika, Holdfast and Lampwright as the bar, and the three references below. Rounds 2 and 3 went to the same auditor, so they check its own fixes rather than being fresh eyes. Scores: 3, 4, 4.

### Checks
- `check_dates.py --year 2026` passes (no weekdays on the page).
- `check_names.py`: 0 errors; 'Databases' is a UI word.
- `engine.py validate`: no errors, 0 warnings. Preflight: no errors or warnings (the headline wraps at a non-breaking space, not a <br>).
- Re-added from the page: 2,100 + 18,500 + 7,200 = 27,800 rows/s; x 86,400 s = 2.40 billion a day (0.18 + 1.6 + 0.62 = 2.4); 2,482,309 rows in flight is about 89 s of flow.

### Left
Blind judges call flat primary shapes with black bars a 'toy' or 'classroom' diagram; the Bauhaus field is the style, so this is the trade-off.
