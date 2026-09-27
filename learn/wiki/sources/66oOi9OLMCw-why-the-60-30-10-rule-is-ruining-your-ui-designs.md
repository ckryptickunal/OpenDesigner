---
type: source
title: "Why the 60-30-10 Rule is RUINING Your UI Designs"
created: 2026-09-27
updated: 2026-09-27
video_id: 66oOi9OLMCw
url: https://www.youtube.com/watch?v=66oOi9OLMCw
channel: Kole Jain
published: 2026-01-08T18:08:21Z
authority: reference
tags:
  - color
  - neutrals
  - dark-mode
  - color-ramps
  - oklch
  - semantic-color
  - chart-colors
  - theming
  - borders
  - buttons
  - text-color
  - product-design
---

# Why the 60-30-10 Rule is RUINING Your UI Designs

## Metadata

- Video ID: `66oOi9OLMCw`
- Channel: Kole Jain
- Published: 2026-01-08T18:08:21Z
- URL: https://www.youtube.com/watch?v=66oOi9OLMCw

## Summary

Kole Jain argues that the 60-30-10 color rule suits beginners and websites but does not cover most product design, where a product like Vercel is mostly black and white with a tiny amount of red. He replaces it with four layers of color: a neutral foundation (backgrounds, strokes, text), a functional accent built as a ramp, semantic colors for meaning and charts, and theming. He gives concrete lightness targets for backgrounds, borders, buttons and text, and a rule for dark mode: dark colors look more alike, so the gaps between neutral steps must roughly double and raised surfaces must get lighter. For charts he uses OKLCH, fixing lightness and chroma while stepping the hue, so every color has the same perceived brightness; for themes he shifts every neutral in OKLCH (slightly lower lightness, slightly higher chroma, new hue). For a design system this maps directly onto neutral ramp steps, surface and text tokens, accent ramp step assignments, a dark-mode derivation rule, a categorical chart palette and a theme generator.

## Key Ideas

- The 60-30-10 rule is great for beginners and websites but does not cover most use cases in product design.
- Product color comes in four layers: neutral foundation, functional accent, semantic communication, theming.
- A product UI needs more neutrals than a landing page: about four background layers, one or two strokes and about three text colors, before hover states.
- The app frame or sidebar acts as a slightly darker anchor; because it is large, it needs only a very small shift.
- In light mode, cards can be lighter than the background, darker than it, or a monochrome layer; if cards are pure white, the background should not be.
- Define card edges with a light gray border (about 85% white), not a thin black border; a subtle shadow alone helps only a little.
- The more important a button is, the darker it is, from ghost buttons up to black buttons with white text.
- Text should not be pure black: headings about 11% white, body text 15 to 20%, subtext 30 to 40%.
- Treat the accent as a ramp, not one color: main at 500 or 600, hover at 700, links at 400 or 500.
- Dark mode is not a mirror of light mode: dark colors look more alike, so double the distance between neutral steps.
- In dark mode, surfaces always get lighter as they elevate, text is dimmed, borders are brightened and the primary moves to 300 or 400.
- Semantic colors override the brand system: status must stay readable and destructive actions should be red even with a purple brand.
- Chart colors need a full spectrum at equal perceived brightness, which OKLCH provides by fixing lightness and chroma and stepping hue by about 25 to 30.
- A whole design can be re-themed by shifting every neutral in OKLCH: lower lightness slightly, raise chroma slightly, then change hue.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Channel host presenting the four-layer color approach for product design
- [[entities/60-30-10-rule|60-30-10 rule]] (concept): Classic color-proportion rule the video says is too simple for product design
- [[entities/vercel|Vercel]] (company): Example of a near-monochrome product (about 90% black, 8% white, 2% red) that still uses semantic build-status colors; dark background with lighter cards
- [[entities/linear|Linear]] (company): Example background at 99% white and a blue-purple accent
- [[entities/notion|Notion]] (company): Example of a 100% white background with darker cards
- [[entities/supabase|Supabase]] (company): Example of monochromatic surface layers and a bright green accent
- [[entities/mercury|Mercury]] (company): Example of a sidebar tinted with 2% blue as a darker anchor
- [[entities/oklch|OKLCH]] (concept): Perceptual color model used to get equal perceived brightness across hues for charts and to re-theme neutrals
- [[entities/oklch-com|oklch.com]] (tool): Site used to set lightness and chroma and step the hue for chart colors
- [[entities/ui-colors|UI colors]] (tool): Tool the creator used to generate the accent color ramp (name as spoken; no URL given)
- [[entities/zero-to-mastery|Zero To Mastery]] (company): Video sponsor selling UI/UX courses
- [[entities/figma|Figma]] (tool): The creator offers a Figma file with the colors and variables from the video

## Topics

- [[topics/color|Color]]: Replaces the 60-30-10 rule with four layers for product UI (neutrals, accent ramp, semantic colors, theming) and gives lightness targets for backgrounds, borders, buttons and text.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: Dark mode needs about double the step distance between neutrals, a lighter primary step (300 or 400), dimmer text, brighter borders and lighter raised surfaces; themes can be generated by shifting neutrals in OKLCH.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: On light backgrounds, card edges read best with a roughly 85% white border rather than a thin black border or a shadow alone; in dark mode elevation is shown by lighter surfaces or a border.
- [[topics/visual-hierarchy|Visual hierarchy]]: Darkness signals importance: the most important buttons and headings are darkest, body and subtext progressively lighter.
- [[topics/buttons-and-actions|Buttons and actions]]: Button importance maps to darkness, from ghost to black with white text; most multi-purpose buttons sit around 90 to 95% white; destructive actions should be red.
- [[topics/dashboards-and-data-display|Dashboards and data display]]: Charts need a full-spectrum palette at equal perceived brightness, made in OKLCH by stepping hue by about 25 to 30; a neutral chart is 'super lame' and a single brand ramp makes series look too similar.
- [[topics/saas-product-ui|SaaS product UI]]: Product and dashboard UIs need far more neutral roles than landing pages: several background layers, strokes, text variants and interaction states.
- [[topics/design-resources|Design resources]]: Mentions UI colors for generating ramps and oklch.com for perceptually even chart hues.
- [[topics/cards-and-sections|Cards and sections]]: In light mode cards can be lighter than the page (can be pure white), darker than it (often the sidebar color) or monochromatic layers; card edges on light backgrounds read best with a roughly 85% white border; in dark mode raised cards must be lighter or bordered.

## Notable Claims

- The 60-30-10 rule is good for beginners but does not cover most use cases in product design. Evidence: Description: 'while great for beginners, doesn't really cover most of the use cases'
- Vercel's interface is roughly 90% black, 8% white and 2% red. Evidence: Opening: 'It's like 90% black, 8% white, and 2% red'
- Linear uses a 99% white background, Notion 100% and Vercel 98%. Evidence: Layer one: 'let's talk backgrounds first'
- A landing page works with 3 to 5 neutrals, but product design generally needs four background layers, one or two strokes and about three text variants. Evidence: 'for a landing page, 3 to five neutrals works great'
- Cards on a light background look washed out, and a subtle drop shadow makes this only slightly better. Evidence: 'it looks very washed out'
- Dark colors look more similar to each other, so they need more distance to look as different as light colors. Evidence: 'when you turn down the lights for dark mode, the rules change'
- Simply reflecting the light palette for dark mode makes background elements lose their distinction. Evidence: 'if you just reflect your light palette'
- Light mode is flexible about card and background arrangement; dark mode is not, because surfaces must get lighter as they elevate. Evidence: 'where light mode was more flexible, dark mode is not'
- Using a brand color ramp alone for charts makes the series look too similar. Evidence: Layer 3: 'if we just use our brand color ramp, things look a bit too similar'
- At the same nominal brightness, bright green looks more neon than bright blue. Evidence: 'bright green seems so much more neon than bright blue'
- OKLCH is based on human perception, so it can give the same perceived brightness across different hues. Evidence: 'the solution is the OKLCH palette'
- Shifting neutrals in OKLCH themes a design reliably, and works as well or better in dark mode. Evidence: Layer four, theming: 'works super well, maybe even better for dark mode'

## Quotes

> You might reach for a thin black border. Don't.
> the more important a button is, the darker it is.
> Surfaces always get lighter as they elevate.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Sponsor read for Zero To Mastery (UI/UX design career path, seven courses, 139 hours, a Discord of over half a million students, 10% promo code, free cheat sheet); not part of the lesson.
- Caveat: Plug for a downloadable Figma file with the video's colors and variables.
- Caveat: Auto-caption spellings: Vercel appears as 'versel', 'Verscell' and 'Versella'; Supabase as 'superbase'; oklch.com as 'oklcch.com'; OKLCH as 'okay LCH'; 60-30-10 as '603010'.
- Caveat: The theming step is captioned 'drop the lightness by 003'; since the chroma step is given as 0.02, this is probably 0.03, but the number is kept as captioned [inferred].
- Caveat: Lightness values are given as '% white' without naming a color model (HSL, HSB or OKLCH lightness), so exact conversion to tokens needs checking [inferred].
- Caveat: Product color proportions and background values (Vercel, Linear, Notion, Mercury) are the creator's approximations as of a January 2026 video and may change.
- Caveat: Some statements are taste rather than fact, e.g. a neutral chart being 'super lame'; the video shows its examples visually, which the transcript does not capture.
- Caveat: The source's view that a neutral chart is 'super lame' and a brand ramp looks too similar runs against Q-color-19's current default 'brand-gray' (one brand chart color plus gray) [inferred].

### Rules and practices

- **should** (color, all): For product UI, do not rely on the 60-30-10 rule; plan color as four layers: neutral foundation, functional accent, semantic colors, theming. Why: 60-30-10 is fine for beginners and simple sites but does not cover most product design cases, where products can be almost entirely neutral. Values: 60-30-10, four layers. [the four layers of color theory for product design]
- **consider** (color, all): A pure white page background is acceptable; real products sit between 98% and 100% white. Why: Linear uses 99% white, Notion 100% and Vercel 98%: 'There is some variance, but nothing to say you can't use pure white.' Values: 99% white, 100%, 98%. ['nothing to say you can't use pure white']
- **should** (tokens, all): Budget neutrals by product type: 3 to 5 neutrals for a landing page; for a product, about four background layers, at least one stroke (often two) and about three text colors, before hover and interactive states. Why: Product UIs have more surfaces and states than a landing page. Values: 3 to five neutrals, four layers of backgrounds, at least one stroke, often two, about three text variants. ['for a product design, you'll generally want four layers of backgrounds']
- **should** (color, all): Make the app frame or sidebar a slightly darker anchor than the main content, keeping the shift very small, especially in light mode (for example a 2% blue tint). Why: It is a large element, so a small change is enough to separate it. Values: 2% blue. ['Mercury adds 2% blue to their sidebar']
- **consider** (color, all): If cards are pure white, do not make the page background pure white as well; darker cards can reuse the sidebar color. Why: The source says pure-white cards are 'a good reason not to have pure white as your background'; darker cards are often the sidebar color. Values: pure white. ['which is a good reason not to have pure white as your background']
- **must** (elevation, all): Define card edges on a light background with a border of roughly 85% white; do not use a thin black border. Why: Cards alone look washed out and a subtle drop shadow is only slightly better; roughly 85% white defines the edge without overpowering it. The source says 'Don't' to the thin black border and calls this kind of guidance a rule ('Another great rule'). Values: roughly 85% white. ['You might reach for a thin black border. Don't.']
- **must** (components, all): Make buttons darker the more important they are, from ghost buttons up to black buttons with white text, with everything else in between. Why: The source states it as a rule: 'the more important a button is, the darker it is'. ['Another great rule is the more important a button is, the darker it is']
- **consider** (components, all): Put most multi-purpose buttons around 90 to 95% white. Why: The source gives this as where most multi-purpose buttons sit within the ghost-to-black range; no further reason is given. Values: 90 to 95% white. ['most multi-purpose buttons sit around 90 to 95% white']
- **should** (color, all): Set text colors by importance: reserve the darkest (about 11% white) for important headings, most body text at 15 to 20% white, subtext at 30 to 40%. Why: The source reserves the darkest text for important headings, and even those are only about 11% white rather than pure black; most text and subtext sit lighter. Values: 11% white, 15 to 20% white, 30 to 40%. ['Finally, text. The darkest colors are reserved for important headings']
- **should** (color, all): Build the accent as a full ramp from lightest to darkest and assign steps by job: main color at 500 or 600, hover at 700, links at 400 or 500. Why: The source says not to think of the accent as a single color: main, hover and link use different steps of one scale, and the ramp also helps when switching to dark mode. Values: 500 or 600, 700, 400 or 500. [Layer 2: 'don't think of your color as a single color']
- **should** (color, all): Do not derive dark mode by reflecting the light palette; roughly double the lightness distance between neutral steps (about 2% apart in light becomes four to 6% in dark). Why: Dark colors look more similar, so reflected steps lose their distinction. Values: double the distance, 2% white, four to 6%. ['a good rule of thumb is double the distance']
- **should** (color, all): In dark mode, move the primary brand color to step 300 or 400 with hover at 400 or 500, dim the text and brighten the borders. Why: The light-mode steps and contrasts do not carry over; the difference is noticeable to anyone staring at the screen all day. Values: 300 or 400, 400 or 500. ['choose a 300 or 400 as our primary brand color on dark mode']
- **must** (elevation, all): In dark mode, make raised surfaces lighter than what they sit on, or give them only a border (like a search bar). Why: Unlike light mode, dark mode is not flexible: surfaces always get lighter as they elevate. ['Surfaces always get lighter as they elevate']
- **must** (color, all): Always include semantic colors for states such as success, failure and in progress, even when the brand is black and white. Why: Colors convey meaning, so the semantic layer has to break the neutral system; Vercel still shows build status in color. [Layer 3: 'you'll always need some semantic colors']
- **must** (color, all): Make destructive actions red regardless of the brand color. Why: The source calls a non-red destructive action 'pretty much a design sin', even with a purple brand. ['it's pretty much a design sin to make destructive actions anything other than red']
- **should** (color, all): Build chart colors in OKLCH: fix lightness and chroma, then step the hue by about 25 to 30 for each series, instead of using neutrals or only the brand ramp. Why: Neutral charts look dull, a single brand ramp looks too similar, and hues at the same nominal brightness look unequal (green looks more neon than blue); OKLCH gives equal perceived brightness. Values: 25 to 30. ['increment the hue by about 25 to 30']
- **consider** (color, all): To create a color-themed version of a design, convert every neutral to OKLCH, drop lightness by 003 (as captioned) and raise chroma by 0.02, then set the hue to the theme color. Why: Instead of guessing each neutral, the OKLCH shift themes any design to red, green or blue 'bang on the money every single time', and works super well, maybe even better, for dark mode. Values: 003, 0.02. [Layer four, theming: 'drop the lightness by 003 and increase the chroma by 0.02']

### Decisions it informs

- In light mode, how should cards relate to the page background? (`Q-color-14`)
  - Dark background, lighter cards: Cards are lighter than the page and can be pure white, which is a reason not to make the page pure white. When: When cards should be the brightest surface (the source's example is Vercel).
  - Light background, darker cards: Cards are darker than the page and are often the same color as the sidebar. When: When the page is pure white (the source's example is Notion).
  - Monochromatic layers: Surfaces are stacked shades of one color [inferred: the source names this option without describing it]. When: The source's example is Supabase; it gives no rule for when to pick it.
  - Recommendation: No single option; the source says light mode is flexible here, while dark mode is not (surfaces always get lighter as they elevate).
- Should the page background be pure white or slightly off-white?
  - Pure white (100%): Brightest possible canvas, as in Notion. When: When cards are darker than the background.
  - Near white (98 to 99%): A barely visible gray that lets pure-white cards stand out, as in Linear (99%) and Vercel (98%). When: When cards or raised elements will be pure white.
  - Recommendation: The source says nothing rules out pure white, but if cards are pure white the background should not be.
- How should card edges be defined on a light background? (`Q-depth-01`)
  - No edge: Cards look washed out against the background. When: Not recommended by the source.
  - Subtle drop shadow: Only slightly better than no edge. When: Not enough on its own, per the source.
  - Thin black border: Too strong for the edge [inferred: the source says the 85% border defines the edge 'but not overpower it', implying black does]. When: Never: the source says 'Don't.'
  - Light gray border (about 85% white): Defines the edge without overpowering it. When: Default for cards on light backgrounds.
  - Recommendation: Use roughly 85% white for the border, because it defines the edge without overpowering it.
- Should the product add a colored accent, or stay neutral? (`Q-color-02`)
  - Stay neutral: Black, white and grays carry the UI; color appears only where meaning needs it (Vercel). When: When the brand is monochrome.
  - Functional accent: One hue becomes recognisable across the product and drives main actions, hovers and links (Linear blue-purple, Supabase bright green). When: When the brand has a signature color.
- How should dark mode be derived from the light palette? (`Q-color-16`)
  - Reflect the light palette: Background elements lose almost all distinction because dark colors look more alike. When: The source advises against it.
  - Stretch the neutral steps (double the distance): Surfaces stay distinct: about 2% steps in light become 4 to 6% in dark; primary moves to 300 or 400, text dims, borders brighten. When: Default.
  - Recommendation: Double the distance between neutral steps rather than reflecting, because dark colors need more separation to look as different.
- Which colors should charts use? (`Q-color-19`)
  - Neutral chart: Grays only; the source calls it 'super lame'. When: Not recommended.
  - Brand color ramp: Series look too similar to tell apart easily. When: Not recommended for multi-series charts.
  - Full spectrum at equal perceived brightness (OKLCH): Every hue looks equally bright, so no series (e.g. green) looks more neon than another. When: Default for charts.
  - Recommendation: Use a full spectrum from OKLCH with fixed lightness and chroma, stepping hue by about 25 to 30.
- How should a color-themed version of the design (red, green, blue) be produced?
  - Guess each neutral by eye: Possible, but the source presents the OKLCH shift as the better way. When: The source mentions it only as the alternative to the OKLCH method.
  - Shift every neutral in OKLCH: Lower lightness slightly, raise chroma by 0.02 and set a new hue; the whole design tints consistently, in light and dark mode. When: When the design needs themed variants.
  - Recommendation: Use the OKLCH shift for every neutral, which the source says lands 'bang on the money every single time'.

### Process

1. Lay the neutral foundation: Pick the page background (pure or near white), a slightly darker frame or sidebar anchor, card surfaces, one or two strokes (about 85% white for card edges) and about three text colors (headings about 11% white, body 15 to 20%, subtext 30 to 40%).
2. Set button emphasis: Order buttons from ghost to black with white text by importance; most multi-purpose buttons around 90 to 95% white.
3. Add a functional accent ramp: Generate a full ramp for the accent (the creator used UI colors); use 500 or 600 as the main color, 700 for hover and 400 or 500 for links.
4. Derive dark mode: Stretch the neutral steps to about double the distance (2% becomes 4 to 6%), move the primary to 300 or 400 with hover at 400 or 500, dim text, brighten borders, and make raised surfaces lighter or bordered.
5. Add semantic colors: Add status colors (success, failed, in progress) and make destructive actions red, regardless of the brand color.
6. Build the chart palette: On oklch.com set a lightness and chroma, then increment hue by about 25 to 30 for each chart color.
7. Generate themes: For each neutral, plug its hex into OKLCH, drop lightness by 003 (as captioned), raise chroma by 0.02 and set the hue to the theme color; the same trick works for dark mode.

### Examples and visual references

- Near-monochrome product palette (Vercel): About 90% black, 8% white and 2% red, showing a product that barely uses an accent yet still shows build success, failure and in-progress states in color.
- Background lightness comparison (Linear, Notion, Vercel): Backgrounds at 99%, 100% and 98% white: small variance, showing pure white is acceptable.
- Tinted sidebar anchor (Mercury): Sidebar with 2% blue added, a barely darker frame around the content.
- Three light-mode card arrangements (Vercel, Notion, Supabase): Dark background with lighter cards (Vercel), light background with darker cards (Notion), monochromatic layers (Supabase).
- Card edge treatments compared: Cards on a light background shown washed out, then with a subtle shadow (slightly better), then with a roughly 85% white border that defines the edge; a good before/after visual sample [inferred].
- Button darkness range: Buttons from ghost to black with white text, darker as they get more important; most multi-purpose buttons around 90 to 95% white.
- Accent colors as brand identity (Linear, Supabase): Linear is recognised by blue-purple, Supabase by bright green.
- Dark-mode raised element with only a border: A search bar in dark mode defined by a border rather than a lighter fill.
- Uneven perceived brightness across hues: Bright green looks more neon than bright blue, motivating OKLCH chart colors with equal perceived brightness.
- One design themed red, green and blue: Every neutral shifted in OKLCH (lightness down, chroma up by 0.02, new hue) to produce red, green and blue themed versions, in light and dark mode.

### Numbers

- 60-30-10: The classic color-proportion rule the video argues against for product UI [Title and opening ('603010' in the caption)]
- 90% black, 8% white, and 2% red: Vercel's approximate color proportions [Opening]
- 99% / 100% / 98%: Background whiteness of Linear, Notion and Vercel [Layer one, backgrounds]
- 3 to five: Neutrals that work for a landing page ['3 to five neutrals works great']
- four layers of backgrounds: Background layers typically needed in product design, plus at least one stroke (often two) and about three text variants [Layer one]
- at least one stroke, often two: Strokes needed in product design [Layer one]
- about three text variants: Text colors needed in product design [Layer one]
- 2% blue: Tint Mercury adds to its sidebar ['Mercury adds 2% blue']
- roughly 85% white: Border color to define card edges on light backgrounds ['use roughly 85% white to define the edge']
- 90 to 95% white: Where most multi-purpose buttons sit [Button rule]
- about 11% white: Darkest text, for important headings [Text section]
- 15 to 20% white: Most body text [Text section]
- 30 to 40%: Subtext [Text section]
- 500 or 600 / 700 / 400 or 500: Light-mode accent ramp steps for main color / hover / link [Layer 2]
- 2% / four to 6%: Distance between neutral steps in light mode vs dark mode ['double the distance']
- 300 or 400 / 400 or 500: Dark-mode primary step / hover step [Dark mode section]
- 25 to 30: Hue increment between chart colors in OKLCH [Layer 3, charts]
- 003 and 0.02: OKLCH lightness drop and chroma increase for theming neutrals [Layer four, theming]

<!-- /od:learn -->
