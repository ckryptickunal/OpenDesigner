---
type: topic
title: Drawers and sheets
created: 2026-09-24
updated: 2026-09-24
sources: []
tags: []
---

# Drawers and sheets

## Overview

A popup from the bottom is dismissed by swiping down, with buttons included, while the background zooms out and moves down when it opens.

## Source Mentions

- [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]: A popup from the bottom is dismissed by swiping down, with buttons included, while the background zooms out and moves down when it opens.
- [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]: Bottom sheets keep the user in context for side tasks such as template selection; they can be any height, carry a title, search, check and X, and zoom the background out as they open.
- [[sources/adev-home-animations-dev|animations.dev]]: Vaul, Emil's drawer library, is showcased; a walkthrough rebuilds the mobile drawer from Family's iOS app.
- [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]: Full build notes for a web drawer that feels like the iOS Sheet: anatomy, drag, scroll, background scale, snap points, keyboard and multi-touch handling.
- [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]: Use formSheet when the sheet is its own destination; otherwise a drag-to-dismiss sheet with a 40% projected threshold, clamped dismissal spring, snap-back spring with a light haptic, and a backdrop derived from the same value. Android caps detents at three.
- [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]: A sheet that is its own screen uses presentation: 'formSheet'; sheet and drawer springs use duration 300 and dampingRatio 0.8 with velocity.
- [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]: Drawer slides translateY(100%) to 0 over 500ms on the --ease-drawer curve, the way Vaul hides a drawer; dragging turns it into a gesture recipe.
- [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]: Sheets use a spring of damping 0.8 and response 0.3; flicks project to a snap point; a grabbed closing sheet follows the finger; stacked sheets progressively dim and push back their parents.
- [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]: iOS-like drawer curve, translateY(100%) hiding, 200-500ms duration, damping and friction when dragging past the top, and avoiding inherited CSS variables during swipe.
- [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]: Sheets are dismissable surfaces that must exit the way they entered, using percentage translations; modals and drawers get 200-500ms, and --ease-drawer is cubic-bezier(0.32, 0.72, 0, 1).
- [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]: An iOS-like drawer curve cubic-bezier(0.32, 0.72, 0, 1) and a 200-500ms duration band for modals and drawers.
- [[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]: Sheet content uses overscroll-behavior: contain, sheets pad the bottom with calc(1rem + env(safe-area-inset-bottom)), drag-to-dismiss surfaces use touch-action: none, and a vertical sheet handle uses pan-x.
- [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]: Modals and drawers get 200–500ms, an iOS-like drawer curve, percentage translates as in Vaul, and real-device testing for drawer gestures.
- [[sources/vaul-api-api-reference-vaul|API Reference – Vaul]]: Full anatomy of a drawer component and the default behaviour of each prop: modal, dismissible, bottom direction, drag from anywhere, input repositioning.
- [[sources/vaul-default-default-vaul|Default – Vaul]]: Variants of a drawer: default bottom, side (right or left), nested, scrollable like Apple's Sheet, and controlled.
- [[sources/vaul-getting-started-getting-started-vaul|Getting Started – Vaul]]: The smallest working drawer: a trigger, a dimmed overlay and bottom-pinned content.
- [[sources/vaul-inputs-inputs-vaul|Inputs – Vaul]]: Vaul corrects the drawer's position when the keyboard opens; repositionInputs false turns this off.
- [[sources/vaul-other-other-vaul|Other – Vaul]]: Non-modal and non-dismissible drawers, plus a recreation of the Family drawer.
- [[sources/vaul-snap-points-snap-points-vaul|Snap Points – Vaul]]: Snap points let a drawer rest partially open; options for background interaction, sequential snapping and where fading starts.
- See also: [[synthesis/drawers-and-sheets|Drawers and sheets synthesis]]
