---
type: synthesis
title: Animation performance
created: 2026-09-24
updated: 2026-09-24
sources:
  - adev-home
  - ek-7-practical-animation-tips
  - ek-agents-with-taste
  - ek-building-a-drawer-component
  - ek-the-magic-of-clip-path
  - eks-performance-cheatsheet
  - eks-skills-animate-expo-recipes
  - eks-skills-animate-expo-skill
  - eks-skills-animate-recipes
  - eks-skills-animate-skill
  - eks-skills-animation-vocabulary-skill
  - eks-skills-apple-design-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-improve-animations-audit
  - eks-skills-improve-animations-skill
  - eks-skills-prototype-picker
  - eks-skills-prototype-skill
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
  - eks-skills-write-swift-skill
  - EHwZzWd-OnQ
  - ZsP20PN14O0
tags:
  - od-area-motion
---
# Animation performance

## In short

Smooth motion depends on what you animate. Moving and fading things with transform and opacity lets the browser slide pixels around without recalculating the page layout, while animating width, height, top or left makes it redo that work on every frame. Values that change every frame, such as a drag position, should be written straight to the element rather than through React state or a shared CSS variable. Pick the cheapest tool that fits, CSS before JavaScript, and treat any dropped frame as a bug. Speed is also about perception: shorter animations and faster spinners make an app feel faster even when loading takes just as long.

## House standards

- `STD-performance-properties-01`: movement, size and visibility are animated with transform and opacity only; never width, height, margin, padding, top or left (in React Native also flex and gap).
- `STD-performance-properties-02`: the only exceptions are clip-path, accordion height on the web, and width on an absolutely positioned element with no children.
- `STD-performance-properties-06`: never `transition: all`; name the properties.
- `STD-performance-properties-09`: in Motion, animate the full transform string, not the `x`, `y` or `scale` shorthands.
- `STD-performance-properties-10` and `STD-performance-properties-11`: per-frame values go to `ref.current.style`, a motion value or a Reanimated shared value, never React state; drag transforms are set on the moving element, never through a CSS variable on a parent.
- `STD-performance-properties-12`: add `will-change: transform` only once you have seen an element shift 1px or jitter as its motion starts.
- `STD-performance-properties-13`, `STD-performance-properties-14` and `STD-performance-properties-15`: pick the cheapest tool (CSS transition, then `@starting-style`, then a CSS animation, then WAAPI, then Motion); use Intersection Observer rather than adding Motion for viewport entry; CSS or WAAPI for predetermined motion, JavaScript for dynamic or gesture-driven motion.
- `STD-performance-properties-16`: dropped frames fail review, measured against 60fps (120fps where supported, an 8ms frame budget).
- `STD-performance-properties-17`: virtualize long lists and large tables; never render 1,000+ rows directly.
- `STD-performance-properties-18`, `STD-performance-properties-19` and `STD-performance-properties-20`: in React Native, motion runs on the UI thread with Reanimated worklets and `Gesture.Pan()`; never animate Android elevation or BlurView intensity; build layout-animation builders outside render.
- `STD-performance-properties-24` and `STD-performance-properties-25`: animate a child to stop hover flicker; keep per-frame movement below the perception threshold.
- `STD-enter-exit-origin-30`: animated blur stays under 20px.
- `STD-enter-exit-origin-24` and `STD-enter-exit-origin-25`: measure heights before animating a collapse, never animate to `auto`, and in React Native never animate a header's height.
- `STD-mobile-touch-35` and `STD-mobile-touch-39`: cross to the React Native JavaScript thread only at thresholds, never per frame; unlock 120fps on ProMotion iPhones.
- `STD-easing-duration-15`: loading spinners spin fast.
- `STD-process-review-taste-33`: judge touch and gesture motion on real hardware.

## What the sources teach

### Animate the cheap properties

- 60fps is the baseline for smooth motion and 120fps on newer displays; jank is the visible stutter of dropped frames. Animating transform and opacity lets the GPU composite motion without redoing layout or paint, `will-change` hints that an element should get its own layer ahead of time, and animating width, height, top or left causes layout thrashing [S-L19-019] [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]].
- Animate only transform and opacity [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]] [S-L19-013] [[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]] [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]], a rule every prototype variant follows [S-L19-031] [[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]] and reviews enforce [S-L19-032] [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]] [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]].
- Clip-path is hardware-accelerated, does not affect layout, avoids layout shift when an image is revealed and needs no extra overflow-hidden wrapper, so it outperforms animating width or height [S-L19-010] [[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]].
- Accordion height costs layout on every frame, so keep it short [S-L19-017] [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]. A picker highlight animates width as a deliberate exception, acceptable because the element is 28px tall, absolutely positioned and has nothing depending on its layout [S-L19-030] [[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]].

### Keep per-frame work off the slow path

- The Vaul drawer lagged once its content passed about 20 list items, even without re-renders: updating a CSS variable on every drag frame made the browser recalculate styles for every child. Setting the transform directly on the element fixed it [S-L19-005] [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]].
- Write per-frame values to `ref.current.style`, not React state [S-L19-013] [[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]]. Never drive child transforms from a parent CSS variable [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]] [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]] [S-L19-032] [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]].

### Choose the right tool and thread

- CSS animations run off the main thread, so they stay smooth while the page is busy; Motion's `x`, `y` and `scale` shorthands are not hardware-accelerated and drop frames under load, so use the full transform string [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]] [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]. WAAPI gives programmatic control with CSS performance and no library [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] [S-L19-017] [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]].
- Never use `transition: all` [S-L19-013] [[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]] [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]; prefer CSS or WAAPI for predetermined motion [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]].
- In React Native only transform and opacity are free: keep motion on the UI runtime, never call `setState` or `scheduleOnRN` per frame, never animate elevation or BlurView intensity, enable 120fps on ProMotion iPhones, and judge feel on a release build on the slowest supported device [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]. Never animate a header's height, clamp scroll interpolations, build layout-animation builders at module scope or in `useMemo`, and drive keyboard-following UI on the UI thread [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]].
- In SwiftUI, an animation that responds to a gesture or scroll starts with `withAnimation` in the synchronous callback, on the same frame as the event; closures marked `@Sendable`, such as `visualEffect`, run off the main thread to keep frames cheap [S-L19-034] [[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]].

### Hints, blur and very fast motion

- Add `will-change: transform` only once you see an element shift 1px as its motion starts [S-L19-013] [[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]]; the practical fix table uses it for shaky or jittery animations [S-L19-004] [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]].
- Keep animated blur under 20px because heavy blur is expensive [S-L19-004] [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]] [S-L19-013] [[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]] [S-L19-017] [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]].
- Use `requestAnimationFrame`, keep the per-frame change below the perception threshold to avoid strobing, and add a subtle motion blur or stretch to very fast motion [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].

### Long lists

- Long lists scroll slowly when every row renders; virtualize so only visible rows exist [S-L19-013] [[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]].

### Severity

- Dropped frames are a HIGH-severity finding in audits [S-L19-027] [[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]].

### Perceived performance

- Fast animations and a faster-spinning spinner make an app feel faster even though loading takes the same time [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]. The course names choosing which properties to animate as the way to keep an animation performant, and teaches performance in its fourth module [S-L19-002] [[sources/adev-home-animations-dev|animations.dev]].

### What the practitioner videos add

- Big or flashy animations can slow a site down; a preloader can give a heavy background video or 3D effect time to load (the creator guesses this is why one site uses it) [S-L19-069] [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]].
- Very large changes in a morphing image can slow the browser and make the animation choppy [S-L19-050] [[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]].

## Where they agree and disagree

- **Heavy effects cost speed.** The videos' warnings [S-L19-069] [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]] [S-L19-050] [[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]] agree with the house performance standards; neither video gives a property-level rule, and the house fills that in (`STD-performance-properties-01`) [inferred].
- **Preloaders.** A preloader [S-L19-069] [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]] is one creator's guess about why a site uses one. The house has no preloader rule, and a preloader is a wait people sit through, which the speed rules (`STD-easing-duration-06`, `STD-easing-duration-09`) and the purpose gate would question outside marketing pages [inferred].
- **Web springs.** DC-L04-22 notes that the web needs a JavaScript spring library or a sampled CSS `linear()` curve; this matches `STD-performance-properties-15`: JavaScript for dynamic, interruptible motion, CSS for predetermined motion [inferred].
- **Input latency.** DC-L13-01 cites INP of 200ms or less and RAIL's 100ms response and 50ms input handling; this sits alongside `STD-springs-gestures-41` (remove latency from the input path) [inferred].
- **Devices.** DC-L14-08 adds device classes (TV, watch, car, e-ink) where motion should shrink or stop; the L19 sources cover phones, desktops and ProMotion displays only.
- **Gap in OpenDesigner.** None of OpenDesigner's questions or Decision Cards covers animation performance directly; it arrives through the build stack (Q-plat-08) and the house standards.

## Decisions this informs

- **Q-plat-08** (what the UI is built with): React, React Native or SwiftUI decides which rules apply: CSS, WAAPI and Motion on the web; Reanimated worklets and Gesture Handler in React Native; `withAnimation` on the event frame in SwiftUI.
- **Q-plat-02** (which devices matter): the slowest supported device is the one that verifies feel; ProMotion iPhones need 120fps unlocked.
- **Q-depth-04** and **Q-dir-01** (glass and translucent surfaces): blur is expensive, so animated blur stays under 20px and React Native never animates BlurView intensity.
- **Q-pattern-02** (how long lists load): long lists are virtualized whatever the loading pattern.
- **Q-motion-04** (how springs are set up): springs on the web add a JavaScript library or a sampled curve.
- **Q-state-08** (what people see while waiting): a fast spinner improves perceived performance.

## Visual examples worth showing

- The drawer with 20+ list items dragged two ways: through a CSS variable on the parent (laggy) and with a direct transform (smooth) [S-L19-005] [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]].
- An image revealed with clip-path next to one revealed by animating its height, showing the layout shift [S-L19-010] [[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]].
- An element that shifts 1px as it starts moving, before and after `will-change: transform` [S-L19-013] [[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]].
- Two spinners at different speeds loading the same data [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]].
- A frame-budget graphic: 16ms at 60fps and 8ms at 120fps, built from `STD-performance-properties-16`.
- The seven problem-and-fix pairs from the cheatsheet as a checklist card [S-L19-013] [[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]].

## Open questions

- Should `engine.py review` flag layout-property animation and `transition: all` in the person's code, as the standards require?
- Should OpenDesigner's generated preview and exports be checked against the frame budget, and on which devices?
- When is a sampled CSS `linear()` spring an acceptable, cheaper stand-in for a JavaScript spring?
- Should marketing pages get a preloader rule, given that only one video discusses preloaders?
