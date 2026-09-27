---
type: source
title: The 8 UI/UX Cheat Codes for INSTANTLY Better Designs
created: 2026-09-27
updated: 2026-09-27
video_id: c1TvOcKdBVE
url: https://www.youtube.com/watch?v=c1TvOcKdBVE
channel: Kole Jain
published: 2025-03-27T01:42:08Z
authority: reference
tags:
  - kerning
  - letter-spacing
  - display-type
  - nested-radius
  - corner-smoothing
  - hsb
  - color-palette
  - hue-shift
  - card-layout
  - dividers
  - spacing-grid
  - tinted-backgrounds
---

# The 8 UI/UX Cheat Codes for INSTANTLY Better Designs

## Metadata

- Video ID: `c1TvOcKdBVE`
- Channel: Kole Jain
- Published: 2025-03-27T01:42:08Z
- URL: https://www.youtube.com/watch?v=c1TvOcKdBVE

## Summary

Kole Jain walks through eight quick fixes that make interface designs look more polished. They cover tightening letter spacing on very large text, rounding nested corners correctly and smoothing corners, building a matching color palette by stepping saturation, brightness and hue in HSB, and redesigning a listing card by grouping and ranking information instead of labelling every field. He also argues for separating list items with space instead of divider lines, keeping spacing on a 4 or 8 pixel grid, and tinting backgrounds with the accent color instead of using pure white or black. For dark mode he builds depth from lighter, less saturated surface layers instead of shadows. For a design system, these give concrete starting values for display letter spacing, nested radius, palette steps, spacing base, tinted backgrounds and dark-mode surface layers.

## Key Ideas

- Kerning (letter spacing) looks fine at small sizes, but large text over roughly 70 to 80 pixels needs tightening, around -2 to -4%.
- When one rounded shape sits inside another, give the inner corner a smaller radius: outer radius minus the gap between them.
- Pill shapes need no nested-radius correction because the gap is the same all the way around.
- Corner smoothing (Figma's iOS corner smoothing) subtly tapers the curve before the corner, making rounded corners look rounder.
- A matching palette can be built in HSB from one base color by adding about 20 saturation and removing about 10 brightness per step.
- Shifting hue toward blue for darker steps improves the palette, because blues and purples read darkest and yellows and reds lightest.
- Card layouts improve when obvious labels are removed, related facts are grouped, and groups are ordered by importance.
- Divider lines are often redundant clutter; spacing items far enough apart usually separates them better.
- If list items must sit close together, subtle alternating row backgrounds beat lines everywhere.
- Consistent spacing on a 4 or 8 pixel base grid makes small components look noticeably more organized.
- At large sizes, exact 8-pixel steps matter less; round to 5 or 10, or grow sizes exponentially.
- Backgrounds tinted with a dark or light version of the accent color bring more color into a design than pure black or white.
- In dark mode, depth comes from cards with different background colors: each layer slightly brighter and less saturated.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): UI/UX designer and YouTuber who presents the eight tips.
- [[entities/mobbin|Mobbin]] (product): UI reference library and Figma plugin that sponsors the video.
- [[entities/figma|Figma]] (tool): Design tool used for every demo: kerning, HSB color picker, iOS corner smoothing and the nudge amount setting.
- [[entities/coolors|Coolors]] (tool): Color generator suggested for finding a starting base color; the auto-caption reads 'coolers', taken to be Coolors [inferred].
- [[entities/tailwind-css|Tailwind CSS]] (library): Its color palette is offered as a shortcut for accent and background pairs in light and dark mode.
- [[entities/github|GitHub]] (company): Example of a dark-mode site that uses a very dark blue background instead of pure black.
- [[entities/hsb|HSB]] (concept): Hue, saturation, brightness color model used to derive matching palette colors and dark-mode surface layers.
- [[entities/ios-corner-smoothing|iOS corner smoothing]] (concept): Figma corner setting that tapers the curve before the corner, making rounded corners look rounder.
- [[entities/kerning|Kerning]] (concept): Space between letters; the video tightens it on large text.

## Topics

- [[topics/typography|Typography]]: Tighten letter spacing to about -2 to -4% on text larger than roughly 70 to 80 pixels, because fonts that look good as paragraphs can look disjointed when scaled up.
- [[topics/shape-and-corner-radius|Shape and corner radius]]: Nested corners need a smaller inner radius (outer radius minus the gap), pills need no correction, and Figma's iOS corner smoothing at maximum makes corners subtly rounder.
- [[topics/color|Color]]: Build matching colors in HSB from a base: +20 saturation and -10 brightness per step, optionally shifting hue about 20 points toward blue for darker steps. Tint backgrounds with the accent instead of pure black or white.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: Use a really dark accent-tinted background (GitHub uses a really dark blue) instead of pure black, or Tailwind's 300 as primary with 950 as background; create depth with brighter, less saturated card layers, since depth is a lot harder without shadows.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: Lines are often redundant clutter; separate items with space or alternating row backgrounds. In dark mode, the best way to create depth is cards with different background colors.
- [[topics/spacing-and-layout|Spacing and layout]]: Keep spacing on a 4 or 8 pixel base grid; round larger sizes to 5 or 10 or scale them exponentially; space list items far enough apart instead of drawing lines between them.
- [[topics/visual-hierarchy|Visual hierarchy]]: Rank information on a card by importance, group related items, and drop labels the layout already implies.
- [[topics/cards-and-sections|Cards and sections]]: A short-term rental listing card is redesigned by stacking name with location and cost with rating, putting listing details in one row with icons, and giving check-in and check-out their own labelled row.
- [[topics/figma-and-design-tools|Figma and design tools]]: Switch the color picker from hex to HSB, use iOS corner smoothing, and change the nudge amount from 10 to 8 in preferences to stay on an 8 pixel grid.
- [[topics/design-resources|Design resources]]: Coolors for a starting base color and the Tailwind CSS color palette for ready-made accent and background pairs.

## Notable Claims

- Figma handles kerning well at smaller text sizes, but at sizes generally over 70 to 80 pixels kerning starts to matter more. Evidence: Kerning on large text: 'on larger Tech sizes generally over 70 to 80 pixels'
- Fonts that look great as paragraphs can look disjointed when scaled up without adjusting kerning. Evidence: Kerning on large text: 'scale it up and it' look disjointed'
- When a rounded corner sits inside another with the same radius, the distance between them is equal on straight edges but increases at the corner. Evidence: Fixing rounded corners: 'as soon as we come to the corner the distance increases'
- The outer-radius-minus-gap rule breaks down once the inner corner is more than 30 pixels away, so the presenter estimates by eye. Evidence: Fixing rounded corners: 'breaks down as soon as the inner corner is more than 30 pixels away'
- Pill shapes need no nested-radius adjustment because the distance is the same all the way around. Evidence: Fixing rounded corners: 'if you got a pill shape'
- Blues and purples tend to be the darkest hues, while yellows and reds are the lightest. Evidence: Better color palettes: 'blues and purples tend to be the darkest'
- Lines are often redundant and add clutter, unless lines are the chosen visual style. Evidence: Lose the lines
- List items become harder to read as they are packed closer together. Evidence: Lose the lines: 'pack them closer and closer together'
- A 4 or 8 pixel base grid makes small elements look noticeably more organized. Evidence: Keep spacing consistent, easily
- At larger sizes an 8-pixel difference, such as 120 versus 128, does not make a visible difference. Evidence: Keep spacing consistent: 'the difference between 120 and 128'
- GitHub and a lot of other dark-mode software landing pages use a really dark blue background instead of pure black. Evidence: Create better backgrounds: 'on GitHub and a lot of other dark mode software'
- Pairing Tailwind's 50 background with its 500 accent (light) or its 950 background with its 300 primary (dark) works for every color in the Tailwind palette. Evidence: Create better backgrounds: 'it works for every single color combo on there'
- Depth is a lot harder in dark mode when you have no shadows; the best way to create it is cards with different background colors. Evidence: Depth on dark modes: 'depth is a lot harder when you have no Shadows'

## Quotes

> the fix is easy just round the inner Corner less
> lines are often redundant and add clutter to a design
> the fewer elements you can use to get your point across the better

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Mobbin sponsors the video: a mid-video read about its UI library and Figma plugin, a link in the description that the presenter says helps support the channel, and a reminder at the end.
- Caveat: Many values are the presenter's rules of thumb, not measurements: he appears to say he eyeballs kerning (caption: 'I just ey all this') [inferred], he prefers to estimate nested radii by eye, and he personally prefers the hue-shifted palette.
- Caveat: The claim that the Tailwind 50/500 and 300/950 pairs work for every color is the presenter's assertion; the transcript mentions no contrast check.
- Caveat: Auto-caption fixes used here: 'King' as kerning, 'mobin' as Mobbin, 'coolers' as Coolors, 'contact' as context, 'read the labels' as re-add the labels, 'Tech sizes' as text sizes; 'axel grid' is read as an 8 pixel grid because the fix changes the nudge amount to 8 [inferred].
- Caveat: The demo palette shapes are captioned 'folder', 'band' and 'strip', and one example site as 'Studio rubric'; these names are uncertain.
- Caveat: Figma interface details (HSB picker, iOS corner smoothing, nudge amount default of 10) reflect Figma as of the video's publication in March 2025.
- Caveat: The video mentions an earlier video for the kerning example design; that video is not part of this source.

### Rules and practices

- **should** (typography, all): Tighten letter spacing to between -2% and -4% on text larger than about 70 to 80 pixels. Why: Figma handles kerning at small sizes, but large text looks disjointed with zero kerning. Values: -2 to -4%, over 70 to 80 pixels. [Kerning on large text]
- **should** (shape, all): Give a nested inner corner a smaller radius: the outer radius minus the gap between the two shapes. Why: With equal radii the gap stays even on the straight edges but widens at the corner. Values: 30 pixel radius, 10 pixel Gap, 20 pixels. [Fixing rounded corners: 'take the outer Corner radius and subtract the distance']
- **consider** (shape, all): Treat outer-radius-minus-gap as a guide and estimate the inner radius by eye, especially when the gap is larger than the outer radius (more than 30 pixels in the 30 pixel example). Why: The subtraction rule breaks down once the inner corner is more than 30 pixels away, so the presenter prefers to squint and guesstimate. Values: more than 30 pixels away. [Fixing rounded corners: 'I just prefer to squint guesstimate']
- **consider** (shape, all): Skip the nested-radius correction for pill shapes. Why: A pill keeps the same distance all the way around, so you don't need to do any of this. [Fixing rounded corners: 'if you got a pill shape']
- **consider** (shape, all): For extra-round corners, set Figma's iOS corner smoothing to the maximum on all four corners. Why: It subtly tapers the curve before the corner, which makes rounded corners look rounder. Values: iOS Corner smoothing to the max. [Fixing rounded corners: 'dial up the iOS Corner smoothing']
- **should** (color, all): Derive each additional palette color from the previous one in HSB by increasing saturation by about 20 and decreasing brightness by about 10. Why: This gives an objective way to get colors that match a base color without guessing. Values: saturation by about 20, brightness by about 10. [Better color palettes: 'increase our saturation by about 20']
- **consider** (color, all): When deriving a darker palette color, also slide the hue about 20 points toward blue. Why: Blues and purples read darkest and yellows and reds lightest, so a darker step should move toward a darker hue; the presenter prefers this version. Values: about 20 points. [Better color palettes: 'we slide towards blue about 20 points']
- **should** (components, all): Remove field labels from a card when the layout already makes each value clear, and keep labels only where values could be confused (such as check-in and check-out). Why: If the UI can't imply the labels, the layout isn't doing its job; check-in and check-out keep labels so they don't get mixed up. [Don't be lame with card layouts]
- **should** (components, all): Group related facts on a card and order the groups by importance, putting the least important group last. Why: Name and location go together, as do cost and rating; check-in and check-out matter least because everything else must be good first. [Don't be lame with card layouts: 'rank the order of importance']
- **consider** (components, all): Put a card's secondary details (such as the listing details) in a single row and add icons for context. Why: Part of making the card better by being a bit more creative than listing every field. [Don't be lame with card layouts: 'add some icons for some more contact']
- **should** (layout, all): Don't separate list items with divider lines unless lines are the product's chosen style; space the items far enough apart instead. Why: Lines are often redundant and add clutter; enough spacing keeps items legible and clearly separate. [Lose the lines]
- **should** (layout, all): If list items must be spaced tightly, use a subtle background on alternating rows instead of lines. Why: It separates rows with fewer elements than lines everywhere. [Lose the lines: 'a subtle background on alternating rows']
- **should** (layout, all): Use as few elements as possible to get the point across; for example, prefer space or alternating backgrounds over lines everywhere. Why: The source states the fewer elements you can use to get your point across, the better. [Lose the lines: 'the fewer elements you can use to get your point across the better']
- **should** (layout, all): Build spacing on a 4 pixel or 8 pixel base grid, especially for small elements. Why: It makes designs look noticeably more organized. Values: 4 pixel, 8 pixel. [Keep spacing consistent, easily]
- **consider** (tooling, all): When working on an 8 pixel grid, change Figma's nudge amount from the default of 10 to eight. Why: You then always stay aligned with your grid, even when making small adjustments. Values: default of 10 to eight. [Keep spacing consistent: 'nudge amount change that from the default of 10 to eight']
- **consider** (layout, all): For large sizes, round to the nearest 5 or 10, or if you must stay on 8, make the steps grow exponentially. Why: At large sizes a small difference like 120 versus 128 is not noticeable. Values: nearest 5 or 10, 120, 128. [Keep spacing consistent: 'round to the nearest 5 or 10']
- **should** (color, all): Use a very dark or very light version of the accent color as the background instead of pure black or pure white. Why: It incorporates more color into the design; GitHub and a lot of other dark-mode software landing pages use a really dark blue instead of pure black. [Create better backgrounds]
- **consider** (color, all): As a shortcut, take a Tailwind color: its 50 as the light background with its 500 as the accent, or its 950 as the dark background with its 300 as the primary. Why: The presenter says these pairs work for every color in the Tailwind palette. Values: 50, 500, 300, 950. [Create better backgrounds: 'copy the 50 color value and the corresponding 500']
- **should** (elevation, all): In dark mode, show depth with card layers whose background is slightly brighter (about four to six) and less saturated (10 to 20) than the layer below, repeating the step for each extra layer. Why: Depth is a lot harder when you have no shadows; cards with different background colors are the best way to create depth, for great depth every single time. Values: brightness slightly by about four to six, saturation by 10 to 20. [Depth on dark modes]

### Decisions it informs

- Should large headings keep the font's default letter spacing or be tightened? (`Q-type-13`)
  - Default (zero kerning): Large text can look loose and disjointed. When: Normal text sizes, where Figma sorts kerning out automatically.
  - Tightened -2 to -4%: Avoids large text looking disjointed; the difference is subtle side by side. When: Text generally over 70 to 80 pixels.
  - Recommendation: Tighten large text by -2 to -4%, especially given the rise of larger text on websites.
- How should the radius of a corner nested inside another corner be set? (`Q-pref-03`)
  - Same radius as the outer corner: The gap is equal on the straight edges but increases at the corner, which looks off. When: Not recommended: the source calls the widening gap an issue.
  - Outer radius minus the gap: The gap stays even around the corner (30 px outer with a 10 px gap gives a 20 px inner radius). When: When the gap is smaller than the outer radius.
  - Estimate by eye: Works where the formula breaks down; the presenter's own preference. When: When the inner corner is more than 30 pixels away (in the 30 pixel example).
  - No correction (pill): A pill keeps the same distance all the way around. When: Pill-shaped elements.
  - Recommendation: Round the inner corner less using outer radius minus the gap; estimate by eye when the gap is large; pills need nothing.
- Should rounded corners be plain circular arcs or smoothed? (`Q-shape-04`)
  - Standard rounded corners: Regular curve into the corner. When: The baseline the demo compares against.
  - iOS corner smoothing at maximum: The curve tapers subtly before the corner, so corners look rounder; hard to see unless stacked side by side. When: When you want to lean into the rounded-corner trend.
  - Recommendation: Dial iOS corner smoothing to the max if you want to lean into rounded corners.
- When deriving matching colors from a base color, should the hue stay fixed or shift?
  - Fixed hue: Each step is the base with +20 saturation and -10 brightness; colors match but stay in one hue. When: Simplest starting point.
  - Hue shifted toward blue: Each darker step also slides about 20 points toward blue, which the presenter says makes the palette even better. When: When you want a better palette; blues and purples tend to be the darkest hues.
  - Recommendation: The presenter personally prefers the hue-shifted version but asks viewers to judge.
- How should items in a list be separated? (`Q-depth-05`)
  - Divider lines: Often redundant and adds clutter to a design. When: When lines are the product's deliberate style.
  - Space: Items read as clearly separate with fewer elements; packing them closer makes them harder to read. When: Default for lists.
  - Alternating row backgrounds: Subtle stripes separate rows without lines everywhere. When: When items must be spaced tightly.
  - Recommendation: Space items apart; if they must be tight, use subtle alternating backgrounds instead of lines.
- What base unit should spacing follow? (`Q-space-01`)
  - 4 pixel grid: Consistent spacing that looks noticeably more organized, especially on smaller elements. When: The source offers 4 or 8 without choosing.
  - 8 pixel grid: Consistent spacing; set Figma's nudge amount to eight to stay aligned. When: The source offers 4 or 8 without choosing.
  - Recommendation: Use either a 4 or 8 pixel base grid; the source does not choose between them.
- What color should the page background be? (`Q-color-09`)
  - Pure white or pure black: Neutral, with less color in the design. When: Not recommended by the source.
  - Accent-tinted background: A really dark tint (GitHub uses a really dark blue) or a very light one (a site captioned 'Studio rubric' uses a very light orange) incorporates more color into the design. When: Default recommendation.
  - Tailwind pair: Light: 50 background with 500 accent. Dark: 950 background with 300 primary. When: When you don't want to pick colors yourself.
  - Recommendation: Use a darker or lighter version of the accent color instead of pure white or black.
- How should cards stand out from the page in dark mode? (`Q-depth-01`)
  - Shadows: The source says depth is a lot harder in dark mode when you have no shadows. When: Not the source's recommendation for dark mode.
  - Tonal layers: Each card layer is slightly brighter (about four to six) and less saturated (10 to 20) than the one below; repeat for many layers, like on a dashboard. When: Dark mode, especially with many layers like a dashboard.
  - Recommendation: Use cards with different background colors, stepping brightness up and saturation down per layer.
- How should spacing and sizes step once they get large? (`Q-space-02`)
  - Round to the nearest 5 or 10: Looser values at large sizes, where an 8 pixel difference is not noticeable. When: The presenter's usual habit for larger sizes.
  - Grow exponentially on the 8 pixel grid: Stays on the grid while steps get much bigger, since 120 versus 128 makes no difference. When: If you need to stick to 8 pixels.
  - Recommendation: At larger sizes the presenter rounds to the nearest 5 or 10; if you must stay on 8, make sizes exponentially larger.
- How dark should the dark-mode background be? (`Q-color-21`)
  - Pure black: Less color in the design. When: Not recommended by the source.
  - Really dark accent tint: A really dark blue, as on GitHub and a lot of other dark-mode software landing pages. When: Default recommendation for dark mode.
  - Tailwind 950: Use the 950 value as the background with 300 as the primary color. When: When you don't want to pick colors yourself.
  - Recommendation: Use a darker version of the accent color instead of pure black.

### Process

1. Pick a base color: Start from a good base color; if you don't have one, use a color generator such as Coolors.
2. Switch the picker to HSB: In Figma's color picker, change from hex to HSB so hue, saturation and brightness can be edited separately.
3. Derive the next colors: Leave hue alone at first; for each next color add about 20 saturation and remove about 10 brightness from the previous one.
4. Shift hue for darker steps: For a richer version, slide each darker step about 20 points toward blue before applying the saturation and brightness change.
5. Strip implied labels from a card: Remove labels the layout already makes clear.
6. Group and rank card content: Group like items (name with location, cost with rating, listing details, check-in with check-out) and order the groups by importance.
7. Lay out the groups: Stack name with location and cost with rating, put listing details in one row with icons for context, and give check-in and check-out their own row with labels restored.
8. Set the nudge amount: In Figma preferences, change the nudge amount from 10 to 8 when working on an 8 pixel grid.
9. Build dark-mode layers: From the dark background, raise brightness by about four to six and lower saturation by 10 to 20 for each card layer; repeat for each additional layer.

### Examples and visual references

- Large heading shown side by side with zero kerning and with -2 to -4% kerning (One of the presenter's earlier designs): The difference is subtle side by side; untightened large text can look disjointed.
- A rounded rectangle nested inside another with the same radius, then corrected: The gap is even along the edges but widens at the corner; rounding the inner corner less (30 px outer, 10 px gap, 20 px inner) fixes it.
- Two stacked shapes, one with iOS corner smoothing and one without (Figma): The smoothed corner tapers before the corner and looks rounder; the difference is only visible when stacked.
- Three-color palette built from a base in HSB, compared with and without hue shift: The version where darker steps shift toward blue is the presenter's preferred option; the demo shapes are captioned as 'folder', 'band' and 'strip'.
- Short-term rental listing card, before and after: Before: every field listed with a label. After: name and location stacked, cost and rating stacked, listing details in one row with icons, check-in and check-out in their own labelled row.
- A list separated by lines versus by spacing, then packed tighter: Items become harder to read as they move closer; alternating subtle row backgrounds work when spacing must be tight.
- Dark-mode landing page with a really dark blue background instead of pure black (GitHub): Shows an accent-tinted dark background bringing color into the design.
- Site with a very light orange background (A site captioned as 'Studio rubric' (name uncertain from auto-captions)): Shows an accent-tinted light background instead of pure white.
- Dark dashboard with several card layers: Each layer is slightly brighter and less saturated than the one beneath, creating depth without shadows.

### Numbers

- 8: Number of UI/UX cheat codes in the video [Title]
- 70 to 80 pixels: Text size above which kerning starts to matter more [Kerning on large text]
- -2 to -4%: Reasonable kerning for large text [Kerning on large text]
- 30 pixel radius: Outer radius in the worked nested-radius example [Fixing rounded corners]
- 10 pixel Gap: Gap between the nested shapes in the worked example [Fixing rounded corners]
- 20 pixels: Resulting inner radius: 30 minus 10 [Fixing rounded corners]
- 30 pixels: Distance beyond which the subtraction rule breaks down in the example [Fixing rounded corners]
- about 20: Saturation added per derived palette color in HSB [Better color palettes]
- about 10: Brightness removed per derived palette color in HSB [Better color palettes]
- about 20 points: Hue shift toward blue for darker palette colors [Better color palettes]
- 4 pixel or 8 pixel: Typical base grid for consistent spacing [Keep spacing consistent, easily]
- 10 to eight: Changing Figma's default nudge amount to match the grid [Keep spacing consistent, easily]
- nearest 5 or 10: Rounding for larger sizes [Keep spacing consistent, easily]
- 120 and 128: Example of a difference too small to matter at large sizes [Keep spacing consistent, easily]
- 50: Tailwind color value to use as a light background [Create better backgrounds]
- 500: Corresponding Tailwind color value to use as the accent on a light background [Create better backgrounds]
- 300: Tailwind color value to use as the primary color in dark mode [Create better backgrounds]
- 950: Tailwind color value to use as the dark-mode background [Create better backgrounds]
- about four to six: Brightness increase per dark-mode card layer [Depth on dark modes]
- 10 to 20: Saturation decrease per dark-mode card layer [Depth on dark modes]

<!-- /od:learn -->
