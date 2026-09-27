---
type: source
title: Designing with Claude Code
created: 2026-09-27
updated: 2026-09-27
video_id: lkKGQVHrXzE
url: https://www.youtube.com/watch?v=lkKGQVHrXzE
channel: Steve Schoger
published: 2026-03-20T19:09:23Z
authority: reference
tags:
  - claude-code
  - ai-design
  - landing-page
  - marketing-site
  - tailwind
  - inter
  - rings-vs-borders
  - screenshots
  - buttons
  - section-headings
  - canvas-grid
  - text-wrap
---

# Designing with Claude Code

## Metadata

- Video ID: `lkKGQVHrXzE`
- Channel: Steve Schoger
- Published: 2026-03-20T19:09:23Z
- URL: https://www.youtube.com/watch?v=lkKGQVHrXzE

## Summary

Steve Schoger designs a marketing home page for a finance app live in Claude Code, starting from a plain prompt and then refining it section by section with short, specific instructions. Most of the video is a stream of concrete polish moves: real app screenshots instead of generated fake UI, neutral grays that match the product, outer rings at low opacity instead of solid borders, the variable display cut of Inter with an in-between weight and tighter headline tracking, left-aligned and split layouts instead of centering everything, and smaller, pill-shaped buttons of equal height. He also shows reusable section treatments: inline section headings, monospace uppercase eyebrows, tinted 'well' containers with inset screenshots and concentric corners, image-backed testimonial cards, and a 'canvas grid' of decorative section borders. For a design system, the video gives exact starting values (for example gray 950 at 10% for rings, 38px hero buttons, 28px nav buttons, 8px insets and gaps, a 40ch heading width) and names the defaults AI tends to fall into, so a guide can steer away from them.

## Key Ideas

- Claude Code can serve as a primary design tool: give a plain first prompt listing the sections, then refine with short, specific instructions.
- AI-generated sites tend to default to an indigo accent, center everything and use the basic default version of Inter.
- A real screenshot of the product is an easy way to add a graphic to a home page when you have no other visuals.
- Solid-color borders next to a shadow look muddy; an outer ring of near-black at low opacity looks crisp and blends into the shadow.
- Match the site's grays and corner radius to what the product screenshot already uses.
- The variable version of Inter gives a display version with more impact, extra font features, and in-between weights such as 550.
- Large headlines read with more impact when their tracking is tightened a little.
- A split hero (headline on the left, supporting text and buttons on the right) fills space more interestingly than a centered or plain left-aligned headline.
- Keep buttons small and consistent: a ring on one button must not make it taller than its neighbour, and the nav button should not compete with the hero button.
- Set text widths in characters (ch) rather than a fixed max width, and put that width on the element that sets the font size.
- Inline section headings, where the title runs into a longer supporting sentence in a softer color, look more interesting than a separate title and subtitle.
- Monospace eyebrows look more designed; the author also sets them uppercase with wider tracking.
- Tinted 'well' containers with tightly inset screenshots, concentric corners and an inset ring on top of the image make product shots pop.
- A 'canvas grid' of decorative borders around each section adds visual interest when you have no custom graphics.
- For fiddly positioning, instead of describing it in words, have the AI build a temporary inline tool, set the values by hand, and bake them into the code.

## Entities

- [[entities/steve-schoger|Steve Schoger]] (person): Designer who presents the video and designs the page live.
- [[entities/adam-wathan|Adam Wathan]] (person): Helped the author get set up initially, devised the span-wrapped button technique that keeps ringed buttons the same height, and is building ui.sh with him.
- [[entities/claude-code|Claude Code]] (tool): The coding agent used as the primary design tool throughout, with no skills loaded.
- [[entities/tailwind-labs|Tailwind Labs]] (company): Company the finance dashboard was made for, to consolidate its revenue streams.
- [[entities/tailwind-play|Tailwind Play]] (tool): Where the span-wrapped equal-height button snippet is saved (linked in the description).
- [[entities/tailwind-plus|Tailwind Plus]] (product): Its homepage is the author's earlier example of a split hero headline.
- [[entities/inter|Inter]] (product): Typeface used for the page; the variable version with a display cut and font features is preferred over the basic default.
- [[entities/rasmus-rsms-me|Rasmus (rsms.me)]] (person): Owner of rsms.me, the website the variable Inter font is loaded from.
- [[entities/geist-mono|Geist Mono]] (product): Monospace font suggested for section eyebrows.
- [[entities/figma|Figma]] (tool): Still used by the author to make vector graphics such as the fake logos, exported as SVG.
- [[entities/quiver-ai|Quiver AI]] (tool): Recently released AI tool the author finds promising for vector graphics but has not tried yet.
- [[entities/chatgpt|ChatGPT]] (tool): Used to generate the portrait images for the testimonial cards.
- [[entities/ghostty|Ghostty]] (tool): Terminal app the author runs Claude Code in; the transcript says 'Ghosty', and the name Ghostty is [inferred].
- [[entities/apple|Apple]] (company): Where the author first saw the inline section-heading treatment.
- [[entities/linear|Linear]] (company): Named as using the inline section-heading treatment.
- [[entities/stripe|Stripe]] (company): Named as using inline headings and a canvas grid of section borders.
- [[entities/attio|Attio]] (company): Named as using inline headings and a canvas grid; the transcript says 'Adio', and the name Attio is [inferred].
- [[entities/ui-sh|ui.sh]] (product): Set of skills for coding agents the author is building with the Tailwind team; plugged at the end.
- [[entities/refactoring-ui|Refactoring UI]] (product): Design resource linked in the video description.
- [[entities/canvas-grid|canvas grid]] (concept): The author's name for decorative borders that contain each section and run between sections.
- [[entities/well-container|well container]] (concept): A softly tinted container (gray 950 at 5%) that holds an inset screenshot.
- [[entities/eyebrow|eyebrow]] (concept): Small label above a section heading, styled here as uppercase monospace.
- [[entities/text-wrap-pretty-and-balance|text-wrap pretty and balance]] (concept): CSS wrapping modes used to fix orphan words and awkward heading wraps.
- [[entities/ch-unit-max-width|ch unit max width]] (concept): Character-based max width that sizes a text block by how many characters fit.

## Topics

- [[topics/ai-assisted-design|AI-assisted design]]: Uses Claude Code as the main design tool: a plain first prompt, then many short, specific refinement prompts, inspecting how elements are built and asking for temporary tools; notes AI defaults (indigo, centering, basic Inter).
- [[topics/landing-pages|Landing pages]]: Builds and polishes a marketing home page: navbar, split hero with product screenshot, logo cloud, feature section, stats, image-backed testimonials, CTA and footer.
- [[topics/typography|Typography]]: Variable Inter with the display cut, a 550 weight between medium and semibold, tighter tracking on large headlines, 40ch heading widths, monospace uppercase eyebrows with wide tracking, text-wrap pretty or balance.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: Outer rings of gray 950 at 10% instead of solid borders beside shadows; inset rings on top of screenshots; a small shadow to lift secondary buttons; tinted wells instead of bordered containers.
- [[topics/shape-and-corner-radius|Shape and corner radius]]: Match the screenshot frame radius to the product, keep inset screenshots concentric with their container, drop the bottom radius on a cropped screenshot, and try pill buttons site-wide.
- [[topics/buttons-and-actions|Buttons and actions]]: Hero buttons at 14px text and 38px tall via padding, nav button 28px with text-sm, no icon, pill shape, secondary button with a small shadow and an outer ring, and a span wrapper so ringed and plain buttons are the same height.
- [[topics/spacing-and-layout|Spacing and layout]]: Split 3/5 and 2/5 hero, a wider 1280 page container, full-width screenshots and stats, 8px insets and gaps, 64px padding around the large hero screenshot, and a canvas grid of section borders.
- [[topics/color|Color]]: Swap slate grays for neutral to match the product, and replace the AI-picked emerald accent with gray 950 for a neutral look; use opacity-based near-black for rings and backgrounds.
- [[topics/visual-hierarchy|Visual hierarchy]]: Keep the nav button smaller so it does not compete with the hero button; set supporting text and stat labels in gray 600; drop unnecessary section titles, background tints and background cards.
- [[topics/cards-and-sections|Cards and sections]]: Feature cards as tinted wells with inset, cropped screenshots; testimonial cards with a portrait background, white quote at the bottom and a dark gradient; stats separated by dividers.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Tailwind utilities and CSS details: ring vs border, inline-flex p-px span wrapper, max width in ch on the font-size element, text-wrap pretty and balance, absolutely positioned inset rings over images.
- [[topics/figma-and-design-tools|Figma and design tools]]: Figma remains the author's tool for vector graphics such as logos, exported as SVG into the project.
- [[topics/design-process|Design process]]: Work top to bottom one section at a time, try values and 'Goldilocks' them, apply a finished treatment to all sections, and compare the before and after versions.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: Left-align nav links next to the logo instead of centering them, make the logo slightly bigger, give sign-in a secondary button treatment, and use a ring for the nav's bottom border.

## Notable Claims

- AI tends to pick an indigo accent color by default. Evidence: indigo, which I find AI kind of defaults to every time
- Sites generated with AI center everything by default. Evidence: defaults it centers everything by default
- Claude typically uses the basic default version of Inter when it generates sites. Evidence: the sort of basic default version of Inter
- Including a screenshot is a great way to add a graphical element to a home page that has no graphics. Evidence: including a screenshot is just a great way to bring a graphical element
- A solid-color border beside a shadow gives a muddy look, while an outer ring at low opacity gives a crisp edge that blends into the shadow. Evidence: you get that muddy-looking effect
- The variable version of Inter includes a text and a display version, and the display version has more impact; it also has font features such as a single-story a. Evidence: it's got a display version of the font
- A button with a ring around it ends up two pixels taller than a button without one. Evidence: technically two pixels taller
- The author thinks a character-based max width sizes the text block by how many zero characters of the current font size fit. Evidence: based on like the the zero character
- The inline section-heading style is used by Apple, Linear, Stripe and 'Adio' (most likely Attio [inferred]). Evidence: I think I first saw it on Apple
- The canvas grid of section borders is a popular treatment used by Stripe, 'Adio' (Attio [inferred]) and the Tailwind site. Evidence: I like to call it a canvas grid
- The author still opens Figma mainly to make vector graphics, because AI is still working on that. Evidence: one of the few reasons I still open up Figma
- Claude applied earlier style changes to later sections without being asked again. Evidence: it's just kind of learning as it goes here
- text-wrap pretty and text-wrap balance give different results, so sometimes both must be tried. Evidence: sometimes you have to play with like text pretty and text balance

## Quotes

> I try to avoid using solid colors cuz you get that muddy-looking effect
> including a screenshot is just a great way to bring a graphical element
> Sometimes you got to Goldilocks it.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Self-promotion: the video ends with a plug for ui.sh, a set of coding-agent skills the author is building with Adam Wathan and the Tailwind team; the description also links ui.sh and Refactoring UI.
- Caveat: Most rules are the author's personal taste stated as preference (he calls himself more of a left-aligned person; pill buttons and monospace eyebrows are his picks), not tested findings.
- Caveat: Values use Tailwind's scale and naming (gray 950, gray 600, text-xs, text-sm, 4XL, 5XL, max-w-3xl, p-px), so they assume Tailwind CSS.
- Caveat: Auto-caption errors (these readings are [inferred]): 'text excess' means text-xs, 'letting' means leading, '95010' means gray 950 at 10%, 'CH45' and 'C35' mean ch values, 'Adio' is most likely Attio, 'Ghosty' is Ghostty, and 'Razmatazzing' is Claude Code's status text.
- Caveat: The span-wrapper technique for equal button heights is only described in outline; the author says he does not fully understand it and the full code is in a Tailwind Play link, not in the transcript.
- Caveat: The feature-text leading instruction is garbled (text-sm is 14, 'double it', '20 pixels'), so the exact line-height value is uncertain.
- Caveat: The explanation that ch widths are based on the zero character is hedged by the author, who says he thinks that is how it works.
- Caveat: Dated to March 2026: Claude Code workflow, and Quiver AI described as recently released and untested by the author.

### Rules and practices

- **should** (patterns, web): Use a real screenshot of the product in the hero instead of a generated mock UI, especially when the page has no other graphics. Why: A screenshot brings a graphical element into the home page and makes it look more splashy and interesting when you have no visual graphics to work with. [including a screenshot is just a great way to bring a graphical element]
- **should** (patterns, web): Capture product screenshots at 3x so they stay sharp. Why: So the screenshot is high resolution. Values: 3x. [Capture it at 3x so it's high resolution]
- **should** (color, all): Match the site's gray family to the grays the product screenshot uses (switch slate to neutral when the app uses neutral grays). Why: The generated page used slate grays that did not match the neutral grays in the app screenshot. Values: neutral, slate. [update all the grays on the site to use neutral]
- **consider** (shape, all): Match the corner radius of a screenshot's frame to the radius used inside the screenshot. Why: The generated radius did not look right; tightening it made it match the corner radius in the screenshot. [tighten up the corner radius on this screenshot]
- **should** (elevation, all): Instead of a solid-color border on buttons, screenshots and the nav's bottom edge, use an outer ring of gray 950 at 10% opacity. Why: A solid border next to a shadow gives a muddy look; the low-opacity outer ring gives a crisp edge that bleeds into the shadow and looks cleaner. Values: gray 950, 10%. [I try to avoid using solid colors cuz you get that muddy-looking effect]
- **must** (components, css): Buttons placed side by side must be the same height: don't let a ring make one button taller. The author's fix wraps the ringed button in a span with inline-flex and p-px (saved in a Tailwind Play). Why: A ring on one button made it technically two pixels taller than the button beside it, which the author says 'we can't have'. Values: inline flex, p-px, two pixels. [this is technically two pixels taller than this button and we can't have that]
- **should** (components, css): When wrapping a button in a span, put the button's shadow on the button itself, not on the parent span. Why: Claude put the shadow on the parent span and the result was wrong until it was moved to the button. [Make sure the button shadow is on the button, not the parent span]
- **should** (typography, web): Load the variable version of Inter (from rsms.me) with its font feature settings, and use its display version. Why: AI-generated sites lean on the basic default Inter; the display version has more impact and the variable version has all the fancy font features, such as a single-story a. [make sure you're using the variable version of Inter]
- **consider** (typography, all): With a variable font, pick an in-between weight when medium feels too thin and semibold too bold, for example 550. Why: Inter's variable version allows all the in-between weights, so you can land between 500 and 600. Values: 550, 500, 600. [I'm going to say 550. Just somewhere in between medium and semi-bold]
- **should** (typography, all): Tighten the letter tracking on headlines once font sizes go above about 24 to 30 pixels. Why: Tighter tracking gives large headlines more impact. Values: 24 to 30 pixels. [24 to 30 pixels, I like to make the tracking just a bit tighter]
- **should** (layout, web): Don't center everything by default; left-align content or use a split hero with the headline on the left and the supporting text and buttons on the right, in roughly a 3/5 and 2/5 split, with the top of the supporting text lined up with the top of the headline. Why: AI centers everything by default; the split gives more weight to the headline, is more interesting than a centered or left-aligned headline, and fills the space nicely. Values: 3/5 and 2/5. [make it like a 3/5 and 2/5 split]
- **consider** (typography, web): In a split hero, make the supporting text small enough (16 pixels here) that its block is almost the same height as the headline. Why: The author wanted the headline and the supporting column to be almost the same height. Values: 16 pixels. [make the supporting text 16 pixels]
- **consider** (typography, web): Put each sentence of a multi-sentence headline on its own line. Why: Letting it wrap mid-sentence looked awkward. [put each sentence in the headline on its own]
- **consider** (layout, web): Widen the page container when the layout feels cramped, for example to 1280. Why: The author wanted the page a bit wider; no further reason is given. Values: 1280. [make the page container wider. Maybe 1280]
- **consider** (layout, web): Make the hero screenshot the full width of the page container instead of letting the layout zigzag. Why: The author disliked the 'zigzaggy thing' the narrower layout was doing. [make the screenshot full width in the page container]
- **should** (components, web): Keep hero buttons small: about 14 pixel text and a 38 pixel height reached with padding, not a fixed height. Why: The generated buttons looked clunky; the author likes buttons in the 36 to 38 pixel range. Values: 14 pixel, 36 38 pixel range, 38 pixels. [Make the button height 38 pixels]
- **consider** (components, all): Remove decorative icons from secondary hero buttons such as 'watch demo'. Why: The author wanted the buttons looking clean. [Get rid of the icon in the watch demo button]
- **consider** (components, all): Lift the secondary button slightly with a small shadow (plus the outer ring instead of a border). Why: It gives the secondary button a bit more elevation and, with the ring, a crisp edge. [button a bit more elevated to give it a small shadow]
- **consider** (shape, all): Try pill-shaped buttons, and apply the shape to every button on the site. Why: After shrinking the hero buttons the author felt their horizontal padding was a bit much, switched to pill buttons to see what happened, and found it looked pretty good. [make the buttons pill shaped]
- **should** (components, web): Make the navbar button smaller than the hero button (28 pixels tall, text-sm) and give the sign-in link a secondary button treatment. Why: So the nav button is not competing with the hero button; 24 pixels was too small. Values: 28 pixels, 24 pixels. [so it's not competing with that button]
- **consider** (layout, web): Left-align navbar links close to the logo instead of centering them. Why: Three separately placed elements made the nav feel busy. [left align the links in the navbar to be closer to the logo]
- **consider** (patterns, web): In a logo cloud, use real SVG logos in solid gray 950 with no opacity, spread full width in the container, without a section title, background tint or top and bottom borders. Why: The title is not necessary; the logos alone make it clear these are likely users of the app. Values: gray 950. [I don't think the title of that was necessary]
- **consider** (typography, web): For section headings, run the title inline into the supporting text at the same size so it reads as one block, with the supporting text in a softer color (gray 600) and medium weight. Why: It looks more interesting than a stacked title and subtitle and is a current style the author has seen on Apple, Linear, Stripe and 'Adio' (Attio [inferred]). Values: gray 600, 4XL. [Make the title inline with the supporting text so it reads like one block]
- **should** (content, all): When using the inline heading style, write a longer supporting sentence. Why: This style of title requires a longer sentence to work. [requires a bit of a longer sentence]
- **should** (typography, css): Set the width of heading and text blocks with a character-based max width (40ch here) instead of a fixed max width. Why: It is more flexible for typography: you get a nice reading width based on how many characters fit, not a set width. Values: 40, 45, 35. [max width character thing]
- **must** (typography, css): Put the ch-based max width on the same element that sets the font size. Why: When Claude put the 40-character max width on a different element, the text came out too tight. Values: 40 characters. [on the same line where the font size is set]
- **consider** (typography, all): Style section eyebrows as monospace (for example Geist Mono), uppercase, text-xs, gray 600, with wider tracking. Why: A monospace eyebrow looks a bit more designed and interesting. Values: Geist Mono, gray 600. [I like using uh a monospace for these eyebrows]
- **should** (typography, all): Widen letter tracking whenever text is set in all uppercase. Why: It gives the uppercase text more room to breathe. [I like to make the tracking a bit wider when I make everything all uppercase]
- **should** (patterns, web): In feature sections, capture the full product screenshot and crop it inside the card to the feature being described, with the relevant state (such as a chart tooltip) showing. Why: It focuses the reader on the specific part of the app the feature text talks about. [crop it in the space so I can focus on a specific part]
- **should** (shape, all): Inset screenshots tightly inside their container (about eight pixels) and make the screenshot's corner radius concentric with the container's radius. Why: The inner radius then hugs the outer radius and looks more correct. Values: eight pixels. [is concentric with the container radius]
- **should** (elevation, all): Put the screenshot's outline ring on top of the image as an inset ring (gray 950 at 10% on a tinted container). Why: An inset ring over the image's edge gives a crisp border; at a lower opacity it matched the tinted background and disappeared. Values: 950, 10%. [I want it to be inset so it's on top of the image]
- **consider** (elevation, web): Use a softly tinted 'well' container (gray 950 background at 5% opacity, no border) behind product screenshots instead of a plain white bordered card. Why: The well helps the image pop more; 2.5% was too soft. Values: gray 950, 2 and 1/2%, five. [give the containers a background color]
- **consider** (layout, web): Make the gap between feature cards match the inset around the screenshots (eight pixels). Why: The author wanted it snug, the same as the space around the image. Values: eight pixels. [gap between the two features uh eight pixels]
- **consider** (typography, web): Set feature-card text (both title and description) at text-sm (14) with a taller line height; the author asked for 20 pixels. Why: The feature text looked a little chunky. Values: 14, 20 pixels. [Make the feature text um text small, maybe]
- **consider** (layout, web): Give a large hero screenshot more liberal padding inside its well (64 pixels), let it sit on the bottom edge with zero bottom padding, crop about 10 pixels off its bottom, remove its bottom corner radius, and add an inset ring at 5% opacity on the container on top of the screenshot. Why: A much bigger element needs more liberal spacing than the tight feature cards, and the inset ring gives definition between the container edge and the cropped screenshot. Values: 64 pixel, 10 pixels, 5%. [64 pixel padding]
- **consider** (patterns, web): Keep sections plain: remove background tints and cards the AI adds, such as the off-white logo-cloud and footer backgrounds, the dark stats background and the CTA background card. Why: The author was not crazy about the dark stats background and wanted the page pretty simple. [get rid of the dark background on the stats section]
- **consider** (patterns, web): Keep a stats section simple: no dark background, left-aligned stats spanning the page container, values in regular weight at a large size (5XL), labels in gray 600, and a divider between stats. Why: The author wanted the section pretty simple, and the generated stat numbers looked clunky. Values: 5XL, gray 600. [Make the values in the stats]
- **should** (typography, css): Apply text-wrap pretty to headings to remove orphan words, and switch to text-wrap balance when pretty still wraps awkwardly. Why: Pretty fixed the orphan in the stats heading, but balance gave better wrapping in the CTA heading. [sometimes you have to play with like text pretty and text balance]
- **consider** (patterns, web): For testimonial cards, use a portrait image as the card background, set the quote in white aligned to the bottom, add a dark gradient from the bottom, drop the star ratings and circular avatar, and set the name and title smaller (text-xs) with a bigger line height. Why: It makes the section more visual, and the gradient makes the text stand out more. [so the text stands out a bit more]
- **consider** (patterns, web): Declutter the footer: remove its off-white background and the text below the logo, use only the logo mark, set links at text-xs, and make social icons smaller and gray 950. Why: It was looking busy and the social icons looked clunky. Values: gray 950. [get rid of the text below the logo]
- **consider** (layout, web): Consider a 'canvas grid': decorative borders the width of the page container around each section, with dividers between sections running the full viewport width and borders hugging contained elements with an eight pixel gap. Why: Like a screenshot, it makes a site more interesting and visual when you have no custom graphics. Values: eight pixel. [I like to call it a canvas grid]

### Decisions it informs

- What graphic should the hero use?
  - Generated mock UI: A fake interface guessed from the description of the app. When: Not recommended by the source.
  - Real product screenshot: Brings a graphical element in and makes the page look more splashy and interesting. When: Whenever you have no other graphics to work with.
  - Recommendation: Use a real screenshot captured at 3x.
- Which gray family should the site use? (`Q-color-09`)
  - Slate: What the AI picked; it did not match the app screenshot. When: When the product itself uses slate grays [inferred]
  - Neutral: Matches the neutral grays used in the product screenshot. When: When the product itself uses neutral grays.
  - Recommendation: Use the gray family the product already uses; here neutral.
- Should the page use a colored accent or stay neutral? (`Q-color-03`)
  - Emerald accent: Colorful; the author liked that it avoided the usual AI indigo. When: When you want color in the accent.
  - Indigo accent: What AI defaults to every time. When: The author was glad the AI avoided it.
  - Gray 950 (near-black): A neutral-looking page. When: When you want to keep the page neutral.
  - Recommendation: The author swapped every use of emerald for gray 950 to keep it neutral.
- How should the edges of buttons, screenshots and the nav be drawn? (`Q-depth-01`)
  - Solid-color border: Muddy where the border meets the shadow. When: Not recommended by the source.
  - Outer ring, gray 950 at 10%: A crisp edge that bleeds nicely into the shadow and looks cleaner. When: On buttons, screenshots and the nav's bottom border.
  - Recommendation: Use the low-opacity outer ring instead of a solid border.
- Should borders, rings and tinted backgrounds use solid grays or a near-black at low opacity? (`Q-color-26`)
  - Solid gray: A muddy-looking effect where the border meets the shadow. When: Not recommended by the source.
  - Gray 950 at low opacity: Crisp edges that blend into the shadow: 10% for rings on buttons, screenshots and the nav, 5% for well backgrounds and the hero's inset ring. When: Rings, borders and soft container tints.
  - Recommendation: Use gray 950 with reduced opacity instead of solid colors.
- Which version of the font should the site load? (`Q-type-05`)
  - Basic default Inter: What Claude leans into; no display cut and fewer font features. When: Not recommended by the source.
  - Variable Inter with the display cut: Feels more 'displayy', with more impact, and fancy font features such as a single-story a become available. When: When the design uses Inter.
  - Recommendation: Load variable Inter from rsms.me with its font features and the display version.
- Which headline weight: medium, semibold, or in between? (`Q-type-07`)
  - Medium (500): Can feel a little too thin. When: Not stated.
  - Semibold (600): Can feel a little too bold. When: Not stated.
  - In-between (550): Sits between the two. When: When the font is variable and neither standard weight feels right.
  - Recommendation: 550, using the variable font's in-between weights.
- Should letter spacing change with text size and case? (`Q-type-13`)
  - Default tracking: Large headlines have less impact. When: Text below about 24 to 30 pixels [inferred]
  - Tighter tracking on large headlines: Gives the headline a little more impact. When: Font sizes over about 24 to 30 pixels.
  - Wider tracking on uppercase text: Gives the letters a little more room to breathe. When: All-uppercase labels such as monospace eyebrows.
  - Recommendation: Tighten tracking on large headlines and widen it on uppercase eyebrows.
- How should the hero headline be laid out? (`Q-dir-05`)
  - Centered: What AI defaults to. When: Not recommended by the source.
  - Left-aligned: The author's general preference. When: Default choice for the author.
  - Split headline (3/5 and 2/5): Headline on the left with more weight, supporting text and buttons on the right; more interesting and fills the space nicely. When: Hero sections with a headline and supporting text.
  - Recommendation: The split layout, with the supporting text's top lined up with the headline's top.
- How tall should buttons be? (`Q-space-04`)
  - 38 pixels (hero): Less clunky than the generated buttons; within the 36 to 38 pixel range the author likes. When: Main hero buttons, with 14 pixel text.
  - 28 pixels (navbar): Smaller, so it does not compete with the hero button. When: Buttons in the navbar, with text-sm.
  - 24 pixels: Too small for the nav button. When: Not recommended here.
  - Recommendation: 38 pixels in the hero and 28 pixels in the nav, reached with padding rather than a fixed height.
- What shape should buttons be? (`Q-shape-01`)
  - The generated shape: Its horizontal padding felt a bit much to the author. When: Not stated.
  - Pill, all through the site: The author's pick; it looked pretty good. When: Every button on the site.
  - Recommendation: Pill-shaped buttons everywhere.
- How should section headings be styled?
  - Separate title and supporting text (generated default): Title and supporting text at different sizes, not running together [inferred] When: Not stated.
  - Inline title leading into the supporting copy: Title and a longer supporting sentence at the same size read as one block, with the supporting text in a different color; looks more interesting. When: When you can write a longer supporting sentence.
  - Recommendation: The inline style, which the author has seen on Apple, Linear, Stripe and 'Adio' (Attio [inferred]), applied to every section heading.
- How should the width of a text block be limited? (`Q-type-14`)
  - Fixed max width (max-w-3xl): A set width regardless of the text. When: Not recommended by the source.
  - Character-based max width (ch): Width follows how many characters fit, giving a nice reading width; more flexible for typography. When: Headings and text blocks; try values such as 45, 35 and 40 and pick one.
  - Recommendation: Use a character-based width (40ch here), set on the element that sets the font size.
- How should headings avoid bad line breaks?
  - text-wrap: pretty: Removes orphaned words. When: First try, as in the stats heading.
  - text-wrap: balance: Evens out line lengths; avoided the funky wrapping around the '14-day free trial' text. When: When pretty still wraps awkwardly, as in the CTA heading.
  - Recommendation: Try both and keep the one that wraps better.
- How should a feature card hold its screenshot? (`Q-depth-01`)
  - Plain white container with a border: The generated default; the image does not pop. When: Not recommended by the source.
  - Tinted well (gray 950 at 5%, no border): A soft, well-styled container that helps the image pop. When: Feature cards and the hero screenshot.
  - Recommendation: The tinted well, with the screenshot inset about eight pixels and an inset ring on top.
- How should testimonial cards look? (`Q-img-02`)
  - Card with stars and a circular avatar: The generated default. When: Not recommended by the source.
  - Portrait image as the card background: More visual; a white quote sits at the bottom over a dark gradient that makes the text stand out. When: When you can supply images.
  - Recommendation: Use the image background with a dark gradient behind the quote.
- Should the site add decorative section borders (a canvas grid)?
  - No decorative borders: Plain sections with no containing lines. When: Not stated.
  - Canvas grid: Borders contain each section and dividers run between them, making the site more interesting and visual as you scroll. When: When you don't have custom graphics to work with.
  - Recommendation: The author added it, with horizontal dividers running the full viewport width.

### Process

1. Start plain: Open a copied project template, start the dev server and Claude Code with no skills, and give one plain prompt describing the product and listing the sections: navbar, hero, logo cloud, two-feature section, stats, testimonials, CTA and footer.
2. Swap in real assets: Replace generated visuals with real ones: screenshots of the app captured at 3x, logos drawn in Figma and exported as SVG into the project's public/logos folder, and generated portrait images placed in the public folder.
3. Inspect before changing: Check how an element is built (border or ring, max width, grid columns) before giving the fix, so the instruction targets the real cause.
4. Give short, specific instructions: Name the exact change and a starting value (pixel sizes, Tailwind colors and opacities, font weights); loosely written sentences are fine.
5. Work top to bottom: Refine one section at a time from navbar to footer, fixing spacing between sections last.
6. Goldilocks the values: Try a value, look, and adjust (for example 45ch, then 40, then 35, then back to 40).
7. Build temporary tools: When positioning is fiddly, have Claude build a temporary inline tool on the page you are working on, set the positions by hand, copy the values, and have it bake them into the code and remove the tool.
8. Spread finished treatments: Once a treatment works in one section (such as the heading style), tell Claude to apply it to all sections below.
9. Compare before and after: Have Claude recreate the original version on a separate page to compare it with the result.

### Examples and visual references

- Three-tier pricing page with a comparison table, a testimonial and an FAQ section (Made by the author for practice): An earlier page designed entirely in Claude Code.
- Finance dashboard consolidating revenue streams (Tailwind Labs internal app): Filled with fake, colorful content; its screenshots become the hero and feature images of the marketing page.
- Marketing home page for the finance app (renamed from Ledger to Axiom) (Built in the video): Neutral gray page with a split hero, full-width screenshot in a tinted well, logo cloud, inline section headings, image-backed testimonials and a canvas grid of section borders.
- Split hero headline with the subheading on the right, not quite 50/50 (Tailwind Plus homepage): Shows a hero that gives more weight to the headline while filling the space beside it.
- Inline section heading where the title leads into the supporting copy in a different color (Apple, Linear, Stripe, 'Adio' (Attio [inferred])): Title and supporting sentence at the same size read as one block.
- Canvas grid of borders around every section (Stripe, 'Adio' (Attio [inferred]), the Tailwind site): Visible lines that contain each section and divide sections across the page.
- Span-wrapped button that keeps ringed and plain buttons the same height (Tailwind Play link in the video description): A span with inline-flex and p-px wraps the bordered button so it is not two pixels taller.
- Feature cards with cropped, zoomed screenshots showing chart tooltips (Unified revenue tracking and smart forecasting features): Screenshots zoomed in about 25%, inset eight pixels in tinted wells with concentric corners and an inset ring.
- Testimonial cards with portrait backgrounds (Built in the video with ChatGPT-generated images): White quote at the bottom of each portrait over a dark gradient rising from the bottom.

### Numbers

- 3x: Screenshot capture scale for high resolution [Capture it at 3x so it's high resolution]
- 10%: Opacity of the gray 950 outer ring used instead of solid borders [gray 950 um at 10%]
- 550: Headline font weight between medium (500) and semibold (600) [I'm going to say 550]
- 24 to 30 pixels: Font size above which the author tightens headline tracking [24 to 30 pixels, I like to make the tracking just a bit tighter]
- 3/5 and 2/5: Split of headline and supporting text in the hero [make it like a 3/5 and 2/5 split]
- 16 pixels: Hero supporting text size [make the supporting text 16 pixels]
- 1280: Wider page container width [make the page container wider. Maybe 1280]
- 14 pixel: Hero button font size [14 pixel font size]
- 38 pixels: Hero button height (the author likes 36 to 38) [Make the button height 38 pixels]
- 28 pixels: Navbar button height; 24 pixels was too small [28 pixels tall]
- two pixels: Extra height a ring adds to one button compared with its neighbour [technically two pixels taller]
- 40: Character-based max width (ch) chosen for section headings after trying 45 and 35 [I like 40 better]
- eight pixels: Inset of screenshots in their containers and gap between feature cards [like eight pixels maybe as a starting point]
- 25%: Zoom applied to the cropped feature screenshots [Maybe 25% as a starting point]
- five: Opacity of the gray 950 well background; 2 and 1/2% was too soft [make it opacity five]
- 64 pixel: Padding around the large hero screenshot inside its well [64 pixel padding]
- 10 pixels: Amount cropped off the bottom of the hero screenshot [10 pixels just to get rid of that like gray]
- 5XL: Size of stat values, set in regular weight [Make the values in the stats]
- 4XL: Size of the inline section headings [Make it bigger like 4XL]
- 2 and 1/2%: First try for the gray 950 well background opacity; too soft [like like 2 and 1/2%]
- 5%: Opacity of the inset ring on the hero well container, on top of the screenshot [5% opacity]
- 20 pixels: Line height asked for on the text-sm (14) feature text; the instruction is partly garbled [just that big 20 pixels]

<!-- /od:learn -->
