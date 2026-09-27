---
type: topic
title: Design systems and tokens
created: 2026-09-24
updated: 2026-09-24
sources: []
tags: []
---

# Design systems and tokens

## Overview

Build the style guide's font sizes from a ratio (square root of the golden ratio, 1.27, from a 16 pixel base) instead of eyeballing one page and deriving the rest.

## Source Mentions

- [[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]: Build the style guide's font sizes from a ratio (square root of the golden ratio, 1.27, from a 16 pixel base) instead of eyeballing one page and deriving the rest.
- [[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]: A design system is how users build trust and speed; keep buttons, spacing, type scales and color scheme the same across contexts, and prefer decisions you can stick to over hundreds of components.
- [[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]: Consistency means styles for colors, variables for measurements and components for UI elements; duplicate components such as back and skip buttons must match.
- [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]: A system has to reflect the values of the team; defining rules, spacing, type scales and interaction patterns gives an architecture for expansion, and the system is a shared language rather than a way to make everything look the same.
- [[sources/adev-home-animations-dev|animations.dev]]: Emil developed the design system on Vercel's design team, which is part of his stated background.
- [[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]: Custom easing curves are kept as a named set of CSS custom properties on :root (--ease-breeze, --ease-silk, --ease-swift, --ease-nova, --ease-crisp, --ease-glide shown out of 18).
- [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]: Motion values come from fixed token tables; extend a codebase's existing easing and duration tokens rather than adding a parallel system.
- [[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]: The recommended design-system toast is headless (toast.custom()) wrapped in your own toast() abstraction.
- [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]: Named easing tokens (--ease-out, --ease-in-out, --ease-drawer) and per-element duration ranges suitable as motion tokens.
- [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]: Suggestions must extend the project's existing easing and duration tokens, not invent parallel ones, and quote exact values from the shared easing vocabulary.
- [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]: Curves and durations should be shared tokens; several near-identical hand-typed cubic-beziers is a consolidation finding; motion personality must match the product.
- [[sources/eks-skills-improve-animations-plan-template-emilkowalski-skills-skills-improve-animations-plan-template-md|emilkowalski/skills: skills/improve-animations/PLAN-TEMPLATE.md]]: New curves go into the repo's existing token file, e.g. --ease-out: cubic-bezier(0.23, 1, 0.32, 1) in src/styles/tokens.css.
- [[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]]: Recon finds existing --ease-* and --duration-* tokens, duration scales and spring configs; plans extend them; token consolidation is LOW severity polish.
- [[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]: Variants use the project's existing colors, radii, spacing, fonts and easing/duration variables so each could ship tomorrow; sharing tokens is not convergence; with no project, a restrained default of neutral grays, one accent and the system font stack.
- [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]: Named easing curves --ease-out, --ease-in-out and --ease-drawer are defined as CSS custom properties alongside a duration table.
- [[sources/sonner-styling-styling-sonner|Styling – Sonner]]: Recommends headless because people usually either use the defaults or go fully custom, and shows abstracting toast() into your own function with props that fit the codebase.
- See also: [[synthesis/design-systems-and-tokens|Design systems and tokens synthesis]]
