# The research behind OpenDesigner

Every default, formula and question in OpenDesigner traces back to a cited research base in this repo. This page is the map. It shows what each research lane covers, where the combined outputs live, and how to find an answer quickly.

Counts on this page were read from the files on 2026-09-24, with `python3 tools/jev_nav.py status` and `python3 tools/jev_nav.py check`. Run those commands for the current numbers.

## At a glance

| | Count | How it was counted |
|---|---|---|
| Research lanes finished | 18 | L00 to L18 on `_coordination/BOARD.md`; L12 is still open |
| Decision Cards | 352 | `### DC-` headings across `research/` and `benchmarks/` |
| Sources logged | 2,740 | distinct source ids in the research lanes' traces (`traces/L*-trace.md`), including sources that were opened and rejected. With the sponsorship research (R4) and the verification pass (V1), `traces/` holds 3,225 |
| Design systems benchmarked | 25 | files in `benchmarks/systems/` |
| Ontology nodes | 275, of which 211 are building blocks outside the builder layer: 156 generatable, 23 tool-assisted, 21 owner input, 9 designer-owned, 2 extractable | `synthesis/ontology.json` [S-V1b-091] |
| Questions in the interview | 193 | `synthesis/questionnaire.json` (27 screens plus a reference panel; 6 are planned and skipped for now) |
| Decision graph | 352 decisions, 470 edges, 12 cycles | `synthesis/decision-graph.json` |
| Claims re-checked (V1) | 161: 134 confirmed, 19 partly right, 5 wrong, 3 unverifiable | [`synthesis/VERIFICATION.md`](../synthesis/VERIFICATION.md) |

## How to read a claim

- `DC-L04-02` is a **Decision Card**: one decision and its options, with what each option looks like. It also records what the decision depends on and affects, how to encode it as tokens, platform notes, accessibility limits, a default, and evidence. The format is in [`_coordination/SCHEMA.md`](../_coordination/SCHEMA.md).
- `[S-L04-012]` is a **source id**. Look it up in `traces/L04-trace.md` for the URL, publisher, date, tier and what was taken from it.
- `[inferred]` means the lane concluded it rather than read it. Treat it as a default to test, not a finding.
- **Tiers:** A is primary: a system's own docs, source code, W3C specs. B is a recognized practitioner, such as NN/g or a design team's engineering blog. C is community opinion, used only with corroboration.

## The lanes

| Lane | Covers | File | Cards | Sources logged |
|---|---|---|---|---|
| L00 | Community pulse: what practitioners said in the last 30 days about design systems, tokens, Figma and OS design languages; the source registry | [`sources/COMMUNITY-SIGNAL.md`](../sources/COMMUNITY-SIGNAL.md), [`sources/SOURCE-REGISTRY.md`](../sources/SOURCE-REGISTRY.md) | - | 76 |
| L01 | Color: ramps, color spaces (OKLCH, HCT), semantic roles, WCAG 2.2 and APCA contrast, dark mode, dynamic color, data-viz color | [`research/L01-color.md`](../research/L01-color.md) | 27 | 76 |
| L02 | Typography: typefaces, type scales, line height, tracking, fluid type, platform fonts, variable fonts, scripts | [`research/L02-typography.md`](../research/L02-typography.md) | 28 | 66 |
| L03 | Space and layout: spacing scales, grids, breakpoints, containers, density, touch targets | [`research/L03-space-layout.md`](../research/L03-space-layout.md) | 26 | 87 |
| L04 | Shape, elevation, materials, borders, motion, sound, haptics | [`research/L04-shape-depth-motion.md`](../research/L04-shape-depth-motion.md) | 28 | 78 |
| L05 | Icons, imagery, illustration, data visualization | [`research/L05-icons-imagery-dataviz.md`](../research/L05-icons-imagery-dataviz.md) | 25 | 97 |
| L06 | Brand and voice: personality to visual attributes, brand-to-product translation, the lever matrix, 21 brand cases | [`research/L06-brand-voice.md`](../research/L06-brand-voice.md) | 24 | 124 |
| L07 | Tokens and Figma: token tiers, naming, the DTCG 2025.10 format, Figma variables and modes, Style Dictionary, Tokens Studio, multi-brand theming | [`research/L07-tokens-figma.md`](../research/L07-tokens-figma.md) | 28 | 148 |
| L08 | Components and patterns: a 64-component cross-system catalog, anatomy, states, WAI-ARIA behavior, 13 patterns | [`research/L08-components-patterns.md`](../research/L08-components-patterns.md), [`research/L08-component-catalog.md`](../research/L08-component-catalog.md) | 23 | 118 |
| L09 | Benchmark: 25 public design systems side by side with real values in 12 dimension tables | [`benchmarks/L09-benchmark-matrix.md`](../benchmarks/L09-benchmark-matrix.md), [`benchmarks/systems/`](../benchmarks/systems/) | 8 | 565 |
| L10 | Platforms: web, iOS, Android, Windows, cross-platform systems, native conventions, React Native, Flutter, SwiftUI and Compose token pipelines | [`research/L10-platforms.md`](../research/L10-platforms.md) | 25 | 94 |
| L11 | Process and governance: audits, principles, contribution, versioning, documentation, adoption, 24 competitors, a kickoff questionnaire | [`research/L11-process-governance.md`](../research/L11-process-governance.md) | 25 | 109 |
| L12 | Figma hands-on: inspecting real community design-system files through the Figma MCP server | not started | - | - |
| L13 | UX laws and heuristics: 30 laws, 44 heuristics, and which become design-system rules | [`research/L13-ux-laws-heuristics.md`](../research/L13-ux-laws-heuristics.md) | 18 | 112 |
| L14 | Device classes: phone, tablet, desktop, watch, TV, car, spatial, voice and AI; 14 invariants and a device matrix | [`research/L14-device-practices.md`](../research/L14-device-practices.md) | 14 | 90 |
| L15 | Visual design principles: hierarchy, Gestalt, color theory, polish, styles; what to automate, guide or expose | [`research/L15-visual-design-principles.md`](../research/L15-visual-design-principles.md) | 11 | 84 |
| L16 | Visual tooling for engineers and the design-to-code round trip: Figma MCP, Paper MCP, Penpot, theme playgrounds, 43 tools | [`research/L16-visual-tooling-for-engineers.md`](../research/L16-visual-tooling-for-engineers.md) | 15 | 324 |
| L17 | How design systems get made today, by hand and with AI; building-block classification (207 blocks on the 23 Sep map; `ontology.json` now has 211 and is canonical [S-V1b-091]) and 14 designer hooks | [`research/L17-how-systems-get-made.md`](../research/L17-how-systems-get-made.md) | 13 | 304 |
| L18 | AI-first distribution: Agent Skills, AGENTS.md, MCP, MCP Apps and visual UI in Claude, ChatGPT and Codex; the host capability matrix; the recommended repo architecture | [`research/L18-ai-first-distribution.md`](../research/L18-ai-first-distribution.md) | 14 | 228 |

"Sources logged" counts rows in each lane's trace file, including rejected sources. Every lane file ends with **Open questions / gaps** and **Confidence** sections: the fastest way to find useful research work (see [SEED-ISSUES.md](SEED-ISSUES.md)).

## The synthesis: where the lanes come together

| File | What it is |
|---|---|
| [`synthesis/ONTOLOGY.md`](../synthesis/ONTOLOGY.md) + `ontology.json` | Every building block of a design system in 10 layers (275 nodes), each mapped to the cards that decide it |
| [`synthesis/QUESTIONNAIRE.md`](../synthesis/QUESTIONNAIRE.md) + `questionnaire.json` | The guided interview: 27 screens and every question with its options, visual effect and downstream effect. It keeps the earlier Quick, Standard and Expert tags. `tools/build_data.py` sets the skill's four zoom levels from those tags and two short hand-picked lists (sketch and broad) |
| [`synthesis/LEVERS.md`](../synthesis/LEVERS.md) + `levers.json` | The eight dials, the formulas from dials and raw inputs to tokens, 13 famous systems as dial recipes, and the guardrails |
| [`synthesis/DECISION-GRAPH.md`](../synthesis/DECISION-GRAPH.md) + `decision-graph.json` | What drives what: dependency steps, cycles that must be decided together, and fan-out (which decisions shape the most) |
| `synthesis/cards.json` | Every Decision Card split into its fields, for tools and models |
| `synthesis/graph-overrides.json` | Hand corrections to the generated graph, kept explicit so they survive regeneration |

The product spec that turns all of this into the builder is `synthesis/OPENDESIGNER-SPEC.md`. A copy for readers is [SPEC.md](SPEC.md).

## Navigating with `tools/jev_nav.py`

```bash
python3 tools/jev_nav.py status                     # cards, sources and [inferred] tags per lane
python3 tools/jev_nav.py find "how many steps should a color ramp have"
python3 tools/jev_nav.py check                      # every cited source id is in a trace; every card id exists
python3 tools/jev_nav.py html                       # rebuilds navigator.html, a visual map of the research
python3 tools/jev_nav.py export                     # rebuilds synthesis/cards.json
python3 tools/jev_nav.py graph                      # rebuilds synthesis/decision-graph.json
```

`find` gathers candidate cards by keyword across all lanes. If `JEV_API_KEY` is set in your environment or a local git-ignored `.env`, it then asks TypeSafe's Jev model to rank them for your question. Without a key it falls back to keyword ranking, which needs no network.

Open [`navigator.html`](../navigator.html) in a browser for a clickable map of lanes and cards.

## What has been checked, and what has not

- **V1 (verification) is done.** Two fresh-context verifiers re-checked 161 claims against live official sources on 2026-09-24. 134 held, 19 were partly right, 5 were wrong and 3 could not be verified. Each fix, with its source id and status, is in [`synthesis/VERIFICATION.md`](../synthesis/VERIFICATION.md).
- **L09's own verifier pass** re-checked 32 benchmark claims: 28 held and 3 were fixed.
- **L12 (Figma hands-on)** has not started. Figma behavior in the research comes from Figma's docs, not from inspecting real files.
- **Many lanes hit search limits** and name the pages they could not read. Those gaps are listed at the end of each lane file and turned into issues in [SEED-ISSUES.md](SEED-ISSUES.md).
