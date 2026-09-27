---
type: topic
title: Toasts and notifications
created: 2026-09-24
updated: 2026-09-24
sources: []
tags: []
---

# Toasts and notifications

## Overview

Vercel notifies users of build status immediately after a deploy, so they never have to guess whether it worked.

## Source Mentions

- [[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]: Vercel notifies users of build status immediately after a deploy, so they never have to guess whether it worked.
- [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]: Toasts are the notification system of a dashboard: confirm changes made in a modal, raise awareness without taking over the screen, prompt action, and surface warning and error states.
- [[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]: A recurring YouTube notification about watch time that only stops if you subscribe to Premium is used as an annoying example.
- [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]: After saving, the quick-save window collapses into a toast notification and slides off the screen.
- [[sources/adev-changelog-animations-dev|animations.dev]]: A toast component is built with CSS transforms and transitions in the CSS module.
- [[sources/adev-home-animations-dev|animations.dev]]: Sonner, Emil's toast library, is showcased, and a toast is built in the CSS module.
- [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]: Full anatomy of the Sonner toast: enter transition, stacked pile with depth, hover-to-expand, optional always-expanded mode, swipe to dismiss, 4-second default timer that pauses on hover and on hidden tabs.
- [[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]]: A toast animation is the example for choosing the right easing.
- [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]: Sonner animates toasts in because a sudden appearance feels off, and enters and exits in the same direction so swipe-down-to-dismiss feels intuitive.
- [[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]]: A toast component should come from a trusted library such as Sonner rather than be hand-rolled by AI [inferred].
- [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]: Toasts enter with FadeInDown 300ms and exit with FadeOutDown 250ms, both ease-out, positioned above the safe-area inset, and exit the way they entered.
- [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]: Toast enters from translateY(100%) over 400ms with plain ease via @starting-style (mount-flag fallback); stacked reflow needs opacity balanced against height by feel.
- [[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]: Full prop and option list for a toast system, with defaults for count, placement, offsets, gap, duration, dismissal, actions and callbacks.
- [[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]: Complete guide to wiring, calling, updating, persisting, dismissing, styling and debugging toasts.
- [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]: Toasts enter and exit from the same direction, use transitions rather than keyframes, pause timers when the tab is hidden, fill stack gaps to keep hover, and Sonner's slower ease-based motion.
- [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]: Toasts should enter and exit by the same edge using translateY(100%) percentages; the worked example enters via @starting-style from opacity 0 and translateY(100%) with a 400ms ease transition.
- [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]: Stacking toasts are rapidly triggered UI and must use transitions or springs, not @keyframes.
- [[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]: Sonner is the pick for toasts; building toasts by hand or with a modal library is a mismatch to catch.
- [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]]: Toasts are named as rapidly triggered UI that must not use keyframes and must be interruptible.
- [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]: Toasts use interruptible transitions and @starting-style entry; Sonner positions toasts with percentage translates and uses slightly slower ease for elegance.
- [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]: Beyond the obvious slide-up, toasts can carry loading animations and celebratory success messages with particles; Vercel's are good and Linear's are preferred. A swipeable card stack can act as a notification center in the bottom right.
- [[sources/sonner-getting-started-getting-started-sonner|Getting Started – Sonner]]: How to install Sonner, mount the Toaster and render a first toast.
- [[sources/sonner-home-sonner|Sonner]]: Lists Sonner's toast types, positions, expand behaviour, rich colors, close button and headless mode.
- [[sources/sonner-other-other-sonner|Other – Sonner]]: Covers updating, dismissing, persisting and reading toasts, close callbacks, custom elements, and Astro and shadow DOM integration.
- [[sources/sonner-styling-styling-sonner|Styling – Sonner]]: How to restyle Sonner toasts: headless, global styles, per-element classNames, unstyled and icon changes.
- [[sources/sonner-toast-toast-sonner|Toast – Sonner]]: Documents every toast variant (success, error, action, cancel, promise, loading, custom, headless) and the per-toast API defaults.
- [[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]: Documents the Toaster container: expand on hover, visible count, positions, multiple toasters, offsets, theme and all container defaults.
- See also: [[synthesis/toasts-and-notifications|Toasts and notifications synthesis]]
