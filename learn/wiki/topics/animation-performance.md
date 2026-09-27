---
type: topic
title: Animation performance
created: 2026-09-24
updated: 2026-09-24
sources: []
tags: []
---

# Animation performance

## Overview

Massive changes to a morphing image can slow the browser and make the animation look choppy.

## Source Mentions

- [[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]]: Massive changes to a morphing image can slow the browser and make the animation look choppy.
- [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]: Too big or flashy animations can slow a site down; a preloader can give heavy background video or 3D effects time to load.
- [[sources/adev-home-animations-dev|animations.dev]]: Choosing which properties to animate is how you keep an animation performant; performance is a Module 4 topic and there is an animation-performance skill.
- [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]: Covers perceived performance only: faster spinners and shorter animations make the app feel faster without changing load time.
- [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]: Add will-change: transform to fix shaky or jittery animations; a subtle blur under 20px can mask animations that still feel off.
- [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]: Updating an inherited CSS variable per drag frame recalculated styles for every child and lagged beyond about 20 list items; setting transform directly on the element fixed it.
- [[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]: clip-path is hardware-accelerated, does not affect layout, avoids layout shift on image reveals and needs no overflow-hidden wrapper, so it outperforms animating width or height.
- [[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]]: Seven problem-to-fix pairs: animate transform/opacity, virtualize long lists, keep animated blur under 20px, animate Motion's full transform string, avoid transition: all, write per-frame values to ref.current.style, and add will-change: transform only when a 1px shift appears.
- [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]: Never animate header height; clamp interpolations; build layout-animation builders at module scope or in useMemo; don't call JS per frame; drive keyboard UI on the UI thread.
- [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]: Only transform and opacity are free; keep motion on the UI runtime; no setState or scheduleOnRN per frame; no animated elevation or BlurView intensity; enable 120fps on ProMotion; verify on a release build on the slowest device.
- [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]: Accordion height costs layout every frame so keep it short; blur under 20px because heavy blur is expensive; set drag transforms directly; WAAPI is hardware-accelerated.
- [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]: Animate transform and opacity only; CSS animations run off the main thread; Motion's x/y/scale shorthands drop frames under load; never drive child transforms from a parent CSS variable.
- [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]: 60fps is the baseline and 120fps on newer displays; jank is visible stutter from dropped frames; animating transform and opacity lets the GPU composite motion without redoing layout or paint, will-change is a hint to promote a layer ahead of time, and animating properties like width, height, top or left causes layout thrashing.
- [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]: Animate only transform and opacity, use requestAnimationFrame, hint with will-change, keep per-frame change below the perception threshold, and use subtle motion blur or stretch for very fast motion.
- [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]: Animate only transform and opacity, avoid inherited CSS variable updates during drag, Framer Motion shorthands are main-thread, CSS animations beat JS under load, and WAAPI for programmatic control; blur under 20px.
- [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]: Animate transform and opacity only, never transition: all, use full transform strings instead of Framer Motion shorthands, avoid parent CSS variables for child transforms, keep blur under 20px, prefer CSS/WAAPI for predetermined motion.
- [[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]]: Dropped frames are HIGH severity.
- [[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]: The highlight uses will-change: transform; animating width is called a deliberate exception to the transform/opacity rule, acceptable because the element is 28px tall, absolutely positioned and has no layout dependents.
- [[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]: Variants animate only transform and opacity.
- [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]]: Only transform and opacity; layout properties, transition: all, busy-page Framer Motion shorthands and parent CSS variables driving child transforms are flagged.
- [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]: Only transform and opacity, no parent CSS variables driving child transforms, full transform strings instead of Framer Motion shorthands, CSS over JS under load, and WAAPI.
- [[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]: In SwiftUI, start animations with a withAnimation state change in the synchronous callback on the same frame as the gesture or scroll event; SwiftUI runs @Sendable closures such as visualEffect off the main thread to keep frames cheap, so copy values into their capture list.
- See also: [[synthesis/animation-performance|Animation performance synthesis]]
