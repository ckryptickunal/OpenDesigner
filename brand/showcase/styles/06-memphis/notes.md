# 06 Plenary: a Memphis landing section for conference ticketing

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
