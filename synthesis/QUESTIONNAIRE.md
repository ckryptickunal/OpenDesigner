# Guided decision flow: the builder's questionnaire (S1b)

This is the question flow at the core of the design-system builder. L11 found that no competitor walks a person through the decisions: tools generate a theme from a few inputs, host an existing system, or extract one [DC-L11-01; S-L11-071, S-L11-073]. This file lists every question the builder asks, in order, with the options, what each option does visually, and what it changes downstream.

`synthesis/questionnaire.json` holds the same content in machine-readable form. It is generated from this file by a small parser that reads the entry format below, so edit this file first and regenerate the JSON.

## How the flow is built

- **One stage = one builder screen.** Stages are ordered by the dependency step in `synthesis/decision-graph.json` (step 0 = nothing upstream). `tools/build_questionnaire.py` checks every edge in the graph, including S1c's `graph-overrides.json`: no question is asked before a question it depends on, within or across stages. Cards that describe the builder itself (L16, L17, L18) are listed under "Not asked" with how this flow applies them; the counts at build time are in `questionnaire.json` meta.
- **Cycles stay on one screen.** The graph has 12 cycles (decisions that constrain each other). Each cycle's cards sit on one screen, and the screen shows one shared live preview so the person sees the trade-off. The largest cycle is color: 21 cards, which is why Stage 08 is one screen with sections.
- **Cards without links were placed by their text.** Many component and pattern cards (L08, L13) have graph step 0 only because their "Depends on" text names lanes rather than card ids (for example DC-L08-07 depends on "radius scale, spacing/density, type scale"). They are placed after the foundations they name [inferred from each card's Depends-on field].
- **Look first, encoding later.** Token naming, file format and governance come after the visual stages. They change how the system is stored, not how it looks, and nothing visual depends on them in the graph.

## Depth modes

Every question is tagged with the lowest mode that asks it. A `Quick` question is also asked in Standard and Expert; a `Standard` question is also asked in Expert. `Any` marks the reference-intake panel, which is available on every screen in every mode and is never required.

People never pick a mode: the interview runs by zoom levels (`skills/opendesigner/references/zoom.md`). `tools/build_data.py` turns these tags into each question's level: a short hand-picked list is zoom 0 (sketch) or zoom 1 (broad), other Quick and Standard questions are zoom 2 (defined), and Expert questions are zoom 3 (detailed).

| Mode | Asks | Who it is for | What happens to the rest |
|---|---|---|---|
| **Quick** | 10 questions | "Give me a complete system in two minutes" | Every other question takes its default. Personality sliders pre-fill style answers through the lever matrix [DC-L06-02]. |
| **Standard** | Quick + Standard questions | An engineer setting up a real product system | Expert questions take defaults and stay editable later. |
| **Expert** | Everything | Design-system leads, multi-platform or multi-brand systems | Nothing is auto-decided; defaults are still pre-filled. |

**Quick mode, in order:** Q-aud-01 (who uses it), Q-brand-01 (personality sliders), Q-plat-01 (platforms), Q-tool-01 (where the system lives), Q-color-01 (brand color input), Q-color-02 (where brand color appears), Q-type-01 (typeface posture), Q-shape-01 (corner softness), Q-depth-01 (how surfaces separate), Q-motion-01 (motion feel).

Why these ten: they combine the highest fan-out step-0 decisions in the graph (personality DC-L06-02 fans out to 15 decisions, platforms DC-L10-01 to 12, source of truth DC-L16-02 to 9, in the graph as of this build) with the L09 divergence points that change the look most (shape, depth, surface color, density, typeface, color generation, motion) [L09 A2; DC-L09-01 to DC-L09-08]. Everything L09 found nearly every system shares is pre-filled instead of asked: a 3-tier token model, a 4px spacing base, neutral surfaces plus one accent plus status colors, 12-step ramps, 100-300 ms ease-out motion, light and dark modes, WCAG 2.2 AA [L09 A1 rows 1-12]. Platform posture (DC-L10-02, fan-out 11) is derived in Quick mode from the personality slider "Bold vs deferential" and shown as a confirm chip [inferred].

## How a model runs this interview

The builder's interface is an LLM (Claude, ChatGPT, Codex or another capable model) interviewing the person, visually where the host allows (artifacts, canvases, Figma or Paper through MCP) and in plain text otherwise [BRIEF requirements 6-7]. `questionnaire.json` carries the same steps under `interview_protocol`.

1. Start at zoom 0: the five sketch questions in `references/zoom.md`, then build. Nobody picks a mode. After each level, offer to stop or to zoom into one area, with its rough minutes from `pacing.json`. Offer the reference panel (Q-ref-01) up front and keep it open.
2. Walk the stages in order. Open each with one sentence on what the stage decides, then render its Preview if the host can show visuals; otherwise describe the Example in words.
3. Ask each question at or below the zoom level being worked whose "Show if" holds, using its **Ask** line. Skip questions whose **Status** is planned: the feature is not built yet, so ask nothing and record nothing. Spend time by **Time weight**: for `high`, explain why, show two or three options with their visual effect and a real system, recommend the default with its source, and state what it changes downstream before moving on; for `medium`, ask with the recommended default and the main alternatives; for `low`, state the default in one line and ask to confirm or change it.
4. For asset hooks, ask "do you have this?", accept the listed formats, and if the answer is no, offer the listed paths with their caveats. Never pretend a generated placeholder is a finished brand asset.
5. Record every answer as {question id, option value, how it was set: chosen, confirmed default, auto default, or from reference}. Questions above the level reached take their default and stay editable.
6. When an answer conflicts with an earlier one (the cycles named in stage headers), show the conflict and settle it with the ranked principles from Q-brand-07; do not average silently [L06 section 4.2].
7. After each stage, summarize the decisions in plain sentences a teammate could read, and append them to the decision log so a later session or another model can continue coherently [BRIEF requirements 9-11].
8. Only offer option values that appear in the question. If the person wants something else, record it as a custom value with their reason.
9. **Show, then ask, on the best surface available.** Pick the highest rung the host supports: an OpenDesigner MCP view, a host canvas or artifact, Figma or Paper through MCP, a local HTML file, the host's question tool, then plain text with hex values and numbered options; say which rung is in use and never block on a visual [DC-L18-06].
10. **One well-formed question per turn.** Show the recommended option and the 2-3 closest alternatives with one visual each, allow "other", and say in one line what the answer changes; put the remaining options behind "more". Ask one high-weight question per turn; group up to three low-weight ones [DC-L18-09, DC-L18-08]. On cycle screens (stage headers name them), a single form with all the linked questions is fine [DC-L18-09].
11. **Gates.** Pause for approval three times: after the scope stages (01-05, with the block map tagged by class), after direction (Stages 06-08), and after the asset checklist; end with a coverage check that lists every block as decided, defaulted, not applicable or pending. At zoom 0 and 1, keep only the direction gate [DC-L17-12, DC-L17-09].
12. **Owner-input blocks are never invented.** Questions tagged Block class I that the zoom level reached skips are recorded as "assumed" and listed for confirmation at the end, not silently decided [DC-L17-08, DC-L17-01].
13. **Write durable outputs to the person's repo:** DTCG tokens (canonical), DESIGN.md (readable view), a decision log in ADR style, a state file with every answer, status and coverage, and an AGENTS.md pointer, plus the exported lint rules [DC-L18-10, DC-L18-11].

**Block class** (auto-filled on every question from L17's scheme, DC-L17-01; the per-question mapping is [inferred]): `G` generatable from inputs and defaults, `E` best extracted from something that exists, `D` designer-owned (an asset hook), `T` tool-assisted with a named tool and caveat, `I` owner input that only the team can decide.

**Time weight rule** [inferred from `decision-graph.json`]: `high` when a decided card constrains 5 or more others (fan-out 5+) or the question is in Quick mode; `medium` when fan-out is 2-4, or the question is an asset hook, an input question, the reference panel, or an owner-input (I) question; `low` otherwise. Each question shows its weight and the fan-out it came from.

## How to read an entry

```
### Q-<area>-<nn> · <question in plain words> · <Quick|Standard|Expert|Any>
- **Status:** (optional) `planned` when the feature behind the question is not built yet; the interview skips it and records nothing
- **Why:** one line on why it matters
- **Ask:** the one short prompt the interviewing model uses
- **Example:** what the model shows, or asks the person for, while asking
- **Control:** single choice | multi-select | slider | color picker | number | text (plus modifiers)
- **Show if:** (optional) condition on earlier answers
- **Options:** one line each: `value` label: visual effect (real systems that use it)
- **Default:** the pre-filled answer; *Source:* L09 shared default, platform convention, accessibility rule, or card heuristic
- **Decides:** the Decision Cards this question settles
- **Changes:** downstream cards and ontology block names that move when the answer changes
- **Preview:** what the builder renders live, and what the person can do with it, while they decide
- **Dials:** (optional) which dials and engine inputs the answer moves, when that is not obvious from the options
- **Use / avoid:** (generatable blocks) where the chosen option belongs and where it does not, shown as a teaching note beside the control
- **Hook:** (asset hooks) accepted formats, and the paths offered when the answer is "no"
- **Pre-answers:** (reference intake) which later questions a reference can pre-fill
- **Skip:** whether it can be skipped and auto-defaulted
- **Block class:** G, E, D, T or I: how the value is obtained (L17's scheme, defined below)
- **Time weight:** high, medium or low: how long the model should spend (rule below)
- **Evidence:** card ids and source ids
- **Merges:** (optional) source questionnaire items folded into this question
```

Source questionnaire codes used in "Merges": `K` = L11 kickoff questionnaire Part H (for example K2.1), `B` = L06 section 8 brand questions (B1-B15), `P` = L10 platform questionnaire (P1-P26), `D` = L14 builder questionnaire extract (D1-D7). Claims carry a card id, a source id, or [inferred].

---

## Three kinds of question (from the product brief)

The product brief (`_coordination/BRIEF.md`) sets three rules this flow follows:

1. **Asset hooks for blocks the builder cannot generate well.** A logo, brand mark, custom icons, illustration, photography, a brand typeface and similar assets need a designer or a dedicated tool. For each, the builder asks "Do you have this?", names the formats it accepts, and offers honest paths when the answer is no. They are asked once as a grouped checklist in Stage 03 (Q-brand-08), then opened one by one at the stage where each asset is used. Hook questions carry a **Hook** line. In Quick mode no hook is asked; each hook's "if no" fallback is applied and the asset tray stays open so files can be dropped in later [DC-L17-04].
2. **Visual, teaching controls for generatable blocks.** Spacing, primitives, tokens and components are chosen on a live preview, and each such question carries a **Use / avoid** line that the builder shows beside the control, so the interface teaches where each option belongs.
3. **Reference intake at any point.** Q-ref-01 is a side panel on every screen. A reference can pre-fill later answers; the person confirms each one.

| Asset hook | Question | Stage |
|---|---|---|
| Grouped "do you have these?" checklist | Q-brand-08 | 03 |
| Logo, brand mark, favicon | Q-brand-03 | 03 |
| Fixed brand colors | Q-color-01 (locked hex input) | 08 |
| Brand typeface files and license | Q-type-02 | 10 |
| Custom icon set | Q-icon-01 | 17 |
| App icon | Q-icon-06 | 17 |
| Photography | Q-img-01 | 18 |
| Illustration, characters, mascot | Q-img-04 | 18 |
| Animated assets (Lottie, 3D, animated icons) | Q-img-06 | 18 |
| UI sounds or sonic logo | Q-motion-08 | 16 |
| Custom haptic patterns | Q-motion-09 | 16 |
| Patterns, textures, gradients (motifs) | Q-img-07 | 18 |
| Existing voice and tone guide | Q-voice-01 | 19 |

---

## Stage 00 · Reference intake (a side panel on every screen)
> Not a step in the sequence. The panel sits beside every stage; anything added here is read once and offered as pre-filled answers on the stages that follow, each marked "from reference" until the person confirms it.

### Q-ref-01 · Do you have a website, screenshot, Figma file or other example to learn from? · Any
- **Why:** A reference lets the builder suggest answers, so you don't start from a blank page. Tools do this now: Google Stitch reads a design system from a URL, and Polymet pulls tokens from one [S-L16-256, S-L16-405].
- **Ask:** "Is there a site, screenshot or Figma file whose structure or quality you like? I'll read it and suggest answers."
- **Example:** Ask for a URL of their own product or an app they admire; show the 'extracted from reference' card with 3-4 found values.
- **Control:** drop zone + URL field; multiple references allowed, each tagged "our product", "inspiration" or "competitor"
- **Options:**
  - `url` A live website URL: the builder reads computed colors, type, spacing, radius, shadows, motion and components [inferred; S-L16-405].
  - `screenshot` Screenshots or images: color, type size ratios, density, radius and depth are estimated from pixels; values are marked as estimates [inferred].
  - `figma` A Figma file or library: variables, styles and components are read through the Figma MCP (`get_variable_defs`, `get_design_context`, `get_screenshot`) [DC-L11-23; S-L11-041].
  - `code` Your code, a CSS file or a token JSON file: exact values, including DTCG files [DC-L07-08; S-L07-011].
  - `doc` A brand book, voice guide or PDF: brand colors, typefaces, voice traits [inferred].
- **Default:** none. *Source:* [inferred].
- **Decides:** none directly (input)
- **Changes:** pre-fills answers only; no card is decided without confirmation
- **Pre-answers:** Q-scope-02 (an existing product becomes the audit), Q-brand-01 and Q-brand-02 (reference placed on the personality map), Q-plat-01, Q-color-01 to Q-color-06, Q-color-09, Q-color-14, Q-type-01, Q-type-03, Q-type-06, Q-space-01, Q-space-02, Q-space-04, Q-layout-01, Q-shape-01, Q-shape-02, Q-depth-01, Q-depth-02, Q-motion-01, Q-motion-02, Q-icon-02, Q-icon-03, Q-comp-01, Q-state-01, Q-form-01 [inferred mapping from what each reference type exposes].
- **Preview:** an "extracted from reference" card listing each found value next to the question it would answer, with Accept, Adjust and Ignore buttons.
- **Use / avoid:** use a reference to copy structure and quality (spacing rhythm, type ratios, density, depth model); avoid copying another brand's identity: its logo, brand color, proprietary typeface or illustration are never carried over, and a "competitor" reference is used only to flag shared tropes [BRIEF requirement 4; S-L06-027].
- **Skip:** yes; always optional.
- **Block class:** E (extractable)
- **Time weight:** medium (fan-out 0)
- **Evidence:** S-L16-256, S-L16-405, S-L11-041, DC-L11-23, DC-L11-04
- **Merges:** K3.3 (reference products), B3 (competitors, as "competitor" references)

---

## Stage 01 · Scope and team
> Screen: what the system is for and who builds it. Graph step 0-2. Cycle kept together: DC-L11-02 + DC-L11-04 (scope decides what to audit; the audit reshapes scope).

### Q-scope-01 · Which products and pages should this system cover, and which should it leave out? · Standard
- **Why:** What the system covers sets how general your components must be. It also sets how many layers of design tokens you need [DC-L11-02].
- **Ask:** "Is this only for your app, or also your marketing site, docs, emails or in-house tools?"
- **Example:** Show two thumbnails, an app screen and a marketing page, drawn from the same tokens.
- **Control:** multi-select + text field for "not served"
- **Options:**
  - `product-app` Product app: tight, opinionated visuals are possible when this is the only surface [DC-L11-02, inferred].
  - `marketing` Marketing site: adds an expressive layer next to the productive one (Carbon splits productive and expressive type and motion) [DC-L06-01; S-L06-001].
  - `internal-tools` Internal or admin tools: usually dense (see Q-aud-01) [inferred].
  - `docs-content` Docs or content site: long-form reading pushes line length and paragraph rules (DC-L02-17) [inferred].
  - `email` Email: a constrained rendering target the token pipeline must also output [DC-L11-02 options].
  - `partner-embed` Inside partner sites or apps: need scoped, context-agnostic components ("card", not "product card") [S-L11-002].
- **Default:** product-app only. *Source:* card heuristic, scope v1 to what the pilot touches [DC-L11-02; S-L11-083].
- **Decides:** DC-L11-02
- **Changes:** DC-L11-03, DC-L11-07, DC-L11-14, DC-L11-16, DC-L11-25, DC-L06-01 · blocks: Strategy > Scope; Tokens > Architecture > Tiers; Components > Inventory
- **Preview:** a strip with one sample screen per selected surface, all rendered from the same draft tokens.
- **Skip:** yes, defaults to a single product app.
- **Block class:** I (owner input)
- **Time weight:** high (fan-out 8)
- **Evidence:** DC-L11-02; S-L11-083, S-L11-002, S-L11-030
- **Merges:** K2.1, K2.2 (surfaces part), B11 (marketing vs product, first half)

### Q-scope-06 · What kind of screens does this system mostly serve? · Standard
- **Why:** A sales page, a work tool, a help page and a showcase need different spacing, card use and big "hero" moments. Naming the kind of screen sets those rules [S-L17-007].
- **Ask:** "What are these screens mostly for: selling, getting work done, reading, or enjoying an experience?"
- **Example:** Show one piece of content four ways: a landing page, a dashboard, a docs page and a showcase.
- **Control:** single choice for the main surface, then one choice per surface named in Q-scope-01
- **Options:**
  - `persuade` Persuade (marketing and landing pages): roomy spacing, one big hero line, sections rather than card grids; display sizes reach further [S-L17-007; DC-L02-11].
  - `operate` Operate (app screens where people get work done): spacing follows Q-aud-01, no hero, cards only to group related data; 14px body text at middle density [S-L17-007; DC-L02-08].
  - `read` Read (docs, articles and help): comfortable spacing, 16px body text, no cards around running text [S-L17-007; DC-L02-08].
  - `experience` Experience (portfolios, showcases and games): roomy spacing, big imagery and hero moments; display sizes reach further [S-L17-007; DC-L02-11].
- **Default:** operate. *Source:* the engine's default product type (work-tool) is an Operate surface [inferred].
- **Dials:** none. Expression and Density stay one setting for the whole system. The main surface sets `raw.productType` (Operate work-tool, Read content, Persuade and Experience marketing), which moves body size; any Persuade or Experience surface sets `raw.marketingSurfaces`, which widens the display sizes. Each surface also gets its own density mode and hero rule in DESIGN.md and PRODUCT.md [inferred].
- **Decides:** none (an owner input; spec 11 settles the modes) [S-L17-007]
- **Changes:** DC-L02-08, DC-L02-11, DC-L03-10 · blocks: Strategy > Scope
- **Preview:** the same sample content as each chosen surface, side by side.
- **Use / avoid:** use one mode per surface; avoid treating a whole product as Persuade because it has one landing page [S-L17-007].
- **Skip:** yes, defaults to operate.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** S-L17-007; DC-L02-08, DC-L02-11, DC-L03-10

### Q-scope-02 · Is there existing UI to clean up and merge, or is this a new product? · Standard
- **Why:** Checking the screens you have (an audit) shows how much to merge. For example, 40 grays can merge into one 10-step color ramp [DC-L11-04, inferred].
- **Ask:** "Do you have screens already that we should clean up and merge, or are we starting fresh?"
- **Example:** If existing, ask for a URL or CSS file; show a count like '38 grays, 14 button styles found'.
- **Control:** single choice (+ URL or CSS import when existing)
- **Options:**
  - `greenfield` New product: skip the audit and go straight to visual language [S-L11-105].
  - `manual-inventory` Existing screens, sorted by hand: screenshots across 16 categories, then keep/merge/kill decisions (Brad Frost) [S-L11-001].
  - `automated-audit` Existing screens, counted by a tool: unique colors and declarations (CSS Stats), component and prop usage (Omlet, react-scanner), Figma library analytics [S-L11-105, S-L11-037, S-L11-039, S-L11-035].
  - `both` Both: automated counts plus the manual inventory for shared vocabulary [DC-L11-04 default].
- **Default:** greenfield; if existing UI, `both`. *Source:* card heuristic, the manual inventory's main value is shared vocabulary and buy-in [DC-L11-04; S-L11-001].
- **Decides:** DC-L11-04
- **Changes:** DC-L11-02, DC-L11-07; foundation ramps (L01-L04), component list (L08), naming (L07) · blocks: Process > Discovery > Audit
- **Preview:** an inventory board: counts of unique colors, type styles and button variants found, with the proposed consolidated ramp beside them.
- **Skip:** yes, defaults to greenfield.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L11-04; S-L11-001, S-L11-105, S-L11-035
- **Merges:** K1.5, K1.6

### Q-scope-03 · Who will use the system itself? · Expert
- **Why:** Each group that uses the system needs its own docs and file formats. AI coding agents need files a machine can read [DC-L11-02; S-L11-083].
- **Ask:** "Who will work with the system: engineers, designers, writers, partners, or AI tools that write code?"
- **Example:** Show the output list per audience, e.g. 'AI agents get DESIGN.md and an MCP manifest'.
- **Control:** multi-select
- **Options:**
  - `engineers` Engineers: component API docs and code packages (DC-L11-18).
  - `designers` Designers: a design-tool library (DC-L16-13).
  - `content-pm` Writers and people in product or marketing: usage and voice guidance (DC-L06-18).
  - `partners` External partners: public docs and stricter versioning (DC-L11-14).
  - `ai-agents` AI coding agents: MCP server, DESIGN.md, llms.txt (12 of 25 benchmarked systems ship one) [L09 A1 row 10; DC-L11-23].
- **Default:** engineers + designers + ai-agents. *Source:* L09 shared pattern row 10 (agent-readable exports in 12 of 25 systems) [inferred choice].
- **Decides:** DC-L11-02 (consumers part)
- **Changes:** DC-L11-18, DC-L11-23, DC-L16-12 · blocks: Docs > Component page; Distribution > Agent context
- **Preview:** a list of the output files the builder will generate for each checked audience.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** high (fan-out 8)
- **Evidence:** DC-L11-02, DC-L11-23; S-L11-083, S-L11-088
- **Merges:** K1.1, K9.1

### Q-scope-04 · How many people will build and look after the system, and how do they work together? · Expert
- **Why:** Team size sets how much the builder must do for you. Small teams should adapt an accessible base that exists, not build from scratch [DC-L11-01, DC-L11-10].
- **Ask:** "How many people will build and look after this, and are they one team or spread across product teams?"
- **Example:** Give the survey split: most teams are 1-5 people.
- **Control:** single choice (size) + single choice (model)
- **Options:**
  - `size-1-2` 1-2 people (28% of teams) [S-L11-030].
  - `size-3-5` 3-5 people (33%) [S-L11-030].
  - `size-6-10` 6-10 people (25%) [S-L11-030].
  - `size-10plus` 10+ people (8%) [S-L11-030].
  - `model-solitary` One team, for itself: one team makes it for itself and shares it (Curtis) [S-L11-005].
  - `model-centralized` One central team: a dedicated team serves product teams [S-L11-005].
  - `model-federated` Shared by several teams: designers from several product teams decide together [S-L11-005].
  - `model-hybrid` Central team plus helpers: central librarian team plus federated contributors (Salesforce) [S-L11-013].
- **Default:** 1-2 people, centralized with a named owner. *Source:* card heuristic [DC-L11-09; S-L11-030].
- **Decides:** DC-L11-09, DC-L11-10
- **Changes:** DC-L11-01, DC-L11-11, DC-L11-12 · blocks: Governance > Team model; Governance > Roles
- **Preview:** none visual; shows which governance defaults (contribution flow, review gates) the builder will switch on.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L11-09, DC-L11-10; S-L11-005, S-L11-013, S-L11-030, S-L11-006
- **Merges:** K9.2, K9.3, K13.2, K1.4


### Q-scope-05 · What are you starting from: a product you have, a UI kit, a site you like, or only a brief? · Standard
- **Why:** A kit makes your system look like the kit, and a reference passes on its rhythm. A brief gives the widest range of looks but needs the most choices. Using a system as is, adapting one or making your own sets the cost [DC-L17-02, DC-L11-01; S-L11-006].
- **Ask:** "Where do we start: your product, a UI kit, a site you admire, or a blank page and a brief?"
- **Example:** Show the same screen started from a stock kit, from a reference's structure with your identity, and from the brief alone.
- **Control:** single choice (entry) + single choice (build posture) + single choice (reference fidelity, shown for the reference path)
- **Options:**
  - `existing-product` From an existing product: audit and extract, then consolidate (the interface inventory; see Q-scope-02) [DC-L17-02; DC-L11-04].
  - `ui-kit` From a UI kit or library (Untitled UI, Material 3 kit, shadcn): fast, but the kit's defaults become the look unless changed (the M3 kit shipped 6 versions in 12 months) [DC-L17-02; S-L17-322].
  - `reference` From a reference you admire: carry structure and quality, never identity (gstack and Stitch support this) [DC-L17-02; S-L17-003].
  - `brief` From a brief only: interview, then generate directions [DC-L17-02; S-L17-021].
  - `adopt` / `adapt` / `create` Use as is, adapt, or build your own: adopt a system as-is (Material, Carbon, Fluent), adapt a themeable base (shadcn create, Radix Themes), or create your own; NN/g ranks their cost lowest to highest [DC-L11-01; S-L11-006, S-L11-071, S-L11-068].
  - `reinterpret` / `replicate-swap` / `flag-only` How close to stay to the reference: reinterpret the lessons (default), replicate structure with every identity element swapped (only for "our version of this"), or read a competitor only to list shared tropes; copying identity is never offered [DC-L17-03; S-L17-023, S-L17-022].
- **Default:** existing product: audit first; otherwise brief first with an optional reference, a kit only as a component base (Q-comp-01), not as the visual direction; small teams adapt an accessible base; references reinterpreted. *Source:* card heuristics [DC-L17-02, DC-L11-01, DC-L17-03; S-L11-030].
- **Decides:** DC-L17-02, DC-L11-01, DC-L17-03
- **Changes:** DC-L11-20, DC-L08-03 · blocks: Context > Starting point > Entry path; Strategy > Starting point; Builder > Input > Reference intake
- **Preview:** the three starting points side by side on one screen, with "carried from reference" and "swapped" labels on each element.
- **Use / avoid:** use a kit for components and a reference for structure; avoid letting either become the brand ("websites made with shadcn/ui famously look the same") [DC-L11-01; S-L11-073].
- **Skip:** yes, brief first.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L17-02, DC-L11-01, DC-L17-03; S-L11-006, S-L11-071, S-L11-073, S-L17-003, S-L17-023
- **Merges:** K0.5, K2.6 (starting library)
---

## Stage 02 · Audience and commitments
> Screen: who the product is for and what it promises them. Graph step 0. These answers bound every later option.

### Q-aud-01 · Who uses the product, and how often? · Quick
- **Why:** Who uses it sets density (how packed the screen is) and base text size. Across systems, body text runs 13-19px. Our L09 study puts this fourth on its list of ways systems look most different (an inferred ranking) [DC-L09-04; L09 A2 row 4].
- **Ask:** "Who uses it, and how often: all day for work, often, or now and then on the go?"
- **Example:** Show one table-and-form screen at dense, regular and large densities side by side.
- **Control:** single choice
- **Options:**
  - `dense` All day, in tools full of data: body 13-14px, controls 28-32px; compact and utilitarian (Polaris 13px, SLDS 13px, Carbon, Atlassian, Primer, Ant 14px) [DC-L09-04; S-L09-403].
  - `regular` Often, in an everyday app: body 16px, controls 36-40px (Radix, shadcn, Mantine, Chakra) [DC-L09-04; L09 A3 density].
  - `large` Now and then, on a phone or in public: body 17px or more, controls and targets 44-48px (iOS 17pt, GOV.UK 19px, Material, USWDS 48px targets) [DC-L09-04; S-L09-540].
- **Default:** regular. *Source:* L09 shared default row 8 (body 16px general, 14px tools) [L09 A1].
- **Decides:** DC-L09-04
- **Changes:** DC-L15-04, DC-L08-13, DC-L02-08, DC-L03-07, DC-L03-10, DC-L15-09 · blocks: Foundations > Typography + Space > Density preset
- **Preview:** the same table-plus-form screen at the three densities side by side; hovering a row shows its height, padding and text size.
- **Use / avoid:** use dense for tables, dashboards and editors people work in all day; avoid dense on touch-first, occasional or public surfaces, where it hurts legibility and forces the targets out of step with the visuals [DC-L09-04, DC-L15-04].
- **Skip:** yes, defaults to regular. Target sizes do not shrink with density; they follow input precision (Q-space-03, DC-L14-03).
- **Block class:** I (owner input)
- **Time weight:** high (fan-out 0)
- **Evidence:** DC-L09-04, DC-L15-04; S-L09-403, S-L09-540
- **Merges:** B1 (audience half), K1.1 (users of the product, not of the system)

### Q-aud-02 · What is at stake for users, and what state are they usually in? · Standard
- **Why:** What's at stake caps how lively the product can be. Google found expressive design may not suit banking [S-L06-010]. How users feel sets the tone [DC-L06-19; S-L06-060].
- **Ask:** "What's at stake for your users, and how do they usually feel when they use it?"
- **Example:** Contrast a banking transfer screen with a game reward screen.
- **Control:** single choice (category) + multi-select (states)
- **Options:**
  - `high-trust` Money, health or government: caps expressiveness and playful motion; calm, formal defaults [S-L06-010, S-L06-041].
  - `work` Work or business tools: productive defaults (Carbon, Atlassian, Primer quadrant) [L09 A3].
  - `consumer` Apps for everyday life: room for brand color and hero moments [DC-L06-03].
  - `play` Games, fun or learning: characters and springs are acceptable (Duolingo, Mailchimp) [S-L06-026, S-L06-027].
  - `state-*` How they feel (pick any): anxious, rushed, curious, celebrating; each shifts the tone matrix (Atlassian tones by emotion) [S-L06-060, S-L06-014].
- **Default:** work, states "rushed". *Source:* [inferred]; matches the L09 productive quadrant most benchmarked systems occupy [L09 A3].
- **Decides:** none directly (input)
- **Changes:** DC-L06-03, DC-L06-19, DC-L13-17 (default positions of their sliders)
- **Preview:** a pre-filled position on the personality sliders of Stage 03, with a note where the category caps them.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L06-03, DC-L06-19; S-L06-010, S-L06-060, S-L06-014
- **Merges:** B1 (emotional state), B2

### Q-aud-03 · Which set of accessibility rules do you need to meet? · Standard
- **Why:** The level you pick sets limits on color, text size, focus rings and target sizes in each later stage [DC-L11-19].
- **Ask:** "How strict do your accessibility rules need to be? WCAG 2.2 has levels A, AA and AAA."
- **Example:** Show a text pair that passes 4.5:1 and one that fails.
- **Control:** single choice
- **Options:**
  - `wcag22-aa` WCAG 2.2 AA: 4.5:1 text, 3:1 large text and UI parts, 24px target floor (GOV.UK commits to 2.2 AA) [S-L11-093; L09 A1 row 11; DC-L03-12].
  - `wcag22-aa-plus` AA plus some AAA rules, like 7:1 body text or bigger targets: stricter palettes, fewer mid-tone text colors [DC-L01-22, inferred].
  - `wcag22-a` Level A only: not recommended; no benchmarked system states a target below AA [L09 A1 row 11].
- **Default:** WCAG 2.2 AA. *Source:* accessibility rule; all 11 benchmarked systems that state a target use AA; WCAG 3 is still a draft, so 2.2 is the enforceable target [L09 A1 row 11; BOARD L01 note].
- **Decides:** DC-L11-19
- **Changes:** DC-L01-22, DC-L03-12, DC-L04-09, DC-L14-03, DC-L02-08 · blocks: Foundations > Accessibility > Program
- **Preview:** a guardrail strip listing which later options will be blocked or flagged at this level.
- **Skip:** yes, AA. The builder also generates the system-vs-product-team responsibility statement GOV.UK publishes [S-L11-092].
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 1)
- **Evidence:** DC-L11-19; S-L11-093, S-L11-092, S-L11-094, S-L11-030
- **Merges:** K4.1, K4.2, B15 (WCAG level)

### Q-aud-04 · Which settings should users be able to adjust, and which situations must you design for? · Standard
- **Why:** These choices turn on extra modes and larger targets. This follows the inclusive design rule "solve for one, extend to many" [DC-L13-14; S-L13-072].
- **Ask:** "Which settings should people be able to change: text size, roomy or compact layout, contrast, or less motion?"
- **Example:** Show the preview with a mode switcher gaining one toggle per setting.
- **Control:** multi-select (settings) + multi-select (situations)
- **Options:**
  - `text-size` Text size: layouts must reflow at large sizes (DC-L02-21).
  - `density` Compact or roomy switch: adds a compact/comfortable token mode (DC-L03-11).
  - `contrast` Contrast themes: adds a high-contrast mode (DC-L01-20).
  - `reduced-motion` Reduced motion: swaps movement for fades (DC-L04-25).
  - `situational` Tough conditions (one hand busy, bright light, older users): larger targets and higher contrast by default; reads calmer and more legible [DC-L13-14; S-L13-076, S-L13-038].
- **Default:** text-size + reduced-motion. *Source:* accessibility rule (WCAG 2.2 AA as the floor; text resize and motion preferences are OS settings the system should honor) [DC-L13-14, DC-L10-16].
- **Decides:** DC-L13-14
- **Changes:** DC-L07-15, DC-L11-25, DC-L01-20, DC-L04-25, DC-L02-21, DC-L03-11 · blocks: Principles > Inclusion; Tokens > Theming > Modes
- **Preview:** a mode switcher on the preview screen that gains one toggle per checked setting.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 1)
- **Evidence:** DC-L13-14; S-L13-072, S-L13-076, S-L13-098
- **Merges:** K4.4, B15 (user settings part)

---

## Stage 03 · Brand personality and principles
> Screen: who the brand is, and which brand assets already exist. Graph step 0-1. Personality has the largest fan-out in the graph (15 decisions), so it comes before any foundation [DC-L06-02]. The grouped asset checklist (Q-brand-08) sits here, as L17 recommends, so missing assets can be commissioned while the rest of the flow continues [DC-L17-04].

### Q-brand-01 · Where does your brand sit on these scales? · Quick
- **Why:** The sliders set starting values for color strength, corner radius and type. They also set font weight, motion, illustration and voice, through the L06 lever matrix [DC-L06-02].
- **Ask:** "Where does your brand sit on each scale? Drag each slider toward the end that sounds like you."
- **Example:** Show 2-3 style tiles updating live; ask for traits in 'X, but not Y' form, e.g. 'Fun, but not childish'.
- **Control:** slider x7 (0-100, 50 = system default) + optional text "X, but not Y" traits. Quick shows rows A, B, C, D, G; Standard and Expert add E and F.
- **Options:**
  - `A playful-serious` Playful: saturated brand color on chrome, large radii and pills, springs with overshoot, characters. Serious: neutral or monochrome scheme, small radii, ease-out without bounce, pictograms (M3 Expressive vs Carbon) [S-L06-011, S-L06-083, S-L06-009, S-L06-002].
  - `B friendly-authoritative` Friendly: warm neutrals, softer borders, rounded corners, sentence case, contractions. Authoritative: cool greys and deep blues or black, tighter radii, strong rules (Linear 2026 warm gray, Airbnb 2025 curves vs Uber black, IBM grid) [S-L06-067, S-L06-062, S-L06-023, S-L06-003].
  - `C minimal-rich` Minimal: near-monochrome with one accent, whitespace instead of containers, fewer outlined icons, no hero moments (Notion, Linear). Rich: primary/secondary/tertiary mixing, visible containers, filled or colored icons, 1-2 hero moments (M3 Expressive) [S-L06-092, S-L06-012, S-L06-009].
  - `D calm-energetic` Calm: shorter, subtle motion (Carbon standard curve), lighter weights, low saturation. Energetic: Carbon expressive curve or springs, heavy weights, high saturation [S-L06-002, S-L06-031, S-L06-083, S-L06-072].
  - `E premium-everyday` Premium: taller, more elegant type, restrained palette, subtle materials. Everyday: sturdy type with tall x-height, bright primaries, flat fills (Google Sans Flex study; Airbnb Cereal) [S-L06-031, S-L06-021, S-L06-100].
  - `F modern-heritage` Modern: geometric or grotesque sans, variable fonts, perceptual generated ramps, a mono companion. Heritage: serif or slab, fixed hand-picked palette (Cooper for Mailchimp) [S-L06-031, S-L06-019, S-L06-028].
  - `G bold-deferential` Bold: brand color on large surfaces, custom components and typeface everywhere. Deferential: accent only on primary actions and status, native type and components (Apple HIG; Fluent reuses native patterns 80% of the time) [S-L06-008, S-L06-098, S-L06-043].
- **Default:** 50 on every slider. *Source:* L06 lever matrix convention (50 = system default) [DC-L06-02]. Q-aud-02 pre-positions A, B and D.
- **Decides:** DC-L06-02
- **Changes:** DC-L06-03, DC-L06-14, DC-L06-18, DC-L06-01, DC-L15-01, DC-L06-04, DC-L06-09, DC-L06-10, DC-L01-10, DC-L01-06, DC-L04-02, DC-L02-02 · blocks: Foundations > Brand > Personality (feeds every foundation)
- **Preview:** 2-3 generated style tiles (type, color, radius, a button, a card) that update as sliders move; slider conflicts (for example "playful" wants large radii, "authoritative" wants small) are shown, not silently averaged [S-L06-078; L06 section 4.2].
- **Skip:** yes; all sliders at 50 give the neutral-toolkit look that L09 warns every generated app starts from [L09 A3].
- **Block class:** I (owner input)
- **Time weight:** high (fan-out 15)
- **Evidence:** DC-L06-02; S-L06-070, S-L06-071, S-L06-078, S-L06-011, S-L06-013
- **Merges:** B5, B6, K3.3 (feel)

### Q-brand-02 · Which products should yours feel like, and what one thing should people recognize it by? · Standard
- **Why:** Naming products you like agrees on taste fast, in a 20-second gut test. The "cover the logo" test then shows the one signature thing worth investing in [S-L11-001, S-L06-004].
- **Ask:** "Which products should yours feel like, and what one thing should people recognize it by?"
- **Example:** Ask for 1-5 product names or URLs; place them on the personality map.
- **Control:** text (up to 5 reference products or URLs) + single choice (signature lever)
- **Options:**
  - `sig-typeface` A signature font (Uber Move, Spotify Mix, IBM Plex) [L09 A3; S-L06-019].
  - `sig-color` One hero color (brand-led systems show their style through one color) [L09 A3].
  - `sig-device` A shape or graphic mark (Slack shapes, M3 shape library) [S-L06-030, S-L06-009].
  - `sig-character` A character or drawing style (Mailchimp Freddie, Duolingo Duo) [S-L06-027, S-L06-026].
  - `competitors` Your competitors (type their names): the builder flags tropes they share so you can avoid them (Collins positioned Mailchimp to "break from SaaS visual tropes") [S-L06-027].
- **Default:** sig-color. *Source:* L09 personality map, brand-led systems keep chrome restrained and spend personality on typeface, one color and imagery [L09 A3, inferred ranking].
- **Decides:** none directly (input)
- **Changes:** DC-L06-02 slider pre-positions, DC-L06-11, DC-L06-07, DC-L06-12
- **Preview:** reference thumbnails placed on the L09 personality map (productive to expressive, neutral to brand-led) with the person's current position.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L06-02, DC-L06-11; S-L06-004, S-L06-027, S-L11-001
- **Merges:** B3, B4, K3.3 (reference products)

### Q-brand-08 · Which of these assets do you already have? · Standard
- **Why:** Asking once for everything a designer must make shows the gaps early. Each "yes" opens its asset hook, and each "no" gets a fallback and a placeholder with a written brief [DC-L17-04; BRIEF requirement 2].
- **Ask:** "Which of these do you already have? Tick all that apply."
- **Example:** Show the asset shelf with empty, briefed slots; a dropped logo SVG fills its slot and proposes brand-color candidates from its fills.
- **Control:** multi-select checklist + drop zone
- **Options:**
  - `logo` Logo and brand mark: opens Q-brand-03 [DC-L05-13].
  - `brand-colors` Exact brand colors: opens the locked-hex input in Q-color-01 [DC-L01-09].
  - `typeface` Brand font files and license: opens Q-type-02 [DC-L02-06].
  - `icons` Icon set: opens Q-icon-01 [DC-L05-01].
  - `app-icon` App icon: opens Q-icon-06 [DC-L05-12].
  - `photography` Photos or a photo brief: opens Q-img-01 [DC-L05-14].
  - `illustration` Illustrations or a mascot: opens Q-img-04 [DC-L06-12].
  - `motion-assets` Animations, Lottie or 3D: opens Q-img-06 [DC-L05-21].
  - `motifs` Patterns, textures, gradients or a signature shape: opens Q-img-07 and Q-shape-05 [DC-L06-11, DC-L06-09].
  - `sounds` UI sounds or a sonic logo: opens Q-motion-08 [DC-L04-27].
  - `voice-guide` Voice and tone guide or word list: opens Q-voice-01 [DC-L06-18].
  - `brand-book` Brand book PDF: read through Q-ref-01; colors, font names and embedded logos are extracted [S-L17-569, S-L17-570, S-L17-571].
- **Default:** nothing ticked; every hook's fallback applies and its slot stays open with a written brief. *Source:* card heuristic, fallback order: have it, commission a designer with the generated brief, an open library with a compatible license, a named tool with its caveat, omit [DC-L17-04].
- **Decides:** none directly (asset inventory)
- **Changes:** pre-answers the hooks listed; records an asset decision per hook (have, commissioning, tool, open library, placeholder, not needed) [inferred from L17 Part I Stage 3]
- **Pre-answers:** Q-brand-03, Q-color-01, Q-type-02, Q-icon-01, Q-icon-06, Q-img-01, Q-img-04, Q-img-06, Q-img-07, Q-shape-05, Q-motion-08, Q-voice-01
- **Hook:** Accepts any of the formats listed on the individual hooks; each asset gets a license ledger entry (source, license, attribution, allowed slots, owner), and assets are fetched per project rather than pooled into a shared catalog, because several open licenses forbid redistribution as a library [S-L17-512, S-L17-517, S-L17-519, S-L17-522]. If no: every slot keeps a briefed placeholder; a generated stand-in is never presented as final [S-L17-004, S-L17-021].
- **Preview:** the asset shelf, one slot per hook, with status chips.
- **Use / avoid:** use this checklist once, early, so the designer hand-off can start in parallel; avoid generating identity assets silently [DC-L17-04].
- **Skip:** yes; Quick mode applies all fallbacks.
- **Block class:** D (designer-owned)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L17-04; S-L17-004, S-L17-021, S-L17-512, S-L17-569
- **Merges:** B7 (asset inventory)

### Q-brand-03 · Do you have a logo and brand mark? · Standard
- **Why:** Your logo shows up in the logo component, the favicons and app icons. The builder cannot make a good logo itself [DC-L05-13; BRIEF requirement 2].
- **Ask:** "Do you have a logo or brand mark? If so, share the SVG."
- **Example:** Show the logo in an app bar at 24-32px and as a favicon; if none, show the placeholder wordmark.
- **Control:** single choice + file upload
- **Options:**
  - `yes-full` Yes, a symbol plus the name: the builder makes a Logo component with Icon and Lockup variants (Atlassian sizes 16-48px, appearances brand, neutral, inverse) [S-L05-044].
  - `yes-wordmark` Only the name as a logo (wordmark): used on sign-in and marketing; the nav uses the name set in the brand typeface [DC-L05-13, inferred].
  - `no` Not yet: see the Hook line.
- **Default:** no, with a text wordmark placeholder. *Source:* [inferred].
- **Decides:** none directly (asset input for DC-L05-13)
- **Changes:** DC-L05-13, DC-L05-12 (app icon), DC-L04-27 (a sonic logo is a separate hook, Q-motion-08) · blocks: Brand in product > Logo usage; Brand in product > Favicon
- **Hook:** Accepts SVG (preferred, one master for the favicon set), PDF or EPS vector, or PNG at 512px or larger; light, dark and monochrome versions if they exist. The builder then derives `favicon.ico` 32px, `icon.svg` with a dark-scheme style, `apple-touch-icon.png` 180px, manifest PNGs 192 and 512 plus a maskable 512 [S-L05-042, S-L05-040, S-L05-041]. If no: (1) commission a designer with the generated brief and a reminder that a contractor's logo needs a written copyright assignment, the recommended path for anything customers will recognize; (2) a wordmark set in the chosen typeface (OFL, Google Fonts, Adobe Fonts and ITF FFL allow fonts in logos), generated and labeled "placeholder"; (3) AI logo generators (Looka, Brandmark) with caveats: Looka's icons and fonts come from a shared database available to others, and a trademark search is needed before adoption [S-L17-534, S-L17-535, S-L17-564, S-L17-579].
- **Preview:** the logo placed in an app bar at 24-32px, on a sign-in screen as a lockup, and as a browser-tab favicon, in light and dark.
- **Use / avoid:** use the symbol-only mark at 24-32px in dense app chrome and the full lockup on sign-in and marketing; avoid recoloring fixed-color product marks (Fluent never recolors launch icons) and avoid relying on inherited color [S-L05-044, S-L05-014].
- **Skip:** yes; the placeholder wordmark is applied.
- **Block class:** D (designer-owned)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L05-13; S-L05-014, S-L05-040, S-L05-042, S-L05-044
- **Merges:** B7 (logo), K3.1 (brand guidelines, logo part)

### Q-brand-04 · How expressive should the product be? · Standard
- **Why:** In Google's tests, expressive design made products seem 34% more modern and key parts up to 4x faster to spot. Too much of it hurts ease of use, and a strong minority prefers calm [DC-L06-03; S-L06-010].
- **Ask:** "How lively should it feel: calm and steady, calm with one or two big moments, or lively all through?"
- **Example:** Show one success moment animated three ways.
- **Control:** single choice
- **Options:**
  - `productive` Calm and steady only: calm, dense, efficient (Carbon product UI, Linear 2026 "calmer interface") [S-L06-002, S-L06-067].
  - `hero-moments` Calm, plus 1-2 big moments: expressive motion and type only at significant moments such as opening a page or the primary action (Carbon expressive motion; Material's own budget) [S-L06-002, S-L06-009].
  - `expressive` Lively throughout: varied shapes, rich color, emphasized type, fluid motion (M3 Expressive's seven tactics) [S-L06-009].
- **Default:** hero-moments. *Source:* card heuristic, Material's "one or two hero moments" rule [DC-L06-03; S-L06-009]. Capped at productive when Q-aud-02 = high-trust [S-L06-010].
- **Decides:** DC-L06-03
- **Changes:** DC-L06-04, DC-L06-10, DC-L06-11, DC-L15-01, DC-L15-03 · blocks: Foundations > Brand > Expression intensity
- **Preview:** one screen shown in all three settings, with the hero moment (for example a success state) animated.
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L06-03; S-L06-002, S-L06-009, S-L06-010, S-L06-067

### Q-brand-05 · How do marketing pages relate to the product? · Standard
- **Show if:** Q-scope-01 includes `marketing`
- **Why:** How you layer brand and product sets whether your marketing site and app look alike or drift apart [DC-L06-01; S-L06-110].
- **Ask:** "How should the marketing site relate to the product: one system with two moods, or separate?"
- **Example:** Show a marketing hero next to a product table under each option.
- **Control:** single choice
- **Options:**
  - `one-system-two-sets` One system, with a calm set and a lively set: same type family and color logic, app denser (Carbon type sets -01/-02) [S-L06-001, S-L06-002].
  - `brand-above` Brand rules on top, the product system below, and marketing beside it: more marketing freedom, more drift risk (IBM Brand Center / Carbon / Carbon for IBM.com) [S-L06-003].
  - `family` A family of systems on one shared base: platforms differ in components, tokens keep one brand (Spotify Encore, Netflix Hawkins) [S-L06-085, S-L06-087].
  - `single` One product system. The brand is only in the logo and color (most startups) [inferred].
- **Default:** one-system-two-sets. *Source:* card heuristic [DC-L06-01].
- **Decides:** DC-L06-01
- **Changes:** DC-L06-16, DC-L02-11 · blocks: Foundations > Brand > Layer architecture
- **Preview:** a marketing hero and a product table side by side, rendered from the chosen layering.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 1)
- **Evidence:** DC-L06-01; S-L06-001, S-L06-003, S-L06-053, S-L06-085, S-L06-110
- **Merges:** B11 (second half)

### Q-brand-06 · Should marketing and article pages get their own, bolder set of text styles? · Expert
- **Why:** One product type scale keeps apps calm. A second, expressive set gives article pages big size jumps. Those "would be distracting if used in product" [DC-L02-11; S-L02-011].
- **Ask:** "Do marketing and article pages need their own set of bigger headings?"
- **Example:** Show a heading ladder, productive vs expressive.
- **Control:** single choice
- **Options:**
  - `two-sets` Two sets: productive base 14px with fixed headings, expressive base 16px with fluid headings (Carbon display from 42px to 156px across breakpoints) [S-L02-012, S-L02-011].
  - `emphasized` One scale plus heavier styles: 15 baseline + 15 heavier styles for actions and headlines (M3 Expressive) [S-L02-006].
  - `brand-face` One scale plus a brand font for brand moments (Atlassian Charlie Sans) [S-L02-015].
  - `productive-only` One product scale only (Polaris, Primer) [DC-L02-11].
- **Default:** one productive scale plus 3-4 expressive display styles; a full second set if more than a third of pages are marketing or editorial. *Source:* card heuristic [DC-L02-11].
- **Decides:** DC-L02-11
- **Changes:** DC-L02-03, DC-L02-09, DC-L02-15, DC-L02-19, DC-L15-02 · blocks: Foundations > Typography > Type sets
- **Preview:** a heading ladder at productive and expressive settings, across three breakpoints.
- **Use / avoid:** use fluid, expressive display styles on marketing and editorial pages; avoid them inside product containers (Carbon: "Do not use these styles inside a container") [S-L02-011].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L02-11; S-L02-006, S-L02-011, S-L02-012, S-L02-015, S-L02-041

### Q-brand-07 · What are your 3-5 design principles, and which one wins a tie? · Standard
- **Why:** When two sliders pull the same setting in opposite ways, your ranked principles break the tie [DC-L06-15; L06 section 4.2].
- **Ask:** "What 3-5 principles should break ties, and which one wins? I can draft some from your sliders."
- **Example:** Show GOV.UK-style imperatives and a do/don't pair per principle.
- **Control:** text list (3-5) + drag to rank + single choice (format)
- **Options:**
  - `checklist` Question checklists (IBM) [S-L06-004].
  - `pairs` Functional and emotional pairs (Fluent) [S-L06-043].
  - `imperatives` Commands that say what they give up (GOV.UK, 11 principles, updated 2 Apr 2025) [S-L06-044].
  - `value-words` Short value words (Carbon system principles) [S-L06-114].
  - `generate` Let the builder draft principles from the sliders, for you to edit [inferred].
- **Default:** generate, 3-5 principles, each naming what it outranks, with one making accessibility non-negotiable. *Source:* card heuristic [DC-L06-15; S-L06-077, S-L06-044].
- **Decides:** DC-L06-15, DC-L11-05
- **Changes:** tie-break rules for slider conflicts; ADRs (DC-L11-12) · blocks: Foundations > Principles; Governance > Principles
- **Preview:** each principle shown with a do/don't pair generated from the current draft.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L06-15, DC-L11-05; S-L06-044, S-L06-077, S-L11-008
- **Merges:** K3.2, B12, K1.2 (interview themes become principle inputs)

---

## Stage 04 · Platforms and devices
> Screen: where the product runs and what people touch it with. Graph step 0-2. Cycle kept together: DC-L10-01 + DC-L10-02 + DC-L10-03 + DC-L10-21 (platforms, posture, sharing layer and framework constrain each other). Placed after personality so the posture default can come from slider G [inferred; DC-L06-14 depends on DC-L06-02].

### Q-plat-01 · Which platforms ship in the first release? · Quick
- **Why:** Each platform brings habits your brand must live with. It also has its own units, smallest target sizes and export files [DC-L10-01].
- **Ask:** "Where will it run first: web, iOS, Android or desktop?"
- **Example:** Show one screen in browser, iOS and Android chrome.
- **Control:** multi-select
- **Options:**
  - `web` Web: one delivery layer (CSS custom properties); the brand can show in every pixel (Polaris calls Shopify's platform "the web platform") [S-L10-047].
  - `ios` iOS/iPadOS: Liquid Glass chrome, pt units, Dynamic Type; bars, controls and sheets are styled by the OS [S-L10-075, S-L10-011].
  - `android` Android: Material 3 conventions, dp/sp units, large-screen layouts mandatory at 600dp+ [S-L10-021, S-L10-071].
  - `desktop` Desktop app (macOS, Windows, or built with web tech) [DC-L10-24].
  - `secondary` Watch, TV, car or headset: see Q-plat-02 [DC-L10-24].
- **Default:** web. *Source:* survey, 94% of systems support web, 35% iOS, 34% Android [DC-L11-01; S-L11-030]. L10's own default for consumer products is web + iOS + Android phones with large-screen layouts [DC-L10-01] (see Disagreements).
- **Decides:** DC-L10-01
- **Changes:** DC-L10-02, DC-L10-08, DC-L10-09, DC-L10-10, DC-L10-11, DC-L10-15, DC-L10-17, DC-L10-19, DC-L10-20, DC-L10-22, DC-L10-24, DC-L14-01 · blocks: Platforms > Scope > Target platforms
- **Preview:** the same screen rendered in each platform's chrome (browser, iOS glass bars, Material top bar), side by side.
- **Skip:** yes, web.
- **Block class:** I (owner input)
- **Time weight:** high (fan-out 12)
- **Evidence:** DC-L10-01; S-L10-021, S-L10-046, S-L10-047, S-L10-075, S-L11-030
- **Merges:** P1, K2.2 (platform part)

### Q-plat-05 · Should your native apps look like the platform, like your brand, or a mix? · Standard
- **Show if:** Q-plat-01 includes ios, android or desktop. In Quick mode it is derived from slider G and shown as a confirm chip.
- **Why:** Apps that look like the platform feel at home and get OS updates for free. Brand-first apps look the same everywhere but must redo every OS change [DC-L10-02].
- **Ask:** "Should your iOS and Android apps look like the platform, like your brand, or a mix?"
- **Example:** Show one screen native-first, hybrid and brand-first.
- **Control:** single choice
- **Options:**
  - `native-first` Like the platform: system components almost everywhere; brand shows in content, accents, imagery and voice (Apple: "Express your brand with familiar components") [S-L10-009].
  - `hybrid` A mix of both: shared brand foundations and signature moments, native navigation and controls (Fluent reuses native patterns 80% of the time) [S-L10-038, S-L06-043].
  - `brand-first` Like your brand: identical custom UI on every platform (CRED NeoPOP); can feel foreign and must rebuild accessibility [S-L06-112, DC-L06-14].
- **Default:** hybrid. *Source:* card heuristic, share what users perceive as the brand, adopt the platform's version of "how the phone works" [DC-L10-02, DC-L06-14].
- **Decides:** DC-L10-02, DC-L06-14
- **Changes:** DC-L10-03, DC-L10-04, DC-L10-06, DC-L10-09, DC-L10-12, DC-L10-13, DC-L10-14, DC-L10-21, DC-L10-25, DC-L06-07, DC-L15-01 · blocks: Platforms > Strategy > Native vs brand posture
- **Preview:** one screen as native-first, hybrid and brand-first on iOS and Android.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** high (fan-out 11)
- **Evidence:** DC-L10-02, DC-L06-14; S-L10-009, S-L10-038, S-L10-075, S-L10-076, S-L06-043
- **Merges:** P3

### Q-plat-10 · How closely should things work the way people already expect? · Standard
- **Why:** Usual behavior feels trusted but plain. New behavior stands out but is harder to learn (Jakob's law). The default follows the look you chose in Q-plat-05 [DC-L13-17; graph-overrides.json edge DC-L10-02 to DC-L13-17].
- **Ask:** "Should it look and work the usual way, work the usual way with your own look, or try something new?"
- **Example:** Show a standard dropdown beside a custom one.
- **Control:** single choice
- **Options:**
  - `native` Like the platform: follow HIG, Material or Fluent behavior and look; instantly usable, generic [DC-L13-17].
  - `custom-skin` Usual behavior, your own look: brand visuals, standard interaction [DC-L13-17].
  - `novel-core` Something new only for what sets you apart, tested [DC-L13-17; S-L13-006].
- **Default:** custom-skin. *Source:* card heuristic; don't override standard shortcuts [DC-L13-17; S-L13-036, S-L13-030].
- **Decides:** DC-L13-17
- **Changes:** DC-L08-03, DC-L10-13 · blocks: Principles > Familiarity
- **Preview:** a standard dropdown and a custom one next to each other, both keyboard-operable.
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L13-17; S-L13-006, S-L13-030, S-L13-036, S-L13-055

### Q-plat-06 · In your iOS, Android or desktop apps, use built-in controls or your own? · Expert
- **Show if:** Q-plat-01 includes ios, android or desktop
- **Why:** System controls change with each OS update, like the rounder, capsule-like ones on iOS 26+. Custom controls keep your brand shape but must bring their own accessibility [DC-L10-13].
- **Ask:** "In your iOS, Android or desktop apps, keep the built-in controls or restyle them?"
- **Example:** Show switches and sliders: system vs custom.
- **Control:** single choice
- **Options:**
  - `system` System controls in your accent color: native feel, Liquid Glass and Material behavior for free [S-L10-075, S-L10-072].
  - `restyled` System controls, restyled for your brand: brand color and label, familiar size, placement and behavior (Apple permits this) [S-L10-009].
  - `custom` Fully custom controls: brand shapes such as square buttons; can look out of place next to system UI [DC-L10-13].
- **Default:** system on native, custom on web. *Source:* platform convention [DC-L10-13].
- **Decides:** DC-L10-13
- **Changes:** DC-L10-14, DC-L10-12 · blocks: Components > Controls > Platform rendering
- **Preview:** switch, slider and segmented control in each style on iOS.
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L10-13; S-L10-009, S-L10-014, S-L10-072, S-L10-075
- **Merges:** P14

### Q-plat-07 · What do the platforms share? · Expert
- **Show if:** more than one platform in Q-plat-01
- **Why:** The more you share, the more your product looks the same on every platform, and the less it feels native [DC-L10-03].
- **Ask:** "What should your platforms share: only ideas, colors and sizes, component plans, or code?"
- **Example:** Show one card component rendered per platform under each option.
- **Control:** single choice
- **Options:**
  - `principles` Principles only: loosest alignment (Fluent's four principles) [S-L10-038].
  - `tokens` Same tokens, own components on each platform: same palette and rhythm, platform-shaped components (Spotify Encore, Fluent) [S-L10-040, S-L10-039].
  - `specs` Same component plans, own code per platform: one spec for 7 stacks including screen-reader specs (Uber Base) [S-L10-046].
  - `code` Shared component code: identical components everywhere [DC-L10-03].
- **Default:** tokens + shared specs, per-platform implementation. *Source:* card heuristic [DC-L10-03].
- **Decides:** DC-L10-03
- **Changes:** DC-L10-19, DC-L10-21, DC-L10-22, DC-L10-24, DC-L14-02 · blocks: Platforms > Architecture > Sharing layer
- **Preview:** a diagram of which layers are shared, with the same card component rendered per platform.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L10-03; S-L10-039, S-L10-040, S-L10-046, S-L10-053
- **Merges:** P4

### Q-plat-08 · What will you build the UI with? · Standard
- **Why:** The tools you build with decide what code the builder writes and how fast new OS looks reach your users [DC-L10-21, DC-L10-20, DC-L10-19].
- **Ask:** "What will you build the UI with?"
- **Example:** Show a generated Button in each selected stack.
- **Control:** multi-select
- **Options:**
  - `react` React (72% of systems), `vue`, `angular` (28%), `svelte`: framework components [S-L11-030; DC-L10-19].
  - `web-components` Web components: framework-agnostic, CDN-delivered (Polaris moved in 2025; Salesforce LWC) [S-L10-047, S-L10-052].
  - `swiftui` SwiftUI/UIKit and `compose` Jetpack Compose: new platform visuals arrive here first ("Android is now Compose First") [S-L10-002, S-L10-075].
  - `react-native` React Native or `maui` .NET MAUI: native views, looks native by default [S-L10-063, S-L10-077].
  - `flutter` Flutter or `cmp` Compose Multiplatform: draws its own pixels, identical everywhere, lags OS design changes (Flutter's Liquid Glass still in progress) [S-L10-055, S-L10-059].
- **Default:** React for web; SwiftUI + Compose for native. *Source:* survey share and card heuristics (framework components when one framework dominates; target the toolkit where the platform owner ships first) [S-L11-030; DC-L10-19, DC-L10-20, DC-L10-21].
- **Decides:** DC-L10-21, DC-L10-20, DC-L10-19
- **Changes:** DC-L10-22, DC-L10-03, DC-L10-01, DC-L08-03 · blocks: Platforms > Implementation
- **Preview:** a code tab showing a generated Button in each selected stack.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L10-19, DC-L10-20, DC-L10-21; S-L10-047, S-L10-055, S-L10-063, S-L11-030
- **Merges:** K2.3, P20, P21, P22

### Q-plat-02 · Which devices must work great on day one, which only need to work, and which are out? · Standard
- **Why:** Each device you fully design for adds a visibly different layout shape. Devices you only adapt look stretched. Google now penalizes that on large screens [DC-L14-01; S-L14-069].
- **Ask:** "Which devices must work great on day one, which only need to work, and which are out?"
- **Example:** Show a device row: phone, tablet, laptop, TV, watch.
- **Control:** tier picker per class (first-class / works / out)
- **Options:**
  - `phone` Phone [DC-L14-01].
  - `tablet-foldable` Tablet and foldable: rails, sidebars, 2-3 panes; Android ignores orientation locks at 600dp+ [S-L10-020, S-L10-025].
  - `desktop-web` Desktop and web [DC-L14-01].
  - `watch` Watch: dark, glanceable, Crown lists; foundations only travel [S-L14-002, DC-L10-24].
  - `tv` TV: big type, focus rows, 66pt targets, overscan safe area [S-L10-012, S-L10-013].
  - `car` Car: system templates, large sparse high-contrast screens [S-L14-010, S-L14-032].
  - `spatial` Headset: glass windows at a distance, 60pt targets [S-L14-007, S-L10-012].
- **Default:** phone + tablet/foldable + desktop/web first-class; TV, watch, car and spatial out until a named use case exists. *Source:* card heuristic [DC-L14-01, DC-L10-24].
- **Decides:** DC-L14-01, DC-L10-24
- **Changes:** DC-L14-02, DC-L14-03, DC-L14-04, DC-L14-05, DC-L14-07, DC-L14-08, DC-L14-10, DC-L14-11, DC-L14-12, DC-L14-14 · blocks: Platforms > Scope > Device classes; token `context` modifier
- **Preview:** a device row (watch, phone, tablet, laptop, TV) showing the draft screen at each first-class size.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** high (fan-out 10)
- **Evidence:** DC-L14-01, DC-L10-24; S-L14-069, S-L14-001, S-L14-017, S-L10-024
- **Merges:** P2, P25, D1, D3

### Q-plat-03 · What do people touch or press with? · Standard
- **Why:** How precise people's input is sets target sizes. A control can look small, but the area that responds to a tap or click can't be [DC-L10-15].
- **Ask:** "What will people touch or press with: fingers, mouse, keyboard, remote, eyes and hands?"
- **Example:** Show one button with its hit area outlined for touch vs mouse.
- **Control:** multi-select
- **Options:**
  - `touch` Touch: 44x44pt iOS, 48x48dp Android; airier layouts, larger rows [S-L10-012, S-L10-072].
  - `pointer` Mouse or trackpad: macOS 28pt default (20 minimum); denser layouts with hover states [S-L10-012].
  - `keyboard` Keyboard: visible focus everywhere (DC-L08-11) [DC-L10-15].
  - `remote` A remote that moves focus: tvOS 66pt, focus highlights and expands items [S-L10-012, S-L10-015].
  - `spatial` Eyes and hands: visionOS 60pt, centers 60pt apart [S-L10-012, S-L10-013].
- **Default:** touch + pointer + keyboard; 44 CSS px targets on web even though AA requires 24, plus a pointer density mode for desktop. *Source:* platform convention [DC-L10-15; S-L10-036].
- **Decides:** DC-L10-15
- **Changes:** DC-L14-03, DC-L03-12, DC-L03-13, DC-L14-06 · blocks: Foundations > Interaction > Input modality and targets
- **Preview:** a button row with its hit area outlined for each input.
- **Use / avoid:** use the touch target size for anything a finger can reach, including web; use pointer-sized visuals only with a hit area padded to the floor; avoid drag-only interactions without a non-drag alternative (WCAG 2.5.7) [DC-L10-15; S-L10-083].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L10-15; S-L10-012, S-L10-036, S-L10-072, S-L10-073, S-L10-083
- **Merges:** P16, D2

### Q-plat-04 · Will anyone use the product while driving, moving, or wearing a headset? · Standard
- **Show if:** Q-plat-02 marks car, watch or spatial as first-class or works
- **Why:** In a car, rules against distraction become hard errors, not warnings [DC-L14-11].
- **Ask:** "Will anyone use this while driving, walking, or in a headset?"
- **Example:** Show which elements would fail the 2-second glance rule.
- **Control:** multi-select
- **Options:**
  - `driving` Driving: glances at most 2 s and 12 s per task (NHTSA), no animation or auto-scroll, 76dp targets, at most 120 characters per text item [S-L14-031, S-L14-032, S-L14-037].
  - `spatial` Headset: content in the field of view, at least 1 m for reading, no fast motion without a stationary reference [S-L14-007, S-L14-008].
  - `watch` On the wrist: tasks done within seconds [S-L14-015].
  - `none` None.
- **Default:** none. *Source:* [inferred]; only asked when a relevant device class is in scope.
- **Decides:** DC-L14-11
- **Changes:** validator rules; DC-L04-19 and DC-L14-08 (motion off in vehicles) · blocks: Governance > Linting > Context safety rules
- **Preview:** the draft screen with failing elements flagged under the chosen context.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L14-11; S-L14-031, S-L14-032, S-L14-037, S-L14-008
- **Merges:** D4

### Q-plat-09 · Which OS versions do you support? · Expert
- **Show if:** Q-plat-01 includes ios or android
- **Why:** If you support only the newest OS, you can count on glass bars, dynamic color and edge-to-edge screens. Supporting older versions too means two designs [DC-L10-23].
- **Ask:** "Which versions of iOS, Android and other systems must you support?"
- **Example:** Show a matrix of assumed features: glass, dynamic color, edge-to-edge.
- **Control:** single choice per platform
- **Options:**
  - `current-prev` The current and last major version: design for the current language, older versions fall back to their native look [DC-L10-23].
  - `apple-26` Apple 26+: Liquid Glass everywhere; apps built with the 27 SDKs cannot keep the old look [S-L10-005, S-L10-076].
  - `android-12` Android 12+: dynamic color available [S-L10-019]; 14+ nonlinear font scaling to 200% [S-L10-071]; 15+ edge-to-edge enforced [S-L10-023]; 16+ predictive back [S-L10-020].
  - `older` Older versions too: conservative, dual-design choices [DC-L10-23].
- **Default:** current-prev. *Source:* card heuristic, design for the OS users will have when you ship [DC-L10-23].
- **Decides:** DC-L10-23
- **Changes:** DC-L10-05, DC-L10-11, DC-L10-12, DC-L10-14 · blocks: Platforms > Scope > OS versions
- **Preview:** a matrix of which platform features (glass, dynamic color, edge-to-edge, predictive back) are assumed.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L10-23; S-L10-005, S-L10-019, S-L10-020, S-L10-023, S-L10-071, S-L10-076
- **Merges:** P24

---

## Stage 05 · Where the system lives
> Screen: design tool, source of truth and how engineers consume the output. Graph step 0-1. Asked before any foundation because it decides what the builder generates on every later preview [DC-L16-02]. The design-tool plan comes first because it limits where the source of truth can live (Figma REST writes need Enterprise) [DC-L07-27, DC-L07-08].

### Q-tool-03 · Which design tool does your team use, and on which plan? · Standard
- **Why:** Your Figma plan caps how many modes each collection can have. That caps which theme setups fit [DC-L07-27].
- **Ask:** "Do you use a design tool? If Figma, which plan?"
- **Example:** Show the mode-budget meter, e.g. '6 of 10 modes used'.
- **Control:** single choice (tool) + single choice (Figma plan)
- **Options:**
  - `figma-starter` Figma Starter: variables but no extra modes, no published libraries [S-L07-011, S-L07-020].
  - `figma-pro` Figma Professional: libraries, 10 modes per collection, no Code Connect or branching [S-L07-014].
  - `figma-org` Figma Organization: 20 modes, Code Connect, branching, analytics [S-L07-014, S-L07-025].
  - `figma-ent` Figma Enterprise: extended collections for multi-brand, REST variables API [S-L07-015, S-L07-034].
  - `paper` Paper (MCP read and write) [S-L16-102].
  - `penpot` Penpot (MCP and DTCG import) [S-L16-111].
  - `none` No design tool: the builder is the visual surface [inferred].
- **Default:** none; if Figma, the builder asks the plan first and greys out architectures it cannot hold (for example 4 brands x light/dark/high-contrast = 12 modes exceeds Professional's 10). *Source:* card heuristic [DC-L07-27; S-L07-014]. 
- **Decides:** DC-L07-27
- **Changes:** DC-L07-08, DC-L07-16, DC-L07-17, DC-L07-18, DC-L07-26, DC-L07-24 · blocks: Tooling > Figma plan
- **Preview:** a mode-budget meter (modes used vs the plan's limit) that later theming answers fill.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L07-27, DC-L16-13; S-L07-014, S-L07-015, S-L07-034, S-L16-002, S-L16-113
- **Merges:** K2.4

### Q-tool-01 · Where should the master copy of the system live? · Quick
- **Why:** Any copy that is not the master (the source of truth) drifts out of date unless it syncs on its own. 60% of teams have no token automation [DC-L07-08; S-L11-030].
- **Ask:** "Where should the master copy live: here, a token file in git, your code, or Figma?"
- **Example:** Show a round-trip diagram for the chosen option.
- **Control:** single choice
- **Options:**
  - `builder` In the builder. It makes DTCG, CSS, native code and design files at once, and sends to design tools [DC-L16-02, DC-L11-16].
  - `token-file` Git token file (DTCG plus Resolver). It feeds code and Figma (Tokens Studio, Penpot write DTCG) [DC-L07-08; S-L07-002, S-L16-113].
  - `code` Code: tokens and components in code, design tools mirror it; the 2026 practitioner majority ("code is the source of truth") [DC-L11-16; COMMUNITY-SIGNAL].
  - `design-file` In Figma, as variables: designers own tokens; fits a single web platform [DC-L07-08; S-L07-011].
- **Default:** builder; design tools are mirrors: write to Figma through its remote MCP when a Full seat exists, otherwise emit one DTCG file per mode Figma imports natively; write to Paper through its MCP. *Source:* card heuristics of L16 and L11 [DC-L16-02, DC-L11-16, DC-L16-13]; L07 prefers token-file (see Disagreements).
- **Decides:** DC-L16-02, DC-L07-08, DC-L11-16, DC-L16-13
- **Changes:** DC-L07-25, DC-L07-09, DC-L16-12, DC-L11-14 · blocks: Builder > Data > Source of truth; Tokens > Architecture > Source of truth; Builder > Interop > Design tools
- **Preview:** a round-trip diagram: which targets are generated, which only mirror, and which direction sync runs.
- **Skip:** yes, builder.
- **Block class:** I (owner input)
- **Time weight:** high (fan-out 9)
- **Evidence:** DC-L16-02, DC-L07-08, DC-L11-16; S-L11-030, S-L07-011, S-L16-113
- **Merges:** K2.5, K10.5

### Q-tool-02 · How will engineers get and use the system? · Standard
- **Why:** Copied-in code drifts apart in each product, while a CDN runtime keeps them all the same. Headless layers leave the look to you [DC-L09-08].
- **Ask:** "How will your engineers use it: an npm package, code copied in, only CSS, or only tokens?"
- **Example:** Show the exported file tree per option.
- **Control:** multi-select
- **Options:**
  - `npm` An npm package of components, with versions (Carbon, Fluent, Ant, Chakra, Mantine) [DC-L09-08].
  - `copy-in` Copy-in source through a CLI and registry (shadcn) [S-L09-589].
  - `cdn` Loaded from a CDN, with a stable channel (Polaris) [S-L09-313].
  - `css-html` CSS and HTML only (GOV.UK, USWDS) [DC-L09-08].
  - `headless` Unstyled building blocks plus your styles (Radix, Base UI) [DC-L09-08].
  - `utilities` Utility classes (Tailwind `@theme`) [S-L09-609].
  - `tokens-only` Tokens only [inferred].
- **Default:** tokens in DTCG JSON, emitted as CSS variables, Tailwind `@theme` and the shadcn contract. *Source:* card heuristic, "where generated systems land today" [DC-L09-08; S-L09-587, S-L09-609].
- **Decides:** DC-L09-08
- **Changes:** DC-L11-14, DC-L16-12, DC-L08-03 · blocks: Delivery > Packaging
- **Preview:** the file tree the builder will export for each checked channel.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L09-08; S-L09-199, S-L09-313, S-L09-587, S-L09-589, S-L09-609
- **Merges:** K10.1

### Q-tool-04 · Should Figma components be linked to code for AI tools? · Expert
- **Show if:** Q-tool-03 is figma-org or figma-ent
- **Why:** Linked components let AI build screens from your real system, not generic React + Tailwind [DC-L07-24; S-L07-042].
- **Ask:** "Should Figma components be linked to code for AI tools?"
- **Example:** Show one MCP response with and without Code Connect.
- **Control:** single choice
- **Options:**
  - `cc-ui` Code Connect set up in Figma, with many frameworks for each component [S-L07-026].
  - `cc-cli` Code Connect from the command line, with repo templates and prop maps [S-L07-026].
  - `none` None: the MCP emits generic React + Tailwind [S-L07-027].
  - `readiness` Only clear names and notes for AI: meaningful names, descriptions, an Examples page (up to 200 examples) [S-L07-042].
- **Default:** cc-ui for the top 20 components, plus descriptions on every component and semantic variable and an Examples page. *Source:* card heuristic [DC-L07-24].
- **Decides:** DC-L07-24
- **Changes:** DC-L11-23 · blocks: Tooling > Design-code bridge
- **Preview:** a sample MCP response for one component, with and without linkage.
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L07-24; S-L07-026, S-L07-027, S-L07-042

---

## Stage 06 · Visual direction
> Screen: the overall look before any single foundation. Graph step 2-3. Cycle kept together: DC-L15-01 (style preset) + DC-L15-04 (density voice): a minimal style needs low density to stay usable, and a dense layout needs a style with strong signifiers [DC-L15-01, DC-L15-04; S-L15-004]. Quick mode derives every answer here from Q-aud-01 and the personality sliders.

### Q-dir-01 · Which overall visual style fits the product? · Standard
- **Why:** The style preset sets depth, glass effects, corner radius, borders and color strength all at once. It steers 12 other choices (fan-out 12) [DC-L15-01].
- **Ask:** "Which overall look fits: flat, tonal, glass, neo-brutalist, soft, or bold and busy?"
- **Example:** Show one product screen in each style.
- **Control:** single choice (visual cards)
- **Options:**
  - `flat2` Flat 2.0: mostly flat surfaces, subtle shadows or tonal steps, clear signifiers; neutral, efficient, timeless (Carbon, Primer, Polaris, Fluent) [S-L15-009].
  - `tonal` Material tonal: tonal surface steps and dynamic color; friendly and systematic (M3; Expressive adds shapes and springs) [DC-L15-01].
  - `glass` Glass: translucent controls and navigation only, 35% dimming under clear glass; premium and native on Apple, can obscure content (Liquid Glass, Fluent Acrylic) [S-L15-073, S-L15-005, S-L15-007].
  - `neo-brutalist` Neo-brutalist: thick borders, solid 4px offset shadow, 2-3 bold colors, quirky display face; bold, indie, irreverent (Figma and Gumroad brands) [S-L15-006].
  - `soft` Soft 3D (neumorphic): extruded same-color surfaces with paired soft shadows; tactile but vague; offered only with a contrast warning [S-L15-060].
  - `maximal` Loud and busy (maximal): vibrant palettes, overlapping visuals, bold type; energetic but busy; marketing surfaces only [S-L15-050].
- **Default:** flat2 with strong signifiers. *Source:* card heuristic; keep the app on a durable base and reserve fashionable styles for marketing [DC-L15-01].
- **Decides:** DC-L15-01
- **Changes:** DC-L04-10, DC-L04-15, DC-L04-02, DC-L04-07, DC-L01-10, DC-L15-05, DC-L15-08, DC-L15-09 · blocks: Foundations > Visual language > Style preset
- **Preview:** one product screen (nav, card, form, table) rendered in each style, with contrast warnings on soft and glass.
- **Use / avoid:** use flat 2.0 or tonal for app surfaces people use daily; use glass only on the functional layer (bars, controls, sheets) and never on reading surfaces; keep neo-brutalist and maximal for marketing or indie products; avoid soft/neumorphic for anything interactive unless borders are added to reach 3:1 [DC-L15-01; S-L10-008 via DC-L10-12].
- **Skip:** yes; Quick maps sliders A, C and E to a preset [inferred from L06 section 4.2].
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 13)
- **Evidence:** DC-L15-01; S-L15-004, S-L15-005, S-L15-006, S-L15-009, S-L15-060, S-L15-073

### Q-dir-02 · How much should fit on a screen? · Standard
- **Why:** Spacious screens look confident but slow down people who come back often. Compact screens look efficient but need strong grouping and clear signs of what you can click [DC-L15-04; S-L15-003, S-L15-004].
- **Ask:** "How much should fit on a screen: compact, comfortable, or spacious?"
- **Example:** Show a data table at each density.
- **Control:** single choice (pre-filled from Q-aud-01)
- **Options:**
  - `compact` Compact: serious, efficient, expert; more data per screen (Carbon table rows from 24px) [S-L08-062; DC-L15-04].
  - `comfortable` Comfortable: calmer, touch-friendly, consumer feel [DC-L08-13].
  - `spacious` Spacious: calm, premium, focused message [DC-L15-04].
  - `user-selectable` Let people choose: default plus a compact mode (Atlassian `spacing="compact"`, Salesforce comfy/compact) [S-L08-063; DC-L03-10].
- **Default:** comfortable for app surfaces, spacious for marketing, compact as a user option for data-heavy components (tables, lists, menus, trees). *Source:* card heuristic [DC-L15-04, DC-L08-13].
- **Decides:** DC-L15-04, DC-L08-13
- **Changes:** DC-L15-02, DC-L15-05, DC-L15-09, DC-L03-10, DC-L03-11, DC-L02-08 · blocks: Foundations > Visual language > Density voice; Components > Density
- **Preview:** a data table and a settings form at each density, with the target-size floor drawn so it visibly does not shrink [DC-L15-04].
- **Use / avoid:** use compact for data-heavy components (tables, lists, menus, trees); use spacious for marketing and focused tasks; avoid shrinking targets with density; they stay at the floor in every mode [DC-L15-04, DC-L08-13; S-L08-070].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 8)
- **Evidence:** DC-L15-04, DC-L08-13; S-L15-003, S-L15-004, S-L08-062, S-L08-063, S-L08-070
- **Merges:** K6.3 (density modes part)

### Q-dir-03 · How dramatic should the difference between headings and body text be? · Standard
- **Why:** This sets the size step between text levels, the font weights and the number of text colors. If too subtle, levels "almost match"; if too dramatic, few steps are left to use [DC-L15-02; S-L15-070].
- **Ask:** "How much should headings stand out from body text?"
- **Example:** Show a heading ladder at subtle, balanced and dramatic.
- **Control:** single choice + Expert sub-choice (lead lever: size, weight or color)
- **Options:**
  - `subtle` Subtle: ratio 1.125-1.2 (16, 18, 20, 23px), weights 400 and 600; calm, dense, professional (Carbon productive) [S-L15-038; DC-L15-02].
  - `balanced` Balanced: ratio 1.25 (16, 20, 25, 31, 39px), weights 400/600/700 [DC-L15-02].
  - `dramatic` Dramatic: ratio 1.333 or more, display jumps of 3-4x; editorial, confident [S-L15-033, S-L15-028].
- **Default:** balanced, two weights, three text colors. *Source:* card heuristic [DC-L15-02]; the builder keeps adjacent levels at least about 10% apart in size [DC-L02-10].
- **Decides:** DC-L15-02
- **Changes:** DC-L01-14, DC-L02-09, DC-L02-15, DC-L03-24 · blocks: Foundations > Visual language > Hierarchy > Strength
- **Preview:** a heading ladder plus an article card at each strength; levels closer than the threshold are flagged.
- **Use / avoid:** use subtle hierarchy in dense tools where color and weight lead; use dramatic hierarchy on editorial and marketing pages; avoid color-only hierarchy and avoid levels that almost match [DC-L15-02; S-L15-002, S-L15-070].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L15-02; S-L15-002, S-L15-028, S-L15-033, S-L15-038, S-L15-070

### Q-dir-04 · How should related things be grouped? · Standard
- **Why:** This decides if screens group things with space, cards or lines. It drives surface colors, divider lines and white space [DC-L15-05].
- **Ask:** "Should related things be grouped by space, cards, or lines?"
- **Example:** Show one settings page grouped three ways.
- **Control:** single choice
- **Options:**
  - `space` Space first: proximity only, outer gaps larger than inner; lighter, calmer, modern (Refactoring UI "Use fewer borders"; Carbon, Fluent) [S-L15-037; DC-L03-24].
  - `containers` Cards and panels first: cards and tinted panels; structured, "enterprise"; "boxes in boxes" when overused [S-L15-012].
  - `lines` Lines first: rules and separators; orderly, editorial, busy if lines multiply [S-L15-033, S-L15-053].
- **Default:** space first; containers when content types mix or items sit in a grid; lines for long lists; inner:outer spacing at 1:2 or more. *Source:* card heuristic [DC-L15-05; DC-L03-24].
- **Decides:** DC-L15-05
- **Changes:** DC-L01-13, DC-L03-24, DC-L04-08, DC-L08-15 · blocks: Foundations > Visual language > Grouping
- **Preview:** a settings page grouped each way.
- **Use / avoid:** use space for simple groups, containers for mixed content or grids, lines for long homogeneous lists; avoid nesting containers inside containers [DC-L15-05; S-L15-012].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L15-05; S-L15-010, S-L15-012, S-L15-033, S-L15-037, S-L15-053

### Q-dir-05 · Should layouts line up on the side where reading starts, or be centered? · Expert
- **Why:** This sets which side text lines up on by default, and where centered layouts are allowed [DC-L15-08].
- **Ask:** "Should things line up on the side where reading starts, or sit in the center?"
- **Example:** Show an empty state and a form in each alignment.
- **Control:** single choice
- **Options:**
  - `start` Lined up at the start side: efficient, modern, scannable (Apple's "top and leading side") [S-L15-053, S-L15-072].
  - `centered` Centered, the same on both sides: calm, ceremonial, "landing page"; long centered text reads poorly [S-L15-001; inferred].
  - `radial` In a circle (radial): rare in UI (gauges, radial menus) [S-L15-001, S-L15-050].
- **Default:** start-aligned everywhere; center only single-focus moments with short text (empty states, dialogs, sign-in). *Source:* card heuristic [DC-L15-08].
- **Decides:** DC-L15-08
- **Changes:** DC-L02-18 · blocks: Foundations > Layout > Balance
- **Preview:** an empty state and a form in each alignment.
- **Use / avoid:** use centered layouts for single-focus moments with short text (empty states, dialogs, sign-in); avoid centering multi-line body text [DC-L15-08].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L15-08; S-L15-001, S-L15-033, S-L15-049, S-L15-053

---

## Stage 07 · Themes and modes
> Screen: which variations of the system exist. Graph step 0-2. Asked before color because every color decision must be made once per mode [DC-L07-15; BOARD L01 note: dark mode is always a separate mapping].

### Q-theme-01 · Which appearance modes does the product support? · Standard
- **Why:** Each extra mode doubles the color choices and contrast checks. Dark mode is its own set of picks, not light mode flipped [DC-L10-17; S-L10-089].
- **Ask:** "Should the app have light and dark modes that follow the device, or just one mode?"
- **Example:** Show the preview split diagonally, light and dark.
- **Control:** single choice
- **Options:**
  - `system-light-dark` Light and dark, matching the device setting: blends with the OS at night (Apple expects apps to respect the preference) [S-L10-089].
  - `light-dark-toggle` Light and dark, plus a switch in the app: web only, in addition to system-follow [DC-L10-17].
  - `light-only` Light only [DC-L07-15].
  - `dark-only` Dark only: brand colors glow, fewer and brighter accents (watch, TV, car at night) [DC-L14-09].
- **Default:** system-light-dark on phone, tablet, desktop and web; dark-only on watch; day/night auto in cars. *Source:* L09 shared default row 6 (21 of 25 systems) and platform convention [L09 A1; DC-L10-17, DC-L14-09].
- **Decides:** DC-L10-17, DC-L14-09
- **Changes:** DC-L01-18, DC-L01-19, DC-L04-13, DC-L07-15, DC-L07-17 · blocks: Foundations > Color > Appearance modes
- **Preview:** the draft screen split diagonally, light and dark.
- **Use / avoid:** use system-following modes on Apple platforms; offer an in-app toggle only on web and only in addition; avoid an app-only appearance switch on Apple, which reads as broken [DC-L10-17; S-L10-089].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L10-17, DC-L14-09; S-L10-089, S-L10-027, S-L14-037, S-L11-030
- **Merges:** K6.1, P18

### Q-theme-02 · Besides light and dark, which other theme switches should exist? · Expert
- **Why:** Each extra theme switch multiplies what must be checked. For example, 2 modes x 3 brands = 6 palettes to test for contrast [DC-L11-25, DC-L07-15].
- **Ask:** "Besides light and dark, what other theme switches do you need?"
- **Example:** Show the palette count, e.g. '2 modes x 2 contrasts = 4 palettes to test'.
- **Control:** multi-select (pre-filled from Q-aud-04)
- **Options:**
  - `contrast` Contrast: standard and high (Material standard/medium/high; Atlassian increased contrast; Primer 14 theme files incl. color-blind variants) [S-L07-104, S-L07-108, S-L07-110].
  - `density` Density or size: compact/comfortable (Radix scaling 90-110%) [S-L11-068].
  - `brand` Brand: see Q-theme-03 [DC-L07-16].
  - `breakpoint` Screen-size values (38% of systems) [S-L11-030].
  - `platform` Platform values (24% of systems) [S-L11-030].
- **Default:** color scheme + contrast; density only with data-dense screens; brand only with a real second brand. *Source:* card heuristic [DC-L07-15, DC-L11-25].
- **Decides:** DC-L07-15, DC-L11-25
- **Changes:** DC-L07-01, DC-L07-17, DC-L07-18, DC-L01-20 · blocks: Tokens > Theming > Modes; Foundations > Theming scope
- **Preview:** a mode-combination grid with the count of palettes to test, and the Figma mode budget from Q-tool-03.
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L07-15, DC-L11-25; S-L07-004, S-L07-104, S-L07-110, S-L11-030
- **Merges:** K6.3 (breakpoint modes), K6.4

### Q-theme-03 · Will other brands, products or clients re-skin this system? · Standard
- **Why:** Locked systems look the same everywhere. Generator systems keep the structure but change the hue, and theme-swap systems can also change shape and depth [DC-L09-07].
- **Ask:** "Will other brands, products or clients put their own look on this system?"
- **Example:** Show the preview re-skinned with two sample brand colors.
- **Control:** single choice
- **Options:**
  - `locked` One brand, locked (Carbon, Primer, Geist) [DC-L09-07].
  - `generator-ready` One brand now, built so more can be added: semantic tier + brand-color generator + contrast check [DC-L09-07].
  - `brand-themes` Several of our own brands on one shared base: shared anatomy and behavior, different color, type, imagery (Brad Frost core + brand + sub-brand layers; Swiggy > Instamart) [S-L06-053, S-L06-066].
  - `white-label` White-label clients: one brand color in, full theme out (Blade `createTheme({brandColor})`, Fluent 16-step ramp, Paste overrides) [DC-L09-07; S-L09-459].
- **Default:** generator-ready. *Source:* card heuristic "build every system as if a second brand will come" [DC-L09-07]; 63% of systems theme by brand [S-L11-030].
- **Decides:** DC-L09-07
- **Changes:** DC-L07-16, DC-L06-16, DC-L06-17, DC-L06-06, DC-L07-01 · blocks: Theming > Brands and modes
- **Preview:** the draft screen re-skinned with two sample brand colors, contrast re-checked live.
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L09-07; S-L09-170, S-L09-237, S-L09-459, S-L06-053, S-L11-030
- **Merges:** K6.2, B10

### Q-theme-04 · What may differ between brands, and how is that stored? · Expert
- **Show if:** Q-theme-03 is brand-themes or white-label
- **Why:** Brands share one base of semantic tokens (values named for their job). If more than about 20% differ, they are separate themes, not brands [DC-L07-16].
- **Ask:** "What may differ between brands, and how should brands be stored?"
- **Example:** Show a table of brandable tokens per brand.
- **Control:** multi-select (what flexes) + single choice (storage)
- **Options:**
  - `flex-color-type-imagery` Change color, font, logo and images; keep parts, how they work, names and status meanings [DC-L06-16].
  - `flex-with-care` Also change corner radius, density and motion, with care [DC-L06-16].
  - `store-mode` Brand as a mode: simple, capped by the plan's mode limit (Pro 10, Org 20) [S-L07-014].
  - `store-axis` Brand as its own switch (a collection or DTCG resolver modifier): additive, 3 brands + 2 schemes = 5 modes [DC-L07-16].
  - `store-extended` Figma extended collections (Enterprise): brands override only what differs [S-L07-015, S-L07-016].
- **Default:** flex color, typeface, logo, imagery; store as its own axis (extended collections on Enterprise). *Source:* card heuristics [DC-L07-16, DC-L06-16].
- **Decides:** DC-L07-16, DC-L06-16
- **Changes:** DC-L07-17, DC-L07-18, DC-L06-17 · blocks: Tokens > Theming > Brands
- **Preview:** a table of brandable tokens with each brand's values.
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L07-16, DC-L06-16; S-L07-011, S-L07-014, S-L07-015, S-L06-053, S-L06-094

---

## Stage 08 · Color system
> Screen: one screen with four sections (brand input, strategy, ramps and neutrals, roles and contrast) around one shared live preview: a product screen, the generated ramps, and a contrast matrix of every foreground/background pair, in light and dark. Graph step 1-4. Cycle kept together: the 21-card color cycle (DC-L01-01 to DC-L01-13, DC-L01-15, DC-L01-18, DC-L01-21 to DC-L01-24, DC-L15-03, DC-L15-06) plus the two-card cycle DC-L10-04 + DC-L10-05. Changing any answer here regenerates the whole palette, so the questions share one preview instead of separate screens [inferred from the cycle].

### Q-color-01 · Do you have fixed brand colors, or should the builder generate the palette from one color? · Quick
- **Why:** Hand-picked colors keep the brand's exact feel; a seed color gives even shades. Contrast targets make text on every color easy to read, in a way you can predict [L09 divergence 6; DC-L09-03].
- **Ask:** "Do you have fixed brand colors, or should I build the palette from one color?"
- **Example:** Ask for hex values; if none, offer 3 seed swatches weighted by the sliders.
- **Control:** color picker (1-3 seeds, each lockable) + single choice (method)
- **Options:**
  - `keep-hex` Keep your exact brand colors and tune the shades by hand (Carbon, Primer, Atlassian, GOV.UK) [DC-L09-03].
  - `seed` Generate from one seed color (Material HCT, Ant, Blade `createTheme`, Fluent brand ramp) [S-L09-459; DC-L09-03].
  - `seed-3` Generate from three inputs: brand color, neutral base and contrast (Linear replaced 98 per-theme variables with 3) [S-L06-012; DC-L06-06].
  - `contrast-targets` Set each step by a contrast goal (Spectrum Leonardo, USWDS grades, Radix APCA steps) [DC-L09-03].
- **Default:** seed-3 in OKLCH with contrast-checked steps; locked brand hexes are pinned to the nearest step, and the UI fill uses the step that reaches 4.5:1 with its text. *Source:* card heuristics [DC-L09-03, DC-L06-06, DC-L01-09].
- **Decides:** DC-L09-03, DC-L01-09
- **Changes:** DC-L01-01, DC-L01-03, DC-L01-04, DC-L06-06, DC-L15-06 · blocks: Foundations > Color > Palette generation
- **Hook:** Accepts hex, RGB or OKLCH values, a brand book PDF, or a reference from Q-ref-01. If no brand color exists: the builder suggests seeds weighted by the personality sliders (blue reads competent, red excitement, per Labrecque & Milne) and labels the choice as a starting point, not a brand decision [S-L06-072].
- **Preview:** the seed becomes ramps live; locked hexes show a pin on their step; a light brand color (yellow, cyan, lime) visibly switches its button text to dark (Spectrum does this) [S-L01-036].
- **Use / avoid:** use the brand hex as a ramp anchor and pick UI steps by contrast; avoid using a brand color whose ratio with white is below 3:1 for small text; use it as a fill with dark text or as a tint [DC-L01-09; S-L01-044].
- **Skip:** yes, a seed is suggested.
- **Block class:** E (extractable)
- **Time weight:** high (fan-out 3)
- **Evidence:** DC-L09-03, DC-L01-09, DC-L06-06 (context); S-L09-459, S-L09-563, S-L06-012, S-L01-036, S-L01-044
- **Merges:** K3.4, B7 (brand colors), K7.1 (ramp method)

### Q-color-02 · Where should your brand color appear? · Quick
- **Why:** Where brand color goes (on actions only, on containers, or on whole surfaces) shapes the look. It is third on L09's (inferred) ranking of visual differences [L09 divergence 3; DC-L06-04].
- **Ask:** "Where should your brand color show: only on key actions, in one standout area, or on the bars and menus?"
- **Example:** Show the same screen with each placement.
- **Control:** single choice (with platform overrides in Expert)
- **Options:**
  - `accent` Only on main actions, links, status and the selected tab: calm, content-first (Apple HIG, Carbon) [S-L06-008, S-L06-001].
  - `signature-surface` One standout area carries the brand: instantly recognizable silhouette (Slack aubergine sidebar) [S-L06-030].
  - `flooded-chrome` Brand color on the app bars and floating buttons: playful, louder (M2 style, rated more playful) [S-L06-011].
  - `content-layer` Brand color in the content, scrolling under glass controls: modern, dynamic (Apple 2026) [S-L06-100, S-L10-009].
  - `neutral-first` Mostly gray, with a faint brand tint on bars and menus (Linear limited its blue there) [S-L06-012].
- **Default:** accent, with signature-surface optional; on Apple glass platforms brand color moves into content, on Android a brand seed, freer on web. *Source:* card heuristics [DC-L06-04, DC-L10-04]; L09 shared pattern row 3 (neutral surfaces + one accent in all but one of 24 systems).
- **Decides:** DC-L06-04, DC-L10-04
- **Changes:** DC-L15-03, DC-L01-13, DC-L08-05, DC-L01-08 · blocks: Foundations > Color > Brand color role; Foundations > Color > Brand accent > Platform application
- **Preview:** the preview screen re-renders per option; on iOS, a tinted nav bar is flagged as "fighting the glass" [S-L10-009, S-L10-010].
- **Use / avoid:** use brand color on the one element per view that matters most; avoid tinting several control backgrounds at once ("Using your brand color too broadly can overwhelm your interface") [S-L06-008].
- **Skip:** yes, accent.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 3)
- **Evidence:** DC-L06-04, DC-L10-04; S-L06-008, S-L06-011, S-L06-030, S-L10-009, S-L10-010
- **Merges:** P5

### Q-color-03 · How colorful should the palette be? · Standard
- **Why:** Color strength (chroma) sets how calm or lively the product feels. If all colors are strong, status colors lose their punch, because everything shouts [DC-L01-10].
- **Ask:** "How colorful should the palette be, from all gray to vivid?"
- **Example:** Show a chroma slider moving surfaces, accent and status together.
- **Control:** single choice (pre-filled from sliders A and D)
- **Options:**
  - `monochrome` All gray or nearly gray: calm, premium, technical (Material Monochrome and Neutral variants, chroma 0 and 8-12; Polaris black brand) [S-L01-010, S-L01-039].
  - `tonal` Tonal, low to medium color: friendly, balanced (Material TonalSpot, primary chroma 32-36) [S-L01-010, S-L06-083].
  - `vivid` Vivid: energetic, consumer-grade (Material Vibrant; Tailwind v4 P3-leaning OKLCH, blue-500 chroma 0.214) [S-L01-010, S-L01-062].
  - `expressive` Hues turned away from the source color (Material Expressive) [S-L06-083].
  - `fidelity` Fidelity: the brand hue stays exact in containers; for hues that are a legal or recognition asset [S-L06-083; DC-L06-05].
- **Default:** tonal for productivity products, vivid for consumer and marketing. *Source:* card heuristic [DC-L01-10, DC-L06-05].
- **Decides:** DC-L01-10, DC-L06-05
- **Changes:** DC-L01-15, DC-L01-24, DC-L15-06 · blocks: Foundations > Color > Palette character > Vibrancy; Foundations > Color > Scheme strategy
- **Preview:** a chroma slider under the five named stops; surfaces, accent and status chips update together.
- **Use / avoid:** use low chroma on large areas (surfaces) and spend chroma on small, high-meaning elements (primary action, status, selection); avoid vivid surfaces in high-trust categories [DC-L01-10; S-L01-013, S-L06-010].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L01-10, DC-L06-05; S-L01-010, S-L01-058, S-L01-062, S-L06-083, S-L06-072

### Q-color-04 · How many accent colors does the product need? · Standard
- **Why:** With one accent color, anything in color looks like you can click it. Three accents feel more expressive but need discipline [DC-L01-08].
- **Ask:** "How many accent colors does the product need?"
- **Example:** Show the screen with each accent's job highlighted.
- **Control:** single choice
- **Options:**
  - `one` One accent plus grays and status colors: focused, calm (Carbon core blue; Apple one app accent; Linear, Notion) [S-L01-029, S-L01-013; DC-L15-06].
  - `analogous` One accent with nearby hues for backgrounds and drawings: harmonious, soft [S-L15-017].
  - `contrasting` An opposite-hue accent on grays tinted to match: the strongest "pop" for primary actions [S-L15-017].
  - `three` Main, second and third accents (Material 3: tertiary for contrasting accents such as badges) [S-L01-004].
  - `multi` Many accents: playful (Mailchimp), needs strict role rules [DC-L15-06].
- **Default:** one accent plus neutrals plus status, analogous tints for surfaces. *Source:* card heuristics, "harmonize the large areas, contrast the small important ones" [DC-L01-08, DC-L15-06]; L09 shared pattern row 3.
- **Decides:** DC-L01-08, DC-L15-06
- **Changes:** DC-L01-11, DC-L01-24, DC-L08-05 · blocks: Foundations > Color > Brand vs UI color > Accent count; Foundations > Color > Scheme strategy
- **Preview:** the product screen with each accent's jobs highlighted (actions, discovery, categories).
- **Use / avoid:** add an accent only when it has a job (a second action tier, discovery, categories); avoid adding one for decoration or picking wheel presets (triadic, complementary) as a palette [DC-L01-08; S-L15-025].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L01-08, DC-L15-06; S-L01-004, S-L01-013, S-L01-029, S-L15-017, S-L15-054

### Q-color-05 · How much of a screen may use accent color and emphasis? · Expert
- **Why:** Making more things stand out, with no limit, makes screens louder, not clearer [DC-L15-03; S-L15-067].
- **Ask:** "How much of a screen may use accent color?"
- **Example:** Show the accent-area meter and a two-primaries warning.
- **Control:** single choice (pre-filled from Q-brand-04)
- **Options:**
  - `strict` Strict: one dominant element and one primary action per view; accent only on primary actions, selection, status (Apple) [S-L15-067, S-L15-054].
  - `moderate` Moderate: one primary plus one highlighted secondary; accent on links and active navigation [S-L15-038].
  - `expressive` Expressive: one or two hero moments per product; large color areas on chrome [DC-L06-03].
- **Default:** strict for app surfaces, moderate for marketing; 60-30-10 is a soft check, not a rule. *Source:* card heuristic [DC-L15-03]; BOARD L15 note (60-30-10 has weak evidence).
- **Decides:** DC-L15-03
- **Changes:** DC-L13-18, DC-L08-05, per-screen lint thresholds (DC-L15-11) · blocks: Foundations > Visual language > Hierarchy > Emphasis budget
- **Preview:** an accent-area meter on the preview screen, plus a warning when two primaries appear.
- **Use / avoid:** use accent for the one thing the user should do next; avoid two primary buttons in one group ("if you need two primaries, one of them is secondary") [DC-L15-03].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L15-03; S-L15-026, S-L15-038, S-L15-048, S-L15-054, S-L15-067

### Q-color-06 · Should colors change to match the user's wallpaper or device accent? · Standard
- **Show if:** Q-plat-01 includes android, ios or desktop
- **Why:** Taking colors from the device feels personal and native. But people remember the brand less, and screenshots look different for each user [DC-L10-05].
- **Ask:** "Should colors match the user's wallpaper or the accent color on their device?"
- **Example:** Show the Android preview recolored by three wallpapers.
- **Control:** single choice
- **Options:**
  - `static` Fixed brand color (Material static baseline; best for work apps and iOS) [S-L06-082, S-L01-006].
  - `dynamic-optional` Fixed, but people can turn on Android dynamic color (API 31+) [S-L10-019; DC-L01-21].
  - `follow-os` Follow the device: Android dynamic color, Wear OS watch-face color, macOS accent [S-L10-019, S-L10-027, S-L10-010].
- **Default:** dynamic on Android for utility apps, fixed brand for brand-led consumer apps; brand-critical and status colors stay fixed; on Apple, design icon layers for all four icon looks. *Source:* card heuristics [DC-L10-05, DC-L01-21].
- **Decides:** DC-L10-05, DC-L01-21
- **Changes:** DC-L01-15, DC-L05-12 · blocks: Foundations > Color > Personalization policy; Foundations > Color > Modes > Dynamic color
- **Preview:** the Android preview recolored with three sample wallpapers; brand-critical colors stay put.
- **Use / avoid:** let dynamic color own surfaces and secondary accents; avoid letting it change error and brand-critical colors [DC-L01-21; S-L01-004].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L10-05, DC-L01-21; S-L10-019, S-L10-075, S-L01-006, S-L01-058, S-L06-082
- **Merges:** P6, B9

### Q-color-07 · How should color ramps be built? · Expert
- **Why:** In HSL, yellow at the same lightness looks lighter than blue. Perceptual or contrast-indexed ramps keep each step just as heavy in every color [DC-L01-01; S-L01-044].
- **Ask:** "How should each color ramp (its shades from light to dark) be built?"
- **Example:** Show blue and green at the same step, HSL vs OKLCH.
- **Control:** single choice (space) + single choice (step rule) + single choice (generator)
- **Options:**
  - `oklch` OKLCH, perceptual (Tailwind v4 moved its palette to oklch in Jan 2025; CSS `oklch()` Baseline since May 2023) [S-L01-045, S-L01-046].
  - `hct` HCT, numbered by tone: same tone gives the same brightness across hues (Material; tones 50 vs 98 give 3:1) [S-L01-006].
  - `contrast-indexed` Steps set by contrast: every step has the same ratio across hues (Spectrum: every 700 is 3.01:1) [S-L01-035].
  - `hand-tuned` Tuned by hand for each color: more character, less predictable (Tailwind 500 steps range L 62-77%) [S-L01-062].
  - `preset` Use a stock palette (Tailwind default, Radix Colors): a recognizable stock look [S-L01-001, S-L01-052].
  - `lab-hsl` CIELAB/LCH or HSL: Lab was Stripe's 2019 fix; HSL is the legacy default that washes out yellows [S-L01-044].
- **Default:** OKLCH with contrast-indexed steps; HCT when the system must feed Material dynamic color. *Source:* card heuristics [DC-L01-01, DC-L01-03, DC-L01-04].
- **Decides:** DC-L01-01, DC-L01-03, DC-L01-04
- **Changes:** DC-L01-02, DC-L01-18, DC-L01-24, DC-L07-10 · blocks: Foundations > Color > Palette generation > Color space; Step semantics; Tooling
- **Preview:** two accents side by side at the same step; switching the method shows whether they stay equally heavy, with the contrast of each step printed.
- **Use / avoid:** use contrast-indexing when users can recolor the accent, so every accent passes the same pairings; avoid HSL-based lightness steps [DC-L01-03, DC-L01-01].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 6)
- **Evidence:** DC-L01-01, DC-L01-03, DC-L01-04; S-L01-006, S-L01-035, S-L01-044, S-L01-045, S-L01-062

### Q-color-08 · How many steps should each ramp have, and how are they numbered? · Expert
- **Why:** More steps allow quieter, layered screens. Fewer steps force bolder jumps [DC-L01-02].
- **Ask:** "How many steps per ramp, and how should they be numbered?"
- **Example:** Show a 12-step ramp with each step's job labeled.
- **Control:** single choice
- **Options:**
  - `tailwind-11` 11 steps, 50-950 (Tailwind) [S-L01-001].
  - `radix-12` 12 steps, 1-12, each with a fixed job (Radix) [S-L01-002].
  - `tones` Tones 0-100 (Material) [S-L01-006].
  - `carbon-10` 10 grades 10-100 plus black and white (Carbon) [S-L01-029].
  - `spectrum-14` 14 tints and shades per color (Spectrum) [S-L01-036].
- **Default:** 12 steps with a fixed job per step, exportable to a 50-950 scale. *Source:* L09 shared default row 4 (12 systems use 10-12 steps) [L09 A1; DC-L01-02].
- **Decides:** DC-L01-02
- **Changes:** DC-L01-07, DC-L01-11, DC-L07-03 · blocks: Foundations > Color > Palette generation > Ramp scale
- **Preview:** the ramp strip with each step's job labeled (app background, subtle fill, border, solid, text).
- **Use / avoid:** use numbers with gaps (50-950) if steps may be inserted later, 1-12 if every step has a fixed job; avoid more steps than distinct UI jobs plus two hover/pressed shifts [DC-L01-02].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L01-02; S-L01-001, S-L01-002, S-L01-006, S-L01-029, S-L01-036

### Q-color-09 · Should grays be pure, or tinted warm or cool? · Standard
- **Why:** Grays fill most of the screen, so warm or cool grays change how the product feels. Linear moved to "a warmer gray" in 2026 [DC-L01-06; S-L06-067].
- **Ask:** "Should grays be pure, cool, warm, or tinted toward your brand?"
- **Example:** Show surfaces re-tinted as the slider moves.
- **Control:** single choice + hue/chroma slider
- **Options:**
  - `pure` Pure gray (chroma 0): neutral, technical, never competes with content (Tailwind neutral, Radix gray, Spectrum for image workflows) [S-L01-062, S-L01-036].
  - `cool` Cool tint: crisp, digital, trustworthy (Tailwind slate chroma 0.046 hue 257; Primer) [S-L01-062, S-L01-027].
  - `warm` Warm tint: friendly, softer (Linear 2026) [S-L06-067; DC-L01-06].
  - `hue-matched` Slight tint toward the accent hue (OKLCH chroma about 0.01-0.03 at mid steps) [DC-L01-06].
- **Default:** hue-matched for branded products, pure for image- or data-critical tools. *Source:* card heuristic [DC-L01-06].
- **Decides:** DC-L01-06
- **Changes:** DC-L01-07, DC-L01-13, DC-L15-06 · blocks: Foundations > Color > Neutrals > Temperature
- **Preview:** the preview screen's surfaces, borders and text re-tinted live as the slider moves.
- **Use / avoid:** use pure gray where color judgment matters (photo, data, charts); keep chroma lowest at the lightest and darkest steps; avoid strong tints that make status colors look off [DC-L01-06; S-L01-036].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L01-06; S-L01-027, S-L01-036, S-L01-053, S-L01-062, S-L06-067
- **Merges:** K3.4 (neutral palette)

### Q-color-10 · How many gray steps, and should there be transparent grays? · Expert
- **Why:** More near-white grays let cards, side bars and sunken areas (wells) stand apart with no borders [DC-L01-07].
- **Ask:** "How many gray steps, and do you want transparent grays for overlays?"
- **Example:** Show the neutral ramp with background, border and text bands.
- **Control:** number (solid steps) + number (alpha steps)
- **Options:**
  - `bands` Solid grays in fixed bands by use (Primer 0-13: 0-5 backgrounds, 7-8 borders, 9-10 text) [S-L01-027].
  - `separate-dark` Separate gray ramps for light and dark (Atlassian Neutral and DarkNeutral) [S-L01-031].
  - `alpha` Add see-through grays to lay over any surface (Radix alpha scales) [S-L01-052].
- **Default:** 12-13 solid neutrals plus 4-5 alpha neutrals, with bands documented; at least three near-white steps in light mode and four dark steps in dark mode. *Source:* card heuristic [DC-L01-07].
- **Decides:** DC-L01-07
- **Changes:** DC-L01-13, DC-L01-14, DC-L01-27 · blocks: Foundations > Color > Neutrals > Ramp and usage
- **Preview:** the neutral ramp with bands shaded (backgrounds, borders, text) and a card stack using them.
- **Use / avoid:** use alpha neutrals for hover fills and overlays that must work on any surface; avoid using alpha for text [inferred].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L01-07; S-L01-027, S-L01-029, S-L01-031, S-L01-036, S-L01-052

### Q-color-11 · How wide a range of colors (gamut) should the system use? · Expert
- **Why:** Display P3 gives richer reds, greens and oranges on modern screens. sRGB is the simplest and shows true colors on most displays [DC-L01-05].
- **Ask:** "Should the system use sRGB only, or richer Display P3 colors where screens allow?"
- **Example:** Show accent chips in sRGB and P3.
- **Control:** single choice
- **Options:**
  - `srgb` sRGB hex only [S-L01-013].
  - `p3-enhance` sRGB with P3 overrides behind `@media (color-gamut: p3)` (Radix ships each scale twice) [S-L01-052, S-L01-049].
  - `oklch-wide` OKLCH values that may go past sRGB, fitted to the screen by browsers (Tailwind v4) [S-L01-045, S-L01-046].
  - `native-p3` Native P3 assets on Apple platforms [DC-L01-05].
- **Default:** sRGB hex primitives with optional P3 overrides for accents only; every token keeps a hex fallback (DTCG 2025.10 supports 14 color spaces plus a hex fallback). *Source:* card heuristics [DC-L01-05, DC-L07-10; S-L07-003].
- **Decides:** DC-L01-05, DC-L07-10
- **Changes:** DC-L10-22, DC-L07-25 · blocks: Foundations > Color > Color spaces and gamut; Tokens > Types > Color
- **Preview:** accent chips in sRGB and P3 next to each other (visible only on a P3 display; otherwise a note).
- **Use / avoid:** use P3 where saturation carries brand or status meaning; avoid P3 for neutrals, where it adds nothing [DC-L01-05, inferred].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L01-05, DC-L07-10; S-L01-045, S-L01-049, S-L01-052, S-L07-003

### Q-color-12 · How should color roles be named? · Expert
- **Why:** Names that start with where a color goes (background, border, text) make it hard to put a border color on text. Names built as pairs guarantee readable pairs [DC-L01-11].
- **Ask:** "How should color roles be named?"
- **Example:** Show `bgColor-accent-muted` vs `primary-container`.
- **Control:** single choice
- **Options:**
  - `property-role` Property x role x emphasis x state (`bgColor-accent-muted`, `fgColor-onEmphasis`: Primer, Atlassian) [S-L01-027, S-L01-032].
  - `material-pairs` Role plus container/on pairs, 26 roles (`primary`, `on-primary`, `surface-container-high`: Material 3) [S-L01-004].
  - `layer-based` Layer and interaction tokens (`$layer-01`: Carbon) [S-L01-029].
- **Default:** property x role x emphasis x state with explicit on-colors; also emit Material role aliases if Android dynamic color matters. *Source:* card heuristic [DC-L01-11].
- **Decides:** DC-L01-11
- **Changes:** DC-L01-12, DC-L01-14, DC-L07-04 · blocks: Foundations > Color > Semantic roles > Taxonomy
- **Preview:** a token-name inspector: hovering any element on the preview shows its role token.
- **Use / avoid:** use paired fg/bg tokens so each pair is contrast-tested; avoid tokens named after a hue ("blue-button") at the semantic tier [DC-L01-11; DC-L07-04].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L01-11; S-L01-004, S-L01-027, S-L01-029, S-L01-032

### Q-color-13 · How many emphasis levels should each color role have? · Expert
- **Why:** More levels let you use soft, tinted status panels and quiet selected states. Two levels look punchier [DC-L01-12].
- **Ask:** "How many levels of strength should each color role have?"
- **Example:** Show a banner, badge and button at each level.
- **Control:** single choice
- **Options:**
  - `two` Muted and strong (Primer) [S-L01-050].
  - `container` Base and container (Material `primary` tone 40, `primary-container` tone 90) [S-L01-004].
  - `three` Subtle, default and bold, plus a text and icon color for bold fills [DC-L01-12].
  - `six` Subtlest to boldest (Atlassian, up to six) [S-L01-030].
- **Default:** three levels plus on-bold. *Source:* card heuristic [DC-L01-12].
- **Decides:** DC-L01-12
- **Changes:** DC-L01-14, DC-L01-17 · blocks: Foundations > Color > Semantic roles > Emphasis
- **Preview:** a status banner, badge and button in each emphasis level.
- **Use / avoid:** use subtle levels on large areas (banners) and bold for small, urgent elements; avoid bold fills on page-size areas [DC-L01-12].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L01-12; S-L01-004, S-L01-030, S-L01-050

### Q-color-14 · How should surfaces be layered? · Standard
- **Why:** This decides how the page, cards and pop-ups stand apart: by shade steps, alternating layers or names by height. It also sets how dark mode shows depth [DC-L01-13].
- **Ask:** "How should stacked layers, like a card on a page, be shaded and named?"
- **Example:** Show a page, card, popover and dialog stack in light and dark.
- **Control:** single choice (pre-filled from Q-dir-04)
- **Options:**
  - `container-tiers` Named layers, not tied to shadow height: flat, calm, modern (Material 3 `surface-container-lowest` to `-highest`) [S-L01-004, S-L01-054].
  - `alternating` Alternating layers in light, stepping lighter in dark: crisp, grid-like enterprise (Carbon White/Gray 10, then Gray 100/90/80) [S-L01-029].
  - `elevation-named` Layers named by height (Atlassian) [S-L01-032].
  - `role-tiers` 4-5 layers named by job (base, raised, overlay, sunken), with their own colors in each mode [DC-L01-13].
- **Default:** role-tiers; light mode separates with shadow or border plus a subtle tone, dark mode with lighter tones. *Source:* card heuristic [DC-L01-13]; L09 shared pattern row 12.
- **Decides:** DC-L01-13
- **Changes:** DC-L04-13, DC-L04-10, DC-L08-15 · blocks: Foundations > Color > Semantic roles > Surfaces
- **Preview:** a page, card, popover and dialog stack in light and dark, with the tier of each labeled.
- **Use / avoid:** use lighter-when-higher surfaces in dark mode; avoid separating interactive surfaces by tone alone when the edge carries meaning (needs 3:1) [DC-L01-13; S-L01-023].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L01-13; S-L01-004, S-L01-010, S-L01-029, S-L01-032, S-L01-054

### Q-color-15 · Which status colors do you need? · Standard
- **Why:** A few status colors keep alerts impossible to miss. Many make busy developer tools easy to scan, but people must learn them [DC-L01-15].
- **Ask:** "Which status colors do you need beyond success, warning, danger and info?"
- **Example:** Show banners and badges per status.
- **Control:** multi-select
- **Options:**
  - `classic-4` Success, warning, danger, info (Radix hue suggestions; Carbon Red 60, Yellow 30, Green 60) [S-L01-053, S-L01-056].
  - `discovery` Discovery for new things (Atlassian purple) [S-L01-030].
  - `workflow` Workflow states: attention, severe, done, open/closed/draft (Primer) [S-L01-050].
- **Default:** the four classic statuses, each with subtle and bold levels plus text and icon, always with an icon; status hues at least 60 degrees from the brand hue. *Source:* card heuristic [DC-L01-15]; L09 shared default row 3 (4 status ramps).
- **Decides:** DC-L01-15
- **Changes:** DC-L08-18, DC-L13-07, DC-L05-23 · blocks: Foundations > Color > Semantic roles > Status
- **Preview:** banners, badges and inline errors for each status, with a warning flag if a status hue sits too close to the brand hue.
- **Use / avoid:** use dark text on yellow and amber fills, which fail 4.5:1 with white (Atlassian `warning.inverse`); avoid conveying status by color alone [DC-L01-15; S-L01-030, S-L01-024].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L01-15; S-L01-030, S-L01-036, S-L01-050, S-L01-053, S-L01-056

### Q-color-16 · How should dark mode be derived from light? · Expert
- **Show if:** Q-theme-01 includes dark
- **Why:** A mirrored mapping keeps what looks most important the same in every mode. Separate hand-tuned dark ramps look richer but drift [DC-L01-18].
- **Ask:** "How should dark mode be derived from light?"
- **Example:** Show both modes with failing pairs lit up.
- **Control:** single choice
- **Options:**
  - `tone-reassign` Same colors, a new shade for each job (Material: primary 40 becomes 80, surface 98 becomes 6) [S-L01-010].
  - `mirrored` Mirrored ramp ("700 in light is 400 in dark") with separate dark neutrals (Atlassian) [S-L01-031].
  - `separate` Separate dark scales with the same step jobs (Radix, Primer, Spectrum) [S-L01-052, S-L01-050].
- **Default:** shared hue ramps with a mirrored mapping plus separate dark neutral ramps; map by role, not by value. *Source:* card heuristic [DC-L01-18].
- **Decides:** DC-L01-18
- **Changes:** DC-L01-19, DC-L01-24, DC-L04-13 · blocks: Foundations > Color > Modes > Dark mode mapping
- **Preview:** light and dark side by side with every pair re-checked; failing pairs light up in the contrast matrix.
- **Use / avoid:** use role-based mapping so each token keeps its contrast relationship; avoid inverting colors [DC-L01-18; S-L10-089].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L01-18; S-L01-006, S-L01-010, S-L01-031, S-L01-052

### Q-color-17 · Which contrast rule should the builder enforce on every color pair? · Standard
- **Why:** AA allows mid-gray text for less important words and softer tints. AAA forces darker text and deeper accent colors [DC-L01-22].
- **Ask:** "Which contrast rule should every color pair pass?"
- **Example:** Show the contrast matrix with pass/fail per mode.
- **Control:** single choice (pre-filled from Q-aud-03)
- **Options:**
  - `aa` WCAG 2.2 AA: text 4.5:1, large text 3:1, UI parts 3:1; no rounding (4.499:1 fails) [S-L01-022, S-L01-023].
  - `aaa` WCAG 2.2 AAA: text 7:1, large text 4.5:1 (target for high-contrast themes: Primer, Material) [S-L01-025, S-L01-027].
  - `aa-apca` AA must pass, plus APCA as advice on body text (Radix and Geist use it) [DC-L01-22; L09 A1 row 11].
- **Default:** aa-apca: AA on all pairs in every mode, AAA for high-contrast modes, APCA advisory. *Source:* accessibility rule [DC-L01-22]; WCAG 3 is still a draft [BOARD L01 note].
- **Decides:** DC-L01-22
- **Changes:** DC-L01-14, DC-L01-16, DC-L01-20, DC-L02-23 · blocks: Foundations > Color > Accessibility > Contrast
- **Preview:** the contrast matrix of all role pairs, pass/fail per mode, with the nearest passing step suggested for failures.
- **Use / avoid:** test tokens as pairs, in every mode, at build time; avoid judging a single color by eye [DC-L01-22].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L01-22; S-L01-022, S-L01-023, S-L01-025, S-L01-027, S-L09-563

### Q-color-18 · How should meaning survive when color can't be seen? · Expert
- **Why:** About 1 in 12 men can't tell some colors apart (color vision deficiency). WCAG 1.4.1 (Level A) forbids color as the only clue [DC-L01-23; S-L01-060, S-L01-024].
- **Ask:** "If someone can't tell colors apart, how should the meaning still come through?"
- **Example:** Show the screen under red-green simulation.
- **Control:** single choice (links) + toggle (CVD themes)
- **Options:**
  - `underline-always` Underline links in body text: robust, more document-like [DC-L01-23].
  - `underline-hover` Links in color only (3:1 to nearby text), with one more cue on hover and focus (G183) [S-L01-024].
  - `cvd-themes` Add themes for people who mix up red and green, or blue and yellow (Primer) [S-L07-110].
- **Default:** underline-always; every color-coded meaning also gets an icon, text or shape. *Source:* accessibility rule [DC-L01-23].
- **Decides:** DC-L01-23
- **Changes:** DC-L01-24, DC-L05-25, DC-L01-20 · blocks: Foundations > Color > Accessibility > Not color alone
- **Preview:** the preview screen under red-green and blue-yellow simulation.
- **Use / avoid:** use a second channel whenever two meanings differ only in hue; avoid red/green-only status pairs [DC-L01-23].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L01-23; S-L01-013, S-L01-024, S-L01-036, S-L01-060

### Q-color-19 · Does the product show charts, and which chart colors does it need? · Standard
- **Why:** Chart colors taken from the app's own shades look at home. Separate bright chart colors pop but can clash, and long lists of group colors get hard to read [DC-L01-24].
- **Ask:** "If the product shows charts, which chart colors does it need?"
- **Example:** Show a bar chart, line chart and heatmap in light and dark.
- **Control:** single choice
- **Options:**
  - `none` No charts.
  - `brand-gray` One brand chart color plus gray: calm, branded, focused [DC-L05-23].
  - `categorical-6-8` 6-8 group colors in set order, plus one light-to-dark ramp. Two-way only for above or below target (Atlassian) [S-L01-032; DC-L05-23].
  - `carbon-14` A long list in set order (Carbon's 14 colors, starting Purple 70 #6929c4, Cyan 50 #1192e8) [S-L01-056].
- **Default:** brand-gray by default, categorical-6-8 for dashboards. *Source:* card heuristics [DC-L05-23, DC-L01-24].
- **Decides:** DC-L01-24, DC-L05-23
- **Changes:** DC-L05-22, DC-L05-24, DC-L05-25 · blocks: Foundations > Color > Data visualization palettes
- **Preview:** a bar chart, line chart and heatmap in light and dark, with the 3:1 check against the surface.
- **Use / avoid:** use direct labels or grouping beyond 8 categories; avoid adding more hues [DC-L01-24; S-L05-075].
- **Skip:** yes, none unless Q-scope-01 includes internal-tools.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L01-24, DC-L05-23; S-L01-023, S-L01-032, S-L01-056, S-L05-034, S-L05-075

---

## Stage 09 · Color details and accessibility modes
> Screen: the fine-grained color roles that follow from Stage 08, on the same live preview. Graph step 5-6. Mostly Expert; Standard asks only about hover feel and dark-mode darkness.

### Q-color-20 · How should hover and pressed states change color? · Standard
- **Why:** Overlays give soft, steady feedback on any color, even colors set by the device. Step shifts give crisper, exact changes in each theme [DC-L01-17].
- **Ask:** "On hover and press, should colors change with a see-through layer or a step along the shades?"
- **Example:** Let them hover and press a live button, row and chip.
- **Control:** single choice
- **Options:**
  - `overlay` See-through state layers: an overlay of the content color, hover +8%, focus +10%, press +10%, drag +16% (Material 3) [S-L01-005, S-L01-065].
  - `step-shift` Step along the shades: hover one step, pressed two steps toward more contrast (Carbon half steps) [S-L01-029; DC-L01-17].
  - `hybrid` Shade steps by default, with a see-through layer for colors the user or device picks [DC-L01-17].
- **Default:** hybrid. *Source:* card heuristic, overlays only where the color is unknown at design time [DC-L01-17].
- **Decides:** DC-L01-17
- **Changes:** DC-L08-09, DC-L04-17, DC-L14-06 · blocks: Foundations > Color > States > Interaction states
- **Preview:** a button, list row and chip you can hover and press on the preview, with the resulting token value shown.
- **Use / avoid:** use overlays for components that sit on user or dynamic colors; avoid state changes that rely on a hue shift alone [DC-L01-17, DC-L01-23].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L01-17; S-L01-005, S-L01-029, S-L01-064, S-L01-065

### Q-color-21 · How dark should dark mode be? · Standard
- **Show if:** Q-theme-01 includes dark
- **Why:** Pure black looks dramatic but smears on OLED screens when you scroll. Near-black looks sleek, and charcoal is softer for long reading [DC-L01-19; S-L01-055].
- **Ask:** "How dark should dark mode be: pure black, near-black, or charcoal?"
- **Example:** Show the dark preview with a darkness slider.
- **Control:** single choice + toggle (dimmed theme)
- **Options:**
  - `black` Pure black #000: cinematic, halation and smear on OLED [S-L01-055].
  - `near-black` Near-black #0D1117 to #161616: sleek, modern (Primer, Carbon Gray 100, Material tone 4) [S-L01-050, S-L01-029, S-L01-010].
  - `charcoal` Charcoal #262626 to #292929: soft and comfortable (Carbon Gray 90, Fluent) [S-L01-029, S-L01-034].
  - `dimmed` Add a dimmed theme for long reading at night (Primer dark-dimmed) [DC-L01-19].
- **Default:** a dark base between #121212 and #1a1a1a with a slight neutral tint; accents one or two steps lighter and lower in chroma than in light. *Source:* card heuristic [DC-L01-19].
- **Decides:** DC-L01-19
- **Changes:** DC-L04-13, DC-L04-12 · blocks: Foundations > Color > Modes > Dark base and dimmed
- **Preview:** the dark preview with a darkness slider; accent chroma drops as the base darkens.
- **Use / avoid:** use "dimmed" only for audiences that read long-form at night (developer tools, reading apps); avoid bright objects on pure black in immersive views [DC-L01-19; S-L01-013].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-19; S-L01-010, S-L01-013, S-L01-029, S-L01-050, S-L01-055

### Q-color-22 · How many text colors, and are they solid or transparent? · Expert
- **Why:** Solid text colors stay crisp on any background. See-through text blends with tinted surfaces but is harder to predict [DC-L01-14].
- **Ask:** "How many text colors, and should they be solid or see-through?"
- **Example:** Show a text ladder on each surface with ratios.
- **Control:** single choice
- **Options:**
  - `solid-levels` Solid tokens per level (Carbon `$text-primary`/`$text-secondary`; Fluent `colorNeutralForeground1`) [S-L01-029, S-L01-034].
  - `opacity-levels` See-through levels (Material 2 dark: 87%, 60%, 38% white) [S-L01-055].
  - `on-colors` Plus an on-color for every bold fill (Material `on-primary`, Primer `fgColor-onEmphasis`) [S-L01-004, S-L01-027].
- **Default:** solid primary, secondary, tertiary/placeholder, disabled, inverse, plus an on-color per bold fill; secondary text passes 4.5:1 on the lowest surface it appears on. *Source:* card heuristic [DC-L01-14]; BOARD L15 note (2-3 text colors per view).
- **Decides:** DC-L01-14
- **Changes:** DC-L02-23 · blocks: Foundations > Color > Semantic roles > Foreground
- **Preview:** a text ladder on every surface tier, each with its ratio.
- **Use / avoid:** use 2-3 text colors per view; avoid placeholder-grey for anything users must read [DC-L01-14; BOARD L15 note].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-14; S-L01-004, S-L01-010, S-L01-027, S-L01-029, S-L01-055

### Q-color-23 · How strong should borders be, and what color is the focus ring? · Expert
- **Why:** Strong outlines feel clear and heavy, like a form; light borders with tinted fills feel softer. A brand-colored focus ring feels branded; a black/white ring always works [DC-L01-16].
- **Ask:** "How strong should borders be, and what color is the focus ring?"
- **Example:** Let them tab through a field, card and table.
- **Control:** single choice (borders) + single choice (focus color)
- **Options:**
  - `two-tier` Two tiers: `outline` for fields, `outline-variant` for dividers (Material) [S-L01-004].
  - `by-purpose` Border steps by purpose: decorative, field, control (Spectrum 200-300, 400, 600; Radix steps 6, 7, 8) [S-L01-036, S-L01-002].
  - `focus-brand` Brand-colored focus ring (Carbon Blue 60 in light, White in dark) [S-L01-029].
  - `focus-neutral` Black/white focus ring [DC-L01-16].
- **Default:** three border strengths (subtle decorative, default interactive at 3:1, strong) and one focus color per mode with an inset or offset ring. *Source:* card heuristic [DC-L01-16].
- **Decides:** DC-L01-16
- **Changes:** DC-L04-09, DC-L08-11, DC-L08-16 · blocks: Foundations > Color > Semantic roles > Borders and focus
- **Preview:** a text field, card and table with each border strength; tab through to see the focus ring.
- **Use / avoid:** use the 3:1 border token whenever an input's only boundary is its border; avoid decorative borders to mark interactive boundaries [DC-L01-16; S-L01-023].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-16; S-L01-002, S-L01-004, S-L01-023, S-L01-029, S-L01-036

### Q-color-24 · What color themes should we ship to help with accessibility? · Expert
- **Why:** High-contrast modes give up some brand feel to be easier to read. Forced colors swap in the user's own colors, so meaning shown only by fills or shadows is lost [DC-L01-20].
- **Ask:** "Which extra themes do you need: high contrast, color-blind, or forced colors?"
- **Example:** Show the screen in each theme.
- **Control:** multi-select (pre-filled from Q-aud-04 and Q-theme-02)
- **Options:**
  - `contrast-levels` Standard, medium (3:1 minimum) and high (7:1) contrast in light and dark (Material) [S-L01-006].
  - `increased` A version of each custom color with more contrast (Apple) [S-L01-013].
  - `high-contrast` High-contrast themes at 7:1 (Primer) [S-L01-027].
  - `cvd` Themes for people who mix up red and green, or blue and yellow (Primer) [S-L01-050].
  - `forced-colors` Parts that still work in forced colors: borders, not only fills or shadows [DC-L01-20].
- **Default:** forced-colors-safe layer always; high contrast as the first extra mode; color-blind themes for data-dense or status-heavy products. *Source:* card heuristic [DC-L01-20].
- **Decides:** DC-L01-20
- **Changes:** DC-L07-15, DC-L07-17, DC-L04-09 · blocks: Foundations > Color > Modes > Accessibility modes
- **Preview:** the preview screen in each checked theme, including a simulated forced-colors rendering.
- **Use / avoid:** use a border or icon wherever status or selection is conveyed by fill; avoid focus rings drawn only with box-shadow (forced colors removes shadows) [DC-L01-20; S-L10-031].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-20; S-L01-006, S-L01-013, S-L01-027, S-L01-048, S-L01-050

### Q-color-25 · Where are gradients allowed? · Expert
- **Why:** Gradients add energy and brand warmth. But they make busy screens less clear and compete with status colors [DC-L01-25].
- **Ask:** "Where are gradients allowed?"
- **Example:** Show a hero gradient interpolated in sRGB vs OKLab.
- **Control:** single choice
- **Options:**
  - `brand-only` Brand and marketing only, blended in OKLab (Tailwind v4 default) [S-L01-066].
  - `none` No gradients anywhere [DC-L01-25].
  - `components` Gradients on UI parts too (consumer, AI and creative products) [DC-L01-25, inferred].
- **Default:** brand-only; never on interactive components. *Source:* card heuristic [DC-L01-25].
- **Decides:** DC-L01-25
- **Changes:** DC-L05-19, DC-L06-11 · blocks: Foundations > Color > Expressive color > Gradients
- **Preview:** a hero banner with gradients interpolated in sRGB and OKLab (the sRGB one shows a gray "dead zone").
- **Use / avoid:** use a sequential palette, not a gradient, when color carries data meaning (Carbon) [S-L01-056]; avoid P3 gradients without an sRGB variant [S-L01-013].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-25; S-L01-013, S-L01-056, S-L01-066

### Q-color-26 · Should the system have see-through colors? · Expert
- **Why:** See-through (alpha) colors let hover, selection and borders pick up the color below. They then blend in on tinted surfaces and photos [DC-L01-27].
- **Ask:** "Which see-through (transparent) colors should the system have?"
- **Example:** Show hover over a white card, a tinted panel and a photo.
- **Control:** single choice
- **Options:**
  - `alpha-ramps` Alpha ramps mirroring every solid ramp (Radix `--blue-a1..a12`, blackA, whiteA) [S-L01-052].
  - `alpha-neutrals` See-through grays only (Atlassian Neutral100A-500A) [S-L01-031].
  - `media-set` See-through white and black for use over photos and video (Spectrum's 8 values) [S-L01-036].
  - `runtime` Runtime opacity via `color-mix()` (Tailwind `bg-blue-500/50`) [DC-L01-27].
- **Default:** alpha-neutrals (4-5 steps) for hover, borders and scrims; solid colors for text. *Source:* card heuristic [DC-L01-27].
- **Decides:** DC-L01-27
- **Changes:** DC-L04-17, DC-L04-18 · blocks: Foundations > Color > Primitives > Alpha colors
- **Preview:** a hover state over a white card, a tinted panel and a photo, solid vs alpha.
- **Use / avoid:** use alpha when the background varies; use solid when the pair must be contrast-certified [DC-L01-27].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-27; S-L01-030, S-L01-031, S-L01-036, S-L01-052

---

## Stage 10 · Typeface
> Screen: which fonts, for which scripts. Graph step 2-4. Cycles kept together: DC-L02-01 + DC-L02-02 + DC-L02-03 + DC-L02-04 + DC-L02-06 + DC-L02-24 (the typeface must cover your scripts and license terms, and those in turn narrow the typeface) and DC-L06-07 + DC-L06-24 (brand typeface vs localization readiness). The preview is a type specimen in the product's own UI, with a coverage bar for each chosen script.

### Q-type-01 · Should the product use the platform's font, a neutral open font, or your own brand typeface? · Quick
- **Why:** After color, the typeface may shape your brand's look the most; L09 infers this (L09 divergence 5). A system font feels native and fades away; a custom font is recognized at once [DC-L09-05].
- **Ask:** "Should it use the device's built-in font, a free plain font like Inter, or your brand font?"
- **Example:** Show the same screen in each option next to the OS chrome.
- **Control:** single choice (specimen cards)
- **Options:**
  - `system` The device's built-in font: SF Pro, Roboto, Segoe UI Variable; native, content leads (Apple, Fluent, Ant, Radix, Mantine, SLDS) [S-L02-001, S-L02-007; DC-L09-05].
  - `open-neutral` A free, plain font: the neutral SaaS look (Inter: Polaris, Chakra, Paste, Linear; Roboto: Material) [DC-L09-05].
  - `open-custom` A free font with character: IBM Plex, Geist, Public Sans, Mona Sans [DC-L09-05; S-L06-006].
  - `brand-display` Brand font for headlines, system font for body (Apple's advice) [S-L10-009, S-L06-008].
  - `brand-everywhere` Your own brand font everywhere: Uber Move, Adobe Clean, Cereal, Spotify Mix [DC-L09-05; S-L06-021, S-L06-019].
- **Default:** system for productivity and internal tools; on native platforms any brand face goes in display roles only. *Source:* card heuristics [DC-L02-01, DC-L10-06]; L09 suggests Inter or the system stack for a neutral start [DC-L09-05].
- **Decides:** DC-L09-05, DC-L02-01, DC-L06-07, DC-L10-06
- **Changes:** DC-L02-02, DC-L02-03, DC-L02-04, DC-L02-06, DC-L02-24, DC-L10-07, DC-L02-21 · blocks: Foundations > Typography > Typeface > Sourcing; Platform map
- **Preview:** the same screen set in each option, side by side with the OS chrome, so the "foreign next to OS chrome" effect is visible [DC-L02-01].
- **Use / avoid:** use system fonts when the product lives inside another OS's chrome; use a brand face when recognition is a stated goal; avoid a brand face in body text if it needs size bumps to match system legibility at 13pt [DC-L02-01, DC-L10-06].
- **Skip:** yes, system.
- **Block class:** T (tool-assisted)
- **Time weight:** high (fan-out 6)
- **Evidence:** DC-L09-05, DC-L02-01, DC-L06-07, DC-L10-06; S-L02-001, S-L02-007, S-L06-031, S-L10-009, S-L09-213
- **Merges:** K3.5, B8, P7

### Q-type-02 · Do you have the brand typeface files and a license that covers web and apps? · Standard
- **Show if:** Q-type-01 is brand-display or brand-everywhere
- **Why:** The builder cannot make a brand typeface. Its license and files decide where it may be used and how it loads [DC-L02-06; BRIEF requirement 2].
- **Ask:** "Do you have the brand font files and a license for web and apps?"
- **Example:** Ask for WOFF2 or OTF files; if none, offer 3 open-source faces with a similar feel.
- **Control:** single choice + file upload + license checkboxes (web, iOS/Android apps, embedding)
- **Options:**
  - `yes` Yes: files and license in hand.
  - `license-only` Licensed, but no files yet.
  - `no` No: see the Hook line.
- **Default:** WOFF2, one variable file per family, `font-display: swap` with a metric-adjusted fallback, subsets per script. *Source:* card heuristic [DC-L02-06].
- **Decides:** DC-L02-06
- **Changes:** DC-L02-04, DC-L02-24, DC-L10-22 · blocks: Foundations > Typography > Typeface > Delivery
- **Hook:** Accepts WOFF2 for web, OTF or TTF for native apps, variable files preferred; the builder reads axes (wght, opsz) and Unicode coverage from the file. OS system fonts must not be embedded (Apple) [S-L02-001]. If no: (1) pick an open-source face under the SIL OFL with a similar personality (Inter, Roboto Flex, Noto, Google Sans Flex, IBM Plex) [S-L02-026, S-L02-012]; (2) license a commercial face, noting per-domain, per-app or per-pageview terms [inferred]; (3) commission a custom face from a type foundry, with the caveat that it is slow and costly (Google needed three iterations to make one brand face work at small sizes) [S-L06-031].
- **Preview:** the loaded font in the specimen, with a first-load simulation showing `swap` reflow vs `optional` stability [S-L02-042].
- **Use / avoid:** use at most 2 families and 1 variable file each on first load; avoid `font-display: block` for body text (brief invisible text) [DC-L02-06; S-L02-042].
- **Skip:** yes; the system stack stands in until files arrive.
- **Block class:** T (tool-assisted)
- **Time weight:** medium (fan-out 1)
- **Evidence:** DC-L02-06; S-L02-001, S-L02-012, S-L02-026, S-L02-042, S-L06-031
- **Merges:** K3.5 (licensing), B7 (typeface licences)

### Q-type-03 · Which style of font fits the product's feel? · Standard
- **Why:** The kind of typeface sets the product's mood: neutral, friendly, warm, like a magazine, or technical [DC-L02-02, DC-L06-08].
- **Ask:** "Which font style fits best: plain, geometric, warm, serif, slab serif, or rounded?"
- **Example:** Show 'Il1 O0 rn m' at 12-14px for each candidate.
- **Control:** single choice (pre-filled from sliders F, B, A and D)
- **Options:**
  - `neo-grotesque` Plain, neutral sans: neutral, efficient, "invisible" (Inter, SF Pro, Roboto; Apple, Material, Polaris) [S-L02-049; DC-L02-02].
  - `geometric` Geometric sans: modern, friendly, fashionable, weaker in long text (DM Sans, Poppins; Google Sans lineage) [S-L02-049, S-L02-024].
  - `humanist` Warm, humanist sans: warm, approachable, very legible small (Segoe, IBM Plex Sans often grouped here) [S-L02-049].
  - `serif` Serif: editorial, heritage (Cooper for Mailchimp's sincerity) [S-L06-028].
  - `slab` Slab serif: publishing heritage, "friendly slab" [S-L06-078].
  - `rounded` Rounded letter ends: "personal, playful" (Google Sans Flex ROND axis) [S-L06-031].
- **Default:** neo-grotesque or humanist sans with a large x-height. *Source:* card heuristic [DC-L02-02]; slider mapping [DC-L06-08].
- **Decides:** DC-L02-02, DC-L06-08
- **Changes:** DC-L02-03, DC-L02-14, DC-L05-03 · blocks: Foundations > Typography > Typeface > Classification; Personality
- **Preview:** a specimen with the confusable-pairs test (Il1, O0, rn/m) at 12-14px for each candidate.
- **Use / avoid:** use geometric faces for headlines, humanist or neo-grotesque for body; avoid any face that fails the confusable-pairs test at 12-14px or lacks your scripts [DC-L02-02].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L02-02, DC-L06-08; S-L02-024, S-L02-049, S-L06-028, S-L06-031, S-L06-078

### Q-type-04 · Which languages and scripts must the product support, now and within two years? · Standard
- **Why:** Your languages can rule out a typeface, and labels need room to grow. Without a matching backup font, Hindi next to a Latin brand font looks the wrong size and sits off the baseline [DC-L02-24, DC-L06-24].
- **Ask:** "Which languages and writing systems must work now and in two years, including right to left?"
- **Example:** Show a button row in each chosen script with overflow flagged.
- **Control:** multi-select (scripts) + toggle (right-to-left)
- **Options:**
  - `latin` Latin (plus Vietnamese and extended Latin; Spotify Mix began here) [S-L06-019].
  - `indic` Indic scripts (Devanagari, Bangla, Tamil, Telugu, Gujarati): Noto Sans per script, Kohinoor on Apple, Nirmala UI on Windows [S-L02-026, S-L02-062].
  - `cjk` Chinese, Japanese, Korean: taller line heights [S-L06-101].
  - `arabic-hebrew` Arabic or Hebrew: right-to-left mirroring of layout and icons [DC-L02-24; K5.1].
  - `thai-other` Thai and other scripts with tall marks [S-L06-101].
- **Default:** Latin; for India-facing products, brand Latin face plus Noto Sans for each target Indic script with a size or x-height adjustment; every label budgets 2-3x length for strings under 10 characters. *Source:* card heuristics [DC-L02-24, DC-L06-24; S-L06-101].
- **Decides:** DC-L02-24, DC-L06-24
- **Changes:** DC-L02-25, DC-L02-13, DC-L05-09, DC-L03-04 · blocks: Foundations > Typography > Internationalization; Content > Localization
- **Preview:** the specimen and a button row rendered in each chosen script, with baseline alignment and label overflow flagged.
- **Use / avoid:** use logical (start/end) spacing and mirrored directional icons when RTL is on; avoid fixing a label width to its English length [DC-L06-24; S-L06-101].
- **Skip:** yes, Latin.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L02-24, DC-L06-24; S-L02-026, S-L02-051, S-L02-053, S-L06-101, S-L06-019
- **Merges:** K5.1, K5.2, B14

### Q-type-05 · One type family, or a pair? · Expert
- **Why:** One font family feels calm and unified. A serif or headline font as a partner adds contrast, like in a magazine [DC-L02-03].
- **Ask:** "Use one font family for everything, or pair two fonts?"
- **Example:** Show a hero and a product panel per pairing.
- **Control:** single choice
- **Options:**
  - `one` One family for everything; weights and optical sizes create contrast (Windows, Apple, Fluent, Polaris guidance) [S-L02-022, S-L02-001].
  - `superfamily` One family with display and text cuts (Google Sans + Google Sans Text; Inter Display + Inter at Linear) [S-L02-006, S-L06-012].
  - `sans-serif` Sans for UI plus a serif (Carbon: Plex Sans and Plex Serif) [S-L02-011].
  - `display-face` A separate headline font for brand moments [DC-L02-03].
- **Default:** 1 UI family + 1 mono, with an optional serif or display face for marketing. *Source:* card heuristic [DC-L02-03].
- **Decides:** DC-L02-03
- **Changes:** DC-L02-06, DC-L02-15 · blocks: Foundations > Typography > Typeface > Families and pairing
- **Preview:** a marketing hero and a product panel with each pairing.
- **Use / avoid:** add a second face only for a change of job (display vs text, code); avoid near-identical pairs that read as a mistake [DC-L02-03; L15 P49].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L02-03; S-L02-001, S-L02-006, S-L02-011, S-L02-022

### Q-type-06 · Which font for code and numbers? · Expert
- **Why:** A code font (mono) looks technical. Digits that are all the same width (tabular figures) keep numbers still in tables and live values [DC-L02-05; S-L02-052].
- **Ask:** "Which font for code and numbers, and should table digits all be the same width?"
- **Example:** Show a live counter with proportional vs tabular digits.
- **Control:** single choice + toggle (tabular numbers in tables)
- **Options:**
  - `system-mono` System mono stack (`ui-monospace, SFMono-Regular, ...`: Primer, Polaris) [S-L02-017, S-L02-014].
  - `brand-mono` A brand code font (IBM Plex Mono code-01 12/16; Atlassian Mono) [S-L02-011, S-L02-015].
  - `numeric-face` A style just for key numbers (Fluent Bahnschrift; Atlassian font.metric.large 28/32) [S-L02-008, S-L02-015].
- **Default:** system mono stack plus `tabular-nums` on numeric table cells; a metric style only if the product has dashboards. *Source:* card heuristic [DC-L02-05].
- **Decides:** DC-L02-05, DC-L02-26
- **Changes:** DC-L02-26, DC-L05-24 · blocks: Foundations > Typography > Typeface > Monospace / numeric
- **Preview:** a code block, a table column and a live counter with proportional vs tabular figures.
- **Use / avoid:** use tabular figures in tables, clocks and anything that updates; avoid mono for body text [DC-L02-05; S-L02-052].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L02-05; S-L02-008, S-L02-011, S-L02-014, S-L02-015, S-L02-052

### Q-type-07 · Should the font use in-between weights and reshape letters for each size? · Expert
- **Why:** Optical sizing makes small text sturdier and large text sleeker. Without it, big headings set in the body version of a font look clunky [DC-L02-04].
- **Ask:** "If the font allows, should it use in-between weights and reshape letters for each size?"
- **Example:** Show 11px to 64px with opsz on and off.
- **Control:** single choice
- **Options:**
  - `static` Static fonts, set weights only (Roboto as applied by M3 components) [S-L02-053].
  - `variable-wght` Variable weight, with in-between weights (Polaris 450/550/650) [S-L02-014].
  - `variable-opsz` Variable weight plus optical size tied to font size (SF Pro, Segoe UI Variable 8-36pt, Inter opsz 14-32; Material sets opsz = font size) [S-L02-001, S-L02-022, S-L02-026].
- **Default:** variable-opsz when the face has it; otherwise separate display tracking and line-height values above about 24px. *Source:* card heuristic [DC-L02-04].
- **Decides:** DC-L02-04
- **Changes:** DC-L02-14, DC-L02-15, DC-L02-06 · blocks: Foundations > Typography > Typeface > Variable axes
- **Preview:** a size ramp from 11px to 64px with opsz on and off.
- **Use / avoid:** use opsz tied to size; avoid setting display sizes in a text cut without tracking adjustments [DC-L02-04, DC-L02-14].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L02-04; S-L02-001, S-L02-014, S-L02-022, S-L02-026, S-L02-053

---

## Stage 11 · Type scale and text
> Screen: sizes, line heights, weights and text behavior, on a live type ladder next to a real product screen. Graph step 0-5. Cycle kept together: DC-L02-13 + DC-L02-25 (line heights must fit each script's height category, and script metrics are set relative to the line-height system). Mostly pre-filled from Q-aud-01 (density) and Q-dir-03 (hierarchy strength).

### Q-type-08 · What size should body text be? · Standard
- **Why:** Body text size sets how packed the text feels. 13-14px reads dense, like a "pro tool"; 16-17 reads comfortable and easy [DC-L02-08].
- **Ask:** "What size should body text be?"
- **Example:** Show a form and a paragraph at 14, 16 and 17.
- **Control:** single choice per platform (pre-filled from Q-aud-01)
- **Options:**
  - `13` 13px (Polaris text-body-md 13/20) [S-L02-014].
  - `14` 14px (Material Body Medium 14/20, Fluent, Carbon productive, Atlassian, Primer) [S-L02-006, S-L02-007, S-L02-011, S-L02-015].
  - `16` 16px (Carbon expressive, Material Body Large 16/24) [S-L02-011, S-L02-005].
  - `17` 17pt (iOS Body) [S-L02-001].
  - `19` 19px (GOV.UK) [DC-L09-04].
- **Default:** web app 14px UI body with 16px for long-form reading; iOS 17pt; Android 14sp Body Medium / 16sp Body Large. *Source:* platform convention and card heuristic [DC-L02-08]; L09 shared default row 8.
- **Decides:** DC-L02-08
- **Changes:** DC-L02-09, DC-L02-13, DC-L02-17, DC-L03-07 · blocks: Foundations > Typography > Type scale > Base size
- **Preview:** a settings form and an article paragraph at each size; the table on the preview shows rows per screen.
- **Use / avoid:** use 16px or more where users mostly read paragraphs; use 14px where they mostly operate controls and tables; avoid anything people must read below 12px on web or 11pt on mobile [DC-L02-08, DC-L02-20].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L02-08; S-L02-001, S-L02-005, S-L02-006, S-L02-011, S-L02-014
- **Merges:** K7.2 (sizes)

### Q-type-15 · Should text sizes change with screen width? · Expert
- **Why:** Fixed sizes look steady and app-like. Big headings that grow with the screen fill wide hero banners smoothly [DC-L02-19].
- **Ask:** "Should text sizes change with screen width?"
- **Example:** Drag the preview width; watch the hero and a card heading.
- **Control:** single choice
- **Options:**
  - `fixed` Fixed everywhere; rely on the OS text-size setting (Carbon productive, Windows, iOS) [S-L02-011, S-L02-022, S-L02-001].
  - `stepped` Steps up at set screen widths (Carbon expressive at md, lg, xlg, max) [S-L02-011].
  - `fluid` Fluid headline sizes using clamp(), within the 2.5x zoom rule [S-L02-028; DC-L02-19].
- **Default:** fixed body and UI text; fluid or stepped only for display and headline styles on the web. *Source:* card heuristic [DC-L02-19].
- **Decides:** DC-L02-19
- **Changes:** DC-L03-17, DC-L07-28 · blocks: Foundations > Typography > Responsive type > Strategy
- **Preview:** a hero and a card heading as the preview width is dragged.
- **Use / avoid:** use fluid type for marketing heroes; avoid fluid styles inside cards, tables or forms [DC-L02-19; S-L02-011].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L02-19; S-L02-011, S-L02-022, S-L02-028

### Q-type-17 · How far must layouts support users' larger-text settings? · Standard
- **Why:** At the largest text settings, sizes bunch together and layouts must restack. On iOS at AX5, Body is 53pt and Large Title only 60pt [DC-L02-21; S-L02-001].
- **Ask:** "When people turn up text size on their device, how far should layouts grow with it?"
- **Example:** Show a list row at default, 200% and AX5.
- **Control:** single choice
- **Options:**
  - `full` Full scaling, no cap on body text: iOS AX1-AX5, Android nonlinear to 200%, web rem [S-L10-011, S-L10-071, S-L10-074].
  - `capped-chrome` Full for content, capped at about 1.5x for fixed parts like tab labels [DC-L10-07].
  - `none` No scaling support: fails platform guidance (Apple asks for at least 200%) [S-L10-012].
- **Default:** capped-chrome, with every text token in scalable units and no fixed-height text containers. *Source:* platform convention and accessibility rule [DC-L10-07, DC-L02-21].
- **Decides:** DC-L02-21, DC-L10-07
- **Changes:** DC-L03-07, DC-L05-05, DC-L08-07 · blocks: Foundations > Typography > Scaling
- **Preview:** a list row and a tab bar at default, 200% and AX5, restacking live.
- **Use / avoid:** use containers that grow with text; avoid truncating at the largest sizes [DC-L02-21, DC-L10-07].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L02-21, DC-L10-07; S-L02-001, S-L10-011, S-L10-012, S-L10-071, S-L10-074
- **Merges:** P8, K4.4 (text scaling)

### Q-type-09 · Which ratio should generate the size scale? · Expert
- **Why:** The ratio decides how many text sizes you can use and how much they differ [DC-L02-09].
- **Ask:** "How much bigger should each text size be than the one below it?"
- **Example:** Show the ladder recomputed; close steps flagged.
- **Control:** single choice + manual override per step
- **Options:**
  - `1.125` 1.125 major second: 16, 18, 20, 23, 26, 29 (Material: "Major Second type scale with 14 as its key base size") [S-L02-006].
  - `1.2` 1.2 minor third: 16, 19, 23, 28, 33, 40 [DC-L02-09].
  - `1.25` 1.25 major third: 16, 20, 25, 31, 39, 49 [DC-L02-09].
  - `1.333` 1.333 perfect fourth and above: editorial [DC-L02-09].
  - `hand-tuned` Hand-tuned list (11-15 named styles in 12 systems; only Carbon and Ant use a formula) [L09 A1 row 8].
- **Default:** ratio from Q-dir-03, rounded to even pixels, then hand-adjusted; 1.125-1.2 dense apps, 1.25 mixed, 1.333+ editorial. *Source:* card heuristic [DC-L02-09]. Golden ratio is offered only as an optional preset (weak evidence) [BOARD L15 note].
- **Decides:** DC-L02-09
- **Changes:** DC-L02-10, DC-L02-13 · blocks: Foundations > Typography > Type scale > Generation
- **Preview:** the ladder recomputed live; adjacent steps closer than about 10% are flagged for merging.
- **Use / avoid:** use a formula to start and hand-tune the result; avoid keeping two sizes that differ by less than about 10% [DC-L02-10].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L02-09; S-L02-006, S-L02-060, S-L09-213

### Q-type-10 · How many text styles, and how are they named? · Expert
- **Why:** Styles named for their job help people pick by purpose and stop one-off sizes. Too many sizes blur what matters most [DC-L02-07, DC-L02-10].
- **Ask:** "How many text styles, and how should they be named?"
- **Example:** Show styles used in context: page title, card title, label.
- **Control:** single choice (naming) + number (styles)
- **Options:**
  - `role-size` Role x size matrix: display, headline, title, body, label x large, medium, small (Material 15 styles) [S-L02-052].
  - `named` Named semantic styles (Apple's 11: Large Title ... Caption 2; Primer) [S-L02-001, S-L02-017].
  - `tshirt` Category plus t-shirt sizes, easy to extend (Atlassian heading.xxlarge ... ) [S-L02-015].
- **Default:** role x size matrix plus code, 8-10 sizes and 12-15 styles (13 in the L09 preset). *Source:* card heuristics [DC-L02-07, DC-L02-10]; L09 shared default row 8.
- **Decides:** DC-L02-07, DC-L02-10
- **Changes:** DC-L02-27, DC-L07-12, DC-L13-04 · blocks: Foundations > Typography > Type roles; Type scale > Step count
- **Preview:** the style list with each style used in context (page title, card title, button label, caption).
- **Use / avoid:** name semantic styles by job and primitives by number; avoid more than about 3 type sizes in a single view [DC-L02-07; BOARD L15 note].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L02-07, DC-L02-10; S-L02-001, S-L02-005, S-L02-006, S-L02-015, S-L02-017

### Q-type-11 · How should line heights be set? · Expert
- **Why:** Tight line height makes headings look solid, and 1.4-1.6 keeps paragraphs easy to follow. Line heights set for Latin clip the marks of Indic and Telugu text [DC-L02-13, DC-L02-25].
- **Ask:** "How should line height, the space between lines, be set for each writing system?"
- **Example:** Show a paragraph in Latin and Devanagari with clipping flagged.
- **Control:** single choice + table of script categories
- **Options:**
  - `4pt` Fixed values snapped to 4pt (Material Body Large 16/24; Atlassian; Polaris) [S-L02-005, S-L02-015, S-L02-014].
  - `2pt` Fixed values on a 2pt grid (Fluent, Carbon) [S-L02-007, S-L02-011].
  - `ratios` Named ratios of the font size (Primer tight 1.25 to loose 1.75) [DC-L02-13].
  - `script-heights` Plus extra height for taller scripts: Medium about +7% (Arabic, Hindi, CJK, Thai), Large +30% (Telugu, Burmese), Extra large +100% (Nastaliq) (Material 3) [S-L02-006].
- **Default:** ratio-derived and rounded to 4px: about 1.5 for 12-16px, 1.4 for 18-24px, 1.25 for 28-40px, 1.1-1.15 for 48px+; Medium height for Indic and CJK, Large for Telugu and Burmese; no italics or all caps for non-Latin scripts. *Source:* card heuristics [DC-L02-13, DC-L02-25].
- **Decides:** DC-L02-13, DC-L02-25
- **Changes:** DC-L02-16, DC-L03-25, DC-L03-07 · blocks: Foundations > Typography > Metrics > Line height; Internationalization > Script metrics
- **Preview:** a paragraph and a two-line button label in Latin and each chosen script, with clipping flagged.
- **Use / avoid:** use smaller ratios as text gets larger; avoid fixed-height components that hold text [DC-L02-13, DC-L02-25].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L02-13, DC-L02-25; S-L02-005, S-L02-006, S-L02-007, S-L02-011, S-L02-015

### Q-type-12 · Which font weights, and how is emphasis shown? · Expert
- **Why:** Headings that stand out by size, in regular weight, look elegant and editorial. Headings that stand out by being bold look sturdy and product-like [DC-L02-15].
- **Ask:** "Which font weights, and how should important text stand out?"
- **Example:** Show headings and a selected chip in each weight set.
- **Control:** single choice (weights) + single choice (emphasis)
- **Options:**
  - `two` Two weights: Regular and Semibold (Windows 11) [S-L02-022].
  - `three` Three weights (Carbon 300/400/600; Material 400/500/700; Atlassian Regular/Medium/Bold) [S-L02-012, S-L02-005, S-L02-015].
  - `four` Four weights (Fluent 400-700; Primer 300-600) [S-L02-008, S-L02-017].
  - `emphasized-twin` One bolder twin per style (Material Expressive 400 to 500, 500 to 700) [S-L02-005, S-L02-006].
  - `strong-stronger` Strong and Stronger variants (Fluent Body 1 400/600/700) [S-L02-007].
- **Default:** 3 weights (400 body, 500-600 labels, 600-700 headings) and one emphasized weight per style. *Source:* card heuristics [DC-L02-15, DC-L02-12]; BOARD L15 note (2 weights per view).
- **Decides:** DC-L02-15, DC-L02-12
- **Changes:** DC-L02-06 (files to load), DC-L08-14 · blocks: Foundations > Typography > Metrics > Weights; Type roles > Emphasis
- **Preview:** headings and a selected chip in each weight set.
- **Use / avoid:** use weight first, color second, italics only inside running text; avoid light (300) below 32px [DC-L02-12, DC-L02-15].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L02-15, DC-L02-12; S-L02-005, S-L02-007, S-L02-012, S-L02-022

### Q-type-13 · Should letter spacing change with size? · Expert
- **Why:** Tighter letter spacing makes headlines look strong and sure. Looser spacing helps small text and all-caps labels [DC-L02-14].
- **Ask:** "Should letter spacing change with text size, or stay as the font sets it?"
- **Example:** Show a headline and an all-caps label with tracking on and off.
- **Control:** single choice
- **Options:**
  - `size-table` A size-specific table (SF Pro: +41/1000 em at 6pt, 0 at 12pt, -26/1000 em at 17pt), applied automatically by the OS [S-L02-001].
  - `per-style` Per-style tracking tokens (Material: Display Large -0.2sp, Body Large 0.5sp) [S-L02-005].
  - `zero` No extra letter spacing beyond the font's defaults [DC-L02-14].
- **Default:** 0 at body sizes, +0.02 to +0.05em at 11-12px and all caps, -0.01 to -0.02em from about 32px, in em units. *Source:* card heuristic [DC-L02-14].
- **Decides:** DC-L02-14
- **Changes:** DC-L07-12 · blocks: Foundations > Typography > Metrics > Letter spacing
- **Preview:** a headline and an all-caps label with tracking on and off.
- **Use / avoid:** use em-based tracking so it scales; let optical-size fonts do most of the work; avoid tracking non-Latin scripts [DC-L02-14, DC-L02-25].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L02-14; S-L02-001, S-L02-005, S-L02-009, S-L02-021

### Q-type-14 · How should body text be laid out: line length, alignment, cut-off text and spacing? · Expert
- **Why:** Very long lines make readers lose their place. Centered or justified text (stretched to both edges) slows reading [DC-L02-17, DC-L02-18].
- **Ask:** "How wide can paragraphs get, and how should long text be cut off?"
- **Example:** Let them drag a width handle on an article.
- **Control:** number (max characters per line) + single choice (overflow) + number (paragraph spacing)
- **Options:**
  - `measure-45-75` 45-75 characters (Bringhurst) or 50-60 (Windows); WCAG 1.4.8 AAA caps at 80, 40 for CJK [S-L02-051, S-L02-022, S-L02-029].
  - `wrap-then-ellipsis` Wrap first, then cut off with an ellipsis (...) and a way to read it all [DC-L02-18].
  - `para-1x` Paragraph spacing equal to the body size (Atlassian body 12px, body large 16px) [S-L02-015; DC-L02-16].
  - `text-box-trim` Trim half-leading so spacing measures from cap height (CSS `text-box: trim-both`) [DC-L02-16].
- **Default:** max prose width about 65-70ch (35-40 characters CJK), start-aligned, wrap then ellipsis, paragraph spacing 1x body size with twice as much space above a heading as below it. *Source:* card heuristics [DC-L02-17, DC-L02-18, DC-L02-16].
- **Decides:** DC-L02-17, DC-L02-18, DC-L02-16
- **Changes:** DC-L03-16, DC-L03-25 · blocks: Foundations > Typography > Layout of text
- **Preview:** an article at the chosen measure with a width handle to drag; lines over the limit highlight.
- **Use / avoid:** constrain the container before touching font size when lines exceed about 10-12 words; avoid full justification and centered paragraphs [DC-L02-17, DC-L02-18].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L02-17, DC-L02-18, DC-L02-16; S-L02-015, S-L02-022, S-L02-029, S-L02-051

### Q-type-16 · Should type sizes differ by platform or viewing distance? · Expert
- **Show if:** more than one platform or device class
- **Why:** Phone text about 1.2x the desktop size makes up for touch and distance. TVs and cars need text scaled to how far away people sit [DC-L02-20, DC-L14-04].
- **Ask:** "Should text sizes change by device or by how far away people sit?"
- **Example:** Show one screen at phone, desktop and TV.
- **Control:** single choice
- **Options:**
  - `platform-modes` One semantic scale with platform modes (Spectrum 2: 14px desktop, 17px mobile) [S-L02-021].
  - `per-platform` Per-platform ramps (Fluent: web Body 1 14/20, iOS 17/22, Android 16/24, macOS 13/16) [S-L02-007].
  - `native-units` One scale in each platform's own units (Material) [DC-L02-20].
  - `distance-modes` Sizes by viewing distance, from native defaults (Apple watch 16, phone 17, Mac 13, TV 29 pt) [S-L14-012].
- **Default:** one semantic scale with platform modes, mobile about 1.15-1.2x desktop, plus distance modes for TV, car and spatial. *Source:* card heuristics [DC-L02-20, DC-L14-04].
- **Decides:** DC-L02-20, DC-L14-04
- **Changes:** DC-L14-13, DC-L07-15 · blocks: Foundations > Typography > Responsive type > Platform scales; Distance classes
- **Preview:** the same screen at phone, desktop and TV with type scaled to a similar visual angle.
- **Use / avoid:** keep roles and roughly the visual angle when moving to a farther device; avoid reusing desktop sizes on phones [DC-L14-04, DC-L02-20].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L02-20, DC-L14-04; S-L02-007, S-L02-021, S-L14-012, S-L14-026

---

## Stage 12 · Space, sizing and density
> Screen: the spacing scale, target sizes and control heights, shown on a live component sheet with spacing overlays (padding in one tint, gaps in another). Graph step 0-6. Pre-filled from Q-aud-01, Q-plat-03 and Q-dir-02.

### Q-space-01 · What should the base spacing unit be? · Standard
- **Why:** The base unit sets the smallest step you can see between two spacings. 8 gives chunky, calm steps; 4 gives finer control [DC-L03-01].
- **Ask:** "What base unit should all spacing be built from, like 4 or 8 pixels?"
- **Example:** Show spacing overlays on a card and form.
- **Control:** single choice
- **Options:**
  - `4-grid-8-rhythm` 4 as the grid, 8 as the rhythm: named on an 8 base with 2, 4, 6, 12 kept for internals (Material 3, Atlassian, Spectrum) [S-L03-030, S-L03-003, S-L03-044].
  - `4` 4 throughout (Fluent 2, Polaris, Primer, Tailwind `--spacing: 0.25rem`) [S-L03-010, S-L03-005, S-L03-009, S-L03-017].
  - `8` 8 with few sub-steps (Carbon's 8px mini unit) [S-L03-002].
  - `rem-16` 16px rem-based (Bootstrap `$spacer: 1rem`) [DC-L03-01].
- **Default:** 4-grid-8-rhythm. *Source:* L09 shared default row 2 (4px base, 17 of 22 systems contain the 4-64 ladder) and card heuristic [L09 A1; DC-L03-01].
- **Decides:** DC-L03-01
- **Changes:** DC-L03-02, DC-L03-03, DC-L03-06, DC-L03-07, DC-L03-15 · blocks: Foundations > Space > Base unit
- **Preview:** a card, form and toolbar with spacing overlays; hovering any gap shows its token and value.
- **Use / avoid:** use the 2/4/6 sub-steps inside components (icon-to-label, chip padding); avoid them between layout sections [DC-L03-01, DC-L03-04].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L03-01; S-L03-002, S-L03-003, S-L03-010, S-L03-030, S-L03-044
- **Merges:** K7.3 (space)

### Q-space-02 · How should spacing steps grow? · Standard
- **Why:** Steps that grow in bigger jumps (hybrid or doubling) make levels of spacing easy to see at a glance. Even steps that sit close together get used in mixed-up ways [DC-L03-02; S-L03-039].
- **Ask:** "How should spacing steps grow: small then big jumps, even steps, or doubling?"
- **Example:** Show the scale as bars mapped to where each is used.
- **Control:** single choice + editable step list
- **Options:**
  - `hybrid` Fine at the bottom, coarse at the top: 0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80 (Atlassian's exact set; Carbon similar to 160) [S-L03-003, S-L03-001].
  - `linear` Even 4px steps (Tailwind open-ended, Fluent to 56, Primer to 48) [S-L03-015, S-L03-010, S-L03-009].
  - `geometric` Doubling: 2, 4, 8, 16, 32, 64 (Curtis: linear offers "too many choices too close together") [S-L03-039].
- **Default:** hybrid, 12-15 steps. *Source:* card heuristic [DC-L03-02]; L09 shared default row 2 (0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96).
- **Decides:** DC-L03-02
- **Changes:** DC-L03-03, DC-L03-04, DC-L03-11, DC-L03-24 · blocks: Foundations > Space > Spacing scale
- **Preview:** the scale as bars; dragging a step shows where it is used on the component sheet.
- **Use / avoid:** keep adjacent steps at least about 25% apart above 8px so the difference is visible; avoid adding steps nobody can tell apart [DC-L03-02].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L03-02; S-L03-001, S-L03-003, S-L03-009, S-L03-039

### Q-space-03 · How big must tap and click targets be? · Standard
- **Why:** Touch target size is a floor for accessibility (WCAG 2.5.8), and it sets how far apart controls sit. A control may look smaller when dense, but its tap area never shrinks [DC-L03-12].
- **Ask:** "How big must tap and click targets be?"
- **Example:** Show hit areas and the 24px-circle test on a toolbar.
- **Control:** single choice (pre-filled from Q-plat-03 and Q-aud-03)
- **Options:**
  - `web-24-44` Web: 24px visual minimum, 44px hit area on touch (`pointer: coarse`) [S-L03-035; DC-L03-12].
  - `ios-44` iOS 44x44pt (visionOS 60, tvOS 66, macOS 28) [S-L03-033, S-L03-034].
  - `android-48` Android 48x48dp, even for small icon buttons [S-L03-029, S-L03-058].
  - `vehicle-76` Vehicle 76x76dp (Design for Driving), 64dp parked [S-L14-037, S-L14-032].
- **Default:** keyed to input, not device: the largest input the device supports; gaps of 8px between controls on desktop and 12px on touch; two sub-24px targets never closer than 24px center to center. *Source:* platform convention and accessibility rule [DC-L14-03, DC-L03-13, DC-L03-12].
- **Decides:** DC-L03-12, DC-L14-03, DC-L03-13
- **Changes:** DC-L03-07, DC-L08-07, DC-L05-05 · blocks: Foundations > Sizing > Targets; Space > Target spacing
- **Preview:** hit areas drawn around every control; the 24px-circle test from WCAG 2.5.8 runs live on a dense toolbar.
- **Use / avoid:** decouple hit area from visual size (padding, pseudo-elements); avoid shrinking hit areas in compact mode [DC-L03-12; S-L03-035].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L03-12, DC-L14-03, DC-L03-13; S-L03-029, S-L03-033, S-L03-035, S-L14-037

### Q-space-09 · Who controls density, and how is it stored? · Expert
- **Why:** Letting users pick density can change the layout, not just the padding. In Salesforce's compact mode, labels move beside their fields [DC-L03-10; S-L03-070].
- **Ask:** "Who decides how packed or roomy the screens are, and how is that choice saved?"
- **Example:** Toggle a table between modes; targets stay fixed.
- **Control:** single choice (who) + single choice (storage)
- **Options:**
  - `fixed` Fixed density, no setting (most consumer and marketing systems) [DC-L03-10].
  - `size-props` Designers pick a size for each component (Carbon, Fluent, Primer) [S-L03-042, S-L03-046, S-L03-009].
  - `user-global` Each person picks a density for the whole app (Salesforce comfy/cozy/compact, Gmail) [S-L03-070].
  - `semantic-mode` Stored as its own token mode, apart from screen sizes and color themes. Base values and minimum targets stay the same [DC-L03-11].
  - `per-device` Density follows viewing distance and input per device class ("a 65-inch TV is a far-away phone") [DC-L14-13; S-L14-026].
- **Default:** consumer: fixed comfortable; enterprise and data: size props plus a user compact mode that shrinks insets, stacks and row heights by one step (about 4px); stored as a semantic mode. *Source:* card heuristics [DC-L03-10, DC-L03-11, DC-L14-13].
- **Decides:** DC-L03-10, DC-L03-11, DC-L14-13
- **Changes:** DC-L07-15, DC-L07-17 · blocks: Foundations > Space > Density; Density > Modes; Density by context
- **Preview:** a data table toggled between modes; target outlines stay fixed while padding shrinks.
- **Use / avoid:** use a compact mode for tables, lists, menus and trees; avoid a type-only density mode that leaves oversized padding [DC-L03-11; S-L03-070].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L03-10, DC-L03-11, DC-L14-13; S-L03-042, S-L03-057, S-L03-070, S-L14-026
- **Merges:** K6.3 (density modes, mechanism)

### Q-space-04 · How tall should buttons and inputs be? · Standard
- **Why:** Control height sets the feel: 32px reads as a desktop work tool, 40-48px as touch-friendly, and 56dp+ as expressive [DC-L03-07].
- **Ask:** "How tall should buttons and inputs be?"
- **Example:** Show a toolbar mixing controls at each height.
- **Control:** single choice (pre-filled from Q-dir-02)
- **Options:**
  - `pointer-24-32-40` sm 24, md 32, lg 40: pointer-first desktop tools (Fluent inputs 24/32/40, 32 default) [S-L03-046].
  - `touch-32-40-48` sm 32, md 40, lg 48: touch-inclusive (Carbon S/M/L; "large 48px is the most common button size in software products") [S-L03-042, S-L03-082].
  - `expressive-m3` XS 32, S 40, M 56, L 96, XL 136dp, round or square, morphing when pressed (M3 Expressive) [S-L08-102].
- **Default:** touch-32-40-48 for touch-inclusive products, pointer-24-32-40 for desktop tools; one shared height scale for every inline control; derive height as line box plus twice the block padding. *Source:* card heuristics [DC-L03-07, DC-L08-07, DC-L03-05].
- **Decides:** DC-L03-07, DC-L08-07
- **Changes:** DC-L04-03, DC-L08-16, DC-L05-05 · blocks: Foundations > Sizing > Control heights; Components > Sizing
- **Preview:** a toolbar mixing a button, input, select and segmented control at each size; mismatched heights are flagged.
- **Use / avoid:** keep sizes on multiples of 8 and never mix sizes in one group; avoid heights below the target floor without padded hit areas [DC-L08-07, DC-L03-12].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L03-07, DC-L08-07; S-L03-042, S-L03-046, S-L08-061, S-L08-062, S-L08-102

### Q-space-05 · How much breathing room between groups versus inside them? · Standard
- **Why:** Much more space between groups than inside them (8px inside, 32px between) looks clear and premium. Too little difference looks cramped and unclear [DC-L03-24].
- **Ask:** "How much more space between groups than inside them?"
- **Example:** Drag the inner:outer slider on a settings page.
- **Control:** slider (inner:outer ratio)
- **Options:**
  - `1:2` 1:2, the minimum for clear grouping [DC-L03-24, DC-L15-05].
  - `1:3-1:4` 1:3 to 1:4: airy brands, generous margins ("spacious layouts feel calm and open", Material) [S-L03-028].
  - `dense` Dense sections inside an uncrowded page (Carbon: "the whole page should not be crowded") [S-L03-001].
- **Default:** 1:2, or 1:3-1:4 when Q-dir-02 is spacious. *Source:* card heuristic [DC-L03-24]; BOARD L15 note (inner gaps smaller than outer gaps, enforced by construction).
- **Decides:** DC-L03-24
- **Changes:** DC-L03-04, DC-L08-15 · blocks: Foundations > Space > Whitespace and hierarchy
- **Preview:** a settings page with the slider live; groups that read as one block are outlined.
- **Use / avoid:** use space as the default grouping cue; add borders only where interactivity or scanning needs them [DC-L03-24].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L03-24; S-L03-001, S-L03-028, S-L03-061

### Q-space-06 · How should spacing be grouped by what it is used for? · Expert
- **Why:** Naming spacing by its job puts the same padding in every card and the same gap between every field. That repeat reads as rhythm [DC-L03-04; S-L03-028].
- **Ask:** "How should spacing values be grouped by their job?"
- **Example:** Show inset shapes on a card, button and input.
- **Control:** single choice + table (inset shapes)
- **Options:**
  - `curtis` Inset, squish inset, stretch inset, stack, inline, grid (EightShapes) [S-L03-039].
  - `material` Padding, gap, margin; "use padding and gaps before margins" (Material 3) [S-L03-030].
  - `layout-component` Keep spacing inside parts separate from page spacing (Carbon) [S-L03-001].
  - `insets` Padding shapes: square for cards and dialogs, squish (vertical about half of horizontal) for buttons and rows, stretch for inputs [S-L03-039, S-L03-046; DC-L03-05].
- **Default:** three families (inset, gap, layout); parents own spacing and children never set outer margins; squish for pill-like controls, stretch for inputs only. *Source:* card heuristics [DC-L03-04, DC-L03-05].
- **Decides:** DC-L03-04, DC-L03-05
- **Changes:** DC-L03-03, DC-L07-04 · blocks: Foundations > Space > Semantic spacing; Inset
- **Preview:** a card, button and input with each inset shape overlaid.
- **Use / avoid:** use padding and gap on parents; avoid margins on reusable components [DC-L03-04; S-L03-030].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L03-04, DC-L03-05; S-L03-001, S-L03-030, S-L03-039, S-L03-046

### Q-space-07 · Do you need tiny nudges and negative spacing? · Expert
- **Why:** Tiny steps fix things that look out of line, like icons that seem off-center. Negative spacing lets things overlap, like a stack of avatars [DC-L03-06].
- **Ask:** "Do you need tiny steps for small fixes, and negative spacing for overlaps?"
- **Example:** Show an icon-label pair and an avatar stack.
- **Control:** multi-select
- **Options:**
  - `nudges` Nudge steps 2, 6, 10 (Fluent; Material nested units) [S-L03-010, S-L03-030].
  - `hairline` 1px step (Spectrum `spacing-25`, Polaris `space-025`) [S-L03-044, S-L03-005].
  - `negatives` Negative steps -2 to -32 (Atlassian, Primer) [S-L03-003, S-L03-009].
- **Default:** 2, 4, 6 (10 only if the icon set needs it), negatives mirroring positives up to 32; 1px reserved for borders, not spacing. *Source:* card heuristic [DC-L03-06].
- **Decides:** DC-L03-06
- **Changes:** DC-L07-03 · blocks: Foundations > Space > Fine and negative
- **Preview:** an icon-label pair and an avatar stack with and without nudges.
- **Use / avoid:** use negatives for deliberate overlaps; avoid using nudges to patch layout bugs [DC-L03-06, inferred].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L03-06; S-L03-003, S-L03-005, S-L03-010, S-L03-030

### Q-space-08 · How should spacing above and below text stay even? · Expert
- **Why:** Extra space inside the line height can make padding look uneven, with more at the top than the bottom [DC-L03-25; S-L03-039].
- **Ask:** "How should we keep spacing above and below text looking even?"
- **Example:** Measure a button's top and bottom padding, trim on and off.
- **Control:** single choice
- **Options:**
  - `box-based` Measure spacing from the text box; spacers snap to the text box (Carbon) [S-L03-002].
  - `baseline` A baseline grid (lines all text sits on) for multi-column pages (Fluent) [S-L03-010].
  - `trim` Trim line-height with CSS `text-box` as progressive enhancement [S-L03-077, S-L03-039].
- **Default:** snap line heights and spacing to 4px, measure from the text box, `text-box` trim as enhancement; content must survive WCAG 1.4.12 text-spacing overrides. *Source:* card heuristic [DC-L03-25]; accessibility rule [DC-L02-22].
- **Decides:** DC-L03-25
- **Changes:** DC-L02-16 · blocks: Foundations > Space > Vertical rhythm
- **Preview:** a button and card with the top and bottom padding measured, trim on and off.
- **Use / avoid:** use a strict baseline grid only for multi-column editorial pages; avoid it for app UI on the web [DC-L03-25].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L03-25; S-L03-002, S-L03-010, S-L03-039, S-L03-077

### Q-space-10 · Which icon and avatar sizes should exist? · Expert
- **Why:** Icons sized to the line height sit level with their labels. Bigger icons make the product feel friendlier and more like a consumer app [DC-L03-08].
- **Ask:** "Which icon and avatar sizes should exist?"
- **Example:** Show icon-label pairs at each text size.
- **Control:** editable size lists
- **Options:**
  - `icons-16-32` Icons 16/20/24/32 (Carbon: 16 and 20 pair with 14 and 16px text) [S-L03-062].
  - `platform-scaled` Icon sizes per platform (Spectrum desktop 14-26, mobile 16-30) [S-L03-044].
  - `button-sized` Icon sized to the button size (Material Expressive 20-40dp for XS-XL) [S-L03-059].
  - `avatars` Avatars 16/20/24/32/40/48/64 (Primer) [S-L03-063].
- **Default:** icons 16/20/24/32, avatars 16-64 as Primer; icon size = body line height minus 0-4px. *Source:* card heuristic [DC-L03-08].
- **Decides:** DC-L03-08
- **Changes:** DC-L05-05, DC-L05-18 · blocks: Foundations > Sizing > Media sizes
- **Preview:** icon-label pairs at each text size, and an avatar row.
- **Use / avoid:** keep the icon-to-text ratio fixed ("Don't alter the icon-text size ratio", Carbon) [S-L03-062]; avoid in-between icon sizes that blur the pixel grid [inferred].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L03-08; S-L03-044, S-L03-059, S-L03-062, S-L03-063

---

## Stage 13 · Layout, navigation and app shell
> Screen: how pages reorganize across widths, shown on a resizable frame the person can drag from phone to wide desktop. Graph step 0-4. Safe areas and edge insets (DC-L03-20, DC-L14-10) are not asked; they are platform rules applied by construction (see "Auto-applied rules").

### Q-layout-01 · At which widths should layouts reorganize? · Standard
- **Why:** At each breakpoint the layout changes: panes appear, the menu swaps and columns double [DC-L03-14].
- **Ask:** "Which breakpoints, the screen widths where the layout changes, should you use?"
- **Example:** Drag the frame across 600, 840 and 1200; show navigation swapping from bar to rail.
- **Control:** single choice + editable values
- **Options:**
  - `material` Material width breakpoints 600 / 840 / 1200 / 1600dp plus height classes 480 / 900 (Android and web) [S-L03-025, S-L03-021].
  - `tailwind` Tailwind 640 / 768 / 1024 / 1280 / 1536 (web-only products) [S-L03-016].
  - `bootstrap` Bootstrap 576 / 768 / 992 / 1200 / 1400 [S-L03-018].
  - `apple-size-classes` Apple size classes, compact or regular for width and height, set by the system [S-L03-032].
- **Default:** material for cross-platform products, tailwind for web-only; web values in rem; design compact first. *Source:* card heuristic [DC-L03-14]; BOARD L03 note (Material renamed window size classes to breakpoints, May 2026).
- **Decides:** DC-L03-14
- **Changes:** DC-L03-15, DC-L03-16, DC-L03-17, DC-L03-18, DC-L03-19, DC-L07-28 · blocks: Foundations > Layout > Breakpoints
- **Preview:** the resizable frame with breakpoint ticks; the layout snaps at each one.
- **Use / avoid:** decide layout by window size, never by device type or orientation [DC-L10-10; S-L10-013]; avoid breakpoints that only nudge padding.
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L03-14; S-L03-016, S-L03-018, S-L03-021, S-L03-025, S-L03-032

### Q-layout-02 · Should layouts stretch fluidly, switch between fixed designs, or both? · Expert
- **Why:** Layouts that stretch feel smooth and continuous. Layouts that switch feel native on each device, with different navigation and pane counts [DC-L03-22, DC-L10-10].
- **Ask:** "Should the layout stretch to fit, switch to a new layout at set widths, or both?"
- **Example:** Show a list-detail screen stretching, then becoming two panes at 840dp.
- **Control:** single choice
- **Options:**
  - `responsive` Responsive: one fluid layout (Fluent, Material definitions) [S-L03-010, S-L03-071].
  - `adaptive` Adaptive: distinct layouts per size (show-and-hide, levitate, reflow) [S-L03-071].
  - `both` Stretch inside panes, switch layouts at breakpoints (Apple size classes, Material breakpoints elsewhere) [DC-L03-22, DC-L10-10].
- **Default:** both, with a list-detail template that becomes two panes at expanded. *Source:* card heuristics [DC-L03-22, DC-L10-10].
- **Decides:** DC-L03-22, DC-L10-10
- **Changes:** DC-L10-09, DC-L03-18, DC-L03-21 · blocks: Foundations > Layout > Adaptation strategy
- **Preview:** the resizable frame; pane boundaries highlight when they change.
- **Use / avoid:** use adaptive changes for pane count and navigation; avoid device-type checks that break in split view and resizable windows [S-L10-013].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L03-22, DC-L10-10; S-L03-010, S-L03-071, S-L10-013, S-L10-022, S-L10-025
- **Merges:** P11

### Q-layout-04 · How should top-level navigation work at each size? · Standard
- **Why:** Where the main menu sits is the part of the app's shape people know best: tab bar, rail, sidebar or menu bar [DC-L14-05, DC-L08-19].
- **Ask:** "How many main sections are there, and should the menu sit at the bottom, side or top?"
- **Example:** Ask for the list of main sections; show them as a bottom bar on phone, rail on tablet, sidebar on desktop.
- **Control:** number (destinations) + single choice (pattern)
- **Options:**
  - `adaptive-bar-rail-sidebar` Bottom bar on phones (3-5), rail from 600dp, sidebar on desktop (Material; iOS floating tab bar; iPad sidebar-adaptable) [S-L08-083, S-L10-014, S-L10-025].
  - `sidebar` Sidebar on all but the smallest screens, grouped for 7+ sections (Carbon UI shell, Primer NavList, shadcn Sidebar) [S-L08-009, S-L08-012].
  - `top-nav` Top navigation (marketing sites) [DC-L08-19].
  - `hidden` Hidden in a hamburger or drawer: looks clean, hides scope [DC-L13-02].
- **Default:** adaptive-bar-rail-sidebar; primary navigation visible whenever width allows; at most two disclosure levels; no seven-item cap. *Source:* card heuristics [DC-L08-19, DC-L13-02, DC-L10-09]; L13 E2 (Miller's 7 does not limit menus).
- **Decides:** DC-L08-19, DC-L13-02, DC-L10-09, DC-L14-05, DC-L03-19
- **Changes:** DC-L10-11, DC-L03-20 · blocks: Patterns > Navigation; Patterns > Layout > App shell
- **Preview:** the person's own destination names in each container across the frame widths.
- **Use / avoid:** keep destinations identical across devices and swap only the container; avoid hiding primary navigation on wide layouts [DC-L14-05; S-L13-097].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L08-19, DC-L13-02, DC-L10-09, DC-L14-05, DC-L03-19; S-L08-083, S-L10-014, S-L13-048, S-L13-063, S-L03-025
- **Merges:** P10, K8.3 (navigation part)

### Q-layout-03 · Are your pages mostly for reading, working, or data? · Standard
- **Why:** The page type decides how wide content gets and how panes are laid out. A reading page feels like a document, a work page like a tool, and a data page uses every pixel [DC-L03-16, DC-L03-18].
- **Ask:** "Are most pages for reading, for working in, or for scanning data?"
- **Example:** Show a centered article, a sidebar app page and a full-width dashboard.
- **Control:** multi-select (page types) + single choice (default pane template)
- **Options:**
  - `reading` Reading: centered, max about 1280px, text measure 40-80 characters (Primer full pages 1280; Carbon editorial model) [S-L03-008, S-L03-074].
  - `working` Working: left navigation plus left-aligned content with a max width [DC-L03-16].
  - `data` Data: fluid, full width (Carbon high-density model) [S-L03-074].
  - `feed` / `list-detail` / `supporting-pane` Material's standard layouts; never more than three panes [S-L03-027, S-L03-026].
- **Default:** working + list-detail; one pane below 840dp, two from 840dp, three only at 1600dp+. *Source:* card heuristics [DC-L03-16, DC-L03-18].
- **Decides:** DC-L03-16, DC-L03-18
- **Changes:** DC-L02-17, DC-L03-15 · blocks: Foundations > Layout > Containers; Patterns > Layout > Canonical layouts
- **Preview:** the three page types in the resizable frame.
- **Use / avoid:** use fluid width for tables and dashboards; avoid full-width paragraphs [DC-L03-16, DC-L02-17].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L03-16, DC-L03-18; S-L03-008, S-L03-025, S-L03-026, S-L03-027, S-L03-074

### Q-layout-05 · Which column grid, and how should sections be arranged? · Expert
- **Why:** 16 columns allow uneven layouts, like a magazine; 12 split things evenly. Bento layouts of mixed tiles feel curated, with a clear hero [DC-L03-15, DC-L15-07].
- **Ask:** "Which grid, and should marketing sections use columns, blocks or bento tiles?"
- **Example:** Show a feature section as columns and as a bento grid.
- **Control:** single choice (grid) + single choice (composition)
- **Options:**
  - `4-8-12` 4 / 8 / 12 columns (compact / medium / expanded), gutter 16-24, margin 16 then 24 (Material) [S-L03-026].
  - `2x-grid` 4 / 8 / 16 columns, 32px gutter with wide/narrow/condensed modes (Carbon) [S-L03-002, S-L03-054].
  - `12-always` 12 columns everywhere, 1.5rem gutters (Bootstrap) [S-L03-066].
  - `bento` Clear size order or bento tiles for marketing; free layout only for bold pages [DC-L15-07].
- **Default:** 4 / 8 / 12 columns; column grid for app surfaces, hierarchical or bento for marketing feature sections; only layout spacing (margins, pane gaps) changes with breakpoint. *Source:* card heuristics [DC-L03-15, DC-L15-07, DC-L03-17].
- **Decides:** DC-L03-15, DC-L15-07, DC-L03-17
- **Changes:** DC-L07-28 · blocks: Foundations > Layout > Grid; Composition model; Space > Responsive spacing
- **Preview:** grid overlay toggle on the frame.
- **Use / avoid:** make every grid break nameable ("this hero breaks the grid to signal X"); avoid changing component spacing by breakpoint [DC-L15-07, DC-L03-17].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L03-15, DC-L15-07, DC-L03-17; S-L03-002, S-L03-026, S-L03-054, S-L15-062

### Q-layout-06 · Should components respond to their container or to the window? · Expert
- **Show if:** Q-plat-01 includes web
- **Why:** Parts that adapt to the space they sit in look right anywhere, like the same card in a sidebar or the main column [DC-L03-21].
- **Ask:** "Should components adapt to the space they sit in (container queries) or to the window width?"
- **Example:** Show the same card in a sidebar and in the main column.
- **Control:** single choice
- **Options:**
  - `viewport` Follow the window width at each breakpoint (media queries) [S-L03-016].
  - `container` Container queries (Baseline since 2025-08-14; Tailwind v4 ships 13 container sizes) [S-L03-056, S-L03-016].
- **Default:** page layout by viewport, components by container queries once multi-pane layouts exist. *Source:* card heuristic [DC-L03-21].
- **Decides:** DC-L03-21
- **Changes:** DC-L10-18 · blocks: Foundations > Layout > Responsive mechanism
- **Preview:** the card dragged between slots.
- **Use / avoid:** use container queries for reusable components; avoid viewport queries inside components placed in panes [DC-L03-21].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L03-21; S-L03-016, S-L03-055, S-L03-056

---

## Stage 14 · Shape
> Screen: corner radius, on a live component sheet (button, input, card, dialog, menu, avatar, image). Graph step 1-5. The signature-shape question comes first because brand shape language drives the roundness dial (graph-overrides.json edge DC-L06-09 to DC-L04-02). Nested radii follow the concentric rule automatically (DC-L04-05, see "Auto-applied rules").

### Q-shape-05 · Should a signature shape from your brand appear in the UI? · Expert
- **Why:** Curves feel friendlier, and sharp angles make people sense more threat. A shape that breaks the pattern draws the eye [DC-L06-09; S-L06-073].
- **Ask:** "Is there a shape in your logo or brand we should echo in the UI?"
- **Example:** Show Slack's speech-bubble lozenge used as a graphic element.
- **Control:** single choice (+ upload of the logo for curvature)
- **Options:**
  - `logo-derived` Shapes from the logo, used as graphics and as the base for icons (Slack, Dropbox) [S-L06-030, S-L06-024].
  - `softened` Brand shapes, softened for the UI (Atlassian) [S-L06-088].
  - `curved` Curved, soft UI (Airbnb 2025) [S-L06-062].
  - `variety` Mixed shapes that morph, for tension (M3 Expressive, 35 shapes) [S-L06-009].
  - `rectilinear` Strict straight lines and right angles (IBM) [S-L06-003].
- **Default:** one radius family derived from the logo's curvature; shape variety only in hero moments. *Source:* card heuristic [DC-L06-09].
- **Decides:** DC-L06-09
- **Changes:** DC-L06-13, DC-L06-11 · blocks: Foundations > Shape > Brand shape language
- **Preview:** the logo curvature overlaid on the button radius.
- **Use / avoid:** use shape variety only in hero moments; avoid shrinking essential actions into small shapes ("smaller shapes can result in essential actions looking less important") [S-L06-009].
- **Skip:** yes.
- **Block class:** D (designer-owned)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L06-09; S-L06-003, S-L06-009, S-L06-030, S-L06-073, S-L06-088


### Q-shape-01 · How soft should corners feel? · Quick
- **Why:** In L09's (inferred) ranking, corner radius is what differs most in how systems look (divergence 1). Every 2025-2026 update got rounder [DC-L09-01; L09 A2].
- **Ask:** "How soft should corners feel: square, slightly rounded, rounded, or pill?"
- **Example:** Show a button, input, card and dialog at 0, 6, 12px and pill side by side.
- **Control:** single choice + radius factor slider (0, 0.75, 1, 1.5, full)
- **Options:**
  - `square` 0-2px: official, engineered (GOV.UK, Carbon v11 buttons) [DC-L09-01, DC-L04-02].
  - `subtle` 4-6px: businesslike (Fluent 4, Primer and Atlassian 6) [S-L04-007, S-L04-024, S-L04-016].
  - `soft` 8-12px: friendly, modern (Polaris, Paste, Blade, Mantine v9 8px; Airbnb 12px) [DC-L09-01].
  - `pill` Pill: consumer, playful, touch-first (Material 3, Spectrum 2, SLDS Cosmos; iOS 26 capsule controls) [DC-L09-01; S-L04-038].
  - `rule-based` Set by size (Spectrum 6-10 by size) or matched to the container's corners (Apple) [DC-L09-01; S-L04-035].
- **Default:** 6px controls, 8-12px containers. *Source:* L09 shared default row 7 (16 of 23 control defaults at 4-8px, median 6) [L09 A1; DC-L09-01]; a radius factor slider as Radix offers [S-L09-559].
- **Decides:** DC-L09-01, DC-L04-02
- **Changes:** DC-L04-01, DC-L04-03, DC-L04-04, DC-L04-06, DC-L04-19, DC-L04-09, DC-L05-18 · blocks: Foundations > Shape > Radius scale and default; Shape personality
- **Preview:** the component sheet morphing as the slider moves; the focus ring follows the radius.
- **Use / avoid:** use sharp corners when density and precision are brand values (data, developer tools) and pill when the brand is consumer and touch-first; avoid pill on dense, short controls, which need taller heights [DC-L04-02, DC-L09-01].
- **Skip:** yes, 6px.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 4)
- **Evidence:** DC-L09-01, DC-L04-02; S-L09-101, S-L09-559, S-L04-005, S-L04-029, S-L04-038
- **Merges:** K7.4 (shape)

### Q-shape-02 · Which radius steps should exist? · Expert
- **Why:** Few radius steps give a tight, even look. More steps let large surfaces get rounder corners [DC-L04-01].
- **Ask:** "How many corner radius steps should the scale have?"
- **Example:** Show the steps with a component named under each one.
- **Control:** editable step list
- **Options:**
  - `minimal` 3-4 steps + full (Primer 3/6/12/full) [S-L04-024].
  - `medium` 6-8 steps + full (Atlassian 2-16/full; Carbon v12 0/2/4/8/16/24/max) [S-L04-016, S-L04-030].
  - `large` 9-11 steps + full (Material 0-48; Fluent 0-40) [S-L04-003, S-L04-006].
  - `derived` No scale; each corner follows its container's corner (Apple) [S-L04-035].
- **Default:** 0, 2, 4, 8, 12, 16, 24, full. *Source:* card heuristic [DC-L04-01]; L09 preset 0, 2, 4, 6, 8, 12, 16, 24, full [L09 A1 row 7].
- **Decides:** DC-L04-01
- **Changes:** DC-L04-03, DC-L04-05, DC-L04-09, DC-L15-10 · blocks: Foundations > Shape > Corner radius scale
- **Preview:** each step with the components that use it; unused steps are flagged for deletion.
- **Use / avoid:** grow radius with component size; delete any step you cannot name a component for [DC-L04-01].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L04-01; S-L04-003, S-L04-016, S-L04-024, S-L04-030

### Q-shape-03 · Which components get which radius? · Expert
- **Why:** Rounder corners on bigger parts keep curves in proportion. Keeping full circles for people gives circles a meaning [DC-L04-03].
- **Ask:** "Should corners get rounder on bigger parts, and should full circles be kept for profile pictures?"
- **Example:** Show Atlassian's mapping: badge 2, tag 4, button 6, card 8, modal 12, avatar full.
- **Control:** mapping table
- **Options:**
  - `atlassian-roles` By component type: xsmall 2 badges, small 4 tags, medium 6 buttons and inputs, large 8 cards, xlarge 12 modals, full for avatars [S-L04-016, S-L04-018].
  - `fluent-roles` None for nav and tab bars, small 2px for badges, medium, large, circular for people (Fluent 2) [S-L04-007].
  - `four-roles` Four roles: detail 2-4, control 4-8 or full, container 8-12, overlay 12-16+, person full [DC-L04-03].
- **Default:** four-roles; the radius steps up one level each time the element's height roughly doubles. *Source:* card heuristic [DC-L04-03].
- **Decides:** DC-L04-03
- **Changes:** DC-L04-05, DC-L07-04 · blocks: Foundations > Shape > Radius roles
- **Preview:** the component sheet with each component's role labeled.
- **Use / avoid:** use full radius for people and pills; avoid giving small badges and large dialogs the same radius [DC-L04-03].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L04-03; S-L04-007, S-L04-016, S-L04-018, S-L04-035

### Q-shape-04 · Plain round corners, or smooth Apple-style corners? · Expert
- **Why:** Smooth (continuous) corners blend into the edges. At the same radius they look softer and more "Apple" [DC-L04-04].
- **Ask:** "Use standard round corners, or smooth Apple-style squircle corners where they work?"
- **Example:** Show a 24px card with a circular arc and with 60% corner smoothing, magnified.
- **Control:** single choice
- **Options:**
  - `circular` Circular arc (CSS `border-radius`; every web system) [DC-L04-04].
  - `continuous` Continuous curvature: SwiftUI `.continuous`, Figma corner smoothing (iOS preset 60%) [S-L04-036, S-L04-055].
  - `squircle-enhance` CSS `corner-shape: squircle` as progressive enhancement (experimental, not Baseline as of 2026-08-27) [DC-L04-04].
- **Default:** circular on the web; continuous on iOS-targeted components. *Source:* card heuristic [DC-L04-04].
- **Decides:** DC-L04-04
- **Changes:** DC-L07-13 · blocks: Foundations > Shape > Corner geometry
- **Preview:** magnified corner comparison.
- **Use / avoid:** use continuous corners only where brand parity with iOS matters; avoid relying on `corner-shape` for anything functional [DC-L04-04].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-04; S-L04-036, S-L04-054, S-L04-055

---

## Stage 15 · Depth, borders and materials
> Screen: how surfaces separate and float, on a live stack (page, card, menu, dialog, sheet over a photo) in light and dark. Graph step 0-4. Cycle kept together: DC-L10-11 + DC-L10-12 (edge-to-edge content under the system bars decides the bar material, and the material decides how bars treat content beneath them). Layer order (z-index) and opaque fallbacks for translucency are applied by construction (see "Auto-applied rules").

### Q-depth-01 · How should surfaces separate from each other? · Quick
- **Why:** Shadows feel real to the touch, color steps feel calm, borders feel technical, and glass feels premium. In L09's (inferred) ranking, this is the second biggest way systems differ in look (divergence 2) [DC-L09-02].
- **Ask:** "How should cards and panels stand out from the page: shadows, color steps, lines, or glass?"
- **Example:** Show the same card stack with shadow, tonal, border and ring-plus-shadow treatments.
- **Control:** single choice (pre-filled from Q-dir-01 and Q-dir-04)
- **Options:**
  - `shadow` Shadow ladder: tactile, layered (Fluent dual shadows, Polaris 7 levels, Tailwind 7) [DC-L09-02; S-L04-008, S-L04-022].
  - `tonal` Tonal layers: flat, calm, color-forward (Carbon layers, Material surface containers, Linear) [DC-L09-02; S-L04-058].
  - `borders` Borders only: dense, technical (GOV.UK, Primer) [DC-L09-02].
  - `ring-shadow` 1px ring plus soft shadow (Radix, Geist, Chakra, Airbnb) [DC-L09-02].
  - `glass` Materials and glass: premium, content-first (Apple Liquid Glass, Airbnb) [DC-L09-02; S-L04-032].
- **Default:** in-page containers flat with a border or tinted fill; shadows only for things that float (menus, popovers, dialogs, drag states); in light mode a 1px ring plus soft shadow, in dark mode a lighter surface per level. *Source:* card heuristics [DC-L04-10, DC-L08-15]; L09 shared pattern row 12.
- **Decides:** DC-L09-02, DC-L04-10, DC-L08-15
- **Changes:** DC-L04-11, DC-L04-12, DC-L04-13, DC-L04-15, DC-L07-13 · blocks: Foundations > Elevation > Depth strategy; Components > Card
- **Preview:** the live stack re-rendered per option, light and dark.
- **Use / avoid:** use tonal or borders for data-dense tools; avoid shadows on static in-page cards when the same color steps would do [DC-L09-02, DC-L04-10].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L09-02, DC-L04-10, DC-L08-15; S-L09-104, S-L09-559, S-L04-008, S-L04-017, S-L04-058

### Q-depth-02 · How many elevation levels, and how do they look in dark mode? · Expert
- **Why:** More elevation levels let you show finer order, but they can muddy it. Most products show only three: resting, raised and overlay [DC-L04-11].
- **Ask:** "How many height levels should surfaces have, from sunken to floating on top?"
- **Example:** Show sunken, default, raised and overlay surfaces in dark mode with their hex steps.
- **Control:** number + mapping table
- **Options:**
  - `4-semantic` 4 semantic levels (sunken, default, raised, overlay) with hover and pressed variants (Atlassian) [S-L04-017, S-L04-018].
  - `6-levels` 6 levels (Material 3, Fluent) [S-L04-003, S-L04-006].
  - `7-levels` 7 levels plus special or inset (Polaris, Primer) [S-L04-022, S-L04-024].
- **Default:** 4 semantic levels backed by 4-6 shadow primitives; dark mode steps surfaces 3-5% lighter per level (Atlassian #18191A, #1F1F21, #242528, #2B2C2F). *Source:* card heuristics [DC-L04-11, DC-L04-13].
- **Decides:** DC-L04-11, DC-L04-13
- **Changes:** DC-L07-13, DC-L04-14 · blocks: Foundations > Elevation > Elevation scale; Surface roles
- **Preview:** the stack with each level labeled in both modes.
- **Use / avoid:** components at the same level never overlap each other; avoid pure-black shadows as the only dark-mode depth cue [DC-L04-11, DC-L04-13].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L04-11, DC-L04-13; S-L04-003, S-L04-017, S-L04-018, S-L04-022

### Q-depth-03 · What should shadows look like? · Expert
- **Show if:** Q-depth-01 is shadow or ring-shadow
- **Why:** One hard shadow looks dated; layered soft shadows look real. Tinted shadows avoid a "dirty grey" look on top of color [DC-L04-12].
- **Ask:** "What should shadows look like: many soft layers, a two-layer pair, or tucked under?"
- **Example:** Show a menu with each recipe over a white and a tinted background.
- **Control:** single choice + alpha slider
- **Options:**
  - `key-ambient` A main shadow plus a soft all-around one, 2 layers (Fluent) [S-L04-008].
  - `multi-layer` Many realistic layers (Primer floating.medium, 5 layers) [S-L04-024].
  - `negative-spread` Tucked under with negative spread (Polaris `0 8px 16px -4px`) [S-L04-022].
  - `tinted` Neutral-tinted shadow color instead of black (Polaris rgba(26,26,26), Atlassian #1E1F21) [S-L04-022, S-L04-018].
- **Default:** 2 layers (1px contact shadow plus a soft blur scaled to elevation), neutral-tinted, alpha 8-24% in light mode; in dark mode double the alpha and add a 1px light edge ring on overlays. *Source:* card heuristic [DC-L04-12].
- **Decides:** DC-L04-12
- **Changes:** DC-L07-13 · blocks: Foundations > Elevation > Shadow recipe
- **Preview:** shadows on the live stack with the alpha slider.
- **Use / avoid:** use one light source for every shadow; avoid single hard shadows [DC-L04-12; L15 P62].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-12; S-L04-008, S-L04-018, S-L04-022, S-L04-024

### Q-depth-04 · Should any surfaces be translucent (glass, blur)? · Standard
- **Why:** Glass looks premium and matches 2025-26 operating systems, and keeps what is behind in view. The cost is lower contrast that shifts with the background [DC-L04-15, DC-L10-12].
- **Ask:** "Should menus, bars and pop-ups be see-through glass, or stay solid?"
- **Example:** Show a toolbar over a photo: solid, regular glass, and clear glass with the 35% dimming layer.
- **Control:** single choice + per-platform chrome table
- **Options:**
  - `none` Opaque surfaces: most legible and cheapest [DC-L04-15].
  - `control-layer` Glass on navigation and controls only, never on content (Apple Liquid Glass: regular for text-heavy parts, clear over media with a 35% dim) [S-L04-032, S-L10-008].
  - `transient` See-through menus and flyouts only; Mica for the window base (Fluent Acrylic) [S-L04-011, S-L04-012].
  - `decorative` Decorative glass effect on cards: flagged for legibility (NN/g) [DC-L04-15].
- **Default:** platform material for native chrome (glass on Apple, Mica on Windows, tonal surfaces on Android); opaque on web with optional blur plus an opaque fallback; content edge-to-edge under the bars with inset-aware components. *Source:* platform convention [DC-L10-12, DC-L10-11, DC-L04-15].
- **Decides:** DC-L04-15, DC-L10-12, DC-L10-11
- **Changes:** DC-L04-16, DC-L10-16, DC-L05-16 · blocks: Foundations > Materials > Translucency; Depth > Materials (platform); Layout > Safe areas and insets
- **Preview:** the toolbar and a sheet over a busy photo with live contrast readouts; the opaque fallback shown beside it.
- **Use / avoid:** use glass on the functional layer (bars, controls, sheets) only; avoid glass on reading surfaces and any translucent token without an opaque twin [S-L10-008; DC-L04-16].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L04-15, DC-L10-12, DC-L10-11; S-L04-011, S-L04-032, S-L10-008, S-L10-023, S-L10-075
- **Merges:** P12, P13

### Q-depth-05 · How thick are borders, and when do dividers appear? · Expert
- **Why:** 1px borders look light and precise; 2px look bolder and more accessible. More lines make screens feel like a "spreadsheet" [DC-L04-07, DC-L04-08].
- **Ask:** "How thick should borders be, and should list items be split by lines, space or background?"
- **Example:** Show a list separated by lines, by space and by alternating surfaces.
- **Control:** editable width list + single choice (divider policy)
- **Options:**
  - `1-2-4` 1 / 2 / 4px with 1 default, 2 for focus and selection (Primer, Spectrum) [S-L03-009, S-L03-044].
  - `1-2-3-4` 1 / 2 / 3 / 4px (Fluent web) [S-L04-006].
  - `inset-shadow-borders` Inset box-shadow borders for states that change width, so layout does not jump (Primer) [S-L04-024].
  - `dividers-space-first` Dividers: space first, then a surface change, then 1px subtle lines (Atlassian, Apple `separator`) [S-L04-017, S-L04-032].
- **Default:** 1 / 2 / 4 with inset-shadow borders for state changes; space first, lines in dense data views. *Source:* card heuristics [DC-L04-07, DC-L03-09, DC-L04-08].
- **Decides:** DC-L04-07, DC-L03-09, DC-L04-08
- **Changes:** DC-L04-09, DC-L07-13 · blocks: Foundations > Borders > Stroke width scale; Dividers
- **Preview:** an input switching from default to error without shifting layout.
- **Use / avoid:** use lines in dense tables; avoid stacking dividers and card borders on the same edge [DC-L04-08; L15 P64].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L04-07, DC-L03-09, DC-L04-08; S-L03-009, S-L04-006, S-L04-017, S-L04-024

### Q-depth-06 · How dark should modal backdrops be, and how strong are state overlays? · Expert
- **Why:** A darker shade behind a dialog (scrim) pulls focus hard; a lighter one keeps the page in view for sheets that don't block it [DC-L04-18]. Overlay strengths set how every color looks on hover, press and when disabled [DC-L04-17].
- **Ask:** "How dark should the shade behind dialogs be, and how strong are hover and press tints?"
- **Example:** Show a dialog over the page at 30%, 45% and 60% scrim.
- **Control:** slider (scrim) + number set (overlays)
- **Options:**
  - `scrim-fluent` Black 40% light / 50% dark (Fluent) [S-L04-071].
  - `scrim-atlassian` Blue-black about 46% light / 60% dark (Atlassian `color.blanket`) [S-L04-070].
  - `overlays-material` Tints for hover 0.08, focus 0.10, pressed 0.10, dragged 0.16, disabled 0.38 (Material 3) [S-L04-003].
  - `overlays-atlassian` Stronger tints in dark mode (Atlassian hovered 16%/pressed 32% light, 20%/36% dark) [S-L04-070].
- **Default:** scrim 40-50% near-black in light, 50-60% in dark, tinted toward the neutral hue; Material overlay numbers, raised in dark mode. *Source:* card heuristics [DC-L04-18, DC-L04-17].
- **Decides:** DC-L04-18, DC-L04-17
- **Changes:** DC-L08-20, DC-L08-09 · blocks: Foundations > Opacity > Scrims; State layers
- **Preview:** a dialog and a bottom sheet over the page with the slider live.
- **Use / avoid:** use lighter scrims for non-blocking sheets; avoid scrims so light that the dialog's modality is unclear [DC-L04-18].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-18, DC-L04-17; S-L04-003, S-L04-069, S-L04-070, S-L04-071

---

## Stage 16 · Motion, haptics and sound
> Screen: motion feel on live interactions the person can trigger (open a menu, navigate, toggle, dismiss a sheet), with a reduced-motion toggle. Graph step 0-6.

### Q-motion-01 · Should motion feel quick and quiet, or physical and playful? · Quick
- **Why:** Motion sets how lively the product feels (L09 divergence 7). Short, smooth moves feel efficient, bouncy springs feel alive, and no motion feels still but calm [DC-L09-06].
- **Ask:** "Should motion be quick and barely seen, calm with a few bold moments, or physical and bouncy?"
- **Example:** Open the same menu and page transition with each setting.
- **Control:** single choice + bounce slider (Expert)
- **Options:**
  - `none` Minimal motion (GOV.UK) [DC-L09-06].
  - `productive` Quick, plain curves: fast, competent, no bounce (Carbon productive `cubic-bezier(0.2, 0, 0.38, 0.9)`) [S-L06-002].
  - `two-mode` Plain for most actions, bold for 1-3 key moments per flow (Carbon expressive; Material standard vs expressive schemes) [S-L04-075, DC-L04-19].
  - `springs` Springs throughout: alive, physical, interruptible (Material spring tokens, Apple duration + bounce, Airbnb) [DC-L09-06; S-L10-024].
- **Default:** two-mode: 7 durations 50-500ms, ease-out to enter, ease-in to exit, springs only for spatial moves in the expressive mode, bounce at or below 0.2. *Source:* L09 shared default row 5 (all 16 systems with motion tokens stay in 100-300ms) and card heuristics [DC-L09-06, DC-L04-19]; capped at productive when Q-aud-02 is high-trust.
- **Decides:** DC-L09-06, DC-L04-19, DC-L06-10
- **Changes:** DC-L04-20, DC-L04-21, DC-L04-22, DC-L04-23, DC-L10-14 · blocks: Foundations > Motion; Motion personality
- **Preview:** the live interactions replay on every change, with a slow-motion button.
- **Use / avoid:** use expressive motion for page transitions, the primary action and alerts; avoid bounce on everyday controls and in high-trust products [DC-L06-10, DC-L04-19].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L09-06, DC-L04-19, DC-L06-10; S-L09-105, S-L06-002, S-L04-075, S-L10-024
- **Merges:** K7.4 (motion personality)

### Q-motion-04 · How should springs be defined and exported? · Expert
- **Show if:** Q-motion-01 is two-mode or springs
- **Why:** Spring animations keep their speed when cut off and come to rest in a natural way. The DTCG format has no spring type, so how you store them matters [DC-L04-22; BOARD L04/L07 note].
- **Ask:** "How should springy motion be set up: time and easing only, spring physics, or Apple's bounce?"
- **Example:** Show one spring as (dampingRatio 0.8, stiffness) and as Apple (duration, bounce) and a CSS `linear()` curve.
- **Control:** single choice
- **Options:**
  - `durations-only` Duration + easing only (Carbon, Fluent, Polaris, Primer) [S-L04-014, S-L04-006].
  - `spatial-effects` Two kinds of spring. Moves may overshoot; color and fade effects never do (Material fast/default/slow) [S-L04-060, S-L10-024].
  - `apple-bounce` Duration + bounce 0 / 0.15 / 0.3 (Apple) [DC-L09-06].
- **Default:** (dampingRatio, stiffness) plus derived (duration, bounce) for Apple and pre-sampled `linear()` for CSS; critically damped springs for effects. *Source:* card heuristic [DC-L04-22].
- **Decides:** DC-L04-22
- **Changes:** DC-L07-14, DC-L04-28, DC-L04-06 · blocks: Foundations > Motion > Physics
- **Preview:** a switch and a sheet driven by the spring, dragged and released mid-flight.
- **Use / avoid:** use springs for spatial moves; avoid overshoot on color and opacity [DC-L04-22; S-L10-024].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L04-22; S-L04-060, S-L04-064, S-L10-024, S-L09-105

### Q-motion-02 · Which durations should exist, and should exits be faster? · Expert
- **Why:** Past about 500ms, motion starts to feel slow. Quick exits that people can cut short respect their time [DC-L04-20, DC-L04-24].
- **Ask:** "How many animation lengths should there be, and should things leave faster than they arrive?"
- **Example:** Show a modal entering at 250ms and exiting at 200ms (Atlassian).
- **Control:** editable duration list + toggle (interruptible)
- **Options:**
  - `4-semantic` 4 steps: micro, short, medium, long (Primer) [S-L04-024].
  - `6-steps` 6 steps: instant 0, micro 100, short 150-200, medium 250-300, long 400-500, extra 700 [DC-L04-20].
  - `16-steps` 16 steps (Material 3) [S-L04-003].
  - `asymmetric` Exits 20-35% shorter than entrances (Atlassian modal 250/200; Primer 300/200) [S-L04-018, S-L04-024].
- **Default:** 6 steps; exits about 70-80% of the entrance; motion is interruptible and never blocks input longer than about 100ms. *Source:* card heuristics [DC-L04-20, DC-L04-24]; Apple: "don't make people wait for an animation to complete" [S-L04-033].
- **Decides:** DC-L04-20, DC-L04-24
- **Changes:** DC-L07-14, DC-L13-01 · blocks: Foundations > Motion > Duration scale; Interruptibility
- **Preview:** a timeline of each transition with its duration; clicking mid-animation shows retargeting.
- **Use / avoid:** scale duration with distance travelled; avoid standard transitions over 500ms [DC-L04-20; L13 E1].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L04-20, DC-L04-24; S-L04-003, S-L04-018, S-L04-024, S-L04-033

### Q-motion-03 · Which easing curves? · Expert
- **Why:** Easing curves that slow down hard make things feel fast as they arrive. Curves named by job are the easiest to use the same way everywhere [DC-L04-21].
- **Ask:** "How should speed-up and slow-down curves be grouped: by job, strength or mood?"
- **Example:** Plot the four curves and animate a card with each.
- **Control:** single choice (structure) + curve editor
- **Options:**
  - `role-based` Standard / enter / exit (Carbon, Primer, Windows) [S-L04-014, S-L04-024, S-L04-013].
  - `intensity-based` Min / mid / max intensity (Fluent) [S-L04-006].
  - `personality-based` Practical vs bold (Atlassian); productive vs expressive (Carbon) [S-L04-018, S-L04-014].
- **Default:** standard (0.2, 0, 0, 1), enter (0, 0, 0, 1) or (0.05, 0.7, 0.1, 1), exit (0.3, 0, 1, 1), linear only for spinners and progress. *Source:* card heuristic [DC-L04-21]; L09 shared default row 5.
- **Decides:** DC-L04-21
- **Changes:** DC-L07-14 · blocks: Foundations > Motion > Easing curves
- **Preview:** the curve editor with a live card.
- **Use / avoid:** use linear only for continuous indicators; avoid ease-in for entrances [DC-L04-21].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L04-21; S-L04-003, S-L04-006, S-L04-013, S-L04-014, S-L04-018

### Q-motion-05 · Should shapes morph or use an expressive shape library? · Expert
- **Show if:** Q-shape-01 is pill or Q-motion-01 is springs
- **Why:** Pill shapes look tappable and friendly. Playful shapes (cookies, bursts, clovers) add fun, but work best on avatars and hero moments [DC-L04-06].
- **Ask:** "Keep one simple full-round shape, or add playful shapes that morph at a few key moments?"
- **Example:** Show a toggle morphing from round to square when selected (M3 Expressive).
- **Control:** single choice
- **Options:**
  - `full-token` `radius.full` token only (Atlassian, Polaris, Primer, Fluent, Carbon v12) [S-L04-006, S-L04-018].
  - `people-status` Pill reserved for people and status (Atlassian; Carbon v12 moved tags away from pill) [S-L04-016, S-L04-031].
  - `expressive-library` An expressive shape library with morphing (M3 Expressive `MaterialShapes`) [S-L04-005].
- **Default:** full-token; expressive shapes only for playful brands targeting Material, limited to 1-3 signature uses. *Source:* card heuristic [DC-L04-06].
- **Decides:** DC-L04-06
- **Changes:** DC-L05-18 · blocks: Foundations > Shape > Full round and expressive shapes
- **Preview:** an avatar, a FAB and a toggle with and without morphing.
- **Use / avoid:** use expressive shapes on avatars and hero moments; avoid them on dense controls [DC-L04-06].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-06; S-L04-005, S-L04-016, S-L04-031

### Q-motion-06 · Which named transitions and stagger should the system ship? · Expert
- **Why:** Using the same screen transitions every time helps people follow the app. They can feel whether they went deeper or sideways [DC-L04-23].
- **Ask:** "Which of the four standard ways to change screens should we use, and should list items show up one by one?"
- **Example:** Show a list item expanding into a detail page (container transform) and tabs switching (fade through).
- **Control:** multi-select + number (stagger)
- **Options:**
  - `fade` Fade for in-screen enter and exit (dialogs, menus) [DC-L04-23].
  - `fade-through` Fade through for unrelated destinations such as tabs [DC-L04-23].
  - `shared-axis` Shared axis x, y or z to show where screens sit (onboarding x, stepper y, parent-child z) [DC-L04-23].
  - `container-transform` Container transform, where an item grows into a full page [DC-L04-23].
  - `stagger` A stagger (small delay between items) of 20-50ms, total at most 500ms [DC-L04-23].
- **Default:** all four plus stagger. *Source:* card heuristic, Material's four patterns [DC-L04-23].
- **Decides:** DC-L04-23
- **Changes:** DC-L07-14 · blocks: Patterns > Motion > Transitions and choreography
- **Preview:** each transition playable on the preview.
- **Use / avoid:** use OS-owned navigation transitions on native platforms; avoid custom page transitions that fight the back gesture [DC-L10-14].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-23; S-L04-009, S-L04-014, S-L04-018, S-L04-033

### Q-motion-07 · What happens when people ask for reduced motion, and how much motion fits each device? · Standard
- **Why:** A good reduced motion mode still feels polished, with crossfades instead of jumps. Where people have less attention to spare, motion shrinks, down to none in cars [DC-L04-25, DC-L14-08].
- **Ask:** "When someone turns on reduced motion, should things fade gently or stop moving?"
- **Example:** Toggle reduced motion on the preview; a sliding panel becomes a crossfade.
- **Control:** single choice + per-device table
- **Options:**
  - `replace` Replace movement with fades and color changes (MDN; WCAG's motion rule leaves out color, blur and opacity) [S-L04-067, S-L04-049].
  - `remove` Remove all non-essential motion (WCAG 2.3.3 AAA, technique C39) [DC-L04-25].
  - `per-device` Per device: system transitions plus brand micro-motion on phone and desktop; subtle focus scale on TV; minimal on watch; none in cars; slow and grounded in headsets [DC-L14-08; S-L14-032].
- **Default:** replace, built as a token mode; 2.3.3 treated as a requirement although it is AAA; per-device budgets applied. *Source:* accessibility rule and card heuristics [DC-L04-25, DC-L14-08].
- **Decides:** DC-L04-25, DC-L14-08
- **Changes:** DC-L07-15, DC-L07-14 · blocks: Foundations > Motion > Accessibility; Motion > Device policy
- **Preview:** the reduced-motion toggle on every live interaction.
- **Use / avoid:** keep feedback (color, opacity) and remove travel (translate, scale, parallax); avoid removing feedback entirely [DC-L04-25].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-25, DC-L14-08; S-L04-049, S-L04-067, S-L04-075, S-L14-032
- **Merges:** B15 (reduced motion)

### Q-motion-08 · Do you have UI sounds or a sonic logo? · Standard
- **Why:** Sound confirms actions but annoys people in shared spaces. The builder cannot compose it well [DC-L04-27; BRIEF requirement 2].
- **Ask:** "Do you have app sounds or a sonic logo (a short brand sound) you want to use?"
- **Example:** Play one confirmation sound and show the mute option beside it.
- **Control:** single choice + file upload
- **Options:**
  - `silent` Silent by default (most web systems; tvOS plays no alert sounds) [S-L04-074].
  - `rare-events` Sounds for rare, meaningful events, always behind mute and silent mode [S-L04-074].
  - `sound-forward` Lots of sound (games, spatial computing) [DC-L04-27].
- **Default:** silent on web and productivity apps. *Source:* card heuristic [DC-L04-27].
- **Decides:** DC-L04-27
- **Changes:** DC-L04-26 · blocks: Foundations > Sound > UI sounds
- **Hook:** Accepts Apple notification sounds as Linear PCM, IMA4, µLaw or aLaw in .aiff, .wav or .caf under 30 seconds; Android decodes Ogg (Vorbis, Opus), WAV, MP3, AAC and FLAC [S-L17-550, S-L17-551, S-L17-552]. If no: (1) stay silent, the norm for web and productivity apps; (2) use platform system sounds (Android `SoundEffectConstants`, iOS system behavior); (3) commission a sound designer for a sonic logo, noting that repeated identical sounds feel mechanical; no verified open UI-sound library was found [S-L04-074, S-L17-553, S-L17-555].
- **Preview:** the event list with a play button per sound and the mute state.
- **Use / avoid:** use sound only for rare, meaningful events that honor silent mode; avoid sounds on web and in shared-space products [DC-L04-27].
- **Skip:** yes, silent.
- **Block class:** D (designer-owned)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L04-27; S-L04-043, S-L04-072, S-L04-074
- **Merges:** B7 (sonic logo)

### Q-motion-09 · On iOS and Android, who owns screen changes, the back gesture and vibrations? · Expert
- **Show if:** Q-plat-01 includes ios or android
- **Why:** When the system owns back gestures and transitions, the app feels native; Android's predictive back peeks at the screen behind. Custom vibrations (haptics) feel cheap if you use too many [DC-L10-14, DC-L04-26].
- **Ask:** "On iOS and Android, should screen changes and vibrations follow the system or your brand?"
- **Example:** Show Android predictive back and an iOS swipe-back on the preview.
- **Control:** single choice (motion) + single choice (haptics)
- **Options:**
  - `os-nav-brand-micro` System screen changes and back gesture, with small brand springs inside content [DC-L10-14].
  - `one-language` One brand motion language everywhere [DC-L10-14].
  - `haptics-system` System haptics only (standard controls already play them) [S-L04-043].
  - `haptics-semantic` About 6 named vibrations (success, warning, error, selection, toggle, light impact) [S-L04-044, S-L04-047].
- **Default:** os-nav-brand-micro and haptics-system; a semantic map only for products with frequent confirmations. *Source:* card heuristics [DC-L10-14, DC-L04-26].
- **Decides:** DC-L10-14, DC-L04-26
- **Changes:** DC-L07-14 · blocks: Foundations > Motion > Platform motion; Haptics > Semantic haptic map
- **Hook:** Custom haptics accept Apple AHAP (.ahap JSON, intensity and sharpness 0-1) and Android `VibrationEffect` compositions. If no: system patterns first (Apple notification, impact, selection; Android `HapticFeedbackConstants`) [S-L17-547, S-L17-548, S-L17-549].
- **Preview:** the event list with each haptic's platform mapping.
- **Use / avoid:** use haptics sparingly ("less is more"); avoid long "buzzy" vibrations [S-L04-046; DC-L04-26].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L10-14, DC-L04-26; S-L04-043, S-L04-044, S-L04-046, S-L10-020, S-L10-024
- **Merges:** P15

### Q-motion-10 · Which accessibility settings on the device must the system follow? · Expert
- **Why:** Following these settings changes the look for that person. With high contrast on, borders get thicker; with reduced transparency on, bars turn solid [DC-L10-16].
- **Ask:** "Which device settings should the design follow, like screen readers, bigger text or less motion?"
- **Example:** Show the preview under Increase Contrast and Reduce Transparency together.
- **Control:** multi-select
- **Options:**
  - `screen-readers` VoiceOver, TalkBack and ARIA labels on every icon-only control [S-L10-075, S-L10-072].
  - `text-size` Dynamic Type, Android font scale, browser font size [DC-L10-07].
  - `contrast` Increase Contrast and forced colors [S-L10-031].
  - `transparency` Reduce Transparency [S-L10-008].
  - `motion` Reduce Motion [DC-L04-25].
  - `bold-text` Bold Text [DC-L10-16].
- **Default:** all, with high contrast and reduced transparency as token modes. *Source:* platform convention [DC-L10-16; L10 baked-in rules 9-10].
- **Decides:** DC-L10-16
- **Changes:** DC-L07-15, DC-L04-09 · blocks: Foundations > Accessibility > Platform settings
- **Preview:** a settings simulator panel with each toggle applied live.
- **Use / avoid:** never convey a boundary or focus state with shadow or translucency alone; avoid app-level switches that override these settings [DC-L10-16].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L10-16; S-L10-008, S-L10-031, S-L10-072, S-L10-075
- **Merges:** P17, K4.4

---

## Stage 17 · Icons, app icon and logo use
> Screen: an icon sheet in the product's own buttons, tabs and lists, next to body text at each size. Graph step 0-4. Two asset hooks live here: the icon set (Q-icon-01) and the app icon (Q-icon-06).

### Q-icon-01 · Do you have a custom icon set, or should the system adopt a library? · Standard
- **Why:** Your own icons add character, the platform's icons feel at home, and free open sets stay the same across the app. The builder should not draw icons from scratch [DC-L05-01; BRIEF requirement 2].
- **Ask:** "Do you have your own icons, or should we start from a ready-made set?"
- **Example:** Show the same toolbar in Lucide, Phosphor, Material Symbols and SF Symbols.
- **Control:** single choice + file upload
- **Options:**
  - `platform-native` The platform's own sets: SF Symbols (7,000+, weight-matched to SF, 20+ scripts) and Material Symbols (variable font, 2,500+) [S-L05-006, S-L05-002].
  - `open-source` An open-source set: Lucide (ISC), Heroicons (MIT, 316), Phosphor (MIT, 1,248, 6 weights), Tabler (6,220), Fluent System Icons (MIT) [S-L05-029, S-L05-032, S-L05-031, S-L05-033, S-L05-014].
  - `custom` Your own brand set (IBM, Atlassian 1.5px at 16px, Octicons) [S-L05-017, S-L05-021, S-L05-024].
  - `extend` A ready-made set plus your own icons on its template (Material 24dp keyline template; Apple symbol template) [S-L05-001, S-L05-010].
- **Default:** platform-native on native apps, one open-source set on web; platform glyphs for system actions (share, back, close, more, search, settings), brand icons for product concepts. *Source:* card heuristics [DC-L05-01, DC-L10-25].
- **Decides:** DC-L05-01, DC-L10-25
- **Changes:** DC-L05-02, DC-L05-03, DC-L05-05, DC-L05-10 · blocks: Foundations > Iconography > Icon library source; Platform mapping
- **Hook:** Accepts one SVG per icon on a 16 or 24px master (outlined strokes, no text), or a Figma icon library; icon fonts are accepted but converted, since fonts blur and flash (GitHub moved Octicons to SVG for this reason) [S-L05-038]. If no: (1) adopt an open-source set whose stroke and corners match the type (the default); (2) commission a designer only for domain icons the library lacks, drawn on the library's template; (3) use AI icon generators only as sketches, with the caveat that stroke, keylines and optical size rarely match across a set [inferred]. Apple's terms forbid SF Symbols or look-alikes in app icons and logos [S-L05-010].
- **Preview:** the icon sheet in context; swapping libraries updates every icon.
- **Use / avoid:** use one icon family per product; avoid mixing two libraries' strokes in one toolbar [DC-L05-01, inferred].
- **Skip:** yes; the default library is applied.
- **Block class:** T (tool-assisted)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-01, DC-L10-25; S-L05-002, S-L05-006, S-L05-010, S-L05-029, S-L05-038
- **Merges:** K7.5 (icons), P26

### Q-icon-02 · Outlined or filled icons, rounded or sharp? · Standard
- **Why:** Outline icons look lighter and sit well with text; filled icons look bolder and are easier to spot when small. Icons bring the brand's shapes and line weight into the app (Atlassian matched its icon lines to its type) [DC-L05-02, DC-L06-13].
- **Ask:** "Should icons be outlines or solid shapes, with round or sharp corners?"
- **Example:** Show a tab bar outlined at rest and filled when selected.
- **Control:** single choice (style) + single choice (corners)
- **Options:**
  - `outlined` Outlined: light, clean, good in dense UIs (Material, Apple toolbars, Fluent Regular) [S-L05-003, S-L05-010, S-L05-014].
  - `filled` Filled: more emphasis (Apple iOS tab bars and swipe actions) [S-L05-010].
  - `duotone` Two-tone (duotone): decorative [DC-L05-02].
  - `rounded` / `sharp` Corners that match the rest of the app: pill UIs with rounded icons, 0-2px UIs with sharp icons [DC-L05-02].
- **Default:** outlined at rest, filled plus accent color when selected (two cues that survive color blindness); corners follow Q-shape-01. *Source:* card heuristics [DC-L05-02, DC-L05-06].
- **Decides:** DC-L05-02, DC-L05-06, DC-L06-13
- **Changes:** DC-L05-03 · blocks: Foundations > Iconography > Style; States; Brand match
- **Preview:** the tab bar and toolbar with style and corner toggles.
- **Use / avoid:** keep hover and pressed feedback on the container, not the glyph; avoid color-only selected states [DC-L05-06].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-02, DC-L05-06; S-L05-003, S-L05-010, S-L05-014

### Q-icon-03 · How thick should icon lines be? · Expert
- **Why:** Thin lines look elegant but get weak below 20px, so icon lines should match the letters beside them. Atlassian went from 2px to 1.5px because 2px felt "too heavy" [DC-L05-03, DC-L06-13].
- **Ask:** "How thick should the lines in your icons be?"
- **Example:** Show an icon next to a label at 1.5px and 2px strokes.
- **Control:** slider (stroke) + single choice (terminals)
- **Options:**
  - `2-at-24` 2px lines on a 24px icon (Material weight 400, Lucide) [S-L05-001, S-L05-029].
  - `1.5-at-24` 1.5px lines on a 24px icon (Heroicons) [S-L05-032].
  - `1.5-at-16` 1.5px lines on a 16px icon (Atlassian, Octicons) [S-L05-021, S-L05-024].
  - `variable` Line weight that changes to match the text (Material wght 100-700; SF Symbols 9 weights) [S-L05-003, S-L05-010].
- **Default:** stroke visually equal to body text weight at the paired size: about 1.5px for 14-16px text, 2px at 24px. *Source:* card heuristics [DC-L05-03, DC-L06-13].
- **Decides:** DC-L05-03
- **Changes:** DC-L15-10 · blocks: Foundations > Iconography > Stroke and corner metrics
- **Preview:** icon-label pairs at each text size with the stroke slider.
- **Use / avoid:** use heavier strokes on busy or photographic backgrounds; avoid sub-1.5px strokes below 20px [DC-L05-03].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-03, DC-L06-13 (context); S-L05-001, S-L05-003, S-L05-021, S-L05-032, S-L06-088

### Q-icon-04 · Which icon sizes, and what drawing grid? · Expert
- **Why:** Guide shapes on the grid (keylines) make a round icon and a square icon look the same size. Sizes tuned to whole pixels stay sharp [DC-L05-04, DC-L05-05].
- **Ask:** "Which icon sizes do you need, and which drawing grid should they follow?"
- **Example:** Show a circle and a square icon on the keyline grid.
- **Control:** editable size list + single choice (grid)
- **Options:**
  - `material-grid` 24dp icon, 20dp art area, 2dp padding; opsz 20-48 thins large icons (Material) [S-L05-001, S-L05-003].
  - `carbon` 16px default, 20/24/32 also, tuned to 14 and 16px text (Carbon; IBM 32px master scaled down) [S-L05-016, S-L05-017].
  - `fluent` Sizes 12, 16, 20, 24, 28, 32 and 48 (Fluent) [S-L05-014].
- **Default:** 16, 20, 24 (plus 12 and 32 if needed), sized to the adjacent text line height; Material construction unless the master is 16 or 32. *Source:* card heuristics [DC-L05-05, DC-L05-04].
- **Decides:** DC-L05-05, DC-L05-04
- **Changes:** DC-L03-08 · blocks: Foundations > Iconography > Sizes; Construction grid
- **Preview:** the icon sheet at each size, magnified to show pixel alignment.
- **Use / avoid:** pixel-align at the smallest shipped size; avoid 12px icons for anything interactive [DC-L05-04, DC-L05-05].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-04, DC-L05-05; S-L05-001, S-L05-003, S-L05-014, S-L05-016

### Q-icon-05 · When do icons need labels, and what color are they? · Expert
- **Why:** Icons with words feel calmer and clearer; rows of icons alone feel expert but can confuse. Only a few icons mean the same thing to almost everyone [DC-L05-07, DC-L05-08].
- **Ask:** "When should icons have words next to them, and what color should icons be?"
- **Example:** Show an icon-only toolbar vs the same toolbar with labels.
- **Control:** single choice (labels) + single choice (color)
- **Options:**
  - `labels-default` Labels by default (Material navigation, Atlassian, Polaris) [S-L05-003, S-L05-021, S-L05-027].
  - `universal-only` Icon-only for about a dozen well-known actions (search, close, more, add, delete, edit, share, settings), with a tooltip and screen-reader name [DC-L05-07].
  - `mono` One color, the same as the text (Carbon 4.5:1, Fluent solid) [S-L05-016, S-L05-014].
  - `semantic-tone` Status colors on status icons (Polaris tone) [S-L05-027].
- **Default:** labels-default plus universal-only; one neutral icon color aliased to secondary text, semantic colors only on status icons. *Source:* card heuristics [DC-L05-07, DC-L05-08].
- **Decides:** DC-L05-07, DC-L05-08
- **Changes:** DC-L08-08 · blocks: Foundations > Iconography > Icon with text; Color
- **Preview:** toolbar variants with a label toggle; hover shows the tooltip.
- **Use / avoid:** give every icon-only control an accessible label; avoid decorative multicolor icons in UI chrome [DC-L05-07, DC-L05-08; L10 baked-in rule 9].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L05-07, DC-L05-08; S-L05-003, S-L05-014, S-L05-016, S-L05-021, S-L05-027

### Q-icon-06 · Do you have an app icon? · Standard
- **Show if:** Q-plat-01 includes ios, android or desktop, or the web app is installable
- **Why:** A designer should make the app icon. On Apple it is layered and lit by Liquid Glass; on Android it is adaptive and themed [DC-L05-12; BRIEF requirement 2].
- **Ask:** "Do you have an app icon? If not, I can make a stand-in from your logo, clearly marked."
- **Example:** Show the icon in default, dark, clear and tinted looks on an iOS home screen and as an Android themed icon.
- **Control:** single choice + file upload
- **Options:**
  - `yes-layered` Yes, a file with background and foreground layers [DC-L05-12].
  - `yes-flat` Yes, a flat 1024px image only [DC-L05-12].
  - `no` No: see the Hook line.
- **Default:** one glyph of 1-3 filled shapes on a solid or gradient background, exported as Apple layers, Android foreground/background/monochrome and PWA icons. *Source:* card heuristic [DC-L05-12].
- **Decides:** DC-L05-12
- **Changes:** DC-L10-05 (icon looks follow the user) · blocks: Brand in product > App icon
- **Hook:** Accepts layered SVG or PNG layers at 1024x1024 (watchOS 1088x1088) for Apple's Icon Composer, which applies Liquid Glass and generates default, dark, clear and tinted looks; Android adaptive foreground, background and monochrome layers; PWA maskable 512px [DC-L05-12; S-L05-042]. If no: (1) the builder generates a placeholder from the logo glyph and labels it "placeholder"; (2) commission a designer, the recommended path for a shipped app; photos, fine lines, text and baked-in effects render poorly under system lighting [DC-L05-12]. SF Symbols may not be used in app icons [S-L05-010].
- **Preview:** a home-screen mock per platform with all appearances.
- **Use / avoid:** use simple filled overlapping shapes; avoid photos, fine lines, text and baked-in shadows [DC-L05-12].
- **Skip:** yes; a placeholder is generated.
- **Block class:** D (designer-owned)
- **Time weight:** medium (fan-out 1)
- **Evidence:** DC-L05-12; S-L05-007, S-L05-008, S-L05-011, S-L05-042, S-L05-010

### Q-icon-07 · How should icons be named and shipped? · Expert
- **Why:** SVG files and the platform's own symbols stay sharp at every size, while icon fonts blur and flash. Naming icons by what they show lets one icon serve many meanings [DC-L05-10, DC-L05-09].
- **Ask:** "Should icons ship as SVG files or an icon font, and be named by shape or by job?"
- **Example:** Show `shield_24_regular.svg` aliased as `action.security`.
- **Control:** single choice (delivery) + single choice (naming)
- **Options:**
  - `svg-components` SVG files as the source, turned into ready code for each framework and app (Octicons, Heroicons) [S-L05-022, S-L05-038].
  - `icon-font` Icon font or variable font (Material Symbols) [S-L05-002].
  - `name-by-shape` Name by shape ("Shield, not security": Fluent; SF Symbols) [S-L05-014, S-L05-012].
  - `function-alias` Plus extra names that say what each icon is for, in the code [DC-L05-09].
- **Default:** SVG source, files named `<name>_<size>_<style>`, size and color as props; name by shape with a function-alias layer; RTL behavior recorded per icon. *Source:* card heuristics [DC-L05-10, DC-L05-09].
- **Decides:** DC-L05-10, DC-L05-09
- **Changes:** DC-L07-09, DC-L16-12 · blocks: Foundations > Iconography > Delivery; Metaphor, naming, localization
- **Preview:** the exported icon package tree.
- **Use / avoid:** mirror directional icons in RTL; avoid mirroring icons that depict real objects (clocks, checkmarks) [DC-L05-09, inferred].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L05-10, DC-L05-09; S-L05-012, S-L05-014, S-L05-022, S-L05-038

### Q-icon-08 · How should the logo appear inside the product? · Expert
- **Why:** A small symbol keeps the app's frame quiet and puts the product first; the full logo with its name feels like marketing. A logo in brand color competes with the main buttons [DC-L05-13].
- **Ask:** "Inside the app, should the logo be the symbol alone or the full logo with its name?"
- **Example:** Show the app bar with the symbol at 24px and the sign-in page with the lockup.
- **Control:** single choice (placement) + single choice (appearance)
- **Options:**
  - `symbol-app-bar` Symbol alone at 24-32px in the top bar, full logo on sign-in and marketing [DC-L05-13].
  - `lockup-everywhere` Full logo with its name everywhere [DC-L05-13].
  - `appearance` Logo in brand color, neutral or inverse (Atlassian Logo component) [S-L05-044].
- **Default:** symbol-app-bar with neutral appearance inside dense tools; favicon set from one SVG master. *Source:* card heuristic [DC-L05-13].
- **Decides:** DC-L05-13
- **Changes:** DC-L08-01 (Logo component) · blocks: Brand in product > Logo usage; Favicon
- **Preview:** the app bar and sign-in page.
- **Use / avoid:** give a logo that acts as a link an accessible name; avoid repeating the logo throughout the UI (Apple) [DC-L05-13; S-L10-009].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L05-13; S-L05-014, S-L05-042, S-L05-044

---

## Stage 18 · Imagery, illustration and charts
> Screen: an empty state, onboarding card, hero and dashboard, with the person's own assets dropped in where they exist. Graph step 0-3. Three asset hooks live here: photography (Q-img-01), illustration (Q-img-04) and animated assets (Q-img-06). Image placeholders, chart anatomy tokens and chart accessibility are applied by construction (see "Auto-applied rules").

### Q-img-01 · Does the product use photography, and do you have photos or a photo brief? · Standard
- **Why:** Photos in natural light with true color feel real and worth trusting; film-like color grading plays on feelings. The builder cannot make photos honestly [DC-L05-14; BRIEF requirement 2].
- **Ask:** "Will the product show photos? If so, do you have a library or a photo brief?"
- **Example:** Show a hero with a documentary-style photo and one with a studio product shot.
- **Control:** single choice (style) + file upload
- **Options:**
  - `none` No photography [DC-L05-14].
  - `documentary` Documentary: "frames from a film" (IBM lifestyle photography) [S-L05-046].
  - `portraiture` Portraits that treat every person as equal (IBM "democratic"; Dropbox People) [S-L05-046, S-L05-057].
  - `still-life` Still life, product or content imagery [S-L05-046].
- **Default:** none for tools; for consumer products, a one-paragraph photo brief (subject types, perspective, light, color treatment, casting) before commissioning or buying. *Source:* card heuristic [DC-L05-14].
- **Decides:** DC-L05-14
- **Changes:** DC-L05-15, DC-L05-16, DC-L05-17 · blocks: Foundations > Imagery > Photography style
- **Hook:** Accepts JPEG, WebP or AVIF exports and a written brief; masters in RAW or TIFF are kept outside the system. If no: (1) the builder drafts the photo brief from the personality sliders for you to edit; (2) commission a photographer (best for recognizability); (3) stock against the brief: Unsplash (free commercial, no competing service) or Pexels (no implied endorsement); (4) AI images with ownership and uniqueness caveats per tool, marked as synthetic under EU AI Act Art. 50; NN/g found AI images close to stock but failing on visible artifacts and stereotypes [S-L17-529, S-L17-530, S-L17-531, S-L17-578, S-L17-126]. Neutral placeholders are used until real images arrive.
- **Preview:** image slots in the hero, cards and avatars with the uploaded photos, or labeled placeholders.
- **Use / avoid:** use real product and people photos where trust matters; avoid stock that contradicts the brief's casting and light [DC-L05-14].
- **Skip:** yes.
- **Block class:** D (designer-owned)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-14; S-L05-046, S-L05-057, S-L05-011
- **Merges:** K7.5 (imagery)

### Q-img-02 · Which image shapes, and can text sit on top of images? · Expert
- **Why:** A few image shapes give grids a calm rhythm. Text next to images looks clean and keeps photos true; a dim veil (scrim) under text looks like film but darkens them [DC-L05-15, DC-L05-16].
- **Ask:** "Which image shapes should you use, and may text sit on top of images?"
- **Example:** Show a card grid with mixed ratios vs a fixed ratio set, and a hero with and without a scrim.
- **Control:** multi-select (ratios) + single choice (text on images)
- **Options:**
  - `ibm-set` 16:9, 4:3, 3:2, 2:1, 1:1 aligned to the grid (IBM) [S-L05-047].
  - `per-component` One shape for each place (16:9 hero, 3:2 card, 1:1 avatar) [DC-L05-15].
  - `text-beside` Text beside images (IBM avoids overlays on photos) [S-L05-047].
  - `scrim` A scrim token (a dim veil) under text on hero images, checked for contrast on the worst spot [S-L05-072].
- **Default:** 3-5 ratios, one per slot; text beside images, a scrim token only for heroes. *Source:* card heuristics [DC-L05-15, DC-L05-16].
- **Decides:** DC-L05-15, DC-L05-16
- **Changes:** DC-L04-18 · blocks: Foundations > Imagery > Aspect ratios; Text on images
- **Preview:** the card grid and hero with live contrast readout.
- **Use / avoid:** use art-directed crops per breakpoint for heroes; avoid text over busy image regions without a scrim [DC-L05-15, DC-L05-16].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L05-15, DC-L05-16; S-L05-047, S-L05-072, S-L05-083

### Q-img-03 · Which avatar shapes should mean what? · Expert
- **Why:** Round avatars feel personal and square ones feel like a company or group. A shape of its own makes an AI helper easy to spot at once [DC-L05-18].
- **Ask:** "What shapes should avatars have for people, teams and AI helpers?"
- **Example:** Show a comment thread with a person, a team and an AI agent.
- **Control:** single choice
- **Options:**
  - `circle-square` Circle for a person, square for a team or org (Primer, Fluent, Atlassian) [S-L05-066, S-L05-067, S-L05-069].
  - `agent-shape` Plus a distinct shape for AI agents (Primer treats bots and agents as square) [S-L05-069].
- **Default:** circle-square plus an agent shape if the product mixes human and AI actors; sizes 16-64 on a 4/8 rhythm with initials fallback. *Source:* card heuristic [DC-L05-18].
- **Decides:** DC-L05-18
- **Changes:** DC-L08-22 · blocks: Components > Avatar
- **Preview:** the comment thread with fallbacks (initials, placeholder) and presence dots.
- **Use / avoid:** keep shape meaning consistent everywhere; avoid using the person circle for bots [DC-L05-18].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L05-18; S-L05-066, S-L05-067, S-L05-069

### Q-img-04 · Do you have illustrations or a mascot, and where should they go? · Standard
- **Why:** Characters and hand-drawn art add warmth and let the rest of the app stay plain, but too much makes screens harder to take in. A designer should make the illustrations [DC-L06-12, DC-L05-19, DC-L05-20].
- **Ask:** "Do you have illustrations or a mascot, or should we pick a drawing style and where it goes?"
- **Example:** Show an empty state with a neutral spot illustration, a mascot, and icon-plus-text.
- **Control:** single choice (style) + multi-select (where) + file upload
- **Options:**
  - `none` None: empty states use an icon and text [DC-L05-20, inferred].
  - `line` Line style: precise, calm, technical (IBM: 4px grid, at most 4 line weights, 15-degree angles) [S-L05-048, S-L05-049].
  - `flat` Flat: bold and energetic (IBM) [S-L05-049].
  - `hand-drawn` Loose, hand-drawn lines (Notion) [S-L06-092].
  - `mascot` A mascot in loading, error and empty states (Mailchimp Freddie, Duolingo Duo) [S-L06-028, S-L06-026].
  - `where` Where drawings go: spot illustrations for empty, error, celebration; low-fidelity UI for onboarding; hero and collage only on marketing (Atlassian, Dropbox) [S-L05-050, S-L05-057].
- **Default:** one style derived from the icon stroke, corner radius and palette; neutral spots for routine empty states, colorful spots only for first run and celebration; no humor in errors. *Source:* card heuristics [DC-L05-19, DC-L05-20, DC-L06-12].
- **Decides:** DC-L05-19, DC-L06-12, DC-L05-20
- **Changes:** DC-L05-11, DC-L13-10, DC-L13-11 · blocks: Foundations > Illustration > Style; Brand style and characters; Types and usage
- **Hook:** Accepts SVG (preferred), PNG at 2x, Lottie JSON for animated pieces, plus any illustration guidelines. If no: (1) ship honest icon-plus-text empty states; (2) commission an illustrator with a brief derived from the icon stroke and palette; (3) open sets under their exact terms: unDraw (free commercial, bans AI training and competing packs), Open Peeps and Humaaans (CC0), Blush (no resale), Storyset (credit required, no logos); (4) AI tools such as Recraft or Firefly, where ownership depends on plan, and style drifts between pieces unless one artist or a strict guide owns it [S-L17-519, S-L17-521, S-L17-522, S-L17-523, S-L17-525; inferred for drift].
- **Preview:** the empty, error and success states with the uploaded art or the fallback.
- **Use / avoid:** use illustration only where it has a job (IBM: "have a job to do"); avoid real screenshots in onboarding illustrations and jokes in error states [S-L05-049, S-L05-050; DC-L06-12].
- **Skip:** yes.
- **Block class:** D (designer-owned)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-19, DC-L06-12, DC-L05-20; S-L05-048, S-L05-049, S-L05-050, S-L06-026, S-L06-028
- **Merges:** K7.5 (illustration), B7 (illustration, mascot)

### Q-img-05 · Do you need a middle size of icon (pictograms) between small icons and drawings? · Expert
- **Show if:** Q-scope-01 includes marketing
- **Why:** Pictograms fill the gap between plain small icons and full drawings, so feature grids look richer [DC-L05-11].
- **Ask:** "Do you need pictograms, bigger icons for feature lists and welcome screens?"
- **Example:** Show a 24px UI icon, a 64px pictogram and a 120px spot icon of the same concept.
- **Control:** single choice
- **Options:**
  - `three-tiers` UI icons 24, pictograms 64, spot icons 120 (Dropbox) [S-L05-058].
  - `ui-pictograms` UI icons plus a pictogram library (IBM) [S-L05-049].
  - `ui-only` UI icons only, with drawings for bigger needs (Atlassian) [S-L05-050].
- **Default:** a pictogram tier only with marketing surfaces, drawn with the UI icon's stroke logic scaled up. *Source:* card heuristic [DC-L05-11].
- **Decides:** DC-L05-11
- **Changes:** none downstream in the graph · blocks: Foundations > Iconography > Tiers
- **Preview:** a feature grid with each tier.
- **Use / avoid:** use pictograms on marketing and onboarding; avoid them inside dense product UI [DC-L05-11].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L05-11; S-L05-049, S-L05-050, S-L05-058

### Q-img-06 · Do you have moving icons, Lottie files, 3D art or your own emoji? · Expert
- **Why:** Moving icons confirm an action without taking much room. 3D art and Lottie make a product feel alive but belong on welcome screens and celebrations [DC-L05-21].
- **Ask:** "Do you have moving icons, Lottie files, 3D art or your own emoji to use?"
- **Example:** Show an SF Symbols bounce on a saved state and a Lottie celebration on first success.
- **Control:** multi-select + file upload
- **Options:**
  - `symbol-animation` Built-in icon motion (SF Symbols Appear, Bounce, Pulse, Replace, Draw) [S-L05-010, S-L05-006].
  - `lottie` Lottie or moving drawings for welcome screens and celebrations [DC-L05-21].
  - `3d` 3D assets [DC-L05-21].
  - `emoji-stickers` Your own emoji or stickers [DC-L05-21].
- **Default:** symbol animation only, to confirm an action or show ongoing status; 3D and Lottie kept for onboarding, celebration and marketing. *Source:* card heuristic [DC-L05-21].
- **Decides:** DC-L05-21
- **Changes:** DC-L04-25 (every animation needs a reduced-motion version) · blocks: Foundations > Rich media
- **Hook:** Accepts Lottie JSON, dotLottie (v2 adds state machines and theming), After Effects via Bodymovin, Rive .riv, glTF/GLB and USDZ for 3D; PNG or SVG for emoji [S-L17-541, S-L17-542, S-L17-543, S-L17-556]. If no: motion comes from the system's motion tokens only (no signature animation); commission a motion designer for celebration moments; community Lottie assets only under their stated licenses [S-L17-544, S-L17-546].
- **Preview:** each asset playing in its slot, with the reduced-motion alternative.
- **Use / avoid:** use animated assets for rare moments; avoid looping animation near reading content [DC-L05-21; DC-L04-25].
- **Skip:** yes.
- **Block class:** D (designer-owned)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L05-21; S-L05-006, S-L05-010, S-L05-062, S-L05-063

### Q-img-07 · Where may brand shapes and patterns appear? · Expert
- **Why:** Brand shapes and patterns make the product easy to recognize and feel warm. Used too much, they clutter screens and fight the content for attention [DC-L06-11].
- **Ask:** "Where should brand shapes and patterns show up in the product, if anywhere?"
- **Example:** Show Slack-style logo shapes on an onboarding card and absent from the product table.
- **Control:** single choice
- **Options:**
  - `none` None in product (Carbon product UI) [S-L06-001].
  - `expressive-only` Only on special screens: marketing, onboarding, empty states, hero moments [DC-L06-11].
  - `logo-shapes` Logo shapes used all over (Slack) [S-L06-030].
- **Default:** expressive-only. *Source:* card heuristic [DC-L06-11].
- **Decides:** DC-L06-11
- **Changes:** DC-L13-10, DC-L13-11 · blocks: Foundations > Brand > Graphic devices
- **Hook:** Accepts SVG patterns, gradient definitions and shape SVGs, recorded as brand-expression tokens with allowed surfaces. If no: commission, or ship none; NN/g and gstack both warn that decoration standing in for content reads as generic [S-L17-004, S-L17-021].
- **Preview:** onboarding and a product screen with the motif on and off.
- **Use / avoid:** let branding defer to content in task screens (Apple) [S-L06-008]; avoid devices behind text.
- **Skip:** yes.
- **Block class:** D (designer-owned)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L06-11; S-L06-001, S-L06-008, S-L06-024, S-L06-030

### Q-viz-01 · Which chart types and chart library? · Standard
- **Show if:** Q-color-19 is not none
- **Why:** Fewer kinds of charts make dashboards consistent and easy to learn. Unusual charts look impressive but take longer to read [DC-L05-22].
- **Ask:** "Which kinds of charts do you need, and which chart kit, if any, should draw them?"
- **Example:** Ask for one real dashboard question ("sales by region this quarter") and show the recommended chart.
- **Control:** multi-select (types) + text (library)
- **Options:**
  - `core-6` Bar, line, area, stacked bar, donut or meter, scatter, plus a KPI big number [DC-L05-22].
  - `by-purpose` Chart advice grouped by the question it answers: comparisons, trends, part-to-whole, correlations, connections, geospatial (Carbon) [S-L05-075].
  - `theme-library` Style a ready-made chart kit instead of building one [DC-L05-22].
- **Default:** core-6 on a themed existing library; chart chrome mapped to text and border tokens; every chart gets an insight title, direct labels, a text summary and a "view as table" option. *Source:* card heuristics [DC-L05-22, DC-L05-24, DC-L05-25].
- **Decides:** DC-L05-22
- **Changes:** DC-L05-24, DC-L05-25 · blocks: Foundations > Data visualization > Chart types and library
- **Preview:** a dashboard with the chosen types in the product's palette.
- **Use / avoid:** use bars for comparison and lines for trends; avoid pie charts with more than a few slices and 3D charts [DC-L05-22, inferred].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L05-22; S-L05-075, S-L05-076, S-L05-077, S-L05-083

---

## Stage 19 · Content and voice
> Screen: the product's own buttons, errors, empty states and a success message, rewritten live as voice and tone settings change. Graph step 1-3. Voice comes before components because every component ships its microcopy rules (L06: "voice is a foundation, not a docs appendix") [DC-L06-18]. One asset hook: an existing voice guide (Q-voice-01).

### Q-voice-01 · Do you have a voice and tone guide? If not, what 3-4 traits describe how the product talks? · Standard
- **Why:** Your voice stays the same everywhere, while tone changes with the moment. The product's words and its look must match [DC-L06-18; S-L06-013].
- **Ask:** "Do you have a voice guide? If not, name 3-4 traits in the form 'X, but not Y'."
- **Example:** Show Mailchimp's "plainspoken, genuine" and Atlassian's "Bold, Optimistic, Practical with a wink" beside the same error message.
- **Control:** single choice + file upload or text (traits)
- **Options:**
  - `upload` Upload an existing guide [DC-L06-18].
  - `plainspoken` Plainspoken and genuine, dry humor (Mailchimp) [S-L06-014].
  - `warm-crisp` Warm and relaxed, crisp and clear, ready to lend a hand (Microsoft) [S-L06-046].
  - `bold-optimistic` Bold, optimistic, practical with a wink (Atlassian) [S-L06-060].
  - `custom` Your own traits, set on NN/g's four tone scales, with words to avoid [S-L06-013].
- **Default:** drafted from the personality sliders: 3-4 traits with "but not", 3 copy examples per trait. *Source:* card heuristic [DC-L06-18; S-L06-070].
- **Decides:** DC-L06-18
- **Changes:** DC-L06-19, DC-L06-20, DC-L06-21, DC-L06-22, DC-L06-23 · blocks: Content > Voice
- **Hook:** Accepts a PDF, Markdown file or URL of an existing style guide. If no: (1) the builder drafts traits and examples from the sliders for review; (2) have a content designer review them (22% of teams have none) [S-L11-030]; the draft is labeled as a draft until someone owns it [inferred].
- **Preview:** the error, empty state and success message rewritten in the chosen voice.
- **Use / avoid:** use the traits to decide copy disputes; avoid traits every product could claim ("simple", "friendly") without a "but not" [DC-L06-18; DC-L11-05].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L06-18; S-L06-013, S-L06-014, S-L06-046, S-L06-060, S-L06-070
- **Merges:** K3.6, B13 (voice)

### Q-voice-02 · How should tone change for errors, success and first use? · Standard
- **Why:** Errors need a calm look and plain words, while success can have drawings, motion and a wink. A joke may amuse once but annoys after a dozen times [DC-L06-19; S-L06-060].
- **Ask:** "How should the tone of the words change for errors, success and first use?"
- **Example:** Show one error and one success message at three tone settings.
- **Control:** tone matrix (situation x dial)
- **Options:**
  - `emotion-dial` By how the person feels: less bold for new or anxious users, a wink for success (Atlassian) [S-L06-060].
  - `situation` By situation: straightforward for serious events, congratulatory for goals (Apple) [S-L06-052].
  - `nng-profile` An NN/g four-part tone profile for each kind of content [S-L06-013].
- **Default:** errors serious, respectful, matter-of-fact; success as warm as the brand allows; clarity beats entertainment. *Source:* card heuristic [DC-L06-19; S-L06-014].
- **Decides:** DC-L06-19
- **Changes:** DC-L13-07, DC-L13-10 · blocks: Content > Tone
- **Preview:** the tone matrix with each cell's example message.
- **Use / avoid:** use warmth after trust is earned (success, completion); avoid humor in errors and in high-trust categories [DC-L06-19; S-L06-060].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L06-19; S-L06-013, S-L06-014, S-L06-052, S-L06-060
- **Merges:** B13 (tone)

### Q-voice-03 · Sentence case or title case? · Standard
- **Why:** Title case looks formal and busy; sentence case looks relaxed and translates well [DC-L06-20; S-L06-052].
- **Ask:** "Capital letter only on the first word (sentence case), or on most words (title case)?"
- **Example:** Show a nav, heading and button in "Create new project" vs "Create New Project".
- **Control:** single choice
- **Options:**
  - `sentence` Sentence case everywhere (Microsoft, Atlassian, Fluent) [S-L06-047, S-L06-056, S-L06-098].
  - `title-headings` Title case for headings and main menus, sentence case for buttons (Mailchimp) [S-L06-051].
  - `per-element` Chosen for each kind of text, then used the same way (Apple) [S-L06-052].
- **Default:** sentence case everywhere; all caps only on 11-12px labels with extra tracking. *Source:* card heuristics [DC-L06-20, DC-L02-18].
- **Decides:** DC-L06-20
- **Changes:** DC-L06-22 · blocks: Content > Mechanics > Capitalization
- **Preview:** the product screen's labels re-cased live.
- **Use / avoid:** use one rule per element type everywhere; avoid all caps for sentences [DC-L06-20, DC-L02-18].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L06-20; S-L06-047, S-L06-051, S-L06-052, S-L06-056

### Q-voice-04 · How easy to read should the words be, and how long should labels be? · Standard
- **Why:** Shorter text keeps components small, gets cut off less and reads faster. Even experts prefer plain language [DC-L13-13; S-L13-091].
- **Ask:** "What school grade should the words suit: 6th-8th for everyone, or 10th-12th for experts?"
- **Example:** Show one help text at grade 7 and grade 12.
- **Control:** single choice + number (max words per button)
- **Options:**
  - `grade-6-8` 6th-8th grade for general audiences [S-L13-091].
  - `grade-10-12` 10th-12th grade for specialists [S-L13-091].
  - `labels-2-4` Button and menu labels of 2-4 words, verb first, naming the result [S-L13-036].
- **Default:** 6th-8th for consumer products, 10th-12th for expert tools; button labels 2-4 words, verb first; readability over target is a lint warning. *Source:* card heuristic [DC-L13-13].
- **Decides:** DC-L13-13
- **Changes:** DC-L13-07, DC-L13-16 · blocks: Foundations > Content > Readability
- **Preview:** a readability score beside each sample string.
- **Use / avoid:** use verbs that name the result ("Save changes"); avoid branded or clever button labels [DC-L13-13, DC-L06-22].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L13-13; S-L13-036, S-L13-091

### Q-voice-05 · Which grammar and punctuation rules? · Expert
- **Why:** Short forms like "you'll", the word "we" and an emoji now and then sound friendlier. Skipping "can't" and exclamation marks sounds more formal and exact [DC-L06-21].
- **Ask:** "Which writing rules should the words follow, like 'don't', 'you', 'we' and exclamation marks?"
- **Example:** Show "We couldn't save your file!" vs "Your file wasn't saved. Try again."
- **Control:** toggles
- **Options:**
  - `contractions` Contractions, but not negative ones like 'can't' in serious steps (GOV.UK writes "cannot") [S-L06-048].
  - `pronouns` "You" for the user, "we" sparingly (Apple avoids "we") [S-L06-052].
  - `exclamations` No exclamation marks in errors [S-L06-049].
  - `numbers` Numerals for counts, "to" for ranges [DC-L06-21].
- **Default:** all four as listed. *Source:* card heuristic [DC-L06-21].
- **Decides:** DC-L06-21
- **Changes:** DC-L06-22 · blocks: Content > Mechanics
- **Preview:** sample strings updating per toggle.
- **Use / avoid:** keep mechanics identical across products; avoid mixing date and number formats (see Q-voice-06) [DC-L06-21].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L06-21; S-L06-046, S-L06-048, S-L06-049, S-L06-052, S-L06-056

### Q-voice-06 · Which short text rules and word list should each component come with? · Expert
- **Why:** Buttons that start with a verb are shorter and make clear what matters most. Using the same words each time makes it easy to find your way and know what empty screens mean [DC-L06-22, DC-L06-23].
- **Ask:** "Which writing rules and word lists should come with each component?"
- **Example:** Ask for 5 terms users see often ("workspace" or "project"?) and show them in the nav and an empty state.
- **Control:** text list (glossary) + toggles (patterns)
- **Options:**
  - `verb-first` Verb-first buttons, clear links (not "Click here"), kind fix-it errors, empty states with a next step [S-L06-052, S-L06-051].
  - `flow-vocab` The same step words everywhere: Get started, Continue/Next, Done [S-L06-052].
  - `word-list` A maintained A-Z word list (Mailchimp, Microsoft) [S-L06-014, S-L06-047].
  - `inclusive` Bias-free rules: role nouns, singular they, people's own pronouns (Microsoft; Atlassian inclusive-language page) [S-L06-102, S-L06-054].
- **Default:** all four; a 20-50 term glossary on day one, linted in copy; locale formats and any regulated copy recorded as fixed patterns. *Source:* card heuristics [DC-L06-22, DC-L06-23]; K5.3 and K5.5 [inferred].
- **Decides:** DC-L06-22, DC-L06-23
- **Changes:** DC-L11-18 · blocks: Content > Microcopy; Content > Terminology
- **Preview:** each component with its microcopy rule and an example.
- **Use / avoid:** use the glossary term everywhere; avoid synonyms for the same object [DC-L06-23].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L06-22, DC-L06-23; S-L06-014, S-L06-047, S-L06-051, S-L06-052, S-L06-102
- **Merges:** K5.3, K5.4, K5.5

---

## Stage 20 · Component base and inventory
> Screen: the component catalog, rendered with every foundation chosen so far; each component opens to a detail card (anatomy, states, when to use, when not to use). Graph step 0-3.

### Q-comp-01 · What should your components be built on? · Standard
- **Why:** Bare parts take their look from your tokens, a copied kit looks like its source until changed, and native controls look like the platform [DC-L08-03]. Take a whole system as it is, and you look like it ("websites made with shadcn/ui famously look the same") [DC-L11-01; S-L11-073].
- **Ask:** "Should your components start from bare parts, a kit you copy in, native controls, or a full system?"
- **Example:** Show the same dialog built on Base UI with your tokens vs stock Material.
- **Control:** single choice per platform (pre-filled from Q-scope-05, Q-plat-08 and Q-tool-02)
- **Options:**
  - `headless` Bare parts you style yourself (headless): Radix, Base UI (v1 stable Dec 2025), React Aria, Ark UI [S-L08-030, S-L08-026, S-L08-032, S-L08-031].
  - `copy-in-styled` Styled parts you copy into your code: shadcn/ui on Base UI (its default since July 2026), Radix or React Aria [S-L08-020; BOARD L08 note].
  - `web-components` Web components (Polaris, Fluent UI Web Components v3) [S-L08-022, S-L08-010].
  - `native` The platform's own controls, styled with your tokens (SwiftUI/UIKit, Compose Material 3) [S-L08-103, S-L08-105].
  - `adopt` Adopt a system as-is (Material, Carbon, Fluent, Untitled UI) [S-L11-078; DC-L11-01].
- **Default:** React web: shadcn on Base UI or React Aria; multi-framework: Ark UI or web components; mobile: native controls; small teams adapt an accessible base and invest in tokens and docs. *Source:* card heuristics [DC-L08-03, DC-L11-01; S-L11-006, S-L11-030].
- **Decides:** DC-L08-03
- **Changes:** DC-L08-04 · blocks: Components > Implementation > Base library
- **Preview:** the catalog re-rendered per base; a keyboard-test strip shows focus order and ARIA roles inherited.
- **Use / avoid:** use accessible primitives so keyboard and ARIA behavior come for free; avoid assuming re-themed colors inherit contrast (they don't) [DC-L11-01].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L08-03, DC-L11-01 (context, decided in Q-scope-05); S-L08-020, S-L08-026, S-L08-030, S-L11-006, S-L11-073
- **Merges:** K2.6 (base library)

### Q-comp-02 · Which components are in version 1? · Standard
- **Why:** Teams most often pick a system because it has every part they need (79%), but more parts cost more to keep up [DC-L08-01; S-L11-030].
- **Ask:** "Which components should the first version have, and when should more be added?"
- **Example:** Show the core 25 as a grid; ask which screens of their product need something missing.
- **Control:** multi-select (catalog, core pre-checked)
- **Options:**
  - `core-25` The core set (about 25, in 8-10 of the 10 systems we studied): Button, Text field, Textarea, Select, Checkbox, Radio, Switch, Slider, Tabs, Tooltip, Popover, Dialog, Menu, Progress bar, Spinner, Alert/banner, Badge, Avatar, Card, List, Table, Link, Breadcrumbs, Side navigation, Accordion [DC-L08-01].
  - `extended` Extended (about 25 more): combobox, multi-select, date picker, file upload, toast, skeleton, empty state, drawer/sheet, pagination and others [DC-L08-01].
  - `logo-ai` Brand and AI extras: Logo, AI label and AI button (see Q-icon-08, Q-ai-01).
- **Default:** core-25; extended components when two or more products ask for them. *Source:* card heuristic [DC-L08-01].
- **Decides:** DC-L08-01
- **Changes:** DC-L11-18 · blocks: Components > Inventory
- **Preview:** the catalog grid with a count and a "used by" tag per component.
- **Use / avoid:** use the audit (Q-scope-02) and pilot to pick extras; avoid building components no product has asked for [DC-L08-01, DC-L11-07].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 1)
- **Evidence:** DC-L08-01; S-L08-001, S-L08-008, S-L08-009, S-L11-030
- **Merges:** K8.1

### Q-comp-03 · Should components use settings, or be built from smaller pieces? · Expert
- **Why:** Settings keep screens alike, while smaller pieces allow richer layouts that vary more. Figma slots let each copy of a component change without breaking its link [DC-L08-04, DC-L07-22].
- **Ask:** "Should components be set up with a list of settings, or built from smaller pieces?"
- **Example:** Show `<Button variant="primary">` vs `<Dialog.Root><Dialog.Title/>...</Dialog.Root>`, and a Figma card with a slot.
- **Control:** single choice (code) + single choice (Figma)
- **Options:**
  - `config` Only settings, called props (Carbon, Primer, Polaris) [S-L08-064, S-L08-068].
  - `compound` Smaller parts you combine, with asChild/Slot and render props (Base UI, Radix, React Aria) [S-L08-087, S-L08-088, S-L08-089].
  - `figma-api` Figma: variants for state, size and type; booleans for optional icons; text props for labels; instance swap for single icons; slots for repeating or freeform content [S-L07-021, S-L07-022].
- **Default:** configuration for leaf components, compound parts for containers; the Figma mapping as listed. *Source:* card heuristics [DC-L08-04, DC-L07-22].
- **Decides:** DC-L08-04, DC-L07-22
- **Changes:** DC-L11-18 · blocks: Components > API; Components > Figma component API
- **Preview:** generated code and the Figma component panel for one component.
- **Use / avoid:** use slots for cards, modals and lists so instances keep receiving updates; avoid variant explosions for optional content [DC-L07-22].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L08-04, DC-L07-22; S-L07-021, S-L07-022, S-L08-064, S-L08-088

### Q-comp-04 · How should components be grouped and named? · Expert
- **Why:** How you group components decides how easy they are to find and whether names match in Figma and code [DC-L08-02].
- **Ask:** "How should components be sorted into groups, and what should each group be called?"
- **Example:** Show "Sheet / Drawer / Side panel" mapped to one name.
- **Control:** single choice
- **Options:**
  - `atomic` Atomic design (atoms to pages) [S-L08-054].
  - `primitives-components-patterns` Primitives / components / patterns (Atlassian, Radix) [S-L08-011, S-L08-021].
  - `foundations-components-patterns` Foundations / components / patterns (Carbon, HIG) [S-L08-009, S-L08-086].
  - `purpose` Groups by job: action, containment, communication, navigation, selection, text input (M3) [S-L08-008].
- **Default:** tokens > primitives > components > patterns > templates, with an alias table. *Source:* card heuristic [DC-L08-02].
- **Decides:** DC-L08-02
- **Changes:** DC-L11-18 · blocks: Components > Taxonomy
- **Preview:** the catalog's sidebar regrouped per option.
- **Use / avoid:** use one canonical name with aliases; avoid two components for one job [DC-L08-02].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-02; S-L08-008, S-L08-011, S-L08-054, S-L08-086
- **Merges:** K8.2

### Q-comp-05 · One component set for all devices, or one per device? · Expert
- **Show if:** Q-plat-02 marks watch, TV or car as first-class or works
- **Why:** One set keeps the brand the same everywhere and costs less, but can leave phone-shaped components on a watch or TV [DC-L14-02].
- **Ask:** "Should every device share one set of components, or should some devices get their own?"
- **Example:** Show a phone list row next to the TV focus-row version.
- **Control:** single choice
- **Options:**
  - `one-set-modes` One set whose tokens change by mode (Spectrum desktop/mobile values; Carbon AI presence mode) [S-L03-044, S-L14-058].
  - `separate-libraries` Shared basics, with a separate set for each device (Wear Compose Material 3, TV Material) [S-L10-026, S-L14-025].
  - `templates` Use the car's own templates, no custom components [S-L14-010].
- **Default:** one set for phone, tablet, desktop and web with context modes; separate small libraries for watch and TV; templates for car. *Source:* card heuristic [DC-L14-02].
- **Decides:** DC-L14-02
- **Changes:** none downstream in the graph · blocks: Components > Architecture > Device variants
- **Preview:** one component across device classes.
- **Use / avoid:** split a library when the input model changes (focus, crown, templates); avoid stretching phone components onto TV [DC-L14-02].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L14-02; S-L03-044, S-L10-026, S-L14-010, S-L14-025

---

## Stage 21 · Actions, states and focus
> Screen: a live component sheet where every control can be hovered, pressed, focused with the keyboard, disabled and set to loading. Graph step 0-7. The microinteraction spec (DC-L13-12) is generated for every component (see "Auto-applied rules").

### Q-state-01 · How many button styles, and how many main buttons in each area? · Standard
- **Why:** Three button styles feel calm and strict, while five or six fit busy toolbars. Several filled buttons together make nothing stand out and look like ads [DC-L08-05, DC-L13-18].
- **Ask:** "How many button styles do you need, and how many main buttons can each area have?"
- **Example:** Show a form footer with primary, secondary, tertiary and ghost buttons, then the same with two primaries flagged.
- **Control:** single choice + toggle (one primary per region)
- **Options:**
  - `three` Solid, outline, text [DC-L08-05].
  - `four-danger` Primary, secondary, tertiary/outline, ghost/text, plus danger (Carbon, Fluent) [S-L08-061, S-L08-066].
  - `five-plus` 5-7 styles, adding tonal, raised, discovery or AI buttons (M3 5; Atlassian 7 incl. Rovo) [S-L08-033, S-L08-063].
- **Default:** four-danger; at most one high-emphasis action per region, placed after the last field in reading order; a destructive button never takes the primary role. *Source:* card heuristics [DC-L08-05, DC-L13-18; S-L13-054, S-L08-039].
- **Decides:** DC-L08-05, DC-L13-18
- **Changes:** DC-L08-06, DC-L08-14, DC-L13-15 · blocks: Components > Button > Variants; Components > Actions > Emphasis hierarchy
- **Preview:** the button sheet in every state, plus a form footer.
- **Use / avoid:** use style, not size, to mark the preferred choice (Apple); avoid two primary buttons in one group [S-L08-039; L13 E1].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L08-05, DC-L13-18; S-L08-033, S-L08-061, S-L08-063, S-L13-014, S-L13-054

### Q-state-02 · How obvious should clickable things be? · Standard
- **Why:** Faint clues look sleek, but people take 22% more time and 25% more eye stops to find what to click (NN/g) [DC-L15-09; S-L15-004].
- **Ask:** "How clearly should buttons and links show they can be tapped or clicked?"
- **Example:** Show the same card with a filled button and underlined link vs flat text-only actions.
- **Control:** single choice (pre-filled from Q-dir-02)
- **Options:**
  - `strong` Strong: filled or slightly raised buttons, colored underlined links, bordered inputs, color reserved for interactive elements [S-L15-004].
  - `balanced` Balanced: filled primary, outline secondary, link-style tertiary, links underlined on hover [S-L15-038].
  - `minimal` Minimal: flat, text-only actions [DC-L15-09].
- **Default:** balanced, with strong signifiers forced on primary actions; minimal only when density is low and layouts are conventional. *Source:* card heuristic [DC-L15-09].
- **Decides:** DC-L15-09
- **Changes:** DC-L08-09, DC-L08-16 · blocks: Foundations > Visual language > Signifiers
- **Preview:** a click-test overlay highlighting everything interactive.
- **Use / avoid:** use stronger signifiers as density rises; avoid minimal signifiers in dense layouts [DC-L15-09; S-L15-004].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L15-09; S-L15-004, S-L15-006, S-L15-038, S-L15-054

### Q-state-03 · What should the keyboard focus ring look like? · Standard
- **Why:** A thicker focus ring with a gap is impossible to miss but louder. A ring drawn inside keeps tight grids neat but can fail contrast on filled controls [DC-L04-09, DC-L08-11].
- **Ask:** "What should the focus ring look like, the outline that shows where the keyboard is?"
- **Example:** Tab through a button, input and table row with each ring style.
- **Control:** single choice + width/offset numbers
- **Options:**
  - `outer-2-2` 2px ring, 2px gap, corners = the part's radius + the gap (Atlassian radius.focus, Primer 2px) [S-L04-016, S-L04-024].
  - `material-3` 3px ring, 2px gap outside, or -3px inside where an outer ring would be cut off (Material 3) [S-L04-003].
  - `inset` Border drawn inside, for tight grids (Carbon $focus + $focus-inset) [S-L08-062].
  - `two-tone` Two-tone ring (inner white, outer dark) that is 3:1 on every surface [DC-L08-11].
- **Default:** outer-2-2 in a high-contrast brand or neutral color with light and dark values, plus a forced-colors fallback (an outline, not a box-shadow alone). *Source:* card heuristics and accessibility rule [DC-L04-09, DC-L08-11; S-L10-031].
- **Decides:** DC-L04-09, DC-L08-11
- **Changes:** DC-L07-13 · blocks: Foundations > Borders > Focus ring; Components > States > Focus-visible
- **Preview:** keyboard tab-through of the preview screen with the ring on every stop.
- **Use / avoid:** show focus only for keyboard (`:focus-visible`); avoid rings that the element's own fill hides [DC-L08-11, DC-L04-09].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-09, DC-L08-11; S-L04-003, S-L04-016, S-L04-024, S-L08-062, S-L08-069

### Q-state-04 · Which states get their own styling, per input type? · Expert
- **Why:** A see-through tint gives any color its states for free; a token for each state lets you tune them to the brand. On TV, focus is large and moving; on desktop, the ring is thin and still [DC-L08-09, DC-L14-06].
- **Ask:** "How should states like hover, pressed and disabled get their look, and does it change by device?"
- **Example:** Show a card's states on desktop vs its focused state on TV.
- **Control:** multi-select (states) + single choice (method)
- **Options:**
  - `overlays` A see-through tint on hover and press (Material state layers) [S-L01-005, S-L08-095].
  - `explicit` Its own token for each state and variant (Carbon) [S-L08-062].
  - `per-input` By how people use each device: desktop rest/hover/focus-visible/pressed/selected/disabled; TV focused with scale and elevation; tablet pointer lift [S-L14-013, S-L14-071].
- **Default:** style all eight states; overlays for hover and press, explicit tokens for selected and error; define states once, render the subset each context can trigger. *Source:* card heuristics [DC-L08-09, DC-L14-06].
- **Decides:** DC-L08-09, DC-L14-06
- **Changes:** DC-L07-02 · blocks: Components > States; Foundations > Interaction > States
- **Preview:** the state matrix for every component.
- **Use / avoid:** make hover content dismissible and persistent (WCAG 1.4.13); avoid hover-only affordances on touch [DC-L14-06].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-09, DC-L14-06; S-L01-005, S-L08-062, S-L14-013, S-L14-070, S-L14-071

### Q-state-05 · How should selected and active items look? · Expert
- **Why:** Showing picked items in brand color feels lively. A neutral look keeps brand color meaning "action" and nothing else [DC-L08-14].
- **Ask:** "How should the app show which tab or item is picked?"
- **Example:** Show a tab bar with a pill indicator, an underline and a neutral fill.
- **Control:** single choice
- **Options:**
  - `pill-indicator` A pill shape behind the icon (M3 navigation) [S-L08-083].
  - `underline` A line under it (Primer UnderlineNav) [S-L08-012].
  - `neutral` A plain look, not the brand color (Atlassian) [S-L08-085].
  - `morph` Shape changes from round to square (M3 Expressive toggles) [S-L08-034].
- **Default:** an indicator plus color, never color alone; brand primary reserved for actions in action-dense products. *Source:* card heuristic [DC-L08-14].
- **Decides:** DC-L08-14
- **Changes:** none downstream in the graph · blocks: Components > States > Selected
- **Preview:** tabs, nav rail and segmented control selected.
- **Use / avoid:** use two cues for selection; avoid selection states that look like primary buttons [DC-L08-14].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-14; S-L08-012, S-L08-034, S-L08-083, S-L08-085

### Q-state-06 · How should destructive actions look? · Expert
- **Why:** Solid red draws the eye and invites mis-clicks on main screens; subtle red keeps lists calm [DC-L08-06].
- **Ask:** "How should delete buttons and other risky actions look?"
- **Example:** Show a table row's delete action and the confirmation dialog.
- **Control:** single choice
- **Options:**
  - `solid-danger` Solid red danger button (Carbon, Primer, shadcn destructive) [S-L08-061, S-L08-064, S-L08-065].
  - `danger-levels` Danger in several button styles (Carbon danger primary/tertiary/ghost) [S-L08-061].
  - `warning-vs-danger` Warning for big changes, danger for the final step you can't undo (Atlassian) [S-L08-063].
- **Default:** subtle danger in context, solid danger only in the confirmation step. *Source:* card heuristic [DC-L08-06].
- **Decides:** DC-L08-06
- **Changes:** DC-L13-08 · blocks: Components > Button > Danger
- **Preview:** a list with delete actions and the confirm step.
- **Use / avoid:** use undo instead of confirmation for reversible actions (Q-form-05); avoid solid red buttons in dense lists [DC-L08-06].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-06; S-L08-061, S-L08-063, S-L08-064, S-L08-075

### Q-state-07 · Where do icons go inside buttons? · Expert
- **Why:** An icon before the words helps people scan; words left and an icon right give Carbon's editorial look. Buttons with only an icon need labels [DC-L08-08].
- **Ask:** "Where should icons go inside buttons: before the words, after, or both?"
- **Example:** Show "Download" with a leading icon and Carbon-style trailing icon.
- **Control:** single choice
- **Options:**
  - `leading` Icon before the words, if wanted (M3, 20dp) [S-L08-033].
  - `trailing` Label left, icon right (Carbon, 16px icon) [S-L08-061, S-L08-062].
  - `both-slots` Icon spots on both sides (Atlassian iconBefore/iconAfter; Primer leadingVisual/trailingVisual) [S-L08-063, S-L08-064].
- **Default:** optional leading icon, sentence-case verb labels. *Source:* card heuristic [DC-L08-08].
- **Decides:** DC-L08-08
- **Changes:** none downstream in the graph · blocks: Components > Button > Content
- **Preview:** the button sheet with icons.
- **Use / avoid:** use trailing icons for direction (next, external); avoid icon-only buttons without an accessible name [DC-L08-08].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-08; S-L08-033, S-L08-061, S-L08-063, S-L08-064

### Q-state-08 · How should the product show that it is working? · Standard
- **Why:** Skeletons, gray boxes where things will load, make pages feel ordered and faster; spinners feel plain and don't say how long. How long the wait is decides which to use [DC-L13-01, DC-L08-12].
- **Ask:** "What should people see while they wait, for short waits and long ones?"
- **Example:** Simulate a 0.5 s, 3 s and 12 s load on the preview.
- **Control:** single choice + threshold numbers
- **Options:**
  - `nng-ladder` Nothing under 1 s, a looping sign for 2-10 s, a percent-done bar over 10 s (NN/g) [S-L13-032, S-L13-031].
  - `skeleton-first` Skeletons (gray boxes) for page or area loads, spinners for smaller parts (Carbon skeletons only on containers) [S-L13-033, S-L05-071].
  - `inline-button` Spinner inside the button you pressed, which keeps focus (S2 pending after 1 s; Carbon inline loading) [S-L08-067, S-L08-061].
- **Default:** acknowledge within 50ms; the NN/g ladder with skeletons for first page load and in-button pending states that stay focusable. *Source:* card heuristics [DC-L13-01, DC-L08-12]; BOARD L13 note (timing ladder).
- **Decides:** DC-L13-01, DC-L08-12
- **Changes:** DC-L07-14 · blocks: Patterns > Feedback > Loading; Components > States > Loading
- **Preview:** the three simulated waits.
- **Use / avoid:** use optimistic UI only when failure is rare and reversible; avoid spinners for waits under a second [DC-L13-01].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L13-01, DC-L08-12; S-L13-031, S-L13-032, S-L13-033, S-L08-067, S-L08-074

---

## Stage 22 · Forms, validation and feedback
> Screen: a live sign-up form and a list with delete actions; the person fills fields, triggers errors and deletes items to feel each option. Graph step 0-6. Cycles kept together: DC-L08-10 + DC-L08-17 (whether submit can be disabled depends on when validation runs, and vice versa), DC-L13-06 + DC-L13-07 (timing and error message pattern), DC-L13-08 + DC-L13-09 (undo needs a channel such as a toast; the channel set depends on whether undo exists).

### Q-form-01 · What style should form fields have, and where do labels go? · Standard
- **Why:** Filled fields feel soft and app-like, while outlined fields feel crisp and form-like. Using hint text inside the box as the only label causes seven known problems [DC-L08-16, DC-L13-05; S-L13-066].
- **Ask:** "Should text boxes have a border or a shaded fill, and where should their labels go?"
- **Example:** Show one field outlined, filled and underline-only, each filled in and in error.
- **Control:** single choice (style) + single choice (label) + single choice (marking)
- **Options:**
  - `outlined` Fields with a border (M3 outlined; Carbon) [S-L08-105, S-L08-106].
  - `filled` Fields with a shaded fill (M3 filled) [S-L08-105].
  - `label-top` Label always above, hint under the label [S-L13-066].
  - `placeholder-label` Hint text inside the box as the label: rejected (memory strain, no way to check entries) [S-L13-066].
  - `mark-minority` Mark only the rarer of required or optional, "(optional)" or "(required)" [S-L08-106].
- **Default:** outlined, top labels of 1-3 words without colons, hint under the label, the rarer of required/optional marked, `autocomplete` on personal-data fields. *Source:* card heuristics [DC-L08-16, DC-L13-05].
- **Decides:** DC-L08-16, DC-L13-05
- **Changes:** DC-L08-17 · blocks: Components > Text field; Patterns > Forms > Field anatomy
- **Preview:** the sign-up form in each style, typed into live.
- **Use / avoid:** use a visible label on every field; avoid placeholder-only labels (a lint warning) [DC-L13-05; L13 E1].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L08-16, DC-L13-05; S-L08-105, S-L08-106, S-L13-066, S-L13-068

### Q-form-02 · When should forms show errors, and should the submit button ever be disabled? · Standard
- **Why:** Errors that show too early feel hostile, and checking on submit keeps forms calm. A disabled button hides why the action can't run [DC-L13-06, DC-L08-17, DC-L08-10].
- **Ask:** "When should a form check answers, and can the submit button ever be turned off?"
- **Example:** Let them type a bad email and tab away, then submit with an empty field.
- **Control:** single choice (timing) + single choice (disabled policy)
- **Options:**
  - `on-submit-summary` On submit, a list of errors at the top that takes focus, "Error:" prefix, notes by each field (GOV.UK) [S-L08-077].
  - `on-blur` When you leave a field ("reward early, punish late"): clear the error on the keystroke that fixes it; validate at complete length for ZIP and phone [S-L13-065, S-L13-100].
  - `disable-short-forms` Turn off submit on short forms until all is right, never on long ones (Carbon) [S-L08-106].
  - `never-disable` Never turn off submit; explain the problem instead (Atlassian) [S-L08-085].
- **Default:** on-blur for format checks, on submit otherwise, summary plus inline for forms over about 5 fields; never-disable, with `aria-disabled` and helper text when an action truly cannot run. *Source:* card heuristics [DC-L13-06, DC-L08-17, DC-L08-10]; systems disagree (see Disagreements).
- **Decides:** DC-L13-06, DC-L08-17, DC-L08-10
- **Changes:** DC-L13-07 · blocks: Patterns > Forms > Validation; Components > States > Disabled
- **Preview:** the live form with timing toggles.
- **Use / avoid:** use on-blur validation for format checks; avoid flagging a field before the person has finished typing [DC-L13-06].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L13-06, DC-L08-17, DC-L08-10; S-L08-077, S-L08-085, S-L08-106, S-L13-065, S-L13-100

### Q-form-03 · How should error messages be shown and written? · Expert
- **Why:** An error by its field shows the problem where it is; banners flag system problems; dialogs stop what you are doing. How loud an error looks should match how serious it is [DC-L13-07; S-L13-064].
- **Ask:** "Where should error messages show up, and how should they be worded?"
- **Example:** Show a field error, a page banner and a blocking dialog for three severities.
- **Control:** mapping (severity to pattern)
- **Options:**
  - `inline` Error next to the field it is about [DC-L13-07].
  - `summary` Error summary at the top of the form [DC-L13-07].
  - `banner` Section or page banner [DC-L13-07].
  - `dialog` A pop-up box that blocks the page [DC-L13-07].
  - `error-page` Full error page for catastrophic failures [DC-L13-07].
- **Default:** NN/g's 13 error-message guidelines: close to the source, visible without color alone, plain words that say what happened and how to fix it. *Source:* card heuristic [DC-L13-07; S-L13-064, S-L13-030].
- **Decides:** DC-L13-07
- **Changes:** DC-L11-18 · blocks: Patterns > Feedback > Errors
- **Preview:** the three severities on the form.
- **Use / avoid:** use a fix-it sentence in every error; avoid blame and jargon codes [DC-L13-07, DC-L06-22].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L13-07; S-L13-030, S-L13-037, S-L13-064

### Q-form-04 · Where should messages like 'Saved' show: in place, a toast, a banner or a pop-up? · Standard
- **Why:** Toasts keep the layout still but flash by and vanish, while banners stay put and are easy to find. Systems disagree on whether toasts belong at all [DC-L08-18, DC-L13-09].
- **Ask:** "Where should messages like 'Saved' appear: in place, in a banner, or in a toast that fades?"
- **Example:** Save a record and show the confirmation as inline text, a toast and a banner.
- **Control:** single choice + per-status table
- **Options:**
  - `inline-banner` Inline or banner by default; toasts only for low-stakes confirmations with undo, never auto-dismissing toasts that contain actions (Carbon matrix of 4 statuses x 7 types) [S-L08-079; DC-L13-09].
  - `no-toasts` No toasts; banners and dialogs only (Primer) [S-L08-098, S-L08-012].
  - `toasts-widely` Toasts and flags used widely (M3 snackbar, Atlassian flags) [S-L08-008, S-L08-011].
- **Default:** inline-banner; the message goes where the cause is. *Source:* card heuristics [DC-L08-18, DC-L13-09]; systems disagree (see Disagreements).
- **Decides:** DC-L08-18, DC-L13-09
- **Changes:** DC-L13-08 · blocks: Patterns > Notifications; Patterns > Feedback > Messaging
- **Preview:** the save action with each channel.
- **Use / avoid:** use toasts only for reversible, low-stakes results; avoid a toast as the only record of an error [DC-L13-09].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L08-18, DC-L13-09; S-L08-008, S-L08-011, S-L08-079, S-L08-098, S-L13-064

### Q-form-05 · For deletes and other risky steps, offer undo or ask first? · Standard
- **Why:** Undo keeps work fast and calm. Asking "Are you sure?" too often feels like red tape, and people stop reading it [DC-L13-08; S-L13-067].
- **Ask:** "When people delete something, should they get an undo button, an 'Are you sure?' step, or both?"
- **Example:** Delete a list item: show the undo toast, then an irreversible delete with a "Delete file / Keep file" dialog.
- **Control:** single choice
- **Options:**
  - `undo-first` Undo with trash or soft delete for actions you can reverse (NN/g calls undo superior; Shneiderman rule 6) [S-L13-067, S-L13-037].
  - `confirm` An 'Are you sure?' box with clear verb buttons, and Cancel as the safe choice [S-L13-067; DC-L13-08].
  - `both` Undo when it can be undone, ask first when it can't or costs a lot [DC-L13-08].
- **Default:** both. *Source:* card heuristic [DC-L13-08].
- **Decides:** DC-L13-08
- **Changes:** DC-L13-09 · blocks: Patterns > Error prevention > Destructive actions
- **Preview:** the list delete flow per option.
- **Use / avoid:** use verb labels on confirmations; avoid "Are you sure?" dialogs for reversible actions [DC-L13-08].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L13-08; S-L13-037, S-L13-067, S-L08-012, S-L08-039

---

## Stage 23 · Patterns and AI surfaces
> Screen: small flows the person can click through: open a dialog and a side sheet, page through a table, reach an empty state, meet a consent prompt, and see AI-generated content. Graph step 0-2. Content hierarchy for scanning (DC-L13-04) is applied by construction.

### Q-pattern-01 · When should the product use a dialog, a sheet or a popover? · Standard
- **Why:** A centered dialog stops people in their tracks. A side sheet keeps the page in view, and a popover feels light [DC-L08-20].
- **Ask:** "Which tasks should open in a box in the middle, a panel that slides in, or a small pop-up?"
- **Example:** Edit a record in a dialog vs a side sheet on the preview.
- **Control:** mapping (task type to overlay)
- **Options:**
  - `hig` Block the page only if it clearly helps; panels and pop-ups for small tasks; full screen for big flows (HIG) [S-L08-086].
  - `sheets` Panels that slide in from the bottom or side (M3, Fluent, Atlassian) [S-L08-008, S-L08-010, S-L08-011].
  - `levitate` Floating "levitate" panes for focused tasks (M3) [S-L08-096].
- **Default:** dialog for short decisions, side sheet for editing with context, bottom sheet on phones; each platform's button order. *Source:* card heuristic [DC-L08-20].
- **Decides:** DC-L08-20
- **Changes:** DC-L04-18 · blocks: Patterns > Modality; Components > Dialog, Sheet, Popover
- **Preview:** the same edit task in each overlay.
- **Use / avoid:** use a dismiss path on every dialog (missing one is a lint error); avoid stacking modals [DC-L08-20; L13 E1].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-20; S-L08-008, S-L08-040, S-L08-086, S-L08-096

### Q-pattern-02 · How should long lists load: pages, "load more", or infinite scroll? · Expert
- **Why:** Numbered pages help people find their place again. Infinite scroll feels endless, and a "Load more" button keeps the footer in reach [DC-L08-21].
- **Ask:** "How should long lists load: in pages, with a 'Load more' button, or by scrolling on and on?"
- **Example:** Show a table with pagination and a feed with infinite scroll.
- **Control:** mapping (collection type to pattern)
- **Options:**
  - `pagination` Page numbers (Carbon, Atlassian, Primer, shadcn) [DC-L08-21].
  - `load-more` Load more [S-L08-073].
  - `infinite` Infinite scroll, for feeds of same-kind items [S-L08-073].
- **Default:** pagination for tables and goal-directed search, load more for result lists, infinite scroll only for feeds. *Source:* card heuristic [DC-L08-21].
- **Decides:** DC-L08-21
- **Changes:** none downstream in the graph · blocks: Patterns > Collections
- **Preview:** each collection type on the preview.
- **Use / avoid:** use pagination where people need to return to a position; avoid infinite scroll above a footer people need [DC-L08-21].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-21; S-L08-017, S-L08-041, S-L08-073

### Q-pattern-03 · How much should be visible up front, and how much behind "more"? · Expert
- **Why:** Keeping extras one step away (progressive disclosure) makes screens calm and short. Showing it all at once feels strong, but busy [DC-L13-03].
- **Ask:** "Should people see every option at once, or the main ones first with the rest tucked away?"
- **Example:** Show a settings page with an "Advanced" section collapsed and expanded.
- **Control:** single choice
- **Options:**
  - `all-visible` Show everything at once [DC-L13-03].
  - `progressive` Main options first, extras behind a clearly named button, two levels at most [S-L13-063].
  - `staged` One step at a time (a wizard), only when steps stand alone [S-L13-063].
  - `contextual` Show extras on hover or when something is picked [DC-L13-03].
- **Default:** progressive. *Source:* card heuristic [DC-L13-03].
- **Decides:** DC-L13-03
- **Changes:** none downstream in the graph · blocks: Patterns > Information density > Disclosure
- **Preview:** the settings page per option.
- **Use / avoid:** use steppers that show position and total; avoid more than two disclosure levels (a lint warning) [DC-L13-03; L13 E1].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L13-03; S-L13-019, S-L13-030, S-L13-063

### Q-pattern-04 · How should empty states and first-time use work? · Standard
- **Why:** A well-made empty state teaches and invites people in. A blank area looks broken, and forced tours slow people down at the start [DC-L13-10, DC-L13-11].
- **Ask:** "What should an empty screen show, and how should first-time users learn the product?"
- **Example:** Show a first-use empty project list, a no-results search and a tour with a skip button.
- **Control:** single choice (onboarding) + checklist (empty-state kinds)
- **Options:**
  - `empty-kinds` Empty states for first use, user-cleared, no results, no permission or error (Primer Blankslate, Spectrum IllustratedMessage, shadcn Empty) [DC-L13-10; S-L08-012, S-L08-015, S-L08-018].
  - `onboarding-none` No onboarding: a self-evident UI (NN/g's first recommendation) [S-L13-070].
  - `onboarding-contextual` Tips and empty-screen hints right when people need them [S-L13-070].
  - `walkthrough` A guided tour, only for truly new and complex screens [S-L13-070].
- **Default:** every collection gets empty variants that state status, help learning and give a direct action; contextual onboarding; everything skippable. *Source:* card heuristics [DC-L13-10, DC-L13-11; S-L13-069, S-L13-070].
- **Decides:** DC-L13-10, DC-L13-11
- **Changes:** none downstream in the graph · blocks: Patterns > States > Empty; Patterns > Guidance > Onboarding
- **Preview:** each empty-state kind with the illustration choice from Q-img-04.
- **Use / avoid:** use an empty state on every collection (missing one is a lint warning); avoid tours without a skip control [DC-L13-10, DC-L13-11; L13 E1].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L13-10, DC-L13-11; S-L13-069, S-L13-070, S-L08-012, S-L08-015

### Q-pattern-05 · Which deceptive patterns should the builder block? · Standard
- **Status:** planned. The engine has no deceptive-pattern lint yet (L13 E1). The interview skips this question and records nothing.
- **Why:** Fair defaults make 'Accept' and 'Decline' look equal and leave opt-in boxes unticked. They also word 'Decline' without guilt [DC-L13-15].
- **Ask:** "How firmly should we stop design tricks, like boxes ticked for you or a louder 'Yes' button?"
- **Example:** Show a consent dialog with equal buttons vs a "confirmshaming" one, flagged.
- **Control:** single choice
- **Options:**
  - `none` No policy [DC-L13-15].
  - `documented` A written ban on the 16 tricks at deceptive.design, like sneaking and fake urgency [S-L13-071].
  - `enforced` Written down, and blocked where a tool can spot it: pre-checked consent or marketing boxes and unequal accept/reject emphasis are lint errors; re-prompting after dismissal is flagged [S-L13-071, S-L13-108].
- **Default:** enforced. *Source:* card heuristic [DC-L13-15]; L13 E1 lint errors.
- **Decides:** DC-L13-15
- **Changes:** DC-L13-16 · blocks: Principles > Ethics > Deceptive patterns
- **Preview:** a consent dialog and a cancellation flow checked live.
- **Use / avoid:** use equal emphasis for accept and reject; avoid nagging and fake urgency (the Zeigarnik effect does not justify nags) [DC-L13-15; L13 E2].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 1)
- **Evidence:** DC-L13-15; S-L13-071, S-L13-108, S-L13-110

### Q-pattern-06 · What should small glance views show, like widgets, tiles and watch complications? · Expert
- **Show if:** Q-plat-02 marks watch or car first-class, or the product ships widgets
- **Why:** Glance views should look like data, not app screens: big numbers, one metric, a status color and almost no frame around them [DC-L14-07].
- **Ask:** "What one number or status should people see without opening the app?"
- **Example:** Ask for the one metric; show it as a watch complication and a home-screen widget.
- **Control:** text (metric) + single choice (surfaces)
- **Options:**
  - `priority-matrix` One fact per complication, one or two per tile, alerts when urgent, all in the app (Google) [S-L14-015].
  - `apple-surfaces` Complications, Smart Stack, Live Activities, CarPlay widgets [S-L14-001, S-L14-047].
- **Default:** design the complication or tile first, then the app; one number or status per glance. *Source:* card heuristic [DC-L14-07].
- **Decides:** DC-L14-07
- **Changes:** none downstream in the graph · blocks: Patterns > Surfaces > Glanceable
- **Preview:** the metric on each glance surface.
- **Use / avoid:** use tiles that are "immediate, predictable, relevant"; avoid shrinking app screens into widgets [S-L14-020; DC-L14-07].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L14-07; S-L14-001, S-L14-015, S-L14-020, S-L14-047
- **Merges:** D5

### Q-ai-01 · Does the product have AI features, and how should AI content be marked? · Standard
- **Why:** Clear AI labels and sources shown apart make AI output read as "assistive, check me". A separate AI accent color can compete with your main action color [DC-L13-16, DC-L08-22].
- **Ask:** "Does your product use AI, and if so, how should people spot and fix its work?"
- **Example:** Show an AI-generated summary with a label, citations, and Edit / Undo / Retry.
- **Control:** single choice + multi-select (surfaces)
- **Options:**
  - `none` No AI features.
  - `label-button` An AI tag and an AI button (Carbon AI label; S2 genai; Atlassian Rovo) [S-L08-009, S-L08-067, S-L08-063].
  - `presence-mode` An AI mode that normal parts can switch on: label, explainability popover, glow tokens, revert (Carbon) [S-L14-058].
  - `chat` Chat components for products people talk to (shadcn Message, Bubble; Carbon AI chat) [S-L08-018, S-L14-058].
  - `voice` Voice-only turns: one breath, 2-5 options (Alexa) [S-L14-065].
- **Default:** label-button as an optional module, chat only for conversational products; label AI content, place citations next to claims, express uncertainty in high-stakes contexts, and pair every generated output with Edit, Undo and Retry. *Source:* card heuristics [DC-L08-22, DC-L13-16, DC-L14-12; S-L13-089, S-L14-011].
- **Decides:** DC-L08-22, DC-L13-16, DC-L14-12
- **Changes:** DC-L05-18 (agent avatars) · blocks: Components > AI; Patterns > AI; Patterns > Conversational
- **Preview:** AI output in a table cell, a side panel and a chat thread.
- **Use / avoid:** use AI styling only on AI-generated content (Carbon warns against decoration); avoid human-sounding anthropomorphic framing and reasoning traces presented as explanations [DC-L14-12, DC-L13-16].
- **Skip:** yes, none.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L08-22, DC-L13-16, DC-L14-12; S-L08-009, S-L08-067, S-L13-089, S-L14-011, S-L14-058
- **Merges:** D6

---

## Stage 24 · Tokens and encoding
> Screen: a token browser beside the product preview; clicking any element shows its token chain (component, semantic, primitive) and the exported code for each platform. Graph step 0-5. Asked after the visual stages because nothing visual depends on it in the graph; everything here changes how the look is stored and shipped [inferred from the graph].

### Q-token-01 · How many token layers should sit between raw values and components? · Standard
- **Why:** A layer of role names (semantic tokens) lets you change the look, like a rebrand or a new mode, without touching components. 24 of the 25 systems we studied have one [DC-L07-01; L09 A1 row 1].
- **Ask:** "Should buttons and cards use raw colors and sizes, or go through layers of named values?"
- **Example:** Show `blue.600` -> `color.bg.accent` -> `button.primary.bg`, and which layer a rebrand edits.
- **Control:** single choice
- **Options:**
  - `one` One layer: palette and scales used directly (Tailwind); theming means find-and-replace [DC-L07-01].
  - `two-plus` Two layers, raw then role, plus component tokens when needed (Atlassian, Polaris; Fluent global + alias) [S-L07-107, S-L07-125, S-L01-033].
  - `three-full` Three layers for every part, raw, role, then part (Material 3; Primer base, functional, component) [S-L07-102, S-L01-027].
- **Default:** two-plus: primitives private, semantics public, component tokens only for components a brand must restyle or values shared by 3+ components; typography as primitives, semantic composites `text.{role}.{size}` and optional component aliases. *Source:* card heuristics [DC-L07-01, DC-L07-02, DC-L01-26, DC-L02-27]; L09 counts this as its 3-tier default with the component tier optional.
- **Decides:** DC-L07-01, DC-L07-02, DC-L01-26, DC-L02-27
- **Changes:** DC-L07-04, DC-L07-18, DC-L07-19 · blocks: Tokens > Architecture > Tiers; Component tokens
- **Preview:** the token chain inspector on the preview.
- **Use / avoid:** use semantic tokens in every component; avoid components referencing a raw hex or px (L09: 24 of 25 systems forbid it) [L09 A1 row 1].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L07-01, DC-L07-02, DC-L01-26, DC-L02-27; S-L07-003, S-L07-036, S-L07-108, S-L01-027
- **Merges:** K7.6 (tiers)

### Q-token-04 · Which units should the source use? · Expert
- **Why:** px maps cleanly to pt, dp and Figma. rem follows browser zoom, and plain numbers carry over 1:1 to every platform [DC-L07-11, DC-L10-08].
- **Ask:** "Should stored sizes be pixels, plain numbers, or rem (the web unit that grows with the browser's text size)?"
- **Example:** Show `16` becoming `1rem`, `16pt`, `16dp` and `16px`.
- **Control:** single choice + toggle (spacing scales with text)
- **Options:**
  - `px-to-rem` px in source, rem on the web (DTCG allows px and rem only; Figma imports px) [S-L07-002, S-L07-011, S-L03-037].
  - `unitless` Plain numbers in steps of 4, output 1:1 as pt, dp, epx or px; rem for web font sizes (Fluent's ramp) [S-L10-039].
  - `rem-source` rem in the source, turned into dp, sp or CGFloat by the build [DC-L10-08].
- **Default:** px-to-rem (equivalently unitless numbers), rem for web type and breakpoints; "spacing scales with text size" is an explicit toggle, off by default; line height unitless. *Source:* card heuristics [DC-L07-11, DC-L10-08, DC-L03-26].
- **Decides:** DC-L07-11, DC-L10-08, DC-L03-26
- **Changes:** DC-L10-22 · blocks: Tokens > Types > Dimension; Encoding > Units per platform
- **Preview:** one value converted per platform.
- **Use / avoid:** question any value not divisible by 4 (except 2, 6, 10 for icon nudges); avoid sp or rem for spacing that must not scale with text on Android [DC-L10-08; L10 baked-in rule 4].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L07-11, DC-L10-08, DC-L03-26; S-L03-037, S-L03-038, S-L07-002, S-L10-039, S-L10-070
- **Merges:** P9

### Q-token-08 · Which file format and build pipeline should produce platform code? · Expert
- **Why:** The build tool decides if tokens reach each codebase in the style that code already uses [DC-L07-25, DC-L10-22].
- **Ask:** "Which file format and build tool should turn your tokens into code for each platform?"
- **Example:** Show the output tree: CSS variables, Tailwind theme, Swift, Compose.
- **Control:** single choice (pipeline) + multi-select (outputs)
- **Options:**
  - `dtcg-resolver` DTCG 2025.10 + Resolver, one file per tier and mode (stable since 28 Oct 2025) [S-L07-002, S-L07-004].
  - `terrazzo` Terrazzo 2.x: full DTCG including resolvers, web-strong [S-L07-179].
  - `style-dictionary` Style Dictionary v5: widest native coverage (Compose, Android XML, Swift, Flutter), no resolver support, so one build per combination [S-L07-151, S-L07-162, S-L10-056].
  - `tokens-studio` Tokens Studio + sd-transforms, when designers author in the plugin [DC-L07-25].
  - `web-delivery` Web: CSS custom properties for semantics, media queries for preferences, container queries for components [S-L10-052, S-L10-031].
- **Default:** dtcg-resolver as the canonical export; Terrazzo for web-only teams, Style Dictionary v5 when native outputs are needed; web-delivery on the web. *Source:* card heuristics [DC-L07-09, DC-L07-25, DC-L10-22, DC-L10-18].
- **Decides:** DC-L07-09, DC-L07-25, DC-L10-22, DC-L10-18
- **Changes:** DC-L16-12 · blocks: Tokens > Architecture > File format; Tooling > Token pipeline; Tokens > Delivery
- **Preview:** the generated file tree with one file open.
- **Use / avoid:** use one canonical export and generate everything else from it; avoid hand-edited platform files [DC-L07-25].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L07-09, DC-L07-25, DC-L10-22, DC-L10-18; S-L07-002, S-L07-004, S-L07-155, S-L07-179, S-L10-056
- **Merges:** P19, P23

### Q-token-02 · How should tokens be named? · Expert
- **Why:** Token names are the shared words for people and AI agents. Use only as many name parts as it takes to tell tokens apart [DC-L07-04; S-L07-036].
- **Ask:** "What naming rules should tokens follow, so people and AI tools read them the same way?"
- **Example:** Show `ds.color.bg.accent.hover`, `space.200`, and `--ds-color-bg-accent-hover` in CSS.
- **Control:** grammar builder + text (prefix)
- **Options:**
  - `grammar` Names in a fixed order, like ds.color.bg.accent.hover, for roles and parts [DC-L07-04].
  - `primitives` Raw color names: hue + numeric step (50-950 or bounded 0-100); descriptive names only for brand colors [DC-L07-03].
  - `spacing-names` Space steps named by percent of base (space.200 = 16px; Atlassian, Material), and role names [S-L03-003, S-L03-030].
  - `prefix` A 2-4 letter prefix in code only (--ds-, --cds-, --md-); no theme or brand in names [S-L07-036, S-L07-108].
  - `casing` Lowercase JSON segments; kebab for CSS, camel for JS/Swift/Kotlin, snake for Android XML [S-L07-158].
- **Default:** all five as listed. *Source:* card heuristics [DC-L07-03, DC-L07-04, DC-L07-05, DC-L07-06, DC-L03-03].
- **Decides:** DC-L07-03, DC-L07-04, DC-L07-05, DC-L07-06, DC-L03-03
- **Changes:** DC-L07-20 · blocks: Tokens > Naming
- **Preview:** a name linter that shows each token's name in JSON, CSS, Swift and Kotlin.
- **Use / avoid:** use role names at the semantic tier; avoid `padding` or `margin` in primitive names and ordinal scales that look proportional but aren't [DC-L03-03].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L07-03, DC-L07-04, DC-L07-05, DC-L07-06, DC-L03-03; S-L07-003, S-L07-036, S-L07-158
- **Merges:** K7.6

### Q-token-03 · Which kinds of values should become tokens? · Expert
- **Why:** A value without a token drifts over time, and lint rules can't check it and themes can't change it [DC-L07-07].
- **Ask:** "Which kinds of values should get a token, from the basics up to almost all of them?"
- **Example:** Show the coverage list with counts per category.
- **Control:** single choice + checklist
- **Options:**
  - `minimal` Color, type, space [DC-L07-07].
  - `standard` Plus corners, borders, shadows, opacity and motion [DC-L07-07].
  - `extended` Plus layer order (z-index), breakpoints, icon sizes, touch targets and chart colors [DC-L07-07; S-L07-036].
- **Default:** extended; one-off illustration values stay untokenized. *Source:* card heuristic [DC-L07-07].
- **Decides:** DC-L07-07
- **Changes:** none downstream in the graph · blocks: Tokens > Scope > Coverage
- **Preview:** a coverage bar per category.
- **Use / avoid:** use tokens for anything a lint rule should check; avoid tokenizing one-off art values [DC-L07-07].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L07-07; S-L07-002, S-L07-036, S-L07-108

### Q-token-05 · How should bundled values like text styles, shadows and motion be stored? · Expert
- **Why:** Bundled tokens keep a style whole in code, and Figma styles bound to variables switch with each mode. DTCG has no type for springs [DC-L07-12, DC-L07-13, DC-L07-14, DC-L04-28].
- **Ask:** "How should styles made of several values, like a text style or a shadow, be stored?"
- **Example:** Show a `typography` composite in JSON and the Figma text style bound to its variables.
- **Control:** single choice per type
- **Options:**
  - `type` Typography: atomic primitives + semantic `typography` composites; Figma text styles with fields bound to variables (bind if more than one brand or platform) [S-L07-013, S-L07-019, S-L02-036].
  - `shadow` Shadows and borders: DTCG `shadow` and `border` composites; Figma effect styles with bound color and offsets [S-L07-002, S-L07-020].
  - `motion` Motion: DTCG `duration`, `cubicBezier`, `transition`; Figma timing and easing variables with a reduced-motion mode; springs as `{dampingRatio, stiffness}` in `$extensions` with a bezier fallback [S-L07-033, S-L04-052].
- **Default:** all three as listed. *Source:* card heuristics [DC-L07-12, DC-L07-13, DC-L07-14, DC-L04-28, DC-L02-28].
- **Decides:** DC-L07-12, DC-L07-13, DC-L07-14, DC-L04-28, DC-L02-28
- **Changes:** DC-L07-25 · blocks: Tokens > Types
- **Preview:** JSON and Figma views of one token of each type.
- **Use / avoid:** use variables for single values that change by mode and styles for bundles; avoid hard-coded style values [DC-L07-21].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L07-12, DC-L07-13, DC-L07-14, DC-L04-28, DC-L02-28; S-L07-002, S-L07-013, S-L07-019, S-L07-033

### Q-token-06 · How should themes and modes combine without too many versions to test? · Expert
- **Why:** Each extra setting, like dark mode or density, multiplies what you must test. If two settings change the same token, they should be one setting [DC-L07-17].
- **Ask:** "How should dark mode, contrast and density mix without too many versions to test?"
- **Example:** Show 2 schemes x 2 contrasts x 2 densities as additive collections instead of 8 flattened modes.
- **Control:** single choice
- **Options:**
  - `flatten` Every mix in one flat list (the DTCG resolver example: light, lightHighContrast, dark, darkHighContrast) [S-L07-004].
  - `orthogonal` Separate settings that never change the same tokens [DC-L07-17].
  - `collections` Figma collections: Primitives (hidden) + Semantic color + Semantic dimension (density or breakpoint) + Motion with a reduced mode [DC-L07-18].
  - `breakpoint-collection` A Breakpoint collection (3 modes) for layout, and grid auto layout for parts with columns [DC-L07-28; S-L07-024].
- **Default:** orthogonal with at most 3 axes plus collections and a breakpoint collection. *Source:* card heuristics [DC-L07-17, DC-L07-18, DC-L07-28].
- **Decides:** DC-L07-17, DC-L07-18, DC-L07-28
- **Changes:** none downstream in the graph · blocks: Tokens > Theming > Combinations; Figma > Variables > Collections; Tokens > Layout
- **Preview:** the combination count and the Figma mode budget from Q-tool-03.
- **Use / avoid:** use additive collections to stay within the plan's mode limit; avoid putting brand and scheme in one flattened axis [DC-L07-18, DC-L07-27].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L07-17, DC-L07-18, DC-L07-28; S-L07-004, S-L07-011, S-L07-014, S-L07-024

### Q-token-07 · How should the Figma library be kept clean? · Expert
- **Show if:** Q-tool-03 is a Figma plan
- **Why:** Hiding raw values and limiting where each variable shows up keeps designers on semantic tokens. Generated code names keep the names the same in Figma and in code [DC-L07-19, DC-L07-20].
- **Ask:** "How should the Figma library stay tidy, so designers pick the right values?"
- **Example:** Show a text-color variable offered only in text fill pickers.
- **Control:** toggles
- **Options:**
  - `hide-scope` Hide raw values, and offer each variable only where its name fits [S-L07-018, S-L07-025].
  - `code-syntax` Make Web, Android and iOS code names from the build's name rules [S-L07-018].
  - `vars-styles` Variables for values, styles for bundles [S-L07-019].
  - `check-designs` Run Check designs before "Ready for dev" and review library analytics quarterly (Org/Enterprise; the builder lints on Professional) [S-L07-025, S-L07-029].
- **Default:** all four. *Source:* card heuristics [DC-L07-19, DC-L07-20, DC-L07-21, DC-L07-26].
- **Decides:** DC-L07-19, DC-L07-20, DC-L07-21, DC-L07-26
- **Changes:** DC-L07-23 · blocks: Figma > Variables > Scope; Code syntax; Styles vs Variables; Governance > Tooling
- **Preview:** the Figma variable panel as a designer would see it.
- **Use / avoid:** use scopes so a spacing token cannot be picked for a color; avoid "show in all" scopes [DC-L07-19].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L07-19, DC-L07-20, DC-L07-21, DC-L07-26; S-L07-018, S-L07-019, S-L07-025, S-L07-029

### Q-token-09 · How should tokens be described and retired? · Expert
- **Why:** A short description tells people and AI agents what each token is for. Marking a token as old before deleting it protects the teams that use it [DC-L07-23].
- **Ask:** "How should each token explain its use, and how should old tokens be phased out?"
- **Example:** Show `$deprecated: "Use color.bg.accent instead"` in JSON and the warning in Figma.
- **Control:** toggles
- **Options:**
  - `descriptions` A short note ($description) on each semantic token [S-L07-002].
  - `deprecate` `$deprecated: true` or "Use X instead", one release before removal [S-L07-002].
  - `usage-check` Check library analytics before you remove it (Org/Enterprise) [S-L07-029].
- **Default:** all three. *Source:* card heuristic [DC-L07-23].
- **Decides:** DC-L07-23
- **Changes:** DC-L11-15 · blocks: Tokens > Governance > Lifecycle
- **Preview:** a token's detail card with description and status.
- **Use / avoid:** use descriptions written for agents as well as people; avoid deleting tokens without a replacement [DC-L07-23].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L07-23; S-L07-002, S-L07-029, S-L07-031, S-L07-042

### Q-token-10 · Which inputs should re-skin the theme, and what may other brands or clients customize? · Expert
- **Show if:** Q-theme-03 is not locked
- **Why:** Fewer inputs give themes that are more consistent and always accessible, but with less nuance. Linear swapped 98 per-theme variables for 3 inputs [DC-L06-06; S-L06-012]. When other brands restyle a product, they almost always change color and type [DC-L06-17; S-L06-053].
- **Ask:** "What should set the theme's look, and what may clients or other brands change?"
- **Example:** Show a client admin panel with a color picker, logo upload and a live contrast check.
- **Control:** multi-select (knobs) + single choice (surface)
- **Options:**
  - `inputs-3` Three generator inputs: brand color, neutral base or temperature, contrast (Linear) [S-L06-012; DC-L06-06].
  - `inputs-seed-variant` One source color plus a scheme variant and contrast level (Material) [S-L06-082, S-L06-083].
  - `code-one-color` One brand color in code (Blade `createTheme({brandColor})`) [S-L06-094].
  - `admin-ui` An admin page, "clicks, not code", for colors, logos, images and chosen accents (Salesforce SLDS 2) [S-L06-068].
  - `user-builder` A theme builder for your users (Linear base, accent, contrast) [S-L06-012].
  - `cms` Overrides people edit in the CMS [S-L06-053].
- **Default:** three generator inputs; clients may change brand color and logo, font and radius only with previews and validation. *Source:* card heuristics [DC-L06-06, DC-L06-17].
- **Decides:** DC-L06-06, DC-L06-17
- **Changes:** none downstream in the graph · blocks: Tokens > Theming > White-label controls
- **Preview:** the client panel re-skinning the preview with contrast re-checked.
- **Use / avoid:** use generated on-colors so client colors keep contrast; avoid exposing raw token editing to clients [DC-L06-17, DC-L06-16].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L06-06, DC-L06-17; S-L06-012, S-L06-053, S-L06-067, S-L06-068, S-L06-094

---

## Stage 25 · Team, governance and change
> Screen: a governance plan generated from earlier answers (team size, scope, platforms), shown as a one-page operating model the person edits. Graph step 1-7. Mostly Expert: these decisions change how the system evolves, not how it looks.

### Q-gov-01 · How strict should the system be: can product teams override or extend it? · Standard
- **Why:** A strict system stays consistent but feels rigid, and a loose one allows experiments but drifts. A strict core with loose edges is the practical middle [DC-L11-03].
- **Ask:** "How strict should the system be, and can product teams change it or add their own parts?"
- **Example:** Show which layers are locked and which are open under each option.
- **Control:** single choice
- **Options:**
  - `strict` Strict: comprehensive docs, design and code fully synced, little deviation [S-L11-018, S-L11-019].
  - `loose` Loose: a framework with room to experiment [S-L11-019].
  - `canon-expanded` A strict core, plus team-owned add-ons, the "expanded universe" (Dan Mall) [S-L11-014].
- **Default:** strict core (tokens, primitives, accessibility behavior), loose edges (patterns, marketing). *Source:* card heuristic [DC-L11-03].
- **Decides:** DC-L11-03
- **Changes:** DC-L11-11, DC-L11-12, DC-L11-24 (lint strictness) · blocks: Strategy > Posture
- **Preview:** a layer diagram with lock icons per layer.
- **Use / avoid:** use a snowflake path for one-off needs; avoid forcing every product-specific component into the core [DC-L11-03, DC-L11-12].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L11-03; S-L11-014, S-L11-018, S-L11-019
- **Merges:** K6.5, K8.4

### Q-gov-02 · In what order will you build, pilot and roll out? · Expert
- **Why:** Foundations first is tidy but abstract. A pilot product keeps components real. Launching all at once draws attention but risks bias toward that pilot [DC-L11-06, DC-L11-07, DC-L11-08].
- **Ask:** "In what order will you build the system, try it in one product, and roll it out?"
- **Example:** Show Dan Mall's 8-criteria pilot scorecard filled for two candidate products.
- **Control:** single choice (order) + scorecard (pilot) + single choice (rollout)
- **Options:**
  - `foundations-first` Foundations first: spacing, color, type, elevation, icons, then components (Figma course order) [S-L11-009].
  - `pilot-driven` Start with a pilot product: extract components from a real product, apply to the next [S-L11-014].
  - `pilot-scorecard` Pick the pilot by 8 tests, like shared parts, a champion, a 3-4 week scope and few ties to old code [S-L11-105].
  - `rollout-incremental` Roll out step by step, worst problems first; all at once only with a rebrand [S-L11-105].
- **Default:** minimal foundations first, then pilot-driven components, incremental rollout. *Source:* card heuristics [DC-L11-06, DC-L11-07, DC-L11-08].
- **Decides:** DC-L11-06, DC-L11-07, DC-L11-08
- **Changes:** DC-L11-01, DC-L11-22 · blocks: Process > Build order; Process > Pilot; Adoption > Rollout
- **Preview:** a timeline of the plan.
- **Use / avoid:** use a second pilot from a different product family to reduce bias; avoid building components no pilot needs [DC-L11-07].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L11-06, DC-L11-07, DC-L11-08; S-L11-009, S-L11-014, S-L11-105, S-L11-107
- **Merges:** K2.7, K2.8, K13.1

### Q-gov-03 · Who can contribute, and how are decisions made and recorded? · Expert
- **Why:** Only 36% of teams are happy with how people add to their system. Decision records explain why things are the way they are [DC-L11-11, DC-L11-12; S-L11-030].
- **Ask:** "Who can add to the system, and how will decisions be made and written down?"
- **Example:** Show a decision record generated from one of this session's answers.
- **Control:** single choice (contribution) + toggle (decision records)
- **Options:**
  - `closed` Closed or narrow: fixes and small enhancements only (Atlassian) [S-L11-024].
  - `criteria-gated` Open, with checks: proposals must be useful and unique; publication must be usable, consistent, versatile (GOV.UK) [S-L11-021].
  - `two-lanes` A fast lane for fixes, icons and docs; a proposal (RFC) lane for new components [S-L11-020, S-L11-021].
  - `frost-flow` Brad Frost's 10-step flow, with a path for one-off needs [S-L11-003].
  - `adrs` Decision records (ADRs) from day one, made from your answers here [S-L11-095; inferred].
- **Default:** two-lanes, frost-flow and adrs. *Source:* card heuristics [DC-L11-11, DC-L11-12].
- **Decides:** DC-L11-11, DC-L11-12
- **Changes:** DC-L11-13 · blocks: Governance > Contribution; Governance > Process
- **Preview:** the generated decision log.
- **Use / avoid:** record why an option was chosen and what it beat; avoid undocumented overrides [DC-L11-12].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L11-11, DC-L11-12; S-L11-003, S-L11-020, S-L11-021, S-L11-024, S-L11-095
- **Merges:** K9.4, K9.5, K9.6, K9.7

### Q-gov-04 · How should each part get a status, a version number, and a way to retire? · Expert
- **Why:** Clear status labels and version numbers protect the teams that use your components. Breaking changes without warning wear away their trust [DC-L11-13, DC-L11-14, DC-L11-15].
- **Ask:** "How should you mark each component's status, number its versions, and retire old ones?"
- **Example:** Show a changelog entry with a deprecation and its codemod.
- **Control:** single choice per item
- **Options:**
  - `status-3` Experimental, then Ready, then Deprecated (Primer cut five to three) [S-L11-025, S-L11-026].
  - `semver-library` One SemVer for the whole library while small; one per package on many platforms [S-L11-106, S-L11-028].
  - `per-component` A version number for each component (Atlassian, Paste) [S-L11-028].
  - `deprecation-polaris` Warn with @deprecated in a minor release, ship codemods, drop it in the next major (Polaris) [S-L11-100].
- **Default:** status-3, semver-library, deprecation-polaris with at least one release cycle of notice; release notes every release (the most common ritual, 56%). *Source:* card heuristics [DC-L11-13, DC-L11-14, DC-L11-15; S-L11-030].
- **Decides:** DC-L11-13, DC-L11-14, DC-L11-15
- **Changes:** DC-L11-22 · blocks: Governance > Component status; Change > Versioning; Change > Deprecation
- **Preview:** status badges in the catalog and a sample changelog.
- **Use / avoid:** pair every removal with a migration path; avoid breaking changes in minor releases [DC-L11-14, DC-L11-15].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L11-13, DC-L11-14, DC-L11-15; S-L11-025, S-L11-028, S-L11-100, S-L11-106
- **Merges:** K8.5, K10.2, K10.3, K10.4

### Q-gov-05 · What problem is the system solving, and how will you know it worked? · Expert
- **Why:** The problem you are solving sets how you measure success. Most teams measure how much the system is used, but only 5% measure return on investment (ROI) [DC-L11-20; S-L11-030].
- **Ask:** "What problem hurts most today, and how will you measure whether the system helped?"
- **Example:** Show an adoption dashboard mock with the three starting metrics.
- **Control:** multi-select (pain) + multi-select (metrics)
- **Options:**
  - `pain` Biggest problem: inconsistency, speed, accessibility, rebrand, AI output drift, multi-platform parity [S-L11-083].
  - `adoption` Design use and code use (Figma analytics; a scanner like Omlet or react-scanner) [S-L11-035, S-L11-037, S-L11-039].
  - `satisfaction` A survey every quarter on how happy people are with it [S-L11-030].
  - `maturity` Stage of growth: building v1, growing adoption, surviving the teenage years, evolving (Sparkbox) [S-L11-033].
- **Default:** design adoption, code adoption and a quarterly survey; most builder users are at stage 1. *Source:* card heuristics [DC-L11-20, DC-L11-21].
- **Decides:** DC-L11-20, DC-L11-21
- **Changes:** none downstream in the graph · blocks: Measurement > Metrics; Measurement > Maturity
- **Preview:** the metrics dashboard mock.
- **Use / avoid:** add speed or ROI studies only when leadership asks; avoid vanity counts of components [DC-L11-20].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 1)
- **Evidence:** DC-L11-20, DC-L11-21; S-L11-030, S-L11-033, S-L11-035, S-L11-037, S-L11-083
- **Merges:** K0.1, K0.2, K0.3, K1.3, K12.1, K12.2, K12.3, K12.4

### Q-gov-06 · How will you announce the system and communicate changes? · Expert
- **Why:** How you share changes matters: only 39% of teams are happy with how changes to their design system are shared [DC-L11-22; S-L11-030].
- **Ask:** "How will you tell people about the system and about each change?"
- **Example:** Show a release-note template filled from a recent change.
- **Control:** multi-select
- **Options:**
  - `release-notes` Release notes (56% of teams) [S-L11-030].
  - `roadmap` Roadmap (48%) [S-L11-030].
  - `office-hours` Office hours (33%) [S-L11-030].
  - `training` Training, pairing, success stories (Frost) [S-L11-002].
- **Default:** release notes, a public roadmap and a support channel. *Source:* card heuristic [DC-L11-22].
- **Decides:** DC-L11-22
- **Changes:** none downstream in the graph · blocks: Adoption > Communication
- **Preview:** the release-note template.
- **Use / avoid:** use changelogs that name the migration; avoid silent releases [DC-L11-22].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L11-22; S-L11-002, S-L11-030, S-L11-105
- **Merges:** K0.4, K13.3, K13.4

### Q-gov-07 · Which assistive tools must you test on each device, and who owns accessibility? · Expert
- **Why:** Automated checks find only about 30% of issues. If a kind of device gets full support, its assistive tools need full support too [DC-L14-14; S-L11-093].
- **Ask:** "On each kind of device you ship, which screen readers, control tools and text sizes will you test?"
- **Example:** Show the generated test matrix for the chosen platforms.
- **Control:** matrix (device class x assistive tech) + text (owner)
- **Options:**
  - `screen-readers` VoiceOver on Apple, TalkBack on Android phone, Wear and TV, NVDA/JAWS on web [S-L14-080, S-L10-072].
  - `motor` Switch Control, Voice Control, Full Keyboard Access, Dwell Control [S-L14-079, S-L14-007].
  - `text-scale` Largest text: Dynamic Type AX5, Android 200%, watch 140% [S-L10-011, S-L10-071].
- **Default:** one screen reader, one motor alternative and the largest text size per shipped device class; a named accessibility owner (44% of teams lack a specialist). *Source:* card heuristic [DC-L14-14; S-L11-030].
- **Decides:** DC-L14-14
- **Changes:** none downstream in the graph · blocks: Governance > Accessibility > Device test matrix
- **Preview:** the test matrix with pass/untested status per cell.
- **Use / avoid:** use manual assistive-technology testing on every release candidate; avoid treating automated scans as compliance [DC-L11-19, DC-L14-14].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L14-14; S-L10-072, S-L11-093, S-L14-007, S-L14-079, S-L14-080
- **Merges:** K4.3, K4.5, D7

---

## Stage 26 · Output, documentation and AI channels
> Screen: the export menu and a preview of every file the builder will produce: tokens, code, docs pages, DESIGN.md, lint rules. Graph step 2-4. These outputs are what keep the system coherent in later sessions and explainable to a team (BRIEF requirements 9 and 10).

### Q-dist-01 · How should the system leave the builder? · Standard
- **Status:** planned. Today the system leaves as token files, code exports and Figma or Paper writes (`engine.py export`). The install command, pull request and MCP tool channels are not built. The interview skips this question and records nothing.
- **Why:** Engineers need the output in a form they already use. It can be a snippet, an install command, a token file, a pull request or a design file [DC-L16-12].
- **Ask:** "In what forms should the system leave the builder: code, a command, files, a pull request, or Figma?"
- **Example:** Show the export menu with one command per channel (for example `npx shadcn@latest add <url>`).
- **Control:** multi-select
- **Options:**
  - `copy-css` Copy snippets (Radix "Copy Theme", Utopia CSS) [S-L16-323, S-L16-341].
  - `cli-url` A one-line install command from a URL (tweakcn via shadcn) [S-L16-333, S-L16-328].
  - `dtcg` Token files (Leonardo "Copy Tokens") [S-L16-338].
  - `pr` A pull request to the repository [DC-L16-12].
  - `design-push` Push to Figma or Paper through MCP [S-L16-002, S-L16-020].
  - `mcp-tool` Make the builder's generator an MCP tool that AI can call (Leonardo's example) [S-L16-338].
- **Default:** all six from one menu. *Source:* card heuristic [DC-L16-12].
- **Decides:** DC-L16-12
- **Changes:** none downstream in the graph · blocks: Builder > Output > Channels
- **Preview:** the export menu and file tree.
- **Use / avoid:** use one canonical source for every channel (Q-tool-01); avoid channels that fork the source [DC-L16-02].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L16-12; S-L16-002, S-L16-323, S-L16-333, S-L16-338

### Q-dist-04 · Where do docs live, and what goes on each component page? · Expert
- **Why:** Docs are how teams learn when to use each piece, and when not to. The core that systems share is usage advice, live examples, API and accessibility [DC-L11-17, DC-L11-18; L09 A1 row 9].
- **Ask:** "Where should the docs live, and what should each component's page show?"
- **Example:** Show the generated Button page.
- **Control:** single choice (platform) + template editor
- **Options:**
  - `figma-storybook` Figma plus Storybook (69% and 61% of teams) [S-L11-030].
  - `docs-platform` A docs tool (zeroheight, Supernova), when people who don't code write the docs [S-L11-088].
  - `custom-site` A custom site (Material, Carbon) [S-L11-088].
  - `carbon-template` Page template: live demo, accessibility status, when to use and not, anatomy, content rules, behaviors, per-variant guidance (Carbon Usage tab; M3 Overview/Specs/Guidelines/Accessibility) [S-L11-090, S-L08-033].
- **Default:** a generated site with the Carbon-style template plus "when not to use" and a changelog, and an llms.txt or MCP twin; docs complete is part of "done". *Source:* card heuristics [DC-L11-17, DC-L11-18, DC-L08-23].
- **Decides:** DC-L11-17, DC-L11-18, DC-L08-23
- **Changes:** none downstream in the graph · blocks: Docs > Platform; Docs > Component page
- **Preview:** a generated component page.
- **Use / avoid:** use generated "use it for / avoid it for" notes from this questionnaire on every page; avoid docs that repeat props without guidance [DC-L11-18].
- **Skip:** yes.
- **Block class:** G (generatable)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L11-17, DC-L11-18, DC-L08-23; S-L11-030, S-L11-088, S-L11-090, S-L08-033
- **Merges:** K11.1, K11.2, K11.3

### Q-dist-02 · How should AI coding tools read the system? · Standard
- **Status:** planned. Today every system ships DESIGN.md plus DTCG files. The MCP server, llms.txt, rules files and registry are not built. The interview skips this question and records nothing.
- **Why:** 59% of teams say some UI gets built around their design system. Channels made for AI agents make the UI they generate follow it [DC-L11-23; S-L11-031].
- **Ask:** "How should AI coding tools like Claude, ChatGPT, Codex or Cursor read your system?"
- **Example:** Show a DESIGN.md excerpt and an agent's generated button using the tokens.
- **Control:** multi-select
- **Options:**
  - `mcp` An MCP server (Figma MCP at mcp.figma.com; Storybook MCP; shadcn MCP) [S-L11-041, S-L11-044, S-L11-045].
  - `design-md` DESIGN.md plus DTCG files [S-L11-047].
  - `llms-txt` llms.txt and Markdown twins of docs (Cloudscape, Geist) [S-L11-048; L09 A1 row 10].
  - `rules` Rules files for AI agents (from Figma's create_design_system_rules) [S-L11-041].
  - `registry` A component registry (shadcn) [S-L11-045].
- **Default:** at least one live channel (MCP) and one file channel (DESIGN.md + DTCG), guidelines as many short structured files. *Source:* card heuristic [DC-L11-23]; L09 shared pattern row 10 (12 of 25 systems).
- **Decides:** DC-L11-23
- **Changes:** DC-L11-24 · blocks: Distribution > Agent context
- **Preview:** the agent-facing files and a sample agent answer.
- **Use / avoid:** use evals to check agents follow the files; avoid assuming docs changes alone steer agents [DC-L11-23; S-L11-108].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L11-23; S-L11-031, S-L11-041, S-L11-045, S-L11-047, S-L11-108
- **Merges:** K11.4, K11.5

### Q-dist-03 · How should the system check that people and agents follow it? · Standard
- **Status:** planned. Today `engine.py review` scans code for raw values. Shipped lint rules and agent evals are not built. The interview skips this question and records nothing.
- **Why:** When AI agents built with a design system, lint rules and structured docs cut accessibility errors. They fell from 5.1 to 0.6 per round in Sanity's evals [DC-L11-24; L13 E3].
- **Ask:** "How should we catch screens that break the system's rules, whether a person or AI made them?"
- **Example:** Show a lint result: "raw hex #3b82f6, use color.bg.accent".
- **Control:** multi-select (pre-filled from Q-gov-01 and Q-pref-01)
- **Options:**
  - `lint-rules` Lint rules shipped with the tokens, like target size, labels and one main button [DC-L11-24; L13 E3].
  - `adherence-scan` Scans that catch raw colors and one-off components (Lovable) [S-L11-053].
  - `drift-audit` Drift detection at the docs layer (zeroheight MCP) [S-L11-104].
  - `evals` Tests that measure how well AI agents follow the system (evals) [S-L11-108].
- **Default:** lint-rules plus evals. *Source:* card heuristic [DC-L11-24].
- **Decides:** DC-L11-24
- **Changes:** none downstream in the graph · blocks: Governance > AI guardrails
- **Preview:** the lint report for the preview screen.
- **Use / avoid:** use lint errors for Tier A rules and warnings for context-dependent ones (L13 E1); avoid automating the misapplied laws in L13 E2 (no seven-item caps) [L13 E1, E2].
- **Skip:** yes.
- **Block class:** T (tool-assisted)
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L11-24; S-L11-053, S-L11-104, S-L11-108, S-L00-036
- **Merges:** K11.6

---

## Stage 27 · Builder preferences
> Screen: how the builder (or the interviewing model) behaves while the person keeps editing. Graph step 0-5. Can be changed at any time.

### Q-pref-01 · How strict should the builder's critique be? · Standard
- **Status:** planned. The engine has no critique modes yet: `validate` always reports errors and warnings, and `build` stops on errors. The interview skips this question and records nothing.
- **Why:** Tips that name the design principle teach people the words for it. Strict mode stops export when something fails badly [DC-L15-11; S-L15-070].
- **Ask:** "Should I give tips as you go, stay quiet, or block export on serious problems like contrast?"
- **Example:** Show one coach message: "Two primary buttons in this group; make one secondary."
- **Control:** single choice
- **Options:**
  - `silent` Silent: only automatic rules apply [DC-L15-11].
  - `coach` Coach: inline messages tied to a goal, each with a one-click fix (NN/g goal-linked critique) [S-L15-075].
  - `strict` Strict: block export on contrast, multiple primaries and undersized targets; warn on the rest [DC-L15-11].
  - `metrics` Plus a panel that scores how complex and colorful it is [S-L15-047].
- **Default:** coach for engineers exploring; strict for teams shipping to production. *Source:* card heuristic [DC-L15-11].
- **Decides:** DC-L15-11
- **Changes:** DC-L11-24 lint severity · blocks: Builder > Guidance > Feedback mode
- **Preview:** the preview screen with messages at each level.
- **Use / avoid:** accessibility failures are at least warnings in every mode; avoid silent mode for production exports [DC-L15-11].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L15-11; S-L15-047, S-L15-070, S-L15-075, S-L15-080

### Q-pref-02 · How should AI edits and variations work? · Expert
- **Status:** planned. Patch review, lock-and-shuffle and the variation grid are not built; locks exist (`engine.py lock`). The interview skips this question and records nothing.
- **Why:** Your own edits do exactly what you set, and AI edits come as patches you review, so you keep control and trust. Lock-and-shuffle tries new options without losing what you like [DC-L16-04, DC-L16-05].
- **Ask:** "When the AI changes your design, how should you review it and try other versions?"
- **Example:** Show a "show 6 variations" grid with two locked parameters.
- **Control:** toggles
- **Options:**
  - `patches` AI changes arrive as patches you review, with before and after views [DC-L16-04].
  - `staged` Your own edits wait, then save all at once (Figma Make) [S-L16-026].
  - `lock-shuffle` Lock what you like and shuffle the rest, for every setting (shadcn create, Realtime Colors) [S-L16-327, S-L16-335].
  - `show-6` A "show 6" grid of versions on the same sample screen [DC-L16-05].
- **Default:** patches, lock-shuffle and show-6; vary only what is not locked. *Source:* card heuristics [DC-L16-04, DC-L16-05].
- **Decides:** DC-L16-04, DC-L16-05
- **Changes:** none downstream in the graph · blocks: Builder > AI > Edit model; Builder > Exploration > Variation
- **Preview:** the variation grid.
- **Use / avoid:** use variations for open, taste-driven questions (color, type, radius); avoid shuffling locked or accessibility-bound values [DC-L16-05].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L16-04, DC-L16-05; S-L16-026, S-L16-031, S-L16-327, S-L16-335

### Q-pref-03 · Should the builder fix shapes that look wrong to the eye, even when the math is right? · Expert
- **Why:** Exact sizes can look wrong: a circle looks smaller than a square in the same box. The known fixes have formulas [DC-L15-10; S-L15-058].
- **Ask:** "How should the builder handle shapes that look off to the eye, like icon sizes and nested corners?"
- **Example:** Show a circle icon at 100% vs 112.84% of a square's box.
- **Control:** single choice
- **Options:**
  - `geometric` Exact math only: exact values [DC-L15-10].
  - `auto-known` Fix known cases for you: area-matched shapes (circle 112.84%), Material keylines, centroid centering, concentric nested radii [S-L15-058, S-L15-059].
  - `suggest` Suggest only [DC-L15-10].
- **Default:** auto-known for generated assets, suggest for custom assets. *Source:* card heuristic [DC-L15-10].
- **Decides:** DC-L15-10
- **Changes:** none downstream in the graph · blocks: Foundations > Visual language > Polish
- **Preview:** before/after pairs for each correction.
- **Use / avoid:** use formulas where they exist; avoid correcting brand assets without approval [DC-L15-10].
- **Skip:** yes.
- **Block class:** I (owner input)
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L15-10; S-L15-055, S-L15-058, S-L15-059

---

## Auto-applied rules (decided by construction, never asked)

These cards have one defensible answer backed by a platform rule, an accessibility rule or strong evidence, so the builder applies them and shows them as locked rules with a reason (L13 E1 level "Default"; L15 "Automate" stance). Each can be overridden in Expert mode with a written rationale.

| Card | Rule the builder applies | Evidence |
|---|---|---|
| DC-L03-20 | Backgrounds edge-to-edge; interactive content inside platform insets plus the layout margin; nothing on a foldable hinge | S-L03-032, S-L03-052, S-L03-071 |
| DC-L14-10 | Safe zones per device: nothing to read or select in the outer 5% on TV; percentage margins on round watches; car targets 24dp from edges | S-L14-023, S-L14-026, S-L14-017, S-L14-032 |
| DC-L04-05 | Nested radius: inner = max(outer - padding, smallest non-zero radius); warn on equal nested radii | S-L04-057, S-L04-035 |
| DC-L04-14, DC-L03-23 | Layer order as named layers spaced by 100: base < sticky < dropdown < overlay/scrim < modal < popover/tooltip < toast < skip link; no hard-coded z-index | S-L04-024, S-L03-040 |
| DC-L04-16 | Every translucent token ships with an opaque twin, honoring Reduce Transparency and `prefers-reduced-transparency` | S-L04-011, S-L04-065 |
| DC-L05-17 | Images always reserve their final box; neutral placeholder fill; skeletons only on container components | S-L05-068, S-L05-071 |
| DC-L05-24 | Chart chrome (titles, ticks, gridlines, legends) maps to existing text and border tokens; chart-specific tokens only for marks and interaction | S-L05-077, S-L05-083 |
| DC-L05-25 | Every chart gets an insight title, direct labels or shape-coded legend, a text summary and "view as table" | S-L05-036, S-L05-077, S-L05-083 |
| DC-L13-04 | Docs and generated pages use a heading per section, front-loaded paragraphs, bullets for 3+ items | S-L13-062 |
| DC-L13-12 | Each interactive component documents trigger, rules, feedback, loops and modes plus its state list | S-L13-079, S-L13-106 |
| DC-L02-22 | Text survives WCAG 1.4.12 overrides (line height 1.5x, paragraph 2x, letter 0.12x, word 0.16x); no fixed-height text boxes | S-L02-027 |
| DC-L02-23 | Every text style is contrast-checked in every mode; below 18.5px bold / 24px regular it needs 4.5:1 | S-L02-007, S-L02-052 |

## Not asked: builder product decisions

These L16, L17 and L18 cards describe how the builder and the OpenDesigner package work (for the builder spec), not choices a person makes about their design system. Where this file applies one, the row says how.

| Card | What it decides for the builder |
|---|---|
| DC-L16-01 | Primary interaction model (canvas, panels, conversation) |
| DC-L16-03 | Canvas rendering substrate |
| DC-L16-06 | Preview surface: real components on the person's own screens, not only swatches |
| DC-L16-07 | Feedback latency budget for live previews |
| DC-L16-08 | State, undo, versioning and sharing of builder sessions |
| DC-L16-09 | Review and visual diff |
| DC-L16-10 | Keyboard-first operation and command palette |
| DC-L16-11 | Multiplayer and agent presence |
| DC-L16-14 | Control widgets for foundation parameters (sliders, pickers) |
| DC-L16-15 | Guardrails inside the editing loop |
| DC-L17-01 | Block classification (G/E/D/T/I): applied as the Block class line on every question |
| DC-L17-04 | Designer-hook policy: applied as the grouped checklist (Q-brand-08) and the fallback order on every Hook line |
| DC-L17-05 | Variant generation ("show me options"): applied in Q-pref-02 previews |
| DC-L17-06 | Proposal framing (safe choices vs risks): applied in the direction gate |
| DC-L17-07 | Anti-generic guardrails: applied through the Use / avoid lines and the critique mode (Q-pref-01) |
| DC-L17-08 | Pacing: applied as Time weight and protocol step 12 |
| DC-L17-09 | Coverage check and completeness scoring: applied in protocol step 11 and by the build script's coverage check |
| DC-L17-10 | What the process records: applied in protocol steps 5, 7 and 13 |
| DC-L17-11 | Preview substrate during the process: applied in the Preview lines |
| DC-L17-12 | Approval gates: applied in protocol step 11 |
| DC-L17-13 | The per-block detail panel: applied as the Preview and Use / avoid lines |
| DC-L18-01 | Primary delivery unit of the OpenDesigner package |
| DC-L18-02 | Repo layout for multi-host discovery |
| DC-L18-03 | Plugin manifests and distribution channels |
| DC-L18-04 | Knowledge format and chunking (this JSON is one stage or question per line for that reason) |
| DC-L18-05 | MCP server scope, hosting and auth |
| DC-L18-06 | Visual surface ladder: applied in protocol step 9 |
| DC-L18-07 | How a visual choice returns to the model |
| DC-L18-08 | Interview pacing: applied as Time weight and protocol step 10 |
| DC-L18-09 | Question format: applied in protocol step 10 |
| DC-L18-10 | Durable outputs: applied in protocol step 13 |
| DC-L18-11 | Enforcement shipped with the system: applied in Q-dist-03 and protocol step 13 |
| DC-L18-12 | The "extend" session protocol |
| DC-L18-13 | Design-tool round trip inside AI hosts |
| DC-L18-14 | Trust and safety of the package |

## Merge log

All 125 source questions were placed; none was dropped outright. The table lists where each went; the notes after it cover the judgment calls.

| Source | Where each question went |
|---|---|
| L11 kickoff (K, 77) | K0.1 Q-gov-05; K0.2 Q-gov-05; K0.3 Q-gov-05; K0.4 Q-gov-06; K0.5 Q-scope-05; K1.1 Q-scope-03, Q-aud-01; K1.2 Q-brand-07; K1.3 Q-gov-05; K1.4 Q-scope-04; K1.5 Q-scope-02; K1.6 Q-scope-02; K2.1 Q-scope-01; K2.2 Q-scope-01, Q-plat-01; K2.3 Q-plat-08; K2.4 Q-tool-03; K2.5 Q-tool-01; K2.6 Q-scope-05, Q-comp-01; K2.7 Q-gov-02; K2.8 Q-gov-02; K3.1 Q-brand-03; K3.2 Q-brand-07; K3.3 Q-ref-01, Q-brand-01, Q-brand-02; K3.4 Q-color-01, Q-color-09; K3.5 Q-type-01, Q-type-02; K3.6 Q-voice-01; K4.1 Q-aud-03; K4.2 Q-aud-03; K4.3 Q-gov-07; K4.4 Q-aud-04, Q-type-17, Q-motion-10; K4.5 Q-gov-07; K5.1 Q-type-04; K5.2 Q-type-04; K5.3 Q-voice-06; K5.4 Q-voice-06; K5.5 Q-voice-06; K6.1 Q-theme-01; K6.2 Q-theme-03; K6.3 Q-dir-02, Q-theme-02, Q-space-09; K6.4 Q-theme-02; K6.5 Q-gov-01; K7.1 Q-color-01; K7.2 Q-type-08; K7.3 Q-space-01; K7.4 Q-shape-01, Q-motion-01; K7.5 Q-icon-01, Q-img-01, Q-img-04; K7.6 Q-token-01, Q-token-02; K8.1 Q-comp-02; K8.2 Q-comp-04; K8.3 Q-layout-04; K8.4 Q-gov-01; K8.5 Q-gov-04; K9.1 Q-scope-03; K9.2 Q-scope-04; K9.3 Q-scope-04; K9.4 Q-gov-03; K9.5 Q-gov-03; K9.6 Q-gov-03; K9.7 Q-gov-03; K10.1 Q-tool-02; K10.2 Q-gov-04; K10.3 Q-gov-04; K10.4 Q-gov-04; K10.5 Q-tool-01; K11.1 Q-dist-04; K11.2 Q-dist-04; K11.3 Q-dist-04; K11.4 Q-dist-02; K11.5 Q-dist-02; K11.6 Q-dist-03; K12.1 Q-gov-05; K12.2 Q-gov-05; K12.3 Q-gov-05; K12.4 Q-gov-05; K13.1 Q-gov-02; K13.2 Q-scope-04; K13.3 Q-gov-06; K13.4 Q-gov-06 |
| L06 brand (B, 15) | B1 Q-aud-01, Q-aud-02; B2 Q-aud-02; B3 Q-ref-01, Q-brand-02; B4 Q-brand-02; B5 Q-brand-01; B6 Q-brand-01; B7 Q-brand-08, Q-brand-03, Q-color-01, Q-type-02, Q-motion-08, Q-img-04; B8 Q-type-01; B9 Q-color-06; B10 Q-theme-03; B11 Q-scope-01, Q-brand-05; B12 Q-brand-07; B13 Q-voice-01, Q-voice-02; B14 Q-type-04; B15 Q-aud-03, Q-aud-04, Q-motion-07 |
| L10 platform (P, 26) | P1 Q-plat-01; P2 Q-plat-02; P3 Q-plat-05; P4 Q-plat-07; P5 Q-color-02; P6 Q-color-06; P7 Q-type-01; P8 Q-type-17; P9 Q-token-04; P10 Q-layout-04; P11 Q-layout-02; P12 Q-depth-04; P13 Q-depth-04; P14 Q-plat-06; P15 Q-motion-09; P16 Q-plat-03; P17 Q-motion-10; P18 Q-theme-01; P19 Q-token-08; P20 Q-plat-08; P21 Q-plat-08; P22 Q-plat-08; P23 Q-token-08; P24 Q-plat-09; P25 Q-plat-02; P26 Q-icon-01 |
| L14 device extract (D, 7) | D1 Q-plat-02; D2 Q-plat-03; D3 Q-plat-02; D4 Q-plat-04; D5 Q-pattern-06; D6 Q-ai-01; D7 Q-gov-07 |

Judgment calls:
- **Folded into generated outputs rather than asked:** K4.2 (what the system guarantees vs product teams) becomes a responsibility statement the builder writes under Q-aud-03, as GOV.UK publishes one [S-L11-092]. K1.4 (who attends the kickoff) and K9.1 (makers and users) are folded into team questions because they do not change the system's output [inferred].
- **Split across several questions:** B7 (existing brand assets) became one asset hook per asset (logo, colors, typeface, sounds, illustration) to meet the brief's "do you have this?" rule. K3.3 (feel and reference products) became the reference-intake panel plus Q-brand-01 and Q-brand-02. K7.1-K7.6 (L11's pointers into the foundation lanes) were replaced by the detailed foundation stages.
- **Merged because two lanes asked the same thing:** L10 P3 and L06's deference level (DC-L10-02 + DC-L06-14) are one question (Q-plat-05); S1c's graph overrides confirm they are one decision. L09's eight benchmark cards were merged into the matching lane questions (for example DC-L09-01 with DC-L04-02 in Q-shape-01).
- **Moved later than the source asked:** L06 suggests starting with its 15 brand questions; this flow asks scope and audience first because they set the ceilings the personality sliders must respect (category trust, density), then brand [L06 cross-lane note; inferred]. K2.5 (source of truth) stays early (Stage 05) because every preview depends on the output target.

## Where lanes or systems disagree (present these as options, not a single answer)

| Question | The disagreement | What the builder should present |
|---|---|---|
| Q-plat-01 | Default platforms: L10 recommends web + iOS + Android phones with large-screen layouts [DC-L10-01]; survey data shows 94% of systems support web and about a third support native [S-L11-030]; L09 finds web-only most common [L09 A2 row 10]. | Default to web, and show the native options with what each adds (chrome, units, targets). |
| Q-tool-01 | Source of truth: L16 and L11 favor the builder's own model [DC-L16-02, DC-L11-16]; L07 favors DTCG JSON in git [DC-L07-08]; the 2026 practitioner majority says code [COMMUNITY-SIGNAL via DC-L11-16]. | All four options with the drift trade-off; default builder model compiled to DTCG and code. |
| Q-form-02 | Disabled submit: Carbon disables on short forms [S-L08-106]; Atlassian never disables [S-L08-085]; Material's disabled components are not focusable [S-L08-095]. BOARD also flags tooltips on disabled controls as contested. | Offer both policies; default never-disable with `aria-disabled` and helper text. |
| Q-form-04 | Toasts: Primer ships none [S-L08-098]; Carbon, Atlassian and Material ship them [S-L08-079, S-L08-011, S-L08-008]. | Three options; default toasts only for low-stakes results with undo. |
| Q-form-02 | Validation timing: GOV.UK validates on submit [S-L08-077]; NN/g research favors on-blur for most inputs [S-L13-100]. | On-blur for format checks, on submit for the rest, with the summary pattern. |
| Q-motion-01 | Motion default: Material's expressive spring scheme is its default for most products [DC-L10-14; S-L10-024]; Carbon and L04 default to productive motion with bounce at or below 0.2 [DC-L04-19]. | Two-mode default; springs as an explicit choice; productive cap for high-trust products. |
| Q-state-03 | Focus ring: Material uses 3px [S-L04-003]; Atlassian and Primer use 2px [S-L04-016, S-L04-024]; BOARD's L13 note flags a Figma article's 3px claim as contradicting WCAG, pending the V1 verification pass. | 2px default with an offset, 3px as an option; both must meet 3:1. |
| Q-type-01 | Typeface default: L02 says the system stack for productivity tools [DC-L02-01]; L09 says Inter or the system stack [DC-L09-05]. | System stack by default for tools, open-neutral (Inter) as the one-click alternative. |
| Q-type-08, Q-aud-01 | Body size: L02's web default is 14px UI text [DC-L02-08]; L09's regular preset is 16px [L09 A1 row 8]. They agree once density is known. | Tie body size to the density answer instead of one fixed default. |
| Q-token-01 | Tiers: L07 says two tiers with component tokens only when needed [DC-L07-01]; L09 and L01 say three tiers with the component tier optional [L09 A1 row 1; DC-L01-26]. Same structure, different counting. | Present it as "primitive -> semantic, component tokens on demand". |
| Q-color-17 | Contrast method: WCAG 2.2 is the enforceable standard; Radix and Geist use APCA; WCAG 3 is still a draft [DC-L01-22; BOARD L01 note]. | Enforce WCAG 2.2, show APCA as advisory. |
| Q-color-06 | Dynamic color: Material pushes dynamic color [DC-L01-21]; brand-led consumer apps keep fixed brand color, and iOS has no equivalent [DC-L10-05]. | Per-platform choice; brand-critical and status colors always fixed. |
| Q-space-01 | Base unit: 8 (Carbon, Atlassian, Material, Spectrum naming) vs 4 (Fluent, Polaris, Primer, Tailwind) [DC-L03-01]. | "4 as the grid, 8 as the rhythm" as a reconciling default. |
| Q-shape-03 | Pills: Material and Spectrum 2 use pills widely [DC-L09-01]; Carbon v12 moved tags away from pills [S-L04-031]; Atlassian reserves full radius for people [S-L04-016]. | Pill as an option per component role; people = full circle by default. |
| Asset hooks | Fallback order: L17's policy puts "commission a designer" before open libraries [DC-L17-04]; the icon and typeface cards default to open libraries first [DC-L05-01, DC-L02-01]. | Icons and typefaces lead with open libraries (they are tool-assisted blocks); identity assets (logo, app icon, illustration, photography, sound) lead with commissioning. |
| Quick mode | L17 says owner-input blocks are never auto-decided [DC-L17-08]; Quick mode asks only 10 questions, so scope, principles and similar owner inputs take defaults. | Quick records them as "assumed" and lists them for confirmation at the end (`meta.quick_mode_assumed_owner_inputs`). |
| Q-voice-03 | Capitalization: sentence case everywhere (Microsoft, Atlassian) vs title-case headings (Mailchimp) vs per element (Apple) [DC-L06-20]. | Three options; sentence case by default. |

## Confidence and gaps

- **Confirmed from files:** every option value, system name and default comes from a card in `synthesis/cards.json` (refreshed 2026-09-23, 325 cards) or from L09's shared-pattern and divergence tables; card and source ids are cited inline. The ordering was validated against `synthesis/decision-graph.json` including S1c's `graph-overrides.json` (see `questionnaire.json` meta for the counts).
- **Inferred (tagged in place):** the Quick-mode selection and the choice to derive posture from slider G; the stage grouping of cards without graph links; accepted file formats in some asset hooks (sounds, animated assets); the time-weight rule; the Ask and Example prompts.
- **Reconciled late:** L17 (`research/L17-how-systems-get-made.md`) and L18 (`research/L18-ai-first-distribution.md`) landed while this file was being finished. L17's 14 hooks map to the Hook lines here (L17 H-brandbook is the brief option of Q-ref-01; H-favicon is derived in Q-brand-03); L17's tool hooks H-tokens, H-figma, H-comp, H-dataviz and H-a11y map to Q-token-08, Q-tool-03, Q-comp-01, Q-viz-01 and Q-gov-07. The per-question Block class is this file's application of L17's scheme, not L17's own block-by-block table (which is keyed to ontology blocks, not questions).
