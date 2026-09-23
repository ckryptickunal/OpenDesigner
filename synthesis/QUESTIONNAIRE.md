# Guided decision flow: the builder's questionnaire (S1b)

This is the question flow at the core of the design-system builder. L11 found that no competitor walks a person through the decisions: tools generate a theme from a few inputs, host an existing system, or extract one [DC-L11-01; S-L11-071, S-L11-073]. This file lists every question the builder asks, in order, with the options, what each option does visually, and what it changes downstream.

`synthesis/questionnaire.json` holds the same content in machine-readable form. It is generated from this file by `tools`-free parsing (see "How to read an entry"), so edit this file first.

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

**Quick mode, in order:** Q-aud-01 (who uses it), Q-brand-01 (personality sliders), Q-plat-01 (platforms), Q-tool-01 (where the system lives), Q-color-01 (brand color input), Q-color-03 (where brand color appears), Q-type-01 (typeface posture), Q-shape-01 (corner softness), Q-depth-01 (how surfaces separate), Q-motion-01 (motion feel).

Why these ten: they combine the highest fan-out step-0 decisions in the graph (personality DC-L06-02 fans out to 15 decisions, platforms DC-L10-01 to 12, source of truth DC-L16-02 to 8) with the L09 divergence points that change the look most (shape, depth, surface color, density, typeface, color generation, motion) [L09 A2; DC-L09-01 to DC-L09-08]. Everything L09 found nearly every system shares is pre-filled instead of asked: a 3-tier token model, a 4px spacing base, neutral surfaces plus one accent plus status colors, 12-step ramps, 100-300 ms ease-out motion, light and dark modes, WCAG 2.2 AA [L09 A1 rows 1-12]. Platform posture (DC-L10-02, fan-out 9) is derived in Quick mode from the personality slider "Bold vs deferential" and shown as a confirm chip [inferred].

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
| Brand typeface files and license | Q-type-02 | 11 |
| Custom icon set | Q-icon-01 | 18 |
| App icon | Q-icon-06 | 18 |
| Photography | Q-img-01 | 19 |
| Illustration, characters, mascot | Q-img-04 | 19 |
| Animated assets (Lottie, 3D, animated icons) | Q-img-06 | 19 |
| UI sounds or sonic logo | Q-motion-08 | 17 |
| Existing voice and tone guide | Q-voice-01 | 21 |

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
- **Pre-answers:** Q-scope-02 (an existing product becomes the audit), Q-brand-01 and Q-brand-02 (reference placed on the personality map), Q-plat-01, Q-color-01 to Q-color-06, Q-color-10, Q-type-01, Q-type-03, Q-type-06, Q-space-01, Q-space-02, Q-space-04, Q-layout-01, Q-shape-01, Q-shape-02, Q-depth-01, Q-depth-02, Q-motion-01, Q-motion-02, Q-icon-02, Q-icon-03, Q-comp-01, Q-state-01, Q-form-01 [inferred mapping from what each reference type exposes].
- **Preview:** an "extracted from reference" card listing each found value next to the question it would answer, with Accept, Adjust and Ignore buttons.
- **Use / avoid:** use a reference to copy structure and quality (spacing rhythm, type ratios, density, depth model); avoid copying another brand's identity: its logo, brand color, proprietary typeface or illustration are never carried over, and a "competitor" reference is used only to flag shared tropes [BRIEF requirement 4; S-L06-027].
- **Skip:** yes; always optional.
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
- **Evidence:** DC-L11-09, DC-L11-10; S-L11-005, S-L11-013, S-L11-030, S-L11-006
- **Merges:** K9.2, K9.3, K13.2, K1.4

---

## Stage 02 · Audience and commitments
> Screen: who the product is for and what it promises them. Graph step 0. These answers bound every later option.

### Q-aud-01 · Who uses the product, and how often? · Quick
- **Why:** Audience sets density and base text size, the fourth-largest visual difference between systems (body text ranges 13-19px) [DC-L09-04; L09 A2 row 4].
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
- **Skip:** yes, defaults to regular. Target sizes do not shrink with density; they follow input precision (Stage 07, DC-L14-03).
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
- **Evidence:** DC-L06-03, DC-L06-19; S-L06-010, S-L06-060, S-L06-014
- **Merges:** B1 (emotional state), B2

### Q-aud-03 · What accessibility standard must the system meet? · Standard
- **Why:** The target bounds color, type size, focus ring and target-size options in every later stage [DC-L11-19].
- **Ask:** "Which accessibility standard must you meet? WCAG 2.2 AA is the usual floor."
- **Example:** Show a text pair that passes 4.5:1 and one that fails.
- **Control:** single choice
- **Options:**
  - `wcag22-aa` WCAG 2.2 AA: 4.5:1 text, 3:1 large text and UI parts, 24px target floor (GOV.UK commits to 2.2 AA) [S-L11-093; L09 A1 row 11].
  - `wcag22-aa-plus` AA plus chosen AAA rules, for example 7:1 body text or larger targets: stricter palettes, fewer mid-tone text colors [DC-L01-22, inferred].
  - `wcag22-a` Level A only: not recommended; no benchmarked system states a target below AA [L09 A1 row 11].
- **Default:** WCAG 2.2 AA. *Source:* accessibility rule; all 11 benchmarked systems that state a target use AA; WCAG 3 is still a draft, so 2.2 is the enforceable target [L09 A1 row 11; BOARD L01 note].
- **Decides:** DC-L11-19
- **Changes:** DC-L01-22, DC-L03-12, DC-L04-09, DC-L14-03, DC-L02-08 · blocks: Foundations > Accessibility > Program
- **Preview:** a guardrail strip listing which later options will be blocked or flagged at this level.
- **Skip:** yes, AA. The builder also generates the system-vs-product-team responsibility statement GOV.UK publishes [S-L11-092].
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
- **Evidence:** DC-L02-11; S-L02-006, S-L02-011, S-L02-012, S-L02-015, S-L02-041

### Q-brand-07 · How closely should interactions follow familiar conventions? · Standard
- **Why:** Native behavior feels trustworthy but generic; novelty is distinctive but costs learnability (Jakob's law) [DC-L13-17].
- **Ask:** "Should interactions follow familiar conventions, get a custom look, or be novel where it matters?"
- **Example:** Show a standard dropdown beside a custom one.
- **Control:** single choice
- **Options:**
  - `native` Platform-native: follow HIG, Material or Fluent behavior and look; instantly usable, generic [DC-L13-17].
  - `custom-skin` Conventional behavior with a custom skin: brand visuals, standard interaction [DC-L13-17].
  - `novel-core` Novel interaction for the core differentiator only, tested [DC-L13-17; S-L13-006].
- **Default:** custom-skin. *Source:* card heuristic; don't override standard shortcuts [DC-L13-17; S-L13-036, S-L13-030].
- **Decides:** DC-L13-17
- **Changes:** DC-L10-02 default posture, DC-L08-03 · blocks: Principles > Familiarity
- **Preview:** a standard dropdown and a custom one next to each other, both keyboard-operable.
- **Skip:** yes.
- **Evidence:** DC-L13-17; S-L13-006, S-L13-030, S-L13-036, S-L13-055

### Q-brand-08 · What are your 3-5 design principles, and which one wins a tie? · Standard
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
- **Evidence:** DC-L06-15, DC-L11-05; S-L06-044, S-L06-077, S-L11-008
- **Merges:** K3.2, B12

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
- **Evidence:** DC-L10-01; S-L10-021, S-L10-046, S-L10-047, S-L10-075, S-L11-030
- **Merges:** P1, K2.2 (platform part)

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
- **Evidence:** DC-L14-11; S-L14-031, S-L14-032, S-L14-037, S-L14-008
- **Merges:** D4

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
- **Evidence:** DC-L10-02, DC-L06-14; S-L10-009, S-L10-038, S-L10-075, S-L10-076, S-L06-043
- **Merges:** P3

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
- **Evidence:** DC-L10-19, DC-L10-20, DC-L10-21; S-L10-047, S-L10-055, S-L10-063, S-L11-030
- **Merges:** K2.3, P20, P21, P22

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
- **Evidence:** DC-L10-23; S-L10-005, S-L10-019, S-L10-020, S-L10-023, S-L10-071, S-L10-076
- **Merges:** P24

---

## Stage 05 · Where the system lives
> Screen: source of truth, design tools and how engineers consume the output. Graph step 0-1. Asked before any foundation because it decides what the builder generates on every later preview [DC-L16-02].

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
- **Default:** builder. *Source:* card heuristics of L16 and L11 [DC-L16-02, DC-L11-16]; L07 prefers token-file (see Disagreements).
- **Decides:** DC-L16-02, DC-L07-08, DC-L11-16
- **Changes:** DC-L07-25, DC-L07-09, DC-L16-12, DC-L16-13, DC-L11-14 · blocks: Builder > Data > Source of truth; Tokens > Architecture > Source of truth
- **Preview:** a round-trip diagram: which targets are generated, which only mirror, and which direction sync runs.
- **Skip:** yes, builder.
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
- **Evidence:** DC-L09-08; S-L09-199, S-L09-313, S-L09-587, S-L09-589, S-L09-609
- **Merges:** K10.1

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
- **Default:** none; if Figma, the builder asks the plan first and greys out architectures it cannot hold (for example 4 brands x light/dark/high-contrast = 12 modes exceeds Professional's 10). *Source:* card heuristic [DC-L07-27; S-L07-014]. Write through Figma's remote MCP when a Full seat exists, otherwise emit one DTCG file per mode [DC-L16-13].
- **Decides:** DC-L07-27, DC-L16-13
- **Changes:** DC-L07-16, DC-L07-17, DC-L07-18, DC-L07-26, DC-L07-24 · blocks: Tooling > Figma plan; Builder > Interop > Design tools
- **Preview:** a mode-budget meter (modes used vs the plan's limit) that later theming answers fill.
- **Skip:** yes.
- **Evidence:** DC-L07-27, DC-L16-13; S-L07-014, S-L07-015, S-L07-034, S-L16-002, S-L16-113
- **Merges:** K2.4

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
- **Decides:** DC-L09-03, DC-L06-06, DC-L01-09
- **Changes:** DC-L01-01, DC-L01-03, DC-L01-04, DC-L06-17, DC-L15-06 · blocks: Foundations > Color > Palette generation; Foundations > Theming > Generator inputs
- **Hook:** Accepts hex, RGB or OKLCH values, a brand book PDF, or a reference from Q-ref-01. If no brand color exists: the builder suggests seeds weighted by the personality sliders (blue reads competent, red excitement, per Labrecque & Milne) and labels the choice as a starting point, not a brand decision [S-L06-072].
- **Preview:** the seed becomes ramps live; locked hexes show a pin on their step; a light brand color (yellow, cyan, lime) visibly switches its button text to dark (Spectrum does this) [S-L01-036].
- **Use / avoid:** use the brand hex as a ramp anchor and pick UI steps by contrast; avoid using a brand color whose ratio with white is below 3:1 for small text; use it as a fill with dark text or as a tint [DC-L01-09; S-L01-044].
- **Skip:** yes, a seed is suggested.
- **Evidence:** DC-L09-03, DC-L06-06, DC-L01-09; S-L09-459, S-L09-563, S-L06-012, S-L01-036, S-L01-044
- **Merges:** K3.4, B7 (brand colors), K7.1 (ramp method)

### Q-color-02 · Where should your brand color appear? · Quick
- **Why:** Brand color placement is the third-largest visual difference between systems: actions only, containers, or whole surfaces (L09 divergence 3) [DC-L06-04].
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
- **Evidence:** DC-L01-27; S-L01-030, S-L01-031, S-L01-036, S-L01-052

---

## Stage 10 · Typeface
> Screen: which fonts, for which scripts. Graph step 2-4. Cycles kept together: DC-L02-01 + DC-L02-02 + DC-L02-03 + DC-L02-04 + DC-L02-06 + DC-L02-24 (the typeface must cover your scripts and license terms, and those in turn narrow the typeface) and DC-L06-07 + DC-L06-24 (brand typeface vs localization readiness). The preview is a type specimen in the product's own UI, with a coverage bar for each chosen script.

### Q-type-01 · Should the product use the platform's font, a neutral open font, or your own brand typeface? · Quick
- **Why:** After color, the typeface is the largest single brand lever; system fonts feel native and invisible, a custom face gives instant recognition (L09 divergence 5) [DC-L09-05].
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
- **Use / avoid:** add a second face only for a change of job (display vs text, code); avoid near-identical pairs that read as a mistake [DC-L02-03; DC-L15 P49 via DC-L15-11].
- **Skip:** yes.
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
- **Decides:** DC-L02-05
- **Changes:** DC-L02-26, DC-L05-24 · blocks: Foundations > Typography > Typeface > Monospace / numeric
- **Preview:** a code block, a table column and a live counter with proportional vs tabular figures.
- **Use / avoid:** use tabular figures in tables, clocks and anything that updates; avoid mono for body text [DC-L02-05; S-L02-052].
- **Skip:** yes.
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
- **Evidence:** DC-L02-08; S-L02-001, S-L02-005, S-L02-006, S-L02-011, S-L02-014
- **Merges:** K7.2 (sizes)

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
- **Evidence:** DC-L02-17, DC-L02-18, DC-L02-16; S-L02-015, S-L02-022, S-L02-029, S-L02-051

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
- **Evidence:** DC-L02-19; S-L02-011, S-L02-022, S-L02-028

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
- **Evidence:** DC-L02-20, DC-L14-04; S-L02-007, S-L02-021, S-L14-012, S-L14-026

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
- **Evidence:** DC-L02-21, DC-L10-07; S-L02-001, S-L10-011, S-L10-012, S-L10-071, S-L10-074
- **Merges:** P8, K4.4 (text scaling)

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
- **Evidence:** DC-L03-12, DC-L14-03, DC-L03-13; S-L03-029, S-L03-033, S-L03-035, S-L14-037

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
- **Evidence:** DC-L03-25; S-L03-002, S-L03-010, S-L03-039, S-L03-077

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
- **Evidence:** DC-L03-10, DC-L03-11, DC-L14-13; S-L03-042, S-L03-057, S-L03-070, S-L14-026
- **Merges:** K6.3 (density modes, mechanism)

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
- **Evidence:** DC-L03-08; S-L03-044, S-L03-059, S-L03-062, S-L03-063

