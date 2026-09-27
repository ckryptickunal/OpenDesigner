---
type: synthesis
title: UI libraries
created: 2026-09-24
updated: 2026-09-24
sources:
  - adev-home
  - ek-7-practical-animation-tips
  - ek-building-a-drawer-component
  - ek-building-a-toast-component
  - ek-the-magic-of-clip-path
  - eks-performance-cheatsheet
  - eks-readme
  - eks-skills-animate-expo-skill
  - eks-skills-animate-skill
  - eks-skills-ask-sonner-api
  - eks-skills-ask-sonner-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-improve-animations-skill
  - eks-skills-pick-ui-library-skill
  - sonner-getting-started
  - sonner-home
  - sonner-toast
  - vaul-api
  - vaul-getting-started
  - xHD01_Onac0
tags:
  - od-area-components
---
# UI libraries

## In short

A UI library is ready-made code for a common part, like a toast, a dialog or a code input, so nobody has to rebuild its tricky details by hand. The house rule is to pick from Emil Kowalski's short curated list, one library per task: base-ui for dialogs, menus and selects, cmdk for command menus, Sonner for toasts, input-otp for code inputs, and motion only when you need springs, layout or exit animations. Check what the project already has installed first, and do not swap a working library out unless asked. Never hand-roll a toast, dropdown or dialog, and never add a heavy animation library for a simple hover or fade.

## House standards

**Choosing a library**
- `STD-visual-details-55` (must): Pick libraries from the curated list.
- `STD-visual-details-56` (must): Reuse installed libraries first.
- `STD-visual-details-57` (must): Never hand-roll standard components.
- `STD-accessibility-motion-16` (must): Build overlays on accessible primitives.
- `STD-process-review-taste-11` (must): Recon before judging or designing motion. (recon includes the motion and component libraries in the stack)

**Named picks**
- `STD-visual-details-59` (must): Animate numbers with NumberFlow.
- `STD-visual-details-61` (must): Shared state in zustand.
- `STD-visual-details-62` (must): clsx or cva for conditional classes.
- `STD-performance-properties-17` (must): Virtualize long lists and large tables.
- `STD-components-toasts-drawers-35` (should): Toast API is a plain function.
- `STD-components-toasts-drawers-24` (should): Headless toast for the design system.
- `STD-components-toasts-drawers-38` (should): Build drawers on an accessible dialog.

**Animation tools**
- `STD-performance-properties-13` (must): Pick the cheapest animation tool.
- `STD-performance-properties-14` (should): Use IntersectionObserver instead of adding Motion.
- `STD-performance-properties-09` (must): Motion: animate the full transform string.
- `STD-process-review-taste-65` (should): Learn CSS animation before Motion.
- `STD-mobile-touch-33` (must): Use Gesture Handler, never PanResponder.
- `STD-mobile-touch-41` (must): Use native pieces instead of JS rebuilds.

**Using a library well**
- `STD-visual-details-26` (must): Use and extend existing tokens.
- `STD-process-review-taste-60` (should): Documentation is part of the product.

## What the sources teach

### The curated list

Emil Kowalski's pick-ui-library skill is a lookup of one library per task [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]):

| Task | Library |
| --- | --- |
| Unstyled, accessible dialogs, popovers, menus, selects | base-ui |
| Command menus (⌘K) | cmdk |
| Toasts and notifications | Sonner |
| One-time password and code inputs | input-otp |
| Control panels and tweak GUIs | Leva (dialkit as the alternative) |
| General animation: springs, layout, enter and exit | motion (Framer Motion) |
| Animated numbers | NumberFlow |
| Animated text | torph |
| 3D globes | Cobe |
| Dynamic OG images | Satori |
| Syntax highlighting | shiki |
| Live, streaming charts | Liveline |
| All other charts | recharts |
| Drag and drop | dnd kit |
| Virtualized long lists and tables | Virtuoso |
| Shared state | zustand |
| Conditional classes / typed variants | clsx / cva |
| Theme switching without a flash | next-themes |

- How to use it: identify the task rather than the library the person named ("show a dropdown" is a primitives task, so base-ui); read `package.json` first and use a listed library that is already there; if a competitor is installed (react-window instead of Virtuoso), flag the pick but do not swap it unasked; recommend one library in one sentence, not a menu; and say plainly when a task is not on the list [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).
- The list names the hand-rolled patterns to replace: hand-built toasts, `<div>` dropdowns and dialogs, numbers animated by re-rendering text, lists of 1,000+ rows rendered directly, shared state passed through a web of `useState` props, and class-name ternaries three conditions deep [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).
- The list is explicitly taste-driven, gives no performance or bundle-size comparisons, is React-centric [inferred from its package.json, className and Tailwind cues], and is pinned to one commit of the skills repo [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]). The skill exists so agents stop hand-rolling toasts or installing abandoned packages [S-L19-014] ([[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]]).
- When a task needs a component (a toast, a drawer, a command menu, a dropdown) rather than an animation, stop and pick a library; hand-rolling is how a `<div>` dropdown ends up with no focus management [S-L19-018] ([[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]).

### Do not add an animation library you do not need

- Reach for motion only for springs, layout animations, exit animations or gesture-driven values; a simple hover or fade is a plain CSS transition [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).
- Learn CSS transforms, transitions and keyframes first, then move to Motion for more complex work [S-L19-002] ([[sources/adev-home-animations-dev|animations.dev]]).
- Framer Motion is heavy, so if the project does not already use it, detect when something scrolls into view with the Intersection Observer API instead [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- Motion's `x`, `y` and `scale` shorthand props can drop frames under load; animate the full `transform` string instead [S-L19-013] ([[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]]) [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]). The Web Animations API gives programmatic control with no library at all [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).
- Before judging motion, note which motion libraries (Motion, React Spring, GSAP, plain CSS, the Web Animations API) and component libraries (Radix, Base UI, shadcn/ui) the project uses [S-L19-027] ([[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]]).
- For React Native the dependency list is Reanimated with worklets, Gesture Handler, Expo Router (for navigation, sheets, native tabs and menus), expo-haptics, keyboard-controller, lottie-react-native and Skia [S-L19-016] ([[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]).

### Working with primitives

- Radix and Base UI already skip the delay for neighboring tooltips, Base UI can also skip their animation, and both expose the trigger's `transform-origin` as a CSS variable [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]).
- Clip-path tabs in production should sit on an accessible tabs primitive such as Radix Tabs [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- Vaul is built on Radix's Dialog and copies its compound API, so it feels familiar [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]). Vaul's docs show it installed as a package and composed from nine parts [S-L19-095] ([[sources/vaul-getting-started-getting-started-vaul|Getting Started – Vaul]]) [S-L19-093] ([[sources/vaul-api-api-reference-vaul|API Reference – Vaul]]), but the project's source list records that Vaul's README calls it unmaintained, so it is a craft reference, not a dependency to recommend.

### Sonner as a library done well

- Sonner is installed as a package (`npm install sonner` on the homepage, `pnpm i sonner` in Getting Started) and imported as `Toaster` and `toast` [S-L19-088] ([[sources/sonner-home-sonner|Sonner]]) [S-L19-087] ([[sources/sonner-getting-started-getting-started-sonner|Getting Started – Sonner]]).
- For a design system, render the toast headless with `toast.custom()`, wrap it in your own `toast()` function, and skip the halfway rungs such as `unstyled` or stacks of `!important` classes [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]) [S-L19-021] ([[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]).
- What made it win: one `<Toaster />` and a `toast()` callable anywhere with no hooks or context, an API shape borrowed from react-hot-toast because it was already very good, a distinctive name, a launch built around its signature stacking animation, and interactive docs with copyable code [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]). The skills turn this into general advice: minimal setup, excellent defaults before options, and edge cases handled invisibly [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).

### AI and component marketplaces

- 21st.dev offers components made with or for AI, as code or as a prompt to paste; when prompting an AI for UI, always name an icon library or it falls back to emojis [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).

## Where they agree and disagree

- **Which primitive.** The curated list names base-ui [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]), while Emil Kowalski's own drawer and tabs are built on Radix [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]) [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]). `STD-accessibility-motion-16` accepts either. OpenDesigner's research (DC-L08-03) defaults React web to shadcn on Base UI or React Aria; React Aria is not on Emil Kowalski's list.
- **Drawers.** `STD-visual-details-57` treats a drawer as a component to take from a library, but the curated list has no drawer entry [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]) and Vaul is unmaintained. This is a real gap.
- **One pick or a menu.** The skill forbids presenting a menu of libraries when the list has an answer [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]), while OpenDesigner's interview offers options (Q-comp-01 asks for a build approach, not a library). The two fit if Q-comp-01 decides the approach and the list then names the library [inferred].
- **Composition.** Vaul's compound parts [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]) match DC-L08-04's default of compound parts for containers such as dialogs and menus, and props for leaf components such as buttons.
- **Popularity figures.** The sources disagree: over 40 million weekly Sonner downloads [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]), "13M+" [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]), and 90 million a week for Sonner and Vaul combined [S-L19-002] ([[sources/adev-home-animations-dev|animations.dev]]). All are self-reported and undated, so none should be quoted as fact.
- **Scope.** DC-L08-01 lists about 25 core components (dialog, popover, menu, tabs, tooltip and so on) and about 25 extended ones (toast, drawer, date picker). The curated list covers only some of them; date pickers, for example, are not on it.

## Decisions this informs

- **Q-comp-01** (bare parts, a copy-in kit, native controls or a full system): React web starts from accessible headless primitives (base-ui).
- **Q-comp-03** (settings or smaller parts): compound parts for containers, as Radix and Vaul do.
- **Q-tool-02** (how engineers use the system): the headless option fits the house picks [inferred].
- **Q-plat-08** (what the UI is built with): the curated list only covers React; other stacks need their own picks.
- **Q-viz-01** (chart kit): recharts, or Liveline for live data.
- **Q-theme-01** (light and dark): next-themes switches themes without a flash.
- **Q-dist-04** (docs): interactive examples with copyable code, like Sonner's.
- **Q-dist-02** (how AI tools read the system): agent skills such as pick-ui-library steer AI toward the right libraries [inferred].
- **Q-icon-01** (icon set): the chosen set is what an AI prompt should name [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).

## Visual examples worth showing

- The curated list as a single lookup card, grouped by task.
- A "mismatch" sheet: each hand-rolled pattern next to the library that replaces it [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).
- A project that uses react-window, with Virtuoso flagged but not swapped [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).
- The Sonner docs page: grouped sidebar, Preview and Code tabs, a Copy Code link and a live "Render toast" button [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]) [S-L19-091] ([[sources/sonner-toast-toast-sonner|Toast – Sonner]]).
- A simple hover done with a CSS transition next to the same hover pulling in a motion library, to show the cost.

## Open questions

- Which library should build drawers, now that Vaul is unmaintained and the curated list has none?
- What are the equivalent picks for SwiftUI, Compose, Vue and other non-React stacks?
- When a project already uses Radix, should OpenDesigner still recommend base-ui for new primitives?
- How often should OpenDesigner re-check the list, since it is pinned to one commit of the skills repo?
- Which library should cover date pickers and other extended components the list does not name?
