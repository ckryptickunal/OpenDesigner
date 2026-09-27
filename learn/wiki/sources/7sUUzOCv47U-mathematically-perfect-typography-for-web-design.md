---
type: source
title: Mathematically Perfect Typography for Web Design
created: 2026-09-27
updated: 2026-09-27
video_id: 7sUUzOCv47U
url: https://www.youtube.com/watch?v=7sUUzOCv47U
channel: Kole Jain
published: 2024-06-09T14:00:05Z
authority: reference
tags:
  - typography
  - font-pairing
  - type-scale
  - golden-ratio
  - fluid-type
  - line-height
  - letter-spacing
  - font-weight
  - text-hierarchy
  - responsive
  - kole-jain
---

# Mathematically Perfect Typography for Web Design

## Metadata

- Video ID: `7sUUzOCv47U`
- Channel: Kole Jain
- Published: 2024-06-09T14:00:05Z
- URL: https://www.youtube.com/watch?v=7sUUzOCv47U

## Summary

Kole Jain walks through web typography from the basics to a sizing formula. He covers font categories (serif, sans-serif, display, handwritten), the parts of a letter that matter to designers (baseline, x-height, cap height, letter spacing), and how many fonts to pair (one is entirely acceptable, two is the limit). He shows that font weight and text color (opacity) both control hierarchy, and argues that size should carry the heading, bold should make subheadings scannable, and paragraphs should stay at full opacity. For sizes he derives a type scale from the golden ratio (1.62), recommends its square root (1.27) for a full style guide and its cube root for dense or small-screen interfaces, then describes a fluid formula that scales each size between a 320 and a 1920 wide screen, optionally capped with min and max. Font colors, weights and pairings stay the same on every screen; only sizes change. For a design system this gives concrete defaults for font count, weight and opacity levels, the scale ratio, fluid sizing and line height.

## Key Ideas

- Fonts fall into serif and sans-serif, plus two growing subgroups: display fonts for giant text and handwritten fonts that imitate handwriting.
- Most everyday interfaces use sans-serif fonts because they read as cleaner and more modern.
- Letter spacing should shrink proportionately as text grows and grow as text shrinks.
- One font is entirely acceptable, two is the limit, three is pushing it and four invites problems.
- Display and handwritten fonts must never be used for small paragraph text.
- At small sizes, a thinner weight and a lighter color look alike because both reduce dark pixels, so either can set hierarchy.
- Rank every text element first, then style it: size gives the heading attention, bold makes subheadings scannable, and paragraphs keep full opacity.
- Making the smallest text also the lowest-contrast text hurts both usability and looks.
- Eyeballing one page and building a style guide around it is not wrong, but a ratio-based type scale improves on it.
- Multiplying by the golden ratio (1.62) at every step grows too fast; its square root (1.27) works across a whole style guide.
- The cube root of the golden ratio gives a tighter scale for dashboards with many text styles or for mobile screens with less room.
- Font colors, weights and pairings can stay constant on any screen; only font sizes change with screen size.
- One fluid formula can scale each text size between the smallest and largest screen width without breakpoints.
- Cap fluid sizes with min and max unless growing past the design widths works for the design.
- Line height should rise as text gets smaller or lines get longer, and fall as text gets larger.
- Always check text on the screens the design is intended for.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): YouTube designer presenting his approach to typography and his fluid sizing formula.
- [[entities/leonardo-bonacci-fibonacci|Leonardo Bonacci (Fibonacci)]] (person): Better known as Fibonacci; his sequence is used to explain where the golden ratio comes from.
- [[entities/golden-ratio|Golden ratio]] (concept): Approximated as 1.62 from the Fibonacci sequence; the base of the proposed type scale.
- [[entities/fibonacci-sequence|Fibonacci sequence]] (concept): Number sequence whose neighbouring terms divide to approximate the golden ratio.
- [[entities/serif-font|Serif font]] (concept): Font with small ticks on letter ends; presented as older, more authoritative and used in books and magazines.
- [[entities/sans-serif-font|Sans-serif font]] (concept): Font without ticks; presented as cleaner and more modern and the default for interfaces.
- [[entities/display-font|Display font]] (concept): Ornamented font meant for giant text, impractical at paragraph size.
- [[entities/handwritten-font|Handwritten font]] (concept): Font imitating human handwriting; can stand in for a display font.
- [[entities/baseline|Baseline]] (concept): The line letters sit on and extend up or down from.
- [[entities/x-height|X-height]] (concept): The lower of the two main letter heights, measured off the letter x.
- [[entities/cap-height|Cap height]] (concept): The height of taller letters, measured off flat-bottomed letters like the capital E.
- [[entities/letter-spacing|Letter spacing]] (concept): Space between letters, adjusted mainly by text size.
- [[entities/line-height|Line height]] (concept): Space between lines; set per size, with suggested percentages for paragraphs and headings.
- [[entities/google-fonts|Google Fonts]] (product): Source of many of the free fonts mentioned in the video.
- [[entities/courier-prime|Courier Prime]] (product): Font Kole uses for small details and image captions on his three-font portfolio.
- [[entities/comic-sans|Comic Sans]] (product): Font mentioned as a joke that all designers dislike.
- [[entities/arial|Arial]] (product): Mentioned as the fallback designers settle on after searching Google Fonts.
- [[entities/youtube-instagram-and-x-twitter|YouTube, Instagram and X (Twitter)]] (product): Examples of everyday interfaces that use sans-serif fonts.

## Topics

- [[topics/typography|Typography]]: Font categories, anatomy (baseline, x-height, cap height), letter spacing, font pairing limits, weight and opacity ranges, a golden-ratio type scale, a fluid size formula with min and max caps, and line-height percentages.
- [[topics/visual-hierarchy|Visual hierarchy]]: List every text element's rank, then use size, weight and color. Let size carry the heading, bold the subheadings for scanning, and keep paragraphs at full opacity rather than making the smallest text the faintest.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Build the style guide's font sizes from a ratio (square root of the golden ratio, 1.27, from a 16 pixel base) instead of eyeballing one page and deriving the rest.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Describes a single CSS line that scales text linearly between the smallest (320) and largest (1920) screen widths, bounded with max() for the lower limit and min() for the upper limit.
- [[topics/design-process|Design process]]: Replace 'eyeball one page, then build a style guide' with a systematic scale, and always review designs on the screens they are meant for.
- [[topics/dashboards-and-data-display|Dashboards and data display]]: Suggests the cube root of the golden ratio as a tighter scale for dashboards that need many different font styles.

## Notable Claims

- Serif fonts date back to ancient Greek times, so they are seen as older and perhaps more authoritative. Evidence: Sara fonts date back to ancient Greek times
- Serif fonts are easier to read at smaller font sizes, which is why books and magazines use them. Evidence: easier to read at smaller font sizes which is why books and magazines use them
- Sans-serif fonts are more common now because they are cleaner and more modern; YouTube, Instagram and X use them. Evidence: most interfaces you use on a daily basis use sansera fonts
- Display fonts carry ornamentation and detail that would be impractical scaled down to paragraph size. Evidence: display fonts are used for giant text elements
- The x-height is measured off the letter x because letters like e extend just above the line. Evidence: X is always the letter that the lower height is measured off of
- Larger text needs proportionately less letter spacing and smaller text proportionately more. Evidence: larger text requiring proportionately less space
- Many industry-standard sites use just one font. Evidence: many industry standard sites use one font
- At small sizes, reducing weight and reducing opacity look very similar because both mean fewer dark pixels. Evidence: fewer dark pixels through reducing the weight or reducing the opacity
- If the smallest text also has the least contrast, the layout is neither very usable nor attractive. Evidence: with the smallest text also having the least contrast
- Making the heading large already gives it the most attention regardless of weight or opacity. Evidence: by making the heading text large we already give it the most attention
- Dividing the larger of two consecutive Fibonacci numbers by the smaller approximates the golden ratio, 1.62. Evidence: an approximation of the golden ratio which is 1.62
- Starting at 16 pixels and multiplying each size by 1.62 gives a largest header of 110 pixels with only four header sizes and a paragraph. Evidence: our largest header is 110 pixels large
- The square root of the golden ratio is 1.27 and works as a scaling system for a full style guide. Evidence: square rooted it to get 1.27
- Applying the square-rooted golden ratio to a design is not a massive change but looks subtly better. Evidence: not a massive change but it definitely looks subtly better
- Adjusting each text size at breakpoints could be messy, especially if close control over the sizes is required (captioned as 'Min control'; the exact word is unclear). Evidence: the previous solution was to have break points
- A linear formula based on the current screen width scales text between the smallest and largest sizes without breakpoints, and keeps growing or shrinking past the chosen widths unless capped. Evidence: our line extends past our smallest and largest size
- Most designers keep line height on auto about 95% of the time, but auto falls off a little for extremely large text. Evidence: keep line height on auto for like 95% of the time
- You will probably reuse the same three fonts for 90% of your projects, and that is okay. Evidence: the same three fonts for 90% of your projects and that's okay
- Font colors, weights and pairings can stay constant on any screen, while font sizes change with screen size. Evidence: fonts change size based on the screen size

## Quotes

> never ever use a display font or a handwritten font for small paragraph text
> three is pushing the envelope and four is asking for problems
> always remember to view your designs on the screen they were intended for

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Opinion framed as 'mathematically perfect': the golden-ratio scale and fluid formula are the creator's personal method ('my magic equation'), not a standard.
- Caveat: The actual CSS line is described in words, not shown in the transcript; the transcript does not name clamp() or viewport units.
- Caveat: The cube-root value of the golden ratio is recommended but never stated as a number (about 1.17 [inferred]).
- Caveat: Historical and readability claims about serif fonts (ancient Greek origin, easier to read small) are stated without evidence.
- Caveat: The Comic Sans remark is a joke, not guidance.
- Caveat: Auto-caption errors: 'seraps' is serifs, 'sansera/sanser' is sans-serif, 'aial' is Arial, 'Comic Sands' is Comic Sans, 'Sara fonts' and 'serf' are serif, 'US designers' is 'us designers', 'Min'/'mint' in the min and max passage is min(); 'Min control over the sizes' is unclear (possibly 'minute control'). The portfolio's display and sans-serif font names ('fola 1', 'AXA Forma') and the word before Courier Prime ('a s font') are garbled and should not be treated as font names.
- Caveat: Visuals (layouts, graph, before/after) are described from narration only; no media list exists for this video.
- Caveat: Published 2024-06-09; closes with a standard subscribe request. The stored video description is truncated. No sponsor segment appears in the transcript.

### Rules and practices

- **should** (typography, all): Use one or two font families; treat a third as a rare edge case and avoid four. Why: One font is entirely acceptable and used by many industry-standard sites; three pushes the envelope and four invites problems. [one font is entirely acceptable]
- **consider** (typography, all): If the system uses a single font, make it a sans-serif. Why: A single-font site is generally sans-serif unless it deliberately wants an old-timey, medieval feel. [if you opt for one it's generally going to be a sanser font]
- **consider** (typography, all): For a two-font pairing, pair a display font with a sans-serif, or a sans-serif with a serif; a handwritten font may replace the display font. Why: These are the pairings seen on most modern websites. [usually it's either a display font and a sansera font]
- **must** (typography, all): Never set small paragraph text in a display font or a handwritten font; keep them for giant text elements. Why: Their extra ornamentation and detail become impractical at paragraph size; the source calls it a design sin. [that is 100% a design sin]
- **should** (typography, all): Reduce letter spacing proportionately as text gets larger, and increase it as text gets smaller. Why: Letter spacing is adjusted mostly by text size: larger text needs proportionately less space, smaller text more. [larger text requiring proportionately less space and smaller text requiring proportionately more]
- **should** (typography, all): Avoid ultra bold and ultra thin weights for regular text. Why: Stay away from extremes when choosing weights for regular text. [try and stay away from extremes with ultra bold and ultra thin]
- **should** (typography, all): Set primary text at 100% opacity and secondary text somewhere between 40 and 70% opacity. Why: Avoid extremes with font colors just as with weights; these two levels work for creating hierarchy. Values: 100%, 40 to 70%. [100% opacity and somewhere between 40 to 70% is good]
- **should** (typography, all): Make weight and color steps visually different enough that each level reads as a distinct level of hierarchy. Why: Weights and colors only create hierarchy if the difference is visible. [things are visually different enough to actually create hierarchy]
- **consider** (typography, all): Use either weight or color (opacity) to push small text forward or back; both work because each reduces the number of dark pixels. Why: At small sizes a thinner weight and a lighter color look very similar. [we can use both color and weights to manipulate hierarchy]
- **should** (process, all): Before styling, list every text element in order of importance (for example header first, subheadings second, paragraphs third), then apply font styles to match that order. Why: You should literally be able to list the hierarchy of all text elements and style them accordingly. [you should literally be able to list the hierarchy of all the text elements]
- **should** (typography, all): Do not make paragraph text lighter than the rest; keep paragraphs at 100% opacity so the smallest text is not also the lowest-contrast text. Why: Smallest text with the least contrast is neither very usable nor aesthetic. Values: 100%. [we want the opacity to be 100%]
- **consider** (typography, all): Let a large size carry the heading's emphasis instead of automatically also making it bold and full-strength. Why: Making the heading large already gives it the most attention regardless of thickness or opacity. [the header doesn't automatically become bolded]
- **consider** (typography, all): Make subheadings bold so they are easy to scan and stand out more than paragraph text. Why: Subheadings should be easily scannable and pop more than the paragraph. [we'll make it bold]
- **consider** (typography, all): Derive font sizes from a scale ratio instead of eyeballing one page and building the style guide around it. Why: Eyeballing one page is not wrong but can be improved with a ratio-based scale. [it's not wrong but it can be improved]
- **consider** (typography, all): With only a heading and body text, make the heading the body size multiplied by 1.62. Why: Multiplying body text by the golden ratio gives a heading size that looks pretty good in the most basic layouts. Values: 1.62. [multiply the body text by 1.62 to get the size of the header text]
- **should** (typography, all): Do not multiply every step of a multi-size scale by the full golden ratio (1.62) from a 16 px base. Why: Sizes grow too large too quickly: with four header sizes and a paragraph the largest header reaches 110 pixels. Values: 16 pixel, 1.62, 110 pixels. [our font sizes start to get very large a little too quickly]
- **consider** (typography, all): Use the square root of the golden ratio, 1.27, as the ratio between consecutive font sizes in a full style guide. Why: It leaves room for an in-between size such as a subheading and works across many font sizes. Values: 1.27. [square rooted it to get 1.27]
- **consider** (typography, all): Use the cube root of the golden ratio for a tighter scale when the interface has many font styles (such as a dashboard) or little room (such as mobile). Why: It gives smaller scaling steps when you need them. [Cube rooting the golden ratio]
- **should** (typography, web): Scale each font size fluidly: smallest size + (largest size - smallest size) x (current screen width - smallest width) / (largest width - smallest width), instead of setting sizes at breakpoints. Why: Adjusting each size at breakpoints could be messy; one line of CSS scales text for every screen size. Values: 1920, 320. [with this single line of CSS we can have scale text]
- **consider** (typography, web): Use 320 as the smallest and 1920 as the largest screen width in the fluid formula, adjusting if needed. Why: These are the widths the source generally uses, while noting you can play with them. Values: 1920, 320. [I generally use 1920 as the largest width and 320 as the smallest width]
- **consider** (typography, css): Cap fluid font sizes: wrap the formula in max() with the lower bound and min() with the upper bound, unless letting text keep growing on larger screens works for the design. Why: The linear formula keeps producing larger or smaller sizes past the chosen widths. [set a cap on the size with a simple Min and Max]
- **should** (typography, all): Increase line height as text gets smaller or lines get longer, and reduce it as text gets larger. Why: It makes text easier to read. [the line height should increase to make things easier to read]
- **should** (typography, all): Set paragraph line height around 150% and heading line height around 110 to 130%. Why: A rule of thumb for readable text; automatic line height falls off toward extremely large text. Values: 150 %, 110 to 130%. [for paragraph text line height should be around 150 %]
- **consider** (typography, all): Do not leave line height on auto for very large text. Why: Most designers leave line height on auto, but it falls off a little for extremely large text. [especially towards extremely large text it falls off]
- **should** (process, all): Review designs on the screen sizes they were intended for to check text size, colors and fonts. Why: It is the way to see whether the typography actually makes sense. [view your designs on the screen they were intended for]
- **consider** (typography, all): Keep font pairings, weights and colors the same on every screen size; let only font sizes change with the screen. Why: Colors, weights and pairings can stay constant on any screen, while sizes change with screen size. [font colors weights and pairings can stay constant on any screen]
- **consider** (typography, all): If a third font is used, pair a display font and a sans-serif with a third font reserved for small details or captions under images. Why: That is the three-font pattern the source has seen elsewhere and uses on his own portfolio, framed as an edge case. [a s font for small details or captions under images]

### Decisions it informs

- How many fonts should the system use, and how should they be paired? (`Q-type-05`)
  - One font (usually sans-serif): Clean and consistent; hierarchy comes from size, weight and color. When: Default; many industry-standard sites do this.
  - Two fonts: display + sans-serif: Headlines get personality from an ornamented display font while body text stays clean. When: Most modern websites that want expressive headings.
  - Two fonts: sans-serif + serif: Mixes a modern sans with a more traditional, authoritative serif. When: When some text should read as more classic or editorial [inferred].
  - Two fonts: handwritten + sans-serif: A handwritten font takes the display role for a personal, human feel. When: Acceptable in place of a display font.
  - Three fonts: display + sans-serif + small-detail font: A third font (Courier Prime on Kole's portfolio) marks small details or image captions. When: Edge case; pushing the envelope.
  - Recommendation: One font is entirely acceptable and two is the limit; three is pushing it and four is asking for problems.
- Which font category should the main text use? (`Q-type-03`)
  - Sans-serif: Cleaner and more modern; what most everyday interfaces use (YouTube, Instagram, X). When: Most interfaces.
  - Serif: Reads as older and perhaps more authoritative; said to be easier to read at small sizes. When: Books, magazines, or an old-timey, medieval style site.
  - Display: Extra ornamentation and detail for giant text. When: Only for large headline elements, never paragraphs.
  - Handwritten: Imitates human handwriting with varying success. When: As a display font substitute, never for small paragraph text.
  - Recommendation: Use a sans-serif when there is only one font; keep display and handwritten fonts for large text.
- Should hierarchy between text levels come from weight, color, or both? (`Q-type-12`)
  - Color (opacity) only: Same weight throughout; lower levels are lighter (for example 40 to 70% opacity against 100%). When: When a single weight should be kept; shown in a layout that only uses color.
  - Weight only: Same color throughout; levels differ by thickness. When: When all text should stay at full opacity; shown in a layout that only uses weights.
  - Both: Weight and color changes used together across levels. When: The source says both can manipulate hierarchy but does not show a combined layout.
  - Recommendation: Both work because at small sizes thinner weight and lighter color look similar; avoid extremes (ultra bold, ultra thin) and make each level visibly different.
- How should a heading, subheadings and paragraphs be styled to show their order?
  - Bold full-opacity heading, plain subheadings, lighter paragraphs: The predictable approach; the smallest text ends up with the least contrast. When: Not recommended: neither very usable nor aesthetic.
  - Large plain heading, bold subheadings, full-opacity paragraphs: Size alone makes the heading lead, subheadings are easy to scan, and body text stays readable. When: Recommended starting point.
  - Recommendation: Let size carry the heading, bold the subheadings for scanning, and keep paragraphs at 100% opacity.
- What ratio should separate each font size from the one below it? (`Q-type-09`)
  - Golden ratio, 1.62: Strong jumps; from 16 px, four header sizes reach 110 px, which is too large too quickly. When: Only a heading and body text.
  - Square root of the golden ratio, 1.27: Gentler steps that leave room for in-between sizes like subheadings; looks subtly better applied to a design. When: A full style guide with several sizes.
  - Cube root of the golden ratio: Even smaller steps between sizes. When: Dashboards with many font styles, or mobile interfaces with less room.
  - Eyeball one page: Sizes set by feel on one page, then a style guide built around it. When: The source's old method: not wrong, but can be improved.
  - Recommendation: Use the square root of the golden ratio (1.27) from a 16 px base for a full style guide; use the cube root for dense or small-screen interfaces.
- Should text sizes change with screen width, and how? (`Q-type-15`)
  - Breakpoints: Each text size is adjusted at set screen widths; could be messy when close control over sizes is needed. When: The previous common approach.
  - Fluid formula: Each size scales linearly from its smallest value at a 320 wide screen to its largest at a 1920 wide screen, with no breakpoints. When: When text should look right on every screen size.
  - Recommendation: Use the single-line fluid formula so text scales from mobile to desktop without breakpoints.
- Should fluid text keep growing or shrinking beyond the chosen smallest and largest screen widths?
  - Uncapped: Larger screens than the largest width get even larger text; smaller screens get smaller text. When: If that works in the design.
  - Capped with min and max: Text stops at the lower and upper bounds regardless of screen size. When: Otherwise.
  - Recommendation: Cap it unless growth works for the design: max() holds the lower bound and min() holds the upper bound.
- How should line height be set? (`Q-type-11`)
  - Auto: What most designers use about 95% of the time; falls off a little toward extremely large text. When: The common habit the source moves away from.
  - Percentage by role: Around 150% for paragraphs and 110 to 130% for headings; higher for smaller text or longer lines, lower for larger text. When: The source's rule of thumb.
  - Recommendation: Set line height explicitly: around 150% for paragraph text and 110 to 130% for heading text.

### Process

1. Choose font categories and pairing: Start with one sans-serif font; add a second (display, serif or handwritten) only if needed. Keep display and handwritten fonts away from paragraph text.
2. Rank the text elements: List every text element in order of importance, for example header first, subheadings second, paragraphs third.
3. Build the size scale: Start from a 16 px base and multiply by the square root of the golden ratio (1.27) for each step; use the cube root for dashboards or mobile, or 1.62 when there is only a heading and body text.
4. Assign weight and color: Avoid ultra bold and ultra thin. Use 100% opacity and a second level between 40 and 70%. Let size carry the heading, bold the subheadings and keep paragraphs at 100% opacity.
5. Set letter spacing by size: Tighten proportionately for large text and loosen for small text.
6. Make sizes fluid: For each style, pick its size on the smallest screen (320 wide) and the largest (1920 wide), then compute smallest size + (largest size - smallest size) x (current width - 320) / (1920 - 320).
7. Cap the fluid sizes: Unless growth past those widths suits the design, wrap the formula in max() with the lower bound and min() with the upper bound.
8. Set line heights: About 150% for paragraphs and 110 to 130% for headings; raise it for smaller text or longer lines, lower it for larger text.
9. Check on real screens: View the design on the screens it is intended for to confirm sizes, colors and fonts make sense.

### Examples and visual references

- Everyday apps using sans-serif fonts (YouTube, Instagram, X (Twitter)): Cited as interfaces people use daily that rely on sans-serif fonts.
- Serif fonts in print (Books and magazines): Cited as the reason serifs are associated with readability at small sizes.
- Font anatomy diagram: Baseline, x-height (measured off x, with e slightly above it) and cap height (measured off a flat-bottomed capital E) marked on sample letters.
- Three-font portfolio (Kole Jain's portfolio website): A display font, a sans-serif, and Courier Prime for small details and image captions; discussed as an edge case for using three fonts.
- Weight versus color demo: The same text made thinner and, separately, lighter in color; at small sizes the two look similar. Two versions of one layout, one using only color and one using only weights, for hierarchy.
- Two ways to style a heading, subheadings and paragraphs: First: bold full-opacity heading, plain subheadings and lighter paragraphs, where the smallest text has the least contrast. Second: large plain heading, bold subheadings and full-opacity paragraphs, which reads better.
- Golden-ratio scale growing too fast: A style guide from 16 px multiplied by 1.62 per step; with four header sizes the largest reaches 110 px.
- Square-root golden ratio applied to a design: Before and after of one design re-sized with the 1.27 ratio; a subtle improvement, flipped back and forth for comparison.
- Fluid font-size graph: A straight line of font size against screen width, extending past the smallest and largest sizes, used to show why min and max caps may be needed.

### Numbers

- 1.62: Approximation of the golden ratio; body size x 1.62 gives a heading size [the golden ratio which is 1.62]
- 1.27: Square root of the golden ratio, proposed as the scale ratio for a full style guide [square rooted it to get 1.27]
- 16 pixel: Base font size for the example scale [if we start with the 16 pixel base font size]
- 110 pixels: Largest header when a 16 px base is multiplied by 1.62 across four header sizes [our largest header is 110 pixels large]
- 1920: Largest screen width used in the fluid formula [I generally use 1920 as the largest width]
- 320: Smallest screen width used in the fluid formula [320 as the smallest width]
- 100%: Opacity for primary text, and for paragraphs in the recommended hierarchy [100% opacity and somewhere between 40 to 70% is good]
- 40 to 70%: Opacity range for lighter secondary text [somewhere between 40 to 70% is good]
- 150 %: Rule-of-thumb line height for paragraph text [for paragraph text line height should be around 150 %]
- 110 to 130%: Rule-of-thumb line height for heading text [for heading text line height should be around 110 to 130%]
- 90%: Share of projects where you will likely reuse the same three fonts [the same three fonts for 90% of your projects]
- 95%: How often designers leave line height on auto, per the source's guess [keep line height on auto for like 95% of the time]
- four: Number of fonts that is 'asking for problems' (one is acceptable, two is the limit, three is pushing the envelope) [four is asking for problems]

<!-- /od:learn -->
