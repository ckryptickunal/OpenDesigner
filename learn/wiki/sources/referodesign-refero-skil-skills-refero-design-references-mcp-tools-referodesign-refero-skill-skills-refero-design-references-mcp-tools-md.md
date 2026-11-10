---
type: source
title: "referodesign/refero_skill: skills/refero-design/references/mcp-tools.md"
created: 2026-10-07
updated: 2026-10-07
video_id: referodesign-refero-skil-skills-refero-design-references-mcp-tools
url: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/mcp-tools.md
channel: referodesign/refero_skill (GitHub, MIT)
published: commit a9b54a3
authority: reference
tags:
  - refero
  - mcp
  - design-research
  - references
  - agent-tools
  - user-flows
  - styles
---

# referodesign/refero_skill: skills/refero-design/references/mcp-tools.md

## Metadata

- Page ID: `referodesign-refero-skil-skills-refero-design-references-mcp-tools`
- Publisher: referodesign/refero_skill (GitHub, MIT)
- Published: commit a9b54a3
- URL: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/mcp-tools.md

## Summary

A tool reference for Refero's MCP server, which gives an AI agent three research layers: styles for visual direction and taste, screens for concrete UI patterns, and flows for multi-step journeys. It lists each tool, its parameters, good example queries and how to search well, plus common mistakes and what to do when results are weak. Its key method is to search several visual angles, treat each returned style as an ingredient rather than a template, pick one primary foundation and borrow one or two details from others. For a design system it shows a research-first way to gather references before choosing tokens, while translating everything to the person's own product.

## Key Ideas

- Refero research has three layers: styles (taste), screens (UI patterns), flows (journeys)
- Search styles first for anything about visual direction, brand feel, type, color, layout or polish
- Run 3-5 style searches from different angles: broad aesthetic, domain, and a known brand
- Do not stop at the first good result; use later pages to find less obvious directions
- Treat each style as a reference ingredient, not a template; never copy one style directly
- Pick one primary foundation for mood and density and borrow 1-2 details from other styles
- Extract layout, component, spacing and elevation rules, not only colors and fonts
- Search screens by what is literally on the screen, using concrete UI terms
- Styles currently cover web marketing and product pages, not dashboards, auth, settings or iOS screens
- Use flows for journey logic such as onboarding, checkout, cancellation and password reset
- When results are weak, broaden the query, drop adjectives, try adjacent categories or a known product

## Entities

- [[entities/refero|Refero]] (product): Design reference library exposed to agents through an MCP server with refero_ tools
- [[entities/model-context-protocol-mcp|Model Context Protocol (MCP)]] (concept): The protocol through which agents call the Refero tools
- [[entities/refero-search-styles|refero_search_styles]] (tool): Semantic search over curated design styles
- [[entities/refero-get-style|refero_get_style]] (tool): Returns full style references (colors, type, layout, components, do/don't rules) for style UUIDs
- [[entities/refero-search-screens|refero_search_screens]] (tool): Semantic search over real UI screens for web or iOS
- [[entities/refero-get-screen|refero_get_screen]] (tool): Full metadata for one or more screens
- [[entities/refero-get-similar-screens|refero_get_similar_screens]] (tool): Visually and functionally similar screens for one screen
- [[entities/refero-get-screen-image|refero_get_screen_image]] (tool): Raw screenshot image for a screen, thumbnail or full
- [[entities/refero-search-flows|refero_search_flows]] (tool): Search connected screens showing how a user completes a task
- [[entities/refero-get-flow|refero_get_flow]] (tool): Step-by-step details of user flows
- [[entities/attio|Attio]] (company): Named in an example style query for editorial SaaS typography
- [[entities/linear|Linear]] (company): Named in an example style query for a dark developer-tool changelog

## Topics

- [[topics/ai-assisted-design|AI-assisted design]]: How an agent should use Refero's MCP tools to research styles, screens and flows before designing.
- [[topics/design-resources|Design resources]]: Refero as a searchable reference library of styles, real screens and user flows.
- [[topics/design-process|Design process]]: Research-first method: several search angles, one primary foundation plus borrowed details, translated to the user's product.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Styles are used to establish taste and visual language; never copy a single style.

## Notable Claims

- Styles currently focus on web marketing and product pages and do not cover in-app dashboards, auth screens, settings screens or iOS app screens as style systems. Evidence: Current coverage
- Full styles are large, so the recommended maximum batch for refero_get_style is 3-4 IDs. Evidence: refero_get_style parameters: recommended max batch is 3-4
- refero_get_similar_screens takes an optional limit whose default is usually 10 and maximum usually 20. Evidence: refero_get_similar_screens: Default is usually 10; max is usually 20
- refero_get_screen_image returns image content and can use more context than text tools. Evidence: refero_get_screen_image
- Flow IDs are numeric while style and screen IDs are UUIDs. Evidence: refero_get_flow: Numeric flow ID

## Quotes

> Treat each style as a reference ingredient, not a template.

> Search by what is literally on the screen.

> Do not copy a single style directly.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: This is product documentation for Refero's own MCP tools; it promotes Refero as the research source.
- Caveat: Tool names, parameters and coverage are tied to commit a9b54a3 and will change as the server changes.
- Caveat: Most content is tool-usage detail rather than design guidance; the transferable parts are the research method and reference-use rules.

### Rules and practices

- **should** (process, all): Search Refero styles first for any task involving visual direction, brand feel, typography, color, layout, spacing, elevation, components, imagery or polish. Why: Styles are the layer for visual direction and taste. [refero_search_styles: Use first for any task with visual direction]
- **should** (process, all): Run 3-5 style searches from different visual angles, including one broad aesthetic query, one domain or category query, and one known-brand query when relevant. Why: Do not stop at the first good result. Values: 3-5. [Search method]
- **should** (process, all): Pick one style as the primary foundation for mood and density and borrow only 1-2 specific details from other styles. Why: Each style is a reference ingredient, not a template. Values: 1-2. [How to use returned styles]
- **should** (process, all): Extract layout, component, spacing and elevation rules from a reference style, not only its colors and fonts. Why: Listed in how to use returned styles. [How to use returned styles]
- **should** (process, all): Keep the source's token, component and imagery roles instead of repurposing them; use real, generated or stock assets, or an intentional art-directed placeholder when none is available. Why: Preserve source roles and media roles. [Preserve source token/component roles]
- **must** (process, all): Translate every borrowed reference to the user's product, audience and constraints; never copy a single style directly. Why: Styles are ingredients, not templates. [Common Mistakes: Do not copy a single style directly]
- **should** (tooling, all): Write screen searches with concrete UI terms for what is literally on the screen (e.g. 'pricing page annual monthly toggle'), and search styles first when the query is aesthetic. Why: Concrete terminology beats broad aesthetic words for screens. [Search guidance]
- **must** (process, all): Do not rely on screens as the main source of visual taste when styles are available. Why: Styles are the taste layer; screens are for product-specific logic. [Common Mistakes]
- **must** (tooling, all): Do not assume Refero styles cover dashboards, auth screens, settings or iOS app screens; for those, use styles for taste and screens/flows for structure. Why: Listed as a common mistake; current style coverage is web marketing and product pages. [Common Mistakes]
- **should** (tooling, all): Fetch at most 3-4 full styles per refero_get_style batch, and retry screen batches with fewer IDs if one fails. Why: Full styles are large. Values: 3-4. [refero_get_style; Batching]
- **should** (tooling, all): Use refero_get_screen_image only when text metadata is not enough to judge a screen. Why: Images use more context than text tools. [refero_get_screen_image]
- **must** (tooling, all): Do not pass limit, image_size or include_similar to search tools, or image_size/include_similar to refero_get_screen; use the dedicated image and similar-screens tools. Why: Listed as common mistakes. Values: limit, image_size, include_similar. [Search guidance; Common Mistakes]
- **must** (tooling, all): Do not use old _tool suffixed names or call get_design_guidance; use the styles, screens and flows tools. Why: Listed as common mistakes. Values: _tool, get_design_guidance. [Common Mistakes]
- **should** (process, all): When results are weak, broaden the query, remove adjectives, search adjacent categories, try a known product, inspect later pages, and for sparse flows rebuild the journey from related screens. Why: If Results Are Weak guidance. [If Results Are Weak]
- **should** (tooling, all): Call the Refero tools by the exact names the client shows (they carry the refero_ prefix, possibly namespaced). Why: MCP clients may namespace tool names. Values: refero_. [Intro]
- **must** (tooling, all): Pass exactly one of the single-id or multi-id parameters (style_id or style_ids, screen_id or screen_ids, flow_id or flow_ids). Why: The parameter tables require exactly one. [Parameter tables]
- **should** (tooling, all): Pass response_format (md or json) only when the client's tool schema includes it. Why: Only some clients expose it. Values: md, json. [Response Formats]

### Decisions it informs

- Which Refero research layer fits the question at hand?
  - Styles: Gives visual direction and taste: colors, type, layout, elevation, do/don't rules When: Brand feel, aesthetics, design-system inspiration, visual polish
  - Screens: Shows concrete page structure, components, hierarchy, copy and states When: Product-specific UI decisions
  - Flows: Shows step-by-step journey logic across connected screens When: Onboarding, checkout, cancellation, upgrade, password reset and other sequences
  - Recommendation: Styles first for taste, then screens and flows for product logic.
- Return research in markdown or JSON?
  - md: Human-readable research notes When: Default, reading
  - json: Structured fields When: Structured comparison or programmatic extraction
  - Recommendation: Use only when the client's tool schema exposes response_format.

### Process

1. Search styles: Run 3-5 refero_search_styles queries from different angles (broad aesthetic, domain, known brand); page through results.
2. Get full styles: Call refero_get_style on the promising UUIDs, 3-4 at most per batch.
3. Compose a direction: Pick one primary foundation for mood and density, borrow 1-2 details from others, extract layout, component, spacing and elevation rules.
4. Search screens: Use refero_search_screens with literal UI terms and a platform (web or ios); open strong hits with refero_get_screen and refero_get_similar_screens.
5. Inspect images if needed: Use refero_get_screen_image only when metadata is not enough.
6. Search flows: For journeys, use refero_search_flows then refero_get_flow for goals, actions, system responses and screens.
7. Translate: Map everything to the user's product, audience and constraints.
8. Recover from weak results: Broaden, drop adjectives, try adjacent categories or a known product, inspect later pages, rebuild sparse flows from screens.

### Examples and visual references

- Example style queries such as 'editorial monochrome SaaS landing page' and 'premium fintech website with restrained typography' (refero_search_styles): Shows the mix of aesthetic, domain and brand angles a style search should cover.
- Known-brand style queries: 'Attio editorial SaaS typography', 'Linear changelog dark developer tool' (refero_search_styles): Demonstrates the known-product query angle.
- Example screen queries such as 'pricing page annual monthly toggle', 'dashboard empty state', 'destructive action confirmation' (refero_search_screens): Shows literal, concrete UI terms rather than aesthetic words.
- Example flow queries such as 'checkout with promo code', 'subscription cancellation', 'password reset 2FA' (refero_search_flows): Shows task- and journey-based query wording.

### Numbers

- 3-5: Number of different visual angles to search for styles [Search method]
- 3-4: Recommended maximum batch of full styles [refero_get_style]
- 1-2: Specific details to borrow from secondary styles [How to use returned styles]
- 10: Usual default limit for refero_get_similar_screens [refero_get_similar_screens]
- 20: Usual maximum limit for refero_get_similar_screens [refero_get_similar_screens]

<!-- /od:learn -->
