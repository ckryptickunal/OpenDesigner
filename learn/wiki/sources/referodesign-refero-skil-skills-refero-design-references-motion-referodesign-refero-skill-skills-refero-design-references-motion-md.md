---
type: source
title: "referodesign/refero_skill: skills/refero-design/references/motion.md"
created: 2026-10-07
updated: 2026-10-07
video_id: referodesign-refero-skil-skills-refero-design-references-motion
url: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/motion.md
channel: referodesign/refero_skill (GitHub, MIT)
published: commit a9b54a3
authority: reference
tags:
  - motion
  - easing
  - duration
  - motion-tokens
  - reduced-motion
  - springs
  - micro-interactions
  - refero
---

# referodesign/refero_skill: skills/refero-design/references/motion.md

## Metadata

- Page ID: `referodesign-refero-skil-skills-refero-design-references-motion`
- Publisher: referodesign/refero_skill (GitHub, MIT)
- Published: commit a9b54a3
- URL: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/motion.md

## Summary

Refero's motion guide for product UI says every animation must serve feedback, continuity or hierarchy, or be removed. It orders motion as a pyramid from micro feedback to rare expressive motion, and gives purpose-based duration bands, enter/exit/change easing curves, spring settings, and concrete specs for buttons, inputs, lists, modals and drawers. It defines a minimum and a complete set of motion tokens with a component mapping, and makes a reduced-motion variant mandatory. It ends with anti-patterns (slow hovers, linear easing, transition: all, endless loops) and a pre-ship checklist. For a design system it supplies ready duration, easing, distance and spring token values and the rules for applying them.

## Key Ideas

- Every animation must provide feedback, continuity or hierarchy; otherwise remove it
- Decide context first: product UI is subtle and fast, marketing can be more expressive
- Higher-frequency and smaller-distance actions get shorter durations
- Start with micro feedback; add state transitions, layout continuity and expressive motion only when justified
- Use duration bands by purpose rather than one duration for everything
- Ease-out for entering, ease-in for exiting, ease-in-out for state changes
- Springs suit drag, swipe and physical elements but must settle quickly
- Define motion tokens for durations, easings and distances to keep a team consistent
- Always ship a prefers-reduced-motion variant: swap slide and scale for fades, remove parallax
- Never use transition: all; list the animated properties
- Set transform-origin to where the element comes from
- Animations must be interruptible by user input
- In product UI nothing should exceed 500ms

## Entities

- [[entities/refero|Refero]] (company): Publisher of the refero_skill repo this guide comes from
- [[entities/motion-framer-motion|Motion / Framer Motion]] (library): Suggested React library for layout animations, springs and variants
- [[entities/web-animations-api|Web Animations API]] (library): Native, dependency-free animation option
- [[entities/gsap|GSAP]] (library): Heavy but powerful library for complex timelines and marketing
- [[entities/rive|Rive]] (tool): Interactive illustrations and icons, suggested for empty states and onboarding
- [[entities/lottie|Lottie]] (library): Illustrative animations; watch file size and export quality
- [[entities/material-design-motion|Material Design Motion]] (product): Listed resource; the standard easings are described as Material-inspired
- [[entities/apple-hig-motion|Apple HIG Motion]] (product): Listed resource for platform conventions and reduced-motion criteria
- [[entities/prefers-reduced-motion|prefers-reduced-motion]] (concept): Media query the guide requires a variant for

## Topics

- [[topics/motion-principles|Motion principles]]: Motion must serve feedback, continuity or hierarchy; the motion pyramid; context first; anti-patterns.
- [[topics/easing-and-timing|Easing and timing]]: Duration bands (90-150, 160-240, 240-360, 360-500ms), duration and easing tokens, and enter/exit/change curves.
- [[topics/spring-animation|Spring animation]]: Use springs for gestures and physical elements; snappy, smooth and bouncy stiffness/damping presets; must decay quickly.
- [[topics/reduced-motion|Reduced motion]]: Mandatory reduced-motion variant: fade only instead of slide or scale, remove parallax, pause loops; token overrides and a CSS shortcut.
- [[topics/micro-interactions|Micro-interactions]]: Specs for hover, press, focus, input focus/error/success, and list add/remove animations.
- [[topics/animation-performance|Animation performance]]: transition: all causes layout recalculation; test on slower devices; animate reorder only if performant.
- [[topics/modals-and-popovers|Modals and popovers]]: Overlay fades 200ms in and 150ms out; modal fades and scales from 0.95; dropdown transform-origin at the trigger corner.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Minimum and complete motion token sets with component mapping.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: CSS transition examples, SVG transform-box fix, and library choice for React/Next.

## Notable Claims

- 500ms or more in product UI almost always feels slow. Evidence: Timing Rules: 500ms+ in product UI almost always feels slow
- Linear easing feels robotic and unnatural. Evidence: Anti-Patterns: Linear easing
- 300-600ms on hover or buttons feels sluggish. Evidence: Anti-Patterns: Red Flags
- transition: all animates unintended properties, causes layout recalculation every frame and hurts performance on low-end devices. Evidence: Why transition: all is dangerous
- Transforms on SVG elements behave differently and need a wrapping g with transform-box: fill-box. Evidence: SVG Animation
- For most SaaS products CSS plus Motion is sufficient. Evidence: Libraries and Tools
- The standard easing tokens are Material-inspired. Evidence: Appendix: Standard (Material-inspired)

## Quotes

> When in doubt — shorter, subtler, or none.

> Motion that doesn't serve function is noise.

> Spring must decay quickly. No prolonged "jello" effect.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Opinionated guide from Refero's design skill; values are presented as defaults, not measured research.
- Caveat: Easing curves are described as Material-inspired; the source does not cite the Material spec version.
- Caveat: Spring presets are Framer Motion / Motion parameters and do not transfer directly to other spring APIs [inferred].
- Caveat: The 0.01ms reduced-motion shortcut removes all motion including fades, which differs from the guide's own fade-only recommendation [inferred].

### Rules and practices

- **must** (motion, all): Remove any animation that does not provide feedback, continuity or hierarchy, or whose removal would not hurt the UX. Why: Motion that doesn't serve function is noise. [Motion serves three purposes; Quick Test]
- **should** (motion, all): Use 90-150ms for hover, press, toggle and focus; 160-240ms for accordions, tabs and small panels; 240-360ms for modals, drawers and route transitions; 360-500ms only for rare large layout reflows. Why: Purpose-based categories instead of 500ms for everything. Values: 90–150ms, 160–240ms, 240–360ms, 360–500ms. [Duration Reference]
- **should** (motion, all): Make smaller-distance and higher-frequency actions shorter; make anything users do 100 times a day instant. Why: Timing rules. Values: 100x/day. [Timing Rules]
- **must** (motion, all): Keep every product UI animation at or under 500ms. Why: 500ms+ almost always feels slow. Values: 500ms. [Pre-Ship Checklist: Nothing exceeds 500ms]
- **should** (motion, css): Use ease-out for elements entering, ease-in for elements exiting and ease-in-out for state changes, with cubic-bezier(0.0, 0.0, 0.2, 1), cubic-bezier(0.4, 0.0, 1, 1) and cubic-bezier(0.4, 0.0, 0.2, 1). Why: Enter: fast start, soft landing; exit: soft start, fast exit; change: smooth both ways. Values: cubic-bezier(0.0, 0.0, 0.2, 1), cubic-bezier(0.4, 0.0, 1, 1), cubic-bezier(0.4, 0.0, 0.2, 1). [Easing: CSS Tokens]
- **must** (motion, all): Never use linear easing in product UI. Why: Robotic, unnatural. [Red Flags; Pre-Ship Checklist]
- **should** (motion, react): Use springs for drag, swipe, gesture responses and physical-feeling elements, and make them settle quickly; snappy is stiffness 400 / damping 30, smooth is stiffness 200 / damping 20. Why: Springs suit physical motion, but a spring that does not settle reads as jello. Values: stiffness: 400, damping: 30, stiffness: 200, damping: 20. [When to Use Spring]
- **consider** (motion, react): Use the bouncy spring (stiffness 300, damping 15) sparingly. Why: Marked use sparingly. Values: stiffness: 300, damping: 15. [Appendix: SPRINGS]
- **should** (components, all): On buttons, shift background color on hover in 120ms, scale to 0.98 on press in 90-120ms, show the focus ring in 120ms, and do not animate the disabled state. Why: Micro-interactions with maximum effect, minimum risk. Values: 120ms, scale: 0.98, 90–120ms. [Buttons and Controls]
- **should** (components, all): Show a clear loading state on buttons, not just a spinner. Why: Listed in Buttons and Controls. [Buttons and Controls: Loading]
- **should** (components, all): Highlight input focus with border or underline without layout shift; shake on error only on submit, about 200ms, never on every keystroke. Why: Input micro-interaction guidance. Values: 200ms. [Inputs]
- **should** (motion, all): Animate added list rows with a fade plus 4-8px slide over 200ms and removed rows with a fade plus collapse over 180ms; animate reorder only if performant. Why: Lists and Tables guidance. Values: 4–8px, 200ms, 180ms. [Lists and Tables]
- **should** (motion, all): Fade overlays in over 200ms and out over 150ms; fade and scale modals from 0.95 on enter and to 0.95 on exit; slide drawers from and to their edge. Why: Modals and Drawers table. Values: 200ms, 150ms, scale(0.95). [Modals and Drawers]
- **must** (tokens, css): Define motion tokens for durations (120ms / 200ms / 320ms), easings and micro-slide distances (4px / 8px / 16px) and use them instead of random values. Why: Prevents chaos across a team. Values: --duration-fast: 120ms, --duration-default: 200ms, --duration-slow: 320ms, --motion-distance-sm: 4px, --motion-distance-md: 8px, --motion-distance-lg: 16px. [Minimum Token Set]
- **should** (tokens, all): Map hover/press and tooltips to --duration-fast with --ease-out, accordion/tabs to --duration-default with --ease-in-out, and modal/drawer to --duration-slow with --ease-out entering and --ease-in exiting. Why: Component Mapping table. Values: --duration-fast, --duration-default, --duration-slow, --ease-out, --ease-in-out, --ease-in. [Component Mapping]
- **must** (accessibility, all): Always provide a prefers-reduced-motion variant: replace slide or scale plus fade with fade only, make spring bounce instant or a short tween, remove parallax and pause or remove auto-playing loops. Why: Reduced motion is not optional. Values: prefers-reduced-motion: reduce. [Reduced Motion: Not Optional]
- **consider** (accessibility, css): In reduced motion, set fast and default durations to 0ms, slow durations to 100ms and motion distances to 0px. Why: Reference token overrides. Values: 0ms, 100ms, 0px. [Appendix: REDUCED MOTION]
- **must** (motion, css): Never use transition: all; list the transitioned properties explicitly. Why: It animates unintended properties, causes layout recalculation and makes debugging hard. Values: transition: all. [Critical: Never Use transition: all]
- **should** (motion, css): Set transform-origin explicitly for scale and rotate: center for modals and button presses, the trigger corner (top left or top right) for dropdowns, and the edge nearest the trigger for tooltips. Why: The source's common origins place it where the trigger is; scale and rotate need an explicit origin. Values: center, top left, top right. [Transform Origin]
- **should** (motion, css): To transform SVG parts, wrap them in a g with transform-box: fill-box and transform-origin: center. Why: Transforms on SVG elements behave differently. Values: transform-box: fill-box, transform-origin: center. [SVG Animation]
- **must** (motion, all): Make animations interruptible; avoid fill modes or delays that block interaction. Why: User input should interrupt any animation mid-flight. [Animations Must Be Interruptible]
- **must** (motion, all): Do not run infinite loops in product screens or animate everything at once. Why: Listed as red flags that instantly make motion feel cheap: loops distract, and animating everything at once leaves no attention hierarchy. [Red Flags]
- **must** (motion, all): Do not use 300-600ms durations on hover or buttons. Why: Feels sluggish. Values: 300–600ms. [Red Flags]
- **consider** (tooling, react): Use CSS transitions for micro feedback and simple states and Motion for layout animations and springs in React; reach for GSAP, Rive or Lottie only for complex timelines or illustrative motion. Why: For most SaaS products CSS + Motion is sufficient. [Libraries and Tools]
- **must** (motion, all): Keep timings consistent across similar components; do not use 200ms in one place and 400ms in a similar one. Why: Inconsistent timings are a red flag: chaos. Values: 200ms, 400ms. [Red Flags: Inconsistent timings; Pre-Ship Checklist]
- **should** (motion, all): Keep product UI motion subtle, fast and functional; allow more expressive motion only on marketing surfaces. Why: Context first: product UI or marketing changes how much motion is acceptable. [0. Context First]
- **should** (components, all): Show input success with a subtle checkmark or color change, without overdoing it. Why: Inputs table: Don't overdo it. [Inputs]
- **should** (motion, all): Performance-test motion on slower devices before shipping. Why: Pre-ship checklist item; transition: all is a performance killer on low-end devices. [Pre-Ship Checklist]

### Decisions it informs

- How much motion should the product use? (`Q-motion-01`)
  - Level 1 micro feedback: Responsive feel without noticeable animation on hover, press, focus, toggles, inline validation When: Always; the starting point
  - Level 2 state transitions: Movement instead of teleportation for accordions, tabs, modals, drawers, popovers When: When state changes need continuity
  - Level 3 layout continuity: Elements resize, reorder, add or remove while keeping context When: Reorder, filter chips, drag and drop, lists
  - Level 4 expressive: Hero animations, illustrations, onboarding sequences When: Rarely in product; marketing pages
  - Recommendation: Start at Level 1 and add higher levels only when justified; when in doubt, shorter, subtler or none.
- Which easing curve for each kind of movement? (`Q-motion-03`)
  - ease-out cubic-bezier(0.0, 0.0, 0.2, 1): Fast start, soft landing When: Elements entering
  - ease-in cubic-bezier(0.4, 0.0, 1, 1): Soft start, fast exit When: Elements exiting
  - ease-in-out cubic-bezier(0.4, 0.0, 0.2, 1): Smooth both ways When: State changes
  - emphasized cubic-bezier(0.2, 0.0, 0, 1): Slightly more alive When: Alternative when more character is wanted
  - Recommendation: Group easings by job: enter, exit, change.
- How should springy motion be set up? (`Q-motion-04`)
  - Snappy spring: Stiffness 400, damping 30: quick and settled When: Snappy, quick response
  - Smooth spring: Stiffness 200, damping 20: softer When: Smoother physical movement
  - Bouncy spring: Stiffness 300, damping 15: visible bounce When: Sparingly
  - Duration and easing only: CSS tweens with tokens When: Micro feedback and simple states
  - Recommendation: Springs for drag, swipe and physical elements, decaying quickly; CSS tweens elsewhere.
- How many duration steps should the token set have? (`Q-motion-02`)
  - Minimum set: fast 120ms, default 200ms, slow 320ms When: Most teams
  - Complete set: instant 0ms, fast 120ms, default 200ms, slow 320ms, slower 400ms When: Reference implementation
  - Recommendation: Start with the three-step minimum set.
- What should happen when the user asks for reduced motion? (`Q-motion-07`)
  - Fade only: Slide or scale plus fade becomes a plain fade When: Modals, slides
  - Instant or short tween: Spring bounce removed When: Spring animations
  - Remove: Parallax gone; auto-playing loops paused or removed When: Parallax and loops
  - Recommendation: Always provide the variant; the CSS shortcut sets durations to 0.01ms.

### Process

1. Answer context questions: Product UI or marketing? How often is it triggered? Does it help or distract?
2. Pick the pyramid level: Start with micro feedback; justify each step up.
3. Choose duration band and easing: Match purpose and frequency to a duration category; ease-out to enter, ease-in to exit, ease-in-out to change.
4. Use tokens: Apply duration, easing and distance tokens through the component mapping.
5. Write the reduced-motion variant: Fade only, no parallax, paused loops; override tokens under prefers-reduced-motion.
6. Run the quick test: Purpose, frequency-appropriate duration, non-linear easing, reduced-motion variant, would removing it hurt? Remove if no to purpose or removal.
7. Pre-ship checklist: Check bands, tokens, no linear, under 500ms, no transition: all, transform-origin set, interruptible, tested on slower devices.

### Examples and visual references

- Button CSS: transition background-color 120ms and transform 90ms with --ease-out, :active scale(0.98) (Buttons and Controls): A button that tints quickly on hover and presses in slightly when clicked.
- List item enter: opacity 0 and translateY(-8px) to 1 and 0 over 200ms ease-out (Lists and Tables): New rows drop in a few pixels while fading in.
- Modal: opacity 0 and scale(0.95) to 1 over 200ms ease-out; reduced motion keeps opacity only over 150ms (Modals and Drawers; Reduced Motion): Modal grows slightly as it fades in; with reduced motion it only fades.
- Dropdown with transform-origin: top right scaling from 0.95 (Transform Origin): Menu appears to grow out of its trigger corner.
- Reduced-motion CSS shortcut setting animation and transition durations to 0.01ms on all elements (CSS Shortcut): Global kill switch for motion.

### Numbers

- 90–150ms: Instant category: hover, press, toggle, focus [Duration Reference]
- 160–240ms: State change: accordion, tabs, small panels [Duration Reference]
- 240–360ms: Page/large: modal, drawer, route transition [Duration Reference]
- 360–500ms: Complex: large layout reflow (rare) [Duration Reference]
- 120ms / 200ms / 320ms: Fast, default and slow duration tokens [Practical Preset]
- 400ms: --duration-slower in the complete token system [Appendix]
- cubic-bezier(0.2, 0.0, 0, 1): --ease-emphasized [CSS Tokens]
- cubic-bezier(0.05, 0.7, 0.1, 1): --ease-emphasized-decel [Appendix]
- 2px / 4px / 8px / 16px / 24px: Motion distance tokens xs to xl [Appendix: DISTANCES]
- 0.98: Button press scale [Buttons and Controls]
- 0.95: Modal and dropdown start scale [Modals and Drawers]
- 0.01ms: Reduced-motion shortcut durations [CSS Shortcut]
- 500ms: Upper limit for product UI motion [Pre-Ship Checklist]

<!-- /od:learn -->
