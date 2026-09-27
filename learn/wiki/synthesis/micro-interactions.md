---
type: synthesis
title: Micro-interactions
created: 2026-09-24
updated: 2026-09-27
sources:
  - ek-7-practical-animation-tips
  - ek-agents-with-taste
  - ek-building-a-toast-component
  - ek-building-an-animation-course
  - ek-the-magic-of-clip-path
  - ek-train-your-judgement
  - ek-you-dont-need-animations
  - eks-skills-animate-expo-recipes
  - eks-skills-animate-expo-skill
  - eks-skills-animate-recipes
  - eks-skills-animate-skill
  - eks-skills-animation-vocabulary-skill
  - eks-skills-apple-design-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-audit
  - eks-skills-mobile-native-skill
  - eks-skills-prototype-picker
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
  - 14h1VnkQvIc
  - AH_ugxmLeUM
  - B7k5rOgmOGY
  - EHwZzWd-OnQ
  - EcbgbKtOELY
  - HE4rLEQpiXY
  - If7iCPDy2vk
  - NtZeYmTMuo4
  - RCneB_MQ7qs
  - SfX43uIubj4
  - V3Omp1hm0Sg
  - VPeTgU7la34
  - Vy0KKvZJRH8
  - ZsP20PN14O0
  - eMMiLeo_UGI
  - eeN7yUcIWbw
  - gKM6b2EnW1k
  - ld1zhQMXxXU
  - nl8OFGdx75w
  - pGYLZyBE32o
  - tNMAFjzapOk
  - ulSOdTgoGeY
tags:
  - od-area-motion
---
# Micro-interactions

## In short

Micro-interactions are the small responses to a single action: a button that shrinks slightly when pressed, a check mark after copying, a tooltip, a loading state. Their main job is feedback, so the interface feels as if it is listening. Because people meet them constantly, they have to be tiny and fast, and things used all day may be better with no animation at all. Richer hover effects and playful touches belong on surfaces people see rarely, such as marketing pages, onboarding and success moments.

## House standards

- `STD-components-toasts-drawers-72`: show press feedback the instant the pointer or finger goes down, and commit the action on release.
- `STD-mobile-touch-05`: every pressable element scales to 0.97 while pressed (range 0.95-0.98) over 100-160ms ease-out on the web, 100-150ms in React Native.
- `STD-easing-duration-07`: press feedback 100-160ms; tooltips and small popovers 125-200ms.
- `STD-when-to-animate-07`: hover effects, list navigation, frequent toggles and row selection, seen tens of times a day, lose their animation or shrink to near-imperceptible.
- `STD-when-to-animate-06`: keyboard-initiated actions never animate.
- `STD-accessibility-motion-15`: every `:hover` animation sits inside `@media (hover: hover) and (pointer: fine)`; `:active` press feedback stays ungated.
- `STD-performance-properties-24`: when a hover effect flickers, animate a child instead of the hovered parent.
- `STD-enter-exit-origin-09` and `STD-enter-exit-origin-10`: tooltips enter from scale 0.97 and opacity 0 in 125ms from their trigger; only the first tooltip in a group is delayed, and neighbours open instantly.
- `STD-components-toasts-drawers-77`: hold-to-confirm fills over 2s linear while pressed and snaps back in 200ms ease-out.
- `STD-enter-exit-origin-29`: blur (about 2px) a crossfade that still shows two overlapping states after other fixes.
- `STD-enter-exit-origin-42`: show a tab's color change by clipping a duplicate of the tab list.
- `STD-easing-duration-15`: loading spinners spin fast.
- `STD-visual-details-59`: animate changing numbers with NumberFlow.
- `STD-springs-gestures-59`, `STD-springs-gestures-60` and `STD-springs-gestures-61`: feedback fires on the causal event, visual, sound and haptic in the same frame, and haptics only for meaningful moments, one per action.
- `STD-mobile-touch-62`: pick the haptic by moment (selection, snap, heavy or destructive, success or error).
- `STD-when-to-animate-09`: delight motion only on rare, high-emotion moments.

## What the sources teach

### Every action gets a response

- The interface should feel like it is listening: a form submit shows a loading state and copy-to-clipboard shows a success state [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]. The practitioner videos agree: every action should produce a response (spinners while data loads, success messages, small animations on scroll or swipe), and a chip that slides up is what confirms a copy [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]].
- Gray a button out as soon as it is pressed when the next screen may take a moment, and add a loading wheel for long waits [S-L19-045] [[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]. On macOS, every shortcut and interaction needs visible feedback, "micro animations, or at least a state change" [S-L19-067] [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]].
- The toast library's "big little details" include pausing the timer when the tab is hidden and filling the gaps between toasts so hover does not flicker [S-L19-006] [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]].

### Press feedback

- A subtle scale-down on press is an easy way to make an interface feel instantly more responsive: `scale(0.97)` on `:active` [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]] [S-L19-004] [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]], over 160ms ease-out and within 0.95-0.98 [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]] [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]] [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]].
- On mobile web, press feedback fires on pointer-down through `:active`, pairs `scale(0.97)` with a background change over 100ms, and stays within 100-160ms ease-out [S-L19-028] [[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]. In React Native: scale 0.97 over 120ms, with `hitSlop` and `pressRetentionOffset` [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]], on press-in in 100-150ms [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]].
- Highlight instantly on press, commit on release, and let people cancel by dragging away; feedback stays continuous during a gesture [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]. The course and the essay on restraint both use the subtle press scale-down as an example of motion that makes an interface feel more responsive [S-L19-007] [[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]] [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]].
- In the videos: the button shrinks when clicked while its label slides up on hover [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]], and "buttons should almost always have a small animation" [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]].

### Hover: judged by how often it is seen

- A hover effect used many times a day is probably best with no animation at all [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]. One judgement exercise hovers through an options list and judges it for frequent use [S-L19-011] [[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]]. Hover motion is gated to fine pointers because touch screens fire false hovers on tap [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]] [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]].
- The videos offer many hover ideas, mostly for websites: a masked button label that slides up while a circle and new label slide in [S-L19-069] [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]; an arrow that fades in to show a whole card is a link [S-L19-075] [[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]; a card image that zooms out while its call to action pops up [S-L19-065] [[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]; images that blur, enlarge and reveal text on hover, next to a call-to-action card with a static gradient stroke [S-L19-082] [[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]; hover rectangles, slide-up menus and icon labels built with Smart Animate [S-L19-059] [[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]; offset buttons whose offset animates on hover [S-L19-085] [[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]; feature images that zoom slightly on hover [S-L19-062] [[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]; a diagram whose items rotate and blur the rest when hovered [S-L19-050] [[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]].
- The same videos keep hover in proportion: simple, well-built hover effects are enough and should not go overboard [S-L19-066] [[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]; one well-built hover animation that demonstrates the product can beat complex scroll animation [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]; subtle hover effects on product visuals and bento tiles are a "level three" detail [S-L19-072] [[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]. One video adds small hover interactions to "pretty much everything" on a very simple site [S-L19-063] [[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]].
- On dashboards, chart hover shows the value in a bubble or dims the other bars [S-L19-047] [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]. Hover states and micro-interactions are commonly forgotten: filling the save icon and adding a red dot to the saved tab shows people where the recipe went [S-L19-045] [[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]].

### Tooltips

- Tooltips need an initial delay, but once one is open, neighbouring tooltips open with no delay and no animation [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]; later tooltips in a sequence skip both [S-L19-004] [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]].
- In one video, a tooltip appears only after the pointer has rested on an icon for a full second, with a slightly bouncy custom easing [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]].

### Loading and success

- A faster-spinning spinner makes loading feel faster [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]. AI loading indicators should be short, looping and fluid (three bouncing dots, a rotating star); skeletons shimmer where content will appear, and research steps fade in one by one [S-L19-055] [[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]].
- A check mark slides into its square through a mask rather than just fading in [S-L19-059] [[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]. When a clean hero needs more attention, a product-native "thinking" loader is preferred over decorative background shapes [S-L19-082] [[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]. Toasts can go beyond a slide-up with loading animations and celebratory success messages [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]].

### Crafting the state change

- When a button crossfades between two states and it still feels off, a 2px blur bridges them [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]].
- Clip-path builds comparison sliders, a mouse-driven text mask, a scroll-progress line and a tab indicator [S-L19-010] [[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]; hold-to-delete uses a clip-path fill [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]], 2s linear on press and 200ms ease-out on release [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]], recipes in [S-L19-017] [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]].
- A picker's active pill slides as spatial feedback, items scale to 0.97 on press, colors lift on hover, and the slide is enabled only after first paint so page load does not animate [S-L19-030] [[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]].
- Press-and-release and hold interactions need asymmetric timing, and toggles must be interruptible [S-L19-032] [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]].
- Named effects worth knowing: shake for errors, ripple from the tap point, text morph, number tickers, hold to confirm [S-L19-019] [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]].

### Haptics on mobile

- Haptics map to moments: selection, snap, heavy landing, success or error [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]; the recipes fire them on snapping home, arming a threshold and pressing a tab [S-L19-015] [[sources/eks-skills-animate-expo-recipes-emilkowalski-skills-skills-animate-expo-recipes-md|emilkowalski/skills: skills/animate-expo/RECIPES.md]].

### Delight, spent where it is rare

- A morphing feedback component is delightful only because people rarely use it [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]. The course site's hero illustrations respond to hover and click, and its logo slowly melts through animated SVG paths [S-L19-007] [[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]].
- The video catalogue of eleven micro-animations (button hover, shortcut hint, toasts, name tag, shimmer stroke, delayed tooltip, text pop-out, progress bar, card swipe, search expansion, upgrade hover) gives most of them a UX reason [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]].
- Other ideas: page indicators with a fluid, magnetic effect on swipe [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]; a carousel indicator that extends into a timer [S-L19-075] [[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]; a text wipe with a thin colored bar [S-L19-081] [[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]]; a blur effect that lifts a multi-select from good to great [S-L19-072] [[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]; a micro-interaction as the way to make a conventional layout your own [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]; a quick-save window that collapses into a toast while saving continues in the background [S-L19-067] [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]; Design Spells as a curated library of micro-interactions from large companies [S-L19-073] [[sources/eeN7yUcIWbw-20-top-underrated-web-design-resources-for-2025|20 Top Underrated Web Design Resources for 2025]]; word-level text animation and hover on almost everything to bring a simple page to life [S-L19-063] [[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]].

## Where they agree and disagree

- **Feedback on every action.** The videos [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]] [S-L19-045] [[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]] [S-L19-067] [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]] and Emil [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]] agree, and so does DC-L13-01 (acknowledge within 50ms, inline loading in the button).
- **Press feedback.** "Buttons should almost always have a small animation" [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]] and the shrinking button [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]] match `STD-mobile-touch-05`, as long as the animation is the press scale. Q-state-04 defaults to a tint overlay for pressed states (DC-L08-09's state layers), and standards.json records that nothing generated scales a pressed control. The tint and the scale can coexist [inferred].
- **Hover everywhere.** Hover on "pretty much everything" [S-L19-063] [[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]] clashes with `STD-when-to-animate-07` in product UI; on a rarely visited marketing page it is less of a problem [inferred]. Hover rules also need the fine-pointer gate (`STD-accessibility-motion-15`), which no video mentions.
- **Keyboard shortcuts.** Animating shortcut hints and shortcut results [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]] [S-L19-067] [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]] conflicts with `STD-when-to-animate-06` (keyboard-initiated actions never animate). The part both sides accept is an immediate state change, which [S-L19-067] [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]] itself offers as the alternative.
- **Tooltips.** The one-second delay with a bouncy easing [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]] is one video's opinion; the house delays only the first tooltip, then opens neighbours instantly without bounce (`STD-enter-exit-origin-10`, `STD-springs-gestures-05`).
- **Looping shimmer.** The video that builds a shimmer stroke adds a pause and play control [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]], because the shimmer moves faster on the edges and some people may not like that, not as an accessibility measure. DC-L13-01 notes that animated skeletons need reduced-motion handling. A stop control and reduced-motion handling for loops both fit `STD-accessibility-motion-01` and `STD-accessibility-motion-08` [inferred].
- **Chart hover.** Dimming other bars [S-L19-047] [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]] indicates state on data rather than decorating it, so it passes `STD-when-to-animate-11` [inferred].
- **Haptics.** DC-L04-26 (at most about six semantic events, used sparingly) agrees with `STD-springs-gestures-61` and `STD-mobile-touch-62`. Q-motion-09's default pairs OS-owned navigation with system haptics only and keeps a semantic map for products with frequent confirmations; that is narrower than the per-moment map, and standards.json records the conflict.

## Decisions this informs

- **Q-state-04** (how hover, pressed and disabled states look): add a press scale of 0.97 alongside whichever tint model is chosen, and gate hover by input.
- **Q-state-02** (how clearly controls show they can be pressed): press feedback on pointer-down is part of the answer for every level.
- **Q-color-20** and **Q-depth-06** (hover and press color changes and tints): the color change runs on `ease`, the transform on ease-out, within 100-160ms.
- **Q-state-05** (how the selected tab or item shows): a sliding pill or a clip-path color change is feedback, not decoration.
- **Q-state-08** (what people see while they wait): an inline spinner in the pressed button, spinning fast, and shimmer only with reduced-motion handling.
- **Q-form-04** (where "Saved" appears): toasts and inline confirmations such as the sliding copy chip.
- **Q-state-06** (risky actions): hold-to-confirm with slow press and fast release is one pattern for irreversible actions [inferred].
- **Q-motion-09** (haptics): the per-moment haptic map, one haptic per action.
- **Q-brand-04** (liveliness): decides how much of the delight catalogue is allowed, and only on rare moments.

## Visual examples worth showing

- The "Paste" buttons: one with the 0.97 press scale, one without [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]].
- A copy button whose confirmation chip slides up [S-L19-052] [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]].
- A tooltip group: the first tooltip delayed, the next ones instant [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]].
- A masked button hover: label slides up, a circle and a new label slide in [S-L19-069] [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]].
- Hold-to-delete: a clip-path fill over 2s linear, snapping back in 200ms [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]] [S-L19-010] [[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]].
- A tab indicator whose color change is a clipped duplicate [S-L19-010] [[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]].
- Two button states crossfading with and without a 2px blur [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]].
- A check mark sliding in through a mask after a spinner [S-L19-059] [[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]].
- AI loaders: bouncing dots, a rotating star, and research steps fading in one by one [S-L19-055] [[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]].
- A saved-recipe flow where the save icon fills and the tab gets a red dot [S-L19-045] [[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]].
- Chart hover that dims the other bars [S-L19-047] [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]].

## Open questions

- How should OpenDesigner classify each default component by frequency, so hover and press motion are removed or kept automatically?
- The engine has no press-scale token (conflict under `STD-mobile-touch-05`). Should press scale become a component token?
- What should the first tooltip's delay be? Only one video gives a value (1s [S-L19-079] [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).
- How should feedback for keyboard shortcuts be written into DESIGN.md so an agent shows a state change but no animation?
