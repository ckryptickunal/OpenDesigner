# 06 Plenary: Memphis ticket counts for a conference organiser

Gallery: Plenary is a fictional ticketing tool; each ticket type is a row of Memphis shapes, one for every 20 tickets.

**This page now:** the "Round 4 (owner review, 2026-10-18)" section, the last one, describes it. The sections between record earlier versions.

**Direction.** Plenary is a fictional ticketing platform sold to conference organisers (events of 300 to 30,000 people). The landing section shows the organiser's view of a real-looking event, "Northfold Design Week 2027" in Rotterdam: four ticket types, sales against capacity, gross revenue and the next payout. The Memphis set around it is not confetti: each big shape is one ticket type, drawn to scale by tickets sold, and the same shapes are the tier markers inside the product. Feel words: **playful, vibrant, practical**.

Render: 1440 x 900, scale 2 (`shot.png`), dark ground by design (`data-theme="dark"` on the page, the product card in its light theme).

## References (Mobbin, cited by URL only)
Mobbin had no true Memphis-style B2B section; the closest are Figma's geometric tiles. The rest is product structure.

| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/ca825e99-08b1-42f7-afde-ab3790f9978a (Figma, CTA tiles) | Memphis-like shapes with discipline: few shapes, each a self-contained motif, lots of empty ground between them. |
| https://mobbin.com/sites/sections/abfa1ea0-e633-4591-bd82-cc4eb6eb1c4e (Mural, webinar hero) | Copy on one side, a block composition of flat colour and a halftone patch on the other; the shapes live in their own half. |
| https://mobbin.com/screens/e9a15838-b7c1-4961-9806-d18fa4016e87 (Luma, event registration) | What an organiser sees: ticket types as rows with registration counts, capacity, the event header. |
| https://mobbin.com/screens/d2d7c5d3-5e48-4545-a7cb-d2ffce5e62e3 (Sweatpals, event analytics) | Capacity as a single bar with taken and remaining; check-in as its own number. |

Also looked at and rejected: the Tines hero (https://mobbin.com/sites/sections/2b05eff8-4978-4c72-b9e6-0b1935bd7b5e), a card in a field of floating objects. That is exactly the "decoration with no data" tell, so the shapes here are few and sized by data.

## System (engine)
```
sketch --name Plenary --brand "#FFE45C" --audience regular --platforms web --feel playful,vibrant,practical --theme system-light-dark --surfaces "landing page:persuade,organizer dashboard:operate" --delegated all
  -> "I picked an olive": the sketch replaced lemon with #877400 (same bug as the Orbika hero)
set raw.brandColor "#FFE45C"             (restored)
set answers.Q-dir-01 "maximal"           (nearest preset to Memphis)
set raw.secondaryColors ["#FF8FB8", "#6FE3C1"]   (the triadic default gave green #238557 and terracotta #b55c41)
set raw.textFace "Bricolage Grotesque"; raw.displayFace "=textFace"; raw.fontLicence all true; raw.marketingSurfaces true
build  -> no errors; 2 warnings (lemon button on white in light mode, 1.25:1; advisory for a labelled button)
```

| Dial | Value | How it expresses Memphis |
|---|---|---|
| expression | 80 | Loud display type and a shape set as the signature |
| brandPresence | 70 | Lemon on the one action and the early-bird tier |
| density | 40 | Roomy around the product card |
| energy | 75 | Squiggle and zigzag; the card itself stays calm |
| roundness | 30 | Memphis mixes hard geometry with circles; UI corners small (4 and 8 px) |
| depth | 0 | Flat laminate colour, no shadows |
| colorfulness | 82 | Three accents allowed (lemon, pink, mint) |
| warmth | 45 | Neutral black ground, no brown |

**What the dials cannot express:** the laminate patterns (dot screen on the lemon disc, stripes on the triangle, black and white stripes on the square, the "Bacterio"-like squiggle print on the pink dome), the shape vocabulary itself, the squiggle line, and the rule that every shape is data. Also by hand: lemon is used at its exact hex in dark mode because the dark ramp dulls it to #d8c568.

**The shapes are a chart.** Area is proportional to tickets sold (63.6 px² per ticket): early bird 400 = lemon disc r 90; standard 1,212 = pink half disc r 221; workshop 186 = mint triangle, side 165; speaker and press 64 = square, side 64. A 12 px note under the triangle says so.

## Fonts and type scale
Bricolage Grotesque only (SIL OFL; width 75 to 100, optical size 12 to 96). Headline at width 84%, the card at 92 to 100%.

| Role | Size | Use |
|---|---|---|
| Display | 90 | Headline: regular, with "last badge." in 700 (highlight by weight) |
| Headline | 38 | 1,862 tickets sold |
| Title | 21 | Lede, event name, wordmark |
| Body | 16 | Nav, table, buttons, facts |
| Label | 12 | Fact labels, card secondary text, scale note |

## Outside the tokens, on purpose
- `--lemon` is `accent-light-9` in dark mode (the dark ramp dulls the brand); pink and mint are `accent2/3-dark-9`.
- Shape geometry and the 1440 x 900 absolute layout (a fixed-size marketing frame).
- `engine.py review`: 9 raw values left (8 layout sizes, the 4 px radius fallback); the px-spacing and 100vh standards it flagged were fixed.

## Checks
- `engine.py validate`: no errors; 2 light-mode warnings about the lemon button on white (the section is dark; on black lemon is 14.3:1).
- `preflight.py html`: 1 error, the M9 Google Fonts false positive; it read no font sizes (tokens).
- Contrast: chalk on black 15.0:1; lede grey 7.9:1; ink on lemon button 12.2:1; card secondary text 7.2:1. Targets: nav, tabs and buttons are 44 px or more. The stage SVG is `aria-hidden`; the sales bar has a text label.

## Self-audit
Compared at 1440 with the Figma CTA tiles, the Mural webinar hero and the Luma registration screen.
- **Round 1, score 3.5.** Headline letters touched in the bold line (tracking -0.025em); the scale note sat on the pink dome and could not be read; four confetti pieces (a pink dash, a mint dot, a lemon triangle) carried no data; the striped square floated alone.
- **Round 2, score 4.** Tracking eased; confetti removed (only the squiggle and one zigzag stay, as the style's signature line); the note moved under the triangle; the square now tucks behind the card edge like stacked laminate.
- **Round 3, score 4.** The section was four fifths of the "same hero recipe" (kicker, highlighted headline, sub-line, button pair). The kicker went, its fact (300 to 30,000) moved into the lede, the second highlight in the lede went, and payouts became a fact. One button and a price.
- **Tells left:** the right half is still "product card with shapes around it", a familiar landing layout; the pattern laminates are computer-even. **Final score: 4.**

## The style: Memphis
- **Plain words.** The loud, cheerful look of the Memphis Group, a 1980s Milan design collective: furniture and prints made of bold flat shapes, clashing colours and black-and-white patterns.
- **What defines it (checkable).** Primitive shapes (circle, half disc, triangle, square, cylinder) as solid flat colour; at least one black-and-white pattern (stripes, dots, squiggle "Bacterio" print); a squiggle or zigzag line; pastels next to brights and black; shapes stacked on and behind each other; no gradients or shadows.
- **How it goes wrong.** Confetti sprinkled everywhere; five or more pastel hues; shapes floating with no relation to the content; patterns on everything, including behind text; a childish rounded font; drop shadows on the shapes.
- **How I kept it premium.** Three accents plus black and white; patterns only on the shapes, never behind text; four shapes, each a ticket type drawn to scale and repeated as the marker in the product; the product shown flat and whole with real numbers; regular-weight display type with one bold phrase.

## Process findings
1. **Brand hex swapped again** (lemon to olive) by a delegated sketch, with no warning beyond "I picked an olive" (feedback: bug, repeat of the Orbika finding).
2. **Dark mode dulls the brand ramp but not the secondary ramps** (#d8c568 vs exact #ff8fb8) (feedback: bug).
3. **Triadic accents from yellow are brown and green**; `raw.secondaryColors` fixes it but no stage question asks for named secondary colours (feedback: gap).
4. **No Memphis preset**; patterns and shape language are outside the dials (feedback: gap).
5. Helped: `raw.secondaryColors` produced exact pink and mint ramps with readable step-11 text colours; `[data-theme="light"]` on the card let the product sit in its own light theme inside a dark page with no extra CSS.

## Polish round 2026-10-14
After the independent audit (score 3: the default hero recipe, a floating card with shapes around it, a footnote explaining the idea, and decoration with no data). **Rebuilt around one idea only this product would have:** each ticket type gets a shape, the shape is printed on every badge so a volunteer at a room's door can tell who belongs, and the same shapes chart sales. The text above describes the version before this round. A fresh-context reviewer re-audited it three times; final score **5 (a narrow 5)**, with no fact errors left.

**What changed**
- **The chart is the hero.** The four ticket types stand on one floor line, unobstructed and labelled. At 50 px² per ticket, the filled shape is issued and the dashed outline is released. The outlines are open along the floor, and the shapes sit 56 px apart. The legend sits in the totals column, so no footnote is needed.
  - Every pattern covers 20% of its shape (dots r 3.53 on 14 px, stripes 2 of 10 and 2.4 of 12, squiggles about 20%), so the visible colour is to scale too.
  - A 3 px inner band keeps the patterns off the edges.
- **The badge is the object.** Femke Verhaegen, type designer at Studio Veldkant, carries a standard ticket and the workshop add-on (Room 3, Fri 10:00). Her badge prints the pink half-disc and the mint triangle. The headline is "The workshop room lets in triangles."
- **The default recipe is gone.** One regular-weight headline with no bold line, one action and the price as plain text. The squiggle, the zigzag and the facts row are gone.
- **Colour and shape belong only to ticket types.** The wordmark, the button and the focus ring are black and white.
- **Facts.**
  - 1,862 issued of 2,520 released (74%), which is 1,676 people plus 186 workshop seats.
  - €647,360 gross.
  - The next payout is Fri 16 Oct 2026, the first Friday after today; it said 13 Nov, which contradicted "every Friday".
- **Names.** The event is now Kanteel Design Week 2027 in Ghent, Hall 4. Northfold was the seventh "North…" name in the showcase, and Rotterdam was used by three other pieces. A web search found no event or studio with these names.
- **Engine.** `pick Q-dir-01 memphis`; build passes. Two light-mode advisories about lemon on white remain; the page is dark.

**References used by the re-audit:** Luma (https://mobbin.com/sites/sections/e9ae7e4b-3538-47fd-9369-6fd7df860b00), Eventbrite organiser page (https://mobbin.com/sites/sections/b1b1d629-b848-4364-a974-0fb4a6502f96), Figma Enterprise (https://mobbin.com/sites/sections/199259c8-fe79-4eb8-8487-77464c455ebb).

**Left:** the top half still puts the copy on the left and the badge on the right.

## Round 3 (polish) 2026-10-15
**Fresh audit: 4 of 5** against the B2B product screens and Orbika (`heroes/08`). Render: `shot.png`, 1440 x 900 at scale 2.

### Why this round
The piece still carried "Being rebuilt" on the public showcase. Two things kept it from the bar. Its badge hung from a lanyard strap, the same object and staging as `styles/03`, so two studies in one set read as related. Its totals were a loose column of phrases that broke mid-thought ("issued of 2,520 / released, 74%").

### What changed
- **The badge lies flat on the grid,** without the strap and clip, top-aligned with the headline and right-aligned with the nav. A caption says what it is: "Badge proof · printed at check-in · 3 × 4 in" (the badge is drawn 280 x 376, a 3:4 ratio).
- **Totals as aligned rows.** 1,862 stays the one big figure, with "issued, 74% of 2,520" under it, then four label and value rows with hairlines: People 1,676, Workshop seats 186, Gross €647,360, Next payout Fri 16 Oct 2026.
- **The key moved beside the chart title,** after "Area to scale". The note "Filled: issued. Dashed: released." under the totals is gone.
- **After the first fresh audit (3):**
  - **Room between the copy and the chart.** The lede lost its last sentence (the chart says it), the copy moved up 14 px, and the chart scale went from 50 to 40 px² per ticket with 48 px gaps. The chart title now has 40 px above it and the Standard dome 42 px below it.
  - **One right column at x 1080:** the badge, its caption and the totals share a left edge; the chart ends near x 1000.
  - **A neutral key:** grey bars for issued and released. The white square looked like the speaker-and-press ticket.
  - **Key data at 16 px:** each shape's price and count line; the date line stays a 12 px caption.
  - **Memphis on the one object:** the badge's half disc and triangle are apart on one baseline, with the chart's squiggles and stripes, a second cue besides colour for the door volunteers.
  - **Patterns centred** on each shape, so the rims cut them evenly.
  - **"Next payout · Fri 16 Oct 2026"** fits the wider column.
- **After the second fresh audit (3):**
  - **A focal point:** the headline is the scale's 90 px display size, two lines, so it reads as the display word; the lede runs to two lines.
  - **Whole glyphs:** dots and squiggles are drawn one by one, only where each sits at least 4 px inside its shape, on the chart and on the badge's half disc, so no fragment touches a rim. Stripes keep their 3 px inset.
  - **Room between the right labels:** a 64 px gap before the speaker square (48 between the others), and "Workshop" as the short label.
  - **One bottom edge:** the chart floor is at y 760, and the totals column ends on it, beside the chart it totals. The scale is 34 px² per ticket so the Standard dome still clears the chart title.
  - **The badge at 240 x 320** (still 3:4), with "Type designer" and a two-line ticket line; Studio Veldkant is no longer on the page. The right column (badge, caption, totals) now runs from x 1120 to 1360, and the last row reads "Payout · Fri 16 Oct 2026" so it fits.
- **After the third fresh audit (3), a new layout:**
  - **One object:** Room 3's door sign, a large striped mint triangle with a solid band naming the room, set at −7°, with Femke's badge leaning on it at +4°. The headline names the triangle and the page now shows it.
  - **Memphis, taught:** large shapes at angles beside the copy, the badge's triangle tilted over its half disc, and a black-and-white zigzag for speakers and press.
  - **The totals beside their chart:** "1,862" (38 px, so it no longer competes) starts on the chart title's line.
  - **Rhythm:** 56 px from the action to the chart; the chart at 28 px² per ticket on a floor at y 768; 96 px before the speaker square so its label clears "Workshop"; the chart starts at x 86 so the first label stays inside the 80 px margin.
  - Stripes are whole too, inside every triangle; the badge caption is "Badge proof, 3 × 4 in".
- **After the fourth fresh audit (4):**
  - The badge caption is gone: it sat in the chart's heading row and read as a chart note (and inches were odd for a euro event).
  - The totals' last rule lands on the chart floor (y 768); "Workshop add-ons 186" makes the 1,676 people figure follow; the totals start at x 1060.
  - Speakers and press: whole zigzag rows 4 px inside the square, and the dashed released outline drawn 1 px outside the fill so it no longer reads as a double border.
  - The badge's printed triangle sits flat on the rule, still over the half disc (tilted, it clipped at the edge).
  - The door's stripes are bolder (4 of every 14 px); the door sign is not drawn to scale.

### Totals, re-added from the page
- Issued: 400 + 1,212 + 64 = 1,676 people, + 186 workshop seats = 1,862.
- Released: 400 + 1,800 + 80 = 2,280 people + 240 seats = 2,520; 1,862 / 2,520 = 73.9%, shown as 74%.
- Gross: 400 x €290 + 1,212 x €420 + 186 x €120 = €116,000 + €509,040 + €22,320 = €647,360 (speakers and press are free).
- Workshop: 6 rooms of 40 = 240 seats.

### References (Mobbin, by link only)
| Reference | What it taught |
|---|---|
| Eventbrite, https://mobbin.com/sites/sections/d2ac77c3-af65-4cfb-9f59-227d98a51578 | Shapes set inside the display line, so word and object read as one. |
| Maze Disco Conf, https://mobbin.com/sites/sections/f1932dd7-d181-45e1-a395-1b42541895d6 | One display word and one drawn object on a dark ground. |
| Figma Shortcut, https://mobbin.com/sites/sections/d89d3841-aea4-4bc6-a310-075eb53e19db | Real Memphis: black-and-white patterns, tilt and collisions. |

### Checks
- **Contrast as rendered:** 44 runs. Two flags come from rotated elements ("Room 3" on the door sign, "Standard + workshop" on the badge): the measuring box is upright, so it takes in stripes and the badge's rule. With the rotation switched off, every run passes; lowest 7.09:1.
- **Weekdays:** `check_dates.py --year 2026` passes. With the payout written without its year, the tool took the event's year from the chart title nearby and flagged the weekday, so the row carries its year.
- Preflight: no type or font errors.

## Round 4 (owner review, 2026-10-18)
**This section describes the page now.** Rebuilt after the round-4 audit scored it 5 of 10 (rebuild). Render: `shot.png`, 1440 x 900 at scale 2.

**One idea:** An organiser sees 1,862 of 2,520 tickets issued as rows of Memphis shapes, one shape for every 20 tickets, solid when issued.

**Why:** The round-4 audit: the ticket shapes sized by sales were good, but the hero used the floating, tilted-fragment tell (a tilted badge and a striped door sign), the headline needed its paragraph, and three textures plus a stats list cluttered it.

### What changed
- **A product screen, not a landing hero:** Plenary's Tickets tab for Kanteel Design Week 2027, with the count as the headline ('1,862 of 2,520 tickets issued', one colour), a totals row (gross, fees, net, next payout) and one action.
- **Nothing tilted or floating:** the badge, the door sign and the lanyard are gone; every shape sits on a strict grid.
- **The decoration carries data, as a count:** each ticket type is one Memphis shape (yellow circle, pink half disc, mint triangle, white square), one shape for every 20 tickets; solid is issued, outline is released and still on sale, and a partly issued shape is filled from the left until that share of its area is covered. This replaced shapes sized by area, which repeated weir (`styles/08`) at gallery size.
- **One face, regular weight:** Bricolage Grotesque, sentence case. No squiggle, dots or stripes now: the outline is the only second state.
- After the fresh audits: one-colour headline, no 'px²' unit, totals moved under the heading, labels centred, then the change from area to count. **After the third audit:** the partial shapes fill by area, not width (the tenth triangle is cut at 38.7% of its width to hold 30% of its area; the 61st half disc at 57.9% for 60%).

### Type scale
Bricolage Grotesque only. 12 labels, 16 body and rows, 21 totals, 51 the headline.

### Blind pairwise test
Three shipped references (Mobbin, cited by link only; images were kept in scratch and deleted). Each pair at the same height, sides random, no labels; fresh judges saw several pairs at once (four sets: 15, 9, 6 and 6 pairs, a new judge each time) and were told to weigh craft, not content. The table gives the result for the final render.

| Reference | Result |
|---|---|
| Eventbrite, https://mobbin.com/screens/0470acb6-b4d1-4b88-a6b7-915d026eed75 | ours better by 4 |
| Sweatpals, https://mobbin.com/screens/d2d7c5d3-5e48-4545-a7cb-d2ffce5e62e3 | ours better by 3 |
| Posh, https://mobbin.com/screens/7d7f34b7-8502-440b-bc06-015b5ff09da6 | ours better by 4 |

**Pass rule:** never lose by 3 or more, and equal or better in at least 2 of 3. Passes. The judges' flaws for ours: white legend swatches that don't match the coloured shapes, and a wide gutter between the labels and the shapes.

### Fresh-eyes audit
Round 1 was a fresh-context auditor given PRESENTATION.md, ROUND3-BRIEF.md, the owner's note, the B2B product screens (product/01, 02, 04, 06), Orbika, Holdfast and Lampwright as the bar, and the three references below. Rounds 2 and 3 went to the same auditor, so they check its own fixes rather than being fresh eyes. Scores: 3, 3, 4. Left open in round 3: Memphis now survives only as palette and shapes (the auditor suggested a flat offset second-colour shadow on each issued shape; not done, to keep the 126 shapes quiet).

### Checks
- `check_dates.py --year 2026` passes; the payout carries its year ('Fri 16 Oct 2026'), since without it the tool takes 2027 from the event line and flags a Saturday.
- `check_names.py`: 0 errors; new words are UI words (Check-in, Payouts) and 'Kanteel Design Week', the registered 'Kanteel Design Week 2027' without its year.
- `engine.py validate`: no errors, 2 warnings, both light-mode contrast of the yellow action colour; this page is dark only.
- Preflight: no type or font errors.
- Re-added from the page: issued 400 + 1,212 + 186 + 64 = 1,862; released 400 + 1,800 + 240 + 80 = 2,520 (74%); gross 116,000 + 509,040 + 22,320 = €647,360; fees 2.5% = 16,184 plus €0.50 x 1,798 paid tickets = 899, so €17,083; net €630,277. Shapes 20 + 90 + 12 + 4 = 126 x 20 = 2,520; issued 20 + 60.6 + 9.3 + 3.2 shapes.

### Left
Memphis is now mostly palette and shape; the legend swatches are white while the shapes are coloured.
