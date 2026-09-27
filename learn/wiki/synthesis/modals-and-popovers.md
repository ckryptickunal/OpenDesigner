---
type: synthesis
title: Modals and popovers
created: 2026-09-24
updated: 2026-09-28
sources:
  - 14h1VnkQvIc
  - ADaQuZS04Rc
  - B7k5rOgmOGY
  - BUDipdbKK7Y
  - Ksx9C2-3yMo
  - Lp6ey4AyDzA
  - PDcQJOPby1k
  - V3Omp1hm0Sg
  - Vy0KKvZJRH8
  - adev-home
  - ek-7-practical-animation-tips
  - ek-agents-with-taste
  - ek-building-a-drawer-component
  - ek-train-your-judgement
  - ek-you-dont-need-animations
  - eks-skills-animate-recipes
  - eks-skills-animate-skill
  - eks-skills-animation-vocabulary-skill
  - eks-skills-apple-design-skill
  - eks-skills-ask-sonner-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-audit
  - eks-skills-improve-animations-skill
  - eks-skills-pick-ui-library-skill
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
  - ld1zhQMXxXU
  - qK7WYCMvjUw
  - vaul-getting-started
  - vaul-other
  - vaul-snap-points
tags:
  - od-area-components
---
# Modals and popovers

## In short

Modals, popovers, dropdown menus and tooltips are layers that float above the page. Pick the lightest one that fits: a popover for simple settings people can click away from, a modal for a bigger task tied to the current page, and a new page for anything large or permanent. Popovers, menus and tooltips grow out of the button that opened them, while a modal grows from the center of the screen with a dimmed backdrop. All of them are built on accessible building blocks (base-ui or Radix) that handle keyboard focus and Escape, never on hand-made `<div>` elements, and anything opened from the keyboard, like a command menu, appears instantly with no animation.

## House standards

**Building them**
- `STD-accessibility-motion-16` (must): Build overlays on accessible primitives.
- `STD-accessibility-motion-24` (must): Never trap the user in an overlay.
- `STD-visual-details-57` (must): Never hand-roll standard components.
- `STD-components-toasts-drawers-37` (should): Prefer drawers over modals on mobile.
- `STD-components-toasts-drawers-03` (should): Keep the Toaster outside stacking contexts. (so toasts do not hide behind modals)

**Origin and entrance**
- `STD-enter-exit-origin-03` (must): Scale popovers from their trigger.
- `STD-enter-exit-origin-04` (must): Keep modals scaling from center.
- `STD-enter-exit-origin-38` (should): Set every transform-origin on purpose.
- `STD-enter-exit-origin-01` (must): Never enter from scale(0).
- `STD-enter-exit-origin-02` (must): No opacity-only fade entrances.
- `STD-enter-exit-origin-08` (must): Dropdowns and popovers: scale 0.95, 200ms.
- `STD-enter-exit-origin-09` (must): Tooltips: scale 0.97, 125ms.
- `STD-enter-exit-origin-10` (must): Delay only the first tooltip.
- `STD-enter-exit-origin-11` (must): Modals: centered scale 0.96, 250ms.
- `STD-enter-exit-origin-12` (should): Fade the backdrop with the modal.

**Timing and feel**
- `STD-easing-duration-03` (must): Never use ease-in on UI.
- `STD-easing-duration-07` (must): Duration budget for each element.
- `STD-springs-gestures-05` (must): Bounce only after a momentum gesture.
- `STD-springs-gestures-12` (must): Every animation can be grabbed mid-flight.
- `STD-when-to-animate-05` (must): No motion on 100+ times-a-day actions.
- `STD-when-to-animate-06` (must): Never animate keyboard-initiated actions.
- `STD-when-to-animate-08` (should): Standard motion for occasional surfaces.

**When to block**
- `STD-visual-details-20` (should): Scrim for modal tasks only.
- `STD-visual-details-40` (must): Undo for slips, confirm only destruction.

## What the sources teach

### Choosing the layer

- Match the layer to the size and permanence of the task. A popover suits simple context such as display settings, because people can click away without consequences. A modal suits more complex context tied to the page, such as creating a link, and it blocks until the person creates or cancels. A new page, with a back button or breadcrumb, suits large or permanent context. After a modal closes, a toast confirms the change [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- Features people rarely use, such as sharing, belong in a popover rather than a permanent panel or a new page, with the popover's main action (a search box) at the top. Before giving a feature its own page, check whether it fits into the hidden states of an existing drawer or modal [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]).
- A short create form that leaves a side flyout mostly empty fits better in a modal; account links fit in a popover opened from an account card [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- An add-on offered on only some products can open as a lightbox card with a full-size photo, a gradient behind the text so it stays readable, and a close X [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).
- On phones, Emil Kowalski uses a drawer instead of a modal for a more native feel, and builds it on Radix's Dialog primitive [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]). A drawer can also be non-modal, leaving the page behind usable [S-L19-097] ([[sources/vaul-other-other-vaul|Other – Vaul]]) [S-L19-098] ([[sources/vaul-snap-points-snap-points-vaul|Snap Points – Vaul]]).
- Mac apps live partly outside their main window, in popovers, new windows and notifications. Kole Jain's example app uses a simple onboarding modal that teaches its key shortcut and keeps a shortcut cheat sheet in a settings popover [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).
- A new modal should be assembled from the system's existing parts (selectors, fields, actions at the bottom) so it feels familiar next to the others [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).

### Blocking layers: use them with care

- Do not block every other action until a chore is done; Figma's forced layer-naming modal is the infuriating example, and even an annoying feature needs a notice explaining how to turn it off. Endless pop-ups and guilt pop-ups are the same problem [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- Do not greet a new user with a modal of six bullet points explaining the whole product; they forget it the moment they close it. Start with one tooltip on the most important action, then a second tooltip or a small checklist [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]).
- A modal task gets a dimming scrim and pushes the page back; a parallel, non-blocking panel uses translucency without a scrim. Confirmation dialogs are only for truly destructive, irreversible actions, because too many train people to click through [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- A paywall people can close is called a soft paywall even when its close button only appears after 5 seconds, as in the astrology app Moonly. Its founder says the soft paywall won across all his tests, while the host says hard paywalls won in the US; the figures are self-reported by one app [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- Pop-ups and bottom pop-ups can be dismissed by swiping, but keep a close button for people who do not know the gesture [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]).

### Motion: origin, scale and speed

- Popovers should grow out of their trigger, not their own center; the default `transform-origin: center` is wrong in most cases, and the difference is most noticeable when neither the horizontal nor the vertical origin matches, as in a top-right position. Radix and Base UI expose the right origin as a CSS variable [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]). A popover scaled from the wrong point is called out as a mistake [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]), and "origin-aware animation" is the name to use when asking for this [S-L19-019] ([[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]).
- The recipes: dropdowns, popovers, menus and selects go from `opacity: 0` and `scale(0.95)` over 200ms ease-out; tooltips from `scale(0.97)` over 125ms; modals from `scale(0.96)` over 250ms, centered, with the backdrop fading on the same timing so both read as one surface [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]).
- The duration bands are 125-200ms for tooltips and small popovers, 150-250ms for dropdowns and selects, and 200-500ms for modals and drawers, with UI generally under 300ms [S-L19-018] ([[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]). A 180ms dropdown feels more responsive than a 400ms one [S-L19-012] ([[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]) [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]).
- Never start from `scale(0)`; start at 0.9 or higher (the demo uses 0.93). Never use ease-in: a 300ms ease-in dropdown feels slower than a 300ms ease-out one [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]) [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).
- Modals are the one exception to trigger origin: they stay centered, and a centered modal must not be reported as a mistake [S-L19-027] ([[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]]) [S-L19-032] ([[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]]) [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]) [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]) [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]).
- A menu that just faded in must not overshoot. A modal or sheet that is closing and gets grabbed again follows the finger instead of finishing its close first [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Emil Kowalski's judgement exercises compare two dialog entrances, two popover animations, and a menu opened and closed rapidly to see which handles interruption better [S-L19-011] ([[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]]). The animations.dev course builds a Feedback popover over three exercises [S-L19-002] ([[sources/adev-home-animations-dev|animations.dev]]).

### Tooltips

- Give the first tooltip a short delay so it does not open by accident; once one is open, neighboring tooltips open instantly with no delay and no animation. Base UI does this with `transition-duration: 0ms` on `[data-instant]` [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]) [S-L19-012] ([[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]) [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).
- Kole Jain delays icon tooltips by a full second, as Obsidian does, and gives the pop-up a slightly bouncy custom easing [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).
- Add tooltips to icons and to ambiguous labels, which beginner dashboards almost always miss; secondary actions can appear on hover with a tooltip when space is tight [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]).

### Command menus open instantly

- A launcher or command menu that people open hundreds of times a day should appear instantly, as Raycast does, and moving the highlight with arrow keys should never animate [S-L19-012] ([[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]). Anything started from the keyboard is ruled out of animation outright [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]). The curated pick for command menus is cmdk [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).

### Build on primitives

- Dialogs, popovers, menus and selects come from base-ui, which handles focus trapping and dismissal; a `<div>` dialog with hand-written focus handling is a mismatch to fix [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]). When the task is really a component (a dropdown, a command menu), stop and pick a library instead of animating a hand-made one [S-L19-018] ([[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]).
- A Toaster mounted inside a dialog or an element with `transform`, `filter` or `overflow` ends up behind the modal; mount it at the root [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]).

### The destructive confirmation

- Kole Jain gives the delete button in a delete dialog the primary fill, preferably red, and demotes cancel [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]). Elsewhere he praises macOS dialogs, where the primary color always marks the non-destructive action [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).

## Where they agree and disagree

- **Choosing the layer.** Kole Jain's popover, modal and page ladder [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]) broadly matches DC-L08-20: present modally only with a clear benefit, use a dialog for short decisions, and use a bottom sheet on phones. They part on editing: DC-L08-20 suggests a side sheet to keep context, while Kole Jain moved a sparse create form from a flyout into a modal [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- **Tooltip delay and bounce.** Everyone delays the first tooltip. Kole Jain puts the delay at a full second and adds bounce [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]), but the house rule says nothing that appears without a gesture may overshoot (`STD-springs-gestures-05`), so the bounce is out for product UI; the one-second delay comes from one video.
- **Modal duration.** Emil Kowalski's sources give 200-300ms for modals in one place [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]), a 200-500ms band in others [S-L19-018] ([[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]), and 250ms in the recipe [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]). The house standard (`STD-enter-exit-origin-11`) takes the 200-500ms band with the 250ms recipe.
- **Scrim.** Apple-style guidance dims only for modal tasks [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]). DC-L04-18 gives 40-50% near-black in light mode and 50-60% in dark mode, which fits Vaul's 40% starter overlay [S-L19-095] ([[sources/vaul-getting-started-getting-started-vaul|Getting Started – Vaul]]) [inferred].
- **Primary role in a destructive dialog.** The two Kole Jain videos disagree [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]) [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]). DC-L13-18 and DC-L08-06 cite Apple's rule that a destructive button never takes the primary role, and DC-L08-06 allows solid red only in the final confirmation step.
- **Confirming at all.** `STD-visual-details-40` and DC-L13-08 agree: undo for reversible actions, confirmation only for costly, irreversible ones.
- **A delayed way out.** Moonly's close button that waits 5 seconds [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]) still gives a way out eventually, but it delays the exit that `STD-accessibility-motion-24` asks every screen and overlay to have. DC-L13-15 lists obstruction among the 16 deceptive patterns and leaves those a tool cannot detect to human review; whether a timed close counts is not settled by any source [inferred].
- **Hover-only actions.** Kole Jain reveals secondary actions on hover [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]), and the video does not say how touch or keyboard users reach those actions [inferred]; `STD-mobile-touch-30` requires hover affordances to be redesigned for touch.
- **Onboarding modals.** Kole Jain warns against a bullet-point modal at login [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]) but uses a small onboarding modal that teaches a shortcut by having people do it [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]). The difference is teaching by doing rather than by reading [inferred].
- **Accessibility.** DC-L08-20 requires focus to be trapped and returned, Escape to close and `aria-modal`; building on base-ui or Radix (`STD-accessibility-motion-16`) is how the house standards get that.

## Decisions this informs

- **Q-pattern-01** (centered box, sliding panel or small pop-up): the popover, modal and page ladder, and drawers on phones.
- **Q-depth-06** (shade behind dialogs): dim only for modal tasks, 40-50% in light mode.
- **Q-depth-04** (glass or solid menus and pop-ups): non-blocking panels use translucency without a scrim.
- **Q-motion-02** (durations): tooltip, dropdown and modal bands; the house standards settle this question (`STD-easing-duration-07`).
- **Q-motion-03** (how curves are grouped): ease-out for entrances and exits, never ease-in.
- **Q-motion-04** (springs and bounce): no overshoot on menus, popovers and dialogs; `STD-springs-gestures-05` rules out the `spatial-effects` option.
- **Q-form-05** (undo or confirm): confirmation dialogs only for destructive, irreversible actions. `STD-visual-details-40` settles this question and rules out the `confirm` option (an "Are you sure?" box instead of undo).
- **Q-state-06** (how risky actions look): who gets the primary color in a delete dialog.
- **Q-pattern-03** (show everything or tuck extras away): popovers for rarely used features, hover-revealed secondary actions.
- **Q-pattern-04** (first-time users): tooltips and a checklist instead of a bullet-point modal.
- **Q-pattern-05** (stopping design tricks): no blocking chore modals or guilt pop-ups, and a decision on close buttons that appear late [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- **Q-icon-05** (when icons get words): tooltips on icon-only controls.
- **Q-comp-01** (bare parts or a full kit): accessible headless primitives for every overlay.

## Visual examples worth showing

- The origin-aware Feedback popover, toggled between center and trigger origin, placed top-right [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]).
- A popover (0.95, 200ms), a tooltip (0.97, 125ms) and a modal with backdrop (0.96, 250ms) side by side [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]).
- Two "Options" dropdowns at 300ms, ease-in against ease-out, and two selects at 180ms and 400ms [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]).
- A toolbar where the first tooltip waits and the rest appear instantly [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]).
- `scale(0)` against a 0.93 start [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]).
- A command menu toggled with and without animation [S-L19-012] ([[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]).
- A share popover with the search box on top and remove buttons revealed on hover [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]).
- The popover, modal and new-page ladder on one dashboard [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- Figma's forced naming modal as an anti-pattern [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- The lightbox card with gradient and close X [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).

## Open questions

- How long should the first tooltip's delay be? Only Kole Jain gives a number (one second).
- Which modal duration should OpenDesigner export by default: 250ms, or a value in the 200-300ms tier?
- On desktop, when does an edit or create task belong in a side sheet rather than a modal?
- In a destructive confirmation, which button gets the primary role and the default focus?
- How should hover-revealed actions work for touch and keyboard users?
- What do modals and popovers do under reduced motion? These sources do not say.
- May a close control appear after a delay, as on Moonly's paywall, or must the way out be there from the start?
