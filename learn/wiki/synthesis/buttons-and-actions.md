---
type: synthesis
title: Buttons and actions
created: 2026-09-24
updated: 2026-09-28
sources:
  - 14h1VnkQvIc
  - 66oOi9OLMCw
  - 9ypqs_2fAl8
  - ADaQuZS04Rc
  - AH_ugxmLeUM
  - ARq1bx3Sfg8
  - BvbFPzLjWcU
  - EOcY3hPMQkk
  - EcbgbKtOELY
  - Gfsd8NNuD9g
  - HE4rLEQpiXY
  - Lp6ey4AyDzA
  - PDcQJOPby1k
  - V3Omp1hm0Sg
  - Vy0KKvZJRH8
  - Yr2uIcFZDDQ
  - ZsP20PN14O0
  - adev-changelog
  - eMMiLeo_UGI
  - ek-7-practical-animation-tips
  - ek-agents-with-taste
  - ek-you-dont-need-animations
  - eks-skills-animate-expo-skill
  - eks-skills-animate-recipes
  - eks-skills-apple-design-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-audit
  - eks-skills-mobile-native-skill
  - eks-skills-review-animations-standards
  - gKM6b2EnW1k
  - goWOAFqJHpA
  - ld1zhQMXxXU
  - lkKGQVHrXzE
  - neE6wOuBIP8
  - pGYLZyBE32o
  - sonner-toast
tags:
  - od-area-components
---
# Buttons and actions

## In short

Buttons are how people act, so each area of a screen needs one clear main action and quieter secondary ones. The house standards make every button answer the moment it is pressed: it shrinks to about 97% of its size within 100-160ms, and the action itself fires when the finger or mouse lets go. Tap targets are at least 44pt on iOS and 48dp on Android, and hover effects only run on devices with a real mouse. Mistakes should be easy to undo; truly destructive actions get a deliberate confirmation, such as a hold-to-confirm button. Practitioner videos add a visual order: one filled primary button per area, quieter secondary buttons, and red for delete.

## House standards

**Press feedback**
- `STD-mobile-touch-05` (must): Press feedback scales to 0.97, briefly.
- `STD-components-toasts-drawers-72` (must): Feedback on press, commit on release.
- `STD-easing-duration-07` (must): Duration budget for each element. (button press: 100-160ms on the web, 100-150ms on iOS and Android)
- `STD-when-to-animate-07` (must): Remove or shrink motion seen tens-of-times daily.
- `STD-springs-gestures-59` (must): Feedback fires on the causal event.
- `STD-mobile-touch-67` (should): Same press scale on iOS and Android.
- `STD-enter-exit-origin-29` (must): Blur a crossfade that won't settle.

**Touch and hover**
- `STD-mobile-touch-09` (must): Touch targets 44pt on iOS, 48dp on Android.
- `STD-mobile-touch-03` (must): Remove the tap highlight flash globally.
- `STD-mobile-touch-06` (must): Remove the tap delay on tappables.
- `STD-mobile-touch-08` (should): Let a drifting finger keep its press.
- `STD-mobile-touch-17` (must): Make controls unselectable, keep content selectable.
- `STD-accessibility-motion-15` (must): Gate hover motion to fine pointers.
- `STD-mobile-touch-30` (must): Redesign hover affordances for touch.

**Risky actions**
- `STD-visual-details-40` (must): Undo for slips, confirm only destruction.
- `STD-components-toasts-drawers-77` (must): Hold to confirm: slow press, fast release.
- `STD-easing-duration-12` (must): Slow deliberate phase, snappy response.

**Consistency and feedback**
- `STD-visual-details-36` (must): Same look, same behaviour.
- `STD-visual-details-49` (must): Feedback on every action.
- `STD-visual-details-62` (must): clsx or cva for conditional classes.

## What the sources teach

### One main action per area

- A header should only ever have one primary call to action. If a second button must stay, remove its background so the two stop competing; otherwise drop it [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- Kole Jain grades importance by darkness: from ghost buttons up to black buttons with white text, with most multi-purpose buttons at about 90-95% white [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]). This scale comes from one video.
- Sidebar links are ghost buttons (no background until hover), and the same ghost style works as a secondary button beside a primary one [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- In a navigation bar, give the sign-up action and the key links more weight (for example an outline), and give the hero button the same label as the nav button when both go to the same place [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]). Kole Jain's redesigned hero carries a primary and a secondary call to action [S-L19-049] ([[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]).
- Chips are not buttons: they are always thinner, almost never use the primary color, and have vertical padding of half or a quarter of their horizontal padding. When cards repeat, the whole card can be the link; keep an explicit button when the action is specific, such as "Try it out". A pricing button moved higher up the card becomes an outline button so the hierarchy holds [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- Keep the action the product's success depends on always visible; Spotify Wrapped's share button is the example. Use one share button that opens three scopes rather than two similar buttons side by side [S-L19-076] ([[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]).
- Only offer actions that make sense for the object: "lock card" on a credit card, not "receive" [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- A call to action does not have to be a button: a search or prompt bar people can type into works as the hero action of an AI product [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]), and a dealer search bar ends a car site [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]). The same site keeps its bright accent for the button's hover state only [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).
- Buttons that do the same job must match in size, corner radius and style [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]), and Linear keeps its buttons, spacing and text styles identical in every context [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- A crowded card is better fixed by lining its buttons up on a new edge than by hiding actions in a corner menu [S-L19-080] ([[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]).

### What the main button says

- A call to action can name what the person is committing to instead of a plain "Continue": Duolingo's product team changed "continue" to "commit to my goal" and called it a massive win, and the video says more apps now frame the button as a promise to yourself [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]). The paywall designer Jonathan Parra finds labels that name what the person is doing hit or miss, so he tests them [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Parra adds a "no commitment, cancel anytime" subtitle under a paywall's main button, which he says always seems to lift conversion a little, and a right chevron on the button: most winning paywalls he has seen have one, though he has never tested the chevron on its own [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).

### Size and shape

- Steve Schoger likes hero buttons with 14px text and a 38px height reached through padding, and a smaller 28px nav button so it does not compete (24px felt too small). Buttons side by side must be the same height, so he wraps a ringed button to stop it growing 2px taller, draws edges with a 10% gray-950 ring instead of a solid border, and tries pill buttons across the whole site [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]). These are one designer's preferences.
- A padding guideline of "double the height for the width" is offered, though the wording is ambiguous [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- Small buttons get a 44px minimum hit area built with a pseudo-element [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]). In React Native, keep 44x44pt on iOS and 48dp on Android with `hitSlop` [S-L19-016] ([[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]).
- Do not pair sharp-cornered images with rounded buttons on the same page [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).

### States

- Every button needs at least four states (default, hover, pressed, disabled), plus a loading state with a spinner when needed [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- Hover is slightly lighter or brighter, pressed is slightly darker, and disabled is desaturated; a light gray button with white text reads as disabled in light and dark mode. Phones have no hover, so a press state does that job [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- When the next screen takes a moment, gray the button out as soon as it is tapped and add a spinner for long waits, so the tap does not look missed [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- Hover and click states alone do not confirm an action such as copying; a small chip that slides up does [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- Show keyboard-shortcut reminders on the buttons they trigger [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]), and Kole Jain suggests a small animated hint so shortcuts are easier to remember [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]). That is one video's idea, and `STD-when-to-animate-06` limits it: whatever the shortcut itself triggers happens instantly, so any animated hint belongs on the button or in onboarding, not on the shortcut's result [inferred].

### Press feedback

- Scale a button to 0.97 on `:active` so the interface feels instantly responsive [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]) [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]). A subtle press scale is one of the purposes that justifies motion at all [S-L19-012] ([[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]).
- The recipe is `transform: scale(0.97)` with a 160ms ease-out transition, applied to the whole button so its label and icons scale too. `:active` stays ungated; only hover is gated [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]). Apple-style guidance uses 100ms ease-out, shows the pressed state on pointer-down and commits on release [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]). The audit and review skills keep press feedback at 100-160ms and the scale between 0.95 and 0.98 [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]) [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]) [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]) [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).
- On the mobile web: remove the tap highlight once, globally; add `touch-action: manipulation` to every tappable element so the click fires without iOS's 300ms wait; make control labels unselectable; style `:active` or listen to `pointerdown`, never only `click`; and put every `:hover` style inside `(hover: hover) and (pointer: fine)`, because touch browsers leave hover stuck after a tap [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- In React Native, a Pressable scales to 0.97 in 100-150ms, gives feedback on press-in and commits on press-out, keeps a press alive when the finger drifts (`pressRetentionOffset`), and uses the same scale on both platforms unless the app is Material-styled. A destructive action fires a medium haptic [S-L19-016] ([[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]).
- When a button swaps between two states and the crossfade still looks like two objects, add 2px of blur during the change [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]); the skill's version blurs the content by 2px and fades it to 0.7 over 200ms [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).

### Hover and motion on marketing buttons (practitioner opinion)

- Kole Jain says buttons should almost always have a small animation [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]). He prefers designing hover and pressed states with motion (the label slides up inside a mask on hover, the button shrinks while pressed) instead of picking colors at the last minute [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).
- Bigger hovers include a masked label slide with a circle that morphs into a rectangle, or a simpler text-and-background swap. A call to action that moves to the cursor is the best use of mouse effects, used sparingly [S-L19-069] ([[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]).
- A call to action that appears on hover is one of the "level four" details of a polished landing page [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]). Inner and outer shadows can make tactile, raised buttons [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).

### Dangerous actions

- Destructive actions are red whatever the brand color; a brand-colored delete button hides its danger [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]) [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- In a delete dialog, Kole Jain gives the delete button the primary fill, preferably red, and demotes cancel to no background, a border or reduced opacity [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- In another video he praises macOS dialogs, where the primary color always marks the non-destructive action, because people can trust that convention [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- For high-impact or irreversible actions, such as sending an email in Resend or buying crypto, a slider that must be dragged all the way across is much harder to trigger by accident than a button [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]).
- Hold-to-confirm: an overlay clipped to `inset(0 100% 0 0)` fills to `inset(0 0 0 0)` over 2s linear while held, snaps back over 200ms ease-out on release, and the button scales to 0.97. Pressing is slow and deliberate; the release is snappy [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]) [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]) [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]) [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]). The animations.dev course builds a "Hold to Delete" exercise the same way [S-L19-001] ([[sources/adev-changelog-animations-dev|animations.dev]]).
- Give easy undo for slips and keep confirmation dialogs for truly destructive, irreversible actions, because too many confirmations train people to click through [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]). Symmetric press-and-release timing on these controls is flagged as a finding [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]).

### Gestures and contextual actions

- A swipe can replace a button (swipe to add a friend, swipe to delete in Gmail), but keep a visible button or a long-press menu for people who do not know the gesture [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]).
- Show actions when they are needed: a note editor hides the nav bar and shows formatting and sharing, a long press blurs the screen and lists the item's actions [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]).

### Buttons inside toasts

- A Sonner toast's `action` is a primary button and `cancel` a secondary one; both close the toast unless the action calls `event.preventDefault()` [S-L19-091] ([[sources/sonner-toast-toast-sonner|Toast – Sonner]]).

## Where they agree and disagree

- **Press feedback.** The sources agree that a press should be felt: Emil Kowalski scales to 0.97 [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]), Kole Jain shows buttons that get smaller when clicked [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]) and uses a darker press color on phones [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]), and the mobile-web sample pairs the scale with a darker background [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- **Primary role in a delete dialog.** Kole Jain disagrees with himself: delete gets the red primary fill in one video [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]), while in another the primary color marks the safe choice [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]). OpenDesigner's research leans toward the second: DC-L13-18 and DC-L08-06 cite Apple's rule that a destructive button never gets the primary role, and DC-L13-08 suggests Cancel as the safe default (a point that card marks as inferred). DC-L08-06 still allows solid red, but only in the final confirmation step. One way to honor both is a red fill for the delete button while the default focus and Enter go to Cancel [inferred].
- **Hover motion.** Kole Jain wants small button animations almost everywhere [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]), while the house standards treat hover as something people see tens of times a day and keep it near-imperceptible or remove it (`STD-when-to-animate-07`). His elaborate hovers are all on marketing sites [S-L19-069] ([[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]), and the skills exempt marketing pages from the speed rules [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]), so the conflict mostly disappears if rich hovers stay on marketing pages [inferred].
- **Hiding actions.** One Kole Jain video says not to fix a crowded card by hiding actions in a corner menu [S-L19-080] ([[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]); another collapses busy card buttons into a three-dot menu [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- **Guarding risky actions.** The slider [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]) and hold-to-confirm [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]) both make accidents hard. OpenDesigner's research (DC-L13-08) covers undo, confirmation dialogs and type-to-confirm, but not these two, so they are new options.
- **Disabled and pending.** Kole Jain grays a button out on tap while the next screen loads [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]). DC-L13-01 agrees that a loading state should block repeat clicks, but DC-L08-10 advises against disabling submit buttons and suggests `aria-disabled` with helper text when an action cannot run.
- **One primary per area.** Kole Jain's single header call to action [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]) matches DC-L13-18 (one high-emphasis action per region) and DC-L08-05 (one primary per view).
- **Button height.** Steve Schoger's 38px hero and 28px nav buttons [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]) are smaller than Q-space-04's default of 32, 40 and 48. DC-L03-12 allows a small visual size as long as the hit area stays large, which `STD-mobile-touch-09` also requires on touch.
- **Icons in buttons.** Steve Schoger strips decorative icons from secondary hero buttons [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]), while the "level three" landing page adds an icon to the primary call to action [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]). DC-L13-18 recommends text plus an icon for key actions.
- **State colors.** Kole Jain's lighter hover and darker press [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]) fit either option in DC-L08-09 (see-through overlays or a token per state). For the pressed state, `STD-mobile-touch-05` records that it supersedes DC-L08-09: a press also scales the button to 0.97, not only its color.
- **Button labels.** "Commit to my goal" [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]) fits DC-L13-13's command labels (2-4 words, verb first). It pulls against DC-L06-22's consistent flow vocabulary (Get Started, Continue or Next, Done) at the one step where the person commits [inferred]. Both label findings are reported wins without test details, and Parra himself calls them hit or miss [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- **Trailing chevron.** Parra's chevron [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]) is a trailing icon, one of Q-state-07's options. It is an untested pattern he has noticed, not a result.

## Decisions this informs

- **Q-state-01** (how many button styles, how many main buttons per area): one filled primary per area, a ghost or outline secondary, and a danger style.
- **Q-state-02** (how clearly buttons look clickable): signifiers such as press states, active highlights and tooltips [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- **Q-state-04** (how hover, pressed and disabled get their look): lighter hover, darker press, desaturated disabled; hover only on fine pointers; the `press-scale` option matches `STD-mobile-touch-05`.
- **Q-state-06** (how risky actions look): red for destructive actions, with the primary-role question above.
- **Q-state-07** (icons in buttons): the sources split on decorative icons; a trailing chevron on a paywall's main button is one practitioner's untested habit [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- **Q-state-08** (what people see while waiting): a grayed or spinning button for short waits.
- **Q-form-05** (undo or confirm): undo first, and a slider or hold-to-confirm for destructive actions. `STD-visual-details-40` settles this question and rules out the `confirm` option (an "Are you sure?" box instead of undo).
- **Q-space-03** (tap target size): a 44px hit area even when the button looks smaller.
- **Q-space-04** (button and input heights): practitioner sizes of 38px and 28px compared with the 32-40-48 default.
- **Q-shape-01** (corner softness): pill buttons applied everywhere, and matching image and button corners.
- **Q-depth-01** (how surfaces stand out): an outer ring at low opacity instead of a solid border [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- **Q-motion-02** (durations): press feedback is the shortest step, 100-160ms.
- **Q-motion-09** (haptics): a medium haptic when a destructive action fires.
- **Q-voice-06** (writing rules per component): `verb-first` labels, and whether the key commitment step may break the `flow-vocab` "Continue" [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).
- **Q-token-01** (layers of named values): `cva` for real button variants (`STD-visual-details-62`) [inferred].

## Visual examples worth showing

- Two "Paste" buttons, one scaling to 0.97 on press and one not [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]).
- A hold-to-delete button whose fill sweeps across over 2s and snaps back in 200ms [S-L19-017] ([[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]).
- The two delete dialogs side by side: red primary delete with a demoted cancel [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]), and the macOS dialog where the primary color marks the safe action [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- A header with two filled buttons, then the same header with the second button's background removed [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- The ghost-to-black importance scale [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- A state sheet: default, lighter hover, darker press, light-gray disabled, in light and dark mode [S-L19-051] ([[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]).
- A two-state button crossfade with and without 2px blur, paused halfway [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]).
- A button stuck in its hover state after a tap on a phone, and the fixed version [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- Resend's swipe-to-send slider [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]).
- The masked label slide-up hover [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]) [S-L19-069] ([[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]).
- The same button labeled "Continue" and "Commit to my goal" [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]), and a paywall button with a right chevron and a "no commitment, cancel anytime" subtitle [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- A ringed button and a plain button at the same height [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).

## Open questions

- In a destructive confirmation, which button gets the primary role and the default focus?
- How much hover motion is allowed on product screens, as opposed to marketing pages?
- Should buttons ever be disabled, or only marked pending and explained?
- Are 28px desktop buttons acceptable when a pointer is the main input, provided touch devices get a 44px hit area?
- Should the button that asks for a commitment get its own label rule, or keep the flow's usual "Continue"?
- Does OpenDesigner need a separate chip component and token set, given how often the sources separate chips from buttons?
