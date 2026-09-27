---
type: synthesis
title: Visual hierarchy
created: 2026-09-24
updated: 2026-09-24
sources:
  - 66oOi9OLMCw
  - 6CC8lLnqa28
  - 7sUUzOCv47U
  - 9WVt1CelBfg
  - EOcY3hPMQkk
  - EcbgbKtOELY
  - HE4rLEQpiXY
  - Ksx9C2-3yMo
  - Lp6ey4AyDzA
  - P2ksReDwWkE
  - PDcQJOPby1k
  - RCneB_MQ7qs
  - SfX43uIubj4
  - ToJiXPTNnLY
  - V3Omp1hm0Sg
  - Yr2uIcFZDDQ
  - c1TvOcKdBVE
  - eMMiLeo_UGI
  - eks-skills-apple-design-skill
  - gKM6b2EnW1k
  - lkKGQVHrXzE
  - neE6wOuBIP8
  - tNMAFjzapOk
  - ulSOdTgoGeY
tags:
  - od-area-layout
  - od-area-overview
  - od-area-typography
---
# Visual hierarchy

## In short

Visual hierarchy means the most important thing on a screen is the most obvious one, and the eye then moves through the rest in order. First decide the order (rank every piece of content), then show it with size, weight, color, position and spacing together, not with font size alone. Something stands out because its neighbours are quieter, so keep one main action and one accent per area and let the rest go gray. Hiding what is rarely needed until someone looks for it is also hierarchy. Most of the numbers below come from single practitioner videos, and some text-opacity values need a contrast check before they become defaults.

## House standards

- STD-visual-details-29 (should): use order, spacing and contrast so the most important thing on a screen is the most obvious.
- STD-visual-details-07 (should): build type hierarchy from weight, size and line-height set together, not from font size alone.
- STD-visual-details-08 (should): emphasise interface text with weight; keep italic for citations and stress in prose.
- STD-visual-details-09 (must): underline only links; emphasise other text with weight or color.
- STD-visual-details-17 (should): darker, heavier materials separate structural regions such as sidebars; lighter materials draw attention to interactive elements such as buttons.
- STD-visual-details-13 (should): over blurred or translucent surfaces, avoid flat gray text; use higher contrast, slightly heavier weight and a little more letter spacing.
- STD-visual-details-30 (should): strip what is unnecessary so the core purpose shows, without burying everything to look minimal.
- STD-visual-details-31 (should): show the common path first and put advanced options one level deeper.
- STD-visual-details-25 (must): with no project to draw tokens from, use a restrained look: neutral grays, one accent color, the system font.
- STD-accessibility-motion-15 (must): put every hover animation (and, on mobile web, every hover style) inside `@media (hover: hover) and (pointer: fine)`.
- STD-mobile-touch-30 (must): in a mobile app, move every affordance the web puts in hover into press, position or nothing.

## What the sources teach

### Rank before you style

- List every text element in order of importance (heading, then subheadings, then paragraphs) and style them to match that order [S-L19-042] [[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]].
- A dashboard redesign starts with a hierarchy assessment: rank each module as high, mid or low priority, and expect to throw some elements away [S-L19-068] [[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]].
- On a card, rank the facts by importance, group the ones that belong together and drop labels the layout already makes clear [S-L19-070] [[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]].
- The apple-design skill states the goal: order, spacing and contrast should make the most important thing the most obvious (STD-visual-details-29) [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- Hierarchy is not an exact science; more than one arrangement can be right if the same ideas apply [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]].

### Size, weight and color together

- Most people use size alone; font weight and text color add much more difference without changing anything else. The presenter caps it at two weights and two text colors: the primary color and the same color at 45–70% opacity [S-L19-057] [[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]. The cap and the opacity range are one video's preference (see the contrast note below).
- The apple-design skill builds hierarchy from weight, size and line-height as a set, and emphasises with weight (STD-visual-details-07, STD-visual-details-08) [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- Color alone can separate two lines of the same size: on one landing page two 15 px stats lines differ only because the second is at 55% opacity [S-L19-043] [[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]. These values come from one site.
- Let size carry the heading without also making it bold, bold the subheadings so they scan, and keep paragraphs at full opacity so the smallest text is not also the faintest. Weight and color steps must look clearly different to read as separate levels [S-L19-042] [[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]].
- Darkness signals importance: the darkest text is kept for important headings (about 11% white), most body text sits at 15–20% white and subtext at 30–40%; the more important a button, the darker it is [S-L19-039] [[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]. These are one video's values, and the color model behind "% white" is not named.
- Use dark gray rather than pure black for secondary information such as file size, file type, labels and borders [S-L19-051] [[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]; set supporting text and stat labels in a softer gray (gray 600) [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]].
- A template-like page has flat hierarchy in its type and navigation. Color and size then build clear hierarchy, though at one stage it was "slightly overdone", so the headline dominated at the expense of the sub-line [S-L19-072] [[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]].
- A gap between text sizes that is too large splits a page into two styles [S-L19-065] [[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]. Dashboards use a narrow range of sizes (normally nothing above 24 px), while landing pages can use up to six sizes with a wide range [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]].

### Position and scale

- The most important item goes at the top, large and bold, with secondary details smaller below it. One key value can be set apart from everything else: on a trip card, the price at the top right in blue [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]].
- On a dashboard, more important information goes higher and farther left [S-L19-068] [[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]].
- People expect information to flow top to bottom and left to right, and calls to action should be eye-catching and easy to find [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]].
- Size things by what people care about: on a pricing card the plan name gets smaller and the cost per month larger [S-L19-061] [[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]].
- Making an element bigger draws attention to it; stacking features into one column keeps attention on one at a time [S-L19-085] [[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]].
- A giant headline feels more important next to very small navbar text, and more so with the navbar placed beneath it [S-L19-060] [[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]].
- Visitors see before they read: in a portfolio the work's imagery should dominate and text should stay secondary [S-L19-064] [[sources/ToJiXPTNnLY-professional-portfolio-breakdown-why-is-theirs-so-much-better|Professional Portfolio Breakdown — Why Is Theirs So Much Better?]].

### Emphasis is a difference from the neighbours

- Emphasis comes from the difference between an element and what is around it. Make default values gray and give color only to what matters, like the single blue item in a menu [S-L19-080] [[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]].
- A header should have only one primary call to action; if a second button must stay, remove its background so it stops competing [S-L19-057] [[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]].
- Give visitors one or maybe two things to look at and click on, and remove everything else [S-L19-040] [[sources/6CC8lLnqa28-6-things-you-probably-need-to-hear-as-a-web-designer|6 Things You Probably Need to Hear (as a web designer)]].
- Navigation needs hierarchy too: the sign-up action and the most important links should stand out, instead of a menu where every item looks the same [S-L19-072] [[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]. Keep the nav button smaller than the hero button so they do not compete [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]].
- When a pricing card's button moves higher up the card, make it stroke-only to keep the hierarchy [S-L19-075] [[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]].
- Direct the eye: darken the hero's edges to pull attention to the centered text, and use motion toward each section's focal point [S-L19-062] [[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]. Decorative elements should pull attention toward a centered message, and one illustration too many turns them into clutter [S-L19-063] [[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]].
- A good layout guides the eye. A product that says what it is only in a 12 px line tucked in a corner leaves visitors unable to tell [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]. In menus, alignment and type differences separate clickable items, non-clickable items and keyboard shortcuts [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]].

### Grouping and scanning

- Grouping the elements that go together is another form of hierarchy [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]. Pushing elements closer together creates hierarchy so no element sits alone [S-L19-065] [[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]], and spacing-based grouping sets the reading order of a hero [S-L19-043] [[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]].
- Screens are scanned, not read. Differentiate dense content with avatars, grouping, chips, icons and recognisable visuals rather than more text, labels or tooltips [S-L19-080] [[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]].
- Listing cards should lead with the details people scan by (location, rating, price) and leave descriptions for the page that opens on click [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]].

### Hierarchy by showing and hiding

- Progressive disclosure is a kind of hierarchy based on what you show and hide. Rarely used features (sharing) go into a popover, secondary actions (removing a user) appear on hover with a tooltip, and onboarding starts with a single tooltip. Each action sits somewhere on a "spectrum of explicitness", from hidden on hover to a global, always-visible button [S-L19-056] [[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]].
- Show the common path first and put advanced options one level deeper (STD-visual-details-31) [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- Remove what does not earn its place: section titles, background tints and background cards that add nothing [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]], and unnecessary elements on pricing cards [S-L19-061] [[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]. Simplicity is not the same as minimalism (STD-visual-details-30) [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].

## Where they agree and disagree

- **Size, weight and color.** [S-L19-057], [S-L19-042] and [S-L19-020] agree that size alone is not enough. This matches STD-visual-details-07 and DC-L15-02, which lets a system lead with size, weight or color.
- **How many weights.** [S-L19-057] caps text at two weights, and DC-L15-02's stated default also uses two weights. DC-L02-15 defaults to three (400 body, 500–600 labels, 600–700 headings). [S-L19-042] only warns against extremes (ultra bold, ultra thin).
- **How many text colors, and how they are made.** [S-L19-057] uses two colors made with opacity; [S-L19-039] describes three lightness bands; DC-L15-02 defaults to three text colors; DC-L01-14 defaults to solid color tokens per level rather than opacities.
- **Contrast.** [S-L19-042] warns that the smallest text should not also be the faintest. OpenDesigner's guardrails lock WCAG 2.2 AA (4.5:1 for text), and DC-L01-14 says secondary text must still pass 4.5:1 on the lowest surface it appears on. The analysis of [S-L19-057] notes that black at 45% on white is about 3.4:1, which fails; the 55% line in [S-L19-043] and the 30–40% subtext band in [S-L19-039] need the same check before any of them becomes a default [inferred]. DC-L15-02 also warns against hierarchy by color alone, so a color-only layout (one of the options shown in [S-L19-042]) needs a size or weight difference as well [inferred].
- **Emphasis budget.** [S-L19-057], [S-L19-040] and [S-L19-080] match DC-L15-03's strict default (one dominant element and one primary action per view, accent kept to primary actions, selection and status) and Q-color-05's `strict` default.
- **Hierarchy strength.** [S-L19-065] (too large a jump in sizes) and [S-L19-072] (slightly overdone) agree with DC-L15-02 that too dramatic a hierarchy fails, just as too subtle a one does. The narrow dashboard range in [S-L19-052] fits DC-L15-02's subtle option for dense apps.
- **Density.** [S-L19-080] (differentiate dense content rather than add space) agrees with DC-L15-04's heuristic that denser layouts need stronger grouping and signifiers.
- **Hover-revealed actions.** [S-L19-056] reveals secondary actions on hover, and its analysis notes that touch and keyboard access are not discussed. STD-accessibility-motion-15 gates hover styles to fine pointers, and STD-mobile-touch-30 requires mobile apps to move hover affordances into press, position or nothing, so a hover-only action needs another path on touch. Q-pattern-03's `contextual` option carries the same risk [inferred].
- **Darker means more important?** [S-L19-039] makes the most important button the darkest, while STD-visual-details-17 uses darker, heavier materials for structural regions and lighter materials to draw attention to interactive elements. The two talk about different layers (button fills versus translucent materials), so they need not conflict, but the builder should not merge them into one rule [inferred].
- **Progressive disclosure.** [S-L19-056] agrees with STD-visual-details-31 and with Q-pattern-03's `progressive` default.

## Decisions this informs

- **Q-dir-03** (how much headings stand out): too large a jump [S-L19-065], "slightly overdone" [S-L19-072], giant headline against tiny nav [S-L19-060], narrow range for dashboards and wide for landing pages [S-L19-052].
- **Q-type-12** (weights and how important text stands out): at most two weights [S-L19-057]; weight or color can each carry a level [S-L19-042].
- **Q-color-22** (text colors, solid or see-through): two colors made with opacity [S-L19-057], three lightness bands [S-L19-039], grays for secondary information ([S-L19-051], [S-L19-103]); opacity values need the 4.5:1 check.
- **Q-type-09** (size ratio): [S-L19-042] proposes the square root of the golden ratio (1.27) for a full style guide and its cube root for dense or small screens; this is the presenter's own method.
- **Q-color-05** (how much accent color): color only for what matters ([S-L19-080], [S-L19-051]).
- **Q-state-01** (button styles and main buttons per area): one primary call to action per header [S-L19-057]; stroke-only when a button's position would otherwise compete [S-L19-075].
- **Q-pattern-03** (everything at once or main options first): the spectrum of explicitness [S-L19-056].
- **Q-dir-02** (density): dense lists need differentiation, not only space [S-L19-080].

## Visual examples worth showing

- The stats row: two 15 px lines, the second at 55% opacity [S-L19-043] (check the contrast before reusing the value).
- The trip card before and after: spreadsheet-like, then image on top, key item large, price top right in blue [S-L19-052].
- One heading, subheading and paragraph styled two ways: bold heading with faint paragraphs, against a large plain heading, bold subheadings and full-opacity paragraphs [S-L19-042].
- A text block with size only, then with two weights and two colors added [S-L19-057].
- A header with two filled buttons, then with the second button's background removed [S-L19-057].
- A menu where the only blue item is the one that matters, and a settings panel where every chip is on its default and nothing stands out [S-L19-080].
- A giant headline with the nav placed beneath it [S-L19-060].
- A pricing card with a smaller plan name and larger price [S-L19-061], and one whose moved-up button becomes stroke-only [S-L19-075].
- A finance dashboard with modules tiered high, mid and low [S-L19-068].
- A dense table shown with its visible UI, then with all its hidden UI (copy chips, comment markers, hover actions) overlaid [S-L19-056].
- A hero whose darkened edges pull the eye to the centered text [S-L19-062].

## Open questions

- Which text opacities pass 4.5:1 on each surface in light and dark mode, and should OpenDesigner offer opacity-based text tiers at all when DC-L01-14 defaults to solid tokens?
- Two weights ([S-L19-057], DC-L15-02) or three (DC-L02-15) as the default?
- No question records where dashboard modules go by priority (higher and farther left) [S-L19-068].
- How should hover-revealed secondary actions [S-L19-056] work on touch screens under STD-mobile-touch-30?
- Should "the more important a button, the darker it is" [S-L19-039] become a button rule, given STD-visual-details-17 treats lighter materials as the attention-drawing ones?
