---
type: source
title: "emilkowalski/skills: skills/improve-animations/AUDIT.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-improve-animations-audit
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/improve-animations/AUDIT.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - motion
  - animation-audit
  - easing
  - duration
  - springs
  - interruptibility
  - performance
  - reduced-motion
  - motion-tokens
  - press-feedback
  - transform-origin
  - stagger
---

# emilkowalski/skills: skills/improve-animations/AUDIT.md

## Metadata

- Video ID: `eks-skills-improve-animations-audit`
- Channel: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/improve-animations/AUDIT.md

## Summary

Emil Kowalski's animation audit playbook: eight categories (purpose and frequency, easing and duration, physicality and origin, interruptibility, performance, accessibility, cohesion and tokens, missed opportunities), each with what to look for and the exact target values to cite. It decides whether something should animate at all from how often people see it, then fixes the curve, the duration budget, the starting scale and origin, how motion behaves when interrupted, which properties are safe to animate, and how reduced motion and touch hover are handled. For a design system it supplies ready motion tokens (three custom cubic-bezier curves, a duration table per element type, one spring config, a stagger range) and a checklist that can be run against any codebase. The file tells readers never to approximate its values and to copy them exactly.

## Key Ideas

- Every animation needs a purpose; looking cool is not one on an element seen often.
- How often an element is seen decides whether it animates: 100+ times a day means no animation at all.
- Pick the easing by what the motion does: ease-out to enter or exit, ease-in-out to move on screen, ease for hover and color, linear for constant motion.
- ease-in on UI is always wrong because it delays the moment the user is watching.
- Built-in CSS easings are too weak; ship strong custom curves as tokens.
- UI animations stay under 300ms, with a set duration band per element type.
- Nothing appears from nothing: start from scale 0.9-0.97 with opacity 0, never scale(0).
- Anchored UI (popovers, dropdowns, tooltips) grows from its trigger; modals stay centered.
- Rapid or reversible motion must use transitions or springs, because keyframes restart from zero.
- Gestures use springs so velocity carries through an interruption; drags dismiss on speed, not just distance.
- Animate only transform and opacity; transition: all and layout properties are findings.
- Reduced motion means fewer and gentler animations, not zero; drop movement, keep opacity and color.
- Curves and durations live as shared tokens, and motion personality stays consistent across components.
- Group entrances get a 30-80ms stagger that never blocks interaction.
- Some UI should animate but does not: teleporting state changes, unexplained panels, rare high-emotion moments.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer whose animation philosophy the playbook is distilled from.
- [[entities/raycast|Raycast]] (product): Cited as correct for having no open/close animation on its command palette.
- [[entities/base-ui|Base UI]] (library): Component library whose --transform-origin variable is used to scale popovers from their trigger.
- [[entities/framer-motion|Framer Motion]] (library): Motion library whose x/y/scale shorthand props the playbook says are not hardware-accelerated.
- [[entities/waapi|WAAPI]] (tool): Grouped with CSS as beating rAF-based JS under load.
- [[entities/starting-style|@starting-style]] (concept): CSS rule for entry animations without JS; a data-mounted attribute set in useEffect is the legacy fallback.
- [[entities/prefers-reduced-motion|prefers-reduced-motion]] (concept): Media query used to keep opacity/color feedback while dropping movement.
- [[entities/usereducedmotion|useReducedMotion]] (tool): Called in JS to branch transform values for reduced motion.
- [[entities/safari|Safari]] (product): Browser where heavy filter: blur() during transitions is called especially expensive.
- [[entities/spring-animation|Spring animation]] (concept): Motion model recommended for gesture-driven UI because it carries velocity when interrupted.

## Topics

- [[topics/motion-principles|Motion principles]]: Every animation needs a purpose (spatial consistency, state indication, feedback, explanation, preventing a jarring change), and frequency of use decides whether to animate; deleting the animation is often the strongest fix.
- [[topics/easing-and-timing|Easing and timing]]: Easing chosen by motion type, ease-in banned on UI, three strong custom cubic-bezier tokens, a sub-300ms UI budget and per-element duration bands, asymmetric timing for deliberate phases.
- [[topics/spring-animation|Spring animation]]: Springs for gesture-driven motion because they carry velocity; Apple-style config { type: "spring", duration: 0.5, bounce: 0.2 } with bounce kept at 0.1-0.3.
- [[topics/animation-performance|Animation performance]]: Animate transform and opacity only, never transition: all, use full transform strings instead of Framer Motion shorthands, avoid parent CSS variables for child transforms, keep blur under 20px, prefer CSS/WAAPI for predetermined motion.
- [[topics/gestures-and-drag|Gestures and drag]]: Velocity-based dismissal (Math.abs(distance)/elapsedMs > ~0.11) and rising friction at drag boundaries instead of hard stops.
- [[topics/micro-interactions|Micro-interactions]]: Press feedback is scale(0.97) on :active with a 160ms ease-out transform transition, kept between 0.95 and 0.98; hover motion gated to fine pointers.
- [[topics/reduced-motion|Reduced motion]]: Reduced motion means fewer and gentler animations, not zero: keep opacity and color transitions that aid comprehension, remove position changes, branch in JS with useReducedMotion().
- [[topics/accessibility|Accessibility]]: Motion without prefers-reduced-motion handling and ungated :hover motion (touch fires false hovers) are findings.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Curves and durations should be shared tokens; several near-identical hand-typed cubic-beziers is a consolidation finding; motion personality must match the product.
- [[topics/modals-and-popovers|Modals and popovers]]: Popovers, dropdowns and tooltips scale from their trigger via transform-origin; modals are exempt and stay centered; tooltip durations 125-200ms and only the first tooltip in a toolbar gets delay plus animation.
- [[topics/toasts-and-notifications|Toasts and notifications]]: Stacking toasts are rapidly triggered UI and must use transitions or springs, not @keyframes.
- [[topics/drawers-and-sheets|Drawers and sheets]]: An iOS-like drawer curve cubic-bezier(0.32, 0.72, 0, 1) and a 200-500ms duration band for modals and drawers.
- [[topics/buttons-and-actions|Buttons and actions]]: Button press feedback runs 100-160ms; pressable elements with no press feedback are a finding.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Concrete CSS and React patterns: @starting-style, data-mounted fallback, transform-origin variable, media queries for reduced motion and hover, translate percentages and clip-path: inset() reveals.

## Notable Claims

- ease-in starts slow, delaying the exact moment the user is watching. Evidence: 2. Easing & duration: ease-in on UI is always a finding
- ease-out starts fast and feels responsive. Evidence: 2. Easing & duration: Entering or exiting
- Built-in CSS easings are too weak for deliberate motion. Evidence: 2. Easing & duration
- Nothing in the real world appears from nothing, which is why the playbook rules out scale(0). Evidence: 3. Physicality & origin: Never scale(0)
- CSS transitions retarget from the current state mid-animation, while keyframes restart from zero. Evidence: 4. Interruptibility
- Springs carry velocity when interrupted, which suits gesture-driven motion. Evidence: 4. Interruptibility: Gesture-driven motion should use springs
- Animating width, height, margin, padding, top or left triggers layout, paint and composite. Evidence: 5. Performance: Animate transform and opacity only
- transition: all animates unintended properties off the GPU. Evidence: 5. Performance: transition: all
- Framer Motion's x/y/scale shorthands are not hardware-accelerated; they run on the main thread and drop frames under load. Evidence: 5. Performance: Framer Motion x/y/scale shorthands
- Driving child transforms through a CSS variable on the parent recalculates styles for all children. Evidence: 5. Performance: Don't drive child transforms via a CSS variable
- CSS and WAAPI animations beat rAF-based JS under load. Evidence: 5. Performance: CSS (and WAAPI) beat rAF-based JS under load
- Heavy filter: blur() is expensive, especially in Safari. Evidence: 5. Performance: Keep transition-time filter: blur() under 20px
- Touch devices fire false hovers on tap. Evidence: 6. Accessibility: @media (hover: hover) and (pointer: fine)
- Raycast's command palette has no open/close transition, which is correct. Evidence: 1. Purpose & frequency: Raycast has none — correct
- A jarring crossfade showing two overlapping states can be masked with subtle filter: blur(2px) during the transition. Evidence: 7. Cohesion & tokens
- translateY(100%) moves an element by its own height. Evidence: 8. Missed opportunities: translate percentages

## Quotes

> Never approximate a value that appears here — copy it.
> "It looks cool" on a frequently-seen element is not a purpose.
> Stagger is decorative — it must never block interaction.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is an AI-agent skill file pinned to commit 85e8e23 of emilkowalski/skills; values can change in later commits.
- Caveat: The playbook says UI animations stay under 300ms but lists modals and drawers at 200–500ms; the 300ms ceiling does not appear to cover modals and drawers [inferred].
- Caveat: The --transform-origin variable is named as Base UI's; other component libraries may expose a different variable name [inferred].
- Caveat: The Framer Motion shorthand and rAF performance claims are stated without a benchmark or library version.
- Caveat: The ~0.11 velocity threshold is written as approximate and has no stated unit; px per ms is implied by distance/elapsedMs [inferred].
- Caveat: Raycast is used as a single example of correct behavior, not a general survey.

### Rules and practices

- **must** (motion, all): Give every animation a stated purpose: spatial consistency, state indication, feedback, explanation, or preventing a jarring change. Why: Every animation must answer "why does this animate?" with one of these purposes. [1. Purpose & frequency]
- **must** (motion, all): Do not accept 'it looks cool' as the purpose for an animation on a frequently seen element. Why: Looking cool on a frequently-seen element is not a purpose. ["It looks cool" on a frequently-seen element is not a purpose]
- **must** (motion, all): Do not animate anything used 100+ times a day, such as keyboard shortcuts and the command palette toggle. Why: At that frequency the decision is no animation, ever. Values: 100+ times/day. [Frequency table: No animation. Ever.]
- **must** (motion, all): Remove or drastically reduce animation on elements used tens of times a day, such as hover effects and list navigation. Why: Frequency table decision for tens of times per day. Values: Tens of times/day. [Frequency table: Remove or drastically reduce]
- **should** (motion, all): Use standard animation for occasional UI such as modals, drawers and toasts. Why: Frequency table decision for occasional elements. [Frequency table: Occasional (modals, drawers, toasts)]
- **consider** (motion, all): Reserve delight animation for rare or first-time moments such as onboarding, feedback and celebrations. Why: Rare moments are the only frequency band that can add delight. [Frequency table: Rare / first-time]
- **must** (motion, all): Do not give keyboard-initiated actions or command palettes an open/close transition. Why: Raycast has none, which the playbook calls correct; these are hunted as findings. [Hunt for: animations on keyboard-initiated actions, command palettes]
- **must** (motion, all): Do not put decorative motion on list items or hover states that are hit constantly; consider deleting the animation first. Why: Hunted as a finding; the strongest fix is often to delete the animation. [Hunt for: decorative motion on list items or hover states]
- **must** (motion, all): Use ease-out for elements entering or exiting. Why: It starts fast and feels responsive. Values: ease-out. [Decision order for easing: Entering or exiting]
- **must** (motion, all): Use ease-in-out for elements moving or morphing on screen. Why: Easing decision order for on-screen movement. Values: ease-in-out. [Moving / morphing on screen]
- **must** (motion, all): Use ease for hover and color changes. Why: Easing decision order for hover/color. Values: ease. [Hover / color change]
- **must** (motion, all): Use linear only for constant motion such as marquees and progress. Why: Easing decision order for constant motion. Values: linear. [Constant motion (marquee, progress)]
- **must** (motion, all): Default to ease-out when no other easing case applies. Why: The easing decision order ends with ease-out as default. Values: ease-out. [Default → ease-out]
- **must** (motion, all): Never use ease-in on UI animation. Why: It starts slow, delaying the exact moment the user is watching; it is always a finding. Values: ease-in. [ease-in on UI is always a finding]
- **must** (motion, all): Do not use bare ease or linear on entrances. Why: Hunted as a finding under easing and duration. Values: ease, linear. [Hunt for: bare ease/linear on entrances]
- **should** (tokens, css): For deliberate motion, introduce strong custom curves as tokens that match the repo's conventions instead of relying on built-in CSS easings. Why: Built-in CSS easings are too weak for deliberate motion. Values: --ease-out, --ease-in-out, --ease-drawer. [plans should introduce strong custom curves (as tokens, matching repo conventions)]
- **must** (tokens, css): Define the strong UI ease-out token as --ease-out: cubic-bezier(0.23, 1, 0.32, 1). Why: Strong ease-out for UI. Values: --ease-out: cubic-bezier(0.23, 1, 0.32, 1). [/* strong ease-out for UI */]
- **must** (tokens, css): Define the on-screen movement token as --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1). Why: Strong ease-in-out for on-screen movement. Values: --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1). [/* strong ease-in-out for on-screen movement */]
- **must** (tokens, css): Define the drawer token as --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1). Why: iOS-like drawer curve. Values: --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1). [/* iOS-like drawer curve */]
- **must** (motion, all): Keep UI animations under 300ms; durations over 300ms on UI elements are findings. Why: Duration budget for UI animation. Values: 300ms. [UI animations stay under 300ms]
- **must** (motion, all): Set button press feedback duration to 100-160ms. Why: Duration budget table. Values: 100–160ms. [Button press feedback | 100–160ms]
- **must** (motion, all): Set tooltip and small popover durations to 125-200ms. Why: Duration budget table. Values: 125–200ms. [Tooltips, small popovers | 125–200ms]
- **must** (motion, all): Set dropdown and select durations to 150-250ms. Why: Duration budget table. Values: 150–250ms. [Dropdowns, selects | 150–250ms]
- **must** (motion, all): Set modal and drawer durations to 200-500ms. Why: Duration budget table. Values: 200–500ms. [Modals, drawers | 200–500ms]
- **consider** (motion, all): Allow marketing and explanatory animations to run longer than the UI budget. Why: Duration budget table: marketing / explanatory can be longer. [Marketing / explanatory | Can be longer]
- **must** (components, all): In a toolbar, give only the first tooltip its delay and animation; show subsequent tooltips instantly. Why: Delay plus animation on every tooltip in a toolbar is hunted as a finding. [tooltip delay + animation on every tooltip in a toolbar (after the first, they should be instant)]
- **must** (process, all): Copy target values from the playbook exactly; never approximate them. Why: The playbook lists exact target values to cite in findings and plans. [Never approximate a value that appears here — copy it.]
- **must** (motion, all): Never animate from scale(0); start entrances from scale(0.9-0.97) combined with opacity: 0. Why: Nothing in the real world appears from nothing. Values: scale(0), scale(0.9–0.97), opacity: 0. [3. Physicality & origin: Never scale(0)]
- **must** (motion, all): Do not use pure-fade entrances with no initial transform. Why: Hunted as a finding under physicality and origin. [Hunt for: pure-fade entrances with no initial transform]
- **must** (motion, css): Scale popovers, dropdowns and tooltips from their trigger, not from center, using transform-origin: var(--transform-origin). Why: transform-origin: center (or none) on trigger-anchored elements is hunted as a finding. Values: transform-origin: var(--transform-origin). [Popovers/dropdowns/tooltips scale from their trigger]
- **must** (motion, all): Keep modals centered with transform-origin: center and do not report it as a finding. Why: Modals are exempt because they appear centered. Values: transform-origin: center. [Modals are exempt]
- **must** (motion, css): Give pressable elements press feedback: transform: scale(0.97) on :active with transition: transform 160ms ease-out. Why: Pressable elements with no press feedback are a finding. Values: transform: scale(0.97), :active, transition: transform 160ms ease-out. [`transform: scale(0.97)` on `:active` with `transition: transform 160ms ease-out`]
- **must** (motion, all): Keep press-feedback scale subtle, between 0.95 and 0.98. Why: Press feedback should stay subtle. Values: 0.95–0.98. [Keep it subtle (0.95–0.98)]
- **must** (motion, all): Use CSS transitions or springs, not keyframes, for anything triggered rapidly or reversible mid-motion (stacking toasts, toggles, drags, expand/collapse). Why: Transitions retarget from the current state mid-animation; keyframes restart from zero. [4. Interruptibility]
- **must** (motion, css): Do not use @keyframes on toasts, toggles or other rapidly triggered UI. Why: Keyframes restart from zero when retriggered. Values: @keyframes. [Hunt for: @keyframes on toasts/toggles/rapidly-triggered UI]
- **should** (motion, css): Animate entry without JS using @starting-style; use a data-mounted attribute set in useEffect as the legacy fallback. Why: Listed as the entry technique under interruptibility. Values: @starting-style, data-mounted, useEffect. [Entry without JS: @starting-style]
- **must** (motion, all): Drive gesture-driven motion with springs, not fixed-duration keyframe tweens. Why: Springs carry velocity when interrupted; gesture handlers that tween with fixed-duration keyframes are hunted as a finding. [Gesture-driven motion should use springs]
- **should** (motion, react): Use the Apple-style spring config { type: "spring", duration: 0.5, bounce: 0.2 } as the recommended default. Why: Recommended spring config. Values: { type: "spring", duration: 0.5, bounce: 0.2 }. [Spring configs, Apple-style (recommended)]
- **must** (motion, all): Keep spring bounce subtle at 0.1-0.3, and reserve visible bounce for drag-to-dismiss and playful moments. Why: Bounce should stay subtle outside those cases. Values: 0.1–0.3. [Keep bounce subtle (0.1–0.3)]
- **must** (motion, all): Use asymmetric timing: animate deliberate phases (press, hold, destructive confirm) slower and make the system's response snap. Why: Symmetric timing on press-and-release is a finding. [Asymmetric timing]
- **must** (motion, all): Dismiss drags by velocity (Math.abs(distance)/elapsedMs > ~0.11), not by distance thresholds alone. Why: Drags without velocity-based dismissal are a finding. Values: Math.abs(distance)/elapsedMs > ~0.11. [drags without velocity-based dismissal]
- **must** (motion, all): Apply rising friction at drag boundaries instead of hard stops. Why: Hard stops at drag boundaries are a finding. [hard stops at drag boundaries instead of rising friction]
- **must** (motion, all): Animate only transform and opacity; never animate width, height, margin, padding, top or left. Why: Layout properties trigger layout, paint and composite. Values: transform, opacity, width, height, margin, padding, top, left. [Animate transform and opacity only]
- **must** (motion, css): Never use transition: all; list the exact properties to transition. Why: It animates unintended properties off-GPU and is always a finding. Values: transition: all. [transition: all animates unintended properties off-GPU]
- **must** (motion, react): In Framer Motion, animate the full transform string (animate={{ transform: "translateX(100px)" }}) instead of the x/y/scale shorthands. Why: The shorthands are not hardware-accelerated; they run on the main thread and drop frames under load. Values: x, y, scale, animate={{ transform: "translateX(100px)" }}. [Framer Motion x/y/scale shorthands are not hardware-accelerated]
- **must** (motion, web): Set transform directly on each animated element; do not drive child transforms through a CSS variable on the parent (e.g. setProperty('--x', ...)). Why: A parent CSS variable recalculates styles for all children. Values: setProperty('--x', …). [Don't drive child transforms via a CSS variable on the parent]
- **must** (motion, web): Use CSS or WAAPI for predetermined motion and JS/springs for dynamic and gesture-driven motion; do not run rAF loops for what CSS could do. Why: CSS and WAAPI beat rAF-based JS under load. [CSS (and WAAPI) beat rAF-based JS under load]
- **must** (motion, web): Keep transition-time filter: blur() under 20px. Why: Heavy blur is expensive, especially in Safari. Values: filter: blur(), 20px. [Keep transition-time filter: blur() under 20px]
- **must** (accessibility, css): Handle prefers-reduced-motion for every moving animation: keep opacity and color, drop movement (e.g. animation: fade 0.2s ease). Why: Movement with no prefers-reduced-motion handling is a finding. Values: @media (prefers-reduced-motion: reduce), animation: fade 0.2s ease. [6. Accessibility]
- **must** (accessibility, all): Do not remove all feedback under reduced motion; keep transitions that aid comprehension and remove position changes. Why: Reduced motion means fewer and gentler animations, not zero. [Reduced motion means fewer and gentler animations, not zero]
- **must** (accessibility, react): In JS, read useReducedMotion() and branch transform values on it. Why: The playbook's JS route for reduced motion: branch transform values. Values: useReducedMotion(). [In JS: `useReducedMotion()` and branch transform values]
- **must** (accessibility, css): Gate hover motion behind @media (hover: hover) and (pointer: fine). Why: Touch fires false hovers on tap; ungated :hover motion is a finding. Values: @media (hover: hover) and (pointer: fine), transform: scale(1.05). [touch fires false hovers on tap]
- **must** (motion, all): Match motion to the product's personality (playful can be bouncier, a dashboard stays crisp) and keep it consistent across components. Why: Mismatched personality across components, such as one bouncy component in a crisp app, is a finding. [7. Cohesion & tokens]
- **must** (tokens, all): Keep curves and durations as shared tokens and consolidate near-identical hand-typed cubic-beziers or durations. Why: Five hand-typed cubic-beziers that almost match is a consolidation finding. [Curves and durations should live as shared tokens]
- **should** (motion, all): Stagger group entrances (lists, grids) by 30-80ms instead of animating everything at once. Why: Everything-at-once group entrances where a stagger belongs are a finding. Values: 30–80ms. [Everything-at-once group entrances where a 30–80ms stagger belongs]
- **must** (motion, all): Never let a stagger block interaction. Why: Stagger is decorative. [Stagger is decorative — it must never block interaction.]
- **consider** (motion, css): Mask a crossfade that visibly double-exposes two states with a subtle filter: blur(2px) during the transition. Why: A jarring crossfade that shows two overlapping states can be masked this way. Values: filter: blur(2px). [crossfades that visibly double-expose]
- **should** (motion, all): Add a brief transition to state changes that teleport, such as content swaps and layout jumps. Why: A brief transition prevents a jarring change. [8. Missed opportunities: State changes that teleport]
- **should** (motion, all): Animate spatially connected UI, such as a panel that appears from a trigger, so the motion explains where it came from. Why: Spatially-connected UI with no motion is a missed opportunity. [Spatially-connected UI (a panel that appears from a trigger)]
- **consider** (motion, all): Spend the delight budget on rare, high-emotion moments such as first run, success and celebration. Why: Rendering these with no delight is a missed opportunity. [Rare, high-emotion moments (first-run, success, celebration)]
- **should** (motion, css): Use translate percentages (translateY(100%) equals the element's own height) and clip-path: inset() reveals instead of hardcoded pixel offsets. Why: Listed as the tools for missed-opportunity motion; no hardcoded pixel offsets. Values: translateY(100%), clip-path: inset(). [translate percentages ... no hardcoded pixel offsets]
- **must** (process, all): Report at most a handful of missed opportunities, each grounded in a UX seam you actually observed. Why: Missed opportunities should not become a wishlist. [Report at most a handful ... not a wishlist.]

### Decisions it informs

- Should this element animate at all, given how often people see it?
  - No animation: The action happens instantly every time. When: Used 100+ times a day, such as keyboard shortcuts or a command palette toggle.
  - Removed or drastically reduced: Barely any motion on constantly used surfaces. When: Used tens of times a day, such as hover effects and list navigation.
  - Standard animation: Normal entrance and exit motion within the duration budget. When: Occasional UI such as modals, drawers and toasts.
  - Delight: Richer, more expressive motion. When: Rare or first-time moments such as onboarding, feedback and celebrations.
  - Recommendation: Decide by frequency using the table; for high-frequency and keyboard-initiated actions, the strongest fix is often deleting the animation.
- Which easing curve should each kind of motion use? (`Q-motion-03`)
  - ease-out: Starts fast and feels responsive. When: Entering or exiting, and the default.
  - ease-in-out: Strong version --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1) for on-screen movement. When: Moving or morphing on screen.
  - ease: The built-in ease curve. When: Hover and color changes.
  - linear: Used only for motion that runs continuously. When: Constant motion such as marquees and progress.
  - ease-in: Starts slow, delaying the moment the user is watching. When: Never on UI; always a finding.
  - Recommendation: Group curves by what the motion does, default to ease-out, never use ease-in on UI, and ship strong custom curves as tokens (--ease-out cubic-bezier(0.23, 1, 0.32, 1), --ease-in-out cubic-bezier(0.77, 0, 0.175, 1), --ease-drawer cubic-bezier(0.32, 0.72, 0, 1)).
- How long should each kind of UI animation run? (`Q-motion-02`)
  - Button press feedback: 100–160ms. When: Pressable elements.
  - Tooltips, small popovers: 125–200ms. When: Small anchored overlays.
  - Dropdowns, selects: 150–250ms. When: Menus and select lists.
  - Modals, drawers: 200–500ms. When: Larger overlays.
  - Marketing / explanatory: Can be longer. When: Marketing pages and explanatory motion, not product UI.
  - Recommendation: Keep UI animations under 300ms and use the band for each element type; durations over 300ms on UI elements are a finding.
- Where should a scaling element grow from?
  - From its trigger: The popover visibly comes out of the button that opened it. When: Popovers, dropdowns and tooltips (transform-origin: var(--transform-origin)).
  - From center: The element grows evenly in place. When: Modals, which appear centered; this is correct and exempt.
  - Recommendation: Anchor trigger-attached elements to their trigger; keep modals centered.
- How should rapidly triggered or reversible motion be built?
  - CSS transitions: Retarget from the current state when interrupted. When: Predetermined, reversible UI such as toggles and expand/collapse.
  - Springs: Carry velocity when interrupted. When: Gesture-driven motion such as drags.
  - Keyframes: Restart from zero when retriggered, so they jump. When: Not for rapidly triggered UI such as toasts and toggles.
  - Recommendation: Use transitions or springs for anything triggered rapidly or reversible mid-motion; springs for gestures.
- How should springs be configured? (`Q-motion-04`)
  - Apple-style duration and bounce: { type: "spring", duration: 0.5, bounce: 0.2 }, with bounce kept subtle at 0.1-0.3. When: Recommended default.
  - Visible bounce: Bounce the eye can clearly see. When: Only drag-to-dismiss and playful moments.
  - Recommendation: Apple-style config with bounce kept at 0.1-0.3.
- What should happen when someone turns on reduced motion? (`Q-motion-07`)
  - Fewer and gentler animations: Movement and position changes are removed; opacity and color transitions that aid comprehension stay. When: The playbook's target.
  - Remove all motion and feedback: Nothing animates, including helpful feedback. When: Treated as a finding (reduced motion is not zero).
  - Recommendation: Keep opacity and color, drop movement; in JS branch transform values on useReducedMotion().
- How lively should the product's motion personality be? (`Q-motion-01`)
  - Crisp: Motion stays crisp, with no bouncy outliers. When: Dashboards.
  - Bouncier: Motion can be bouncier. When: Playful products.
  - Recommendation: Match the product's personality and keep it consistent; one bouncy component in a crisp app is a finding.
- Should groups of items enter one by one? (`Q-motion-06`)
  - Stagger: Items appear 30-80ms apart. When: List and grid entrances.
  - All at once: Everything appears together. When: Treated as a finding where a stagger belongs.
  - Recommendation: Use a 30-80ms stagger that never blocks interaction.

### Process

1. Audit purpose and frequency: Hunt for animations on keyboard-initiated actions, command palettes with open/close transitions, and decorative motion on list items or hover states hit constantly; often the fix is to delete the animation.
2. Audit easing and duration: Hunt for ease-in anywhere, bare ease/linear on entrances, durations over 300ms on UI elements, and delay plus animation on every tooltip in a toolbar.
3. Audit physicality and origin: Hunt for scale(0), pure-fade entrances with no initial transform, transform-origin: center (or none) on trigger-anchored elements, and pressable elements with no press feedback; skip modals.
4. Audit interruptibility: Hunt for @keyframes on toasts, toggles and rapidly triggered UI, gesture handlers that tween with fixed-duration keyframes, drags without velocity-based dismissal, and hard stops at drag boundaries.
5. Audit performance: Hunt for transition: all, animated layout properties, Framer Motion shorthand props on busy pages, setProperty('--x', ...) driving child transforms, and rAF loops doing what CSS could.
6. Audit accessibility: Hunt for movement with no prefers-reduced-motion handling, ungated :hover motion, and reduced-motion implementations that remove all feedback.
7. Audit cohesion and tokens: Hunt for duplicated near-identical easings and durations, one bouncy component in a crisp app, list or grid entrances with no stagger, and crossfades that visibly double-expose.
8. Note missed opportunities: List a handful of places that should animate but do not (teleporting state changes, unexplained spatially connected panels, rare high-emotion moments), grounded in observed UX seams.

### Examples and visual references

- Command palette with no open/close animation (Raycast): Cited as the correct behavior for a UI used 100+ times a day.
- Motion token block with three custom curves: CSS custom properties --ease-out: cubic-bezier(0.23, 1, 0.32, 1), --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1), --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1), shown as the tokens plans should introduce.
- Popover scaling from its trigger (Base UI): .popover { transform-origin: var(--transform-origin); } makes the popover grow from the element that opened it rather than from its center.
- Framer Motion transform string (Framer Motion): animate={{ transform: "translateX(100px)" }} shown as the hardware-accelerated alternative to the x/y/scale shorthand props.
- Reduced-motion and hover media queries: @media (prefers-reduced-motion: reduce) swaps to animation: fade 0.2s ease (keeps opacity/color, drops movement); @media (hover: hover) and (pointer: fine) gates a :hover transform: scale(1.05).

### Numbers

- 100+ times/day: Frequency at which an element gets no animation, ever. [Frequency table]
- 300ms: Upper limit for UI animations. [UI animations stay under 300ms]
- 100–160ms: Button press feedback duration. [Duration table]
- 125–200ms: Tooltip and small popover duration. [Duration table]
- 150–250ms: Dropdown and select duration. [Duration table]
- 200–500ms: Modal and drawer duration. [Duration table]
- cubic-bezier(0.23, 1, 0.32, 1): Strong ease-out for UI (--ease-out). [2. Easing & duration]
- cubic-bezier(0.77, 0, 0.175, 1): Strong ease-in-out for on-screen movement (--ease-in-out). [2. Easing & duration]
- cubic-bezier(0.32, 0.72, 0, 1): iOS-like drawer curve (--ease-drawer). [2. Easing & duration]
- scale(0.9–0.97): Starting scale for entrances, with opacity: 0. [Never scale(0)]
- scale(0.97): Press feedback on :active. [Press feedback]
- 160ms: Press feedback transform transition with ease-out. [Press feedback]
- 0.95–0.98: Range for subtle press-feedback scale. [Press feedback]
- duration: 0.5, bounce: 0.2: Recommended Apple-style spring config. [Spring configs]
- 0.1–0.3: Subtle spring bounce range. [Keep bounce subtle]
- ~0.11: Velocity threshold, Math.abs(distance)/elapsedMs, for drag dismissal. [velocity-based dismissal]
- 20px: Maximum transition-time filter: blur(). [5. Performance]
- 0.2s: Fade animation duration in the reduced-motion example. [6. Accessibility]
- scale(1.05): Hover transform in the gated hover example. [6. Accessibility]
- 30–80ms: Stagger between items in group entrances. [7. Cohesion & tokens]
- blur(2px): Filter used to mask a double-exposing crossfade. [7. Cohesion & tokens]
- translateY(100%): Moves an element by its own height, instead of hardcoded pixel offsets. [8. Missed opportunities]

<!-- /od:learn -->
