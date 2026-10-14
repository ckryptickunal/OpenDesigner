---
type: source
title: "referodesign/refero_skill: skills/refero-design/references/example-workflow.md"
created: 2026-10-07
updated: 2026-10-07
video_id: referodesign-refero-skil-skills-refero-design-references-example-workflow
url: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/example-workflow.md
channel: referodesign/refero_skill (GitHub, MIT)
published: commit a9b54a3
authority: reference
tags:
  - design-process
  - pricing-page
  - reference-lock
  - decision-ledger
  - research
  - saas
  - tokens
  - refero
---

# referodesign/refero_skill: skills/refero-design/references/example-workflow.md

## Metadata

- Page ID: `referodesign-refero-skil-skills-refero-design-references-example-workflow`
- Publisher: referodesign/refero_skill (GitHub, MIT)
- Published: commit a9b54a3
- URL: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/example-workflow.md

## Summary

This Refero walkthrough shows the full design process on an example task: a pricing page for Northstar, a fictional B2B analytics product for operations teams that must feel trustworthy and precise without looking like a generic AI SaaS template. It moves through discovery (a written brief with audience, goal, tone, main objection and constraints), style research, screen research, flow research, synthesis and an implementation blueprint. The key moves are choosing one primary reference and writing a 'reference lock' that lists what to preserve, what to borrow, role rules, media strategy, what to reject and token commitments, then recording every choice in a design decision ledger with its source and reason. It ends with tokens, a page structure and a quality gate. For a design system it models how to turn research into locked, sourced decisions and tokens.

## Key Ideas

- Start with a written brief: audience, goal, tone, main objection, what must be remembered, constraints and research needed.
- Research styles first for visual or brand tasks, then screens for concrete patterns, then flows for what happens after the click.
- Pick one primary reference as the foundation and borrow only specific details from the others.
- Write a reference lock: preserve, borrow only, role rules, media strategy, reject, token commitments.
- Explicitly reject the generic defaults, such as cream editorial canvas, serif hero, muted clay accent and decorative cards.
- Reserve the accent for one role, here value proof and the selected plan.
- Use product screenshots as evidence, or labelled fixed-ratio placeholders, never fake decorative mockups.
- Place proof modules next to the decision they support, such as ROI near plans and security near Enterprise.
- Record each decision in a ledger with area, decision, source, source rule and why.
- Give the page one memorable detail tied to the product's value.
- Close with a quality gate that checks research influenced each layer and no reference was copied directly.

## Entities

- [[entities/northstar|Northstar]] (product): Fictional B2B analytics product used as the example task.
- [[entities/refero-mcp|Refero MCP]] (tool): Research tool whose refero_get_style, refero_get_screen, refero_get_similar_screens and refero_get_flow calls the workflow uses.
- [[entities/reference-lock|Reference lock]] (concept): A written commitment to one primary direction, listing what is preserved, borrowed, rejected and which tokens are committed.
- [[entities/design-decision-ledger|Design decision ledger]] (concept): Table recording each decision with its source, the source's role rule and the reason.
- [[entities/inter|Inter]] (product): Sans font used in the example token set.

## Topics

- [[topics/design-process|Design process]]: Six phases: discovery brief, styles research, screen research, flow research, synthesis with a decision ledger, and an implementation blueprint with a quality gate.
- [[topics/paywalls-and-pricing-pages|Paywalls and pricing pages]]: 3 plan cards with Pro highlighted, monthly/annual toggle above cards with exact savings, ROI strip, compact comparison table, Enterprise 'Talk to sales' with security cues, FAQ.
- [[topics/ai-assisted-design|AI-assisted design]]: Shows how an agent should use reference research without averaging it: lock one primary direction and reject generic AI defaults.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Token commitments from the reference lock become a small token set: white bg, #171717 text, green accent #1f8a5b, 8px card radius, 4px-based spacing.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Preserve the primary reference's signature traits, borrow bounded details, and justify each choice in a ledger.
- [[topics/a-b-testing-and-conversion|A/B testing and conversion]]: Conversion tactics: 'No credit card required' near the trial CTA, exact annual savings, objection killers under the primary CTA, proof near decision points.

## Notable Claims

- Full styles are large, so larger research should be split into multiple batches. Evidence: Open 3-4 strong styles with refero_get_style
- Screens should be used for concrete pricing decisions after the visual direction is clear. Evidence: Phase 2: Screen Research
- Flows matter because pricing can lead into upgrade, checkout or sales contact journeys. Evidence: Phase 3: Flow Research
- A muted green accent with white, charcoal and cool neutrals reads trustworthy and precise and avoids generic blue/purple SaaS. Evidence: Design Decision Ledger, Palette

## Quotes

> Make Enterprise feel like a tailored plan, not a vague catch-all.

> The page has one memorable detail tied to this product's value.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Northstar and its references (Style A-D) are placeholders; the source says to replace them with real MCP results.
- Caveat: The workflow depends on Refero's MCP tools, which are a product of the source's authors.
- Caveat: Pricing decisions (3 plans, Pro highlighted) are specific to this example, not general rules.
- Caveat: The research summary says 5 styles were reviewed while the findings table lists four (Style A-D); the numbers are illustrative.

### Rules and practices

- **should** (process, all): Write a discovery brief before research that states audience, goal, tone, main objection or risk, what must be remembered, constraints and research needed. Why: It frames which research to run and what the page must achieve [inferred]. [Phase 0: Discovery]
- **should** (process, all): For a visual or brand task, research styles first, then screens for concrete patterns, then flows for the post-click journey. Why: Screens are used for concrete decisions after the visual direction is clear. [Start with styles because this is a visual/brand task.]
- **should** (process, all): Write a reference lock naming the primary direction, what to preserve, what to borrow only, role rules, media strategy, what to reject, and token commitments. Why: It keeps the primary direction from being diluted by secondary references [inferred]. [Reference lock]
- **should** (process, all): Record every design decision in a ledger with area, decision, source, the source's rule or role, and why. Why: Makes each choice traceable to research and the brief [inferred]. [Design Decision Ledger]
- **should** (color, all): Reserve the accent color for one role, such as value proof and the selected plan state. Why: Accent discipline keeps the page trustworthy and precise. Values: #1f8a5b, #e8f5ee. [Role rules: green proof accent only for selected state/value proof]
- **should** (iconography, all): Use real product screenshots as evidence, or fixed-ratio labelled placeholders with art direction when none exist, not fake decorative app mockups. Why: Keeps proof honest without low-quality invented imagery. [Media strategy]
- **should** (patterns, web): Place proof modules next to the decision they support, for example ROI metrics near plans and security/procurement cues near the Enterprise CTA. Why: Answers buyer objections where they appear. [Proof: ROI metrics near pricing, security near Enterprise]
- **consider** (content, web): Put "No credit card required" next to the trial CTA rather than in the FAQ. Why: Concrete tactic from screen research. [Concrete tactics to adapt]
- **consider** (content, web): Show annual savings as an exact value where possible, not just a percentage. Why: Pricing should feel transparent. [Concrete tactics to adapt]
- **should** (components, web): Give primary button treatment only to the self-serve action (Pro trial) and make Enterprise sales secondary. Why: Supports both self-serve and sales-led paths. [CTA hierarchy]
- **should** (components, web): Use cards only for plan comparison and interaction, with thin borders, a subtle selected state and no heavy shadows. Why: Keeps evaluation calm and scannable. Values: 8px max radius. [Cards: Thin borders, subtle selected state, no heavy shadows]
- **should** (patterns, web): Repeat the selected plan, billing period, savings and renewal date in checkout, and keep the selected plan visible through signup. Why: Flow research decisions for confirming annual billing and letting users recover without losing state. [Flow Findings]
- **should** (process, all): Before shipping, check that styles shaped the visual language, screens the structure, flows the journey, no reference was copied directly, the palette is not indigo/violet, and the first viewport makes the decision clear. Also check buyer objections are handled near the relevant action and the page has one memorable detail tied to the product's value. Why: Quality gate. [Quality Gate]
- **should** (layout, web): Keep the first viewport decisive: use a comparison table for evaluation buyers, but compact by default, under the cards, grouped by buyer concern, with expandable details. Why: Concrete tactic from screen research. [keep the first viewport decisive]
- **consider** (patterns, web): Make Enterprise a tailored plan with a "Talk to sales" CTA that opens a short form asking only essential qualification fields such as company size. Why: Enterprise should not feel like a vague catch-all. [Enterprise CTA opens short sales form with company size]
- **consider** (content, web): Use a literal page headline ("Pricing") with a short value sentence, and put an objection killer under the primary CTA. Why: Part of the example page structure. [Literal headline: "Pricing"]
- **consider** (process, all): Explicitly list what the direction rejects, such as a cream editorial canvas, serif hero, muted clay/orange accent and decorative cards. Why: The reference lock names generic defaults to avoid. [Reject: cream editorial canvas, serif hero, muted clay/orange accent, decorative cards.]

### Decisions it informs

- Which reference should be the primary foundation when several conflict? (`Q-brand-02`)
  - Data infrastructure website: Dense technical credibility, grid structure, product screenshot framing. When: Chosen here for a precise, evidence-led B2B analytics page.
  - Editorial monochrome SaaS: Strong type hierarchy, low color, confidence through restraint. When: Borrowed only for type hierarchy and low color discipline.
  - Productivity SaaS: Airy spacing, friendly trust, softer sections. When: Borrowed only for section spacing and proof blocks.
  - Premium fintech: Accent discipline, numbers presented with authority. When: Borrowed only for the proof treatment.
  - Recommendation: Data infrastructure website as the primary, with the others contributing bounded details.
- How many plans and which is highlighted?
  - 3 plans, Pro highlighted: Starter, Pro, Enterprise with Pro as the default choice. When: This example.
  - Recommendation: 3 plans with Pro highlighted as default.
- Where does the monthly/annual toggle go?
  - Above the plan cards: Billing period is set before comparing plans; show exact annual savings. When: This example.
  - Recommendation: Above the cards, with exact annual savings.
- How detailed should the feature comparison be? (`Q-pattern-03`)
  - Compact with expandable details: First viewport stays decisive; evaluation buyers can dig in. When: This example.
  - Complete table: All features at once. When: Not chosen.
  - Recommendation: Compact comparison under the cards, grouped by buyer concern, with expandable details.
- What does the trial CTA start with?
  - Account creation before payment: Lower friction to start a trial. When: This example.
  - Recommendation: Account creation before payment.

### Process

1. Phase 0: Discovery: Write a brief: audience, goal, tone, main objection/risk, must remember, constraints, research needed.
2. Phase 1: Styles research: Run several style searches, open 3-4 strong styles, note what each contributes and what to adapt, choose a primary foundation and write a reference lock.
3. Phase 2: Screen research: Search for concrete patterns (toggle, comparison table, contact sales, ROI calculator), open the strongest screens, and record a decision per pattern.
4. Phase 3: Flow research: Search the journeys after the click (upgrade, checkout, sales contact, trial signup) and decide each journey question.
5. Phase 4: Synthesis: Write a research summary and a design decision ledger with area, decision, source, source rule and why.
6. Phase 5: Implementation blueprint: Define tokens and the page structure, then pass the quality gate before shipping.

### Examples and visual references

- Northstar pricing page direction (Northstar (fictional)): White canvas, deep charcoal text, compact sans-led headlines, thin rule lines, quiet plan cards, exact operational metrics, one muted green accent for value proof and selected actions.
- Example token set (Northstar (fictional)): Inter sans, bg #ffffff, text #171717, muted #6b7280, line #e5e7eb, accent #1f8a5b, accent-soft #e8f5ee, 8px card radius, spacing 4/8/12/16/24/32/48/64px.
- Page structure (Northstar (fictional)): Literal 'Pricing' header with toggle, three plan cards, operational value strip (saved hours, faster reporting, forecast confidence), compact comparison, Enterprise proof, FAQ.
- Memorable detail (Northstar (fictional)): An 'Operational value' strip showing saved hours and cost by plan, used as evidence rather than decoration.

### Numbers

- 3-4: Strong styles to open with refero_get_style. [Open 3-4 strong styles]
- 5: Styles reviewed in the research summary. [Styles reviewed: 5]
- 8px: Maximum radius / card radius committed in the tokens. [8px max radius; --radius-card: 8px]
- 15-16px: Readable body text size. [readable 15-16px body]
- 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px: Spacing scale in the example tokens. [--space-1 to --space-16]
- 3: Number of plans, with Pro highlighted. [Use 3 plans; highlight Pro as default]

<!-- /od:learn -->
