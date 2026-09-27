---
type: source
title: "emilkowalski/skills: skills/emil-design-eng/SKILL.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-emil-design-eng-skill
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/emil-design-eng/SKILL.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - animation
  - motion
  - easing
  - duration
  - springs
  - gestures
  - performance
  - reduced-motion
  - css
  - react
  - sonner
  - design-engineering
---

# emilkowalski/skills: skills/emil-design-eng/SKILL.md

## Metadata

- Page ID: `eks-skills-emil-design-eng-skill`
- Publisher: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/emil-design-eng/SKILL.md

## Summary

This is Emil Kowalski's design-engineering agent skill: a compact rulebook for UI polish, animation decisions and component details. It gives a four-step framework for any animation (should it animate, why, which easing, how fast) with a frequency table, an easing decision tree, three custom cubic-bezier curves and a duration table capped at 300ms for UI. It adds concrete component rules (press scale 0.97, never scale(0), origin-aware popovers, instant subsequent tooltips), spring, gesture and performance rules, reduced-motion and touch-hover handling, the principles behind Sonner, stagger and debugging practice, and a review checklist. For a design system these become motion tokens, component behaviour defaults and a locked review checklist.

## Key Ideas

- Taste is trained by studying and reverse engineering great interfaces.
- Invisible details compound; people love interfaces without knowing why.
- Decide whether to animate by how often people see the element; frequent or keyboard actions get no animation.
- Every animation needs a purpose: spatial consistency, state, explanation, feedback or avoiding jarring change.
- Easing follows the job: ease-out to enter or exit, ease-in-out to move, ease for hover, linear for constant motion, never ease-in.
- Built-in CSS easings are too weak; use strong custom curves.
- UI animation stays under 300ms, and speed shapes perceived performance.
- Springs suit gestures and interruptible motion because they keep velocity; keep bounce subtle.
- Pressable things scale to about 0.97; nothing enters from scale(0); popovers grow from their trigger, modals from center.
- Transitions beat keyframes for rapidly triggered UI because they retarget instead of restarting.
- Animate only transform and opacity; prefer CSS or WAAPI when the main thread is busy.
- Reduced motion means fewer and gentler animations, not zero.
- Loved components come from low-friction setup, excellent defaults, invisible edge-case handling and cohesive motion.
- Be slow where the user decides and fast where the system responds.
- Debug motion in slow motion, frame by frame, on real devices and the next day.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer whose philosophy the skill encodes; the component principles come from building Sonner, presumably his library [inferred].
- [[entities/paul-graham|Paul Graham]] (person): Quoted on unseen details combining into something stunning.
- [[entities/raycast|Raycast]] (product): Example of a frequently used tool with no open/close animation.
- [[entities/dynamic-island|Dynamic Island]] (product): Apple feature cited as an element that should feel alive, suited to springs.
- [[entities/motion-formerly-framer-motion|Motion (formerly Framer Motion)]] (library): React animation library; useSpring for springs, with a caveat that x/y/scale shorthands are not hardware-accelerated.
- [[entities/base-ui|Base UI]] (library): Component library whose var(--transform-origin) makes popovers origin-aware.
- [[entities/ionic-framework|Ionic Framework]] (library): Source of the iOS-like drawer easing curve.
- [[entities/sonner|Sonner]] (library): Toast library (13M+ weekly npm downloads per the source) whose building produced the component principles.
- [[entities/vaul|Vaul]] (library): Drawer library cited for hiding the drawer with translateY(100%) before animating in.
- [[entities/vercel|Vercel]] (company): Where a dashboard tab animation dropped frames until moved to CSS animations.
- [[entities/family|Family]] (product): App whose drawer list shows the opacity + height combination.
- [[entities/easing-dev|easing.dev]] (tool): Resource for stronger custom easing curves.
- [[entities/easings-co|easings.co]] (tool): Resource for stronger custom easing curves.
- [[entities/web-animations-api-waapi|Web Animations API (WAAPI)]] (tool): Browser API for programmatic, hardware-accelerated CSS-performance animations.
- [[entities/starting-style|@starting-style]] (concept): CSS at-rule for animating an element's entry without JavaScript.
- [[entities/clip-path-inset|clip-path inset()]] (concept): CSS clipping used for reveals, tabs, hold-to-delete and comparison sliders.
- [[entities/prefers-reduced-motion|prefers-reduced-motion]] (concept): Media query for users who want fewer and gentler animations.
- [[entities/chrome-devtools-animations-panel|Chrome DevTools Animations panel]] (tool): Used for slow-motion and frame-by-frame animation inspection.
- [[entities/safari-remote-devtools|Safari remote devtools]] (tool): Used to debug gestures on a physical phone; Xcode Simulator is the weaker alternative.
- [[entities/intersectionobserver|IntersectionObserver]] (tool): Browser API for triggering image reveals when an element enters the viewport.

## Topics

- [[topics/motion-principles|Motion principles]]: A four-step decision framework (should it animate, purpose, easing, speed), frequency-based rules, valid purposes, no scale(0), cohesion with component personality, and asymmetric timing.
- [[topics/easing-and-timing|Easing and timing]]: Easing decision tree by job, three custom cubic-bezier tokens, never ease-in, a duration table per element type, a 300ms cap for UI, exits faster than entrances, and 30-80ms stagger.
- [[topics/spring-animation|Spring animation]]: When to use springs, useSpring for decorative mouse tracking, Apple duration+bounce config recommended over mass/stiffness/damping, subtle bounce 0.1-0.3, and velocity-preserving interruption.
- [[topics/animation-performance|Animation performance]]: Animate only transform and opacity, avoid inherited CSS variable updates during drag, Framer Motion shorthands are main-thread, CSS animations beat JS under load, and WAAPI for programmatic control; blur under 20px.
- [[topics/gestures-and-drag|Gestures and drag]]: Velocity-based dismissal above ~0.11, damping and friction at boundaries, pointer capture, multi-touch protection, and testing gestures on real devices.
- [[topics/micro-interactions|Micro-interactions]]: Press scale 0.97 on :active, blur to mask crossfades, hold-to-delete with clip-path, clipped tab color transitions and comparison sliders.
- [[topics/reduced-motion|Reduced motion]]: Reduced motion means fewer and gentler animations, keeping opacity and color while removing movement; useReducedMotion in React.
- [[topics/accessibility|Accessibility]]: Motion sickness risk and reduced motion, plus gating hover animations behind (hover: hover) and (pointer: fine) for touch devices.
- [[topics/toasts-and-notifications|Toasts and notifications]]: Toasts enter and exit from the same direction, use transitions rather than keyframes, pause timers when the tab is hidden, fill stack gaps to keep hover, and Sonner's slower ease-based motion.
- [[topics/drawers-and-sheets|Drawers and sheets]]: iOS-like drawer curve, translateY(100%) hiding, 200-500ms duration, damping and friction when dragging past the top, and avoiding inherited CSS variables during swipe.
- [[topics/modals-and-popovers|Modals and popovers]]: Popovers and tooltips scale from their trigger via var(--transform-origin); modals stay centered; tooltip delay then instant subsequent tooltips.
- [[topics/buttons-and-actions|Buttons and actions]]: Buttons scale to 0.97 on press with a 160ms ease-out transform, and hold-to-delete uses a slow press and snappy release.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: Faster-spinning spinners make loading feel faster; transitions prevent jarring appear/disappear changes.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Taste is trained, unseen details compound, and beauty is leverage in software.
- [[topics/design-process|Design process]]: Answer the framework before coding, review the next day, slow motion and frame-by-frame inspection, real-device testing, and Before/After/Why review tables.
- [[topics/ui-libraries|UI libraries]]: Sonner principles for building loved components: minimal setup, great defaults over options, memorable naming, invisible edge cases, transitions for dynamic UI, and interactive docs.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Named easing tokens (--ease-out, --ease-in-out, --ease-drawer) and per-element duration ranges suitable as motion tokens.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: @starting-style with a data-mounted fallback, percentage translates, 3D transforms, clip-path inset techniques, WAAPI, useInView and IntersectionObserver.

## Notable Claims

- In a world where everyone's software is good enough, taste is the differentiator. Evidence: You are a design engineer with the craft sensibility.
- Good taste is a trained instinct, not personal preference or something innate. Evidence: Taste is trained, not innate
- People select tools based on the overall experience, not just functionality. Evidence: Beauty is leverage
- Animation on actions repeated hundreds of times a day makes them feel slow, delayed and disconnected. Evidence: Never animate keyboard-initiated actions.
- Built-in CSS easings are too weak to make animations feel intentional. Evidence: Critical: use custom easing curves.
- A dropdown with ease-in at 300ms feels slower than one with ease-out at 300ms, because ease-in delays the initial movement. Evidence: Never use ease-in for UI animations.
- A faster-spinning spinner makes loading feel faster even when load time is identical. Evidence: Perceived performance
- ease-out at 200ms feels faster than ease-in at 200ms because the user sees immediate movement. Evidence: Perceived performance
- Springs feel more natural than duration-based animations because they simulate real physics and have no fixed duration. Evidence: Spring Animations
- Springs maintain velocity when interrupted, while CSS animations and keyframes restart from zero. Evidence: Interruptibility advantage
- The default transform-origin: center is wrong for almost every popover. Evidence: Make popovers origin-aware
- CSS transitions can be interrupted and retargeted mid-animation; keyframes restart from zero. Evidence: Use CSS transitions over keyframes for interruptible UI
- Blur during a crossfade blends old and new states so the eye perceives one smooth transformation instead of two objects swapping. Evidence: Why blur works
- Heavy blur is expensive, especially in Safari. Evidence: Keep blur under 20px.
- @starting-style replaces the React pattern of setting mounted: true in useEffect after the first render. Evidence: Animate enter states with @starting-style
- Percentage values in translate() are relative to the element's own size. Evidence: translateY with percentages
- scale() scales an element's children too, unlike width/height, so text and icons scale with a pressed button. Evidence: scale() scales children too
- Clipping a duplicated, active-styled tab list creates a color transition that timing individual color transitions can never achieve. Evidence: Tabs with perfect color transitions
- A clip-path comparison slider needs no extra DOM elements and is fully hardware-accelerated. Evidence: Comparison sliders
- Without multi-touch protection, switching fingers mid-drag makes the element jump to the new position. Evidence: Multi-touch protection
- Transform and opacity skip layout and paint and run on the GPU; animating padding, margin, height or width triggers all three rendering steps. Evidence: Only animate transform and opacity
- Changing a CSS variable on a parent recalculates styles for all its children. Evidence: CSS variables are inheritable
- Framer Motion's x, y and scale shorthands are not hardware-accelerated; they use requestAnimationFrame on the main thread. Evidence: Framer Motion hardware acceleration caveat
- At Vercel, a dashboard tab animation using Shared Layout Animations dropped frames during page loads, and switching to CSS animations fixed it. Evidence: Framer Motion hardware acceleration caveat
- CSS animations run off the main thread and stay smooth when the browser is busy loading a page. Evidence: CSS animations beat JS under load
- The Web Animations API is hardware-accelerated, interruptible and needs no library. Evidence: Use WAAPI for programmatic CSS animations
- Animations can cause motion sickness. Evidence: prefers-reduced-motion
- Touch devices trigger hover on tap, causing false positives. Evidence: Touch device hover states
- Most users never customize a component's defaults. Evidence: Good defaults matter more than options.
- Sonner's animation is slightly slower than typical UI animation and uses ease rather than ease-out to feel more elegant. Evidence: Cohesion matters
- There is no formula for combining opacity and height animations on list items; it takes trial and error. Evidence: The opacity + height combination
- Imperfections missed during development are noticed when reviewing the next day. Evidence: Review your work the next day

## Quotes

> Never animate keyboard-initiated actions.
> Reduced motion means fewer and gentler animations, not zero.
> Good defaults matter more than options.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is an AI agent skill (SKILL.md), so parts of it are agent behaviour rather than design guidance: a scripted first reply and a required review output format.
- Caveat: Snapshot of commit 85e8e23; library-specific advice (Framer Motion shorthands not being hardware-accelerated, @starting-style browser support) may change with later versions [inferred].
- Caveat: Internal tension: 'UI animations should stay under 300ms' and the checklist fix of 150-250ms sit beside a 200-500ms range for modals and drawers and 400ms toast examples; Sonner is deliberately slower than typical UI.
- Caveat: The checklist example 'enter 2s, exit 200ms' comes from the hold-to-delete press/release pattern, not from ordinary entrance animations. [inferred]
- Caveat: The 0.11 velocity threshold is computed as swipe distance divided by milliseconds in the code sample; units are not stated [inferred].
- Caveat: Sonner's '13M+ weekly npm downloads' is a figure the source states about the library it draws its principles from, likely the author's own (self-promotion) [inferred]; not independently checked here.
- Caveat: The spring mouse-tracking pattern is explicitly decorative; the source says functional displays (a banking graph) are better without animation.
- Caveat: The 'Initial Response' section (a scripted first reply, then nothing until the user asks a question) is persona behaviour for this agent skill and is deliberately not recorded as a design rule.

### Rules and practices

- **should** (process, all): Study why the best interfaces feel the way they do: reverse engineer their animations and inspect their interactions instead of stopping once the UI works. Why: Taste is a trained instinct, built by surrounding yourself with great work, thinking about why it feels good and practising. [Taste is trained, not innate]
- **should** (patterns, all): Make every feature behave exactly as people assume it will, so they carry on without giving it a second thought. Why: Most details are never consciously noticed; the aggregate of invisible correctness is what makes people love an interface. [Unseen details compound]
- **should** (process, all): Treat good defaults and good animations as a product differentiator, not an afterthought. Why: People choose tools on the overall experience, and beauty is underused in software, so it is leverage to stand out. [Beauty is leverage]
- **must** (process, all): When reviewing UI code, report findings as one markdown table with Before | After | Why columns, one row per issue; never as separate 'Before:' and 'After:' lines. Why: The skill marks this format as required and shows the line-by-line format as wrong. Values: | Before | After | Why |. [Review Format (Required)]
- **should** (motion, all): Before writing any animation code, answer in order: should it animate at all, what is its purpose, which easing, and how fast. Why: The Animation Decision Framework says to answer these questions in order before writing any animation code. [The Animation Decision Framework]
- **must** (motion, all): Do not animate anything people trigger 100+ times a day, such as keyboard shortcuts or a command palette toggle. Why: The frequency table says 'No animation. Ever.' for this band; animation makes very frequent actions feel slow. Values: 100+ times/day. [1. Should this animate at all?]
- **should** (motion, all): Remove or drastically reduce animation on things people see tens of times a day, such as hover effects and list navigation. Why: Frequency table: tens of times/day means remove or drastically reduce. Values: Tens of times/day. [1. Should this animate at all?]
- **should** (motion, all): Give occasional elements (modals, drawers, toasts) a standard animation, and keep delight for rare or first-time moments (onboarding, feedback forms, celebrations). Why: Frequency table: occasional gets standard animation; rare/first-time can add delight. [1. Should this animate at all?]
- **must** (motion, all): Never animate keyboard-initiated actions. Why: They are repeated hundreds of times daily, and animation makes them feel slow, delayed and disconnected from the user's actions. [Never animate keyboard-initiated actions.]
- **must** (motion, all): Give every animation a clear answer to 'why does this animate?': spatial consistency, state indication, explanation, feedback, or preventing a jarring change. Why: Every animation must have a clear purpose; these are the valid ones the source lists. [2. What is the purpose?]
- **must** (motion, all): Do not animate something people see often when the only reason is that it looks cool. Why: If the purpose is just 'it looks cool' and the user will see it often, don't animate. [2. What is the purpose?]
- **should** (components, all): Make toasts enter and exit from the same direction. Why: Spatial consistency makes swipe-to-dismiss feel intuitive. [Spatial consistency]
- **should** (motion, all): Give elements a transition when they appear or disappear rather than letting them pop in or out. Why: Elements appearing or disappearing without transition feel broken. [Preventing jarring changes]
- **must** (motion, all): Use ease-out for elements entering or exiting the screen. Why: It starts fast and feels responsive. Values: ease-out. [3. What easing should it use?]
- **should** (motion, all): Use ease-in-out for elements that move or morph while staying on screen. Why: It gives natural acceleration and deceleration. Values: ease-in-out. [Is it moving/morphing on screen?]
- **should** (motion, all): Use ease for hover and color changes. Why: The easing decision tree assigns ease to hover/color changes. Values: ease. [Is it a hover/color change?]
- **should** (motion, all): Use linear only for constant motion such as a marquee or progress bar. Why: The easing decision tree assigns linear to constant motion. Values: linear. [Is it constant motion (marquee, progress bar)?]
- **should** (motion, all): When no other easing case applies, default to ease-out. Why: The decision tree's default branch is ease-out. Values: ease-out. [Default → ease-out]
- **must** (motion, css): Use custom easing curves instead of the built-in CSS keywords. Why: The built-in CSS easings are too weak and lack the punch that makes animations feel intentional. [Critical: use custom easing curves.]
- **should** (tokens, css): Define a strong ease-out token for UI interactions. Why: Given as the strong ease-out for UI interactions. Values: --ease-out: cubic-bezier(0.23, 1, 0.32, 1). [Strong ease-out for UI interactions]
- **should** (tokens, css): Define a strong ease-in-out token for on-screen movement. Why: Given as the strong ease-in-out for on-screen movement. Values: --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1). [Strong ease-in-out for on-screen movement]
- **should** (tokens, css): Define an iOS-like drawer easing token for drawers. Why: Given as the iOS-like drawer curve, taken from Ionic Framework. Values: --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1). [iOS-like drawer curve (from Ionic Framework)]
- **must** (motion, all): Never use ease-in for UI animations. Why: It starts slow, delaying movement at the moment the user watches most closely; a dropdown with ease-in at 300ms feels slower than ease-out at the same 300ms. Values: ease-in, 300ms. [Never use ease-in for UI animations.]
- **should** (tooling, all): Do not invent easing curves from scratch; pick stronger variants of standard easings from easing.dev or easings.co. Why: The source points to these as easing curve resources. Values: https://easing.dev/, https://easings.co/. [Easing curve resources]
- **should** (motion, all): Make button press feedback last 100-160ms. Why: Duration table for button press feedback. Values: 100-160ms. [4. How fast should it be?]
- **should** (motion, all): Make tooltips and small popovers animate in 125-200ms. Why: Duration table for tooltips and small popovers. Values: 125-200ms. [4. How fast should it be?]
- **should** (motion, all): Make dropdowns and selects animate in 150-250ms. Why: Duration table for dropdowns and selects. Values: 150-250ms. [4. How fast should it be?]
- **should** (motion, all): Make modals and drawers animate in 200-500ms. Why: Duration table for modals and drawers. Values: 200-500ms. [4. How fast should it be?]
- **consider** (motion, all): Allow marketing and explanatory animations to run longer than UI animations. Why: Duration table: marketing/explanatory can be longer. [Marketing/explanatory]
- **must** (motion, all): Keep UI animations under 300ms; if a UI element's animation is longer, reduce it to 150-250ms. Why: A 180ms dropdown feels more responsive than a 400ms one; the review checklist flags durations over 300ms. Values: 300ms, 150-250ms, 180ms, 400ms. [Rule: UI animations should stay under 300ms.]
- **consider** (components, all): Make loading spinners spin fast. Why: A faster-spinning spinner makes the app feel like it loads faster even when load time is identical. [Perceived performance]
- **should** (motion, all): Use springs for drag interactions with momentum, elements that should feel alive, gestures that can be interrupted mid-animation, and decorative mouse-tracking. Why: Springs simulate real physics, settle from physical parameters rather than a fixed duration, and feel more natural. [When to use springs]
- **should** (motion, react): For decorative mouse-tracking effects, interpolate the value with a spring (Motion's useSpring) instead of tying the visual directly to mouse position. Why: Tying visuals directly to mouse position feels artificial and instant; a spring adds momentum. Values: useSpring, mouseX * 0.1, stiffness: 100, damping: 10. [Spring-based mouse interactions]
- **should** (motion, all): Do not add decorative motion to functional displays, such as a functional graph in a banking app. Why: The spring mouse effect works only because it is decorative; for a functional graph no animation would be better. [If this were a functional graph in a banking app]
- **should** (motion, all): Configure springs with Apple's duration-and-bounce approach by default. Why: The source recommends it as easier to reason about. Values: { type: "spring", duration: 0.5, bounce: 0.2 }. [Apple's approach (recommended — easier to reason about)]
- **consider** (motion, all): Use traditional mass, stiffness and damping spring parameters only when you need more control. Why: The source presents traditional physics as the option with more control. Values: { type: "spring", mass: 1, stiffness: 100, damping: 10 }. [Traditional physics (more control)]
- **should** (motion, all): Avoid bounce in most UI; when you use it, keep it subtle (0.1-0.3) and reserve it for drag-to-dismiss and playful interactions. Why: The source says to keep bounce subtle and avoid it in most UI contexts. Values: 0.1-0.3. [Keep bounce subtle (0.1-0.3) when used.]
- **should** (motion, all): Use springs for interactions people may reverse mid-motion, such as clicking an item open and quickly pressing Escape. Why: Springs keep their velocity when interrupted and reverse smoothly from the current position, while CSS animations and keyframes restart from zero. [Interruptibility advantage]
- **must** (components, css): Give every pressable element a subtle scale-down on :active, with a transform transition. Why: Instant press feedback makes the UI feel like it is truly listening to the user. Values: transform: scale(0.97), transition: transform 160ms ease-out, 0.95-0.98. [Buttons must feel responsive]
- **must** (motion, css): Never animate an element in from scale(0); start from scale(0.9) or higher combined with opacity. Why: Nothing in the real world appears from nothing; scale(0) entrances look like they come out of nowhere. Values: scale(0), scale(0.9), transform: scale(0.95), opacity: 0. [Never animate from scale(0)]
- **must** (components, css): Make popovers scale in from their trigger by setting transform-origin to the trigger position (for example Base UI's CSS variable). Why: The default transform-origin: center is wrong for almost every popover; unseen details compound. Values: transform-origin: var(--transform-origin). [Make popovers origin-aware]
- **should** (components, css): Keep modals at transform-origin: center. Why: Modals are not anchored to a trigger; they appear centered in the viewport. Values: transform-origin: center. [Exception: modals.]
- **should** (components, all): Add a delay before the first tooltip appears. Why: It prevents accidental activation. [Tooltips: skip delay on subsequent hovers]
- **should** (components, css): Once one tooltip is open, open adjacent tooltips instantly with no delay and no animation. Why: It feels faster without defeating the purpose of the initial delay, and makes the whole toolbar feel faster. Values: .tooltip[data-instant], transition-duration: 0ms. [Skip animation on subsequent tooltips]
- **should** (components, css): Animate tooltips from their trigger with a short transform and opacity transition, starting and ending at a slightly reduced scale. Why: The source's tooltip CSS pattern. Values: transition: transform 125ms ease-out, opacity 125ms ease-out, opacity: 0, transform: scale(0.97), transform-origin: var(--transform-origin). [Tooltips: skip delay on subsequent hovers]
- **must** (motion, css): Use CSS transitions, not keyframes, for any UI that can be triggered rapidly (adding toasts, toggling states). Why: Transitions can be interrupted and retargeted mid-animation; keyframes restart from zero. Values: transition: transform 400ms ease. [Use CSS transitions over keyframes for interruptible UI]
- **consider** (motion, css): If a crossfade still looks wrong after trying other easings and durations, add a subtle blur during the transition. Why: Blur blends the old and new states so the eye sees one smooth transformation instead of two overlapping objects. Values: filter: blur(2px). [Use blur to mask imperfect transitions]
- **consider** (components, css): For a polished button state change, combine scale-on-press with a blurred, slightly faded content transition. Why: The source's example of blur plus press feedback. Values: transform: scale(0.97), transition: filter 200ms ease, opacity 200ms ease, filter: blur(2px), opacity: 0.7. [Combine blur with scale-on-press]
- **should** (motion, web): Keep blur under 20px. Why: Heavy blur is expensive, especially in Safari. Values: 20px. [Keep blur under 20px.]
- **should** (motion, css): Animate enter states with CSS @starting-style where browser support allows; otherwise fall back to a data-mounted attribute set after first render. Why: @starting-style animates entry without JavaScript and replaces the useEffect mounted pattern. Values: @starting-style, opacity 400ms ease, transform 400ms ease, translateY(100%), data-mounted. [Animate enter states with @starting-style]
- **should** (motion, css): Use percentage translate values (such as translateY(100%)) to move an element by its own size instead of hardcoded pixel values. Why: Percentages are relative to the element's own size, less error-prone and adapt to content; Sonner and Vaul use this. Values: translateY(100%), translateY(-100%). [translateY with percentages]
- **consider** (motion, css): Use rotateX()/rotateY() with transform-style: preserve-3d for depth effects such as orbits and coin flips, without JavaScript. Why: These create real 3D effects in CSS. Values: transform-style: preserve-3d, translateZ(72px). [3D transforms for depth]
- **should** (motion, css): Set transform-origin to where the trigger lives for origin-aware interactions. Why: Every element transforms from an anchor point that defaults to center. [transform-origin]
- **consider** (motion, css): Use clip-path: inset() to animate reveals; each value eats into the element from that side. Why: clip-path is one of the most powerful animation tools in CSS, not just for shapes. Values: clip-path: inset(0 100% 0 0), clip-path: inset(0 0 0 0). [The inset shape]
- **should** (components, css): For tab color transitions, duplicate the tab list, style the copy as active, clip the copy so only the active tab shows, and animate the clip on tab change. Why: It creates a seamless color transition that timing individual color transitions can never achieve. [Tabs with perfect color transitions]
- **should** (components, css): Build hold-to-delete with a colored overlay clipped to inset(0 100% 0 0) that transitions to inset(0 0 0 0) over 2s linear on :active, snaps back in 200ms ease-out on release, and scales the button to 0.97 on press. Why: Slow where the user is deciding, fast where the system responds, with press feedback. Values: clip-path: inset(0 100% 0 0), inset(0 0 0 0), 2s linear, 200ms ease-out, scale(0.97). [Hold-to-delete pattern]
- **consider** (motion, web): Reveal images on scroll by animating clip-path from inset(0 0 100% 0) to inset(0 0 0 0) when they enter the viewport, triggering once. Why: The source's image reveal pattern using IntersectionObserver or useInView. Values: clip-path: inset(0 0 100% 0), inset(0 0 0 0), { once: true, margin: "-100px" }. [Image reveals on scroll]
- **consider** (components, css): Build before/after comparison sliders by overlaying two images and changing the right inset of the top image's clip-path with the drag position. Why: No extra DOM elements are needed and it is fully hardware-accelerated. Values: clip-path: inset(0 50% 0 0). [Comparison sliders]
- **should** (patterns, all): Dismiss on a quick flick: compute velocity as distance divided by elapsed time and dismiss when it exceeds about 0.11, regardless of distance; do not require dragging past a threshold. Why: A quick flick should be enough. Values: velocity > 0.11, Math.abs(dragDistance) / elapsedTime. [Momentum-based dismissal]
- **should** (patterns, all): Apply damping when someone drags past a natural boundary, so the further they drag the less the element moves. Why: Things in real life don't suddenly stop; they slow down first. [Damping at boundaries]
- **should** (patterns, web): Once dragging starts, capture all pointer events on the dragged element. Why: Dragging continues even if the pointer leaves the element bounds. [Pointer capture for drag]
- **should** (patterns, all): Ignore additional touch points after the first drag begins. Why: Otherwise switching fingers mid-drag makes the element jump to the new position. [Multi-touch protection]
- **should** (patterns, all): Allow drags beyond the limit with increasing friction instead of blocking them with a hard stop. Why: It feels more natural than hitting an invisible wall. [Friction instead of hard stops]
- **must** (motion, web): Animate only transform and opacity; do not animate padding, margin, height or width. Why: Transform and opacity skip layout and paint and run on the GPU; the others trigger all three rendering steps. Values: transform, opacity. [Only animate transform and opacity]
- **must** (motion, css): Never use transition: all; name the exact properties being transitioned. Why: The review table says to specify exact properties and avoid `all`; the review checklist flags `transition: all` as an issue. Values: transition: transform 200ms ease-out. [Review Checklist]
- **must** (motion, web): During drags or frequent updates, set transform directly on the moving element instead of updating a CSS variable on its container. Why: CSS variables are inherited, so changing one on a parent recalculates styles for all children. Values: --swipe-amount, element.style.transform = `translateY(${distance}px)`. [CSS variables are inheritable]
- **must** (motion, react): In Framer Motion, animate the full transform string instead of the x, y or scale shorthands when the animation must stay smooth under load. Why: The shorthands use requestAnimationFrame on the main thread and are not hardware-accelerated, so they drop frames under load; the review checklist flags Framer Motion x/y props under load. Values: animate={{ transform: "translateX(100px)" }}, transform: "translateX()". [Framer Motion hardware acceleration caveat]
- **should** (motion, web): Use CSS animations for predetermined animations and JavaScript for dynamic, interruptible ones. Why: CSS animations run off the main thread and stay smooth while the browser is busy; requestAnimationFrame animations drop frames. [CSS animations beat JS under load]
- **should** (motion, web): Use the Web Animations API when you need programmatic control of CSS-performance animations. Why: It is hardware-accelerated, interruptible and needs no library. Values: duration: 1000, fill: 'forwards', easing: 'cubic-bezier(0.77, 0, 0.175, 1)'. [Use WAAPI for programmatic CSS animations]
- **should** (accessibility, all): Under prefers-reduced-motion, keep fewer and gentler animations rather than none: keep opacity and color transitions that aid comprehension and remove movement and position animations. Why: Animations can cause motion sickness, but reduced motion does not mean zero motion. Values: @media (prefers-reduced-motion: reduce), animation: fade 0.2s ease. [prefers-reduced-motion]
- **should** (accessibility, react): In React, read useReducedMotion and swap position-based values for static ones when it is on. Why: The source's React pattern for reduced motion. Values: closedX = shouldReduceMotion ? 0 : '-100%'. [prefers-reduced-motion]
- **must** (accessibility, css): Gate hover animations behind a hover-capable, fine-pointer media query. Why: Touch devices trigger hover on tap, causing false positives. Values: @media (hover: hover) and (pointer: fine), transform: scale(1.05). [Touch device hover states]
- **should** (components, react): Make components adoptable with minimal setup: no hooks, no context, one component mounted once and a function callable from anywhere. Why: The less friction to adopt, the more people will use it. Values: <Toaster />, toast(). [Developer experience is key.]
- **should** (process, all): Invest in excellent defaults (easing, timing, visual design) before adding options; ship beautiful out of the box. Why: Most users never customize. [Good defaults matter more than options.]
- **consider** (content, all): Give components a memorable name, trading some discoverability for memorability when appropriate. Why: Naming creates identity; 'Sonner' feels more elegant than 'react-toast'. [Naming creates identity.]
- **should** (components, web): Pause toast timers while the tab is hidden. Why: Handling edge cases invisibly is part of what makes a component loved. [Handle edge cases invisibly.]
- **should** (components, css): Fill the gaps between stacked toasts with pseudo-elements so hover state is kept while moving between them. Why: Handle edge cases invisibly; users never notice, and that is right. [Handle edge cases invisibly.]
- **should** (process, all): Build an interactive documentation site where people can touch and play with the component, with ready-to-use code snippets. Why: Interactive examples lower the barrier to adoption. [Build a great documentation site.]
- **should** (motion, all): Match animation easing and duration to the component's personality and the surrounding design: bouncier for playful components, crisp and fast for a professional dashboard. Why: Cohesion makes animation satisfying; Sonner's motion, design, page and name are in harmony. [Cohesion matters]
- **should** (motion, all): When items enter and exit a list, tune the opacity change against the height animation by trial and error until it feels right. Why: There is no formula for the opacity + height combination. [The opacity + height combination]
- **should** (process, all): Review animations again the next day with fresh eyes. Why: You notice imperfections the next day that you missed during development. [Review your work the next day]
- **must** (motion, all): Make deliberate actions slow and responses fast: slow where the user is deciding (hold-to-delete 2s linear), snappy where the system responds (release 200ms ease-out). Why: Pressing should be deliberate but release should always be snappy. Values: 2s linear, 200ms ease-out. [Asymmetric enter/exit timing]
- **must** (motion, all): Make exits faster than entrances instead of using the same speed for both. Why: The review checklist flags the same enter/exit transition speed as an issue; the source's reason is to be slow where the user is deciding and fast where the system is responding. Values: enter 2s, exit 200ms. [Same enter/exit transition speed]
- **must** (motion, all): Stagger elements that enter together, with 30-80ms between items. Why: A cascade feels more natural than everything appearing at once, and the review checklist flags elements all appearing at once; long delays make the interface feel slow. Values: 30-80ms, 0ms, 50ms, 100ms, 150ms, translateY(8px), 300ms ease-out. [Stagger Animations]
- **must** (motion, all): Never block interaction while a stagger animation is playing. Why: Stagger is decorative. [Stagger is decorative]
- **should** (process, web): Test animations in slow motion (2-5x the normal duration, or the DevTools animation inspector) and check color overlap, easing, transform-origin and whether properties stay in sync. Why: Slow motion reveals issues invisible at full speed. Values: 2-5x. [Slow motion testing]
- **should** (process, web): Step through animations frame by frame in the Chrome DevTools Animations panel. Why: It reveals timing issues between coordinated properties that you cannot see at full speed. [Frame-by-frame inspection]
- **should** (process, all): Test touch interactions such as drawers and swipe gestures on physical devices (USB, local dev server by IP, Safari remote devtools) rather than only the Xcode Simulator. Why: Real hardware is better for gesture testing. [Test on real devices]
- **should** (process, all): When reviewing UI code, check for every Review Checklist issue: transition: all, scale(0) entries, ease-in on UI elements, transform-origin: center on popovers (modals exempt), animation on keyboard actions, UI durations over 300ms, hover animation without the hover/pointer media query, keyframes on rapidly triggered elements, Framer Motion x/y props under load, the same enter/exit speed, and elements all appearing at once. Why: The source lists these as the issues to check for when reviewing UI code, each with its fix. Values: transition: all, scale(0), Duration > 300ms, Reduce to 150-250ms, @media (hover: hover) and (pointer: fine), 30-80ms. [Review Checklist]

### Decisions it informs

- Should this element animate at all?
  - No animation: Instant response; nothing slows the action down. When: Seen 100+ times a day, such as keyboard shortcuts or a command palette toggle; any keyboard-initiated action.
  - Remove or drastically reduce: Motion removed or drastically reduced. When: Seen tens of times a day, such as hover effects and list navigation.
  - Standard animation: Normal enter and exit motion. When: Occasional elements such as modals, drawers and toasts.
  - Add delight: Room to add delight. When: Rare or first-time moments such as onboarding, feedback forms and celebrations.
  - Recommendation: Decide by how often people will see it; never animate keyboard-initiated actions (Raycast has no open/close animation).
- How should easing be chosen for each animation? (`Q-motion-03`)
  - ease-out (custom, e.g. cubic-bezier(0.23, 1, 0.32, 1)): Starts fast and feels responsive. When: Elements entering or exiting; also the default.
  - ease-in-out (custom, e.g. cubic-bezier(0.77, 0, 0.175, 1)): Natural acceleration and deceleration. When: Elements moving or morphing on screen.
  - ease: Gentle, even change. [inferred] When: Hover and color changes.
  - linear: Constant speed. When: Constant motion such as a marquee or progress bar.
  - ease-in: Starts slow, so the UI feels sluggish. When: Never for UI animations.
  - Recommendation: Choose by the job the motion does, using strong custom curves rather than the built-in keywords; never ease-in.
- How long should UI animations be, and should exits match entrances? (`Q-motion-02`)
  - Per-element durations under 300ms: Button press 100-160ms, tooltips 125-200ms, dropdowns 150-250ms; UI feels responsive. When: All product UI.
  - Longer durations: Modals and drawers 200-500ms; marketing can be longer. When: Modals, drawers, marketing or explanatory animation.
  - Asymmetric timing: Slow where the user decides, fast where the system responds; exits faster than entrances. When: Deliberate actions like hold-to-delete (2s linear press, 200ms ease-out release).
  - Recommendation: Keep UI animations under 300ms and make exits faster than entrances.
- How should springs be configured? (`Q-motion-04`)
  - Apple's duration + bounce: Easier to reason about, e.g. { type: "spring", duration: 0.5, bounce: 0.2 }. When: Default.
  - Mass, stiffness, damping: More control, e.g. { type: "spring", mass: 1, stiffness: 100, damping: 10 }. When: When you need finer control.
  - Recommendation: Apple's approach; keep bounce subtle (0.1-0.3) and avoid it in most UI.
- What motion personality should a component have? (`Q-motion-01`)
  - Playful: Bouncier motion. When: Playful components; drag-to-dismiss and playful interactions.
  - Crisp and fast: Crisp and fast motion. When: A professional dashboard.
  - Elegant: Slightly slower than typical UI, using ease rather than ease-out (Sonner). When: When the whole product's vibe calls for it and it stays cohesive.
  - Recommendation: Match the motion to the mood so easing, timing, design and name are in harmony.
- What should happen when someone turns on reduced motion? (`Q-motion-07`)
  - Fewer and gentler animations: Keeps opacity and color transitions that aid comprehension, removes movement and position animation. When: Default.
  - Zero animation: Removes all motion, including helpful fades. When: The source says reduced motion does not mean zero.
  - Recommendation: Fewer and gentler, not zero.
- Should elements that enter together appear one by one? (`Q-motion-06`)
  - All at once: Everything appears together, which feels less natural. When: Flagged as an issue in the review checklist.
  - Short stagger (30-80ms): A cascade that feels natural without slowing the UI. When: Multiple elements entering together.
  - Recommendation: Stagger by 30-80ms and never block interaction while it plays.
- Which animation technique should drive a UI animation?
  - CSS transitions: Interruptible and retargetable mid-animation. When: Anything triggered rapidly, like adding toasts or toggling states.
  - CSS keyframes: Restart from zero when interrupted; run off the main thread. When: Predetermined animations that will not be interrupted.
  - Springs (JS): Keep velocity when interrupted. When: Gestures, drag with momentum, reversible interactions.
  - Web Animations API: JS control with CSS performance, hardware-accelerated and interruptible. When: Programmatic animations without a library.
  - Recommendation: Transitions for dynamic UI, CSS for predetermined animation, JS for dynamic interruptible motion, WAAPI for programmatic control.
- Where should a popup scale from?
  - Its trigger (var(--transform-origin)): Grows out of the button that opened it. When: Popovers and tooltips.
  - Center: Grows from the middle of the viewport. When: Modals only, since they are not anchored to a trigger.
  - Recommendation: Trigger for popovers, center for modals.
- When should a swipe dismiss something?
  - Distance threshold only: People must drag far enough before release dismisses. When: Not recommended on its own.
  - Distance or velocity: A quick flick (velocity > 0.11) dismisses regardless of distance. When: Default for swipe-to-dismiss.
  - Recommendation: Dismiss when distance passes the threshold or velocity exceeds about 0.11.
- How should an element's enter state be animated in CSS?
  - @starting-style: Animates entry without JavaScript. When: When browser support allows.
  - data-mounted attribute set in useEffect: Legacy pattern that works everywhere. When: Fallback when @starting-style is not supported.
  - Recommendation: @starting-style, with the data-mounted fallback.

### Process

1. Decide whether to animate: Ask how often people will see it: 100+ times a day or keyboard-initiated means no animation; tens of times a day means remove or drastically reduce; occasional gets standard motion; rare can add delight.
2. Name the purpose: Write down why it animates: spatial consistency, state indication, explanation, feedback or preventing a jarring change. If it is only 'looks cool' and seen often, drop it.
3. Pick the easing: Entering or exiting: ease-out; moving on screen: ease-in-out; hover or color: ease; constant motion: linear; otherwise ease-out. Use strong custom curves, never ease-in.
4. Set the duration: Use the duration table (press 100-160ms, tooltips 125-200ms, dropdowns 150-250ms, modals and drawers 200-500ms) and keep UI animation under 300ms; make exits faster than entrances.
5. Choose the technique: Transitions for rapidly triggered UI, springs for gestures and interruptible motion, CSS for predetermined animation, WAAPI for programmatic control; animate only transform and opacity.
6. Test in slow motion: Raise durations 2-5x or use the DevTools animation inspector; check color overlap, easing, transform-origin and property sync.
7. Step frame by frame: Use the Chrome DevTools Animations panel to catch timing issues between coordinated properties.
8. Test gestures on real devices: Connect a phone over USB, open the local dev server by IP and use Safari remote devtools; the Xcode Simulator is a weaker alternative.
9. Review the next day: Look at the animation again with fresh eyes to spot imperfections missed during development.
10. Report review findings as a table: Run the review checklist and output one markdown table with Before | After | Why columns, one row per issue.

### Examples and visual references

- Launcher with no open/close animation (Raycast): Opens and closes instantly; the source calls this optimal for something used hundreds of times a day.
- An element that feels alive (Apple Dynamic Island): Cited as the kind of element that suits spring animation.
- Toast positioning with percentage translates such as translateY(-100%) (Sonner): Toasts move by their own height; the animation is slightly slower than typical UI and uses ease for an elegant, cohesive feel.
- Drawer hidden with translateY(100%) before animating in (Vaul): Works regardless of drawer height.
- Dashboard tab animation that dropped frames (Vercel): Shared Layout Animations dropped frames during page loads; switching to CSS animations (off main thread) fixed it.
- List items entering and exiting a drawer (Family): Opacity and height animations had to be tuned together by trial and error.
- Hold-to-delete button: A colored overlay fills left to right via clip-path over 2s linear while held, snaps back in 200ms ease-out on release; the button scales to 0.97.
- Tabs with a clipped duplicate layer: An 'active' copy of the tab list is clipped so only the active tab shows; animating the clip on tab change gives a seamless color transition.
- Before/after comparison slider: Two stacked images; the top one is clipped with inset(0 50% 0 0) and the inset follows the drag.
- Spring-smoothed mouse-tracking rotation: Rotation follows mouseX * 0.1 through useSpring (stiffness 100, damping 10), giving momentum instead of an instant, artificial response.
- CSS 3D orbit: An element orbits using rotateY and translateZ(72px) inside a preserve-3d wrapper, with no JavaScript.
- Balloon analogy for entry scale: Starting from scale(0.9)+ is like a deflated balloon that still has a visible shape, rather than appearing from nothing.

### Numbers

- 100+ times/day: Frequency at which an element should never animate (keyboard shortcuts, command palette toggle) [1. Should this animate at all?]
- 100-160ms: Button press feedback duration [4. How fast should it be?]
- 125-200ms: Tooltips and small popovers duration [4. How fast should it be?]
- 150-250ms: Dropdowns and selects duration; also the fix for UI durations over 300ms [4. How fast should it be?]
- 200-500ms: Modals and drawers duration [4. How fast should it be?]
- 300ms: Upper limit for UI animations; also the ease-in vs ease-out dropdown comparison and the stagger fade-in duration [Rule: UI animations should stay under 300ms.]
- 180ms: A 180ms dropdown/select feels more responsive than a 400ms one [Perceived performance]
- cubic-bezier(0.23, 1, 0.32, 1): Strong ease-out for UI interactions [Critical: use custom easing curves.]
- cubic-bezier(0.77, 0, 0.175, 1): Strong ease-in-out for on-screen movement; also used in the WAAPI example [Critical: use custom easing curves.]
- cubic-bezier(0.32, 0.72, 0, 1): iOS-like drawer curve from Ionic Framework [Critical: use custom easing curves.]
- scale(0.97): Button :active press scale; also tooltip start/end scale [Buttons must feel responsive]
- 0.95-0.98: Range for press scale on pressable elements [The scale should be subtle (0.95-0.98).]
- 160ms: Button transform transition for press feedback [transition: transform 160ms ease-out]
- scale(0.9): Minimum starting scale for entrances (with opacity) [Never animate from scale(0)]
- 125ms: Tooltip transform and opacity transition [Tooltips: skip delay on subsequent hovers]
- 0ms: Transition duration for subsequent (instant) tooltips [.tooltip[data-instant]]
- 400ms: Toast transition in the transitions-vs-keyframes and @starting-style examples; also the slower dropdown compared with 180ms [transition: transform 400ms ease]
- blur(2px): Blur added during crossfades to mask imperfect transitions [Use blur to mask imperfect transitions]
- 20px: Maximum blur, because heavy blur is expensive especially in Safari [Keep blur under 20px.]
- 0.1-0.3: Subtle spring bounce range [Spring configuration]
- duration: 0.5, bounce: 0.2: Apple-style spring configuration example [Apple's approach]
- mass: 1, stiffness: 100, damping: 10: Traditional physics spring configuration example [Traditional physics (more control)]
- 0.11: Swipe velocity above which a toast/drawer dismisses regardless of distance [Momentum-based dismissal]
- 2s: Linear hold duration for hold-to-delete press [Hold-to-delete pattern]
- 200ms: ease-out release/snap-back for hold-to-delete; also the exact-property transition example and the blurred button-content filter/opacity transition [Asymmetric enter/exit timing]
- 30-80ms: Delay between staggered items [Stagger Animations]
- translateY(8px): Starting offset for staggered items fading in over 300ms ease-out [Stagger Animations]
- 2-5x: How much to lengthen durations for slow-motion testing [Slow motion testing]
- 0.2s: Fade animation duration in the reduced-motion example [prefers-reduced-motion]
- -100px: useInView margin for triggering image reveals on scroll [Image reveals on scroll]
- 13M+: Sonner weekly npm downloads, as stated by the source [The Sonner Principles]
- scale(0.95): Entry start scale, combined with opacity: 0, instead of scale(0) (review table and checklist fix) [Never animate from scale(0)]
- opacity: 0.7: Button content opacity while blurred during a state transition [Use blur to mask imperfect transitions]
- transform: scale(1.05): Example hover scale gated behind @media (hover: hover) and (pointer: fine) [Touch device hover states]
- 50ms: Step between nth-child animation delays in the stagger example (0ms, 50ms, 100ms, 150ms) [Stagger Animations]
- translateY(100%): Hides a drawer (Vaul) or starts a toast's @starting-style entry by its own height [translateY with percentages]
- translateZ(72px): Orbit radius in the CSS 3D orbit keyframes [3D transforms for depth]
- duration: 1000: WAAPI clip-path reveal example duration [Use WAAPI for programmatic CSS animations]
- inset(0 50% 0 0): Starting clip on the top image of a comparison slider [Comparison sliders]
- mouseX * 0.1: Rotation factor in the spring mouse-tracking example [Spring-based mouse interactions]

<!-- /od:learn -->
