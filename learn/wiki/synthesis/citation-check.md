---
type: synthesis
title: Citation check
tags:
  - quality
---

# Citation check (Jev)

Every must/should rule in `learn/analysis/` was checked against the source passage its evidence points to. Code finds the passage; TypeSafe's Jev judges whether it supports the rule. Verdicts below 0.8 confidence, and every verdict other than *supports*, go to review. Run: `python3 tools/wiki.py cite-check`.

- Rules checked: 2372
- supports: 2361
- contradicts: 1
- unsupported: 10
- Flagged for review: 47

## Flagged

| source | rule # | verdict | confidence | how the passage was found | rule |
|---|---|---|---|---|---|
| `eMMiLeo_UGI` | 17 | contradicts | 0.29 | evidence found | Do not rely largely on images to supply the page's color. |
| `referodesign-refero-skil-skills-refero-design-references-typography` | 12 | unsupported | 0.37 | keyword window | Set line height to 1.5-1.7 for body, 1.4-1.5 for short paragraphs, 1.0-1.2 for headlines, 0.9-1.1 for large display, 1.2-1.4 for UI text and 1 for buttons. |
| `referodesign-refero-skil-skills-refero-design-skill` | 32 | unsupported | 0.48 | evidence found | Before final delivery, run the quality gate checklist; if any answer is no, research or refine more before delivering. |
| `referodesign-refero-skil-skills-refero-design-references-example-workflow` | 10 | unsupported | 0.55 | keyword window | Use cards only for plan comparison and interaction, with thin borders, a subtle selected state and no heavy shadows. |
| `referodesign-refero-skil-skills-refero-design-references-craft-details` | 33 | unsupported | 0.59 | evidence found | Format dates and numbers with Intl.DateTimeFormat and Intl.NumberFormat instead of hardcoding. |
| `palantir-workshop-applic-application-design-best-practices` | 6 | unsupported | 0.67 | evidence found | In a row and column combination layout, anchor filters in the left-most section so the application's content flows to the right. |
| `referodesign-refero-skil-skills-refero-design-skill` | 22 | unsupported | 0.76 | evidence found | Use real product evidence for copy, trust signals, objection handling and section order. |
| `referodesign-refero-skil-skills-refero-design-references-mcp-tools` | 5 | unsupported | 0.83 | keyword window | Translate every borrowed reference to the user's product, audience and constraints; never copy a single style directly. |
| `palantir-workshop-applic-application-design-best-practices` | 3 | unsupported | 0.89 | evidence found | Maintain sufficient whitespace; ideally it makes up 30 to 40 percent of the screen. |
| `referodesign-refero-skil-skills-refero-design-references-typography` | 18 | unsupported | 0.95 | keyword window | Always specify letter spacing in em, never px. |
| `referodesign-refero-skil-skills-refero-design-references-mcp-tools` | 9 | unsupported | 0.98 | evidence found | Fetch at most 3-4 full styles per refero_get_style batch, and retry screen batches with fewer IDs if one fails. |
| `vaul-other` | 2 | supports | 0.17 | evidence found | If a drawer is non-dismissible, give it an explicit way to close [inferred]. |
| `BUDipdbKK7Y` | 6 | supports | 0.21 | evidence found | Do not pair a progress warning with a button that suggests the user change their goal. |
| `referodesign-refero-skil-skills-refero-design-references-typography` | 33 | supports | 0.27 | evidence found | Build hierarchy in this order of impact: size, weight, color, case (caps for labels), spacing, then italic (rarely); do not make everything bold or use italic everywhere. |
| `referodesign-refero-skil-skills-refero-design-references-typography` | 17 | supports | 0.33 | evidence found | Tighten large headings (32px+) to 0 to -0.02em and display text (48px+) to -0.02em to -0.03em, only for non-light headlines where pairs like AV, WA, To do not collide. |
| `BUDipdbKK7Y` | 3 | supports | 0.35 | evidence found | Do not use a modal that blocks every other action until the user finishes a chore such as naming a layer. |
| `BUDipdbKK7Y` | 7 | supports | 0.35 | evidence found | Do not lock a web app to one browser or make users watch an ad to get access. |
| `BUDipdbKK7Y` | 5 | supports | 0.40 | evidence found | Do not write guilt-tripping or passive-aggressive messages about a user's progress, such as telling them they would need to run a marathon today to hit their step goal. |
| `BUDipdbKK7Y` | 10 | supports | 0.40 | evidence found | Do not punish users for breaking a streak, for example by making them guess where they were in a book. |
| `eMMiLeo_UGI` | 12 | supports | 0.46 | evidence found | Give the navigation menu hierarchy: make the sign-up action and the more important links (such as Product) stand out, for example with an outline on the most important buttons. |
| `ek-the-magic-of-clip-path` | 1 | supports | 0.48 | evidence found | Use the inset() shape for clip-path animations; inset(100%) (the article's shorthand for inset(100%, 100%, 100%, 100%)) hides the whole element and inset(0 0 0 0) shows all of it. Write the values space-separated, as the article's code does (its comma form in prose is not valid CSS [inferred]). |
| `vaul-api` | 7 | supports | 0.50 | evidence found | Render an Overlay that covers the inert part of the view while the drawer is open. |
| `referodesign-refero-skil-skills-refero-design-references-typography` | 30 | supports | 0.53 | keyword window | Keep small text at 11px minimum, with positive tracking. |
| `BUDipdbKK7Y` | 0 | supports | 0.54 | evidence found | Do not fill a site with endless pop-ups, paywalls in front of content or premium subscriptions that add nothing. |
| `BUDipdbKK7Y` | 4 | supports | 0.56 | evidence found | Do not shame users about how much they use the product (videos watched, time spent browsing), especially when the only choices offered are an upsell or continued notifications. |
| `eks-skills-prototype-picker` | 34 | supports | 0.56 | evidence found | Persist the selected variant across reloads in a 1-based URL parameter (?v=2), written with history.replaceState, falling back to variant 1. |
| `referodesign-refero-skil-skills-refero-design-references-typography` | 27 | supports | 0.56 | keyword window | Check that an interface has at most 8 font sizes, 4 text colors and 4 font weights. |
| `eks-skills-improve-animations-plan-template` | 15 | supports | 0.58 | evidence found | List the files and components the executor must not touch. |
| `d4MF6pdAZNw` | 1 | supports | 0.59 | evidence found | Put each element that will animate in into its hidden starting state (opacity 0, width 0% or max-width 0px), in CSS or with gsap.set, before the timeline runs. |
| `referodesign-refero-skil-skills-refero-design-references-example-workflow` | 3 | supports | 0.61 | evidence found | Record every design decision in a ledger with area, decision, source, the source's rule or role, and why. |
| `eks-skills-mobile-native-skill` | 30 | supports | 0.62 | evidence found | Keep pull-to-refresh (drop overscroll-behavior: none from html) when the app is a scrolling document where pull-to-refresh is welcome. |
| `referodesign-refero-skil-skills-refero-design-references-motion` | 22 | supports | 0.62 | keyword window | Do not use 300-600ms durations on hover or buttons. |
| `adev-changelog` | 0 | supports | 0.63 | evidence found | Use an ease-out curve as the default easing for most animations. Read with the rule on built-in easings, this means a custom ease-out curve rather than the built-in `ease-out` keyword [inferred]. |
| `eks-skills-emil-design-eng-skill` | 88 | supports | 0.63 | evidence found | When reviewing UI code, check for every Review Checklist issue: transition: all, scale(0) entries, ease-in on UI elements, transform-origin: center on popovers (modals exempt), animation on keyboard actions, UI durations over 300ms, hover animation without the hover/pointer media query, keyframes on rapidly triggered elements, Framer Motion x/y props under load, the same enter/exit speed, and elements all appearing at once. |
| `eks-skills-improve-animations-audit` | 41 | supports | 0.67 | evidence found | Apply rising friction at drag boundaries instead of hard stops. |
| `eks-skills-mobile-native-skill` | 48 | supports | 0.68 | evidence found | If the app switches theme with a class rather than the OS setting, update the theme-color tag from JavaScript on toggle. |
| `referodesign-refero-skil-skills-refero-design-references-color` | 0 | supports | 0.69 | evidence found | Before choosing colors, decide whether it is product UI or marketing, how data-dense it is, and whether a brand exists. |
| `palantir-workshop-applic-application-design-best-practices` | 4 | supports | 0.69 | evidence found | Limit the number of visible components to no more than ten in a single view, counting buttons, panels and widgets. |
| `adev-changelog` | 4 | supports | 0.70 | evidence found | Use each easing curve for its described use case. |
| `eks-skills-review-animations-skill` | 40 | supports | 0.74 | evidence found | Group remaining review commentary by impact tier, highest first, and omit empty tiers: feel-breaking regressions, missed simplifications, performance, interruptibility and timing, origin/physicality/cohesion, accessibility. |
| `referodesign-refero-skil-skills-refero-design-references-anti-ai-slop` | 5 | supports | 0.76 | evidence found | Do not swap one word or short phrase of a headline into a different serif, italic or color just to add 'taste'; create distinction through layout, scale, weight, media or a source-backed color role. |
| `eks-readme` | 7 | supports | 0.78 | evidence found | Describe an animation to an AI with its exact term rather than a vague description. |
| `ek-the-magic-of-clip-path` | 0 | supports | 0.79 | evidence found | Use clip-path (not width, height or extra wrapper elements) to hide and reveal parts of an element in animations, because it does not change layout. |
| `lkKGQVHrXzE` | 30 | supports | 0.79 | evidence found | Put the screenshot's outline ring on top of the image as an inset ring (gray 950 at 10% on a tinted container). |
| `eks-skills-emil-design-eng-skill` | 54 | supports | 0.79 | evidence found | For tab color transitions, duplicate the tab list, style the copy as active, clip the copy so only the active tab shows, and animate the clip on tab change. |
| `referodesign-refero-skil-skills-refero-design-references-example-workflow` | 9 | supports | 0.79 | evidence found | Give primary button treatment only to the self-serve action (Pro trial) and make Enterprise sales secondary. |
| `referodesign-refero-skil-skills-refero-design-references-typography` | 16 | supports | 0.79 | keyword window | Add letter spacing of 0.06em-0.10em to all-caps text, 0.01em-0.02em to 11-13px small text, and 0.01em-0.03em to UI labels and buttons. |
