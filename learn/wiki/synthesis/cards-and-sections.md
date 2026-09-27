---
type: synthesis
title: Cards and sections
created: 2026-09-24
updated: 2026-09-24
sources:
  - 14h1VnkQvIc
  - 66oOi9OLMCw
  - 9WVt1CelBfg
  - B7k5rOgmOGY
  - BvbFPzLjWcU
  - EOcY3hPMQkk
  - EcbgbKtOELY
  - Gfsd8NNuD9g
  - HE4rLEQpiXY
  - Lp6ey4AyDzA
  - P2ksReDwWkE
  - PDcQJOPby1k
  - V3Omp1hm0Sg
  - VPeTgU7la34
  - Yr2uIcFZDDQ
  - c1TvOcKdBVE
  - eMMiLeo_UGI
  - gKM6b2EnW1k
  - lkKGQVHrXzE
  - neE6wOuBIP8
  - pGYLZyBE32o
  - ulSOdTgoGeY
tags:
  - od-area-layout
  - od-area-elevation
  - od-area-components
---
# Cards and sections

## In short

A card is a container that groups content, gives it four clean edges and sets it apart from the page. Cards help most on small screens and in dashboards, but too many of them, or a card inside a card, add clutter, so many sources remove cards and let space do the grouping. When a card is needed, separate it from the page with a light edge, a step in tone or a soft shadow, and in dark mode make raised cards lighter than what they sit on. Inside a card, rank the content so the key fact leads and drop labels the layout already makes clear. Marketing pages build their sections from a small set of patterns (bento grids, carousels, stacked cards, logo strips) chosen by how much content there is, and vary them from section to section.

## House standards

- STD-visual-details-14 (should): separate surfaces with a semi-transparent shadow rather than a solid, opaque border.
- STD-accessibility-motion-12 (must): under `prefers-contrast: more`, give surfaces near-solid backgrounds with a defined, contrasting border.
- STD-visual-details-17 (should): darker, heavier materials separate structural regions; lighter materials draw attention to interactive elements.
- STD-visual-details-18 (must): never place a light translucent surface on top of another light translucent surface.
- STD-visual-details-19 (should): bigger surfaces get a stronger blur and a deeper shadow than small chips.
- STD-visual-details-24 (should): give each color role a light value and a dark value.
- STD-visual-details-36 (must): things that look the same behave the same and live in the same place.
- STD-visual-details-30 (should): strip what is unnecessary and make every element earn its place.
- STD-mobile-touch-19 (should): build a carousel with native scroll snap (`scroll-snap-type: x mandatory`, `scroll-snap-align: start`) when it can be native scroll.
- STD-mobile-touch-18 (must): a horizontal JavaScript carousel sets `touch-action: pan-y`.
- STD-accessibility-motion-15 (must): gate every hover animation (and every hover style on mobile web) to `(hover: hover) and (pointer: fine)`.
- STD-mobile-touch-30 (must): in a mobile app, move hover affordances into press, position or nothing.
- STD-when-to-animate-07 (must): remove or shrink hover and similar motion on things people see tens of times a day.
- STD-when-to-animate-13 and STD-enter-exit-origin-13 (must): stagger entrances only for grids and lists seen occasionally, by 30–80 ms per item.
- STD-enter-exit-origin-28 (must): fire a scroll reveal once, when at least 100 px of the element is in view.
- STD-process-review-taste-43 (must): show design variants one at a time, full size and in context; a card needs its siblings.

## What the sources teach

### Use a card only when it earns its place

- On mobile, cards are the main building block because they group content without needing much white space. Avoid a card inside a card: it creates padding on padding and cramps the content, so group the inner content with space instead [S-L19-053] [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]].
- Cards take a much larger footprint, especially in multi-column layouts such as a store; removing cards and dividers lets content breathe, and many containers make a design feel cluttered [S-L19-057] [[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]].
- A card gives four edges for free, but people who fill a wide canvas with containers end up with "borders on borders and three radii" stacked together. A single line and a column edge can dissolve the cards into the interface while sections do the grouping [S-L19-080] [[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]].
- Remove cards that do nothing [S-L19-061] [[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]. Merge related cards (a growth rate into the profits card, the card lock into the credit card), which took a 12-card dashboard down to a few meaningful modules [S-L19-068] [[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]].
- Most dashboards are made of many cards, so keep card margins well spaced [S-L19-047] [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]] and keep them consistent across modules even when a module then shows fewer items [S-L19-068] [[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]].
- Drop the background tints and background cards an AI tends to add (on the logo cloud, footer, stats and call to action) [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]].

### Setting a card apart from the page

- In light mode there are three ways: cards lighter than the page (if cards are pure white, the page should not be), cards darker than the page (often the sidebar color), or monochrome layers [S-L19-039] [[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]].
- On a light background, define card edges with a light gray border of about 85% white, not a thin black border; a subtle drop shadow alone is only slightly better than nothing [S-L19-039] [[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]. The 85% value is one video's.
- A card can be separated by a border or by a background color; the presenter prefers outlines in dark mode and fills in light mode, and says the choice is "totally up to you" [S-L19-047] [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]].
- Shadows should be softer than most people make them: cards need less shadow than popovers, and a shadow should never be the first thing you notice [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]].
- Instead of a solid border next to a shadow, use an outer ring of near-black at 10% opacity; put screenshots in a softly tinted "well" (near-black at 5%, no border) [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]. These are one designer's values in Tailwind terms.
- Do not give every card its own bright accent. Lighten a brand-colored card and switch its text to black, give cards a light tint of the brand color (as Headspace does), or drop the card background and use a simple border [S-L19-051] [[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]].
- Depth does not have to come from shadows: offset elements, sections with adjusted backgrounds, and a dark background behind lighter cards all add it [S-L19-085] [[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]].
- In dark mode raised surfaces always get lighter as they rise, or get only a border [S-L19-039] [[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]. Make cards lighter than the background, lower the contrast of light borders and dim bright chips [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]. One video steps each layer about 4–6 brightness up and 10–20 saturation down [S-L19-070] [[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]. A dark design that still lacks something can add frosted glass to its cards [S-L19-085] [[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]].

### What goes inside a card

- Turn a spreadsheet-like card into one with hierarchy: an image, the key item large and bold on top, smaller secondary details, a standout price and icons for the route [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]].
- Group related facts (name with location, cost with rating), rank the groups, drop labels the layout already implies, keep labels only where values could be confused (check-in and check-out), and put minor details in one row with icons [S-L19-070] [[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]].
- Listing cards should show the specifics people scan by (location, rating, price), truncate long names, and put a circle behind icons that sit on bright images [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]].
- Give a card only the actions that make sense for the real object (a credit card gets "lock card", not "receive"), and retitle a card when its content changes [S-L19-068] [[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]].
- When list cards feel busy, collapse their action buttons into a triple-dot menu and reduce chips to icons [S-L19-061] [[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]. Another source disagrees: hiding secondary actions in a corner menu is generally not the best fix; move content or manufacture a new edge so the buttons line up [S-L19-080] [[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]].
- Place content against the card's edges instead of filling empty space with more content [S-L19-080] [[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]].
- Nested corners: the inner radius is the outer radius minus the gap (a 30 px outer radius with a 10 px gap gives 20 px). Estimate by eye when the gap is larger than the outer radius, and skip the correction for pills [S-L19-070] [[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]]. Screenshots inset about 8 px inside their container get corners concentric with it [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]].
- Rounded corners make cards feel friendlier, and better image and text margins are among the first fixes for a weak card [S-L19-075] [[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]].

### Links, images and hover

- When cards repeat, make the whole card the link and drop the button; an arrow can fade in on hover to show it is clickable. Keep an explicit button when the card has a specific action such as "Try it out" [S-L19-075] [[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]].
- Text on an image card: make the image about 3/4 of the card's height and run a smooth gradient up from its bottom under the text. The overlay only works with some images and colors, while a standard card with text beside the image always works [S-L19-075] [[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]].
- Put card titles above the images when legibility on the photo is uncertain; a lightbox card with text over a full-size photo gets a gradient and a close button [S-L19-065] [[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]. Testimonial cards can use a portrait as the background, with a white quote at the bottom over a dark gradient [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]].
- Hover effects on marketing cards: zoom the image out and pop up the call to action [S-L19-065] [[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]], or blur and enlarge the image and reveal extra text [S-L19-082] [[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]. A pricing section can make the purchase call to action one of the plan cards, marked with a gradient stroke [S-L19-082] [[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]].

### Section patterns for marketing pages

- One video catalogues section layouts [S-L19-060] [[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]]: cards on a dark background, placed very close together with precise spacing; a thin cropped photo with a strong line of text as an interlude; stacked cards that slide up on scroll, for three to five options that need detail; a horizontal carousel for 3 to about 10 cards that should not rely on small buttons alone; a bento only when there is enough content, with box sizes that change as the content is planned; a text-only section with at least three lines of body text. The counts are one presenter's judgment.
- Another looked at 50 software sites and found the same few sections [S-L19-066] [[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]: a customer logo strip (on 41 of the 50 sites), plain or as a marquee; a hero of big text and a big image; a tabbed "clickable multisection" where every tab must be designed before handoff; a simple bento built on plain grids; and a "straight line grid" with visible lines between cells.
- Replace a row of four cards with a bento grid and a static row of three cards with a clickable multi-select, and make each section lead into the next [S-L19-072] [[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]].
- A features list that would run off the screen can become a bento grid so nothing is lost while scrolling [S-L19-043] [[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]. A product card slider shows every product when room is short [S-L19-049] [[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]], and a feature slider followed by a bento gives two feature sections different layouts [S-L19-065] [[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]].
- Drop a redundant section title above a bento and let the card headers carry it; build diagrams or real product UI into the bento cards [S-L19-082] [[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]].
- Mix full-screen sections with cards, shift cards up and down, and let a sliding row of cards extend past the frame [S-L19-085] [[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]].
- Feature cards can be tinted wells with inset, cropped screenshots, stats can be separated by dividers, and section headings can run the title into a softer supporting sentence as one block [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]].
- On mobile, swipeable scrolling cards work better than stacking the same items vertically, and a swipeable set needs page indicators [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]. The house standard builds it with native scroll snap where possible (STD-mobile-touch-19).
- On a dashboard, a tasks button can become a full section, and a gap left in the grid can be filled with a section the product was missing [S-L19-068] [[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]].

### Lists instead of cards

- Stacking items into one list is less cluttered than giving each its own card; add a border per item only when you want stronger separation [S-L19-047] [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]].
- Separate list rows with space, and use a subtle alternating background when rows must sit tight [S-L19-070] [[sources/c1TvOcKdBVE-the-8-ui-ux-cheat-codes-for-instantly-better-designs|The 8 UI/UX Cheat Codes for INSTANTLY Better Designs]].

## Where they agree and disagree

- **How to separate a card.** DC-L08-15 defaults to a tinted fill or an outline for static cards and keeps elevation for things that float; DC-L04-10's hybrid default is flat surfaces with borders in the page and shadows only for menus, popovers and dialogs. [S-L19-039], [S-L19-047] and [S-L19-051] agree (borders or fills). [S-L19-052] puts soft shadows on light-mode cards, closer to DC-L01-13's heuristic of a shadow or border plus a subtle tone in light mode.
- **Borders against the house standard.** STD-visual-details-14 prefers a semi-transparent shadow to a solid, opaque border, and the standards file already lists Q-depth-01's `borders` option and the opaque border tokens as conflicts. The low-opacity ring in [S-L19-103] is the closest source match [inferred]; the 85% white border in [S-L19-039] and the simple border in [S-L19-051] are solid borders and would need to become semi-transparent to meet the standard [inferred]. The standard wins.
- **Contrast of card edges.** DC-L08-15 notes that if a border is the only boundary of an interactive card it needs 3:1 contrast. A border of about 85% white on a white page [S-L19-039] is well below that [inferred], so it suits static cards, not clickable ones that rely on the border alone.
- **Dark mode.** [S-L19-039], [S-L19-052], [S-L19-070] and [S-L19-085] all make raised cards lighter than the background, which matches DC-L01-13 and DC-L04-10.
- **Nesting.** [S-L19-053] (no card inside a card) and [S-L19-080] (borders on borders) point to a single level of cards [inferred]; DC-L15-05 proposes a builder check, itself marked as inferred in the card, with a maximum container depth of 2.
- **Cards or space.** [S-L19-053] uses cards on mobile because space is short, while [S-L19-057] removes cards in a desktop store grid. The contexts differ [inferred], and DC-L15-05's rule covers both: add a container when content types mix, items sit in a grid or spacing cannot be controlled.
- **Nested radius.** [S-L19-070] and [S-L19-103] agree with DC-L04-05 (inner radius is the outer radius minus the padding, with a floor) and with Q-pref-03's `auto-known` default. The eyeball rule in [S-L19-070] and DC-L04-05's floor both handle a gap larger than the outer radius.
- **Hiding card actions.** [S-L19-061] collapses buttons into a triple-dot menu and [S-L19-068] tucks a rarely wanted detail behind a kebab icon; [S-L19-080] says hiding actions is generally not the fix. Q-pattern-03's `progressive` default (extras behind a clearly named button) sits between them.
- **Hover affordances.** Hover arrows, zooms and reveals ([S-L19-075], [S-L19-065], [S-L19-082]) must be gated to fine pointers (STD-accessibility-motion-15) and redesigned for touch in mobile apps (STD-mobile-touch-30). STD-when-to-animate-07 also limits hover motion on things seen tens of times a day, which suits occasional marketing cards more than dashboard cards used all day [inferred].
- **Bento.** [S-L19-060], [S-L19-066], [S-L19-072] and [S-L19-082] all treat bento grids as a marketing pattern that needs enough content and simple construction; DC-L15-07 calls bento a hierarchical grid for marketing feature sections. They agree.
- **Carousel size.** Only [S-L19-060] gives a count (3 to about 10 cards); treat it as opinion. The build method comes from the house standards (STD-mobile-touch-19, STD-mobile-touch-18).

## Decisions this informs

- **Q-depth-01** (how cards stand out): borders ([S-L19-039], [S-L19-047], [S-L19-051]), soft shadows [S-L19-052], a low-opacity ring [S-L19-103]; STD-visual-details-14 favors a semi-transparent treatment.
- **Q-color-14** (how stacked layers are shaded): lighter, darker or monochrome cards in light mode [S-L19-039]; lighter steps per layer in dark mode [S-L19-070]; a neutral gray page with white cards [S-L19-051].
- **Q-depth-02** (how many surface levels): cards need less shadow than popovers [S-L19-052], which implies at least two raised levels [inferred].
- **Q-dir-04** (group by space, cards or lines): cards on mobile [S-L19-053], cards removed on desktop grids [S-L19-057], cards dissolved with lines [S-L19-080].
- **Q-layout-05** (grid and bento for marketing sections): bento only with enough content [S-L19-060], simple bentos [S-L19-066], four cards to a bento [S-L19-072].
- **Q-pref-03** (nested corners): outer radius minus the gap [S-L19-070], concentric insets [S-L19-103].
- **Q-img-02** (text on images): an image about 3/4 of the card's height with a smooth gradient under the text, or text beside the image [S-L19-075], titles above images [S-L19-065], gradient-backed testimonial cards [S-L19-103], a circle behind icons on bright images [S-L19-054].
- **Q-depth-05** (how list rows are split): one stacked list [S-L19-047]; space or alternating rows [S-L19-070].
- **Q-pattern-03** (main options first): triple-dot menus [S-L19-061] against manufactured edges [S-L19-080].
- **Q-shape-01** (how soft corners feel): rounded cards read as friendlier [S-L19-075].

## Visual examples worth showing

- Card edges on a light background: no edge (washed out), a subtle shadow, then a border of about 85% white [S-L19-039].
- The trip card before and after [S-L19-052], and the rental listing card before and after [S-L19-070].
- A card nested in a card (padding on padding) next to the same content grouped with space [S-L19-053].
- A wide canvas of stacked containers dissolved with a single line and a column edge [S-L19-080].
- A whole-card link with a hover arrow next to a card with an explicit button, and an image card (image about 3/4 of the card's height, gradient under the text) next to a standard card [S-L19-075].
- A dark dashboard with card layers stepping lighter and less saturated [S-L19-070].
- A tinted well with an inset screenshot and concentric corners [S-L19-103].
- The section catalogue: cards on a dark background, stacked scroll cards, a card carousel, a bento and a text-only section [S-L19-060]; a simple bento next to a straight line grid [S-L19-066].
- Busy link cards calmed with a triple-dot menu and icon chips [S-L19-061].
- A row of four cards turned into a bento, and three cards turned into a clickable multi-select [S-L19-072].
- Following STD-process-review-taste-43, show each card option with its siblings on a real page, not as isolated thumbnails.

## Open questions

- How should OpenDesigner reconcile STD-visual-details-14 (semi-transparent shadow over a solid border) with the sources that recommend solid borders ([S-L19-039], [S-L19-047], [S-L19-051]) and with Q-depth-01's `borders` option, especially in dark mode where the sources say shadows do little?
- What should replace hover-only card affordances (a fading arrow, a reveal on hover) on touch screens under STD-mobile-touch-30?
- Should busy cards hide actions in a menu ([S-L19-061]) or manufacture edges ([S-L19-080])? Neither is tested.
- Is 3 to about 10 cards the right carousel range? Only [S-L19-060] says so.
- Should the builder's nesting check allow one level of card ([S-L19-053], [S-L19-080]) or two (DC-L15-05)?
