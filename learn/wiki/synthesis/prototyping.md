---
type: synthesis
title: Prototyping
created: 2026-09-24
updated: 2026-09-24
sources:
  - 7cTdCu8HMgM
  - Lp6ey4AyDzA
  - NtZeYmTMuo4
  - adev-home
  - d4MF6pdAZNw
  - ek-friction-as-a-feature
  - eks-readme
  - eks-skills-apple-design-skill
  - eks-skills-prototype-picker
  - eks-skills-prototype-skill
  - ld1zhQMXxXU
  - nl8OFGdx75w
  - ulSOdTgoGeY
tags:
  - od-area-process
---

# Prototyping

## In short

A prototype is a working version you can click, hover and feel, and every source here prefers it to a static picture or a written description. Emil Kowalski's sources say prototyping is a way of thinking: build a few genuinely different versions, compare them one at a time, and ship only the one that wins; those rules are locked house standards. Kole Jain's videos show the Figma side: frames linked by triggers and delays, Smart Animate matching layers by name, and custom springs and curves, with timing values that are his choices for one demo. When a Figma prototype moves to code, its timings and curves still have to meet the house motion standards. Building options is cheap now, so the judgement step, deciding what deserves to ship, matters more than before.

## House standards

- `STD-process-review-taste-35` (should): explore interactions with working, interactive prototypes rather than static designs.
- `STD-process-review-taste-36` (should): design a component's motion together with its visuals, never as a layer added afterwards.
- `STD-when-to-animate-22` (should): decide whether an idea deserves to be built; when you build options A and B to compare, validate them and ship the winner, not both.
- `STD-process-review-taste-42` (must): explore one UI piece per prototype run, restated in one sentence.
- `STD-process-review-taste-11` (must): before prototyping motion, map the stack, the existing motion conventions, the product's personality and how often each surface is seen.
- `STD-process-review-taste-37` (must): every variant diverges on a named axis (layout, density, personality, motion or interaction model); two that differ only in accent color or copy count as one.
- `STD-process-review-taste-38` (must): three variants by default, five at most.
- `STD-process-review-taste-39` (must): every variant meets the motion craft bar (ease-out entrances, UI motion under 300ms, correct transform-origin, transform and opacity only, reduced motion handled).
- `STD-process-review-taste-40` (must): every variant fully works, with realistic content.
- `STD-process-review-taste-41` (must): build variants in an isolated surface and never touch or import into production code while exploring.
- `STD-process-review-taste-43` to `STD-process-review-taste-48` (must): show one variant at a time behind the fixed picker, switch instantly, verify every variant, and hand off with an honest table and no favorite (see [[synthesis/presenting-designs|Presenting designs synthesis]]).
- `STD-process-review-taste-49` (must): when the person picks, integrate only that variant following the project's conventions and delete the prototype surface unless asked to keep it.
- `STD-visual-details-25` (must): with no project tokens, prototype in a restrained look: neutral grays, one accent, the system font stack.
- `STD-visual-details-26` (must): build from the project's existing tokens and extend them; never add a parallel set.
- `STD-easing-duration-06` and `STD-easing-duration-09` (must): UI motion under 300ms unless a reason is stated, and nothing over 1s unless it is illustrative.

## What the sources teach

### Why prototype at all

- An interactive demo is worth "a million static designs": you discover the interface by building and playing with it, and a working prototype sets a concrete bar that stops the final build from being mediocre [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Building option A and option B and comparing them is often better validation than theorizing, but only if the comparison actually happens. Because AI makes building cheap, nothing now stops you shipping both, and output with no judgement behind it feels undesigned [S-L19-009] ([[sources/ek-friction-as-a-feature-friction-as-a-feature|Friction as a Feature]]).
- For clients, a prototype shows instead of describing, and reveals hidden details such as swipe actions, a modal animating in, or the sequence when a link is deleted [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).
- Animation theory applies to prototypes and design files as well as code [S-L19-002] ([[sources/adev-home-animations-dev|animations.dev (home)]]).

### Prototyping variants in code

- The prototype skill builds several fully working versions of one described UI piece and lets you flip between them with a switcher [S-L19-014] ([[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]]).
- Its six phases: scope one piece and restate it in one sentence; recon the stack, tokens, personality and context; choose named directions before any code; build a harness in an isolated route such as `/prototypes/<slug>` (or one self-contained HTML file when there is no project); run and verify every variant; then promote the pick and delete the prototype, or "riff" on the direction the person leaned toward [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).
- Divergence is the point: three tints of one idea teach nothing. Name variants for their direction (Quiet, Editorial, Playful, Dense), never Option A, B and C. If two converge while you build them, cut one and say so; two truly different directions beat three padded ones [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).
- The product's personality limits how bold the boldest variant may go, and every variant still meets the full craft bar [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).
- The picker has a fixed contract: number and arrow keys switch, R replays, keys are ignored while typing, the choice persists in `?v=`, and each switch re-mounts the variant so its entrance runs again [S-L19-030] ([[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]).

### Prototyping motion in Figma

- Smart Animate treats layers with exactly the same name in two frames as one element and animates between them; differently named layers crossfade. Toggle visibility with the layer's opacity, not the fill's. Use "while hovering" for hover effects and "on click" for menus [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]).
- A menu slides up because its hidden state sits a few pixels lower; a rectangle morphs into a search bar because both layers share a name; a check mark slides in through a mask. The sidebar's spinner steps through rotated frames on a 300 millisecond delay with a custom spring (stiffness 550, damping 40) [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]).
- Page-load sequences are chains of duplicated frames, each holding one state, linked by after-delay triggers; a 1 millisecond delay starts each step right after the last. It helps to build the frames backwards from the finished screen. The example waits 1,000 milliseconds, slides the loading screen away over 800 milliseconds with a custom curve dragged by eye, expands a dot into the navbar over 400 milliseconds and sweeps a text wipe over 700 milliseconds [S-L19-081] ([[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]]). These are one demo's values.
- Eleven micro-interactions are built the same way (masks, subtract shapes, mouse enter and leave, while pressing, delays). The only timings spoken are a name tag's spring (500 milliseconds, stiffness 636, damping 24) and a one-second hover delay on tooltips. Figma prototypes cannot bind the Command or Shift keys, so X and A stood in for a shortcut demo [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).
- An offset-button hover is two frames (the second with the background moved) joined by a hover interaction [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]).
- The Figma mobile app can mirror a prototype so you can try it on the real screen size [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).

### From prototype to code

- The same load animations were rebuilt with GSAP, using the `expo.inOut` ease to match the Figma curves and paused timelines of chained steps (for example a 0.2 second stagger on navbar items). The presenter says the timings may need adjusting in code [S-L19-071] ([[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]).

## Where they agree and disagree

Between the sources:

- **Prototype rather than describe:** all agree [S-L19-020] [S-L19-009] [S-L19-041] [S-L19-002].
- **Figma frames versus working code:** Kole's prototypes are chains of frames and delays [S-L19-059] [S-L19-081] [S-L19-079]; the prototype skill builds variants that fully work, with real interactions [S-L19-031]. Figma cannot bind modifier keys [S-L19-079], a limit code does not have. For keyboard and gesture feel, only a coded prototype is a fair test [inferred].
- **How many to build:** the friction essay compares two options [S-L19-009]; the prototype skill defaults to three and caps at five [S-L19-031]. Kole's videos build one direction and polish it.

Against the house motion standards:

- **Long load sequences:** the 800 and 700 millisecond steps [S-L19-081] are over the 300ms UI cap in `STD-easing-duration-06`. As marketing page-load motion they fall under that standard's "can be longer" clause and each step stays under the 1s limit of `STD-easing-duration-09`, but the standard also says a rarely seen animation must still pass a speed check, and the whole sequence holds the content back for almost two seconds [inferred].
- **Curves set by eye:** hand-dragged bezier handles and Figma's ease in and out preset [S-L19-081] differ from `STD-easing-duration-02`, which asks for the named strong curves or a curve from easing.dev or easings.co. In code, `expo.inOut` [S-L19-071] suits movement on screen under `STD-easing-duration-01`, but a loading screen sliding away is an exit, where the flowchart picks ease-out [inferred].
- **A spring-stepped spinner:** the Figma spinner steps through frames with a spring [S-L19-059]; `STD-easing-duration-01` gives constant motion such as a spinner linear easing, and `STD-easing-duration-15` says spinners spin fast [inferred].

Against OpenDesigner's existing research:

- **Divergence agrees:** DC-L17-05 generates three concepts first and enforces anti-convergence, and DC-L16-05 cites Dow et al. (2010): designers who made several prototypes in parallel produced better and more varied results. Both support [S-L19-031]. DC-L17-05's anti-convergence asks variants to differ in font family, palette and layout; `STD-process-review-taste-37` adds that a difference in accent color alone never counts as a new direction.
- **The "show 6" grid conflicts:** DC-L16-05's default grid of six variants side by side breaks both the five-variant cap (`STD-process-review-taste-38`) and one-at-a-time viewing (`STD-process-review-taste-43`). The option gallery's 3 to 8 side-by-side directions is already recorded as a conflict on both standards.
- **Rendered, not raster:** DC-L17-11 (decide on rendered components, use images only for mood boards) agrees with fully working variants.

## Decisions this informs

- **Q-pref-02** (planned, not asked yet: how to review AI changes and try other versions): the house standards point to a picker showing three to five named variants one at a time; `show-6` conflicts with them, and `lock-shuffle` fits fine-tuning after a direction is chosen [inferred].
- **Q-motion-01** (how motion should feel): each prototype variant must meet the craft bar whatever the answer, and the product's personality bounds the boldest variant [S-L19-031].
- **Q-motion-04** (how springy motion is set up): Figma's stiffness-and-damping springs [S-L19-059] [S-L19-079] are spring physics; `durations-only` has no place for them [inferred].
- **Q-tool-03** (which design tool): the Figma prototype workflow of [S-L19-059] [S-L19-081] [S-L19-079] applies when the answer is a Figma plan; without a design tool, the code prototype of [S-L19-031] still works.

## Visual examples worth showing

- A variant picker over three directions of one toast, each shown full size on a realistic page, flipped with the number keys [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).
- The animated dashboard sidebar: hover highlights, a menu sliding up, a rectangle morphing into a search bar, a yellow focus glow, a spinner and a masked check mark [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]).
- Three page-load animations (a loading screen sliding up, a navbar growing from a dot, a text wipe) shown as the chain of frames with their delays, beside the finished motion [S-L19-081] ([[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]]), and the same animations in code [S-L19-071] ([[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]).
- The name tag popping over a headshot with and without its custom spring, where the easing is the whole difference [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).
- A dashboard prototype for a client: a create-link modal animating in, swipe actions and the delete sequence [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).

## Open questions

- How should a Figma spring (stiffness, damping) or a hand-dragged curve be translated into code that meets `STD-easing-duration-02`? None of the sources give a mapping.
- What counts as validating a prototype? The friction essay insists on it but does not say who judges, how, or what passing means [S-L19-009].
- Should OpenDesigner's own option gallery switch to the one-at-a-time picker, or is a gallery of whole design-system directions a different job from comparing variants of one piece?
- Is a page-load sequence that holds content back for close to two seconds acceptable under the house standards, even on a marketing page?
