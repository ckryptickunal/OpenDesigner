---
type: synthesis
title: Spring animation
created: 2026-09-24
updated: 2026-09-28
sources:
  - adev-changelog
  - adev-home
  - eks-skills-animate-expo-recipes
  - eks-skills-animate-expo-skill
  - eks-skills-animate-recipes
  - eks-skills-animate-skill
  - eks-skills-animation-vocabulary-skill
  - eks-skills-apple-design-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-audit
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
  - 14h1VnkQvIc
  - NtZeYmTMuo4
  - ld1zhQMXxXU
tags:
  - od-area-motion
---
# Spring animation

## In short

A spring moves things the way a physical object would. Instead of running for a fixed time, it settles according to how stiff and how damped it is, and it can take over the speed of a moving finger. That makes springs the right tool for anything a person drags, flicks or might grab halfway. The house default is a spring that does not bounce; a small bounce (0.1 to 0.3) is kept for motion that follows a flick or throw, and for deliberately playful moments. Designers should describe a spring by its damping and response rather than by raw physics numbers.

## House standards

- `STD-springs-gestures-01`: drags, flicks, swipes and anything the user can interrupt or reverse run on a spring; motion no finger started or can interrupt runs on an easing curve and a duration.
- `STD-springs-gestures-02`: specify each spring by damping ratio (or bounce) and response (or perceptual duration), not mass, stiffness and damping, and never treat response as a fixed duration.
- `STD-springs-gestures-04`: the default UI spring is critically damped (damping 1.0, no overshoot) with a response of 0.3-0.4s; moves and repositions use 1.0 and 0.4s.
- `STD-springs-gestures-05`: no overshoot on UI that appears or moves without a gesture behind it (menus, popovers, dialogs, plain repositions).
- `STD-springs-gestures-06`: a released drag settles with a slightly under-damped spring (about 0.8, bounce 0.2) started from the release velocity.
- `STD-springs-gestures-07`: when a spring bounces, bounce stays between 0.1 and 0.3, reserved for drag-to-dismiss and playful interactions.
- `STD-springs-gestures-08` and `STD-springs-gestures-09`: sheets and drawers use damping 0.8 and response 0.3s (dismissal stays critically damped); rotating elements use 0.8 and 0.4s.
- `STD-springs-gestures-10`: any spring that must not pass a hard edge is clamped (`overshootClamping: true`).
- `STD-springs-gestures-11`: two-dimensional motion uses two independent springs, one for X and one for Y.
- `STD-springs-gestures-14`, `STD-springs-gestures-16` and `STD-springs-gestures-17`: start from the live on-screen value, carry velocity through a reversal, and hand the release velocity to the spring.
- `STD-springs-gestures-45`: decorative mouse tracking goes through a spring (`useSpring`) instead of following the pointer directly.
- `STD-mobile-touch-51`: Reanimated springs use `duration` and `dampingRatio`, never mass, stiffness and damping.
- `STD-performance-properties-15`: springs and other dynamic, interruptible motion run in JavaScript; predetermined motion stays in CSS or WAAPI.

## What the sources teach

### When to reach for a spring

- Use springs for anything touchable: if a finger drives it, it is a spring [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]] [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]. The web skill lists drag with momentum, elements that should feel alive, interruptible gestures and decorative mouse tracking [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]].
- Draggable or swipeable elements that snap into place with no physics are a missed opportunity for a spring [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]] [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]. Springs that retarget from their current state are one accepted way to make gesture-driven motion interruptible, and a polish move for elements meant to feel alive [S-L19-032] [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]].
- The course teaches when to use springs and uses a Dynamic Island walkthrough to make motion feel organic [S-L19-002] [[sources/adev-home-animations-dev|animations.dev]].

### Why springs feel different

- Springs are driven by stiffness (higher is snappier), damping (lower is bouncier) and mass (more is slower); they carry velocity into the next animation, can be interrupted, and have a perceptual rather than a fixed duration [S-L19-019] [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]].
- A drag that settles with a spring keeps its velocity when it is interrupted [S-L19-017] [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]].

### How to describe a spring

- Emil recommends Apple's duration-and-bounce form over mass, stiffness and damping because it is easier to reason about [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]. The web skill gives both forms: `{ type: "spring", duration: 0.5, bounce: 0.2 }` (Apple-style) and `{ type: "spring", mass: 1, stiffness: 100, damping: 10 }` (traditional physics, more control) [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]].
- The Apple design skill describes springs by damping ratio and response, and warns that response is not a duration [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]. In Expo apps, springs take `duration` and `dampingRatio` from a fixed table, get the gesture's velocity, and are clamped at hard edges [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]].
- The course's spring lesson has a visualiser that now accepts decimals for mass [S-L19-001] [[sources/adev-changelog-animations-dev|animations.dev]].

### The values

- Damping 1.0 by default; about 0.8 only after a gesture with momentum. Apple's values: move or reposition 1.0 and 0.4s, rotation 0.8 and 0.4s, drawer or sheet 0.8 and 0.3s; in Motion that maps to bounce 0 or 0.2 with duration 0.4 [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- Expo recipes: dismiss a sheet with `{ duration: 300, dampingRatio: 1, velocity, overshootClamping: true }`, snap it back with `{ duration: 300, dampingRatio: 0.8, velocity }`, and return a swiped row with damping 1 [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]].
- Keep bounce at 0.1-0.3 and out of most UI [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]] [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]. Beyond draggable elements, bounce belongs only to rare delight moments [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]].

### Decorative springs

- Decorative mouse tracking goes through `useSpring` [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]. The course's `useSpring` lessons build an interactive, spring-driven graph and say this kind of interaction is meant for illustrations, not functional charts such as stock charts [S-L19-001] [[sources/adev-changelog-animations-dev|animations.dev]].

### What the practitioner videos add

- Opening up the easing curve for more bounce makes swiped cards carry momentum, and an elastic snap finishes a swipe-up page transition [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]].
- Figma prototypes use custom springs: a loading spinner faked from frames uses stiffness 550 and damping 40 with default mass, the only custom spring in that flow [S-L19-059] [[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]. A hover name tag uses a 500ms custom spring with stiffness 636 and damping 24, which the creator says makes the difference between two versions; the delayed tooltip also gets a custom easing "with a bit more bounce" [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]].

## Where they agree and disagree

- **Bounce after a swipe.** The video's bouncy swiped cards [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]] match the house rule that bounce follows a gesture that carried momentum (`STD-springs-gestures-05`, `STD-springs-gestures-06`).
- **Bounce without a gesture.** The springy hover name tag and the bouncier tooltip [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]] are pop-ups with no gesture behind them, which `STD-springs-gestures-05` says must not overshoot unless the moment is deliberately playful (see Open questions); tooltips get 125ms at scale 0.97 in the house recipes (`STD-enter-exit-origin-09`). Assuming Figma's default mass of 1, stiffness 636 with damping 24 gives a damping ratio of about 0.48 [inferred], so a bounce of about 0.5 by the conversion OpenDesigner uses in `synthesis/levers.json` (bounce = 1 − damping ratio), well past the 0.1-0.3 range. The spinner spring (550 and 40) works out to about 0.85 [inferred]. The house would drive a real spinner with linear, fast rotation (`STD-easing-duration-01`, `STD-easing-duration-15`); the spring is a Figma workaround for a spinning frame sequence [inferred]. These values come from single videos and are practitioner opinion.
- **How springs are specified.** DC-L04-22 recommended storing springs as damping ratio plus stiffness (Material's form) with a derived duration and bounce for Apple. `STD-springs-gestures-02` now supersedes it and, with `STD-springs-gestures-04`, settles Q-motion-04, which the interview therefore skips. DC-L19-190 carries the house form into storage: damping ratio and response as the stored values, with stiffness derived for Compose and a sampled `linear()` curve for CSS. The Q-motion-04 stage default still names damping ratio and stiffness.
- **Which motion may overshoot.** DC-L04-22 kept under-damped springs for "spatial hero motion", and Q-motion-04's `spatial-effects` option lets moves overshoot; that option is now marked as breaking `STD-springs-gestures-04` and `STD-springs-gestures-05`, and `apple-bounce` (bounce steps of 0.15 and 0.3) as breaking `STD-springs-gestures-04`. The energy dial still makes every spatial spring under-damped above energy 33, but standards.json records that the lock in `STD-springs-gestures-04` (damping 1.0, stiffness 246.7 for a 0.4s response) replaces it in every project unless the person overrides the standard.
- **Bounce ceiling.** DC-L04-19 keeps bounce at or below 0.2 except for playful brands, close to the house 0.1-0.3 range for momentum settles (`STD-springs-gestures-07`). Its placement of bold moments is now superseded by `STD-when-to-animate-09` (delight only on rare moments).
- **Interruptibility.** DC-L04-22 and DC-L04-24 note that springs keep their velocity when interrupted, which agrees with `STD-springs-gestures-12` and `STD-springs-gestures-16`. On blocking input, `STD-springs-gestures-13` now supersedes DC-L04-24: never, rather than for up to about 100ms.
- **Momentum and sheet springs.** The standards add `motion.spring.momentum` (damping 0.8) and `motion.spring.sheet` (damping 0.8, response 0.3s) tokens, but standards.json records that no generated transition points released drags or sheets at them; the engine's label still sends sheets to the generic spatial spring (`STD-springs-gestures-06`, `STD-springs-gestures-08`).
- **Platforms.** DC-L10-14's split (the OS owns screen transitions, brand springs live inside content) agrees with the native-stack standards (`STD-mobile-touch-42`) on screens. Its "as springs" for all in-content brand motion goes further than `STD-springs-gestures-01`, which puts motion no finger drives on timing curves.

## Decisions this informs

- **Q-motion-04** (how springs are set up): settled by `STD-springs-gestures-02` and `STD-springs-gestures-04`, so the interview skips it. Every option is marked as breaking a standard: `durations-only` cannot serve gesture-driven UI (`STD-springs-gestures-01`), `spatial-effects` lets plain moves overshoot (`STD-springs-gestures-04`, `STD-springs-gestures-05`), and `apple-bounce` offers bounce 0.15 and 0.3 as presets (`STD-springs-gestures-04`). The house form is damping ratio and response, critically damped by default.
- **Q-motion-01** (motion feel): the house answer is neither springs everywhere nor no springs, but springs for anything a finger drives (and for decorative mouse tracking, `STD-springs-gestures-45`) and timing curves for everything else; the `springs` option (springs throughout) is marked as breaking `STD-springs-gestures-01`.
- **Q-motion-09** (system versus brand motion on iOS and Android): brand motion inside content, on springs only where a finger drives it; platform transitions for screens (its `one-language` option is marked as breaking `STD-mobile-touch-42`).
- **Q-pattern-01** (dialog, sheet or popover): a draggable sheet settles with 0.8 and 0.3s and dismisses critically damped and clamped.
- **Q-brand-04** (liveliness): only a playful product earns extra bounce, and still within 0.1-0.3.

## Visual examples worth showing

- One drag released three ways: critically damped (1.0), momentum settle (0.8), and an over-bouncy spring (about 0.5), with the release velocity carried in [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- Apple's spring table as cards: move, rotation, drawer [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- A sheet dismissed with a clamped spring next to one that snaps back with a slight bounce [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]].
- Swiped cards with a rigid curve and with a bouncier curve that carries momentum [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]].
- The course's interactive spring-driven graph, labelled as an illustration and not a chart [S-L19-001] [[sources/adev-changelog-animations-dev|animations.dev]].
- The springy name-tag hover [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]], shown as a counter-example for pop-ups that have no gesture behind them.

## Open questions

- The traditional config (mass 1, stiffness 100, damping 10) [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]] [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]] and the mouse-tracking example with the same stiffness and damping [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] work out to a damping ratio of about 0.5 [inferred], bouncier than the 0.1-0.3 range the same sources recommend. Is that intended for decorative tracking only?
- DTCG has no spring type (DC-L04-22). DC-L19-190 proposes storing damping ratio and response; does that encoding survive to CSS, Motion, Reanimated and SwiftUI without loss?
- On the web, springs need a JavaScript library or a sampled CSS `linear()` curve (DC-L04-22). When is a sampled `linear()` spring good enough, given that it cannot take a release velocity [inferred]?
- `STD-springs-gestures-07` allows bounce in "playful interactions". Does a playful hover pop-up count, or only gesture-driven ones?
- Should the engine point sheets and released drags at the new sheet and momentum springs instead of the generic spatial spring?
