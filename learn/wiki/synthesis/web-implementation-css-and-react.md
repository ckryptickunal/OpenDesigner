---
type: synthesis
title: Web implementation (CSS and React)
created: 2026-09-24
updated: 2026-09-27
sources:
  - eks-performance-cheatsheet
  - eks-skills-animate-skill
  - eks-skills-animate-recipes
  - eks-skills-emil-design-eng-skill
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
  - eks-skills-improve-animations-audit
  - eks-skills-improve-animations-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-animation-vocabulary-skill
  - eks-skills-apple-design-skill
  - eks-skills-mobile-native-skill
  - eks-skills-pick-ui-library-skill
  - eks-skills-prototype-skill
  - eks-skills-prototype-picker
  - eks-skills-ask-sonner-skill
  - eks-skills-ask-sonner-api
  - ek-7-practical-animation-tips
  - ek-agents-with-taste
  - ek-building-a-toast-component
  - ek-building-a-drawer-component
  - ek-the-magic-of-clip-path
  - ek-building-an-animation-course
  - adev-home
  - adev-changelog
  - sonner-home
  - sonner-getting-started
  - sonner-toaster
  - sonner-toast
  - sonner-styling
  - sonner-other
  - vaul-api
  - vaul-default
  - vaul-getting-started
  - lkKGQVHrXzE
  - 7sUUzOCv47U
  - ZsP20PN14O0
  - d4MF6pdAZNw
tags:
  - od-area-tokens
---

# Web implementation (CSS and React)

## In short

This page is about turning design decisions into working CSS and React. The house rules (Emil Kowalski) are short: use the cheapest tool that does the job, so a CSS transition before a JavaScript library; animate only `transform` and `opacity`, apart from a few named exceptions; never write `transition: all`; and use transitions, not keyframes, for anything a person can trigger again before it finishes. Hover effects, reduced motion and touch are handled with CSS media queries, not by guessing the device in JavaScript. Standard components come from proven libraries (Sonner for toasts, Base UI for dialogs and menus) that you mount once, and values that change every frame stay out of React state. Practitioner videos add Tailwind and GSAP details; where their code animates width or runs longer than a second, the house standards win.

## House standards

These apply to every system OpenDesigner builds and cannot be traded away. Motion timing itself is covered in the [[synthesis/easing-and-timing|Easing and timing synthesis]]; the standards below are the ones about how the code is written.

**Choosing the tool and the library**

- **STD-performance-properties-13** (must): pick the cheapest tool that fits and stop there: CSS transition, then `@starting-style`, then a CSS animation, then WAAPI (`element.animate()`), then Motion.
- **STD-performance-properties-15** (should): predetermined motion in CSS or WAAPI; JavaScript animation only for dynamic, interruptible or gesture-driven motion.
- **STD-performance-properties-14** (should): if Motion is not already installed, detect viewport entry with IntersectionObserver instead of adding Motion for `useInView`.
- **STD-process-review-taste-65** (should): learn CSS transforms, transitions and keyframes before reaching for Motion.
- **STD-visual-details-55** (must): name the task, then recommend one library from the curated list in one sentence.
- **STD-visual-details-56** (must): read `package.json` first; use a listed library the project already has, and flag (not replace) a competitor it uses.
- **STD-visual-details-57** (must): never hand-roll standard components; toasts with Sonner, command menus with cmdk, dropdowns with Base UI.
- **STD-visual-details-59** (must): animate numbers with NumberFlow, not by re-rendering text.
- **STD-visual-details-61** (must): shared state in zustand, not a web of per-component `useState` and props.
- **STD-visual-details-62** (must): conditional classes with clsx, or cva when a component has real variants; never three nested template-literal ternaries.

**Properties and performance**

- **STD-performance-properties-01** (must): animate movement, size and visibility with `transform` and `opacity` only; never `width`, `height`, `margin`, `padding`, `top` or `left`.
- **STD-performance-properties-02** (must): the only exceptions are `clip-path`, accordion height, and `width` on an absolutely positioned element with no children (a tab pill, a progress fill).
- **STD-performance-properties-06** (must): never `transition: all` (or Tailwind's `transition-all`); list the exact properties.
- **STD-performance-properties-09** (must): in Motion, animate the full transform string, not the `x`, `y` or `scale` shorthands.
- **STD-performance-properties-10** (must): per-frame values (drag, scroll, pointer) go to `ref.current.style` or a Motion value, never React state.
- **STD-performance-properties-11** (must): set drag transforms directly on the moving element, never through a CSS variable on a parent or container.
- **STD-performance-properties-12** (should): add `will-change: transform` only as the fix for an element you have seen shift or jitter.
- **STD-performance-properties-16** (must): dropped frames fail review (60fps, or 120fps where the display supports it).
- **STD-performance-properties-17** (must): virtualize long lists and large tables; never render 1,000+ rows directly.
- **STD-performance-properties-24** (should): when a hover effect flickers, animate a child instead of the hovered parent.
- **STD-enter-exit-origin-30** (must): keep any animated `blur()` under 20px.

**Entering, leaving and interrupting**

- **STD-springs-gestures-15** (must): anything that can be triggered rapidly or reversed mid-motion uses CSS transitions or springs, never `@keyframes`.
- **STD-enter-exit-origin-17** (should): animate mount entry with `@starting-style`, falling back to a `data-mounted` attribute set in `useEffect` after the first render.
- **STD-enter-exit-origin-21** (should): slide an element by its own size with percentages such as `translateY(100%)`, not hardcoded pixels.
- **STD-enter-exit-origin-24** (must): measure content height before animating a collapse; never animate to `auto`.
- **STD-enter-exit-origin-26** (should): reveal part of an element with `clip-path: inset()`, not by animating width, height or an overflow-hidden wrapper.
- **STD-enter-exit-origin-28** (must): fire scroll reveals once, when at least 100px of the element is in view.
- **STD-enter-exit-origin-42** (should): animate a tab color change by clipping a duplicated, active-styled tab list.
- **STD-enter-exit-origin-44** (should): build a theme-switch reveal with the View Transitions API, not by duplicating the page.
- **STD-enter-exit-origin-10** (must): delay only the first tooltip; neighbours open instantly (Base UI: `transition-duration: 0ms` on `[data-instant]`).
- **STD-visual-details-26** (must): write curves and durations as the project's tokens (`var(--ease-out)`), never hand-typed; see the [[synthesis/design-systems-and-tokens|Design systems and tokens synthesis]].

**Media queries and accessibility**

- **STD-accessibility-motion-01** (must): ship the `prefers-reduced-motion` variant and the hover gating in the same change as the animation.
- **STD-accessibility-motion-02** (must): reduced motion is gentler, never zero: drop movement, keep a short opacity cross-fade and the color changes that explain state.
- **STD-accessibility-motion-11** (must): `prefers-reduced-transparency: reduce` makes translucent surfaces solid or frostier.
- **STD-accessibility-motion-12** (must): `prefers-contrast: more` gets near-solid surfaces with a defined border.
- **STD-accessibility-motion-15** (must): every `:hover` animation (and, on mobile web, every `:hover` style) goes inside `@media (hover: hover) and (pointer: fine)`; `:active` stays ungated.
- **STD-accessibility-motion-17** (should): a visual-only duplicate layer is `aria-hidden`, with `tabIndex={-1}` on buttons inside it.
- **STD-accessibility-motion-13** (must): respect the user's text size; on the web write spacing in rem or em.
- **STD-accessibility-motion-27** (must): never disable pinch zoom; fix the input's font size instead.

**Mobile web**

- **STD-mobile-touch-02** (must): detect touch with media queries and platform features, never user-agent strings, screen width or a JavaScript touch check.
- **STD-mobile-touch-21** (must): ship the mobile baseline before the first component: the full viewport meta, one theme-color per scheme, `-webkit-tap-highlight-color: transparent`, `-webkit-text-size-adjust: 100%` and `overscroll-behavior: none` on `html`, 16px inputs, `touch-action: manipulation` and `user-select: none` on controls, and gated hover.
- **STD-mobile-touch-10** (must): `height: 100dvh` for app shells, drawers and bottom-pinned UI; `min-height: 100svh` for marketing heroes; never `100vh` or `lvh`.
- **STD-mobile-touch-11** (must): input, textarea and select text at 16px or more (at least under `@media (pointer: coarse)`).
- **STD-mobile-touch-16** (must): `viewport-fit=cover` plus `env(safe-area-inset-*)` padding, with a `0px` fallback inside `calc()`.
- **STD-mobile-touch-20** (must): one `theme-color` meta tag per color scheme, matching the top of the page, updated from JavaScript when the theme switches by class.
- **STD-mobile-touch-09** (must): small controls get a 44px touch hit area, grown with a pseudo-element, never by growing the visual.

**React libraries**

- **STD-components-toasts-drawers-02** (must): mount exactly one `<Toaster />`, as close to the app root as possible (in Next.js, `layout.tsx`).
- **STD-components-toasts-drawers-03** (should): keep the Toaster outside any dialog, portal or ancestor with `transform`, `filter` or `overflow`.
- **STD-components-toasts-drawers-04** (must): call `toast()` only from client code; in a server action, return the result and toast on the client.
- **STD-components-toasts-drawers-25** (must): classes on toast parts need `!important` (Tailwind `!`) unless unstyled; go headless once more than a few need it.
- **STD-components-toasts-drawers-33** (must) and **STD-components-toasts-drawers-34** (should): copy Sonner's styles into a shadow root, and import `sonner/dist/styles.css` when toasts render unstyled (Astro, view transitions).
- **STD-components-toasts-drawers-35** (should): expose the toast as a plain `toast()` function with one `<Toaster />`: no hooks, no context.
- **STD-accessibility-motion-25** and **STD-enter-exit-origin-40** (should, from the good-to-have Vaul docs): a controlled Vaul drawer also passes `onOpenChange`; a side drawer that does not touch the edge adjusts `--initial-transform`. Vaul is unmaintained, so flag that before suggesting it as a dependency.

**Process**

- **STD-process-review-taste-41** (must): prototype only in an isolated route or a self-contained HTML file, never in production code.
- **STD-process-review-taste-33** (must): judge touch and gesture motion on a real phone on the local dev server, not a shrunken desktop window.

## What the sources teach

### Pick the cheapest tool

- Walk down the ladder and stop at the first tool that fits: a CSS transition for hover, press and state toggles; `@starting-style` for entry on mount; a CSS animation for predetermined motion that must stay smooth while the page is busy; WAAPI for programmatic control without a library; Motion only for springs, layout animations, exit animations and gesture-driven values [S-L19-018] ([[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]). The library list says the same: do not reach for Motion for a simple hover or fade [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).
- The reason is the main thread. CSS animations keep running when the browser is busy, while `requestAnimationFrame`-driven animations drop frames. At Vercel, the dashboard tab animation used Framer Motion's shared layout animations and dropped frames during page loads; switching to CSS fixed it [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]). Hence CSS for predetermined motion, JavaScript for dynamic and interruptible motion [S-L19-032] ([[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]])[S-L19-033].
- WAAPI keeps JavaScript control with CSS performance, for example a clip-path reveal with `{ duration: 1000, fill: 'forwards', easing: 'cubic-bezier(0.77, 0, 0.175, 1)' }` [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]). Emil used WAAPI so that all the animation logic sat in one place [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- Learn CSS first. animations.dev teaches transforms, transitions and keyframes before moving to Motion for complex components [S-L19-002] ([[sources/adev-home-animations-dev|animations.dev]]). Its CSS module runs transforms, transitions, keyframe animations (a blinking cursor, an orbit with 3D transforms), then clip-path; its examples moved from `framer-motion` to the `motion/react` import [S-L19-001] ([[sources/adev-changelog-animations-dev|animations.dev]]).
- For viewport entry, use IntersectionObserver unless Motion is already in the project, because Motion is "quite heavy" [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- GSAP code appears only in the practitioner videos: Kole builds his load animations with GSAP timelines, `to` and `fromTo` steps, the `"<"` marker to run a step alongside the previous one, `stagger`, and paused timelines played later [S-L19-071] ([[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]). GSAP is not on the curated list [S-L19-029], though recon lists it as a stack to recognise [S-L19-027] ([[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]]).

### Animate cheap properties, and keep frames out of React

- The performance cheatsheet: animate `transform` and `opacity`, not `width` or `top`; virtualize long lists; keep animated `blur()` under 20px; in Motion animate the full `transform` string, not `x` or `y`; never `transition: all`; write per-frame values to `ref.current.style`, not state; add `will-change: transform` only once you see an element shift 1px as motion starts [S-L19-013] ([[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]]).
- Motion's `x`, `y` and `scale` shorthands run on the main thread and drop frames under load; `animate={{ transform: "translateX(100px)" }}` stays smooth [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]])[S-L19-023].
- Drag without re-renders, and put the transform on the moving element itself. Vaul's drag first set a `--swipe-amount` CSS variable read by `translateY()`; past about 20 list items it lagged, because a changed CSS variable is inherited and makes every child recalculate its styles. Setting `transform: translateY(...)` directly on the element fixed it [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).
- When a hover effect flickers, animate a child instead of the hovered parent; small buttons get a 44px hit area from a pseudo-element [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]).
- Use `clip-path` rather than width, height or wrapper elements to hide and show parts of an element: it changes no layout and needs no extra DOM. A before-and-after slider clips the top image with `inset(0 50% 0 0)` and updates the right edge from the drag [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]). Vercel's security page uses clip-path; Tuple uses the less performant width approach [S-L19-010].
- Long lists of 1,000+ rows are virtualized with Virtuoso [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).

### Entering, leaving and interrupting

- Transitions retarget; keyframes restart. In Sonner's demo, toasts added quickly with keyframes make older toasts jump into place, while transitions move them smoothly [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]). So toasts, toggles and anything that can fire twice in a second use transitions [S-L19-018] ([[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]).
- Entry on mount: `@starting-style` where supported, else render the start state, set a mounted flag in `useEffect` and style from `data-mounted` [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]])[S-L19-023]. Sonner itself was built with the mounted flag, and Emil says `@starting-style` would make it much simpler [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- Style states through data attributes: Sonner uses `data-mounted`, `data-expanded` and `data-front` [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]); the recipes use `[data-starting-style]`, `[data-ending-style]`, `[data-closed]` and `[data-visible]` [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]); Base UI marks neighbouring tooltips with `data-instant`, which get `transition-duration: 0ms` [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]).
- Let JavaScript measure and CSS compose. Sonner passes per-toast numbers to CSS as custom properties (`--offset`, `--lift-amount`, `--toasts-before`) and builds the stacked transform in CSS, each toast behind the front one scaled down by 0.05 per step [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- Move elements by their own size with percentages (`translateY(100%)` for toasts and drawers, whatever their height) [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]])[S-L19-023]. Kole's GSAP code does the same with `yPercent: 100` [S-L19-071] ([[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]).
- Scale popovers and dropdowns from their trigger with the library's variable: `var(--radix-dropdown-menu-content-transform-origin)` in Radix, `var(--transform-origin)` in Base UI [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]); modals stay centered [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]).
- Scroll reveals fire once: IntersectionObserver, or Motion's `useInView` with `{ once: true, margin: "-100px" }` [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]). For a reveal that follows scroll position, map `useScroll` progress (offset `["start end", "end end"]`) through `useTransform` onto a clip inset, and keep it a motion value end to end with `useMotionTemplate` instead of copying it into a plain variable [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- Tabs whose active state changes color: duplicate the list, style the copy as active, clip it to the active tab with `inset(... round 17px)` computed from `offsetLeft` and `offsetWidth`, and animate the clip. Hide the copy with `aria-hidden` and `tabIndex={-1}`, and build on an accessible tabs primitive in production [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]). The course's Hold to Delete exercise hides its overlay copy the same way [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- A theme-switch reveal is better built with the View Transitions API than by duplicating the page [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]). The vocabulary skill names the CSS pieces behind such effects: fill mode `forwards`, perspective, clip-path versus mask (a mask gives soft edges), view transitions and scroll-driven animation [S-L19-019] ([[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]).
- Depth without JavaScript: `rotateX()`/`rotateY()` inside a `transform-style: preserve-3d` wrapper, for example an orbit at `translateZ(72px)` [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).
- Springs in Motion are written Apple-style as `{ type: "spring", duration: 0.5, bounce: 0.2 }` or with physics values (`mass: 1, stiffness: 100, damping: 10`) [S-L19-018] ([[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]); the house prefers the first form (STD-springs-gestures-02). See the [[synthesis/spring-animation|Spring animation synthesis]].

### Media queries: hover, motion, transparency, contrast

- Gate hover with both conditions, `@media (hover: hover) and (pointer: fine)`, and give touch users `:active` feedback instead. `(pointer: fine)` rules out styluses and the odd Android device that claims hover. Do not detect touch with a `useIsTouchDevice()` hook [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]). In Tailwind v4 the `hover:` variant already compiles to `@media (hover: hover)`; in v3 set `future.hoverOnlyWhenSupported` [S-L19-028].
- Reduced motion: under `@media (prefers-reduced-motion: reduce)` keep opacity and color (the example is `animation: fade 0.2s ease`) and drop transform-based movement; in React read `useReducedMotion()` and swap moving values for static ones [S-L19-018] ([[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]). The apple-design sample turns a sheet into `transition: opacity 200ms ease; transform: none` [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Reduced transparency and contrast are separate signals: a translucent toolbar (`rgba(255, 255, 255, 0.6)`, `backdrop-filter: blur(20px) saturate(180%)`, a 1px `rgba(255, 255, 255, 0.4)` top border) becomes solid white with no backdrop filter under `prefers-reduced-transparency: reduce`, and surfaces get near-solid backgrounds with a border under `prefers-contrast: more` [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Mouse-following effects need a backup for tablet and phone [S-L19-069] ([[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]). Neither of Kole's build videos covers reduced motion [S-L19-069][S-L19-071].

### The mobile web baseline

- Before the first component: the viewport meta `width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content`; `-webkit-text-size-adjust: 100%`; `-webkit-tap-highlight-color: transparent` on `html` with an `:active` state on every tappable element; `touch-action: manipulation` and `user-select: none` on controls (never on `body`) [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- Heights: `100dvh` for app shells, drawers and bottom-pinned UI, `100svh` for heroes, with an old `100vh` line above only if the support matrix needs it [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- Inputs at 16px (1rem at the default root size), or 16px only under `@media (pointer: coarse)` if desktop wants smaller text; never `user-scalable=no` or `maximum-scale=1` [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- Scrolling: `overscroll-behavior: none` on the root for apps (keep pull-to-refresh on scrolling documents) and `contain` on inner scrollables; `touch-action: pan-y` on a horizontal gesture carousel, `pan-x` on a vertical sheet handle, `none` only where the gesture owns every axis [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- Safe areas and browser color: `env(safe-area-inset-*)` padding on fixed bars, toasts and sheets (with `env(safe-area-inset-bottom, 0px)` inside `calc()`); one `theme-color` per `prefers-color-scheme` plus `<meta name="color-scheme" content="light dark">`, set in Next.js through the `viewport` export's `themeColor` [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- The on-screen keyboard: Vaul listens to `visualViewport` resize in an effect (removed in its cleanup) and sets the drawer's height and bottom from it, accepting a slight delay [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]). Emil also tried stepping the `theme-color` tag through 50 interpolated colors every 10ms to follow the drawer overlay, but has not shipped it because it falls out of step when frames drop [S-L19-005].
- Test drawers on a physical phone, opening the local dev server by the computer's IP address, with Safari's devtools attached [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).

### React libraries: mount once, call from anywhere

- Sonner: render `<Toaster />` at the root of the app and call `toast()` from a button's `onClick` [S-L19-088] ([[sources/sonner-home-sonner|Sonner]]). The docs mount it in the root `layout.tsx` after `{children}` and note it can sit inside a server component [S-L19-087] ([[sources/sonner-getting-started-getting-started-sonner|Getting Started – Sonner]]).
- The house skill adds the failure cases: call `toast()` only on the client and never inside a server action; never mount a Toaster in both a layout and a page; under React StrictMode a toast fired in an effect can appear twice, so fire it from the event handler or pass a stable `id`; keep the Toaster out of dialogs, portals and ancestors with `transform`, `filter` or `overflow` [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]).
- Theming: wrap the Toaster in a `'use client'` component that passes `resolvedTheme` from next-themes [S-L19-092] ([[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]); the curated list names next-themes for theme switching without a flash on load [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).
- Options: shared options on `<Toaster />`, per-toast options in `toast()`'s second argument, and per-toast options win [S-L19-091] ([[sources/sonner-toast-toast-sonner|Toast – Sonner]]). Part classes (`toast`, `title`, `description`, `actionButton`, `cancelButton`, `closeButton`) need `!important` unless the toast is unstyled; `testId` renders as `data-testid` for end-to-end tests [S-L19-021] ([[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]). Tailwind users add the `!` prefix, and the preferred class-based route is headless [S-L19-090] ([[sources/sonner-styling-styling-sonner|Styling – Sonner]]).
- Outside the happy path: read toasts with `useSonner()` inside React and `toast.getActiveToasts()` outside it; import `sonner/dist/styles.css` in Astro with view transitions; inside shadow DOM, copy the `<style>` tags containing `[data-sonner-toaster]` into the shadow root [S-L19-089] ([[sources/sonner-other-other-sonner|Other – Sonner]]).
- Why the API looks like that: a plain `toast()` backed by an observer pattern that `<Toaster />` subscribes to, so no hooks or context are needed; toasts render as an `<ol>` of list items keyed by id; a `useIsDocumentHidden` hook pauses the timer in a hidden tab [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]). See the [[synthesis/toasts-and-notifications|Toasts and notifications synthesis]].
- Vaul (good-to-have, unmaintained): compound parts `Drawer.Root`, `Trigger`, `Portal`, `Overlay`, `Content`, `Handle`, `Title`, `Description`, `Close`, portalled into `document.body` by default [S-L19-093] ([[sources/vaul-api-api-reference-vaul|API Reference – Vaul]]); a `'use client'` starter styled with utility classes, an overlay of `fixed inset-0 bg-black/40` and content pinned with `fixed bottom-0 left-0 right-0` [S-L19-095] ([[sources/vaul-getting-started-getting-started-vaul|Getting Started – Vaul]]); the `direction` prop for side drawers, `--initial-transform` when a drawer does not touch the edge, and `open` with `onOpenChange` for a controlled drawer [S-L19-094] ([[sources/vaul-default-default-vaul|Default – Vaul]]). Emil built it on Radix's Dialog with an API that mirrors it, so it feels familiar [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]). See the [[synthesis/drawers-and-sheets|Drawers and sheets synthesis]].
- Picking libraries: name the task, read `package.json`, recommend one pick in one sentence, and do not churn an installed competitor. The list: base-ui (dialogs, popovers, menus, selects), cmdk, Sonner, input-otp, motion, NumberFlow, Virtuoso, zustand, clsx and cva, next-themes, dnd kit, recharts and others [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).

### Tailwind, layout and effect details (practitioner opinion)

- Steve Schoger, building a page with Claude Code and Tailwind: use an outer ring of gray 950 at 10% instead of a solid border; because a ring made one button 2px taller than its neighbour, wrap it in a `span` with `inline-flex p-px` and keep the shadow on the button, not the span; put an inset ring on top of a screenshot; set text widths in `ch` on the same element that sets the font size (40ch for his headings); use `text-wrap: pretty`, or `balance` when pretty still wraps badly [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]). He admits he does not fully understand the span trick, and its code is in a Tailwind Play link, not the transcript [S-L19-103].
- Fluid type: Kole's one-line formula scales a size linearly from a 320px to a 1920px wide screen, capped with `max()` and `min()` [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]); the apple-design display style uses `clamp(2rem, 5vw, 4rem)` [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Kole's GSAP code-along: a fixed full-screen loading overlay (top and left 0, `100vw` by `100vh`, z-index 10, flex centering); hidden start states set in CSS or with `gsap.set`; a pill navbar that scales from 0, then animates `max-width` from its measured height (27px from `gsap.getProperty`) to 500px; `max-width` alone did nothing until `width: 100%` was added; a wipe block that sometimes needs `left: auto` next to `right: 0` [S-L19-071] ([[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]).
- Kole's five web animation types and how each is built: a preloader that slides up while the content and background under it move; a masked button hover; text highlighted on scroll by a two-color gradient with its stops almost together, masked by the text and moved with scroll; a slow icon on a semicircle path; a call to action centered on the tracked mouse position [S-L19-069] ([[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]).

### Prototyping and auditing code

- Prototypes live on an isolated route such as `/prototypes/<slug>` with one file per variant and a small harness, or in one self-contained HTML file when there is no project [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]). The variant picker's reference wiring is vanilla JS; in a framework, keep its class names and behavior but use state instead of `innerHTML`, a keyed re-mount instead of `requestAnimationFrame`, and refs plus a layout effect to measure the highlight [S-L19-030] ([[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]).
- Audits start with a grep sweep for `transition`, `animation`, `@keyframes`, `motion.`, `animate={`, `useSpring`, `ease-in`, `transition: all`, `scale(0)`, `prefers-reduced-motion` and `transform-origin` [S-L19-027] ([[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]]). Hunting for missed motion looks for conditional renders with no transition (`{isOpen &&`, `display: none` toggles), `onClick` elements with no `:active`, and `.map(` renders of entering lists [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]). The audit's concrete patterns are the same ones listed above (`@starting-style`, the `data-mounted` fallback, the transform-origin variable, gated media queries, percentage translates and `clip-path: inset()`) [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]).

## Where they agree and disagree

**Between the sources**

- `will-change`: the cheatsheet says add it only once you see the 1px shift [S-L19-013], and Agents with Taste uses it as the fix for jittery motion [S-L19-004]; both are reactive. The apple-design skill says to hint with `will-change` "where motion is imminent" [S-L19-020], which reads as pre-emptive. STD-performance-properties-12 takes the reactive side.
- Motion shorthands: three skills ask for the full transform string [S-L19-013][S-L19-018][S-L19-033], but the apple-design spring sample is `animate(el, { y: 0 }, { type: 'spring', ... })` [S-L19-020]. Follow STD-performance-properties-09 [inferred].
- Built-in keywords: the house wants `var(--ease-out)` (STD-easing-duration-02), as the recipes use [S-L19-017], but the apple-design press sample uses `100ms ease-out` [S-L19-020] and the tooltip snippet in 7 Practical Animation Tips uses `0.125s ease-out` [S-L19-003] [inferred comparison].
- CSS variables during a drag: the toast article sets `--swipe-amount` on the toast from the pointer handler [S-L19-006]; the drawer article found that same pattern laggy once children multiply [S-L19-005]. STD-performance-properties-11 follows the drawer article. The toast article sets the variable on the toast itself, which has few children, so it may never have hit the problem [inferred].
- Mount flag versus `@starting-style`: the toast article used the flag and considered switching [S-L19-006]; the later skills put `@starting-style` first with the flag as fallback [S-L19-017][S-L19-023]. This is the same advice over time.
- Where the Toaster goes: the skill says as close to the root as possible [S-L19-022]; the docs say it need not sit in a particular place [S-L19-087]. The skill's reason (stacking contexts can hide or clip toasts) is why STD-components-toasts-drawers-02 and -03 follow it.
- Tailwind hover: the mobile-native skill says both `(hover: hover)` and `(pointer: fine)` matter, then says Tailwind v4's `hover:` variant already compiles to `(hover: hover)` [S-L19-028]. That variant alone leaves out `(pointer: fine)`, so it does not fully meet STD-accessibility-motion-15 [inferred].
- Radix or Base UI: the drawer and clip-path articles build on Radix Dialog and Radix Tabs [S-L19-005][S-L19-010]; the curated list names base-ui for unstyled accessible components [S-L19-029]. STD-visual-details-55 follows the list.
- Kole's GSAP load animations against the house standards: the navbar animates `max-width` on an element with children (STD-performance-properties-01); the wipe block animates `width`, which may fall under the childless, absolutely positioned exception of STD-performance-properties-02 [inferred]; steps of 1.3s pass the 1s cap unless a marketing load animation counts as illustrative (STD-easing-duration-09) [inferred]; the big moves use `expo.inOut` where entrances and exits call for ease-out (STD-easing-duration-01); the overlay is `100vh` (STD-mobile-touch-10); and there is no reduced-motion variant (STD-accessibility-motion-01) [S-L19-071].
- Schoger's low-opacity ring instead of a solid border [S-L19-103] agrees in spirit with STD-visual-details-14 (a semi-transparent shadow rather than a solid, opaque border) [inferred]. His `ch` widths agree with the 65ch cap for body text (STD-visual-details-01); the 40ch value is his heading choice.

**With OpenDesigner's existing research**

- Web delivery, DC-L10-18: CSS custom properties as the runtime token layer, media queries for preferences (including `prefers-reduced-transparency`, which the card notes is not Baseline), and `pointer` and `hover` queries. This agrees with the house media-query rules [S-L19-020][S-L19-028]. The card's default also sends component responsiveness to container queries, which none of the sources mention.
- Component base, DC-L08-03: the React default is "shadcn on Base UI or React Aria". `standards.json` records the conflict with STD-visual-details-55: React Aria is outside the curated list, whose pick is base-ui [S-L19-029].
- Component API, DC-L08-04: props for leaf components, compound parts for containers. Vaul's compound drawer [S-L19-093] and its Radix-like API [S-L19-005] agree. Sonner's plain `toast()` function [S-L19-006] is a third style, an imperative call, that the card does not list [inferred].
- Implementation technology, DC-L10-19: framework components when one framework dominates, web components when many consume the system. The sources are React-first; a web-component host that renders Sonner inside shadow DOM has to copy its styles in by hand [S-L19-089] [inferred link].
- Interruptibility, DC-L04-24: the card marks "CSS transitions reverse from their current value, while keyframe animations do not" as inferred; Sonner's demo now supports it [S-L19-006].
- Engine conflicts that `standards.json` already records: `engine.py review` answers `transition: all 300ms` with a duration fix and never flags the `all` (STD-performance-properties-06), and never flags animated layout properties (STD-performance-properties-01); the generated `preview.html` has ungated `:hover` rules (STD-accessibility-motion-15) and a viewport meta without `viewport-fit=cover` or `interactive-widget=resizes-content` (STD-mobile-touch-21); the CSS export writes spacing in px while font sizes are rem (STD-accessibility-motion-13); and the preview's inputs use a 14px body style (STD-mobile-touch-11). The stage 24 default for Q-token-04 also keeps "spacing scales with text size" as a toggle that is off by default, which fits the same conflict [inferred].
- Stage 05's delivery default emits tokens as CSS variables, Tailwind `@theme` and the shadcn contract. Tailwind is also what the practitioner and Vaul examples use [S-L19-103][S-L19-095] [inferred].

## Decisions this informs

- **Q-plat-08** (what the UI is built with): the house web skills assume React [S-L19-018] and give Next.js specifics [S-L19-022][S-L19-028]; React Native has separate skills [S-L19-018].
- **Q-tool-02** (how engineers use the system): Tailwind utilities need the `!` prefix on toast classes and a hover gate [S-L19-090][S-L19-028]; headless primitives from base-ui [S-L19-029].
- **Q-comp-01** (component base): base-ui for dialogs, popovers, menus and selects, Sonner for toasts, never hand-rolled (STD-visual-details-55, STD-visual-details-57) [S-L19-029]; drawers on an accessible dialog primitive [S-L19-005].
- **Q-comp-03** (props or smaller parts): compound parts for containers such as drawers [S-L19-093]; a plain function for toasts [S-L19-006].
- **Q-token-04** (px, plain numbers or rem): spacing in rem or em so layout follows text size (STD-accessibility-motion-13) [S-L19-020]; inputs at 1rem [S-L19-028].
- **Q-token-08** (build tool and web delivery): recipes consume curves as `var(--ease-out)` custom properties [S-L19-017].
- **Q-motion-07** (reduced motion): replace movement with a 200ms fade, never remove all feedback [S-L19-018][S-L19-020].
- **Q-motion-10** (device settings to follow): reduced transparency and increased contrast as separate media queries [S-L19-020].
- **Q-motion-06** (screen changes and staggered lists): the CSS stagger recipe with 50ms steps [S-L19-017].
- **Q-state-04** (hover and pressed by device): gate hover, keep `:active` ungated [S-L19-028].
- **Q-state-05** (showing the picked tab): the clipped duplicate tab list [S-L19-010].
- **Q-theme-01** (light and dark): one `theme-color` per scheme and the `color-scheme` meta [S-L19-028]; next-themes and a themed Toaster [S-L19-029][S-L19-092].
- **Q-depth-01** (how surfaces stand out, `ring-shadow` option): the Tailwind ring technique [S-L19-103].
- **Q-depth-04** (glass): the translucent toolbar and its reduced-transparency fallback [S-L19-020].
- **Q-depth-06** (scrim): Vaul's `bg-black/40` overlay [S-L19-095].
- **Q-space-03** (target size): a 44px pseudo-element hit area [S-L19-004].
- **Q-type-14** and **Q-type-15** (text width and fluid sizes): `ch` on the font-size element and `text-wrap` [S-L19-103]; the capped fluid formula and `clamp()` [S-L19-042][S-L19-020].
- **Q-pattern-01** (dialog, sheet or pop-up): on mobile, a drawer instead of a modal [S-L19-005].
- **Q-form-04** (where messages appear): if toasts are used, Sonner mounted once at the root [S-L19-022].
- **Q-dist-03** (catching rule breaks): the audit grep sweep [S-L19-027] and the opportunity sweep [S-L19-024].
- **Q-pref-02** (reviewing and trying versions): the isolated prototype route and picker [S-L19-031][S-L19-030].

## Visual examples worth showing

- **Keyframes versus transitions**: toasts added quickly, jumping with keyframes and gliding with transitions [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- **The toast stack**: three toasts at `Y(0) scale(1)`, `Y(-14px) scale(0.95)` and `Y(-28px) scale(0.9)` [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- **CSS variable versus direct transform**: a drawer with 20+ list items dragged both ways, with frame drops visible on the first [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).
- **Motion shorthand versus transform string under load**: `animate={{ x: 100 }}` next to `animate={{ transform: "translateX(100px)" }}` while the page is busy [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]).
- **Before-and-after slider**: Raycast's red and blue wallpapers split by `clip-path: inset(0 50% 0 0)` following the handle [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- **Clipped tabs**: Payments, Balances, Customers and Billing with the "Toggle clip path" button showing the hidden duplicate list [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- **Origin-aware popover**: the same popover scaling from its center and from its trigger [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]).
- **Hover on a phone**: an ungated `:hover` stuck after a tap next to a gated one with `:active` feedback [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- **Viewport units**: `100vh`, `100dvh` and `100svh` boxes as the browser toolbar shows and hides [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- **Glass and its fallbacks**: the translucent toolbar, then the same toolbar under reduced transparency and increased contrast [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- **Ring versus border**: a button with a solid border next to one with a 10% gray 950 ring and a shadow, and the 2px height difference fixed by the `span` wrapper [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- **A CSS 3D orbit**: an element circling at `translateZ(72px)` inside a `preserve-3d` wrapper, no JavaScript [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).
- **Kole's load animations**: the loading screen sliding up with the hero text, the navbar growing from a dot to a circle to a pill, and the text wipe [S-L19-071] ([[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]).
- **Five kinds of web animation**: entrance, hover, scroll, loop and mouse, each in its subtle form [S-L19-069] ([[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]).

## Open questions

- Should `engine.py review` flag `transition: all`, animated layout properties and ungated `:hover` in the person's code, as the standards require? The gaps are recorded in `standards.json` but not fixed.
- Does Tailwind v4's `hover:` variant satisfy STD-accessibility-motion-15, or should OpenDesigner's Tailwind export add a custom variant with `(pointer: fine)` [inferred]? DC-L19-184 proposes the custom variant, and also pointing Tailwind's own easing and the bare `transition` class's default curve at the house curves; the engine does neither yet.
- What should OpenDesigner recommend for web drawers? Vaul is unmaintained, the curated list names no drawer library [S-L19-029], and STD-visual-details-57 says not to hand-roll standard components.
- Should the CSS export ship ready recipes (`@starting-style` with a `data-mounted` fallback, the gated hover block, the reduced-motion block), or only tokens?
- Container queries are the DC-L10-18 default for component responsiveness and a Q-layout-06 option, but no source here speaks to them. Is there a house view?
- When a project already uses GSAP (as Kole's code does [S-L19-071]), STD-visual-details-56 says keep it. Which house rules need a GSAP translation (for example, `transform`-only tweens and custom curves in place of `expo.inOut`) [inferred]?
- Is Kole's `max()`/`min()` fluid formula [S-L19-042] compatible with STD-accessibility-motion-13, given a pure viewport-based size ignores the user's text setting? A `clamp()` with rem ends [S-L19-020] keeps it at the limits [inferred]. DC-L19-31 proposes rem ends plus a rem term in the middle value.
