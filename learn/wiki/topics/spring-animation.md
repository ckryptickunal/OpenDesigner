---
type: topic
title: Spring animation
created: 2026-09-24
updated: 2026-09-24
sources: []
tags: []
---

# Spring animation

## Overview

Bounce in the easing curve and an elastic snap at the end of a page transition make swipes feel natural and fluid.

## Source Mentions

- [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]: Bounce in the easing curve and an elastic snap at the end of a page transition make swipes feel natural and fluid.
- [[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]: A custom spring with stiffness 550, damping 40 and default mass drives the loading spinner, the only custom spring in the flow.
- [[sources/adev-changelog-animations-dev|animations.dev]]: Hooks lessons cover useSpring and useTransform; a spring visualiser shows parameters such as mass (with decimals). Spring-driven interactive graphs are for illustrations, not functional charts.
- [[sources/adev-home-animations-dev|animations.dev]]: The course teaches when to use spring animations; the Dynamic Island walkthrough focuses on springs to make motion feel organic and natural.
- [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]: Dismiss with { duration: 300, dampingRatio: 1, velocity, overshootClamping: true }; snap back with { duration: 300, dampingRatio: 0.8, velocity }; row return with dampingRatio 1.
- [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]: Springs whenever a finger was involved, configured with duration and dampingRatio from a fixed table, velocity passed in, overshootClamping at hard edges, bounce only after momentum.
- [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]: Drag settles with { type: "spring", duration: 0.5, bounce: 0.2 } so an interrupted drag keeps its velocity.
- [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]: Springs for drag with momentum, living elements, interruptible gestures and mouse-tracking; two configs (duration 0.5/bounce 0.2, or mass 1/stiffness 100/damping 10); bounce 0.1-0.3.
- [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]: Springs are driven by stiffness, damping and mass; higher stiffness is snappier, lower damping bouncier, more mass slower; springs carry velocity into the next animation, support interruption and have a perceptual duration.
- [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]: Use springs for anything touchable, described by damping ratio and response; damping 1.0 by default, ~0.8 only after momentum; Apple's values for move (1.0/0.4), rotation (0.8/0.4) and drawer (0.8/0.3); Motion mapping bounce 0 or 0.2 with duration 0.4.
- [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]: When to use springs, useSpring for decorative mouse tracking, Apple duration+bounce config recommended over mass/stiffness/damping, subtle bounce 0.1-0.3, and velocity-preserving interruption.
- [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]: Draggable and swipeable elements that snap with no physics should use springs such as { type: "spring", duration: 0.5, bounce: 0.2 }, with bounce kept between 0.1 and 0.3; bounce otherwise belongs only to rare delight moments.
- [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]: Springs for gesture-driven motion because they carry velocity; Apple-style config { type: "spring", duration: 0.5, bounce: 0.2 } with bounce kept at 0.1-0.3.
- [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]]: Springs that retarget from current state are one of the accepted ways to make gesture-driven motion interruptible, and a polish move for 'alive' elements.
- [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]: Apple-style { duration: 0.5, bounce: 0.2 } recommended, a traditional mass/stiffness/damping alternative, subtle bounce 0.1–0.3, and useSpring for decorative mouse tracking.
- [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]: The name tag pop-up uses a custom spring of 500 milliseconds, stiffness 636 and dampening 24, which the creator says is what creates the difference between two versions of the animation; the tooltip also gets a custom easing with more bounce.
- See also: [[synthesis/spring-animation|Spring animation synthesis]]
