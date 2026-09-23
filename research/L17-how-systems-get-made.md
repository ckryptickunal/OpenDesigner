# L17: How design systems get made today (manual and AI), which blocks need a designer, and the process the builder should run

Lane: L17. Author: orchestrator subagent L17, with four helper subagents (H1 NN/g, H2 AI workflows and extractors, H3 designsystems.surf and manual workflows, H4 designer-hook formats and fallbacks). Written 2026-09-23.
Trace: `traces/L17-trace.md`. Helper rows are re-logged there with their reserved id ranges.
Status: see `## Open questions / gaps` and `## Confidence` at the end.

Related lanes this file links to rather than repeats: L11 (lifecycle, 24 competitors, 77-question kickoff questionnaire), L16 (43 tools, interaction models, round trip), L06 (brand inputs, lever matrix), L05 (icons, imagery, data viz), L07 (tokens, Figma), and the S1 synthesis files (`synthesis/ONTOLOGY.md`, `synthesis/LEVERS.md`).

## Lane overview

This lane answers four questions for OpenDesigner: how design systems get made today, by hand and with AI; what gstack, NN/g and designsystems.surf teach about doing it well; which building blocks the builder can generate, read from a reference, or must ask a designer or a tool for; and what process a model should run with a person to build a system without missing anything. It rests on 303 logged sources (264 used, 39 rejected or not used): gstack's source files, 43 NN/g articles, all 90 designsystems.surf system pages, official docs for 15 AI tools and 6 extractors, and 81 Tier A licence and platform pages for the designer hooks.

**Top findings**
1. **Two thirds of a design system is generatable; the designer-owned part is small but it is what people see first.** Of 207 ontology blocks, 135 are generatable from a few inputs and dials, 31 are tool-assisted, 29 are decisions only the owner can make, 7 are designer-owned and 5 are best read from existing assets; 44 can be pre-filled from a reference (Part G). The 7 designer-owned blocks expand into 14 asset hooks (Part H). The task's four classes needed a fifth, owner input, so business decisions are not misfiled as design work (DC-L17-01).
2. **Nothing on the market checks coverage, and generating from nothing yields a theme, not a system.** Relume, Uizard, tweakcn, Subframe and Polymet produce color, type, radius and shadow; none produces accessibility targets, usage rules or governance. Bolt says a docs site alone gives "a theme rather than a true design system"; Lovable removed its Themes feature for low usage; Motiff shut down [S-L17-206] [S-L17-234] [S-L17-229]. The closest precedent for a guided process is Figma's own `figma-generate-library` skill, which starts from an existing codebase [S-L17-210].
3. **gstack's most transferable methods** are: read what exists before asking; one "memorable thing" question; label every proposal as safe choices versus risks with gain and cost; concepts in text first, then variants that must differ in type, palette and layout; a comparison board with remix; sorting decisions into Mechanical, Taste and User Challenge; deterministic lint before model critique; and writing DESIGN.md plus an agent rule to read it. Reject: tokens extracted from a generated image as the source of truth, hard font bans, and raster mockups as the main preview (Part A3).
4. **The generic AI look is admitted by the vendors and measured by NN/g.** Google's and Anthropic's official skills list the default looks; NN/g's study of 10 tools found the same sans-serif, shadcn-and-Tailwind output and said in May 2025 that no AI tool effectively supported design systems [S-L17-218] [S-L17-021] [S-L17-120] [S-L17-122]. The fix is feeding the system itself (tokens, component code, rules, glossary) and forcing an explicit decision per block, not a better prompt [S-L17-121] [S-L17-124].
5. **References give values, not intent.** Color, type, spacing, radius and shadow are read reliably from a URL, Figma file or code; states, modes, motion (without a live browser), component usage and brand meaning are not. Only one extractor (Dembrandt) forbids copying a third party's identity, so the identity firewall has to be a hard rule in the builder (Part F, DC-L17-03).
6. **Manual reality sets the bar to beat.** 61% of design-system teams have five or fewer people, only 40% automate token sync, documentation is the most common complaint, and a v1 takes about 12 weeks with 3-8 people in Dan Mall's program [S-L17-347] [S-L17-349] [S-L17-352]. Docs must be a by-product of every decision (DC-L17-13).
7. **Designer hooks need licence intelligence, not just upload slots.** Fontshare's licence bans subsetting and offering its fonts in a design tool's picker; Adobe Fonts cannot be self-hosted or embedded in apps; AI output ownership varies by plan; purely AI-generated work is not copyrightable in the US (Supreme Court denied review in Thaler, 2 Mar 2026) [S-L17-536] [S-L17-538] [S-L17-525] [S-L17-563].

**How to read this file.** Parts A-E are evidence (gstack, NN/g, designsystems.surf, manual workflows, AI workflows). Part F is reference intake. Part G classifies every block; Part H specifies every hook. Part I is the proposed process, written as what the model asks, shows, recommends and records at each of 11 stages. Part J holds Decision Cards DC-L17-01 to DC-L17-13. The file ends with reconciliation, cross-lane notes, gaps and confidence.

---

## Part A. gstack's design skills (read-only review, 2026-09-23)

gstack is Garry Tan's MIT-licensed set of 53 Claude Code skills, created 11 Mar 2026 and pushed daily (last push 23 Sep 2026) [S-L17-001]. Six skills and one pipeline phase are about design. I read every one from raw.githubusercontent.com and did not install anything [S-L17-002 to S-L17-018]. Tier C (practitioner open source): its methods are opinion, but they are concrete, versioned and tested, which makes them unusually easy to evaluate.

### A1. The design skills and what each does

| Skill (verified name) | Role in gstack | What it produces | Evidence |
|---|---|---|---|
| `/design-consultation` | "Design Partner": builds a design system from scratch | Proposal with safe choices and risks, a preview (AI mockups or an HTML specimen page), then `DESIGN.md` plus a CLAUDE.md rule to always read it | [S-L17-003] [S-L17-004] |
| `/design-shotgun` | "Design Explorer": "show me options" | 3 variants by default (up to 8), a local comparison board with ratings, comments, remix and regenerate, and a taste profile | [S-L17-005] [S-L17-013] |
| `/plan-design-review` | "Senior Designer" reviewing a plan before code | A 0-10 score per dimension, one question per gap, edits to the plan | [S-L17-006] [S-L17-007] |
| `/design-review` | "Designer Who Codes": audits a live site, then fixes it | First-impression critique, an inferred design system read from the rendered page, an 80-item checklist with A-F grades, atomic fix commits with before/after screenshots | [S-L17-008] |
| `/design-html` | "Design Engineer": approved mockup to production HTML | Framework-aware HTML/CSS with computed text layout | [S-L17-002] [S-L17-018] |
| `/ios-design-review` | HIG audit of an iOS app | Findings against Apple's guidelines | [S-L17-018] |
| `/autoplan` design phase | Runs the design review automatically inside a plan pipeline | Fixes structural gaps itself; flags aesthetic questions as taste decisions for the human | [S-L17-015] |

### A2. The methods, step by step

**1. Interview (context before taste).**
- It reads what already exists before asking anything: an existing `DESIGN.md`, a `PRODUCT.md`, the README, `package.json`, the source tree, and earlier office-hours notes. A `PRODUCT.md` counts as the user's prior answers, confirmed in one line, not re-asked [S-L17-003].
- The first question bundles what the product is, who it is for, the project type (web app, dashboard, marketing site, editorial, internal tool) and whether to research competitors. It tells the user the flow is a conversation, not a form [S-L17-003].
- One forcing question: "What's the one thing you want someone to remember after they see this product for the first time?" The answer becomes the test every later decision must pass [S-L17-003].
- For screen-level work, the brief has five dimensions: who, the job to be done, what exists, the user flow, and edge cases. It allows two rounds of questions at most, then proceeds and notes its assumptions [S-L17-005].
- impeccable (the tool gstack interoperates with) separates durable product truth (`PRODUCT.md`: audience, purpose, constraints, voice) from the visual system (`DESIGN.md`) [S-L17-020].

**2. Research the landscape.**
- It finds 5-10 products in the category, then asks the user to confirm the exact URLs before opening any of them, because search results should not choose which sites get the user's browser session [S-L17-003].
- It synthesizes in three layers: tried and true (what the category expects), new and popular (current trends), and first principles (where the category's convention fails this product's users). A "EUREKA" line names a justified departure: every product in the category does X because it assumes Y, but these users need Z [S-L17-003].
- Optional independent "outside voices": a Codex run and a Claude subagent each get the same written brief, without the main agent's draft, and propose a full direction. Agreement is not counted as a vote [S-L17-003] [S-L17-004].

**3. Propose safe versus risky choices.**
- The proposal covers aesthetic, decoration level, layout, color (with hex values), typography roles, spacing (base unit and density) and motion, plus one sentence on why the parts reinforce each other [S-L17-004].
- It then splits the proposal into **SAFE CHOICES** (2-3 category conventions users expect, with the reason to play safe) and **RISKS** (at least 2 deliberate departures, each with what it is, why it works, what it gains and what it costs). Its stated reason: coherence alone can look generic [S-L17-004].
- It offers named menus behind the proposal rather than as a form: 10 aesthetic directions (brutally minimal, editorial, industrial/utilitarian, and so on), 3 decoration levels, 3 layout approaches, 4 color strategies (Restrained, Committed, Full palette, Drenched) and 3 motion approaches [S-L17-004].
- Fonts follow a procedure, not a menu: name the audience's world and the surface mode, shortlist three faces per role, apply exclusions, verify the face exists and is licensed (Google Fonts, Fontshare or local files), then specify loading. An unverified face is marked pending, never invented [S-L17-004].
- A coherence check flags mismatches after any override (for example brutalist plus expressive motion) but never blocks: the user's final choice wins [S-L17-004].

**4. Generate variants.**
- Concepts first, in text: N named directions, each one line. The user confirms before any paid image generation [S-L17-005].
- Anti-convergence is a hard rule: each variant must use a different font family, palette and layout. Test: if you could swap the headlines between two variants without noticing, they are too similar [S-L17-005].
- Variants are generated in parallel, each passes a vision quality check, and they open on a local comparison board where the user rates, comments, remixes ("layout from A, colors from B") or regenerates. The board writes JSON that the agent reads [S-L17-004] [S-L17-005] [S-L17-013].
- A taste profile records approvals and rejections by dimension (fonts, colors, layouts, aesthetics). Confidence decays 5% a week, and the agent flags a conflict when a new request contradicts a strong past preference [S-L17-002] [S-L17-005].
- Mockups are generated through OpenAI's image API, with the Google Stitch SDK named as a backup, and screenshots are sent only after a one-time consent prompt [S-L17-012].

**5. Write DESIGN.md.**
- Tokens come from the approved visual, not from the text proposal: an `extract` step runs a vision model over the chosen mockup to pull colors, type, spacing, layout and mood [S-L17-004] [S-L17-014].
- The file follows Google's open DESIGN.md format: YAML front matter with five token groups (`colors`, `typography`, `rounded`, `spacing`, `components`, with `{colors.primary}`-style references) and a Markdown body in eight canonical sections (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts). gstack adds Motion and a Decisions Log [S-L17-004] [S-L17-010].
- Writing is gated on explicit approval, and the skill then appends a rule to CLAUDE.md: read DESIGN.md before any visual decision and do not deviate without approval [S-L17-004].

**6. Review and grade.**
- Plan review rates seven passes 0-10 (information architecture, interaction-state coverage, user journey and emotional arc, AI slop risk, design-system alignment, responsive and accessibility, unresolved decisions). For each score below 10 it says what a 10 looks like, asks one question per gap, and re-rates [S-L17-006] [S-L17-007].
- It classifies each surface by what the visitor's win looks like: Persuade (marketing), Operate (app UI), Read (docs) or Experience (portfolios), with different rules for each [S-L17-007].
- Live-site review starts with a first-person first impression ("the first 3 things my eye goes to are..."), then reads the design system actually rendered (font families, colors, heading scale, touch targets under 44px) and flags more than 3 font families or more than 12 non-gray colors. Grades are A-F across 10 weighted categories, with AI slop graded separately [S-L17-008].
- The pipeline sorts decisions into Mechanical (one right answer: decide silently), Taste (reasonable people disagree: decide with a recommendation, surface at a final gate) and User Challenge (changes the user's stated direction: never auto-decide) [S-L17-015].

**7. Avoid "AI slop".**
- A named catalog of tells: purple or blue-to-purple gradients, the three-column icon-in-a-circle feature grid, centered everything, one bubbly radius on every element, decorative blobs and wavy dividers, emoji as decoration, a colored left border on cards, generic hero copy, cookie-cutter section rhythm, and system-ui as the primary face [S-L17-004] [S-L17-007].
- A "three looks" calibration that AI output falls into regardless of product: cream ground with serif display and terracotta accent; near-black with one neon accent and glowing edges; broadsheet hairlines with italic serif and tiny tracked mono. Each is fine only when the brief asks for it [S-L17-004] [S-L17-007]. Anthropic's own frontend-design skill lists five such clusters (adding the SaaS-card kit and template chrome) and warns that the terracotta near #D97757 is Anthropic's accent, so it reads as a tell on a user's brief [S-L17-021].
- Role-scoped font lists: 25 faces never used as the display voice (Inter, Roboto, Geist, Space Grotesk and others), a few allowed as body/UI on Operate or Read surfaces, and 14 banned outright [S-L17-004].
- Craft reflexes no detector catches: theme browser surfaces (selection color, caret, scrollbars, focus rings, tabular numerals), one authored motion moment, shadows with an offset rather than a zero-offset glow, secondary text on a colored surface tinted from that hue, more space above a heading than below [S-L17-007].
- Deterministic checks where possible: gstack runs impeccable's 61-rule engine on source or on a dump of the rendered DOM, speaks the same rule ids, and puts a "Never:" line built from ten catalog ids into every image prompt. A vision-model slop rubric was deferred because vision misjudges cream palettes and nested cards [S-L17-011] [S-L17-016]. The slop lists and visitor modes are derived from impeccable (Apache-2.0), and the hard-rejection rules cite OpenAI's GPT-5.4 frontend guidance [S-L17-016] [S-L17-007] [S-L17-019].

### A3. What the builder should adopt, adapt or reject

| gstack method | Verdict | How it maps to the builder | Why |
|---|---|---|---|
| Read what exists before asking (DESIGN.md, PRODUCT.md, repo, prior answers) | **Adopt** | Stage 0 scans the repo, any DESIGN.md, tokens files, Figma file and references; pre-fills answers and asks only for gaps | Matches L11's finding that the questionnaire is long (77 questions); pre-filling is how to keep it short [S-L17-003] [inferred] |
| The memorable-thing forcing question | **Adopt** | One required field in the brand step; every later "risk" proposal cites it | Cheap, and gives the AI a test for distinctiveness [S-L17-003] |
| Separate product truth (PRODUCT.md) from the visual system (DESIGN.md) | **Adopt** | Context and principles live in their own file; tokens and visual rules in another; both exported | Different readers and change rates; impeccable and gstack both read both [S-L17-020] [S-L17-003] |
| Research with user-confirmed references | **Adopt** | Reference intake always shows the URL list for approval before fetching | Privacy and relevance; the user decides what counts as a reference [S-L17-003] |
| Three-layer synthesis + EUREKA line | **Adapt** | Each block's detail panel shows "category convention", "trend" and "your departure (optional)" | Good teaching device; the builder presents it per block rather than as prose [inferred] |
| SAFE vs RISK split | **Adopt** | Every proposal screen labels which choices follow convention and which are deliberate risks, with gain and cost | The single most transferable idea: it makes taste legible to engineers [S-L17-004] |
| Named menus behind a conversation (aesthetic, decoration, color strategy, motion approach) | **Adapt** | Map onto the eight LEVERS dials and macros (`synthesis/LEVERS.md`); keep the menus as presets | The builder already has sourced dials; gstack's names are useful preset labels [inferred] |
| Concepts in text first, confirm, then generate | **Adopt** | Direction cards (one line each) before any expensive generation | Saves cost and time; users redirect early [S-L17-005] |
| Anti-convergence rule and the headline-swap test | **Adopt** | Variant generator enforces distinct type, palette and layout; a diversity check rejects near-duplicates | Directly counters the sameness complaint in the community signal [S-L17-005] [COMMUNITY-SIGNAL topic on slop] |
| Comparison board with rate, comment, remix, regenerate | **Adopt** | The builder's variant view; remix at block level ("type from A, color from B") | It is the visual-first loop the brief asks for [S-L17-005] |
| Taste profile with decay | **Adapt** | Per-project taste memory, visible and editable, never silently applied across projects | Useful, but invisible cross-project bias would fight anti-convergence [inferred] |
| Tokens extracted from the approved image by a vision model | **Reject as the source of truth** | The builder's tokens come from its own model; vision extraction is used only to read references | A vision guess is lossy; the builder already holds exact values [S-L17-014] [inferred] |
| DESIGN.md in Google's open format | **Adopt as one export** | Emit DESIGN.md next to DTCG, CSS and Figma variables | Other agents (Stitch, impeccable, gstack) read it; it is a draft spec, so it cannot be the only format [S-L17-010] [COMMUNITY-SIGNAL: DESIGN.md is a draft] |
| CLAUDE.md rule "read DESIGN.md before visual work" | **Adopt** | Export includes agent instructions for Claude Code, Cursor and others | Keeps agents inside the system after export [S-L17-004] |
| 0-10 rating per dimension with "what a 10 looks like" | **Adopt** | The coverage check scores each layer and shows the gap in plain words | Makes completeness measurable; matches brief requirement 5 [S-L17-006] |
| Persuade / Operate / Read / Experience modes | **Adopt** | A per-surface setting that switches default rules (density, card use, hero rules) | Resolves the "marketing vs app" conflict inside one system [S-L17-007] |
| Mechanical / Taste / User Challenge | **Adopt** | Generatable blocks are decided silently with defaults; taste blocks are surfaced; changes to stated direction need consent | This is the builder's classification seen from the decision side [S-L17-015] |
| Slop catalog, three looks, font lists | **Adapt** | Ship as lint rules with ids, severity and a one-line reason, and let users waive a rule per project | The lists are opinionated (Inter as display is fine for many products); lint with waivers keeps them honest [S-L17-004] [inferred] |
| Hard font bans (e.g. Raleway, Courier New) | **Reject as bans** | Warn, do not block | Taste, not evidence; the brief says the builder helps rather than replaces designers [inferred] |
| Deterministic detector first, model judgment second | **Adopt** | Validators (contrast, target size, scale steps, slop rules) run before any AI critique | Cheaper, repeatable, and gstack found vision misjudges some patterns [S-L17-011] |
| Generated raster mockups as the main preview | **Reject for system work** | The builder previews on real rendered components; generated images only for mood exploration | Raster mockups cannot be edited or measured; L16 recommends real HTML/CSS rendering [inferred; L16 finding 7] |

---

## Part B. NN/g guidance, 2024-2026 (helper H1; 43 articles used, 8 rejected)

NN/g is Tier B. Most of its AI studies are qualitative expert evaluations; the few numbers are flagged. NN/g has no topic page at `/topic/design-systems/` (404) and no article on style tiles or interface inventories [S-L17-100] [H1 search note under S-L17-119].

### B1. Design systems and their documentation
- **Definitions.** A design system manages design at scale with reusable components and patterns; a style guide is one part of it, in three kinds (visual/front-end, brand, content). A component library holds single elements with their states; a pattern library holds groups of elements [S-L17-109].
- **What every element's documentation needs.** NN/g's canonical checklist (2016, still cited): a categorized table of contents, grid, palette, type styles with usage contexts, **the context of use for each element**, code snippets, implementation specs, and **do's and don'ts** [S-L17-112]. Pattern docs add when and how to use, real examples and variations by context [S-L17-111]. Content standards (style, accessibility, format) belong inside each component, with do/avoid examples, an owner and a yearly review [S-L17-110]. Developer specs should use real content, not placeholders [S-L17-114].
- **How "where not to use" is written.** NN/g's usage articles are comparative: decision criteria, a numeric threshold, then the named alternative. Dropdowns: fewer than about 5-7 options, use radio buttons; more than about 15, use a combobox (USWDS threshold under 7, Material 6, Carbon 3) [S-L17-117]. Comparison pieces follow "X vs Y" [S-L17-116]. The UI elements glossary has 61 entries, a ready naming layer [S-L17-115].
- **Maturity is multidimensional (Jul 2026).** Six dimensions scored 1-5 by 4-8 people independently, then discussed; fix the lowest first; reassess about quarterly [S-L17-107].
- **Governance needs a steward** who reviews after exploration and before implementation; standardize a change when three or more teams benefit [S-L17-108]. Most teams have 2-5 people; build what product teams need, with precise rather than exhaustive docs [S-L17-113].
- **Audit method.** The closest NN/g method to an interface inventory is the content inventory plus audit: every item listed with owner and metadata, then rated keep/update/remove, time-boxed to about 6 weeks [S-L17-119]. A consistency review about once a year finds the worst offenders [S-L17-118].

### B2. AI-generated and AI-assisted design
- **2024 baseline:** Uizard, UX Pilot and a Figma plugin produced generic, templated output; one identical prompt gave three very different designs [S-L17-123].
- **May 2025:** "Currently, no genAI tool effectively supports design systems" (verbatim), and 500-character prompts are not enough [S-L17-122].
- **Oct 2025 study of 10 tools** (Figma Make, Figma First Draft, Relume, Bolt, UX Pilot, Lovable, Replit, v0, Stitch, Claude) at three prompt levels: output had "a similar, generic look using sans-serif typeface and minimalistic styling" (verbatim) and defaulted to shadcn and Tailwind; weak spacing, grouping, contrast and hierarchy; wrong patterns; no intent. Prompts with artifacts (sketches, mockups, Figma links) gave the most faithful results. Heuristic evaluation, no participant counts [S-L17-120].
- **Dec 2025 fixes for vague prompts:** precise visual keywords instead of "clean", lightweight references (mood boards, design-system screenshots), a chatbot drafting the prompt from the reference, realistic mock data, and component code snippets. NN/g adds that copying an existing brand's identity "is not a sustainable strategy" [S-L17-121].
- **Human in the loop:** critique is the core skill (Judge-Evaluate-Iterate; calibrate LLM judges to F1 0.8 or better against human labels; one judge per criterion) [S-L17-130]; one output is an example, not an evaluation (worked example: 10 inputs x 5 runs) [S-L17-132]; the "fidelity trap" is polish hiding wrong patterns [S-L17-133]; confident output discourages checking, so show uncertainty and sources [S-L17-142].
- **Context beats prompts:** a UX.md beside the code with seven context types (research, interaction standards, design system values plus guidance, user models, world models, glossary, component libraries), updated when research or AI mistakes teach something [S-L17-124]; information architecture applies to AI context [S-L17-140]; Markdown sources of truth built by dictation decay within weeks [S-L17-135]; UX debt piles up when building is cheaper than evaluating [S-L17-131].
- **Sameness and trust:** polish no longer signals quality; visibly handmade work signals care (argument, no study data) [S-L17-125]; AI images scored close to stock photos in a 77-person test (only authenticity significant, +0.4 on a 7-point scale) but fail on visible artifacts and stereotypes [S-L17-126]; decent-looking UI is being commoditized [S-L17-136].

### B3. Visual direction
- **Mood boards:** six steps, starting from brand assets and **4-5 mood words**, converging through comparison and a stakeholder workshop [S-L17-146]; they double as AI prompt references [S-L17-121].
- **Checking a direction:** 5-second tests, first-click, preference tests with 2-3 variants, and closed word choice against the target brand attributes (with opposites and distractors) [S-L17-148].
- **Icons need craft:** 19 of 20 intranets had bad icon sets [S-L17-149]; icons need labels, and if no icon comes to mind in about 5 seconds it will not communicate [S-L17-150].

### B4. What the builder takes from NN/g
1. Every block's detail panel follows the NN/g record: what it is, states, context of use, do's and don'ts with the alternative named, real-content example, content standard, code [S-L17-112] [S-L17-110] [S-L17-111].
2. "Where not to use" is always a comparison with a threshold and a named alternative [S-L17-117].
3. Generation is fed from the system (tokens, component code, rules, glossary), not free text, which is NN/g's diagnosis of generic output [S-L17-120] [S-L17-124].
4. Direction starts with mood words and references, and is checked with closed word choice [S-L17-146] [S-L17-148].
5. Critique uses rubrics set in advance, repeated runs, and calibrated judges [S-L17-130] [S-L17-132].
6. The coverage check behaves like a content audit (inventory, keep/update/remove) and the maturity radar is a later-stage health view [S-L17-119] [S-L17-107].

---

## Part C. designsystems.surf: how 90 real systems structure their documentation (helper H3)

**What the site is.** A curated link index launched in fall 2023 by Ilya Greben [S-L17-312]. Each system page links out to that system's own foundation and component docs, with three source tags (Figma, Repository, Storybook) [S-L17-301] [S-L17-302]. It has no filters by company, platform or technology, does not synthesize docs apart from 7 component "blueprints", sells its own Figma foundation kits, and lists no third-party tools or plugins [S-L17-306] [S-L17-309] [S-L17-310]. L00 rejected one of its articles as a listicle [S-L00-005]; this lane uses only its directory data, as a structured sample (Tier C). All counts below were made by H3 with a script over the live pages on 2026-09-23 [S-L17-301] [S-L17-302].

**Scale.** 90 systems; median 12 foundations (range 4-19) and 27 components (range 0-41) per system. Tags: Repository 62, Figma 42, Storybook 30. The site's own index badges are stale (Button shows 69 while 87 system pages link to Button), and two listed doc sites have moved (Twilio Paste now redirects to GitHub, Polaris into shopify.dev) [S-L17-303] [S-L17-315] [S-L17-320].

**Which documentation sections recur (systems of 90 linking to each):** Color 86, Icons 86, Typography 85, Spacing 60, Accessibility 56, Layout/grid 55, Component overview 54, Tokens 49, Patterns 45, Elevation 42, Voice and tone 41, Motion 36, Styles page 34, Theming 31, Data visualization 30, Illustrations 26, Responsive 22, Component status 15, Localization 11, States 10, Component lifecycle 4 [S-L17-302]. Surf does not track Getting started, Principles, Contribution, Changelog, radius or border; the own-docs checks show Getting started at the top level of Material 3, GOV.UK and Primer and under Designing/Developing in Carbon, with Carbon also carrying Contributing, Migrating and Releases [S-L17-313] [S-L17-314] [S-L17-316] [S-L17-319].

**Which components recur.** In 60 or more of 90 systems: button 87, text field 85, checkbox 83, radio 81, tabs 79, alert banner 74, switch 74, tooltip 70, progress indicator 69, cards 68, data table 68, pagination 65, date picker 63, accordion 62, progress bar 62, select 62, text area 61, badges 60. In 40-59: breadcrumbs, link, modal, popover, avatar, snackbar/toast, menus, tag, slider, dropdown, search, sidebar [S-L17-302].

**Two shapes of system** [inferred from H3's 12-system sample]: enterprise and government systems document 14-19 foundations including content, accessibility, data viz and illustration (Carbon, Polaris, Fluent 2, Salesforce, Paste); developer-led systems document 5-11 foundations and put the weight on components and tokens (Vercel Geist 5, Tailwind 11) [S-L17-302].

**Blueprint format worth copying.** Surf's component blueprints (switch, tabs and five others) use: anatomy, states, behavior, real-use examples, when and when not to use, a comparison with neighbors (switch vs checkbox vs radio vs segmented control), and best practices [S-L17-306]. This matches NN/g's comparative "use this when, otherwise that" format [S-L17-117].

**What the builder takes** [inferred from the counts]:
1. The frequencies give a tiered coverage checklist: core (85+ of 90: color, icons, type), common (41-62: spacing, accessibility, layout, component overview, tokens, patterns, elevation, voice and tone), specialist (30 or fewer: motion, theming, data viz, illustration, responsive, status, localization, states, lifecycle), plus what surf does not track (getting started, principles, contribution, changelog, radius, border). The ontology (S1a) already covers all of these; the frequencies tell the builder which to show by default and which to show as optional.
2. The 18 components found in 60+ systems are a defensible starter set, with the next 12 as a "likely next" tier; the builder should present them as a prunable checklist rather than generate everything.
3. Only 15 of 90 systems document component status, which is cheap for a builder to generate.

---

## Part D. Manual workflows today (helper H3; extends L11 Part A)

| Workflow | Steps | Artifacts | Time and effort | Pain points | Evidence |
|---|---|---|---|---|---|
| **Start from a UI kit** (Untitled UI, Material 3 kit, Apple Design Resources, shadcn community kits) | Duplicate or buy the kit, publish it as a library, change brand variables (color, type, radius), switch modes, delete what is not needed, hand off to code | Branded Figma library; variables; theme CSS | Not published. The M3 kit shipped 6 versions in 12 months (V1.20 to V1.25, latest 19 May 2026), so upkeep never stops | Kit updates can reset instances (M3 V1.21 warning); kits supply parts, not decisions | [S-L17-322] [S-L17-323] [S-L17-324] [S-L17-325] [S-L17-327] [S-L17-328] [S-L17-330] [S-L17-331] |
| **Interface inventory and code audit** | Screenshot every unique UI treatment, group in slides, decide keep/merge/kill (Brad Frost, 2013); count unique colors, sizes and specificity with CSS Stats or Project Wallace | Inventory deck; value lists; health score | Not published | The CSS Stats package was last updated in 2022; Project Wallace is maintained and groups values automatically | [S-L17-332] [S-L17-333] [S-L17-335] |
| **Figma variables and library** | Collections (primitives, then semantic), modes, aliases, scopes, code syntax (Web, Android, iOS), hide primitives, publish; subscribers accept updates | Variable collections; published library | Limits: 10 modes per collection on Pro, 20 on Org, unlimited only through extended collections on Enterprise; 5,000 variables per collection; publishing needs a paid Full seat. Seat prices: Pro $16, Org $55, Enterprise $90 per month | Branching and library analytics need Org or Enterprise; extended collections cannot rename modes or variables | [S-L17-336] [S-L17-337] [S-L17-338] [S-L17-339] [S-L17-340] [S-L17-341] |
| **Tokens Studio pipeline** | Author token sets, combine into themes, sync JSON to git, export to Figma variables and styles, transform with Style Dictionary | Token repo; Figma variables; platform code | Not published | Themes, multi-file sync and branching are Pro features; only 40% of teams automate design-to-code tokens at all | [S-L17-342] [S-L17-347] |
| **Docs: Storybook autodocs** | Write stories, add the `autodocs` tag, extend with MDX | One page per component: description, primary story with controls, props table | Not published | Autodocs cover API and props, not usage guidance or do's and don'ts [inferred from S-L17-343] | [S-L17-343] |
| **Docs: zeroheight, Supernova** | Connect Figma, Storybook and tokens; author pages with live blocks; publish; Supernova also runs exporters that open PRs | Docs site; token exports; PRs | Not published | Docs-tool satisfaction 60% vs 73% for design tools; subscribers' top complaint is poor documentation (39%), then unclear status (35%) | [S-L17-344] [S-L17-345] [S-L17-347] [S-L17-349] |
| **Agency or program engagement** | Dan Mall's 90-day program: team and asset audit, customer interviews, pilot, first components and contribution, testing, launch, v1.0. Nathan Curtis (now Directed Edges): vision, team model, support, metrics, releases. Clearleft: audit, grouping and naming workshops. Sparkbox: onboarding, sprints, knowledge transfer | North Star, ecosystem map, glossary, coverage map, component roadmap, reference site, 3+ pilot components | 12 weeks with 3-8 people at 20-30 hours a week (about 720-2,880 person-hours [inferred arithmetic]); Curtis embeds for 9+ months | The engineer plus DesignOps pairing carries the load; designers mostly support | [S-L17-352] [S-L17-354] [S-L17-355] [S-L17-359] [S-L17-361] [S-L17-364] |
| **Survey baseline** | - | - | Team size (zeroheight 2026, n=147): 1-2 people 28%, 3-5 33%, 6-10 25%, 10+ 12%; 61% under-resourced. NN/g: 2-5 typical. Value: designers 34% faster with an up-to-date system (Figma 2019); 8 developers 47% faster with Carbon (small sample) | 2026: resourcing 56%, prioritizing updates 35%, buy-in 31%, cross-team consistency 31%; 44% call their system unstable. 2022 (Sparkbox, n=219): tech or creative debt 43%, design-code parity 37%, adoption 36% | [S-L17-347] [S-L17-349] [S-L17-351] [S-L17-362] [S-L17-363] |

**UI kits: what you get and what is still undecided** [S-L17-322] [S-L17-323] [S-L17-324] [S-L17-325] [S-L17-327] [S-L17-328] [S-L17-330] [S-L17-331] [S-L17-367]

| Kit | What you get | Price | What the team must still decide |
|---|---|---|---|
| Untitled UI | Pro: 10k+ components and variants, 900+ styles, 420+ page examples, 2,000+ icons, variables (color, spacing, radius, width, type, effects), dark mode | Figma Solo $129 to Enterprise $2,499; React Solo $349 to $8,999 | Brand ramps, typeface, radius and density, which variants to keep, naming, accessibility target, product-specific components |
| Material 3 Design Kit | V1.25 (19 May 2026) with Expressive components; color roles fed by the Theme Builder plugin; 1.14m users | Free | Source color and contrast level, custom colors, fonts, whether to go Expressive, deviations from Material behavior |
| Apple Design Resources | iOS/iPadOS 27 and macOS 27 kits (Figma, Sketch), SF Symbols 27 (7,000+ symbols, 9 weights, 3 scales), SF fonts, Icon Composer | Free, bound by Apple's guidelines | Brand color and accent, custom components beyond system controls, parity with web and Android |
| shadcn/ui kits (community only; the shadcn docs list 4 free and 7 paid) | Obra: all components in all 8 shadcn styles, under 300 variables, 1,800+ Lucide icons; shadcndesign: 2,000+ components, 60+ blocks. Code theme: about 30 CSS variables in OKLCH with a `.dark` selector | Obra CE free; others paid | Base color, style, radius, fonts, icon library, extra semantic colors (success, warning and info are not in the default token list [inferred from S-L17-367]), and everything beyond components |

**What manual practice tells the builder** [inferred]:
- **Kits supply parts, not decisions.** Every kit leaves the same questions open: brand color, type, radius, density, which components to keep, naming and the accessibility target. A kit can be taken as a component base, and the builder asks exactly those questions.
- **The token pipeline is the most skipped step.** Only 40% of teams automate design-to-code tokens, and design-code parity is a top-two pain [S-L17-347] [S-L17-349]. One model emitting Figma variables, DTCG and code closes it (L07, L16).
- **Documentation is the chronic complaint**, so docs must be a by-product of each decision, not a later phase [S-L17-347] [S-L17-349].
- **The target team is 1-5 people** doing in weeks what a program does in 12 weeks with 3-8 people. The builder compresses the audit, coverage map, glossary and roadmap work that Dan Mall's program names as deliverables [S-L17-347] [S-L17-352].
- **Plan limits shape the Figma export**: stay within 10 modes per collection unless the plan allows more; extended collections are Enterprise-only [S-L17-338] [S-L17-340].

---

## Part E. AI workflows 2025-2026: how a design system gets made with each tool (helper H2; extends L11 Part G and L16 Part C)

L16 covers how these tools are operated and how designs move to code; L11 Part G lists them as competitors. This table adds what each tool **asks for** to make or define a system, what it **produces**, where the **human** stays in the loop, and how it **fails**. Vendor quality claims are vendor claims.

| Tool | Asks for | Produces | Human in the loop | Failure modes and limits | As of | Evidence |
|---|---|---|---|---|---|---|
| **Figma Make kits** | npm package, library variables and styles, a guidelines folder; or "start from scratch" by prompting components; attachments (PDF, MD, CSV/JSON, screenshots, SVG, video) | Published kit: packages, simplified CSS from library styles, `guidelines/` (Guidelines.md, setup.md, tokens or foundations, components with when-to-use and variant decision trees, composition) | Author writes or generates guidelines; tests by prompting; publishes | Full seat on paid plans; extracted CSS "won't capture every design detail"; token quirks break code unless documented; long guidelines flood context, so Figma recommends many short files | 2026-09-21 | [S-L17-200] [S-L17-211] [S-L17-212] |
| **Figma agent in Figma Design** (style-guide agent, brand-guidelines page) | A connected library, screens, prompts; for brand guidelines, a prose brand description | Canvas docs pages, variable scales (for example 0-1000 color scales from a screen's core colors), styles, components; brand guidelines (type, color, components, usage, voice, logo spacing, accessibility) | Everything editable; undo in chat; the agent as a pre-publish reviewer | Beta; edits need a Full seat; credits vary; quality depends on component descriptions | 2026-09-23 | [S-L17-207] [S-L17-209] [S-L17-257] [S-L17-259] |
| **Figma MCP skill `figma-generate-library`** | Codebase tokens and components, the target Figma file, subscribed libraries | Variable collections (primitives, semantic aliases, modes, scopes, code syntax), styles, page skeleton (Cover, Getting Started, Foundations, Components, Utilities), docs pages, component sets, Code Connect | Phase 0 discovery prints a gap analysis and locks v1 scope before any write; code-vs-Figma conflicts shown side by side with provenance and a recommendation; checklists per phase | "NEVER a one-shot task" (skill's words); writes are sequential; needs a write-capable seat; published as an example skill | 2026-09-22 | [S-L17-210] [S-L17-256] [S-L17-258] |
| **v0 Design Systems 2.0** | Up to 3 GitHub repos, Figma frames, Storybook or doc links, screenshots, ZIP, .tgz, notes on providers and deprecated components | Starter app, a "skill" that points at the sources, `v0.json` | Pauses for review before saving | Consumes an existing system (no from-scratch path found); will not use components, props or tokens it cannot verify | 2026-09-23 | [S-L17-201] |
| **Lovable** | React component source, tokens, docs (PDF, MD, screenshots); npm wrapper on Enterprise | `design-system.json`, a hand-authored `system.md`, `rules/*.md`; three rendered directions before a first build | Inspect and fix the generated files, re-release with a version bump | React only; one system per project; Themes launched Nov 2025 and were removed Mar 2026 "due to low usage and performance issues" | 2026-09-21 | [S-L17-202] [S-L17-233] [S-L17-234] |
| **Bolt Design System Agents** | Files (up to 10), a public docs URL, public GitHub, Storybook URL, npm (private token), agent instructions | A generated Storybook (collections, pages, light/dark, states) that apps build from | Review, refine instructions, resync, pick a revision | Team plan; 10 adds or syncs per team per week; 45-60 minutes per run; a docs site alone yields "a theme rather than a true design system"; conflicting or mixed-framework sources degrade output | 2026-09-23 | [S-L17-203] [S-L17-206] |
| **Google Stitch + DESIGN.md** | Prompt with "vibe" adjectives, images, voice, a URL; DESIGN.md import; via official skills, source code or project screens | DESIGN.md (tokens plus prose), an applied design system, screens, HTML/CSS; MCP tools to create, apply and list systems | The official skill must confirm name, key colors, fonts and roundness with the user before upload | URL-extraction docs are JavaScript-only, so reliability is undocumented; DESIGN.md is alpha; Google's own taste skill bans "AI Purple/Blue Neon" and Inter as defaults | 2026-09-14 | [S-L17-213] [S-L17-215] [S-L17-216] [S-L17-217] [S-L17-218] |
| **Relume Style Guide Builder** | An existing sitemap and wireframes; brand colors and fonts, or AI suggestion | Brand, accent and neutral colors, heading/body fonts, button, card and form settings; Figma kit styles and Webflow style guide | Surprise me, shuffle, lock fonts; used to present concepts | Marketing-site scope; the light/dark toggle inverts colors rather than defining modes; beta since Nov 2024 | 2026-09-23 | [S-L17-221] [S-L17-222] [S-L17-223] |
| **Magic Patterns Design System Agent** | GitHub, ZIP, npm, Figma, website, prompt or pasted screenshot; colors as CSV or Figma variables JSON; free-text Rules | Components, type and icon sets, color tokens with dark mode, Rules, versioned publishes | Review imports before they land; assign color groups to modes | An engineering-grade system is "not fully self-serve" (sales call); Rules are free text | 2026-09-23 | [S-L17-204] [S-L17-205] |
| **UX Pilot** | Prose descriptions, a Figma library, brand details | Components, Figma export, code | Follow-up prompts; Enterprise "design system as a service" with model fine-tuning | Marketing-level evidence only | 2026-09-23 | [S-L17-230] [S-L17-231] |
| **Uizard** (Theme Generator, Brand Kits) | Prompt, screenshot, URL or manual picks | Theme (colors, font style, shadows, borders); Brand Kit (colors, fonts, logos, icons, components) | Preview with a before/after toggle, then apply | Theme settings not editable after apply; project-scoped; Brand Kits on Business plan; help article dated Jul 2024 | 2024-07-09 | [S-L17-224] [S-L17-225] [S-L17-226] |
| **Motiff** | Prompts, images, PDFs, markdown, screenshots, preset stylings | UI plus React/HTML | Select-and-describe edits | **Discontinued**; data export until 31 Oct 2026 | 2026-09-23 | [S-L17-227] [S-L17-228] [S-L17-229] |
| **Subframe** | Manual theme building; an "Ask AI" prompt; token import | Theme tokens (colors, type, borders, corners, shadows) as a Tailwind config; components synced by CLI | AI theme change previews, then Apply; 1-4 variations as real pages; version history; find usages before renaming | AI theme edits hit the whole project; React and Tailwind only | 2026-09-23 | [S-L17-235] |
| **tweakcn** | Text prompt, image or SVG, a base theme, about 40 manual inputs | shadcn CSS variables (light/dark), Google fonts, radius, shadows, letter spacing | Asks 1-2 questions when input is unclear; manual editing with undo | Solid colors only, hex only; shadcn only; exists because shadcn sites "famously look the same" and tells its model to commit to a direction | 2026-09-03 | [S-L17-232] |
| **Claude Design** | Codebases, design files, screenshots, decks, PDFs, logos, palettes, type specimens | An organization design system (colors, type, components, layout and spacing); `/design-sync` from code | Validate with test prompts, then publish; admins approve and lock; output checked against the system before display | Paid plans only | 2026-06-17 | [S-L17-219] [S-L17-220] |

### E1. DESIGN.md and other rule-file conventions
- **Google's DESIGN.md spec** (github.com/google-labs-code/design.md; created 10 Apr 2026, open-sourced as a draft 21 Apr 2026, v0.4.0 on 27 Jul 2026, status "alpha", Apache-2.0): YAML front matter (`version`, `name`, `description`, `colors`, `typography`, `rounded`, `spacing`, `components` with a fixed property list) and eight ordered body sections (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts). Its CLI lints 11 rules (broken references, contrast below AA 4.5:1, missing primary color, orphaned tokens, section order and others), diffs, and exports Tailwind v3/v4 and DTCG. Its philosophy: prose carries intent, tokens support it [S-L17-213] [S-L17-217]. As read, it has no keys for modes, motion, icons, imagery, voice or breakpoints [inferred from the schema; S-L17-213], which is why gstack adds Motion and a Decisions Log [S-L17-004].
- **Variants of the idea:** Stitch's older prose-first skill format (visual theme, palette and roles, typography rules, component stylings, layout principles) and a taste variant with dials and banned lists [S-L17-218]; the community awesome-design-md collection (117k stars) adds Responsive Behavior and an Agent Prompt Guide and ships preview HTML, but its files are extracted from real brands with no trademark disclaimer found (Tier C) [S-L17-236]; Figma Make kit `guidelines/` (many short files) [S-L17-200]; Lovable `system.md` plus `design-system.json` [S-L17-202]; v0 skill plus `v0.json`, Magic Patterns Rules, Bolt agent instructions, Polymet rules and design files [S-L17-201] [S-L17-205] [S-L17-206] [S-L17-250]. Every tool pairs prose rules with tokens.

### E2. Patterns across the AI tools [inferred from the rows cited]
1. **Code beats prose as a source.** Bolt ranks repos and npm above docs sites; Magic Patterns pairs a visual source with a code source; v0 refuses what it cannot verify [S-L17-206] [S-L17-205] [S-L17-201].
2. **Creation runs as scan, propose, review, publish, version** (v0, Magic Patterns, Claude Design, Lovable, Bolt, the Figma skill, Stitch's skill) [S-L17-201] [S-L17-205] [S-L17-219] [S-L17-202] [S-L17-206] [S-L17-210] [S-L17-218].
3. **Generating from nothing yields a theme, not a system.** Relume, Uizard, tweakcn, Subframe, Polymet Auto and Motiff presets produce color, type, radius and shadow; none produces accessibility targets, usage rules or governance. Lovable removed Themes and Motiff shut down [S-L17-222] [S-L17-225] [S-L17-232] [S-L17-235] [S-L17-250] [S-L17-234] [S-L17-229]. This is the gap Kunal's guided builder fills, consistent with L11's finding that no competitor walks a person through the decisions.
4. **Vendors admit a default look.** Google bans purple neon and Inter in its taste skill; Anthropic lists five clusters; tweakcn exists because shadcn sites look alike; NN/g found the same generic sans-serif, shadcn-and-Tailwind look across 10 tools [S-L17-218] [S-L17-021] [S-L17-232] [S-L17-120].
5. **Verification is narrow.** Lovable scans for raw literals and one-off values, the DESIGN.md linter checks references and AA contrast, the Figma skill audits contrast, naming and unbound values, Dembrandt checks WCAG and drift. None checks coverage against a full ontology of building blocks [S-L17-202] [S-L17-213] [S-L17-210] [S-L17-237].
6. **Human-in-the-loop takes a few forms:** pick one of N, preview then apply with before/after, forks with provenance and a recommendation, admin approve and lock, undo in chat [S-L17-233] [S-L17-235] [S-L17-225] [S-L17-210] [S-L17-220] [S-L17-259].
7. **Gating shapes who can make a system:** React-only (Lovable), React + Tailwind (Subframe), Team plans and weekly quotas (Bolt), Full seats (Make kits), sales calls (Magic Patterns engineering systems, UX Pilot) [S-L17-202] [S-L17-235] [S-L17-206] [S-L17-211] [S-L17-205] [S-L17-231]. An open-source, model-agnostic builder avoids all of these by design [inferred].
8. **The closest precedent for the builder's process is Figma's own `figma-generate-library` skill**: discovery and a printed gap analysis before writing, locked scope, foundations before components, forks presented with provenance and a recommendation, and a QA phase auditing contrast, naming and unbound values [S-L17-210]. It starts from an existing codebase, though; the builder has to support starting from nothing.

---

## Part F. Reference intake: what can be read from a URL, screenshot or Figma file, and the ethics

### F1. How the two local extractor skills and gstack read a reference (internal references)
- **design-system-extractor** splits a site into seven layers, each with its own true source: structure (live DOM and computed layout), tokens (CSS custom properties, computed styles), components (bundled CSS and computed styles on real nodes), motion (behavior over time plus keyframes and library detection), interaction (clicking, hovering, resizing), narrative and value proposition (reading the page as a pitch), and assets (download plus analysis). Its core rule: "Never guess a layer you can observe." Static HTML exposes about two of the seven layers; without a live browser, motion, interaction and value proposition come out incomplete and the skill says so [S-L17-022].
- **site-soul-extractor** extracts five layers with surface last on purpose: positioning, voice, signature, rhythm (including animation), then surface (palette, type, grid, spacing, radius, texture). Every surface choice must trace back to a reason in the first four layers, or it is decoration. It requires a capture manifest (HTML, CSS, a scroll strip of screenshots at 100-160px steps, a motion dump, a section map ending at the footer) before any opinion is formed [S-L17-023].
- **gstack `/design-review`** reads the design system actually rendered on a page with in-page scripts: font families, text and background colors, heading sizes and weights, and touch targets under 44px, capped at 500 elements. It flags more than 3 families or more than 12 non-gray colors and offers to save the result as a DESIGN.md baseline [S-L17-008]. gstack's `extract` reads colors, type, spacing and mood from an image with a vision model [S-L17-014].

### F1b. Extractor tools that exist today (helper H2)

| Tool | Input | What it extracts | Reliability and limits (official) | Ethics notes | Evidence |
|---|---|---|---|---|---|
| **Dembrandt** (open-source CLI) | URL rendered in Playwright; multi-page crawl, dark mode and mobile flags | Logo, colors (including CSS variables and gradients), typography with font file URLs, spacing, borders, shadows, motion durations and easing, breakpoints, icons; exports DTCG, Tailwind v4, shadcn, DESIGN.md; WCAG checks on real DOM pairs; a CI drift gate | Hover and focus read from CSS, not by interacting; canvas and WebGL sites unreadable; dynamic content can be missed | The only tool found that forbids reproducing third-party identities, logos and trademarks; own or permitted sites only | [S-L17-237] |
| **Firecrawl `branding` format** (API) | URL | Color scheme, logo, colors, fonts, type sizes, spacing, radius, button and input styles, icons, animations, layout, and "personality" (tone, energy, audience) | v2 (6 Feb 2026) fixed logos in background images and Wix/Framer sites; no accuracy numbers published; personality fields are interpretive [inferred] | None found | [S-L17-238] [S-L17-239] |
| **Brandfetch Brand API** | Domain, email, ticker | Logos (light/dark), icons, symbols, colors, fonts, images | Published coverage on 542 brands: any logo 95%, dark logo 87.5%, light 58.3%, symbols 33.4%, colors 97%; returns nulls rather than guesses | Assets belong to the brands; suitable for the person's own brand [inferred] | [S-L17-240] [S-L17-241] |
| **Figma code to canvas** | A running app or site | Editable layers bound to *existing* color, number and string variables | Binds only variables already in the file or added libraries; colors with opacity stay unbound; does not create a token set [inferred from S-L17-243] | None stated | [S-L17-243] |
| **html.to.design** | URL, HTML, ZIP, logged-in page via extension | Layers, auto layout, local styles and variables (colors, type, spacing, button and form styles), components with hover variants | Free 10 imports per 30 days; no mode handling stated | No guidance on third-party content found | [S-L17-245] [S-L17-246] |
| **Project Wallace** | URL, CSS files | Colors, font sizes and families, line heights, gradients, shadows, radii, animation durations and timing functions | Static CSS analysis: declared values, not what renders [inferred] | None stated | [S-L17-249] [S-L17-335] |
| **Stitch, Polymet, Superdesign, Uizard, Magic Patterns, Claude Design, tweakcn** | URL, screenshot or image | Colors, fonts, spacing, radius, button and input styles (varies by tool) | Stitch's URL extraction is documented only in its launch blog; Polymet keeps the screenshot in chat so the person sees what was read; Superdesign takes 60-120 s and continues without the extraction if it fails; tweakcn maps gradients to solid colors | None found | [S-L17-216] [S-L17-250] [S-L17-251] [S-L17-225] [S-L17-205] [S-L17-219] [S-L17-232] |

Across extractors, color, font family and size, radius, shadow and spacing values are read reliably; interaction states, modes, motion beyond CSS durations, component anatomy and variants, semantic roles and usage intent are weak or absent [inferred from the limits above]. Figma's own documentation makes the same point about agents reading components: without descriptions, an agent may not know when to use a component or its states [S-L17-261].

### F2. What can be extracted reliably, by reference type

Reliability ratings are this lane's synthesis of F1, the extractor rows in F1b and L16/L07 findings [inferred unless a row cites a source].

| Layer | Live URL (browser, computed styles) | Screenshot / image | Figma file (MCP read) | Code / tokens file | Brand book (PDF) |
|---|---|---|---|---|---|
| Color values | High: computed colors and CSS custom properties [S-L17-022] [S-L17-008] | Medium: pixel sampling; antialiasing, gradients and photos confuse it; roles are guesses | High: variables and styles (`get_variable_defs`, L16 A1) | High: exact | High for brand colors |
| Color roles (which color means what) | Medium: inferred from usage (buttons, links, borders) | Low | High when variables are semantically named | High when tokens are tiered | Medium |
| Typefaces | High for family names; the licence is not extractable and proprietary faces cannot be reused [S-L17-022] | Low: face identification is a guess | High | High | High, often with licence notes |
| Type scale, weights, line heights | High (computed) | Medium: ratios only, estimated | High | High | Medium |
| Spacing scale | Medium-high: sampled paddings and gaps, scale inferred by clustering | Low-medium | High if variables are used, otherwise sampled from auto layout | High | Rare |
| Radius, borders | High | Medium | High | High | Rare |
| Shadows, elevation | High (box-shadow strings) | Low | High (effect styles) | High | Rare |
| Breakpoints, grid, containers | High (media queries, computed widths) | Low (one width only) | Medium (frames per breakpoint) | High | Rare |
| Motion (durations, easing, choreography) | Medium, and only with a live browser observing over time; static HTML gives almost nothing [S-L17-022] [S-L17-023] | None | Partial (Figma motion and timing variables where used, L07/L16) | High if motion tokens exist | Rare |
| Component inventory | Medium: DOM patterns and class names | Medium: a vision model can list component types | High: component sets, variants and properties | High: component files, Storybook | Low |
| Interaction states | Partial: needs hovering, focusing, opening each control [S-L17-022] | None beyond what is visible | High if variants exist | High | None |
| Icons and imagery | Medium: files can be downloaded, the library can often be recognized, but licences are unknown | Low | High (components, exports) | High | Medium |
| Voice and tone | Medium: copy can be read and attributes inferred; the copy itself must not be reused [S-L17-023] | Low | Low | Low | High if the book has a voice section |
| **Intent, principles, brand meaning, audience, why a choice was made** | **Not extractable**; can only be guessed from the page as a pitch [S-L17-023] | Not extractable | Not extractable (unless documented in the file) | Not extractable (unless in ADRs or docs) | Partly, if the book states them |
| Unseen states, dark mode, error and empty states | Only if reachable without signing in | No | Only if designed | Only if implemented | Rarely |

**What this means for the builder** [inferred]:
- A reference is strongest for the *surface* layers (color values, type, spacing, radius, shadow, breakpoints) and weakest for *meaning* (intent, principles, audience, brand meaning). The builder should pre-fill the first and always ask for the second.
- Every extracted value carries its method and confidence: measured (computed style, variable, token), estimated (pixels, vision model), or inferred (usage pattern). Estimated values are shown as ranges or with a warning, and none is decided until the person accepts it.
- Motion needs a live browser and time. A builder that only fetches HTML should not claim to have extracted motion.
- Extracted colors must be re-validated in the new context: a reference's brand color on the new product's surfaces may fail the contrast target.

### F3. Ethics and the identity firewall
- **Copy structure and quality, never identity.** The builder carries the system (layout, rhythm, scales, component anatomy, motion character, quality bar) and never the identity layer: brand name, wordmark and logo, photography, video and illustration, verbatim copy, and proprietary typefaces. site-soul-extractor puts this boundary at the top of its precedence ladder, above even an explicit operator instruction, and calls reproducing identity "passing-off, not replication" [S-L17-023]. design-system-extractor logs every proprietary-font substitution and teaches the recipe with original copy [S-L17-022]. NN/g reaches the same conclusion from the product side: copying another brand's visual identity is not sustainable [S-L17-121]. BRIEF requirement 4 states it directly.
- **A reference's brand color is identity, not structure.** When a reference's accent is its brand color, the builder takes its *role and strength* (one saturated accent, used only on actions) rather than the hex value [inferred; consistent with QUESTIONNAIRE Q-ref-01].
- **Consent before fetching.** The person confirms each URL before anything is opened, and the builder never signs in to a competitor's site or bypasses a login or bot check [S-L17-003] [S-L17-022].
- **Data leaving the machine.** Sending screenshots or briefs to a third-party model is a data flow the person should approve once; gstack asks before sending a screenshot to OpenAI [S-L17-012].
- **Provenance is part of the output.** Both local skills open their outputs with "sources used and substitutions" [S-L17-023]; the builder's decision log does the same, so a team can see which values came from which reference.

---

## Part G. Building-block classification: who or what produces each block

### G1. The classes and the rule for assigning them

The unit is every leaf block in `synthesis/ONTOLOGY.md` (S1a, read 2026-09-23), excluding the `builder` meta layer, which describes the tool rather than the design system: **207 blocks**. Each block gets one **primary class** (how the builder should obtain a good value when the person supplies nothing) and optional **also** classes (other routes that work). The assignment is this lane's judgment [inferred], grounded in the Decision Card or lane named in the Basis column.

| Class | Code | Meaning | What the builder does |
|---|---|---|---|
| **Generatable** | G | Derived by rule or formula from a few inputs: the raw inputs and eight dials in `synthesis/LEVERS.md` (brand color, typeface, base size, platforms, contrast target; Expression, Brand presence, Density, Energy, Roundness, Depth, Colorfulness, Warmth), or shipped as a sourced default | Decides silently with a default (gstack's "Mechanical" class [S-L17-015]); shows it visually with use/avoid detail; the person adjusts |
| **Extractable** | E | The best source is something that already exists: the person's logo, brand book, live product, repo or Figma file, read reliably | Reads it at intake, shows each value with its provenance, asks the person to accept, adjust or ignore |
| **Designer-owned** | D | Needs a human creator for acceptable quality (identity assets, art direction, sound) | Opens a hook: "Do you have this?", accepted formats, validation, fallbacks, a briefed placeholder slot |
| **Tool-assisted** | T | An engineer can produce it with a named tool or library, with caveats (licence, platform API, review by a specialist) | Recommends the tool, runs or links it where possible, states the caveat, records the choice |
| **Owner input** | I | A decision only the product owner or team can make (scope, platforms, governance); it is not a creative artifact and not derivable | Asks it, pre-filled where the repo or a reference hints at the answer; never invents it |

The fifth class (I) is an addition to the four classes in the task. Without it, 29 blocks (scope, platform posture, governance, terminology and so on) would have to be misfiled as "designer-owned" or "generatable", and neither is true: they are business decisions, which gstack also separates as "User Challenge" decisions that are never auto-decided [S-L17-015] [inferred]. See DC-L17-01.

### G2. Counts

| Class | Primary count | Share of 207 |
|---|---|---|
| Generatable (G) | **135** | 65% |
| Tool-assisted (T) | **31** | 15% |
| Owner input (I) | **29** | 14% |
| Designer-owned (D) | **7** | 3% |
| Extractable (E) | **5** | 2% |
| *Extractable as any route (primary or also)* | *44* | *21%* |

By layer: Context 10 I + 2 E; Principles 10 G + 5 I; Foundations 74 G, 16 T, 7 D, 2 E, 1 I; Tokens 12 G, 2 I, 1 T; Components 15 G, 2 I, 2 T, 1 E; Patterns 14 G, 4 T; Guardrails 3 G, 1 T, 1 I; Delivery 5 G, 6 T, 1 I; Governance 7 I, 2 G, 1 T (counted by script from the table below).

What the counts say [inferred]:
- **Two thirds of the system is generatable.** Kunal's instinct in the brief holds: paddings, margins, primitives, tokens, most components and patterns follow from a handful of inputs and dials. These blocks need visual editing and teaching, not creation.
- **Only 7 ontology nodes are designer-owned, but they are the ones people notice first**: brand marks, photography, illustration, rich media and motion signature, graphic motifs, pictograms and spot icons, and sound. They expand into the 14 asset hooks in Part H2 (logo, app icon, favicon, icons, illustration, photography, brand typeface, brand colors, motion, motifs, sound, haptics, voice guide, brand book).
- **Extraction is a route, not a class.** Only 5 blocks are best obtained by extraction (the existing inventory, the stack, the brand color, the component inventory, brand gradients), but 44 blocks can be pre-filled from a reference. Extraction pre-fills; it does not decide (see Part F).
- **The tool-assisted blocks cluster in four places**: typography sourcing and delivery, icons, content and voice drafting, and the delivery pipeline (token build, Figma variables, Code Connect, Paper, Penpot). Each has a named tool and a caveat.

### G3. The full table

Codes: G generatable, E extractable, D designer-owned, T tool-assisted, I owner input. "Hook" names the Part H hook (H-...) or R for reference intake (Part F). Basis cites the Decision Card or lane whose default or formula the classification relies on.

**Context and inputs** (12 blocks: E 2, I 10)

| Block | Name | Class | Also | Basis | Hook |
|---|---|---|---|---|---|
| `ctx.strategy` | Starting point and system posture | I | - | Adopt/adapt/create is a business choice (DC-L11-01) | - |
| `ctx.scope` | Scope: products, audience and stack | I | - | Products, audience, stack (DC-L11-02) | - |
| `ctx.inventory` | Existing UI inventory (audit) | E | T | Crawl the existing product; CSS stats; Figma file read (DC-L11-04) | R |
| `ctx.platforms.posture` | Platform posture (native-first, brand-first or hybrid) | I | - | Native-first vs brand-first (DC-L10-02) | - |
| `ctx.platforms.sharing` | What is shared across platforms | I | - | Tokens vs components vs principles shared (DC-L10-03) | - |
| `ctx.platforms.devices` | Device classes in scope | I | - | Device tiers (DC-L14-01) | - |
| `ctx.platforms.stack` | Implementation stack | E | I | Read from repo manifests; confirm (Q-plat-08) | R |
| `ctx.platforms.os-floor` | OS version floor | I | - | OS support policy | - |
| `ctx.brand.personality` | Brand personality profile | I | E | Sliders; a reference can be placed on the map (DC-L06-02) | R |
| `ctx.brand.layering` | Brand-to-product layering | I | - | Brand-to-product layering (DC-L06-01) | - |
| `ctx.brand.expression` | Expressiveness level and hero-moment budget | I | G | Hero-moment budget; follows Expression dial (DC-L06-03) | - |
| `ctx.constraints` | Hard constraints | I | - | Legal, tech, deadline limits | - |

**Principles** (15 blocks: G 10, I 5)

| Block | Name | Class | Also | Basis | Hook |
|---|---|---|---|---|---|
| `prin.design` | Design principles | I | T | Owner ranks principles; model drafts from interview (DC-L06-15) | - |
| `prin.ux.laws` | Laws of UX catalog | G | - | Shipped knowledge (L13 catalog) | - |
| `prin.ux.heuristics` | Heuristic consensus set | G | - | Shipped knowledge (L13) | - |
| `prin.ux.rules` | Behavior-rule model and automation boundary | G | - | Behavior-rule defaults (L13 Part E3) | - |
| `prin.ux.timing` | Response-time ladder | G | - | Response-time ladder (L13) | - |
| `prin.ux.familiarity` | Convention versus novelty | I | - | Convention vs novelty stance | - |
| `prin.ux.inclusion` | Inclusive design stance | I | G | Stance; default inclusive policy | - |
| `prin.ux.ethics` | Deceptive-pattern policy | I | G | Deceptive-pattern policy; default is none allowed | - |
| `prin.visual.style` | Visual style direction | I | E | Style preset picked from variants or a reference (DC-L15-01) | R |
| `prin.visual.hierarchy` | Hierarchy strength and emphasis budget | G | - | Lint numbers (DC-L15-02) | - |
| `prin.visual.grouping` | Grouping strategy | G | - | Inner gap < outer gap by construction (L15) | - |
| `prin.visual.composition` | Composition, balance and alignment | G | - | Rules + lint (L15) | - |
| `prin.visual.signifiers` | Interactive signifier strength | G | - | Strength follows Expression/Depth dials (L15) | - |
| `prin.visual.polish` | Optical correction and polish | G | T | Optical corrections as rules; some need manual nudge (L15) | - |
| `prin.visual.aesthetics` | Aesthetics and complexity readouts | G | - | Computed readouts (L15) | - |

**Foundations** (100 blocks: D 7, E 2, G 74, I 1, T 16)

| Block | Name | Class | Also | Basis | Hook |
|---|---|---|---|---|---|
| `found.color.space` | Color space and gamut | G | E | Default OKLCH/HCT (DC-L01-01) | - |
| `found.color.ramp` | Ramp generation and step meaning | G | E | Formula from seed (DC-L01-03) | - |
| `found.color.neutral` | Neutral ramp | G | E | Tinted from brand hue by Warmth dial (LEVERS) | - |
| `found.color.alpha` | Transparent (alpha) colors | G | - | Derived from ramps | - |
| `found.color.brand` | Brand and accent color | E | I | From logo, brand book or reference; else picked (DC-L06-04) | H-color |
| `found.color.character` | Palette character (chroma and scheme variant) | G | E | Colorfulness dial (LEVERS A0) | - |
| `found.color.roles.surface` | Surface roles | G | - | Mapped from ramps | - |
| `found.color.roles.foreground` | Foreground and text colors | G | - | Mapped from ramps + contrast target | - |
| `found.color.roles.status` | Status and feedback colors | G | - | Hue rules + contrast | - |
| `found.color.roles.border` | Border, outline and focus colors | G | - | Mapped + 3:1 non-text contrast | - |
| `found.color.states` | Interaction state colors | G | - | State-layer opacity formula | - |
| `found.color.modes.dark` | Dark mode mapping | G | E | Separate mapping (DC-L01-18); review needed | - |
| `found.color.modes.contrast` | Accessibility color themes | G | - | High-contrast remap | - |
| `found.color.modes.appearance` | Appearance modes by platform and device | G | - | Platform rules | - |
| `found.color.personalization` | Dynamic and personalized color | T | - | Platform dynamic-color APIs (DC-L01-21) | H-tokens |
| `found.color.contrast` | Contrast and color independence | G | - | Validator (DC-L01-22) | - |
| `found.color.expressive` | Gradients and expressive color | E | D | Brand gradients from brand book/reference; else designer (L01) | H-motif |
| `found.type.typeface.sourcing` | Typeface sourcing and platform mapping | T | D | Pick verified open/system faces; custom face is a hook (DC-L02-01) | H-type |
| `found.type.typeface.personality` | Typeface classification and personality | G | E | Suggested from personality dials (DC-L02-02) | - |
| `found.type.typeface.families` | Families, pairing and monospace | T | E | Pairing from a short verified list (DC-L02-03) | H-type |
| `found.type.typeface.axes` | Variable axes and optical sizing | G | - | Settings if variable (DC-L02-04) | - |
| `found.type.typeface.delivery` | Font licensing and loading | T | - | Licence check, subsetting, loading | H-type |
| `found.type.roles` | Type roles and emphasis | G | - | Role set from platform + density | - |
| `found.type.scale` | Type scale | G | E | Ratio formula (Expression dial) | - |
| `found.type.metrics` | Text metrics | G | E | Line height/tracking by size | - |
| `found.type.text-layout` | Text layout (measure, alignment, casing, truncation) | G | - | Measure, alignment rules | - |
| `found.type.responsive` | Responsive and device-distance type | G | - | Fluid clamp formula | - |
| `found.type.scaling` | Text scaling and legibility | G | - | Dynamic Type / font scale rules | - |
| `found.type.numerals` | Numerals | G | - | OpenType feature settings | - |
| `found.space.base` | Base spacing unit | G | E | Base unit (DC-L03-01) | - |
| `found.space.scale` | Spacing scale | G | E | Progression (DC-L03-02) | - |
| `found.space.semantic` | Semantic spacing (inset, gap, layout) | G | E | Inset/gap/layout aliases | - |
| `found.space.responsive` | Responsive spacing | G | - | Formula by breakpoint | - |
| `found.space.whitespace` | Whitespace personality and grouping | G | E | Density dial | - |
| `found.space.rhythm` | Vertical rhythm | G | E | Baseline rule | - |
| `found.space.sizing.controls` | Control height scale | G | E | Control heights from density | - |
| `found.space.sizing.media` | Icon and avatar size scales | G | E | Icon/avatar size steps | - |
| `found.space.density.voice` | Density voice and base size | G | E | Density dial (DC-L15-04) | - |
| `found.space.density.strategy` | Density strategy and modes | G | - | Modes from platforms | - |
| `found.space.density.context` | Density by device class | G | - | By device class (L14) | - |
| `found.layout.breakpoints` | Breakpoints | G | E | Breakpoint set (DC-L03-14) | - |
| `found.layout.grid` | Column grid | G | E | Columns/gutters by breakpoint | - |
| `found.layout.containers` | Containers and maximum content width | G | E | Max widths | - |
| `found.layout.adaptation` | Responsive and adaptive strategy | G | - | Canonical layouts by size class | - |
| `found.layout.safe-areas` | Safe areas, insets and edge policy | G | - | Platform insets | - |
| `found.interaction.modalities` | Input modalities | G | - | From device classes | - |
| `found.interaction.targets` | Target size and spacing | G | - | Input precision table (L14) | - |
| `found.interaction.focus` | Focus indicator | G | - | WCAG 2.2 focus appearance | - |
| `found.shape.radius` | Radius scale and default control radius | G | E | Roundness dial (DC-L04-01/02) | - |
| `found.shape.personality` | Roundness and brand shape language | G | E | Roundness dial | - |
| `found.shape.roles` | Radius roles per component | G | - | Radius per component size | - |
| `found.shape.geometry` | Corner geometry and nesting | G | - | Nesting formula (inner = outer - gap) | - |
| `found.shape.expressive` | Full-round and expressive shapes | T | D | Shape libraries; a signature shape is a designer asset (DC-L06-09) | H-motif |
| `found.shape.border` | Border widths and dividers | G | E | Width steps | - |
| `found.elevation.depth-model` | Depth model | G | E | Depth dial (DC-L04-10) | - |
| `found.elevation.scale` | Elevation levels | G | - | Levels | - |
| `found.elevation.shadow` | Shadow recipe | G | E | Layered shadow recipe | - |
| `found.elevation.surfaces` | Surface roles for elevation | G | - | Tonal surface mapping | - |
| `found.elevation.stacking` | Stacking order (z-index layers) | G | - | z-index layers | - |
| `found.elevation.materials` | Translucent materials | T | - | Platform material APIs (Liquid Glass, Mica) | H-tokens |
| `found.elevation.opacity` | Opacity, state layers and scrims | G | - | Scrim/state opacities | - |
| `found.motion.personality` | Motion personality and model | G | E | Energy dial (DC-L04-19); reference capture needs a live browser | - |
| `found.motion.duration` | Duration scale | G | E | Duration scale | - |
| `found.motion.easing` | Easing set | G | E | Easing set | - |
| `found.motion.springs` | Springs and physics | G | - | Spring presets from duration + bounce | - |
| `found.motion.interruptibility` | Enter and exit asymmetry and interruptibility | G | - | Rules | - |
| `found.motion.reduced` | Reduced motion | G | - | Reduced-motion mapping | - |
| `found.motion.platform` | Motion by platform and device class | G | - | Per platform | - |
| `found.sensory.haptics` | Haptic vocabulary | T | D | Platform haptic primitives; custom patterns need a designer | H-haptic |
| `found.sensory.sound` | UI sounds | D | T | UI sounds / sonic logo need a sound designer; system sounds as fallback | H-sound |
| `found.icon.source` | Icon library strategy | T | D | Library choice (DC-L05-01) | H-icons |
| `found.icon.style` | Icon style and brand match | G | E | Match stroke/fill to type and roundness (DC-L05-02) | - |
| `found.icon.construction` | Stroke, grid and keylines | G | D | Derived from type weight; custom set is a hook (DC-L05-03) | H-icons |
| `found.icon.sizes` | Icon sizes and optical sizing | G | - | Size scale (DC-L05-05) | - |
| `found.icon.states` | Icon states | G | - | State rules (DC-L05-06) | - |
| `found.icon.labels` | Icons with labels | G | - | Label pairing rules (DC-L05-07) | - |
| `found.icon.color` | Icon color and rendering mode | G | - | Color roles (DC-L05-08) | - |
| `found.icon.naming` | Icon metaphors, naming and localization | T | I | Metaphor search + human review (DC-L05-09) | H-icons |
| `found.icon.delivery` | Icon delivery | T | - | SVG sprite / component tooling (DC-L05-10) | H-icons |
| `found.icon.tiers` | Icon tiers beyond UI icons | D | T | Pictograms and spot icons (DC-L05-11) | H-icons |
| `found.icon.platform` | Icons across platforms | T | - | SF Symbols / Material mapping | H-icons |
| `found.imagery.photo` | Photography art direction | D | T | Art direction + photos (DC-L05-14) | H-photo |
| `found.imagery.ratios` | Aspect ratios and cropping | G | - | Ratio set (DC-L05-15) | - |
| `found.imagery.text-on-image` | Text and UI on images | G | - | Scrim + contrast check (DC-L05-16) | - |
| `found.imagery.loading` | Image loading and placeholders | G | T | Placeholder rules (DC-L05-17) | - |
| `found.imagery.illustration` | Illustration style and tiers | D | T | Style + tiers (DC-L05-19/20) | H-illus |
| `found.imagery.rich-media` | Emoji, 3D, animated icons and Lottie | D | T | Lottie, 3D, animated icons (DC-L05-21) | H-motion |
| `found.imagery.motifs` | Graphic devices and motifs | D | E | Graphic devices (DC-L06-11) | H-motif |
| `found.imagery.brand-marks` | App icon, logo and favicon | D | E | Logo, app icon, favicon (DC-L05-12/13) | H-logo |
| `found.dataviz.scope` | Chart scope and library | T | - | Chart library choice (DC-L05-22) | H-dataviz |
| `found.dataviz.color` | Data-visualization palettes | G | - | Palettes + CVD checks (DC-L05-23) | - |
| `found.dataviz.anatomy` | Chart anatomy and tokens | G | - | Chart tokens (DC-L05-24) | - |
| `found.content.voice` | Voice | T | E | Model drafts from personality; existing guide is read; content designer ideal (DC-L06-18) | H-voice |
| `found.content.tone` | Tone by situation | T | - | Tone matrix drafted, reviewed (DC-L06-19) | H-voice |
| `found.content.mechanics` | Grammar, mechanics and capitalization | G | - | Settings (DC-L06-20/21) | - |
| `found.content.microcopy` | Component microcopy | T | - | Patterns drafted per component, reviewed (DC-L06-22) | H-voice |
| `found.content.terminology` | Terminology and inclusive language | I | - | Word list is product knowledge (DC-L06-23) | - |
| `found.content.localization` | Localization readiness | T | - | i18n tooling + native review (DC-L06-24) | H-voice |
| `found.content.readability` | Readability and plain language | G | - | Readability lint | - |
| `found.content.scannability` | Content hierarchy for scanning | G | - | Structure rules | - |

**Tokens** (15 blocks: G 12, I 2, T 1)

| Block | Name | Class | Also | Basis | Hook |
|---|---|---|---|---|---|
| `tok.tiers` | Token tiers | G | - | DC-L07-01 | - |
| `tok.naming.primitives` | Primitive naming | G | - | Naming scheme | - |
| `tok.coverage` | Token coverage | G | - | Coverage check | - |
| `tok.types.color` | Color encoding | G | - | DTCG 2025.10 | - |
| `tok.types.dimension` | Dimension units | G | - | DTCG | - |
| `tok.types.typography` | Typography encoding | G | - | DTCG composite | - |
| `tok.types.shadow-border` | Shadow, border and elevation encoding | G | - | DTCG composite | - |
| `tok.types.motion` | Motion encoding | G | - | DTCG duration/cubicBezier | - |
| `tok.types.layout` | Layout and breakpoint encoding | G | - | Builder convention | - |
| `tok.types.extensions` | Builder extension types | G | - | Builder extension types (L05 note) | - |
| `tok.modes` | Modes and theming axes | G | - | From theming answers | - |
| `tok.themes.generator` | Theme-generator inputs | G | - | Raw inputs + dials (LEVERS) | - |
| `tok.themes.brands` | Multi-brand architecture | I | G | How many brands, what flexes (DC-L06-16) | - |
| `tok.themes.whitelabel` | White-label customization surface | I | - | Customer-facing surface (DC-L06-17) | - |
| `tok.delivery` | Platform delivery of tokens | T | - | Style Dictionary / Terrazzo transforms | H-tokens |

**Components** (20 blocks: E 1, G 15, I 2, T 2)

| Block | Name | Class | Also | Basis | Hook |
|---|---|---|---|---|---|
| `comp.inventory` | Component inventory scope | E | G | From audit or reference; else archetype defaults (L08) | R |
| `comp.taxonomy` | Hierarchy model and naming | G | - | Hierarchy model | - |
| `comp.implementation` | Build strategy and technology | I | T | Build vs adopt a headless library | - |
| `comp.api` | Component API (code and Figma) | T | - | Headless libraries + conventions | H-comp |
| `comp.device-variants` | Device variants of components | G | - | By device class | - |
| `comp.platform-rendering` | System controls versus custom controls | I | - | System vs custom controls (Q-plat-06) | - |
| `comp.states.disabled` | Disabled and unavailable actions | G | - | Default policy; surfaced as a question (L08 note) | - |
| `comp.states.loading` | Loading state | G | - | From motion + feedback rules | - |
| `comp.states.selected` | Selected and active state | G | - | From color states | - |
| `comp.behavior` | Microinteraction specification | G | T | Microinteraction spec from motion tokens | - |
| `comp.action.button` | Button hierarchy, content and destructive treatment | G | E | Hierarchy + tokens | - |
| `comp.input.field` | Form field style and label placement | G | E | Label placement + tokens | - |
| `comp.selection` | Selection components | G | - | - | - |
| `comp.navigation` | Navigation components | G | - | - | - |
| `comp.feedback.ai` | AI surfaces module | T | - | AI surface kits; fast-moving | H-comp |
| `comp.overlay` | Overlay components | G | - | - | - |
| `comp.containment.card` | Card and panel separation | G | E | Separation from depth model | - |
| `comp.data.avatar` | Avatars | G | - | Sizes/fallbacks (DC-L05-18); photos come from users | - |
| `comp.media` | Media components | G | - | - | - |
| `comp.layout` | Layout primitives and utilities | G | - | - | - |

**Patterns and templates** (18 blocks: G 14, T 4)

| Block | Name | Class | Also | Basis | Hook |
|---|---|---|---|---|---|
| `pat.forms.validation` | Validation timing and error presentation | G | - | - | - |
| `pat.feedback.loading` | Loading and wait feedback | G | - | Timing ladder | - |
| `pat.feedback.messaging` | Message channel selection | G | - | - | - |
| `pat.feedback.errors` | Error messages | G | T | Structure generated; copy reviewed | - |
| `pat.destructive` | Destructive actions: undo versus confirm | G | - | - | - |
| `pat.navigation.containers` | Navigation containers by size, platform and device | G | - | From platform + IA | - |
| `pat.overlay` | Modality and overlays | G | - | - | - |
| `pat.collections` | Long collections | G | - | - | - |
| `pat.disclosure` | Progressive disclosure | G | - | - | - |
| `pat.empty` | Empty states | T | D | Structure generated; illustration and copy are hooks | H-illus |
| `pat.onboarding` | Onboarding | T | - | Flow drafted from product context, reviewed | H-voice |
| `pat.ai` | AI and conversational patterns | T | - | Fast-moving patterns (L13/L08) | H-comp |
| `pat.glanceable` | Glanceable surfaces | G | - | - | - |
| `pat.layout.canonical` | Canonical layouts and panes | G | - | - | - |
| `pat.layout.shell` | App shell regions | G | E | - | - |
| `pat.motion` | Transitions and choreography | G | - | - | - |
| `pat.other` | Other product patterns | T | - | Product-specific patterns | H-comp |
| `pat.templates` | Page templates | G | E | - | - |

**Guardrails** (5 blocks: G 3, I 1, T 1)

| Block | Name | Class | Also | Basis | Hook |
|---|---|---|---|---|---|
| `guard.enforcement` | Rule enforcement and exported lint | G | - | - | - |
| `guard.checks` | Check catalog | G | - | - | - |
| `guard.critique` | Visual critique strictness | I | - | Strictness setting | - |
| `guard.safety` | Safety and distraction limits | G | - | Driving/distraction rules (L14) | - |
| `guard.testing` | Accessibility test matrix by device | T | - | axe + human assistive-tech walkthroughs | H-a11y |

**Delivery and tooling** (12 blocks: G 5, I 1, T 6)

| Block | Name | Class | Also | Basis | Hook |
|---|---|---|---|---|---|
| `deliver.source-of-truth` | Source of truth and round-trip direction | I | - | DC-L16-02 | - |
| `deliver.interchange` | Interchange format and file layout | G | - | DTCG 2025.10 files | - |
| `deliver.pipeline` | Token build pipeline | T | - | Build tooling | H-tokens |
| `deliver.packaging` | Distribution model | T | - | npm / registry | H-tokens |
| `deliver.channels` | Export and handoff channels | G | - | - | - |
| `deliver.ai` | Agent-readable distribution | G | - | DESIGN.md, llms.txt, rules files (L11 DC-L11-23) | - |
| `deliver.interop.figma.variables` | Collections, modes, scopes and publishing | T | - | use_figma (remote MCP, Full seat) or DTCG import | H-figma |
| `deliver.interop.figma.code-syntax` | Code syntax | G | - | - | - |
| `deliver.interop.figma.styles` | Styles versus variables | G | - | - | - |
| `deliver.interop.figma.code-connect` | Code Connect and AI readiness | T | - | Code Connect setup (Org/Enterprise) | H-figma |
| `deliver.interop.paper` | Paper | T | - | Paper MCP write_html/create_tokens | H-figma |
| `deliver.interop.penpot` | Penpot | T | - | Native DTCG import | H-figma |

**Governance, docs and adoption** (10 blocks: G 2, I 7, T 1)

| Block | Name | Class | Also | Basis | Hook |
|---|---|---|---|---|---|
| `gov.process` | Build order and pilot | I | - | - | - |
| `gov.team` | Team model and roles | I | - | - | - |
| `gov.contribution` | Contribution model | I | G | Template generated | - |
| `gov.decisions` | Governance flow and decision records | I | G | ADR template generated | - |
| `gov.lifecycle` | Component status labels | G | - | Default status labels | - |
| `gov.change.deprecation` | Deprecation and migration | I | - | - | - |
| `gov.docs.component-page` | Component documentation page | G | - | Generated page template (DC-L11-18) | - |
| `gov.adoption` | Rollout and communication | I | - | - | - |
| `gov.measure` | Metrics and maturity | I | - | - | - |
| `gov.tooling` | Governance tooling in Figma | T | - | Figma library analytics (plan-gated) | H-figma |

---

## Part H. Designer hooks and tool hooks (every D and T block)

Every block classed D or T in Part G, and the E blocks that depend on the person's own assets, maps to one hook below (the Hook column in G3). The hook ids line up with the asset-hook questions in `synthesis/QUESTIONNAIRE.md` (Q-brand-03, Q-color-01, Q-type-02, Q-icon-01, Q-icon-06, Q-img-01, Q-img-04, Q-img-06, Q-motion-08, Q-voice-01); this part adds formats, fallbacks and checks verified by helper H4 (90 sources, S-L17-500 to 589, 81 of them Tier A).

### H1. Rules that apply to every hook
1. **Ask once, as a grouped checklist (Stage 3), and keep slots open.** In Quick mode apply the fallback and leave a briefed placeholder (DC-L17-04).
2. **One vector master, generated derivatives.** Ask for the master (SVG or PDF with outlined text; layered SVG for app icons) and generate the platform sets from it, with automatic size and safe-zone checks [S-L17-500] [S-L17-502] [S-L17-503] [S-L17-505] [S-L17-506] [S-L17-507] [S-L17-508] (the generation pipeline itself is [inferred]).
3. **A licence ledger on every asset**: source, licence, attribution string, allowed slots, owner. The builder inserts required credits (Storyset), keeps ISC/MIT/Apache notices for icon libraries, and blocks assets from slots their licence forbids (Storyset and Blush art in logos) [S-L17-512] [S-L17-515] [S-L17-517] [S-L17-522] [S-L17-523] [S-L17-524].
4. **Fetch per project; never pool assets into a shared catalog.** Several licences ban offering their assets as a selectable library to a tool's users or compiling competing collections (ITF Free Font License, unDraw, Blush, Unsplash, Pexels) [S-L17-536] [S-L17-519] [S-L17-522] [S-L17-529] [S-L17-530] [inferred application to an open-source builder].
5. **AI fallbacks state the terms for the person's plan.** Who owns the output differs by tool and plan (Recraft's free tier gives ownership to Recraft; Midjourney requires Pro or Mega for companies over $1M revenue; OpenAI and Ideogram assign rights "if any" and say outputs may not be unique) [S-L17-525] [S-L17-531] [S-L17-532] [S-L17-533]. In the US, purely AI-generated material is not copyrightable: prompts alone are not enough, human selection, arrangement and modification can be [S-L17-559] [S-L17-560] [S-L17-561], and the Supreme Court denied review of Thaler v. Perlmutter on 2 Mar 2026 [S-L17-563]. The EU AI Act Art. 50 requires machine-readable marking of synthetic output (recheck the application date; the Commission notes pending amendments) [S-L17-578].
6. **The commission path ships a brief and a contract reminder.** The brief lists the required files and sizes from this part plus the system's tokens and direction; the reminder says a contractor's logo is not work made for hire unless it falls into one of nine statutory categories with a signed agreement, so a written copyright assignment is needed [S-L17-579]. Channels, by their own descriptions: Dribbble (job posts $150/month, 2-5% project fee), Contra (commission-free), Behance (Adobe; matching, fee waived for Behance Pro freelancers), 99designs (contests or 1-to-1; says copyright passes to the client) [S-L17-572] [S-L17-573] [S-L17-574] [S-L17-575]. No endorsement implied.
7. **A generated stand-in is never presented as final.** CSS-shape illustrations, stock heroes and generated mascots are the tells gstack and Anthropic catalog [S-L17-004] [S-L17-021]. NN/g adds that visibly handmade work now signals care [S-L17-125].

### H2. Asset hooks (designer-owned blocks)

| Hook | "Do you have this?" | Accepted formats | What the builder does with it | Fallbacks when the answer is no | Quality checks the builder can automate | Evidence |
|---|---|---|---|---|---|---|
| **H-logo** Logo, wordmark, symbol, lockups (`found.imagery.brand-marks`; Q-brand-03) | "Do you have a logo? Which versions: symbol only, horizontal and stacked lockups, one-color?" | Master SVG or PDF with text outlined (EPS legacy); derived transparent PNG in color, black and white | Places it in the app bar, sign-in and emails per the logo rules in DC-L05-13; proposes brand-color candidates from its fills; derives app icon, favicon and social image drafts | Commission a designer (brief + assignment reminder). AI logo generators (Looka, Brandmark) with caveats: Looka says its icons and fonts come from a shared database and stay available to others, and trademark filing needs an attorney; run a trademark search before adoption. Wordmark-only fallback: the brand name set in the chosen typeface (OFL, Google Fonts, Adobe Fonts and ITF FFL all allow fonts in logos) | SVG parses; no `<text>` nodes; no embedded raster in the master; viewBox present; SVGO pass; one-fill mono variant; legibility at 16 and 32px; renders on light and dark surfaces | [S-L17-534] [S-L17-535] [S-L17-536] [S-L17-537] [S-L17-564] [S-L17-565] [S-L17-566] [S-L17-567] [S-L17-568] |
| **H-appicon** App icon (part of brand marks; Q-icon-06) | "Do you have app icon artwork, ideally as layers?" | Apple: layers as SVG/PDF (preferred) or PNG, assembled in Icon Composer. Android: adaptive foreground, background and monochrome layers (vector preferred). Play: 32-bit PNG. PWA: PNG, WebP or SVG in the manifest | Builds each platform set from the layered master | Designer (brief lists the sizes below); Icon Composer (macOS Tahoe 26.4+); Android Studio Image Asset Studio; Maskable.app | Apple: 1024x1024 canvas (1088 watchOS; tvOS 800x480 with 2-5 layers); appearances Default, Dark, Clear and Tinted (the system generates missing ones); no custom shadows or bevels; no photos. Android: 108dp layers, 66dp safe zone, monochrome layer for themed icons (API 33+). Play: 512x512 sRGB PNG, 1024 KB or less, no pre-rounding. PWA: a maskable icon inside a centered circle of radius 40% | [S-L17-500] [S-L17-501] [S-L17-502] [S-L17-503] [S-L17-504] [S-L17-505] [S-L17-506] [S-L17-507] |
| **H-favicon** Favicon set (tool-assisted derivative) | Asked with the logo | Master SVG; derived ICO, PNGs, manifest | Generates the set from the symbol | Generated from the logo; SVGO, Squoosh, Inkscape | Files exist at stated sizes: favicon.ico 32x32, icon.svg with a dark-mode media query, apple-touch-icon 180x180, manifest 192 and 512 plus a 512 maskable | [S-L17-508] [S-L17-507] (L05 DC-L05-13) |
| **H-icons** Custom icons, pictograms, spot icons (`found.icon.*` T and D blocks; Q-icon-01) | "Do you have an icon set, or icons the libraries lack (domain objects, brand concepts)?" | SVG on the library's grid; icon font or sprite; SF Symbol template SVG; Android Vector Drawable | Matches stroke, corners and size scale to the typeface (DC-L05-03); ships icons as components; maps to SF Symbols on Apple platforms | Open libraries: Lucide (ISC; Feather-derived icons MIT), Phosphor, Tabler, Heroicons (MIT), Material Symbols (Apache 2.0), all keeping their notices; custom icons drawn on the Material 24dp keyline template or an exported SF Symbols template; IcoMoon and SVGO for packaging; Recraft vector output with its plan terms. Pictograms and spot icons: commission | viewBox matches the grid (for example 0 0 24 24); stroke width consistent with the chosen library; SF Symbols template validates (filled paths, no strokes, equal path counts); SVGO pass; licence file carried into the build; labels present (NN/g: 19 of 20 intranet icon sets were bad) | [S-L17-509] [S-L17-510] [S-L17-511] [S-L17-512] [S-L17-513] [S-L17-514] [S-L17-515] [S-L17-516] [S-L17-518] [S-L17-526] [S-L17-149] [S-L17-150] |
| **H-illus** Illustration, characters, empty-state art (`found.imagery.illustration`, `pat.empty`; Q-img-04) | "Do you have illustrations or a character style?" | Master SVG; derived PNG; animated as Lottie (see H-motion) | Records the style (DC-L05-19/20), places art in empty states and onboarding, tints to palette where the licence allows modification | Commission (brief with style references and palette). Open sets with exact terms: unDraw (free commercial, no attribution; bans AI training and competing packs), Open Peeps and Humaaans (CC0), Blush (free commercial; no resale or merchandise, no ownership claim), Storyset (free use must credit Storyset; no logos). AI: Recraft (SVG; paid tiers assign copyright) or Firefly (commercial use for non-beta features; indemnity only on qualifying plans). Or ship no illustration: honest text empty states | Valid SVG; licence ledger entry with attribution string; blocks Storyset or Blush art from logo slots; palette distance to brand tokens [inferred] | [S-L17-519] [S-L17-520] [S-L17-521] [S-L17-522] [S-L17-523] [S-L17-524] [S-L17-525] [S-L17-526] [S-L17-527] [S-L17-528] [S-L17-589] |
| **H-photo** Photography and art direction (`found.imagery.photo`; Q-img-01) | "Do you have photography, or a photo style you follow?" | Highest-resolution originals; derived responsive JPEG, WebP, AVIF [inferred] | Writes art-direction rules (DC-L05-14), sets ratios and crops, applies text-on-image scrims with contrast checks | Commission a photographer. Stock: Unsplash (free, irrevocable, commercial; no competing service) or Pexels (no implied endorsement, no use as a trademark). AI images: ownership and uniqueness caveats per tool; mark synthetic output under EU AI Act Art. 50; NN/g's 77-person test found AI images close to stock (only authenticity significant, small) but failing on visible artifacts and stereotypes | Minimum resolution per slot; source, licence and author stored; faces and logos flagged for release review [inferred]; Content Credentials metadata checked on AI images [inferred] | [S-L17-529] [S-L17-530] [S-L17-531] [S-L17-532] [S-L17-533] [S-L17-578] [S-L17-126] |
| **H-type** Brand typeface files (`found.type.typeface.sourcing`, `families`, `delivery`; Q-type-02) | "Do you have a brand typeface? Which licences do you hold: web, app embedding, self-hosting?" | OTF or TTF masters; WOFF2 for web (W3C Recommendation, supports variable fonts); variable fonts with registered axes (wght, wdth, ital, slnt, opsz) | Reads the font's own licence data, sets up loading, maps weights to roles, checks script coverage | Open faces: Google Fonts (OFL, Apache, UFL; self-host and use in apps and logos). Fontshare under ITF FFL v2.0 (17 Aug 2026): free commercial use and app embedding, but **no modification including subsetting or format conversion**, and it **may not be offered as a selectable font to third-party users of a design tool**. Adobe Fonts: web only through Adobe's embed code; no self-hosting; no embedding in native apps. Commercial foundries: buy web and app licences. Platform faces (SF Pro, Roboto) for native-first products | Read name IDs 0, 7, 13, 14 and OS/2 fsType; refuse subsetting when fsType 0x100 is set or the licence is ITF FFL; detect variable fonts (fvar table); confirm the WOFF2 signature | [S-L17-534] [S-L17-535] [S-L17-536] [S-L17-537] [S-L17-538] [S-L17-539] [S-L17-540] [S-L17-576] [S-L17-577] |
| **H-color** Fixed brand colors (`found.color.brand`, E; Q-color-01) | "Do you have brand colors that must be exact?" | Hex, RGB, OKLCH, Pantone references, Figma variables JSON, CSS | Locks them as the seed; builds ramps and roles around them; flags where a locked color fails contrast in a role and proposes the nearest passing step for text use | Candidates from the logo or brand book; otherwise picked in Stage 4 with the Colorfulness and Warmth dials | Contrast of each role against its surfaces in every mode; gamut check for P3 values [inferred] | DC-L06-04; [S-L17-571] |
| **H-motion** Motion signature and rich media (`found.imagery.rich-media`; Q-img-06) | "Do you have animations: a logo animation, loaders, animated illustrations, 3D?" | Lottie JSON; dotLottie (.lottie zip, v2 adds state machines and theming); After Effects via Bodymovin; Rive .riv with state machines; glTF/GLB; USDZ | Places them in the one authored motion moment the direction allows; wires reduced-motion alternatives | Commission a motion designer; otherwise motion comes from the system's motion tokens only (no signature animation); LottieFiles-format community assets under their stated licences | Validate Lottie against the published JSON Schema; reject layer types lottie-web cannot render (image sequences, video, audio); size, fps and duration budgets; glTF Validator; a reduced-motion alternative exists | [S-L17-541] [S-L17-542] [S-L17-543] [S-L17-544] [S-L17-545] [S-L17-546] [S-L17-556] [S-L17-557] [S-L17-558] |
| **H-motif** Graphic devices, patterns, textures, brand gradients, signature shape (`found.imagery.motifs`, `found.color.expressive`, `found.shape.expressive`) | "Do you have brand patterns, textures, gradients or a signature shape?" | SVG patterns; gradient definitions; shape SVG | Records them as brand-expression tokens and assets with the allowed surfaces (hero moments only, per the Expression dial) | Commission; or none (NN/g and gstack both warn that decoration standing in for content reads as generic) | Contrast of text over gradients and textures; usage limited to allowed surfaces | [S-L17-004] [S-L17-021] DC-L06-11 |
| **H-sound** UI sounds and sonic logo (`found.sensory.sound`; Q-motion-08) | "Do you have UI sounds or a sonic logo?" | Apple notification sounds: Linear PCM, IMA4, µLaw or aLaw in .aiff, .wav or .caf, under 30 seconds. Android decodes Ogg (Vorbis, Opus), WAV, MP3, AAC, FLAC | Maps sounds to semantic events; respects silent mode | Commission a sound designer. Otherwise use platform system sounds (Android `SoundEffectConstants`; iOS system behavior) or no sound. The official Material sound resources page now returns 404 and the only mirror has conflicting licence metadata, so it is not offered; no verified open UI-sound library was found | Codec, container and duration checks; loudness normalization [inferred]; silent-switch behavior | [S-L17-550] [S-L17-551] [S-L17-552] [S-L17-553] [S-L17-554] [S-L17-555] |
| **H-haptic** Custom haptic patterns (`found.sensory.haptics`, T) | "Do you need custom haptic patterns, or are system patterns enough?" | Apple AHAP (.ahap JSON: transient and continuous events, intensity and sharpness 0-1, curves); Android `VibrationEffect` compositions | Maps semantic haptic tokens to platform constants | System patterns first (Apple: notification, impact, selection; Android: `HapticFeedbackConstants`, no permission needed; composition primitives only where supported) | Lint AHAP (values 0-1; unknown keys are ignored and out-of-range values clamped, so warn); fallback when primitives are unsupported | [S-L17-547] [S-L17-548] [S-L17-549] |
| **H-voice** Voice and tone guide (`found.content.voice`, `tone`, `microcopy`, `localization`, `pat.onboarding`; Q-voice-01) | "Do you have a voice and tone guide or a word list?" | PDF, Markdown, Google Doc export, existing product copy | Extracts voice attributes and rules; drafts the tone matrix and microcopy in that voice | Model drafts voice from the personality answers, marked as a draft until a content designer or owner reviews it; terminology stays owner input | Readability lint; banned-word list; capitalization and mechanics settings applied consistently | DC-L06-18 DC-L06-19; [S-L17-110] |
| **H-brandbook** Brand guidelines PDF (reference intake, E) | "Do you have a brand book?" | PDF | Extracts candidate color tokens from vector fills and text colors, font names, embedded logo images; asks for the SVG master of any logo found | n/a | Text, fonts, colors and vector fills are extractable with PyMuPDF; a PDF cannot become editable Figma layers (Figma import does not list PDF; the Figma agent reads PDFs as reference only, 5 MB) | [S-L17-569] [S-L17-570] [S-L17-571] |

### H3. Tool hooks (tool-assisted blocks that are not identity assets)

| Hook | Blocks | Question | Named tools | Caveat | Check | Evidence |
|---|---|---|---|---|---|---|
| **H-tokens** | `tok.delivery`, `deliver.pipeline`, `deliver.packaging`, `found.color.personalization`, `found.elevation.materials` | "Which platforms consume tokens, and how do you ship packages?" | Style Dictionary, Terrazzo, Tokens Studio (sync, themes on Pro); platform dynamic-color and material APIs | Only 40% of teams automate token sync; DTCG import into Figma is partial (L07) | Build output compiles; every semantic token resolves in every mode | [S-L17-342] [S-L17-347]; L07 |
| **H-figma** | `deliver.interop.figma.variables`, `code-connect`, `deliver.interop.paper`, `deliver.interop.penpot`, `gov.tooling` | "Which design tool and plan do you use?" (Q-tool-03) | Figma remote MCP `use_figma` or the `figma-generate-library` skill (Full seat); Tokens Studio; Paper MCP; Penpot native DTCG | Modes per collection 10 on Pro, 20 on Org; extended collections Enterprise only; Code Connect and analytics plan-gated | Collections within plan limits; scopes set (never all scopes); code syntax filled for each platform | [S-L17-210] [S-L17-337] [S-L17-338] [S-L17-339] [S-L17-340]; L16 A1 |
| **H-comp** | `comp.api`, `comp.feedback.ai`, `pat.ai`, `pat.other` | "Which component library or stack do you build on?" | Headless libraries and registries (Radix, Base UI, React Aria, shadcn registry) per L08 | AI surfaces and product-specific patterns change fast; review against WAI-ARIA APG | Keyboard and ARIA tests per component; states matrix complete | L08 (DC-L08-03, DC-L08-04) |
| **H-dataviz** | `found.dataviz.scope` | "Do you show charts? Which library?" | Chart libraries per L05 DC-L05-22 | Library defaults override tokens unless themed | Chart palette passes CVD and contrast checks | DC-L05-22 DC-L05-23 |
| **H-a11y** | `guard.testing` | "Who tests with assistive technology?" | axe-core and lint rules for automated checks; human screen-reader walkthroughs | Automated tools catch only part of WCAG; human testing remains | Automated checks in CI; AT walkthrough recorded | [S-L17-023]; L11 DC-L11-19 |

---

## Part I. The proposed process: what the model runs with the person, stage by stage

Written for OpenDesigner as a process any capable model (Claude, ChatGPT, Codex) runs with a person, per BRIEF requirements 6-11. How it is packaged and which host surfaces it uses (skills, MCP, visual UI in chat, artifacts) is lane L18's scope; this part says only what the model asks, shows, recommends and records, with a text fallback for hosts that cannot render UI. Question ids (Q-...) point into `synthesis/QUESTIONNAIRE.md`; block ids point into `synthesis/ONTOLOGY.md`; classes and hooks are Parts G and H.

### I1. Principles the process follows (each traced)

1. **Read before asking.** The model scans what exists and asks only for gaps, confirming pre-filled answers in one line [S-L17-003] [S-L17-005].
2. **Define the blocks first.** The person sees the whole map of building blocks, with each block's class and how it shapes what follows, before choosing anything (BRIEF requirement 1).
3. **Spend time where the fan-out is.** The model slows down on the decisions with the most downstream effect in `synthesis/decision-graph.json`: brand personality (DC-L06-02, fan-out 15), target platforms (DC-L10-01, 12), visual style direction (DC-L15-01, 12), device classes (DC-L14-01, 10), platform posture (DC-L10-02, 9), scope (DC-L11-02, 8), source of truth (DC-L16-02, 8), density voice (DC-L15-04, 7). Everything classed G moves fast on defaults (BRIEF requirement 8) [S-L17-015].
4. **Concepts before generation, variants that genuinely differ.** Named directions in one line each, confirmed, then rendered; each variant differs in type, palette and layout [S-L17-005].
5. **Label safe versus risky.** Every proposal says which choices follow the category and which are deliberate departures, with gain and cost [S-L17-004].
6. **Deterministic checks before model judgment.** Contrast, target size, scale steps and lint rules run first; the model's critique comes after [S-L17-011].
7. **Hooks, not replacement.** Designer-owned blocks get a "do you have this?" hook with honest fallbacks and a briefed placeholder, never a generated stand-in presented as final (BRIEF requirement 2) [S-L17-004: "Produce the asset or ship nothing"] [S-L17-023].
8. **References pre-fill; they never decide, and never carry identity.** (BRIEF requirement 4; Part F.)
9. **Record everything in the repo.** Every decision is written with its reason, its source (default, reference, person, designer) and what it changed, so the next session and the team can read it (BRIEF requirements 9-11).

### I2. The stages

Each stage lists what the model **asks**, **shows** (visual when the host allows it, text otherwise), **recommends**, **records**, how much time it should take, and where a designer stays in the loop.

**Stage 0. Orient (fast).**
- *Asks:* one bundled question with everything pre-filled: what the product is, who it is for, which surfaces (and their mode: Persuade, Operate, Read, Experience [S-L17-007]), and the depth mode (Quick 10 questions, Standard, Expert, per QUESTIONNAIRE). Plus the memorable-thing question [S-L17-003].
- *Reads first:* repo manifests (stack), existing token files, an existing DESIGN.md or PRODUCT.md, any Figma link, earlier decision logs. Code sources beat prose: Bolt reports that a docs site alone yields a theme rather than a system [S-L17-206].
- *Shows:* a one-screen summary of what it found and what it assumed. Text fallback: a short list with "found / assumed / missing".
- *Records:* the product context file (audience, purpose, constraints, surfaces, modes) and the depth mode.
- *Designer in loop:* not needed.

**Stage 1. Define the building blocks (medium).**
- *Shows:* the block map (the ontology's layers and blocks), each tagged G / E / D / T / I, with the high fan-out blocks highlighted and a line on what each shapes downstream. Text fallback: a nested list with class tags.
- *Asks:* the scope questions that prune the map: platforms and device classes (Q-plat-01, Q-plat-02), existing UI or new product (Q-scope-02), where the system lives (Q-tool-01), accessibility target (Q-aud-03).
- *Recommends:* which blocks are out of scope (for example haptics for a web-only product), each marked "not applicable" with the reason, so the coverage check counts them as decided rather than missing. Like Figma's `figma-generate-library` skill, it prints a gap analysis and locks the v1 scope before writing anything [S-L17-210].
- *Records:* the pruned block list with a status per block: `pending`, `default`, `decided`, `not applicable`, `awaiting asset`.

**Stage 2. Reference intake (offered here, open at every stage).**
- *Asks:* "Do you have an example website, screenshot, Figma file, repo or brand book?" Each reference is tagged "our product", "inspiration" or "competitor" (Q-ref-01). URLs are shown back for confirmation before anything is fetched [S-L17-003].
- *Shows:* an "extracted from reference" card per block: value, source, confidence (measured / estimated from pixels / inferred), with Accept, Adjust, Ignore.
- *Recommends:* what to carry (structure, rhythm, ratios, density, depth model, motion character) and what never to carry (logo, brand name, brand color as identity, proprietary typeface, photography, illustration, copy) [S-L17-023] [S-L17-022].
- *Records:* a reference log with provenance for every pre-filled value; nothing is `decided` until the person accepts it.

**Stage 3. Asset inventory: the designer hooks (medium).**
- *Asks:* one grouped "Do you have these?" checklist: logo and marks, brand typeface, brand colors, icons, illustration, photography, motion assets, sound, voice guide (Part H). In Quick mode it asks nothing and applies each hook's fallback, leaving the slots open.
- *Does with a yes:* ingests the file, validates it (Part H checks), derives what follows (brand color candidates from the logo, favicon and app-icon sizes from the master SVG) and marks those derived values "from asset".
- *Does with a no:* shows the fallbacks in order (commission a designer, use an open library, use a named tool with its caveat, or omit) and creates a placeholder slot with a written brief, so a designer can fill it later without re-reading the whole system.
- *Records:* an Asset Decision Record per hook: have / commissioning / tool / open library / placeholder / not needed, and who owns the follow-up [S-L17-023].
- *Designer in loop:* this is the main hand-off point; the brief for each missing asset is written so a designer can act on it directly.

**Stage 4. Brand and direction (slow: the highest fan-out decisions).**
- *Asks:* personality sliders (Q-brand-01), 4-5 mood words (NN/g's mood-board method [S-L17-146]), products it should feel like and the one thing people should recognize (Q-brand-02), expressiveness (Q-brand-04), native versus brand posture (Q-plat-05). Vague words ("clean", "modern") are turned into precise visual keywords before generating, which is NN/g's first fix for generic output [S-L17-121].
- *Shows:* first, 3 direction concepts in one line each (named, distinct); after the person picks or edits, the same concepts rendered on real components and 2-3 real screens, light and dark side by side. The model states for each direction which choices are safe and which are risks [S-L17-004] [S-L17-005]. Text fallback: the concept lines plus a token table per direction.
- *Recommends:* one direction, with the reason tied to the memorable thing and the audience; it flags when a choice lands in a known generic look (the three looks, the slop catalog) and says so once [S-L17-004] [S-L17-021].
- *Checks:* optionally, a closed word-choice test of the chosen direction against the target brand attributes (with opposites and distractors) or a 5-second test with a few teammates [S-L17-148].
- *Records:* the chosen direction, the dial values it implies, the rejected directions and why (useful for later sessions and for explaining the choice to the team).
- *Designer in loop:* optional review of the direction; the recorded rationale is what a designer would ask for.

**Stage 5. Foundations, block by block (fast on defaults, slow on high fan-out).**
- *Order:* the dependency steps in `synthesis/decision-graph.json` (color space and ramps before roles; base unit before scale; type scale before components).
- *Shows per block (the detail panel):* what the block is, where to use it, where not to, the current value and its source, a live preview on a specimen and on real screens, every mode side by side, and what else changes if it changes (downstream blocks from the graph). Validators run on every edit (contrast, target size, scale monotonicity).
- *Asks:* only the Standard or Expert questions for the depth mode; G blocks take defaults and stay editable.
- *Recommends:* a default with a one-line reason and the systems that use it (from the lane cards).
- *Records:* DTCG tokens and a decision-log line per changed block: value, reason, source, downstream blocks touched.

**Stage 6. Components and patterns (medium).**
- *Shows:* a prunable component checklist in tiers (the 18 components found in 60+ of the 90 designsystems.surf systems as the starter set, the next 12 as "likely next" [S-L17-302]), then each chosen component generated from the tokens (anatomy, variants, states matrix: default, hover, focus, active, disabled, loading, error, empty), with its use / avoid guidance and accessibility behavior (DC-L17-13).
- *Asks:* the questions where systems genuinely disagree: disabled submit buttons, tooltips on disabled controls, toasts versus inline messages (L08 cross-lane note), confirm versus undo for destructive actions.
- *Recommends:* the headless library or implementation route for the stack (tool-assisted hook H-comp).
- *Records:* component specs, generated docs pages, and the policy answers.

**Stage 7. Content and voice (medium).**
- *Asks:* for an existing voice guide (hook H-voice); otherwise the model drafts voice attributes and a tone matrix from the personality answers.
- *Shows:* microcopy for the real components (buttons, errors, empty states) in the drafted voice, beside a neutral version.
- *Records:* voice rules and the word list (terminology is owner input).
- *Designer in loop:* a content designer ideally reviews; the draft is marked as a draft until someone does.

**Stage 8. Critique and coverage check (medium).**
- *Runs:* deterministic checks first, then the model's critique: a 0-10 score per layer with "what a 10 looks like" and one question per gap [S-L17-006] [S-L17-011]. Critique uses a rubric fixed in advance and, for generated content, more than one run, because one output is an example, not an evaluation [S-L17-130] [S-L17-132]. It flags the fidelity trap: polished output with unverified patterns [S-L17-133].
- *Shows:* the coverage map: every block with its status and source; pending assets; blocks still on unreviewed defaults; hard failures (contrast, targets); lint warnings with waivers.
- *Asks:* one question per remaining gap, or confirmation to accept a named remainder.
- *Records:* the coverage report and waivers with reasons. Nothing is silently skipped: a block is either decided, defaulted, not applicable, or pending, and each state is visible (BRIEF requirement 5).

**Stage 9. Export and hand-off (fast).**
- *Writes:* DTCG tokens, platform code, DESIGN.md, the product context file, the decision log, the coverage report, briefs for missing assets, and a short plain-language summary for the team ("what we chose, why, and what is still open"). Formats and channels are L18's and L07/L16's scope.

**Stage 10. Extend over time (per change).**
- *Reads:* the decision log and DESIGN.md before any change, the way gstack makes agents read DESIGN.md first [S-L17-004].
- *Shows:* the change on the block's detail panel with the downstream blocks it touches, before committing.
- *Records:* the change as a new decision-log line; a changed direction (a "user challenge" in gstack's terms) needs explicit confirmation [S-L17-015].

### I3. Where the designer stays in the loop (summary)

| Point | What the designer receives | Why |
|---|---|---|
| Stage 3 hooks | A brief per missing asset, with the system's tokens, the direction, formats and sizes | Designer-owned blocks are commissioned, not generated (BRIEF requirement 2) |
| Stage 4 direction | The direction, its safe/risk split and the rejected options | Designers review reasoning, not just a picture [S-L17-004] |
| Stage 7 voice | Drafted voice and microcopy marked as draft | Content design is a specialist skill (L11 Part F) |
| Stage 8 critique | Coverage map, lint waivers, open decisions | A reviewable list instead of a finished-looking artifact |
| Stage 10 changes | Diffs with downstream impact | Keeps coherence over time |

---

## Part J. Decision Cards

These are decisions about how the builder makes a system, so "Visual effect" describes the effect on the product and on the person's experience, and "Token encoding" says how the builder stores the decision (mostly metadata, not DTCG tokens), following the convention L11 used for process cards.

### DC-L17-01: Block classification scheme (who or what produces each block)
- **Block path:** Builder > Guidance > Block classification (applies to every ontology node)
- **Questions the designer answers:** None directly; this is how the builder decides, per block, whether to generate, extract, ask for an asset, recommend a tool, or ask the owner.
- **Options:**
  - *Two classes (generate vs ask):* what most theme generators do; shadcn create, tweakcn and Radix take 3-10 inputs and generate the rest (L11 Part G).
  - *Four classes (generatable, extractable, designer-owned, tool-assisted):* the task's proposal.
  - *Five classes, primary plus "also":* the four plus owner input (I), each block with one primary route and optional secondary routes. Recommended.
  - *Decision-side classes:* gstack's Mechanical / Taste / User Challenge, which classify decisions by who should decide rather than by who produces the value [S-L17-015].
- **Visual effect:** Five classes make the block map honest: the person sees at a glance that most blocks will be generated (G, 65%), which few need their files (D), where a tool is involved (T), and which decisions only they can make (I). Without I, business decisions look like design tasks [inferred].
- **Depends on (upstream):** the ontology (S1a), the lever set (S1c).
- **Affects (downstream):** stage order and pacing (DC-L17-08), the hook list (DC-L17-04), the coverage check (DC-L17-09), Quick-mode behavior (defaults for G, fallbacks for D and T, required answers for I).
- **Token encoding:** metadata on each ontology node: `class: G|E|D|T|I`, `also: [..]`, `hook: H-..`. Not a DTCG token.
- **Platform notes:** a few blocks change class by platform: haptics are T on iOS/Android and not applicable on web; app icons are D everywhere but their size sets are T (platform tools) [inferred].
- **Accessibility constraints:** accessibility blocks are G (validators) except assistive-technology testing, which is T with a human step (guard.testing).
- **Default + heuristic:** Five classes. Rule: if a formula or sourced default gives an acceptable value, G; if an existing asset is the truth, E; if quality depends on a human creator, D; if a named tool gets an engineer there with a caveat, T; if only the business knows, I. Map the classes onto gstack's decision side: G is Mechanical, D and taste-heavy T and I blocks are Taste, and anything that changes stated direction is a User Challenge.
- **Evidence:** [S-L17-015] Part G counts; L11 Part G; `synthesis/LEVERS.md`

### DC-L17-02: Entry path (how a new system starts)
- **Block path:** Context > Starting point > Entry path
- **Questions the designer answers:** Are we starting from an existing product, a UI kit, a reference we admire, or nothing? Is there a brand already?
- **Options:**
  - *From an existing product (audit):* inventory and extract, then consolidate; the canonical practice (Brad Frost's interface inventory, DC-L11-04).
  - *From a UI kit:* Untitled UI, Material 3 kit, Apple kits, shadcn kits; fast, but the kit's defaults become the look unless changed (Part D).
  - *From a reference:* extract structure and quality from a site the person admires (Part F); gstack and Stitch both support this [S-L17-003].
  - *From a brief only:* interview, then generate directions (gstack `/design-consultation` [S-L17-003]; Anthropic's two-pass plan-then-build [S-L17-021]).
- **Visual effect:** kit-first systems look like the kit (the sameness complaint in COMMUNITY-SIGNAL); reference-first systems inherit the reference's rhythm; brief-first systems vary most but need the most decisions [inferred].
- **Depends on (upstream):** ctx.strategy (DC-L11-01), ctx.scope.
- **Affects (downstream):** which stages run long (audit-heavy vs direction-heavy), which blocks start as E vs G.
- **Token encoding:** `entry: existing | kit | reference | brief` in the product context file, plus references with provenance.
- **Platform notes:** native apps often start from platform kits (Apple, Material), which makes native-first posture the path of least resistance [inferred; L10].
- **Accessibility constraints:** kits and references carry their own contrast and target choices; validators must re-check them rather than trust them [inferred].
- **Default + heuristic:** Existing product: audit first. Otherwise brief first, with an optional reference; offer a kit only as a component base (headless library or registry), not as the visual direction.
- **Evidence:** [S-L17-003] [S-L17-021] DC-L11-01 DC-L11-04; Part D [S-L17-322] [S-L17-328] [S-L17-120]

### DC-L17-03: Reference intake: fidelity and the identity firewall
- **Block path:** Builder > Input > Reference intake
- **Questions the designer answers:** What should we learn from this reference: its structure, its quality bar, its motion, or nothing but a warning (competitor)? How faithful should we be?
- **Options:**
  - *Replicate the system, swap the identity:* keep layout, rhythm, scales, component anatomy and motion character; replace brand name, logo, copy, imagery and brand color (site-soul-extractor's replication path) [S-L17-023].
  - *Reinterpret:* take the lessons (one signature, pacing) and rebuild in the subject's world; each carried mechanic needs a line "reference does X because audience A, we do Y because audience B" [S-L17-023].
  - *Flag only (competitor):* read to list the category's shared tropes so the builder can avoid them [inferred; QUESTIONNAIRE Q-ref-01].
  - *Copy everything including identity:* never offered [S-L17-023].
- **Visual effect:** replication gives a recognizable structure with new identity; reinterpretation gives a new product that shares a quality bar; flag-only reduces sameness with competitors [inferred].
- **Depends on (upstream):** entry path (DC-L17-02), brand inputs (ctx.brand).
- **Affects (downstream):** pre-filled values for up to 44 blocks (Part G), the provenance log, the anti-generic checks.
- **Token encoding:** every pre-filled token carries `$extensions.opendesigner.source = {reference: id, method: computed|pixel|vision|file, confidence}` [inferred; DTCG allows `$extensions`, L07].
- **Platform notes:** web references expose computed styles; app references usually arrive as screenshots, so values are estimates [inferred].
- **Accessibility constraints:** extracted colors often fail the chosen target in the new context (a new background, dark mode); validators run on every accepted value [inferred].
- **Default + heuristic:** Default to reinterpretation for inspiration references and replication-with-identity-swap only when the person says "our version of this". Never carry name, logo, copy, photography, illustration or proprietary fonts; offer licensed substitutes and log each substitution [S-L17-022] [S-L17-023].
- **Evidence:** [S-L17-022] [S-L17-023] [S-L17-003]; Part F [S-L17-237] [S-L17-121]

### DC-L17-04: Designer-hook policy (ask, accept, fall back)
- **Block path:** Builder > Guidance > Designer hooks
- **Questions the designer answers:** Do you have this asset? If not, will you commission it, use an open library, use a tool, or leave a placeholder?
- **Options:**
  - *Generate a stand-in silently:* what most AI builders do; it produces the generic tells gstack and Anthropic catalog (CSS-shape illustrations, stock heroes, generated mascots) [S-L17-004] [S-L17-021].
  - *Ask every hook up front:* thorough but slow; bad for Quick mode.
  - *Grouped checklist at Stage 3, fallbacks applied in Quick mode, slots left open:* recommended; matches QUESTIONNAIRE's hook rule.
  - *Ask only when the block is first needed:* lower friction, but the asset gap surfaces late.
- **Visual effect:** honest placeholders with written briefs look unfinished on purpose; generated stand-ins look finished but generic, and they tend to ship [inferred from S-L17-004].
- **Depends on (upstream):** classification (DC-L17-01), scope (which assets apply).
- **Affects (downstream):** brand color candidates (from logo), favicon and app-icon sets, empty states, onboarding, marketing surfaces, the coverage report.
- **Token encoding:** assets are referenced, not tokenized: an asset manifest with `id, status (have|commissioning|tool|library|placeholder|n/a), files, licence, owner, brief`; DTCG has no asset type (L05 cross-lane note).
- **Platform notes:** app icons and favicons have platform size sets (Part H); fonts need app-embedding rights for native apps, not only web rights (Part H).
- **Accessibility constraints:** logos are exempt from contrast minimums but meaningful icons and images need text alternatives (L05).
- **Default + heuristic:** Grouped checklist; fallback order: have it > commission a designer (with the generated brief) > open library with a compatible licence > named tool with its caveat > omit. Never present a generated identity asset as final.
- **Evidence:** [S-L17-004] [S-L17-021] [S-L17-023]; Part H; QUESTIONNAIRE hooks table [S-L17-525] [S-L17-560] [S-L17-579]

### DC-L17-05: Variant generation (how "show me options" works)
- **Block path:** Builder > Exploration > Variants
- **Questions the designer answers:** How many directions do you want to see? Which parts should vary (type, color, layout, motion)?
- **Options:**
  - *Parameter shuffle with locks:* shadcn create, Realtime Colors (L16 Part D).
  - *Concepts first, then renders, anti-convergence enforced:* gstack (3 default, up to 8; each variant differs in family, palette and layout) [S-L17-005].
  - *Creative range dial:* Stitch SDK REFINE / EXPLORE / REIMAGINE with aspects (L16 C2).
  - *Endless feed:* Variant (L16 C2).
- **Visual effect:** anti-convergence produces directions that feel like different teams made them; shuffle produces siblings [S-L17-005] [inferred].
- **Depends on (upstream):** brand inputs, memorable thing, any references.
- **Affects (downstream):** the chosen direction sets dial values for every foundation.
- **Token encoding:** each variant is a dial vector plus overrides; the chosen one becomes the token source; rejected ones are kept in the log.
- **Platform notes:** render variants on the target platform's real components (web and native previews differ) [inferred].
- **Accessibility constraints:** every variant must pass the contrast target before it is shown [inferred].
- **Default + heuristic:** 3 concepts in text, confirm, render on real components with light and dark side by side; remix at block level; lock and shuffle for fine exploration afterwards.
- **Evidence:** [S-L17-005] [S-L17-004]; L16 Part C2 and D [S-L17-233] [S-L17-235] [S-L17-132]

### DC-L17-06: Proposal framing (safe choices versus risks)
- **Block path:** Builder > Guidance > Proposal framing
- **Questions the designer answers:** Which departures from the category do you want to take?
- **Options:** *Plain recommendation;* *options table without a recommendation;* *safe/risk split with gain and cost per risk* (gstack) [S-L17-004]; *three-layer synthesis* (convention, trend, first principles) [S-L17-003].
- **Visual effect:** the safe/risk split keeps most of the product conventional and concentrates distinctiveness in 2-3 places, which Anthropic's skill also recommends ("spend your boldness in one place") [S-L17-021].
- **Depends on (upstream):** research or references, brand inputs.
- **Affects (downstream):** where the Expression and Brand presence dials sit; which blocks carry the signature.
- **Token encoding:** `rationale: {safe: [...], risks: [{what, why, gain, cost}]}` in the decision log.
- **Platform notes:** on native platforms, risks usually belong in content and brand moments, not in system controls (L10) [inferred].
- **Accessibility constraints:** a risk may never break a hard rule (contrast, targets, reduced motion).
- **Default + heuristic:** Always show the split; default to 2 risks, at least one tied to the memorable thing.
- **Evidence:** [S-L17-003] [S-L17-004] [S-L17-021]

### DC-L17-07: Anti-generic guardrails
- **Block path:** Guardrails > Checks > Genericness
- **Questions the designer answers:** How strict should the builder be about common AI-generated looks? Which rules do you want to waive?
- **Options:**
  - *None:* accept whatever the model produces.
  - *Hard bans:* gstack's banned faces and blacklist as absolute rules [S-L17-004].
  - *Lint with ids, severity and waivers:* impeccable's 61 deterministic rules as a model [S-L17-020] [S-L17-011].
  - *Model critique only:* a vision or LLM pass; gstack deferred this because vision misjudges some patterns [S-L17-011].
- **Visual effect:** lint with waivers removes accidental defaults (purple gradients, identical card grids, one radius everywhere) while allowing a chosen look, such as Inter for a dense tool [inferred].
- **Depends on (upstream):** direction and surface modes.
- **Affects (downstream):** critique stage, export lint rules.
- **Token encoding:** rule catalog with `id, severity, rationale, waived_by, reason` in the guardrails config.
- **Platform notes:** most rules are web-marketing tells; Operate surfaces and native apps need a smaller set [S-L17-007] [inferred].
- **Accessibility constraints:** accessibility rules are never waivable; taste rules are.
- **Default + heuristic:** Lint with waivers, deterministic first, model critique second; taste rules warn, accessibility rules fail.
- **Evidence:** [S-L17-004] [S-L17-007] [S-L17-011] [S-L17-020] [S-L17-021] [S-L17-218] [S-L17-120]

### DC-L17-08: Pacing (where the model slows down)
- **Block path:** Builder > Guidance > Pacing
- **Questions the designer answers:** How deep do you want to go (Quick, Standard, Expert)?
- **Options:** *Uniform* (every question equal); *depth modes only* (QUESTIONNAIRE); *fan-out weighted with decision classes* (slow on high fan-out and taste decisions, silent on mechanical ones) [S-L17-015].
- **Visual effect:** the person spends minutes on brand, platforms and direction and seconds on spacing steps, which is where the downstream effect is (decision-graph fan-out: DC-L06-02 15, DC-L10-01 12, DC-L15-01 12) [inferred from `synthesis/decision-graph.json`].
- **Depends on (upstream):** the decision graph, classification.
- **Affects (downstream):** stage length, which questions appear in Quick mode.
- **Token encoding:** per node `fan_out`, `class`, `min_mode`.
- **Platform notes:** multi-platform scope raises the weight of platform decisions (L10).
- **Accessibility constraints:** the accessibility target (Q-aud-03) is always asked in Standard and above even though its fan-out is modest, because it bounds many values [inferred].
- **Default + heuristic:** Weight time by fan-out and class; never auto-decide an I block; auto-decide G blocks with visible defaults.
- **Evidence:** [S-L17-015]; `synthesis/decision-graph.json`; QUESTIONNAIRE depth modes

### DC-L17-09: Coverage check and completeness scoring
- **Block path:** Guardrails > Coverage
- **Questions the designer answers:** Which open items are acceptable for now?
- **Options:** *Checklist of sections;* *per-block status over the ontology* (pending, default, decided, not applicable, awaiting asset); *0-10 per layer with "what a 10 looks like"* (gstack) [S-L17-006]; *A-F grades with weighted categories* (gstack live review) [S-L17-008].
- **Visual effect:** the person sees exactly what is missing; nothing is silently skipped (BRIEF requirement 5).
- **Depends on (upstream):** ontology, classification, hook statuses.
- **Affects (downstream):** export gate, team summary.
- **Token encoding:** coverage report generated from node statuses; waivers carry reasons.
- **Platform notes:** a block can be decided on one platform and pending on another; status is per platform where the node varies by platform [inferred].
- **Accessibility constraints:** unmet hard rules block "complete" status.
- **Default + heuristic:** Per-block status plus a 0-10 score per layer with the gap in plain words; export allowed with a named remainder.
- **Evidence:** [S-L17-006] [S-L17-008]; ONTOLOGY coverage check [S-L17-119] [S-L17-107] [S-L17-210]

### DC-L17-10: What the process records (for harmony and team communication)
- **Block path:** Delivery > Records
- **Questions the designer answers:** Who else needs to understand these decisions?
- **Options:** *Tokens only;* *tokens + DESIGN.md* (gstack, Stitch) [S-L17-004] [S-L17-010]; *product context + DESIGN.md + tokens + decision log with provenance + asset manifest + coverage report* (recommended); *full docs site* (Part D tools).
- **Visual effect:** none on the product; on the team, a decision log in plain words lets engineers explain choices and lets the next session extend the system without drift (BRIEF requirements 9-10) [inferred].
- **Depends on (upstream):** every stage.
- **Affects (downstream):** later sessions (Stage 10), other agents reading the repo, team reviews.
- **Token encoding:** decision-log entries `{date, block, value, reason, source: default|reference|person|designer|asset, downstream}`; gstack's Decisions Log table is the minimal form [S-L17-004].
- **Platform notes:** none.
- **Accessibility constraints:** record the accessibility target and every waiver.
- **Default + heuristic:** Always write all six records; the packaging of these files is L18's scope.
- **Evidence:** [S-L17-004] [S-L17-010] [S-L17-020] [S-L17-124] [S-L17-135] [S-L17-213]

### DC-L17-11: Preview substrate during the process
- **Block path:** Builder > Preview
- **Questions the designer answers:** None; the builder chooses.
- **Options:** *Generated raster mockups* (gstack via an image model) [S-L17-012]; *real rendered components and screens from the current tokens* (L16 recommendation); *both: raster for mood exploration, rendered for decisions*.
- **Visual effect:** rendered previews are exact and editable; raster previews look richer early but cannot be measured, and their values have to be re-extracted by a vision model [S-L17-014] [inferred].
- **Depends on (upstream):** host capabilities (L18).
- **Affects (downstream):** accuracy of every decision made while looking at a preview.
- **Token encoding:** none.
- **Platform notes:** native previews need platform renderers or screenshots; web previews render directly [inferred].
- **Accessibility constraints:** only rendered previews can be checked for contrast and targets.
- **Default + heuristic:** Rendered components for every decision; raster only for optional mood boards, labeled as such.
- **Evidence:** [S-L17-012] [S-L17-014]; L16 finding 7

### DC-L17-12: Approval gates
- **Block path:** Builder > Governance > Approval gates
- **Questions the designer answers:** Do you approve this structure, this direction, these assets?
- **Options:** *No gates (one-shot generation);* *gates at structure, direction, assets* (site-soul-extractor, which calls skipping the direction gate its most repeated failure) [S-L17-023]; *gate per issue* (gstack plan review asks once per gap) [S-L17-006]; *final gate only for taste decisions* (gstack autoplan) [S-L17-015].
- **Visual effect:** gates prevent building a full system on a direction nobody chose [S-L17-023].
- **Depends on (upstream):** depth mode.
- **Affects (downstream):** cost of rework.
- **Token encoding:** gate records in the decision log.
- **Platform notes:** none.
- **Accessibility constraints:** none.
- **Default + heuristic:** Three gates (block map and scope, direction, assets) plus a final taste-decision review; Quick mode keeps only the direction gate.
- **Evidence:** [S-L17-006] [S-L17-015] [S-L17-023] [S-L17-210] [S-L17-201]

### DC-L17-13: The per-block detail panel (how the builder teaches while editing)
- **Block path:** Builder > Guidance > Block detail panel (every G block; component pages extend DC-L08-23)
- **Questions the designer answers:** None; this is what the person sees beside every control.
- **Options:**
  - *Value and live preview only:* most theme playgrounds (L16 Part D).
  - *Props and stories only:* Storybook autodocs gives description, primary story with controls and a props table, but no usage guidance [S-L17-343].
  - *NN/g record:* what it is, states, context of use, do's and don'ts, real-content example, content standard, code [S-L17-112] [S-L17-110] [S-L17-111].
  - *Comparative guidance:* "use this when X, otherwise use Y", with a numeric threshold and the named alternative (NN/g dropdowns; designsystems.surf blueprints compare switch vs checkbox vs radio vs segmented control) [S-L17-117] [S-L17-306].
  - *Agent-oriented guidelines:* Figma Make kit component files carry when-to-use, variant decision trees and correct/incorrect usage, in many short files [S-L17-200]; Figma notes agents may not know when to use a component without descriptions [S-L17-261].
- **Visual effect:** the panel turns each decision into a small lesson, so the person learns where a block belongs while choosing it (BRIEF requirement 3) [inferred].
- **Depends on (upstream):** the lane Decision Cards (defaults, options, systems that use them).
- **Affects (downstream):** generated docs, DESIGN.md prose, agent rule files, the team summary.
- **Token encoding:** per block `{what, use_when, avoid_when: [{condition, instead}], threshold, example, source_cards, downstream}` stored beside the tokens and exported into docs and agent files.
- **Platform notes:** thresholds and alternatives can differ by platform (for example sheet vs dialog on phones, L08); the panel shows the platform variant [inferred].
- **Accessibility constraints:** every panel lists the accessibility rule that bounds the block, with the check result.
- **Default + heuristic:** Always show what it is, where to use, where not to (with the alternative and a threshold when one exists), a live preview in all modes, its source, and what else changes. Keep it short: NN/g's lean-team guidance favors precise over exhaustive docs [S-L17-113].
- **Evidence:** [S-L17-110] [S-L17-111] [S-L17-112] [S-L17-113] [S-L17-117] [S-L17-200] [S-L17-261] [S-L17-306] [S-L17-343]

---

## Reconciliation with `sources/COMMUNITY-SIGNAL.md` (L00)
- **designsystems.surf.** L00 rejected a surf article as a listicle [S-L00-005]. This lane used only surf's directory data, counted by script, as a Tier C structured sample (Part C); no claim rests on a surf article except its five-bucket component taxonomy, labeled as such [S-L17-311].
- **"Figma Make is judged weak"** (community: "ideation and concepts") agrees with NN/g's 10-tool study (generic look, weak hierarchy) and with Figma's own caveat that kit CSS "won't capture every design detail" [S-L17-120] [S-L17-211].
- **"AI slop" sameness** is now confirmed at vendor level, not only by the community: Google's official taste skill bans purple neon and Inter, Anthropic's frontend-design skill lists five default clusters, tweakcn exists because shadcn sites look alike [S-L17-218] [S-L17-021] [S-L17-232].
- **DESIGN.md schema** was "low / unverified" in L00 [S-L00-052]. It is now read from the GitHub repo: v0.4.0 (27 Jul 2026), alpha, five token groups and eight sections, an 11-rule linter, and no keys for modes, motion, icons or breakpoints [S-L17-213]. It remains a draft, so the builder emits it as one format among several.
- **zeroheight 2026 sample size.** L00 could not find it; H3 reports n=147 from report.zeroheight.com [S-L17-347]. L00's correction stands: quote the main report (28% rate AI highly), not the "15%" social post.
- **Code as source of truth** (practitioner consensus in L00) matches the AI-tool evidence: Bolt, Magic Patterns and v0 all rank code sources above docs and prompts [S-L17-206] [S-L17-205] [S-L17-201].

## Cross-lane notes (for the orchestrator to post; this lane did not edit BOARD.md)
- [L17 -> S1a/S1d] Part G gives `class / also / hook` for all 207 non-builder ontology leaves (G 135, T 31, I 29, D 7, E 5; 44 extractable by any route). Suggest adding these as node metadata. A fifth class, owner input (I), was needed.
- [L17 -> S1b] Part H adds hooks the questionnaire lacks: app icon sizes by platform, favicon set, motifs/gradients/signature shape, custom haptics, brand-book intake. Fontshare's ITF FFL v2.0 bans subsetting and offering its fonts as selectable fonts in a design tool; Adobe Fonts cannot be self-hosted or embedded in native apps [S-L17-536] [S-L17-538].
- [L17 -> L08] designsystems.surf counts support DC-L08-01: 18 components appear in 60+ of 90 systems; NN/g's comparative "use this when, otherwise that" format supports DC-L08-23 [S-L17-302] [S-L17-117].
- [L17 -> L18] Part I is written as a model-run process (asks, shows, recommends, records) and leaves packaging and host surfaces to L18. DESIGN.md alone cannot carry modes, motion or breakpoints [S-L17-213].
- [L17 -> L11] Update the competitor table: Motiff is discontinued (export until 31 Oct 2026); Lovable removed Themes on 16 Mar 2026 and made design systems a paid feature on 19 Aug 2026; Figma ships an official `figma-generate-library` skill [S-L17-229] [S-L17-234] [S-L17-210].
- [L17 -> L05] The official Material sound resources page returns 404; no verified open UI-sound library was found; unDraw and Recraft ban using their assets for AI training [S-L17-552] [S-L17-519] [S-L17-525].
- [L17 -> L07/L16] Figma variable limits as read on 2026-09-23: 10 modes per collection on Pro, 20 on Org, extended collections Enterprise only, 5,000 variables per collection [S-L17-337] [S-L17-338] [S-L17-340]. Reconcile with L07.
- [L17 -> V1] Re-verify: Figma seat prices, ITF FFL v2.0 terms, Apple and Android icon sizes, the date of OpenAI's GPT-5.4 frontend post (not shown on the page; gstack says Mar 2026) [S-L17-340] [S-L17-536] [S-L17-500] [S-L17-503] [S-L17-019].

## Open questions / gaps
- **gstack was read, not run.** Its board, taste memory and detector behavior are described from its docs and code, not observed (by instruction).
- **The classification is this lane's judgment.** It is reproducible from the table, but borderline blocks could reasonably move: typeface sourcing (T or D), voice (T or D), brand color (E or I), expressive shape and gradients (T, E or D). It has not been reviewed by practicing designers.
- **The ontology is still changing.** S1a added and removed nodes during this session (for example `found.type.i18n` no longer appears), so the counts will shift; they can be recomputed by counting the Class column of the G3 table [inferred].
- **No published effort numbers** for customizing a UI kit or running an interface audit; the only effort figure is Dan Mall's 90-day program (12 weeks, 3-8 people) [S-L17-352].
- **Stitch's URL extraction** is documented only in its launch post; UX Pilot and Figma's AI "solutions" pages are marketing-level [S-L17-216] [S-L17-230] [S-L17-208].
- **NN/g has no article on style tiles or interface inventories**; the content-audit method is used as the stand-in [S-L17-119].
- **EightShapes material** could not be read (domain did not resolve); Nathan Curtis now works as Directed Edges [S-L17-353] [S-L17-354].
- **Legal notes are US and EU only.** Copyright and trademark rules for AI assets in India (Kunal's context) were not researched.
- **Unverified details:** the Icon Composer file extension, the Lottie spec version, and the extraction reliability of screenshot-based tools (no vendor publishes accuracy numbers except Brandfetch) [S-L17-241].
- **Reliability ratings in F2** are a synthesis, not a benchmark; a hands-on test of three extractors on the same site would firm them up.

## Confidence
- **High (read from primary sources or counted):** gstack's methods (read from its source files); NN/g claims (dated articles); official platform and product limits (Apple, Android, Figma help, Storybook, Tokens Studio); licence terms (read from licence pages); designsystems.surf counts (scripted over 90 live pages); DESIGN.md structure (GitHub repo).
- **Medium:** AI tool behavior from vendor docs without hands-on use; survey numbers (vendor-run surveys: zeroheight, Sparkbox); the classification counts (judgment applied consistently, basis cited per row).
- **Low or inferred:** reliability ratings in F2; person-hour arithmetic for the 90-day program; the process design in Part I and the Decision Card defaults, which are recommendations built from the evidence rather than findings.
- **Verification pass (2026-09-23, lane author, after the helpers finished):** eight load-bearing claims were re-checked against the live pages: Lovable's Themes removal date, Motiff's shutdown, Bolt's "theme rather than a true design system", NN/g's "no genAI tool effectively supports design systems", the Thaler certiorari denial, Figma's mode limits and seat prices (a WebFetch summary misread the table; the raw page confirmed 10 / 20 / unlimited), and the zeroheight 2026 numbers. All held [S-L17-024] [S-L17-025] [S-L17-026] [S-L17-027] [S-L17-028] [S-L17-031] [S-L17-032]. The Fontshare licence page is JavaScript-only; its design-tool clause was corroborated by a search summary, but the subsetting clause rests on helper H4's browser reading alone [S-L17-029] [S-L17-030] [S-L17-536].
