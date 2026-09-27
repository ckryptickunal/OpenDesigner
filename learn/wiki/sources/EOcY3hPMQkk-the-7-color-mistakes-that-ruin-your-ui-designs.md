---
type: source
title: The 7 Color Mistakes that RUIN your UI Designs
created: 2026-09-27
updated: 2026-09-27
video_id: EOcY3hPMQkk
url: https://www.youtube.com/watch?v=EOcY3hPMQkk
channel: Kole Jain
published: 2025-09-14T02:45:41Z
authority: reference
tags:
  - color
  - palette
  - 60-30-10
  - neutral-balance
  - contrast
  - wcag
  - brand-color
  - analogous
  - complementary
  - grays
  - dark-mode
  - semantic-color
---

# The 7 Color Mistakes that RUIN your UI Designs

## Metadata

- Video ID: `EOcY3hPMQkk`
- Channel: Kole Jain
- Published: 2025-09-14T02:45:41Z
- URL: https://www.youtube.com/watch?v=EOcY3hPMQkk

## Summary

Kole Jain redesigns a file management app to show the common color mistakes that make beginner UIs look cheap or confusing, arguing that less color is almost always better. He covers cutting competing accent colors, keeping backgrounds neutral (which he calls neutral balance), stretching a small brand palette with analogous and complementary hues, and using grays instead of pure black and white to build hierarchy. He shows that dark mode should be designed on purpose rather than made by inverting light mode, that destructive actions need red even when it is off-brand, and that hover, press and disabled states can be made from lighter, darker and desaturated versions of the base color. For a design system, this gives concrete rules for accent use, neutral surfaces, text grays, dark-mode adjustments, semantic colors and state colors, plus brand examples (Lemon Squeezy, Headspace, Dribbble, Mailchimp, Airbnb).

## Key Ideas

- Less is almost always more with color: not everything should be a different color.
- Several accent colors on one screen compete for attention; reducing the palette creates clarity.
- The 60-30-10 rule splits a screen into 60% dominant neutral, 30% secondary and 10% accent color.
- A brand color on an unimportant element can dominate the page; lighten it and switch its text to black.
- Icons are recognizable symbols and mostly need no color; color on icons should signal status, such as an active tab.
- Neutral balance works like white space: backgrounds should stay in the background, so start with a neutral gray background and a white or very light foreground.
- A neutral gray can carry a hint of the brand hue to add color without overpowering the visuals.
- Sometimes the cleanest way to separate a card is a simple border rather than another background layer.
- A limited brand palette can be extended by rotating the brand hue slightly (analogous) or crossing the color wheel (complementary).
- Brand colors can be adapted, for example darkened, to pass contrast checks and serve good design.
- Pure black and white are not wrong, but grays are often the better option for hierarchy; less important text, labels and borders can be gray.
- Dark mode is not the inverse of light mode: borders and surfaces need more separation, text should be light gray, and pure white is kept for the most important items.
- Destructive actions use red even when the brand color is different, which is why red and green sit in many brand palettes.
- Hover is slightly lighter or brighter, press is slightly darker and disabled is desaturated; mobile has no hover, so it relies on press effects.
- The seven mistakes the title promises are, in order: too many colors, no neutral balance, being stuck with brand colors, overusing pure black and white, inverting for dark mode, on-brand destructive actions, and missing element states [inferred]

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Creator of the channel; presents the file management app redesign.
- [[entities/lemon-squeezy|Lemon Squeezy]] (company): Colorful example of the 60-30-10 rule: purple 60%, yellow 30%, white as the accent in one section.
- [[entities/headspace|Headspace]] (company): Uses a tint of its bright orange in card backgrounds to add color without overpowering the visuals.
- [[entities/dribbble|Dribbble]] (company): Example of reversing background and foreground in light mode for a small UI feature (its search bar).
- [[entities/mailchimp|Mailchimp]] (company): Bright yellow primary paired with a complementary turquoise secondary.
- [[entities/airbnb|Airbnb]] (company): Very bright pink paired with a much deeper pink.
- [[entities/wcag|WCAG]] (concept): Contrast checks used to judge whether card colors and brand colors with white text are usable.
- [[entities/60-30-10-rule|60-30-10 rule]] (concept): Color proportion guide: 60% dominant neutral, 30% secondary, 10% accent.
- [[entities/neutral-balance|Neutral balance]] (concept): Using neutral color the way white space is used, so backgrounds recede and hierarchy is clear.
- [[entities/figma|Figma]] (tool): The redesign's Figma files are linked in the description.

## Topics

- [[topics/color|Color]]: Reduce competing accents, follow 60-30-10 loosely, keep backgrounds neutral, extend a small brand palette with analogous and complementary hues, and use grays instead of pure black and white for hierarchy.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: Do not invert light mode: brighten borders and cards, use light grays for text, reserve pure white for the most important text or actions, lower gray brightness more aggressively, and desaturate the logo a touch.
- [[topics/accessibility|Accessibility]]: Colored cards and brand colors with white text often fail WCAG contrast checks; lighten backgrounds with black text, darken the brand color, or pick a complementary color that passes.
- [[topics/visual-hierarchy|Visual hierarchy]]: Neutral balance works like white space; secondary information such as file size, type and labels can be dark or light gray instead of black.
- [[topics/buttons-and-actions|Buttons and actions]]: Delete buttons use red rather than the brand color; hover is lighter or brighter, press darker, disabled desaturated, and a light gray button with white text reads as disabled on its own.
- [[topics/icons-and-imagery|Icons and imagery]]: Icons mostly need no color; color on an icon should communicate status, such as the active tab.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: Instead of adding another colored background layer to cards, a simple border is sometimes the best way to separate them.
- [[topics/cards-and-sections|Cards and sections]]: Do not give each card its own bright accent; lighten a brand-colored card and switch its text to black, use a light brand tint behind cards (Headspace), or drop the card background and use a simple border.

## Notable Claims

- Most of the brightly colored cards in the starting design fail WCAG contrast checks, so they cannot reasonably be used. Evidence: they almost all fail the WCAG contrast checks
- The 60-30-10 rule means 60% dominant neutral color, 30% secondary color and 10% accent color. Evidence: 60% of our dominant neutral color, 30% secondary color, and 10% accent color
- Lemon Squeezy uses purple as the 60%, yellow as the 30%, and white as the accent in one section. Evidence: Lemon Squeezy is a good and very colorful example
- Five or more accent colors on the cards compete for attention. Evidence: at least five different accent colors on these cards
- Using the bright brand color on the cards makes an unimportant element dominate the page and creates accessibility issues. Evidence: The bright purple dominates the page
- Reducing the palette creates more clarity for the user. Evidence: By reducing our palette, we've already created more clarity for the user
- Bright colors are almost never right for backgrounds, because backgrounds should stay in the background. Evidence: Almost never will you want bright colors for your background
- Headspace uses a tint of its bright orange in card backgrounds to add color without overpowering the visuals. Evidence: Headspace does this very thing
- In light mode, reversing background and foreground can give better accessibility for smaller UI features such as Dribbble's search bar. Evidence: reversing the background and foreground
- Analogous and complementary colors derived from the brand color work well together in the UI. Evidence: they're analogous and complimentary colors
- An orange brand color that fails WCAG with white text passes once darkened, and a complementary blue also passes. Evidence: fails WCAG checks with white text
- Mailchimp pairs bright yellow with a complementary turquoise, and Airbnb pairs a very bright pink with a much deeper pink. Evidence: Take Mailchimp for example
- Dark colors need to be more different from each other than light colors for the difference to be visible. Evidence: dark colors need to be more different than light colors
- Inverting all light-mode colors gives a dark mode that is not awful but not ideal. Evidence: If we were to inverse all the colors on our light mode
- A brand-colored delete button draws attention and does not show that the action is destructive. Evidence: draws attention to the button and doesn't illustrate its destructive nature
- Red and green are often in a brand's color palette even when they are not brand colors, for usability. Evidence: red and green are often in a brand's color palette
- A light gray button with white text reads as disabled without any other visual cue, and this also holds in dark mode. Evidence: this button is obviously disabled
- Mobile has no hover effects, so designs rely on press effects; a slightly darker gray on press feels like pressing into something. Evidence: we don't have hover effects on mobile
- Using more gray and less black and white is what separates mediocre designers from professional ones (opinion). Evidence: Getting comfortable with using more gray

## Quotes

> Less is almost always more with color.
> For the most part, icons need no color.
> dark mode is not just the inverse of light mode.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Sponsor segment for Final Round AI (job search), repeated at the end; not design advice.
- Caveat: Self-promotion: a resources page on kolejain.com and the Figma files in the description.
- Caveat: Auto-caption errors: '603010' is the 60-30-10 rule and the 'BY' before it is a mis-hearing; 'complimentary' means complementary; 'dribble' is Dribbble.
- Caveat: The seven mistakes are not numbered in the transcript; the list in key_ideas is an inferred grouping.
- Caveat: The source treats 60-30-10 loosely (the redesign only 'somewhat' hits it); OpenDesigner's Q-color-05 already treats 60-30-10 as a soft check [inferred]
- Caveat: Several statements are opinion, such as using more gray being what separates mediocre from professional designers.
- Caveat: Brand examples (Lemon Squeezy, Headspace, Dribbble, Mailchimp, Airbnb) reflect their designs around the September 2025 publish date and may have changed.
- Caveat: Color values (hex codes, exact contrast ratios, tint amounts) are shown on screen but not stated in the transcript, so none are recorded here.
- Caveat: The hint of purple in the neutral gray and the Headspace tint are introduced right after the dark-mode point, so it is unclear whether the source means dark mode only or both modes.
- Caveat: Strength 'must' is used only where the transcript is firm (WCAG failures 'we can't reasonably use', an on-brand delete button 'wouldn't fly'); other points are hedged ('almost always', 'not bad', 'notable exceptions') and kept as should or consider.

### Rules and practices

- **should** (color, all): Do not give each card or element its own accent color; keep one accent and reduce the palette. Why: At least five different accent colors on the cards all compete for attention; reducing the palette creates clarity. [at least five different accent colors on these cards]
- **must** (accessibility, all): Check colored card and text pairs against WCAG contrast and drop colors that fail. Why: Cards that fail the WCAG contrast checks cannot reasonably be used. [they almost all fail the WCAG contrast checks]
- **consider** (color, all): Use the 60-30-10 split as a rough check: about 60% dominant neutral, 30% secondary color, 10% accent. Why: Five accents competing for attention is the problem it addresses; the redesign only 'somewhat' hits it, so it works as a guide rather than a strict rule [inferred] Values: 60%, 30%, 10%. [603010 rule]
- **should** (color, all): When a brand-colored surface belongs to an unimportant element, lighten the color and switch its text to black. Why: The bright brand color dominates the page for an element that isn't important and causes accessibility issues. [A good fix is to lighten it up]
- **should** (iconography, all): Leave icons uncolored and reserve icon color for status, such as marking the active tab. Why: An icon's job is to be a recognizable symbol; color should communicate status. [icons need no color]
- **should** (color, all): Remove colors that are used only for the sake of using color. Why: Reducing the palette creates more clarity for the user. [used just for the sake of using color]
- **should** (color, all): Do not use bright colors or bright gradients for page backgrounds; start with a neutral gray background and a very light or white foreground. Why: Backgrounds should stay in the background (neutral balance, the color version of white space); the sandy yellow gradient did not. [Almost never will you want bright colors for your background]
- **should** (color, all): In dark mode, put the darker colors in the background and slightly lighter colors in the foreground. Why: Same neutral-balance idea as light mode. [This is the same idea for a dark mode]
- **consider** (color, all): Add a hint of the brand hue to neutral grays, or use a light tint of the brand color on card backgrounds, to bring in color without overpowering the visuals. Why: It adds a splash of color without overpowering the visuals (Headspace does this with a tint of its orange on cards). [adding a hint of purple to it]
- **consider** (color, all): In light mode, consider reversing the usual background and foreground for smaller UI features such as a search bar. Why: It can give better accessibility for smaller UI features, as in Dribbble's search bar. [reversing the background and foreground]
- **consider** (elevation, all): To separate cards, prefer a simple border over adding another colored background layer. Why: Adding another layer of color to the UI is a lot of clutter; maintaining neutral balance sometimes means removing backgrounds altogether. [sometimes a simple border is the best solution]
- **should** (color, all): When the brand palette is too small, extend it by rotating the brand hue slightly on the color wheel (analogous) or picking the color across the wheel (complementary), rather than only changing opacity. Why: Changing opacity feels bland; analogous and complementary colors work well together on the UI. [rotate our purple slightly on the color wheel]
- **should** (accessibility, all): If a brand color fails WCAG with white text, darken it until it passes or use a complementary color that passes. Why: The orange brand color failed with white text; the darker version and a complementary blue both pass. [fails WCAG checks with white text]
- **should** (color, all): Adapt brand colors when needed to accommodate good design instead of treating brand guidelines as fixed. Why: Many brands do this, such as Mailchimp's yellow with turquoise and Airbnb's bright pink with a deeper pink. [don't be afraid to adapt brand colors]
- **should** (color, all): Use dark gray, not pure black, for less important information such as file size and file type, and the same for labels and borders; well-grouped elements can go lighter still. Why: Hierarchy: this information isn't super important, and because the elements are well grouped they can be lightened. [we can use a dark gray instead]
- **consider** (color, all): In light mode, consider a very dark brand hue (such as dark purple) for text instead of pure black. Why: Often there are better options than black or white; most of the redesign's text is light gray or dark purple, not black. [most of the text is light gray or dark purple, not even black]
- **should** (color, all): In dark mode, lower the brightness of grays more aggressively than in light mode and reserve white for only the most important actions. Why: Dark modes have a distinct focus on eye strain. [Reserving white only for the most important actions]
- **should** (color, all): Do not make dark mode by inverting the light-mode colors; build the palette with the goals of dark mode in mind. Why: Inverting gives a result that is not awful but certainly not ideal. [dark mode is not just the inverse of light mode]
- **should** (color, all): In dark mode, brighten borders and main card surfaces more than an inversion would. Why: Dark colors need to be more different than light colors to see the difference. [brighten up these borders and the main card]
- **should** (color, all): In dark mode, use light grays for text and brighten only the most important text (for example the logo and storage used) to pure white. Why: Light grays are easier on the eyes than white. [light grays work best on dark mode]
- **consider** (color, all): In dark mode, desaturate the logo a touch. Why: The source gives no reason; its redesign does this when converting to dark mode, while saying the other colors are probably fine. [our logo should be desaturated a touch]
- **must** (components, all): Use red, not the brand color, for destructive actions such as delete. Why: A brand-colored delete button draws attention and doesn't illustrate its destructive nature; it wouldn't fly from a usability point of view. [Instead, we use red; wouldn't fly from a usability point of view]
- **should** (color, all): Include red and green in the palette even when they are not brand colors. Why: Usability needs them, for example for destructive actions. [red and green are often in a brand's color palette]
- **consider** (color, all): Notification indicators may use red or the brand color. Why: Notifications are much more flexible than destructive actions. [Red is also often used for notifications]
- **should** (components, all): Make hover states a slightly lighter or brighter version of the base color. Why: Hover and press are the most common element states, and color alone can show them. [For hover states, use a slightly lighter or brighter version]
- **should** (components, all): Make active or pressed states a slightly darker version of the base color. Why: Hover and press are the most common element states, and color alone can show them. [For an active or press state, use a slightly darker version]
- **should** (components, all): Make disabled states by desaturating the color, unless it is already grayscale; a light gray fill with white text reads as disabled on its own. Why: The button is obviously disabled without other visual cues, and this is bulletproof for dark mode too. [for a disabled state, just desaturate the color]
- **should** (components, all): On mobile, where there is no hover, give tappable elements a press state, such as a slightly darker gray on press. Why: It makes it feel like you're actually pressing into something. [we don't have hover effects on mobile]

### Decisions it informs

- How should cards that are not the main focus be colored?
  - A different bright accent color per card: Cards burn the eye, compete for attention and mostly fail WCAG contrast. When: Not recommended.
  - Solid brand color: Roughly hits 60-30-10, but the bright brand color dominates the page for an unimportant element and causes accessibility issues. When: Not recommended for low-importance elements.
  - Lightened brand tint with black text: Draws less attention and keeps text readable. When: When the element should carry some brand color.
  - No background, just a simple border: Avoids adding another cluttering layer of color; keeps neutral balance. When: When cards only need to be separated.
  - Recommendation: Lighten the brand color and use black text, or drop the background and use a simple border; the source says adding another colored layer is a lot of clutter.
- How much of the screen should accent color cover? (`Q-color-05`)
  - Many competing accents: At least five accents on the cards all compete for attention, and most fail WCAG contrast. When: Not recommended.
  - Brand color on large secondary surfaces: Somewhat hits 60-30-10, but the bright brand color dominates the page for an element that isn't important. When: Not for low-importance elements.
  - 60-30-10 split: 60% dominant neutral, 30% secondary, 10% accent; it also works with bold colors, as Lemon Squeezy shows. When: As a rough check on the balance of a screen.
  - Recommendation: Use less color: one accent kept off unimportant elements, with 60-30-10 as a loose guide rather than a strict rule.
- Should icons be colored? (`Q-icon-05`)
  - Colored icons: Adds more competing color to the screen. When: Not recommended by default.
  - Uncolored icons, color only for status: Icons read as recognizable symbols, and color signals status such as the active tab. When: Default.
  - Recommendation: Mostly no color; reserve color for status like the active tab.
- What should backgrounds and foregrounds look like? (`Q-color-14`)
  - Bright color or gradient background: The background stops staying in the background (the sandy yellow gradient). When: Almost never; the source allows notable exceptions.
  - Neutral gray background, white or very light foreground: Backgrounds recede and content stands out, like white space does for hierarchy. When: General starting point in light mode.
  - Reversed background and foreground: Small features stand out with better accessibility. When: Light mode, for smaller UI features such as Dribbble's search bar.
  - Neutral gray with a hint of the brand hue: Adds a splash of color without overpowering the visuals (Headspace's orange tint on cards). When: When you want a little more brand color in the neutrals.
  - Recommendation: Start with a neutral gray background and a very light or white foreground; tinting the neutral toward the brand hue is an option.
- Should neutral grays be pure or tinted toward the brand color? (`Q-color-09`)
  - Pure neutral gray: Backgrounds stay fully neutral. When: The plain starting point.
  - Neutral gray with a hint of the brand hue: Brings a little brand color into backgrounds without overpowering visuals. When: To integrate more color, as Headspace does with its orange.
- The brand guidelines give too few colors. How do you get more colors for things like a storage bar? (`Q-color-04`)
  - Change the brand color's opacity: Works but feels a little bland. When: When a quiet variation is enough.
  - Analogous: rotate the brand hue slightly: Adds related colors (a blue and a pinkish color from purple) that sit well together. When: To add variety that stays close to the brand.
  - Complementary: cross the color wheel: Adds a contrasting color (bright yellow opposite purple) that still works with the brand. When: When you need a color that pops against the brand, or when the brand color fails contrast.
  - Recommendation: Rotate the hue or pick a complementary color rather than only changing opacity; brands like Mailchimp and Airbnb do this.
- The brand color fails WCAG contrast with white text. What do you do?
  - Darken the brand color: The darker version passes with white text. When: When the brand hue must stay.
  - Use a complementary color: A complementary blue also passes with white text. When: When a secondary color can carry that job.
  - Recommendation: Either works; don't be afraid to adapt brand colors to accommodate good design.
- What color should less important text, labels and borders be?
  - Pure black (or pure white in dark mode): Everything has the same weight, so hierarchy is weaker. When: Not bad in itself; best kept for the most important items.
  - Dark or light gray (or a very dark brand hue): Secondary information recedes and hierarchy becomes clear. When: File size and type, labels, borders; most text in the redesign is light gray or dark purple.
  - Recommendation: Use more gray and less black and white; the source says this separates mediocre from professional designers.
- How should dark mode be made from light mode? (`Q-color-16`)
  - Invert the light-mode colors: Not awful, but certainly not ideal: borders and cards lack separation and all text turns light purple. When: Not recommended.
  - Build the palette with dark-mode goals in mind: Brighter borders and cards, light gray text, pure white only on the most important text, a slightly desaturated logo. When: Recommended.
  - Recommendation: Build the palette for dark mode on purpose rather than inverting.
- Should a delete button use the brand color or red? (`Q-state-06`)
  - Brand color background: More on brand, but it draws attention to the button and doesn't show it is destructive. When: Not for destructive actions.
  - Red background: Clearly signals a destructive action. When: Delete and other destructive actions.
  - Recommendation: Use red; a brand-colored destructive action wouldn't fly from a usability point of view.
- What color should notification indicators be?
  - Red: The common convention for notifications. When: Default choice.
  - Brand color: Stays on brand. When: Acceptable, since notifications are much more flexible than destructive actions.
  - Recommendation: Either; the source says notifications could be swapped to the brand color.
- Which interactive states should be designed, and does it differ on mobile? (`Q-state-04`)
  - Hover, press and disabled: Hover is slightly lighter or brighter, press slightly darker, disabled desaturated. When: Pointer devices where hover exists.
  - Press only (plus disabled): A slightly darker gray on press makes it feel like pressing into something. When: Mobile, which has no hover effects.
  - Recommendation: Use lighter for hover, darker for press, desaturated for disabled; on mobile rely on press effects.

### Process

1. Cut competing colors: Replace multiple accent colors with the brand color, lighten it for unimportant elements with black text, strip color from icons except for status, and remove colors used only for the sake of color.
2. Set neutral balance: Make backgrounds a neutral gray with white or very light foregrounds (darker background, lighter foreground in dark mode), optionally tint the gray toward the brand hue, and use a simple border instead of another colored layer where possible.
3. Extend the brand palette: Where brand guidelines give too few colors, rotate the brand hue slightly for analogous colors or cross the wheel for a complementary one; darken or swap brand colors that fail WCAG with white text.
4. Build hierarchy with grays: Move secondary text, labels and borders from black to dark or light grays; keep pure black or white for the most important items.
5. Design dark mode separately: Starting from the light palette, brighten borders and main surfaces, use light grays for text, brighten only the most important text to pure white, lower gray brightness more aggressively, and desaturate the logo a touch.
6. Add semantic colors: Use red for destructive actions such as delete and keep red and green in the palette; notifications can use red or the brand color.
7. Define element states: Hover: slightly lighter or brighter. Press: slightly darker. Disabled: desaturated (light gray with white text). On mobile, add press states, since there is no hover.

### Examples and visual references

- File management app redesign, before and after (Kole Jain's demo design (Figma files linked in the description)): Starts with brightly colored cards in at least five accents, colored icons and a sandy yellow gradient background; ends with a neutral gray background, white foreground, brand-tinted or bordered cards, uncolored icons and gray secondary text, in both light and dark mode.
- 60-30-10 color split in a colorful section (Lemon Squeezy): Purple fills about 60%, yellow about 30%, and white acts as the accent, showing the rule also works with bold colors.
- Brand tint in card backgrounds (Headspace): A tint of the bright orange sits behind cards, adding a splash of color without overpowering the visuals.
- Reversed background and foreground for a small feature (Dribbble): Dribbble's search bar reverses the usual light-mode background and foreground, which the source says can help accessibility for smaller UI features.
- Storage bar colored with analogous and complementary hues (Kole Jain's demo design): Changing the purple's opacity feels bland; slightly rotated blue and pinkish hues plus a complementary bright yellow all work well on the UI.
- Orange brand color with white text failing contrast (Kole Jain's demo): Orange with white text fails WCAG; a darker orange passes, and so does a complementary blue.
- Complementary and paired brand colors (Mailchimp and Airbnb): Mailchimp's bright yellow primary with a turquoise secondary; Airbnb's very bright pink with a much deeper pink.
- Inverted light mode versus designed dark mode (Kole Jain's demo design): The straight inversion has weak borders and all-light-purple text; the designed version brightens borders and cards, uses light gray text, makes the logo and storage-used text pure white and desaturates the logo.
- Delete confirmation pop-up: purple versus red button (Kole Jain's demo design): The purple delete button is on brand but hides the destructive nature; the red one signals it clearly.
- Disabled and pressed button states (Kole Jain's demo design): A light gray button with white text reads as disabled in light and dark mode; on mobile a slightly darker gray on press gives a pressed-in feel.

### Numbers

- 60%: 60-30-10 rule: share of the dominant neutral color [60% of our dominant neutral color]
- 30%: 60-30-10 rule: share of the secondary color [30% secondary color]
- 10%: 60-30-10 rule: share of the accent color [10% accent color]
- at least five: Number of competing accent colors on the starting design's cards [at least five different accent colors on these cards]
- 7: Number of color mistakes promised in the video title [Title: The 7 Color Mistakes that RUIN your UI Designs]

<!-- /od:learn -->
