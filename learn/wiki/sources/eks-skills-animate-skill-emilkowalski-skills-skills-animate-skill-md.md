---
type: source
title: "emilkowalski/skills: skills/animate/SKILL.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-animate-skill
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/animate/SKILL.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - animation
  - motion
  - easing
  - duration
  - springs
  - reduced-motion
  - hover-gating
  - transform-origin
  - css
  - react
  - motion-library
  - waapi
---

# emilkowalski/skills: skills/animate/SKILL.md

## Metadata

- Video ID: `eks-skills-animate-skill`
- Channel: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/animate/SKILL.md

## Summary

Emil Kowalski's animate skill is an instruction file for an AI agent that builds a web animation from scratch by making decisions in a fixed order: whether it should animate at all (judged by how often people see it), what purpose it serves, the cheapest tool, which properties, which curve and duration or spring, how it handles interruption and exit, and how reduced motion and hover gating ship with it. It gives exact tables for easing (three strong custom cubic-bezier tokens), durations per kind of element and two spring configurations, and forbids invented or approximated values. It closes with a 'Never Ship' checklist of automatic review blocks and a short output format that reports the gate result, the ingredients and what still needs a feel-check. For a design system it supplies motion tokens, a frequency gate that decides which components animate, and accessibility defaults for reduced motion and touch hover that ship with every animation [inferred].

## Key Ideas

- The worse motion mistake is animating something that should not animate; deciding to write no animation is a valid, successful result.
- How often an element is seen decides whether it animates: 100+ times a day means never, tens of times means barely, occasional means standard, rare or first-time moments get the delight budget.
- Keyboard-initiated actions never animate; this is a fixed rule, not a judgment call.
- Every animation needs a named purpose (feedback, spatial consistency, state indication, preventing a jarring change, explanation, delight); if none fits, it is not built.
- Data people read or act on should not move for style; decorative motion belongs on marketing pages.
- Use the cheapest tool that works, stepping up from CSS transitions to @starting-style, CSS animations, WAAPI and finally the Motion library.
- Animate only transform and opacity (clip-path is also allowed, height only for accordions) because they skip layout and paint.
- Nothing appears from nothing: entrances start at scale 0.9-0.97 with opacity 0, never scale(0), and popovers grow from their trigger while modals stay centered.
- Easing follows the situation: ease-out to enter or exit, ease-in-out to move on screen, ease for hover and color, linear for constant motion, and never ease-in on UI.
- Built-in CSS curves are too weak; three strong custom curves become tokens, and existing tokens are extended rather than forked.
- UI animations stay under 300ms, with a set duration range per kind of element.
- Springs are for drag with momentum, living elements, reversible gestures and mouse-tracking; bounce stays between 0.1 and 0.3 and is rare in UI.
- Elements that can be triggered rapidly use transitions, which retarget from the current value, not keyframes, which restart from zero.
- Exits mirror entrances, and timing can be asymmetric where the user is deliberating: slow on the deliberate phase, snappy on the system's response.
- Reduced motion and hover gating ship with the animation; reduced motion means fewer and gentler animations, not none.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Person whose animation philosophy sets the bar for this skill
- [[entities/motion-motion-dev|Motion (motion.dev)]] (library): Animation library reserved for springs, layout animations, exit animations and gesture-driven values
- [[entities/base-ui|Base UI]] (library): Supplies var(--transform-origin) for trigger-anchored popovers
- [[entities/raycast|Raycast]] (product): Product cited as correctly having no open/close animation, since it is opened hundreds of times a day
- [[entities/ionic|Ionic]] (library): Credited in parentheses for the iOS-like drawer curve cubic-bezier(0.32, 0.72, 0, 1)
- [[entities/easing-dev|easing.dev]] (tool): Recommended source for easing curves not in the skill's table
- [[entities/easings-co|easings.co]] (tool): Recommended source for easing curves not in the skill's table
- [[entities/web-animations-api-waapi|Web Animations API (WAAPI)]] (concept): element.animate(), for programmatic control with CSS performance and no library
- [[entities/starting-style|@starting-style]] (concept): CSS at-rule for entry animations on mount without JS state
- [[entities/prefers-reduced-motion|prefers-reduced-motion]] (concept): Media query whose gentler variant must ship with every animation
- [[entities/usereducedmotion|useReducedMotion]] (concept): React hook used to swap movement values (e.g. -100% to 0) for reduced motion
- [[entities/review-animations|review-animations]] (tool): Sibling skill that critiques motion; its automatic blocks form the Never Ship list
- [[entities/improve-animations|improve-animations]] (tool): Sibling skill for auditing a whole codebase's motion
- [[entities/find-animation-opportunities|find-animation-opportunities]] (tool): Sibling skill that hunts for places that could animate
- [[entities/animate-expo|animate-expo]] (tool): Sibling skill for building animations in React Native
- [[entities/pick-ui-library|pick-ui-library]] (tool): Skill to invoke when the task needs a component (toast, drawer, command menu, dropdown) rather than an animation

## Topics

- [[topics/motion-principles|Motion principles]]: A gate before any motion: animate only when the frequency tier allows it and a purpose can be named; keyboard actions and 100+/day actions never animate.
- [[topics/easing-and-timing|Easing and timing]]: Easing by situation (ease-out, ease-in-out, ease, linear; never ease-in), three custom cubic-bezier tokens, a duration table per element, and a 300ms ceiling for UI.
- [[topics/spring-animation|Spring animation]]: Springs for drag with momentum, living elements, interruptible gestures and mouse-tracking; two configs (duration 0.5/bounce 0.2, or mass 1/stiffness 100/damping 10); bounce 0.1-0.3.
- [[topics/animation-performance|Animation performance]]: Animate transform and opacity only; CSS animations run off the main thread; Motion's x/y/scale shorthands drop frames under load; never drive child transforms from a parent CSS variable.
- [[topics/reduced-motion|Reduced motion]]: Reduced-motion variants ship with every animation and keep opacity and color while dropping transform-based movement: fewer and gentler, not zero.
- [[topics/micro-interactions|Micro-interactions]]: Button press feedback at 100-160ms, hover motion gated to fine pointers, hold-to-confirm with asymmetric timing.
- [[topics/modals-and-popovers|Modals and popovers]]: Popovers, dropdowns, menus and tooltips scale from their trigger via transform-origin; modals are exempt and stay centered; per-type durations.
- [[topics/gestures-and-drag|Gestures and drag]]: Gestures use springs because they carry velocity through interruptions; exits mirror entrances so swipe-to-dismiss feels obvious.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Tool ladder (CSS transition, @starting-style, CSS animation, WAAPI, Motion), CSS media queries for reduced motion and hover, React useReducedMotion, Motion transform strings.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Motion values come from fixed token tables; extend a codebase's existing easing and duration tokens rather than adding a parallel system.
- [[topics/ai-assisted-design|AI-assisted design]]: The source is an agent skill: it tells the model to make the motion call itself, write code, and report the gate, the ingredients and what needs a human feel-check.

## Notable Claims

- Animating something that shouldn't animate is a worse failure than animating the right thing with the wrong ingredients. Evidence: Operating Posture: Two failure modes, and the first is worse
- Raycast having no open/close animation is correct for something opened hundreds of times a day. Evidence: Keyboard-initiated actions are a disqualifier, not a judgment call
- CSS animations beat JS under load because they run off the main thread, while requestAnimationFrame-based animation drops frames while the browser loads, scripts or paints. Evidence: 3. Pick the tool: CSS animations beat JS under load
- transform and opacity skip layout and paint and run on the GPU; width, height, margin, padding, top and left trigger all three. Evidence: 4. Pick the properties
- Percentages in translate() are relative to the element's own size, so translateY(100%) moves it by its own height whatever the content. Evidence: Percentages in translate()
- Motion's x/y/scale shorthands are not hardware-accelerated and drop frames under load; the full transform string is hardware-accelerated. Evidence: In Motion, use the full transform string
- Driving a child's transform from a CSS variable on the parent recalculates styles for every child. Evidence: Never drive a child's transform from a CSS variable on the parent
- ease-in starts slow, delaying the exact moment the user is watching; ease-out at 200ms feels faster than ease-in at 200ms. Evidence: Never ease-in on UI
- Built-in CSS easings are too weak. Evidence: Built-in CSS easings are too weak. Use these
- A 180ms dropdown feels more responsive than a 400ms one. Evidence: UI animations stay under 300ms
- The Apple-style spring (duration and bounce) is easier to reason about; the traditional physics spring (mass, stiffness, damping) gives more control. Evidence: Reach for a spring instead
- Transitions retarget from the current value; keyframes restart from zero. Evidence: 6. Interruption and exit
- Springs carry velocity through an interruption. Evidence: Springs for gestures
- Symmetric enter and exit paths are what make swipe-to-dismiss feel obvious. Evidence: Exit the way it entered
- Touch devices fire false hovers on tap. Evidence: @media (hover: hover) and (pointer: fine) ... touch fires false hovers on tap
- Hand-rolling components such as dropdowns leads to a div dropdown with no focus management. Evidence: Hand-rolling those is how you end up with a <div> dropdown
- The --ease-drawer curve cubic-bezier(0.32, 0.72, 0, 1) is an iOS-like drawer curve from Ionic. Evidence: --ease-drawer ... iOS-like drawer curve (Ionic)

## Quotes

> Never present motion options as a menu.
> Keyboard-initiated actions are a disqualifier, not a judgment call.
> Nothing in the real world appears from nothing.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is an instruction file for an AI agent (it includes a scripted first reply and references sibling skills such as review-animations, improve-animations, find-animation-opportunities, animate-expo and pick-ui-library that are not part of OpenDesigner).
- Caveat: The instruction to never present motion options as a menu is aimed at the agent building code; OpenDesigner's own interview asks one decision at a time with options, so the two need reconciling when these rules are applied [inferred].
- Caveat: The skill is web-focused (CSS, React, Motion); React Native is handled by a separate animate-expo skill.
- Caveat: Values are pinned to commit 85e8e23 of emilkowalski/skills (MIT); later versions may change them.
- Caveat: The ranges in the duration table (for example modals and drawers 200-500ms) partly exceed the 'UI animations stay under 300ms' ceiling; the source does not reconcile the two [inferred].
- Caveat: Claims about performance (GPU, main thread, Motion shorthands not hardware-accelerated) are stated by the source without measurements.
- Caveat: Tool picks and the easing, duration and spring tables are marked must because the Hard Rules require running the sequence in order, taking every value from the tables and using the cheapest tool that works [inferred].

### Rules and practices

- **must** (motion, all): Do not animate an element when motion would not serve it; treat producing no animation code as a successful outcome. Why: Animating something that shouldn't animate is the worse of the two failure modes; the gate exists to sometimes produce zero lines of code. [Operating Posture: Animating something that shouldn't animate]
- **must** (process, all): Make the motion call yourself, state the reasoning in one line and write the code instead of presenting motion options as a menu. Why: The skill builds animation as a senior design engineer would, aiming to pass a strict review the first time. [Never present motion options as a menu]
- **must** (process, all): Run the build sequence in order, and settle steps 1 (should it animate) and 2 (purpose) before choosing any curve. Why: Steps 1 and 2 gate everything; don't reach for a curve before you know whether it animates at all. [Hard Rules: 1. Run the sequence in order]
- **must** (motion, all): Take every curve, duration and spring config from the skill's tables; never invent or approximate one such as cubic-bezier(0.4, 0, 0.2, 1) because it looks familiar. Why: No approximated values are allowed. Values: cubic-bezier(0.4, 0, 0.2, 1). [Hard Rules: 2. No approximated values]
- **must** (tokens, all): Use the codebase's existing motion tokens (for example --ease-out or an existing duration scale) and extend them instead of adding a parallel system. Why: Adding a parallel system is a defect. Values: --ease-out. [Hard Rules: 3. Extend the codebase's tokens, don't fork them]
- **must** (accessibility, web): Ship the reduced-motion variant and hover gating in the same change as the animation, never as a follow-up. Why: Reduced motion and hover gating ship with the animation, every time. [Hard Rules: 4 and 7. Reduced motion and pointer gating]
- **must** (tooling, web): Use the cheapest tool that works; do not install a motion library for a fade. Why: Cheapest tool that works. [Hard Rules: 5. Cheapest tool that works]
- **must** (motion, all): Never animate actions performed 100+ times a day, such as keyboard shortcuts or toggling a command palette. Why: Frequency gate: at this tier the answer is no animation, ever. Values: 100+ times/day. [1. Should this animate at all? (frequency table)]
- **must** (motion, all): For elements used tens of times a day (hover effects, list navigation), use only near-imperceptible motion that is fast and subtle, or none. Why: Frequency gate for tens of times a day. Values: Tens of times/day. [1. Should this animate at all? (frequency table)]
- **should** (motion, all): Give occasional elements such as modals, drawers and toasts standard animation. Why: Frequency gate: occasional use gets standard animation. [1. Should this animate at all? (frequency table)]
- **must** (motion, all): Spend the delight budget only on rare or first-time moments such as onboarding, success and celebration. Why: The delight budget lives at the rare/first-time tier; delight is allowed only there. [Rare / first-time ... The delight budget lives here]
- **must** (motion, all): Do not animate keyboard-initiated actions. Why: Keyboard-initiated actions are a disqualifier, not a judgment call; Raycast has no open/close animation for something opened hundreds of times a day. [Keyboard-initiated actions are a disqualifier]
- **must** (process, all): When a request fails the frequency gate, say so plainly, do not write the animation, and offer a non-motion alternative such as an instant state change or a static affordance. Why: The gate exists to produce zero lines of code sometimes; that's a success, not a dodge. [If the request fails this gate, say so plainly]
- **must** (motion, all): Name the animation's purpose as one of feedback, spatial consistency, state indication, preventing a jarring change, explanation or delight before building it; if none fits, do not build it. Why: Can't name it? Don't build it. [2. What is the purpose?]
- **must** (motion, all): Do not add motion to a frequently seen element because it looks cool. Why: "It looks cool" on a frequently-seen element is a reason to stop. [It looks cool on a frequently-seen element is a reason to stop]
- **must** (motion, all): Use explanatory animation (demonstrating how something works) only on marketing and onboarding surfaces. Why: Explanation is listed as a purpose for marketing/onboarding only. [Explanation — demonstrating how something works (marketing/onboarding only)]
- **must** (motion, all): Do not move data the user is reading or acting on for style; keep decorative effects such as mouse-tracking on marketing pages, not on functional views like a graph in a banking app. Why: Function check: data the user reads or acts on should not move for style. [Also check function]
- **must** (tooling, css): Use a CSS transition for hover, press, color and state toggles controlled by a class or attribute. Why: It is the cheapest tool that fits this need. [3. Pick the tool (table)]
- **must** (tooling, css): Use CSS @starting-style for entry animations on mount that need no JS state. Why: Cheapest tool that fits an entry animation on mount: walk down the tool list and stop at the first that fits. Values: @starting-style. [3. Pick the tool (table)]
- **must** (tooling, css): Use a CSS animation for predetermined motion that must stay smooth while the page is busy loading. Why: CSS animations run off the main thread, so they stay smooth while the page is busy; walk down the tool list and stop at the first that fits. [3. Pick the tool (table)]
- **must** (tooling, web): Use WAAPI (element.animate()) when you need programmatic control with CSS performance and no library. Why: Programmatic control with CSS performance and no library; walk down the tool list and stop at the first that fits. Values: element.animate(). [3. Pick the tool (table)]
- **must** (tooling, web): Reserve the Motion library (motion.dev) for springs, layout animations, exit animations and gesture-driven values. Why: Motion is the last step of the cheapest-tool list; don't install a motion library for a fade. [3. Pick the tool (table)]
- **must** (tooling, web): Use CSS for predetermined motion and JS for dynamic and interruptible motion. Why: requestAnimationFrame-based animation drops frames while the browser loads, scripts or paints; CSS runs off the main thread. [CSS animations beat JS under load]
- **must** (components, web): When the task needs a component (toast, drawer, command menu, dropdown) rather than an animation, stop and choose a UI library (the source invokes its pick-ui-library skill) instead of hand-rolling it. Why: Hand-rolling those is how you end up with a div dropdown and no focus management. [If the task needs a component rather than an animation]
- **must** (motion, web): Animate only transform and opacity; do not animate width, height, margin, padding, top or left. Why: transform and opacity skip layout and paint and run on the GPU; width, height, margin, padding, top and left trigger all three. Values: transform, opacity. [4. Pick the properties]
- **must** (motion, web): Treat clip-path as the only sanctioned fourth animatable property, and animate height only for accordions. Why: Accordions have no transform equivalent. Values: clip-path, height. [clip-path is the sanctioned fourth ... height is tolerated only for accordions]
- **must** (motion, all): Never start an entrance from scale(0); start from scale(0.9-0.97) with opacity: 0. Why: Nothing in the real world appears from nothing. Values: scale(0), scale(0.9–0.97), opacity: 0, scale(0.95). [Never scale(0); Never Ship: transform: scale(0) entrance]
- **must** (components, web): Set transform-origin at the trigger for popovers, dropdowns, menus and tooltips (var(--transform-origin) in Base UI), and keep modals centered. Why: Modals are not anchored to a trigger, so they are exempt and stay centered. Values: var(--transform-origin). [transform-origin at the trigger; Never Ship: transform-origin: center on a trigger-anchored popover]
- **should** (motion, css): Use percentages in translate() (for example translateY(100%)) rather than hardcoded pixels. Why: Percentages are relative to the element's own size, so the move matches its height whatever the content. Values: translateY(100%). [Percentages in translate()]
- **must** (motion, react): In Motion, animate with the full transform string (for example transform: "translateX(100px)") instead of the x, y or scale shorthands. Why: The shorthands are not hardware-accelerated and drop frames under load. Values: animate={{ transform: "translateX(100px)" }}, animate={{ x: 100 }}. [In Motion, use the full transform string; Never Ship: Motion x/y/scale props under load]
- **must** (motion, web): Set transform on the animated element directly; never drive a child's transform from a CSS variable on the parent. Why: A parent CSS variable recalculates styles for every child. [Never drive a child's transform from a CSS variable on the parent]
- **must** (motion, all): Use ease-out for elements entering or exiting, and as the default. Why: Easing decision order: entering or exiting, and default, are ease-out. Values: ease-out. [5. Easing and duration (easing table)]
- **must** (motion, all): Use ease-in-out for elements moving or morphing on screen. Why: Easing decision order. Values: ease-in-out. [5. Easing and duration (easing table)]
- **must** (motion, all): Use ease for hover and color changes. Why: Easing decision order. Values: ease. [5. Easing and duration (easing table)]
- **must** (motion, all): Use linear for constant motion such as a marquee or progress. Why: Easing decision order. Values: linear. [5. Easing and duration (easing table)]
- **must** (motion, all): Never use ease-in on a UI element. Why: It starts slow, delaying the exact moment the user is watching; ease-out at 200ms feels faster than ease-in at 200ms. Values: ease-in, 200ms. [Never ease-in on UI]
- **must** (tokens, css): Define and use strong custom curves instead of built-in CSS easings: --ease-out: cubic-bezier(0.23, 1, 0.32, 1) for UI, --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1) for on-screen movement, --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1) for iOS-like drawers. Why: Built-in CSS easings are too weak. Values: --ease-out: cubic-bezier(0.23, 1, 0.32, 1), --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1), --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1). [Built-in CSS easings are too weak. Use these]
- **must** (motion, css): Do not use the built-in ease-out keyword on a deliberate animation; use cubic-bezier(0.23, 1, 0.32, 1). Why: It is an automatic block in review-animations. Values: cubic-bezier(0.23, 1, 0.32, 1). [Never Ship: Built-in ease-out on a deliberate animation]
- **must** (motion, all): When a curve is needed that is not in the table, take it from easing.dev or easings.co; do not hand-roll one. Why: No approximated values. [Need a curve that isn't here? ... Don't hand-roll one.]
- **must** (motion, all): Give button press feedback a duration of 100-160ms. Why: Duration table. Values: 100–160ms. [Duration table: Button press feedback]
- **must** (motion, all): Give tooltips and small popovers a duration of 125-200ms. Why: Duration table. Values: 125–200ms. [Duration table: Tooltips, small popovers]
- **must** (motion, all): Give dropdowns and selects a duration of 150-250ms. Why: Duration table. Values: 150–250ms. [Duration table: Dropdowns, selects]
- **must** (motion, all): Give modals and drawers a duration of 200-500ms. Why: Duration table. Values: 200–500ms. [Duration table: Modals, drawers]
- **consider** (motion, all): Allow marketing and explanatory animations to run longer than UI animations. Why: Duration table: marketing / explanatory can be longer. [Duration table: Marketing / explanatory]
- **must** (motion, all): Keep UI animations under 300ms; without a reason, use 150-250ms. Why: A 180ms dropdown feels more responsive than a 400ms one. Values: 300ms, 150–250ms, 180ms, 400ms. [UI animations stay under 300ms; Never Ship: UI duration over 300ms with no reason]
- **must** (motion, all): Use a spring instead of a duration for drag with momentum, elements that should feel alive, gestures the user can interrupt or reverse, and decorative mouse-tracking. Why: These motions need the behaviour of a spring. [Reach for a spring instead]
- **must** (motion, react): Configure springs as { type: "spring", duration: 0.5, bounce: 0.2 } (Apple-style) or { type: "spring", mass: 1, stiffness: 100, damping: 10 } (traditional physics). Why: Apple-style is easier to reason about; traditional physics gives more control. Values: { type: "spring", duration: 0.5, bounce: 0.2 }, { type: "spring", mass: 1, stiffness: 100, damping: 10 }. [Reach for a spring instead (spring configs)]
- **must** (motion, all): Keep spring bounce between 0.1 and 0.3, avoid bounce in most UI, and reserve it for drag-to-dismiss and playful interactions. Why: The source gives no further reason; bounce is reserved for drag-to-dismiss and playful interactions. Values: 0.1–0.3. [Keep bounce at 0.1–0.3]
- **must** (motion, css): Use CSS transitions, not keyframes, for toasts, toggles and anything a user can fire twice in a second. Why: Transitions retarget from the current value; keyframes restart from zero. [6. Interruption and exit; Never Ship: Keyframes on toasts, toggles]
- **must** (motion, all): Use springs for gestures. Why: Springs carry velocity through an interruption. [Springs for gestures]
- **must** (motion, all): Exit the way it entered: an element that slides in from the bottom leaves through the bottom. Why: Symmetric paths are what make swipe-to-dismiss feel obvious. [Exit the way it entered]
- **must** (motion, all): Use asymmetric timing where the user is deciding: slow on the deliberate phase (hold-to-confirm press 2s linear), snappy on the system response (release 200ms ease-out). Why: The deliberate phase and the system response need different speeds. Values: 2s linear, 200ms ease-out. [Asymmetric timing where the user is deciding]
- **must** (accessibility, css): Under @media (prefers-reduced-motion: reduce), keep opacity and color animation (for example animation: fade 0.2s ease) and drop transform-based motion. Why: Reduced motion means fewer and gentler animations, not zero. Values: @media (prefers-reduced-motion: reduce), animation: fade 0.2s ease. [7. Reduced motion and pointer gating]
- **must** (accessibility, all): Do not remove all animation for reduced motion; keep transitions that aid comprehension and remove movement and position changes. Why: Reduced motion means fewer and gentler, not zero. [Reduced motion means fewer and gentler animations, not zero; Never Ship: Missing prefers-reduced-motion]
- **should** (accessibility, react): In React, read useReducedMotion() and swap movement values for static ones (for example closedX = reduce ? 0 : '-100%'). Why: Reduced motion ships with the animation. Values: useReducedMotion(), 0, '-100%'. [const reduce = useReducedMotion()]
- **must** (accessibility, css): Gate hover motion behind @media (hover: hover) and (pointer: fine); never ship ungated :hover motion. Why: Touch fires false hovers on tap. Values: @media (hover: hover) and (pointer: fine), transform: scale(1.05). [7. Reduced motion and pointer gating; Never Ship: Ungated :hover motion]
- **should** (process, web): Start from the matching recipe (button press, dropdown, tooltip, modal, drawer, toast, accordion, stagger, hold-to-confirm, tab indicator, scroll reveal, drag-to-dismiss) instead of a blank file. Why: The recipes are ready-to-build implementations of the common cases. [Recipes: start from the recipe rather than from a blank file]
- **must** (motion, css): Never use transition: all; name the exact properties being transitioned. Why: It is an automatic block in review-animations. Values: transition: all. [Never Ship: transition: all]
- **must** (motion, all): Do not bring every element in at once; stagger group entrances by 30-80ms. Why: Everything entering at once is an automatic block in review-animations. Values: 30–80ms. [Never Ship: Everything entering at once]
- **must** (process, all): Self-check the finished animation against the Never Ship list before finishing. Why: Each item is an automatic block in review-animations. [Self-check before you finish. Each of these is an automatic block in `review-animations`]
- **must** (process, all): After writing the code, report in a few lines the gate result (frequency tier, named purpose, anything rejected and why) and the ingredients (tool, properties, curve, duration or spring config), one line each. Why: The code is the deliverable; the note explains the decisions briefly. [Output]
- **must** (process, all): When a result depends on feel that cannot be judged from code (a crossfade, a spring's bounce, the opacity/height balance in an entering list), say so and point to the check: play it at 2-5x duration or in the DevTools animation inspector, step it frame by frame, test gestures on a real device, and look again the next day. Why: When feel genuinely can't be settled from code, say so instead of guessing at a value. Values: 2–5×. [Output: What to feel-check; Tone]
- **should** (process, all): Do not pad the output into a report; keep the explanation to a few lines after the code. Why: The code is the deliverable. [Don't pad this into a report]
- **should** (process, all): Build every animation so it passes a strict review (the review-animations bar) the first time. Why: The bar is Emil Kowalski's animation philosophy, the same bar review-animations enforces. [Operating Posture: Write it so it passes that review the first time]
- **should** (process, all): Keep an animation-building task to construction: send codebase audits to improve-animations, diff critiques to review-animations, hunting for places that could animate to find-animation-opportunities, and React Native work to animate-expo. Why: The skill does ONE thing: turn a request for motion into an implementation that would survive a strict review. [A construction skill. It does ONE thing]
- **must** (motion, all): Avoid the wrong ingredients even when the element should animate: ease-in on an entrance, scale(0), keyframes on a toast, or a duration that makes a dropdown feel sluggish. Why: The source names this as the second failure mode: animating the right thing with the wrong ingredients. Values: ease-in, scale(0). [Operating Posture: 2. Animating the right thing with the wrong ingredients]
- **must** (process, all): When first invoked without a specific question, the animate skill replies only with its one-line readiness statement and gives no other information until the user asks (this skill's own agent behaviour). Why: Stated in the skill's Initial Response section; no reason given. [Initial Response: respond only with ... Do not provide any other information until the user asks a question]
- **should** (process, all): Keep the tone opinionated and brief, and give the honest answer 'this shouldn't animate' when it applies. Why: That answer is the reason the skill exists. [Tone: Opinionated and brief]

### Decisions it informs

- Should this element animate at all, given how often people will see it?
  - No animation: The change is instant; nothing moves. When: Actions done 100+ times a day, such as keyboard shortcuts or the command palette toggle, and any keyboard-initiated action.
  - Near-imperceptible motion: Fast and subtle, or nothing. When: Things used tens of times a day, such as hover effects and list navigation.
  - Standard animation: Normal enter/exit motion within the duration table. When: Occasional elements such as modals, drawers and toasts.
  - Delight: Room for expressive, memorable motion. When: Rare or first-time moments such as onboarding, success and celebration.
  - Recommendation: Decide by frequency before anything else; the more often it is seen, the less it moves, and keyboard-initiated actions never animate.
- Which tool should build the animation?
  - CSS transition: Cheapest; retargets smoothly between states. When: Hover, press, color, or a state toggle controlled by a class or attribute.
  - CSS @starting-style: Entry animation on mount without JS. When: Entry animations that need no JS state.
  - CSS animation: Runs off the main thread, so it stays smooth while the page is busy. When: Predetermined motion that must stay smooth while the page is loading.
  - WAAPI (element.animate()): Programmatic control with CSS performance and no library. When: Motion needs JS control but not a dependency.
  - Motion (motion.dev): Springs, layout and exit animations, gesture-driven values. When: Springs, layout animations, exit animations or gestures.
  - Recommendation: Walk down the list and stop at the first tool that fits; use CSS for predetermined motion and JS for dynamic, interruptible motion.
- Which easing curve should each kind of motion use? (`Q-motion-03`)
  - ease-out (cubic-bezier(0.23, 1, 0.32, 1)): Strong ease-out for UI; feels faster than ease-in at the same duration. When: Entering or exiting, and the default.
  - ease-in-out (cubic-bezier(0.77, 0, 0.175, 1)): Strong ease-in-out for on-screen movement. When: Moving or morphing on screen.
  - ease: The built-in CSS ease curve. When: Hover and color changes.
  - linear: Constant speed. When: Constant motion such as a marquee or progress.
  - ease-in: Starts slow, delaying what the user is watching; feels slower at the same duration. When: Never on UI.
  - Recommendation: Choose the curve by the job the motion does (enter/exit, move, hover/color, constant), using strong custom curves rather than the weak built-in keywords.
- Should motion be timed with a duration and curve, or driven by a spring? (`Q-motion-04`)
  - Duration + easing curve: Predictable timing from the duration table. When: Most UI transitions.
  - Apple-style spring { type: "spring", duration: 0.5, bounce: 0.2 }: Physical motion that is easier to reason about. When: Drag with momentum, living elements, interruptible gestures, mouse-tracking.
  - Physics spring { type: "spring", mass: 1, stiffness: 100, damping: 10 }: Traditional physics with more control. When: When more control over the spring is needed.
  - Recommendation: Use durations for ordinary UI and springs for gestures and interruptible motion; keep bounce at 0.1-0.3 and reserve it for drag-to-dismiss and playful interactions.
- How long should each kind of UI animation run?
  - 100–160ms: Instant-feeling press feedback. When: Button press feedback.
  - 125–200ms: Quick, light appearance. When: Tooltips and small popovers.
  - 150–250ms: Responsive menus. When: Dropdowns and selects.
  - 200–500ms: Larger surfaces get more time. When: Modals and drawers.
  - Longer: Room to explain. When: Marketing and explanatory animation.
  - Recommendation: Keep UI animations under 300ms; a 180ms dropdown feels more responsive than a 400ms one.
- What should happen to animations when someone turns on reduced motion? (`Q-motion-07`)
  - Gentler variant: Opacity and color changes stay; movement and position changes are removed. When: Always; this ships with the animation.
  - No animation at all: Everything becomes instant, including transitions that help people understand a change. When: The source rejects this: reduced motion is not zero.
  - Recommendation: Fewer and gentler, not zero: keep transitions that aid comprehension and drop transform-based motion.
- Should rapidly triggered elements animate with keyframes or transitions?
  - CSS transitions: Retarget from the current value when triggered again. When: Toasts, toggles and anything a user can fire twice in a second.
  - Keyframes: Restart from zero on each trigger. When: Not for rapidly triggered elements.
  - Recommendation: Transitions, because they retarget smoothly instead of restarting.
- Where should a floating panel grow from?
  - From its trigger (var(--transform-origin)): The panel looks like it came out of the thing you clicked. When: Popovers, dropdowns, menus and tooltips.
  - From the center: Grows evenly from the middle. When: Modals only, because they are not anchored to a trigger.
  - Recommendation: Trigger-anchored origin for anything attached to a trigger; modals stay centered.

### Process

1. Gate by frequency: Place the element in a tier: 100+ times a day (no animation), tens of times (near-imperceptible or none), occasional (standard), rare/first-time (delight). Keyboard-initiated actions never animate. If it fails, say so and offer an instant state change or static affordance.
2. Name the purpose: Pick one of feedback, spatial consistency, state indication, preventing a jarring change, explanation (marketing/onboarding only) or delight (rare tier only). Also check that data being read or acted on is not moving for style. If no purpose fits, stop.
3. Pick the tool: Walk down: CSS transition, CSS @starting-style, CSS animation, WAAPI, Motion. Stop at the first that fits. If the task is really a component (toast, drawer, command menu, dropdown), use a UI library instead.
4. Pick the properties: transform and opacity only (clip-path allowed; height only for accordions). Start entrances at scale(0.9-0.97) with opacity 0, set transform-origin at the trigger (modals stay centered), prefer percentage translates, use full transform strings in Motion, and set transform on the element itself.
5. Choose easing and duration, or a spring: Easing by situation (ease-out, ease-in-out, ease, linear; never ease-in) using the custom curve tokens; duration from the table and under 300ms for UI; a spring for drag, momentum, interruptible gestures and mouse-tracking, with bounce 0.1-0.3.
6. Plan interruption and exit: Transitions for anything triggered rapidly, springs for gestures, exits that mirror entrances, and asymmetric timing where the user is deciding.
7. Add reduced motion and pointer gating: Ship a prefers-reduced-motion variant that keeps opacity/color and drops movement, and wrap hover motion in @media (hover: hover) and (pointer: fine).
8. Self-check against Never Ship: Check for transition: all, scale(0), ease-in, built-in ease-out on deliberate motion, animated shortcuts, UI over 300ms, centered popover origin, keyframes on rapid elements, layout properties, Motion shorthands, ungated hover, missing reduced motion, and everything entering at once.
9. Report briefly: After the code, state the gate result, the ingredients one per line, and what needs a feel-check (2-5x speed or DevTools inspector, frame by frame, real device, fresh eyes next day).

### Examples and visual references

- A command launcher with no open/close animation (Raycast): Opens and closes instantly, which the source calls correct for something opened hundreds of times a day.
- Decorative mouse-tracking effect (Marketing page vs a graph in a banking app): Fine on a marketing page; wrong on data the user is reading or acting on.
- Motion shorthand vs full transform string (Motion (React)): animate={{ x: 100 }} drops frames under load; animate={{ transform: "translateX(100px)" }} is hardware accelerated.
- Toast entering and leaving: A toast that slides in from the bottom leaves through the bottom, which makes swipe-to-dismiss feel obvious.
- Hold-to-confirm timing: The press fills slowly over 2s linear; releasing snaps back in 200ms ease-out.
- Reduced-motion and hover-gating CSS: Under prefers-reduced-motion the element uses animation: fade 0.2s ease; hover scale(1.05) is wrapped in @media (hover: hover) and (pointer: fine).
- Dropdown speed comparison: A 180ms dropdown feels more responsive than a 400ms one.

### Numbers

- 100+ times/day: Frequency at which an action gets no animation, ever [1. Should this animate at all?]
- cubic-bezier(0.23, 1, 0.32, 1): --ease-out: strong ease-out for UI [Built-in CSS easings are too weak]
- cubic-bezier(0.77, 0, 0.175, 1): --ease-in-out: strong ease-in-out for on-screen movement [Built-in CSS easings are too weak]
- cubic-bezier(0.32, 0.72, 0, 1): --ease-drawer: iOS-like drawer curve (Ionic) [Built-in CSS easings are too weak]
- cubic-bezier(0.4, 0, 0.2, 1): Example of a familiar-looking curve that must not be invented [Hard Rules: 2. No approximated values]
- 100–160ms: Button press feedback duration [Duration table]
- 125–200ms: Tooltips and small popovers duration [Duration table]
- 150–250ms: Dropdowns and selects duration; also the fallback for UI durations over 300ms [Duration table; Never Ship]
- 200–500ms: Modals and drawers duration [Duration table]
- 300ms: Ceiling for UI animations [UI animations stay under 300ms]
- 180ms / 400ms: A 180ms dropdown feels more responsive than a 400ms one [UI animations stay under 300ms]
- 200ms: ease-out at 200ms feels faster than ease-in at 200ms [Never ease-in on UI]
- scale(0.9–0.97): Starting scale for entrances, with opacity 0 [Never scale(0)]
- scale(0.95): Replacement for a scale(0) entrance, with opacity 0 [Never Ship]
- duration: 0.5, bounce: 0.2: Apple-style spring config [Reach for a spring instead]
- mass: 1, stiffness: 100, damping: 10: Traditional physics spring config [Reach for a spring instead]
- 0.1–0.3: Range for spring bounce [Keep bounce at 0.1–0.3]
- 2s linear / 200ms ease-out: Hold-to-confirm press vs release timing [Asymmetric timing where the user is deciding]
- 0.2s: Reduced-motion fade duration in the example (animation: fade 0.2s ease) [7. Reduced motion and pointer gating]
- scale(1.05): Example hover transform shown inside the hover/pointer media query [7. Reduced motion and pointer gating]
- 30–80ms: Stagger between items entering together [Never Ship: Everything entering at once]
- 2–5×: Slow-down factor for feel-checking an animation [Output: What to feel-check]

<!-- /od:learn -->
