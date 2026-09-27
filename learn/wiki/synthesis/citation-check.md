---
type: synthesis
title: Citation check
tags:
  - quality
---

# Citation check (Jev)

Every must/should rule in `learn/analysis/` was checked against the source passage its evidence points to. Code finds the passage; TypeSafe's Jev judges whether it supports the rule. Verdicts below 0.8 confidence, and every verdict other than *supports*, go to review. Run: `python3 tools/wiki.py cite-check`.

- Rules checked: 2025
- supports: 2024
- contradicts: 1
- unsupported: 0
- Flagged for review: 26

## Flagged

| source | rule # | verdict | confidence | how the passage was found | rule |
|---|---|---|---|---|---|
| `eMMiLeo_UGI` | 17 | contradicts | 0.29 | evidence found | Do not rely largely on images to supply the page's color. |
| `vaul-other` | 2 | supports | 0.17 | evidence found | If a drawer is non-dismissible, give it an explicit way to close [inferred]. |
| `BUDipdbKK7Y` | 6 | supports | 0.21 | evidence found | Do not pair a progress warning with a button that suggests the user change their goal. |
| `BUDipdbKK7Y` | 3 | supports | 0.35 | evidence found | Do not use a modal that blocks every other action until the user finishes a chore such as naming a layer. |
| `BUDipdbKK7Y` | 7 | supports | 0.35 | evidence found | Do not lock a web app to one browser or make users watch an ad to get access. |
| `BUDipdbKK7Y` | 5 | supports | 0.40 | evidence found | Do not write guilt-tripping or passive-aggressive messages about a user's progress, such as telling them they would need to run a marathon today to hit their step goal. |
| `BUDipdbKK7Y` | 10 | supports | 0.40 | evidence found | Do not punish users for breaking a streak, for example by making them guess where they were in a book. |
| `eMMiLeo_UGI` | 12 | supports | 0.46 | evidence found | Give the navigation menu hierarchy: make the sign-up action and the more important links (such as Product) stand out, for example with an outline on the most important buttons. |
| `ek-the-magic-of-clip-path` | 1 | supports | 0.48 | evidence found | Use the inset() shape for clip-path animations; inset(100%) (the article's shorthand for inset(100%, 100%, 100%, 100%)) hides the whole element and inset(0 0 0 0) shows all of it. Write the values space-separated, as the article's code does (its comma form in prose is not valid CSS [inferred]). |
| `vaul-api` | 7 | supports | 0.50 | evidence found | Render an Overlay that covers the inert part of the view while the drawer is open. |
| `BUDipdbKK7Y` | 0 | supports | 0.54 | evidence found | Do not fill a site with endless pop-ups, paywalls in front of content or premium subscriptions that add nothing. |
| `BUDipdbKK7Y` | 4 | supports | 0.56 | evidence found | Do not shame users about how much they use the product (videos watched, time spent browsing), especially when the only choices offered are an upsell or continued notifications. |
| `eks-skills-prototype-picker` | 34 | supports | 0.56 | evidence found | Persist the selected variant across reloads in a 1-based URL parameter (?v=2), written with history.replaceState, falling back to variant 1. |
| `eks-skills-improve-animations-plan-template` | 15 | supports | 0.58 | evidence found | List the files and components the executor must not touch. |
| `d4MF6pdAZNw` | 1 | supports | 0.59 | evidence found | Put each element that will animate in into its hidden starting state (opacity 0, width 0% or max-width 0px), in CSS or with gsap.set, before the timeline runs. |
| `eks-skills-mobile-native-skill` | 30 | supports | 0.62 | evidence found | Keep pull-to-refresh (drop overscroll-behavior: none from html) when the app is a scrolling document where pull-to-refresh is welcome. |
| `adev-changelog` | 0 | supports | 0.63 | evidence found | Use an ease-out curve as the default easing for most animations. Read with the rule on built-in easings, this means a custom ease-out curve rather than the built-in `ease-out` keyword [inferred]. |
| `eks-skills-emil-design-eng-skill` | 88 | supports | 0.63 | evidence found | When reviewing UI code, check for every Review Checklist issue: transition: all, scale(0) entries, ease-in on UI elements, transform-origin: center on popovers (modals exempt), animation on keyboard actions, UI durations over 300ms, hover animation without the hover/pointer media query, keyframes on rapidly triggered elements, Framer Motion x/y props under load, the same enter/exit speed, and elements all appearing at once. |
| `eks-skills-improve-animations-audit` | 41 | supports | 0.67 | evidence found | Apply rising friction at drag boundaries instead of hard stops. |
| `eks-skills-mobile-native-skill` | 48 | supports | 0.68 | evidence found | If the app switches theme with a class rather than the OS setting, update the theme-color tag from JavaScript on toggle. |
| `adev-changelog` | 4 | supports | 0.70 | evidence found | Use each easing curve for its described use case. |
| `eks-skills-review-animations-skill` | 40 | supports | 0.74 | evidence found | Group remaining review commentary by impact tier, highest first, and omit empty tiers: feel-breaking regressions, missed simplifications, performance, interruptibility and timing, origin/physicality/cohesion, accessibility. |
| `eks-readme` | 7 | supports | 0.78 | evidence found | Describe an animation to an AI with its exact term rather than a vague description. |
| `ek-the-magic-of-clip-path` | 0 | supports | 0.79 | evidence found | Use clip-path (not width, height or extra wrapper elements) to hide and reveal parts of an element in animations, because it does not change layout. |
| `lkKGQVHrXzE` | 30 | supports | 0.79 | evidence found | Put the screenshot's outline ring on top of the image as an inset ring (gray 950 at 10% on a tinted container). |
| `eks-skills-emil-design-eng-skill` | 54 | supports | 0.79 | evidence found | For tab color transitions, duplicate the tab list, style the copy as active, clip the copy so only the active tab shows, and animate the clip on tab change. |
