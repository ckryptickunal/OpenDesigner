---
type: topic
title: Gestures and drag
created: 2026-09-24
updated: 2026-09-24
sources: []
tags: []
---

# Gestures and drag

## Overview

Groups mobile swipes into within-page, between-page and gesture types; recommends swipe-to-dismiss, swipe-to-confirm for risky actions, and swipes that replace a button once users learn them.

## Source Mentions

- [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]: Groups mobile swipes into within-page, between-page and gesture types; recommends swipe-to-dismiss, swipe-to-confirm for risky actions, and swipes that replace a button once users learn them.
- [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]: Swipe right to go back with the background shifting about 35%, swipe down to close sheets, swipe up to search, and long press as the mobile right click; teach users the swipes before relying on them.
- [[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]: Apple Reminders reveals secondary actions on swipe left and right, keeping the main action (checking off a reminder) primary.
- [[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]]: A horizontal card carousel would be better if the cards were draggable with the mouse instead of only using small buttons.
- [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]: Drag and drop of anything anywhere is a must: drop content into the quick-save window and drag content out to Figma, Finder or elsewhere.
- [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]: Momentum-based dismissal, damping past the top, a shouldDrag rule tied to scroll position, a 100ms post-scroll block, ignoring extra touches, and momentum-aware snap points.
- [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]: Swipe down to dismiss, momentum-based with a velocity threshold of 0.11, pointer capture during drag, and friction when dragging the wrong way.
- [[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]: A before/after slider adjusts the top image's inset from the drag position.
- [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]: Matching enter and exit direction to the dismiss direction makes a swipe-to-dismiss gesture feel intuitive.
- [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]: Pan gestures with declared axes, context captured on start, momentum projection for commit decisions, velocity handed to springs, rubber-banding past edges, gestures memoized.
- [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]: Gesture.Pan() instead of PanResponder, interruptibility and velocity handoff as baseline, velocity-or-distance dismissal and rubber-band resistance at boundaries.
- [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]: Drag-to-dismiss dismisses on distance or velocity > 0.11, sets transform directly, uses pointer capture, multi-touch protection, damping and friction, and settles with a spring.
- [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]: Gestures use springs because they carry velocity through interruptions; exits mirror entrances so swipe-to-dismiss feels obvious.
- [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]: Defines drag with momentum, drag to reorder where other items shift to make room, swipe to dismiss for drawers and toasts, and rubber-banding past a boundary.
- [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]: 1:1 tracking with pointer capture and grab offset, velocity history, velocity handoff, momentum projection with deceleration rate 0.998 or 0.99, rubber-banding with constant 0.55, ~10px hysteresis, parallel gesture detection and commit-or-reverse by velocity sign.
- [[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]: Swipe-to-dismiss directions default to ones based on position and can be overridden with swipeDirections; onDismiss fires when a toast is swiped away.
- [[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]: Swipe-to-dismiss directions derive from position and are overridden with swipeDirections; swipes fire onDismiss.
- [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]: Velocity-based dismissal above ~0.11, damping and friction at boundaries, pointer capture, multi-touch protection, and testing gestures on real devices.
- [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]: Drag seams get springs, velocity-based dismissal (Math.abs(distance)/elapsedMs > ~0.11) and rubber-banding at boundaries instead of hard stops.
- [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]: Velocity-based dismissal (Math.abs(distance)/elapsedMs > ~0.11) and rising friction at drag boundaries instead of hard stops.
- [[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]: touch-action tells the browser which axes an element owns (pan-y, pan-x, none, manipulation); native scroll-snap beats a hand-rolled spring for carousels.
- [[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]: dnd kit is the pick for drag and drop; motion is the pick when gesture-driven values are needed.
- [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]: Velocity-based momentum dismissal, damping at boundaries, pointer capture, multi-touch protection, and friction over hard stops.
- [[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]: Rely on the tap-to-pause gesture people know from every social media platform instead of a pause button, scroll instead of clicking through slides, and let people swipe through each month.
- [[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok’s UX is so GOOD it should be ILLEGAL (seriously)]]: The swipe up is the core interaction: a near full-screen target, almost zero thumb travel, and no decision required.
- [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]: A dragged card rotates out and fades to 0% opacity while the cards behind scale up and shift down to fill its place, which makes the stack feel like it moves forward.
- [[sources/sonner-home-sonner|Sonner]]: Notes that the swipe direction for dismissing a toast depends on the toaster's position.
- [[sources/sonner-other-other-sonner|Other – Sonner]]: Swiping a toast dismisses it and fires onDismiss, like clicking the close button.
- [[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]: Swipe directions default to being based on the position and can be set with swipeDirections.
- [[sources/vaul-api-api-reference-vaul|API Reference – Vaul]]: An optional Handle drags the drawer; handleOnly defaults to false, which by its name decides whether only the handle starts a drag [inferred].
- [[sources/vaul-snap-points-snap-points-vaul|Snap Points – Vaul]]: Velocity-based snapping can skip points on a fast drag; snapToSequentialPoint prevents that.
- See also: [[synthesis/gestures-and-drag|Gestures and drag synthesis]]
