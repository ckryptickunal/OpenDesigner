---
type: source
title: "emilkowalski/skills: performance-cheatsheet.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-performance-cheatsheet
url: https://github.com/emilkowalski/skills/blob/85e8e23/performance-cheatsheet.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - performance
  - animation
  - css
  - react
  - motion-library
  - will-change
  - blur
  - virtualization
  - transitions
---

# emilkowalski/skills: performance-cheatsheet.md

## Metadata

- Page ID: `eks-performance-cheatsheet`
- Publisher: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/performance-cheatsheet.md

## Summary

A seven-row lookup table from Emil Kowalski's skills repository that pairs a common animation or rendering performance problem with its fix. It says to animate transform and opacity instead of width or top, to virtualize long lists, to keep animated blur under 20px, and to animate Motion's full transform string instead of its x/y props. It also bans transition: all, tells React code to write per-frame values to ref.current.style instead of state, and allows will-change: transform only once a 1px shift is actually seen. For a design system these become locked implementation rules for motion tokens and components, so every project's animations stay smooth by default.

## Key Ideas

- Smooth animation depends on which CSS properties move: transform and opacity, not width or top.
- Long lists should only render what is visible (virtualization).
- Animated blur is expensive; keep it under 20px.
- Motion's x/y props drop frames; animating the full transform string instead is the fix.
- transition: all animates properties you did not mean to animate; name each property instead.
- Per-frame values in React state cause a re-render every frame; write to the DOM style through a ref instead.
- will-change: transform fixes a 1px shift at the start of motion, but should only be added once that shift is seen.
- Each fix is keyed to a visible symptom, so the table works as a troubleshooting checklist [inferred].

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Author of the emilkowalski/skills repository this cheatsheet belongs to
- [[entities/emilkowalski-skills|emilkowalski/skills]] (product): MIT-licensed GitHub repository of agent skills; source of this cheatsheet (commit 85e8e23)
- [[entities/motion|Motion]] (library): Animation library whose x/y props the cheatsheet says drop frames; animate the full transform string instead
- [[entities/react|React]] (library): UI library whose per-frame state updates cause re-renders every frame
- [[entities/transform|transform]] (concept): CSS property recommended for animation instead of width/top, and as a full string in Motion
- [[entities/opacity|opacity]] (concept): CSS property recommended, with transform, for smooth animation
- [[entities/virtualization|Virtualization]] (concept): Rendering only the visible part of a long list so it scrolls quickly
- [[entities/blur|blur()]] (concept): CSS filter function whose animated value should stay under 20px for performance
- [[entities/transition-all|transition: all]] (concept): CSS declaration the cheatsheet bans because it animates unintended properties
- [[entities/ref-current-style|ref.current.style]] (concept): Direct DOM style write in React used instead of state for per-frame values
- [[entities/will-change-transform|will-change: transform]] (concept): CSS hint that fixes a 1px shift when motion starts, used only after the shift is seen

## Topics

- [[topics/animation-performance|Animation performance]]: Seven problem-to-fix pairs: animate transform/opacity, virtualize long lists, keep animated blur under 20px, animate Motion's full transform string, avoid transition: all, write per-frame values to ref.current.style, and add will-change: transform only when a 1px shift appears.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: CSS-level rules (which properties to animate, no transition: all, blur limit, will-change) and React-level rules (ref style writes instead of state, virtualized lists).
- [[topics/ui-libraries|UI libraries]]: Motion's x/y props can drop frames; animate the full transform string instead.

## Notable Claims

- Animating width or top makes animations stutter; animating transform or opacity avoids it. Evidence: Animation stutters
- A long list scrolls slowly when everything is rendered; virtualizing so only visible items render fixes it. Evidence: Long list scrolls slowly
- Animated blur causes performance issues, which keeping it under 20px avoids. Evidence: Blur causes perf issues
- Motion's x/y props drop frames; the fix is to animate the full transform string instead. Evidence: Motion's `x`/`y` drops frames
- transition: all makes random, unintended properties animate. Evidence: Random properties animate
- Storing per-frame animation values in React state re-renders the component every frame. Evidence: React re-renders every frame
- An element can shift 1px as its motion starts, and will-change: transform fixes it. Evidence: Element shifts 1px as motion starts

## Quotes

> Virtualize — only render what's visible
> Animate the full `transform` string instead
> Write to `ref.current.style`, not state

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: The table gives symptoms and fixes only, with no measurements or browser details behind them; the 20px blur limit is stated as a rule of thumb without a benchmark [inferred].
- Caveat: The Motion x/y advice reflects the Motion library as of this cheatsheet (skills repo commit 85e8e23); later Motion versions may behave differently [inferred].
- Caveat: The will-change rule is conditional: the source says to add it only once the 1px shift is seen, so it should not become a blanket default.

### Rules and practices

- **must** (motion, css): Animate transform and opacity, not width or top. Why: Animating width/top makes the animation stutter. Values: transform, opacity, width, top. [Animation stutters]
- **must** (components, web): Virtualize long lists so only the visible items are rendered. Why: A long list that renders everything scrolls slowly. [Long list scrolls slowly]
- **must** (motion, css): Keep any animated blur() value under 20px. Why: Animated blur causes performance issues. Values: blur(), 20px. [Blur causes perf issues]
- **must** (motion, web): In Motion, animate the full transform string instead of the x/y props. Why: Motion's x/y props can drop frames. Values: x, y, transform. [Motion's `x`/`y` drops frames]
- **must** (motion, css): Never write transition: all; list the exact properties that should transition. Why: transition: all makes random, unintended properties animate. Values: transition: all. [Random properties animate]
- **must** (motion, react): For per-frame animation values in React, write to ref.current.style instead of setting state. Why: Setting state every frame re-renders the component every frame. Values: ref.current.style. [React re-renders every frame]
- **must** (motion, css): Add will-change: transform only after you actually see an element shift 1px as its motion starts; do not add it pre-emptively. Why: It fixes the 1px shift at the start of motion, and the source limits it to when that shift is seen. Values: will-change: transform, 1px. [Element shifts 1px as motion starts]

### Numbers

- 20px: Upper limit for an animated blur() value before it causes performance issues [Keep animated `blur()` under 20px]
- 1px: The shift an element can make as motion starts, which will-change: transform fixes [Element shifts 1px as motion starts]

<!-- /od:learn -->
