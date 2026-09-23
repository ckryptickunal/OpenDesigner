# Guided decision flow: the builder's questionnaire (S1b)

This is the question flow at the core of the design-system builder. L11 found that no competitor walks a person through the decisions: tools generate a theme from a few inputs, host an existing system, or extract one [DC-L11-01; S-L11-071, S-L11-073]. This file lists every question the builder asks, in order, with the options, what each option does visually, and what it changes downstream.

`synthesis/questionnaire.json` holds the same content in machine-readable form. It is generated from this file by a small parser that reads the entry format below, so edit this file first and regenerate the JSON.

## How the flow is built

- **One stage = one builder screen.** Stages are ordered by the dependency step in `synthesis/decision-graph.json` (step 0 = nothing upstream). A validator checked every one of the graph's 431 edges: no question is asked before a question it depends on, except the 10 builder-product cards listed under "Not asked" that the builder designs rather than asks.
- **Cycles stay on one screen.** The graph has 12 cycles (decisions that constrain each other). Each cycle's cards sit on one screen, and the screen shows one shared live preview so the person sees the trade-off. The largest cycle is color: 21 cards, which is why Stage 08 is one screen with sections.
- **Cards without links were placed by their text.** Many component and pattern cards (L08, L13) have graph step 0 only because their "Depends on" text names lanes rather than card ids (for example DC-L08-07 depends on "radius scale, spacing/density, type scale"). They are placed after the foundations they name [inferred from each card's Depends-on field].
- **Look first, encoding later.** Token naming, file format and governance come after the visual stages. They change how the system is stored, not how it looks, and nothing visual depends on them in the graph.

## Depth modes

Every question is tagged with the lowest mode that asks it. A `Quick` question is also asked in Standard and Expert; a `Standard` question is also asked in Expert. `Any` marks the reference-intake panel, which is available on every screen in every mode and is never required.

| Mode | Asks | Who it is for | What happens to the rest |
|---|---|---|---|
| **Quick** | 10 questions | "Give me a complete system in two minutes" | Every other question takes its default. Personality sliders pre-fill style answers through the lever matrix [DC-L06-02]. |
| **Standard** | Quick + Standard questions | An engineer setting up a real product system | Expert questions take defaults and stay editable later. |
| **Expert** | Everything | Design-system leads, multi-platform or multi-brand systems | Nothing is auto-decided; defaults are still pre-filled. |

**Quick mode, in order:** Q-aud-01 (who uses it), Q-brand-01 (personality sliders), Q-plat-01 (platforms), Q-tool-01 (where the system lives), Q-color-01 (brand color input), Q-color-02 (where brand color appears), Q-type-01 (typeface posture), Q-shape-01 (corner softness), Q-depth-01 (how surfaces separate), Q-motion-01 (motion feel).

Why these ten: they combine the highest fan-out step-0 decisions in the graph (personality DC-L06-02 fans out to 15 decisions, platforms DC-L10-01 to 12, source of truth DC-L16-02 to 8) with the L09 divergence points that change the look most (shape, depth, surface color, density, typeface, color generation, motion) [L09 A2; DC-L09-01 to DC-L09-08]. Everything L09 found nearly every system shares is pre-filled instead of asked: a 3-tier token model, a 4px spacing base, neutral surfaces plus one accent plus status colors, 12-step ramps, 100-300 ms ease-out motion, light and dark modes, WCAG 2.2 AA [L09 A1 rows 1-12]. Platform posture (DC-L10-02, fan-out 9) is derived in Quick mode from the personality slider "Bold vs deferential" and shown as a confirm chip [inferred].

## How a model runs this interview

The builder's interface is an LLM (Claude, ChatGPT, Codex or another capable model) interviewing the person, visually where the host allows (artifacts, canvases, Figma or Paper through MCP) and in plain text otherwise [BRIEF requirements 6-7]. `questionnaire.json` carries the same steps under `interview_protocol`.

1. Agree the mode (Quick, Standard, Expert) and say roughly how many questions it means. Offer the reference panel (Q-ref-01) up front and keep it open.
2. Walk the stages in order. Open each with one sentence on what the stage decides, then render its Preview if the host can show visuals; otherwise describe the Example in words.
3. Ask each question whose mode is included and whose "Show if" holds, using its **Ask** line. Spend time by **Time weight**: for `high`, explain why, show two or three options with their visual effect and a real system, recommend the default with its source, and state what it changes downstream before moving on; for `medium`, ask with the recommended default and the main alternatives; for `low`, state the default in one line and ask to confirm or change it.
4. For asset hooks, ask "do you have this?", accept the listed formats, and if the answer is no, offer the listed paths with their caveats. Never pretend a generated placeholder is a finished brand asset.
5. Record every answer as {question id, option value, how it was set: chosen, confirmed default, auto default, or from reference}. Questions outside the mode take their default and stay editable.
6. When an answer conflicts with an earlier one (the cycles named in stage headers), show the conflict and settle it with the ranked principles from Q-brand-07; do not average silently [L06 section 4.2].
7. After each stage, summarize the decisions in plain sentences a teammate could read, and append them to the decision log so a later session or another model can continue coherently [BRIEF requirements 9-11].
8. Only offer option values that appear in the question. If the person wants something else, record it as a custom value with their reason.

**Time weight rule** [inferred from `decision-graph.json`]: `high` when a decided card constrains 5 or more others (fan-out 5+) or the question is in Quick mode; `medium` when fan-out is 2-4, or the question is an asset hook, an input question or the reference panel; `low` otherwise. Each question shows its weight and the fan-out it came from.

## How to read an entry

```
### Q-<area>-<nn> · <question in plain words> · <Quick|Standard|Expert|Any>
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
- **Use / avoid:** (generatable blocks) where the chosen option belongs and where it does not, shown as a teaching note beside the control
- **Hook:** (asset hooks) accepted formats, and the paths offered when the answer is "no"
- **Pre-answers:** (reference intake) which later questions a reference can pre-fill
- **Skip:** whether it can be skipped and auto-defaulted
- **Time weight:** high, medium or low: how long the model should spend (rule below)
- **Evidence:** card ids and source ids
- **Merges:** (optional) source questionnaire items folded into this question
```

Source questionnaire codes used in "Merges": `K` = L11 kickoff questionnaire Part H (for example K2.1), `B` = L06 section 8 brand questions (B1-B15), `P` = L10 platform questionnaire (P1-P26), `D` = L14 builder questionnaire extract (D1-D7). Claims carry a card id, a source id, or [inferred].

---

## Three kinds of question (from the product brief)

The product brief (`_coordination/BRIEF.md`) sets three rules this flow follows:

1. **Asset hooks for blocks the builder cannot generate well.** A logo, brand mark, custom icons, illustration, photography, a brand typeface and similar assets need a designer or a dedicated tool. For each, the builder asks "Do you have this?", names the formats it accepts, and offers honest paths when the answer is no. Hook questions carry a **Hook** line. In Quick mode no hook is asked; each hook's "if no" fallback is applied and the asset tray stays open so files can be dropped in later.
2. **Visual, teaching controls for generatable blocks.** Spacing, primitives, tokens and components are chosen on a live preview, and each such question carries a **Use / avoid** line that the builder shows beside the control, so the interface teaches where each option belongs.
3. **Reference intake at any point.** Q-ref-01 is a side panel on every screen. A reference can pre-fill later answers; the person confirms each one.

| Asset hook | Question | Stage |
|---|---|---|
| Logo, brand mark, favicon | Q-brand-03 | 03 |
| Fixed brand colors | Q-color-01 (locked hex input) | 08 |
| Brand typeface files and license | Q-type-02 | 10 |
| Custom icon set | Q-icon-01 | 17 |
| App icon | Q-icon-06 | 17 |
| Photography | Q-img-01 | 18 |
| Illustration, characters, mascot | Q-img-04 | 18 |
| Animated assets (Lottie, 3D, animated icons) | Q-img-06 | 18 |
| UI sounds or sonic logo | Q-motion-08 | 16 |
| Existing voice and tone guide | Q-voice-01 | 19 |

---

## Stage 00 · Reference intake (a side panel on every screen)
> Not a step in the sequence. The panel sits beside every stage; anything added here is read once and offered as pre-filled answers on the stages that follow, each marked "from reference" until the person confirms it.

### Q-ref-01 · Do you have an example website, screenshot, Figma file or other resource the builder should learn from? · Any
- **Why:** Tools already extract design systems from references (Google Stitch extracts from a URL; Polymet extracts tokens from a URL); the builder uses the same idea to pre-answer questions instead of starting blank [S-L16-256, S-L16-405].
- **Ask:** "Before we start, is there a site, screenshot or Figma file whose structure or quality you like? I'll read it and suggest answers."
- **Example:** Ask for a URL of their own product or an app they admire; show the 'extracted from reference' card with 3-4 found values.
- **Control:** drop zone + URL field; multiple references allowed, each tagged "our product", "inspiration" or "competitor"
- **Options:**
  - `url` A live website URL: the builder reads computed colors, type, spacing, radius, shadows, motion and components [inferred; S-L16-405].
  - `screenshot` Screenshots or images: color, type size ratios, density, radius and depth are estimated from pixels; values are marked as estimates [inferred].
  - `figma` A Figma file or library: variables, styles and components are read through the Figma MCP (`get_variable_defs`, `get_design_context`, `get_screenshot`) [DC-L11-23; S-L11-041].
  - `code` A repository, CSS file or token JSON: exact values, including DTCG files [DC-L07-08; S-L07-011].
  - `doc` A brand book, voice guide or PDF: brand colors, typefaces, voice traits [inferred].
- **Default:** none. *Source:* [inferred].
- **Decides:** none directly (input)
- **Changes:** pre-fills answers only; no card is decided without confirmation
- **Pre-answers:** Q-scope-02 (an existing product becomes the audit), Q-brand-01 and Q-brand-02 (reference placed on the personality map), Q-plat-01, Q-color-01 to Q-color-06, Q-color-09, Q-color-14, Q-type-01, Q-type-03, Q-type-06, Q-space-01, Q-space-02, Q-space-04, Q-layout-01, Q-shape-01, Q-shape-02, Q-depth-01, Q-depth-02, Q-motion-01, Q-motion-02, Q-icon-02, Q-icon-03, Q-comp-01, Q-state-01, Q-form-01 [inferred mapping from what each reference type exposes].
- **Preview:** an "extracted from reference" card listing each found value next to the question it would answer, with Accept, Adjust and Ignore buttons.
- **Use / avoid:** use a reference to copy structure and quality (spacing rhythm, type ratios, density, depth model); avoid copying another brand's identity: its logo, brand color, proprietary typeface or illustration are never carried over, and a "competitor" reference is used only to flag shared tropes [BRIEF requirement 4; S-L06-027].
- **Skip:** yes; always optional.
- **Time weight:** medium (fan-out 0)
- **Evidence:** S-L16-256, S-L16-405, S-L11-041, DC-L11-23, DC-L11-04
- **Merges:** K3.3 (reference products), B3 (competitors, as "competitor" references)

---

## Stage 01 · Scope and team
> Screen: what the system is for and who builds it. Graph step 0-2. Cycle kept together: DC-L11-02 + DC-L11-04 (scope decides what to audit; the audit reshapes scope).

### Q-scope-01 · Which products and surfaces will this system serve, and which will it explicitly not serve? · Standard
- **Why:** Scope sets how abstract components must be and how many token layers you need [DC-L11-02].
- **Ask:** "What will this system style: just your app, or also a marketing site, docs, emails or internal tools?"
- **Example:** Show two thumbnails, an app screen and a marketing page, drawn from the same tokens.
- **Control:** multi-select + text field for "not served"
- **Options:**
  - `product-app` Product app: tight, opinionated visuals are possible when this is the only surface [DC-L11-02, inferred].
  - `marketing` Marketing site: adds an expressive layer next to the productive one (Carbon splits productive and expressive type and motion) [DC-L06-01; S-L06-001].
  - `internal-tools` Internal or admin tools: usually dense (see Q-aud-01) [inferred].
  - `docs-content` Docs or content site: long-form reading pushes line length and paragraph rules (DC-L02-17) [inferred].
  - `email` Email: a constrained rendering target the token pipeline must also output [DC-L11-02 options].
  - `partner-embed` Embedded or partner surfaces: need scoped, context-agnostic components ("card", not "product card") [S-L11-002].
- **Default:** product-app only. *Source:* card heuristic, scope v1 to what the pilot touches [DC-L11-02; S-L11-083].
- **Decides:** DC-L11-02
- **Changes:** DC-L11-03, DC-L11-07, DC-L11-14, DC-L11-16, DC-L11-25, DC-L06-01 · blocks: Strategy > Scope; Tokens > Architecture > Tiers; Components > Inventory
- **Preview:** a strip with one sample screen per selected surface, all rendered from the same draft tokens.
- **Skip:** yes, defaults to a single product app.
- **Time weight:** high (fan-out 8)
- **Evidence:** DC-L11-02; S-L11-083, S-L11-002, S-L11-030
- **Merges:** K2.1, K2.2 (surfaces part), B11 (marketing vs product, first half)

### Q-scope-02 · Is there existing UI to consolidate, or is this a new product? · Standard
- **Why:** An audit sets how much the system must consolidate, for example 40 grays merged into one 10-step ramp [DC-L11-04, inferred].
- **Ask:** "Is there existing UI we should consolidate, or are we starting fresh?"
- **Example:** If existing, ask for a URL or CSS file; show a count like '38 grays, 14 button styles found'.
- **Control:** single choice (+ URL or CSS import when existing)
- **Options:**
  - `greenfield` New product: skip the audit and go straight to visual language [S-L11-105].
  - `manual-inventory` Existing UI, run an interface inventory: screenshots across 16 categories, then keep/merge/kill decisions (Brad Frost) [S-L11-001].
  - `automated-audit` Existing UI, import an automated audit: unique colors and declarations (CSS Stats), component and prop usage (Omlet, react-scanner), Figma library analytics [S-L11-105, S-L11-037, S-L11-039, S-L11-035].
  - `both` Both: automated counts plus the manual inventory for shared vocabulary [DC-L11-04 default].
- **Default:** greenfield; if existing UI, `both`. *Source:* card heuristic, the manual inventory's main value is shared vocabulary and buy-in [DC-L11-04; S-L11-001].
- **Decides:** DC-L11-04
- **Changes:** DC-L11-02, DC-L11-07; foundation ramps (L01-L04), component list (L08), naming (L07) · blocks: Process > Discovery > Audit
- **Preview:** an inventory board: counts of unique colors, type styles and button variants found, with the proposed consolidated ramp beside them.
- **Skip:** yes, defaults to greenfield.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L11-04; S-L11-001, S-L11-105, S-L11-035
- **Merges:** K1.5, K1.6

### Q-scope-03 · Who will consume the system? · Expert
- **Why:** Each audience needs different docs and export formats; AI agents need machine-readable exports [DC-L11-02; S-L11-083].
- **Ask:** "Who will use the system itself: engineers, designers, content people, partners, AI coding agents?"
- **Example:** Show the output list per audience, e.g. 'AI agents get DESIGN.md and an MCP manifest'.
- **Control:** multi-select
- **Options:**
  - `engineers` Engineers: component API docs and code packages (DC-L11-18).
  - `designers` Designers: a design-tool library (DC-L16-13).
  - `content-pm` Content, PM, marketing: usage and voice guidance (DC-L06-18).
  - `partners` External partners: public docs and stricter versioning (DC-L11-14).
  - `ai-agents` AI coding agents: MCP server, DESIGN.md, llms.txt (12 of 25 benchmarked systems ship one) [L09 A1 row 10; DC-L11-23].
- **Default:** engineers + designers + ai-agents. *Source:* L09 shared pattern row 10 (agent-readable exports in 12 of 25 systems) [inferred choice].
- **Decides:** DC-L11-02 (consumers part)
- **Changes:** DC-L11-18, DC-L11-23, DC-L16-12 · blocks: Docs > Component page; Distribution > Agent context
- **Preview:** a list of the output files the builder will generate for each checked audience.
- **Skip:** yes.
- **Time weight:** high (fan-out 8)
- **Evidence:** DC-L11-02, DC-L11-23; S-L11-083, S-L11-088
- **Merges:** K1.1, K9.1

### Q-scope-04 · How many people will build and maintain the system, and how are they organized? · Expert
- **Why:** Small teams should adapt an existing accessible base rather than build from scratch; team size sets how much the builder must automate [DC-L11-01, DC-L11-10].
- **Ask:** "How many people will build and maintain this, and are they one team or spread across product teams?"
- **Example:** Give the survey split: most teams are 1-5 people.
- **Control:** single choice (size) + single choice (model)
- **Options:**
  - `size-1-2` 1-2 people (28% of teams) [S-L11-030].
  - `size-3-5` 3-5 people (33%) [S-L11-030].
  - `size-6-10` 6-10 people (25%) [S-L11-030].
  - `size-10plus` 10+ people (8%) [S-L11-030].
  - `model-solitary` Solitary: one team makes it for itself and shares it (Curtis) [S-L11-005].
  - `model-centralized` Centralized: a dedicated team serves product teams [S-L11-005].
  - `model-federated` Federated: designers from several product teams decide together [S-L11-005].
  - `model-hybrid` Hybrid: central librarian team plus federated contributors (Salesforce) [S-L11-013].
- **Default:** 1-2 people, centralized with a named owner. *Source:* card heuristic [DC-L11-09; S-L11-030].
- **Decides:** DC-L11-09, DC-L11-10
- **Changes:** DC-L11-01, DC-L11-11, DC-L11-12 · blocks: Governance > Team model; Governance > Roles
- **Preview:** none visual; shows which governance defaults (contribution flow, review gates) the builder will switch on.
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L11-09, DC-L11-10; S-L11-005, S-L11-013, S-L11-030, S-L11-006
- **Merges:** K9.2, K9.3, K13.2, K1.4

---

## Stage 02 · Audience and commitments
> Screen: who the product is for and what it promises them. Graph step 0. These answers bound every later option.

### Q-aud-01 · Who uses the product, and how often? · Quick
- **Why:** Audience sets density and base text size, fourth on L09's list of the biggest visual differences between systems (an inferred ranking; body text ranges 13-19px) [DC-L09-04; L09 A2 row 4].
- **Ask:** "Who uses the product and how often: all day in data-heavy work, regularly, or occasionally on the go?"
- **Example:** Show one table-and-form screen at dense, regular and large densities side by side.
- **Control:** single choice
- **Options:**
  - `dense` People working all day in data-heavy tools: body 13-14px, controls 28-32px; compact and utilitarian (Polaris 13px, SLDS 13px, Carbon, Atlassian, Primer, Ant 14px) [DC-L09-04; S-L09-403].
  - `regular` Regular users of a general app: body 16px, controls 36-40px (Radix, shadcn, Mantine, Chakra) [DC-L09-04; L09 A3 density].
  - `large` Occasional, mobile or public users: body 17px or more, controls and targets 44-48px (iOS 17pt, GOV.UK 19px, Material, USWDS 48px targets) [DC-L09-04; S-L09-540].
- **Default:** regular. *Source:* L09 shared default row 8 (body 16px general, 14px tools) [L09 A1].
- **Decides:** DC-L09-04
- **Changes:** DC-L15-04, DC-L08-13, DC-L02-08, DC-L03-07, DC-L03-10, DC-L15-09 · blocks: Foundations > Typography + Space > Density preset
- **Preview:** the same table-plus-form screen at the three densities side by side; hovering a row shows its height, padding and text size.
- **Use / avoid:** use dense for tables, dashboards and editors people work in all day; avoid dense on touch-first, occasional or public surfaces, where it hurts legibility and forces the targets out of step with the visuals [DC-L09-04, DC-L15-04].
- **Skip:** yes, defaults to regular. Target sizes do not shrink with density; they follow input precision (Q-space-03, DC-L14-03).
- **Time weight:** high (fan-out 0)
- **Evidence:** DC-L09-04, DC-L15-04; S-L09-403, S-L09-540
- **Merges:** B1 (audience half), K1.1 (users of the product, not of the system)

### Q-aud-02 · What is at stake for users, and what state are they usually in? · Standard
- **Why:** The category sets a ceiling on expressiveness; Google found expressive design may not suit banking [S-L06-010]. User state drives tone [DC-L06-19; S-L06-060].
- **Ask:** "What's at stake for your users, and what state are they usually in when they use it?"
- **Example:** Contrast a banking transfer screen with a game reward screen.
- **Control:** single choice (category) + multi-select (states)
- **Options:**
  - `high-trust` Money, health or government: caps expressiveness and playful motion; calm, formal defaults [S-L06-010, S-L06-041].
  - `work` Productivity or B2B: productive defaults (Carbon, Atlassian, Primer quadrant) [L09 A3].
  - `consumer` Consumer lifestyle: room for brand color and hero moments [DC-L06-03].
  - `play` Play, entertainment, learning: characters and springs are acceptable (Duolingo, Mailchimp) [S-L06-026, S-L06-027].
  - `state-*` States (multi): anxious, rushed, curious, celebrating; each shifts the tone matrix (Atlassian tones by emotion) [S-L06-060, S-L06-014].
- **Default:** work, states "rushed". *Source:* [inferred]; matches the L09 productive quadrant most benchmarked systems occupy [L09 A3].
- **Decides:** none directly (input)
- **Changes:** DC-L06-03, DC-L06-19, DC-L13-17 (default positions of their sliders)
- **Preview:** a pre-filled position on the personality sliders of Stage 03, with a note where the category caps them.
- **Skip:** yes.
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L06-03, DC-L06-19; S-L06-010, S-L06-060, S-L06-014
- **Merges:** B1 (emotional state), B2

### Q-aud-03 · What accessibility standard must the system meet? · Standard
- **Why:** The target bounds color, type size, focus ring and target-size options in every later stage [DC-L11-19].
- **Ask:** "Which accessibility standard must you meet? WCAG 2.2 AA is the usual floor."
- **Example:** Show a text pair that passes 4.5:1 and one that fails.
- **Control:** single choice
- **Options:**
  - `wcag22-aa` WCAG 2.2 AA: 4.5:1 text, 3:1 large text and UI parts, 24px target floor (GOV.UK commits to 2.2 AA) [S-L11-093; L09 A1 row 11; DC-L03-12].
  - `wcag22-aa-plus` AA plus chosen AAA rules, for example 7:1 body text or larger targets: stricter palettes, fewer mid-tone text colors [DC-L01-22, inferred].
  - `wcag22-a` Level A only: not recommended; no benchmarked system states a target below AA [L09 A1 row 11].
- **Default:** WCAG 2.2 AA. *Source:* accessibility rule; all 11 benchmarked systems that state a target use AA; WCAG 3 is still a draft, so 2.2 is the enforceable target [L09 A1 row 11; BOARD L01 note].
- **Decides:** DC-L11-19
- **Changes:** DC-L01-22, DC-L03-12, DC-L04-09, DC-L14-03, DC-L02-08 · blocks: Foundations > Accessibility > Program
- **Preview:** a guardrail strip listing which later options will be blocked or flagged at this level.
- **Skip:** yes, AA. The builder also generates the system-vs-product-team responsibility statement GOV.UK publishes [S-L11-092].
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L11-19; S-L11-093, S-L11-092, S-L11-094, S-L11-030
- **Merges:** K4.1, K4.2, B15 (WCAG level)

### Q-aud-04 · Which settings should users be able to adjust, and which situations must you design for? · Standard
- **Why:** Inclusive defaults ("solve for one, extend to many") switch on extra modes and larger targets [DC-L13-14; S-L13-072].
- **Ask:** "Which settings should users be able to change: text size, density, contrast, reduced motion?"
- **Example:** Show the preview with a mode switcher gaining one toggle per setting.
- **Control:** multi-select (settings) + multi-select (situations)
- **Options:**
  - `text-size` Text size: layouts must reflow at large sizes (DC-L02-21).
  - `density` Density switch: adds a compact/comfortable token mode (DC-L03-11).
  - `contrast` Contrast themes: adds a high-contrast mode (DC-L01-20).
  - `reduced-motion` Reduced motion: swaps movement for fades (DC-L04-25).
  - `situational` Situational limits (one hand busy, bright light, older users): larger targets and higher contrast by default; reads calmer and more legible [DC-L13-14; S-L13-076, S-L13-038].
- **Default:** text-size + reduced-motion. *Source:* accessibility rule (WCAG 2.2 AA as the floor; text resize and motion preferences are OS settings the system should honor) [DC-L13-14, DC-L10-16].
- **Decides:** DC-L13-14
- **Changes:** DC-L07-15, DC-L11-25, DC-L01-20, DC-L04-25, DC-L02-21, DC-L03-11 · blocks: Principles > Inclusion; Tokens > Theming > Modes
- **Preview:** a mode switcher on the preview screen that gains one toggle per checked setting.
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L13-14; S-L13-072, S-L13-076, S-L13-098
- **Merges:** K4.4, B15 (user settings part)

---

## Stage 03 · Brand personality and principles
> Screen: who the brand is. Graph step 0-1. Personality has the largest fan-out in the graph (15 decisions), so it comes before any foundation [DC-L06-02].

### Q-brand-01 · Where does your brand sit on these scales? · Quick
- **Why:** The sliders set defaults for color saturation, radius, type, weight, motion, illustration and voice through the L06 lever matrix [DC-L06-02].
- **Ask:** "Place your brand on these scales; drag each slider toward the end that sounds like you."
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
- **Time weight:** high (fan-out 15)
- **Evidence:** DC-L06-02; S-L06-070, S-L06-071, S-L06-078, S-L06-011, S-L06-013
- **Merges:** B5, B6, K3.3 (feel)

### Q-brand-02 · Which products should yours feel like, and what one thing should people recognize it by? · Standard
- **Why:** References align taste fast (a 20-second gut test), and the "cover the logo" test names the signature lever to invest in [S-L11-001, S-L06-004].
- **Ask:** "Which products should yours feel like, and what one thing should people recognize it by?"
- **Example:** Ask for 1-5 product names or URLs; place them on the personality map.
- **Control:** text (up to 5 reference products or URLs) + single choice (signature lever)
- **Options:**
  - `sig-typeface` Signature typeface (Uber Move, Spotify Mix, IBM Plex) [L09 A3; S-L06-019].
  - `sig-color` One hero color (brand-led systems spend personality on one signature color) [L09 A3].
  - `sig-device` A graphic device or shape (Slack shapes, M3 shape library) [S-L06-030, S-L06-009].
  - `sig-character` A character or illustration style (Mailchimp Freddie, Duolingo Duo) [S-L06-027, S-L06-026].
  - `competitors` Competitors (text): the builder flags tropes they share so you can avoid them (Collins positioned Mailchimp to "break from SaaS visual tropes") [S-L06-027].
- **Default:** sig-color. *Source:* L09 personality map, brand-led systems keep chrome restrained and spend personality on typeface, one color and imagery [L09 A3, inferred ranking].
- **Decides:** none directly (input)
- **Changes:** DC-L06-02 slider pre-positions, DC-L06-11, DC-L06-07, DC-L06-12
- **Preview:** reference thumbnails placed on the L09 personality map (productive to expressive, neutral to brand-led) with the person's current position.
- **Skip:** yes.
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L06-02, DC-L06-11; S-L06-004, S-L06-027, S-L11-001
- **Merges:** B3, B4, K3.3 (reference products)

### Q-brand-03 · Do you have a logo and brand mark? · Standard
- **Why:** A logo is a block the builder cannot generate well; it feeds the logo component, favicons and app icons [DC-L05-13; BRIEF requirement 2].
- **Ask:** "Do you have a logo or brand mark? If so, share the SVG."
- **Example:** Show the logo in an app bar at 24-32px and as a favicon; if none, show the placeholder wordmark.
- **Control:** single choice + file upload
- **Options:**
  - `yes-full` Yes, symbol and wordmark: the builder makes a Logo component with Icon and Lockup variants (Atlassian sizes 16-48px, appearances brand, neutral, inverse) [S-L05-044].
  - `yes-wordmark` Wordmark only: used on sign-in and marketing; the nav uses the name set in the brand typeface [DC-L05-13, inferred].
  - `no` Not yet: see the Hook line.
- **Default:** no, with a text wordmark placeholder. *Source:* [inferred].
- **Decides:** none directly (asset input for DC-L05-13)
- **Changes:** DC-L05-13, DC-L05-12 (app icon), DC-L04-27 (a sonic logo is a separate hook, Q-motion-08) · blocks: Brand in product > Logo usage; Brand in product > Favicon
- **Hook:** Accepts SVG (preferred, one master for the favicon set), PDF or EPS vector, or PNG at 512px or larger; light, dark and monochrome versions if they exist. The builder then derives `favicon.ico` 32px, `icon.svg` with a dark-scheme style, `apple-touch-icon.png` 180px, manifest PNGs 192 and 512 plus a maskable 512 [S-L05-042, S-L05-040, S-L05-041]. If no: (1) commission a designer (the recommended path for anything customers will recognize), (2) use a temporary wordmark set in the chosen typeface, which the builder generates and labels "placeholder", or (3) use an AI or template logo tool, with the caveat that its output may not be distinctive or ownable [inferred].
- **Preview:** the logo placed in an app bar at 24-32px, on a sign-in screen as a lockup, and as a browser-tab favicon, in light and dark.
- **Use / avoid:** use the symbol-only mark at 24-32px in dense app chrome and the full lockup on sign-in and marketing; avoid recoloring fixed-color product marks (Fluent never recolors launch icons) and avoid relying on inherited color [S-L05-044, S-L05-014].
- **Skip:** yes; the placeholder wordmark is applied.
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L05-13; S-L05-014, S-L05-040, S-L05-042, S-L05-044
- **Merges:** B7 (logo), K3.1 (brand guidelines, logo part)

### Q-brand-04 · How expressive should the product be? · Standard
- **Why:** Expressive design raised perceived modernity by 34% and made key elements up to 4x faster to spot in Google's tests, but overdone it hurts usability and a strong minority prefers calm [DC-L06-03; S-L06-010].
- **Ask:** "How expressive should the product be: calm and productive, calm with one or two big moments, or expressive throughout?"
- **Example:** Show one success moment animated three ways.
- **Control:** single choice
- **Options:**
  - `productive` Productive only: calm, dense, efficient (Carbon product UI, Linear 2026 "calmer interface") [S-L06-002, S-L06-067].
  - `hero-moments` Productive plus 1-2 hero moments: expressive motion and type only at significant moments such as opening a page or the primary action (Carbon expressive motion; Material's own budget) [S-L06-002, S-L06-009].
  - `expressive` Expressive throughout: varied shapes, rich color, emphasized type, fluid motion (M3 Expressive's seven tactics) [S-L06-009].
- **Default:** hero-moments. *Source:* card heuristic, Material's "one or two hero moments" rule [DC-L06-03; S-L06-009]. Capped at productive when Q-aud-02 = high-trust [S-L06-010].
- **Decides:** DC-L06-03
- **Changes:** DC-L06-04, DC-L06-10, DC-L06-11, DC-L15-01, DC-L15-03 · blocks: Foundations > Brand > Expression intensity
- **Preview:** one screen shown in all three settings, with the hero moment (for example a success state) animated.
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L06-03; S-L06-002, S-L06-009, S-L06-010, S-L06-067

### Q-brand-05 · How do marketing pages relate to the product? · Standard
- **Show if:** Q-scope-01 includes `marketing`
- **Why:** The layering model decides whether marketing and app look visibly related or drift apart [DC-L06-01; S-L06-110].
- **Ask:** "How should the marketing site relate to the product: one system with two moods, or separate?"
- **Example:** Show a marketing hero next to a product table under each option.
- **Control:** single choice
- **Options:**
  - `one-system-two-sets` One system with productive and expressive value sets: same type family and color logic, app denser (Carbon type sets -01/-02) [S-L06-001, S-L06-002].
  - `brand-above` Brand language above, product system below, marketing beside it: more marketing freedom, more drift risk (IBM Brand Center / Carbon / Carbon for IBM.com) [S-L06-003].
  - `family` Family of systems on one foundation: platforms differ in components, tokens keep one brand (Spotify Encore, Netflix Hawkins) [S-L06-085, S-L06-087].
  - `single` Single product system, brand only in logo and color (most startups) [inferred].
- **Default:** one-system-two-sets. *Source:* card heuristic [DC-L06-01].
- **Decides:** DC-L06-01
- **Changes:** DC-L06-16, DC-L02-11 · blocks: Foundations > Brand > Layer architecture
- **Preview:** a marketing hero and a product table side by side, rendered from the chosen layering.
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L06-01; S-L06-001, S-L06-003, S-L06-053, S-L06-085, S-L06-110
- **Merges:** B11 (second half)

### Q-brand-06 · Should marketing and editorial pages get their own, more dramatic type set? · Expert
- **Why:** One productive scale keeps apps calm; an expressive set gives editorial pages big size jumps that "would be distracting if used in product" [DC-L02-11; S-L02-011].
- **Ask:** "Do marketing pages need their own dramatic heading styles?"
- **Example:** Show a heading ladder, productive vs expressive.
- **Control:** single choice
- **Options:**
  - `two-sets` Two sets: productive base 14px with fixed headings, expressive base 16px with fluid headings (Carbon display from 42px to 156px across breakpoints) [S-L02-012, S-L02-011].
  - `emphasized` One scale plus emphasized variants: 15 baseline + 15 heavier styles for actions and headlines (M3 Expressive) [S-L02-006].
  - `brand-face` One scale plus a separate brand typeface for brand moments (Atlassian Charlie Sans) [S-L02-015].
  - `productive-only` Single productive scale (Polaris, Primer) [DC-L02-11].
- **Default:** one productive scale plus 3-4 expressive display styles; a full second set if more than a third of pages are marketing or editorial. *Source:* card heuristic [DC-L02-11].
- **Decides:** DC-L02-11
- **Changes:** DC-L02-03, DC-L02-09, DC-L02-15, DC-L02-19, DC-L15-02 · blocks: Foundations > Typography > Type sets
- **Preview:** a heading ladder at productive and expressive settings, across three breakpoints.
- **Use / avoid:** use fluid, expressive display styles on marketing and editorial pages; avoid them inside product containers (Carbon: "Do not use these styles inside a container") [S-L02-011].
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L02-11; S-L02-006, S-L02-011, S-L02-012, S-L02-015, S-L02-041

### Q-brand-07 · What are your 3-5 design principles, and which one wins a tie? · Standard
- **Why:** Principles break ties between sliders that pull the same lever in opposite directions [DC-L06-15; L06 section 4.2].
- **Ask:** "What 3-5 principles should break ties, and which one wins? I can draft some from your sliders."
- **Example:** Show GOV.UK-style imperatives and a do/don't pair per principle.
- **Control:** text list (3-5) + drag to rank + single choice (format)
- **Options:**
  - `checklist` Question checklists (IBM) [S-L06-004].
  - `pairs` Functional and emotional pairs (Fluent) [S-L06-043].
  - `imperatives` Imperatives that name their sacrifice (GOV.UK, 11 principles, updated 2 Apr 2025) [S-L06-044].
  - `value-words` Short value words (Carbon system principles) [S-L06-114].
  - `generate` Let the builder draft principles from the sliders, for you to edit [inferred].
- **Default:** generate, 3-5 principles, each naming what it outranks, with one making accessibility non-negotiable. *Source:* card heuristic [DC-L06-15; S-L06-077, S-L06-044].
- **Decides:** DC-L06-15, DC-L11-05
- **Changes:** tie-break rules for slider conflicts; ADRs (DC-L11-12) · blocks: Foundations > Principles; Governance > Principles
- **Preview:** each principle shown with a do/don't pair generated from the current draft.
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L06-15, DC-L11-05; S-L06-044, S-L06-077, S-L11-008
- **Merges:** K3.2, B12, K1.2 (interview themes become principle inputs)

---

## Stage 04 · Platforms and devices
> Screen: where the product runs and what people touch it with. Graph step 0-2. Cycle kept together: DC-L10-01 + DC-L10-02 + DC-L10-03 + DC-L10-21 (platforms, posture, sharing layer and framework constrain each other). Placed after personality so the posture default can come from slider G [inferred; DC-L06-14 depends on DC-L06-02].

### Q-plat-01 · Which platforms ship in the first release? · Quick
- **Why:** Each platform adds conventions the brand must coexist with, plus units, target minimums and exporters [DC-L10-01].
- **Ask:** "Which platforms ship first: web, iOS, Android, desktop?"
- **Example:** Show one screen in browser, iOS and Android chrome.
- **Control:** multi-select
- **Options:**
  - `web` Web: one delivery layer (CSS custom properties); the brand can show in every pixel (Polaris calls Shopify's platform "the web platform") [S-L10-047].
  - `ios` iOS/iPadOS: Liquid Glass chrome, pt units, Dynamic Type; bars, controls and sheets are styled by the OS [S-L10-075, S-L10-011].
  - `android` Android: Material 3 conventions, dp/sp units, large-screen layouts mandatory at 600dp+ [S-L10-021, S-L10-071].
  - `desktop` Desktop app (macOS, Windows, or a web-tech shell) [DC-L10-24].
  - `secondary` Watch, TV, car or headset: see Q-plat-02 [DC-L10-24].
- **Default:** web. *Source:* survey, 94% of systems support web, 35% iOS, 34% Android [DC-L11-01; S-L11-030]. L10's own default for consumer products is web + iOS + Android phones with large-screen layouts [DC-L10-01] (see Disagreements).
- **Decides:** DC-L10-01
- **Changes:** DC-L10-02, DC-L10-08, DC-L10-09, DC-L10-10, DC-L10-11, DC-L10-15, DC-L10-17, DC-L10-19, DC-L10-20, DC-L10-22, DC-L10-24, DC-L14-01 · blocks: Platforms > Scope > Target platforms
- **Preview:** the same screen rendered in each platform's chrome (browser, iOS glass bars, Material top bar), side by side.
- **Skip:** yes, web.
- **Time weight:** high (fan-out 12)
- **Evidence:** DC-L10-01; S-L10-021, S-L10-046, S-L10-047, S-L10-075, S-L11-030
- **Merges:** P1, K2.2 (platform part)

### Q-plat-05 · Should your native apps look like the platform, like your brand, or a mix? · Standard
- **Show if:** Q-plat-01 includes ios, android or desktop. In Quick mode it is derived from slider G and shown as a confirm chip.
- **Why:** Native apps feel at home and inherit OS updates for free; brand-first apps look identical everywhere but must re-implement every OS change [DC-L10-02].
- **Ask:** "Should your iOS and Android apps look like the platform, like your brand, or a mix?"
- **Example:** Show one screen native-first, hybrid and brand-first.
- **Control:** single choice
- **Options:**
  - `native-first` Native-first: system components almost everywhere; brand shows in content, accents, imagery and voice (Apple: "Express your brand with familiar components") [S-L10-009].
  - `hybrid` Coherent hybrid: shared brand foundations and signature moments, native navigation and controls (Fluent reuses native patterns 80% of the time) [S-L10-038, S-L06-043].
  - `brand-first` Brand-first: identical custom UI on every platform (CRED NeoPOP); can feel foreign and must rebuild accessibility [S-L06-112, DC-L06-14].
- **Default:** hybrid. *Source:* card heuristic, share what users perceive as the brand, adopt the platform's version of "how the phone works" [DC-L10-02, DC-L06-14].
- **Decides:** DC-L10-02, DC-L06-14
- **Changes:** DC-L10-03, DC-L10-04, DC-L10-06, DC-L10-09, DC-L10-12, DC-L10-13, DC-L10-14, DC-L10-21, DC-L10-25, DC-L06-07, DC-L15-01 · blocks: Platforms > Strategy > Native vs brand posture
- **Preview:** one screen as native-first, hybrid and brand-first on iOS and Android.
- **Skip:** yes.
- **Time weight:** high (fan-out 11)
- **Evidence:** DC-L10-02, DC-L06-14; S-L10-009, S-L10-038, S-L10-075, S-L10-076, S-L06-043
- **Merges:** P3

### Q-plat-10 · How closely should interactions follow familiar conventions? · Standard
- **Why:** Native behavior feels trustworthy but generic; novelty is distinctive but costs learnability (Jakob's law); the default follows the posture chosen in Q-plat-05 [DC-L13-17; graph-overrides.json edge DC-L10-02 to DC-L13-17].
- **Ask:** "Should interactions follow familiar conventions, get a custom look, or be novel where it matters?"
- **Example:** Show a standard dropdown beside a custom one.
- **Control:** single choice
- **Options:**
  - `native` Platform-native: follow HIG, Material or Fluent behavior and look; instantly usable, generic [DC-L13-17].
  - `custom-skin` Conventional behavior with a custom skin: brand visuals, standard interaction [DC-L13-17].
  - `novel-core` Novel interaction for the core differentiator only, tested [DC-L13-17; S-L13-006].
- **Default:** custom-skin. *Source:* card heuristic; don't override standard shortcuts [DC-L13-17; S-L13-036, S-L13-030].
- **Decides:** DC-L13-17
- **Changes:** DC-L08-03, DC-L10-13 · blocks: Principles > Familiarity
- **Preview:** a standard dropdown and a custom one next to each other, both keyboard-operable.
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L13-17; S-L13-006, S-L13-030, S-L13-036, S-L13-055

### Q-plat-06 · On native platforms, use system controls or custom-branded ones? · Expert
- **Show if:** Q-plat-01 includes ios, android or desktop
- **Why:** System controls update with the OS (rounder, capsule-like on iOS 26+); custom controls keep brand shape but must supply their own accessibility [DC-L10-13].
- **Ask:** "On native platforms, keep the system's controls or restyle them?"
- **Example:** Show switches and sliders: system vs custom.
- **Control:** single choice
- **Options:**
  - `system` System controls tinted with the accent: native feel, Liquid Glass and Material behavior for free [S-L10-075, S-L10-072].
  - `restyled` Restyled system controls: brand color and label, familiar size, placement and behavior (Apple permits this) [S-L10-009].
  - `custom` Fully custom controls: brand shapes such as square buttons; can look out of place next to system UI [DC-L10-13].
- **Default:** system on native, custom on web. *Source:* platform convention [DC-L10-13].
- **Decides:** DC-L10-13
- **Changes:** DC-L10-14, DC-L10-12 · blocks: Components > Controls > Platform rendering
- **Preview:** switch, slider and segmented control in each style on iOS.
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L10-13; S-L10-009, S-L10-014, S-L10-072, S-L10-075
- **Merges:** P14

### Q-plat-07 · What do the platforms share? · Expert
- **Show if:** more than one platform in Q-plat-01
- **Why:** The more is shared, the more identical the product looks across platforms and the less native [DC-L10-03].
- **Ask:** "What should platforms share: principles, tokens, component specs, or code?"
- **Example:** Show one card component rendered per platform under each option.
- **Control:** single choice
- **Options:**
  - `principles` Principles only: loosest alignment (Fluent's four principles) [S-L10-038].
  - `tokens` Foundation tokens, platform component libraries: same palette and rhythm, platform-shaped components (Spotify Encore, Fluent) [S-L10-040, S-L10-039].
  - `specs` Shared component specs, per-platform code: one spec for 7 stacks including screen-reader specs (Uber Base) [S-L10-046].
  - `code` Shared component code: identical components everywhere [DC-L10-03].
- **Default:** tokens + shared specs, per-platform implementation. *Source:* card heuristic [DC-L10-03].
- **Decides:** DC-L10-03
- **Changes:** DC-L10-19, DC-L10-21, DC-L10-22, DC-L10-24, DC-L14-02 · blocks: Platforms > Architecture > Sharing layer
- **Preview:** a diagram of which layers are shared, with the same card component rendered per platform.
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L10-03; S-L10-039, S-L10-040, S-L10-046, S-L10-053
- **Merges:** P4

### Q-plat-08 · What will you build the UI with? · Standard
- **Why:** The stack decides the code the builder generates and how fast OS visual changes reach users [DC-L10-21, DC-L10-20, DC-L10-19].
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
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L10-19, DC-L10-20, DC-L10-21; S-L10-047, S-L10-055, S-L10-063, S-L11-030
- **Merges:** K2.3, P20, P21, P22

### Q-plat-02 · Which device classes must work great on day one, which only need to work, and which are out? · Standard
- **Why:** Each first-class device class adds a visibly different silhouette; "adapted only" classes look stretched, which Google now penalizes on large screens [DC-L14-01; S-L14-069].
- **Ask:** "Which devices must work great on day one, which just need to work, and which are out?"
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
- **Time weight:** high (fan-out 10)
- **Evidence:** DC-L14-01, DC-L10-24; S-L14-069, S-L14-001, S-L14-017, S-L10-024
- **Merges:** P2, P25, D1, D3

### Q-plat-03 · What do people touch or press with? · Standard
- **Why:** Input precision sets target sizes: the visible control can be small, the hit area can't [DC-L10-15].
- **Ask:** "What will people touch or press with: fingers, mouse, keyboard, remote, eyes and hands?"
- **Example:** Show one button with its hit area outlined for touch vs mouse.
- **Control:** multi-select
- **Options:**
  - `touch` Touch: 44x44pt iOS, 48x48dp Android; airier layouts, larger rows [S-L10-012, S-L10-072].
  - `pointer` Mouse or trackpad: macOS 28pt default (20 minimum); denser layouts with hover states [S-L10-012].
  - `keyboard` Keyboard: visible focus everywhere (DC-L08-11) [DC-L10-15].
  - `remote` Remote or focus: tvOS 66pt, focus highlights and expands items [S-L10-012, S-L10-015].
  - `spatial` Eyes and hands: visionOS 60pt, centers 60pt apart [S-L10-012, S-L10-013].
- **Default:** touch + pointer + keyboard; 44 CSS px targets on web even though AA requires 24, plus a pointer density mode for desktop. *Source:* platform convention [DC-L10-15; S-L10-036].
- **Decides:** DC-L10-15
- **Changes:** DC-L14-03, DC-L03-12, DC-L03-13, DC-L14-06 · blocks: Foundations > Interaction > Input modality and targets
- **Preview:** a button row with its hit area outlined for each input.
- **Use / avoid:** use the touch target size for anything a finger can reach, including web; use pointer-sized visuals only with a hit area padded to the floor; avoid drag-only interactions without a non-drag alternative (WCAG 2.5.7) [DC-L10-15; S-L10-083].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L10-15; S-L10-012, S-L10-036, S-L10-072, S-L10-073, S-L10-083
- **Merges:** P16, D2

### Q-plat-04 · Will anyone use the product while driving, moving, or wearing a headset? · Standard
- **Show if:** Q-plat-02 marks car, watch or spatial as first-class or works
- **Why:** In a vehicle context, distraction limits become hard errors, not warnings [DC-L14-11].
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
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L14-11; S-L14-031, S-L14-032, S-L14-037, S-L14-008
- **Merges:** D4

### Q-plat-09 · Which OS versions do you support? · Expert
- **Show if:** Q-plat-01 includes ios or android
- **Why:** A floor at the newest OS lets the system assume glass chrome, dynamic color and edge-to-edge; a lower floor forces dual designs [DC-L10-23].
- **Ask:** "Which OS versions must you support?"
- **Example:** Show a matrix of assumed features: glass, dynamic color, edge-to-edge.
- **Control:** single choice per platform
- **Options:**
  - `current-prev` Current and previous major: design for the current language, older versions fall back to their native look [DC-L10-23].
  - `apple-26` Apple 26+: Liquid Glass everywhere; apps built with the 27 SDKs cannot keep the old look [S-L10-005, S-L10-076].
  - `android-12` Android 12+: dynamic color available [S-L10-019]; 14+ nonlinear font scaling to 200% [S-L10-071]; 15+ edge-to-edge enforced [S-L10-023]; 16+ predictive back [S-L10-020].
  - `older` Older floors: conservative, dual-design choices [DC-L10-23].
- **Default:** current-prev. *Source:* card heuristic, design for the OS users will have when you ship [DC-L10-23].
- **Decides:** DC-L10-23
- **Changes:** DC-L10-05, DC-L10-11, DC-L10-12, DC-L10-14 · blocks: Platforms > Scope > OS versions
- **Preview:** a matrix of which platform features (glass, dynamic color, edge-to-edge, predictive back) are assumed.
- **Skip:** yes.
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L10-23; S-L10-005, S-L10-019, S-L10-020, S-L10-023, S-L10-071, S-L10-076
- **Merges:** P24

---

## Stage 05 · Where the system lives
> Screen: design tool, source of truth and how engineers consume the output. Graph step 0-1. Asked before any foundation because it decides what the builder generates on every later preview [DC-L16-02]. The design-tool plan comes first because it limits where the source of truth can live (Figma REST writes need Enterprise) [DC-L07-27, DC-L07-08].

### Q-tool-03 · Which design tool does your team use, and on which plan? · Standard
- **Why:** The plan caps modes per collection, so it bounds which theming architectures fit [DC-L07-27].
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
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L07-27, DC-L16-13; S-L07-014, S-L07-015, S-L07-034, S-L16-002, S-L16-113
- **Merges:** K2.4

### Q-tool-01 · Where should the master copy of the system live? · Quick
- **Why:** Whichever side is not the source of truth drifts unless sync runs automatically; 60% of teams have no token automation [DC-L07-08; S-L11-030].
- **Ask:** "Where should the master copy live: here, a token file in git, your code, or Figma?"
- **Example:** Show a round-trip diagram for the chosen option.
- **Control:** single choice
- **Options:**
  - `builder` The builder's own model, compiled to DTCG, CSS, native code and design files in one step; design tools are push targets [DC-L16-02, DC-L11-16].
  - `token-file` A token file in git (DTCG JSON plus a Resolver); code and Figma are generated from it (Tokens Studio, Penpot write DTCG) [DC-L07-08; S-L07-002, S-L16-113].
  - `code` Code: tokens and components in code, design tools mirror it; the 2026 practitioner majority ("code is the source of truth") [DC-L11-16; COMMUNITY-SIGNAL].
  - `design-file` Design file (Figma variables): designers own tokens; fits a single web platform [DC-L07-08; S-L07-011].
- **Default:** builder; design tools are mirrors: write to Figma through its remote MCP when a Full seat exists, otherwise emit one DTCG file per mode Figma imports natively; write to Paper through its MCP. *Source:* card heuristics of L16 and L11 [DC-L16-02, DC-L11-16, DC-L16-13]; L07 prefers token-file (see Disagreements).
- **Decides:** DC-L16-02, DC-L07-08, DC-L11-16, DC-L16-13
- **Changes:** DC-L07-25, DC-L07-09, DC-L16-12, DC-L11-14 · blocks: Builder > Data > Source of truth; Tokens > Architecture > Source of truth; Builder > Interop > Design tools
- **Preview:** a round-trip diagram: which targets are generated, which only mirror, and which direction sync runs.
- **Skip:** yes, builder.
- **Time weight:** high (fan-out 9)
- **Evidence:** DC-L16-02, DC-L07-08, DC-L11-16; S-L11-030, S-L07-011, S-L16-113
- **Merges:** K2.5, K10.5

### Q-tool-02 · How will engineers consume the system? · Standard
- **Why:** Copy-in source drifts per product, CDN runtimes stay uniform, headless layers leave the look to you [DC-L09-08].
- **Ask:** "How will engineers consume it: npm package, copy-in source, CSS only, tokens only?"
- **Example:** Show the exported file tree per option.
- **Control:** multi-select
- **Options:**
  - `npm` Versioned npm component library (Carbon, Fluent, Ant, Chakra, Mantine) [DC-L09-08].
  - `copy-in` Copy-in source through a CLI and registry (shadcn) [S-L09-589].
  - `cdn` CDN runtime with a stable channel (Polaris) [S-L09-313].
  - `css-html` CSS and HTML only (GOV.UK, USWDS) [DC-L09-08].
  - `headless` Headless primitives plus your styles (Radix, Base UI) [DC-L09-08].
  - `utilities` Utility classes (Tailwind `@theme`) [S-L09-609].
  - `tokens-only` Tokens only [inferred].
- **Default:** tokens in DTCG JSON, emitted as CSS variables, Tailwind `@theme` and the shadcn contract. *Source:* card heuristic, "where generated systems land today" [DC-L09-08; S-L09-587, S-L09-609].
- **Decides:** DC-L09-08
- **Changes:** DC-L11-14, DC-L16-12, DC-L08-03 · blocks: Delivery > Packaging
- **Preview:** the file tree the builder will export for each checked channel.
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L09-08; S-L09-199, S-L09-313, S-L09-587, S-L09-589, S-L09-609
- **Merges:** K10.1

### Q-tool-04 · Should Figma components be linked to code for AI tools? · Expert
- **Show if:** Q-tool-03 is figma-org or figma-ent
- **Why:** Linked components make generated UI match the real system instead of generic React + Tailwind [DC-L07-24; S-L07-042].
- **Ask:** "Should Figma components be linked to code for AI tools?"
- **Example:** Show one MCP response with and without Code Connect.
- **Control:** single choice
- **Options:**
  - `cc-ui` Code Connect UI inside Figma, several frameworks per component [S-L07-026].
  - `cc-cli` Code Connect CLI with repo templates and property mappings [S-L07-026].
  - `none` None: the MCP emits generic React + Tailwind [S-L07-027].
  - `readiness` AI-readiness content only: meaningful names, descriptions, an Examples page (up to 200 examples) [S-L07-042].
- **Default:** cc-ui for the top 20 components, plus descriptions on every component and semantic variable and an Examples page. *Source:* card heuristic [DC-L07-24].
- **Decides:** DC-L07-24
- **Changes:** DC-L11-23 · blocks: Tooling > Design-code bridge
- **Preview:** a sample MCP response for one component, with and without linkage.
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L07-24; S-L07-026, S-L07-027, S-L07-042

---

## Stage 06 · Visual direction
> Screen: the overall look before any single foundation. Graph step 2-3. Cycle kept together: DC-L15-01 (style preset) + DC-L15-04 (density voice): a minimal style needs low density to stay usable, and a dense layout needs a style with strong signifiers [DC-L15-01, DC-L15-04; S-L15-004]. Quick mode derives every answer here from Q-aud-01 and the personality sliders.

### Q-dir-01 · Which overall visual style fits the product? · Standard
- **Why:** The style preset moves depth, materials, radius, borders and chroma together (fan-out 12) [DC-L15-01].
- **Ask:** "Which overall style fits: flat, tonal, glass, neo-brutalist, soft, or maximal?"
- **Example:** Show one product screen in each style.
- **Control:** single choice (visual cards)
- **Options:**
  - `flat2` Flat 2.0: mostly flat surfaces, subtle shadows or tonal steps, clear signifiers; neutral, efficient, timeless (Carbon, Primer, Polaris, Fluent) [S-L15-009].
  - `tonal` Material tonal: tonal surface steps and dynamic color; friendly and systematic (M3; Expressive adds shapes and springs) [DC-L15-01].
  - `glass` Glass or material: translucent controls and navigation only, 35% dimming under clear glass; premium and native on Apple, can obscure content (Liquid Glass, Fluent Acrylic) [S-L15-073, S-L15-005, S-L15-007].
  - `neo-brutalist` Neo-brutalist: thick borders, solid 4px offset shadow, 2-3 bold colors, quirky display face; bold, indie, irreverent (Figma and Gumroad brands) [S-L15-006].
  - `soft` Soft or neumorphic: extruded same-color surfaces with paired soft shadows; tactile but vague; offered only with a contrast warning [S-L15-060].
  - `maximal` Expressive or maximal: vibrant palettes, overlapping visuals, bold type; energetic but busy; marketing surfaces only [S-L15-050].
- **Default:** flat2 with strong signifiers. *Source:* card heuristic; keep the app on a durable base and reserve fashionable styles for marketing [DC-L15-01].
- **Decides:** DC-L15-01
- **Changes:** DC-L04-10, DC-L04-15, DC-L04-02, DC-L04-07, DC-L01-10, DC-L15-05, DC-L15-08, DC-L15-09 · blocks: Foundations > Visual language > Style preset
- **Preview:** one product screen (nav, card, form, table) rendered in each style, with contrast warnings on soft and glass.
- **Use / avoid:** use flat 2.0 or tonal for app surfaces people use daily; use glass only on the functional layer (bars, controls, sheets) and never on reading surfaces; keep neo-brutalist and maximal for marketing or indie products; avoid soft/neumorphic for anything interactive unless borders are added to reach 3:1 [DC-L15-01; S-L10-008 via DC-L10-12].
- **Skip:** yes; Quick maps sliders A, C and E to a preset [inferred from L06 section 4.2].
- **Time weight:** high (fan-out 12)
- **Evidence:** DC-L15-01; S-L15-004, S-L15-005, S-L15-006, S-L15-009, S-L15-060, S-L15-073

### Q-dir-02 · How much should fit on a screen? · Standard
- **Why:** Spacious layouts look confident but slow repeat users; compact layouts look efficient but need strong grouping and signifiers [DC-L15-04; S-L15-003, S-L15-004].
- **Ask:** "How much should fit on a screen: compact, comfortable, or spacious?"
- **Example:** Show a data table at each density.
- **Control:** single choice (pre-filled from Q-aud-01)
- **Options:**
  - `compact` Compact: serious, efficient, expert; more data per screen (Carbon table rows from 24px) [S-L08-062; DC-L15-04].
  - `comfortable` Comfortable: calmer, touch-friendly, consumer feel [DC-L08-13].
  - `spacious` Spacious: calm, premium, focused message [DC-L15-04].
  - `user-selectable` User-selectable: default plus a compact mode (Atlassian `spacing="compact"`, Salesforce comfy/compact) [S-L08-063; DC-L03-10].
- **Default:** comfortable for app surfaces, spacious for marketing, compact as a user option for data-heavy components (tables, lists, menus, trees). *Source:* card heuristic [DC-L15-04, DC-L08-13].
- **Decides:** DC-L15-04, DC-L08-13
- **Changes:** DC-L15-02, DC-L15-05, DC-L15-09, DC-L03-10, DC-L03-11, DC-L02-08 · blocks: Foundations > Visual language > Density voice; Components > Density
- **Preview:** a data table and a settings form at each density, with the target-size floor drawn so it visibly does not shrink [DC-L15-04].
- **Use / avoid:** use compact for data-heavy components (tables, lists, menus, trees); use spacious for marketing and focused tasks; avoid shrinking targets with density; they stay at the floor in every mode [DC-L15-04, DC-L08-13; S-L08-070].
- **Skip:** yes.
- **Time weight:** high (fan-out 8)
- **Evidence:** DC-L15-04, DC-L08-13; S-L15-003, S-L15-004, S-L08-062, S-L08-063, S-L08-070
- **Merges:** K6.3 (density modes part)

### Q-dir-03 · How dramatic should the difference between headings and body text be? · Standard
- **Why:** Hierarchy strength sets the type ratio, weights and text-color tiers; too subtle makes levels "almost match", too dramatic leaves few usable steps [DC-L15-02; S-L15-070].
- **Ask:** "How dramatic should headings be compared with body text?"
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
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L15-02; S-L15-002, S-L15-028, S-L15-033, S-L15-038, S-L15-070

### Q-dir-04 · How should related things be grouped? · Standard
- **Why:** Grouping sets whether surfaces use space, cards or lines, which drives surface colors, dividers and whitespace [DC-L15-05].
- **Ask:** "Should related things be grouped by space, cards, or lines?"
- **Example:** Show one settings page grouped three ways.
- **Control:** single choice
- **Options:**
  - `space` Space first: proximity only, outer gaps larger than inner; lighter, calmer, modern (Refactoring UI "Use fewer borders"; Carbon, Fluent) [S-L15-037; DC-L03-24].
  - `containers` Containers first: cards and tinted panels; structured, "enterprise"; "boxes in boxes" when overused [S-L15-012].
  - `lines` Lines first: rules and separators; orderly, editorial, busy if lines multiply [S-L15-033, S-L15-053].
- **Default:** space first; containers when content types mix or items sit in a grid; lines for long lists; inner:outer spacing at 1:2 or more. *Source:* card heuristic [DC-L15-05; DC-L03-24].
- **Decides:** DC-L15-05
- **Changes:** DC-L01-13, DC-L03-24, DC-L04-08, DC-L08-15 · blocks: Foundations > Visual language > Grouping
- **Preview:** a settings page grouped each way.
- **Use / avoid:** use space for simple groups, containers for mixed content or grids, lines for long homogeneous lists; avoid nesting containers inside containers [DC-L15-05; S-L15-012].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L15-05; S-L15-010, S-L15-012, S-L15-033, S-L15-037, S-L15-053

### Q-dir-05 · Should layouts be start-aligned or centered? · Expert
- **Why:** Alignment sets the text alignment defaults and where centered layouts are allowed [DC-L15-08].
- **Ask:** "Start-aligned layouts, or centered?"
- **Example:** Show an empty state and a form in each alignment.
- **Control:** single choice
- **Options:**
  - `start` Start-aligned, asymmetric: efficient, modern, scannable (Apple's "top and leading side") [S-L15-053, S-L15-072].
  - `centered` Centered, symmetric: calm, ceremonial, "landing page"; long centered text reads poorly [S-L15-001; inferred].
  - `radial` Radial: rare in UI (gauges, radial menus) [S-L15-001, S-L15-050].
- **Default:** start-aligned everywhere; center only single-focus moments with short text (empty states, dialogs, sign-in). *Source:* card heuristic [DC-L15-08].
- **Decides:** DC-L15-08
- **Changes:** DC-L02-18 · blocks: Foundations > Layout > Balance
- **Preview:** an empty state and a form in each alignment.
- **Use / avoid:** use centered layouts for single-focus moments with short text (empty states, dialogs, sign-in); avoid centering multi-line body text [DC-L15-08].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L15-08; S-L15-001, S-L15-033, S-L15-049, S-L15-053

---

## Stage 07 · Themes and modes
> Screen: which variations of the system exist. Graph step 0-2. Asked before color because every color decision must be made once per mode [DC-L07-15; BOARD L01 note: dark mode is always a separate mapping].

### Q-theme-01 · Which appearance modes does the product support? · Standard
- **Why:** Dark mode is a separate mapping, not an inversion, so each mode doubles color decisions and contrast checks [DC-L10-17; S-L10-089].
- **Ask:** "Light and dark following the system, or one mode only?"
- **Example:** Show the preview split diagonally, light and dark.
- **Control:** single choice
- **Options:**
  - `system-light-dark` Light and dark, following the system setting: blends with the OS at night (Apple expects apps to respect the preference) [S-L10-089].
  - `light-dark-toggle` Light and dark plus an in-app override: web only, in addition to system-follow [DC-L10-17].
  - `light-only` Light only [DC-L07-15].
  - `dark-only` Dark only: brand colors glow, fewer and brighter accents (watch, TV, car at night) [DC-L14-09].
- **Default:** system-light-dark on phone, tablet, desktop and web; dark-only on watch; day/night auto in cars. *Source:* L09 shared default row 6 (21 of 25 systems) and platform convention [L09 A1; DC-L10-17, DC-L14-09].
- **Decides:** DC-L10-17, DC-L14-09
- **Changes:** DC-L01-18, DC-L01-19, DC-L04-13, DC-L07-15, DC-L07-17 · blocks: Foundations > Color > Appearance modes
- **Preview:** the draft screen split diagonally, light and dark.
- **Use / avoid:** use system-following modes on Apple platforms; offer an in-app toggle only on web and only in addition; avoid an app-only appearance switch on Apple, which reads as broken [DC-L10-17; S-L10-089].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L10-17, DC-L14-09; S-L10-089, S-L10-027, S-L14-037, S-L11-030
- **Merges:** K6.1, P18

### Q-theme-02 · Which other theme axes should exist? · Expert
- **Why:** Each extra axis multiplies the values to check: 2 modes x 3 brands = 6 palettes to contrast-test [DC-L11-25, DC-L07-15].
- **Ask:** "Besides light and dark, which other theme variations do you need?"
- **Example:** Show the palette count, e.g. '2 modes x 2 contrasts = 4 palettes to test'.
- **Control:** multi-select (pre-filled from Q-aud-04)
- **Options:**
  - `contrast` Contrast: standard and high (Material standard/medium/high; Atlassian increased contrast; Primer 14 theme files incl. color-blind variants) [S-L07-104, S-L07-108, S-L07-110].
  - `density` Density or scale: compact/comfortable (Radix scaling 90-110%) [S-L11-068].
  - `brand` Brand: see Q-theme-03 [DC-L07-16].
  - `breakpoint` Breakpoint values (38% of systems) [S-L11-030].
  - `platform` Platform values (24% of systems) [S-L11-030].
- **Default:** color scheme + contrast; density only with data-dense screens; brand only with a real second brand. *Source:* card heuristic [DC-L07-15, DC-L11-25].
- **Decides:** DC-L07-15, DC-L11-25
- **Changes:** DC-L07-01, DC-L07-17, DC-L07-18, DC-L01-20 · blocks: Tokens > Theming > Modes; Foundations > Theming scope
- **Preview:** a mode-combination grid with the count of palettes to test, and the Figma mode budget from Q-tool-03.
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L07-15, DC-L11-25; S-L07-004, S-L07-104, S-L07-110, S-L11-030
- **Merges:** K6.3 (breakpoint modes), K6.4

### Q-theme-03 · Will other brands, products or clients re-skin this system? · Standard
- **Why:** Locked systems look consistent; generator systems keep structure and vary hue; theme-swap systems can change shape and depth too [DC-L09-07].
- **Ask:** "Will other brands, products or clients re-skin this system?"
- **Example:** Show the preview re-skinned with two sample brand colors.
- **Control:** single choice
- **Options:**
  - `locked` One brand, locked (Carbon, Primer, Geist) [DC-L09-07].
  - `generator-ready` One brand now, built generator-ready: semantic tier + brand-color generator + contrast check [DC-L09-07].
  - `brand-themes` Several internal brands over one core: shared anatomy and behavior, different color, type, imagery (Brad Frost core + brand + sub-brand layers; Swiggy > Instamart) [S-L06-053, S-L06-066].
  - `white-label` White-label clients: one brand color in, full theme out (Blade `createTheme({brandColor})`, Fluent 16-step ramp, Paste overrides) [DC-L09-07; S-L09-459].
- **Default:** generator-ready. *Source:* card heuristic "build every system as if a second brand will come" [DC-L09-07]; 63% of systems theme by brand [S-L11-030].
- **Decides:** DC-L09-07
- **Changes:** DC-L07-16, DC-L06-16, DC-L06-17, DC-L06-06, DC-L07-01 · blocks: Theming > Brands and modes
- **Preview:** the draft screen re-skinned with two sample brand colors, contrast re-checked live.
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L09-07; S-L09-170, S-L09-237, S-L09-459, S-L06-053, S-L11-030
- **Merges:** K6.2, B10

### Q-theme-04 · What may differ between brands, and how is that stored? · Expert
- **Show if:** Q-theme-03 is brand-themes or white-label
- **Why:** If brands differ in more than about 20% of semantic tokens, they are separate themes, not brands [DC-L07-16].
- **Ask:** "What may differ between brands, and how should brands be stored?"
- **Example:** Show a table of brandable tokens per brand.
- **Control:** multi-select (what flexes) + single choice (storage)
- **Options:**
  - `flex-color-type-imagery` Flex brand color, typeface, logo, imagery; fix anatomy, behavior, semantic names, status meanings [DC-L06-16].
  - `flex-with-care` Also flex radius, density and motion ("flex with care") [DC-L06-16].
  - `store-mode` Brand as a mode: simple, capped by the plan's mode limit (Pro 10, Org 20) [S-L07-014].
  - `store-axis` Brand as its own axis (collection or DTCG resolver modifier): additive, 3 brands + 2 schemes = 5 modes [DC-L07-16].
  - `store-extended` Figma extended collections (Enterprise): brands override only what differs [S-L07-015, S-L07-016].
- **Default:** flex color, typeface, logo, imagery; store as its own axis (extended collections on Enterprise). *Source:* card heuristics [DC-L07-16, DC-L06-16].
- **Decides:** DC-L07-16, DC-L06-16
- **Changes:** DC-L07-17, DC-L07-18, DC-L06-17 · blocks: Tokens > Theming > Brands
- **Preview:** a table of brandable tokens with each brand's values.
- **Skip:** yes.
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L07-16, DC-L06-16; S-L07-011, S-L07-014, S-L07-015, S-L06-053, S-L06-094

---

## Stage 08 · Color system
> Screen: one screen with four sections (brand input, strategy, ramps and neutrals, roles and contrast) around one shared live preview: a product screen, the generated ramps, and a contrast matrix of every foreground/background pair, in light and dark. Graph step 1-4. Cycle kept together: the 21-card color cycle (DC-L01-01 to DC-L01-13, DC-L01-15, DC-L01-18, DC-L01-21 to DC-L01-24, DC-L15-03, DC-L15-06) plus the two-card cycle DC-L10-04 + DC-L10-05. Changing any answer here regenerates the whole palette, so the questions share one preview instead of separate screens [inferred from the cycle].

### Q-color-01 · Do you have fixed brand colors, or should the builder generate the palette from one color? · Quick
- **Why:** Hand-picked hexes keep brand nuance; a seed algorithm gives even ramps; contrast targets give predictable legibility across hues (L09 divergence 6) [DC-L09-03].
- **Ask:** "Do you have fixed brand colors, or should I generate the palette from one color?"
- **Example:** Ask for hex values; if none, offer 3 seed swatches weighted by the sliders.
- **Control:** color picker (1-3 seeds, each lockable) + single choice (method)
- **Options:**
  - `keep-hex` Keep exact brand hexes and hand-tune ramps around them (Carbon, Primer, Atlassian, GOV.UK) [DC-L09-03].
  - `seed` Generate from one seed color (Material HCT, Ant, Blade `createTheme`, Fluent brand ramp) [S-L09-459; DC-L09-03].
  - `seed-3` Generate from three inputs: brand color, neutral base and contrast (Linear replaced 98 per-theme variables with 3) [S-L06-012; DC-L06-06].
  - `contrast-targets` Generate by contrast targets so each step has a known ratio (Spectrum Leonardo, USWDS grades, Radix APCA steps) [DC-L09-03].
- **Default:** seed-3 in OKLCH with contrast-checked steps; locked brand hexes are pinned to the nearest step, and the UI fill uses the step that reaches 4.5:1 with its text. *Source:* card heuristics [DC-L09-03, DC-L06-06, DC-L01-09].
- **Decides:** DC-L09-03, DC-L01-09
- **Changes:** DC-L01-01, DC-L01-03, DC-L01-04, DC-L06-06, DC-L15-06 · blocks: Foundations > Color > Palette generation
- **Hook:** Accepts hex, RGB or OKLCH values, a brand book PDF, or a reference from Q-ref-01. If no brand color exists: the builder suggests seeds weighted by the personality sliders (blue reads competent, red excitement, per Labrecque & Milne) and labels the choice as a starting point, not a brand decision [S-L06-072].
- **Preview:** the seed becomes ramps live; locked hexes show a pin on their step; a light brand color (yellow, cyan, lime) visibly switches its button text to dark (Spectrum does this) [S-L01-036].
- **Use / avoid:** use the brand hex as a ramp anchor and pick UI steps by contrast; avoid using a brand color whose ratio with white is below 3:1 for small text; use it as a fill with dark text or as a tint [DC-L01-09; S-L01-044].
- **Skip:** yes, a seed is suggested.
- **Time weight:** high (fan-out 3)
- **Evidence:** DC-L09-03, DC-L01-09, DC-L06-06 (context); S-L09-459, S-L09-563, S-L06-012, S-L01-036, S-L01-044
- **Merges:** K3.4, B7 (brand colors), K7.1 (ramp method)

### Q-color-02 · Where should your brand color appear? · Quick
- **Why:** Brand color placement is third on L09's (inferred) ranking of visual differences: actions only, containers, or whole surfaces (L09 divergence 3) [DC-L06-04].
- **Ask:** "Where should your brand color appear: only on key actions, on one signature area, or across the chrome?"
- **Example:** Show the same screen with each placement.
- **Control:** single choice (with platform overrides in Expert)
- **Options:**
  - `accent` Reserved accent on primary actions, links, status, selected tab: calm, content-first (Apple HIG, Carbon) [S-L06-008, S-L06-001].
  - `signature-surface` One signature surface carries the brand: instantly recognizable silhouette (Slack aubergine sidebar) [S-L06-030].
  - `flooded-chrome` Brand-flooded chrome, colored app bars and FABs: playful, louder (M2 style, rated more playful) [S-L06-011].
  - `content-layer` Brand in the content layer, scrolling beneath glass controls: modern, dynamic (Apple 2026) [S-L06-100, S-L10-009].
  - `neutral-first` Neutral first with a restrained chrome tint (Linear limited how much blue chrome it used) [S-L06-012].
- **Default:** accent, with signature-surface optional; on Apple glass platforms brand color moves into content, on Android a brand seed, freer on web. *Source:* card heuristics [DC-L06-04, DC-L10-04]; L09 shared pattern row 3 (neutral surfaces + one accent in all but one of 24 systems).
- **Decides:** DC-L06-04, DC-L10-04
- **Changes:** DC-L15-03, DC-L01-13, DC-L08-05, DC-L01-08 · blocks: Foundations > Color > Brand color role; Foundations > Color > Brand accent > Platform application
- **Preview:** the preview screen re-renders per option; on iOS, a tinted nav bar is flagged as "fighting the glass" [S-L10-009, S-L10-010].
- **Use / avoid:** use brand color on the one element per view that matters most; avoid tinting several control backgrounds at once ("Using your brand color too broadly can overwhelm your interface") [S-L06-008].
- **Skip:** yes, accent.
- **Time weight:** high (fan-out 3)
- **Evidence:** DC-L06-04, DC-L10-04; S-L06-008, S-L06-011, S-L06-030, S-L10-009, S-L10-010
- **Merges:** P5

### Q-color-03 · How colorful should the palette be? · Standard
- **Why:** Chroma sets how calm or energetic the product reads; high chroma weakens status colors because everything shouts [DC-L01-10].
- **Ask:** "How colorful should the palette be, from monochrome to vivid?"
- **Example:** Show a chroma slider moving surfaces, accent and status together.
- **Control:** single choice (pre-filled from sliders A and D)
- **Options:**
  - `monochrome` Monochrome or neutral: calm, premium, technical (Material Monochrome and Neutral variants, chroma 0 and 8-12; Polaris black brand) [S-L01-010, S-L01-039].
  - `tonal` Tonal, low to medium colorfulness: friendly, balanced (Material TonalSpot, primary chroma 32-36) [S-L01-010, S-L06-083].
  - `vivid` Vivid: energetic, consumer-grade (Material Vibrant; Tailwind v4 P3-leaning OKLCH, blue-500 chroma 0.214) [S-L01-010, S-L01-062].
  - `expressive` Expressive, hue-rotated away from the source color (Material Expressive) [S-L06-083].
  - `fidelity` Fidelity: the brand hue stays exact in containers; for hues that are a legal or recognition asset [S-L06-083; DC-L06-05].
- **Default:** tonal for productivity products, vivid for consumer and marketing. *Source:* card heuristic [DC-L01-10, DC-L06-05].
- **Decides:** DC-L01-10, DC-L06-05
- **Changes:** DC-L01-15, DC-L01-24, DC-L15-06 · blocks: Foundations > Color > Palette character > Vibrancy; Foundations > Color > Scheme strategy
- **Preview:** a chroma slider under the five named stops; surfaces, accent and status chips update together.
- **Use / avoid:** use low chroma on large areas (surfaces) and spend chroma on small, high-meaning elements (primary action, status, selection); avoid vivid surfaces in high-trust categories [DC-L01-10; S-L01-013, S-L06-010].
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L01-10, DC-L06-05; S-L01-010, S-L01-058, S-L01-062, S-L06-083, S-L06-072

### Q-color-04 · How many accent colors does the product need? · Standard
- **Why:** One accent makes every colored element read as actionable; three accents feel expressive but need discipline [DC-L01-08].
- **Ask:** "How many accent colors does the product need? One is usual."
- **Example:** Show the screen with each accent's job highlighted.
- **Control:** single choice
- **Options:**
  - `one` One accent plus neutrals and status: focused, calm (Carbon core blue; Apple one app accent; Linear, Notion) [S-L01-029, S-L01-013; DC-L15-06].
  - `analogous` One accent with analogous tints for surfaces and illustration: harmonious, soft [S-L15-017].
  - `contrasting` A contrasting accent on analogous neutrals: the strongest "pop" for primary actions [S-L15-017].
  - `three` Primary, secondary and tertiary (Material 3: tertiary for contrasting accents such as badges) [S-L01-004].
  - `multi` Multi-accent: playful (Mailchimp), needs strict role rules [DC-L15-06].
- **Default:** one accent plus neutrals plus status, analogous tints for surfaces. *Source:* card heuristics, "harmonize the large areas, contrast the small important ones" [DC-L01-08, DC-L15-06]; L09 shared pattern row 3.
- **Decides:** DC-L01-08, DC-L15-06
- **Changes:** DC-L01-11, DC-L01-24, DC-L08-05 · blocks: Foundations > Color > Brand vs UI color > Accent count; Foundations > Color > Scheme strategy
- **Preview:** the product screen with each accent's jobs highlighted (actions, discovery, categories).
- **Use / avoid:** add an accent only when it has a job (a second action tier, discovery, categories); avoid adding one for decoration or picking wheel presets (triadic, complementary) as a palette [DC-L01-08; S-L15-025].
- **Skip:** yes.
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L01-08, DC-L15-06; S-L01-004, S-L01-013, S-L01-029, S-L15-017, S-L15-054

### Q-color-05 · How much of a screen may use accent color and emphasis? · Expert
- **Why:** Raising emphasis without a budget makes screens louder, not clearer [DC-L15-03; S-L15-067].
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
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L15-03; S-L15-026, S-L15-038, S-L15-048, S-L15-054, S-L15-067

### Q-color-06 · Should colors follow the user's wallpaper or system accent? · Standard
- **Show if:** Q-plat-01 includes android, ios or desktop
- **Why:** Following the OS feels personal and native but weakens brand recall and makes screenshots differ per user [DC-L10-05].
- **Ask:** "Should colors follow the user's wallpaper or system accent?"
- **Example:** Show the Android preview recolored by three wallpapers.
- **Control:** single choice
- **Options:**
  - `static` Fixed brand color everywhere (Material static baseline; advised for enterprise and iOS) [S-L06-082, S-L01-006].
  - `dynamic-optional` Static by default, Android dynamic color behind a user setting (API 31+) [S-L10-019; DC-L01-21].
  - `follow-os` Follow the OS: Android dynamic color, Wear OS watch-face color, macOS accent [S-L10-019, S-L10-027, S-L10-010].
- **Default:** dynamic on Android for utility apps, fixed brand for brand-led consumer apps; brand-critical and status colors stay fixed; on Apple, design icon layers for all four icon looks. *Source:* card heuristics [DC-L10-05, DC-L01-21].
- **Decides:** DC-L10-05, DC-L01-21
- **Changes:** DC-L01-15, DC-L05-12 · blocks: Foundations > Color > Personalization policy; Foundations > Color > Modes > Dynamic color
- **Preview:** the Android preview recolored with three sample wallpapers; brand-critical colors stay put.
- **Use / avoid:** let dynamic color own surfaces and secondary accents; avoid letting it change error and brand-critical colors [DC-L01-21; S-L01-004].
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L10-05, DC-L01-21; S-L10-019, S-L10-075, S-L01-006, S-L01-058, S-L06-082
- **Merges:** P6, B9

### Q-color-07 · How should color ramps be built? · Expert
- **Why:** In HSL, yellow at the same lightness looks lighter than blue; perceptual or contrast-indexed ramps keep every hue's steps equally heavy [DC-L01-01; S-L01-044].
- **Ask:** "How should ramps be built: perceptual, tone-based, contrast-based, hand-tuned or a preset?"
- **Example:** Show blue and green at the same step, HSL vs OKLCH.
- **Control:** single choice (space) + single choice (step rule) + single choice (generator)
- **Options:**
  - `oklch` OKLCH, perceptual (Tailwind v4 moved its palette to oklch in Jan 2025; CSS `oklch()` Baseline since May 2023) [S-L01-045, S-L01-046].
  - `hct` HCT, tone-indexed: same tone gives the same brightness across hues (Material; tones 50 vs 98 give 3:1) [S-L01-006].
  - `contrast-indexed` Contrast-indexed steps: every step has the same ratio across hues (Spectrum: every 700 is 3.01:1) [S-L01-035].
  - `hand-tuned` Hand-tuned per hue: more character, less predictable (Tailwind 500 steps range L 62-77%) [S-L01-062].
  - `preset` Adopt a preset palette (Tailwind default, Radix Colors): a recognizable stock look [S-L01-001, S-L01-052].
  - `lab-hsl` CIELAB/LCH or HSL: Lab was Stripe's 2019 fix; HSL is the legacy default that washes out yellows [S-L01-044].
- **Default:** OKLCH with contrast-indexed steps; HCT when the system must feed Material dynamic color. *Source:* card heuristics [DC-L01-01, DC-L01-03, DC-L01-04].
- **Decides:** DC-L01-01, DC-L01-03, DC-L01-04
- **Changes:** DC-L01-02, DC-L01-18, DC-L01-24, DC-L07-10 · blocks: Foundations > Color > Palette generation > Color space; Step semantics; Tooling
- **Preview:** two accents side by side at the same step; switching the method shows whether they stay equally heavy, with the contrast of each step printed.
- **Use / avoid:** use contrast-indexing when users can recolor the accent, so every accent passes the same pairings; avoid HSL-based lightness steps [DC-L01-03, DC-L01-01].
- **Skip:** yes.
- **Time weight:** high (fan-out 6)
- **Evidence:** DC-L01-01, DC-L01-03, DC-L01-04; S-L01-006, S-L01-035, S-L01-044, S-L01-045, S-L01-062

### Q-color-08 · How many steps should each ramp have, and how are they numbered? · Expert
- **Why:** More steps allow quieter, layered UIs; fewer steps force bolder jumps [DC-L01-02].
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
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L01-02; S-L01-001, S-L01-002, S-L01-006, S-L01-029, S-L01-036

### Q-color-09 · Should grays be pure, or tinted warm or cool? · Standard
- **Why:** Neutrals cover most of the screen, so their temperature is a personality lever (Linear moved to "a warmer gray" in 2026) [DC-L01-06; S-L06-067].
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
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L01-06; S-L01-027, S-L01-036, S-L01-053, S-L01-062, S-L06-067
- **Merges:** K3.4 (neutral palette)

### Q-color-10 · How many gray steps, and should there be transparent grays? · Expert
- **Why:** More near-white steps let cards, sidebars and wells separate without borders [DC-L01-07].
- **Ask:** "How many gray steps, and do you want transparent grays for overlays?"
- **Example:** Show the neutral ramp with background, border and text bands.
- **Control:** number (solid steps) + number (alpha steps)
- **Options:**
  - `bands` Solid neutrals with fixed usage bands (Primer 0-13: 0-5 backgrounds, 7-8 borders, 9-10 text) [S-L01-027].
  - `separate-dark` Separate light and dark neutral ramps (Atlassian Neutral and DarkNeutral) [S-L01-031].
  - `alpha` Add alpha neutrals for overlays on any surface (Radix alpha scales) [S-L01-052].
- **Default:** 12-13 solid neutrals plus 4-5 alpha neutrals, with bands documented; at least three near-white steps in light mode and four dark steps in dark mode. *Source:* card heuristic [DC-L01-07].
- **Decides:** DC-L01-07
- **Changes:** DC-L01-13, DC-L01-14, DC-L01-27 · blocks: Foundations > Color > Neutrals > Ramp and usage
- **Preview:** the neutral ramp with bands shaded (backgrounds, borders, text) and a card stack using them.
- **Use / avoid:** use alpha neutrals for hover fills and overlays that must work on any surface; avoid using alpha for text [inferred].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L01-07; S-L01-027, S-L01-029, S-L01-031, S-L01-036, S-L01-052

### Q-color-11 · Which color gamut should the system target? · Expert
- **Why:** Display P3 gives richer reds, greens and oranges on modern screens; sRGB is simplest and accurate on most displays [DC-L01-05].
- **Ask:** "sRGB only, or richer Display P3 colors where screens support them?"
- **Example:** Show accent chips in sRGB and P3.
- **Control:** single choice
- **Options:**
  - `srgb` sRGB hex only [S-L01-013].
  - `p3-enhance` sRGB with P3 overrides behind `@media (color-gamut: p3)` (Radix ships each scale twice) [S-L01-052, S-L01-049].
  - `oklch-wide` OKLCH values that may exceed sRGB, gamut-mapped by browsers (Tailwind v4) [S-L01-045, S-L01-046].
  - `native-p3` Native P3 assets on Apple platforms [DC-L01-05].
- **Default:** sRGB hex primitives with optional P3 overrides for accents only; every token keeps a hex fallback (DTCG 2025.10 supports 14 color spaces plus a hex fallback). *Source:* card heuristics [DC-L01-05, DC-L07-10; S-L07-003].
- **Decides:** DC-L01-05, DC-L07-10
- **Changes:** DC-L10-22, DC-L07-25 · blocks: Foundations > Color > Color spaces and gamut; Tokens > Types > Color
- **Preview:** accent chips in sRGB and P3 next to each other (visible only on a P3 display; otherwise a note).
- **Use / avoid:** use P3 where saturation carries brand or status meaning; avoid P3 for neutrals, where it adds nothing [DC-L01-05, inferred].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L01-05, DC-L07-10; S-L01-045, S-L01-049, S-L01-052, S-L07-003

### Q-color-12 · How should color roles be named? · Expert
- **Why:** Property-first grammars make it hard to put a border color on text; pairing grammars guarantee legible pairs [DC-L01-11].
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
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L01-11; S-L01-004, S-L01-027, S-L01-029, S-L01-032

### Q-color-13 · How many emphasis levels should each color role have? · Expert
- **Why:** More levels allow soft tinted status panels and quiet selection; two levels look punchier [DC-L01-12].
- **Ask:** "How many emphasis levels per color role?"
- **Example:** Show a banner, badge and button at each level.
- **Control:** single choice
- **Options:**
  - `two` Muted and emphasis (Primer) [S-L01-050].
  - `container` Base and container (Material `primary` tone 40, `primary-container` tone 90) [S-L01-004].
  - `three` Subtle, default, bold plus an on-bold foreground [DC-L01-12].
  - `six` Subtlest to boldest (Atlassian, up to six) [S-L01-030].
- **Default:** three levels plus on-bold. *Source:* card heuristic [DC-L01-12].
- **Decides:** DC-L01-12
- **Changes:** DC-L01-14, DC-L01-17 · blocks: Foundations > Color > Semantic roles > Emphasis
- **Preview:** a status banner, badge and button in each emphasis level.
- **Use / avoid:** use subtle levels on large areas (banners) and bold for small, urgent elements; avoid bold fills on page-size areas [DC-L01-12].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L01-12; S-L01-004, S-L01-030, S-L01-050

### Q-color-14 · How should surfaces be layered? · Standard
- **Why:** The surface model decides whether depth comes from tone steps, alternating layers, or elevation names, and how dark mode shows depth [DC-L01-13].
- **Ask:** "How should surfaces stack: tone steps, alternating layers, or elevation names?"
- **Example:** Show a page, card, popover and dialog stack in light and dark.
- **Control:** single choice (pre-filled from Q-dir-04)
- **Options:**
  - `container-tiers` Named container tiers not tied to elevation: flat, calm, modern (Material 3 `surface-container-lowest` to `-highest`) [S-L01-004, S-L01-054].
  - `alternating` Alternating layers in light, stepping lighter in dark: crisp, grid-like enterprise (Carbon White/Gray 10, then Gray 100/90/80) [S-L01-029].
  - `elevation-named` Elevation-named surfaces (Atlassian) [S-L01-032].
  - `role-tiers` 4-5 tiers named by role (base, raised, overlay, sunken), mapped separately per mode [DC-L01-13].
- **Default:** role-tiers; light mode separates with shadow or border plus a subtle tone, dark mode with lighter tones. *Source:* card heuristic [DC-L01-13]; L09 shared pattern row 12.
- **Decides:** DC-L01-13
- **Changes:** DC-L04-13, DC-L04-10, DC-L08-15 · blocks: Foundations > Color > Semantic roles > Surfaces
- **Preview:** a page, card, popover and dialog stack in light and dark, with the tier of each labeled.
- **Use / avoid:** use lighter-when-higher surfaces in dark mode; avoid separating interactive surfaces by tone alone when the edge carries meaning (needs 3:1) [DC-L01-13; S-L01-023].
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L01-13; S-L01-004, S-L01-010, S-L01-029, S-L01-032, S-L01-054

### Q-color-15 · Which status colors do you need? · Standard
- **Why:** Few statuses keep alerts unmistakable; many make dense developer UIs scannable but cost learning [DC-L01-15].
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
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L01-15; S-L01-030, S-L01-036, S-L01-050, S-L01-053, S-L01-056

### Q-color-16 · How should dark mode be derived from light? · Expert
- **Show if:** Q-theme-01 includes dark
- **Why:** Mirrored mappings keep hierarchy identical across modes; separate hand-tuned dark ramps look richer but drift [DC-L01-18].
- **Ask:** "How should dark mode be derived from light?"
- **Example:** Show both modes with failing pairs lit up.
- **Control:** single choice
- **Options:**
  - `tone-reassign` Same palettes, different tones per role (Material: primary 40 becomes 80, surface 98 becomes 6) [S-L01-010].
  - `mirrored` Mirrored ramp ("700 in light is 400 in dark") with separate dark neutrals (Atlassian) [S-L01-031].
  - `separate` Separate dark scales with the same step jobs (Radix, Primer, Spectrum) [S-L01-052, S-L01-050].
- **Default:** shared hue ramps with a mirrored mapping plus separate dark neutral ramps; map by role, not by value. *Source:* card heuristic [DC-L01-18].
- **Decides:** DC-L01-18
- **Changes:** DC-L01-19, DC-L01-24, DC-L04-13 · blocks: Foundations > Color > Modes > Dark mode mapping
- **Preview:** light and dark side by side with every pair re-checked; failing pairs light up in the contrast matrix.
- **Use / avoid:** use role-based mapping so each token keeps its contrast relationship; avoid inverting colors [DC-L01-18; S-L10-089].
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L01-18; S-L01-006, S-L01-010, S-L01-031, S-L01-052

### Q-color-17 · Which contrast rule should the builder enforce on every color pair? · Standard
- **Why:** AA allows mid-gray secondary text and softer tints; AAA forces darker text and deeper accents [DC-L01-22].
- **Ask:** "Which contrast rule should I enforce on every color pair?"
- **Example:** Show the contrast matrix with pass/fail per mode.
- **Control:** single choice (pre-filled from Q-aud-03)
- **Options:**
  - `aa` WCAG 2.2 AA: text 4.5:1, large text 3:1, UI parts 3:1; no rounding (4.499:1 fails) [S-L01-022, S-L01-023].
  - `aaa` WCAG 2.2 AAA: text 7:1, large text 4.5:1 (target for high-contrast themes: Primer, Material) [S-L01-025, S-L01-027].
  - `aa-apca` AA enforced plus APCA as an advisory second opinion on body text (Radix and Geist use APCA) [DC-L01-22; L09 A1 row 11].
- **Default:** aa-apca: AA on all pairs in every mode, AAA for high-contrast modes, APCA advisory. *Source:* accessibility rule [DC-L01-22]; WCAG 3 is still a draft [BOARD L01 note].
- **Decides:** DC-L01-22
- **Changes:** DC-L01-14, DC-L01-16, DC-L01-20, DC-L02-23 · blocks: Foundations > Color > Accessibility > Contrast
- **Preview:** the contrast matrix of all role pairs, pass/fail per mode, with the nearest passing step suggested for failures.
- **Use / avoid:** test tokens as pairs, in every mode, at build time; avoid judging a single color by eye [DC-L01-22].
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L01-22; S-L01-022, S-L01-023, S-L01-025, S-L01-027, S-L09-563

### Q-color-18 · How should meaning survive when color can't be seen? · Expert
- **Why:** About 1 in 12 men have a color vision deficiency; WCAG 1.4.1 (Level A) forbids color as the only cue [DC-L01-23; S-L01-060, S-L01-024].
- **Ask:** "How should meaning survive for color-blind users: underlined links, icons, special themes?"
- **Example:** Show the screen under red-green simulation.
- **Control:** single choice (links) + toggle (CVD themes)
- **Options:**
  - `underline-always` Underline links in body text: robust, more document-like [DC-L01-23].
  - `underline-hover` Color-only links at 3:1 against surrounding text plus a non-color cue on hover and focus (technique G183) [S-L01-024].
  - `cvd-themes` Add color-blind themes (Primer protanopia-deuteranopia and tritanopia variants) [S-L07-110].
- **Default:** underline-always; every color-coded meaning also gets an icon, text or shape. *Source:* accessibility rule [DC-L01-23].
- **Decides:** DC-L01-23
- **Changes:** DC-L01-24, DC-L05-25, DC-L01-20 · blocks: Foundations > Color > Accessibility > Not color alone
- **Preview:** the preview screen under red-green and blue-yellow simulation.
- **Use / avoid:** use a second channel whenever two meanings differ only in hue; avoid red/green-only status pairs [DC-L01-23].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L01-23; S-L01-013, S-L01-024, S-L01-036, S-L01-060

### Q-color-19 · Does the product show charts, and which chart colors does it need? · Standard
- **Why:** Chart palettes drawn from UI ramps look native; separate high-chroma palettes pop but can clash; long categorical lists become illegible [DC-L01-24].
- **Ask:** "Does the product show charts? Which chart colors?"
- **Example:** Show a bar chart, line chart and heatmap in light and dark.
- **Control:** single choice
- **Options:**
  - `none` No charts.
  - `brand-gray` One brand chart color plus gray: calm, branded, focused [DC-L05-23].
  - `categorical-6-8` A 6-8 color categorical sequence in fixed order plus one sequential ramp; diverging only for above/below-target data (Atlassian `color.chart.categorical.1-8`) [S-L01-032; DC-L05-23].
  - `carbon-14` A long ordered sequence (Carbon's 14 colors, starting Purple 70 #6929c4, Cyan 50 #1192e8) [S-L01-056].
- **Default:** brand-gray by default, categorical-6-8 for dashboards. *Source:* card heuristics [DC-L05-23, DC-L01-24].
- **Decides:** DC-L01-24, DC-L05-23
- **Changes:** DC-L05-22, DC-L05-24, DC-L05-25 · blocks: Foundations > Color > Data visualization palettes
- **Preview:** a bar chart, line chart and heatmap in light and dark, with the 3:1 check against the surface.
- **Use / avoid:** use direct labels or grouping beyond 8 categories; avoid adding more hues [DC-L01-24; S-L05-075].
- **Skip:** yes, none unless Q-scope-01 includes internal-tools.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L01-24, DC-L05-23; S-L01-023, S-L01-032, S-L01-056, S-L05-034, S-L05-075

---

## Stage 09 · Color details and accessibility modes
> Screen: the fine-grained color roles that follow from Stage 08, on the same live preview. Graph step 5-6. Mostly Expert; Standard asks only about hover feel and dark-mode darkness.

### Q-color-20 · How should hover and pressed states change color? · Standard
- **Why:** Overlays give soft, consistent feedback on any color, including dynamic ones; step shifts give crisper, exact changes per theme [DC-L01-17].
- **Ask:** "Should hover and pressed states use an overlay or a step darker?"
- **Example:** Let them hover and press a live button, row and chip.
- **Control:** single choice
- **Options:**
  - `overlay` State layers: an overlay of the content color, hover +8%, focus +10%, press +10%, drag +16% (Material 3) [S-L01-005, S-L01-065].
  - `step-shift` Step shift on the ramp: hover one step, pressed two steps toward more contrast (Carbon half steps) [S-L01-029; DC-L01-17].
  - `hybrid` Step shift by default with an overlay fallback for dynamic or user colors [DC-L01-17].
- **Default:** hybrid. *Source:* card heuristic, overlays only where the color is unknown at design time [DC-L01-17].
- **Decides:** DC-L01-17
- **Changes:** DC-L08-09, DC-L04-17, DC-L14-06 · blocks: Foundations > Color > States > Interaction states
- **Preview:** a button, list row and chip you can hover and press on the preview, with the resulting token value shown.
- **Use / avoid:** use overlays for components that sit on user or dynamic colors; avoid state changes that rely on a hue shift alone [DC-L01-17, DC-L01-23].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L01-17; S-L01-005, S-L01-029, S-L01-064, S-L01-065

### Q-color-21 · How dark should dark mode be? · Standard
- **Show if:** Q-theme-01 includes dark
- **Why:** Pure black is dramatic but smears on OLED when scrolling; near-black looks sleek; charcoal is softer for long reading [DC-L01-19; S-L01-055].
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
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-19; S-L01-010, S-L01-013, S-L01-029, S-L01-050, S-L01-055

### Q-color-22 · How many text colors, and are they solid or transparent? · Expert
- **Why:** Solid text tokens stay crisp over any background; opacity-based text blends with tinted surfaces but is less predictable [DC-L01-14].
- **Ask:** "How many text colors, solid or transparent?"
- **Example:** Show a text ladder on each surface with ratios.
- **Control:** single choice
- **Options:**
  - `solid-levels` Solid tokens per level (Carbon `$text-primary`/`$text-secondary`; Fluent `colorNeutralForeground1`) [S-L01-029, S-L01-034].
  - `opacity-levels` Opacity levels (Material 2 dark: 87%, 60%, 38% white) [S-L01-055].
  - `on-colors` Plus an on-color for every bold fill (Material `on-primary`, Primer `fgColor-onEmphasis`) [S-L01-004, S-L01-027].
- **Default:** solid primary, secondary, tertiary/placeholder, disabled, inverse, plus an on-color per bold fill; secondary text passes 4.5:1 on the lowest surface it appears on. *Source:* card heuristic [DC-L01-14]; BOARD L15 note (2-3 text colors per view).
- **Decides:** DC-L01-14
- **Changes:** DC-L02-23 · blocks: Foundations > Color > Semantic roles > Foreground
- **Preview:** a text ladder on every surface tier, each with its ratio.
- **Use / avoid:** use 2-3 text colors per view; avoid placeholder-grey for anything users must read [DC-L01-14; BOARD L15 note].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-14; S-L01-004, S-L01-010, S-L01-027, S-L01-029, S-L01-055

### Q-color-23 · How strong should borders be, and what color is the focus ring? · Expert
- **Why:** Strong outlines feel explicit and form-heavy; subtle borders plus tonal fills feel softer; a brand focus ring feels branded, a black/white ring always works [DC-L01-16].
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
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-16; S-L01-002, S-L01-004, S-L01-023, S-L01-029, S-L01-036

### Q-color-24 · Which accessibility color themes should ship? · Expert
- **Why:** High-contrast modes trade brand nuance for legibility; forced colors reduce the UI to the user's palette, so meaning carried only by fills or shadows disappears [DC-L01-20].
- **Ask:** "Which accessibility color themes should ship: high contrast, color-blind, forced colors?"
- **Example:** Show the screen in each theme.
- **Control:** multi-select (pre-filled from Q-aud-04 and Q-theme-02)
- **Options:**
  - `contrast-levels` Contrast levels standard, medium (3:1 minimum) and high (7:1) in both modes (Material) [S-L01-006].
  - `increased` Increased-contrast variant of every custom color (Apple) [S-L01-013].
  - `high-contrast` High-contrast themes at 7:1 (Primer) [S-L01-027].
  - `cvd` Color-blind themes (Primer protanopia-deuteranopia, tritanopia) [S-L01-050].
  - `forced-colors` A forced-colors-safe component layer: borders, not only fills or shadows [DC-L01-20].
- **Default:** forced-colors-safe layer always; high contrast as the first extra mode; color-blind themes for data-dense or status-heavy products. *Source:* card heuristic [DC-L01-20].
- **Decides:** DC-L01-20
- **Changes:** DC-L07-15, DC-L07-17, DC-L04-09 · blocks: Foundations > Color > Modes > Accessibility modes
- **Preview:** the preview screen in each checked theme, including a simulated forced-colors rendering.
- **Use / avoid:** use a border or icon wherever status or selection is conveyed by fill; avoid focus rings drawn only with box-shadow (forced colors removes shadows) [DC-L01-20; S-L10-031].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-20; S-L01-006, S-L01-013, S-L01-027, S-L01-048, S-L01-050

### Q-color-25 · Where are gradients allowed? · Expert
- **Why:** Gradients add energy and brand warmth but reduce clarity in dense UIs and compete with status color [DC-L01-25].
- **Ask:** "Where are gradients allowed?"
- **Example:** Show a hero gradient interpolated in sRGB vs OKLab.
- **Control:** single choice
- **Options:**
  - `brand-only` Brand and marketing surfaces only, interpolated in OKLab (Tailwind v4 default) [S-L01-066].
  - `none` No gradients anywhere [DC-L01-25].
  - `components` Gradients on components too (consumer, AI and creative products) [DC-L01-25, inferred].
- **Default:** brand-only; never on interactive components. *Source:* card heuristic [DC-L01-25].
- **Decides:** DC-L01-25
- **Changes:** DC-L05-19, DC-L06-11 · blocks: Foundations > Color > Expressive color > Gradients
- **Preview:** a hero banner with gradients interpolated in sRGB and OKLab (the sRGB one shows a gray "dead zone").
- **Use / avoid:** use a sequential palette, not a gradient, when color carries data meaning (Carbon) [S-L01-056]; avoid P3 gradients without an sRGB variant [S-L01-013].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-25; S-L01-013, S-L01-056, S-L01-066

### Q-color-26 · Should the system include transparent colors? · Expert
- **Why:** Alpha colors let hover, selection and borders pick up the surface beneath, so they look integrated on tinted surfaces and photos [DC-L01-27].
- **Ask:** "Should the system include transparent colors?"
- **Example:** Show hover over a white card, a tinted panel and a photo.
- **Control:** single choice
- **Options:**
  - `alpha-ramps` Alpha ramps mirroring every solid ramp (Radix `--blue-a1..a12`, blackA, whiteA) [S-L01-052].
  - `alpha-neutrals` Alpha neutrals only (Atlassian Neutral100A-500A) [S-L01-031].
  - `media-set` Transparent white/black for use over media (Spectrum's 8 values) [S-L01-036].
  - `runtime` Runtime opacity via `color-mix()` (Tailwind `bg-blue-500/50`) [DC-L01-27].
- **Default:** alpha-neutrals (4-5 steps) for hover, borders and scrims; solid colors for text. *Source:* card heuristic [DC-L01-27].
- **Decides:** DC-L01-27
- **Changes:** DC-L04-17, DC-L04-18 · blocks: Foundations > Color > Primitives > Alpha colors
- **Preview:** a hover state over a white card, a tinted panel and a photo, solid vs alpha.
- **Use / avoid:** use alpha when the background varies; use solid when the pair must be contrast-certified [DC-L01-27].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L01-27; S-L01-030, S-L01-031, S-L01-036, S-L01-052

---

## Stage 10 · Typeface
> Screen: which fonts, for which scripts. Graph step 2-4. Cycles kept together: DC-L02-01 + DC-L02-02 + DC-L02-03 + DC-L02-04 + DC-L02-06 + DC-L02-24 (the typeface must cover your scripts and license terms, and those in turn narrow the typeface) and DC-L06-07 + DC-L06-24 (brand typeface vs localization readiness). The preview is a type specimen in the product's own UI, with a coverage bar for each chosen script.

### Q-type-01 · Should the product use the platform's font, a neutral open font, or your own brand typeface? · Quick
- **Why:** L09 infers the typeface is the largest brand lever after color; system fonts feel native and invisible, a custom face gives instant recognition (L09 divergence 5) [DC-L09-05].
- **Ask:** "Platform font, a neutral open font like Inter, or your own brand typeface?"
- **Example:** Show the same screen in each option next to the OS chrome.
- **Control:** single choice (specimen cards)
- **Options:**
  - `system` Platform system fonts: SF Pro, Roboto, Segoe UI Variable; native, content leads (Apple, Fluent, Ant, Radix, Mantine, SLDS) [S-L02-001, S-L02-007; DC-L09-05].
  - `open-neutral` A neutral open font: the neutral SaaS look (Inter: Polaris, Chakra, Paste, Linear; Roboto: Material) [DC-L09-05].
  - `open-custom` An open font with character: IBM Plex, Geist, Public Sans, Mona Sans [DC-L09-05; S-L06-006].
  - `brand-display` Brand face for headlines, system font for body (Apple's recommendation) [S-L10-009, S-L06-008].
  - `brand-everywhere` Proprietary brand face everywhere: Uber Move, Adobe Clean, Cereal, Spotify Mix [DC-L09-05; S-L06-021, S-L06-019].
- **Default:** system for productivity and internal tools; on native platforms any brand face goes in display roles only. *Source:* card heuristics [DC-L02-01, DC-L10-06]; L09 suggests Inter or the system stack for a neutral start [DC-L09-05].
- **Decides:** DC-L09-05, DC-L02-01, DC-L06-07, DC-L10-06
- **Changes:** DC-L02-02, DC-L02-03, DC-L02-04, DC-L02-06, DC-L02-24, DC-L10-07, DC-L02-21 · blocks: Foundations > Typography > Typeface > Sourcing; Platform map
- **Preview:** the same screen set in each option, side by side with the OS chrome, so the "foreign next to OS chrome" effect is visible [DC-L02-01].
- **Use / avoid:** use system fonts when the product lives inside another OS's chrome; use a brand face when recognition is a stated goal; avoid a brand face in body text if it needs size bumps to match system legibility at 13pt [DC-L02-01, DC-L10-06].
- **Skip:** yes, system.
- **Time weight:** high (fan-out 6)
- **Evidence:** DC-L09-05, DC-L02-01, DC-L06-07, DC-L10-06; S-L02-001, S-L02-007, S-L06-031, S-L10-009, S-L09-213
- **Merges:** K3.5, B8, P7

### Q-type-02 · Do you have the brand typeface files and a license that covers web and apps? · Standard
- **Show if:** Q-type-01 is brand-display or brand-everywhere
- **Why:** A brand typeface is a block the builder cannot create; its license and files decide where it may be used and how it loads [DC-L02-06; BRIEF requirement 2].
- **Ask:** "Do you have the brand font files and a license for web and apps?"
- **Example:** Ask for WOFF2 or OTF files; if none, offer 3 open-source faces with a similar feel.
- **Control:** single choice + file upload + license checkboxes (web, iOS/Android apps, embedding)
- **Options:**
  - `yes` Yes: files and license in hand.
  - `license-only` Licensed but files not yet supplied.
  - `no` No: see the Hook line.
- **Default:** WOFF2, one variable file per family, `font-display: swap` with a metric-adjusted fallback, subsets per script. *Source:* card heuristic [DC-L02-06].
- **Decides:** DC-L02-06
- **Changes:** DC-L02-04, DC-L02-24, DC-L10-22 · blocks: Foundations > Typography > Typeface > Delivery
- **Hook:** Accepts WOFF2 for web, OTF or TTF for native apps, variable files preferred; the builder reads axes (wght, opsz) and Unicode coverage from the file. OS system fonts must not be embedded (Apple) [S-L02-001]. If no: (1) pick an open-source face under the SIL OFL with a similar personality (Inter, Roboto Flex, Noto, Google Sans Flex, IBM Plex) [S-L02-026, S-L02-012]; (2) license a commercial face, noting per-domain, per-app or per-pageview terms [inferred]; (3) commission a custom face from a type foundry, with the caveat that it is slow and costly (Google needed three iterations to make one brand face work at small sizes) [S-L06-031].
- **Preview:** the loaded font in the specimen, with a first-load simulation showing `swap` reflow vs `optional` stability [S-L02-042].
- **Use / avoid:** use at most 2 families and 1 variable file each on first load; avoid `font-display: block` for body text (brief invisible text) [DC-L02-06; S-L02-042].
- **Skip:** yes; the system stack stands in until files arrive.
- **Time weight:** medium (fan-out 1)
- **Evidence:** DC-L02-06; S-L02-001, S-L02-012, S-L02-026, S-L02-042, S-L06-031
- **Merges:** K3.5 (licensing), B7 (typeface licences)

### Q-type-03 · Which kind of typeface fits the personality? · Standard
- **Why:** Classification carries personality: neutral, friendly, warm, editorial or technical [DC-L02-02, DC-L06-08].
- **Ask:** "Which kind of typeface fits: neutral grotesque, geometric, humanist, serif, slab or rounded?"
- **Example:** Show 'Il1 O0 rn m' at 12-14px for each candidate.
- **Control:** single choice (pre-filled from sliders F, B, A and D)
- **Options:**
  - `neo-grotesque` Neo-grotesque sans: neutral, efficient, "invisible" (Inter, SF Pro, Roboto; Apple, Material, Polaris) [S-L02-049; DC-L02-02].
  - `geometric` Geometric sans: modern, friendly, fashionable, weaker in long text (DM Sans, Poppins; Google Sans lineage) [S-L02-049, S-L02-024].
  - `humanist` Humanist sans: warm, approachable, very legible small (Segoe, IBM Plex Sans often grouped here) [S-L02-049].
  - `serif` Serif: editorial, heritage (Cooper for Mailchimp's sincerity) [S-L06-028].
  - `slab` Slab serif: publishing heritage, "friendly slab" [S-L06-078].
  - `rounded` Rounded terminals: "personal, playful" (Google Sans Flex ROND axis) [S-L06-031].
- **Default:** neo-grotesque or humanist sans with a large x-height. *Source:* card heuristic [DC-L02-02]; slider mapping [DC-L06-08].
- **Decides:** DC-L02-02, DC-L06-08
- **Changes:** DC-L02-03, DC-L02-14, DC-L05-03 · blocks: Foundations > Typography > Typeface > Classification; Personality
- **Preview:** a specimen with the confusable-pairs test (Il1, O0, rn/m) at 12-14px for each candidate.
- **Use / avoid:** use geometric faces for headlines, humanist or neo-grotesque for body; avoid any face that fails the confusable-pairs test at 12-14px or lacks your scripts [DC-L02-02].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L02-02, DC-L06-08; S-L02-024, S-L02-049, S-L06-028, S-L06-031, S-L06-078

### Q-type-04 · Which languages and scripts must the product support, now and within two years? · Standard
- **Why:** Scripts veto typefaces: without a matched fallback, Hindi next to a brand Latin face looks a different size and sits off the baseline; labels need room to grow [DC-L02-24, DC-L06-24].
- **Ask:** "Which languages and scripts must work now and within two years? Any right-to-left?"
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
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L02-24, DC-L06-24; S-L02-026, S-L02-051, S-L02-053, S-L06-101, S-L06-019
- **Merges:** K5.1, K5.2, B14

### Q-type-05 · One type family, or a pair? · Expert
- **Why:** One family feels calm and coherent; a serif or display partner adds editorial contrast [DC-L02-03].
- **Ask:** "One type family, or a pair?"
- **Example:** Show a hero and a product panel per pairing.
- **Control:** single choice
- **Options:**
  - `one` One family for everything; weights and optical sizes create contrast (Windows, Apple, Fluent, Polaris guidance) [S-L02-022, S-L02-001].
  - `superfamily` One family with display and text cuts (Google Sans + Google Sans Text; Inter Display + Inter at Linear) [S-L02-006, S-L06-012].
  - `sans-serif` Sans for UI plus a serif (Carbon: Plex Sans and Plex Serif) [S-L02-011].
  - `display-face` A distinct display face for brand moments [DC-L02-03].
- **Default:** 1 UI family + 1 mono, with an optional serif or display face for marketing. *Source:* card heuristic [DC-L02-03].
- **Decides:** DC-L02-03
- **Changes:** DC-L02-06, DC-L02-15 · blocks: Foundations > Typography > Typeface > Families and pairing
- **Preview:** a marketing hero and a product panel with each pairing.
- **Use / avoid:** add a second face only for a change of job (display vs text, code); avoid near-identical pairs that read as a mistake [DC-L02-03; L15 P49].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L02-03; S-L02-001, S-L02-006, S-L02-011, S-L02-022

### Q-type-06 · Which font for code and numbers? · Expert
- **Why:** Mono reads technical; tabular figures stop numbers jittering in tables and live values [DC-L02-05; S-L02-052].
- **Ask:** "Which font for code and numbers, and should table numbers be tabular?"
- **Example:** Show a live counter with proportional vs tabular digits.
- **Control:** single choice + toggle (tabular numbers in tables)
- **Options:**
  - `system-mono` System mono stack (`ui-monospace, SFMono-Regular, ...`: Primer, Polaris) [S-L02-017, S-L02-014].
  - `brand-mono` Brand mono (IBM Plex Mono code-01 12/16; Atlassian Mono) [S-L02-011, S-L02-015].
  - `numeric-face` A dedicated numeric or metric style for KPIs (Fluent Bahnschrift; Atlassian `font.metric.large` 28/32) [S-L02-008, S-L02-015].
- **Default:** system mono stack plus `tabular-nums` on numeric table cells; a metric style only if the product has dashboards. *Source:* card heuristic [DC-L02-05].
- **Decides:** DC-L02-05, DC-L02-26
- **Changes:** DC-L02-26, DC-L05-24 · blocks: Foundations > Typography > Typeface > Monospace / numeric
- **Preview:** a code block, a table column and a live counter with proportional vs tabular figures.
- **Use / avoid:** use tabular figures in tables, clocks and anything that updates; avoid mono for body text [DC-L02-05; S-L02-052].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L02-05; S-L02-008, S-L02-011, S-L02-014, S-L02-015, S-L02-052

### Q-type-07 · Should the font use variable weights and automatic optical sizing? · Expert
- **Why:** Optical sizing makes small text sturdier and large text sleeker; without it, display text in a text cut looks clunky [DC-L02-04].
- **Ask:** "Use variable weights and automatic optical sizing where the font supports it?"
- **Example:** Show 11px to 64px with opsz on and off.
- **Control:** single choice
- **Options:**
  - `static` Static fonts, discrete weights (Roboto as applied by M3 components) [S-L02-053].
  - `variable-wght` Variable weight axis, including in-between weights (Polaris 450/550/650) [S-L02-014].
  - `variable-opsz` Variable weight plus optical size tied to font size (SF Pro, Segoe UI Variable 8-36pt, Inter opsz 14-32; Material sets opsz = font size) [S-L02-001, S-L02-022, S-L02-026].
- **Default:** variable-opsz when the face has it; otherwise separate display tracking and line-height values above about 24px. *Source:* card heuristic [DC-L02-04].
- **Decides:** DC-L02-04
- **Changes:** DC-L02-14, DC-L02-15, DC-L02-06 · blocks: Foundations > Typography > Typeface > Variable axes
- **Preview:** a size ramp from 11px to 64px with opsz on and off.
- **Use / avoid:** use opsz tied to size; avoid setting display sizes in a text cut without tracking adjustments [DC-L02-04, DC-L02-14].
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L02-04; S-L02-001, S-L02-014, S-L02-022, S-L02-026, S-L02-053

---

## Stage 11 · Type scale and text
> Screen: sizes, line heights, weights and text behavior, on a live type ladder next to a real product screen. Graph step 0-5. Cycle kept together: DC-L02-13 + DC-L02-25 (line heights must fit each script's height category, and script metrics are set relative to the line-height system). Mostly pre-filled from Q-aud-01 (density) and Q-dir-03 (hierarchy strength).

### Q-type-08 · What size should body text be? · Standard
- **Why:** Base size is the density dial for text: 13-14px reads dense and "pro tool", 16-17 comfortable and reading-friendly [DC-L02-08].
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
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L02-08; S-L02-001, S-L02-005, S-L02-006, S-L02-011, S-L02-014
- **Merges:** K7.2 (sizes)

### Q-type-15 · Should text sizes change with screen width? · Expert
- **Why:** Fixed sizes look consistent and app-like; fluid display type fills wide heroes smoothly [DC-L02-19].
- **Ask:** "Should text sizes change with screen width?"
- **Example:** Drag the preview width; watch the hero and a card heading.
- **Control:** single choice
- **Options:**
  - `fixed` Fixed everywhere; rely on the OS text-size setting (Carbon productive, Windows, iOS) [S-L02-011, S-L02-022, S-L02-001].
  - `stepped` Per-breakpoint steps (Carbon expressive at md, lg, xlg, max) [S-L02-011].
  - `fluid` Fluid display sizes with `clamp()` within the 2.5x zoom rule [S-L02-028; DC-L02-19].
- **Default:** fixed body and UI text; fluid or stepped only for display and headline styles on the web. *Source:* card heuristic [DC-L02-19].
- **Decides:** DC-L02-19
- **Changes:** DC-L03-17, DC-L07-28 · blocks: Foundations > Typography > Responsive type > Strategy
- **Preview:** a hero and a card heading as the preview width is dragged.
- **Use / avoid:** use fluid type for marketing heroes; avoid fluid styles inside cards, tables or forms [DC-L02-19; S-L02-011].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L02-19; S-L02-011, S-L02-022, S-L02-028

### Q-type-17 · How far must layouts support users' larger-text settings? · Standard
- **Why:** At the largest sizes hierarchy compresses (iOS AX5 Body 53pt vs Large Title 60pt) and layouts must restack [DC-L02-21; S-L02-001].
- **Ask:** "How far must layouts support users' larger-text settings?"
- **Example:** Show a list row at default, 200% and AX5.
- **Control:** single choice
- **Options:**
  - `full` Full scaling, no cap on body text: iOS AX1-AX5, Android nonlinear to 200%, web rem [S-L10-011, S-L10-071, S-L10-074].
  - `capped-chrome` Full for content, capped at about 1.5x for fixed chrome like tab labels [DC-L10-07].
  - `none` No scaling support: fails platform guidance (Apple asks for at least 200%) [S-L10-012].
- **Default:** capped-chrome, with every text token in scalable units and no fixed-height text containers. *Source:* platform convention and accessibility rule [DC-L10-07, DC-L02-21].
- **Decides:** DC-L02-21, DC-L10-07
- **Changes:** DC-L03-07, DC-L05-05, DC-L08-07 · blocks: Foundations > Typography > Scaling
- **Preview:** a list row and a tab bar at default, 200% and AX5, restacking live.
- **Use / avoid:** use containers that grow with text; avoid truncating at the largest sizes [DC-L02-21, DC-L10-07].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L02-21, DC-L10-07; S-L02-001, S-L10-011, S-L10-012, S-L10-071, S-L10-074
- **Merges:** P8, K4.4 (text scaling)

### Q-type-09 · Which ratio should generate the size scale? · Expert
- **Why:** The ratio sets how many usable steps exist and how strongly they differ [DC-L02-09].
- **Ask:** "Which ratio should generate the size scale?"
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
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L02-09; S-L02-006, S-L02-060, S-L09-213

### Q-type-10 · How many text styles, and how are they named? · Expert
- **Why:** Purpose-named roles make people pick by job and stop ad-hoc sizes; too many steps blur hierarchy [DC-L02-07, DC-L02-10].
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
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L02-07, DC-L02-10; S-L02-001, S-L02-005, S-L02-006, S-L02-015, S-L02-017

### Q-type-11 · How should line heights be set? · Expert
- **Why:** Tight leading makes headings solid; 1.4-1.6 makes paragraphs easy to track; Latin line heights clip Indic and Telugu marks [DC-L02-13, DC-L02-25].
- **Ask:** "How should line heights be set, including for other scripts?"
- **Example:** Show a paragraph in Latin and Devanagari with clipping flagged.
- **Control:** single choice + table of script categories
- **Options:**
  - `4pt` Fixed values snapped to 4pt (Material Body Large 16/24; Atlassian; Polaris) [S-L02-005, S-L02-015, S-L02-014].
  - `2pt` Fixed values on a 2pt grid (Fluent, Carbon) [S-L02-007, S-L02-011].
  - `ratios` Named unitless ratios (Primer tight 1.25 to loose 1.75) [DC-L02-13].
  - `script-heights` Plus language height categories: Medium about +7% (Arabic, Hindi, CJK, Thai), Large +30% (Telugu, Burmese), Extra large +100% (Nastaliq) (Material 3) [S-L02-006].
- **Default:** ratio-derived and rounded to 4px: about 1.5 for 12-16px, 1.4 for 18-24px, 1.25 for 28-40px, 1.1-1.15 for 48px+; Medium height for Indic and CJK, Large for Telugu and Burmese; no italics or all caps for non-Latin scripts. *Source:* card heuristics [DC-L02-13, DC-L02-25].
- **Decides:** DC-L02-13, DC-L02-25
- **Changes:** DC-L02-16, DC-L03-25, DC-L03-07 · blocks: Foundations > Typography > Metrics > Line height; Internationalization > Script metrics
- **Preview:** a paragraph and a two-line button label in Latin and each chosen script, with clipping flagged.
- **Use / avoid:** use smaller ratios as text gets larger; avoid fixed-height components that hold text [DC-L02-13, DC-L02-25].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L02-13, DC-L02-25; S-L02-005, S-L02-006, S-L02-007, S-L02-011, S-L02-015

### Q-type-12 · Which font weights, and how is emphasis shown? · Expert
- **Why:** Size-led hierarchy with regular headings looks elegant and editorial; weight-led hierarchy with bold headings looks sturdy and product-like [DC-L02-15].
- **Ask:** "Which font weights, and how is emphasis shown?"
- **Example:** Show headings and a selected chip in each weight set.
- **Control:** single choice (weights) + single choice (emphasis)
- **Options:**
  - `two` Two weights: Regular and Semibold (Windows 11) [S-L02-022].
  - `three` Three weights (Carbon 300/400/600; Material 400/500/700; Atlassian Regular/Medium/Bold) [S-L02-012, S-L02-005, S-L02-015].
  - `four` Four weights (Fluent 400-700; Primer 300-600) [S-L02-008, S-L02-017].
  - `emphasized-twin` One emphasized twin per style (Material Expressive 400 to 500, 500 to 700) [S-L02-005, S-L02-006].
  - `strong-stronger` Strong and Stronger variants (Fluent Body 1 400/600/700) [S-L02-007].
- **Default:** 3 weights (400 body, 500-600 labels, 600-700 headings) and one emphasized weight per style. *Source:* card heuristics [DC-L02-15, DC-L02-12]; BOARD L15 note (2 weights per view).
- **Decides:** DC-L02-15, DC-L02-12
- **Changes:** DC-L02-06 (files to load), DC-L08-14 · blocks: Foundations > Typography > Metrics > Weights; Type roles > Emphasis
- **Preview:** headings and a selected chip in each weight set.
- **Use / avoid:** use weight first, color second, italics only inside running text; avoid light (300) below 32px [DC-L02-12, DC-L02-15].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L02-15, DC-L02-12; S-L02-005, S-L02-007, S-L02-012, S-L02-022

### Q-type-13 · Should letter spacing change with size? · Expert
- **Why:** Negative tracking makes headlines confident; positive tracking helps small text and all-caps labels [DC-L02-14].
- **Ask:** "Should letter spacing tighten for big text and loosen for small text?"
- **Example:** Show a headline and an all-caps label with tracking on and off.
- **Control:** single choice
- **Options:**
  - `size-table` A size-specific table (SF Pro: +41/1000 em at 6pt, 0 at 12pt, -26/1000 em at 17pt), applied automatically by the OS [S-L02-001].
  - `per-style` Per-style tracking tokens (Material: Display Large -0.2sp, Body Large 0.5sp) [S-L02-005].
  - `zero` No tracking beyond the font's defaults [DC-L02-14].
- **Default:** 0 at body sizes, +0.02 to +0.05em at 11-12px and all caps, -0.01 to -0.02em from about 32px, in em units. *Source:* card heuristic [DC-L02-14].
- **Decides:** DC-L02-14
- **Changes:** DC-L07-12 · blocks: Foundations > Typography > Metrics > Letter spacing
- **Preview:** a headline and an all-caps label with tracking on and off.
- **Use / avoid:** use em-based tracking so it scales; let optical-size fonts do most of the work; avoid tracking non-Latin scripts [DC-L02-14, DC-L02-25].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L02-14; S-L02-001, S-L02-005, S-L02-009, S-L02-021

### Q-type-14 · How should running text be laid out: line length, alignment, truncation and paragraph spacing? · Expert
- **Why:** Lines that are too wide make readers lose their place; centered or justified text slows reading [DC-L02-17, DC-L02-18].
- **Ask:** "How wide can paragraphs get, and how should long text be cut off?"
- **Example:** Let them drag a width handle on an article.
- **Control:** number (max characters per line) + single choice (overflow) + number (paragraph spacing)
- **Options:**
  - `measure-45-75` 45-75 characters (Bringhurst) or 50-60 (Windows); WCAG 1.4.8 AAA caps at 80, 40 for CJK [S-L02-051, S-L02-022, S-L02-029].
  - `wrap-then-ellipsis` Wrap first, then ellipsis with access to the full text [DC-L02-18].
  - `para-1x` Paragraph spacing equal to the body size (Atlassian body 12px, body large 16px) [S-L02-015; DC-L02-16].
  - `text-box-trim` Trim half-leading so spacing measures from cap height (CSS `text-box: trim-both`) [DC-L02-16].
- **Default:** max prose width about 65-70ch (35-40 characters CJK), start-aligned, wrap then ellipsis, paragraph spacing 1x body size with twice as much space above a heading as below it. *Source:* card heuristics [DC-L02-17, DC-L02-18, DC-L02-16].
- **Decides:** DC-L02-17, DC-L02-18, DC-L02-16
- **Changes:** DC-L03-16, DC-L03-25 · blocks: Foundations > Typography > Layout of text
- **Preview:** an article at the chosen measure with a width handle to drag; lines over the limit highlight.
- **Use / avoid:** constrain the container before touching font size when lines exceed about 10-12 words; avoid full justification and centered paragraphs [DC-L02-17, DC-L02-18].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L02-17, DC-L02-18, DC-L02-16; S-L02-015, S-L02-022, S-L02-029, S-L02-051

### Q-type-16 · Should type sizes differ by platform or viewing distance? · Expert
- **Show if:** more than one platform or device class
- **Why:** Mobile type about 1.2x desktop compensates for touch and distance; TVs and cars need distance-scaled type [DC-L02-20, DC-L14-04].
- **Ask:** "Should sizes differ by platform or viewing distance?"
- **Example:** Show one screen at phone, desktop and TV.
- **Control:** single choice
- **Options:**
  - `platform-modes` One semantic scale with platform modes (Spectrum 2: 14px desktop, 17px mobile) [S-L02-021].
  - `per-platform` Per-platform ramps (Fluent: web Body 1 14/20, iOS 17/22, Android 16/24, macOS 13/16) [S-L02-007].
  - `native-units` One scale in native units (Material) [DC-L02-20].
  - `distance-modes` Distance modes seeded from native defaults (Apple watch 16, phone 17, Mac 13, TV 29 pt) [S-L14-012].
- **Default:** one semantic scale with platform modes, mobile about 1.15-1.2x desktop, plus distance modes for TV, car and spatial. *Source:* card heuristics [DC-L02-20, DC-L14-04].
- **Decides:** DC-L02-20, DC-L14-04
- **Changes:** DC-L14-13, DC-L07-15 · blocks: Foundations > Typography > Responsive type > Platform scales; Distance classes
- **Preview:** the same screen at phone, desktop and TV with type scaled to a similar visual angle.
- **Use / avoid:** keep roles and roughly the visual angle when moving to a farther device; avoid reusing desktop sizes on phones [DC-L14-04, DC-L02-20].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L02-20, DC-L14-04; S-L02-007, S-L02-021, S-L14-012, S-L14-026

---

## Stage 12 · Space, sizing and density
> Screen: the spacing scale, target sizes and control heights, shown on a live component sheet with spacing overlays (padding in one tint, gaps in another). Graph step 0-6. Pre-filled from Q-aud-01, Q-plat-03 and Q-dir-02.

### Q-space-01 · What should the base spacing unit be? · Standard
- **Why:** The base sets the smallest perceptible difference between spacings; 8 gives chunky, calm steps, 4 gives finer control [DC-L03-01].
- **Ask:** "What base unit should spacing use? 4 as the grid and 8 as the rhythm is common."
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
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L03-01; S-L03-002, S-L03-003, S-L03-010, S-L03-030, S-L03-044
- **Merges:** K7.3 (space)

### Q-space-02 · How should spacing steps grow? · Standard
- **Why:** Hybrid and geometric scales make levels of separation read instantly; linear scales with close steps get used inconsistently [DC-L03-02; S-L03-039].
- **Ask:** "How should spacing steps grow: fine then coarse, linear, or doubling?"
- **Example:** Show the scale as bars mapped to where each is used.
- **Control:** single choice + editable step list
- **Options:**
  - `hybrid` Fine at the bottom, coarse at the top: 0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80 (Atlassian's exact set; Carbon similar to 160) [S-L03-003, S-L03-001].
  - `linear` Linear 4px increments (Tailwind open-ended, Fluent to 56, Primer to 48) [S-L03-015, S-L03-010, S-L03-009].
  - `geometric` Doubling: 2, 4, 8, 16, 32, 64 (Curtis: linear offers "too many choices too close together") [S-L03-039].
- **Default:** hybrid, 12-15 steps. *Source:* card heuristic [DC-L03-02]; L09 shared default row 2 (0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96).
- **Decides:** DC-L03-02
- **Changes:** DC-L03-03, DC-L03-04, DC-L03-11, DC-L03-24 · blocks: Foundations > Space > Spacing scale
- **Preview:** the scale as bars; dragging a step shows where it is used on the component sheet.
- **Use / avoid:** keep adjacent steps at least about 25% apart above 8px so the difference is visible; avoid adding steps nobody can tell apart [DC-L03-02].
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L03-02; S-L03-001, S-L03-003, S-L03-009, S-L03-039

### Q-space-03 · How big must tap and click targets be? · Standard
- **Why:** Target size is an accessibility floor (WCAG 2.5.8) and sets how far apart controls sit; the visual may shrink with density, the hit area never does [DC-L03-12].
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
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L03-12, DC-L14-03, DC-L03-13; S-L03-029, S-L03-033, S-L03-035, S-L14-037

### Q-space-09 · Who controls density, and how is it stored? · Expert
- **Why:** User-selectable density can change layout, not just padding (Salesforce compact moves labels inline) [DC-L03-10; S-L03-070].
- **Ask:** "Who controls density, and how is it stored?"
- **Example:** Toggle a table between modes; targets stay fixed.
- **Control:** single choice (who) + single choice (storage)
- **Options:**
  - `fixed` Fixed density, no setting (most consumer and marketing systems) [DC-L03-10].
  - `size-props` Component size props chosen by designers (Carbon, Fluent, Primer) [S-L03-042, S-L03-046, S-L03-009].
  - `user-global` User-selectable global density (Salesforce comfy/cozy/compact, Gmail) [S-L03-070].
  - `semantic-mode` Stored as a semantic-layer mode, separate from breakpoints and color themes; primitives and target minimums untouched [DC-L03-11].
  - `per-device` Density follows viewing distance and input per device class ("a 65-inch TV is a far-away phone") [DC-L14-13; S-L14-026].
- **Default:** consumer: fixed comfortable; enterprise and data: size props plus a user compact mode that shrinks insets, stacks and row heights by one step (about 4px); stored as a semantic mode. *Source:* card heuristics [DC-L03-10, DC-L03-11, DC-L14-13].
- **Decides:** DC-L03-10, DC-L03-11, DC-L14-13
- **Changes:** DC-L07-15, DC-L07-17 · blocks: Foundations > Space > Density; Density > Modes; Density by context
- **Preview:** a data table toggled between modes; target outlines stay fixed while padding shrinks.
- **Use / avoid:** use a compact mode for tables, lists, menus and trees; avoid a type-only density mode that leaves oversized padding [DC-L03-11; S-L03-070].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L03-10, DC-L03-11, DC-L14-13; S-L03-042, S-L03-057, S-L03-070, S-L14-026
- **Merges:** K6.3 (density modes, mechanism)

### Q-space-04 · How tall should buttons and inputs be? · Standard
- **Why:** 32px defaults read as desktop productivity; 40-48px read as touch-friendly; 56dp+ read as expressive [DC-L03-07].
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
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L03-07, DC-L08-07; S-L03-042, S-L03-046, S-L08-061, S-L08-062, S-L08-102

### Q-space-05 · How much breathing room between groups versus inside them? · Standard
- **Why:** A high inner-to-outer ratio (8px inside, 32px between) reads clear and premium; a low ratio reads cramped and ambiguous [DC-L03-24].
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
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L03-24; S-L03-001, S-L03-028, S-L03-061

### Q-space-06 · How should spacing tokens be organized by purpose? · Expert
- **Why:** Semantic roles make the same inset appear in every card and the same stack between every field, which reads as rhythm [DC-L03-04; S-L03-028].
- **Ask:** "How should spacing tokens be organized by purpose?"
- **Example:** Show inset shapes on a card, button and input.
- **Control:** single choice + table (inset shapes)
- **Options:**
  - `curtis` Inset, squish inset, stretch inset, stack, inline, grid (EightShapes) [S-L03-039].
  - `material` Padding, gap, margin; "use padding and gaps before margins" (Material 3) [S-L03-030].
  - `layout-component` Separate component spacing from layout spacing (Carbon) [S-L03-001].
  - `insets` Inset shapes: square for cards and dialogs, squish (vertical about half of horizontal) for buttons and rows, stretch for inputs [S-L03-039, S-L03-046; DC-L03-05].
- **Default:** three families (inset, gap, layout); parents own spacing and children never set outer margins; squish for pill-like controls, stretch for inputs only. *Source:* card heuristics [DC-L03-04, DC-L03-05].
- **Decides:** DC-L03-04, DC-L03-05
- **Changes:** DC-L03-03, DC-L07-04 · blocks: Foundations > Space > Semantic spacing; Inset
- **Preview:** a card, button and input with each inset shape overlaid.
- **Use / avoid:** use padding and gap on parents; avoid margins on reusable components [DC-L03-04; S-L03-030].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L03-04, DC-L03-05; S-L03-001, S-L03-030, S-L03-039, S-L03-046

### Q-space-07 · Do you need tiny nudges and negative spacing? · Expert
- **Why:** Nudges fix optical misalignment (icons that look off-center); negatives create overlaps such as avatar stacks [DC-L03-06].
- **Ask:** "Do you need tiny nudges and negative spacing?"
- **Example:** Show an icon-label pair and an avatar stack.
- **Control:** multi-select
- **Options:**
  - `nudges` Nudge steps 2, 6, 10 (Fluent; Material nested units) [S-L03-010, S-L03-030].
  - `hairline` 1px step (Spectrum `spacing-25`, Polaris `space-025`) [S-L03-044, S-L03-005].
  - `negatives` Negative tokens -2 to -32 (Atlassian, Primer) [S-L03-003, S-L03-009].
- **Default:** 2, 4, 6 (10 only if the icon set needs it), negatives mirroring positives up to 32; 1px reserved for borders, not spacing. *Source:* card heuristic [DC-L03-06].
- **Decides:** DC-L03-06
- **Changes:** DC-L07-03 · blocks: Foundations > Space > Fine and negative
- **Preview:** an icon-label pair and an avatar stack with and without nudges.
- **Use / avoid:** use negatives for deliberate overlaps; avoid using nudges to patch layout bugs [DC-L03-06, inferred].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L03-06; S-L03-003, S-L03-005, S-L03-010, S-L03-030

### Q-space-08 · How should vertical rhythm be kept? · Expert
- **Why:** Stray line-height space makes padding look uneven (top bigger than bottom) [DC-L03-25; S-L03-039].
- **Ask:** "How should vertical rhythm be kept?"
- **Example:** Measure a button's top and bottom padding, trim on and off.
- **Control:** single choice
- **Options:**
  - `box-based` Measure spacing from the text box; spacers snap to the text box (Carbon) [S-L03-002].
  - `baseline` A baseline grid for multi-column content (Fluent) [S-L03-010].
  - `trim` Trim line-height with CSS `text-box` as progressive enhancement [S-L03-077, S-L03-039].
- **Default:** snap line heights and spacing to 4px, measure from the text box, `text-box` trim as enhancement; content must survive WCAG 1.4.12 text-spacing overrides. *Source:* card heuristic [DC-L03-25]; accessibility rule [DC-L02-22].
- **Decides:** DC-L03-25
- **Changes:** DC-L02-16 · blocks: Foundations > Space > Vertical rhythm
- **Preview:** a button and card with the top and bottom padding measured, trim on and off.
- **Use / avoid:** use a strict baseline grid only for multi-column editorial pages; avoid it for app UI on the web [DC-L03-25].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L03-25; S-L03-002, S-L03-010, S-L03-039, S-L03-077

### Q-space-10 · Which icon and avatar sizes should exist? · Expert
- **Why:** Icons sized to the text line height sit level with labels; oversized icons shift the personality toward friendly and consumer [DC-L03-08].
- **Ask:** "Which icon and avatar sizes should exist?"
- **Example:** Show icon-label pairs at each text size.
- **Control:** editable size lists
- **Options:**
  - `icons-16-32` Icons 16/20/24/32 (Carbon: 16 and 20 pair with 14 and 16px text) [S-L03-062].
  - `platform-scaled` Platform-scaled icon sizes (Spectrum desktop 14-26, mobile 16-30) [S-L03-044].
  - `button-sized` Icon sized to the button size (Material Expressive 20-40dp for XS-XL) [S-L03-059].
  - `avatars` Avatars 16/20/24/32/40/48/64 (Primer) [S-L03-063].
- **Default:** icons 16/20/24/32, avatars 16-64 as Primer; icon size = body line height minus 0-4px. *Source:* card heuristic [DC-L03-08].
- **Decides:** DC-L03-08
- **Changes:** DC-L05-05, DC-L05-18 · blocks: Foundations > Sizing > Media sizes
- **Preview:** icon-label pairs at each text size, and an avatar row.
- **Use / avoid:** keep the icon-to-text ratio fixed ("Don't alter the icon-text size ratio", Carbon) [S-L03-062]; avoid in-between icon sizes that blur the pixel grid [inferred].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L03-08; S-L03-044, S-L03-059, S-L03-062, S-L03-063

---

## Stage 13 · Layout, navigation and app shell
> Screen: how pages reorganize across widths, shown on a resizable frame the person can drag from phone to wide desktop. Graph step 0-4. Safe areas and edge insets (DC-L03-20, DC-L14-10) are not asked; they are platform rules applied by construction (see "Auto-applied rules").

### Q-layout-01 · At which widths should layouts reorganize? · Standard
- **Why:** Each breakpoint is a moment where panes appear, navigation swaps and columns double [DC-L03-14].
- **Ask:** "Which breakpoint set should layouts use? Material's five work across web and Android."
- **Example:** Drag the frame across 600, 840 and 1200; show navigation swapping from bar to rail.
- **Control:** single choice + editable values
- **Options:**
  - `material` Material width breakpoints 600 / 840 / 1200 / 1600dp plus height classes 480 / 900 (Android and web) [S-L03-025, S-L03-021].
  - `tailwind` Tailwind 640 / 768 / 1024 / 1280 / 1536 (web-only products) [S-L03-016].
  - `bootstrap` Bootstrap 576 / 768 / 992 / 1200 / 1400 [S-L03-018].
  - `apple-size-classes` Apple size classes, compact or regular per axis, set by the system [S-L03-032].
- **Default:** material for cross-platform products, tailwind for web-only; web values in rem; design compact first. *Source:* card heuristic [DC-L03-14]; BOARD L03 note (Material renamed window size classes to breakpoints, May 2026).
- **Decides:** DC-L03-14
- **Changes:** DC-L03-15, DC-L03-16, DC-L03-17, DC-L03-18, DC-L03-19, DC-L07-28 · blocks: Foundations > Layout > Breakpoints
- **Preview:** the resizable frame with breakpoint ticks; the layout snaps at each one.
- **Use / avoid:** decide layout by window size, never by device type or orientation [DC-L10-10; S-L10-013]; avoid breakpoints that only nudge padding.
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L03-14; S-L03-016, S-L03-018, S-L03-021, S-L03-025, S-L03-032

### Q-layout-02 · Should layouts stretch fluidly, switch between fixed designs, or both? · Expert
- **Why:** Responsive layouts feel continuous; adaptive layouts feel native per device (different navigation, pane counts) [DC-L03-22, DC-L10-10].
- **Ask:** "Stretch within a layout, switch layouts at breakpoints, or both?"
- **Example:** Show a list-detail screen stretching, then becoming two panes at 840dp.
- **Control:** single choice
- **Options:**
  - `responsive` Responsive: one fluid layout (Fluent, Material definitions) [S-L03-010, S-L03-071].
  - `adaptive` Adaptive: distinct layouts per size (show-and-hide, levitate, reflow) [S-L03-071].
  - `both` Responsive inside panes, adaptive between breakpoints; window size classes on Apple, Material breakpoints elsewhere [DC-L03-22, DC-L10-10].
- **Default:** both, with a list-detail template that becomes two panes at expanded. *Source:* card heuristics [DC-L03-22, DC-L10-10].
- **Decides:** DC-L03-22, DC-L10-10
- **Changes:** DC-L10-09, DC-L03-18, DC-L03-21 · blocks: Foundations > Layout > Adaptation strategy
- **Preview:** the resizable frame; pane boundaries highlight when they change.
- **Use / avoid:** use adaptive changes for pane count and navigation; avoid device-type checks that break in split view and resizable windows [S-L10-013].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L03-22, DC-L10-10; S-L03-010, S-L03-071, S-L10-013, S-L10-022, S-L10-025
- **Merges:** P11

### Q-layout-04 · How should top-level navigation work at each size? · Standard
- **Why:** The navigation container is the most recognizable part of the app's silhouette: tab bar, rail, sidebar or menu bar [DC-L14-05, DC-L08-19].
- **Ask:** "How many top-level destinations, and should navigation be a bottom bar, rail, sidebar or top bar?"
- **Example:** Ask for the list of main sections; show them as a bottom bar on phone, rail on tablet, sidebar on desktop.
- **Control:** number (destinations) + single choice (pattern)
- **Options:**
  - `adaptive-bar-rail-sidebar` Bottom bar on phones (3-5), rail from 600dp, sidebar on desktop (Material; iOS floating tab bar; iPad sidebar-adaptable) [S-L08-083, S-L10-014, S-L10-025].
  - `sidebar` Sidebar at every size above compact, with groups for 7+ destinations (Carbon UI shell, Primer NavList, shadcn Sidebar) [S-L08-009, S-L08-012].
  - `top-nav` Top navigation (marketing sites) [DC-L08-19].
  - `hidden` Hidden in a hamburger or drawer: looks clean, hides scope [DC-L13-02].
- **Default:** adaptive-bar-rail-sidebar; primary navigation visible whenever width allows; at most two disclosure levels; no seven-item cap. *Source:* card heuristics [DC-L08-19, DC-L13-02, DC-L10-09]; L13 E2 (Miller's 7 does not limit menus).
- **Decides:** DC-L08-19, DC-L13-02, DC-L10-09, DC-L14-05, DC-L03-19
- **Changes:** DC-L10-11, DC-L03-20 · blocks: Patterns > Navigation; Patterns > Layout > App shell
- **Preview:** the person's own destination names in each container across the frame widths.
- **Use / avoid:** keep destinations identical across devices and swap only the container; avoid hiding primary navigation on wide layouts [DC-L14-05; S-L13-097].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L08-19, DC-L13-02, DC-L10-09, DC-L14-05, DC-L03-19; S-L08-083, S-L10-014, S-L13-048, S-L13-063, S-L03-025
- **Merges:** P10, K8.3 (navigation part)

### Q-layout-03 · Are your pages mostly for reading, working, or data? · Standard
- **Why:** The page type decides container width and pane templates: reading pages feel like documents, working pages like tools, data pages use every pixel [DC-L03-16, DC-L03-18].
- **Ask:** "Are most pages for reading, for working in, or for scanning data?"
- **Example:** Show a centered article, a sidebar app page and a full-width dashboard.
- **Control:** multi-select (page types) + single choice (default pane template)
- **Options:**
  - `reading` Reading: centered, max about 1280px, text measure 40-80 characters (Primer full pages 1280; Carbon editorial model) [S-L03-008, S-L03-074].
  - `working` Working: left navigation plus left-aligned content with a max width [DC-L03-16].
  - `data` Data: fluid, full width (Carbon high-density model) [S-L03-074].
  - `feed` / `list-detail` / `supporting-pane` Material canonical layouts; never more than three panes [S-L03-027, S-L03-026].
- **Default:** working + list-detail; one pane below 840dp, two from 840dp, three only at 1600dp+. *Source:* card heuristics [DC-L03-16, DC-L03-18].
- **Decides:** DC-L03-16, DC-L03-18
- **Changes:** DC-L02-17, DC-L03-15 · blocks: Foundations > Layout > Containers; Patterns > Layout > Canonical layouts
- **Preview:** the three page types in the resizable frame.
- **Use / avoid:** use fluid width for tables and dashboards; avoid full-width paragraphs [DC-L03-16, DC-L02-17].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L03-16, DC-L03-18; S-L03-008, S-L03-025, S-L03-026, S-L03-027, S-L03-074

### Q-layout-05 · Which column grid and composition style? · Expert
- **Why:** 16 columns allow asymmetric, editorial layouts; 12 give symmetric splits; bento layouts feel curated with a clear hero [DC-L03-15, DC-L15-07].
- **Ask:** "Which grid, and should marketing sections use a column, modular or bento composition?"
- **Example:** Show a feature section as columns and as a bento grid.
- **Control:** single choice (grid) + single choice (composition)
- **Options:**
  - `4-8-12` 4 / 8 / 12 columns (compact / medium / expanded), gutter 16-24, margin 16 then 24 (Material) [S-L03-026].
  - `2x-grid` 4 / 8 / 16 columns, 32px gutter with wide/narrow/condensed modes (Carbon) [S-L03-002, S-L03-054].
  - `12-always` 12 columns everywhere, 1.5rem gutters (Bootstrap) [S-L03-066].
  - `bento` Hierarchical or bento composition for marketing; free composition only for expressive pages [DC-L15-07].
- **Default:** 4 / 8 / 12 columns; column grid for app surfaces, hierarchical or bento for marketing feature sections; only layout spacing (margins, pane gaps) changes with breakpoint. *Source:* card heuristics [DC-L03-15, DC-L15-07, DC-L03-17].
- **Decides:** DC-L03-15, DC-L15-07, DC-L03-17
- **Changes:** DC-L07-28 · blocks: Foundations > Layout > Grid; Composition model; Space > Responsive spacing
- **Preview:** grid overlay toggle on the frame.
- **Use / avoid:** make every grid break nameable ("this hero breaks the grid to signal X"); avoid changing component spacing by breakpoint [DC-L15-07, DC-L03-17].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L03-15, DC-L15-07, DC-L03-17; S-L03-002, S-L03-026, S-L03-054, S-L15-062

### Q-layout-06 · Should components respond to their container or to the window? · Expert
- **Show if:** Q-plat-01 includes web
- **Why:** Container-aware components look right in any slot, such as a sidebar card vs a main-column card [DC-L03-21].
- **Ask:** "Should components adapt to the space they sit in (container queries) or to the window width?"
- **Example:** Show the same card in a sidebar and in the main column.
- **Control:** single choice
- **Options:**
  - `viewport` Viewport media queries keyed to the breakpoints [S-L03-016].
  - `container` Container queries (Baseline since 2025-08-14; Tailwind v4 ships 13 container sizes) [S-L03-056, S-L03-016].
- **Default:** page layout by viewport, components by container queries once multi-pane layouts exist. *Source:* card heuristic [DC-L03-21].
- **Decides:** DC-L03-21
- **Changes:** DC-L10-18 · blocks: Foundations > Layout > Responsive mechanism
- **Preview:** the card dragged between slots.
- **Use / avoid:** use container queries for reusable components; avoid viewport queries inside components placed in panes [DC-L03-21].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L03-21; S-L03-016, S-L03-055, S-L03-056

---

## Stage 14 · Shape
> Screen: corner radius, on a live component sheet (button, input, card, dialog, menu, avatar, image). Graph step 1-5. The signature-shape question comes first because brand shape language drives the roundness dial (graph-overrides.json edge DC-L06-09 to DC-L04-02). Nested radii follow the concentric rule automatically (DC-L04-05, see "Auto-applied rules").

### Q-shape-05 · Should a signature shape from your brand appear in the UI? · Expert
- **Why:** Curves read friendlier; sharp angles raise threat perception; a shape that breaks the pattern draws attention [DC-L06-09; S-L06-073].
- **Ask:** "Is there a shape in your logo or brand we should echo in the UI?"
- **Example:** Show Slack's speech-bubble lozenge used as a graphic element.
- **Control:** single choice (+ upload of the logo for curvature)
- **Options:**
  - `logo-derived` Logo-derived shapes as graphic elements and icon basis (Slack, Dropbox) [S-L06-030, S-L06-024].
  - `softened` Brand geometry softened for UI (Atlassian) [S-L06-088].
  - `curved` Curved, soft UI (Airbnb 2025) [S-L06-062].
  - `variety` Mixed shapes for tension, shape morph (M3 Expressive, 35 shapes) [S-L06-009].
  - `rectilinear` Strict rectilinear (IBM) [S-L06-003].
- **Default:** one radius family derived from the logo's curvature; shape variety only in hero moments. *Source:* card heuristic [DC-L06-09].
- **Decides:** DC-L06-09
- **Changes:** DC-L06-13, DC-L06-11 · blocks: Foundations > Shape > Brand shape language
- **Preview:** the logo curvature overlaid on the button radius.
- **Use / avoid:** use shape variety only in hero moments; avoid shrinking essential actions into small shapes ("smaller shapes can result in essential actions looking less important") [S-L06-009].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L06-09; S-L06-003, S-L06-009, S-L06-030, S-L06-073, S-L06-088


### Q-shape-01 · How soft should corners feel? · Quick
- **Why:** Corner radius tops L09's (inferred) ranking of visual differences between systems (divergence 1), and every 2025-2026 revision got rounder [DC-L09-01; L09 A2].
- **Ask:** "How soft should corners feel: square, slightly rounded, rounded, or pill?"
- **Example:** Show a button, input, card and dialog at 0, 6, 12px and pill side by side.
- **Control:** single choice + radius factor slider (0, 0.75, 1, 1.5, full)
- **Options:**
  - `square` 0-2px: official, engineered (GOV.UK, Carbon v11 buttons) [DC-L09-01, DC-L04-02].
  - `subtle` 4-6px: businesslike (Fluent 4, Primer and Atlassian 6) [S-L04-007, S-L04-024, S-L04-016].
  - `soft` 8-12px: friendly, modern (Polaris, Paste, Blade, Mantine v9 8px; Airbnb 12px) [DC-L09-01].
  - `pill` Pill: consumer, playful, touch-first (Material 3, Spectrum 2, SLDS Cosmos; iOS 26 capsule controls) [DC-L09-01; S-L04-038].
  - `rule-based` Size-dependent (Spectrum 6-10 by size) or concentric with the container (Apple) [DC-L09-01; S-L04-035].
- **Default:** 6px controls, 8-12px containers. *Source:* L09 shared default row 7 (16 of 23 control defaults at 4-8px, median 6) [L09 A1; DC-L09-01]; a radius factor slider as Radix offers [S-L09-559].
- **Decides:** DC-L09-01, DC-L04-02
- **Changes:** DC-L04-01, DC-L04-03, DC-L04-04, DC-L04-06, DC-L04-19, DC-L04-09, DC-L05-18 · blocks: Foundations > Shape > Radius scale and default; Shape personality
- **Preview:** the component sheet morphing as the slider moves; the focus ring follows the radius.
- **Use / avoid:** use sharp corners when density and precision are brand values (data, developer tools) and pill when the brand is consumer and touch-first; avoid pill on dense, short controls, which need taller heights [DC-L04-02, DC-L09-01].
- **Skip:** yes, 6px.
- **Time weight:** high (fan-out 4)
- **Evidence:** DC-L09-01, DC-L04-02; S-L09-101, S-L09-559, S-L04-005, S-L04-029, S-L04-038
- **Merges:** K7.4 (shape)

### Q-shape-02 · Which radius steps should exist? · Expert
- **Why:** A short scale gives a tighter, more uniform look; a long scale lets large surfaces curve more [DC-L04-01].
- **Ask:** "Which radius steps should the scale have?"
- **Example:** Show the steps with a component named under each one.
- **Control:** editable step list
- **Options:**
  - `minimal` 3-4 steps + full (Primer 3/6/12/full) [S-L04-024].
  - `medium` 6-8 steps + full (Atlassian 2-16/full; Carbon v12 0/2/4/8/16/24/max) [S-L04-016, S-L04-030].
  - `large` 9-11 steps + full (Material 0-48; Fluent 0-40) [S-L04-003, S-L04-006].
  - `derived` No scale; radii derived from the container through concentricity (Apple) [S-L04-035].
- **Default:** 0, 2, 4, 8, 12, 16, 24, full. *Source:* card heuristic [DC-L04-01]; L09 preset 0, 2, 4, 6, 8, 12, 16, 24, full [L09 A1 row 7].
- **Decides:** DC-L04-01
- **Changes:** DC-L04-03, DC-L04-05, DC-L04-09, DC-L15-10 · blocks: Foundations > Shape > Corner radius scale
- **Preview:** each step with the components that use it; unused steps are flagged for deletion.
- **Use / avoid:** grow radius with component size; delete any step you cannot name a component for [DC-L04-01].
- **Skip:** yes.
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L04-01; S-L04-003, S-L04-016, S-L04-024, S-L04-030

### Q-shape-03 · Which components get which radius? · Expert
- **Why:** Scaling radius with element size keeps curvature proportional; reserving full circles for people makes circles carry meaning [DC-L04-03].
- **Ask:** "Should radius step up with component size, and should full circles be reserved for avatars?"
- **Example:** Show Atlassian's mapping: badge 2, tag 4, button 6, card 8, modal 12, avatar full.
- **Control:** mapping table
- **Options:**
  - `atlassian-roles` Role by component family: xsmall 2 badges, small 4 tags, medium 6 buttons and inputs, large 8 cards, xlarge 12 modals, full for avatars [S-L04-016, S-L04-018].
  - `fluent-roles` None for nav and tab bars, small 2px for badges, medium, large, circular for people (Fluent 2) [S-L04-007].
  - `four-roles` Four roles: detail 2-4, control 4-8 or full, container 8-12, overlay 12-16+, person full [DC-L04-03].
- **Default:** four-roles; the radius steps up one level each time the element's height roughly doubles. *Source:* card heuristic [DC-L04-03].
- **Decides:** DC-L04-03
- **Changes:** DC-L04-05, DC-L07-04 · blocks: Foundations > Shape > Radius roles
- **Preview:** the component sheet with each component's role labeled.
- **Use / avoid:** use full radius for people and pills; avoid giving small badges and large dialogs the same radius [DC-L04-03].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L04-03; S-L04-007, S-L04-016, S-L04-018, S-L04-035

### Q-shape-04 · Circular corners, or Apple-style continuous corners? · Expert
- **Why:** Continuous curves blend into edges and read softer and more "Apple" at the same nominal radius [DC-L04-04].
- **Ask:** "Keep standard circular corners, or use continuous (squircle) corners where supported?"
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
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-04; S-L04-036, S-L04-054, S-L04-055

---

## Stage 15 · Depth, borders and materials
> Screen: how surfaces separate and float, on a live stack (page, card, menu, dialog, sheet over a photo) in light and dark. Graph step 0-4. Cycle kept together: DC-L10-11 + DC-L10-12 (edge-to-edge content under the system bars decides the bar material, and the material decides how bars treat content beneath them). Layer order (z-index) and opaque fallbacks for translucency are applied by construction (see "Auto-applied rules").

### Q-depth-01 · How should surfaces separate from each other? · Quick
- **Why:** The depth model is second on L09's (inferred) ranking of visual differences (divergence 2): shadows feel tactile, tonal feels calm, borders feel technical, glass feels premium [DC-L09-02].
- **Ask:** "How should cards and panels separate from the page: shadows, color steps, lines, or translucent material?"
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
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L09-02, DC-L04-10, DC-L08-15; S-L09-104, S-L09-559, S-L04-008, S-L04-017, S-L04-058

### Q-depth-02 · How many elevation levels, and how do they look in dark mode? · Expert
- **Why:** More levels allow fine hierarchy but muddy it; most products visibly use three: resting, raised, overlay [DC-L04-11].
- **Ask:** "How many elevation levels do you need? Four named levels is typical."
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
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L04-11, DC-L04-13; S-L04-003, S-L04-017, S-L04-018, S-L04-022

### Q-depth-03 · What should shadows look like? · Expert
- **Show if:** Q-depth-01 is shadow or ring-shadow
- **Why:** Single hard shadows look dated; layered soft shadows look realistic; tinted shadows avoid a "dirty grey" on colored surfaces [DC-L04-12].
- **Ask:** "Soft layered shadows, a key-plus-ambient pair, or tucked-under shadows?"
- **Example:** Show a menu with each recipe over a white and a tinted background.
- **Control:** single choice + alpha slider
- **Options:**
  - `key-ambient` Key plus ambient, 2 layers (Fluent) [S-L04-008].
  - `multi-layer` Multi-layer realistic (Primer floating.medium, 5 layers) [S-L04-024].
  - `negative-spread` Tucked under with negative spread (Polaris `0 8px 16px -4px`) [S-L04-022].
  - `tinted` Neutral-tinted shadow color instead of black (Polaris rgba(26,26,26), Atlassian #1E1F21) [S-L04-022, S-L04-018].
- **Default:** 2 layers (1px contact shadow plus a soft blur scaled to elevation), neutral-tinted, alpha 8-24% in light mode; in dark mode double the alpha and add a 1px light edge ring on overlays. *Source:* card heuristic [DC-L04-12].
- **Decides:** DC-L04-12
- **Changes:** DC-L07-13 · blocks: Foundations > Elevation > Shadow recipe
- **Preview:** shadows on the live stack with the alpha slider.
- **Use / avoid:** use one light source for every shadow; avoid single hard shadows [DC-L04-12; L15 P62].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-12; S-L04-008, S-L04-018, S-L04-022, S-L04-024

### Q-depth-04 · Should any surfaces be translucent (glass, blur)? · Standard
- **Why:** Translucency reads premium and OS-native in 2025-26 and keeps context visible, at the cost of lower, variable contrast [DC-L04-15, DC-L10-12].
- **Ask:** "Should navigation or overlays be translucent glass, or stay solid?"
- **Example:** Show a toolbar over a photo: solid, regular glass, and clear glass with the 35% dimming layer.
- **Control:** single choice + per-platform chrome table
- **Options:**
  - `none` Opaque surfaces: most legible and cheapest [DC-L04-15].
  - `control-layer` Glass on navigation and controls only, never on content (Apple Liquid Glass: regular for text-heavy parts, clear over media with a 35% dim) [S-L04-032, S-L10-008].
  - `transient` Translucent menus and flyouts only; Mica for the window base (Fluent Acrylic) [S-L04-011, S-L04-012].
  - `decorative` Decorative glassmorphism on cards: flagged for legibility (NN/g) [DC-L04-15].
- **Default:** platform material for native chrome (glass on Apple, Mica on Windows, tonal surfaces on Android); opaque on web with optional blur plus an opaque fallback; content edge-to-edge under the bars with inset-aware components. *Source:* platform convention [DC-L10-12, DC-L10-11, DC-L04-15].
- **Decides:** DC-L04-15, DC-L10-12, DC-L10-11
- **Changes:** DC-L04-16, DC-L10-16, DC-L05-16 · blocks: Foundations > Materials > Translucency; Depth > Materials (platform); Layout > Safe areas and insets
- **Preview:** the toolbar and a sheet over a busy photo with live contrast readouts; the opaque fallback shown beside it.
- **Use / avoid:** use glass on the functional layer (bars, controls, sheets) only; avoid glass on reading surfaces and any translucent token without an opaque twin [S-L10-008; DC-L04-16].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L04-15, DC-L10-12, DC-L10-11; S-L04-011, S-L04-032, S-L10-008, S-L10-023, S-L10-075
- **Merges:** P12, P13

### Q-depth-05 · How thick are borders, and when do dividers appear? · Expert
- **Why:** 1px borders read light and precise; 2px read bolder and more accessible; more lines read more "spreadsheet" [DC-L04-07, DC-L04-08].
- **Ask:** "Which border widths, and should lists be separated by lines, space or surface shifts?"
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
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L04-07, DC-L03-09, DC-L04-08; S-L03-009, S-L04-006, S-L04-017, S-L04-024

### Q-depth-06 · How dark should modal backdrops be, and how strong are state overlays? · Expert
- **Why:** Darker scrims focus attention hard; lighter scrims keep context for non-blocking sheets [DC-L04-18]. Overlay strengths set hover, press and disabled looks for every color [DC-L04-17].
- **Ask:** "How dark should the backdrop behind dialogs be, and should we use Material's standard state-overlay strengths?"
- **Example:** Show a dialog over the page at 30%, 45% and 60% scrim.
- **Control:** slider (scrim) + number set (overlays)
- **Options:**
  - `scrim-fluent` Black 40% light / 50% dark (Fluent) [S-L04-071].
  - `scrim-atlassian` Blue-black about 46% light / 60% dark (Atlassian `color.blanket`) [S-L04-070].
  - `overlays-material` State overlays hover 0.08, focus 0.10, pressed 0.10, dragged 0.16, disabled 0.38 (Material 3) [S-L04-003].
  - `overlays-atlassian` Stronger overlays in dark mode (Atlassian hovered 16%/pressed 32% light, 20%/36% dark) [S-L04-070].
- **Default:** scrim 40-50% near-black in light, 50-60% in dark, tinted toward the neutral hue; Material overlay numbers, raised in dark mode. *Source:* card heuristics [DC-L04-18, DC-L04-17].
- **Decides:** DC-L04-18, DC-L04-17
- **Changes:** DC-L08-20, DC-L08-09 · blocks: Foundations > Opacity > Scrims; State layers
- **Preview:** a dialog and a bottom sheet over the page with the slider live.
- **Use / avoid:** use lighter scrims for non-blocking sheets; avoid scrims so light that the dialog's modality is unclear [DC-L04-18].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-18, DC-L04-17; S-L04-003, S-L04-069, S-L04-070, S-L04-071

---

## Stage 16 · Motion, haptics and sound
> Screen: motion feel on live interactions the person can trigger (open a menu, navigate, toggle, dismiss a sheet), with a reduced-motion toggle. Graph step 0-6.

### Q-motion-01 · Should motion feel quick and invisible, or physical and playful? · Quick
- **Why:** Motion is L09 divergence 7: short beziers feel efficient, springs with bounce feel alive, no motion feels static but calm [DC-L09-06].
- **Ask:** "Should motion be quick and invisible, calm with a few expressive moments, or physical and bouncy?"
- **Example:** Open the same menu and page transition with each setting.
- **Control:** single choice + bounce slider (Expert)
- **Options:**
  - `none` Minimal motion (GOV.UK) [DC-L09-06].
  - `productive` Productive beziers: fast, competent, no bounce (Carbon productive `cubic-bezier(0.2, 0, 0.38, 0.9)`) [S-L06-002].
  - `two-mode` Productive for most interactions, expressive for 1-3 hero moments per flow (Carbon expressive; Material standard vs expressive schemes) [S-L04-075, DC-L04-19].
  - `springs` Springs throughout: alive, physical, interruptible (Material spring tokens, Apple duration + bounce, Airbnb) [DC-L09-06; S-L10-024].
- **Default:** two-mode: 7 durations 50-500ms, ease-out to enter, ease-in to exit, springs only for spatial moves in the expressive mode, bounce at or below 0.2. *Source:* L09 shared default row 5 (all 16 systems with motion tokens stay in 100-300ms) and card heuristics [DC-L09-06, DC-L04-19]; capped at productive when Q-aud-02 is high-trust.
- **Decides:** DC-L09-06, DC-L04-19, DC-L06-10
- **Changes:** DC-L04-20, DC-L04-21, DC-L04-22, DC-L04-23, DC-L10-14 · blocks: Foundations > Motion; Motion personality
- **Preview:** the live interactions replay on every change, with a slow-motion button.
- **Use / avoid:** use expressive motion for page transitions, the primary action and alerts; avoid bounce on everyday controls and in high-trust products [DC-L06-10, DC-L04-19].
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L09-06, DC-L04-19, DC-L06-10; S-L09-105, S-L06-002, S-L04-075, S-L10-024
- **Merges:** K7.4 (motion personality)

### Q-motion-04 · How should springs be defined and exported? · Expert
- **Show if:** Q-motion-01 is two-mode or springs
- **Why:** Springs keep velocity when interrupted and settle naturally; DTCG has no spring type, so the storage format matters [DC-L04-22; BOARD L04/L07 note].
- **Ask:** "Store springs as damping and stiffness, with Apple and CSS versions derived?"
- **Example:** Show one spring as (dampingRatio 0.8, stiffness) and as Apple (duration, bounce) and a CSS `linear()` curve.
- **Control:** single choice
- **Options:**
  - `durations-only` Duration + easing only (Carbon, Fluent, Polaris, Primer) [S-L04-014, S-L04-006].
  - `spatial-effects` Springs split into spatial (may overshoot) and effects (critically damped, for color and opacity) (Material fast/default/slow) [S-L04-060, S-L10-024].
  - `apple-bounce` Duration + bounce 0 / 0.15 / 0.3 (Apple) [DC-L09-06].
- **Default:** (dampingRatio, stiffness) plus derived (duration, bounce) for Apple and pre-sampled `linear()` for CSS; critically damped springs for effects. *Source:* card heuristic [DC-L04-22].
- **Decides:** DC-L04-22
- **Changes:** DC-L07-14, DC-L04-28, DC-L04-06 · blocks: Foundations > Motion > Physics
- **Preview:** a switch and a sheet driven by the spring, dragged and released mid-flight.
- **Use / avoid:** use springs for spatial moves; avoid overshoot on color and opacity [DC-L04-22; S-L10-024].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L04-22; S-L04-060, S-L04-064, S-L10-024, S-L09-105

### Q-motion-02 · Which durations should exist, and should exits be faster? · Expert
- **Why:** Past about 500ms UI starts to feel slow; fast, interruptible exits respect the user's time [DC-L04-20, DC-L04-24].
- **Ask:** "Keep the standard duration ladder, with exits shorter than entrances?"
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
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L04-20, DC-L04-24; S-L04-003, S-L04-018, S-L04-024, S-L04-033

### Q-motion-03 · Which easing curves? · Expert
- **Why:** Strong decelerate curves make entrances feel fast and "arriving"; role-based sets are easiest to apply consistently [DC-L04-21].
- **Ask:** "Use role-based curves: standard, enter, exit, linear?"
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
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L04-21; S-L04-003, S-L04-006, S-L04-013, S-L04-014, S-L04-018

### Q-motion-05 · Should shapes morph or use an expressive shape library? · Expert
- **Show if:** Q-shape-01 is pill or Q-motion-01 is springs
- **Why:** Pills read tappable and friendly; expressive shapes (cookies, bursts, clovers) add playfulness, best kept to avatars and hero moments [DC-L04-06].
- **Ask:** "Keep a simple full-round token, or add expressive shapes and morphing for a few signature moments?"
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
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-06; S-L04-005, S-L04-016, S-L04-031

### Q-motion-06 · Which named transitions and stagger should the system ship? · Expert
- **Why:** Consistent transitions make navigation legible (you can feel whether you went deeper or sideways) [DC-L04-23].
- **Ask:** "Ship the four standard transitions: fade, fade-through, shared axis, container transform?"
- **Example:** Show a list item expanding into a detail page (container transform) and tabs switching (fade through).
- **Control:** multi-select + number (stagger)
- **Options:**
  - `fade` Fade for in-screen enter and exit (dialogs, menus) [DC-L04-23].
  - `fade-through` Fade through for unrelated destinations such as tabs [DC-L04-23].
  - `shared-axis` Shared axis x, y or z for spatial relationships (onboarding x, stepper y, parent-child z) [DC-L04-23].
  - `container-transform` Container transform for element-to-page transitions [DC-L04-23].
  - `stagger` A stagger token of 20-50ms, total at most 500ms [DC-L04-23].
- **Default:** all four plus stagger. *Source:* card heuristic, Material's four patterns [DC-L04-23].
- **Decides:** DC-L04-23
- **Changes:** DC-L07-14 · blocks: Patterns > Motion > Transitions and choreography
- **Preview:** each transition playable on the preview.
- **Use / avoid:** use OS-owned navigation transitions on native platforms; avoid custom page transitions that fight the back gesture [DC-L10-14].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-23; S-L04-009, S-L04-014, S-L04-018, S-L04-033

### Q-motion-07 · What happens when users ask for reduced motion, and how much motion does each device allow? · Standard
- **Why:** A good reduced mode still feels polished (crossfades) rather than broken (jumps); motion budgets shrink as attention narrows (none in cars) [DC-L04-25, DC-L14-08].
- **Ask:** "When someone turns on reduced motion, should movement become gentle fades or stop entirely?"
- **Example:** Toggle reduced motion on the preview; a sliding panel becomes a crossfade.
- **Control:** single choice + per-device table
- **Options:**
  - `replace` Replace spatial motion with opacity and color changes (MDN; WCAG's motion definition excludes color, blur and opacity) [S-L04-067, S-L04-049].
  - `remove` Remove all non-essential motion (WCAG 2.3.3 AAA, technique C39) [DC-L04-25].
  - `per-device` Per device: system transitions plus brand micro-motion on phone and desktop; subtle focus scale on TV; minimal on watch; none in cars; slow and grounded in headsets [DC-L14-08; S-L14-032].
- **Default:** replace, built as a token mode; 2.3.3 treated as a requirement although it is AAA; per-device budgets applied. *Source:* accessibility rule and card heuristics [DC-L04-25, DC-L14-08].
- **Decides:** DC-L04-25, DC-L14-08
- **Changes:** DC-L07-15, DC-L07-14 · blocks: Foundations > Motion > Accessibility; Motion > Device policy
- **Preview:** the reduced-motion toggle on every live interaction.
- **Use / avoid:** keep feedback (color, opacity) and remove travel (translate, scale, parallax); avoid removing feedback entirely [DC-L04-25].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-25, DC-L14-08; S-L04-049, S-L04-067, S-L04-075, S-L14-032
- **Merges:** B15 (reduced motion)

### Q-motion-08 · Do you have UI sounds or a sonic logo? · Standard
- **Why:** Sound is a block the builder cannot compose well; it adds confirmation but annoys in shared spaces [DC-L04-27; BRIEF requirement 2].
- **Ask:** "Do you have UI sounds or a sonic logo you want in the product? Most web and productivity apps stay silent."
- **Example:** Play one confirmation sound and show the mute option beside it.
- **Control:** single choice + file upload
- **Options:**
  - `silent` Silent by default (most web systems; tvOS plays no alert sounds) [S-L04-074].
  - `rare-events` Sounds for rare, meaningful events, always behind mute and silent mode [S-L04-074].
  - `sound-forward` Sound-forward (games, spatial computing) [DC-L04-27].
- **Default:** silent on web and productivity apps. *Source:* card heuristic [DC-L04-27].
- **Decides:** DC-L04-27
- **Changes:** DC-L04-26 · blocks: Foundations > Sound > UI sounds
- **Hook:** Accepts short audio files (WAV master plus compressed AAC or CAF for apps) [inferred formats]. If no: (1) stay silent, which is the norm for web and productivity apps; (2) use system sounds on native platforms; (3) commission a sound designer for a sonic logo, with the caveat that repeated identical sounds feel mechanical [S-L04-074].
- **Preview:** the event list with a play button per sound and the mute state.
- **Use / avoid:** use sound only for rare, meaningful events that honor silent mode; avoid sounds on web and in shared-space products [DC-L04-27].
- **Skip:** yes, silent.
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L04-27; S-L04-043, S-L04-072, S-L04-074
- **Merges:** B7 (sonic logo)

### Q-motion-09 · On native platforms, whose transitions, back behavior and haptics? · Expert
- **Show if:** Q-plat-01 includes ios or android
- **Why:** OS-owned back gestures and transitions feel native (Android predictive back peeks behind); custom haptics feel cheap when overused [DC-L10-14, DC-L04-26].
- **Ask:** "Use the platform's own navigation transitions and haptics, with brand motion only inside content?"
- **Example:** Show Android predictive back and an iOS swipe-back on the preview.
- **Control:** single choice (motion) + single choice (haptics)
- **Options:**
  - `os-nav-brand-micro` OS navigation transitions and back behavior, brand micro-motion as springs in content [DC-L10-14].
  - `one-language` One brand motion language everywhere [DC-L10-14].
  - `haptics-system` System haptics only (standard controls already play them) [S-L04-043].
  - `haptics-semantic` A semantic haptic map of about 6 events (success, warning, error, selection, toggle, light impact) [S-L04-044, S-L04-047].
- **Default:** os-nav-brand-micro and haptics-system; a semantic map only for products with frequent confirmations. *Source:* card heuristics [DC-L10-14, DC-L04-26].
- **Decides:** DC-L10-14, DC-L04-26
- **Changes:** DC-L07-14 · blocks: Foundations > Motion > Platform motion; Haptics > Semantic haptic map
- **Preview:** the event list with each haptic's platform mapping.
- **Use / avoid:** use haptics sparingly ("less is more"); avoid long "buzzy" vibrations [S-L04-046; DC-L04-26].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L10-14, DC-L04-26; S-L04-043, S-L04-044, S-L04-046, S-L10-020, S-L10-024
- **Merges:** P15

### Q-motion-10 · Which OS accessibility settings must the system honor? · Expert
- **Why:** Honoring settings changes the look for that user: thicker borders in high contrast, opaque bars under reduced transparency [DC-L10-16].
- **Ask:** "Honor every OS accessibility setting: screen readers, text size, contrast, reduced transparency, reduced motion, bold text, forced colors?"
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
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L10-16; S-L10-008, S-L10-031, S-L10-072, S-L10-075
- **Merges:** P17, K4.4

---

## Stage 17 · Icons, app icon and logo use
> Screen: an icon sheet in the product's own buttons, tabs and lists, next to body text at each size. Graph step 0-4. Two asset hooks live here: the icon set (Q-icon-01) and the app icon (Q-icon-06).

### Q-icon-01 · Do you have a custom icon set, or should the system adopt a library? · Standard
- **Why:** Icons are a block the builder should not draw from scratch; native sets feel "of the platform", open sets are free and consistent, custom sets carry personality [DC-L05-01; BRIEF requirement 2].
- **Ask:** "Do you already have icons? If not, I'd adopt a library that matches your type and corners."
- **Example:** Show the same toolbar in Lucide, Phosphor, Material Symbols and SF Symbols.
- **Control:** single choice + file upload
- **Options:**
  - `platform-native` Platform-native sets: SF Symbols (7,000+, weight-matched to SF, 20+ scripts) and Material Symbols (variable font, 2,500+) [S-L05-006, S-L05-002].
  - `open-source` An open-source set: Lucide (ISC), Heroicons (MIT, 316), Phosphor (MIT, 1,248, 6 weights), Tabler (6,220), Fluent System Icons (MIT) [S-L05-029, S-L05-032, S-L05-031, S-L05-033, S-L05-014].
  - `custom` Your own brand set (IBM, Atlassian 1.5px at 16px, Octicons) [S-L05-017, S-L05-021, S-L05-024].
  - `extend` A library extended with custom domain icons drawn on its template (Material 24dp keyline template; Apple symbol template) [S-L05-001, S-L05-010].
- **Default:** platform-native on native apps, one open-source set on web; platform glyphs for system actions (share, back, close, more, search, settings), brand icons for product concepts. *Source:* card heuristics [DC-L05-01, DC-L10-25].
- **Decides:** DC-L05-01, DC-L10-25
- **Changes:** DC-L05-02, DC-L05-03, DC-L05-05, DC-L05-10 · blocks: Foundations > Iconography > Icon library source; Platform mapping
- **Hook:** Accepts one SVG per icon on a 16 or 24px master (outlined strokes, no text), or a Figma icon library; icon fonts are accepted but converted, since fonts blur and flash (GitHub moved Octicons to SVG for this reason) [S-L05-038]. If no: (1) adopt an open-source set whose stroke and corners match the type (the default); (2) commission a designer only for domain icons the library lacks, drawn on the library's template; (3) use AI icon generators only as sketches, with the caveat that stroke, keylines and optical size rarely match across a set [inferred]. Apple's terms forbid SF Symbols or look-alikes in app icons and logos [S-L05-010].
- **Preview:** the icon sheet in context; swapping libraries updates every icon.
- **Use / avoid:** use one icon family per product; avoid mixing two libraries' strokes in one toolbar [DC-L05-01, inferred].
- **Skip:** yes; the default library is applied.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-01, DC-L10-25; S-L05-002, S-L05-006, S-L05-010, S-L05-029, S-L05-038
- **Merges:** K7.5 (icons), P26

### Q-icon-02 · Outlined or filled icons, rounded or sharp? · Standard
- **Why:** Outline reads lighter and blends with text; filled reads bolder and is easier to spot at small sizes; icons are where the brand's shape and stroke translate into UI (Atlassian matched icon stroke to its type) [DC-L05-02, DC-L06-13].
- **Ask:** "Outlined or filled icons, and should their corners match your rounded or sharp UI?"
- **Example:** Show a tab bar outlined at rest and filled when selected.
- **Control:** single choice (style) + single choice (corners)
- **Options:**
  - `outlined` Outlined: light, clean, good in dense UIs (Material, Apple toolbars, Fluent Regular) [S-L05-003, S-L05-010, S-L05-014].
  - `filled` Filled: more emphasis (Apple iOS tab bars and swipe actions) [S-L05-010].
  - `duotone` Duotone or two-tone: decorative [DC-L05-02].
  - `rounded` / `sharp` Corners matched to the radius family: pill UIs with rounded icons, 0-2px UIs with sharp icons [DC-L05-02].
- **Default:** outlined at rest, filled plus accent color when selected (two cues that survive color blindness); corners follow Q-shape-01. *Source:* card heuristics [DC-L05-02, DC-L05-06].
- **Decides:** DC-L05-02, DC-L05-06, DC-L06-13
- **Changes:** DC-L05-03 · blocks: Foundations > Iconography > Style; States; Brand match
- **Preview:** the tab bar and toolbar with style and corner toggles.
- **Use / avoid:** keep hover and pressed feedback on the container, not the glyph; avoid color-only selected states [DC-L05-06].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-02, DC-L05-06; S-L05-003, S-L05-010, S-L05-014

### Q-icon-03 · How heavy should icon strokes be? · Expert
- **Why:** Thin strokes look elegant but get fragile below 20px; icons should match the stem weight of the text beside them (Atlassian dropped 2px for 1.5px because 2px felt "too heavy") [DC-L05-03, DC-L06-13].
- **Ask:** "Match icon stroke to your body text weight: about 1.5px at 16px, 2px at 24px?"
- **Example:** Show an icon next to a label at 1.5px and 2px strokes.
- **Control:** slider (stroke) + single choice (terminals)
- **Options:**
  - `2-at-24` 2px at 24 (Material weight 400, Lucide) [S-L05-001, S-L05-029].
  - `1.5-at-24` 1.5px at 24 (Heroicons) [S-L05-032].
  - `1.5-at-16` 1.5px at 16 (Atlassian, Octicons) [S-L05-021, S-L05-024].
  - `variable` Variable weight matched to text (Material wght 100-700; SF Symbols 9 weights) [S-L05-003, S-L05-010].
- **Default:** stroke visually equal to body text weight at the paired size: about 1.5px for 14-16px text, 2px at 24px. *Source:* card heuristics [DC-L05-03, DC-L06-13].
- **Decides:** DC-L05-03
- **Changes:** DC-L15-10 · blocks: Foundations > Iconography > Stroke and corner metrics
- **Preview:** icon-label pairs at each text size with the stroke slider.
- **Use / avoid:** use heavier strokes on busy or photographic backgrounds; avoid sub-1.5px strokes below 20px [DC-L05-03].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-03, DC-L06-13 (context); S-L05-001, S-L05-003, S-L05-021, S-L05-032, S-L06-088

### Q-icon-04 · Which icon sizes, and on which construction grid? · Expert
- **Why:** Keylines make a circle icon and a square icon look the same size; pixel-hinted sizes stay crisp [DC-L05-04, DC-L05-05].
- **Ask:** "Ship 16, 20 and 24px icons on a standard 24/20/2 grid?"
- **Example:** Show a circle and a square icon on the keyline grid.
- **Control:** editable size list + single choice (grid)
- **Options:**
  - `material-grid` 24dp master, 20dp live area, 2dp padding; opsz 20-48 thins large icons (Material) [S-L05-001, S-L05-003].
  - `carbon` 16px default, 20/24/32 also, tuned to 14 and 16px text (Carbon; IBM 32px master scaled down) [S-L05-016, S-L05-017].
  - `fluent` 12, 16, 20, 24, 28, 32, 48 [S-L05-014].
- **Default:** 16, 20, 24 (plus 12 and 32 if needed), sized to the adjacent text line height; Material construction unless the master is 16 or 32. *Source:* card heuristics [DC-L05-05, DC-L05-04].
- **Decides:** DC-L05-05, DC-L05-04
- **Changes:** DC-L03-08 · blocks: Foundations > Iconography > Sizes; Construction grid
- **Preview:** the icon sheet at each size, magnified to show pixel alignment.
- **Use / avoid:** pixel-align at the smallest shipped size; avoid 12px icons for anything interactive [DC-L05-04, DC-L05-05].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-04, DC-L05-05; S-L05-001, S-L05-003, S-L05-014, S-L05-016

### Q-icon-05 · When do icons need labels, and what color are they? · Expert
- **Why:** Labelled icons read calmer and clearer; icon-only toolbars read expert but ambiguous; only a handful of icons are near-universal [DC-L05-07, DC-L05-08].
- **Ask:** "Label icons in navigation, and allow icon-only buttons just for universal actions like search and close?"
- **Example:** Show an icon-only toolbar vs the same toolbar with labels.
- **Control:** single choice (labels) + single choice (color)
- **Options:**
  - `labels-default` Labels by default (Material navigation, Atlassian, Polaris) [S-L05-003, S-L05-021, S-L05-027].
  - `universal-only` Icon-only for about a dozen universal actions (search, close, more, add, delete, edit, share, settings), with a tooltip and accessible name [DC-L05-07].
  - `mono` Monochrome icons matching text color (Carbon 4.5:1, Fluent solid) [S-L05-016, S-L05-014].
  - `semantic-tone` Semantic tones on status icons (Polaris `tone`) [S-L05-027].
- **Default:** labels-default plus universal-only; one neutral icon color aliased to secondary text, semantic colors only on status icons. *Source:* card heuristics [DC-L05-07, DC-L05-08].
- **Decides:** DC-L05-07, DC-L05-08
- **Changes:** DC-L08-08 · blocks: Foundations > Iconography > Icon with text; Color
- **Preview:** toolbar variants with a label toggle; hover shows the tooltip.
- **Use / avoid:** give every icon-only control an accessible label; avoid decorative multicolor icons in UI chrome [DC-L05-07, DC-L05-08; L10 baked-in rule 9].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L05-07, DC-L05-08; S-L05-003, S-L05-014, S-L05-016, S-L05-021, S-L05-027

### Q-icon-06 · Do you have an app icon? · Standard
- **Show if:** Q-plat-01 includes ios, android or desktop, or the web app is installable
- **Why:** The app icon is a designer-made block; on Apple it is layered and lit by Liquid Glass, on Android it is adaptive and themed [DC-L05-12; BRIEF requirement 2].
- **Ask:** "Do you have an app icon? If so, share the layered source; if not, I can make a clearly-marked placeholder from your logo."
- **Example:** Show the icon in default, dark, clear and tinted looks on an iOS home screen and as an Android themed icon.
- **Control:** single choice + file upload
- **Options:**
  - `yes-layered` Yes, layered source (background + foreground layers) [DC-L05-12].
  - `yes-flat` Yes, a flat 1024px image only [DC-L05-12].
  - `no` No: see the Hook line.
- **Default:** one glyph of 1-3 filled shapes on a solid or gradient background, exported as Apple layers, Android foreground/background/monochrome and PWA icons. *Source:* card heuristic [DC-L05-12].
- **Decides:** DC-L05-12
- **Changes:** DC-L10-05 (icon looks follow the user) · blocks: Brand in product > App icon
- **Hook:** Accepts layered SVG or PNG layers at 1024x1024 (watchOS 1088x1088) for Apple's Icon Composer, which applies Liquid Glass and generates default, dark, clear and tinted looks; Android adaptive foreground, background and monochrome layers; PWA maskable 512px [DC-L05-12; S-L05-042]. If no: (1) the builder generates a placeholder from the logo glyph and labels it "placeholder"; (2) commission a designer, the recommended path for a shipped app; photos, fine lines, text and baked-in effects render poorly under system lighting [DC-L05-12]. SF Symbols may not be used in app icons [S-L05-010].
- **Preview:** a home-screen mock per platform with all appearances.
- **Use / avoid:** use simple filled overlapping shapes; avoid photos, fine lines, text and baked-in shadows [DC-L05-12].
- **Skip:** yes; a placeholder is generated.
- **Time weight:** medium (fan-out 1)
- **Evidence:** DC-L05-12; S-L05-007, S-L05-008, S-L05-011, S-L05-042, S-L05-010

### Q-icon-07 · How should icons be named and shipped? · Expert
- **Why:** SVG and native symbols render crisp at every size; icon fonts blur and flash; literal names keep one icon reusable across meanings [DC-L05-10, DC-L05-09].
- **Ask:** "Ship icons as SVG with per-framework components, named by shape with function aliases?"
- **Example:** Show `shield_24_regular.svg` aliased as `action.security`.
- **Control:** single choice (delivery) + single choice (naming)
- **Options:**
  - `svg-components` SVG source of truth generating per-framework components and native packages (Octicons, Heroicons) [S-L05-022, S-L05-038].
  - `icon-font` Icon font or variable font (Material Symbols) [S-L05-002].
  - `name-by-shape` Name by shape ("Shield, not security": Fluent; SF Symbols) [S-L05-014, S-L05-012].
  - `function-alias` Plus a function-alias layer in the component API [DC-L05-09].
- **Default:** SVG source, files named `<name>_<size>_<style>`, size and color as props; name by shape with a function-alias layer; RTL behavior recorded per icon. *Source:* card heuristics [DC-L05-10, DC-L05-09].
- **Decides:** DC-L05-10, DC-L05-09
- **Changes:** DC-L07-09, DC-L16-12 · blocks: Foundations > Iconography > Delivery; Metaphor, naming, localization
- **Preview:** the exported icon package tree.
- **Use / avoid:** mirror directional icons in RTL; avoid mirroring icons that depict real objects (clocks, checkmarks) [DC-L05-09, inferred].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L05-10, DC-L05-09; S-L05-012, S-L05-014, S-L05-022, S-L05-038

### Q-icon-08 · How should the logo appear inside the product? · Expert
- **Why:** A small symbol keeps chrome quiet and product-led; a full lockup reads marketing-led; a brand-colored logo competes with primary actions [DC-L05-13].
- **Ask:** "Symbol-only logo in the app bar and the full lockup on sign-in?"
- **Example:** Show the app bar with the symbol at 24px and the sign-in page with the lockup.
- **Control:** single choice (placement) + single choice (appearance)
- **Options:**
  - `symbol-app-bar` Symbol only at 24-32px in the app bar, lockup on sign-in and marketing [DC-L05-13].
  - `lockup-everywhere` Full lockup everywhere [DC-L05-13].
  - `appearance` Appearance brand, neutral or inverse (Atlassian Logo component) [S-L05-044].
- **Default:** symbol-app-bar with neutral appearance inside dense tools; favicon set from one SVG master. *Source:* card heuristic [DC-L05-13].
- **Decides:** DC-L05-13
- **Changes:** DC-L08-01 (Logo component) · blocks: Brand in product > Logo usage; Favicon
- **Preview:** the app bar and sign-in page.
- **Use / avoid:** give a logo that acts as a link an accessible name; avoid repeating the logo throughout the UI (Apple) [DC-L05-13; S-L10-009].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L05-13; S-L05-014, S-L05-042, S-L05-044

---

## Stage 18 · Imagery, illustration and charts
> Screen: an empty state, onboarding card, hero and dashboard, with the person's own assets dropped in where they exist. Graph step 0-3. Three asset hooks live here: photography (Q-img-01), illustration (Q-img-04) and animated assets (Q-img-06). Image placeholders, chart anatomy tokens and chart accessibility are applied by construction (see "Auto-applied rules").

### Q-img-01 · Does the product use photography, and do you have photos or a photo brief? · Standard
- **Why:** Photography is a block the builder cannot make honestly; natural light and ungraded color read factual and trustworthy, graded cinematic images read emotional [DC-L05-14; BRIEF requirement 2].
- **Ask:** "Will the product show photos? If so, do you have a library or a photo brief?"
- **Example:** Show a hero with a documentary-style photo and one with a studio product shot.
- **Control:** single choice (style) + file upload
- **Options:**
  - `none` No photography [DC-L05-14].
  - `documentary` Documentary: "frames from a film" (IBM lifestyle photography) [S-L05-046].
  - `portraiture` Portraiture with equal stature for every subject (IBM "democratic"; Dropbox People) [S-L05-046, S-L05-057].
  - `still-life` Still life, product or content imagery [S-L05-046].
- **Default:** none for tools; for consumer products, a one-paragraph photo brief (subject types, perspective, light, color treatment, casting) before commissioning or buying. *Source:* card heuristic [DC-L05-14].
- **Decides:** DC-L05-14
- **Changes:** DC-L05-15, DC-L05-16, DC-L05-17 · blocks: Foundations > Imagery > Photography style
- **Hook:** Accepts JPEG, WebP or AVIF exports and a written brief; masters in RAW or TIFF are kept outside the system. If no: (1) the builder drafts the photo brief from the personality sliders for you to edit; (2) commission a photographer (best for recognizability); (3) license stock against the brief; (4) AI-generated images only for placeholders, with the caveat that they can misrepresent people and products [inferred]. Neutral placeholders are used until real images arrive.
- **Preview:** image slots in the hero, cards and avatars with the uploaded photos, or labeled placeholders.
- **Use / avoid:** use real product and people photos where trust matters; avoid stock that contradicts the brief's casting and light [DC-L05-14].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-14; S-L05-046, S-L05-057, S-L05-011
- **Merges:** K7.5 (imagery)

### Q-img-02 · Which aspect ratios, and can text sit on images? · Expert
- **Why:** A small ratio set gives grids a calm rhythm; text beside images reads clean and keeps photos honest, scrims read cinematic but darken them [DC-L05-15, DC-L05-16].
- **Ask:** "Limit images to a few ratios like 16:9, 3:2 and 1:1, and keep text beside images rather than on them?"
- **Example:** Show a card grid with mixed ratios vs a fixed ratio set, and a hero with and without a scrim.
- **Control:** multi-select (ratios) + single choice (text on images)
- **Options:**
  - `ibm-set` 16:9, 4:3, 3:2, 2:1, 1:1 aligned to the grid (IBM) [S-L05-047].
  - `per-component` One ratio per component slot (16:9 hero, 3:2 card, 1:1 avatar) [DC-L05-15].
  - `text-beside` Text beside images (IBM avoids overlays on photos) [S-L05-047].
  - `scrim` A scrim token under text on heroes, contrast-tested against the worst-case region [S-L05-072].
- **Default:** 3-5 ratios, one per slot; text beside images, a scrim token only for heroes. *Source:* card heuristics [DC-L05-15, DC-L05-16].
- **Decides:** DC-L05-15, DC-L05-16
- **Changes:** DC-L04-18 · blocks: Foundations > Imagery > Aspect ratios; Text on images
- **Preview:** the card grid and hero with live contrast readout.
- **Use / avoid:** use art-directed crops per breakpoint for heroes; avoid text over busy image regions without a scrim [DC-L05-15, DC-L05-16].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L05-15, DC-L05-16; S-L05-047, S-L05-072, S-L05-083

### Q-img-03 · Which avatar shapes should mean what? · Expert
- **Why:** Circles read personal, squares institutional; a distinct shape makes AI actors instantly recognizable [DC-L05-18].
- **Ask:** "Circle for people, square for teams, and a third shape for AI agents?"
- **Example:** Show a comment thread with a person, a team and an AI agent.
- **Control:** single choice
- **Options:**
  - `circle-square` Circle = person, square = team or org (Primer, Fluent, Atlassian) [S-L05-066, S-L05-067, S-L05-069].
  - `agent-shape` Plus a distinct shape for AI agents (Primer treats bots and agents as square) [S-L05-069].
- **Default:** circle-square plus an agent shape if the product mixes human and AI actors; sizes 16-64 on a 4/8 rhythm with initials fallback. *Source:* card heuristic [DC-L05-18].
- **Decides:** DC-L05-18
- **Changes:** DC-L08-22 · blocks: Components > Avatar
- **Preview:** the comment thread with fallbacks (initials, placeholder) and presence dots.
- **Use / avoid:** keep shape meaning consistent everywhere; avoid using the person circle for bots [DC-L05-18].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L05-18; S-L05-066, S-L05-067, S-L05-069

### Q-img-04 · Do you have illustrations or a mascot, and where should illustration appear? · Standard
- **Why:** Illustration is a designer-made block; characters and hand-drawn styles add warmth and let the UI stay neutral, but overuse adds cognitive load [DC-L06-12, DC-L05-19, DC-L05-20].
- **Ask:** "Do you have illustrations or a mascot? If not, should empty and error states use simple icons and text instead?"
- **Example:** Show an empty state with a neutral spot illustration, a mascot, and icon-plus-text.
- **Control:** single choice (style) + multi-select (where) + file upload
- **Options:**
  - `none` None: empty states use an icon and text [DC-L05-20, inferred].
  - `line` Line style: precise, calm, technical (IBM: 4px grid, at most 4 line weights, 15-degree angles) [S-L05-048, S-L05-049].
  - `flat` Flat: bold and energetic (IBM) [S-L05-049].
  - `hand-drawn` Hand-drawn gestural line (Notion) [S-L06-092].
  - `mascot` A mascot in loading, error and empty states (Mailchimp Freddie, Duolingo Duo) [S-L06-028, S-L06-026].
  - `where` Where: spot illustrations for empty, error, celebration; low-fidelity UI for onboarding; hero and collage only on marketing (Atlassian, Dropbox) [S-L05-050, S-L05-057].
- **Default:** one style derived from the icon stroke, corner radius and palette; neutral spots for routine empty states, colorful spots only for first run and celebration; no humor in errors. *Source:* card heuristics [DC-L05-19, DC-L05-20, DC-L06-12].
- **Decides:** DC-L05-19, DC-L06-12, DC-L05-20
- **Changes:** DC-L05-11, DC-L13-10, DC-L13-11 · blocks: Foundations > Illustration > Style; Brand style and characters; Types and usage
- **Hook:** Accepts SVG (preferred), PNG at 2x, Lottie JSON for animated pieces, plus any illustration guidelines. If no: (1) ship icon-plus-text empty states, which is honest and cheap; (2) commission an illustrator with a brief derived from the icon stroke and palette; (3) use AI generation for drafts only, with the caveat that style drifts from piece to piece unless one artist or a strict style guide owns it [inferred].
- **Preview:** the empty, error and success states with the uploaded art or the fallback.
- **Use / avoid:** use illustration only where it has a job (IBM: "have a job to do"); avoid real screenshots in onboarding illustrations and jokes in error states [S-L05-049, S-L05-050; DC-L06-12].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L05-19, DC-L06-12, DC-L05-20; S-L05-048, S-L05-049, S-L05-050, S-L06-026, S-L06-028
- **Merges:** K7.5 (illustration), B7 (illustration, mascot)

### Q-img-05 · Do you need pictograms between UI icons and illustrations? · Expert
- **Show if:** Q-scope-01 includes marketing
- **Why:** A pictogram tier bridges austere UI icons and full illustration, so feature grids look richer [DC-L05-11].
- **Ask:** "Add larger pictograms for feature grids and onboarding, drawn with the icon stroke logic?"
- **Example:** Show a 24px UI icon, a 64px pictogram and a 120px spot icon of the same concept.
- **Control:** single choice
- **Options:**
  - `three-tiers` UI icons 24, pictograms 64, spot icons 120 (Dropbox) [S-L05-058].
  - `ui-pictograms` UI icons plus a pictogram library (IBM) [S-L05-049].
  - `ui-only` UI icons only; illustrations cover larger needs (Atlassian) [S-L05-050].
- **Default:** a pictogram tier only with marketing surfaces, drawn with the UI icon's stroke logic scaled up. *Source:* card heuristic [DC-L05-11].
- **Decides:** DC-L05-11
- **Changes:** none downstream in the graph · blocks: Foundations > Iconography > Tiers
- **Preview:** a feature grid with each tier.
- **Use / avoid:** use pictograms on marketing and onboarding; avoid them inside dense product UI [DC-L05-11].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L05-11; S-L05-049, S-L05-050, S-L05-058

### Q-img-06 · Do you have animated icons, Lottie files, 3D assets or custom emoji? · Expert
- **Why:** Animated symbols confirm actions in little space; 3D and Lottie make a product feel alive but belong to onboarding and celebration [DC-L05-21].
- **Ask:** "Any animated or 3D assets to include? Otherwise I'll animate icons only to confirm actions or show status."
- **Example:** Show an SF Symbols bounce on a saved state and a Lottie celebration on first success.
- **Control:** multi-select + file upload
- **Options:**
  - `symbol-animation` Built-in symbol animation (SF Symbols Appear, Bounce, Pulse, Replace, Draw) [S-L05-010, S-L05-006].
  - `lottie` Lottie or animated illustration for onboarding and celebration [DC-L05-21].
  - `3d` 3D assets [DC-L05-21].
  - `emoji-stickers` Custom emoji or stickers [DC-L05-21].
- **Default:** symbol animation only, to confirm an action or show ongoing status; 3D and Lottie kept for onboarding, celebration and marketing. *Source:* card heuristic [DC-L05-21].
- **Decides:** DC-L05-21
- **Changes:** DC-L04-25 (every animation needs a reduced-motion version) · blocks: Foundations > Rich media
- **Hook:** Accepts Lottie JSON or dotLottie, animated SVG, GLB or USDZ for 3D, PNG or SVG for emoji [inferred formats]. If no: use built-in symbol animation; commission a motion designer for celebration moments.
- **Preview:** each asset playing in its slot, with the reduced-motion alternative.
- **Use / avoid:** use animated assets for rare moments; avoid looping animation near reading content [DC-L05-21; DC-L04-25].
- **Skip:** yes.
- **Time weight:** medium (fan-out 0)
- **Evidence:** DC-L05-21; S-L05-006, S-L05-010, S-L05-062, S-L05-063

### Q-img-07 · Where may brand graphic devices and motifs appear? · Expert
- **Why:** Graphic devices add recognizability and warmth; overused they clutter and compete with content [DC-L06-11].
- **Ask:** "Should brand shapes or motifs appear only on marketing, onboarding and empty states?"
- **Example:** Show Slack-style logo shapes on an onboarding card and absent from the product table.
- **Control:** single choice
- **Options:**
  - `none` None in product (Carbon product UI) [S-L06-001].
  - `expressive-only` Only on expressive surfaces: marketing, onboarding, empty states, hero moments [DC-L06-11].
  - `logo-shapes` Logo shapes as devices throughout (Slack) [S-L06-030].
- **Default:** expressive-only. *Source:* card heuristic [DC-L06-11].
- **Decides:** DC-L06-11
- **Changes:** DC-L13-10, DC-L13-11 · blocks: Foundations > Brand > Graphic devices
- **Preview:** onboarding and a product screen with the motif on and off.
- **Use / avoid:** let branding defer to content in task screens (Apple) [S-L06-008]; avoid devices behind text.
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L06-11; S-L06-001, S-L06-008, S-L06-024, S-L06-030

### Q-viz-01 · Which chart types and chart library? · Standard
- **Show if:** Q-color-19 is not none
- **Why:** Fewer chart types make dashboards consistent and learnable; exotic types look impressive but need more reading [DC-L05-22].
- **Ask:** "Which charts do you need? I'd start with bar, line, area, stacked bar, donut and scatter, themed on an existing library."
- **Example:** Ask for one real dashboard question ("sales by region this quarter") and show the recommended chart.
- **Control:** multi-select (types) + text (library)
- **Options:**
  - `core-6` Bar, line, area, stacked bar, donut or meter, scatter, plus a KPI big number [DC-L05-22].
  - `by-purpose` Guidance grouped by question: comparisons, trends, part-to-whole, correlations, connections, geospatial (Carbon) [S-L05-075].
  - `theme-library` Theme an existing chart library rather than building one [DC-L05-22].
- **Default:** core-6 on a themed existing library; chart chrome mapped to text and border tokens; every chart gets an insight title, direct labels, a text summary and a "view as table" option. *Source:* card heuristics [DC-L05-22, DC-L05-24, DC-L05-25].
- **Decides:** DC-L05-22
- **Changes:** DC-L05-24, DC-L05-25 · blocks: Foundations > Data visualization > Chart types and library
- **Preview:** a dashboard with the chosen types in the product's palette.
- **Use / avoid:** use bars for comparison and lines for trends; avoid pie charts with more than a few slices and 3D charts [DC-L05-22, inferred].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L05-22; S-L05-075, S-L05-076, S-L05-077, S-L05-083

---

## Stage 19 · Content and voice
> Screen: the product's own buttons, errors, empty states and a success message, rewritten live as voice and tone settings change. Graph step 1-3. Voice comes before components because every component ships its microcopy rules (L06: "voice is a foundation, not a docs appendix") [DC-L06-18]. One asset hook: an existing voice guide (Q-voice-01).

### Q-voice-01 · Do you have a voice and tone guide? If not, what 3-4 traits describe how the product talks? · Standard
- **Why:** Voice is constant while tone shifts by situation; the product's words and visuals must agree [DC-L06-18; S-L06-013].
- **Ask:** "Do you have a voice guide? If not, give me 3-4 traits in 'X, but not Y' form and I'll draft copy examples."
- **Example:** Show Mailchimp's "plainspoken, genuine" and Atlassian's "Bold, Optimistic, Practical with a wink" beside the same error message.
- **Control:** single choice + file upload or text (traits)
- **Options:**
  - `upload` Upload an existing guide [DC-L06-18].
  - `plainspoken` Plainspoken and genuine, dry humor (Mailchimp) [S-L06-014].
  - `warm-crisp` Warm and relaxed, crisp and clear, ready to lend a hand (Microsoft) [S-L06-046].
  - `bold-optimistic` Bold, optimistic, practical with a wink (Atlassian) [S-L06-060].
  - `custom` Custom traits on NN/g's four tone dimensions with anti-tone words [S-L06-013].
- **Default:** drafted from the personality sliders: 3-4 traits with "but not", 3 copy examples per trait. *Source:* card heuristic [DC-L06-18; S-L06-070].
- **Decides:** DC-L06-18
- **Changes:** DC-L06-19, DC-L06-20, DC-L06-21, DC-L06-22, DC-L06-23 · blocks: Content > Voice
- **Hook:** Accepts a PDF, Markdown file or URL of an existing style guide. If no: (1) the builder drafts traits and examples from the sliders for review; (2) have a content designer review them (22% of teams have none) [S-L11-030]; the draft is labeled as a draft until someone owns it [inferred].
- **Preview:** the error, empty state and success message rewritten in the chosen voice.
- **Use / avoid:** use the traits to decide copy disputes; avoid traits every product could claim ("simple", "friendly") without a "but not" [DC-L06-18; DC-L11-05].
- **Skip:** yes.
- **Time weight:** high (fan-out 5)
- **Evidence:** DC-L06-18; S-L06-013, S-L06-014, S-L06-046, S-L06-060, S-L06-070
- **Merges:** K3.6, B13 (voice)

### Q-voice-02 · How should tone change for errors, success and first use? · Standard
- **Why:** Errors need calm visuals and plain words; success can carry illustration, motion and a wink; a joke once may amuse but a dozen times annoys [DC-L06-19; S-L06-060].
- **Ask:** "How should tone shift: serious for errors, warmer for success, gentler for new users?"
- **Example:** Show one error and one success message at three tone settings.
- **Control:** tone matrix (situation x dial)
- **Options:**
  - `emotion-dial` By user emotion: less bold for new or anxious users, a wink for success (Atlassian) [S-L06-060].
  - `situation` By situation: straightforward for serious events, congratulatory for goals (Apple) [S-L06-052].
  - `nng-profile` An NN/g four-dimension profile per content type [S-L06-013].
- **Default:** errors serious, respectful, matter-of-fact; success as warm as the brand allows; clarity beats entertainment. *Source:* card heuristic [DC-L06-19; S-L06-014].
- **Decides:** DC-L06-19
- **Changes:** DC-L13-07, DC-L13-10 · blocks: Content > Tone
- **Preview:** the tone matrix with each cell's example message.
- **Use / avoid:** use warmth after trust is earned (success, completion); avoid humor in errors and in high-trust categories [DC-L06-19; S-L06-060].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L06-19; S-L06-013, S-L06-014, S-L06-052, S-L06-060
- **Merges:** B13 (tone)

### Q-voice-03 · Sentence case or title case? · Standard
- **Why:** Title case reads formal and lengthens the visual texture of labels; sentence case reads casual and localizes cleanly [DC-L06-20; S-L06-052].
- **Ask:** "Sentence case everywhere, or title case for headings and navigation?"
- **Example:** Show a nav, heading and button in "Create new project" vs "Create New Project".
- **Control:** single choice
- **Options:**
  - `sentence` Sentence case everywhere (Microsoft, Atlassian, Fluent) [S-L06-047, S-L06-056, S-L06-098].
  - `title-headings` Title case for headings and global nav, sentence case for buttons (Mailchimp) [S-L06-051].
  - `per-element` Per-element choice applied consistently (Apple) [S-L06-052].
- **Default:** sentence case everywhere; all caps only on 11-12px labels with extra tracking. *Source:* card heuristics [DC-L06-20, DC-L02-18].
- **Decides:** DC-L06-20
- **Changes:** DC-L06-22 · blocks: Content > Mechanics > Capitalization
- **Preview:** the product screen's labels re-cased live.
- **Use / avoid:** use one rule per element type everywhere; avoid all caps for sentences [DC-L06-20, DC-L02-18].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L06-20; S-L06-047, S-L06-051, S-L06-052, S-L06-056

### Q-voice-04 · What reading level and label length should copy target? · Standard
- **Why:** Shorter strings shrink components, truncate less and read faster; even experts prefer plain language [DC-L13-13; S-L13-091].
- **Ask:** "Plain language for everyone, around a 6th-8th grade level, or 10th-12th for specialist tools?"
- **Example:** Show one help text at grade 7 and grade 12.
- **Control:** single choice + number (max words per button)
- **Options:**
  - `grade-6-8` 6th-8th grade for general audiences [S-L13-091].
  - `grade-10-12` 10th-12th grade for specialists [S-L13-091].
  - `labels-2-4` Command labels of 2-4 words, verb first, describing the resulting state [S-L13-036].
- **Default:** 6th-8th for consumer products, 10th-12th for expert tools; button labels 2-4 words, verb first; readability over target is a lint warning. *Source:* card heuristic [DC-L13-13].
- **Decides:** DC-L13-13
- **Changes:** DC-L13-07, DC-L13-16 · blocks: Foundations > Content > Readability
- **Preview:** a readability score beside each sample string.
- **Use / avoid:** use verbs that name the result ("Save changes"); avoid branded or clever button labels [DC-L13-13, DC-L06-22].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L13-13; S-L13-036, S-L13-091

### Q-voice-05 · Which grammar and punctuation rules? · Expert
- **Why:** Contractions, "we" and occasional emoji read friendlier; no negative contractions and no exclamation marks read more formal and precise [DC-L06-21].
- **Ask:** "Contractions yes, 'you' for the user, 'we' sparingly, and no exclamation marks in errors?"
- **Example:** Show "We couldn't save your file!" vs "Your file wasn't saved. Try again."
- **Control:** toggles
- **Options:**
  - `contractions` Contractions, except negative ones in high-stakes flows (GOV.UK writes "cannot") [S-L06-048].
  - `pronouns` "You" for the user, "we" sparingly (Apple avoids "we") [S-L06-052].
  - `exclamations` No exclamation marks in errors [S-L06-049].
  - `numbers` Numerals for counts, "to" for ranges [DC-L06-21].
- **Default:** all four as listed. *Source:* card heuristic [DC-L06-21].
- **Decides:** DC-L06-21
- **Changes:** DC-L06-22 · blocks: Content > Mechanics
- **Preview:** sample strings updating per toggle.
- **Use / avoid:** keep mechanics identical across products; avoid mixing date and number formats (see Q-voice-06) [DC-L06-21].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L06-21; S-L06-046, S-L06-048, S-L06-049, S-L06-052, S-L06-056

### Q-voice-06 · Which microcopy patterns and word list should components ship with? · Expert
- **Why:** Verb labels shorten buttons and clarify hierarchy; consistent terms make navigation and empty states predictable [DC-L06-22, DC-L06-23].
- **Ask:** "Start a 20-50 term glossary and ship microcopy rules with every component?"
- **Example:** Ask for 5 terms users see often ("workspace" or "project"?) and show them in the nav and an empty state.
- **Control:** text list (glossary) + toggles (patterns)
- **Options:**
  - `verb-first` Verb-first buttons, descriptive links (not "Click here"), blame-free fix-it errors, empty states with a next step [S-L06-052, S-L06-051].
  - `flow-vocab` Consistent flow vocabulary: Get started, Continue/Next, Done [S-L06-052].
  - `word-list` A maintained A-Z word list (Mailchimp, Microsoft) [S-L06-014, S-L06-047].
  - `inclusive` Bias-free rules: role nouns, singular they, people's own pronouns (Microsoft; Atlassian inclusive-language page) [S-L06-102, S-L06-054].
- **Default:** all four; a 20-50 term glossary on day one, linted in copy; locale formats and any regulated copy recorded as fixed patterns. *Source:* card heuristics [DC-L06-22, DC-L06-23]; K5.3 and K5.5 [inferred].
- **Decides:** DC-L06-22, DC-L06-23
- **Changes:** DC-L11-18 · blocks: Content > Microcopy; Content > Terminology
- **Preview:** each component with its microcopy rule and an example.
- **Use / avoid:** use the glossary term everywhere; avoid synonyms for the same object [DC-L06-23].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L06-22, DC-L06-23; S-L06-014, S-L06-047, S-L06-051, S-L06-052, S-L06-102
- **Merges:** K5.3, K5.4, K5.5

---

## Stage 20 · Component base and inventory
> Screen: the component catalog, rendered with every foundation chosen so far; each component opens to a detail card (anatomy, states, when to use, when not to use). Graph step 0-3.

### Q-comp-01 · What should your components be built on? · Standard
- **Why:** Headless primitives leave every visual choice to your tokens; styled forks inherit the source's look until re-themed; native controls inherit the platform look [DC-L08-03]. Adopting a whole system makes you look like it ("websites made with shadcn/ui famously look the same") [DC-L11-01; S-L11-073].
- **Ask:** "Build on headless primitives, a copy-in styled layer like shadcn, web components, native controls, or adopt a full system as-is?"
- **Example:** Show the same dialog built on Base UI with your tokens vs stock Material.
- **Control:** single choice per platform (pre-filled from Q-plat-08 and Q-tool-02)
- **Options:**
  - `headless` Headless primitives: Radix, Base UI (v1 stable Dec 2025), React Aria, Ark UI [S-L08-030, S-L08-026, S-L08-032, S-L08-031].
  - `copy-in-styled` Copy-in styled layer: shadcn/ui on Base UI (its default since July 2026), Radix or React Aria [S-L08-020; BOARD L08 note].
  - `web-components` Web components (Polaris, Fluent UI Web Components v3) [S-L08-022, S-L08-010].
  - `native` Native controls themed with your tokens (SwiftUI/UIKit, Compose Material 3) [S-L08-103, S-L08-105].
  - `adopt` Adopt a system as-is (Material, Carbon, Fluent, Untitled UI) [S-L11-078; DC-L11-01].
- **Default:** React web: shadcn on Base UI or React Aria; multi-framework: Ark UI or web components; mobile: native controls; small teams adapt an accessible base and invest in tokens and docs. *Source:* card heuristics [DC-L08-03, DC-L11-01; S-L11-006, S-L11-030].
- **Decides:** DC-L08-03, DC-L11-01
- **Changes:** DC-L08-04, DC-L11-20 · blocks: Components > Implementation > Base library; Strategy > Starting point
- **Preview:** the catalog re-rendered per base; a keyboard-test strip shows focus order and ARIA roles inherited.
- **Use / avoid:** use accessible primitives so keyboard and ARIA behavior come for free; avoid assuming re-themed colors inherit contrast (they don't) [DC-L11-01].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L08-03, DC-L11-01; S-L08-020, S-L08-026, S-L08-030, S-L11-006, S-L11-073
- **Merges:** K0.5, K2.6

### Q-comp-02 · Which components are in version 1? · Standard
- **Why:** Completeness is the top adoption factor (79%), but a large inventory raises maintenance cost [DC-L08-01; S-L11-030].
- **Ask:** "Start with the 25 core components most systems share, and add others when two products need them?"
- **Example:** Show the core 25 as a grid; ask which screens of their product need something missing.
- **Control:** multi-select (catalog, core pre-checked)
- **Options:**
  - `core-25` Core (about 25, in 8-10 of 10 benchmark systems): Button, Text field, Textarea, Select, Checkbox, Radio, Switch, Slider, Tabs, Tooltip, Popover, Dialog, Menu, Progress bar, Spinner, Alert/banner, Badge, Avatar, Card, List, Table, Link, Breadcrumbs, Side navigation, Accordion [DC-L08-01].
  - `extended` Extended (about 25 more): combobox, multi-select, date picker, file upload, toast, skeleton, empty state, drawer/sheet, pagination and others [DC-L08-01].
  - `logo-ai` Brand and AI extras: Logo, AI label and AI button (see Q-icon-08, Q-ai-01).
- **Default:** core-25; extended components when two or more products ask for them. *Source:* card heuristic [DC-L08-01].
- **Decides:** DC-L08-01
- **Changes:** DC-L11-18 · blocks: Components > Inventory
- **Preview:** the catalog grid with a count and a "used by" tag per component.
- **Use / avoid:** use the audit (Q-scope-02) and pilot to pick extras; avoid building components no product has asked for [DC-L08-01, DC-L11-07].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L08-01; S-L08-001, S-L08-008, S-L08-009, S-L11-030
- **Merges:** K8.1

### Q-comp-03 · Configuration props or composable parts? · Expert
- **Why:** Configuration keeps screens uniform; composition allows richer layouts with more variance; Figma slots let instances vary without detaching [DC-L08-04, DC-L07-22].
- **Ask:** "Props for small components like Button, composable parts for containers like Dialog and Card?"
- **Example:** Show `<Button variant="primary">` vs `<Dialog.Root><Dialog.Title/>...</Dialog.Root>`, and a Figma card with a slot.
- **Control:** single choice (code) + single choice (Figma)
- **Options:**
  - `config` Props-only configuration (Carbon, Primer, Polaris) [S-L08-064, S-L08-068].
  - `compound` Compound parts, asChild/Slot, render props (Base UI, Radix, React Aria) [S-L08-087, S-L08-088, S-L08-089].
  - `figma-api` Figma: variants for state, size and type; booleans for optional icons; text props for labels; instance swap for single icons; slots for repeating or freeform content [S-L07-021, S-L07-022].
- **Default:** configuration for leaf components, compound parts for containers; the Figma mapping as listed. *Source:* card heuristics [DC-L08-04, DC-L07-22].
- **Decides:** DC-L08-04, DC-L07-22
- **Changes:** DC-L11-18 · blocks: Components > API; Components > Figma component API
- **Preview:** generated code and the Figma component panel for one component.
- **Use / avoid:** use slots for cards, modals and lists so instances keep receiving updates; avoid variant explosions for optional content [DC-L07-22].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L08-04, DC-L07-22; S-L07-021, S-L07-022, S-L08-064, S-L08-088

### Q-comp-04 · How should components be grouped and named? · Expert
- **Why:** The hierarchy affects findability and consistent naming across Figma and code [DC-L08-02].
- **Ask:** "Group as tokens, primitives, components, patterns and templates, with an alias table for other systems' names?"
- **Example:** Show "Sheet / Drawer / Side panel" mapped to one name.
- **Control:** single choice
- **Options:**
  - `atomic` Atomic design (atoms to pages) [S-L08-054].
  - `primitives-components-patterns` Primitives / components / patterns (Atlassian, Radix) [S-L08-011, S-L08-021].
  - `foundations-components-patterns` Foundations / components / patterns (Carbon, HIG) [S-L08-009, S-L08-086].
  - `purpose` Purpose categories: action, containment, communication, navigation, selection, text input (M3) [S-L08-008].
- **Default:** tokens > primitives > components > patterns > templates, with an alias table. *Source:* card heuristic [DC-L08-02].
- **Decides:** DC-L08-02
- **Changes:** DC-L11-18 · blocks: Components > Taxonomy
- **Preview:** the catalog's sidebar regrouped per option.
- **Use / avoid:** use one canonical name with aliases; avoid two components for one job [DC-L08-02].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-02; S-L08-008, S-L08-011, S-L08-054, S-L08-086
- **Merges:** K8.2

### Q-comp-05 · One component set for every device, or separate sets? · Expert
- **Show if:** Q-plat-02 marks watch, TV or car as first-class or works
- **Why:** One set keeps the brand identical and cheap but risks phone-shaped components on a watch or TV [DC-L14-02].
- **Ask:** "One set with device modes for phone, tablet and desktop, plus small separate libraries for watch and TV?"
- **Example:** Show a phone list row next to the TV focus-row version.
- **Control:** single choice
- **Options:**
  - `one-set-modes` One set, tokens vary by mode (Spectrum desktop/mobile values; Carbon AI presence mode) [S-L03-044, S-L14-058].
  - `separate-libraries` Shared foundations, separate libraries per device (Wear Compose Material 3, TV Material) [S-L10-026, S-L14-025].
  - `templates` Template adapters, no custom components (car) [S-L14-010].
- **Default:** one set for phone, tablet, desktop and web with context modes; separate small libraries for watch and TV; templates for car. *Source:* card heuristic [DC-L14-02].
- **Decides:** DC-L14-02
- **Changes:** none downstream in the graph · blocks: Components > Architecture > Device variants
- **Preview:** one component across device classes.
- **Use / avoid:** split a library when the input model changes (focus, crown, templates); avoid stretching phone components onto TV [DC-L14-02].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L14-02; S-L03-044, S-L10-026, S-L14-010, S-L14-025

---

## Stage 21 · Actions, states and focus
> Screen: a live component sheet where every control can be hovered, pressed, focused with the keyboard, disabled and set to loading. Graph step 0-7. The microinteraction spec (DC-L13-12) is generated for every component (see "Auto-applied rules").

### Q-state-01 · How many button emphasis levels, and how many primary actions per view? · Standard
- **Why:** Three levels read calm and strict; five or six allow dense toolbars; several filled buttons flatten hierarchy and look like ads [DC-L08-05, DC-L13-18].
- **Ask:** "Four button levels plus danger, with one primary action per region?"
- **Example:** Show a form footer with primary, secondary, tertiary and ghost buttons, then the same with two primaries flagged.
- **Control:** single choice + toggle (one primary per region)
- **Options:**
  - `three` Solid, outline, text [DC-L08-05].
  - `four-danger` Primary, secondary, tertiary/outline, ghost/text, plus danger (Carbon, Fluent) [S-L08-061, S-L08-066].
  - `five-plus` 5-7 levels including tonal, elevated, discovery or AI variants (M3 5; Atlassian 7 incl. Rovo) [S-L08-033, S-L08-063].
- **Default:** four-danger; at most one high-emphasis action per region, placed after the last field in reading order; a destructive button never takes the primary role. *Source:* card heuristics [DC-L08-05, DC-L13-18; S-L13-054, S-L08-039].
- **Decides:** DC-L08-05, DC-L13-18
- **Changes:** DC-L08-06, DC-L08-14, DC-L13-15 · blocks: Components > Button > Variants; Components > Actions > Emphasis hierarchy
- **Preview:** the button sheet in every state, plus a form footer.
- **Use / avoid:** use style, not size, to mark the preferred choice (Apple); avoid two primary buttons in one group [S-L08-039; L13 E1].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L08-05, DC-L13-18; S-L08-033, S-L08-061, S-L08-063, S-L13-014, S-L13-054

### Q-state-02 · How obvious should clickable things be? · Standard
- **Why:** Minimal signifiers look sleek but cost 22% more time and 25% more fixations to find targets (NN/g) [DC-L15-09; S-L15-004].
- **Ask:** "Strong, balanced or minimal signals that something is clickable?"
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
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L15-09; S-L15-004, S-L15-006, S-L15-038, S-L15-054

### Q-state-03 · What should the keyboard focus ring look like? · Standard
- **Why:** Thicker, offset rings are unmistakable but louder; inner rings keep dense grids tight but can fail contrast on filled controls [DC-L04-09, DC-L08-11].
- **Ask:** "A 2px ring with a 2px gap that follows each component's corners, in a color that shows on every surface?"
- **Example:** Tab through a button, input and table row with each ring style.
- **Control:** single choice + width/offset numbers
- **Options:**
  - `outer-2-2` 2px solid ring, 2px offset, radius = component radius + offset (Atlassian `radius.focus`, Primer 2px) [S-L04-016, S-L04-024].
  - `material-3` 3px ring, 2px outer offset, -3px inner offset where outside rings would clip (Material 3) [S-L04-003].
  - `inset` Inset border for dense grids (Carbon `$focus` + `$focus-inset`) [S-L08-062].
  - `two-tone` Two-tone ring (inner white, outer dark) that is 3:1 on every surface [DC-L08-11].
- **Default:** outer-2-2 in a high-contrast brand or neutral color with light and dark values, plus a forced-colors fallback (an outline, not a box-shadow alone). *Source:* card heuristics and accessibility rule [DC-L04-09, DC-L08-11; S-L10-031].
- **Decides:** DC-L04-09, DC-L08-11
- **Changes:** DC-L07-13 · blocks: Foundations > Borders > Focus ring; Components > States > Focus-visible
- **Preview:** keyboard tab-through of the preview screen with the ring on every stop.
- **Use / avoid:** show focus only for keyboard (`:focus-visible`); avoid rings that the element's own fill hides [DC-L08-11, DC-L04-09].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L04-09, DC-L08-11; S-L04-003, S-L04-016, S-L04-024, S-L08-062, S-L08-069

### Q-state-04 · Which states get their own styling, per input type? · Expert
- **Why:** Overlays give automatic states for any color; explicit tokens allow tuned brand states; TV focus is large and animated while a desktop ring is thin and static [DC-L08-09, DC-L14-06].
- **Ask:** "Style enabled, hover, focus, pressed, selected, disabled, loading and error, with each device rendering the states its inputs can trigger?"
- **Example:** Show a card's states on desktop vs its focused state on TV.
- **Control:** multi-select (states) + single choice (method)
- **Options:**
  - `overlays` Overlays for hover and press (Material state layers) [S-L01-005, S-L08-095].
  - `explicit` Explicit tokens per state and variant (Carbon) [S-L08-062].
  - `per-input` Per input context: desktop rest/hover/focus-visible/pressed/selected/disabled; TV focused with scale and elevation; tablet pointer lift [S-L14-013, S-L14-071].
- **Default:** style all eight states; overlays for hover and press, explicit tokens for selected and error; define states once, render the subset each context can trigger. *Source:* card heuristics [DC-L08-09, DC-L14-06].
- **Decides:** DC-L08-09, DC-L14-06
- **Changes:** DC-L07-02 · blocks: Components > States; Foundations > Interaction > States
- **Preview:** the state matrix for every component.
- **Use / avoid:** make hover content dismissible and persistent (WCAG 1.4.13); avoid hover-only affordances on touch [DC-L14-06].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-09, DC-L14-06; S-L01-005, S-L08-062, S-L14-013, S-L14-070, S-L14-071

### Q-state-05 · How should selected and active items look? · Expert
- **Why:** Brand-colored selection is lively; neutral selection keeps brand color meaning "action" only [DC-L08-14].
- **Ask:** "Show selection with an indicator plus color, and keep brand color for actions?"
- **Example:** Show a tab bar with a pill indicator, an underline and a neutral fill.
- **Control:** single choice
- **Options:**
  - `pill-indicator` Pill-shaped indicator behind the icon (M3 navigation) [S-L08-083].
  - `underline` Underline indicator (Primer UnderlineNav) [S-L08-012].
  - `neutral` Neutral, non-brand selected treatment (Atlassian) [S-L08-085].
  - `morph` Shape morph round to square (M3 Expressive toggles) [S-L08-034].
- **Default:** an indicator plus color, never color alone; brand primary reserved for actions in action-dense products. *Source:* card heuristic [DC-L08-14].
- **Decides:** DC-L08-14
- **Changes:** none downstream in the graph · blocks: Components > States > Selected
- **Preview:** tabs, nav rail and segmented control selected.
- **Use / avoid:** use two cues for selection; avoid selection states that look like primary buttons [DC-L08-14].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-14; S-L08-012, S-L08-034, S-L08-083, S-L08-085

### Q-state-06 · How should destructive actions look? · Expert
- **Why:** Solid red draws the eye and invites mis-clicks on main screens; subtle red keeps lists calm [DC-L08-06].
- **Ask:** "Subtle red in context, solid red only in the confirmation step?"
- **Example:** Show a table row's delete action and the confirmation dialog.
- **Control:** single choice
- **Options:**
  - `solid-danger` Solid red danger button (Carbon, Primer, shadcn destructive) [S-L08-061, S-L08-064, S-L08-065].
  - `danger-levels` Danger at several emphasis levels (Carbon danger primary/tertiary/ghost) [S-L08-061].
  - `warning-vs-danger` Separate warning (significant change) and danger (final irreversible step) (Atlassian) [S-L08-063].
- **Default:** subtle danger in context, solid danger only in the confirmation step. *Source:* card heuristic [DC-L08-06].
- **Decides:** DC-L08-06
- **Changes:** DC-L13-08 · blocks: Components > Button > Danger
- **Preview:** a list with delete actions and the confirm step.
- **Use / avoid:** use undo instead of confirmation for reversible actions (Q-form-05); avoid solid red buttons in dense lists [DC-L08-06].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-06; S-L08-061, S-L08-063, S-L08-064, S-L08-075

### Q-state-07 · Where do icons go inside buttons? · Expert
- **Why:** Leading icons aid scanning; a trailing icon with a left label gives Carbon's editorial look; icon-only buttons need labels [DC-L08-08].
- **Ask:** "Optional leading icons on buttons, with sentence-case verb labels?"
- **Example:** Show "Download" with a leading icon and Carbon-style trailing icon.
- **Control:** single choice
- **Options:**
  - `leading` Optional leading icon (M3, 20dp) [S-L08-033].
  - `trailing` Label left, icon right (Carbon, 16px icon) [S-L08-061, S-L08-062].
  - `both-slots` Both slots (Atlassian iconBefore/iconAfter; Primer leadingVisual/trailingVisual) [S-L08-063, S-L08-064].
- **Default:** optional leading icon, sentence-case verb labels. *Source:* card heuristic [DC-L08-08].
- **Decides:** DC-L08-08
- **Changes:** none downstream in the graph · blocks: Components > Button > Content
- **Preview:** the button sheet with icons.
- **Use / avoid:** use trailing icons for direction (next, external); avoid icon-only buttons without an accessible name [DC-L08-08].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-08; S-L08-033, S-L08-061, S-L08-063, S-L08-064

### Q-state-08 · How should the product show that it is working? · Standard
- **Why:** Skeletons make pages feel structured and faster; spinners feel generic and give no duration; response-time thresholds decide which to use [DC-L13-01, DC-L08-12].
- **Ask:** "Nothing under a second, skeletons for page loads, spinners for single actions, progress bars past ten seconds?"
- **Example:** Simulate a 0.5 s, 3 s and 12 s load on the preview.
- **Control:** single choice + threshold numbers
- **Options:**
  - `nng-ladder` No indicator under 1 s, looped indicator 2-10 s, percent-done over 10 s (NN/g) [S-L13-032, S-L13-031].
  - `skeleton-first` Skeletons for page or region loads, spinners for modules (Carbon skeletons only on containers) [S-L13-033, S-L05-071].
  - `inline-button` Spinner inside the triggering button, which keeps focus (S2 pending after 1 s; Carbon inline loading) [S-L08-067, S-L08-061].
- **Default:** acknowledge within 50ms; the NN/g ladder with skeletons for first page load and in-button pending states that stay focusable. *Source:* card heuristics [DC-L13-01, DC-L08-12]; BOARD L13 note (timing ladder).
- **Decides:** DC-L13-01, DC-L08-12
- **Changes:** DC-L07-14 · blocks: Patterns > Feedback > Loading; Components > States > Loading
- **Preview:** the three simulated waits.
- **Use / avoid:** use optimistic UI only when failure is rare and reversible; avoid spinners for waits under a second [DC-L13-01].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L13-01, DC-L08-12; S-L13-031, S-L13-032, S-L13-033, S-L08-067, S-L08-074

---

## Stage 22 · Forms, validation and feedback
> Screen: a live sign-up form and a list with delete actions; the person fills fields, triggers errors and deletes items to feel each option. Graph step 0-6. Cycles kept together: DC-L08-10 + DC-L08-17 (whether submit can be disabled depends on when validation runs, and vice versa), DC-L13-06 + DC-L13-07 (timing and error message pattern), DC-L13-08 + DC-L13-09 (undo needs a channel such as a toast; the channel set depends on whether undo exists).

### Q-form-01 · What style should form fields have, and where do labels go? · Standard
- **Why:** Filled fields feel soft and app-like, outlined feel crisp and form-heavy; placeholder-only labels cause seven known problems [DC-L08-16, DC-L13-05; S-L13-066].
- **Ask:** "Outlined or filled fields, with labels always visible above them?"
- **Example:** Show one field outlined, filled and underline-only, each filled in and in error.
- **Control:** single choice (style) + single choice (label) + single choice (marking)
- **Options:**
  - `outlined` Outlined fields (M3 outlined; Carbon) [S-L08-105, S-L08-106].
  - `filled` Filled fields (M3 filled) [S-L08-105].
  - `label-top` Persistent label above, hint under the label [S-L13-066].
  - `placeholder-label` Placeholder as label: rejected (memory strain, no way to check entries) [S-L13-066].
  - `mark-minority` Mark whichever of required/optional is rarer, "(optional)" or "(required)" [S-L08-106].
- **Default:** outlined, top labels of 1-3 words without colons, hint under the label, the rarer of required/optional marked, `autocomplete` on personal-data fields. *Source:* card heuristics [DC-L08-16, DC-L13-05].
- **Decides:** DC-L08-16, DC-L13-05
- **Changes:** DC-L08-17 · blocks: Components > Text field; Patterns > Forms > Field anatomy
- **Preview:** the sign-up form in each style, typed into live.
- **Use / avoid:** use a visible label on every field; avoid placeholder-only labels (a lint warning) [DC-L13-05; L13 E1].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L08-16, DC-L13-05; S-L08-105, S-L08-106, S-L13-066, S-L13-068

### Q-form-02 · When should forms show errors, and should the submit button ever be disabled? · Standard
- **Why:** Premature errors feel hostile; on-submit keeps forms calm; disabled buttons hide why an action can't run [DC-L13-06, DC-L08-17, DC-L08-10].
- **Ask:** "Check fields when people leave them, show a summary on submit, and never disable the submit button?"
- **Example:** Let them type a bad email and tab away, then submit with an empty field.
- **Control:** single choice (timing) + single choice (disabled policy)
- **Options:**
  - `on-submit-summary` On submit with an error summary that takes focus, "Error:" prefix, inline messages (GOV.UK) [S-L08-077].
  - `on-blur` On blur ("reward early, punish late"): clear the error on the keystroke that fixes it; validate at complete length for ZIP and phone [S-L13-065, S-L13-100].
  - `disable-short-forms` Disable submit on short forms until valid, never on long ones (Carbon) [S-L08-106].
  - `never-disable` Never disable submit; explain instead (Atlassian) [S-L08-085].
- **Default:** on-blur for format checks, on submit otherwise, summary plus inline for forms over about 5 fields; never-disable, with `aria-disabled` and helper text when an action truly cannot run. *Source:* card heuristics [DC-L13-06, DC-L08-17, DC-L08-10]; systems disagree (see Disagreements).
- **Decides:** DC-L13-06, DC-L08-17, DC-L08-10
- **Changes:** DC-L13-07 · blocks: Patterns > Forms > Validation; Components > States > Disabled
- **Preview:** the live form with timing toggles.
- **Use / avoid:** use on-blur validation for format checks; avoid flagging a field before the person has finished typing [DC-L13-06].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L13-06, DC-L08-17, DC-L08-10; S-L08-077, S-L08-085, S-L08-106, S-L13-065, S-L13-100

### Q-form-03 · How should error messages be shown and written? · Expert
- **Why:** Inline errors keep context; banners signal system problems; dialogs interrupt; prominence should match severity [DC-L13-07; S-L13-064].
- **Ask:** "Errors next to their cause, a banner only for system-level problems, a dialog only when work would be lost?"
- **Example:** Show a field error, a page banner and a blocking dialog for three severities.
- **Control:** mapping (severity to pattern)
- **Options:**
  - `inline` Inline field error next to the source [DC-L13-07].
  - `summary` Error summary at the top of the form [DC-L13-07].
  - `banner` Section or page banner [DC-L13-07].
  - `dialog` Blocking dialog [DC-L13-07].
  - `error-page` Full error page for catastrophic failures [DC-L13-07].
- **Default:** NN/g's 13 error-message guidelines: close to the source, visible without color alone, plain words that say what happened and how to fix it. *Source:* card heuristic [DC-L13-07; S-L13-064, S-L13-030].
- **Decides:** DC-L13-07
- **Changes:** DC-L11-18 · blocks: Patterns > Feedback > Errors
- **Preview:** the three severities on the form.
- **Use / avoid:** use a fix-it sentence in every error; avoid blame and jargon codes [DC-L13-07, DC-L06-22].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L13-07; S-L13-030, S-L13-037, S-L13-064

### Q-form-04 · Where should confirmations and notifications appear: inline, toast, banner or dialog? · Standard
- **Why:** Toasts keep layouts still but flash and vanish; banners persist and are findable; systems disagree on whether toasts belong at all [DC-L08-18, DC-L13-09].
- **Ask:** "Inline or banner by default, toasts only for low-stakes confirmations with undo?"
- **Example:** Save a record and show the confirmation as inline text, a toast and a banner.
- **Control:** single choice + per-status table
- **Options:**
  - `inline-banner` Inline or banner by default; toasts only for low-stakes confirmations with undo, never auto-dismissing toasts that contain actions (Carbon matrix of 4 statuses x 7 types) [S-L08-079; DC-L13-09].
  - `no-toasts` No toasts; banners and dialogs only (Primer) [S-L08-098, S-L08-012].
  - `toasts-widely` Toasts and flags widely (M3 snackbar, Atlassian flags) [S-L08-008, S-L08-011].
- **Default:** inline-banner; the message goes where the cause is. *Source:* card heuristics [DC-L08-18, DC-L13-09]; systems disagree (see Disagreements).
- **Decides:** DC-L08-18, DC-L13-09
- **Changes:** DC-L13-08 · blocks: Patterns > Notifications; Patterns > Feedback > Messaging
- **Preview:** the save action with each channel.
- **Use / avoid:** use toasts only for reversible, low-stakes results; avoid a toast as the only record of an error [DC-L13-09].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L08-18, DC-L13-09; S-L08-008, S-L08-011, S-L08-079, S-L08-098, S-L13-064

### Q-form-05 · For destructive actions, undo or confirm? · Standard
- **Why:** Undo keeps flow fast and calm; frequent confirmations feel bureaucratic and stop being read [DC-L13-08; S-L13-067].
- **Ask:** "Offer undo for anything reversible, and confirm only irreversible or costly actions?"
- **Example:** Delete a list item: show the undo toast, then an irreversible delete with a "Delete file / Keep file" dialog.
- **Control:** single choice
- **Options:**
  - `undo-first` Undo with soft delete or trash for reversible actions (NN/g calls undo superior; Shneiderman rule 6) [S-L13-067, S-L13-037].
  - `confirm` Confirmation dialog with specific verb labels, Cancel as the safe default [S-L13-067; DC-L13-08].
  - `both` Undo for reversible, confirm for irreversible and costly [DC-L13-08].
- **Default:** both. *Source:* card heuristic [DC-L13-08].
- **Decides:** DC-L13-08
- **Changes:** DC-L13-09 · blocks: Patterns > Error prevention > Destructive actions
- **Preview:** the list delete flow per option.
- **Use / avoid:** use verb labels on confirmations; avoid "Are you sure?" dialogs for reversible actions [DC-L13-08].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L13-08; S-L13-037, S-L13-067, S-L08-012, S-L08-039

---

## Stage 23 · Patterns and AI surfaces
> Screen: small flows the person can click through: open a dialog and a side sheet, page through a table, reach an empty state, meet a consent prompt, and see AI-generated content. Graph step 0-2. Content hierarchy for scanning (DC-L13-04) is applied by construction.

### Q-pattern-01 · When should the product use a dialog, a sheet or a popover? · Standard
- **Why:** Centered dialogs interrupt strongly; side sheets keep context visible; popovers feel lightweight [DC-L08-20].
- **Ask:** "Dialogs for short decisions, side sheets for editing with context, bottom sheets on phones?"
- **Example:** Edit a record in a dialog vs a side sheet on the preview.
- **Control:** mapping (task type to overlay)
- **Options:**
  - `hig` Modal only with a clear benefit; sheets and popovers for scoped tasks; full-screen for immersive multi-step tasks (HIG) [S-L08-086].
  - `sheets` Bottom and side sheets, drawers and panels (M3, Fluent, Atlassian) [S-L08-008, S-L08-010, S-L08-011].
  - `levitate` Layered "levitate" panes for focused tasks (M3) [S-L08-096].
- **Default:** dialog for short decisions, side sheet for editing with context, bottom sheet on phones; each platform's button order. *Source:* card heuristic [DC-L08-20].
- **Decides:** DC-L08-20
- **Changes:** DC-L04-18 · blocks: Patterns > Modality; Components > Dialog, Sheet, Popover
- **Preview:** the same edit task in each overlay.
- **Use / avoid:** use a dismiss path on every dialog (missing one is a lint error); avoid stacking modals [DC-L08-20; L13 E1].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-20; S-L08-008, S-L08-040, S-L08-086, S-L08-096

### Q-pattern-02 · How should long lists load: pages, "load more", or infinite scroll? · Expert
- **Why:** Pagination gives landmarks; infinite scroll feels endless; "Load more" keeps the footer reachable [DC-L08-21].
- **Ask:** "Pagination for tables, load more for results, infinite scroll only for feeds?"
- **Example:** Show a table with pagination and a feed with infinite scroll.
- **Control:** mapping (collection type to pattern)
- **Options:**
  - `pagination` Pagination (Carbon, Atlassian, Primer, shadcn) [DC-L08-21].
  - `load-more` Load more [S-L08-073].
  - `infinite` Infinite scroll for homogeneous feeds [S-L08-073].
- **Default:** pagination for tables and goal-directed search, load more for result lists, infinite scroll only for feeds. *Source:* card heuristic [DC-L08-21].
- **Decides:** DC-L08-21
- **Changes:** none downstream in the graph · blocks: Patterns > Collections
- **Preview:** each collection type on the preview.
- **Use / avoid:** use pagination where people need to return to a position; avoid infinite scroll above a footer people need [DC-L08-21].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-21; S-L08-017, S-L08-041, S-L08-073

### Q-pattern-03 · How much should be visible up front, and how much behind "more"? · Expert
- **Why:** Progressive disclosure gives calmer, shorter screens; everything-visible reads powerful but dense [DC-L13-03].
- **Ask:** "Show primary options up front and advanced ones behind a clearly labeled trigger, at most two levels deep?"
- **Example:** Show a settings page with an "Advanced" section collapsed and expanded.
- **Control:** single choice
- **Options:**
  - `all-visible` Everything visible [DC-L13-03].
  - `progressive` Progressive disclosure, at most two levels, trigger label says what is behind it [S-L13-063].
  - `staged` Staged disclosure (wizard or stepper), for independent steps only [S-L13-063].
  - `contextual` Contextual reveal on hover or selection [DC-L13-03].
- **Default:** progressive. *Source:* card heuristic [DC-L13-03].
- **Decides:** DC-L13-03
- **Changes:** none downstream in the graph · blocks: Patterns > Information density > Disclosure
- **Preview:** the settings page per option.
- **Use / avoid:** use steppers that show position and total; avoid more than two disclosure levels (a lint warning) [DC-L13-03; L13 E1].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L13-03; S-L13-019, S-L13-030, S-L13-063

### Q-pattern-04 · How should empty states and first-time use work? · Standard
- **Why:** A designed empty state teaches and invites; a blank area looks broken; forced tours add friction up front [DC-L13-10, DC-L13-11].
- **Ask:** "Designed empty states with a next step, and contextual tips instead of a forced tour?"
- **Example:** Show a first-use empty project list, a no-results search and a tour with a skip button.
- **Control:** single choice (onboarding) + checklist (empty-state kinds)
- **Options:**
  - `empty-kinds` Empty states for first use, user-cleared, no results, no permission or error (Primer Blankslate, Spectrum IllustratedMessage, shadcn Empty) [DC-L13-10; S-L08-012, S-L08-015, S-L08-018].
  - `onboarding-none` No onboarding: a self-evident UI (NN/g's first recommendation) [S-L13-070].
  - `onboarding-contextual` Contextual help and empty-state guidance at the moment of need [S-L13-070].
  - `walkthrough` Interactive walkthrough, only for genuinely new, complex interfaces [S-L13-070].
- **Default:** every collection gets empty variants that state status, help learning and give a direct action; contextual onboarding; everything skippable. *Source:* card heuristics [DC-L13-10, DC-L13-11; S-L13-069, S-L13-070].
- **Decides:** DC-L13-10, DC-L13-11
- **Changes:** none downstream in the graph · blocks: Patterns > States > Empty; Patterns > Guidance > Onboarding
- **Preview:** each empty-state kind with the illustration choice from Q-img-04.
- **Use / avoid:** use an empty state on every collection (missing one is a lint warning); avoid tours without a skip control [DC-L13-10, DC-L13-11; L13 E1].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L13-10, DC-L13-11; S-L13-069, S-L13-070, S-L08-012, S-L08-015

### Q-pattern-05 · Which deceptive patterns should the builder block? · Standard
- **Why:** Ethical defaults give accept and decline equal visual weight, leave opt-ins unchecked and keep decline copy neutral [DC-L13-15].
- **Ask:** "Block the deceptive patterns a machine can detect, like pre-checked marketing boxes and consent buttons with unequal emphasis?"
- **Example:** Show a consent dialog with equal buttons vs a "confirmshaming" one, flagged.
- **Control:** single choice
- **Options:**
  - `none` No policy [DC-L13-15].
  - `documented` Documented policy against the 16 types at deceptive.design (sneaking, forced action, hard to cancel, preselection, fake urgency, confirmshaming ...) [S-L13-071].
  - `enforced` Documented and enforced where detectable: pre-checked consent or marketing boxes and unequal accept/reject emphasis are lint errors; re-prompting after dismissal is flagged [S-L13-071, S-L13-108].
- **Default:** enforced. *Source:* card heuristic [DC-L13-15]; L13 E1 lint errors.
- **Decides:** DC-L13-15
- **Changes:** DC-L13-16 · blocks: Principles > Ethics > Deceptive patterns
- **Preview:** a consent dialog and a cancellation flow checked live.
- **Use / avoid:** use equal emphasis for accept and reject; avoid nagging and fake urgency (the Zeigarnik effect does not justify nags) [DC-L13-15; L13 E2].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L13-15; S-L13-071, S-L13-108, S-L13-110

### Q-pattern-06 · What should appear on glanceable surfaces (widgets, tiles, complications)? · Expert
- **Show if:** Q-plat-02 marks watch or car first-class, or the product ships widgets
- **Why:** Glance surfaces look like data, not UI: big numerals, one metric, a status color, almost no chrome [DC-L14-07].
- **Ask:** "What single number or status should people see without opening the app?"
- **Example:** Ask for the one metric; show it as a watch complication and a home-screen widget.
- **Control:** text (metric) + single choice (surfaces)
- **Options:**
  - `priority-matrix` Complication = one datum, notification = urgent event, tile = one or two items, app = everything (Google) [S-L14-015].
  - `apple-surfaces` Complications, Smart Stack, Live Activities, CarPlay widgets [S-L14-001, S-L14-047].
- **Default:** design the complication or tile first, then the app; one number or status per glance. *Source:* card heuristic [DC-L14-07].
- **Decides:** DC-L14-07
- **Changes:** none downstream in the graph · blocks: Patterns > Surfaces > Glanceable
- **Preview:** the metric on each glance surface.
- **Use / avoid:** use tiles that are "immediate, predictable, relevant"; avoid shrinking app screens into widgets [S-L14-020; DC-L14-07].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L14-07; S-L14-001, S-L14-015, S-L14-020, S-L14-047
- **Merges:** D5

### Q-ai-01 · Does the product have AI features, and how should AI content be marked? · Standard
- **Why:** Clear AI identifiers and distinct citation styling make output read as "assistive, check me"; a distinct AI accent can compete with the primary action color [DC-L13-16, DC-L08-22].
- **Ask:** "Does the product generate content or act with AI? If so, how should AI content be labeled and corrected?"
- **Example:** Show an AI-generated summary with a label, citations, and Edit / Undo / Retry.
- **Control:** single choice + multi-select (surfaces)
- **Options:**
  - `none` No AI features.
  - `label-button` AI label plus an AI button variant (Carbon AI label; S2 `genai`; Atlassian Rovo) [S-L08-009, S-L08-067, S-L08-063].
  - `presence-mode` AI presence as a mode on normal components: label, explainability popover, glow tokens, revert (Carbon) [S-L14-058].
  - `chat` Chat components for conversational products (shadcn Message, Bubble; Carbon AI chat) [S-L08-018, S-L14-058].
  - `voice` Voice-only turns: one breath, 2-5 options (Alexa) [S-L14-065].
- **Default:** label-button as an optional module, chat only for conversational products; label AI content, place citations next to claims, express uncertainty in high-stakes contexts, and pair every generated output with Edit, Undo and Retry. *Source:* card heuristics [DC-L08-22, DC-L13-16, DC-L14-12; S-L13-089, S-L14-011].
- **Decides:** DC-L08-22, DC-L13-16, DC-L14-12
- **Changes:** DC-L05-18 (agent avatars) · blocks: Components > AI; Patterns > AI; Patterns > Conversational
- **Preview:** AI output in a table cell, a side panel and a chat thread.
- **Use / avoid:** use AI styling only on AI-generated content (Carbon warns against decoration); avoid human-sounding anthropomorphic framing and reasoning traces presented as explanations [DC-L14-12, DC-L13-16].
- **Skip:** yes, none.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L08-22, DC-L13-16, DC-L14-12; S-L08-009, S-L08-067, S-L13-089, S-L14-011, S-L14-058
- **Merges:** D6

---

## Stage 24 · Tokens and encoding
> Screen: a token browser beside the product preview; clicking any element shows its token chain (component, semantic, primitive) and the exported code for each platform. Graph step 0-5. Asked after the visual stages because nothing visual depends on it in the graph; everything here changes how the look is stored and shipped [inferred from the graph].

### Q-token-01 · How many token layers should sit between raw values and components? · Standard
- **Why:** A semantic layer lets the look change (rebrand, new mode) without touching components; 24 of 25 benchmarked systems have one [DC-L07-01; L09 A1 row 1].
- **Ask:** "Raw values, then semantic tokens, with component tokens only where a component must differ?"
- **Example:** Show `blue.600` -> `color.bg.accent` -> `button.primary.bg`, and which layer a rebrand edits.
- **Control:** single choice
- **Options:**
  - `one` One tier: palette and scales used directly (Tailwind); theming means find-and-replace [DC-L07-01].
  - `two-plus` Primitive -> semantic, component tokens only when needed (Atlassian, Polaris; Fluent global + alias) [S-L07-107, S-L07-125, S-L01-033].
  - `three-full` Primitive -> semantic -> component for every component (Material 3 comp tokens; Primer base/functional/component) [S-L07-102, S-L01-027].
- **Default:** two-plus: primitives private, semantics public, component tokens only for components a brand must restyle or values shared by 3+ components; typography as primitives, semantic composites `text.{role}.{size}` and optional component aliases. *Source:* card heuristics [DC-L07-01, DC-L07-02, DC-L01-26, DC-L02-27]; L09 counts this as its 3-tier default with the component tier optional.
- **Decides:** DC-L07-01, DC-L07-02, DC-L01-26, DC-L02-27
- **Changes:** DC-L07-04, DC-L07-18, DC-L07-19 · blocks: Tokens > Architecture > Tiers; Component tokens
- **Preview:** the token chain inspector on the preview.
- **Use / avoid:** use semantic tokens in every component; avoid components referencing a raw hex or px (L09: 24 of 25 systems forbid it) [L09 A1 row 1].
- **Skip:** yes.
- **Time weight:** medium (fan-out 4)
- **Evidence:** DC-L07-01, DC-L07-02, DC-L01-26, DC-L02-27; S-L07-003, S-L07-036, S-L07-108, S-L01-027
- **Merges:** K7.6 (tiers)

### Q-token-04 · Which units should the source use? · Expert
- **Why:** px maps cleanly to pt, dp and Figma; rem respects browser zoom; unitless numbers translate 1:1 across platforms [DC-L07-11, DC-L10-08].
- **Ask:** "Store plain px-style numbers and convert to rem for web text?"
- **Example:** Show `16` becoming `1rem`, `16pt`, `16dp` and `16px`.
- **Control:** single choice + toggle (spacing scales with text)
- **Options:**
  - `px-to-rem` px in source, rem at the web transform (DTCG allows px and rem only; Figma imports px) [S-L07-002, S-L07-011, S-L03-037].
  - `unitless` Unitless 4-based numbers emitted 1:1 as pt/dp/epx/px, rem for web font sizes (Fluent's ramp) [S-L10-039].
  - `rem-source` rem in source, converted down to dp/sp/CGFloat by transforms [DC-L10-08].
- **Default:** px-to-rem (equivalently unitless numbers), rem for web type and breakpoints; "spacing scales with text size" is an explicit toggle, off by default; line height unitless. *Source:* card heuristics [DC-L07-11, DC-L10-08, DC-L03-26].
- **Decides:** DC-L07-11, DC-L10-08, DC-L03-26
- **Changes:** DC-L10-22 · blocks: Tokens > Types > Dimension; Encoding > Units per platform
- **Preview:** one value converted per platform.
- **Use / avoid:** question any value not divisible by 4 (except 2, 6, 10 for icon nudges); avoid sp or rem for spacing that must not scale with text on Android [DC-L10-08; L10 baked-in rule 4].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L07-11, DC-L10-08, DC-L03-26; S-L03-037, S-L03-038, S-L07-002, S-L10-039, S-L10-070
- **Merges:** P9

### Q-token-08 · Which file format and build pipeline should produce platform code? · Expert
- **Why:** The pipeline decides whether tokens arrive in each codebase in the idiom it already uses [DC-L07-25, DC-L10-22].
- **Ask:** "Export DTCG 2025.10 files with a resolver, built with Terrazzo for web or Style Dictionary for native?"
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
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L07-09, DC-L07-25, DC-L10-22, DC-L10-18; S-L07-002, S-L07-004, S-L07-155, S-L07-179, S-L10-056
- **Merges:** P19, P23

### Q-token-02 · How should tokens be named? · Expert
- **Why:** Names are the shared vocabulary for humans and agents; only include the levels needed to tell tokens apart [DC-L07-04; S-L07-036].
- **Ask:** "Use `namespace.category.property.variant.state` for semantic tokens, hue plus step for colors, and a short prefix only in code output?"
- **Example:** Show `ds.color.bg.accent.hover`, `space.200`, and `--ds-color-bg-accent-hover` in CSS.
- **Control:** grammar builder + text (prefix)
- **Options:**
  - `grammar` Semantic grammar `[namespace].category.property.concept?.variant?.state?`; component grammar `[namespace].component.element?.property.variant?.state?` [DC-L07-04].
  - `primitives` Primitives: hue + numeric step (50-950 or bounded 0-100); descriptive names only for brand colors [DC-L07-03].
  - `spacing-names` Spacing primitives as percent of base (`space.200` = 16px, Atlassian, Material), semantic spacing by role [S-L03-003, S-L03-030].
  - `prefix` A 2-4 letter prefix in platform output only (`--ds-`, `--cds-`, `--md-`); theme and brand never in names [S-L07-036, S-L07-108].
  - `casing` Lowercase JSON segments; kebab for CSS, camel for JS/Swift/Kotlin, snake for Android XML [S-L07-158].
- **Default:** all five as listed. *Source:* card heuristics [DC-L07-03, DC-L07-04, DC-L07-05, DC-L07-06, DC-L03-03].
- **Decides:** DC-L07-03, DC-L07-04, DC-L07-05, DC-L07-06, DC-L03-03
- **Changes:** DC-L07-20 · blocks: Tokens > Naming
- **Preview:** a name linter that shows each token's name in JSON, CSS, Swift and Kotlin.
- **Use / avoid:** use role names at the semantic tier; avoid `padding` or `margin` in primitive names and ordinal scales that look proportional but aren't [DC-L03-03].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L07-03, DC-L07-04, DC-L07-05, DC-L07-06, DC-L03-03; S-L07-003, S-L07-036, S-L07-158
- **Merges:** K7.6

### Q-token-03 · Which properties become tokens? · Expert
- **Why:** Anything left untokenized drifts and cannot be linted or themed [DC-L07-07].
- **Ask:** "Tokenize every property Figma can bind and lint, plus motion and focus?"
- **Example:** Show the coverage list with counts per category.
- **Control:** single choice + checklist
- **Options:**
  - `minimal` Color, type, space [DC-L07-07].
  - `standard` Plus radius, border width, shadow/elevation, opacity, motion [DC-L07-07].
  - `extended` Plus z-index, breakpoints, icon sizes, touch targets, data-viz palettes [DC-L07-07; S-L07-036].
- **Default:** extended; one-off illustration values stay untokenized. *Source:* card heuristic [DC-L07-07].
- **Decides:** DC-L07-07
- **Changes:** none downstream in the graph · blocks: Tokens > Scope > Coverage
- **Preview:** a coverage bar per category.
- **Use / avoid:** use tokens for anything a lint rule should check; avoid tokenizing one-off art values [DC-L07-07].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L07-07; S-L07-002, S-L07-036, S-L07-108

### Q-token-05 · How should composite values (type, shadows, motion) be encoded? · Expert
- **Why:** Composites keep a style whole for code; bound variables let styles switch with modes in Figma; DTCG has no spring type [DC-L07-12, DC-L07-13, DC-L07-14, DC-L04-28].
- **Ask:** "Atomic primitives plus semantic composites, Figma styles bound to variables, and springs stored as extensions?"
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
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L07-12, DC-L07-13, DC-L07-14, DC-L04-28, DC-L02-28; S-L07-002, S-L07-013, S-L07-019, S-L07-033

### Q-token-06 · How should themes and modes be structured so combinations don't explode? · Expert
- **Why:** Each axis multiplies QA; if two axes set the same token they should be one axis [DC-L07-17].
- **Ask:** "At most three independent axes, with high contrast as a layered override, and one Figma collection per axis?"
- **Example:** Show 2 schemes x 2 contrasts x 2 densities as additive collections instead of 8 flattened modes.
- **Control:** single choice
- **Options:**
  - `flatten` Flatten into one axis (the DTCG resolver example: light, lightHighContrast, dark, darkHighContrast) [S-L07-004].
  - `orthogonal` Orthogonal axes, each touching a disjoint set of tokens [DC-L07-17].
  - `collections` Figma: Primitives (hidden) + Semantic color + Semantic dimension (density or breakpoint) + Motion with a reduced mode [DC-L07-18].
  - `breakpoint-collection` A Breakpoint collection with 3 modes driving layout variables; grid auto layout for multi-column components [DC-L07-28; S-L07-024].
- **Default:** orthogonal with at most 3 axes plus collections and a breakpoint collection. *Source:* card heuristics [DC-L07-17, DC-L07-18, DC-L07-28].
- **Decides:** DC-L07-17, DC-L07-18, DC-L07-28
- **Changes:** none downstream in the graph · blocks: Tokens > Theming > Combinations; Figma > Variables > Collections; Tokens > Layout
- **Preview:** the combination count and the Figma mode budget from Q-tool-03.
- **Use / avoid:** use additive collections to stay within the plan's mode limit; avoid putting brand and scheme in one flattened axis [DC-L07-18, DC-L07-27].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L07-17, DC-L07-18, DC-L07-28; S-L07-004, S-L07-011, S-L07-014, S-L07-024

### Q-token-07 · How should the Figma library be kept clean? · Expert
- **Show if:** Q-tool-03 is a Figma plan
- **Why:** Hidden primitives and precise scopes keep designers on semantic tokens; generated code syntax keeps Figma and code names identical [DC-L07-19, DC-L07-20].
- **Ask:** "Hide primitives, scope every variable to its property, and generate code names automatically?"
- **Example:** Show a text-color variable offered only in text fill pickers.
- **Control:** toggles
- **Options:**
  - `hide-scope` Hide primitives from publishing; scope each semantic variable to the properties its name says [S-L07-018, S-L07-025].
  - `code-syntax` Generate Web, Android and iOS code syntax from the pipeline's name transform [S-L07-018].
  - `vars-styles` Variables for values, styles for bundles [S-L07-019].
  - `check-designs` Run Check designs before "Ready for dev" and review library analytics quarterly (Org/Enterprise; the builder lints on Professional) [S-L07-025, S-L07-029].
- **Default:** all four. *Source:* card heuristics [DC-L07-19, DC-L07-20, DC-L07-21, DC-L07-26].
- **Decides:** DC-L07-19, DC-L07-20, DC-L07-21, DC-L07-26
- **Changes:** DC-L07-23 · blocks: Figma > Variables > Scope; Code syntax; Styles vs Variables; Governance > Tooling
- **Preview:** the Figma variable panel as a designer would see it.
- **Use / avoid:** use scopes so a spacing token cannot be picked for a color; avoid "show in all" scopes [DC-L07-19].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L07-19, DC-L07-20, DC-L07-21, DC-L07-26; S-L07-018, S-L07-019, S-L07-025, S-L07-029

### Q-token-09 · How should tokens be described and retired? · Expert
- **Why:** Descriptions tell people and agents what a token is for; deprecating before deleting protects consumers [DC-L07-23].
- **Ask:** "Give every semantic token a one-line description, and deprecate for one release before deleting?"
- **Example:** Show `$deprecated: "Use color.bg.accent instead"` in JSON and the warning in Figma.
- **Control:** toggles
- **Options:**
  - `descriptions` `$description` on every semantic token [S-L07-002].
  - `deprecate` `$deprecated: true` or "Use X instead", one release before removal [S-L07-002].
  - `usage-check` Check library analytics before removal (Org/Enterprise) [S-L07-029].
- **Default:** all three. *Source:* card heuristic [DC-L07-23].
- **Decides:** DC-L07-23
- **Changes:** DC-L11-15 · blocks: Tokens > Governance > Lifecycle
- **Preview:** a token's detail card with description and status.
- **Use / avoid:** use descriptions written for agents as well as people; avoid deleting tokens without a replacement [DC-L07-23].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L07-23; S-L07-002, S-L07-029, S-L07-031, S-L07-042

### Q-token-10 · Which inputs should re-skin the theme, and what may other brands or clients customize? · Expert
- **Show if:** Q-theme-03 is not locked
- **Why:** Fewer inputs give more consistent, always-accessible themes but less nuance (Linear replaced 98 per-theme variables with 3 inputs); white-label customization almost always centers on color and typography [DC-L06-06, DC-L06-17; S-L06-012, S-L06-053].
- **Ask:** "Let clients set brand color and logo, and allow font and radius only with previews and validation?"
- **Example:** Show a client admin panel with a color picker, logo upload and a live contrast check.
- **Control:** multi-select (knobs) + single choice (surface)
- **Options:**
  - `inputs-3` Three generator inputs: brand color, neutral base or temperature, contrast (Linear) [S-L06-012; DC-L06-06].
  - `inputs-seed-variant` One source color plus a scheme variant and contrast level (Material) [S-L06-082, S-L06-083].
  - `code-one-color` One brand color in code (Blade `createTheme({brandColor})`) [S-L06-094].
  - `admin-ui` Admin UI "clicks, not code" for colors, logos, images and curated accents (Salesforce SLDS 2) [S-L06-068].
  - `user-builder` A user-facing theme builder (Linear base/accent/contrast) [S-L06-012].
  - `cms` CMS-editable overrides [S-L06-053].
- **Default:** three generator inputs; clients may change brand color and logo, font and radius only with previews and validation. *Source:* card heuristics [DC-L06-06, DC-L06-17].
- **Decides:** DC-L06-06, DC-L06-17
- **Changes:** none downstream in the graph · blocks: Tokens > Theming > White-label controls
- **Preview:** the client panel re-skinning the preview with contrast re-checked.
- **Use / avoid:** use generated on-colors so client colors keep contrast; avoid exposing raw token editing to clients [DC-L06-17, DC-L06-16].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L06-06, DC-L06-17; S-L06-012, S-L06-053, S-L06-067, S-L06-068, S-L06-094

---

## Stage 25 · Team, governance and change
> Screen: a governance plan generated from earlier answers (team size, scope, platforms), shown as a one-page operating model the person edits. Graph step 1-7. Mostly Expert: these decisions change how the system evolves, not how it looks.

### Q-gov-01 · How strict should the system be: can product teams override or extend it? · Standard
- **Why:** Strict systems stay consistent but feel rigid; loose ones allow experiments but drift; a strict core with loose edges is the practical middle [DC-L11-03].
- **Ask:** "Strict core (tokens, primitives, accessibility), with product teams free to build their own patterns on top?"
- **Example:** Show which layers are locked and which are open under each option.
- **Control:** single choice
- **Options:**
  - `strict` Strict: comprehensive docs, design and code fully synced, little deviation [S-L11-018, S-L11-019].
  - `loose` Loose: a framework with room to experiment [S-L11-019].
  - `canon-expanded` Strict canon plus product-owned "expanded universe" extensions (Dan Mall) [S-L11-014].
- **Default:** strict core (tokens, primitives, accessibility behavior), loose edges (patterns, marketing). *Source:* card heuristic [DC-L11-03].
- **Decides:** DC-L11-03
- **Changes:** DC-L11-11, DC-L11-12, DC-L11-24 (lint strictness) · blocks: Strategy > Posture
- **Preview:** a layer diagram with lock icons per layer.
- **Use / avoid:** use a snowflake path for one-off needs; avoid forcing every product-specific component into the core [DC-L11-03, DC-L11-12].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L11-03; S-L11-014, S-L11-018, S-L11-019
- **Merges:** K6.5, K8.4

### Q-gov-02 · In what order will you build, pilot and roll out? · Expert
- **Why:** Foundations-first is tidy but abstract; pilot-driven work keeps components real; a big-bang launch creates a moment but risks pilot bias [DC-L11-06, DC-L11-07, DC-L11-08].
- **Ask:** "Minimal foundations first, then components proven in one pilot product, rolled out incrementally?"
- **Example:** Show Dan Mall's 8-criteria pilot scorecard filled for two candidate products.
- **Control:** single choice (order) + scorecard (pilot) + single choice (rollout)
- **Options:**
  - `foundations-first` Foundations first: spacing, color, type, elevation, icons, then components (Figma course order) [S-L11-009].
  - `pilot-driven` Pilot-driven: extract components from a real product, apply to the next [S-L11-014].
  - `pilot-scorecard` Score pilots on common components, common patterns, high-value elements, feasibility, a champion, a 3-4 week scope, independence from legacy, marketing potential [S-L11-105].
  - `rollout-incremental` Incremental rollout led by pain points; big-bang only with a rebrand [S-L11-105].
- **Default:** minimal foundations first, then pilot-driven components, incremental rollout. *Source:* card heuristics [DC-L11-06, DC-L11-07, DC-L11-08].
- **Decides:** DC-L11-06, DC-L11-07, DC-L11-08
- **Changes:** DC-L11-01, DC-L11-22 · blocks: Process > Build order; Process > Pilot; Adoption > Rollout
- **Preview:** a timeline of the plan.
- **Use / avoid:** use a second pilot from a different product family to reduce bias; avoid building components no pilot needs [DC-L11-07].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L11-06, DC-L11-07, DC-L11-08; S-L11-009, S-L11-014, S-L11-105, S-L11-107
- **Merges:** K2.7, K2.8, K13.1

### Q-gov-03 · Who can contribute, and how are decisions made and recorded? · Expert
- **Why:** Only 36% of teams are satisfied with their contribution process; decision records explain why things are the way they are [DC-L11-11, DC-L11-12; S-L11-030].
- **Ask:** "A fast lane for fixes and icons, a proposal lane for new components, and every foundation decision logged as a decision record?"
- **Example:** Show a decision record generated from one of this session's answers.
- **Control:** single choice (contribution) + toggle (decision records)
- **Options:**
  - `closed` Closed or narrow: fixes and small enhancements only (Atlassian) [S-L11-024].
  - `criteria-gated` Open but gated: proposals must be useful and unique; publication must be usable, consistent, versatile (GOV.UK) [S-L11-021].
  - `two-lanes` A fast lane for fixes, icons and docs; an RFC lane for new components [S-L11-020, S-L11-021].
  - `frost-flow` Brad Frost's 10-step governance flow with a snowflake path [S-L11-003].
  - `adrs` Decision records (ADRs) from day one; this questionnaire's answers map to them [S-L11-095; inferred].
- **Default:** two-lanes, frost-flow and adrs. *Source:* card heuristics [DC-L11-11, DC-L11-12].
- **Decides:** DC-L11-11, DC-L11-12
- **Changes:** DC-L11-13 · blocks: Governance > Contribution; Governance > Process
- **Preview:** the generated decision log.
- **Use / avoid:** record why an option was chosen and what it beat; avoid undocumented overrides [DC-L11-12].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L11-11, DC-L11-12; S-L11-003, S-L11-020, S-L11-021, S-L11-024, S-L11-095
- **Merges:** K9.4, K9.5, K9.6, K9.7

### Q-gov-04 · How are components labeled, versioned and retired? · Expert
- **Why:** Predictable status and versioning protect consumers; breaking changes without notice erode trust [DC-L11-13, DC-L11-14, DC-L11-15].
- **Ask:** "Three statuses (experimental, ready, deprecated), one semver for the library, and deprecations removed only in the next major with a migration guide?"
- **Example:** Show a changelog entry with a deprecation and its codemod.
- **Control:** single choice per item
- **Options:**
  - `status-3` Experimental > Ready > Deprecated (Primer simplified from five to three) [S-L11-025, S-L11-026].
  - `semver-library` One SemVer for the whole library while small; per-package once multi-platform [S-L11-106, S-L11-028].
  - `per-component` Per-component versions (Atlassian, Paste) [S-L11-028].
  - `deprecation-polaris` Deprecate in a minor, announce with `@deprecated` and warnings, ship codemods, remove in the next major (Polaris) [S-L11-100].
- **Default:** status-3, semver-library, deprecation-polaris with at least one release cycle of notice; release notes every release (the most common ritual, 56%). *Source:* card heuristics [DC-L11-13, DC-L11-14, DC-L11-15; S-L11-030].
- **Decides:** DC-L11-13, DC-L11-14, DC-L11-15
- **Changes:** DC-L11-22 · blocks: Governance > Component status; Change > Versioning; Change > Deprecation
- **Preview:** status badges in the catalog and a sample changelog.
- **Use / avoid:** pair every removal with a migration path; avoid breaking changes in minor releases [DC-L11-14, DC-L11-15].
- **Skip:** yes.
- **Time weight:** medium (fan-out 2)
- **Evidence:** DC-L11-13, DC-L11-14, DC-L11-15; S-L11-025, S-L11-028, S-L11-100, S-L11-106
- **Merges:** K8.5, K10.2, K10.3, K10.4

### Q-gov-05 · What problem is the system solving, and how will you know it worked? · Expert
- **Why:** The problem sets the success metric; most teams measure adoption, but only 5% measure ROI [DC-L11-20; S-L11-030].
- **Ask:** "What hurts most today, and should we track design adoption, code adoption and a quarterly satisfaction survey?"
- **Example:** Show an adoption dashboard mock with the three starting metrics.
- **Control:** multi-select (pain) + multi-select (metrics)
- **Options:**
  - `pain` Pain: inconsistency, speed, accessibility, rebrand, AI output drift, multi-platform parity [S-L11-083].
  - `adoption` Design adoption (Figma analytics) and code adoption (a scanner such as Omlet or react-scanner) [S-L11-035, S-L11-037, S-L11-039].
  - `satisfaction` A quarterly satisfaction survey [S-L11-030].
  - `maturity` Maturity stage: building v1, growing adoption, surviving the teenage years, evolving (Sparkbox) [S-L11-033].
- **Default:** design adoption, code adoption and a quarterly survey; most builder users are at stage 1. *Source:* card heuristics [DC-L11-20, DC-L11-21].
- **Decides:** DC-L11-20, DC-L11-21
- **Changes:** none downstream in the graph · blocks: Measurement > Metrics; Measurement > Maturity
- **Preview:** the metrics dashboard mock.
- **Use / avoid:** add speed or ROI studies only when leadership asks; avoid vanity counts of components [DC-L11-20].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L11-20, DC-L11-21; S-L11-030, S-L11-033, S-L11-035, S-L11-037, S-L11-083
- **Merges:** K0.1, K0.2, K0.3, K1.3, K12.1, K12.2, K12.3, K12.4

### Q-gov-06 · How will you announce the system and communicate changes? · Expert
- **Why:** Only 39% of teams are satisfied with how design-system changes are communicated [DC-L11-22; S-L11-030].
- **Ask:** "Release notes every release, a public roadmap and a support channel to start?"
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
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L11-22; S-L11-002, S-L11-030, S-L11-105
- **Merges:** K0.4, K13.3, K13.4

### Q-gov-07 · Which assistive technologies must be tested on each device class, and who owns accessibility? · Expert
- **Why:** Automated tools find only about 30% of issues; if a device class is first-class, its assistive technology is too [DC-L14-14; S-L11-093].
- **Ask:** "Test one screen reader, one motor alternative and the largest text size on each device class you ship?"
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
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L14-14; S-L10-072, S-L11-093, S-L14-007, S-L14-079, S-L14-080
- **Merges:** K4.3, K4.5, D7

---

## Stage 26 · Output, documentation and AI channels
> Screen: the export menu and a preview of every file the builder will produce: tokens, code, docs pages, DESIGN.md, lint rules. Graph step 2-4. These outputs are what keep the system coherent in later sessions and explainable to a team (BRIEF requirements 9 and 10).

### Q-dist-01 · How should the system leave the builder? · Standard
- **Why:** Engineers need the output in the form they already use: a snippet, a CLI install, a token file, a pull request, or a design file [DC-L16-12].
- **Ask:** "Export as CSS, a CLI install URL, DTCG files, a pull request, and a push to Figma or Paper?"
- **Example:** Show the export menu with one command per channel (for example `npx shadcn@latest add <url>`).
- **Control:** multi-select
- **Options:**
  - `copy-css` Copy snippets (Radix "Copy Theme", Utopia CSS) [S-L16-323, S-L16-341].
  - `cli-url` CLI install from a URL (tweakcn via shadcn) [S-L16-333, S-L16-328].
  - `dtcg` Token files (Leonardo "Copy Tokens") [S-L16-338].
  - `pr` A pull request to the repository [DC-L16-12].
  - `design-push` Push to Figma or Paper through MCP [S-L16-002, S-L16-020].
  - `mcp-tool` Expose the builder's generator as an MCP tool (Leonardo's example) [S-L16-338].
- **Default:** all six from one menu. *Source:* card heuristic [DC-L16-12].
- **Decides:** DC-L16-12
- **Changes:** none downstream in the graph · blocks: Builder > Output > Channels
- **Preview:** the export menu and file tree.
- **Use / avoid:** use one canonical source for every channel (Q-tool-01); avoid channels that fork the source [DC-L16-02].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L16-12; S-L16-002, S-L16-323, S-L16-333, S-L16-338

### Q-dist-04 · Where do docs live, and what goes on each component page? · Expert
- **Why:** Docs are how teams learn when and when not to use each piece; the shared core is usage guidance, live examples, API and accessibility [DC-L11-17, DC-L11-18; L09 A1 row 9].
- **Ask:** "Generate a docs site with a page per component (usage, when not to use, live example, props, accessibility, changelog), plus a machine-readable twin?"
- **Example:** Show the generated Button page.
- **Control:** single choice (platform) + template editor
- **Options:**
  - `figma-storybook` Figma plus Storybook (69% and 61% of teams) [S-L11-030].
  - `docs-platform` A docs platform (zeroheight, Supernova) when non-engineers author [S-L11-088].
  - `custom-site` A custom site (Material, Carbon) [S-L11-088].
  - `carbon-template` Page template: live demo, accessibility status, when to use and not, anatomy, content rules, behaviors, per-variant guidance (Carbon Usage tab; M3 Overview/Specs/Guidelines/Accessibility) [S-L11-090, S-L08-033].
- **Default:** a generated site with the Carbon-style template plus "when not to use" and a changelog, and an llms.txt or MCP twin; docs complete is part of "done". *Source:* card heuristics [DC-L11-17, DC-L11-18, DC-L08-23].
- **Decides:** DC-L11-17, DC-L11-18, DC-L08-23
- **Changes:** none downstream in the graph · blocks: Docs > Platform; Docs > Component page
- **Preview:** a generated component page.
- **Use / avoid:** use generated "use it for / avoid it for" notes from this questionnaire on every page; avoid docs that repeat props without guidance [DC-L11-18].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L11-17, DC-L11-18, DC-L08-23; S-L11-030, S-L11-088, S-L11-090, S-L08-033
- **Merges:** K11.1, K11.2, K11.3

### Q-dist-02 · How should AI coding tools read the system? · Standard
- **Why:** 59% of teams report UI bypassing their design system; agent channels make generated UI follow it [DC-L11-23; S-L11-031].
- **Ask:** "Ship an MCP server plus a DESIGN.md and token files, so Claude, ChatGPT, Codex or Cursor build with your system?"
- **Example:** Show a DESIGN.md excerpt and an agent's generated button using the tokens.
- **Control:** multi-select
- **Options:**
  - `mcp` An MCP server (Figma MCP at mcp.figma.com; Storybook MCP; shadcn MCP) [S-L11-041, S-L11-044, S-L11-045].
  - `design-md` DESIGN.md plus DTCG files [S-L11-047].
  - `llms-txt` llms.txt and Markdown twins of docs (Cloudscape, Geist) [S-L11-048; L09 A1 row 10].
  - `rules` Agent rules files (from Figma's `create_design_system_rules`) [S-L11-041].
  - `registry` A component registry (shadcn) [S-L11-045].
- **Default:** at least one live channel (MCP) and one file channel (DESIGN.md + DTCG), guidelines as many short structured files. *Source:* card heuristic [DC-L11-23]; L09 shared pattern row 10 (12 of 25 systems).
- **Decides:** DC-L11-23
- **Changes:** DC-L11-24 · blocks: Distribution > Agent context
- **Preview:** the agent-facing files and a sample agent answer.
- **Use / avoid:** use evals to check agents follow the files; avoid assuming docs changes alone steer agents [DC-L11-23; S-L11-108].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L11-23; S-L11-031, S-L11-041, S-L11-045, S-L11-047, S-L11-108
- **Merges:** K11.4, K11.5

### Q-dist-03 · How should the system check that people and agents follow it? · Standard
- **Why:** Linting and structured docs cut accessibility violations per iteration from 5.1 to 0.6 when agents built with a design system (Sanity evals) [DC-L11-24; L13 E3].
- **Ask:** "Export lint rules with the tokens, so every generated screen is checked against the system?"
- **Example:** Show a lint result: "raw hex #3b82f6, use color.bg.accent".
- **Control:** multi-select (pre-filled from Q-gov-01 and Q-pref-01)
- **Options:**
  - `lint-rules` Lint rules exported alongside tokens, including the behavior rules (target size, labels, one primary) [DC-L11-24; L13 E3].
  - `adherence-scan` Adherence scanning for raw colors and custom components (Lovable) [S-L11-053].
  - `drift-audit` Drift detection at the docs layer (zeroheight MCP) [S-L11-104].
  - `evals` Evals that measure agent conformance [S-L11-108].
- **Default:** lint-rules plus evals. *Source:* card heuristic [DC-L11-24].
- **Decides:** DC-L11-24
- **Changes:** none downstream in the graph · blocks: Governance > AI guardrails
- **Preview:** the lint report for the preview screen.
- **Use / avoid:** use lint errors for Tier A rules and warnings for context-dependent ones (L13 E1); avoid automating the misapplied laws in L13 E2 (no seven-item caps) [L13 E1, E2].
- **Skip:** yes.
- **Time weight:** low (fan-out 1)
- **Evidence:** DC-L11-24; S-L11-053, S-L11-104, S-L11-108, S-L00-036
- **Merges:** K11.6

---

## Stage 27 · Builder preferences
> Screen: how the builder (or the interviewing model) behaves while the person keeps editing. Graph step 0-5. Can be changed at any time.

### Q-pref-01 · How strict should the builder's critique be? · Standard
- **Why:** Messages that name the principle teach the vocabulary; strict mode blocks export on hard failures [DC-L15-11; S-L15-070].
- **Ask:** "Should I coach with inline tips, stay silent, or block export on hard failures like contrast?"
- **Example:** Show one coach message: "Two primary buttons in this group; make one secondary."
- **Control:** single choice
- **Options:**
  - `silent` Silent: only automatic rules apply [DC-L15-11].
  - `coach` Coach: inline messages tied to a goal, each with a one-click fix (NN/g goal-linked critique) [S-L15-075].
  - `strict` Strict: block export on contrast, multiple primaries and undersized targets; warn on the rest [DC-L15-11].
  - `metrics` Plus a metrics panel (complexity and colorfulness scores) [S-L15-047].
- **Default:** coach for engineers exploring; strict for teams shipping to production. *Source:* card heuristic [DC-L15-11].
- **Decides:** DC-L15-11
- **Changes:** DC-L11-24 lint severity · blocks: Builder > Guidance > Feedback mode
- **Preview:** the preview screen with messages at each level.
- **Use / avoid:** accessibility failures are at least warnings in every mode; avoid silent mode for production exports [DC-L15-11].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
- **Evidence:** DC-L15-11; S-L15-047, S-L15-070, S-L15-075, S-L15-080

### Q-pref-02 · How should AI edits and variations work? · Expert
- **Why:** Deterministic human edits keep control; agent edits as reviewable patches keep trust; lock-and-shuffle explores without losing what you like [DC-L16-04, DC-L16-05].
- **Ask:** "Apply your edits instantly, show my suggestions as before/after patches, and let you lock values and shuffle the rest?"
- **Example:** Show a "show 6 variations" grid with two locked parameters.
- **Control:** toggles
- **Options:**
  - `patches` Agent edits arrive as reviewable patches with before/after previews [DC-L16-04].
  - `staged` Direct edits staged and committed together (Figma Make) [S-L16-026].
  - `lock-shuffle` Lock + Shuffle on every parameter (shadcn create, Realtime Colors) [S-L16-327, S-L16-335].
  - `show-6` A "show 6" grid of variants rendered on the same specimen [DC-L16-05].
- **Default:** patches, lock-shuffle and show-6; vary only what is not locked. *Source:* card heuristics [DC-L16-04, DC-L16-05].
- **Decides:** DC-L16-04, DC-L16-05
- **Changes:** none downstream in the graph · blocks: Builder > AI > Edit model; Builder > Exploration > Variation
- **Preview:** the variation grid.
- **Use / avoid:** use variations for open, taste-driven questions (color, type, radius); avoid shuffling locked or accessibility-bound values [DC-L16-05].
- **Skip:** yes.
- **Time weight:** medium (fan-out 3)
- **Evidence:** DC-L16-04, DC-L16-05; S-L16-026, S-L16-031, S-L16-327, S-L16-335

### Q-pref-03 · Should the builder apply optical corrections automatically? · Expert
- **Why:** Geometric values can look wrong (a circle looks smaller than a square of the same box); known corrections have formulas [DC-L15-10; S-L15-058].
- **Ask:** "Auto-correct known optical cases like icon sizing and nested corners, and only suggest fixes for custom assets?"
- **Example:** Show a circle icon at 100% vs 112.84% of a square's box.
- **Control:** single choice
- **Options:**
  - `geometric` Geometric only: exact values [DC-L15-10].
  - `auto-known` Auto-correct known cases: area-matched shapes (circle 112.84%), Material keylines, centroid centering, concentric nested radii [S-L15-058, S-L15-059].
  - `suggest` Suggest only [DC-L15-10].
- **Default:** auto-known for generated assets, suggest for custom assets. *Source:* card heuristic [DC-L15-10].
- **Decides:** DC-L15-10
- **Changes:** none downstream in the graph · blocks: Foundations > Visual language > Polish
- **Preview:** before/after pairs for each correction.
- **Use / avoid:** use formulas where they exist; avoid correcting brand assets without approval [DC-L15-10].
- **Skip:** yes.
- **Time weight:** low (fan-out 0)
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

These L16 cards describe how the builder itself should work (for the builder spec, S2), not choices a person makes about their design system. They shaped the Preview lines in this file.

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

## Merge log

All 125 source questions were placed; none was dropped outright. The table lists where each went; the notes after it cover the judgment calls.

| Source | Where each question went |
|---|---|
| L11 kickoff (K, 77) | K0.1 Q-gov-05; K0.2 Q-gov-05; K0.3 Q-gov-05; K0.4 Q-gov-06; K0.5 Q-comp-01; K1.1 Q-scope-03, Q-aud-01; K1.2 Q-brand-07; K1.3 Q-gov-05; K1.4 Q-scope-04; K1.5 Q-scope-02; K1.6 Q-scope-02; K2.1 Q-scope-01; K2.2 Q-scope-01, Q-plat-01; K2.3 Q-plat-08; K2.4 Q-tool-03; K2.5 Q-tool-01; K2.6 Q-comp-01; K2.7 Q-gov-02; K2.8 Q-gov-02; K3.1 Q-brand-03; K3.2 Q-brand-07; K3.3 Q-ref-01, Q-brand-01, Q-brand-02; K3.4 Q-color-01, Q-color-09; K3.5 Q-type-01, Q-type-02; K3.6 Q-voice-01; K4.1 Q-aud-03; K4.2 Q-aud-03; K4.3 Q-gov-07; K4.4 Q-aud-04, Q-type-17, Q-motion-10; K4.5 Q-gov-07; K5.1 Q-type-04; K5.2 Q-type-04; K5.3 Q-voice-06; K5.4 Q-voice-06; K5.5 Q-voice-06; K6.1 Q-theme-01; K6.2 Q-theme-03; K6.3 Q-dir-02, Q-theme-02, Q-space-09; K6.4 Q-theme-02; K6.5 Q-gov-01; K7.1 Q-color-01; K7.2 Q-type-08; K7.3 Q-space-01; K7.4 Q-shape-01, Q-motion-01; K7.5 Q-icon-01, Q-img-01, Q-img-04; K7.6 Q-token-01, Q-token-02; K8.1 Q-comp-02; K8.2 Q-comp-04; K8.3 Q-layout-04; K8.4 Q-gov-01; K8.5 Q-gov-04; K9.1 Q-scope-03; K9.2 Q-scope-04; K9.3 Q-scope-04; K9.4 Q-gov-03; K9.5 Q-gov-03; K9.6 Q-gov-03; K9.7 Q-gov-03; K10.1 Q-tool-02; K10.2 Q-gov-04; K10.3 Q-gov-04; K10.4 Q-gov-04; K10.5 Q-tool-01; K11.1 Q-dist-04; K11.2 Q-dist-04; K11.3 Q-dist-04; K11.4 Q-dist-02; K11.5 Q-dist-02; K11.6 Q-dist-03; K12.1 Q-gov-05; K12.2 Q-gov-05; K12.3 Q-gov-05; K12.4 Q-gov-05; K13.1 Q-gov-02; K13.2 Q-scope-04; K13.3 Q-gov-06; K13.4 Q-gov-06 |
| L06 brand (B, 15) | B1 Q-aud-01, Q-aud-02; B2 Q-aud-02; B3 Q-ref-01, Q-brand-02; B4 Q-brand-02; B5 Q-brand-01; B6 Q-brand-01; B7 Q-brand-03, Q-color-01, Q-type-02, Q-motion-08, Q-img-04; B8 Q-type-01; B9 Q-color-06; B10 Q-theme-03; B11 Q-scope-01, Q-brand-05; B12 Q-brand-07; B13 Q-voice-01, Q-voice-02; B14 Q-type-04; B15 Q-aud-03, Q-aud-04, Q-motion-07 |
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
| Q-voice-03 | Capitalization: sentence case everywhere (Microsoft, Atlassian) vs title-case headings (Mailchimp) vs per element (Apple) [DC-L06-20]. | Three options; sentence case by default. |

## Confidence and gaps

- **Confirmed from files:** every option value, system name and default comes from a card in `synthesis/cards.json` (refreshed 2026-09-23, 325 cards) or from L09's shared-pattern and divergence tables; card and source ids are cited inline. The ordering was validated against `synthesis/decision-graph.json` including S1c's `graph-overrides.json` (see `questionnaire.json` meta for the counts).
- **Inferred (tagged in place):** the Quick-mode selection and the choice to derive posture from slider G; the stage grouping of cards without graph links; accepted file formats in some asset hooks (sounds, animated assets); the time-weight rule; the Ask and Example prompts.
- **Not yet reconciled:** L17's block classification (`research/L17-how-systems-get-made.md`) was not written when this file was produced; when it lands, check that every block it marks "cannot generate" has an asset hook here.
