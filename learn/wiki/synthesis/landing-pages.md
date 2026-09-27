---
type: synthesis
title: Landing pages
created: 2026-09-24
updated: 2026-09-28
sources:
  - 5JxUJ1fuyO8
  - 6CC8lLnqa28
  - 9WVt1CelBfg
  - A_Ozpb0XDuw
  - BvbFPzLjWcU
  - EHwZzWd-OnQ
  - EcbgbKtOELY
  - HE4rLEQpiXY
  - If7iCPDy2vk
  - Lp6ey4AyDzA
  - P2ksReDwWkE
  - PDcQJOPby1k
  - RCneB_MQ7qs
  - SfX43uIubj4
  - V3Omp1hm0Sg
  - VPeTgU7la34
  - ZsP20PN14O0
  - d4MF6pdAZNw
  - eMMiLeo_UGI
  - ek-train-your-judgement
  - ek-you-dont-need-animations
  - eks-skills-animate-recipes
  - eks-skills-find-animation-opportunities-skill
  - gKM6b2EnW1k
  - lkKGQVHrXzE
  - nl8OFGdx75w
  - pGYLZyBE32o
  - tNMAFjzapOk
  - ulSOdTgoGeY
tags:
  - od-area-patterns
---
# Landing pages

## In short

A landing page is a short story that leads a visitor to one action, such as signing up or trying the product. It opens with a clear hero: a short headline, one main button and a real picture of the product. The sections after it (logos, features, testimonials, a final call to action) should vary in layout and lead into each other. Landing pages may use bigger type and richer motion than the product, and the house standards reserve explanation motion, scroll reveals and decorative effects for marketing surfaces. That motion still needs a job, usually pointing at the product. Match the amount of effects to the page's goal: pages built to convert stay simple, pages built to be remembered can be showier.

## House standards

- `STD-when-to-animate-03` (must): every animation names a purpose; "it looks cool" is not one.
- `STD-when-to-animate-10` (must): explanation motion (showing how a feature works) only on marketing and onboarding surfaces.
- `STD-when-to-animate-11` (must): decorative motion such as mouse-tracking belongs on marketing pages and illustrations, never on functional data.
- `STD-enter-exit-origin-27` (must): scroll-triggered reveals only on marketing surfaces; `STD-enter-exit-origin-26` (should): reveal with `clip-path: inset()` rather than animating width or height.
- `STD-easing-duration-06` (must) and `STD-easing-duration-09` (must): UI motion stays under 300 ms and nothing runs over 1 s, but marketing and explanatory motion may run longer; `STD-easing-duration-06` still asks whether a slow moment needs to be slow.
- `STD-easing-duration-01` (must): pick easing by job: entrances ease-out, on-screen moves ease-in-out, constant motion such as a marquee linear.
- `STD-enter-exit-origin-13` (must): stagger group entrances by 30-80 ms; `STD-springs-gestures-13` (must): never block input while a stagger or transition plays.
- `STD-accessibility-motion-02` (must): under reduced motion, replace movement with a short opacity cross-fade instead of removing all feedback; this applies to marketing effects too [inferred].
- `STD-mobile-touch-10` (must): size marketing heroes and first screens with `min-height: 100svh`, never `100vh`.
- `STD-visual-details-01` (must): cap body text at about 65ch.

## What the sources teach

### Start from the goal and one action

- Most clients need more customers, sales or sign-ups, so lay pages out so the information is clear and the next click is obvious, and pick sections for the goal they serve (testimonials for an agency, an impact list for a nonprofit) [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- Give the header one call to action and one main thing, as Google and Apple do, because people are easily distracted; the same video allows one or maybe two things to click [S-L19-040] ([[sources/6CC8lLnqa28-6-things-you-probably-need-to-hear-as-a-web-designer|6 Things You Probably Need to Hear (as a web designer)]]). If a second button stays, remove its fill so it stops competing [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- When the nav button and the hero button go to the same place, give them the same label [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).
- Treat the page as a story that guides someone to an action: follow expected layouts (navigation at the top, top-to-bottom flow) and skip flare that gets in the way [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- A structure test: someone scrolling for 5 seconds should understand the idea [S-L19-084] ([[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]).
- Prompt-based AI products can drop the landing page entirely and open on a large prompt box above the fold [S-L19-055] ([[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]]); a typeable search bar as the hero call to action engages the visitor in an action [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- A company with one product can skip a homepage whose only job is to redirect, and lead with the product [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).

### Hero anatomy

- Many different-looking pages share one skeleton: text block, navbar, stats and image. Hero copy stays short (a seven-word heading and 14-word subtext in the example), and spacing groups it: subtext 8 px from the heading, eyebrow 12 px, buttons 32 px [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]). A simple hero example uses 32 px between items [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- The common hero is big text, a big image and generous space, set apart with one distinctive touch such as a font, an inline diagram, an interactive product image or a subtle gradient [S-L19-066] ([[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]).
- Show the real product (its dashboard or crafted crops of it) instead of unrelated stock images [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]); capture product screenshots at 3x and match the site's grays to the product's [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]); show the product early so motion can point at it [S-L19-084] ([[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]); use images of your own screens instead of generic icons [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- Use images that relate to the audience; a product site with no images at all feels robotic [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]). A few context illustrations around the hero tell people what the product is, but one too many tips it into clutter [S-L19-063] ([[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]).
- Hero layouts differ by source: a stacked hero [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]), a split hero with the headline on the left in roughly a 3/5 and 2/5 split [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]), an ultrawide split for a beauty brand [S-L19-049] ([[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]), or giant display text with a small navbar underneath [S-L19-060] ([[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]]).
- Design desktop heroes for a real viewport of about 1920 by 1,000 px, fix photo contrast by choosing a better photo before adding a subtle overlay, and keep written testimonials out of the header [S-L19-049] ([[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]). Never place hero text over the image's focal point [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).
- One practitioner sizes hero buttons at 38 px and nav buttons at 28 px, reached with padding [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]); another puts the buttons at least twice as far below the subtext as the subtext sits below the heading [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]).

### Sections and page flow

- Customer logos appeared on 41 of the 50 software sites one creator reviewed; other recurring sections are a tabbed multi-section, a simple bento on plain grids, a straight-line grid and images in the navigation menu [S-L19-066] ([[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]).
- A catalog of section layouts with rules of thumb: stacked scroll cards for three to five detailed options, a horizontal carousel for 3 to about 10 cards (not driven only by small buttons), bento only when there is enough content to fill every box, and text-only sections with at least three lines of body text [S-L19-060] ([[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]]).
- Do not alternate text-left, image-right rows all the way down; vary layouts [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]), mix in full-screen sections, cards and three-column sections [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]), flip a section when things line up too uniformly [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]), and never reuse one layout for two sections [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- Each section should lead into the next [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]). Keep structure restrained and grid-driven, then break the pattern once with a well-built surprise [S-L19-084] ([[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]).
- Add social proof beyond logos, such as testimonials [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]); testimonial cards can use a portrait as the background with a dark gradient behind the quote [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- Give the navigation hierarchy (the sign-up action stands out, a mega menu for the key links) [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]); images in navigation menus help when product names do not explain themselves [S-L19-050] ([[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]]).
- Most sites need only 3 to 5 footer links in a simple centered footer [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- Separate the wireframe from the visual identity: assemble the flow from reference sections, keep only the wireframe, then apply your own identity [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]).
- Copy gets shorter and punchier, and at the top level says how the product helps rather than only what it does [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).

### Type, color and texture

- Landing pages can use up to six font sizes with a large range, and custom landing pages often break from the column grid [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- Tighten tracking on headlines above about 24-30 px, fix orphans with `text-wrap: pretty` or `balance`, and consider inline section headings that run the title into softer supporting text [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- Let color pops come from product visuals so buttons can stay neutral, instead of spreading the accent over everything [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]); one redesign shows the bright accent only on the call to action's hover [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).
- Texture options: a very subtle gradient behind the hero [S-L19-066] ([[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]), off-whites or a noise overlay instead of flat white [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]), and a palette pulled from one moody image [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]).
- When there are no custom graphics, a "canvas grid" of borders around sections adds interest [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]); line dividers are coming back as a trend, though lines on everything can recall old slide decks [S-L19-050] ([[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]]), and piling on separators and containers adds clutter [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).

### Motion with a job

- On marketing pages an animation can replace a static asset when it explains a feature in the first viewport, as Linear's Product Intelligence page does, and marketing sites are exempt from the need for fast animation [S-L19-012] ([[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]).
- Decorative effects such as mouse-tracking are fine on marketing pages, and marketing or explanatory motion can run longer than the UI budget [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]).
- Scroll reveals use a `clip-path` transition over 600 ms and fire once; group entrances use a short stagger that never blocks interaction [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]).
- A hero's staggered entrance (announcement pill, headline, subtext, two buttons) is judged by whether it feels intentional [S-L19-011] ([[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]]).
- Motion should direct the eye to the product; one well-built hover animation can be enough, and complex animation for its own sake makes navigation harder [S-L19-084] ([[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]). Repeating a few motion themes can become part of the brand [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]).
- Motion matures from none, to simple load animations, to smooth hover effects and fluid sliders, to small high-quality details such as a blur transition [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]). Software sites are moving to simple, tasteful animation, and an imported scroll effect that renders blurry gives itself away [S-L19-066] ([[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]).
- Pages built to convert work without 3D or heavy effects; heavy scrollytelling suits awareness sites [S-L19-040] ([[sources/6CC8lLnqa28-6-things-you-probably-need-to-hear-as-a-web-designer|6 Things You Probably Need to Hear (as a web designer)]]). A counter-view: a spinning 3D logo as the hero means the rest of the page needs less design [S-L19-046] ([[sources/A_Ozpb0XDuw-how-hard-is-it-to-really-make-a-no-code-3d-animated-website|How hard is it to REALLY make a no-code 3D animated website?]]).
- Preloaders add a premium feel and cover heavy media but must stay short [S-L19-069] ([[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]); two build recipes hold the loading screen for 1,000 ms and slide it away over 800 ms [S-L19-081] ([[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]]), or slide it over 1.3 s with `expo.inOut` while the hero text rises with it [S-L19-071] ([[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]).
- Less common effects: swapping a line of text on scroll, morphing images (keep the changes small so it does not stutter) and diagrams that reveal a process step by step [S-L19-050] ([[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]]).
- Marquee text is trendy but reduces usability [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]), and scrolljacking should be used very sparingly, if ever [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- A 404 page is the place to be quirky, with a quiz, a character or a mini game [S-L19-063] ([[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]).

## Where they agree and disagree

- **Show the product.** Four sources agree: three Kole Jain videos [S-L19-061] [S-L19-072] [S-L19-084] and Steve Schoger [S-L19-103], so two practitioners. [S-L19-062] adds a related point: images of the people and settings the product serves, because a site with no images feels robotic.
- **Vary section layouts.** Four videos agree [S-L19-065] [S-L19-072] [S-L19-082] [S-L19-085], all by one practitioner (Kole Jain).
- **One main action.** [S-L19-040] and [S-L19-057] say one primary call to action per header, while [S-L19-049] and the hero in [S-L19-011] show a primary and a secondary button. They reconcile as one filled primary plus an unfilled secondary [inferred], which matches the research rule of at most one high-emphasis action per region (DC-L13-18).
- **Hero layout has no winner.** Stacked [S-L19-072], split [S-L19-103] [S-L19-049] and centered (the most common, per [S-L19-043]) are all recommended; [S-L19-043] says to pick by what the content is trying to do.
- **Effects.** [S-L19-046] argues 3D carries a page; [S-L19-040], [S-L19-054] and [S-L19-066] warn that heavy graphics slow pages or get in the way. The house purpose rule (`STD-when-to-animate-03`) sides with motion that has a job.
- **Preloaders.** The two recipes [S-L19-071] [S-L19-081] hold content back for over a second, and [S-L19-069] warns they must stay short. The house limits let marketing motion run longer (`STD-easing-duration-06`, `STD-easing-duration-09`), so the length is a judgement call [inferred]. One recipe fades the navigation in with ease-in-out [S-L19-081], and the other slides the loading screen off the page with `expo.inOut` [S-L19-071]; the house rule gives entrances and exits ease-out (`STD-easing-duration-01`), so both follow the standard instead (DC-L19-133) [inferred application].
- **Stagger timing.** The house standard is 30-80 ms per item (`STD-enter-exit-origin-13`); the research proposes 20-50 ms with a 500 ms total (DC-L04-23, the Q-motion-06 "stagger" option). The standard is locked, so the research value should follow it.
- **Marketing and product in one system.** The research defaults to one system with a calm set and a lively set (DC-L06-01), productive type plus 3-4 expressive display styles (DC-L02-11), and one or two hero moments (DC-L06-03), or one to three per flow (DC-L04-19). The sources' bigger type range [S-L19-052] and richer motion fit that "second mood" [inferred].
- **Long pages.** [S-L19-054] prefers a Load more button to infinite scroll so the footer stays reachable, which the research also says (DC-L08-21).
- **Conversion claims are unmeasured.** Statements such as "better presentation means better conversion" [S-L19-061] or logos signalling trust [S-L19-066] are practitioner opinion; none of these sources shows test data (see [[synthesis/a-b-testing-and-conversion|A/B testing and conversion synthesis]]).

## Decisions this informs

- **Q-scope-01** (marketing site in scope) and **Q-scope-06** ("persuade" screens).
- **Q-brand-05** (how the marketing site relates to the product) and **Q-brand-06** (a separate set of bigger headings).
- **Q-brand-04** and **Q-motion-01** (how lively; hero moments): marketing is where the lively set lives.
- **Q-motion-06** (screen changes and stagger), bounded by `STD-enter-exit-origin-13`.
- **Q-layout-05** (grid and bento for marketing sections).
- **Q-dir-05** (start-aligned or centered): split hero versus centered hero.
- **Q-type-05** (one font or a pair) and **Q-type-13** (tracking by size).
- **Q-color-02** (where the brand color shows): color from product visuals, accent on the call to action.
- **Q-color-25** (where gradients are allowed): subtle hero gradients, gradient strokes on call-to-action cards [S-L19-082].
- **Q-img-01** (photos) and **Q-img-02** (text on images).
- **Q-state-01** (button styles and how many main buttons per area).
- **Q-space-04** (button heights) and **Q-shape-01** (pill buttons tried in [S-L19-103]).
- **Q-pattern-02** (Load more versus infinite scroll).

## Visual examples worth showing

- The four levels of a SaaS landing page side by side, from template to crafted [S-L19-072].
- A hero with annotated spacing: 8 px to the subtext, 12 px to the eyebrow, 32 px to the buttons [S-L19-043].
- A split hero with a product screenshot inset in a tinted well, a low-opacity ring instead of a border, and inline section headings [S-L19-103].
- A logo marquee fading out at the edges with a gradient and progressive blur [S-L19-066].
- Linear's Product Intelligence animation explaining a feature in the first viewport [S-L19-012].
- A `clip-path` scroll reveal over 600 ms that fires once [S-L19-017].
- A preloader that slides up while the page content rises with it and the nav fades in last [S-L19-071] [S-L19-081].
- The Micro page restructured into a restrained layout, then given back its personality with motion [S-L19-084].
- A giant-text hero with the navbar beneath the headline [S-L19-060].
- Quirky 404 pages: an interface quiz, a movie character, a snake game [S-L19-063].
- Merged AI plans with the purchase call to action as a card with a gradient stroke [S-L19-082].

## Open questions

- Should OpenDesigner default to one hero layout, or ask? The sources do not agree.
- How long can a preloader hold content before it hurts? Only one source warns, and none measures.
- None of the conversion claims here is backed by test data.
- Reduced-motion versions of marquees, parallax, 3D heroes and scroll effects are not discussed by any practitioner source; only the house standard covers them.
- Performance budgets for video and 3D heroes are not covered.
