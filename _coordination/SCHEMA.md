# Shared research schema (every lane and every session follows this)

Goal: we are building a **design-system builder**, a tool that helps people create their own design system from building blocks. The aim is to make creating design systems, designs and visuals a beautiful, visual process for engineers and technical people, the way Figma makes it for designers. Good UX practice (UX laws, heuristics, device conventions) should be baked into what the builder generates. The research has to give the builder three things:
1. **Ontology**: every building block of a design system, from foundations and tokens to components, patterns, governance and docs.
2. **Questions**: every decision a designer makes, the options available, and what each option does visually.
3. **Causality**: what drives what. Which upstream choices change which downstream tokens and components, and how that makes the product look and feel.

## Files each lane writes
- `research/<LANE>-<slug>.md`: the findings, written as Decision Cards (template below) plus a short lane overview.
- `traces/<LANE>-trace.md`: an append-only log of **every** source you opened, including the ones you rejected. One row per source:
  `| time | S-id | URL | publisher | published/updated date | tier | verdict (used/rejected/why) | what was taken |`
- Never edit another lane's files. Put cross-lane notes in `_coordination/BOARD.md` under "Cross-lane notes".

## Source validation (applies before you learn from a source)
- **Tier A, primary**: the system's own official docs (m3.material.io, developer.apple.com/design, fluent2.microsoft.design, carbondesignsystem.com, polaris.shopify.com, atlassian.design, primer.style, spectrum.adobe.com, help.figma.com, developers.figma.com, W3C DTCG, W3C WCAG/WAI-ARIA APG, and similar). These can be used directly. Record the page's last-updated date when it shows one.
- **Tier B, recognized practitioner**: named experts or teams with a track record (EightShapes/Nathan Curtis, Brad Frost, Dan Mall, Jina Anne, NN/g, Smashing Magazine, Figma blog and Config talks, zeroheight/Sparkbox surveys, the design system teams' own engineering blogs). Use them, but corroborate any numeric or factual claim.
- **Tier C, community/secondary**: Medium, personal blogs, Reddit, X, YouTube. Use only as opinion, or when a Tier A or B source corroborates it. Label it as such.
- **Reject**: undated SEO listicles, AI content farms, pages that contradict the official docs, and anything stale on a fast-moving topic (Figma features, token specs, OS design languages) unless you are citing it as history.
- **Community pulse**: `sources/COMMUNITY-SIGNAL.md` is produced by the last30days validation lane (L00). Read it before finalizing, if it exists, and reconcile. Flag any source or claim the community currently disputes.
- Tag every claim `[S-xx]` (a source id from your trace) or `[inferred]`. Never present an inference as fact.
- Source ids are lane-prefixed so they cannot collide: `S-L01-001`, `S-L01-002`, and so on.

## Decision Card template
```
### DC-<LANE>-<nn>: <Decision name>
- **Block path:** e.g. Foundations > Color > Neutral ramp
- **Questions the designer answers:** 1-4 plain-language questions
- **Options:** each option, and which famous systems use it (with real values where public)
- **Visual effect:** what each option makes the product look/feel like
- **Depends on (upstream):** decisions that must come first or that constrain this one
- **Affects (downstream):** tokens, components and patterns that change when this changes
- **Token encoding:** DTCG $type, example token names across tiers (primitive > semantic > component)
- **Platform notes:** Web / iOS / Android / cross-platform differences
- **Accessibility constraints:** WCAG/APCA/HIG/Material rules that bound the options
- **Default + heuristic:** a sensible default and a rule of thumb for choosing
- **Evidence:** [S-ids]
```

## Quality bar
- Prefer real values (actual type scales, spacing steps, radii, durations, contrast ratios) taken from official docs over generic advice.
- Breadth first, then depth. Cover every sub-block in your lane before you polish any one of them.
- End your lane file with: `## Open questions / gaps`, and `## Confidence` (what is confirmed vs inferred).
