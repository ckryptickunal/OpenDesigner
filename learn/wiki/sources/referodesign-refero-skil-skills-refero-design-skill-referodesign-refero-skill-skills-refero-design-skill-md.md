---
type: source
title: "referodesign/refero_skill: skills/refero-design/SKILL.md"
created: 2026-10-07
updated: 2026-10-07
video_id: referodesign-refero-skil-skills-refero-design-skill
url: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/SKILL.md
channel: referodesign/refero_skill (GitHub, MIT)
published: commit a9b54a3
authority: reference
tags:
  - ai-agents
  - research-first
  - references
  - reference-lock
  - decision-ledger
  - anti-ai-slop
  - design-process
  - token-roles
  - agent-skill
---

# referodesign/refero_skill: skills/refero-design/SKILL.md

## Metadata

- Page ID: `referodesign-refero-skil-skills-refero-design-skill`
- Publisher: referodesign/refero_skill (GitHub, MIT)
- Published: commit a9b54a3
- URL: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/SKILL.md

## Summary

This is the main SKILL.md of Refero's agent skill, a research-first methodology for AI agents doing UI and product design. It says every design must be grounded in references before implementation, using three research layers: styles for visual direction, screens for concrete UI patterns, and flows for multi-step journeys. It teaches agents to pick one dominant reference and preserve its sharp traits rather than averaging several references into a safe middle, and to keep each token in the role its source gave it. Before building, the agent writes a design brief, a reference lock and a decision ledger that traces every major choice to a reference, a user constraint or a craft rule. It ends with craft rules aimed at avoiding generic AI design defaults and a quality gate checklist, which matters to a design system builder because it shows how to keep a chosen direction from drifting into the bland centroid.

## Key Ideas

- Research references before any design work instead of relying on the model's generic taste.
- Use three research layers: styles for look and feel, screens for concrete UI patterns, flows for journeys.
- Do not copy one reference and do not average several; choose one dominant direction and borrow 1-2 narrow details.
- Keep token roles from the source: a CTA color stays CTA-only, syntax colors stay inside code, decorative gradients stay decorative.
- Write a short brief first and ask only for information that would materially change the result.
- Lock the direction before building with a reference lock: primary source, traits to preserve, borrowed details, role rules, media strategy, rejects, token commitments.
- Convert research into a decision ledger; a major choice with no source is researched more, tied to a constraint, or removed.
- Choose the lightest workflow: direct build, visual exploration with three options, audit, or asset generation.
- Match research depth to task risk.
- Preserve imagery roles; an honest, well-sized placeholder beats a weak fake illustration made of CSS.
- Treat calm editorial looks, cream canvases, earthy palettes, decorative headline word swaps and default indigo/violet as AI-slop risks unless research justifies them.
- Create at least one memorable detail users would remember.
- Validate the rendered build against the locked target and fix drift before handoff.

## Entities

- [[entities/refero|Refero]] (product): Design reference library whose agent skill this is; offers styles, screens and flows through an MCP server.
- [[entities/refero-mcp|Refero MCP]] (tool): MCP server at api.refero.design with tools such as refero_search_styles, refero_get_style, refero_search_screens and refero_search_flows.
- [[entities/reference-lock|Reference lock]] (concept): A written commitment to one primary reference and the traits, roles and tokens that must survive implementation.
- [[entities/decision-ledger|Decision ledger]] (concept): Table tying each design decision to its source, the role to preserve and the reason.
- [[entities/claude-code|Claude Code]] (tool): Host where the skill installs the Refero MCP with claude mcp add.
- [[entities/attio|Attio]] (company): Named in an example style query for editorial SaaS typography.
- [[entities/linear|Linear]] (company): Named in an example style query for a dark developer-tool changelog.
- [[entities/shadcn|shadcn]] (library): Named in an example style query for a monochrome design system.

## Topics

- [[topics/ai-assisted-design|AI-assisted design]]: A full methodology for AI agents doing design: research first, lock a reference, keep a decision ledger, and pass a quality gate against generic AI defaults.
- [[topics/design-process|Design process]]: Brief, workflow routing, research by layer, synthesis into three buckets, presenting findings, building, then visual validation.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Pick one dominant direction, preserve its sharp traits, avoid averaging references and avoid listed AI-slop defaults.
- [[topics/design-resources|Design resources]]: Explains how to use a reference library's styles, screens and flows and what to extract from each.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Define tokens before implementation and keep each token in the role its source assigned.
- [[topics/landing-pages|Landing pages]]: Styles cover marketing pages; avoid the generic hero, features grid, pricing, FAQ, CTA sequence unless research supports it.
- [[topics/typography|Typography]]: Use text-wrap: balance for headings and short display text, text-wrap: pretty selectively for prose; avoid decorative serif or italic word swaps.
- [[topics/color|Color]]: Use brand-appropriate colors from research, keep accents rare when the reference does, and do not default to indigo or violet.
- [[topics/icons-and-imagery|Icons and imagery]]: Preserve the imagery role of an image-led style; use real, generated or stock assets, or an intentional placeholder with art direction.
- [[topics/paywalls-and-pricing-pages|Paywalls and pricing pages]]: Example pattern: billing toggle above plan cards, one highlighted plan, detailed comparison below.
- [[topics/onboarding|Onboarding]]: Onboarding and signup are listed as flow research cases; extract entry point, step count, friction reducers and system responses.

## Notable Claims

- Generic frontend or product design skills tend to pull work back toward generic AI design. Evidence: Non-Negotiables: generic design skills tend to pull work back toward generic AI design
- Refero styles currently cover web marketing and product pages, not in-app dashboards, auth screens, settings screens or iOS app screens. Evidence: Current limitation: Refero styles currently cover web marketing/product pages
- A style is a semantic design reference extracted from a real web page, not a screenshot and not a component library. Evidence: Use Styles First For Visual Work
- Averaging conflicting references produces a bland result, e.g. dark, acid and serif references collapse into warm cream, muted orange and a polite serif. Evidence: Synthesis rule: the answer is not warm cream + muted orange + polite serif
- Image generation can be slow and may not exist in every coding environment. Evidence: Non-Negotiables: Use image generation only when it changes the outcome
- Calm editorial styling is a current AI-slop risk. Evidence: Core craft rules: Treat "calm editorial" as a current AI-slop risk
- Pricing pages commonly put the billing toggle above plan cards, highlight one plan and move detailed feature comparison below. Evidence: Synthesis, Product Pattern output example
- Cancellation flows usually collect a reason, offer an alternative, confirm the destructive action and state when access ends. Evidence: Synthesis, Journey Logic output example

## Quotes

> Do not average references into a safe middle.

> A brief is not a build target.

> No design from vibe memory.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: This is a vendor's own skill: it insists on Refero MCP research and tells agents not to use generic design skills as a parallel design authority, which is self-promotion.
- Caveat: The style library is limited to web marketing and product pages, per the source's own stated limitation.
- Caveat: The AI-slop list (calm editorial, cream canvases, indigo/violet) is the authors' opinion of current trends and may date.
- Caveat: Linked reference files (typography.md, color.md, visual-workflow.md and others) were not part of this raw source.

### Rules and practices

- **must** (process, all): Ground every design in researched references before implementation instead of the model's generic design taste. Why: The source says not to rely on the model's generic design taste; references give taste and product evidence. [Non-Negotiables: Research before design work]
- **must** (process, all): When references conflict, choose one dominant direction, preserve its sharp traits and let secondary references add only narrow details. Why: Averaging collapses the direction into a safe middle. [Do not average references into a safe middle]
- **must** (process, all): Do not copy a single reference; study several strong references and synthesize a new direction for the product. Why: The result should be a new direction inspired by several references, not a copy. [Do not copy one reference]
- **must** (tokens, all): Use a token only for the role its source assigns: CTA colors stay CTA-only, syntax colors stay inside code, decorative gradients stay decorative. Why: Repurposing tokens changes their meaning and breaks the direction. [Do not change token meanings; Never move a token outside its source role]
- **must** (color, all): Do not turn a CTA accent into a background, a code-only color into UI chrome, or a decorative gradient into an interface surface. Why: Token roles from references must be preserved. [Core craft rules: Preserve token roles from references]
- **must** (components, all): Keep card and button rules at their specified radius, shadow and state behavior when borrowing them. Why: The source says never to move a token outside its source role, and lists card and button rules among those roles. [card/button rules keep their specified radius, shadow, and state behavior]
- **must** (iconography, all): If the primary style is image-led, keep the image slot with stable dimensions, aspect ratio, caption or alt text and an art-direction note rather than switching to a text-only layout. Why: The media role is part of the style; weak fakes are worse than an honest placeholder. [If the primary style is image-led, do not replace it with text-only layout]
- **must** (iconography, all): Do not fake complex imagery with weak CSS, text or decorative boxes. Why: An honest, well-sized placeholder beats a poor fake illustration or photo. [Respect imagery guidance]
- **must** (process, all): Write a reference lock (primary direction, 3-5 traits to preserve, 1-2 borrowed details, role rules, media strategy, rejects, token commitments) before implementation. Why: It stops implementation drifting into safer colors, fonts, radius or generic layouts. Values: 3-5, 1-2. [Before implementation, create a reference lock]
- **must** (process, all): If implementation drifts from the lock, stop and correct it; do not soften distinctive traits into safer colors, fonts, softer radius or generic section layouts. Why: Softening loses the chosen direction. [If implementation drifts from the lock, stop and correct it]
- **must** (process, all): Before implementation, fill a decision ledger with Decision, Source, Source rule / role and Why for each major choice, and remove any major choice that has no source. Why: Every major choice must trace to a reference, user constraint or craft rule. [convert research into a short decision ledger]
- **should** (process, all): In discovery, ask only for missing information that would materially change the result; otherwise assume and proceed. Why: Keeps the brief short without blocking work. [Discovery]
- **should** (process, all): For variants, a new visual language, a major redesign or a landing page, default to three reference-locked options and ask the user to choose. Why: High-visibility surfaces have several plausible directions. Values: three. [Workflow Routing: Visual exploration]
- **must** (tooling, all): Use image generation only for visual exploration, mockups, imagery, illustrations, textures and difficult assets; skip it for small fixes, obvious production edits or code-native UI. Why: It can be slow and may not exist in every environment. [Use image generation only when it changes the outcome]
- **should** (process, all): Use styles, not screens, as the primary source for visual direction; use screens afterwards for structure and concrete details. Why: Styles are the layer for visual direction and taste; screens are for structure and concrete UI patterns. [Avoid using screens as the primary style source when the task is visual]
- **must** (tokens, all): Define tokens before implementation: type scale, colors, spacing, radius, shadows. Why: Core craft rule after research. [Core craft rules]
- **must** (color, all): Do not default to indigo or violet unless the user explicitly asks for it; use brand-appropriate colors from research. Why: Listed as a generic AI design default. [Core craft rules: Do not default to indigo/violet]
- **must** (typography, all): Do not default to decorative headline word swaps (one word or short phrase set in a different display, serif, script or italic style or accent color) unless research and product context justify them. Why: The source treats calm editorial as a current AI-slop risk, and the quality gate checks for these swaps. [Treat "calm editorial" as a current AI-slop risk]
- **must** (color, all): Do not default to warm ivory or cream canvases or olive, clay or terracotta palettes unless research and product context justify them. Why: The source lists these as part of the calm editorial look it treats as a current AI-slop risk. [Core craft rules: Treat "calm editorial" as a current AI-slop risk]
- **should** (layout, web): Avoid the generic hero, features grid, pricing, FAQ, CTA page sequence unless research supports it. Why: It is a generic AI design default. [Avoid generic hero -> features grid -> pricing -> FAQ -> CTA]
- **should** (typography, css): Use text-wrap: balance on headings and short display text, use text-wrap: pretty selectively for prose, and check key breakpoints for orphan words. Why: Avoids orphan words and awkward final lines. Values: text-wrap: balance, text-wrap: pretty. [Core craft rules: Balance headings]
- **should** (process, all): Create at least one memorable detail: a visual move, interaction, layout choice or copy detail. Why: Users should remember something about the design. [Create at least one memorable detail]
- **should** (content, all): Use real product evidence for copy, trust signals, objection handling and section order. Why: Avoids invented content decisions. [Core craft rules]
- **should** (accessibility, all): Build accessibility and responsive behavior into the design, not as a late pass. Why: Core craft rule. [Keep accessibility and responsive behavior in the design]
- **must** (process, all): After building visual work, compare the rendered implementation against the locked target and fix actionable drift before handoff. Why: Research alone is not sufficient. [Validate after building visual work]
- **should** (process, all): Give the user a short research summary before designing a non-trivial task instead of dumping every result. Why: Keeps findings readable. [Present Findings]
- **must** (process, all): Make research output specific: name the references, describe concrete choices and explain what will be adapted. Why: Stated as a non-negotiable so that every decision can be traced. [Non-Negotiables: Research output must be specific]
- **must** (process, all): Before implementation, lock a build target: a user-provided visual source, an existing product or design-system target, a selected generated mockup, or an approved reference-locked direction; a brief alone is not enough. Why: A brief is not a build target. [Non-Negotiables: A brief is not a build target]
- **should** (process, all): When combining styles, give each source a bounded job, for example one owns canvas and type, another the code-window treatment, another the primary CTA. Why: Keeps borrowed details from spreading beyond their role. [When combining styles, assign each source a bounded job]
- **should** (iconography, all): Build simple diagrams, icons, code windows or geometric primitives only when they match the source style. Why: Code-native stand-ins must fit the primary style's media role. [Build simple diagrams, icons, code windows, or geometric primitives only when they match the source style]
- **must** (process, all): Preserve the primary reference's strongest traits instead of normalizing them. Why: Normalizing traits collapses the chosen direction. [Core craft rules]
- **must** (content, all): Present the result as a new direction inspired by several references, never as copying one. Why: The aim is a new direction for the user's product, not a clone. [Never present the result as "copying X"]
- **must** (process, all): Before final delivery, run the quality gate checklist; if any answer is no, research or refine more before delivering. Why: Catches copying, averaging, lost token roles and generic AI defaults before handoff. [Quality Gate]
- **should** (tooling, all): Load bundled craft references only when relevant; do not load every file by default. Why: Stated in the Design Craft section [inferred: keeps context small]. [Design Craft: do not load every file by default]

### Decisions it informs

- Which workflow fits this design task?
  - Direct build: Research and lock the direction, then code straight away. When: Small UI fixes, clear production edits, existing design-system work, or a concrete source to match.
  - Visual exploration: Three reference-locked options the user chooses between. When: Variants, a new visual language, a major redesign, a landing page or another high-visibility surface.
  - Audit: Critique grounded in screenshots, screens or flows as evidence. When: Reviewing an existing design.
  - Asset generation: Generated bitmap imagery. When: The reference lock needs bitmap media that code, icons or existing assets cannot provide.
  - Recommendation: Choose the lightest workflow that can produce a high-quality result.
- How do you combine several references that point in different directions?
  - Copy one reference: A clone of someone else's product. When: Never.
  - Average all references: A safe, bland centroid such as warm cream, muted orange and a polite serif. When: Never.
  - One primary plus borrowed details: The primary style sets mood, density and structure; secondary styles add 1-2 bounded details. When: Always.
  - Recommendation: One primary foundation with 1-2 borrowed details, each source given a bounded job, because averaging loses the sharp traits.
- Which research layer should answer this question?
  - Styles: Look and feel: typography, palette, layout, spacing, radius, elevation, imagery. When: Any task with a visual component; start here.
  - Screens: What a screen contains: layout, hierarchy, components, CTAs, copy, states. When: A specific screen type, component or UI pattern.
  - Flows: Steps, decision points, confirmations, recovery and system responses. When: Onboarding, signup, checkout, cancellation or any multi-step process.
  - Recommendation: Combine layers: styles for visual direction, screens for patterns, flows for sequencing.
- What do you put in an image slot when you cannot make the image the style needs?
  - Fake it in CSS or text: Weak decorative boxes standing in for imagery. When: Never.
  - Switch to a text-only layout: Loses the image-led character of the style. When: Never for an image-led primary style.
  - Intentional placeholder: Stable dimensions, aspect ratio, caption or alt text and an art-direction note. When: When real, generated or stock assets are not available.
  - Recommendation: Use real, generated or stock assets when available; otherwise an honest, well-sized placeholder.

### Process

1. Write a brief: Designing [WHAT] for [WHO] on [PLATFORM], with goal, tone, main objection, must-remember hook, constraints, research needed and path.
2. Route the workflow: Pick direct build, visual exploration, audit or asset generation; the lightest that gives a high-quality result.
3. Research styles: Search 3-5 visual angles (one broad aesthetic, one domain, one known brand), retrieve 3-4 full styles, compare, pick one primary and borrow 1-2 details.
4. Research screens: Search by page type, component, state, company or on-screen text; extract layout, hierarchy, components, CTAs, copy, states and tactics.
5. Research flows: For multi-step tasks, extract entry and exit, step count, decisions, friction reducers, confirmations, recovery, errors and system responses; broaden or reconstruct from screens if sparse.
6. Match depth to risk: Quick improvement: 2-3 style searches, 2-3 full styles, 1 short synthesis. New landing page or redesign: 3-5 searches, 3-4 full styles, plus screen research.
7. Synthesize into three buckets: Visual direction from styles, product pattern from screens, journey logic from flows.
8. Create a reference lock: Primary direction, traits to preserve, borrowed details, role rules, media strategy, rejects and token commitments.
9. Present findings and ledger: Give a short research summary and a decision ledger with source, role and reason for each choice.
10. Build with craft rules: Define tokens first, preserve roles and signature traits, avoid listed AI defaults.
11. Quality gate and visual QA: Run the checklist and compare the rendered result to the lock; research or refine more if any answer is no.

### Examples and visual references

- Visual direction synthesis for an analytics SaaS: White canvas, compact UI copy, restrained black primary actions, thin borders, product screenshots in framed panels, accent color kept rare.
- Pricing page pattern: Billing toggle above plan cards, one plan highlighted, detailed feature comparison moved below; hero kept quieter for a product that sells trust.
- Cancellation flow logic: Collect a reason, offer a relevant alternative, confirm the destructive action, state when access ends, give a clear return path.
- Example style queries (Attio, Linear, shadcn): Queries like 'Linear changelog dark developer tool' and 'shadcn monochrome design system' show how to search by brand, domain and aesthetic.
- Averaging failure: Dark, acid and serif references averaged into warm cream, muted orange and a polite serif: the bland centroid to avoid.

### Numbers

- 3-5: Different visual angles to search for styles; also traits to preserve in a reference lock [Recommended loop; Preserve: [3-5 traits]
- 3-4: Full styles to retrieve in one batch [Retrieve 3-4 strong styles]
- 1-2: Specific details to borrow from secondary styles [borrow 1-2 specific details]
- 2-3: Style searches and full styles for a quick visual improvement [Research Depth: For a quick visual improvement]
- three: Default number of reference-locked options in visual exploration [Default to three reference-locked options]
- 1: Short synthesis for a quick visual improvement [Research Depth: 1 short synthesis]

<!-- /od:learn -->
