---
type: synthesis
title: Design resources
created: 2026-09-24
updated: 2026-09-24
sources:
  - 59XWYgN00nQ
  - 66oOi9OLMCw
  - 6CC8lLnqa28
  - 9WVt1CelBfg
  - AH_ugxmLeUM
  - BvbFPzLjWcU
  - If7iCPDy2vk
  - Lp6ey4AyDzA
  - MZSm6MA8bww
  - PDcQJOPby1k
  - RCneB_MQ7qs
  - V3Omp1hm0Sg
  - adev-changelog
  - c1TvOcKdBVE
  - eeN7yUcIWbw
  - ek-building-an-animation-course
  - ek-developing-taste
  - eks-readme
  - gKM6b2EnW1k
  - pGYLZyBE32o
  - xHD01_Onac0
tags:
  - od-area-process
---

# Design resources

## In short

Designers lean on outside resources for four things: inspiration, ready-made assets (icons, photos, mockups, fonts, 3D), tools that do one job better than Figma, and learning material. The sources name dozens of sites; what matters more is how to use them. Take one consistent icon set rather than hunting icon by icon, pick references from real products rather than showy gallery shots, and borrow structure, never identity or unlicensed assets. Emil Kowalski's sources add that easing curves and UI libraries should come from a short trusted list, which OpenDesigner locks as house standards. Most picks here are one creator's opinions with dates attached, and several videos are sponsored, so check that a site still exists, what it costs and what its licence allows before relying on it.

## House standards

- `STD-easing-duration-02` (must): use the named strong curves, and take any other curve from easing.dev or easings.co instead of hand-rolling one.
- `STD-visual-details-55` (must): when a task needs a library, recommend one from the curated list in one sentence, not a menu.
- `STD-visual-details-56` (must): read `package.json` first and reuse a listed library the project already has.
- `STD-visual-details-57` (must): never hand-roll standard components; build toasts with Sonner.
- `STD-visual-details-26` (must): build from the project's existing tokens and extend them; never add a parallel set.
- `STD-process-review-taste-51` (should): train taste on the best work, from a curated list of respected tastemakers and the people they admire.
- `STD-process-review-taste-27` (should): when a requested animation matches a recipe, start from the recipe.

Also locked, in `skills/opendesigner/references/guardrails.md`: the identity firewall (section 1: copy structure and quality, never a reference's logo, brand hue, proprietary fonts, photography or copy) and the licence rules (section 3: keep a licence ledger, keep icon libraries' MIT, ISC or Apache notices, and say who owns AI-generated assets).

## What the sources teach

### Inspiration: where to look, and what to look for

- Common inspiration sources are Dribbble, Pinterest, Instagram and Behance [S-L19-037] ([[sources/59XWYgN00nQ-create-a-portfolio-with-no-experience-or-clients-needed|Create A Portfolio With No Experience (or clients) Needed]]); Dribbble and Behance again for a mood board before opening Figma [S-L19-040] ([[sources/6CC8lLnqa28-6-things-you-probably-need-to-hear-as-a-web-designer|6 Things You Probably Need to Hear (as a web designer)]]); and Mobbin, Dribbble and Pinterest for a swipe file of about 20 hero and feature sections [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]). Mobbin sponsors that last video.
- Unsectioned splits real websites into searchable sections for layout ideas; Design Spells collects micro-interactions from large brands; trending.design gathers trending work from Twitter [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]).
- Real competitors and sibling products are references too: EV sites before a car-brand redesign [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]), and OpenAI, Microsoft and Google pages before an AI-product redesign [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- For an AI tool, a screenshot of a real product such as Linear or a realistic site from SiteInspire works better than a busy Dribbble dashboard, whose small details the AI cannot see [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).
- Emil Kowalski's method is to build a curated list of respected tastemakers, then the people they admire, and study their work; Brian Lovin's App Dissection is his example of studying apps rather than just using them [S-L19-008] ([[sources/ek-developing-taste-developing-taste|Developing Taste]]).
- Practice prompts for self-initiated projects come from Good Brief or Sharpen Design [S-L19-037] ([[sources/59XWYgN00nQ-create-a-portfolio-with-no-experience-or-clients-needed|Create A Portfolio With No Experience (or clients) Needed]]).

### Color tools

- A color generator such as Coolors gives a starting base color, and the Tailwind palette gives ready-made accent and background pairs (50 as a light background with 500 as the accent, or 950 as a dark background with 300 as the primary) [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]). Online color pickers help beginners break out of one saturated blue; keep only the one or two colors that catch your eye [S-L19-040] ([[sources/6CC8lLnqa28-6-things-you-probably-need-to-hear-as-a-web-designer|6 Things You Probably Need to Hear (as a web designer)]]).
- The UI colors tool generates a full accent ramp, and oklch.com helps build chart colors of equal brightness by fixing lightness and chroma and stepping the hue [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]). For more, see [[synthesis/color|Color synthesis]].

### Icons

- Pick one icon pack and stay with it: searching a mixed-style site such as Flaticon icon by icon gives an overwhelming mix of styles. The presenter's go-to is Feather Icons in Figma [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- Another video searches Flaticon filtered to interface icons, which returns only clean, simple icons [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]); a third downloads from Flaticon or uses the Feather or Phosphor Figma plugins [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- In SaaS product UI, swap emojis for an interface icon library such as Phosphor or Lucide [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]); when prompting an AI for a screen, name an icon library or it fills the UI with emojis [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).
- Isocons offers isometric icons with switchable rounded or sharp corners and stroke weight [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]).

### Photos, mockups, logos and other assets

- Keep more than one stock photo source: Burst (Shopify's free library) is smaller than Pexels but better organized [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]). When searching Google Images, filter to large images so photos are not grainy when enlarged [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).
- Ready-made product mockups (minimalmockups.com) give a real-looking product without building renders [S-L19-049] ([[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]).
- Logo libraries such as Logo System and Logoipsum help designers who are weak at logos; Uiverse elements paste straight into Figma, and the Relume kit (about 54 pages) is free in the Figma Community [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]).
- Dedicated tools beat Figma for some jobs: Photo Gradient for mesh gradients, Handy Arrows for hand-drawn arrows, Phase for animating Figma designs more easily than plugins or After Effects, Endless Tools for customizable 3D, and Fontjoy for a font pairing in one click, since beginners tend to pair fonts badly [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]).
- 21st.dev supplies AI-ready components whose code or prompt can be pasted into Claude, though one such result could not be imported into Figma because of its code format [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).
- Several videos give away the Figma files of what they build: nine redesigned UI elements [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]), seven AI-product components [S-L19-055] ([[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]]).

### Learning material and reference libraries

- The animations.dev course keeps a regularly updated "Vault" of resources and interviews with practitioners [S-L19-001] ([[sources/adev-changelog-animations-dev|animations.dev (changelog)]]); its bonuses include the Vault of curated articles, videos and personal websites, and 18 custom easings [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- Emil Kowalski's skills repository README indexes his agent skills (build, review, audit, find opportunities, name effects, pick libraries, prototype, mobile polish) with an install command [S-L19-014] ([[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]]).
- UX of AI is recommended because most designers will work with AI or near it; Design Sphere offers web design podcasts; Wall of Portfolios lists each designer's experience and location [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]).

## Where they agree and disagree

Between the sources:

- **Icon sources disagree:** one video rules out searching Flaticon icon by icon [S-L19-057]; another recommends Flaticon filtered to interface icons [S-L19-082]; a third uses Flaticon alongside plugin sets [S-L19-045]. All three want a consistent, simple set; the filter in [S-L19-082] is one way to get there [inferred].
- **Dribbble as inspiration, with limits:** it is a default inspiration source in [S-L19-037] [S-L19-040] [S-L19-043] [S-L19-065], but other videos warn that Dribbble shots favor looks over usability [S-L19-040] and make poor references for AI [S-L19-086]. Real products and real sites are the safer reference [S-L19-086] [S-L19-082] [inferred].
- **Curated lists over big menus:** Emil's sources narrow choices to trusted lists: libraries the author trusts [S-L19-014], a curated list of tastemakers [S-L19-008], and curves only from easing.dev or easings.co (`STD-easing-duration-02`). [S-L19-073] instead offers 20 tools to try. One is about what to ship, the other about what to explore [inferred].
- **Sponsorship:** Mobbin sponsors [S-L19-043] and Relume sponsors [S-L19-062], while [S-L19-073] recommends the Relume kit without a sponsor read. Treat any sponsored pick as a plug.

Against OpenDesigner's existing research and rules:

- **Icons:** DC-L05-01 lists open-source sets with their licences (Lucide ISC, Heroicons MIT, Phosphor MIT, Tabler) and Q-icon-01 defaults to the platform's own set. Phosphor and Lucide [S-L19-061] are on that list; Flaticon [S-L19-082] is not, and its licence terms are not covered by any source here [inferred].
- **Color ramps:** DC-L01-01 builds ramps in OKLCH and notes that Tailwind v4 moved its palette to OKLCH. The Tailwind pairs [S-L19-070] come from that palette, but the video mentions no contrast check, so each pair still needs one [inferred]. Coolors [S-L19-040] [S-L19-070] gives a base color, not a ramp.
- **Font pairing:** DC-L02-03 says a pairing needs both distinction and harmony and that too-similar faces read as a mistake. A one-click generator such as Fontjoy [S-L19-073] can suggest pairs, but the pair still needs a stated reason (`STD-visual-details-11` starts from the system font) [inferred].
- **Identity and licences:** borrowing a logo from Logoipsum, which the presenter jokes about stealing [S-L19-073], runs into the identity firewall and licence rules if it ships. Logo libraries fit as clearly marked placeholders only; the guardrails say a generated placeholder is never shown as a finished asset [inferred].
- **3D and animated assets:** DC-L05-21 notes that 3D and animated assets make a product feel alive but are heavy and can distract. Endless Tools [S-L19-073] fits Q-img-06's `3d` option with that caution [inferred].

## Decisions this informs

- **Q-ref-01** (a site, screenshot or Figma file you like): prefer real products and realistic sites over busy gallery shots [S-L19-086]; references give structure and quality, never identity (`guardrails.md` section 1).
- **Q-icon-01** (your own icons or a ready-made set): one consistent set [S-L19-057], such as Phosphor or Lucide [S-L19-061], backs `open-source` for web products.
- **Q-color-01** (fixed brand colors, or a palette built from one color) and **Q-color-07** (how each ramp is built, default `oklch`): Coolors can supply the one starting color for `seed` [S-L19-070] [S-L19-040]; OpenDesigner still builds the ramp itself [inferred].
- **Q-type-05** (one family or a pair): a pairing tool [S-L19-073] can suggest options for the `sans-serif` or `display-face` answers.
- **Q-img-01** (photos) and **Q-img-06** (3D and animated assets): stock sources and mockup sites [S-L19-073] [S-L19-049] fill `still-life` or `3d` slots, each logged with its licence.
- **Q-comp-01** (where components start): Uiverse and the Relume kit [S-L19-073] are copy-in sources for designs; for code, the curated library list of `STD-visual-details-55` applies.

## Visual examples worth showing

- Searching Flaticon unfiltered (many clashing styles) beside one consistent icon pack [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- A busy Dribbble dashboard as an AI reference beside a Linear screenshot, and the two results [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).
- Tailwind 50 with 500 and 950 with 300 as ready-made background and accent pairs [S-L19-070] ([[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]).
- Isocons' rounded and sharp isometric icons at two stroke weights [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]).
- A mesh gradient from a dedicated generator such as Photo Gradient [S-L19-073] ([[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]), beside the plugin-free Figma recipe of stacked, blurred circles on Overlay [S-L19-058] ([[sources/MZSm6MA8bww-advanced-figma-web-design-effects|Advanced FIGMA Web Design Effects]]).

## Open questions

- Which of the named sites are still live, free and licensed for commercial use? The list in [S-L19-073] dates from January 2025, and no source checks licences.
- Should OpenDesigner keep its own vetted resource list per asset slot (icons, photos, mockups, fonts, 3D), with licence notes, the way `STD-visual-details-55` does for code libraries?
- Is Flaticon's "interface icons" filter consistent enough to count as one set, or does it mix icon families?
