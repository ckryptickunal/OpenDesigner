---
type: source
title: "emilkowalski/skills: skills/pick-ui-library/SKILL.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-pick-ui-library-skill
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/pick-ui-library/SKILL.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - ui-libraries
  - library-selection
  - react
  - frontend
  - sonner
  - base-ui
  - motion
  - charts
  - virtualization
  - state-management
  - tailwind
  - dark-mode
---

# emilkowalski/skills: skills/pick-ui-library/SKILL.md

## Metadata

- Page ID: `eks-skills-pick-ui-library-skill`
- Publisher: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/pick-ui-library/SKILL.md

## Summary

This is Emil Kowalski's pick-ui-library agent skill: a lookup table that matches a frontend task to one library from his curated, taste-driven list, covering UI primitives, command menus, toasts, OTP inputs, animation, number and text animation, charts, drag and drop, virtualization, state, class names, variants and theme switching. It sets a short procedure: identify the task rather than the library the person named, check package.json first, recommend a single library in one sentence, and say plainly when the task falls outside the list. It also warns against churning an installed competitor without being asked. A closing list of common mismatches names the hand-rolled patterns (hand-built toasts, div-based dialogs, re-rendered number text, huge unvirtualized lists, prop-drilled state, nested className ternaries) that should be replaced by a listed library. For a design system it fixes the default building blocks and states when a heavier tool is not needed, such as plain CSS transitions for a simple hover or fade.

## Key Ideas

- Choose a library by the underlying task, not by the library name the person happened to mention.
- Look at package.json before recommending anything; if a listed library is already installed, use it.
- If a competitor is already installed, mention the recommended pick but do not swap dependencies unless asked.
- Give one library and a one-sentence reason, not a menu of options, whenever the curated list has a clear answer.
- Stay inside the curated list; leave it only when asked or when the task is not covered, and say so explicitly.
- Unstyled, accessible primitives (base-ui) replace hand-built dropdowns and dialogs with manual focus handling.
- Use a general animation library only for springs, layout animations, exit animations and gesture-driven values; a simple hover or fade is plain CSS.
- Chart choice has one split: live, time-scrolling data uses Liveline, and everything else uses recharts.
- clsx is for ad-hoc conditional classes; cva is for components with real variants (size, intent, state) that deserve a typed API, and the two compose.
- Long lists of 1,000+ rows should be virtualized with Virtuoso before resorting to pagination hacks.
- Shared state spread across per-component useState and props should move to zustand.
- Theme switching and dark mode should use a tool that avoids a flash on load (next-themes).
- Toasts built by hand or with a modal library are a mismatch to catch; Sonner exists for exactly that job.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Curator of the library list the skill draws on; the skill lives in the emilkowalski/skills repo.
- [[entities/pick-ui-library|pick-ui-library]] (tool): The agent skill itself; a lookup that only runs when explicitly invoked.
- [[entities/base-ui|base-ui]] (library): Pick for unstyled, accessible UI components such as dialogs, popovers, menus and selects.
- [[entities/cmdk|cmdk]] (library): Pick for command menus (⌘K palettes).
- [[entities/sonner|Sonner]] (library): Pick for toasts and notifications; linked at sonner.emilkowal.ski, so likely Emil Kowalski's own library [inferred].
- [[entities/input-otp|input-otp]] (library): Pick for one-time password and verification code inputs.
- [[entities/leva|Leva]] (library): Pick for customizable GUIs and control panels.
- [[entities/dialkit|dialkit]] (library): Named alternative to Leva for control panels.
- [[entities/motion-framer-motion|motion (Framer Motion)]] (library): Pick for general-purpose animation: springs, layout animations, enter and exit.
- [[entities/numberflow|NumberFlow]] (library): Pick for animating numbers such as counters, prices and stats; handles digit transitions.
- [[entities/torph|torph]] (library): Pick for animated text components.
- [[entities/cobe|Cobe]] (library): Pick for 3D globes.
- [[entities/satori|Satori]] (library): Pick for dynamic OG images, turning HTML/CSS into SVG/PNG.
- [[entities/shiki|shiki]] (library): Pick for syntax highlighting.
- [[entities/liveline|Liveline]] (library): Pick for real-time or streaming charts that scroll with time.
- [[entities/recharts|recharts]] (library): Pick for general charts, static or interactive dashboards.
- [[entities/dnd-kit|dnd kit]] (library): Pick for drag and drop.
- [[entities/virtuoso|Virtuoso]] (library): Pick for virtualization of long lists and large tables.
- [[entities/react-window|react-window]] (library): Named as an example of an installed competitor to Virtuoso that should not be churned unasked.
- [[entities/zustand|zustand]] (library): Pick for state management.
- [[entities/clsx|clsx]] (library): Pick for constructing className strings conditionally.
- [[entities/cva|cva]] (library): Pick for type-safe, variant-driven styling with Tailwind.
- [[entities/next-themes|next-themes]] (library): Pick for theme switching and dark mode with no flash on load.
- [[entities/tailwind|Tailwind]] (tool): The styling system cva's variant-driven styling targets.

## Topics

- [[topics/ui-libraries|UI libraries]]: Gives a curated, one-pick-per-task library list for frontend work and a procedure for recommending from it without churning existing dependencies.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Covers className composition (clsx, cva), state management (zustand), virtualization, and using plain CSS transitions instead of an animation library for simple hovers and fades.
- [[topics/toasts-and-notifications|Toasts and notifications]]: Sonner is the pick for toasts; building toasts by hand or with a modal library is a mismatch to catch.
- [[topics/modals-and-popovers|Modals and popovers]]: base-ui is the pick for dialogs, popovers, menus and selects, replacing div-based versions with manual focus handling because it handles accessibility, focus trapping and dismissal.
- [[topics/forms-and-inputs|Forms and inputs]]: input-otp is the pick for one-time password and verification code inputs.
- [[topics/dashboards-and-data-display|Dashboards and data display]]: Liveline for live, time-scrolling charts, recharts for all other charts, and Virtuoso for long lists and large tables of 1,000+ rows.
- [[topics/gestures-and-drag|Gestures and drag]]: dnd kit is the pick for drag and drop; motion is the pick when gesture-driven values are needed.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: next-themes is the pick for theme switching and dark mode because it avoids a flash on load.
- [[topics/motion-principles|Motion principles]]: Reach for motion only for springs, layout animations, exit animations or gesture-driven values; NumberFlow for number transitions and torph for animated text.
- [[topics/ai-assisted-design|AI-assisted design]]: Written as instructions for an AI agent: fixed initial response, identify the task, check package.json, recommend one library, and flag when leaving the curated list.
- [[topics/accessibility|Accessibility]]: base-ui is the pick because it handles accessibility, focus trapping and dismissal; a div-based dropdown or dialog with manual focus handling is a mismatch to catch.

## Notable Claims

- The picks are deliberate, taste-driven choices from Emil Kowalski's curated list. Evidence: These are deliberate, taste-driven picks
- The skill only runs when explicitly invoked and does not trigger on its own. Evidence: Only runs when explicitly invoked; disable-model-invocation: true
- A dropdown request is a UI-primitives task served by base-ui, even if the person asked about something else. Evidence: How to use this, step 1
- base-ui handles accessibility, focus trapping and dismissal. Evidence: Common mismatches to catch
- NumberFlow handles digit transitions properly, unlike re-rendering text. Evidence: Animating a number by re-rendering text
- A simple hover or fade does not need the motion library; plain CSS transitions are the right tool. Evidence: Reach for motion when you need springs
- If data points arrive live and the chart scrolls with time, Liveline fits; everything else is recharts. Evidence: The split: if data points arrive live
- clsx and cva compose, because cva uses clsx-style inputs internally. Evidence: The styling split
- next-themes switches themes and dark mode without a flash on load. Evidence: Theme switching / dark mode (no flash on load)
- Satori turns HTML/CSS into SVG/PNG for dynamic OG images. Evidence: Dynamic OG images (HTML/CSS → SVG/PNG)
- Sonner exists for exactly the job of toasts. Evidence: Toasts built by hand or with a modal library

## Quotes

> Identify the task, not the library the user named.
> Don't present a menu of options when the list has a clear answer.
> plain CSS transitions are the right tool there.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Self-promotion: Sonner, the toast pick, is linked at sonner.emilkowal.ski, so it is likely Emil Kowalski's own library [inferred].
- Caveat: The list is explicitly opinionated and taste-driven, not a benchmark; the source gives no performance or bundle-size comparisons.
- Caveat: Pinned to commit 85e8e23 of the skills repo; library picks may change in later versions.
- Caveat: The list is web and React-centric (package.json, useState, className, Tailwind) and says nothing about native iOS or Android choices [inferred].
- Caveat: The skill has disable-model-invocation: true, so an agent should use it only when explicitly invoked, not automatically.
- Caveat: The fixed initial-response line is behaviour for this skill only, not a design rule for products.

### Rules and practices

- **must** (process, web): Identify the underlying task before picking a library, not the library the person named; for example, treat 'I need to show a dropdown' as a UI-primitives task and pick base-ui. Why: The curated list is organised by task (a Task and Library table), so the task, not the named library, decides the pick. Values: base-ui. [not the library the user named]
- **must** (process, web): Read package.json before recommending a library, and if the project already uses a listed library, use that one. Why: The source says to look at package.json first and use a listed library the project already has. Values: package.json. [Check what's already installed]
- **must** (process, web): Do not replace an installed competitor library (for example react-window instead of Virtuoso) unless asked; flag the recommended pick instead. Why: The source gives no further reason; it states the instruction to flag the recommendation but not churn the dependency without being asked. Values: react-window, Virtuoso. [flag the recommendation but don't churn the dependency]
- **must** (process, web): Recommend exactly one library, state what it is for in one sentence, and install and wire it up when that is part of the request. Why: The list has a clear answer per task, so one pick is enough. Values: one library, one sentence. [Recommend one library]
- **must** (process, web): Do not present a menu of library options when the curated list has a clear answer. Why: The list has a clear answer for the task, and its picks are deliberate and taste-driven. [Don't present a menu of options]
- **must** (process, web): Do not substitute alternatives from outside the curated list unless the person asks for one or the task is genuinely not covered. Why: The list holds deliberate, taste-driven picks. [don't substitute alternatives outside this list]
- **must** (process, web): When a task is not covered by the list, say so explicitly, then recommend from general knowledge while making clear you have left the curated list. Why: The person should know when a pick is not from the curated list. [say so explicitly and recommend from your own knowledge]
- **must** (tooling, all): When the skill is invoked without a specific question, reply only with the fixed ready line and give no other information until a question is asked. Why: The source describes the skill as a lookup that answers a task; it says to give no other information until the user asks a question. Values: I'm ready to pick the right library for your task, my picks come from Emil Kowalski's curated list.. [When this skill is first invoked without a specific question]
- **must** (tooling, all): Run the library-picking lookup only when it is explicitly invoked; it must not trigger on its own. Why: The skill is configured with disable-model-invocation: true and says it does not trigger on its own. Values: disable-model-invocation: true. [Only runs when explicitly invoked]
- **should** (components, web): Use base-ui for unstyled, accessible UI components such as dialogs, popovers, menus and selects. Why: It is the curated pick for UI primitives and handles accessibility, focus trapping and dismissal. Values: base-ui, https://base-ui.com. [Unstyled, accessible UI components]
- **should** (components, web): Use cmdk for command menus (⌘K palettes). Why: It is the curated pick for command menus. Values: cmdk, ⌘K, https://cmdk.paco.me. [Command menus (⌘K palettes)]
- **should** (components, web): Use Sonner for toasts and notifications. Why: It is the curated pick for toasts. Values: Sonner, https://sonner.emilkowal.ski. [Toasts / notifications]
- **should** (components, web): Use input-otp for one-time password and verification code inputs. Why: It is the curated pick for OTP inputs. Values: input-otp, https://input-otp.rodz.dev. [One-time password / verification code inputs]
- **should** (tooling, web): Use Leva for customizable GUIs and control panels, with dialkit as the named alternative. Why: Leva is the curated pick; dialkit is listed as an alternative. Values: Leva, https://github.com/pmndrs/leva, dialkit, https://joshpuckett.me/dialkit. [Customizable GUIs / control panels]
- **should** (motion, web): Use motion (Framer Motion) for general-purpose animation: springs, layout animations, and enter and exit animations. Why: It is the curated pick for general-purpose animation. Values: motion, Framer Motion, https://motion.dev. [General-purpose animation (springs, layout animations, enter/exit)]
- **should** (motion, web): Reach for motion when you need springs, layout animations, exit animations or gesture-driven values. Why: Those are the cases the source names as needing it; a simple hover or fade does not. Values: springs, layout animations, exit animations, gesture-driven values. [Reach for motion when you need springs]
- **should** (motion, css): Do not reach for motion for a simple hover or fade; use plain CSS transitions. Why: A simple hover or fade doesn't need it; plain CSS transitions are the right tool there. Values: plain CSS transitions. [A simple hover or fade doesn't need it]
- **should** (motion, web): Use NumberFlow to animate numbers such as counters, prices and stats. Why: It is the curated pick and handles digit transitions properly. Values: NumberFlow, https://number-flow.barvian.me. [Animating numbers (counters, prices, stats)]
- **should** (motion, web): Use torph for animated text components. Why: It is the curated pick for animated text. Values: torph, https://torph.lochie.me/. [Animated text components]
- **should** (components, web): Use Cobe for 3D globes. Why: It is the curated pick for 3D globes. Values: Cobe, https://cobe.vercel.app. [cobe.vercel.app]
- **should** (tooling, web): Use Satori to generate dynamic OG images from HTML/CSS to SVG/PNG. Why: It is the curated pick for dynamic OG images. Values: Satori, https://github.com/vercel/satori, HTML/CSS → SVG/PNG. [Dynamic OG images]
- **should** (tooling, web): Use shiki for syntax highlighting. Why: It is the curated pick for syntax highlighting. Values: shiki, https://shiki.style. [Syntax highlighting]
- **should** (components, web): Use Liveline for real-time or streaming charts where data points arrive live and the chart scrolls with time. Why: That is the one split in the chart picks. Values: Liveline, https://github.com/benjitaylor/liveline. [The split: if data points arrive live]
- **should** (components, web): Use recharts for every other chart, static or interactive dashboards. Why: Everything that is not live, time-scrolling data goes to recharts. Values: recharts, https://recharts.org. [Everything else is recharts]
- **should** (patterns, web): Use dnd kit for drag and drop. Why: It is the curated pick for drag and drop. Values: dnd kit, https://dndkit.com. [Drag and drop | [dnd kit]]
- **should** (patterns, web): Use Virtuoso for virtualization of long lists and large tables. Why: It is the curated pick for virtualization. Values: Virtuoso, https://virtuoso.dev. [Virtualization (long lists, large tables)]
- **should** (tooling, react): Use zustand for state management. Why: It is the curated pick for state management. Values: zustand, https://zustand.docs.pmnd.rs. [State management]
- **should** (tooling, web): Use clsx to construct className strings conditionally for ad-hoc conditional classes. Why: It is the curated pick for building className strings conditionally, meant for ad-hoc conditional classes. Values: clsx, https://github.com/lukeed/clsx. [clsx for ad-hoc conditional classes]
- **should** (tooling, web): Use cva when a component has real variants (size, intent, state) that deserve a typed API, for type-safe, variant-driven Tailwind styling. Why: cva is the pick for variant-shaped styling; clsx stays for ad-hoc classes and the two compose. Values: cva, https://cva.style, size, intent, state. [cva when a component has real variants]
- **should** (tooling, web): Use next-themes for theme switching and dark mode so there is no flash on load. Why: It is the curated pick for theme switching without a flash on load. Values: next-themes, https://github.com/pacocoursey/next-themes, no flash on load. [Theme switching / dark mode (no flash on load)]
- **must** (components, web): Do not build toasts by hand or with a modal library; use Sonner. Why: Sonner exists for exactly this. Values: Sonner. [Toasts built by hand or with a modal library]
- **must** (accessibility, web): Do not build a <div>-based dropdown or dialog with manual focus handling; use base-ui. Why: base-ui handles accessibility, focus trapping and dismissal. Values: <div>, base-ui. [manual focus handling]
- **must** (motion, web): Do not animate a number by re-rendering its text; use NumberFlow. Why: NumberFlow handles digit transitions properly. Values: NumberFlow. [Animating a number by re-rendering text]
- **must** (patterns, web): Do not render a list of 1,000+ rows directly; virtualize it with Virtuoso before reaching for pagination hacks. Why: The source says to reach for Virtuoso before pagination hacks; it gives no further reason. Values: 1,000+, Virtuoso. [Rendering a 1,000+ row list directly]
- **must** (tooling, react): Do not share state through a useState-per-component web of props; use zustand. Why: The source names zustand as the fix for shared state held in a useState-per-component web of props. Values: useState, zustand. [per-component web of props for shared state]
- **must** (tooling, react): Do not write template-literal className ternaries three conditions deep; use clsx, or cva if the styling is variant-shaped. Why: clsx handles conditional classes and cva handles variants. Values: three conditions deep, clsx, cva. [Template-literal className ternaries three conditions deep]

### Decisions it informs

- Should components start from unstyled, accessible primitives or be hand-built? (`Q-comp-01`)
  - Unstyled, accessible primitives (base-ui): Dialogs, popovers, menus and selects come with accessibility, focus trapping and dismissal handled; you add the styling. When: Any dropdown, dialog, popover, menu or select.
  - Hand-built <div> components with manual focus handling: Accessibility, focus and dismissal must be written and maintained by hand. When: Listed as a mismatch to catch, not a recommended path.
  - Recommendation: base-ui, because it handles accessibility, focus trapping and dismissal.
- Should an animation use a motion library or plain CSS transitions?
  - motion (Framer Motion): Springs, layout animations, exit animations and gesture-driven values. When: When any of those are needed.
  - Plain CSS transitions: A simple hover or fade with no extra dependency. When: A simple hover or fade.
  - Recommendation: Plain CSS for simple hovers and fades; motion only for springs, layout, exit or gesture-driven animation.
- Which chart library should draw the charts? (`Q-viz-01`)
  - Liveline: Charts where data points arrive live and the chart scrolls with time. When: Real-time or streaming data.
  - recharts: General charts, static or interactive dashboards. When: Everything that is not live, time-scrolling data.
  - Recommendation: Liveline for live, time-scrolling data; recharts for everything else.
- How should conditional and variant styling be composed?
  - clsx: Builds className strings from ad-hoc conditions. When: Ad-hoc conditional classes.
  - cva: A type-safe, variant-driven API for Tailwind styling. When: A component has real variants (size, intent, state) that deserve a typed API.
  - Recommendation: clsx for ad-hoc classes and cva for real variants; they compose because cva uses clsx-style inputs internally.
- What should happen when the project already uses a competitor to the listed library?
  - Keep the installed library and flag the recommendation: No dependency churn; the person learns the curated pick. When: Default, unless the person asks for a change.
  - Switch to the listed library: Replaces the dependency. When: Only when the person asks.
  - Recommendation: Flag the recommendation but do not churn the dependency without being asked.
- Which library should power customizable GUIs and control panels?
  - Leva: The curated pick for control panels. When: Default choice.
  - dialkit: The named alternative. When: When an alternative to Leva is wanted.
  - Recommendation: Leva, with dialkit as the alternative.
- How should toasts and notifications be built?
  - Sonner: A library that exists for exactly this job. When: Any toast or notification.
  - Built by hand or with a modal library: The source flags this as a mismatch and points to Sonner instead; it gives no further detail. When: Listed as a mismatch to catch, not a recommended path.
  - Recommendation: Sonner, because it exists for exactly this.
- How should a very long list (1,000+ rows) be shown?
  - Virtualize it with Virtuoso: Long lists and large tables are virtualized instead of rendered row by row. When: A list of 1,000+ rows, or a large table.
  - Render every row directly: Every row is rendered at once. When: Listed as a mismatch to catch, not a recommended path.
  - Pagination hacks: The list is split up to avoid rendering it all. When: Only after virtualization; the source ranks it behind Virtuoso.
  - Recommendation: Virtuoso before reaching for pagination hacks.

### Process

1. Wait for a task: If invoked with no question, reply only with the fixed ready line and nothing else until the person asks.
2. Identify the task: Work out the underlying task rather than the library the person named; a dropdown is a UI-primitives task (base-ui).
3. Check what is installed: Read package.json first. Use a listed library if it is already there; if a competitor is installed, flag the recommendation without churning the dependency unless asked.
4. Recommend one library: Name one library from the list, say what it is for in one sentence, and install and wire it up if the request includes that. Do not present a menu when the list has a clear answer.
5. Handle uncovered tasks: If the task is not on the list, say so explicitly and recommend from general knowledge, making clear the pick is outside the curated list.
6. Catch mismatches: Look for hand-built toasts, div-based dropdowns or dialogs, numbers animated by re-rendering text, 1,000+ row lists rendered directly, useState-per-component prop webs, and className ternaries three conditions deep, and point each to its listed library.

### Examples and visual references

- A request to show a dropdown is treated as a UI-primitives task and answered with base-ui.: Shows task-first matching: the named need, not the named library, decides the pick.
- A project that already uses react-window instead of Virtuoso.: Shows the no-churn rule: flag Virtuoso as the recommendation but keep react-window unless asked.
- Sample invocations such as 'I need toasts' and 'what should I use for drag and drop?'.: Shows the lookup being driven by a task phrase, answered with Sonner and dnd kit from the list.

### Numbers

- 1,000+: Row count at which a list should be virtualized with Virtuoso instead of rendered directly. [Rendering a 1,000+ row list directly]
- three conditions deep: Depth of template-literal className ternaries that signals a switch to clsx or cva. [Template-literal className ternaries three conditions deep]
- one: Number of libraries to recommend per task, with a one-sentence reason. [Recommend one library]

<!-- /od:learn -->
