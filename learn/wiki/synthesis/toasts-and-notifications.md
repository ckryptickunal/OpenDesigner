---
type: synthesis
title: Toasts and notifications
created: 2026-09-24
updated: 2026-09-24
sources:
  - ADaQuZS04Rc
  - B7k5rOgmOGY
  - BUDipdbKK7Y
  - Vy0KKvZJRH8
  - adev-changelog
  - adev-home
  - ek-building-a-toast-component
  - ek-train-your-judgement
  - ek-you-dont-need-animations
  - eks-readme
  - eks-skills-animate-expo-recipes
  - eks-skills-animate-recipes
  - eks-skills-ask-sonner-api
  - eks-skills-ask-sonner-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-audit
  - eks-skills-pick-ui-library-skill
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
  - ld1zhQMXxXU
  - sonner-getting-started
  - sonner-home
  - sonner-other
  - sonner-styling
  - sonner-toast
  - sonner-toaster
tags:
  - od-area-components
---
# Toasts and notifications

## In short

A toast is a small message that slides in near the edge of the screen, says what just happened, and then goes away by itself. The house rule is to build toasts with Sonner rather than by hand, mount one Toaster near the root of the app, and call a plain `toast()` function wherever something happens. A toast rises from below, leaves the way it came, closes after 4 seconds, and pauses that timer while the pointer rests on it or the browser tab is hidden. Practitioner videos use toasts to confirm changes made in a modal and to report slow jobs such as a deploy. OpenDesigner's own research is more careful: it keeps toasts for low-stakes news and puts blocking errors somewhere that stays on screen.

## House standards

These are locked. Standards backed by the Sonner docs and Emil Kowalski's writing apply to every project.

**Setup and API**
- `STD-visual-details-57` (must): Never hand-roll standard components.
- `STD-components-toasts-drawers-35` (should): Toast API is a plain function.
- `STD-components-toasts-drawers-02` (must): Mount one Toaster at the root.
- `STD-components-toasts-drawers-03` (should): Keep the Toaster outside stacking contexts.
- `STD-components-toasts-drawers-04` (must): Call toast() only from client code.
- `STD-components-toasts-drawers-05` (should): Fire toasts from handlers or stable ids.
- `STD-components-toasts-drawers-19` (should): Pick the toast call by need.
- `STD-components-toasts-drawers-20` (must): Promise toasts need a settling promise.
- `STD-components-toasts-drawers-21` (should): Update a toast by its id.
- `STD-components-toasts-drawers-78` (should): Dismiss toasts from code by id.
- `STD-components-toasts-drawers-26` (should): Set toast defaults on the Toaster.
- `STD-components-toasts-drawers-27` (must): Target toasts when several toasters exist.
- `STD-components-toasts-drawers-28` (should): Handle dismiss and auto-close separately.
- `STD-components-toasts-drawers-33` (must): Copy Sonner styles into shadow DOM.
- `STD-components-toasts-drawers-34` (should): Import Sonner styles when they are lost.

**Motion**
- `STD-components-toasts-drawers-07` (should): Web toast enter: 400ms ease from below. The 400ms is an allowed exception to the 300ms ceiling in `STD-easing-duration-06`, because the motion is tuned to Sonner's personality (`STD-easing-duration-13`).
- `STD-easing-duration-06` (must): UI motion under 300ms unless justified.
- `STD-easing-duration-13` (must): Motion fits the component's personality.
- `STD-components-toasts-drawers-08` (must): React Native toasts: 300ms in, 250ms out.
- `STD-enter-exit-origin-06` (must): Exit the way it entered.
- `STD-enter-exit-origin-17` (should): Use @starting-style for mount entry.
- `STD-enter-exit-origin-21` (should): Slide by percentages, not pixels.
- `STD-easing-duration-11` (should): Exits run about 20% faster.
- `STD-springs-gestures-15` (must): Transitions, not keyframes, for rapid UI.
- `STD-when-to-animate-08` (should): Standard motion for occasional surfaces.

**Stack, timer and swipe**
- `STD-components-toasts-drawers-10` (should): Stack toasts with lift and depth.
- `STD-components-toasts-drawers-11` (should): Stacked toasts share the front height.
- `STD-components-toasts-drawers-12` (should): Expand the toast stack on hover.
- `STD-components-toasts-drawers-13` (must): Fill gaps between toasts for hover.
- `STD-components-toasts-drawers-14` (should): Show at most three toasts.
- `STD-components-toasts-drawers-15` (should): Auto-dismiss toasts after 4 seconds.
- `STD-components-toasts-drawers-16` (should): Pause the toast timer on hover.
- `STD-components-toasts-drawers-17` (must): Pause toast timers in a hidden tab.
- `STD-components-toasts-drawers-18` (should): Swipe toasts away along their position.
- `STD-springs-gestures-21` (must): A flick is enough to dismiss.
- `STD-springs-gestures-28` (must): Capture the pointer during a drag.
- `STD-springs-gestures-25` (must): Rubber-band at edges, never hard-stop.

**Look, place and access**
- `STD-components-toasts-drawers-22` (must): Toasts follow the app theme.
- `STD-components-toasts-drawers-23` (should): Rich colors and invert from defaults.
- `STD-components-toasts-drawers-24` (should): Headless toast for the design system.
- `STD-components-toasts-drawers-25` (must): Toast classNames need !important.
- `STD-components-toasts-drawers-29` (should): Toasts default to bottom-right.
- `STD-components-toasts-drawers-30` (should): Toaster edge offsets: 32px and 16px.
- `STD-mobile-touch-16` (must): Paint edge to edge, pad the safe areas.
- `STD-accessibility-motion-23` (should): Keep the toaster labelled and reachable.

## What the sources teach

### When a toast is the right tool

- A dashboard's toasts are its notification system. They confirm the changes someone made inside a modal (the page was hidden while they worked), make people aware of something without taking over the screen, prompt an action, and carry warning and error states, which often get missed [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- When an action takes time, such as a deploy, report its status right away so nobody has to guess whether it worked; Vercel's build-status notification is the example [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- A toast can close out an optimistic action: in Kole Jain's macOS quick-save window, pressing Enter collapses the window into a toast that slides off while the save finishes in the background [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).
- Notifications must not shame people. A recurring YouTube watch-time message whose only exits are "subscribe to Premium" or "keep getting this" is shown as an infuriating example [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- Toasts should animate in, because a toast that suddenly appears feels off [S-L19-012] ([[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]). Emil Kowalski's frequency table puts toasts with modals and drawers as occasional UI: they get standard animation, and delight is saved for rare moments [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]) [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]) [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]) [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]).

### Use Sonner, and set it up once

- Sonner is the curated pick for toasts; building them by hand or with a modal library is a mismatch to catch [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]). The skills repo exists partly so agents stop hand-rolling toast components [S-L19-014] ([[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]]).
- After installing the package, setup is two pieces: render `<Toaster />` once (the docs put it in the root `layout.tsx`, and a server component is fine), then call `toast('...')` from an event handler such as a button's `onClick` [S-L19-087] ([[sources/sonner-getting-started-getting-started-sonner|Getting Started – Sonner]]) [S-L19-088] ([[sources/sonner-home-sonner|Sonner]]) [S-L19-092] ([[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]).
- The API won adoption because it needs no hooks and no context: `toast()` notifies an observer-pattern store that `<Toaster />` subscribes to, so it works from anywhere. Its rendering API is modeled on react-hot-toast, which the author calls simply very good [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- Common mistakes and their fixes: a Toaster rendered per page or behind a condition duplicates or loses toasts; `toast()` is client-only, so a server action returns its result and the client shows the toast; React StrictMode runs effects twice, so fire toasts from handlers or pass a stable id; a Toaster inside an ancestor with `transform`, `filter` or `overflow` ends up hidden behind modals [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]).
- When styles go missing (Astro with view transitions), import `sonner/dist/styles.css` in a layout; inside shadow DOM, copy the `<style>` tags containing `[data-sonner-toaster]` into the shadow root [S-L19-089] ([[sources/sonner-other-other-sonner|Other – Sonner]]) [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]).

### Motion: up from below, out the same way

- Use CSS transitions, not keyframes. When toasts arrive quickly, keyframes make the older toasts jump to their new places, while transitions retarget smoothly [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]). The review skills name toasts as rapidly triggered UI that must stay interruptible [S-L19-032] ([[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]]) [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]).
- On the web a toast starts at `opacity: 0` and `translateY(100%)` and transitions over `400ms ease`, using `@starting-style`, or a mounted flag set in `useEffect` where that is not available [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]) [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]). A percentage translate moves the toast by its own height whatever its size [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]).
- The plain `ease` at 400ms is slower than typical UI on purpose: Sonner's easing, timing, look and name are meant to match one elegant personality [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]) [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]).
- In React Native, toasts enter with `FadeInDown` over 300ms and leave with `FadeOutDown` over 250ms, both ease-out. A toast is uninvited, so it stays within a 300ms cap, exits about 20% faster than it enters, and sits at `bottom: insets.bottom + 16` so the home indicator does not cover it [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]).
- Entering and leaving from the same edge gives spatial consistency, which makes swipe-down-to-dismiss feel natural [S-L19-012] ([[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]) [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).
- When stacked toasts reflow, balance the opacity change against the height change by eye and look again the next day; there is no formula [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]) [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]).
- Pick a toast's easing by comparing two variants side by side; it is one of Emil Kowalski's judgement exercises [S-L19-011] ([[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]]). The animations.dev CSS module builds its toast with transforms and transitions only [S-L19-001] ([[sources/adev-changelog-animations-dev|animations.dev]]) [S-L19-002] ([[sources/adev-home-animations-dev|animations.dev]]).

### The stack, hover and swipe

- Collapsed toasts are absolutely positioned. Each toast behind the front one is lifted by the gap times its index and scaled down by 0.05 per step, so the illustration reads `Y(0) scale(1)`, `Y(-14px) scale(0.95)`, `Y(-28px) scale(0.9)`. Every stacked toast takes the height of the front toast so they stick out evenly [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- Hovering the area expands the pile. Each toast's expanded offset is its index times the gap plus the heights of the toasts before it; the gap defaults to 14, and an `expand` prop keeps the pile open all the time [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]) [S-L19-092] ([[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]) [S-L19-021] ([[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]).
- An `:after` pseudo-element fills each gap so the hover state is not lost while the pointer crosses between toasts [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- Toasts can be swiped away on touch screens and on desktop. A swipe dismisses when it passes a distance threshold or when its velocity (distance divided by time) passes 0.11, a value found by trial and error. Once a drag starts the toast captures the pointer, and dragging the wrong way meets friction instead of a hard stop [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]). Swipe directions follow the toaster's position [S-L19-088] ([[sources/sonner-home-sonner|Sonner]]) [S-L19-092] ([[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]).
- Three toasts are visible by default; the docs show `visibleToasts={9}` as a custom value [S-L19-092] ([[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]).

### How long a toast stays

- The default is 4 seconds (`duration: 4000`). The timer pauses while the pointer hovers and while the tab is hidden, using `document.hidden` and the `visibilitychange` event, so a toast fired in a background tab is not lost [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]) [S-L19-021] ([[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]) [S-L19-091] ([[sources/sonner-toast-toast-sonner|Toast – Sonner]]).
- `duration: Infinity` keeps a toast until someone dismisses it. If a toast never closes, check for `Infinity`, `dismissible: false`, or a `toast.promise` whose promise never settles [S-L19-089] ([[sources/sonner-other-other-sonner|Other – Sonner]]) [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]).

### Choosing the right call

- Plain message: `toast('Title')`, with `{ description }` for a second line. Status: `toast.success`, `.error`, `.info` or `.warning`, each with its own icon. Work tied to one promise: `toast.promise(promise, { loading, success, error })`. Work you track yourself: `toast.loading(...)`, then update it by id [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]) [S-L19-091] ([[sources/sonner-toast-toast-sonner|Toast – Sonner]]) [S-L19-088] ([[sources/sonner-home-sonner|Sonner]]).
- `action` adds a primary button and `cancel` a secondary one. Both close the toast when clicked; calling `event.preventDefault()` in the action keeps it open [S-L19-091] ([[sources/sonner-toast-toast-sonner|Toast – Sonner]]).
- To change a toast already on screen, call `toast()` again with its id and only the props that change; a typed call such as `toast.success('Uploaded', { id })` changes its type. `toast.dismiss(id)` removes one toast and `toast.dismiss()` removes all [S-L19-089] ([[sources/sonner-other-other-sonner|Other – Sonner]]) [S-L19-021] ([[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]).
- `onDismiss` fires when someone closes or swipes a toast; `onAutoClose` fires when it times out. They are different events [S-L19-089] ([[sources/sonner-other-other-sonner|Other – Sonner]]).
- Several toasters are only for a clear separation, each with an id and targeted with `toasterId`; the docs' example puts a "global" toaster top right and a "canvas" toaster bottom left [S-L19-092] ([[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]).

### Styling a toast for a design system

- The styling ladder runs from the defaults, to `toastOptions.style`, to per-part `classNames` (which need `!important`, or Tailwind's `!` prefix), to `unstyled`, to headless. The docs recommend going headless with `toast.custom()` and wrapping it in your own `toast()` function, because people usually either keep the defaults or go fully custom [S-L19-090] ([[sources/sonner-styling-styling-sonner|Styling – Sonner]]) [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]).
- The theme defaults to light and does not follow the OS, so a dark-mode app passes `theme="system"` or the theme provider's resolved theme [S-L19-092] ([[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]) [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]). Success and error toasts are gray until `richColors` is on; `invert` flips toasts against the page [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]) [S-L19-021] ([[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]).
- Icons can be replaced for the whole app with `icons`, for one toast with `icon`, or removed with `null` [S-L19-090] ([[sources/sonner-styling-styling-sonner|Styling – Sonner]]).
- There are six positions and bottom-right is the default. Toasts sit 32px from the edges on desktop and 16px below 600px wide; offsets accept a number, a CSS string or a per-side object [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]) [S-L19-092] ([[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]).

### Accessibility

- The toast container carries an ARIA label ("Notifications" by default, changed with `containerAriaLabel`), `Alt+T` moves focus to the toaster, and toasts are dismissible unless told otherwise [S-L19-091] ([[sources/sonner-toast-toast-sonner|Toast – Sonner]]) [S-L19-092] ([[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]) [S-L19-021] ([[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]).

### Beyond the slide-up (practitioner opinion)

- Kole Jain wants toasts to do more than the obvious slide-up and suggests toasts that show a small loading animation and then a celebratory success message, sometimes with particles. He likes Linear's toasts more than Vercel's, and he places a swipeable card stack in the bottom right as a notification center, noting that dub.co keeps one in its sidebar [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]). He also points to Dub and Linear using the sidebar's empty space for notifications [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]). These are one creator's preferences, not tested findings.

### What made Sonner succeed

- The author credits developer experience and good looks: a distinctive name ("Sonner", from French words about notifications), a signature stacking animation used in the launch videos, and interactive docs with live examples and copyable code [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).

## Where they agree and disagree

- **Timing.** Emil Kowalski's sources hold a tension: UI should stay under 300ms, yet the web toast runs 400ms and the React Native toast is capped at 300ms [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]) [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]). The house standards settle it: 400ms on the web is a named exception for personality (`STD-easing-duration-06`, `STD-easing-duration-13`), and React Native keeps 300ms in and 250ms out (`STD-components-toasts-drawers-08`).
- **Delight in toasts.** Kole Jain's celebratory, particle-filled toasts [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]) pull against the frequency rule that toasts are occasional UI and get standard motion, not delight (`STD-when-to-animate-08`). A reasonable split is a plain toast for routine confirmations and a celebratory one only for a rare first success [inferred].
- **Errors in toasts.** Kole Jain uses toasts for warnings and errors precisely because they are easy to miss elsewhere [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]). OpenDesigner's research says the opposite about blocking errors: DC-L13-09 keeps toasts for low-stakes confirmations and says a toast should never be the only channel for an error that stops progress, and DC-L13-07 lists toasts as unsuited to form errors. Both of those are marked [inferred] in the research itself, so neither side has hard evidence here.
- **Actions and auto-dismiss.** DC-L08-18 says never auto-dismiss a toast that contains an action, citing WCAG 2.2.1 and 2.2.3 on timing. Sonner closes every toast after 4000ms unless `duration: Infinity` is set, and clicking an action closes it [S-L19-091] ([[sources/sonner-toast-toast-sonner|Toast – Sonner]]) [S-L19-021] ([[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]). Sonner's pause on hover and on hidden tabs covers part of the "pausable" requirement, but not keyboard or screen-reader users who never hover [inferred]. Giving action toasts `duration: Infinity` would satisfy both [inferred].
- **Whether to use toasts at all.** DC-L13-09 notes that Primer deliberately ships no toast, and Q-form-04 defaults to inline messages and banners. The house standards do not decide that question; they only lock how a toast is built once a product uses one.
- **Undo.** DC-L13-08 recommends a toast with Undo for reversible actions. Sonner's `action` button is the natural place for that Undo [inferred].
- **Loading.** DC-L13-01 lists optimistic UI as an option, which matches Kole Jain's save-then-toast pattern [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]) and Sonner's `toast.loading` and `toast.promise` [S-L19-091] ([[sources/sonner-toast-toast-sonner|Toast – Sonner]]).
- **Native apps.** DC-L08-18 notes that iOS uses system notifications and in-place status rather than toasts, and the Sonner guidance is React-only [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]). The React Native recipe [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]) is the only native guidance in these sources.

## Decisions this informs

- **Q-form-04** (where "Saved" messages appear): the sources favour toasts for confirmations in dashboards, while the default is `inline-banner`. Whichever is chosen, the house standards fix how toasts behave.
- **Q-form-05** (undo or confirm on delete): a toast with an Undo action is the undo channel [inferred].
- **Q-state-08** (what people see while they wait): `toast.loading` and `toast.promise` cover background work that finishes after the person has moved on.
- **Q-motion-01** (motion personality): Sonner is the worked example of motion tuned to a component's personality.
- **Q-motion-02** (durations, faster exits): toasts show the 20%-faster exit (300ms in, 250ms out on React Native).
- **Q-theme-01** (light and dark): toasts must follow the app theme, never the light default.
- **Q-color-15** (status colors): typed toasts need success, error, info and warning colors and icons; `richColors` is off by default.
- **Q-comp-01** (bare parts or a full kit): the headless `toast.custom()` route matches the headless option [inferred].
- **Q-dist-04** (where docs live): Sonner's interactive docs are the model the author recommends.
- **Q-pattern-05** (stopping design tricks): usage-shaming notifications are an example to block.

## Visual examples worth showing

- The three-toast stack with `Y(0) scale(1)`, `Y(-14px) scale(0.95)` and `Y(-28px) scale(0.9)` labels [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- Adding toasts quickly with keyframes (older toasts jump) against transitions (they glide) [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- The expanded pile with the `:after` gap fillers drawn as dark bars [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- A loading toast that turns into a success toast in place: `const id = toast.loading('Uploading…')`, then `toast.success('Uploaded', { id })` [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]).
- The six-position grid, showing how the swipe direction changes with each position [S-L19-088] ([[sources/sonner-home-sonner|Sonner]]).
- A "create link" modal that closes and is followed by a confirming toast [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- The macOS quick-save window collapsing into a toast [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).
- A React Native toast sitting 16 points above the home indicator [S-L19-015] ([[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]]).
- Kole Jain's loading-to-celebration toast, labeled as practitioner opinion [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).

## Open questions

- Should toasts that carry an action (such as Undo) persist until dismissed, as DC-L08-18 asks, or keep the 4-second default with hover and hidden-tab pausing? The standards and the research need one answer.
- May a toast carry an error that blocks progress, as Kole Jain does, or must that error also appear in place?
- Does Sonner announce new toasts to screen readers through a live region? None of these sources says; it needs a check against Sonner's code or a screen-reader test.
- What does a toast do under reduced motion? None of the toast sources gives a reduced-motion variant, and `STD-accessibility-motion-01` requires one.
- On narrow screens, should the default stay bottom-right or move to bottom-center? The sources give a 16px mobile offset but no mobile position.
- What should OpenDesigner recommend for SwiftUI and Compose, where Sonner does not exist?
