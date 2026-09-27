---
type: source
title: "emilkowalski/skills: skills/apple-design/SKILL.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-apple-design-skill
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/apple-design/SKILL.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - apple
  - wwdc
  - fluid-interfaces
  - springs
  - interruptibility
  - velocity-handoff
  - momentum-projection
  - rubber-banding
  - gestures
  - pointer-events
  - hysteresis
  - materials
---

# emilkowalski/skills: skills/apple-design/SKILL.md

## Metadata

- Video ID: `eks-skills-apple-design-skill`
- Channel: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/apple-design/SKILL.md

## Summary

This agent skill from emilkowalski/skills distils Apple's WWDC design talks, chiefly Designing Fluid Interfaces (WWDC 2018), and translates them to the web with CSS, Pointer Events, requestAnimationFrame and spring libraries such as Motion. Its core idea is that an interface feels alive when motion starts from the current on-screen value, inherits the user's velocity, projects momentum forward and can be grabbed and reversed at any moment, with springs as the tool that makes this natural. It gives exact values: Apple's spring damping and response pairs, a momentum projection function, a rubber-band formula, ~10px gesture hysteresis, press feedback at scale(0.97) over 100ms, and type tracking of -0.02em for display text. It also covers translucent materials and depth, audio-haptic feedback, three accessibility media queries (reduced motion, reduced transparency, more contrast), size-specific typography, Apple's eight design principles and a short design process. For a design system it is a ready set of motion, material, typography and interaction standards that can be written as tokens and component rules.

## Key Ideas

- Fluid means motion starts from the current on-screen value, inherits the user's velocity, projects momentum and can be grabbed and reversed at any instant.
- Response is the foundation: give feedback on pointer-down and remove every non-essential delay on the input path.
- Direct manipulation means 1:1 tracking that respects where the user grabbed the element.
- Interruptibility is the single most important principle; never lock out input and always animate from the live presentation value.
- Use springs for anything a user can touch, described by damping ratio and response rather than mass, stiffness and damping.
- Critically damped springs (damping 1.0) are the default; bounce (damping ~0.8) is reserved for interactions that carried momentum.
- Hand the release velocity to the spring and project the resting point from velocity before choosing a snap target.
- Keep spatial consistency: enter and exit along the same path, and anchor popovers and sheets to their trigger.
- Rubber-band at boundaries instead of stopping hard.
- Translucent materials express hierarchy; heavier materials for structure, lighter for interactive elements, and never light glass on light glass.
- Sound, haptics and visuals must be causal, fire on the same frame, and be used only where they earn their place.
- Reduced motion means a gentler, non-vestibular equivalent (cross-fades), not no feedback; also honour reduced transparency and more contrast.
- Typography changes with size: size-specific tracking, leading inverse to size, hierarchy from weight, size and leading together, and respect for the user's text size.
- Apple's eight principles (purpose, agency, responsibility, familiarity, flexibility, simplicity, craft, delight) are the names to reason with.
- Prototype interactively, design interaction and visuals together, and review motion frame by frame.

## Entities

- [[entities/apple|Apple]] (company): Source of the design approach, values and principles the skill translates for the web.
- [[entities/designing-fluid-interfaces-wwdc-2018|Designing Fluid Interfaces (WWDC 2018)]] (product): The main WWDC talk the skill draws on; its sample code supplies the momentum projection function.
- [[entities/the-details-of-ui-typography-wwdc-2020|The Details of UI Typography (WWDC 2020)]] (product): WWDC talk cited for the optical sizing, tracking and leading guidance.
- [[entities/designing-audio-haptic-experiences|Designing Audio-Haptic Experiences]] (product): Apple talk cited for the three rules of multimodal feedback: causality, harmony, utility.
- [[entities/principles-of-great-design-wwdc-2026|Principles of Great Design (WWDC 2026)]] (product): Apple talk cited for the eight design principles.
- [[entities/emilkowalski-skills|emilkowalski/skills]] (product): The MIT-licensed GitHub repository of agent skills that contains this apple-design skill.
- [[entities/motion-framer-motion|Motion / Framer Motion]] (library): Spring animation library whose bounce and duration API maps closely to Apple's damping and response, and which takes absolute px/s velocity.
- [[entities/pointer-events|Pointer Events]] (tool): Web input API used with setPointerCapture for 1:1 drag tracking.
- [[entities/requestanimationframe|requestAnimationFrame]] (tool): The web's display-synced clock, the counterpart of Apple's CADisplayLink.
- [[entities/cadisplaylink|CADisplayLink]] (tool): Apple's display-synced timer, named as the native equivalent of requestAnimationFrame.
- [[entities/backdrop-filter|backdrop-filter]] (tool): CSS property used to approximate Apple's translucent materials on the web.
- [[entities/vibration-api|Vibration API]] (tool): Web API for haptics that must fire on the same frame as the visual change.
- [[entities/vaul|Vaul]] (library): Bottom-sheet library named as an example of momentum projection done well.
- [[entities/embla|Embla]] (library): Carousel library named as an example of momentum projection done well.
- [[entities/control-center|Control Center]] (product): iOS feature whose modules grow up and out toward the finger, the example of hinting in the direction of a gesture.
- [[entities/dynamic-type|Dynamic Type]] (concept): Apple's user text-size setting; the skill says layouts should scale with it.
- [[entities/damping-ratio|Damping ratio]] (concept): Spring parameter that controls overshoot; 1.0 is critically damped, below 1.0 bounces.
- [[entities/response|Response]] (concept): Spring parameter in seconds for how quickly the value reaches the target; not a duration.
- [[entities/presentation-value|Presentation value]] (concept): The live on-screen value an interrupted animation must start from.
- [[entities/additive-animations|Additive animations]] (concept): iOS's native way of carrying velocity through a re-targeted animation.
- [[entities/momentum-projection|Momentum projection]] (concept): Using release velocity to predict where a flicked element would come to rest, then snapping near that point.
- [[entities/rubber-banding|Rubber-banding]] (concept): Progressive resistance past a boundary instead of a hard stop.
- [[entities/hysteresis|Hysteresis]] (concept): A small movement threshold or hit padding (~10px) before a gesture commits or a tap cancels.
- [[entities/vibrancy|Vibrancy]] (concept): Keeping text legible over translucent surfaces with higher contrast, heavier weight and slightly wider letter-spacing.
- [[entities/scroll-edge-effect|Scroll edge effect]] (concept): A small blur or gradient mask where content meets floating chrome, used instead of a hard divider.

## Topics

- [[topics/motion-principles|Motion principles]]: Motion should start from the current value, inherit velocity, project momentum and be interruptible; enter and exit along the same path; hint toward the outcome; motion is designed together with visuals.
- [[topics/spring-animation|Spring animation]]: Use springs for anything touchable, described by damping ratio and response; damping 1.0 by default, ~0.8 only after momentum; Apple's values for move (1.0/0.4), rotation (0.8/0.4) and drawer (0.8/0.3); Motion mapping bounce 0 or 0.2 with duration 0.4.
- [[topics/easing-and-timing|Easing and timing]]: Press feedback transitions transform over 100ms ease-out; reversible transitions mirror their easing with inverse cubic-bezier control points; a spring's response is not a duration.
- [[topics/gestures-and-drag|Gestures and drag]]: 1:1 tracking with pointer capture and grab offset, velocity history, velocity handoff, momentum projection with deceleration rate 0.998 or 0.99, rubber-banding with constant 0.55, ~10px hysteresis, parallel gesture detection and commit-or-reverse by velocity sign.
- [[topics/micro-interactions|Micro-interactions]]: Buttons highlight instantly on press with scale(0.97); taps commit on release and can be cancelled by dragging away; feedback is continuous during a gesture.
- [[topics/animation-performance|Animation performance]]: Animate only transform and opacity, use requestAnimationFrame, hint with will-change, keep per-frame change below the perception threshold, and use subtle motion blur or stretch for very fast motion.
- [[topics/reduced-motion|Reduced motion]]: Reduced motion swaps slides, springs and parallax for short opacity cross-fades and drops overshoot while keeping helpful opacity and colour changes; also avoid full-viewport moving backgrounds, ~0.2 Hz loops and abrupt brightness jumps.
- [[topics/accessibility|Accessibility]]: Components respond to prefers-reduced-motion, prefers-reduced-transparency and prefers-contrast: more, respect the user's text size with rem/em spacing, and keep text legible over translucent surfaces.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: Translucent materials convey hierarchy; bigger surfaces get stronger blur and deeper shadow; context-aware shadows; scrims for modal tasks only; scroll edge effects instead of 1px dividers; a bright top border as light catching the material.
- [[topics/typography|Typography]]: Tracking is size-specific (negative for display, e.g. -0.02em; near 0 for body); leading tightens as size grows (1.05 display, 1.5 body); hierarchy from weight, size and leading together; system font by default; font-optical-sizing: auto.
- [[topics/visual-hierarchy|Visual hierarchy]]: Build hierarchy with order, spacing and contrast so the most important thing is the most obvious, and in type with weight, size and leading as a set.
- [[topics/spacing-and-layout|Spacing and layout]]: Proximity implies relationship; place controls near what they affect and mirror what they change; use rem/em spacing so layouts grow with text size.
- [[topics/drawers-and-sheets|Drawers and sheets]]: Sheets use a spring of damping 0.8 and response 0.3; flicks project to a snap point; a grabbed closing sheet follows the finger; stacked sheets progressively dim and push back their parents.
- [[topics/modals-and-popovers|Modals and popovers]]: Popovers and menus originate from their trigger via transform-origin; modal tasks pair the surface with a dimming scrim while non-blocking panels use translucency without a scrim; confirmation dialogs are only for destructive, irreversible actions.
- [[topics/buttons-and-actions|Buttons and actions]]: Buttons respond on pointer-down with an instant scale(0.97) press state and commit on release, with ~10px hit padding.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: Feedback comes in four kinds (status, completion, warning, error); confirm meaningful actions, expose ongoing status, warn before problems; sound and haptics only for meaningful moments.
- [[topics/forms-and-inputs|Forms and inputs]]: Validate inline rather than on submit.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: Every screen answers where am I, where can I go, what's there and how do I get out; nav items get specific names like Progress or Library rather than Home; sidebars use heavier materials.
- [[topics/content-and-microcopy|Content and microcopy]]: Plain language without jargon, fewer steps, and direct, specific labels over safe generic ones.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: Colours should adapt to light and dark, and theme changes between dark and light should be eased to avoid abrupt brightness jumps.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Apple's eight principles; craft means every spacing, timing and alignment value is a deliberate, defensible choice; delight comes from getting the other seven right.
- [[topics/design-process|Design process]]: Prototype interactively, design interaction and visuals together, test with real people in real context and review motion in slow motion.
- [[topics/prototyping|Prototyping]]: An interactive demo is worth a million static designs and sets a concrete bar that prevents a mediocre final build.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Code for press feedback, pointer capture with grab offset, Motion springs, projection and rubber-band functions, a backdrop-filter toolbar, reduced-motion and reduced-transparency media queries, and a display type style.

## Notable Claims

- An interface feels alive when motion starts from the current on-screen value, inherits the user's velocity, projects momentum forward and can be grabbed and reversed at any instant. Evidence: The through-line
- Springs make fluid motion natural because they are inherently interruptible and velocity-aware. Evidence: The through-line
- Apple frames design as serving four human needs: safety/predictability, understanding, achievement and joy. Evidence: The Core Idea
- The moment lag appears, the feeling of directness falls off a cliff. Evidence: 1. Response — kill latency
- Waiting for click or touch-up to show feedback feels dead. Evidence: Respond on pointer-down, not on release
- Snapping a dragged element to its center on grab breaks the illusion immediately. Evidence: 2. Direct manipulation — 1:1 tracking
- Starting an interrupted animation from the logical or target value causes a visible jump. Evidence: Always animate from the presentation (current) value
- CSS transitions and @keyframes cannot be smoothly grabbed and reversed mid-flight, while springs animate from the current value by default. Evidence: Avoid CSS transitions and @keyframes for anything gesture-driven
- Replacing one animation with another at a reversal creates a velocity discontinuity, a brick wall. Evidence: When a gesture reverses, blend velocity
- A single spring on a 2D distance desyncs when X and Y have different velocities. Evidence: Decompose 2D motion into independent X and Y springs
- A pre-scripted fixed-duration animation cannot respond to new input; a spring can, because new input just changes the target. Evidence: 4. Behavior over animation — use springs
- Apple deliberately replaced mass, stiffness and damping with two designer-friendly parameters, damping ratio and response. Evidence: Apple deliberately replaced the physics triplet
- A spring has no fixed duration; its settle time emerges from its parameters. Evidence: This is not "duration"
- Overshoot on a menu that just faded in feels wrong; overshoot on a card you flicked feels right. Evidence: Add bounce (damping ~0.8) only when the gesture itself carried momentum
- Apple ships damping 1.0 / response 0.4 for move or reposition (e.g. PiP), 0.8 / 0.4 for rotation and 0.8 / 0.3 for drawer or sheet. Evidence: Concrete values Apple ships
- Motion's bounce and duration spring API maps closely to Apple's damping and response. Evidence: Web mapping (Motion / Framer Motion)
- Continuing the animation at the finger's exact velocity after release is the detail that most separates fluid from fine. Evidence: 5. Velocity handoff
- Framer Motion and Motion take absolute px/s velocity directly through the velocity option. Evidence: Framer Motion / Motion take absolute px/s velocity directly
- Projecting the resting position from velocity is what makes a flick feel like it throws the element. Evidence: 6. Momentum projection
- Apple ships an exponential-decay projection, not the textbook v²/(2·decel). Evidence: Note: the physics-textbook
- Momentum projection is standard behaviour in good bottom-sheets and carousels such as Vaul and Embla. Evidence: This is the standard behavior in good bottom-sheets and carousels
- Entering from the right and exiting out the bottom feels disconnected and confusing. Evidence: Enter and exit along the same path
- Humans predict a final state from a trajectory. Evidence: 8. Hint in the direction of the gesture
- A hard stop at an edge reads as frozen, while continuous resistance reads as responsive but with nothing more there. Evidence: 9. Rubber-banding — soft boundaries
- Recognizers that only report a final state throw away the continuous tracking needed for feedback. Evidence: Detect all plausible gestures in parallel
- Double-tap detection unavoidably delays single taps. Evidence: Minimize disambiguation delays
- Smoothness is about what is in the frames, not just the frame rate. Evidence: 11. Frame-level smoothness
- For very fast motion, a subtle motion blur or stretch encodes speed and reads better than a hard sharp streak. Evidence: 11. Frame-level smoothness
- Stacking a light translucent surface on another makes legibility collapse. Evidence: Never stack a light translucent surface on another
- Over-feedback trains users to ignore all feedback. Evidence: Utility
- Latency between visual, sound and haptic destroys the illusion. Evidence: Harmony
- Large display text reads with letters too far apart as it grows, so it wants negative tracking; small text wants slightly positive tracking. Evidence: Tracking (letter-spacing) is size-specific
- Weight adds presence without taking more space. Evidence: Emphasize with weight
- The platform system font already ships optical sizing, tracking tables and legibility tuning. Evidence: Default to the platform's system font
- Overusing confirmation dialogs trains people to click through. Evidence: Agency
- Burying everything in one place looks minimal but isn't simple. Evidence: Simplicity — not minimalism
- Jittery scroll, misaligned icons and layouts that break on rotation read as carelessness. Evidence: Craft
- If you need a label to explain a control, the mapping is weak. Evidence: Grouping & mapping
- Specific labels create predictability. Evidence: Direct, specific labels beat safe generic ones
- A working prototype sets a concrete bar that prevents a mediocre final implementation. Evidence: 17. Process
- An interface is fluid when it behaves like the physical world: things respond instantly, move continuously, carry momentum, resist at boundaries and can be redirected mid-motion. Evidence: The Core Idea

## Quotes

> Touch and content should move together.
> The thought and the gesture happen in parallel.
> If something disappears one way, we expect it to emerge from where it came.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is an agent skill file, not an Apple document: it says it distils and translates WWDC talks for the web, so quotes and values attributed to Apple are second-hand and were not checked against the talks here.
- Caveat: The Initial Response section tells the agent what to say when invoked; it is skill behaviour, not design guidance, and was left out of the rules.
- Caveat: The Motion bounce + duration mapping is described as mapping 'closely' to Apple's damping + response, not exactly; library APIs may change between versions.
- Caveat: Many values are approximate in the source (~0.8 damping, ~10px hysteresis, ~300ms tap delay, near 0.2 Hz), and the code snippets use undefined helpers (nearestSnapPoint, animateSpringTo).
- Caveat: The source is pinned to commit 85e8e23 of emilkowalski/skills; later commits may change it.
- Caveat: The toolbar CSS is a light-theme sample (white at 60%); the source gives no dark-theme values.
- Caveat: No media list exists for this source, so no images were reviewed.

### Rules and practices

- **must** (components, all): Respond on pointer-down, not on release: highlight a button the instant it is pressed. Why: Waiting for click or touch-up to show feedback feels dead; response is the foundation everything else is built on. [Respond on pointer-down, not on release]
- **should** (motion, css): Give buttons an instant press state: on :active apply transform: scale(0.97) with transition: transform 100ms ease-out. Why: Feedback lives on the press, and it's instant. Values: scale(0.97), 100ms, ease-out, transition: transform 100ms ease-out. [Feedback lives on the press, and it's instant]
- **must** (patterns, all): Audit every latency on the input path (debounces, artificial timers, transition waits, the ~300ms tap delay) and remove anything that is not essential. Why: The moment lag appears, the feeling of directness falls off a cliff; anything non-essential on the input path is a regression. Values: ~300ms. [Be vigilant about every latency]
- **must** (motion, all): For a drag, slider or drawer, update the UI 1:1 with the pointer the whole way through the interaction; never animate only when the gesture completes. Why: Feedback must be continuous during the interaction, not just at the end. [update the UI 1:1 with the pointer the whole way through]
- **must** (motion, all): Keep a dragged element glued to the finger and preserve the offset from where the user grabbed it; do not snap the element's center to the pointer on grab. Why: Touch and content should move together; snapping to the center breaks the illusion immediately. Values: grabOffset = e.clientY - el.getBoundingClientRect().top. [2. Direct manipulation — 1:1 tracking]
- **should** (tooling, web): Track drags with Pointer Events and call setPointerCapture on pointerdown. Why: Tracking then continues even when the pointer leaves the element's bounds. Values: setPointerCapture(e.pointerId). [so tracking continues even when the pointer leaves the element's bounds]
- **should** (motion, web): Record a short position and timestamp history (the last few pointermove events), not just the current point. Why: You will need velocity at release. [not just the current point — you'll need velocity at release]
- **must** (motion, all): Make every animation interruptible and redirectable at any moment, so a user can grab a moving element mid-flight and reverse it without waiting. Why: Interruptibility is the single most important principle; the thought and the gesture happen in parallel. [3. Interruptibility — the single most important principle]
- **must** (components, all): When a user grabs a closing modal or sheet again, make it follow the finger immediately rather than finishing the close and then reopening. Why: Every animation must be interruptible and redirectable at any moment. [A closing modal the user grabs again should follow the finger]
- **must** (motion, all): Never lock out input during a transition. Why: Users must be able to redirect motion at any instant. [Never lock out input during a transition]
- **must** (motion, all): On interrupt, read the element's live on-screen (presentation) transform and start the new animation from there, never from the target or logical value. Why: Starting from the logical or target value causes a visible jump. [read the element's live on-screen transform and start the new animation from there]
- **should** (motion, css): Do not use CSS transitions or @keyframes for anything gesture-driven; use springs. Why: They cannot be smoothly grabbed and reversed mid-flight, while springs animate from the current value by default. [they can't be smoothly grabbed and reversed mid-flight]
- **must** (motion, web): When a gesture reverses, blend velocity through the re-target instead of hard-cutting to a new animation; choose a spring library that re-targets from the current velocity. Why: Replacing one animation with another at a reversal creates a velocity discontinuity, a brick wall (iOS does this natively with additive animations). [When a gesture reverses, blend velocity — don't hard-cut it]
- **should** (motion, all): Animate 2D motion with two independent springs, one for X and one for Y, not one spring on the 2D distance. Why: A single spring on a 2D distance desyncs when X and Y have different velocities. [Decompose 2D motion into independent X and Y springs]
- **should** (motion, all): Use springs, not pre-scripted fixed-duration animations, for anything a user can touch. Why: A fixed-duration animation cannot respond to new input; with a spring, new input just changes the target and motion stays continuous. [4. Behavior over animation — use springs]
- **should** (tokens, all): Specify springs with two parameters, damping ratio and response, rather than mass, stiffness and damping. Why: Apple deliberately replaced the physics triplet with these two designer-friendly parameters. Values: 1.0 = critically damped, < 1.0 = overshoots and oscillates. [Apple deliberately replaced the physics triplet]
- **should** (tokens, all): Do not treat a spring's response as a duration; its settle time emerges from the parameters. Why: A spring has no fixed duration; response is how quickly the value reaches the target, in seconds. [This is not "duration"]
- **should** (motion, all): Default UI springs to damping 1.0 (critically damped, no overshoot) with response 0.3-0.4. Why: Critically damped motion is graceful and non-distracting; the source calls damping 1.0 everywhere by default a safe house style. Values: damping 1.0, response 0.3–0.4. [(critically damped) — graceful and non-distracting]
- **must** (motion, all): Add bounce (damping ~0.8, response 0.3-0.4) only when the gesture itself carried momentum, such as a flick, a throw or a drag release. Why: Overshoot on a card you flicked feels right. Values: damping ~0.8, response 0.3–0.4. [only when the gesture itself carried momentum]
- **must** (motion, all): Do not overshoot on elements that appear without a gesture, such as a menu that just faded in. Why: Overshoot on a menu that just faded in feels wrong. [Overshoot on a menu that just faded in feels wrong]
- **should** (motion, all): For moving or repositioning an element (e.g. picture-in-picture), use a spring with damping 1.0 and response 0.4. Why: These are the values Apple ships for move/reposition. Values: 1.0, 0.4. [Move / reposition (e.g. PiP)]
- **should** (motion, all): For rotation, use a spring with damping 0.8 and response 0.4. Why: These are the values Apple ships for rotation. Values: 0.8, 0.4. [Rotation | `0.8` | `0.4`]
- **should** (motion, all): For drawers and sheets, use a spring with damping 0.8 and response 0.3. Why: These are the values Apple ships for drawer/sheet. Values: 0.8, 0.3. [Drawer / sheet | `0.8` | `0.3`]
- **should** (motion, web): In Motion / Framer Motion, express the default spring as { type: 'spring', bounce: 0, duration: 0.4 } and a momentum spring as { type: 'spring', bounce: 0.2, duration: 0.4 }. Why: Motion's bounce + duration API maps closely to Apple's damping + response; bounce is reserved for momentum-driven, physical interactions. Values: type: 'spring', bounce: 0, duration: 0.4, type: 'spring', bounce: 0.2, duration: 0.4. [Web mapping (Motion / Framer Motion)]
- **must** (motion, all): When a gesture ends, pass the pointer's release velocity as the spring's initial velocity so the animation continues at the finger's exact speed. Why: There is then no visible seam between dragging and animating; this detail most separates fluid from fine. [5. Velocity handoff — the seam between drag and animation]
- **should** (motion, all): If the spring API wants relative velocity, normalise the release velocity by the remaining distance: relativeVelocity = gestureVelocity / (targetValue − currentValue). Why: Some spring APIs take relative velocity; e.g. at y=50 with target y=150 and the finger moving 50px/s, the initial velocity is 50 / 100 = 0.5. Values: relativeVelocity = gestureVelocity / (targetValue − currentValue), 50 / 100 = 0.5. [normalize it by the remaining distance to the target]
- **should** (motion, web): In Motion / Framer Motion, hand the raw absolute px/s release velocity to the velocity option instead of normalising it. Why: Framer Motion / Motion take absolute px/s velocity directly. Values: velocity. [Framer Motion / Motion take absolute px/s velocity directly]
- **must** (motion, all): Do not snap to the boundary nearest the release point; project the resting position from the release velocity and snap to the target nearest that projected point. Why: This is what makes a flick feel like it throws the element, like scroll deceleration. [6. Momentum projection — animate to where the gesture is going]
- **should** (motion, all): Project momentum with Apple's exponential-decay function: (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate), with decelerationRate ≈ 0.998 for normal scroll feel or 0.99 for snappier, then add it to the current position. Why: It is Apple's exact projection function from the Designing Fluid Interfaces sample code. Values: (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate), decelerationRate ≈ 0.998, 0.99, current + (v/1000)·d/(1−d). [Apple's exact projection function]
- **should** (motion, all): Do not use the physics-textbook projection v²/(2·decel). Why: It is not what Apple ships; use the exponential-decay form. Values: v²/(2·decel). [use the exponential-decay form above]
- **should** (motion, all): Decide whether to reverse or commit a gesture at release by the sign of the velocity, not by the position. Why: Listed in the Quick Reference as the way to decide reverse vs. commit. [Decide reverse vs. commit]
- **must** (motion, all): Make elements enter and exit along the same path: a panel that slides in from the right must dismiss to the right. Why: In-from-right / out-the-bottom feels disconnected and confusing; if something disappears one way, we expect it to emerge from where it came. [Enter and exit along the same path]
- **should** (motion, all): Make menus, popovers and sheets originate from the element that triggered them by setting transform-origin to the trigger, so popovers scale from their trigger, not their center. Why: The spatial relationship between button and content becomes obvious. Values: transform-origin. [Anchor interactions to their source]
- **should** (motion, all): Mirror the easing on reversible transitions using inverse cubic-bézier control points for the two directions. Why: The outbound path then matches the return path. Values: inverse cubic-bézier. [Mirror the easing on reversible transitions]
- **should** (motion, all): Make intermediate frames telegraph where the motion is going, e.g. growing up and out toward the finger, rather than interpolating blindly. Why: Humans predict a final state from a trajectory, as with Control Center modules. [8. Hint in the direction of the gesture]
- **must** (motion, all): At a boundary, rubber-band with progressively increasing resistance instead of stopping hard. Why: A hard stop reads as frozen; continuous resistance reads as responsive but with nothing more there. [9. Rubber-banding — soft boundaries]
- **should** (motion, all): Compute rubber-band displacement as (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot)) with constant = 0.55. Why: The further past the bound, the less the element follows; real things slow before they stop. Values: constant = 0.55, (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot)). [function rubberband]
- **must** (components, all): For taps, highlight on touch-down and commit on touch-up. Why: Feedback is instant on press while the action waits for release. [highlight on touch-*down* (instant), commit on touch-*up*]
- **should** (components, all): Add ~10px of hysteresis or hit padding around tap targets, and let users cancel a tap by dragging away and back. Why: Part of the tap feel checklist. Values: ~10px. [Add ~10px of hysteresis/hit padding]
- **should** (motion, all): For drags and swipes, require a small movement threshold (~10px) before committing to a direction, then track 1:1. Why: Part of the drag/swipe feel checklist. Values: ~10px. [require a small movement threshold (hysteresis, ~10px) before committing to a direction]
- **should** (patterns, all): Detect all plausible gestures in parallel from the first move, then confidently cancel the losers once intent is clear. Why: Recognizers that only report a final state throw away the continuous tracking needed for feedback. [Detect all plausible gestures in parallel from the first move]
- **should** (tooling, web): Do not use gesture recognizers that only report a final state (swipeleft-type events). Why: They throw away the continuous tracking you need for feedback. Values: swipeleft. [Avoid recognizers that only report a final state]
- **should** (patterns, all): Only add double-tap detection where a double-tap action truly exists. Why: Double-tap detection unavoidably delays single taps. [Minimize disambiguation delays]
- **should** (motion, all): Keep the per-frame positional change below the perception threshold. Why: It avoids strobing; smoothness is about what is in the frames, not just frame rate. [11. Frame-level smoothness]
- **consider** (motion, all): For very fast motion, add a subtle motion blur or stretch. Why: It encodes speed and reads better than a hard sharp streak. [encodes speed and reads better than a hard sharp streak]
- **should** (motion, web): Drive frame-by-frame animation with requestAnimationFrame. Why: It is the web's display-synced clock (Apple uses CADisplayLink). Values: requestAnimationFrame. [is the web's display-synced clock]
- **must** (motion, web): Animate only compositor-friendly properties: transform and opacity. Why: Part of frame-level smoothness. Values: transform, opacity. [Animate only compositor-friendly properties]
- **consider** (motion, css): Hint with will-change where motion is imminent. Why: Part of frame-level smoothness. Values: will-change. [where motion is imminent]
- **should** (elevation, web): Build nav bars, toolbars and sheets as translucent layers (backdrop-filter: blur() plus a semi-transparent background) with content scrolling underneath, not opaque bars that consume a fixed strip. Why: Translucent materials act as a floating functional layer that brings structure without stealing focus. Values: backdrop-filter: blur(). [Build nav/toolbars/sheets as translucent layers]
- **should** (elevation, all): Use darker, heavier materials to separate structural regions such as sidebars, and lighter materials to draw attention to interactive elements such as buttons. Why: Material weight encodes hierarchy. [Material weight encodes hierarchy]
- **must** (elevation, all): Never stack a light translucent surface on another. Why: Legibility collapses. [Never stack a light translucent surface on another]
- **should** (elevation, all): Make bigger surfaces read as thicker: give them stronger blur and a deeper shadow than small chips. Why: Bigger surfaces should read as thicker material. [Bigger surfaces should read as thicker]
- **consider** (elevation, all): Use context-aware shadow: heavier over busy or text content for separation, lighter over plain backgrounds. Why: A heavier shadow over busy or text content gives separation. [Consider context-aware shadow]
- **should** (elevation, all): For a modal task, pair the surface with a dimming scrim and push the background back or down. Why: Dim to focus. [Dim to focus, separate to keep flow]
- **should** (elevation, all): For a parallel, non-blocking panel, use translucency and offset without a scrim. Why: Separate to keep flow, so the flow is not broken. [A parallel, non-blocking panel uses translucency and offset without a scrim]
- **should** (elevation, all): For stacked sheets, progressively dim and push back each parent layer. Why: Part of dimming to focus. [For stacked sheets, progressively dim and push back each parent layer]
- **should** (typography, all): Over blurred or translucent surfaces, do not use flat gray text; use higher contrast, a slightly heavier weight and a small letter-spacing bump. Why: Vibrancy keeps text legible over changing backgrounds. [Vibrancy keeps text legible over changing backgrounds]
- **should** (color, all): Put color on a solid layer, not on the translucent foreground. Why: Part of keeping content legible over translucent materials. [Put color on a solid layer, not the translucent foreground]
- **should** (elevation, all): Instead of a 1px border under a sticky header, fade a small blur or gradient mask where content meets floating chrome, and only where floating UI actually overlaps content. Why: Scroll edge effects, not hard dividers. Values: 1px. [Scroll edge effects, not hard dividers]
- **should** (motion, all): For glass or blur surfaces, animate blur radius and scale together on enter and exit rather than a plain opacity fade. Why: The surface reads as a real material arriving. [Materialize, don't just fade]
- **consider** (elevation, css): Style a light translucent toolbar as background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(20px) saturate(180%); border-top: 1px solid rgba(255, 255, 255, 0.4). Why: The bright top edge reads as light catching the material. Values: rgba(255, 255, 255, 0.6), blur(20px) saturate(180%), 1px solid rgba(255, 255, 255, 0.4). [bright top edge = light catching the material]
- **must** (motion, all): Trigger multimodal feedback on the actual causal event (the toggle flipping, the item snapping home) and match its character to the physicality of the action. Why: Causality: it must be obvious what caused the feedback. [it must be obvious what caused the feedback]
- **must** (motion, all): Fire the visual, the sound and the haptic on the same frame; do not let a CSS transition lag the audio or Vibration API haptic. Why: Harmony: latency between them destroys the illusion. [Latency between them destroys the illusion]
- **must** (patterns, all): Reserve haptics and sound for meaningful moments (success, error, commit, snap). Why: Utility: over-feedback trains users to ignore all of it. Values: success, error, commit, snap. [add feedback only where it earns its place]
- **must** (accessibility, all): Treat reduced motion as a gentler, non-vestibular equivalent, not as removing feedback. Why: Reduced motion doesn't mean no feedback. [14. Reduced motion & accessibility]
- **must** (accessibility, web): Respond to three independent signals and bake them into your components: prefers-reduced-motion, prefers-reduced-transparency and prefers-contrast. Why: Reduced motion doesn't mean no feedback; it means a gentler, non-vestibular equivalent, and each signal needs its own treatment. Values: prefers-reduced-motion: reduce, prefers-reduced-transparency: reduce, prefers-contrast: more. [Respond to three independent signals]
- **must** (accessibility, web): Under prefers-reduced-motion: reduce, replace slides, springs and parallax with short opacity cross-fades or static transitions, drop elastic and overshoot, and keep opacity and colour changes that aid comprehension. Why: It gives a gentler, non-vestibular equivalent. Values: .sheet { transition: opacity 200ms ease; transform: none !important; }, 200ms. [prefers-reduced-motion: reduce]
- **must** (accessibility, web): Under prefers-reduced-transparency: reduce, make translucent surfaces frostier or solid: raise background opacity and drop the blur. Why: It is one of the three independent signals the source says to bake into components. Values: .toolbar { background: white; backdrop-filter: none; }. [prefers-reduced-transparency: reduce]
- **must** (accessibility, web): Under prefers-contrast: more, use near-solid backgrounds with a defined, contrasting border. Why: It is one of the three independent signals the source says to bake into components. Values: prefers-contrast: more. [prefers-contrast: more]
- **should** (accessibility, all): Avoid full-viewport moving backgrounds. Why: Listed among motion to avoid for accessibility. [avoid full-viewport moving backgrounds]
- **should** (accessibility, all): Avoid slow looping oscillations near 0.2 Hz (one cycle per 5s). Why: Listed among motion to avoid for accessibility. Values: 0.2 Hz, one cycle per 5s. [slow looping oscillations (near 0.2 Hz / one cycle per 5s)]
- **should** (accessibility, all): Avoid abrupt brightness jumps; ease theme changes between dark and light. Why: Listed among changes to avoid for accessibility. [abrupt brightness jumps (ease dark↔light theme changes)]
- **should** (accessibility, all): Make large moving objects semi-transparent while they travel. Why: Part of the reduced-motion and accessibility guidance. [Make large moving objects semi-transparent while they travel]
- **should** (accessibility, all): During a large reposition, fade big surfaces out and fade them back in once settled. Why: Part of the reduced-motion and accessibility guidance. [fade big surfaces out during a large reposition]
- **must** (typography, all): Make tracking (letter-spacing) size-specific; never use one letter-spacing value for all sizes. Why: A fixed letter-spacing is wrong somewhere. [Tracking (letter-spacing) is size-specific — never one value for all sizes]
- **should** (typography, all): Give large display text negative tracking (e.g. letter-spacing: -0.02em) and small text slightly positive tracking; leave body text near 0. Why: Letters read too far apart as text grows; small text needs slightly positive tracking for legibility. Values: -0.02em, near 0. [letters read too far apart as they grow]
- **should** (typography, all): Set leading (line-height) inversely to size: tight on large headings (e.g. 1.05 for display), looser on body copy (e.g. 1.5). Why: Leading tracks size inversely. Values: line-height: 1.05, 100%/1.5. [Leading (line-height) tracks size inversely]
- **should** (typography, all): Increase line-height for scripts with tall ascenders and descenders. Why: Part of the leading guidance. [Increase it for scripts with tall ascenders/descenders]
- **should** (typography, all): Tighten line-height for dense, information-heavy UI. Why: Part of the leading guidance. [tighten it for dense, information-heavy UI]
- **should** (typography, all): Build type hierarchy from weight, size and leading as a set, not from size alone, and emphasise with weight. Why: Weight adds presence without taking more space. [Build hierarchy from weight + size + leading as a set]
- **must** (typography, all): Respect the user's text-size setting (Dynamic Type): scale layout with the text by using rem/em for spacing, not fixed px. Why: A larger font then does not break the layout. Values: rem, em. [Respect the user's text-size setting (Dynamic Type)]
- **should** (typography, all): Default to the platform's system font (e.g. font: 100%/1.5 system-ui, sans-serif) before a custom face; override only with a reason. Why: The system font already ships optical sizing, tracking tables and legibility tuning. Values: font: 100%/1.5 system-ui, sans-serif. [Default to the platform's system font]
- **consider** (typography, css): Style display text with fluid size, tight leading, negative tracking and optical sizing, e.g. font-size: clamp(2rem, 5vw, 4rem); line-height: 1.05; letter-spacing: -0.02em; font-optical-sizing: auto. Why: Apple designs type to change shape with size; the same discipline applies on the web. Values: clamp(2rem, 5vw, 4rem), line-height: 1.05, letter-spacing: -0.02em, font-optical-sizing: auto. [font-optical-sizing: auto]
- **should** (process, all): Decide what not to build; spend the user's time, attention and trust only on features that pay off. Why: Purpose: every feature asks for the user's time, attention and trust. [Every feature asks for the user's time, attention, and trust]
- **should** (patterns, all): Keep people in control by offering choices instead of forcing a single path. Why: Agency. [Keep people in control: offer choices, don't force a single path]
- **must** (patterns, all): Provide easy undo for slips, and use a confirmation dialog only for genuinely destructive, irreversible actions, sparingly. Why: Forgiveness backs agency; overusing confirmations trains people to click through. [easy undo for slips, a confirmation dialog only for genuinely destructive, irreversible actions]
- **should** (patterns, all): Ask for private data at the right moment, only for what is needed, and transparently. Why: Responsibility: act in the user's interest. [Privacy: ask at the right moment, only for what's needed, transparently]
- **should** (process, all): Anticipate misuse and harm, especially with AI features: add previews, confirmations and disclaimers, and cut a feature whose risk outweighs its value. Why: Responsibility: e.g. an allergy-aware recipe app must not suggest a harmful ingredient. [Safety: anticipate misuse and harm]
- **should** (patterns, all): Use metaphors that are neither too literal nor too abstract (a trash can means delete) and honour their physics. Why: Familiarity: build on what people already know. [Use metaphors that are neither too literal nor too abstract]
- **must** (patterns, all): Keep things that look the same behaving the same and living in the same place (e.g. close is always top-left on macOS). Why: People can then predict what happens next. [Be consistent: things that look the same must behave the same]
- **should** (process, all): Only break a familiar pattern if you can prove the new one is better, and test it rather than assume. Why: Familiarity. [Only break a familiar pattern if you can prove it's better]
- **should** (platforms, all): Adapt to the platform and situation: quick touch on iPhone, deep workflows with precise pointer control on desktop. Why: Flexibility: design for different contexts, devices and abilities. [desktop = deep workflows with precise pointer control]
- **should** (accessibility, all): Design inclusively for age, language, expertise and accessibility. Why: Flexibility: the full range of abilities. [Design inclusively (age, language, expertise, accessibility)]
- **consider** (patterns, all): When no single layout fits everyone, let people personalise: rearrange controls and hide what they do not use. Why: Flexibility. [let people personalize]
- **should** (layout, all): Do not bury everything in one place to look minimal; strip the unnecessary so the core purpose shines. Why: Simplicity is not minimalism; burying everything looks minimal but isn't simple. [Simplicity — not minimalism]
- **should** (content, all): Be concise: plain language, no jargon, fewer steps. Why: Simplicity. [Be concise (plain language, no jargon, fewer steps)]
- **should** (layout, all): Use hierarchy (order, spacing, contrast) so the most important thing is the most obvious. Why: Simplicity: be clear. [clear (use hierarchy — order, spacing, contrast)]
- **should** (content, all): Make every element earn its place, and add context where it simplifies (e.g. a video scrubber that shows time remaining). Why: Sometimes adding context simplifies. [Every element earns its place]
- **should** (patterns, all): Show the common path first and put advanced options one level deeper. Why: Simplicity. [Show the common path first, advanced options one level deeper]
- **must** (tokens, all): Make every spacing, timing and alignment value a deliberate choice you can defend; nothing is random. Why: Craft: uncompromising attention to detail builds trust. [Nothing is random]
- **should** (color, all): Use colours that adapt to light and dark, clear iconography and responsive animations that give immediate, natural feedback. Why: Craft: uncompromising attention to detail builds trust. [colors that adapt to light/dark, clear iconography]
- **must** (layout, all): Do not ship jittery scroll, misaligned icons or layouts that break on rotation. Why: They read as carelessness. [Jittery scroll, misaligned icons, and layouts that break on rotation read as carelessness]
- **should** (process, all): Keep evolving the design as features and hardware change. Why: Craft needs iteration and longevity. [Craft needs iteration and longevity]
- **should** (process, all): Decide the emotion you want people to feel (calm, confident, excited) and reinforce it in every decision, instead of tacking delight on top. Why: Delight is the result of getting the other seven principles right, not confetti. Values: calm, confident, excited. [Decide the emotion you want people to feel]
- **should** (patterns, all): Cover the four kinds of feedback (status, completion, warning, error): confirm meaningful actions, expose ongoing status and warn before problems. Why: Feedback comes in four kinds: status, completion, warning, error. Values: status, completion, warning, error. [Feedback comes in four kinds]
- **should** (components, all): Validate form input inline, not on submit. Why: Listed as a tactical feedback rule. [validate inline (not on submit)]
- **must** (patterns, all): Make every screen answer: Where am I? Where can I go? What's there? How do I get out? Never trap the user. Why: Wayfinding. [Every screen should answer: Where am I?]
- **should** (layout, all): Place a control near what it affects and arrange controls to mirror what they change. Why: Proximity implies relationship; if you need a label to explain a control, the mapping is weak. [Grouping & mapping]
- **should** (content, all): Name navigation items for their contents (e.g. "Progress", "Library"), not with vague umbrellas like "Home". Why: Direct, specific labels create predictability. Values: Progress, Library, Home. [Direct, specific labels beat safe generic ones]
- **should** (process, all): Prototype interactively rather than relying on static designs. Why: You discover the interface by building and playing with it, and a working prototype sets a concrete bar that prevents a mediocre final implementation. [Prototype interactively]
- **should** (process, all): Design interaction and visuals together; do not add motion as a layer after the pixels. Why: You shouldn't be able to tell where one ends and the other begins. [Design interaction and visuals together]
- **should** (process, all): Test with real people in real context. Why: Part of the process guidance. [Test with real people in real context]
- **should** (process, all): Review motion with fresh eyes by playing it in slow motion or frame by frame. Why: It catches what is invisible at full speed. [play it in slow motion / frame-by-frame]
- **should** (process, all): Reason with Apple's eight principles by name (purpose, agency, responsibility, familiarity, flexibility, simplicity, craft, delight) when making and defending design decisions. Why: The motion and craft guidance serves these eight principles; the source says to use them as the names you reason with. [Use these as the names you reason with]

### Decisions it informs

- Should touchable UI animate with fixed-duration transitions or with springs? (`Q-motion-01`)
  - Fixed-duration animations (CSS transitions, @keyframes): Pre-scripted motion that cannot respond to new input or be smoothly grabbed and reversed mid-flight. When: The source does not recommend it for anything gesture-driven.
  - Springs: New input just changes the target and motion stays continuous; they animate from the current value and carry velocity. When: Anything a user can touch.
  - Recommendation: Springs for anything a user can touch, because they are interruptible and velocity-aware.
- How should spring settings be expressed? (`Q-motion-04`)
  - Mass, stiffness and damping: The physics triplet that Apple deliberately replaced. When: Not recommended by the source.
  - Damping ratio and response: Damping controls overshoot (1.0 no bounce, lower bouncier); response in seconds controls snappiness; settle time emerges rather than being a set duration. When: Default; on the web, Motion's bounce + duration maps closely.
  - Recommendation: Think in damping ratio and response, designer-friendly parameters Apple adopted.
- How much bounce should springs have?
  - Critically damped (damping 1.0, bounce 0): Smooth settle with no overshoot; graceful and non-distracting. When: Most UI, by default.
  - Under-damped (damping ~0.8, bounce 0.2): Slight overshoot that feels like physical momentum. When: Only after a gesture that carried momentum: a flick, throw or drag release.
  - Recommendation: damping 1.0 everywhere by default; reserve bounce for momentum-driven, physical interactions.
- Where should a flicked element land on release?
  - Nearest boundary from the release point: Ignores the flick's speed, so a throw does not feel like a throw. When: Not recommended.
  - Nearest snap point to the momentum-projected endpoint: Uses velocity to predict the resting point like scroll deceleration, so a flick throws the element. When: Bottom sheets and carousels (the source names Vaul and Embla); any flickable element [inferred].
  - Recommendation: Project with Apple's exponential-decay function (decelerationRate ≈ 0.998, or 0.99 for snappier) and snap to the point nearest the projection, then hand off velocity.
- At release, how do you decide whether a gesture commits or reverses?
  - By position: Decides from where the element is at release. When: Not recommended by the source.
  - By the sign of the velocity: Decides from the direction the finger was moving at release. When: Default.
  - Recommendation: Use velocity sign, not position.
- Should bars, toolbars and sheets be opaque or translucent? (`Q-depth-04`)
  - Opaque bars: Consume a fixed strip of the screen. When: The source does not recommend them for chrome; also the fallback under reduced transparency.
  - Translucent layers (backdrop-filter blur + semi-transparent background): A floating functional layer with content scrolling underneath that brings structure without stealing focus. When: Nav, toolbars and sheets by default.
  - Recommendation: Translucent layers, with heavier materials for structure and lighter ones for interactive elements, never light on light.
- Should a secondary panel dim the content behind it?
  - Dimming scrim and push the background back or down: Focuses the user on a modal task. When: Modal tasks; stacked sheets progressively dim and push back each parent.
  - Translucency and offset without a scrim: Separates the panel while keeping the flow unbroken. When: Parallel, non-blocking panels.
  - Recommendation: Dim to focus, separate to keep flow.
- How should a sticky header be separated from scrolling content?
  - 1px border: A hard divider line under the header. When: Not recommended by the source.
  - Scroll edge effect: A small blur or gradient mask fades where content meets floating chrome, only where it overlaps content. When: Default for floating chrome.
  - Recommendation: Scroll edge effects, not hard dividers.
- When people turn on reduced motion, what should happen? (`Q-motion-07`)
  - Replace with gentler equivalents: Slides, springs and parallax become short opacity cross-fades or static transitions; overshoot is dropped; helpful opacity and colour changes stay. When: Default.
  - Remove all feedback: No motion or feedback at all. When: The source says reduced motion does not mean no feedback.
  - Recommendation: Replace with a gentler, non-vestibular equivalent such as a 200ms opacity cross-fade.
- Which user settings should components respond to? (`Q-motion-10`)
  - prefers-reduced-motion: reduce: Cross-fades instead of slides and springs. When: Always.
  - prefers-reduced-transparency: reduce: Frostier or solid surfaces with higher background opacity and no blur. When: Always.
  - prefers-contrast: more: Near-solid backgrounds with a defined, contrasting border. When: Always.
  - Text size (Dynamic Type): Layout scales with the text through rem/em spacing. When: Always.
  - Recommendation: All of them, baked into components.
- Should letter spacing be one value or change with text size? (`Q-type-13`)
  - One fixed letter-spacing: Wrong somewhere: too loose on large text or too tight on small text. When: Never, per the source.
  - Size-specific tracking: Negative on large display text (e.g. -0.02em), near 0 for body, slightly positive for small text. When: Default.
  - Recommendation: Size-specific tracking: tighten headings, leave body near 0.
- Should the UI use the system font or a custom typeface? (`Q-type-01`)
  - Platform system font (system-ui): Ships with optical sizing, tracking tables and legibility tuning. When: Default.
  - Custom typeface: A brand face that needs its own tuning [inferred]. When: Only with a reason.
  - Recommendation: Default to the system font; override only with a reason.
- Should layouts grow when people turn up their text size? (`Q-type-17`)
  - Scale layout with text (rem/em spacing): A larger font does not break the layout. When: Default.
  - Fixed px spacing: Larger text can break the layout. When: Not recommended by the source.
  - Recommendation: Respect the user's text-size setting and scale layout with it.
- How should people recover from mistakes and destructive actions? (`Q-form-05`)
  - Easy undo: Slips can be reversed without interruption. When: Slips and reversible actions.
  - Confirmation dialog: An extra step before acting; overuse trains people to click through. When: Only genuinely destructive, irreversible actions, sparingly.
  - Recommendation: Both, each in its place: undo for slips, confirmation only for destructive, irreversible actions.
- How much sound and haptic feedback should the product use? (`Q-motion-08`)
  - Feedback on many interactions: Over-feedback trains users to ignore all of it. When: Not recommended.
  - Only meaningful moments: Sound and haptics on success, error, commit and snap, fired on the same frame as the visual. When: Default.
  - Recommendation: Reserve haptics and sound for meaningful moments.
- When should form input be validated? (`Q-form-02`)
  - Inline: Problems are shown as people type or leave a field [inferred]. When: Default.
  - On submit: Problems appear only after submitting. When: Not recommended by the source.
  - Recommendation: Validate inline, not on submit.
- How should navigation items be labelled?
  - Specific labels ("Progress", "Library"): Creates predictability about what is behind each item. When: Default.
  - Generic umbrellas ("Home"): Safe but vague. When: Not recommended by the source.
  - Recommendation: Direct, specific labels beat safe generic ones.

### Process

1. Respond on press: Show feedback on pointer-down (e.g. scale(0.97) over 100ms ease-out), commit on release, and remove debounces, artificial timers and the ~300ms tap delay from the input path.
2. Capture and track: On pointerdown call setPointerCapture, record the grab offset, and keep a short history of positions and timestamps from pointermove.
3. Disambiguate quickly: Wait for ~10px of movement before committing to a direction, detect plausible gestures in parallel from the first move, cancel the losers once intent is clear, and only delay taps where double-tap exists.
4. Follow 1:1 and rubber-band: Update the element with the pointer every frame via transform, and past a boundary apply the rubber-band formula with constant 0.55.
5. Decide at release: Compute release velocity from the history, decide commit or reverse by the velocity's sign, project the resting point with (v/1000)·d/(1−d) using d ≈ 0.998 (or 0.99), and pick the nearest snap point to that projection.
6. Hand off to a spring: Animate to the target with a spring given the release velocity (normalised by remaining distance if the API wants relative velocity); damping 1.0 by default, ~0.8 only after momentum; use separate X and Y springs for 2D.
7. Stay interruptible: Never lock input; on a new grab read the live on-screen transform and re-target from there, carrying velocity through reversals.
8. Keep space consistent: Exit along the entry path, set transform-origin to the trigger, mirror easing for reversible transitions, and let intermediate frames point at the outcome.
9. Add multimodal feedback carefully: Fire sound or haptics on the causal event, on the same frame as the visual, and only for success, error, commit or snap.
10. Bake in accessibility variants: Add prefers-reduced-motion (cross-fades, no overshoot), prefers-reduced-transparency (solid, no blur) and prefers-contrast: more (near-solid with a contrasting border) styles to each component.
11. Prototype and review: Build an interactive prototype, design interaction and visuals together, test with real people in real context, and review motion in slow motion or frame by frame.

### Examples and visual references

- Button press state: CSS sample: .button:active { transform: scale(0.97); transition: transform 100ms ease-out; } shows instant feedback on press.
- Apple's shipped spring values (Apple platforms): Table: move/reposition such as picture-in-picture uses damping 1.0 / response 0.4, rotation 0.8 / 0.4, drawer or sheet 0.8 / 0.3.
- Motion spring calls (Motion (web)): animate(el, { y: 0 }, { type: 'spring', bounce: 0, duration: 0.4 }) for the no-overshoot default, and bounce: 0.2 for a flick-driven move.
- Relative velocity worked example: An element at y=50 heading to y=150 with the finger at 50px/s gets an initial relative spring velocity of 50 / 100 = 0.5.
- Momentum projection in bottom sheets and carousels (Vaul, Embla): Named as good implementations that project a flick's resting point before snapping.
- Control Center modules (iOS Control Center): Modules grow up and out toward the finger, so intermediate frames hint at the final state.
- Additive animations (iOS): iOS natively carries velocity through a re-targeted animation, avoiding the brick wall at a reversal.
- Translucent toolbar: CSS sample: 60% white background, blur(20px) saturate(180%), and a 1px rgba(255, 255, 255, 0.4) top border as light catching the material.
- Reduced motion and reduced transparency overrides: CSS sample: the sheet becomes a 200ms opacity transition with transform: none; the toolbar becomes solid white with no backdrop-filter.
- Display type style: CSS sample: body at 100%/1.5 system-ui; display at clamp(2rem, 5vw, 4rem), line-height 1.05, letter-spacing -0.02em, font-optical-sizing: auto.
- Trash can metaphor: A metaphor neither too literal nor too abstract: a trash can means delete.
- Close button placement (macOS): Close is always top-left on macOS, an example of things that look the same living in the same place.
- Allergy-aware recipe app: An AI feature that must not suggest a harmful ingredient, illustrating responsibility and anticipating harm.
- Video scrubber with time remaining: Adding context that simplifies rather than clutters.
- Specific navigation labels: "Progress" and "Library" instead of a vague "Home".

### Numbers

- scale(0.97): Button press transform [.button:active code sample]
- 100ms ease-out: Press feedback transition [.button:active code sample]
- ~300ms: Tap delay to audit and remove from the input path [Be vigilant about every latency]
- 1.0: Damping ratio for critically damped, no-bounce springs; the default for most UI [Damping ratio]
- ~0.8: Damping ratio for bounce, only after momentum [Defaults]
- 1.0: Damping Apple ships for move / reposition (e.g. PiP), paired with response 0.4 [Move / reposition (e.g. PiP)]
- 0.4: Response (seconds) Apple ships for move / reposition (e.g. PiP) and for rotation [Concrete values Apple ships]
- 0.8: Damping Apple ships for rotation (response 0.4) and for drawer / sheet (response 0.3) [Concrete values Apple ships]
- 0.3: Response (seconds) Apple ships for drawer / sheet, paired with damping 0.8 [Drawer / sheet]
- 0.3–0.4: Response range for both default and momentum springs [Quick Reference]
- bounce: 0, duration: 0.4: Motion default spring (critically damped) [Web mapping code sample]
- bounce: 0.2, duration: 0.4: Motion momentum spring [Web mapping code sample]
- 50 / 100 = 0.5: Relative velocity for an element at y=50, target y=150, finger at 50px/s [5. Velocity handoff]
- 0.998: Deceleration rate for normal scroll feel in the projection function [6. Momentum projection]
- 0.99: Deceleration rate for a snappier projection [6. Momentum projection]
- 1000: Divisor converting px/s velocity in the projection function [function project]
- 0.55: Default rubber-band constant [function rubberband]
- ~10px: Hysteresis or hit padding for taps, and movement threshold before a drag commits to a direction [10. Gesture design details]
- 0.2 Hz / one cycle per 5s: Slow looping oscillation rate to avoid [14. Reduced motion & accessibility]
- 200ms: Opacity cross-fade under reduced motion [@media (prefers-reduced-motion: reduce) code sample]
- rgba(255, 255, 255, 0.6): Translucent toolbar background [.toolbar code sample]
- blur(20px) saturate(180%): Toolbar backdrop-filter [.toolbar code sample]
- 1px solid rgba(255, 255, 255, 0.4): Bright top border on the toolbar [.toolbar code sample]
- 100%/1.5: Body font size and line-height with system-ui [:root code sample]
- clamp(2rem, 5vw, 4rem): Display font size [.display code sample]
- 1.05: Display line-height [.display code sample]
- -0.02em: Display letter-spacing [.display code sample]
- four: Human needs design serves: safety/predictability, understanding, achievement, joy [The Core Idea]
- eight: Apple design principles from Principles of Great Design (WWDC 2026) [16. Design foundations]
- four: Kinds of feedback: status, completion, warning, error [Feedback comes in four kinds]

<!-- /od:learn -->
