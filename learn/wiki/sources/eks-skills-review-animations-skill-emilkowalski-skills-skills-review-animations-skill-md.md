---
type: source
title: "emilkowalski/skills: skills/review-animations/SKILL.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-review-animations-skill
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/review-animations/SKILL.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - animation
  - motion
  - code-review
  - easing
  - duration
  - interruptibility
  - performance
  - reduced-motion
  - hover-gating
  - transform-origin
  - springs
  - emil-kowalski
---

# emilkowalski/skills: skills/review-animations/SKILL.md

## Metadata

- Page ID: `eks-skills-review-animations-skill`
- Publisher: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/review-animations/SKILL.md

## Summary

This is Emil Kowalski's review-animations agent skill: a strict reviewer that judges animation and motion code against a high craft bar and defaults to flagging. It sets ten non-negotiable standards (justified motion, frequency, easing, sub-300ms UI, origin, interruptibility, GPU-only properties, accessibility, asymmetric timing, cohesion), a list of patterns to flag on sight, and an ordered list of fixes that starts with deleting the animation. It also fixes the review output: a Before/After/Why table, a verdict grouped by impact tier, and an explicit Block or Approve decision with stated criteria. For a design system this is a ready-made motion quality gate that can be run on every change to motion tokens and components.

## Key Ideas

- Motion must feel right, not merely run; a transition that works but feels sluggish or drops frames is a regression.
- Review posture defaults to flagging: approval is earned by meeting explicit criteria.
- Every animation needs a stated purpose; 'it looks cool' on a frequently seen element is a block.
- How often an action happens decides whether it animates: keyboard and 100+/day actions get none.
- Entering and exiting UI uses ease-out or a strong custom curve; ease-in on UI is a block.
- UI motion stays under 300ms unless a reason is stated.
- Popovers, dropdowns and tooltips scale from their trigger (modals stay centered), and no entrance starts from scale(0).
- Rapid or gesture-driven motion must be interruptible, so use transitions or springs, not keyframes.
- Only transform and opacity are animated; layout properties and busy-page Framer Motion shorthands are performance findings.
- Reduced motion is gentler, not zero, and hover motion is gated to fine pointers.
- Deliberate phases (press, hold, destructive confirm) are slow; system responses snap.
- Fixes follow a preference order: delete, reduce, fix easing, fix origin, make interruptible, move to GPU, asymmetric timing, polish, then accessibility and cohesion.
- Output is a Before/After/Why table plus a tiered verdict ending in Block or Approve, citing file:line and exact values from STANDARDS.md.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer whose animation philosophy sets the review's craft bar.
- [[entities/animations-dev|animations.dev]] (product): Named in parentheses after Emil Kowalski's animation philosophy as where the substantive bar comes from.
- [[entities/review-animations|review-animations]] (tool): The agent skill itself: a motion-only code reviewer.
- [[entities/standards-md|STANDARDS.md]] (concept): Companion rule catalog holding the exact curves, durations and spring configs to cite in findings.
- [[entities/base-ui|Base UI]] (library): Credited for var(--transform-origin), the suggested fix for popover origin.
- [[entities/framer-motion|Framer Motion]] (library): Its x/y/scale shorthand props are flagged on motion that runs while the page is busy.
- [[entities/starting-style|@starting-style]] (concept): Suggested for entry animations (a polish move) and for predetermined motion.
- [[entities/waapi|WAAPI]] (concept): Suggested for programmatic CSS animation when moving work to the GPU, and for predetermined motion.
- [[entities/prefers-reduced-motion|prefers-reduced-motion]] (concept): Must be honored with gentler motion (keep opacity/color, drop movement), not zero.

## Topics

- [[topics/motion-principles|Motion principles]]: Ten non-negotiable standards: every animation needs a purpose, motion is matched to frequency of use, and deleting motion is often the strongest move.
- [[topics/easing-and-timing|Easing and timing]]: Ease-out or strong custom curves for entering and exiting, ease-in on UI is a block, UI under 300ms, and asymmetric timing for press and hold interactions.
- [[topics/spring-animation|Spring animation]]: Springs that retarget from current state are one of the accepted ways to make gesture-driven motion interruptible, and a polish move for 'alive' elements.
- [[topics/animation-performance|Animation performance]]: Only transform and opacity; layout properties, transition: all, busy-page Framer Motion shorthands and parent CSS variables driving child transforms are flagged.
- [[topics/reduced-motion|Reduced motion]]: prefers-reduced-motion must be honored by keeping opacity and color and dropping movement, not by removing everything.
- [[topics/accessibility|Accessibility]]: Reduced-motion handling and hover gating behind (hover: hover) and (pointer: fine) are review criteria and an approval condition.
- [[topics/micro-interactions|Micro-interactions]]: Press-and-release and hold interactions need asymmetric timing; toggles must be interruptible.
- [[topics/toasts-and-notifications|Toasts and notifications]]: Toasts are named as rapidly triggered UI that must not use keyframes and must be interruptible.
- [[topics/modals-and-popovers|Modals and popovers]]: Popovers, dropdowns and tooltips scale from their trigger; modals are exempt and stay centered.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: CSS transitions, @starting-style and WAAPI for predetermined motion; JS and springs for dynamic, gesture-driven motion; specific CSS before/after fixes.
- [[topics/design-process|Design process]]: A repeatable motion review method: standards, escalation triggers, a remedial hierarchy, tiered output and explicit approval criteria.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Motion must match the component's personality; when unsure, review in slow motion and with fresh eyes, or delete the motion.
- [[topics/ai-assisted-design|AI-assisted design]]: Packaged as an agent skill with a fixed opening line, a narrow scope and a required output format for AI reviewers.

## Notable Claims

- A transition that works but feels sluggish, lands from the wrong origin, fires too often, or drops frames is a regression. Evidence: Operating Posture
- ease-in delays the moment the user watches most, so it feels sluggish. Evidence: 3. Responsive easing; findings table row for ease-in on dropdown
- Built-in CSS easings are too weak for UI motion. Evidence: 3. Responsive easing
- scale(0) makes an element look like it came from nowhere. Evidence: Findings table: transform: scale(0)
- transition: all animates unintended properties off the GPU. Evidence: Findings table: transition: all 300ms
- Keyframes restart from zero, whereas CSS transitions or springs retarget from the current state. Evidence: 6. Interruptibility
- Framer Motion x/y/scale shorthands are a performance risk under load. Evidence: 7. GPU-only properties; Aggressive Escalation Triggers
- Updating a CSS variable on a parent to drive a child transform causes a style recalc storm. Evidence: Aggressive Escalation Triggers
- A subtle blur can bridge two states where a crossfade would be jarring. Evidence: 10. Cohesion
- The review method (standards, escalation triggers, remedial hierarchy, tiered output, approval criteria) is adapted from aggressive code-quality review. Evidence: Operating Posture

## Quotes

> Default to flagging. Approval is earned, not assumed.
> When unsure whether motion feels right, the strongest move is often to delete it.
> Nothing appears from nothing

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is an AI-agent skill file pinned to commit 85e8e23 of emilkowalski/skills (MIT); values can change in later commits.
- Caveat: The fixed opening line, disable-model-invocation flag and output format are instructions for an AI reviewer, not design rules for the product.
- Caveat: Precise values (curves, per-element durations, spring configs) are delegated to the companion STANDARDS.md; this file states only the thresholds above.
- Caveat: The review method is described as adapted from aggressive code-quality review, so its default-to-flag posture is a deliberate stance, not a measured finding.
- Caveat: Flagging pure-fade entrances sits alongside a reduced-motion standard that keeps opacity changes; the pure-fade flag appears to apply to full-motion entrances only [inferred].
- Caveat: The Framer Motion shorthand performance claim is stated without a library version or benchmark.
- Caveat: var(--transform-origin) is Base UI's variable; other libraries may name it differently [inferred].
- Caveat: 'Reduced motion' in the frequency standard (tens/day) means smaller, less motion for frequent actions, not the prefers-reduced-motion setting covered by standard 8 [inferred].
- Caveat: The remedial hierarchy lists stagger as polish (item 8), while the escalation triggers flag an everything-at-once entrance where a stagger belongs; the flag applies only where a stagger belongs [inferred].

### Rules and practices

- **must** (process, all): When the review skill is invoked without a specific question, reply only with the fixed ready line (ready to review animations against a high craft bar from Emil Kowalski's animation philosophy) and give no other information until the user asks. Why: The Initial Response section requires it. [Initial Response]
- **must** (process, all): When reviewing motion code, default to flagging and approve only when every approval criterion is met. Why: Approval is earned, not assumed; the bias is toward motion that feels right, not motion that merely runs. [Operating Posture]
- **must** (motion, all): Treat a transition that works but feels sluggish, lands from the wrong origin, fires too often, or drops frames as a regression, not a pass. Why: The bias is toward motion that feels right, not motion that merely runs. [Operating Posture]
- **must** (process, all): Keep an animation review scoped to animation and motion code; decline general code review and point to a general review skill. Why: The skill does one thing: review motion against a high craft bar. [A specialized review skill. It does ONE thing]
- **must** (motion, all): Give every animation a stated purpose: spatial consistency, state indication, feedback, explanation, or preventing a jarring change. Why: Every animation must answer 'why does this animate?'; a violation is a finding. [1. Justified motion]
- **must** (motion, all): Do not add animation to a frequently seen element when its only justification is that it looks cool; a review blocks it. Why: 'It looks cool' on a frequently-seen element is a block. ["It looks cool" on a frequently-seen element is a block]
- **must** (motion, all): Do not animate keyboard-initiated actions, command-palette toggles, or any action performed 100+ times a day. Why: Keyboard-initiated and 100+/day actions get no animation; animation on them is a block. Values: 100+/day. [2. Frequency-appropriate; Aggressive Escalation Triggers]
- **must** (motion, all): Use reduced (smaller, less) motion for actions seen tens of times a day. Why: Motion is matched to how often it is seen; a violation of this standard is a finding. Values: Tens/day. [2. Frequency-appropriate]
- **should** (motion, all): Use standard animation for occasionally seen actions. Why: Motion is matched to how often it is seen. [2. Frequency-appropriate]
- **consider** (motion, all): Reserve delightful motion for rare or first-time moments. Why: Rare/first-time can have delight; frequent actions cannot. [2. Frequency-appropriate]
- **must** (motion, all): Use ease-out or a strong custom curve for elements entering or exiting. Why: Responsive easing; entering and exiting motion must not delay what the user is watching. Values: ease-out. [3. Responsive easing]
- **must** (motion, all): Never use ease-in on any UI interaction. Why: ease-in delays the moment the user watches most and feels sluggish; it is a block. Values: ease-in. [3. Responsive easing; findings table]
- **must** (motion, css): Replace weak built-in CSS easings on deliberate animations with custom cubic-bezier curves taken from STANDARDS.md. Why: Built-in CSS easings are too weak; weak built-in easing on a deliberate animation is flagged on sight. Values: cubic-bezier. [Built-in CSS easings are too weak; expect custom cubic-beziers]
- **must** (motion, all): Keep UI animations under 300ms; any slower UI animation needs a stated reason or it is a finding. Why: Sub-300ms UI; per-element budgets live in STANDARDS.md. Values: 300ms. [4. Sub-300ms UI]
- **must** (motion, css): Scale popovers, dropdowns and tooltips from their trigger with transform-origin, not from center. Why: Origin and physical correctness: popovers scale from their trigger, not center; transform-origin: center on a trigger-anchored popover, dropdown or tooltip is flagged on sight. Values: transform-origin, var(--transform-origin). [5. Origin & physical correctness; findings table]
- **must** (motion, all): Keep modals centered; they are exempt from trigger-origin scaling. Why: Modals stay centered. [5. Origin & physical correctness]
- **must** (motion, all): Never animate an entrance from scale(0); start from scale(0.9–0.97) plus opacity. Why: Nothing appears from nothing; scale(0) looks like it came from nowhere. Values: scale(0), scale(0.9–0.97). [5. Origin & physical correctness]
- **must** (motion, all): Do not ship pure-fade entrances with no initial transform. Why: Listed with scale(0) as an escalation trigger to flag on sight. [Aggressive Escalation Triggers]
- **must** (motion, all): Make rapidly triggered or gesture-driven motion (toasts, toggles, drags) interruptible with CSS transitions or springs that retarget from the current state. Why: Keyframes restart from zero; transitions and springs retarget. [6. Interruptibility]
- **must** (motion, css): Do not use keyframe animations on toasts, toggles, or anything added or triggered rapidly. Why: Keyframes restart from zero instead of retargeting. [Aggressive Escalation Triggers]
- **must** (motion, all): Animate only transform and opacity. Why: GPU-only properties; anything else is a performance finding. Values: transform, opacity. [7. GPU-only properties]
- **must** (motion, all): Do not animate width, height, margin, padding, top or left. Why: Animating layout properties is a performance finding flagged on sight. Values: width, height, margin, padding, top, left. [7. GPU-only properties; Aggressive Escalation Triggers]
- **must** (motion, react): Do not use Framer Motion x/y/scale shorthand props on motion that runs while the page is busy; use the full transform string instead. Why: The shorthands are a performance finding under load; the remedy is shorthand to full transform string. Values: x, y, scale. [props on motion that runs while the page is busy]
- **must** (motion, web): Do not update a CSS variable on a parent to drive a child's transform. Why: It causes a style recalc storm. [Updating a CSS variable on a parent to drive a child transform]
- **must** (motion, css): Never use transition: all; list the exact properties, for example transition: transform 200ms ease-out. Why: all is unbounded and animates unintended properties off-GPU. Values: transition: all 300ms, transition: transform 200ms ease-out. [Specify exact properties; `all` animates unintended properties off-GPU]
- **must** (accessibility, all): Honor prefers-reduced-motion on every animation that moves things, by keeping opacity and color changes and dropping movement. Why: Reduced motion means gentler, not zero; missing handling on movement is flagged on sight. Values: prefers-reduced-motion. [is honored (gentler, not zero — keep opacity/color, drop movement)]
- **must** (accessibility, css): Gate hover animations behind @media (hover: hover) and (pointer: fine). Why: Ungated :hover motion is flagged on sight. Values: @media (hover: hover) and (pointer: fine). [8. Accessibility]
- **must** (motion, all): Animate deliberate actions (a press, a hold, a destructive confirm) slower and let system responses snap. Why: Stated as non-negotiable standard 9; symmetric timing on a press-and-release or hold interaction is a finding. [9. Asymmetric enter/exit]
- **must** (motion, all): Do not use symmetric enter/exit timing on press-and-release or hold interactions. Why: Symmetric timing there is a finding. [9. Asymmetric enter/exit]
- **must** (motion, all): Match motion to the component's personality and the rest of the product: playful components can be bouncier, dashboards stay crisp. Why: Mismatched personality is a finding. [10. Cohesion]
- **must** (motion, all): When a crossfade between two states looks jarring and a subtle blur would bridge them, add the blur instead of leaving the plain crossfade. Why: A jarring crossfade where a subtle blur would bridge two states is a finding. Values: blur. [10. Cohesion; Remedial Preference Hierarchy item 8]
- **should** (motion, all): When unsure whether motion feels right, consider deleting it. Why: The strongest move is often to delete it. [When unsure whether motion feels right, the strongest move is often to delete it]
- **must** (motion, all): Where a group entrance calls for a stagger, stagger the items by 30–80ms instead of showing everything at once. Why: An everything-at-once entrance where a 30–80ms stagger belongs is flagged on sight. Values: 30–80ms. [Everything-at-once entrance where a 30–80ms stagger belongs]
- **should** (process, all): When proposing fixes, prefer earlier moves in the remedial hierarchy, starting with deleting the animation if it is high-frequency, has no purpose, or is keyboard-triggered. Why: The remedial preference hierarchy ranks fixes; deletion comes first. [Remedial Preference Hierarchy]
- **should** (motion, all): If the animation should stay, reduce it first (shorter duration, smaller transform, fewer animated properties) before fixing easing, origin or other properties. Why: Reduce is the second preferred move, after deletion. [Remedial Preference Hierarchy item 2]
- **must** (motion, all): Replace scale(0) with scale(0.95) plus opacity: 0. Why: Fix origin and physicality; scale(0) looks like it came from nowhere. Values: scale(0.95), opacity: 0. [Remedial Preference Hierarchy item 4; findings table]
- **should** (motion, all): Convert keyframes to transitions for interruptible UI, or use a spring for gesture-driven motion. Why: Make it interruptible. [Remedial Preference Hierarchy item 5]
- **should** (motion, web): Use WAAPI for programmatic CSS animation. Why: Part of moving motion to the GPU. Values: WAAPI. [Remedial Preference Hierarchy item 6]
- **consider** (motion, css): Use @starting-style for entry animations and a spring for 'alive' elements as polish. Why: Listed as polish moves after the core fixes. Values: @starting-style. [Remedial Preference Hierarchy item 8]
- **must** (process, all): Report findings as a single markdown table with Before, After and Why columns, one row per issue, and never as a Before:/After: list. Why: Part 1 of the required output format. Values: Before | After | Why. [Part 1 — Findings table (REQUIRED)]
- **must** (process, all): Group remaining review commentary by impact tier, highest first, and omit empty tiers: feel-breaking regressions, missed simplifications, performance, interruptibility and timing, origin/physicality/cohesion, accessibility. Why: Part 2 of the required output format. [Group remaining commentary by impact tier, highest first. Omit empty tiers.]
- **must** (process, all): End every review with an explicit Block or Approve decision. Why: The verdict must close with an explicit decision. Values: Block, Approve. [Close with an explicit decision]
- **must** (process, all): Block when there is any feel-breaking regression, animation on a keyboard or high-frequency action, scale(0) or ease-in on UI, or a non-GPU animation with an easy GPU fix. Why: These are the stated Block criteria. [Block —]
- **must** (process, all): Approve only when there are no feel-breaking regressions, no obvious motion that should be deleted, durations and easing within bounds, interruptibility handled where needed, and reduced motion respected. Why: These are the stated Approve criteria. [Approve —]
- **must** (process, all): Cite file:line for every finding. Why: Be specific. Values: file:line. [Be specific and cite `file:line`]
- **must** (process, all): Take exact curves, durations and spring configs from STANDARDS.md instead of approximating. Why: When a value is needed, pull the exact one rather than approximating. [pull the exact one from STANDARDS.md]
- **should** (motion, web): Use CSS transitions, @starting-style or WAAPI for predetermined motion, and JS or springs for dynamic, interruptible, gesture-driven motion. Why: Each tool fits a kind of motion. [Guidelines]
- **should** (process, all): When unsure whether motion feels right, recommend reviewing it in slow motion or frame-by-frame and with fresh eyes the next day rather than guessing. Why: The source recommends this rather than guessing. [recommend reviewing it in slow motion / frame-by-frame and with fresh eyes the next day rather than guessing]

### Decisions it informs

- Should this change to motion code be blocked or approved?
  - Block: The change does not ship until the motion is fixed. When: Any feel-breaking regression, animation on a keyboard or high-frequency action, scale(0) or ease-in on UI, or a non-GPU animation with an easy GPU fix.
  - Approve: The change ships. When: No feel-breaking regressions, no obvious motion to delete, durations and easing within bounds, interruptibility handled where needed, reduced motion respected.
  - Recommendation: Default to flagging; approval is earned by meeting every Approve criterion.
- Should this action animate at all, given how often people do it?
  - No animation: The action happens instantly. When: Keyboard-initiated or 100+/day actions.
  - Reduced motion: Very little movement. When: Actions seen tens of times a day.
  - Standard animation: Normal entrance and exit motion within the duration budget. When: Occasional actions.
  - Delight: Richer, more expressive motion. When: Rare or first-time moments.
  - Recommendation: Match motion to frequency; deleting the animation is the first remedial move for high-frequency or keyboard-triggered motion.
- When reduced motion is on, should animations become gentler or stop entirely? (`Q-motion-07`)
  - Gentler motion: Opacity and color changes stay; movement is dropped. When: The source's standard for every animation that moves things.
  - Zero motion: All animation removed. When: Rejected by the source: 'gentler, not zero'.
  - Recommendation: Gentler, not zero: keep opacity and color, drop movement.
- What personality should a component's motion have? (`Q-motion-01`)
  - Bouncier: More playful, springy motion. When: Playful components.
  - Crisp: Fast, plain motion. When: Dashboards and professional tools.
  - Recommendation: Match the component's personality and the rest of the product; when unsure, delete the motion.
- Which tool should drive a given animation?
  - CSS transitions, @starting-style or WAAPI: Predetermined motion with CSS performance. When: The motion is known in advance.
  - JS or springs: Motion that can retarget from its current state. When: Dynamic, interruptible, gesture-driven motion.
  - Recommendation: CSS for predetermined motion; JS or springs for dynamic, interruptible, gesture-driven motion.
- Where should a scaling surface grow from?
  - From its trigger: The surface appears to come out of the button that opened it. When: Popovers, dropdowns and tooltips.
  - From center: The surface grows in place. When: Modals only.
  - Recommendation: Trigger-anchored surfaces scale from the trigger via transform-origin; modals stay centered.

### Process

1. Open with the fixed line: When invoked without a question, reply only that you are ready to review animations against a high craft bar from Emil Kowalski's philosophy, and say nothing else until asked.
2. Measure against the ten standards: Check every animation in the diff for justified motion, frequency, easing, sub-300ms duration, origin, interruptibility, GPU-only properties, accessibility, asymmetric timing and cohesion; each violation is a finding.
3. Flag escalation triggers on sight: Hard-flag transition: all, scale(0) or pure-fade entrances, ease-in or weak built-in easing, animation on keyboard or 100+/day actions, UI over 300ms without reason, center origin on trigger-anchored surfaces, keyframes on rapid UI, layout-property animation, busy-page Framer Motion shorthands, parent CSS variables driving child transforms, missing reduced-motion handling, ungated :hover motion, symmetric press/hold timing, and everything-at-once entrances.
4. Propose fixes in preference order: Delete; reduce; fix easing; fix origin and physicality; make interruptible; move to the GPU; asymmetric timing; polish (blur, stagger, @starting-style, springs); accessibility and cohesion.
5. Write the findings table: One markdown table, one row per issue, columns Before | After | Why, citing file:line and exact values from STANDARDS.md.
6. Write the tiered verdict: Group remaining commentary by impact tier, highest first, omitting empty tiers.
7. Decide: Close with Block or Approve according to the stated criteria.
8. Resolve uncertainty about feel: Recommend reviewing in slow motion, frame-by-frame, and with fresh eyes the next day rather than guessing.

### Examples and visual references

- Unbounded transition fixed to a named property: Before: transition: all 300ms. After: transition: transform 200ms ease-out. Shows naming the exact property and shortening the duration.
- Entrance from nothing fixed to a near-full scale: Before: transform: scale(0). After: transform: scale(0.95); opacity: 0. The element no longer appears to come from nowhere.
- Sluggish dropdown easing fixed: Before: ease-in on a dropdown. After: ease-out plus a custom curve, so motion starts fast when the user is watching.
- Popover origin fixed to the trigger (Base UI): Before: transform-origin: center on a popover. After: var(--transform-origin), so the popover grows out of its trigger; modals are exempt.

### Numbers

- 10: Number of non-negotiable standards every animation is measured against. [The Ten Non-Negotiable Standards]
- 100+/day: Actions this frequent (and keyboard-initiated ones) get no animation. [2. Frequency-appropriate]
- 300ms: Upper limit for UI animations without a stated reason. [4. Sub-300ms UI]
- scale(0.9–0.97): Starting scale for entrances instead of scale(0), paired with opacity. [5. Origin & physical correctness]
- scale(0.95): Replacement value for scale(0) in the remedial hierarchy and findings table. [Remedial Preference Hierarchy item 4]
- 30–80ms: Stagger between items in a group entrance. [Aggressive Escalation Triggers]
- 200ms: Duration in the suggested fix transition: transform 200ms ease-out. [Findings table]

<!-- /od:learn -->
