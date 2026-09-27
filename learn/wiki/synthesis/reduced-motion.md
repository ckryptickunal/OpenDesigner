---
type: synthesis
title: Reduced motion
created: 2026-09-24
updated: 2026-09-24
sources:
  - eks-skills-animate-expo-recipes
  - eks-skills-animate-expo-skill
  - eks-skills-animate-skill
  - eks-skills-animation-vocabulary-skill
  - eks-skills-apple-design-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-audit
  - eks-skills-improve-animations-plan-template
  - eks-skills-improve-animations-skill
  - eks-skills-prototype-picker
  - eks-skills-prototype-skill
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
tags:
  - od-area-motion
---
# Reduced motion

## In short

Some people feel dizzy, sick or distracted when things move on screen, so they ask their device to reduce motion. When that setting is on, the interface should stop things sliding, scaling, bouncing or drifting, but still show what changed with short fades and color changes, so it never feels broken. Reduced motion means fewer and gentler animations, not zero. The reduced version ships together with every animation, never as a later fix, and is checked by switching the setting on.

## House standards

- `STD-accessibility-motion-01`: ship the `prefers-reduced-motion` variant of every animation that moves something in the same change, including prototype variants and proposed motion recipes.
- `STD-accessibility-motion-02`: under reduced motion, remove translation, scale, slides, springs, parallax, elastic and overshoot, and replace them with a short opacity cross-fade (the sources use 200ms, ease) or a static transition; keep the opacity and color changes that explain a state change; never remove all animation or feedback.
- `STD-accessibility-motion-03`: in JavaScript-driven motion, read the setting (`useReducedMotion()`, or Reanimated's `ReduceMotion.System`) and swap movement values for static ones.
- `STD-accessibility-motion-04`: native stack screen transitions switch to a crossfade when reduced motion is on.
- `STD-accessibility-motion-05`: every motion change is verified by toggling `prefers-reduced-motion` in DevTools and confirming that movement is gone and opacity feedback remains.
- `STD-accessibility-motion-06`: movement without reduced-motion handling is a MEDIUM finding, and reduced-motion code that removes all feedback is also reported.
- `STD-accessibility-motion-07`, `STD-accessibility-motion-08` and `STD-accessibility-motion-09`: no full-viewport moving backgrounds, no slow looping oscillation near 0.2 Hz, and no abrupt brightness jumps between themes.
- `STD-accessibility-motion-10`: large moving surfaces turn semi-transparent while they travel, and fade out and back in during a large reposition.
- `STD-accessibility-motion-11` and `STD-accessibility-motion-12`: reduced transparency and increased contrast are separate signals with their own handling.

## What the sources teach

### Ship it with the animation

- Reduced motion ships with the animation, not as a follow-up [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]] [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]. Every suggested animation must include its reduced-motion handling [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]], and it is part of the craft bar every prototype variant has to meet [S-L19-031] [[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]].
- Missing reduced-motion handling is a MEDIUM-severity finding and a target for a codebase-wide sweep [S-L19-027] [[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]].

### Gentler, not zero

- Keep opacity and color changes and drop transform-based movement: fewer and gentler animations, not none [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]] [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]. Keep the opacity and color transitions that aid comprehension and remove position changes [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]. Honour the setting by keeping opacity and color, not by removing everything [S-L19-032] [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]].
- The vocabulary skill defines reduced motion more loosely, as respecting the setting by "toning down or removing motion" [S-L19-019] [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]].

### What goes, and what replaces it

- Drop translation, scale, parallax and overshoot; keep opacity and color; screen transitions become a fade [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]].
- Slides, springs and parallax become short opacity cross-fades and overshoot goes, while helpful opacity and color changes stay; a sheet under reduced motion transitions opacity over 200ms ease with its transform removed [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- A sliding picker highlight simply loses its transition under reduced motion [S-L19-030] [[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]].

### How to implement it

- In React, branch JavaScript motion with `useReducedMotion()` [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]] [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]. In Expo apps, screen transitions switch to `animation: 'fade'` when reduced motion is on [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]] [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]].

### How to check it

- Every fix plan's verification toggles `prefers-reduced-motion` in the DevTools Rendering panel and confirms that movement is dropped while opacity feedback remains [S-L19-026] [[sources/eks-skills-improve-animations-plan-template-emilkowalski-skills-skills-improve-animations-plan-template-md|emilkowalski/skills: skills/improve-animations/PLAN-TEMPLATE.md]].

### Beyond the setting

- Avoid full-viewport moving backgrounds, slow looping oscillations near 0.2 Hz (one cycle every 5 seconds) and abrupt brightness jumps between light and dark themes; make large moving objects semi-transparent while they travel [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].

## Where they agree and disagree

- **The sources agree.** Every source that covers reduced motion is an Emil Kowalski skill file, and all of them say gentler, not zero. The only looser wording is the vocabulary skill's "toning down or removing" [S-L19-019] [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]; `STD-accessibility-motion-02` settles it: never remove all feedback.
- **Instant versus fade.** The picker drops its transition entirely [S-L19-030] [[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]], so the highlight jumps into place instead of fading. `STD-accessibility-motion-02` allows "a static transition", so this is within the rule [inferred].
- **OpenDesigner's research agrees on the core.** DC-L04-25's default ("keep feedback (color, opacity) and remove travel (translate, scale, parallax)") matches `STD-accessibility-motion-02`, and its note that shared-axis transitions should swap to a fade matches the native crossfade in `STD-accessibility-motion-04`.
- **The "remove" option.** Q-motion-07 offers `remove` (all non-essential motion, WCAG 2.3.3). standards.json records this as a conflict with `STD-accessibility-motion-02`, because the engine then sets the reduced feedback, enter, exit and expand transitions to 0ms, leaving no motion at all. The same entry records that the engine's reduced cross-fade is 100ms on the standard curve, while the sources use 200ms ease.
- **Separate settings.** DC-L10-16 and Q-motion-10 treat reduced motion, reduced transparency and increased contrast as separate modes, in line with `STD-accessibility-motion-11` and `STD-accessibility-motion-12`.
- **Oscillation and devices.** DC-L14-08 and DC-L04-25 cite Apple's visionOS warning about oscillation near 0.2 Hz; `STD-accessibility-motion-08` makes it a rule for every platform. The per-device motion budgets in DC-L14-08 are not covered by these sources.
- **Loading shimmer.** DC-L13-01 notes that animated skeletons raise accessibility concerns and should honour reduced motion, which `STD-accessibility-motion-01` covers.
- **In-app setting.** DC-L04-25 mentions an in-app "no motion" setting (Fluent) and Q-aud-04 asks whether people can switch motion off inside the product; these sources only discuss the operating-system setting.

## Decisions this informs

- **Q-motion-07** (fade gently or stop moving): `replace` is the house answer; `remove` needs rewording so it never removes feedback, and the reduced cross-fade should be 200ms ease.
- **Q-motion-10** (which device settings the design follows): reduced motion is always followed, and reduced transparency and increased contrast get their own handling.
- **Q-aud-04** (which settings people can change): whether to add an in-app reduced-motion switch on top of the OS setting.
- **Q-motion-06** (screen transitions): under reduced motion, spatial transitions become fades.
- **Q-motion-04** (how springs are set up): springs and bounce are removed under reduced motion.
- **Q-plat-08** (what the UI is built with): decides the mechanism: the CSS media query, `useReducedMotion()`, or Reanimated's `ReduceMotion.System`.

## Visual examples worth showing

- A sheet opening twice: sliding up normally, then fading in over 200ms with no movement under reduced motion [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- A native screen push next to its reduced-motion fade [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]].
- The DevTools Rendering panel with `prefers-reduced-motion` toggled, next to the checklist line from the fix plan [S-L19-026] [[sources/eks-skills-improve-animations-plan-template-emilkowalski-skills-skills-improve-animations-plan-template-md|emilkowalski/skills: skills/improve-animations/PLAN-TEMPLATE.md]].
- The picker highlight sliding normally and jumping into place under reduced motion [S-L19-030] [[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]].
- A "do not" card: a full-viewport moving background and a slow 5-second loop [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].

## Open questions

- Should OpenDesigner offer an in-app reduced-motion switch (Q-aud-04), or rely on the OS setting alone as these sources do?
- Should reduced motion be exported as a token mode (DC-L04-25) or written per component? The sources show per-component code only.
- Is a jump (no transition) acceptable for every moving element under reduced motion, or only for small ones such as the picker highlight [S-L19-030] [[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]?
- Haptics and sound as alternatives when motion is reduced (DC-L04-25, from Apple) are not discussed in these sources.
