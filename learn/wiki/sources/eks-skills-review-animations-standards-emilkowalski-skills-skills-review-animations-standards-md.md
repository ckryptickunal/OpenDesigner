---
type: source
title: "emilkowalski/skills: skills/review-animations/STANDARDS.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-review-animations-standards
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/review-animations/STANDARDS.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - animation
  - motion
  - easing
  - cubic-bezier
  - duration
  - springs
  - interruptibility
  - performance
  - clip-path
  - gestures
  - stagger
  - reduced-motion
---

# emilkowalski/skills: skills/review-animations/STANDARDS.md

## Metadata

- Video ID: `eks-skills-review-animations-standards`
- Channel: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/review-animations/STANDARDS.md

## Summary

This is the rule catalog behind Emil Kowalski's review-animations skill: the exact values, curves and rules a motion review should cite instead of approximating. It covers whether to animate by frequency of use, easing by motion type with three strong custom cubic-bezier curves, a per-element duration table with a sub-300ms UI rule, physical correctness (no scale(0), trigger-origin popovers, press feedback), spring configs, interruptibility, asymmetric timing, GPU-only performance, transforms and clip-path techniques, drag gestures, crossfade blur, stagger, accessibility, debugging and cohesion. For a design system it is close to a ready-made motion token set and rulebook: the curves, durations, spring parameters and thresholds can become locked tokens and lint checks.

## Key Ideas

- Frequency decides whether to animate: 100+/day and keyboard actions never animate, rare moments can delight.
- Easing is chosen by motion type, with ease-out as the default and ease-in banned on UI.
- Built-in CSS easings are too weak; three strong custom curves cover UI, on-screen movement and drawers.
- Each element type has a duration band, and UI animation stays under 300ms.
- Nothing appears from nothing: start from scale(0.9–0.97) with opacity, scale popovers from the trigger, keep modals centered.
- Springs have no fixed duration and keep velocity when interrupted; the Apple-style duration-plus-bounce config is recommended.
- Transitions retarget mid-animation while keyframes restart, so rapid UI uses transitions or @starting-style.
- Slow where the user decides, fast where the system responds.
- Only transform and opacity are animated; a CSS variable on a parent recalcs every child's styles, and Framer Motion shorthands drop frames under load.
- clip-path: inset() and percentage translates are versatile tools for reveals, overlays, tabs and drawers.
- Drag dismissal uses velocity, boundary damping, pointer capture, multi-touch protection and friction instead of hard stops.
- A small blur masks imperfect crossfades; stagger groups by 30–80ms without blocking interaction.
- Reduced motion keeps opacity and color but drops movement; hover motion is gated to fine pointers.
- Feel is checked in slow motion, frame-by-frame, on real devices and with fresh eyes.
- Motion should match the component's personality, as Sonner's slightly slower ease shows.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer whose philosophy these standards are distilled from.
- [[entities/raycast|Raycast]] (product): Cited as correct for having no open/close animation on something used hundreds of times a day.
- [[entities/ionic|Ionic]] (library): Source of the iOS-like drawer curve cubic-bezier(0.32, 0.72, 0, 1).
- [[entities/easing-dev|easing.dev]] (tool): Suggested place to find easing curves instead of hand-rolling them.
- [[entities/easings-co|easings.co]] (tool): Suggested place to find easing curves instead of hand-rolling them.
- [[entities/base-ui|Base UI]] (library): Exposes var(--transform-origin) for trigger-origin popovers.
- [[entities/dynamic-island|Dynamic Island]] (product): Example of an 'alive' element suited to spring animation.
- [[entities/framer-motion|Framer Motion]] (library): Its x/y/scale shorthands run on the main thread and drop frames under load; the full transform string is the fix.
- [[entities/sonner|Sonner]] (library): Toast library cited for percentage translates and as the model of motion cohesion.
- [[entities/vaul|Vaul]] (library): Drawer library cited for positioning with percentage translates.
- [[entities/waapi|WAAPI]] (concept): Gives JS control with CSS performance: hardware-accelerated, interruptible, no library.
- [[entities/starting-style|@starting-style]] (concept): Used for entry animations without JS.
- [[entities/clip-path-inset|clip-path: inset()]] (concept): Animation tool for reveals, hold-to-delete overlays, tab color transitions and comparison sliders.
- [[entities/chrome-devtools-animations-panel|Chrome DevTools Animations panel]] (tool): Used for slow-motion and frame-by-frame animation inspection.
- [[entities/safari-remote-devtools|Safari remote devtools]] (tool): Used to debug gestures on a real phone.

## Topics

- [[topics/motion-principles|Motion principles]]: A frequency table decides whether to animate; valid purposes are spatial consistency, state indication, explanation, feedback and preventing jarring change.
- [[topics/easing-and-timing|Easing and timing]]: Easing by motion type (ease-out default, never ease-in on UI), three custom cubic-bezier curves, per-element durations, the sub-300ms UI rule and asymmetric timing.
- [[topics/spring-animation|Spring animation]]: Apple-style { duration: 0.5, bounce: 0.2 } recommended, a traditional mass/stiffness/damping alternative, subtle bounce 0.1–0.3, and useSpring for decorative mouse tracking.
- [[topics/animation-performance|Animation performance]]: Only transform and opacity, no parent CSS variables driving child transforms, full transform strings instead of Framer Motion shorthands, CSS over JS under load, and WAAPI.
- [[topics/gestures-and-drag|Gestures and drag]]: Velocity-based momentum dismissal, damping at boundaries, pointer capture, multi-touch protection, and friction over hard stops.
- [[topics/micro-interactions|Micro-interactions]]: Button press feedback at scale(0.97) with a 160ms ease-out transition, and asymmetric press/release timing for a press-and-hold clip-path overlay.
- [[topics/reduced-motion|Reduced motion]]: Keep opacity and color, drop transform-based movement; fewer and gentler animations, not zero; useReducedMotion example.
- [[topics/accessibility|Accessibility]]: Reduced-motion media query and hover gating behind (hover: hover) and (pointer: fine) because touch fires false hovers.
- [[topics/toasts-and-notifications|Toasts and notifications]]: Toasts use interruptible transitions and @starting-style entry; Sonner positions toasts with percentage translates and uses slightly slower ease for elegance.
- [[topics/drawers-and-sheets|Drawers and sheets]]: Modals and drawers get 200–500ms, an iOS-like drawer curve, percentage translates as in Vaul, and real-device testing for drawer gestures.
- [[topics/modals-and-popovers|Modals and popovers]]: Popovers scale from the trigger via var(--transform-origin); modals stay centered; tooltips and small popovers run 125–200ms and later tooltips can be instant.
- [[topics/buttons-and-actions|Buttons and actions]]: Every pressable element gets subtle scale(0.95–0.98) press feedback on :active.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: Faster spinners make loading feel faster for the same actual time.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Concrete CSS and JS snippets for transitions, @starting-style, clip-path, WAAPI, stagger, media queries and Framer Motion.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Motion must match component personality; list opacity and height tuning has no formula and needs trial and error; review with fresh eyes.
- [[topics/design-process|Design process]]: Debugging method for motion feel: slow motion, frame-by-frame, real devices and fresh eyes the next day.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Named easing curves --ease-out, --ease-in-out and --ease-drawer are defined as CSS custom properties alongside a duration table.

## Notable Claims

- Animating keyboard-initiated actions makes them feel slow and disconnected because they repeat hundreds of times daily. Evidence: Never animate keyboard-initiated actions
- Raycast has no open/close animation, which is correct for something used hundreds of times a day. Evidence: Should it animate? (frequency table)
- ease-in starts slow, delaying the exact moment the user is watching. Evidence: Never `ease-in` on UI
- ease-out at 200ms feels faster than ease-in at 200ms. Evidence: Never `ease-in` on UI
- Built-in CSS easings are too weak. Evidence: Easing
- A 180ms dropdown feels more responsive than a 400ms one. Evidence: Duration
- Faster spinners make load feel faster for the same actual time. Evidence: Duration
- Making tooltips instant after the first one (skipping delay and animation) makes a toolbar feel faster. Evidence: Duration
- Springs feel natural because they simulate physics and have no fixed duration. Evidence: Springs
- Springs maintain velocity when interrupted, whereas keyframes restart from zero. Evidence: Springs
- Tying a value directly to mouse position feels artificial and has no momentum. Evidence: Mouse interactions
- CSS transitions can be interrupted and retargeted mid-animation; keyframes restart from zero. Evidence: Interruptibility
- transform and opacity skip layout and paint and run on the GPU; padding, margin, height, width, top and left trigger all three rendering steps. Evidence: Performance
- Setting a CSS variable on a parent recalculates styles for all children. Evidence: Don't drive child transforms via a CSS variable on the parent
- Framer Motion x/y/scale shorthands are not hardware-accelerated; they run on the main thread via rAF and drop frames under load. Evidence: Framer Motion shorthands are NOT hardware-accelerated
- CSS animations run off the main thread and beat JS under load; rAF-based animations stutter while the browser loads, scripts or paints. Evidence: CSS animations beat JS under load
- WAAPI gives JS control with CSS performance: hardware-accelerated, interruptible, no library. Evidence: WAAPI
- translate percentages are relative to the element's own size, which is how Sonner and Vaul position toasts and drawers. Evidence: Transforms & clip-path
- scale() scales children too, including font, icons and content. Evidence: Transforms & clip-path
- Touch devices fire false hovers on tap. Evidence: Accessibility: gate hover motion
- Heavy blur is expensive, especially in Safari. Evidence: Masking imperfect crossfades
- Stagger delays longer than 30–80ms feel slow. Evidence: Stagger
- Sonner feels right partly because easing, duration, design and even the name are in harmony. Evidence: Cohesion
- Opacity plus height in entering/exiting lists has no formula and is trial and error. Evidence: Cohesion
- Imperfections invisible during development surface later, so a fresh look the next day catches them. Evidence: Debugging: Fresh eyes next day

## Quotes

> No animation. Ever.
> Nothing in the real world appears from nothing.
> Slow where the user is deciding, fast where the system responds.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is the reference file of an AI-agent skill, pinned to commit 85e8e23 of emilkowalski/skills (MIT); values can change in later commits.
- Caveat: The sub-300ms UI rule sits beside a 200–500ms band for modals and drawers and 400ms toast examples; the 300ms ceiling does not appear to cover modals, drawers or these toasts [inferred].
- Caveat: The toast examples use plain ease at 400ms, which differs from the ease-out default; the Cohesion section explains Sonner's slightly slower ease as a deliberate choice for elegance, which likely accounts for the toast examples [inferred].
- Caveat: The stagger example uses @keyframes, which the Interruptibility section avoids for rapidly triggered UI; stagger is a one-off group entrance, not a rapid trigger [inferred].
- Caveat: The ~0.11 velocity threshold is written as approximate and has no stated unit; px per ms is implied by distance/elapsedMs [inferred].
- Caveat: The Framer Motion shorthand and rAF performance claims are stated without a benchmark or library version.
- Caveat: var(--transform-origin) is Base UI's variable; other libraries may expose a different name [inferred].
- Caveat: Raycast, Dynamic Island, Sonner and Vaul are single illustrative examples, not surveys.
- Caveat: The Cohesion section tunes opacity plus height for entering and exiting lists, while Performance says not to animate height; list enter/exit appears to be a named exception tuned by feel [inferred].
- Caveat: OpenDesigner's questionnaire suggests different values: Q-motion-06 offers a 20-50ms stagger (this source: 30–80ms) and Q-motion-04's Apple option lists bounce 0 / 0.15 / 0.3 (this source: 0.2 recommended, 0.1–0.3 range). As a non-negotiable source these values should take precedence [inferred].

### Rules and practices

- **must** (process, all): Cite the exact values in this reference in review findings instead of approximating. Why: These are the precise values behind the review. [Cite these in findings instead of approximating]
- **must** (motion, all): Do not animate actions used 100+ times a day, such as keyboard shortcuts and the command palette toggle. Why: No animation. Ever. Values: 100+ times/day. [Should it animate? (frequency table)]
- **must** (motion, all): Remove or drastically reduce animation on actions used tens of times a day, such as hover effects and list navigation. Why: Frequency table decision for tens of times/day. Values: Tens of times/day. [Should it animate? (frequency table)]
- **should** (motion, all): Give occasional UI such as modals, drawers and toasts standard animation. Why: Frequency table decision for occasional use. [Should it animate? (frequency table)]
- **consider** (motion, all): Add delight only to rare or first-time moments such as onboarding, feedback and celebrations. Why: Frequency table decision for rare/first-time use. [Should it animate? (frequency table)]
- **must** (motion, all): Never animate keyboard-initiated actions. Why: They repeat hundreds of times daily; animation makes them feel slow and disconnected. [Never animate keyboard-initiated actions]
- **must** (motion, all): Animate only for a valid purpose: spatial consistency, state indication, explanation, feedback, or preventing a jarring change. Why: These are the valid purposes for motion. [Valid purposes for motion]
- **must** (motion, all): Do not justify motion on a frequently seen element with 'it looks cool'. Why: 'It looks cool' on a frequently-seen element is not valid. [Valid purposes for motion]
- **must** (motion, all): Use ease-out for elements entering or exiting. Why: It starts fast and feels responsive. Values: ease-out. [Easing: Decision order]
- **should** (motion, all): Use ease-in-out for elements moving or morphing on screen. Why: Easing decision order for on-screen movement. Values: ease-in-out. [Easing: Decision order]
- **should** (motion, all): Use ease for hover and color changes. Why: Easing decision order for hover and color. Values: ease. [Easing: Decision order]
- **should** (motion, all): Use linear for constant motion such as marquees and progress. Why: Easing decision order for constant motion. Values: linear. [Easing: Decision order]
- **should** (motion, all): Default to ease-out when no other easing case applies. Why: Easing decision order default. Values: ease-out. [Easing: Decision order]
- **must** (motion, all): Never use ease-in on UI. Why: It starts slow, delaying the exact moment the user is watching; ease-out at 200ms feels faster than ease-in at 200ms. Values: ease-in, 200ms. [Never `ease-in` on UI]
- **must** (motion, all): Use the strong custom curve cubic-bezier(0.23, 1, 0.32, 1) as the ease-out for UI instead of the built-in ease-out. Why: Built-in CSS easings are too weak. Values: --ease-out: cubic-bezier(0.23, 1, 0.32, 1). [Easing: strong custom curves]
- **must** (motion, all): Use cubic-bezier(0.77, 0, 0.175, 1) as the ease-in-out for on-screen movement. Why: Built-in CSS easings are too weak. Values: --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1). [Easing: strong custom curves]
- **should** (motion, all): Use cubic-bezier(0.32, 0.72, 0, 1) for iOS-like drawers. Why: It is the iOS-like drawer curve (Ionic). Values: --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1). [Easing: strong custom curves]
- **should** (tooling, all): Find easing curves at easing.dev or easings.co instead of hand-rolling them from scratch. Why: Don't hand-roll from scratch. Values: easing.dev, easings.co. [Find curves at easing.dev or easings.co]
- **must** (motion, all): Keep button press feedback at 100–160ms. Why: Duration table value. Values: 100–160ms. [Duration table]
- **must** (motion, all): Keep tooltips and small popovers at 125–200ms. Why: Duration table value. Values: 125–200ms. [Duration table]
- **must** (motion, all): Keep dropdowns and selects at 150–250ms. Why: Duration table value; a 180ms dropdown feels more responsive than a 400ms one. Values: 150–250ms, 180ms, 400ms. [Duration table]
- **must** (motion, all): Keep modals and drawers at 200–500ms. Why: Duration table value. Values: 200–500ms. [Duration table]
- **consider** (motion, all): Allow longer durations only for marketing or explanatory animation. Why: Marketing / explanatory can be longer. [Duration table]
- **must** (motion, all): Keep UI animations under 300ms. Why: A 180ms dropdown feels more responsive than a 400ms one. Values: 300ms. [Rule: UI animations stay under 300ms]
- **should** (components, all): Make loading spinners spin faster. Why: Faster spinners make load feel faster for the same actual time. [Duration]
- **should** (components, all): After the first tooltip in a toolbar has shown, show later tooltips instantly, skipping both the delay and the animation. Why: Instant tooltips after the first make a toolbar feel faster. [Duration]
- **must** (motion, all): Never animate from scale(0); start from scale(0.9–0.97) with opacity: 0. Why: Nothing in the real world appears from nothing. Values: scale(0), scale(0.9–0.97), opacity: 0. [Physicality]
- **must** (motion, css): Scale popovers from their trigger with transform-origin: var(--transform-origin), not from center. Why: Origin-aware popovers scale from the trigger. Values: transform-origin: var(--transform-origin). [Physicality: Origin-aware popovers]
- **must** (motion, css): Keep modals at transform-origin: center. Why: Modals appear centered in the viewport, so they are exempt from trigger origin. Values: transform-origin: center. [Modals are exempt]
- **should** (components, css): Give every pressable element press feedback of transform: scale(0.97) on :active with transition: transform 160ms ease-out. Why: Button press feedback applies to any pressable element. Values: transform: scale(0.97), :active, transition: transform 160ms ease-out. [Physicality: Button press feedback]
- **should** (components, all): Keep press-feedback scale subtle, between 0.95 and 0.98. Why: Press feedback should be subtle. Values: 0.95–0.98. [Physicality: Button press feedback]
- **should** (motion, all): Use springs for drag with momentum, 'alive' elements such as the Dynamic Island, interruptible gestures and decorative mouse tracking. Why: Springs simulate physics, settle on parameters rather than a fixed duration, and feel natural. [Springs]
- **should** (motion, all): Prefer the Apple-style spring config { type: "spring", duration: 0.5, bounce: 0.2 }. Why: It is easier to reason about and is recommended. Values: type: "spring", duration: 0.5, bounce: 0.2. [Springs: Apple-style ... recommended]
- **consider** (motion, all): Use a traditional physics spring { type: "spring", mass: 1, stiffness: 100, damping: 10 } only when you need more control. Why: Traditional physics gives more control. Values: mass: 1, stiffness: 100, damping: 10. [Springs: Traditional physics (more control)]
- **must** (motion, all): Keep spring bounce subtle, between 0.1 and 0.3. Why: Bounce should be subtle. Values: 0.1–0.3. [Keep bounce subtle]
- **should** (motion, all): Avoid bounce in most UI; reserve it for drag-to-dismiss and playful interactions. Why: Bounce belongs to specific interactions, not general UI. [avoid bounce in most UI]
- **should** (motion, all): Use springs for gestures users may reverse mid-motion. Why: Springs maintain velocity when interrupted; keyframes restart from zero. [Springs maintain velocity when interrupted]
- **should** (motion, react): For decorative mouse-following motion, interpolate with useSpring rather than tying the value directly to mouse position. Why: Direct tying feels artificial and has no momentum. Values: useSpring. [Mouse interactions]
- **must** (motion, all): Do not spring-smooth mouse-tied motion unless the motion is decorative. Why: Only do this when the motion is decorative. [Mouse interactions]
- **must** (motion, css): Use CSS transitions for anything triggered rapidly, such as toasts being added or toggles. Why: Transitions can be interrupted and retargeted mid-animation, so they are smoother. Values: transition: transform 400ms ease. [Interruptibility]
- **must** (motion, css): Avoid @keyframes animations for dynamic UI. Why: Keyframes restart from zero and cannot be retargeted. Values: @keyframes slideIn. [Not interruptible — avoid for dynamic UI]
- **should** (motion, css): Use @starting-style for entry animations without JS. Why: It gives entry animation without JS, on top of an interruptible transition. Values: @starting-style { opacity: 0; transform: translateY(100%); }, transition: opacity 400ms ease, transform 400ms ease. [Use `@starting-style` for entry without JS]
- **consider** (motion, react): Where @starting-style is unavailable, fall back to useEffect(() => setMounted(true), []) with a data-mounted attribute. Why: Legacy fallback for entry animation. Values: useEffect(() => setMounted(true), []), data-mounted. [Legacy fallback]
- **must** (motion, all): Make motion slow where the user is deciding and fast where the system responds. Why: Asymmetric timing matches deliberate action versus system response. [Asymmetric timing]
- **should** (motion, css): For a press-and-hold overlay (.button:active .overlay), run the press phase slow and linear and the release phase fast with ease-out. Why: Press is deliberate; release is a system response. Values: transition: clip-path 2s linear, transition: clip-path 200ms ease-out. [Asymmetric timing code]
- **must** (motion, all): Animate only transform and opacity. Why: They skip layout and paint and run on the GPU. Values: transform, opacity. [Performance]
- **must** (motion, all): Do not animate padding, margin, height, width, top or left. Why: They trigger all three rendering steps. Values: padding, margin, height, width, top, left. [Performance]
- **must** (motion, web): Do not drive child transforms through a CSS variable on the parent; set transform directly on the element. Why: A parent variable recalculates styles for all children; a direct transform touches only that element. Values: element.style.setProperty('--swipe-amount', `${d}px`), element.style.transform = `translateY(${d}px)`. [Don't drive child transforms via a CSS variable on the parent]
- **must** (motion, react): Use the full transform string in Framer Motion (animate={{ transform: "translateX(100px)" }}) instead of x/y/scale shorthands. Why: Shorthands are not hardware-accelerated; they run on the main thread via rAF and drop frames under load. Values: animate={{ x: 100 }}, animate={{ transform: "translateX(100px)" }}. [Framer Motion shorthands are NOT hardware-accelerated]
- **should** (motion, web): Use CSS for predetermined motion and JS for dynamic or interruptible motion. Why: CSS animations run off the main thread and beat JS under load; rAF-based animations stutter while the browser loads, scripts or paints. [CSS animations beat JS under load]
- **should** (motion, web): Use WAAPI (element.animate) when you need JS control with CSS performance. Why: WAAPI is hardware-accelerated, interruptible and needs no library. Values: duration: 1000, fill: 'forwards', easing: 'cubic-bezier(0.77, 0, 0.175, 1)'. [WAAPI]
- **should** (motion, css): Move elements by their own size with translate percentages such as translateY(100%) rather than hardcoded pixels. Why: Percentages are relative to the element's own size regardless of dimensions; Sonner and Vaul position toasts and drawers this way. Values: translateY(100%). [Transforms & clip-path]
- **consider** (motion, all): Use scale() for press feedback so children (font, icons, content) scale with the element. Why: scale() scaling children is a feature for press feedback. Values: scale(). [Transforms & clip-path]
- **consider** (motion, css): Use rotateX/Y with transform-style: preserve-3d for depth, orbit or flip effects without JS. Why: 3D transforms give depth, orbit and flip without JS. Values: rotateX/Y, transform-style: preserve-3d. [Transforms & clip-path: 3D]
- **consider** (motion, css): Reveal content on scroll by animating clip-path from inset(0 0 100% 0) to inset(0 0 0 0). Why: clip-path: inset(t r b l) eats in from each side and is a powerful animation tool. Values: inset(0 0 100% 0), inset(0 0 0 0). [clip-path: inset(t r b l)]
- **consider** (motion, css): Build hold-to-delete overlays with an animated clip-path. Why: Listed use of clip-path: inset(). Values: clip-path. [clip-path: inset(t r b l)]
- **consider** (motion, css): Make tab color transitions seamless by duplicating the tabs and clipping the active copy. Why: Listed use of clip-path: inset(). Values: clip-path. [clip-path: inset(t r b l)]
- **consider** (motion, css): Build comparison sliders with clip-path. Why: Listed use of clip-path: inset(). Values: clip-path. [clip-path: inset(t r b l)]
- **must** (patterns, all): Dismiss swipeable elements by velocity: compute Math.abs(distance)/elapsedMs and dismiss if it exceeds about 0.11. Why: A flick should be enough. Values: Math.abs(distance)/elapsedMs, > ~0.11. [Gestures & drag: Momentum dismissal]
- **must** (patterns, all): Do not require crossing a distance threshold to dismiss a swipe. Why: A flick should be enough. [Gestures & drag: Momentum dismissal]
- **should** (patterns, all): Damp drags past a natural edge so the element moves less the further you drag. Why: Real things slow before stopping. [Damping at boundaries]
- **must** (patterns, web): Capture the pointer once dragging starts. Why: The drag continues when the pointer leaves the element's bounds. [Pointer capture]
- **must** (patterns, all): Ignore extra touch points after a drag begins (if (isDragging) return). Why: Prevents jumps. Values: if (isDragging) return. [Multi-touch protection]
- **should** (patterns, all): Allow over-drag with rising resistance instead of an invisible hard stop. Why: Friction over hard stops. [Friction over hard stops]
- **should** (motion, css): When a crossfade still shows two overlapping states after tuning easing and duration, add filter: blur(2px) during the transition. Why: It blends them into one perceived transformation. Values: filter: blur(2px). [Masking imperfect crossfades]
- **must** (motion, web): Keep animated blur under 20px. Why: Heavy blur is expensive, especially in Safari. Values: < 20px. [Masking imperfect crossfades]
- **must** (motion, all): Stagger group entrances with 30–80ms between items. Why: Stated as the stagger rule; longer delays feel slow. Values: 30–80ms, 50ms, 100ms, translateY(8px), 300ms ease-out. [Stagger]
- **should** (motion, all): Do not use stagger delays longer than 30–80ms between items. Why: Longer delays feel slow. Values: 30–80ms. [Stagger]
- **must** (motion, all): Never block interaction while a stagger plays. Why: Stagger is decorative. [Stagger]
- **must** (accessibility, css): Under prefers-reduced-motion: reduce, keep opacity and color animation and drop transform-based motion. Why: Reduced motion keeps comprehension aids and removes movement. Values: @media (prefers-reduced-motion: reduce), animation: fade 0.2s ease. [Accessibility]
- **must** (accessibility, css): Gate hover motion behind @media (hover: hover) and (pointer: fine). Why: Touch fires false hovers on tap. Values: @media (hover: hover) and (pointer: fine), transform: scale(1.05). [Accessibility]
- **should** (accessibility, react): In React, read useReducedMotion and remove positional movement when it is on, for example closedX = reduce ? 0 : '-100%'. Why: Reduced motion removes movement and position changes. Values: useReducedMotion(), closedX = reduce ? 0 : '-100%'. [Accessibility: useReducedMotion]
- **must** (accessibility, all): Do not remove all animation for reduced motion; keep transitions that aid comprehension and remove movement and position changes. Why: Reduced motion means fewer and gentler animations, not zero. [Reduced motion means fewer and gentler animations, not zero]
- **should** (process, web): Check motion feel in slow motion by raising duration 2–5× or using the DevTools animation inspector, verifying clean color crossfades, no abrupt easing stop, the right transform-origin, and coordinated properties staying in sync. Why: Recommended in reviews when feel is uncertain. Values: 2–5×. [Debugging: Slow motion]
- **should** (process, web): Step through animations frame by frame in the Chrome DevTools Animations panel to find timing drift between coordinated properties. Why: Frame-by-frame reveals timing drift. [Debugging: Frame-by-frame]
- **should** (process, all): Test gestures such as drawers and swipes on real devices by connecting a phone, hitting the dev server by IP and using Safari remote devtools. Why: Gestures need real devices to judge. [Debugging: Real devices]
- **should** (process, all): Review motion again with fresh eyes the next day. Why: Imperfections invisible during development surface later. [imperfections invisible during development surface later]
- **must** (motion, all): Match motion to the component's personality: playful can be bouncier, a professional dashboard should be crisp and fast. Why: Cohesion between motion and personality makes a component feel right. [Cohesion]
- **consider** (motion, all): For a component meant to feel elegant, consider slightly slower timing and ease rather than ease-out, as Sonner does. Why: Sonner's easing, duration, design and name are in harmony. Values: ease. [Cohesion: Sonner]
- **consider** (motion, all): Tune opacity plus height for entering and exiting list items by trial and error until it feels right. Why: There is no formula for it. [Cohesion: Opacity + height in entering/exiting lists]

### Decisions it informs

- Should this action animate at all, given how often people do it?
  - No animation: Instant every time; nothing feels slow or disconnected. When: 100+ times a day, such as keyboard shortcuts and the command palette toggle.
  - Remove or drastically reduce: Barely any motion. When: Tens of times a day, such as hover effects and list navigation.
  - Standard animation: Normal entrance and exit within the duration table. When: Occasional UI such as modals, drawers and toasts.
  - Delight: Expressive motion. When: Rare or first-time moments such as onboarding, feedback and celebrations.
  - Recommendation: Use the frequency table; never animate keyboard-initiated actions (Raycast has no open/close animation).
- Which easing should this motion use? (`Q-motion-03`)
  - ease-out (cubic-bezier(0.23, 1, 0.32, 1)): Starts fast and feels responsive. When: Entering or exiting; also the default.
  - ease-in-out (cubic-bezier(0.77, 0, 0.175, 1)): Strong ease-in-out for on-screen movement. When: Moving or morphing on screen.
  - ease: The built-in ease curve. When: Hover and color changes.
  - linear: Even motion for constant movement. When: Marquees and progress.
  - drawer curve (cubic-bezier(0.32, 0.72, 0, 1)): iOS-like drawer motion. When: Drawers.
  - Recommendation: Choose by job, default to a strong ease-out, and never use ease-in on UI.
- How long should each kind of element animate?
  - 100–160ms: Snappy press feedback. When: Button press feedback.
  - 125–200ms: Quick appear and disappear. When: Tooltips and small popovers.
  - 150–250ms: Responsive menus: a 180ms dropdown feels more responsive than a 400ms one. When: Dropdowns and selects.
  - 200–500ms: The longest UI band in the table. When: Modals and drawers.
  - Longer: Can run longer than UI motion. When: Marketing or explanatory animation.
  - Recommendation: UI animations stay under 300ms; a 180ms dropdown feels more responsive than a 400ms one.
- How should springs be configured? (`Q-motion-04`)
  - Apple-style: duration + bounce: { type: "spring", duration: 0.5, bounce: 0.2 }; easier to reason about. When: Default, recommended.
  - Traditional physics: mass, stiffness, damping: { type: "spring", mass: 1, stiffness: 100, damping: 10 }; more control. When: When you need finer control.
  - Recommendation: Apple-style is recommended; keep bounce at 0.1–0.3 and avoid bounce in most UI.
- Should rapidly triggered UI use CSS transitions or keyframes?
  - CSS transitions (with @starting-style for entry): Interrupted and retargeted mid-animation. When: Toasts being added, toggles, anything triggered rapidly.
  - @keyframes: Restart from zero when triggered again. When: Avoid for dynamic UI.
  - Recommendation: Transitions for anything triggered rapidly; @starting-style gives entry without JS.
- Should this animation run in CSS, WAAPI or JS?
  - CSS: Runs off the main thread; smooth under load. When: Predetermined motion.
  - WAAPI: JS control with CSS performance, interruptible, no library. When: Programmatic motion that still needs to be smooth.
  - JS / springs: rAF-based; can stutter while the browser is busy. When: Dynamic or interruptible motion.
  - Recommendation: CSS for predetermined motion, JS for dynamic and interruptible motion, WAAPI when JS control is needed with CSS performance.
- Where should a scaling surface grow from?
  - Trigger origin: transform-origin: var(--transform-origin); the popover grows out of its trigger. When: Popovers.
  - Center: transform-origin: center; the surface grows in place. When: Modals, which appear centered in the viewport.
  - Recommendation: Popovers scale from the trigger; modals are exempt and stay centered.
- How should a swipe-to-dismiss decide to dismiss?
  - Velocity: A quick flick dismisses. When: Recommended: dismiss when Math.abs(distance)/elapsedMs exceeds about 0.11.
  - Distance threshold: The user must drag past a set point. When: Not recommended.
  - Recommendation: Use velocity; a flick should be enough.
- What happens when a drag reaches a boundary?
  - Friction: Over-drag is allowed with rising resistance. When: Recommended.
  - Hard stop: An invisible wall. When: Not recommended.
  - Recommendation: Friction over hard stops, damping more the further past the edge.
- When reduced motion is on, should animations become gentler or stop entirely? (`Q-motion-07`)
  - Fewer and gentler: Opacity and color remain; movement and position changes go. When: Recommended.
  - Zero animation: Everything stops, including transitions that aid comprehension. When: Rejected: reduced motion does not mean zero.
  - Recommendation: Fewer and gentler animations, not zero.
- Should group items appear one by one? (`Q-motion-06`)
  - Stagger 30–80ms: Items cascade in quickly. When: Group entrances.
  - Longer stagger: Feels slow. When: Not recommended.
  - Recommendation: Stagger by 30–80ms and never block interaction while it plays.
- What personality should a component's motion have? (`Q-motion-01`)
  - Bouncier: Playful, springy. When: Playful components.
  - Crisp and fast: Professional, efficient. When: Professional dashboards.
  - Slightly slower with ease: Elegant. When: Components meant to feel elegant, as Sonner does.
  - Recommendation: Match motion to the component's personality so easing, duration, design and name are in harmony.
- How should a crossfade that shows two overlapping states be fixed?
  - Add a subtle blur: filter: blur(2px) blends the states into one perceived transformation. When: After tuning easing and duration has not fixed it.
  - Plain crossfade: Both states visibly overlap. When: Only if it already looks like one change [inferred].
  - Recommendation: Add blur(2px), keeping blur under 20px because heavy blur is expensive, especially in Safari.

### Process

1. Decide whether it animates: Place the action in the frequency table (100+/day, tens/day, occasional, rare) and confirm a valid purpose.
2. Pick the easing: Entering or exiting: ease-out; moving or morphing on screen: ease-in-out; hover or color: ease; constant motion: linear; default: ease-out. Use the strong custom curves.
3. Pick the duration: Use the per-element table and keep UI under 300ms.
4. Check physicality: No scale(0); trigger-origin popovers; centered modals; subtle press feedback.
5. Implement interruptibly and on the GPU: Transitions or springs for rapid and gesture UI; only transform and opacity; full transform strings; CSS or WAAPI for predetermined motion.
6. Compute swipe dismissal: Measure Math.abs(distance)/elapsedMs and dismiss when it exceeds about 0.11; capture the pointer; ignore extra touches; damp past edges.
7. Add accessibility: Reduced-motion media query or useReducedMotion that keeps opacity and color and drops movement; gate hover motion to (hover: hover) and (pointer: fine).
8. Debug in slow motion: Raise durations 2–5× or use the DevTools animation inspector; check color crossfades, easing endings, transform-origin and property sync.
9. Step frame by frame: Use the Chrome DevTools Animations panel to find timing drift between coordinated properties.
10. Test on a real device: For drawers and swipes, connect a phone, open the dev server by IP and use Safari remote devtools.
11. Look again tomorrow: Review with fresh eyes the next day to catch imperfections invisible during development.

### Examples and visual references

- Command palette with no open/close animation (Raycast): Cited as correct for something used hundreds of times a day.
- Easing tokens as CSS custom properties: --ease-out: cubic-bezier(0.23, 1, 0.32, 1); --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1); --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1) (Ionic).
- Origin-aware popover (Base UI): .popover { transform-origin: var(--transform-origin); } so the popover grows from its trigger.
- 'Alive' element driven by springs (Dynamic Island): Named as the kind of element springs suit.
- Interruptible toast versus non-interruptible keyframes: .toast { transition: transform 400ms ease; } versus @keyframes slideIn from translateY(100%) to translateY(0).
- Toast entry with @starting-style: The toast transitions opacity and transform over 400ms ease, starting from opacity: 0 and translateY(100%) inside @starting-style, with no JS.
- Hold-to-confirm overlay with asymmetric timing: .button:active .overlay uses clip-path 2s linear while pressing; .overlay returns with clip-path 200ms ease-out on release.
- CSS variable versus direct transform: element.style.setProperty('--swipe-amount', ...) recalcs all children; element.style.transform = translateY(...) touches only that element.
- Framer Motion shorthand versus transform string (Framer Motion): <motion.div animate={{ x: 100 }} /> drops frames under load; animate={{ transform: "translateX(100px)" }} is hardware accelerated.
- WAAPI clip-path reveal: element.animate from clipPath inset(0 0 100% 0) to inset(0 0 0 0), duration 1000, fill forwards, easing cubic-bezier(0.77, 0, 0.175, 1).
- Percentage translates for toasts and drawers (Sonner, Vaul): translateY(100%) moves by the element's own height regardless of dimensions.
- Staggered list entrance: Items start at opacity 0 and translateY(8px), fade in over 300ms ease-out, with animation-delay 50ms and 100ms for the second and third child.
- Reduced-motion and hover-gating media queries: Reduced motion swaps to animation: fade 0.2s ease; hover scale(1.05) only inside @media (hover: hover) and (pointer: fine).
- useReducedMotion closed position: const closedX = reduce ? 0 : '-100%' removes the slide when reduced motion is on.
- Motion cohesion (Sonner): Slightly slower timing and ease rather than ease-out make it feel elegant; easing, duration, design and name are in harmony.

### Numbers

- 100+ times/day: Frequency at which an action gets no animation. [Should it animate? (frequency table)]
- Tens of times/day: Frequency (hover effects, list navigation) at which animation is removed or drastically reduced. [Should it animate? (frequency table)]
- cubic-bezier(0.23, 1, 0.32, 1): Strong ease-out for UI. [Easing]
- cubic-bezier(0.77, 0, 0.175, 1): Strong ease-in-out for on-screen movement; also used in the WAAPI example. [Easing; WAAPI]
- cubic-bezier(0.32, 0.72, 0, 1): iOS-like drawer curve (Ionic). [Easing]
- 200ms: ease-out at 200ms feels faster than ease-in at 200ms. [Never `ease-in` on UI]
- 100–160ms: Button press feedback duration. [Duration table]
- 125–200ms: Tooltips and small popovers duration. [Duration table]
- 150–250ms: Dropdowns and selects duration. [Duration table]
- 200–500ms: Modals and drawers duration. [Duration table]
- 300ms: Ceiling for UI animation duration. [Rule: UI animations stay under 300ms]
- 180ms: A 180ms dropdown feels more responsive than a 400ms one. [Duration]
- scale(0.9–0.97): Entrance starting scale, with opacity: 0. [Physicality]
- scale(0.97): Press feedback on :active. [Button press feedback]
- 160ms ease-out: Transition for press feedback. [Button press feedback]
- 0.95–0.98: Subtle range for press-feedback scale. [Button press feedback]
- duration: 0.5, bounce: 0.2: Recommended Apple-style spring. [Springs]
- mass: 1, stiffness: 100, damping: 10: Traditional physics spring. [Springs]
- 0.1–0.3: Subtle spring bounce range. [Springs]
- 400ms: Transition duration in the interruptible toast and @starting-style examples; also the slower dropdown in the 180ms comparison. [Interruptibility; Duration]
- 2s linear: Press (slow, deliberate) timing for the overlay clip-path. [Asymmetric timing]
- 200ms ease-out: Release (fast) timing for the overlay clip-path. [Asymmetric timing]
- 1000: WAAPI example duration (ms) for a clip-path reveal. [WAAPI]
- translateY(100%): Moves an element by its own height; how Sonner and Vaul position toasts and drawers, and the toast entry start state. [Transforms & clip-path]
- inset(0 0 100% 0): clip-path start state for a reveal-on-scroll, animated to inset(0 0 0 0). [Transforms & clip-path]
- ~0.11: Velocity (Math.abs(distance)/elapsedMs) above which a swipe dismisses. [Momentum dismissal]
- blur(2px): Blur added to mask an imperfect crossfade. [Masking imperfect crossfades]
- < 20px: Maximum blur because heavy blur is expensive, especially in Safari. [Masking imperfect crossfades]
- 30–80ms: Delay between staggered items. [Stagger]
- translateY(8px): Starting offset for items in the stagger example. [Stagger code]
- 300ms ease-out: Per-item fade-in in the stagger example. [Stagger code]
- 50ms: animation-delay for the second item in the stagger example. [Stagger code]
- 100ms: animation-delay for the third item in the stagger example. [Stagger code]
- 0.2s: Fade duration in the reduced-motion example. [Accessibility]
- scale(1.05): Hover scale inside the hover-gating media query. [Accessibility]
- 2–5×: How much to slow durations when debugging feel. [Debugging: Slow motion]

<!-- /od:learn -->
