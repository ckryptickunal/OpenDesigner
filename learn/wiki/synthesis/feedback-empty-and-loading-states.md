---
type: synthesis
title: Feedback, empty and loading states
created: 2026-09-24
updated: 2026-09-28
sources:
  - ADaQuZS04Rc
  - AH_ugxmLeUM
  - B7k5rOgmOGY
  - EcbgbKtOELY
  - Gfsd8NNuD9g
  - If7iCPDy2vk
  - NtZeYmTMuo4
  - Qsq-Sj_rojU
  - SfX43uIubj4
  - Vy0KKvZJRH8
  - ZsP20PN14O0
  - d4MF6pdAZNw
  - ek-7-practical-animation-tips
  - ek-building-a-toast-component
  - ek-you-dont-need-animations
  - eks-skills-animation-vocabulary-skill
  - eks-skills-apple-design-skill
  - eks-skills-ask-sonner-api
  - eks-skills-ask-sonner-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-review-animations-standards
  - ixUq4HM4FNg
  - kdRkuqu8apE
  - nl8OFGdx75w
  - sonner-toast
tags:
  - od-area-patterns
---
# Feedback, empty and loading states

## In short

Every action needs a visible answer, so the interface feels like it is listening. Every screen also has more states than the ideal full one: empty, loading, success and error, and each needs designing. Use the smallest signal that fits: a pressed button, an inline message, a fast spinner or a skeleton while waiting, a toast for a quick confirmation. Empty screens should say what is going on and offer the next step. The house standards fix how spinners move and how toasts are built, and they name empty states and success moments among the few places where delight motion is allowed.

## House standards

- `STD-visual-details-49` (must): feedback on every action as soon as possible: a loading state while a form submits, a success state after copy to clipboard, visible ongoing status, warnings before problems, inline validation.
- `STD-easing-duration-15` (should): loading spinners spin fast; `STD-easing-duration-01` (must): constant motion such as a spinner or progress fill is linear.
- `STD-when-to-animate-09` (must): delight motion only at rare moments, including empty states and success or completion.
- `STD-enter-exit-origin-16` (should): give content that appears, disappears or swaps a short enter and exit transition instead of letting it pop.
- `STD-accessibility-motion-02` (must): under reduced motion, drop movement but keep opacity and color changes that explain a state change; never remove all feedback.
- `STD-springs-gestures-61` (must): haptics and sound only for meaningful moments such as success and error.
- `STD-visual-details-40` (must): easy undo for slips; confirmation dialogs only for destructive, irreversible actions.
- `STD-visual-details-57` (must): build toasts with Sonner, never by hand or with a modal library.
- `STD-components-toasts-drawers-19` (should): pick the toast call by need (typed status toasts, `toast.promise` for one promise, `toast.loading` plus an update by id when you manage the states, `action` and `cancel` for buttons).
- `STD-components-toasts-drawers-20` (must): a promise passed to `toast.promise` must actually resolve or reject.
- `STD-components-toasts-drawers-21` (should): change a toast already on screen by its id instead of adding another.
- `STD-components-toasts-drawers-15` (should) and `STD-components-toasts-drawers-14` (should): auto-close after 4000 ms by default, except a toast with an action button, which stays until the person acts or dismisses it; show at most three toasts at once.
- `STD-components-toasts-drawers-23` (should) and `STD-components-toasts-drawers-24` (should): start from Sonner's defaults (add `richColors` when success and error must read green and red), and build the design system's own toast headless.
- `STD-components-toasts-drawers-07` (should): on the web a toast enters from below with opacity and transform over 400 ms ease.
- `STD-accessibility-motion-23` (should): keep the toaster's accessible label, its Alt+T hotkey and dismissible toasts.

## What the sources teach

### Every action gets an answer

- Give feedback on every action as soon as possible so the interface feels like it is listening: a loading state when a form is submitted, a success state after copying to the clipboard [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]).
- Feedback comes in four kinds (status, completion, warning, error); highlight a control the moment it is pressed and commit on release [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Every interaction needs a response: spinners while data loads, success messages when an action completes [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]). Feedback means an immediate response to any action, and for creators it extends to likes, comments and shares [S-L19-077] ([[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok’s UX is so GOOD it should be ILLEGAL (seriously)]]).
- A short delay with no feedback looks like the tap failed: gray the button out on press and add a loading wheel for long waits [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- A password field that ticks off each requirement as the user types removes a reason to get stuck; none of this is flashy, but it makes the experience feel effortless [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- Every keyboard shortcut needs a visible change, or people assume something went wrong [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).

### While people wait

- A faster-spinning spinner makes loading feel faster at the same load time [S-L19-012] ([[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]); [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]); [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]).
- A skeleton, placeholders with a moving shimmer, is the named pattern for content that is loading; a quick side-to-side shake signals rejected input [S-L19-019] ([[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]).
- In AI tools, loaders should be short, looping and fluid; stream output word by word, show skeletons with shimmer where content will land, and never make people wait without feedback [S-L19-055] ([[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]]).
- Optimistic UI updates the screen at once on the assumption the request will succeed, as Gmail does when deleting an email [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]); a quick-save window can collapse into a toast while the save finishes in the background [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).
- In a long onboarding, even loading and verification steps can get smooth animation so something is always happening (Bump); these states rarely get special treatment [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- A Figma prototype moves an integration tile from focus to a spinning loading state to a success state whose check mark slides in through a mask instead of fading [S-L19-059] ([[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]).

### Toasts

- A toast library can expose a promise API: pass one promise and a message for each of its three states (loading, success, error), and one toast moves through them; toasts auto-dismiss after 4 seconds by default [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- Use `toast.success`, `toast.error`, `toast.info` and `toast.warning` so each gets its icon; `toast.loading` shows a spinner that you update by id; `toast.promise` moves from loading to success or error when the promise settles [S-L19-021] ([[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]); [S-L19-091] ([[sources/sonner-toast-toast-sonner|Toast – Sonner]]).
- A toast that never closes usually has `duration: Infinity`, `dismissible: false` or a promise that never settles; clicking an action closes the toast unless its handler calls `event.preventDefault()` [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]).
- In a dashboard, toasts confirm changes made in a modal (the page was hidden while the change happened) and surface warnings and errors that are easy to miss [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).

### Empty states

- Real apps must handle empty, loading, success and error states, not just the ideal one. Dub's empty dashboard has an animation, a message and a clear next step; Vercel reports build status right after a deploy; a Notion integration shows loading, then success or error [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- Design two kinds of empty state: first use, which points at the main action with a full-screen state and a small popover, and no results, which needs imagery, an acknowledgement, suggestions in case of a typo and a way out [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]).
- Show a simple empty state that invites the first action, and hide filters until there is content to filter [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]). Lists need an empty state for when there is no data [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- Instead of a blank first screen, to-do apps show a small nudge in the right place, with no guided tour and no pop-ups [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- When everything is done, the empty state can reward people: Mercury lets them play a game instead of showing an empty table once all bills are paid [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- Empty states and success or completion moments are rare, high-emotion places where the delight budget (bounce, a generous stagger, a longer beat) may be spent [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]).

### Errors, dead ends and loading screens

- A 404 page is the place to be quirky: a quiz, a movie character, a mini game that redirects [S-L19-063] ([[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]).
- Marketing sites sometimes use a branded loading screen: it adds a premium feel and covers heavy media, but must stay short [S-L19-069] ([[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]). Build recipes slide a black screen with the logo away after a hold, with the page content rising beneath it [S-L19-081] ([[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]]); [S-L19-071] ([[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]).

## Where they agree and disagree

- **Empty states.** [S-L19-044], [S-L19-047], [S-L19-053] and [S-L19-067] (all Kole Jain) agree with the research on the substance: say what is happening and give one action. [S-L19-053] separates first use from no results; the research adds the other kinds (user-cleared, no permission or error) and says loading is not an empty state (DC-L13-10).
- **When to show a loading indicator.** The sources say to respond at once [S-L19-003] [S-L19-052] and to show a wheel on long waits [S-L19-045]. The research adds thresholds: acknowledge input within about 50 ms, no indicator under about 1 s, a skeleton or spinner for 1-10 s, and determinate progress with a cancel option beyond 10 s (DC-L13-01, DC-L08-12). The two fit: the pressed state answers at once, and the spinner waits about a second [inferred].
- **Spinner motion.** The house rule is a fast, linear spin (`STD-easing-duration-15`, `STD-easing-duration-01`), and [S-L19-019] reserves linear easing for spinners and marquees. The Figma recipe in [S-L19-059] fakes a spinner with a springy curve (stiffness 550, damping 40); that is a prototype trick, and code should follow the standard.
- **Shimmer and reduced motion.** [S-L19-019] and [S-L19-055] recommend shimmer; the research notes that animated skeletons raise accessibility concerns (DC-L13-01), and the house rule keeps a gentle opacity change under reduced motion (`STD-accessibility-motion-02`).
- **What toasts are for.** [S-L19-047] routes warnings and errors through toasts. The research limits toasts to low-stakes confirmations and says a toast must never be the only channel for an error that blocks progress (DC-L13-09, DC-L08-18); the default of Q-form-04 is inline or banner first. The house standards cover how to build toasts, not this choice, so blocking errors can stay inline while `toast.error` handles non-blocking ones [inferred].
- **Toasts with actions (agree).** The research says never auto-dismiss a toast that carries an action (DC-L08-18), and the house standard now says the same: auto-close after 4000 ms except a toast with an action button, which stays until the person acts or dismisses it (`STD-components-toasts-drawers-15`). Sonner does this per toast with `duration: Infinity` [S-L19-021]. DC-L19-112 and DC-L19-128 carry it into Q-form-04's option text.
- **Optimistic UI.** [S-L19-047] and [S-L19-067] recommend it; the research lists it with a visible rollback on failure (DC-L13-01).
- **Loading screens.** [S-L19-069] warns they must stay short, while the recipes hold content back for over a second [S-L19-071] [S-L19-081]. The house limits let marketing motion run longer (`STD-easing-duration-06`, `STD-easing-duration-09`), so the length is a judgement call on marketing pages only; the recipes' ease-in-out curves still give way to ease-out, because the loading screen exits the page (`STD-easing-duration-01`, DC-L19-133) [inferred].
- **An all-done empty state.** Mercury's game after all bills are paid [S-L19-110] is the "user-cleared" kind of empty state in DC-L13-10 [inferred mapping], and a rare completion moment where `STD-when-to-animate-09` allows delight. DC-L19-126 keeps empty states people hit every day, such as inbox zero, subtle (`STD-when-to-animate-04`) [inferred split].
- **Nudges, not tours.** The to-do apps' empty-state nudge [S-L19-107] agrees with the first-use anatomy in [S-L19-053] and DC-L19-126: one focused hint rather than a tour.
- **Checking as people type.** A password checklist that ticks off requirements live [S-L19-107] is positive, in-place feedback (`STD-visual-details-49`). Q-form-02's default checks answers when a field loses focus; a requirement list that fills in as you type does not show errors early, so the two can sit together [inferred].
- **Delight in waits.** Animated loading and verification in onboarding [S-L19-107] fits the first-run delight budget (`STD-when-to-animate-09`); the same states in daily use stay fast and plain (`STD-easing-duration-15`, `STD-when-to-animate-04`) [inferred].
- **Success moments.** Sliding a check mark in rather than fading it [S-L19-059] is the kind of success detail the delight budget allows (`STD-when-to-animate-09`); after something people do many times a day, such as copying, it should stay subtle (`STD-when-to-animate-07`) [inferred].

## Decisions this informs

- **Q-state-08** (what people see while they wait): the research ladder ("nng-ladder"), skeletons for regions, and in-button spinners all appear in the sources.
- **Q-form-04** (where "Saved" appears): inline or banner by default versus toasts widely.
- **Q-form-03** (where error messages go) and **Q-form-05** (undo or confirm).
- **Q-form-02** (when forms check answers): a live requirement checklist on password fields [S-L19-107].
- **Q-pattern-04** (empty screens): "empty-kinds" matches the first-use and no-results split in [S-L19-053]; add the all-done case, which can reward people [S-L19-110], and nudges instead of tours on first use [S-L19-107].
- **Q-voice-02** (tone for errors, success and first use).
- **Q-img-04** (illustrations or a mascot in loading, error and empty states).
- **Q-color-15** (status colors) for success, warning, error and info toasts and messages.
- **Q-motion-07** (reduced motion): spinners and shimmer keep a gentle cross-fade.
- **Q-motion-08** (app sounds): sound only for meaningful moments.

## Visual examples worth showing

- A Sonner promise toast moving from loading to success in place, next to stacked toasts [S-L19-006] [S-L19-091].
- Two spinners at different speeds, the faster one feeling quicker [S-L19-012].
- Dub's empty dashboard with an animation, a message and a next step [S-L19-044].
- A first-use empty state and a no-results state side by side [S-L19-053].
- Skeleton loading with shimmer while an AI tool generates a wireframe, and a response streaming word by word [S-L19-055].
- An integration moving from loading to success, with the check mark sliding in through a mask [S-L19-059].
- An optimistic save: a quick-save window collapsing into a toast [S-L19-067].
- Quirky 404 pages: an interface quiz, a movie character and a snake game [S-L19-063].
- Mercury's game in place of an empty table once all bills are paid [S-L19-110].
- A password field ticking off requirements as you type, and an empty to-do list with a single nudge [S-L19-107].

## Open questions

- Error message wording is barely covered by these sources; the research has a separate card for it.
- Skeleton or spinner for a given wait? The sources name both without a rule; the research gives one (DC-L13-01).
- Screen reader announcements for loading and success (live regions) are not discussed, apart from the toaster's label and hotkey in the house standards.
- Should OpenDesigner scaffold empty, loading, success and error variants for every collection component by default? The research warns when an empty variant is missing (DC-L13-10) and, as an [inferred] Peak-End lint, when success and error variants are missing (L13 law table); DC-L19-125 proposes scaffolding all four.
