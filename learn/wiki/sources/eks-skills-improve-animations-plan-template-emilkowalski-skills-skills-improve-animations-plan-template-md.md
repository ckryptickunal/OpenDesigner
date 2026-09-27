---
type: source
title: "emilkowalski/skills: skills/improve-animations/PLAN-TEMPLATE.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-improve-animations-plan-template
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/improve-animations/PLAN-TEMPLATE.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - motion
  - implementation-plan
  - handoff
  - template
  - verification
  - feel-check
  - agents
  - process
---

# emilkowalski/skills: skills/improve-animations/PLAN-TEMPLATE.md

## Metadata

- Page ID: `eks-skills-improve-animations-plan-template`
- Publisher: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/improve-animations/PLAN-TEMPLATE.md

## Summary

The plan template that Emil Kowalski's improve-animations skill uses for every animation fix it hands off. Each plan is written for an executor that may be a less capable model with no context and no taste, so it must spell out the problem with file:line citations and verbatim current code, the exact target values, the repo's own conventions with an exemplar, one concrete edit per step, hard scope boundaries, and a verification section that includes a slow-motion feel check. For a design system team it is a ready format for turning motion findings into safe, reviewable work that cheaper agents or junior contributors can carry out without guessing.

## Key Ideas

- Write plans for the weakest executor: zero context, zero taste.
- Never point back to earlier discussion; inline every value, path and code excerpt.
- Stamp each plan with the commit it was written against so drift can be detected.
- Problem sections cite file:line and quote the current code verbatim.
- Target sections spell out every curve, duration, spring config and media query.
- Plans extend the repo's existing tokens and patterns, shown through one exemplar.
- Boundaries limit edits to motion properties, forbid new dependencies, and require stopping on drift.
- Verification pairs mechanical checks with a feel check in slow motion and under reduced motion.
- One plan per finding, merged only when files and fix pattern are identical.
- A plans/README.md index tracks order, dependencies and status.

## Entities

- [[entities/improve-animations|improve-animations]] (tool): Emil Kowalski's agent skill that writes every plan in this format.
- [[entities/audit-md|AUDIT.md]] (concept): The audit playbook every target value in a plan must be pulled from.
- [[entities/devtools-animations-panel|DevTools Animations panel]] (tool): Used to slow animation playback to 10% for the feel check.
- [[entities/devtools-rendering-panel|DevTools Rendering panel]] (tool): Used to toggle prefers-reduced-motion during verification.
- [[entities/git-rev-parse-short-head|git rev-parse --short HEAD]] (tool): Command whose output stamps each plan with the commit it was written against.
- [[entities/feel-check|Feel check]] (concept): Mandatory manual check that motion looks right, not just that it compiles.

## Topics

- [[topics/design-process|Design process]]: A fixed plan structure (status, commit, severity, category, scope, problem, target, conventions, steps, boundaries, verification) and an index README for turning motion findings into executable work.
- [[topics/ai-assisted-design|AI-assisted design]]: Plans are written so a less capable model with zero context and zero taste can execute them without improvising.
- [[topics/motion-principles|Motion principles]]: Motion can be mechanically correct and still feel wrong, so a feel check in slow motion is required.
- [[topics/easing-and-timing|Easing and timing]]: The example target replaces transition: all 400ms ease-in with separate transform and opacity transitions at 200ms using var(--ease-out).
- [[topics/reduced-motion|Reduced motion]]: Verification toggles prefers-reduced-motion and confirms movement is dropped while opacity feedback remains.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: New curves go into the repo's existing token file, e.g. --ease-out: cubic-bezier(0.23, 1, 0.32, 1) in src/styles/tokens.css.

## Notable Claims

- The executor of a plan may be a less capable model with zero context and zero taste. Evidence: # Plan Template
- Motion can be mechanically correct and still feel wrong. Evidence: Notes for the plan author: The feel check is not optional
- Code may drift after the commit a plan was stamped with, so steps may stop matching the code. Evidence: Boundaries: drift since the commit stamp

## Quotes

> The executor may be a less capable model with zero context and zero taste
> The feel check is not optional.
> Motion can be mechanically correct and still feel wrong

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is an AI-agent skill file pinned to commit 85e8e23 of emilkowalski/skills.
- Caveat: The file paths (src/styles/tokens.css, src/components/dropdown.css:14) are placeholders in a template, not real files.
- Caveat: The DevTools panel names (Animations, Rendering) are written without naming a browser.
- Caveat: The template governs plan documents for code changes; its only motion values are in the example (the --ease-out curve and a 200ms dropdown transition), which agree with AUDIT.md's --ease-out token and 150–250ms dropdown band [inferred].

### Rules and practices

- **must** (process, all): Write every animation-fix plan in the fixed structure: a title line '# NNN — <Short imperative title>' followed by Status, Commit, Severity, Category and Estimated scope, then Problem, Target, Repo conventions to follow, Steps, Boundaries and Verification sections. Why: Every plan written by improve-animations follows this structure. Values: NNN, Status, Commit, Severity, Category, Estimated scope. [Every plan written by improve-animations follows this structure]
- **must** (process, all): Write the plan so an executor with zero context and zero taste can complete it; the plan must contain everything, exactly. Why: The executor may be a less capable model. [the plan must contain everything, exactly]
- **must** (process, all): Never refer back to earlier discussion such as 'the audit above' or 'the easing we discussed'. Why: The executor has no context from that discussion. [No references to "the audit above" or "the easing we discussed."]
- **must** (process, all): Set a new plan's Status to TODO. Why: Template header field. Values: TODO. [**Status**: TODO]
- **must** (process, all): Stamp the Commit field with the output of git rev-parse --short HEAD at the time the plan is written. Why: Lets the executor detect drift since the commit stamp. Values: git rev-parse --short HEAD. [**Commit**]
- **must** (process, all): Mark Severity as exactly one of HIGH, MEDIUM or LOW, and name the audit category. Why: Template header fields. Values: HIGH, MEDIUM, LOW. [**Severity**: HIGH | MEDIUM | LOW]
- **must** (process, all): State the estimated scope as the number of files and a rough size. Why: Template header field. Values: <n files, rough size>. [**Estimated scope**]
- **must** (process, all): In Problem, say what is wrong, where, and why it matters to how the product feels. Why: Template Problem section. [## Problem]
- **must** (process, all): Cite every problem location as path/to/file.tsx:123 and include the current code verbatim. Why: Template Problem section. Values: path/to/file.tsx:123. [Cite every location as path/to/file.tsx:123]
- **should** (process, all): Label each code excerpt with a comment giving its location and whether it is the current or the target code, e.g. /* src/components/dropdown.css:14 — current */ and /* target */. Why: The template's Problem and Target excerpts are labelled this way. Values: /* target */. [/* src/components/dropdown.css:14 — current */]
- **must** (process, all): In Target, spell out the exact end state with every value: curves, durations, spring configs and media queries. Why: The executor has zero context and zero taste, so the plan must contain everything, exactly. [## Target: Every value spelled out]
- **must** (process, all): Never write a vague target such as 'use a nicer easing'. Why: Every value must be spelled out. [Never "use a nicer easing"]
- **must** (process, all): Document how the codebase already handles the pattern (token names, file placement, prop patterns) and give one exemplar file:line for the executor to imitate. Why: The executor should follow repo conventions. Values: <exemplar file:line that already does this correctly>. [## Repo conventions to follow]
- **should** (tokens, css): Add new easing curves to the repo's existing token file rather than inline, e.g. --ease-out: cubic-bezier(0.23, 1, 0.32, 1) in src/styles/tokens.css. Why: Template example of following repo conventions. Values: src/styles/tokens.css, --ease-out: cubic-bezier(0.23, 1, 0.32, 1). [Easing tokens live in src/styles/tokens.css]
- **must** (process, all): Write Steps as one concrete edit per step: the file, what changes, and the resulting code. Why: Template Steps section. [## Steps]
- **must** (process, all): List the files and components the executor must not touch. Why: Template Boundaries section. [Do NOT touch <files/components out of scope>]
- **must** (process, all): Restrict the executor to motion properties; do not change markup or structure unless a step says so. Why: Template Boundaries section. [Do NOT change markup/structure — motion properties only]
- **must** (process, all): Do not add new dependencies in an animation-fix plan. Why: Template Boundaries section. [Do NOT add new dependencies.]
- **must** (process, all): If a step does not match the code found (drift since the commit stamp), stop and report instead of improvising. Why: Template Boundaries section. [STOP and report instead of improvising]
- **must** (process, all): In Verification, give the exact mechanical commands (typecheck, lint, build) with their expected outcome. Why: Template Verification section. Values: typecheck, lint, build. [**Mechanical**]
- **must** (motion, all): Include a feel check: run the UI, trigger the interaction, and list observable checks such as 'the dropdown scales from its trigger, not from center' and 'spamming the toggle never restarts the animation from zero'. Why: Motion can be mechanically correct and still feel wrong. [**Feel check**]
- **must** (tooling, web): In the feel check, set DevTools animation playback to 10% (Animations panel) and confirm the specific detail. Why: Motion can be mechanically correct and still feel wrong; the executor needs concrete things to watch for in slow motion. Values: 10%. [In DevTools, set playback to 10% (Animations panel)]
- **must** (accessibility, web): In the feel check, toggle prefers-reduced-motion (Rendering panel) and confirm movement is dropped but opacity feedback remains. Why: Template verification step for reduced motion. Values: prefers-reduced-motion. [Toggle prefers-reduced-motion (Rendering panel)]
- **must** (process, all): End Verification with 'Done when' criteria that a machine or an eye can check. Why: Template Verification section. [**Done when**]
- **must** (process, all): Write one plan per finding; merge two findings into one plan only when they share every file and the same fix pattern. Why: Notes for the plan author, e.g. the same easing token swap across components. [One plan per finding]
- **must** (process, all): Pull every value from AUDIT.md; never approximate from memory. Why: Notes for the plan author. [Pull every value from AUDIT.md]
- **must** (process, all): Never skip the feel check; give the executor or reviewer concrete things to watch in slow motion. Why: Motion can be mechanically correct and still feel wrong. [The feel check is not optional.]
- **must** (process, all): After writing plans, create or update plans/README.md with a table of plans (number, title, severity, status), the recommended execution order and dependencies between plans. Why: Notes for the plan author. Values: plans/README.md. [create or update plans/README.md]

### Decisions it informs

- Should related animation findings be fixed in one plan or several?
  - One plan per finding: Each fix is small, reviewable and independently executable. When: The default.
  - Merged plan: One plan covers several findings with the same edit. When: Only when the findings share every file and the same fix pattern, such as the same easing token swap across components.
  - Recommendation: One plan per finding; merge only when files and fix pattern are identical.

### Process

1. Header: Title '# NNN — <Short imperative title>', then Status TODO, Commit from git rev-parse --short HEAD, Severity HIGH/MEDIUM/LOW, audit Category, and Estimated scope (files, rough size).
2. Problem: What is wrong, where, and why it matters to how the product feels; cite every location as file:line and quote current code verbatim.
3. Target: The exact end state with every curve, duration, spring config and media query spelled out, pulled from AUDIT.md.
4. Repo conventions: Where tokens live, naming, file placement and prop patterns, plus one exemplar file:line to imitate.
5. Steps: Numbered steps, each one concrete edit with the file, the change and the resulting code.
6. Boundaries: Out-of-scope files, motion properties only, no new dependencies, stop and report on drift.
7. Verification: Mechanical commands with expected outcome; a feel check with observable checks, 10% playback in DevTools and a reduced-motion toggle; Done-when criteria.
8. Index: Create or update plans/README.md with the plan table (number, title, severity, status), execution order and dependencies.

### Examples and visual references

- Dropdown with a sluggish all-property transition: Current code .dropdown { transition: all 400ms ease-in; } at src/components/dropdown.css:14, shown as the kind of verbatim excerpt a Problem section cites.
- Dropdown target state: transition: transform 200ms var(--ease-out), opacity 200ms var(--ease-out); plus transform-origin: var(--transform-origin): only transform and opacity animate, with the strong ease-out token, scaling from the trigger.
- Feel-check observations: Example checks: the dropdown scales from its trigger, not from center; spamming the toggle never restarts the animation from zero.

### Numbers

- 10%: DevTools animation playback speed for the feel check. [In DevTools, set playback to 10% (Animations panel)]
- 400ms: Duration in the example's current (wrong) dropdown transition, with ease-in and transition: all. [src/components/dropdown.css:14 — current]
- 200ms: Duration in the example's target dropdown transition for transform and opacity. [/* target */]
- cubic-bezier(0.23, 1, 0.32, 1): Example --ease-out token added to the repo's token file. [Repo conventions to follow]

<!-- /od:learn -->
