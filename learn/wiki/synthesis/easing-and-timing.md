---
type: synthesis
title: Easing and timing
created: 2026-09-24
updated: 2026-09-27
sources:
  - adev-changelog
  - adev-home
  - ek-7-practical-animation-tips
  - ek-agents-with-taste
  - ek-building-a-drawer-component
  - ek-building-a-toast-component
  - ek-building-an-animation-course
  - ek-the-magic-of-clip-path
  - ek-train-your-judgement
  - ek-you-dont-need-animations
  - eks-readme
  - eks-skills-animate-expo-recipes
  - eks-skills-animate-expo-skill
  - eks-skills-animate-recipes
  - eks-skills-animate-skill
  - eks-skills-animation-vocabulary-skill
  - eks-skills-apple-design-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-audit
  - eks-skills-improve-animations-plan-template
  - eks-skills-improve-animations-skill
  - eks-skills-mobile-native-skill
  - eks-skills-prototype-picker
  - eks-skills-prototype-skill
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
  - 14h1VnkQvIc
  - NtZeYmTMuo4
  - SfX43uIubj4
  - ZsP20PN14O0
  - d4MF6pdAZNw
  - ld1zhQMXxXU
  - nl8OFGdx75w
tags:
  - od-area-motion
---
# Easing and timing

## In short

Easing is how the speed of a movement changes from start to finish; timing is how long it takes. The house rule picks the curve by the job the motion does: ease-out for things entering or leaving, ease-in-out for things moving across the screen, plain ease for hover and color changes, linear only for constant motion such as spinners, and never ease-in. Interface motion stays under 300ms, bigger things may take a little longer, and exits run a little faster than entrances. Long, slow curves are for marketing and illustration, such as page-load sequences, not for everyday controls.

## House standards

- `STD-easing-duration-01`: pick the curve by the motion's job: enters or exits the screen (ease-out), moves or morphs on screen (ease-in-out), hover or color change (ease), constant motion such as a spinner or marquee (linear); the default is ease-out.
- `STD-easing-duration-02`: use the strong custom curves `cubic-bezier(0.23, 1, 0.32, 1)` (ease-out) and `cubic-bezier(0.77, 0, 0.175, 1)` (ease-in-out), not built-in keywords other than `ease` and `linear`.
- `STD-easing-duration-03`: never use ease-in on any UI animation, entering or exiting, and do not try to rescue it with a shorter duration.
- `STD-easing-duration-06`: UI motion stays under 300ms unless there is a stated reason (a 500ms web drawer, a toast tuned to its personality); marketing and explanatory motion may be longer; native screen transitions keep the platform default.
- `STD-easing-duration-07`: budgets per element: press feedback 100-160ms, tooltips and small popovers 125-200ms, dropdowns and selects 150-250ms, modals and drawers 200-500ms.
- `STD-easing-duration-09`: nothing runs longer than 1s unless it is illustrative.
- `STD-easing-duration-10`: larger elements and longer travel get longer durations.
- `STD-easing-duration-11`: exits are about 20% faster than entrances.
- `STD-easing-duration-12`: where the user is deciding (press-and-hold, hold-to-confirm), the deliberate phase is slow (2s linear) and the response snappy (200ms ease-out).
- `STD-easing-duration-13`: the component's personality sets its easing and duration.
- `STD-easing-duration-15`: loading spinners spin fast.
- `STD-easing-duration-17`: choose and state every curve and duration deliberately.
- `STD-components-toasts-drawers-40` and `STD-enter-exit-origin-41`: drawers use `cubic-bezier(0.32, 0.72, 0, 1)` over 500ms; once a finger drives them they settle with a spring instead.
- `STD-enter-exit-origin-13`: items entering together are staggered by 30-80ms each.
- `STD-enter-exit-origin-39`: reversible transitions mirror their easing, while UI entrances and exits still follow the ease-out rule.

## What the sources teach

### Easing matters more than the animation itself

- Easing is called the most important part of any animation: it can make a bad animation look great and a great one look bad [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]. A bad easing or duration can ruin an otherwise good animation, and the course says the reasoning behind the chosen easing and duration is often more important than the code [S-L19-002] [[sources/adev-home-animations-dev|animations.dev]].
- Choosing easing and duration is described as judgement that AI is not good at [S-L19-007] [[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]], and agents often get enter easing wrong [S-L19-014] [[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]]. One judgement exercise is dedicated to choosing the right easing for a toast [S-L19-011] [[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]].

### Pick the curve by the job

- A strict flowchart: ease-out for anything entering or leaving and as the default, ease-in-out for movement or morphing on screen, ease for hover and color changes, linear for constant motion [S-L19-004] [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]] [S-L19-007] [[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]] [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]. The same flowchart appears in the design-engineering and review standards [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]].
- Never ease-in: it starts slow, so a 300ms ease-in dropdown feels slower than the same dropdown with ease-out [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]. Wrong easing on UI is rated HIGH severity in audits [S-L19-027] [[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]] and blocks a review [S-L19-032] [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]]. The prototype craft bar repeats the rule: ease-out on entrances, never ease-in [S-L19-031] [[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]].
- The vocabulary skill agrees (ease-out for UI and user responses, ease-in usually avoided, linear only for spinners or marquees) and adds that asymmetric curves feel more alive [S-L19-019] [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]].
- Reversible transitions can mirror their easing with inverse control points [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].

### Custom curves beat the built-in ones

- CSS's built-in curves are usually too weak; custom ones feel more energetic [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]. The course guideline says not to use built-in CSS easings unless it is `ease` or `linear` [S-L19-001] [[sources/adev-changelog-animations-dev|animations.dev]].
- Three shared tokens recur: `--ease-out: cubic-bezier(0.23, 1, 0.32, 1)`, `--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1)` and `--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1)` [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]] [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]], with the same values as `Easing.bezier` constants in React Native [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]. The course keeps 18 named custom easings as `--ease-*` variables (six are shown) [S-L19-007] [[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]; all six shown have both control points below the diagonal, the slow-starting ease-in shape, so they are not UI curves under `STD-easing-duration-03` [inferred from the control points].
- The drawer curve comes from the Ionic Framework and closely matches iOS; its 500ms duration is meant to mimic the iOS sheet [S-L19-005] [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]].

### How long

- UI animations should generally stay under 300ms; a 180ms select feels more responsive than a 400ms one [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]] [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]. Marketing sites are the exception [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]. Most animations sit around 0.2-0.3s and none should pass 1s unless illustrative [S-L19-001] [[sources/adev-changelog-animations-dev|animations.dev]].
- Per-element bands: press feedback 100-160ms, tooltips and small popovers 125-200ms, dropdowns and selects 150-250ms, modals and drawers 200-500ms [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]. Another version: micro-interactions 100-150ms, standard UI 150-250ms, modals and drawers 200-300ms, longer for bigger elements and longer travel, exits about 20% faster [S-L19-004] [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]].
- In Expo apps the bands are 100-150ms, 150-200ms and about 300ms, all under 300ms except platform navigation [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]. The mobile recipes give press 120ms on the strong ease-out, swipe-out 200ms ease-out, a tab pill 250ms ease-in-out, list entrances 250ms with a 30-80ms stagger, and toasts 300ms in and 250ms out [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]].
- The web recipes give exact per-component values, linear for progress fills, ease for toasts, and ease-in-out for tab clips and scroll reveals [S-L19-017] [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]. A worked plan replaces `transition: all 400ms ease-in` with separate transform and opacity transitions at 200ms on `var(--ease-out)` [S-L19-026] [[sources/eks-skills-improve-animations-plan-template-emilkowalski-skills-skills-improve-animations-plan-template-md|emilkowalski/skills: skills/improve-animations/PLAN-TEMPLATE.md]].
- Small examples: press feedback over 100ms ease-out [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]], 100-160ms ease-out reusing the existing tokens instead of a new curve [S-L19-028] [[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]], and a picker highlight that slides over 250ms on the strong ease-out while item colors change in 150ms, with no transition on the variant swap itself [S-L19-030] [[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]].
- Components tuned to their personality: Sonner's toasts use `transform 400ms ease` and dismiss after 4 seconds by default [S-L19-006] [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]. The clip-path image reveal runs 1s on `cubic-bezier(0.77, 0, 0.175, 1)` [S-L19-010] [[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]; the house standards list it as illustrative marketing motion, right at the 1s ceiling (`STD-easing-duration-09`).

### Asymmetric timing

- Press-and-hold and hold-to-confirm interactions need asymmetric timing: slow while the user decides, snappy when they let go [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]] [S-L19-032] [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]] [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]].

### What the practitioner videos add

- "Almost never" use a linear ease, because real things speed up and slow down; the curve also sets the tone (snappy, springy, or slow and smooth) [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]].
- Easing on decorative entrances makes them feel natural, and a plain fade-in is called robotic [S-L19-063] [[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]. Loops and marquees should move slowly, and a cursor-following element can be tuned to snap faster or ease in slower [S-L19-069] [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]].
- Load sequences in Figma: hold the loading screen 1,000ms, slide it up over 800ms on a custom "exponential" bezier, fade the nav in with 200ms ease in and out, and run each text-wipe pass over 700ms [S-L19-081] [[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]]. The coded version uses GSAP's `expo.inOut` with 1.3s for large moves, 0.6s item fades staggered by 0.2s and a 0.3s navbar fade with no ease named, and grows its pill navbar from scale 0 over 0.8s [S-L19-071] [[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]].
- In a Figma sidebar tutorial, a 300ms after-delay chains the spinner frames and a regular ease-out handles the final success transition [S-L19-059] [[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]].
- Tooltips appear only after a full second of hover [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]].

## Where they agree and disagree

- **Linear.** The video's advice to almost never use a linear ease [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]] agrees with `STD-easing-duration-01`, which says exactly where linear is right: constant motion such as spinners, marquees and progress fills.
- **Load sequences.** The 1.3s moves in [S-L19-071] [[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]] and the 1,000ms hold plus 800ms slide in [S-L19-081] [[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]] go past the 300ms and 1s budgets. They are marketing page-load motion, which `STD-easing-duration-06` and `STD-easing-duration-09` allow to be longer when illustrative [inferred]; the same creator also says to keep preloaders short because people are impatient [S-L19-069] [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]. The Figma version fades the nav in with ease-in-out [S-L19-081] [[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]], whereas the house rule gives entering elements ease-out [inferred]. The coded version's `expo.inOut` slides a full-screen loader off the screen and the header text into place [S-L19-071] [[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]; by the house flowchart those are an exit and an entrance (ease-out), not on-screen moves [inferred]. Its navbar grows from scale 0, which `STD-enter-exit-origin-01` forbids on every surface.
- **Tooltip delay.** "A full second" [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]] comes from one video and no other source gives a number, so treat it as opinion. The house rule (`STD-enter-exit-origin-10`) delays only the first tooltip and opens its neighbours instantly, without fixing the first delay.
- **Exit curves in OpenDesigner.** DC-L04-21 and DC-L04-24 give exits an accelerate curve (for example `(0.3, 0, 1, 1)`), and the Q-motion-01 default says "ease-in to exit". Both conflict with `STD-easing-duration-03` (never ease-in), and standards.json records the conflict. Q-motion-03's role-based option (standard, enter, exit) is closest to picking the curve by job, but the house set groups by four jobs and fixes one curve per job instead of letting an energy dial swap curves (recorded under `STD-easing-duration-02`).
- **Duration scale.** DC-L04-20 recommends 6 steps up to a 700ms "extra" step and long steps of 400-500ms; `STD-easing-duration-06` caps UI motion under 300ms unless there is a stated reason. Both agree that exits are faster: DC-L04-20 says 20-35% shorter, the house says about 20% (`STD-easing-duration-11`).
- **Stagger.** DC-L04-23 and Q-motion-06 suggest 20-50ms per item (500ms total at most); the house range is 30-80ms (`STD-enter-exit-origin-13`), recorded as a conflict. The 0.2s stagger in the GSAP load sequence [S-L19-071] [[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]] is marketing motion and outside both ranges.
- **Toasts at 400ms.** Sonner's 400ms ease [S-L19-006] [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]] is above the 300ms cap; the house reconciles it through the stated-reason clause in `STD-easing-duration-06` and component personality (`STD-easing-duration-13`). That reconciliation covers the web toast only: the React Native recipe says a toast is no exception to the 300ms cap and runs it at 300ms in and 250ms out on ease-out [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]] (`STD-components-toasts-drawers-07`, `STD-components-toasts-drawers-08`).
- **Response time.** DC-L13-01 asks for acknowledgement within 50ms; press feedback that starts on pointer-down and lasts 100-160ms fits that rule [inferred].

## Decisions this informs

- **Q-motion-02** (how many durations, exits faster): an asymmetric set with exits about 20% shorter, capped under 300ms for UI, with named exceptions (drawers 500ms, toasts by personality).
- **Q-motion-03** (how curves are grouped): group by job (enter/exit, on-screen move, hover and color, constant) with the three custom curves; no ease-in exit curve.
- **Q-motion-01** (motion feel): the `two-mode` default's "ease-in to exit" needs to change to ease-out to meet `STD-easing-duration-03`.
- **Q-motion-06** (transitions and stagger): stagger step 30-80ms.
- **Q-pattern-01** (dialog, sheet or popover): sheets and drawers get the drawer curve over 500ms, modals 200-500ms.
- **Q-state-08** (waiting): spinners use linear and spin fast (`STD-easing-duration-15`).

## Visual examples worth showing

- Two 300ms "Options" dropdowns side by side, ease-in on the left and ease-out on the right, plus the replayable curve graph [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]].
- A 180ms and a 400ms select opened one after the other [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]].
- CSS's built-in ease-in-out next to a custom ease-in-out [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]].
- A drawer opening on the Ionic curve over 500ms [S-L19-005] [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]].
- A hold-to-delete button: 2s linear fill while pressed, 200ms ease-out snap-back on release [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]].
- The load sequence as a timeline: loading screen slide, dot growing into a pill navbar, text wipe, with each step's delay and duration [S-L19-081] [[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]] [S-L19-071] [[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]].
- Swiped cards with a rigid curve and with a bouncier, momentum-carrying curve [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]].

## Open questions

- How long should the first tooltip's delay be? Only one video gives a number (1s [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).
- `STD-enter-exit-origin-39` notes a tension: mirroring an ease-out on the way back produces an ease-in shape, which the easing rules forbid. Which wins for reversible transitions?
- Do page-load holds (such as the 1,000ms hold in [S-L19-081] [[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]]) count toward the 1s ceiling in `STD-easing-duration-09`?
- Should OpenDesigner let each component carry its own curve and duration (as the toast needs), rather than sharing one enter transition across menus, popovers and toasts?
