---
type: synthesis
title: Color
created: 2026-09-24
updated: 2026-09-24
sources:
  - 66oOi9OLMCw
  - 6CC8lLnqa28
  - AH_ugxmLeUM
  - EOcY3hPMQkk
  - EcbgbKtOELY
  - Ksx9C2-3yMo
  - Lp6ey4AyDzA
  - MZSm6MA8bww
  - NtZeYmTMuo4
  - PDcQJOPby1k
  - RCneB_MQ7qs
  - V3Omp1hm0Sg
  - c1TvOcKdBVE
  - eMMiLeo_UGI
  - eeN7yUcIWbw
  - gKM6b2EnW1k
  - jSxxAFxjxbU
  - lkKGQVHrXzE
  - neE6wOuBIP8
  - pGYLZyBE32o
  - ulSOdTgoGeY
  - xHD01_Onac0
tags:
  - od-area-color
---

# Color

## In short

Most of a good interface is gray: backgrounds, borders and most text are neutral colors, and real color is saved for the few things that need attention or carry meaning, such as the main button, a status or a chart. The sources agree that one accent color is usually enough, that pure black and pure white can often be swapped for slightly tinted grays, and that delete buttons stay red even when the brand color is something else. It helps to treat the accent as a ladder of lighter and darker shades (a ramp) instead of a single color, so hover, links and dark mode can each use their own step. Every color pair still has to pass the contrast check that OpenDesigner locks (WCAG 2.2 AA). All the sources on this page are practitioner videos, so their exact numbers are starting points, not rules.

## House standards

The sources tagged Color are all reference videos, so no house standard comes from them directly. These standards from the non-negotiable sources apply to any color work:

- `STD-visual-details-24` (should): give every color role a light value and a dark value.
- `STD-visual-details-21` (should): put color on a solid layer, not on a translucent foreground surface.
- `STD-visual-details-13` (should): over blurred or translucent surfaces, avoid flat gray text; use higher-contrast text, a slightly heavier weight and a little more letter spacing.
- `STD-visual-details-25` (must): when prototyping with no project tokens, use a restrained look: neutral grays, one accent color and the system font stack.
- `STD-visual-details-26` (must): build from the project's existing color tokens and extend them; never add a parallel set or hand-type an approximate value.
- `STD-visual-details-14` (should): separate surfaces with a semi-transparent shadow rather than a solid, opaque border.
- `STD-visual-details-09` (must): underline only links; emphasise other text with weight or color, never an underline.
- `STD-visual-details-29` (should): use order, spacing and contrast so the most important thing on a screen is the most obvious.
- `STD-easing-duration-01` (must): a hover or color change animates with `ease`.
- `STD-enter-exit-origin-42` (should): when the active tab changes background or text color, clip a styled duplicate of the tab list instead of timing text-color transitions.
- `STD-components-toasts-drawers-23` (should): start toast colors from Sonner's defaults and add `richColors` when success and error must read green and red.
- `STD-accessibility-motion-12` (must): under `prefers-contrast: more`, surfaces get near-solid backgrounds with a defined, contrasting border.
- `STD-process-review-taste-37` (must): prototype variants that differ only in accent color are not real variants; replace or cut them.

Also locked, as an OpenDesigner accessibility floor rather than an STD: text 4.5:1, large text 3:1, UI parts and focus indicators 3:1, measured with WCAG 2 math and no rounding up, and never meaning by color alone (`skills/opendesigner/references/guardrails.md`, section 4).

## What the sources teach

### Color needs a job, and most of the screen stays neutral

- Product color works in four layers: a neutral foundation (backgrounds, strokes, text), one functional accent, semantic colors for meaning, and theming. The 60-30-10 split (60% dominant neutral, 30% secondary, 10% accent, as defined in [S-L19-051]) suits beginners and websites but not most product screens; Vercel is roughly 90% black, 8% white and 2% red [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- The same creator's earlier color video still uses 60-30-10 as a rough balance check and shows it working with bold colors (Lemon Squeezy), while admitting the redesign only "somewhat" hits it [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- Keep one accent and remove colors used only for the sake of color; five accent colors on one screen all compete for attention [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]). Color should have a purpose, such as an announcement bar, an input's focus state or a green "new" chip, and not be decoration [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- Emphasis is the difference between an element and its neighbours, so show default values in gray and give color only to what changed or needs attention: a checkbox earns color only when it is on, and a menu's only blue item is the one asking you to resubscribe [S-L19-080] ([[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]).
- On dashboards, color should come from the data, such as a red icon in a chip for an urgent action [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]), or from charts that carry information rather than from colored buttons and icons [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]). On landing pages, color pops can come from the product visuals, which lets the buttons stay white; a weak page spreads its accent over everything that will take it [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).
- Brand color on navigation fits best on active states [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]). One site redesign shows its bright orange accent only when the call to action is hovered, so it never overpowers the page [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).
- A neutral page is a valid choice: Steve Schoger replaced every use of an AI-picked emerald accent with gray 950 to keep a marketing page neutral, and says AI tends to default to indigo [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).

### Neutrals: backgrounds, borders and text

- Real products sit between 98% and 100% white (Linear 99%, Notion 100%, Vercel 98%), so pure white is acceptable, but if cards are pure white the page behind them should not be. The app frame or sidebar can be a slightly darker anchor with a very small shift, such as the 2% blue Mercury adds [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- A product needs more neutrals than a landing page: about four background layers, one or two strokes and about three text colors before any hover state, against 3 to 5 neutrals for a landing page [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- Other videos push further away from pure white and black: off-whites in light mode and bluish blacks in dark mode mark a more experienced designer [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]); a very light or very dark version of the accent as the background brings color in, as GitHub's very dark blue does [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]); off-whites, or an image background with noise, add color and cohesion [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]).
- Start from a neutral gray background with a white or very light foreground, and consider a hint of the brand hue in the grays or a light brand tint on cards (Headspace does this with its orange) [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]). That video introduces the tint right after its dark-mode point, so it is unclear whether it meant both modes.
- Match the gray family to the product: an AI-generated page used slate grays that clashed with the neutral grays in the app screenshot, so every gray on the page was switched to neutral [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- Use grays instead of pure black for less important text, labels and borders, and consider a very dark brand hue for text [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]). One video gives targets: headings about 11% white, body 15 to 20%, subtext 30 to 40% [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]). These are one creator's numbers, and the video never says which color model "% white" means.
- Use at most two text colors: the primary and the same color at 45 to 70% opacity [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]). One video's opinion; black at 45% on white works out to about 3.4:1, below the locked 4.5:1 for body text [inferred].
- For card edges on a light background, use a light gray border (about 85% white) instead of a thin black border or a shadow alone [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]). A very subtle outline on nearly every element lets a palette stay mostly pure white or near white, and the pop-up shadow uses a very light gray instead of transparent black [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]). Schoger swaps solid borders for an outer ring of gray 950 at 10% opacity, which looks crisper next to a shadow, and puts screenshots in a soft "well" of gray 950 at 5% [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- Background differences have to be visible: if two surfaces are meant to differ, give them enough contrast to see it [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).

### The accent is a ramp, not one color

- Build the accent as a ramp from lightest to darkest and give each job a step: main color at 500 or 600, hover at 700, links at 400 or 500. The ramp also makes dark mode easier [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]). A simpler start is one primary color, lightened for backgrounds and darkened for text, which is already halfway to a ramp for chips, states and charts [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- To find matching colors from a base color, work in HSB: add about 20 saturation and remove about 10 brightness per step, optionally sliding the hue about 20 points toward blue for darker steps, because blues and purples read darkest [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]). One video's recipe.
- A Tailwind shortcut: its 50 as a light background with 500 as the accent, or 950 as a dark background with 300 as the primary. The presenter says this works for every Tailwind color and mentions no contrast check [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]).
- When the brand palette is too small, rotate the brand hue slightly (analogous) or cross the color wheel (complementary) instead of only changing opacity; Mailchimp pairs yellow with turquoise, and Airbnb a bright pink with a deeper pink [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- Adapt brand colors when design needs it: if the brand color fails WCAG with white text, darken it until it passes or use a complementary color that passes [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]). If brand colors look off on headline text, bring the brand in through the logo instead [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).

### Meaning: semantic and state colors

- Semantic colors override the brand. Always include status colors (success, failed, in progress), and making a destructive action anything other than red is "pretty much a design sin", even with a purple brand [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]). Delete uses red, not the brand color, which is why red and green are often in a brand's palette even when they are not brand colors; notifications are more flexible and may use the brand color [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]). In a delete dialog, delete takes the primary fill, preferably red [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]). Three videos agree here, the third more softly.
- The usual meanings are blue for trust, red for danger or urgency, yellow for warning and green for success, presented as conventions [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- Status colors must match the state: if one color means completed, only completed work gets it [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).
- States can come from one base color: hover slightly lighter or brighter, pressed slightly darker, disabled desaturated. A light gray fill with white text reads as disabled in light and dark mode, and mobile, which has no hover, relies on a slightly darker press [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- Icons mostly need no color; save icon color for status, such as the active tab [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]). Other videos color icons on purpose: feature icons drawn in the brand's accent colors on a marketing site [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]), small icons that add information and a splash of color to dense rows [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]), and solid brand-blue feature icons instead of gradient icons [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).

### Charts

- A gray-only chart looks dull and a single brand ramp makes series too similar, so use a full spectrum at the same perceived brightness: in OKLCH, fix lightness and chroma and step the hue by about 25 to 30 for each series, because otherwise bright green looks more neon than bright blue [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]). One video's method.
- For business metrics, draw the previous period as a gray line behind the current one [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).

### Muted colors beat loud ones

- Beginners tend to stay with white, gray and one super-saturated color; explore online color pickers (keep the one or two colors that catch your eye) and look at nature and artwork [S-L19-040] ([[sources/6CC8lLnqa28-6-things-you-probably-need-to-hear-as-a-web-designer|6 Things You Probably Need to Hear (as a web designer)]]). Muted colors such as baby blue, beige and lavender are "your friend" [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- Never let an AI tool pick the palette, because it goes for bright colors that don't work together [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]). Color is one of the three biggest fixes to an AI-generated screen: purples made bluer, backgrounds darker, chip contrast fixed [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]). The "never" is one video's opinion.
- A palette can come from a mood: one redesign starts from a single moody image instead of a bright, sterile light mode or a flat, typical dark mode, and pulls earthy base tones from the images plus a few accents [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]). Another app palette borrows from Wise's palette with purple worked in [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]). One site redesign avoids a dark theme for the whole page as a stated personal dislike [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]). For more on dark themes, see [[synthesis/dark-mode-and-themes|Dark mode and themes synthesis]].

### Gradients and texture

- Avoid gradients that blend two hues, like blue to green; if one is needed, use lighter and darker shades of one color, and no gradient is usually cleaner [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]). Review gradients honestly and remove them if they aren't working [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- Where gradients are part of the brand: mesh gradients with noise and fully rounded corners for an AI product, a gradient stroke on the purchase card and on hover, and noise used sparingly so the site doesn't look like TV static [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]). A section background can be a gradient sampled from the image above it when black looks too close to the product [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).
- Decorative recipes: muted colors for a clay effect, a clear color change in the middle of the gradient for metal, a 20% colored fill to tint metal to rose gold, gold, bronze or titanium, and 8 to 10 or more overlapping blurred layers for a vivid mesh gradient [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]). A dedicated tool such as Photo Gradient makes mesh gradients Figma cannot [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]).
- Subtle noise on an image or color background adds texture and helps text contrast, and darkened hero edges pull the eye to the center [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]).

## Where they agree and disagree

Between the sources:

- **Agree:** one accent on a mostly neutral screen, with color that has a purpose [S-L19-039] [S-L19-051] [S-L19-052] [S-L19-056] [S-L19-061] [S-L19-072] [S-L19-080]; red for destructive actions [S-L19-039] [S-L19-051] [S-L19-057]; grays or tinted darks instead of pure black text [S-L19-039] [S-L19-051] ([S-L19-057] keeps black or white as the primary text color and grays the second level by opacity).
- **Pure white backgrounds:** acceptable if cards aren't also pure white [S-L19-039], against off-whites or accent-tinted backgrounds as the better choice [S-L19-057] [S-L19-070] [S-L19-085].
- **Hover direction:** slightly lighter or brighter, with press darker [S-L19-051], against a darker step (700 from a 500 or 600 main) [S-L19-039].
- **How many text colors:** two, the second made with opacity [S-L19-057], against about three solid levels [S-L19-039].
- **60-30-10:** rejected for product UI [S-L19-039], kept as a loose check [S-L19-051].
- **Colored icons:** only for status [S-L19-051], against colored feature icons and row icons [S-L19-061] [S-L19-062] [S-L19-082]. The split lines up with app chrome versus marketing sections and data-dense rows [inferred].
- **How to build matching colors:** HSB steps [S-L19-070], against OKLCH for equal perceived brightness [S-L19-039].

Against OpenDesigner's existing research:

- **Accent restraint agrees** with DC-L01-08 (one accent plus neutrals and status by default; add an accent only when it has a job), DC-L01-10 (keep large areas low in chroma and spend chroma on small, high-meaning elements) and DC-L15-03 (a strict emphasis budget with 60-30-10 only as a soft check). DC-L15-06 calls 60-30-10 folk wisdom, which sides with [S-L19-039].
- **Tinted neutrals agree** with DC-L01-06, whose default is a slight tint toward the accent hue (OKLCH chroma about 0.01 to 0.03 at mid steps) and pure gray for image- or data-critical tools. Schoger's switch to pure neutral to match the product screenshot [S-L19-103] fits that exception [inferred].
- **Ramp building differs:** DC-L01-01 and Q-color-07 default to OKLCH and advise against HSL-based lightness steps. The HSB recipe [S-L19-070] is a quick way to find a few matching colors, not a replacement for the ramp generator [inferred]. DC-L01-01 also warns that equal OKLCH lightness does not guarantee equal WCAG contrast, which applies to the OKLCH chart and theming tricks in [S-L19-039].
- **Brand adaptation mostly agrees:** DC-L01-09 anchors a ramp on the brand hex and picks the UI step by contrast, but notes that Stripe found simply darkening its brand colors looked "dark and muddy", a caution on the "darken it until it passes" advice [S-L19-051].
- **Palette extension is narrower in OpenDesigner:** DC-L15-06 reports Refactoring UI calling wheel-generated palettes "not very useful" for UI, and Q-color-04 advises against wheel presets as a palette. [S-L19-051] uses analogous and complementary hues for specific jobs (a storage bar, a failing brand color), which matches Q-color-04's `analogous` and `contrasting` options rather than a whole wheel palette [inferred].
- **State direction is contested in research too:** DC-L01-17 records that systems disagree (Fluent darkens on interaction, Windows lightens, Carbon depends on the base shade) and defaults to stepping toward more contrast with the surface, which in light mode sides with the darker hover of [S-L19-039] over the lighter hover of [S-L19-051] [inferred].
- **Text colors:** DC-L01-14 defaults to solid text tokens and calls opacity-based text less predictable; the opacity approach of [S-L19-057] exists as Q-color-22's `opacity-levels` option but needs a contrast check at its low end [inferred].
- **Borders conflict with a house standard:** `STD-visual-details-14` prefers a semi-transparent edge over an opaque border. Schoger's 10% gray 950 ring [S-L19-103] agrees; the opaque 85% white border of [S-L19-039] does not, and neither do OpenDesigner's current opaque border tokens, which that standard's own conflict note already flags. Under the standards policy the house standard wins [inferred].
- **Charts partly conflict with a default:** [S-L19-039] rejects gray-only and single-ramp charts, which runs against Q-color-19's default `brand-gray` (one brand chart color plus gray) for multi-series charts [inferred]; the default already switches to `categorical-6-8` for dashboards. DC-L01-24 recommends 6 to 8 ordered categorical colors, and DC-L01-23 requires a second cue besides hue; equal-lightness hues from [S-L19-039] differ only in hue, so they need that second cue even more [inferred].
- **Status colors agree** with DC-L01-15 (four statuses, each with an icon); every Q-state-06 option already uses red for danger.
- **Gradients:** DC-L01-25 and Q-color-25 default to brand-only gradients, never on interactive parts. [S-L19-045] and [S-L19-057] are stricter (usually none), while [S-L19-082] puts gradient strokes on a purchase card and on hover, which is Q-color-25's `components` option for AI and creative products.
- **See-through colors agree:** the near-black at 10% and 5% in [S-L19-103] fits DC-L01-27 and Q-color-26's `alpha-neutrals` default.

## Decisions this informs

- **Q-color-01** (fixed brand colors or generated): [S-L19-051] supports adapting a brand color that fails contrast by darkening it or pairing it with a complementary color.
- **Q-color-02** (where the brand color shows): [S-L19-056] [S-L19-061] [S-L19-072] [S-L19-075] back `accent` (key actions, active states, data); [S-L19-065] shows a hover-only accent.
- **Q-color-03** (how colorful): [S-L19-040] [S-L19-057] [S-L19-061] favor muted over saturated, which backs the `tonal` default for products.
- **Q-color-04** (how many accents): [S-L19-051] backs `one`, with analogous or complementary hues added only for specific jobs.
- **Q-color-05** (accent area): [S-L19-039] and [S-L19-051] both fit `strict` with 60-30-10 as a soft check at most.
- **Q-color-07** (how ramps are built): [S-L19-070] (HSB) and [S-L19-039] (OKLCH); keep `oklch`.
- **Q-color-08** (ramp steps): the step jobs in [S-L19-039] (500 or 600 main, 700 hover, 400 or 500 link) assume a 50 to 950 scale and can serve as a sample mapping.
- **Q-color-09** (gray tint): [S-L19-039] [S-L19-051] [S-L19-057] [S-L19-070] back `hue-matched`; [S-L19-103] shows when to match a product's pure neutrals instead.
- **Q-color-10** (how many grays): the neutral budget in [S-L19-039] (four backgrounds, one or two strokes, about three text colors) is a sizing check for the gray ramp.
- **Q-color-14** (layering): [S-L19-039] gives three light-mode card options (lighter cards on a darker page, darker cards on a white page, monochrome layers).
- **Q-color-15** (status colors): [S-L19-039] [S-L19-051] [S-L19-052] always include them, whatever the brand.
- **Q-color-17** (contrast rule): [S-L19-051] [S-L19-075] [S-L19-086] all check contrast, which backs AA on every pair.
- **Q-color-19** (chart colors): [S-L19-039] argues for a full, equal-brightness spectrum; [S-L19-075] adds a gray previous-period line.
- **Q-color-20** and **Q-state-04** (hover and pressed): lighter hover, darker press and desaturated disabled [S-L19-051], against a darker hover step [S-L19-039].
- **Q-color-22** (text colors): two colors with opacity [S-L19-057], against about three solid levels [S-L19-039].
- **Q-color-23** (border strength): an 85% white border [S-L19-039], a 10% near-black ring [S-L19-103], or dimmed strokes where contrast is a worry [S-L19-045].
- **Q-color-25** (gradients): none or one hue [S-L19-045] [S-L19-057], components allowed [S-L19-082], decorative recipes [S-L19-058] [S-L19-073].
- **Q-color-26** (see-through colors): near-black at low opacity for rings and wells [S-L19-103].
- **Q-state-06** (risky actions): red [S-L19-039] [S-L19-051] [S-L19-057].
- **Q-icon-05** (icon color): uncolored except for status [S-L19-051].

## Visual examples worth showing

- Vercel's near-monochrome palette (about 90% black, 8% white, 2% red) that still shows build success, failure and progress in color [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- Card edges on a light background shown three ways (none and washed out, a subtle shadow, a roughly 85% white border) [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]), next to a gray 950 ring at 10% opacity [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- A ladder of buttons from ghost to black, darker as they get more important, with most multi-purpose buttons around 90 to 95% white [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- A file manager before and after: five competing accent cards, colored icons and a sandy gradient background, then a neutral gray background, brand-tinted or bordered cards, uncolored icons and gray secondary text [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- A storage bar colored three ways: opacity only (bland), analogous hues, and a complementary yellow [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- An orange brand color with white text failing contrast, beside a darker orange and a complementary blue that pass [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- The same delete dialog with a purple and a red delete button [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- HSB palette steps with and without the hue slide toward blue [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]).
- Chart series at fixed OKLCH lightness and chroma with the hue stepped by 25 to 30, beside a version where green looks neon [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- A menu whose only blue item is the resubscribe prompt, and a settings panel with its default values in gray [S-L19-080] ([[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]).
- A dashboard where colored buttons and icons give way to micro charts on the KPIs [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- A blue-to-green gradient replaced by a flat fill [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- A plugin-free mesh gradient from stacked, blurred Overlay circles [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).

## Open questions

- Which color model do the "% white" targets in [S-L19-039] use (HSL lightness, HSB brightness or OKLCH lightness)? Until that is known they cannot become token values.
- Q-color-19 already uses `categorical-6-8` for dashboards; should the switch depend on the number of series rather than on the product type, given [S-L19-039] and DC-L01-24? How many hues does a 25 to 30 step give before series become hard to tell apart for people with color-vision deficiency (DC-L01-23)?
- Should hover get lighter [S-L19-051] or darker [S-L19-039]? DC-L01-17's "toward more contrast with the surface" is a rule of thumb, and no source here tested it.
- Is 45% opacity secondary text [S-L19-057] ever acceptable (large text only, at 3:1), or should the lowest opacity be raised so body text passes 4.5:1?
- Do the Tailwind pairs in [S-L19-070] (50 with 500, 950 with 300) pass AA for every hue, as the video claims? Not checked here.
- Should OpenDesigner's border tokens become semi-transparent to meet `STD-visual-details-14`, and does that change the advice in [S-L19-039]? The border side of this is covered in [[synthesis/depth-shadows-and-borders|Depth, shadows and borders synthesis]].
