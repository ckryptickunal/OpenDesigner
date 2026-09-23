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

