---
type: source
title: "emilkowalski/skills: skills/animate/RECIPES.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-animate-recipes
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/animate/RECIPES.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - animation
  - recipes
  - button-press
  - popover
  - tooltip
  - modal
  - drawer
  - toast
  - accordion
  - stagger
  - hold-to-confirm
  - tabs
---

# emilkowalski/skills: skills/animate/RECIPES.md

## Metadata

- Video ID: `eks-skills-animate-recipes`
- Channel: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/animate/RECIPES.md

## Summary

The animate skill's recipes file gives ready-to-build CSS and JS for the animations that come up most: button press, dropdown/popover/menu/select, tooltip, modal, drawer, toast, accordion, staggered group entrance, hold-to-confirm, tab indicator, scroll reveal, drag-to-dismiss, a blur-masked crossfade and programmatic WAAPI motion. Each recipe fixes exact durations, curves (the --ease-out, --ease-in-out and --ease-drawer tokens), starting scales, transform origins and the detail most implementations miss, such as neighbouring tooltips opening instantly, dismissing a drag on velocity as well as distance, or clipping a duplicated tab list instead of timing colour changes. It also says where each recipe belongs (scroll reveal on marketing only, stagger only for lists seen occasionally, hold-to-confirm for destructive actions). For a design system, it is a per-component motion specification that can become component motion tokens and default behaviours [inferred].

## Key Ideas

- Start from a recipe and adapt it rather than building motion from scratch.
- A press scales the whole button to 0.97, labels and icons included, so it reads as a physical press.
- Popovers, dropdowns and tooltips scale out of their trigger using the supplied transform origin; the modal is the one popover that stays centered.
- Tooltips are faster than popovers, and once one is open its neighbours open with no delay and no animation.
- A modal's backdrop fades together with the modal so they read as one surface.
- Drawers slide up from translateY(100%) over 500ms on the --ease-drawer curve, the way Vaul hides a drawer; add drag and it becomes a gesture problem.
- Toast motion is tuned to the component's personality: plain ease and slightly slower than typical UI.
- Accordion height animation costs layout on every frame, so it stays short and animates to a measured height, not auto.
- Stagger is decorative, reserved for occasionally seen groups, and must never block interaction.
- Hold-to-confirm uses a clip-path fill that is slow and linear on press (it is a progress indicator) and snappy on release.
- Clipping a styled duplicate of the tab list keeps text and background colour changes perfectly in sync.
- Scroll reveals are for marketing surfaces only and fire once.
- Drag-to-dismiss uses springs, dismisses on a fast flick as well as on distance, and needs pointer capture, multi-touch protection, damping and friction past edges.
- When a crossfade still shows two objects swapping, a small blur blends them into one perceived change.
- WAAPI gives CSS-grade, interruptible, hardware-accelerated motion from JS with no bundle cost.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Author of the skills repository these recipes come from
- [[entities/base-ui|Base UI]] (library): Supplies var(--transform-origin) used by the popover and tooltip recipes
- [[entities/vaul|Vaul]] (library): Drawer library; the drawer recipe shows how Vaul hides a drawer before animating it in
- [[entities/sonner|Sonner]] (library): Toast library whose elegant feel comes partly from motion tuned to the component's personality
- [[entities/motion-motion-dev|Motion (motion.dev)]] (library): Its useInView hook ({ once: true, margin: "-100px" }) is one way to trigger the scroll reveal; the drag settle config { type: "spring", duration: 0.5, bounce: 0.2 } is in its format [inferred]
- [[entities/intersectionobserver|IntersectionObserver]] (concept): Browser API for triggering the scroll reveal
- [[entities/web-animations-api-waapi|Web Animations API (WAAPI)]] (concept): element.animate() for programmatic motion without a library
- [[entities/starting-style|@starting-style]] (concept): CSS at-rule used for the toast's entry state, with a mount-flag fallback
- [[entities/clip-path|clip-path]] (concept): Property animated for hold-to-confirm, the tab indicator, scroll reveal and WAAPI examples
- [[entities/safari|Safari]] (product): Browser where heavy blur is especially expensive

## Topics

- [[topics/micro-interactions|Micro-interactions]]: Button press scale(0.97) at 160ms, hold-to-confirm fill, tab indicator colour change via clip-path, crossfade masked with blur.
- [[topics/buttons-and-actions|Buttons and actions]]: Every pressable element scales to 0.97 on :active; destructive actions can use hold-to-confirm (2s linear press, 200ms release).
- [[topics/modals-and-popovers|Modals and popovers]]: Popover/dropdown/menu/select at 200ms from scale(0.95) out of the trigger; tooltip at 125ms from scale(0.97) with instant neighbours; modal centered at 250ms from scale(0.96) with a matching backdrop fade.
- [[topics/drawers-and-sheets|Drawers and sheets]]: Drawer slides translateY(100%) to 0 over 500ms on the --ease-drawer curve, the way Vaul hides a drawer; dragging turns it into a gesture recipe.
- [[topics/toasts-and-notifications|Toasts and notifications]]: Toast enters from translateY(100%) over 400ms with plain ease via @starting-style (mount-flag fallback); stacked reflow needs opacity balanced against height by feel.
- [[topics/gestures-and-drag|Gestures and drag]]: Drag-to-dismiss dismisses on distance or velocity > 0.11, sets transform directly, uses pointer capture, multi-touch protection, damping and friction, and settles with a spring.
- [[topics/easing-and-timing|Easing and timing]]: Exact per-component durations and curve tokens, linear for progress fills, ease for toasts, ease-in-out for tab clips and scroll reveals.
- [[topics/spring-animation|Spring animation]]: Drag settles with { type: "spring", duration: 0.5, bounce: 0.2 } so an interrupted drag keeps its velocity.
- [[topics/animation-performance|Animation performance]]: Accordion height costs layout every frame so keep it short; blur under 20px because heavy blur is expensive; set drag transforms directly; WAAPI is hardware-accelerated.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: Tab indicator: duplicate the tab list, style the copy as active and animate its clip-path over 250ms.
- [[topics/landing-pages|Landing pages]]: Scroll reveal via clip-path over 600ms belongs on marketing surfaces only and fires once.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: CSS for each recipe using data-starting-style/data-ending-style attributes, @starting-style with a React mount-flag fallback, IntersectionObserver or useInView, and WAAPI.

## Notable Claims

- scale() scales children too, so the label and icons come along, which makes a press read as physical. Evidence: Button press: scale() scales children too
- :active is a real press on touch, so the button press needs no hover gating. Evidence: No hover gating needed here
- The transform-origin is the whole point of the popover recipe: the panel should look like it came out of the thing you clicked. Evidence: Dropdown, popover, menu, select
- The tooltip's initial delay prevents accidental activation; after that, skipping both delay and animation makes the whole toolbar feel faster. Evidence: Tooltip: Once one tooltip is open, neighbours open instantly
- Animating the backdrop's opacity alongside the modal makes them read as one surface. Evidence: Modal: Animate the backdrop's opacity alongside it
- Vaul hides a drawer with translateY(100%) before animating it in. Evidence: Drawer / sheet: This is how Vaul hides a drawer
- Sonner reads as elegant partly because its motion is tuned to the component's personality rather than the generic UI budget. Evidence: Toast: ease rather than ease-out
- There is no formula for balancing opacity against height when stacked toasts reflow. Evidence: When toasts stack and the list reflows
- The accordion is one of the few animations that costs layout on every frame, so a long duration is expensive as well as sluggish. Evidence: Accordion / collapse
- Timing individual colour transitions across a tab list never quite lands; clipping one duplicated element keeps text and background in perfect sync. Evidence: Tab indicator with a color transition
- Re-animating a scroll reveal on every scroll-by is an interface fighting its reader. Evidence: Scroll reveal: Fire it once
- Driving a dragged element's transform through a CSS variable on the parent recalculates styles for every child. Evidence: Drag to dismiss: Set transform on the dragged element directly
- Without blur, the eye reads two distinct objects swapping; blur blends them into one perceived transformation. Evidence: Masking a crossfade that won't settle
- Heavy blur is expensive, especially in Safari. Evidence: Keep it under 20px
- WAAPI is hardware-accelerated, interruptible and has no bundle cost. Evidence: Programmatic, without a library

## Quotes

> Stagger is decorative — it must never block interaction while it plays.
> progress shouldn't ease.
> Real things slow before they stop.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Recipes are web-only CSS and JS; the data-starting-style, data-ending-style and data-instant attributes assume a component library that sets them (Base UI is named only for --transform-origin) [inferred].
- Caveat: The tab indicator's clip-path: inset(0 60% 0 20%) is a placeholder; the source says the real values are driven by the active tab's position.
- Caveat: SWIPE_THRESHOLD is referenced but its value is not given.
- Caveat: Several recipes exceed the skill's 'UI animations stay under 300ms' rule (toast 400ms, drawer 500ms, scroll reveal 600ms, WAAPI example 1000ms); the source justifies the toast by personality and scroll reveal by being marketing-only [inferred for the comparison].
- Caveat: The stagger recipe uses keyframes, while the skill forbids keyframes only for rapidly triggered elements; stagger is scoped to occasionally seen groups [inferred].
- Caveat: Values are pinned to commit 85e8e23 of emilkowalski/skills (MIT).
- Caveat: The tooltip's initial delay is mentioned but its length is not given.
- Caveat: The source says 'Start from the recipe, then adapt', so exact recipe durations, scales and offsets are marked should; must is kept for what the source states as a rule (trigger transform origin, centered modal, instant neighbouring tooltips, short accordions, stagger never blocking and not on all-day lists, linear progress, clipped tab list, marketing-only scroll reveal fired once, springs and the four drag details, blur under 20px) [inferred].

### Rules and practices

- **should** (process, web): Start from the matching recipe and adapt it; do not rebuild common animations from scratch. Why: The recipes are ready-to-build implementations for the cases that come up most. [Animation Recipes intro]
- **should** (tokens, css): Write the recipes' curves as the --ease-out, --ease-in-out and --ease-drawer tokens defined in SKILL.md, referenced with var(). Why: The source states that the recipes' curves are the tokens defined in SKILL.md. Values: --ease-out, --ease-in-out, --ease-drawer. [Curves are the --ease-out, --ease-in-out, and --ease-drawer tokens defined in SKILL.md]
- **should** (components, css): Give every pressable element press feedback: transition: transform 160ms var(--ease-out) and transform: scale(0.97) on :active. Why: Instant feedback that the interface heard the user. Values: transition: transform 160ms var(--ease-out), transform: scale(0.97). [Button press]
- **should** (components, css): Apply the press scale to the whole button so the label and icons scale with it. Why: scale() scales children too, which is what makes it read as a physical press. Values: scale(). [scale() scales children too]
- **must** (accessibility, css): Leave the :active press ungated, and gate any :hover styling separately. Why: :active is a real press on touch, so it needs no hover gating. Values: :active, :hover. [No hover gating needed here: :active is a real press on touch. Gate any :hover styling separately.]
- **must** (components, css): Scale dropdowns, popovers, menus, selects and tooltips out of their trigger with transform-origin: var(--transform-origin). Why: The transform-origin is the whole point: the panel should look like it came out of the thing you clicked. Values: transform-origin: var(--transform-origin). [Dropdown, popover, menu, select: The transform-origin is the whole point; Tooltip uses the same origin]
- **should** (components, css): Transition dropdown, popover, menu and select opacity and transform over 200ms var(--ease-out), entering from and exiting to opacity: 0 and transform: scale(0.95) ([data-starting-style] and [data-ending-style]). Why: The recipe for panels that scale out of their trigger, not out of thin air. Values: opacity 200ms var(--ease-out), transform 200ms var(--ease-out), opacity: 0, transform: scale(0.95), [data-starting-style], [data-ending-style]. [Dropdown, popover, menu, select]
- **should** (components, css): Transition tooltip transform and opacity over 125ms var(--ease-out), entering from and exiting to opacity: 0 and transform: scale(0.97). Why: Same shape as a popover, faster. Values: transform 125ms var(--ease-out), opacity 125ms var(--ease-out), opacity: 0, transform: scale(0.97). [Tooltip]
- **should** (components, all): Keep an initial delay before the first tooltip opens. Why: The initial delay prevents accidental activation. [The initial delay prevents accidental activation]
- **must** (components, css): Once one tooltip is open, open neighbouring tooltips instantly by skipping both the delay and the animation (transition-duration: 0ms on [data-instant]). Why: The initial delay prevents accidental activation; after that, skipping both the delay and the animation makes the whole toolbar feel faster. Values: .tooltip[data-instant], transition-duration: 0ms. [Tooltip: the detail most implementations miss; Once one tooltip is open, neighbours open instantly]
- **must** (components, css): Keep modals centered with transform-origin: center; they are exempt from the trigger origin. Why: The modal is the one popover that stays centered: it is not anchored to a trigger. Values: transform-origin: center. [Modal: The one popover that stays centered; exempt — not anchored to a trigger]
- **should** (components, css): Transition modal opacity and transform over 250ms var(--ease-out), entering from and exiting to opacity: 0 and transform: scale(0.96). Why: The source's modal recipe values; it gives no separate reason for 250ms or 0.96. Values: opacity 250ms var(--ease-out), transform 250ms var(--ease-out), opacity: 0, transform: scale(0.96). [Modal]
- **should** (components, css): Fade the modal backdrop's opacity alongside the modal with the same timing (opacity 250ms var(--ease-out)). Why: So the modal and backdrop read as one surface. Values: opacity 250ms var(--ease-out). [Animate the backdrop's opacity alongside it]
- **should** (components, css): Animate drawers and sheets with transform: translateY(0) when open and translateY(100%) when closed ([data-closed]), over 500ms var(--ease-drawer). Why: This is how Vaul hides a drawer before animating it in. Values: transform: translateY(0), transform 500ms var(--ease-drawer), transform: translateY(100%), [data-closed]. [Drawer / sheet]
- **should** (components, all): When a drawer can be dragged, treat it as a gesture and follow the drag-to-dismiss recipe. Why: Add drag and it becomes a gesture problem. [Add drag and it becomes a gesture problem]
- **should** (components, css): Animate toasts in from opacity: 0 and translateY(100%) using @starting-style, transitioning opacity and transform over 400ms ease. Why: The source's toast recipe; its plain ease and slower timing are tuned to the toast's personality rather than to the generic UI budget. Values: opacity 400ms ease, transform 400ms ease, opacity: 0, transform: translateY(100%), @starting-style. [Toast]
- **should** (motion, all): Use ease rather than ease-out for toasts and run them slightly slower than typical UI, tuning motion to the component's personality. Why: Sonner reads as elegant partly because its motion is tuned to the component's personality rather than to the generic UI budget. Values: ease, 400ms. [ease rather than ease-out, slightly slower than typical UI]
- **should** (tooling, react): Where @starting-style is not available, fall back to a mount flag (useEffect(() => { setMounted(true); }, []) with data-mounted={mounted}). Why: Fallback for the toast entry state. Values: useEffect(() => { setMounted(true); }, []);, data-mounted={mounted}. [If @starting-style isn't available, fall back to the mount flag]
- **should** (process, all): When stacked toasts reflow, adjust the opacity change against the height change by feel, then check it again the next day. Why: There's no formula for that pair. [When toasts stack and the list reflows]
- **should** (components, css): Animate accordions with overflow: hidden and height and opacity over 200ms var(--ease-out). Why: The source's accordion recipe; it stays short because height costs layout on every frame. Values: overflow: hidden, height 200ms var(--ease-out), opacity 200ms var(--ease-out). [Accordion / collapse]
- **must** (motion, web): Keep accordion animations short. Why: It is one of the few animations that costs layout on every frame, so a long duration is expensive as well as sluggish. [Keep it short]
- **should** (motion, web): Do not animate height to auto; measure the content height in JS, or use a headless primitive that supplies it. Why: Stated in the accordion recipe; the source gives no further reason. Values: auto. [Measure the content height in JS (or use a headless primitive that supplies it) rather than animating to auto]
- **should** (motion, css): Stagger a group entrance: each item starts at opacity: 0 and transform: translateY(8px) and runs animation: fadeIn 300ms var(--ease-out) forwards to opacity: 1 and translateY(0), with animation-delay 50ms, 100ms and 150ms on the 2nd, 3rd and 4th items. Why: The source's recipe for a list or grid the user sees occasionally. Values: opacity: 0, transform: translateY(8px), animation: fadeIn 300ms var(--ease-out) forwards, animation-delay: 50ms, animation-delay: 100ms, animation-delay: 150ms, @keyframes fadeIn, opacity: 1, transform: translateY(0). [Stagger a group entrance]
- **must** (motion, all): Do not stagger a list the user scrolls past all day; keep stagger for lists or grids seen occasionally. Why: Stated as the recipe's scope; the source gives no further reason here (SKILL.md's frequency gate gives little or no motion to frequently seen UI) [inferred]. [For a list or grid the user sees occasionally — not for a list they scroll past all day]
- **must** (motion, all): Never let a stagger block interaction while it plays. Why: Stagger is decorative. [Stagger is decorative — it must never block interaction]
- **should** (patterns, all): Use hold-to-confirm for destructive actions where a plain click is too easy to fire by accident. Why: A plain click is too easy to fire by accident on a destructive action. [Hold to confirm: For destructive actions]
- **should** (components, css): Build hold-to-confirm with an overlay clipped by clip-path: inset(0 100% 0 0) that fills to inset(0 0 0 0) over 2s linear while the button is :active, snaps back over 200ms var(--ease-out) on release, and scale(0.97) on the button while pressed. Why: Press slow and deliberate; release snappy. Values: clip-path: inset(0 100% 0 0), clip-path: inset(0 0 0 0), clip-path 2s linear, clip-path 200ms var(--ease-out), transform: scale(0.97). [Hold to confirm]
- **must** (motion, all): Use linear easing for progress fills. Why: The fill is a progress indicator, and progress shouldn't ease. Values: linear. [linear is correct here]
- **must** (components, css): For a tab indicator with a colour change, do not time individual colour transitions; duplicate the tab list, style the copy as the active state (different background and text colour), clip the copy so only the active tab shows, and animate the clip. Why: Timing individual colour transitions never quite lands; one element being revealed keeps text and background in perfect sync. [Tab indicator with a color transition]
- **should** (components, css): Animate the active tab copy's clip-path (driven by the active tab's position) over 250ms var(--ease-in-out). Why: Tab indicator recipe. Values: clip-path: inset(0 60% 0 20%), clip-path 250ms var(--ease-in-out). [.tabs-active-copy]
- **must** (motion, web): Use scroll reveals only on marketing surfaces, never on functional UI a user visits daily. Why: Scroll reveal recipe scope. [Scroll reveal: Marketing surfaces only]
- **should** (motion, css): Build scroll reveals by transitioning clip-path from inset(0 0 100% 0) to inset(0 0 0 0) over 600ms var(--ease-in-out) when [data-visible] is set. Why: The source's scroll reveal recipe. Values: clip-path: inset(0 0 100% 0), clip-path 600ms var(--ease-in-out), clip-path: inset(0 0 0 0), [data-visible]. [Scroll reveal]
- **must** (motion, web): Trigger scroll reveals with IntersectionObserver or Motion's useInView with { once: true, margin: "-100px" }, and fire them only once. Why: Re-animating on every scroll-by is an interface fighting its reader. Values: { once: true, margin: "-100px" }. [Trigger with IntersectionObserver ... Fire it once]
- **must** (motion, all): Use springs, not durations, for drag-to-dismiss. Why: The user can reverse mid-motion. [Drag to dismiss: Springs, not durations]
- **should** (patterns, web): Dismiss a dragged element on a flick as well as on distance: compute velocity = Math.abs(swipeAmount) / timeTaken and dismiss when Math.abs(swipeAmount) >= SWIPE_THRESHOLD or velocity > 0.11. Why: Dismiss on a flick, not just on distance. Values: velocity > 0.11, SWIPE_THRESHOLD. [Dismiss on a flick, not just on distance]
- **must** (motion, web): Set the dragged element's transform directly (element.style.transform = `translateY(${distance}px)`) rather than through a CSS variable on the parent. Why: Driving it through a CSS variable on the parent recalcs styles for every child. Values: element.style.transform. [Set transform on the dragged element directly]
- **must** (patterns, web): Capture the pointer once a drag starts. Why: So the drag continues when the pointer leaves the element's bounds. [Pointer capture]
- **must** (patterns, web): Ignore new touch points while a drag is in progress (if (isDragging) return). Why: Otherwise switching fingers mid-drag makes the element jump. Values: if (isDragging) return. [Multi-touch protection]
- **must** (patterns, all): Damp dragging past a natural boundary so the element moves less the further it goes. Why: Real things slow before they stop. [Damping past boundaries]
- **must** (patterns, all): Allow over-drag with rising resistance instead of stopping it at a hard wall. Why: Listed among the four details that separate a good drag from a bad one: friction, not a wall. [Friction, not a wall]
- **must** (motion, react): Settle a released or interrupted drag with a spring, { type: "spring", duration: 0.5, bounce: 0.2 }, not a duration. Why: So an interrupted drag keeps its velocity. Values: { type: "spring", duration: 0.5, bounce: 0.2 }. [Settle with a spring]
- **consider** (motion, css): When two states visibly overlap during a crossfade and no easing or duration tuning fixes it, blur the seam: transition filter and opacity over 200ms ease, with filter: blur(2px) and opacity: 0.7 while transitioning. Why: Without blur the eye reads two distinct objects swapping; blur blends them into one perceived transformation. Values: filter 200ms ease, opacity 200ms ease, filter: blur(2px), opacity: 0.7. [Masking a crossfade that won't settle]
- **must** (motion, web): Keep blur under 20px. Why: Heavy blur is expensive, especially in Safari. Values: 20px. [Keep it under 20px]
- **should** (tooling, web): When motion needs JS control but not a dependency, use WAAPI (element.animate()), for example a clip-path reveal with { duration: 1000, fill: 'forwards', easing: 'cubic-bezier(0.77, 0, 0.175, 1)' }. Why: WAAPI gives CSS-grade performance: hardware-accelerated, interruptible, no bundle cost. Values: element.animate(, duration: 1000, fill: 'forwards', easing: 'cubic-bezier(0.77, 0, 0.175, 1)'. [Programmatic, without a library]

### Decisions it informs

- Should list or grid items enter together or one after another? (`Q-motion-06`)
  - Staggered entrance: Items fade up from translateY(8px) one after another, 50ms apart, each over 300ms. When: A list or grid the user sees occasionally.
  - All at once / no entrance: Items appear together without a sequence. When: Lists the user scrolls past all day.
  - Recommendation: Stagger only occasionally seen groups, and never let it block interaction.
- How should toasts move: to the generic UI budget or tuned to the component's personality?
  - Generic UI budget: ease-out and a typical short UI duration. When: Most UI elements.
  - Tuned to personality: Plain ease and slightly slower (400ms), which reads as elegant. When: Toasts, following Sonner.
  - Recommendation: Tune toast motion to its personality: 400ms ease from translateY(100%).
- How should a destructive action be confirmed?
  - Plain click: Fires immediately; easy to trigger by accident. When: Non-destructive actions [inferred].
  - Hold to confirm: A fill sweeps across the button over 2s while held and snaps back in 200ms on release. When: Destructive actions where a plain click is too easy to fire by accident.
  - Recommendation: Hold to confirm for destructive actions that are too easy to fire by accident.
- How should a tab indicator change colour when the active tab changes?
  - Individual colour transitions: Text and background colours interpolate separately, and the timing never quite lands. When: Not recommended.
  - Clipped duplicate tab list: A styled copy of the tabs is revealed by an animated clip, so text and background change in perfect sync. When: Tab lists with a colour change on the active tab.
  - Recommendation: Clip a duplicated, active-styled tab list and animate the clip over 250ms var(--ease-in-out).
- When should a drag dismiss the element?
  - Distance only: Dismisses only past a set swipe threshold; a fast short flick does not dismiss [inferred]. When: Not recommended.
  - Distance or velocity: Dismisses past the threshold or on a fast flick (velocity > 0.11). When: Drag-to-dismiss surfaces, such as a draggable drawer.
  - Recommendation: Dismiss on distance or velocity, and settle with a spring so interrupted drags keep their velocity.
- How should an element's entry state be set up?
  - CSS @starting-style: The browser animates from the starting style on mount with no JS. When: Where @starting-style is available.
  - Mount flag: A useEffect sets mounted to true and a data-mounted attribute drives the transition. When: Where @starting-style isn't available.
  - Recommendation: Use @starting-style and fall back to the mount flag.
- What to do when a crossfade still shows two overlapping states?
  - Keep tuning easing and duration: Often still reads as two objects swapping. When: First attempt.
  - Blur the seam: blur(2px) and opacity 0.7 during the transition blend the states into one perceived change. When: When no amount of easing or duration tuning fixes it.
  - Recommendation: Add a small blur (under 20px) once tuning fails.

### Process

1. Match a recipe: Find the recipe for the component (button press, dropdown, tooltip, modal, drawer, toast, accordion, stagger, hold-to-confirm, tab indicator, scroll reveal, drag-to-dismiss) and start from it, then adapt.
2. Build a tab indicator by clipping: Duplicate the tab list, style the copy as active (background and text colour), clip it so only the active tab shows, and animate the clip-path from the active tab's position over 250ms var(--ease-in-out).
3. Build drag-to-dismiss: Set transform directly on the element while dragging, capture the pointer, ignore extra touch points, damp and add friction past edges, dismiss on distance or velocity > 0.11, and settle with a spring (duration 0.5, bounce 0.2).
4. Tune stacked toast reflow by feel: Adjust the opacity change against the height change until it feels right, then check it again the next day.
5. Rescue a stubborn crossfade: If easing and duration tuning fail, add filter: blur(2px) and opacity 0.7 during the transition, both over 200ms ease, keeping blur under 20px.

### Examples and visual references

- Button press: The button, with its label and icons, shrinks to 97% on press over 160ms, reading as a physical press.
- Popover scaling out of its trigger (Base UI (var(--transform-origin))): The panel grows from 95% scale and 0 opacity out of the clicked element over 200ms.
- Toolbar tooltips: The first tooltip waits and animates in over 125ms from scale 0.97; neighbouring tooltips then appear instantly with no delay or animation.
- Modal with backdrop: The modal grows from 96% scale at the center while the backdrop fades over the same 250ms, reading as one surface.
- Drawer hidden below the screen (Vaul): The drawer sits at translateY(100%) and slides up over 500ms on the --ease-drawer curve.
- Toast motion (Sonner): Toasts rise from translateY(100%) with plain ease over 400ms, slightly slower than typical UI, which reads as elegant.
- Hold-to-confirm button: A fill sweeps left to right over 2s linearly while pressed and snaps back in 200ms when released.
- Tab indicator via clipped duplicate: An active-styled copy of the tab list is clipped to the active tab; moving the clip changes text and background colour in sync.
- Scroll reveal: A marketing section is revealed top to bottom by clip-path over 600ms, once, when it scrolls into view.
- Blur-masked crossfade: During a state change the content blurs 2px and drops to 0.7 opacity so the two states read as one transformation.

### Numbers

- 160ms / scale(0.97): Button press transition and pressed scale [Button press]
- 200ms / scale(0.95): Dropdown, popover, menu, select duration and starting scale [Dropdown, popover, menu, select]
- 125ms / scale(0.97): Tooltip duration and starting scale [Tooltip]
- 0ms: Transition duration for neighbouring tooltips once one is open [.tooltip[data-instant]]
- 250ms / scale(0.96): Modal and backdrop duration and modal starting scale [Modal]
- 500ms / translateY(100%): Drawer transition on --ease-drawer and its closed position [Drawer / sheet]
- 400ms ease: Toast opacity and transform transition [Toast]
- 200ms: Accordion height and opacity transition [Accordion / collapse]
- 300ms / translateY(8px): Stagger item fadeIn duration and starting offset [Stagger a group entrance]
- 50ms / 100ms / 150ms: animation-delay on the 2nd, 3rd and 4th staggered items [.item:nth-child(2) { animation-delay: 50ms; }]
- 2s linear / 200ms: Hold-to-confirm press fill vs release [Hold to confirm]
- 250ms: Tab indicator clip-path transition on --ease-in-out [Tab indicator with a color transition]
- 600ms: Scroll reveal clip-path transition on --ease-in-out [Scroll reveal]
- -100px: useInView margin for triggering the scroll reveal once [{ once: true, margin: "-100px" }]
- 0.11: Velocity above which a drag dismisses regardless of distance [velocity > 0.11]
- duration: 0.5, bounce: 0.2: Spring used to settle a drag [Settle with a spring]
- blur(2px) / 0.7 / 200ms: Blur, opacity and duration for masking a crossfade [Masking a crossfade that won't settle]
- 20px: Maximum blur to keep costs down, especially in Safari [Keep it under 20px]
- 1000: Duration in ms of the WAAPI clip-path example, with cubic-bezier(0.77, 0, 0.175, 1) [Programmatic, without a library]
- cubic-bezier(0.77, 0, 0.175, 1): Easing of the WAAPI clip-path example (the same curve as --ease-in-out in SKILL.md [inferred]) [Programmatic, without a library]

<!-- /od:learn -->
