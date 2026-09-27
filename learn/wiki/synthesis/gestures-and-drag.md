---
type: synthesis
title: Gestures and drag
created: 2026-09-24
updated: 2026-09-28
sources:
  - ek-building-a-drawer-component
  - ek-building-a-toast-component
  - ek-the-magic-of-clip-path
  - ek-you-dont-need-animations
  - eks-skills-animate-expo-recipes
  - eks-skills-animate-expo-skill
  - eks-skills-animate-recipes
  - eks-skills-animate-skill
  - eks-skills-animation-vocabulary-skill
  - eks-skills-apple-design-skill
  - eks-skills-ask-sonner-api
  - eks-skills-ask-sonner-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-audit
  - eks-skills-mobile-native-skill
  - eks-skills-pick-ui-library-skill
  - eks-skills-review-animations-standards
  - 14h1VnkQvIc
  - Gfsd8NNuD9g
  - Ksx9C2-3yMo
  - P2ksReDwWkE
  - Vy0KKvZJRH8
  - goWOAFqJHpA
  - ixUq4HM4FNg
  - ld1zhQMXxXU
  - sonner-home
  - sonner-other
  - sonner-toaster
  - vaul-api
  - vaul-snap-points
tags:
  - od-area-motion
---
# Gestures and drag

## In short

A gesture is motion the person drives with a finger or a pointer, so the interface has to follow it exactly and react to how fast it was moving. Drag things one-to-one from the point where they were grabbed. When the finger lets go, decide what happens from its speed and where the motion would come to rest, not from distance alone, and settle with a spring. At an edge, add growing resistance instead of a hard stop. Gestures are invisible, so important ones need a visible alternative such as a button, and people may need to be taught them first.

## House standards

- `STD-springs-gestures-01`: anything a finger drives or can interrupt runs on a spring.
- `STD-springs-gestures-26`: a drag, slider, drawer or sheet follows the pointer 1:1 for the whole interaction, glued at the offset where it was grabbed.
- `STD-springs-gestures-28`: capture the pointer once a drag starts, so the drag continues outside the element.
- `STD-springs-gestures-30`: a drag takes over after about 10px along its axis, and a pan inside a scroll view declares its axis.
- `STD-springs-gestures-18` and `STD-springs-gestures-17`: record recent pointer positions and times, and hand the release velocity to the spring.
- `STD-springs-gestures-19` and `STD-springs-gestures-20`: on release, project where the flick would come to rest and decide from that point; the sign of the velocity decides commit or reverse.
- `STD-springs-gestures-21`: dismiss when the distance passes the threshold or the velocity passes about 0.11 (px per ms); never require distance alone.
- `STD-springs-gestures-22`: a draggable sheet dismisses when its projected position passes 40% of its height.
- `STD-springs-gestures-24`: when every snap point matters, disable velocity-based snapping (Vaul `snapToSequentialPoint`).
- `STD-springs-gestures-25`: past a boundary, the element follows with rising resistance (rubber band constant 0.55), never a dead stop.
- `STD-springs-gestures-12`, `STD-springs-gestures-14` and `STD-springs-gestures-16`: anything moving can be grabbed mid-flight, starting from its live on-screen value and carrying its velocity.
- `STD-springs-gestures-34`: everything that follows a drag (backdrop opacity, background scale and radius) derives from the same drag value.
- `STD-springs-gestures-39` and `STD-springs-gestures-41`: recognize gestures continuously and in parallel, and remove latency from the input path.
- `STD-enter-exit-origin-06`: an element leaves the way it came in, and its swipe-to-dismiss direction matches.
- `STD-components-toasts-drawers-18` and `STD-components-toasts-drawers-44`: toasts and drawers can be swiped away on touch and desktop; a scrollable drawer drags only from its scroll top, with a 100ms block after scrolling reaches the top.
- `STD-mobile-touch-18`, `STD-mobile-touch-19` and `STD-mobile-touch-28`: set `touch-action` per gesture surface, prefer native scroll-snap carousels, and ignore extra fingers during a drag.
- `STD-mobile-touch-33`: in React Native, build gestures with Gesture Handler, never PanResponder.
- `STD-performance-properties-11`: during a drag, set the transform directly on the moving element.
- `STD-process-review-taste-33`: judge touch and gesture motion on real hardware.

## What the sources teach

### Follow the finger exactly

- Touch and content should move together: 1:1 tracking with pointer capture and the grab offset, a history of recent velocities, about 10px of hysteresis before a drag commits, and all plausible gestures tracked in parallel until intent is clear [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- Sonner's toast captures the pointer so the drag keeps working when the pointer leaves the toast [S-L19-006] [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]. Drag transforms are set directly on the element [S-L19-017] [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]. A before-and-after slider moves the top image's clip-path inset with the drag position [S-L19-010] [[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]].

### Let go: speed and momentum decide

- A toast is removed when the swipe passes a threshold or its velocity is higher than 0.11 [S-L19-006] [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]. A drawer can simply be flicked closed instead of dragged to a point [S-L19-005] [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]].
- Apple-style momentum projection uses a deceleration rate of 0.998 for a normal feel or 0.99 for snappier, and the sign of the velocity decides commit or reverse [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]. The Expo recipes capture context when the pan starts, project momentum for commit decisions and hand the velocity to springs [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]] [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]].
- Snap points in a drawer are momentum-aware [S-L19-005] [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]. In Vaul, velocity-based snapping can skip a point on a fast drag; `snapToSequentialPoint` prevents that when every point matters [S-L19-098] [[sources/vaul-snap-points-snap-points-vaul|Snap Points – Vaul]].

### Edges: friction, not walls

- Dragging a toast the wrong way does not stop dead; it slows down and eventually stops [S-L19-006] [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]. Dragging a drawer upward when it is already at the top damps the drag, so the more you drag, the less it moves [S-L19-005] [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]].
- Rubber-banding with a constant of 0.55 is Apple's formula for going past a boundary [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]], and the vocabulary skill names the effect [S-L19-019] [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]. Hard stops at drag boundaries are flagged in audits and opportunity searches [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]] [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]].

### Gestures that share the screen with scroll and other fingers

- A scrollable drawer only drags when its content is at the top, and dragging is blocked for 100ms after scrolling reaches the top, so a fast scroll does not close it by accident; a second finger is ignored so the drawer does not jump [S-L19-005] [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]].
- Multi-touch protection appears in the drag recipes and review standards [S-L19-017] [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]] [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]].
- `touch-action` tells the browser which axes an element owns (pan-y, pan-x, none, manipulation), and native scroll-snap beats a hand-rolled spring for carousels [S-L19-028] [[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]].
- React Native gestures use `Gesture.Pan()` with declared axes instead of PanResponder, and treat interruptibility and velocity handoff as the baseline [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]] [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]].

### Direction and dismissal

- A toast that enters and leaves in the same direction makes swipe-down-to-dismiss feel intuitive [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]; exits mirror entrances so the dismiss gesture is obvious [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]].
- In Sonner, swipe directions follow the toaster's position by default and can be overridden with `swipeDirections`; a swipe fires `onDismiss`, like the close button [S-L19-092] [[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]] [S-L19-088] [[sources/sonner-home-sonner|Sonner]] [S-L19-089] [[sources/sonner-other-other-sonner|Other – Sonner]] [S-L19-021] [[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]] [S-L19-022] [[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]].
- Vaul has an optional handle; `handleOnly` defaults to false, which by its name decides whether only the handle starts a drag [inferred] [S-L19-093] [[sources/vaul-api-api-reference-vaul|API Reference – Vaul]].

### Tools and testing

- dnd kit is the pick for drag and drop, and Motion when gesture-driven values are needed [S-L19-029] [[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]. Gestures are tested on real devices [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]].

### What the practitioner videos add

- Mobile swipes fall into three kinds: navigating within a page, between pages, and gestures that replace buttons. Swipe to dismiss popovers and sheets but keep a close button; use swipe-to-confirm sliders for high-impact or irreversible actions such as sending an email or buying crypto; let a swipe replace a button once people know it, with a fallback [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]].
- Swipe right to go back with the background starting about 35% to the left; zoom the background out as a bottom sheet rises; swipe up to open search; teach a swipe before relying on it [S-L19-053] [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]].
- Apple Reminders reveals secondary actions on a left or right swipe while checking off an item stays the primary action [S-L19-056] [[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]].
- Horizontal card carousels should be draggable with the mouse instead of relying on small buttons [S-L19-060] [[sources/P2ksReDwWkE-website-layouts-to-make-a-professional-website-design-in-2024|Website Layouts To Make A Professional Website Design in 2024]]. On macOS, dragging content into and out of an app (to Figma or Finder) is a must [S-L19-067] [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]].
- Rely on gestures people already know: tap to pause as on every social platform, scroll instead of clicking through slides, swipe through months [S-L19-076] [[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]. TikTok's swipe up works because the target is almost the whole screen, the thumb barely moves and no decision is needed [S-L19-077] [[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok’s UX is so GOOD it should be ILLEGAL (seriously)]].
- In a swipeable card stack, the dragged card rotates away and fades to 0% while the cards behind scale up and shift down to fill its place [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]].

## Where they agree and disagree

- **Fallbacks for invisible gestures.** The videos' advice to pair a swipe with a visible button [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]] and to teach swipes first [S-L19-053] [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]] agrees with DC-L10-15, which cites WCAG 2.5.7's requirement for a non-drag alternative, and with `STD-accessibility-motion-24`, which keeps drawers dismissible by outside click and Escape as well as drag [inferred link]. DC-L19-97 makes it the default that every gesture has a visible button or menu doing the same job.
- **Guarding risky actions.** The swipe-to-confirm slider [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]] and the house hold-to-confirm (`STD-components-toasts-drawers-77`) both slow down an irreversible action; the mechanism differs. Swipe-to-confirm comes from one video, so it is practitioner opinion.
- **Swipe back.** The 35% background offset [S-L19-053] [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]] is a single-video number. On iOS and Android the house keeps screen transitions and back gestures native (`STD-mobile-touch-42`, `STD-mobile-touch-44`), and DC-L10-14 documents Android's predictive back and iOS swipe-back, so the number only matters for custom or web builds [inferred].
- **Card stack.** Rotating and fading the dragged card while the stack moves up [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]] uses only transform and opacity and points toward the outcome, which fits `STD-performance-properties-01` and `STD-springs-gestures-42` [inferred].
- **Interruptibility.** DC-L04-24 (let people cancel motion; springs keep velocity) agrees with `STD-springs-gestures-12` and `STD-springs-gestures-16`; on blocking input, `STD-springs-gestures-13` now supersedes it.
- **Overlays on phones.** DC-L08-20 defaults to bottom sheets on phones, in line with `STD-components-toasts-drawers-37` (prefer drawers over modals on mobile).
- **Release physics in OpenDesigner.** The older questions and Decision Cards said nothing about release physics. The house standards now write them as tokens: `motion.gesture.dismiss-velocity` 0.11, `motion.gesture.sheet-dismiss-fraction` 0.4, `motion.gesture.rubberband-constant` 0.55, `motion.gesture.deceleration-rate` 0.998, `motion.gesture.direction-threshold` 10px and `motion.gesture.drag-lock-after-scroll` 100ms. DC-L19-97 locks the momentum model and keeps sequential snap points for flows where every point matters.

## Decisions this informs

- **Q-plat-03** (how people touch or press): touch input brings the gesture standards and touch-action rules, alongside the target sizes in DC-L10-15.
- **Q-pattern-01** (dialog, sheet or popover): sheets need drag-to-dismiss with projection (40% of height), rubber-banding upward, and sequential snap points when every point matters.
- **Q-motion-04** (how springs are set up): settled by `STD-springs-gestures-02` and `STD-springs-gestures-04`; gesture-driven UI rules out `durations-only`, which is marked as breaking `STD-springs-gestures-01`.
- **Q-motion-09** (system versus brand motion on iOS and Android): back gestures and screen transitions stay with the OS; `one-language` is marked as breaking `STD-mobile-touch-42`.
- **Q-form-04** (where messages like "Saved" appear): toasts that appear must be swipeable along their position.
- **Q-state-06** (risky actions): a hold-to-confirm or swipe-to-confirm control is one way to guard an irreversible action, alongside the danger styling this question covers [inferred].

## Visual examples worth showing

- Sonner's toast: swipe down to dismiss with a flick, and drag it up to feel the friction [S-L19-006] [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]].
- A drawer: a slow drag that returns, a fast flick that closes, and a damped pull past the top [S-L19-005] [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]].
- A momentum projection diagram: release point, projected rest point, and the snap target chosen from it [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- Vaul snap points with and without `snapToSequentialPoint` [S-L19-098] [[sources/vaul-snap-points-snap-points-vaul|Snap Points – Vaul]].
- A swipe-to-confirm slider next to a button, to show how much harder it is to trigger by accident [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]].
- The swipe-back transition with the background moving in from about 35% [S-L19-053] [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]].
- The card stack: the top card rotating away while the others scale up [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]].
- A clip-path before-and-after slider [S-L19-010] [[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]].

## Open questions

- Toasts use a velocity threshold (0.11) and sheets a projected position (40% of height). The standards now export both as plain number tokens, since DTCG has no gesture or spring type (DC-L04-22). Should toasts and sheets share one gesture model, and do the Swift and Compose exports need these values in a native form?
- Should a swipe-to-confirm control join hold-to-confirm as an approved pattern for irreversible actions? Only one video supports it.
- How should OpenDesigner check that every gesture has a non-drag alternative (WCAG 2.5.7 via DC-L10-15)? DC-L19-97 makes it the default, but no L19 source states it as a rule.
