---
type: synthesis
title: Drawers and sheets
created: 2026-09-24
updated: 2026-09-24
sources:
  - 14h1VnkQvIc
  - Gfsd8NNuD9g
  - PDcQJOPby1k
  - adev-home
  - ek-agents-with-taste
  - ek-building-a-drawer-component
  - eks-skills-animate-expo-recipes
  - eks-skills-animate-expo-skill
  - eks-skills-animate-recipes
  - eks-skills-apple-design-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-audit
  - eks-skills-mobile-native-skill
  - eks-skills-pick-ui-library-skill
  - eks-skills-review-animations-standards
  - vaul-api
  - vaul-default
  - vaul-getting-started
  - vaul-inputs
  - vaul-other
  - vaul-snap-points
tags:
  - od-area-components
---
# Drawers and sheets

## In short

A drawer, also called a bottom sheet, is a panel that slides in from the edge of the screen for a side task, so people keep their place in what they were doing. On phones the house standard prefers a drawer over a centered modal. On the web a drawer opens and closes over 500ms on an iOS-like curve, `cubic-bezier(0.32, 0.72, 0, 1)`; once a finger drags it, it settles with a spring instead. People can close a drawer by dragging it down, and a quick flick is enough. Build drawers on an accessible dialog primitive; the Vaul library shows how, but it is unmaintained, so treat it as a guide rather than a dependency.

## House standards

Most of these are locked. Four come only from the Vaul docs, a good-to-have source, so they are recommended defaults that people can change: `STD-components-toasts-drawers-39`, `STD-enter-exit-origin-40`, `STD-springs-gestures-24` and `STD-accessibility-motion-25`.

**When and how to build one**
- `STD-components-toasts-drawers-37` (should): Prefer drawers over modals on mobile.
- `STD-components-toasts-drawers-38` (should): Build drawers on an accessible dialog.
- `STD-components-toasts-drawers-39` (should): Drawer defaults: modal, bottom, dismissible.
- `STD-accessibility-motion-16` (must): Build overlays on accessible primitives.
- `STD-accessibility-motion-24` (must): Never trap the user in an overlay.
- `STD-accessibility-motion-25` (should): Controlled drawers still react to Escape.
- `STD-accessibility-motion-26` (should): Cover the inert page behind a drawer.
- `STD-visual-details-20` (should): Scrim for modal tasks only.
- `STD-components-toasts-drawers-59` (must): React Native: native sheet presentations.
- `STD-components-toasts-drawers-60` (must): React Native: form sheets on both platforms.
- `STD-mobile-touch-41` (must): Use native pieces instead of JS rebuilds.

**Motion**
- `STD-components-toasts-drawers-40` (must): Drawer curve: cubic-bezier(0.32, 0.72, 0, 1).
- `STD-enter-exit-origin-41` (should): Drawers: 500ms on the drawer curve. This 500ms is a named exception to the 300ms ceiling in `STD-easing-duration-06`.
- `STD-enter-exit-origin-21` (should): Slide by percentages, not pixels.
- `STD-enter-exit-origin-06` (must): Exit the way it entered.
- `STD-enter-exit-origin-40` (should): Vaul: --initial-transform off the edge.
- `STD-easing-duration-07` (must): Duration budget for each element.
- `STD-easing-duration-19` (should): Companion values follow the drawer curve.
- `STD-when-to-animate-08` (should): Standard motion for occasional surfaces.
- `STD-springs-gestures-01` (must): Springs for anything a finger drives.
- `STD-springs-gestures-08` (must): Sheet and drawer spring values.

**Drag, flick and snap**
- `STD-springs-gestures-12` (must): Every animation can be grabbed mid-flight.
- `STD-springs-gestures-14` (must): Start from the on-screen value.
- `STD-springs-gestures-21` (must): A flick is enough to dismiss.
- `STD-springs-gestures-22` (must): Sheets dismiss on projected position.
- `STD-springs-gestures-24` (should): Sequential snap points when all matter.
- `STD-springs-gestures-25` (must): Rubber-band at edges, never hard-stop.
- `STD-springs-gestures-28` (must): Capture the pointer during a drag.
- `STD-performance-properties-11` (must): Set drag transforms on the moving element.
- `STD-mobile-touch-28` (must): Ignore extra fingers during a drag.
- `STD-components-toasts-drawers-44` (should): Drag a drawer only from its scroll top.

**Keyboard, viewport and device**
- `STD-components-toasts-drawers-45` (should): Keep drawer inputs above the keyboard.
- `STD-components-toasts-drawers-48` (should): Fixed-pixel snap points for inputs.
- `STD-components-toasts-drawers-65` (should): Safari theme bar must match the overlay.
- `STD-mobile-touch-10` (must): Size full-height layouts with dvh and svh.
- `STD-mobile-touch-14` (must): Contain overscroll in app layouts.
- `STD-mobile-touch-16` (must): Paint edge to edge, pad the safe areas.
- `STD-mobile-touch-18` (must): Set touch-action per gesture surface.
- `STD-process-review-taste-33` (must): Judge feel on real hardware.

## What the sources teach

### When a sheet beats a new page or a modal

- Use a bottom sheet for a side task that should not pull people away, such as picking a template while editing a note; use a new page for something new that does not depend on the current screen. The template sheet has a title, a search bar, a check to confirm and an X to close [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]).
- On mobile, Emil Kowalski presents content in a drawer rather than a modal because it feels more native. He frames this as his preference, and the article offers no measurement [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).
- In React Native, a sheet that is its own destination uses `presentation: 'formSheet'` (a short interruption such as a picker, filter or share); a custom drag-to-dismiss sheet is only for a sheet that must live inside an existing screen; a self-contained task with its own navigation uses `presentation: 'modal'` [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]) [S-L19-016] ([[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]).
- Vaul's variants cover a bottom drawer (the default), side drawers (`direction` right or left), nested drawers, a scrollable drawer that behaves like Apple's Sheet, and a drawer opened from code [S-L19-094] ([[sources/vaul-default-default-vaul|Default – Vaul]]). `modal={false}` keeps the page behind usable; `dismissible={false}` blocks outside click, Escape and drag [S-L19-097] ([[sources/vaul-other-other-vaul|Other – Vaul]]).
- Drawers are occasional UI, so they get standard animation, not delight [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]) [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]) [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]) [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]).

### Anatomy and defaults

- Vaul is built on Radix's Dialog primitive, which makes it accessible and handles focus, and it copies Radix's compound API so it feels familiar [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).
- The parts are Root, Trigger, Portal, Overlay, Content, Handle, Title, Description and Close. Root defaults to modal, bottom, dismissible, draggable from anywhere (`handleOnly: false`), repositioning for inputs, and portalled into `document.body`. The Overlay covers the inert page, and Title and Description are announced when the drawer opens [S-L19-093] ([[sources/vaul-api-api-reference-vaul|API Reference – Vaul]]).
- The starter example styles the overlay as a fixed full-screen black layer at 40% (`bg-black/40`) and pins the content to the bottom edge at its own height [S-L19-095] ([[sources/vaul-getting-started-getting-started-vaul|Getting Started – Vaul]]).
- A drawer controlled with `open` also needs `onOpenChange` so it still reacts to Escape and outside clicks [S-L19-094] ([[sources/vaul-default-default-vaul|Default – Vaul]]). A non-dismissible drawer needs an explicit close control: the docs' demo can only be closed by refreshing the page [S-L19-097] ([[sources/vaul-other-other-vaul|Other – Vaul]]).
- Drawers do not all have to look alike; the Family app's drawer was recreated with Vaul to prove it [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]). The course credits that walkthrough's visual components to Family and marks them for educational purposes only [S-L19-002] ([[sources/adev-home-animations-dev|animations.dev]]), so its look is not something to copy [inferred].

### Motion

- On the web, hide the drawer at `translateY(100%)` and transition `transform` over 500ms with `cubic-bezier(0.32, 0.72, 0, 1)`, a curve from the Ionic Framework that closely matches iOS; 500ms mimics the iOS Sheet [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]) [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]). The skills store this curve once as the `--ease-drawer` token [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]) [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]) [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]) [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).
- Modals and drawers sit in a 200-500ms duration band [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).
- When a finger drives the sheet, use a spring: Apple ships damping 0.8 with a 0.3s response for sheets [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]), which Reanimated writes as `{ duration: 300, dampingRatio: 0.8, velocity }` [S-L19-016] ([[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]).
- A dismissable sheet leaves by the same edge it came in from [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]), and a percentage translate moves it by its own height whatever its content [S-L19-016] ([[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]).
- Kole Jain treats the easing curve as the product's tone: snappy and performant, fun and springy, or slow and smooth [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]).

### Drag, flick and snap

- Dismissal is momentum-based: a flick closes the drawer without dragging it past a set point [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]). The skills put the flick at a velocity above about 0.11 [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]). The React Native recipe projects where the sheet would land and dismisses when that passes 40% of its height; dismissal uses a critically damped, clamped spring, and snapping back uses damping 0.8 plus a light haptic [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]).
- Dragging up past the top meets growing resistance instead of a hard stop [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]) [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]).
- For smooth dragging, write the offset straight onto the moving element as `transform: translateY(...)`. Driving it through an inherited CSS variable made Vaul lag once the content passed about 20 list items [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).
- A scrollable drawer can be dragged only when its content is scrolled to the top, and dragging stays blocked for 100ms after reaching the top so a fast scroll does not throw the drawer closed. Every touch after the first is ignored until release, so a second finger cannot make the drawer jump [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).
- A grabbed closing sheet follows the finger at once, keeping the offset where it was grabbed. On release, project the resting point from the velocity (Apple's decay rate of about 0.998, or 0.99 for snappier) and snap to the nearest point [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Snap points let a drawer rest part-open, as in Apple Maps. On release it snaps to the closest point, and a hard flick can skip points or close it. Points can be a fraction of the viewport or a fixed pixel value; use pixels when an input must peek out by the same amount on every device [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]). When every point matters equally, `snapToSequentialPoint` turns off velocity skipping; `fadeFromIndex` sets the snap point from which the drawer starts fading (the docs do not say exactly what fades) [S-L19-098] ([[sources/vaul-snap-points-snap-points-vaul|Snap Points – Vaul]]).
- React Native form sheets: Android caps detents at three, `sheetGrabberVisible` shows nothing on Android, content stays a single screen, `fitToContents` needs explicitly sized content. The custom drag-to-dismiss sheet's pan waits for 10 points of vertical movement before committing, so a horizontal swipe can win [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]).
- On the mobile web, a drag-to-dismiss sheet owns every axis (`touch-action: none`) and a vertical sheet handle uses `touch-action: pan-x` [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).

### The page behind the drawer

- Vaul's opt-in `scaleBackground` makes the page look like another sheet by scaling it and rounding its corners; while dragging, the values follow drag progress (dragging down 40% sets the radius to 60% of its maximum) [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).
- Kole Jain zooms the background out as a sheet rises and back in when it is swiped down [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]), and moves it down as well for pop-ups from the bottom [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]).
- A modal task gets a dimming scrim and pushes the background back; stacked sheets progressively dim and push back each parent; a parallel, non-blocking panel gets no scrim [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- In React Native the backdrop's opacity is derived from the sheet's own position, so the two always move together [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]).
- Matching Safari's theme bar to the dimmed overlay is an idea Emil Kowalski has not shipped, because the stepped color updates fall out of step with the overlay when frames drop [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).

### Keyboard, viewport and safe areas

- When an input inside the drawer opens the keyboard, the browser scrolls and can hide content. Vaul turns that off and uses the Visual Viewport API to size the drawer and sit it just above the keyboard, accepting a slight delay [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]). `repositionInputs` controls this [S-L19-096] ([[sources/vaul-inputs-inputs-vaul|Inputs – Vaul]]) and is on by default [S-L19-093] ([[sources/vaul-api-api-reference-vaul|API Reference – Vaul]]).
- Drawers use `100dvh`, not `100vh`; the page root gets `overscroll-behavior: none` and the sheet's content `contain`; sheets pad the bottom with `calc(1rem + env(safe-area-inset-bottom))` [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).

### Testing

- Test drawers on a real phone connected by cable with Safari's devtools, not in a shrunken desktop window; Xcode Simulator is an alternative [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]). The skills repeat that gestures need real devices [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]) [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]).

## Where they agree and disagree

- **Sheets on phones.** Emil Kowalski's preference for drawers over modals on mobile [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]), Kole Jain's use of bottom sheets to keep side tasks in context [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]) and DC-L08-20's default of a bottom sheet on phones all agree.
- **A visible way out.** Kole Jain keeps buttons on swipe-dismissable pop-ups because swiping is not obvious to everyone [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]). That matches `STD-accessibility-motion-24` and Vaul's warning about non-dismissible drawers [S-L19-097] ([[sources/vaul-other-other-vaul|Other – Vaul]]).
- **Duration.** The sources do not agree on one number. The drawer article uses 500ms [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]), the skills give a 200-500ms band [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]), and native sheets use a spring of about 300ms perceived [S-L19-016] ([[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]). The house standards settle it: 500ms on the web for timed open and close, a spring once a finger is involved.
- **The background.** Kole Jain's zoom-out [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]), Vaul's `scaleBackground` [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]) and Apple's push-back of parent sheets [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]) are the same idea at different strengths [inferred].
- **Scrim darkness.** Vaul's 40% black starter [S-L19-095] ([[sources/vaul-getting-started-getting-started-vaul|Getting Started – Vaul]]) sits inside DC-L04-18's default of 40-50% near-black in light mode, and matches Q-depth-06's Fluent option [inferred].
- **Where the drawer comes from.** Vaul is built on Radix Dialog [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]), while Emil Kowalski's curated list names base-ui for dialogs and has no drawer entry at all [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]). Vaul itself is unmaintained, per the note in `learn/sources.json`. DC-L08-03's default for React web is shadcn on Base UI or React Aria.
- **Desktop side panels.** DC-L08-20 suggests a side sheet for editing with context, but Kole Jain replaced a sparse side flyout with a modal because it had few fields and a lot of empty space [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]). The number of fields seems to decide it [inferred].
- **Button order.** DC-L08-20 records iOS sheets putting Cancel on the leading edge and Done on the trailing edge. Kole Jain's template sheet has a check and an X, but the video does not say where each sits [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]).

## Decisions this informs

- **Q-pattern-01** (centered box, sliding panel or small pop-up): sheets for side tasks and for most overlays on phones; `formSheet` in React Native.
- **Q-depth-06** (how dark the shade behind dialogs is): the 40% starter scrim, and dimming only for modal tasks.
- **Q-motion-01** (quick, calm or bouncy): the drawer curve and sheet spring are locked, so sheets keep them whatever personality is picked [inferred].
- **Q-motion-03** (how curves are grouped): the drawer curve is its own token next to ease-out and ease-in-out.
- **Q-motion-04** (how springs are set up): springs are written as damping and response (0.8 and 0.3s for sheets).
- **Q-motion-02** (how many durations): 500ms for web drawers is a named exception.
- **Q-motion-07** (reduced motion): Apple's sample turns the sheet into a 200ms opacity fade with no transform [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- **Q-motion-09** (system or brand motion and haptics): a light haptic when the sheet snaps home.
- **Q-depth-04** (glass or solid): sheets are translucent layers under the Apple guidance [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- **Q-comp-03** (settings or smaller parts): drawers are built from compound parts.
- **Q-plat-06** (built-in or restyled controls): in React Native the native form sheet comes first [inferred].

## Visual examples worth showing

- A web drawer with `scaleBackground`: the page shrinks behind it and its corners round as the drawer rises [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).
- A drag-to-dismiss sheet: it follows the finger down, resists upward, dismisses on a flick, and springs home with a light haptic while the backdrop fades with it [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]).
- Snap points like Apple Maps, including a fixed-pixel point that keeps an input peeking out [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).
- The note editor with a template sheet (title, search, check, X) and the background zoomed out [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]).
- A bottom pop-up with swipe down plus buttons, the background moving back and down [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]).
- A drawer with an input, repositioned above the keyboard versus pushed up by the browser [S-L19-096] ([[sources/vaul-inputs-inputs-vaul|Inputs – Vaul]]).
- Stacked sheets, each parent dimmer and pushed further back [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Vaul's side drawer that does not touch the screen edge, adjusted with `--initial-transform` [S-L19-094] ([[sources/vaul-default-default-vaul|Default – Vaul]]).

## Open questions

- Which library should build drawers now that Vaul is unmaintained and Emil Kowalski's curated list has no drawer entry?
- Should strong flicks skip snap points by default, or should drawers default to sequential snapping?
- When does a desktop create or edit form belong in a side sheet rather than a modal?
- Should the Safari theme-color sync ever ship, given it cannot stay in step when frames drop?
- Which duration should OpenDesigner export as the drawer default for timed motion: 500ms, or something inside the 200-300ms modal and drawer tier given in "Agents with Taste" [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]])?
