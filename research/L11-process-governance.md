# L11: The designer's job, design system lifecycle, governance, AI-era trends

Lane: L11. Author: orchestrator subagent L11. Written 2026-09-23.
Trace: `traces/L11-trace.md` (108 source rows, including rejected ones).
Status: complete (see `## Open questions / gaps` and `## Confidence` at the end).

## Lane overview

This lane answers three questions for the builder: what a designer actually does to create a design system and in what order; which questions they must answer at each step; and how the system is run once it exists (teams, contribution, versioning, docs, accessibility, metrics). It also covers what changed in 2025-2026 with AI agents, and it reviews 24 products that already generate or host design systems.

Top findings:
1. **The canonical order is: sell, discover, audit, set principles, build foundations and components together against a real pilot, document, roll out, govern, measure.** Every major source agrees on that order, with one refinement: foundations and components are built concurrently against a pilot product, not in a strict foundations-then-components waterfall. Brad Frost says atomic design "is not a linear process" [S-L11-107]; Dan Mall's pilot flywheel extracts components from a real product and then applies the draft system to more products [S-L11-014, S-L11-105]; Figma's course teaches foundations first (spacing, color, type, elevation, icons) [S-L11-009].
2. **The system is a product, not a project.** It needs an owner, a roadmap, a backlog, releases and support channels [S-L11-002, S-L11-105]. The 2026 zeroheight survey shows the cost of skipping this: 61% of teams are understaffed, 56% name resourcing as their top challenge, and leadership buy-in satisfaction fell from 42% to 32% [S-L11-030].
3. **Adoption depends on completeness and mandate more than on docs.** The most-cited adoption success factor is component completeness (79%). The biggest barrier is lack of mandate (73%), then weak governance (55%) [S-L11-030].
4. **In 2026 the design system has a second audience: AI agents.** 48% of surveyed teams already run an MCP server [S-L11-031]. Figma, Storybook, shadcn, zeroheight, Supernova, v0, Lovable, Bolt, Stitch and Claude Design all now ingest or serve a design system as agent context [S-L11-043, S-L11-044, S-L11-045, S-L11-104, S-L11-049, S-L11-052, S-L11-053, S-L11-103, S-L11-077, S-L11-055]. Machine-readable docs measurably help: Sanity's evals raised agent build success from 20% to 90% (Sonnet 4.6) by restructuring docs into a JSON spec with code chunks and linting [S-L11-108].
5. **No competitor walks a designer through the decisions.** Theme generators (shadcn create, tweakcn, Radix, Realtime Colors, Material Theme Builder) take 3-8 visual inputs and output tokens. Platforms (Supernova, zeroheight, Knapsack) host and deliver a system that already exists. AI tools (Claude Design, Stitch, Magic Patterns, v0) extract a system from an existing codebase or URL. None of them asks about principles, audience, platforms, accessibility target, governance, or theming dimensions, and none explains why each choice matters. [inferred from the competitor table below]

---

## Part A. The end-to-end workflow

### A1. Phase map (what the designer does, what they produce, what they must decide)

| # | Phase | What the designer does | Artifacts produced | Key questions (full list in Part H) | Evidence |
|---|---|---|---|---|---|
| 0 | Sell and frame | Frames the system around time and money saved rather than design method. Names the problem, the goals, and what failure looks like. Finds champions. | One-page case: problems, goals, failure scenario, sponsor list | Why build it? What will happen if it fails? Who has to be convinced? | [S-L11-001, S-L11-083, S-L11-012] |
| 1 | Discovery and kickoff | Interviews a cross-section of users of the system (designers, engineers, PMs, content, leaders) about workflow, tools, hopes and fears. Then runs a kickoff workshop to agree on outcomes and priorities. | Interview synthesis (themes, quotes), kickoff outcomes, priorities, success definition | Who are the users of the system? What does success look like in a year? What will sink this ship? | [S-L11-084, S-L11-083, S-L11-105] |
| 2 | Audit / interface inventory | Screenshots one instance of every unique UI pattern across products, grouped into categories. Also runs a visual audit of colors, type and spacing, and a CSS audit of rule counts and unique values. Presents the findings, then decides what to keep, merge or kill, and what to name things. | Inventory "über-document", visual inventory, CSS stats, naming decisions, scope estimate | Which patterns stay, go or merge? What do we call them? | [S-L11-001, S-L11-105] |
| 3 | Principles and parameters | Writes 3 or more principles, each with a characteristic, its impact, and examples. Picks the system's posture: strict or loose, modular or integrated, centralized or distributed. | Principles page, posture statement | What do we value when two good options conflict? How much freedom do teams get? | [S-L11-008, S-L11-018, S-L11-019] |
| 4 | Visual direction | Runs quick alignment exercises before full comps: a 20-second gut test on 20-30 reference sites, style tiles, element collages. | Mood and direction board, style tiles, element collage | What should it feel like? Which references do stakeholders agree on? | [S-L11-001] (feeds L06) |
| 5 | Foundations | Defines accessibility, color, typography, spacing and layout grids, elevation, iconography and motion as tokens with semantic names. | Token set (primitive, semantic, component), Figma variables and styles, code tokens | See lanes L01-L07 | [S-L11-008, S-L11-009] |
| 6 | Components via pilot | Picks 1-2 pilot products with a scorecard. Extracts and builds components against real screens. Moves between atoms and whole pages. | Component library in design and code, first templates | Which pilot? Which components first? | [S-L11-105, S-L11-014, S-L11-107] |
| 7 | Documentation | Writes docs as part of each component's definition of done: usage, anatomy, variants, states, content, accessibility, code. | Docs site, component pages, changelog | Where will docs live? Who reads them (designer, engineer, PM, agent)? | [S-L11-088, S-L11-089, S-L11-090] |
| 8 | Rollout and adoption | Chooses either a big-bang redesign or an incremental rollout. Runs training, sandboxes, office hours and announcements. | Launch plan, migration guides, training materials | Big launch or incremental? How will we announce it? | [S-L11-105, S-L11-002, S-L11-030] |
| 9 | Governance and maintenance | Runs contribution intake, the snowflake-versus-system decision, releases with semver, deprecations and support. | Contribution guide, governance flow, RFC/ADR log, release notes, roadmap | Who can contribute? How do changes ship? How are users told? | [S-L11-003, S-L11-021, S-L11-095, S-L11-106] |
| 10 | Measure and evolve | Tracks adoption in design and in code, coverage, detach rates, satisfaction and speed. Reports value to leadership. | Metrics dashboard, surveys, maturity self-assessment | What do we measure? What counts as adopted? | [S-L11-030, S-L11-035, S-L11-038, S-L11-033] |

### A2. What the canonical sources each contribute

- **Brad Frost, Atomic Design (2016)**: the interface inventory (a 5-step method with 16 categories: global elements, navigation, image types, icons, forms, buttons, headings, blocks, lists, interactive components, media, third-party components, advertising, messaging, colors, animation) [S-L11-001]. "Make it official, adaptable, maintainable, cross-disciplinary, approachable, visible, bigger, context-agnostic, contextual, last" [S-L11-002]. The 10-step governance flow (2019) [S-L11-003]. The five stages (atoms to pages), which he describes as a mental model, not a sequence [S-L11-107]. His design-system questionnaire (Sell, Kickoff, Plan, Design & Build, Launch, Maintain) [S-L11-083] and his stakeholder interview script [S-L11-084].
- **Nathan Curtis / EightShapes**: team models, solitary, centralized and federated (2015) [S-L11-005]. Contribution sizing: fixing small things differs from making large new things, so a team needs more than one contribution path [S-L11-020, snippet only; Medium blocked full text]. The Salesforce hybrid ("cyclical") model comes from Jina Anne, not Curtis [S-L11-013].
- **Dan Mall, Design That Scales (2023)**: the book's chapters cover fundamentals, the parts of a design system product, the "broken business of buy-in", pilots, governance and contribution, roles, process, success metrics and evangelism [S-L11-015]. Its pilot flywheel: take a product design, extract components, apply the draft system to more products, repeat [S-L11-014]. Other ideas: alternating "flow weeks" and "system weeks"; "don't expect product teams to contribute", meaning the system team does the abstraction work; "canon vs expanded universe" for core versus product-specific components [S-L11-014, Tier C notes, consistent with S-L11-015 chapter list]. His 8-criterion pilot scorecard is reproduced in the InVision handbook [S-L11-105].
- **Alla Kholmatova, Design Systems (Smashing, 2017)**: functional patterns versus perceptual patterns, shared language, and the system's parameters (strict or loose rules, modular or integrated parts, centralized or distributed organization) [S-L11-018, S-L11-019].
- **InVision Design Systems Handbook (2017, now historical because InVision shut down)**: team disciplines; team model chosen by goal (solitary for speed, centralized for speed plus buy-in, federated for shared ownership); interview customers first; two inventories (visual attributes and UI elements); build principles (consistent, self-contained, reusable, accessible, robust); rollout by large-scale redesign or incremental rollout [S-L11-105].
- **Figma Learn course and blog**: principles, foundations (a11y, color, type, elevation, iconography, spatial), naming as "Category/Use/Variation", processes [S-L11-008]. Build order in the course: spacing, color, typography, elevation, icons [S-L11-009]. Docs, testing with and without the system, contribution path, semver, branching (Organization/Enterprise plans), library analytics [S-L11-010]. The 3-step blog version: groundwork, foundations, build mapped to code [S-L11-012].
- **NN/g**: definition ("a complete set of standards intended to manage design at scale using reusable components and patterns"); adopt, adapt or create; minimum team of an interaction designer, a visual designer and a developer [S-L11-006].

---

## Part B. Decision Cards: setup and strategy

Note on the template: these are process and governance decisions, not visual ones. "Visual effect" here means the effect on the product and the system. "Token encoding" means how the builder should store the decision, since many of these become metadata the builder emits (for example a `status` field on components) rather than DTCG tokens.

### DC-L11-01: Starting point (adopt, adapt, or create)
- **Block path:** Strategy > Starting point
- **Questions the designer answers:** Do we build our own system, fork an existing one, or adopt one as-is? How different must we look from everyone else? How much engineering capacity do we have?
- **Options:** (a) Adopt an open system as-is: Material, Carbon, Fluent, or a kit such as Untitled UI (Figma kit with 10,000+ components and variants, and a React library on React Aria + Tailwind v4.3) [S-L11-078]. (b) Adapt: theme an existing library. shadcn create lets you pick Radix or Base UI, a style (Vega, Nova, Maia, Lyra, Mira), base color, theme, icon set, fonts, radius and menu style, and it rewrites the component code [S-L11-071]. Radix Themes exposes accent, gray, radius, scaling and panel background [S-L11-068]. (c) Create a bespoke system. NN/g ranks these from lowest to highest cost: adopt, adapt, create [S-L11-006].
- **Visual effect:** Adopting makes the product look like the source system. The tweakcn README puts it bluntly: "Websites made with shadcn/ui famously look the same" [S-L11-073]. Adapting keeps the component behavior but changes the perceptual layer. Creating gives full brand control at the highest cost.
- **Depends on (upstream):** brand distinctiveness needs (L06), team size (DC-L11-10), tech stack (DC-L11-02).
- **Affects (downstream):** every foundation and component decision; the licensing and update path; how much documentation you must write yourself.
- **Token encoding:** builder metadata `system.origin = adopt|adapt|create`, plus `system.base = "radix-themes"|"shadcn:base-ui:vega"|...`.
- **Platform notes:** Open web systems rarely cover native iOS/Android. zeroheight 2026: 94% of systems support web, 35% iOS, 34% Android [S-L11-030].
- **Accessibility constraints:** Adopting a system built on accessible primitives (React Aria, Radix, Base UI) inherits keyboard and ARIA behavior. It does not inherit contrast if you re-theme colors [inferred].
- **Default + heuristic:** For small teams (1-5 people, which is 61% of teams [S-L11-030]), adapt an accessible headless or themeable base and put your effort into tokens and docs. Create from scratch only if you have a dedicated team and a strong brand differentiation need [inferred from S-L11-006, S-L11-030].
- **Evidence:** [S-L11-006, S-L11-068, S-L11-071, S-L11-073, S-L11-078, S-L11-030]

### DC-L11-02: Scope: products, platforms, stack, audience
- **Block path:** Strategy > Scope
- **Questions the designer answers:** Which products will the system serve, and which will it explicitly not serve? Which platforms (web, iOS, Android, desktop, email, marketing site)? Which frameworks? Who are the consumers (designers, engineers, content, agents)?
- **Options:** Web-only system (most common). Web + native, with platform-specific components. A cross-platform token core with per-platform component libraries. Marketing and product in one system, or separate. zeroheight 2026 frameworks: React 72%, Web Components 36%, Angular 28%, Vue 18%; mobile: Swift/SwiftUI 54%, React Native 47%, Kotlin/Compose 39% [S-L11-030].
- **Visual effect:** A wider scope forces more abstract, context-agnostic components ("card", not "product card") [S-L11-002] and more semantic token layers. A narrow scope allows tighter, more opinionated visuals [inferred].
- **Depends on (upstream):** discovery interviews and audit (DC-L11-04).
- **Affects (downstream):** token tiers and transforms (L07), component inventory (L08), platform conventions (L10), doc audiences, number of code packages to version.
- **Token encoding:** `system.platforms = ["web","ios","android"]`, `system.frameworks = ["react"]`; this drives which exporters the builder runs (CSS vars, Swift, Compose, Tailwind).
- **Platform notes:** Brad Frost's questionnaire asks both "What platforms does the design system apply to?" and "What web technologies does it need to consider?" [S-L11-083]. Marketing-versus-product drift is a live community governance question [S-L00-034 via COMMUNITY-SIGNAL].
- **Accessibility constraints:** Each platform brings its own assistive technology (VoiceOver, TalkBack, NVDA/JAWS), so the test matrix grows with scope [S-L11-093].
- **Default + heuristic:** Scope version 1 to the products the pilot touches, and list the products you will not serve [S-L11-083]. Add platforms only when a real product needs them.
- **Evidence:** [S-L11-083, S-L11-002, S-L11-030, S-L11-093]

### DC-L11-03: System posture (Kholmatova's parameters)
- **Block path:** Strategy > Posture
- **Questions the designer answers:** How strict are the rules? Are parts interchangeable modules or tightly integrated to one product? Does one team own the system, or many?
- **Options:** Strict (comprehensive docs, design and code fully synced, little deviation) versus loose (a framework with room to experiment). Modular (interchangeable, reusable parts) versus integrated (parts optimized for one context). Centralized versus distributed ownership [S-L11-018, S-L11-019]. Mall's "canon vs expanded universe" is a practical middle ground: a strict core plus product-owned extensions [S-L11-014].
- **Visual effect:** Strict and modular gives high consistency and a more uniform, sometimes generic, product. Loose and integrated gives more expressive, product-specific screens and more drift [inferred].
- **Depends on (upstream):** org size and culture, number of products (DC-L11-02), brand needs.
- **Affects (downstream):** contribution model (DC-L11-11), lint and enforcement strictness (DC-L11-24), how many component variants you ship, how "snowflakes" are handled (DC-L11-12).
- **Token encoding:** `governance.posture = {rules: strict|loose, parts: modular|integrated, org: centralized|distributed}`; could set default lint severity (error vs warn).
- **Platform notes:** none specific.
- **Accessibility constraints:** Looser systems need page-level accessibility review, because more UI is built outside the tested components [inferred from S-L11-092].
- **Default + heuristic:** Strict core (tokens, primitives, accessibility behavior), loose edges (patterns, marketing) [inferred]. Kholmatova's point, as summarized by practitioners, is to pick deliberately and manage the downsides [S-L11-019].
- **Evidence:** [S-L11-018, S-L11-019, S-L11-014]

### DC-L11-04: Audit method (interface inventory)
- **Block path:** Process > Discovery > Audit
- **Questions the designer answers:** What UI exists today and how inconsistent is it? What are things called? What should we keep, merge or kill? Is there anything to audit at all (a greenfield product)?
- **Options:** (a) Brad Frost's interface inventory. Cross-disciplinary team, one shared tool, a 30-90 minute screenshot exercise across 16 categories, 5-10 minute presentations per category, then one combined über-document with keep/merge/kill and naming decisions [S-L11-001]. (b) InVision's two inventories: a visual attributes inventory (color, type, spacing) plus a UI element inventory. Add a CSS audit with a tool like CSS Stats to count unique colors and declarations [S-L11-105]. (c) Automated audit: Figma library analytics for detaches and usage [S-L11-035], code scanners such as Omlet or react-scanner for component and prop usage [S-L11-037, S-L11-039]. (d) Greenfield: skip the audit and go straight to visual language [S-L11-105].
- **Visual effect:** The audit sets the size of the consolidation. Merging 40 grays into a 10-step ramp is visible across the whole product [inferred].
- **Depends on (upstream):** scope (DC-L11-02).
- **Affects (downstream):** foundation ramps (L01-L04), component list and priority (L08), naming conventions (L07), the buy-in pitch (shows the "pain of an inconsistent UI" [S-L11-001]).
- **Token encoding:** audit output can seed candidate primitives, for example the most-used hex values clustered into ramps [inferred]; stored as `audit.findings[]` with counts.
- **Platform notes:** Run one inventory per platform; naming differs (sheet vs modal vs dialog; see L10).
- **Accessibility constraints:** Record contrast failures and missing focus states during the audit; this becomes the accessibility baseline [inferred].
- **Default + heuristic:** Do the manual inventory even when automated data exists. Its main value is shared vocabulary and buy-in, not the count [S-L11-001].
- **Evidence:** [S-L11-001, S-L11-105, S-L11-035, S-L11-037, S-L11-039]

### DC-L11-05: Design principles
- **Block path:** Foundations > Principles
- **Questions the designer answers:** What do we value when two good options conflict (for example density vs clarity, delight vs speed)? What makes our product ours?
- **Options:** Figma: 3 or more principles, each with a defining characteristic, its impact on customers and business, and actionable examples, sourced from brand, marketing, writing and support [S-L11-008]. InVision's system principles for the system itself: consistent, self-contained, reusable, accessible, robust [S-L11-105]. Interview findings can be turned into principles, metrics and user stories [S-L11-105].
- **Visual effect:** Principles are the tie-breaker that shapes perceptual choices. "Calm and dense" leads to smaller radii, neutral surfaces and tighter spacing; "friendly" leads to rounder shapes and warmer color [inferred; see L06 for personality-to-visual mapping].
- **Depends on (upstream):** brand strategy (L06), discovery interviews.
- **Affects (downstream):** every default in the builder: the color strategy, type scale ratio, density, motion personality.
- **Token encoding:** not tokens. Stored as `principles[] {name, statement, doExample, dontExample}`; the builder can map principle keywords to suggested token presets [inferred].
- **Platform notes:** none.
- **Accessibility constraints:** Figma's foundations list opens with accessibility: "Disability is part of being human" [S-L11-008]. Making accessibility an explicit principle is common [inferred].
- **Default + heuristic:** 3-5 principles, each testable by a "would this screen pass?" question. Avoid generic words that every product could claim ("simple", "beautiful") [inferred].
- **Evidence:** [S-L11-008, S-L11-105]

### DC-L11-06: Build order (foundations first vs components first vs pilot-driven)
- **Block path:** Process > Build order
- **Questions the designer answers:** Do we finish tokens before any component? Or do we build a real screen and extract?
- **Options:** (a) Foundations first: the Figma course order is spacing, color, typography, elevation, icons, then components [S-L11-009]. (b) Pilot-driven and concurrent: extract components from a real product, apply to the next product, repeat [S-L11-014]. Atomic design moves between atoms and pages at the same time [S-L11-107]. (c) Imaginary product: some teams design a fictional product to escape legacy constraints [S-L11-105].
- **Visual effect:** Foundations-first tends to produce a coherent but untested palette and scale. Pilot-driven produces components that fit real content, but they can be biased toward the pilot. Etsy's pilot-built system "ended up being biased to the needs of that product" [S-L11-105].
- **Depends on (upstream):** whether a pilot exists (DC-L11-07), timeline.
- **Affects (downstream):** how the builder sequences its UI. Should it ask for foundations first, or let the user start from a screen?
- **Token encoding:** n/a (workflow).
- **Platform notes:** none.
- **Accessibility constraints:** Contrast and target size have to be settled at the foundations step; retrofitting them into components is expensive [inferred].
- **Default + heuristic:** Minimal foundations first (color roles, type scale, spacing scale, radius), then pilot-driven components, then back-fill foundations as components expose gaps [inferred synthesis of S-L11-009, S-L11-014, S-L11-107].
- **Evidence:** [S-L11-009, S-L11-014, S-L11-105, S-L11-107]

### DC-L11-07: Pilot selection
- **Block path:** Process > Pilot
- **Questions the designer answers:** Which product or feature proves the system? Is it doable in the pilot window?
- **Options:** Dan Mall's scorecard, as reproduced by InVision: (1) potential for common components, (2) potential for common patterns, (3) high-value elements, (4) technical feasibility, (5) an available champion, (6) scope doable in the pilot timeframe (example: 3-4 weeks), (7) technical independence from legacy, (8) marketing potential [S-L11-105]. Alternative: Primer's incremental approach, "find the biggest pain points, reduce them to their smallest part", with no pilot at all [S-L11-105].
- **Visual effect:** The pilot's visual context (dense dashboard vs marketing page) sets the default density and tone of the first components [inferred].
- **Depends on (upstream):** scope (DC-L11-02), audit (DC-L11-04).
- **Affects (downstream):** the first component list, the first metrics baseline, the adoption story.
- **Token encoding:** `pilots[] {product, score, champion, window}`.
- **Platform notes:** Pick one pilot per platform if the system is multi-platform [inferred].
- **Accessibility constraints:** A pilot is a good place to run the first assistive-technology test pass [inferred].
- **Default + heuristic:** Score 2-3 candidates on the 8 criteria. Pick the one with a champion and common components, then plan a second pilot from a different product family to reduce bias [S-L11-105].
- **Evidence:** [S-L11-105, S-L11-014]

### DC-L11-08: Rollout strategy
- **Block path:** Adoption > Rollout
- **Questions the designer answers:** Big launch or incremental? How do teams migrate? How will it be announced?
- **Options:** (a) Large-scale redesign: build a fuller system (primitives to page layouts) before rolling it out everywhere. It is a big moment, but slow, and it risks pilot bias [S-L11-105]. (b) Incremental rollout: ship parts as they become ready. Less disruptive, but there is no launch moment, so you must create occasions to introduce it [S-L11-105]. Adoption tactics: sandboxes for hands-on use, tutorials, up-to-date docs [S-L11-105]; training, office hours, newsletters, a public style guide [S-L11-002].
- **Visual effect:** Incremental rollout means old and new UI coexist for a while, so the product looks visibly mixed during migration [inferred].
- **Depends on (upstream):** team capacity, business moments (rebrands).
- **Affects (downstream):** versioning (DC-L11-14), deprecation timelines (DC-L11-15), comms rituals (DC-L11-22).
- **Token encoding:** n/a; the builder could emit a migration checklist.
- **Platform notes:** Native apps roll out through app releases, so migrations are slower than on web [inferred].
- **Accessibility constraints:** During a mixed-UI period, both old and new components must meet the target [inferred].
- **Default + heuristic:** Incremental, led by pain points, unless a rebrand gives you a natural big-bang moment [S-L11-105].
- **Evidence:** [S-L11-105, S-L11-002]

---

## Part C. Decision Cards: team, roles, governance, change

### DC-L11-09: Team model
- **Block path:** Governance > Team model
- **Questions the designer answers:** Who makes the system: one product team, a dedicated central team, representatives from many teams, or a mix? Who funds it?
- **Options:** Nathan Curtis (2015): **Solitary**, where one team makes the system mainly for itself and makes it available to others (fast, but other teams' needs become a distraction). **Centralized**, where a dedicated team serves product teams without designing products (broad and unbiased, but lacks product context and has a tenuous position). **Federated**, where designers from multiple product teams decide the system together (relevant and eases adoption, but coordination is hard and it needs people to rise above tribal loyalty). His federated recommendations: represent the platforms that matter, spread UX/visual/interaction/content expertise, mix doers and directors, invest centrally in documentation, reciprocate contribution with autonomy [S-L11-005]. **Hybrid / cyclical** (Salesforce, Jina Anne): a central team acts as "librarian, distributor, and facilitator" plus federated contributors, so product design informs the system and vice versa [S-L11-013]. The InVision handbook's rule of thumb: solitary to move fast, centralized for speed plus buy-in, federated for the most shared ownership [S-L11-105]. 2026 distribution: centralized 51%, hybrid 31%, federated 13%. Under-resourcing by model: centralized 53%, hybrid 68%, federated 74% [S-L11-030].
- **Visual effect:** Centralized tends toward more uniform output. Federated tends toward broader coverage with more variation between products [inferred].
- **Depends on (upstream):** org size, number of products, sponsor (DC-L11-02).
- **Affects (downstream):** contribution model (DC-L11-11), governance flow (DC-L11-12), comms rituals, metrics ownership.
- **Token encoding:** `governance.teamModel = solitary|centralized|federated|hybrid`, `governance.owner`.
- **Platform notes:** Federated models help multi-platform systems, since each platform team is represented [S-L11-005].
- **Accessibility constraints:** A centralized team is the natural owner of component-level accessibility testing [inferred].
- **Default + heuristic:** Start centralized (even with 1-2 people) with a named owner. Add federated contributors once there is a contribution process. Survey data shows federated teams are the most under-resourced [S-L11-030].
- **Evidence:** [S-L11-005, S-L11-013, S-L11-105, S-L11-030]

### DC-L11-10: Roles and staffing
- **Block path:** Governance > Roles
- **Questions the designer answers:** Which roles do we need now, and which later? Who is the owner? Who allocates time and budget?
- **Options:** NN/g minimum: an interaction designer, a visual designer and a developer. Ideal: add a researcher, an architect, a content writer, and an executive sponsor [S-L11-006]. InVision: designers, front-end developers, accessibility experts, content strategists, plus researchers, performance and product people [S-L11-105]. Knapsack adds business analysts and QA, and notes that part-time contributors can work [S-L11-098]. DesignOps roles (lead/specialist, program manager, producer) support process and tooling [S-L11-097]. zeroheight 2026, the most under-represented roles: accessibility specialists (missing in 44% of teams), product managers (44%), DesignOps (24%), content designers (22%), UX researchers (18%). Team size: 1-2 people 28%, 3-5 33%, 6-10 25%, 10+ 8%. Average team of 11 at companies with 5,000+ employees, 2 at companies with 1-100 [S-L11-030].
- **Visual effect:** No content designer means inconsistent labels and error messages. No accessibility specialist means contrast and focus issues ship [inferred].
- **Depends on (upstream):** team model (DC-L11-09), budget.
- **Affects (downstream):** what the builder must automate. Every role a small team lacks is a role the builder can partly play (content linting, contrast checks, docs generation) [inferred].
- **Token encoding:** `team.roles[] {role, person, allocation}`.
- **Platform notes:** Native platforms need iOS and Android engineers on the system team [inferred].
- **Accessibility constraints:** see DC-L11-19.
- **Default + heuristic:** Role skills summary (see the table in Part F): the DS designer needs systems thinking plus Figma variables and components; the DS engineer needs component APIs, tokens pipeline and testing; the PM needs roadmap, adoption and value storytelling; the content designer needs voice and microcopy guidelines; the accessibility specialist needs WCAG plus assistive-technology testing [inferred synthesis of S-L11-006, S-L11-098, S-L11-105].
- **Evidence:** [S-L11-006, S-L11-030, S-L11-097, S-L11-098, S-L11-105]

### DC-L11-11: Contribution model
- **Block path:** Governance > Contribution
- **Questions the designer answers:** Who can contribute? What can they contribute (fixes, enhancements, new components)? What criteria must a contribution meet?
- **Options:** (a) Closed or narrow: Atlassian accepts contributions only from Atlassians, and only fixes and small enhancements (like icons), not new components or patterns. Intake is via Slack and fortnightly critique [S-L11-024]. (b) Criteria-gated open: GOV.UK has proposal criteria (**useful**: evidence many teams need it; **unique**: not already in the system) and publication criteria (**usable**: researched including with disabled users; **consistent**: reuses existing styles and components; **versatile**: works across services, browsers, assistive tech and devices) [S-L11-021]. (c) Open source with process: Carbon uses fork and pull request with a CLA, plus a larger discovery, delivery, launch & scale track for new components, prioritized by business impact and reuse [S-L11-023]. (d) The "system team does the abstraction" view: Dan Mall says not to expect product teams to contribute [S-L11-014]. Curtis: small fixes and large new things need different paths [S-L11-020]. 2026 data: 65% let anyone on a product team contribute, 17% specific people, 14% the DS team only, 4% company-wide. Only 36% are satisfied with their contribution process [S-L11-030].
- **Visual effect:** Looser contribution speeds up coverage but risks visual drift [inferred].
- **Depends on (upstream):** team model (DC-L11-09), posture (DC-L11-03).
- **Affects (downstream):** governance flow (DC-L11-12), lifecycle labels (DC-L11-13), docs (a contribution guide page).
- **Token encoding:** `governance.contribution = {who, types:[fix, enhancement, new], criteria:[...]}`.
- **Platform notes:** none.
- **Accessibility constraints:** Make accessibility testing a publication gate, as GOV.UK's "usable" and "versatile" criteria do [S-L11-021].
- **Default + heuristic:** Two lanes: a fast lane for fixes, icons and docs; a proposal lane (RFC) for new components, gated by "useful + unique" before any build work [S-L11-021, S-L11-020].
- **Evidence:** [S-L11-014, S-L11-020, S-L11-021, S-L11-023, S-L11-024, S-L11-030]

### DC-L11-12: Governance flow and decision records
- **Block path:** Governance > Process
- **Questions the designer answers:** What happens when a team needs something the system does not have? Who approves changes? Where do we record why a decision was made?
- **Options:** Brad Frost's 10-step flow: (1) use existing components; (2) contact the DS team when something is missing; (3) decide whether it is a one-off "snowflake", which goes to the product backlog, or a system addition, which goes to the DS backlog; (4) concept; (5) joint review; (6) the DS team designs, builds and tests (content, accessibility, cross-browser, responsive, stress tests, reviews, trial apps); (7) final review; (8) document, update the changelog, merge; (9) release with semver and communicate; (10) product team upgrades and tests [S-L11-003]. Decision records: GOV.UK runs a public repo with RFCs (proposals refined in the open) and ADRs (decisions made), so it can "answer questions from our users as to why things are the way they are". It was inspired by React RFCs and Swift Evolution [S-L11-095]. Rituals: Atlassian's fortnightly critique [S-L11-024]; Mall's alternating flow weeks and system weeks [S-L11-014].
- **Visual effect:** A snowflake policy controls how much off-system UI exists [inferred].
- **Depends on (upstream):** team model, contribution model.
- **Affects (downstream):** versioning and release cadence, docs changelog, metrics (snowflake counts).
- **Token encoding:** `decisions[] {id, type: rfc|adr, status: proposed|accepted|rejected|superseded, date, links}`. The builder could keep an ADR per foundation choice, recording the "why" behind each token decision [inferred].
- **Platform notes:** none.
- **Accessibility constraints:** Step 6 of the flow includes accessibility testing before release [S-L11-003].
- **Default + heuristic:** Adopt the 10-step flow. Log every foundation decision as an ADR from day one; the builder's Decision Cards map naturally to ADRs [inferred].
- **Evidence:** [S-L11-003, S-L11-095, S-L11-024, S-L11-014]

### DC-L11-13: Component lifecycle / status labels
- **Block path:** Governance > Component status
- **Questions the designer answers:** How do consumers know whether a component is safe for production? How mature does something have to be before it is "stable"?
- **Options:** Primer, current: **Experimental** (proof of concept or work in progress) > **Ready** (production, long-term support, breaking changes only in a major with migration guidance) > **Deprecated** (avoid; docs explain why and name alternatives; consumers see warnings) [S-L11-025]. Primer, earlier: Experimental > Alpha (no external dependencies, no hard-coded values) > Beta > Stable (API stable, no breaking changes for at least a month) > Deprecated [S-L11-026, history]. Carbon shows accessibility test status only once components are stable [S-L11-091].
- **Visual effect:** none directly; it controls how much unstable UI reaches users [inferred].
- **Depends on (upstream):** governance flow (DC-L11-12).
- **Affects (downstream):** docs badges, lint rules (warn on experimental imports), versioning (DC-L11-14).
- **Token encoding:** `component.status = experimental|ready|deprecated` (plus optional `alpha|beta`), `component.since`, `component.replacedBy`.
- **Platform notes:** Status can differ per platform package (ready on web, experimental on iOS) [inferred].
- **Accessibility constraints:** Make "passes a11y test matrix" an entry criterion for Ready [inferred from S-L11-091, S-L11-021].
- **Default + heuristic:** Three states (experimental, ready, deprecated) are enough for most teams. Primer itself simplified from five to three [S-L11-025, S-L11-026].
- **Evidence:** [S-L11-025, S-L11-026, S-L11-091]

### DC-L11-14: Versioning strategy
- **Block path:** Change > Versioning
- **Questions the designer answers:** Do we version the whole library or each component? How often do we release? How do design files and code versions line up?
- **Options:** SemVer 2.0.0: MAJOR for incompatible changes, MINOR for backward-compatible features (and deprecations, documented), PATCH for fixes; 0.y.z means anything may change [S-L11-106]. Library-level major bundles (Carbon, Material, Polaris); incremental frequent releases (Spectrum is nearly monthly, SLDS releases as needed); per-component versioning (Atlassian, Twilio Paste) [S-L11-028]. Figma: semver for libraries plus branching to test changes before merging (Organization/Enterprise plans) [S-L11-010].
- **Visual effect:** Big majors create visible "generation" shifts (Carbon v10 to v11); per-component versions let visuals drift between products running different versions [inferred].
- **Depends on (upstream):** number of packages and platforms (DC-L11-02), rollout (DC-L11-08).
- **Affects (downstream):** release notes, migration guides, deprecation windows, the token package version (tokens need semver too) [inferred].
- **Token encoding:** `package.version` per artifact (tokens, components-web, components-ios, figma-library); the builder should version the token export itself [inferred].
- **Platform notes:** Native libraries ship through package managers (SPM, Gradle), while Figma libraries publish separately. Keeping versions aligned is manual unless automated. Only 5% of teams have bi-directional token sync; 60% have no automation [S-L11-030].
- **Accessibility constraints:** An accessibility fix that changes behavior (focus order, roles) may count as breaking for consumers' tests [inferred].
- **Default + heuristic:** One semver for the whole library while small. Move to per-package versions once you have more than one platform. Release on a predictable cadence and write release notes every time; release notes are the most common governance ritual, at 56% [S-L11-030].
- **Evidence:** [S-L11-106, S-L11-028, S-L11-010, S-L11-030]

### DC-L11-15: Deprecation and migration policy
- **Block path:** Change > Deprecation
- **Questions the designer answers:** How much notice do teams get? How are deprecations marked in design and code? Do we ship codemods?
- **Options:** Polaris: announce deprecations and document migrations one month before the next major; mark with `@deprecated` JSDoc on components and props; show a dev-only `console.warn` for deprecated prop values; ship automated migrations (codemods); document in the major-version guide (reason, alternatives, automated and manual steps); remove in the next major. Deprecated tokens go on the stylelint disallowed list [S-L11-100]. Primer: deprecated docs explain why, list alternatives, and warn the consumer [S-L11-025]. SemVer: deprecate in a minor with docs, remove in a major [S-L11-106]. Large-scale example: Shopify deprecated Polaris React in favor of Polaris web components and published 60+ component migration pages [S-L11-101].
- **Visual effect:** none directly; it governs how long legacy visuals persist [inferred].
- **Depends on (upstream):** versioning (DC-L11-14), lifecycle (DC-L11-13).
- **Affects (downstream):** docs (a migration guide per major), lint rules, Figma library (deprecated components moved to a "deprecated" page) [inferred].
- **Token encoding:** DTCG supports `$deprecated` on tokens (covered by L07) [inferred; L07 to confirm]; `component.deprecated = {since, removeIn, replacement}`.
- **Platform notes:** Native apps can't force upgrades, so deprecation windows are longer [inferred].
- **Accessibility constraints:** none specific.
- **Default + heuristic:** Deprecate in a minor, remove in the next major, give at least one release cycle of notice, and pair every removal with a codemod or migration guide [S-L11-100, S-L11-106].
- **Evidence:** [S-L11-100, S-L11-101, S-L11-025, S-L11-106]

### DC-L11-16: Source of truth and design-code sync
- **Block path:** Change > Source of truth
- **Questions the designer answers:** Is the truth in Figma or in code? How do tokens move between them? What happens when they disagree?
- **Options:** (a) Figma-first: variables authored in Figma and exported. (b) Code-first: tokens and components in code, with Figma mirroring them. The community majority in 2026 says "Code is the source of truth" [S-L00-034/040 via COMMUNITY-SIGNAL]. (c) Token-platform-first: Tokens Studio or Supernova as the hub syncing to GitHub [S-L11-060, S-L11-061]. (d) Mapped: Figma Code Connect links Figma nodes to code components, which the Figma MCP exposes to agents [S-L11-043]. zeroheight 2026: tokens live in Figma variables for 90% and in code for 82%; 66% document them; 60% have no automation, 29% automate design-to-code, 6% code-to-design, 5% bi-directional [S-L11-030].
- **Visual effect:** Without sync, design and code drift and products visibly diverge from the spec. "Discrepancies between design and code" is a named survey challenge [S-L11-034].
- **Depends on (upstream):** stack (DC-L11-02), team skills.
- **Affects (downstream):** tooling choice (DC-L11-17), agent context (DC-L11-23), versioning.
- **Token encoding:** the builder should emit DTCG JSON as the canonical file, plus transforms (L07 owns format details).
- **Platform notes:** Code-first needs a transform pipeline (for example Style Dictionary v5) per platform (L07, L10).
- **Accessibility constraints:** Contrast checks are easiest to automate on the canonical token file [inferred].
- **Default + heuristic:** Make the builder's own token file the source of truth. Export to Figma variables and to code in one step, which closes the gap that 60% of teams have [S-L11-030; inferred].
- **Evidence:** [S-L11-030, S-L11-034, S-L11-043, S-L11-060, S-L11-061, COMMUNITY-SIGNAL]

---

## Part D. Decision Cards: documentation, accessibility, measurement

### DC-L11-17: Documentation platform
- **Block path:** Docs > Platform
- **Questions the designer answers:** Where do docs live? Who maintains them? Do engineers need live code examples? Do agents need to read them?
- **Options:** zeroheight 2026 usage: Figma 69%, Storybook 61%, zeroheight 32%, Confluence 18%, custom 16%. Satisfaction with documentation tools is 60%, against 73% for design tools [S-L11-030]. Options named by Figma: custom sites (Material, Carbon, eBay Playbook), Notion or Confluence for quick setup, Storybook for technical specs, custom plugins [S-L11-088]. Docs platforms now also serve agents: zeroheight MCP [S-L11-104], Supernova scoped MCP servers plus llms.txt [S-L11-049, S-L11-061], Storybook MCP docs toolset [S-L11-044].
- **Visual effect:** n/a (the docs site itself should use the system; Frost: "make it approachable" [S-L11-002]).
- **Depends on (upstream):** team size, source of truth (DC-L11-16), audience.
- **Affects (downstream):** contribution friction, agent readiness (DC-L11-23), update cadence.
- **Token encoding:** n/a; the builder should generate docs pages from the same data model as the tokens [inferred].
- **Platform notes:** Storybook's component manifest (which powers the MCP docs toolset) supports React, Angular (Vite) and Vue 3 (Vite) [S-L11-044].
- **Accessibility constraints:** The docs site must itself meet the target [inferred].
- **Default + heuristic:** Small teams: document in Figma plus Storybook. Add a docs platform when non-engineers need to author. Whatever the tool, also publish a machine-readable export (llms.txt or MCP) [S-L11-048, S-L11-108].
- **Evidence:** [S-L11-030, S-L11-088, S-L11-104, S-L11-049, S-L11-044, S-L11-048]

### DC-L11-18: Component documentation page template
- **Block path:** Docs > Component page
- **Questions the designer answers:** What goes on each component page? What is the split between usage guidelines (when and why) and specs (what and how)?
- **Options:** Carbon uses tabs (Usage, Style, Code, Accessibility). The Usage tab runs: live demo, accessibility test status, overview (when to use, when not to use, variants), formatting (anatomy, sizes, emphasis, alignment), content (labels, RTL internationalization, overflow), universal behaviors (focus, states, mouse and keyboard interactions, loading), then per-variant best practices [S-L11-090]. GOV.UK: when to use, how it works (every variant with HTML and a Nunjucks macro plus an options table), research on this component, recent changes, help improve this component [S-L11-089]. Figma recommends usage guidelines with real examples, specs (anatomy, dimensions, behavior), code snippets, interactive states, and accessibility requirements, written for designers, developers and PMs [S-L11-088]. Frost: show where each pattern is used in real products ("make it contextual") [S-L11-002].
- **Visual effect:** n/a.
- **Depends on (upstream):** component inventory (L08).
- **Affects (downstream):** agent context. Sanity's evals found structured, JSON-specified docs with code chunks beat prose Markdown for agents [S-L11-108].
- **Token encoding:** `component.docs = {whenToUse[], whenNotToUse[], anatomy[], variants[], states[], content[], a11y{keyboard[], screenReader[], testStatus}, code{props[], examples[]}, research[], changelog[]}`.
- **Platform notes:** Multi-platform pages need per-platform code tabs and platform-specific behavior notes [inferred].
- **Accessibility constraints:** Include a per-component accessibility section with keyboard, screen reader and test status, as Carbon does [S-L11-091].
- **Default + heuristic:** Use the template above. Make "docs complete" part of the definition of done, since Figma calls docs updates "a required step" [S-L11-088].
- **Evidence:** [S-L11-088, S-L11-089, S-L11-090, S-L11-091, S-L11-002, S-L11-108]

### DC-L11-19: Accessibility program
- **Block path:** Foundations > Accessibility > Program
- **Questions the designer answers:** Which conformance target? What does the system guarantee, and what must product teams still do? How is each component tested?
- **Options:** Target: WCAG 2.2 AA is the current norm. GOV.UK commits to WCAG 2.2 AA and supports the latest version once it has been available for at least a year [S-L11-093]. Testing: automated tools (jest-axe, @axe-core/puppeteer, html-validate), but GOV.UK notes "only about 30% of issues are found by automated testing tools". Manual assistive-technology testing covers screen readers, magnifiers, high contrast, and speech recognition [S-L11-093]. Carbon publishes per-component status: default state, advanced states and keyboard navigation tested automatically; screen reader tested manually with JAWS, VoiceOver, NVDA [S-L11-091]. Responsibility split: "Using the GOV.UK Design System in a service does not immediately make that service accessible" [S-L11-092]. Some success criteria apply at page level (for example redundant entry), so they stay with the consuming team [S-L11-094].
- **Visual effect:** The target bounds the color, type size, focus ring and target-size options in every other lane (L01-L04, L08).
- **Depends on (upstream):** legal context (for example public sector, EU accessibility rules; see gaps), principles.
- **Affects (downstream):** contrast minimums in color ramps (L01), minimum type sizes (L02), target sizes (L03), focus indicators (L04), per-component ARIA patterns (L08), the component Ready gate (DC-L11-13).
- **Token encoding:** `system.a11yTarget = "WCAG 2.2 AA"`; the builder validates token pairs against it. DESIGN.md's linter already checks WCAG contrast [S-L11-047].
- **Platform notes:** Native targets have their own guidance (Apple HIG, Material); see L10.
- **Accessibility constraints:** This is the constraint card itself.
- **Default + heuristic:** WCAG 2.2 AA. The system guarantees component-level behavior and contrast-safe token pairs. Product teams own page-level criteria, content, and composition testing. Publish that split explicitly [S-L11-092, S-L11-093, S-L11-094]. Signal: in the zeroheight 2026 report only 59% of systems include accessibility guidelines, and accessibility satisfaction is 44% [S-L11-030].
- **Evidence:** [S-L11-091, S-L11-092, S-L11-093, S-L11-094, S-L11-030, S-L11-047]

### DC-L11-20: Success metrics and instrumentation
- **Block path:** Measurement > Metrics
- **Questions the designer answers:** What does "adopted" mean? How will we prove value to leadership? What can we instrument automatically?
- **Options:** What teams measure (zeroheight 2026): adoption 41%, component usage in design tools 41%, in code 38%, accessibility compliance 36%, development speed 31%, team happiness 28%, consistency 26%, design speed 23%, bug volume 20%, contributions 20%, docs coverage 20%, NPS 9%, ROI 5%. Tools: Figma analytics 56%, surveys 50%, code repo analytics 37%, dedicated code adoption tracking 9% [S-L11-030]. Instruments: Figma library analytics (components, styles, variables; instances, insertions, detachments by team and file; Organization and Enterprise plans; daily; 1 year of history; variables and styles tracked since 10 Oct 2024; API on Enterprise only) [S-L11-035]. Pinterest's design adoption = DS layers / total layers (for example 7/15 = 46.6%), limited to handoff pages edited in the last 2 weeks, computed nightly via the REST API [S-L11-038]. athenahealth tracks detaches as signals of bugs or feature requests (100k insertions a month) [S-L11-036]. Code: Omlet (React usage, props, adoption trends) [S-L11-037]; react-scanner (counts components and props, raw report with locations, `importedFrom` filter) [S-L11-039]. ROI evidence: Sparkbox found a form built 47% faster with Carbon (4.2 h vs 2 h median, 8 developers, small n) [S-L11-099]. Figma cites designers completing tasks 34% faster (vendor study) [S-L11-036].
- **Visual effect:** n/a; detach-rate spikes point at components whose visuals or flexibility don't fit [S-L11-036].
- **Depends on (upstream):** goals set at kickoff (DC-L11-01 and Phase 1).
- **Affects (downstream):** roadmap priorities, deprecation choices ("component deprecation impact estimates" in Omlet [S-L11-037]).
- **Token encoding:** `metrics[] {name, definition, source: figma|code|survey, target}`.
- **Platform notes:** Native code usage needs separate scanners. Pinterest tracked web, iOS and Android code adoption separately [S-L11-038].
- **Accessibility constraints:** Track accessibility defects per component as a quality metric [inferred].
- **Default + heuristic:** Start with three measures: design adoption (Figma analytics), code adoption (a scanner), and a quarterly satisfaction survey. Add speed or ROI studies only when leadership asks [inferred from S-L11-030 frequencies].
- **Evidence:** [S-L11-030, S-L11-035, S-L11-036, S-L11-037, S-L11-038, S-L11-039, S-L11-099]

### DC-L11-21: Maturity stage targeting
- **Block path:** Measurement > Maturity
- **Questions the designer answers:** Where is our system now, and what is the next stage's work?
- **Options:** Sparkbox (Ben Callahan, 2021) has 4 stages: (1) Building version one, (2) Growing adoption, (3) Surviving the teenage years (leadership scrutiny, proving business value, consistency vs flexibility), (4) Evolving a healthy product (dedicated team, governance, subscriber programs). It also distinguishes grassroots from top-down origins [S-L11-033]. The latest Sparkbox survey is 2022 (200+ respondents): onboarding, training, support and a contribution model mark mature systems [S-L11-034]. zeroheight 2026 adoption distribution: fully 7%, widely 31%, moderately 38%, minimally 22%, not 1%. Trust: high 42%, moderate 49%, low 8% [S-L11-030].
- **Visual effect:** n/a.
- **Depends on (upstream):** metrics (DC-L11-20).
- **Affects (downstream):** which builder features matter. Stage 1 users need generation and defaults; stage 2 needs docs and comms; stage 3 needs metrics and ROI; stage 4 needs governance and versioning [inferred].
- **Token encoding:** `system.maturityStage = 1..4`.
- **Platform notes:** none.
- **Accessibility constraints:** Stage 3 is where accessibility metrics are typically demanded [S-L11-033].
- **Default + heuristic:** Most builder users will be at stage 1. Design the onboarding for stage 1 and grow features toward stage 2-4 [inferred].
- **Evidence:** [S-L11-033, S-L11-034, S-L11-030]

### DC-L11-22: Communication and community rituals
- **Block path:** Adoption > Communication
- **Questions the designer answers:** How will people hear about changes? Where do they get help?
- **Options:** zeroheight 2026 rituals: release notes 56%, roadmap 48%, office hours 33%, communication plan 24%, designer/engineer secondments 21%, roadshows 14%, newsletters 12%. Only 39% are satisfied with how DS changes are communicated. 44% have no dedicated community-building focus [S-L11-030]. Frost's list: internal blog, newsletters, changelogs, roadmaps, success stories, training (pairing, workshops, webinars, onboarding), support (issue tracker, office hours, Slack, forums), and a public style guide [S-L11-002]. The InVision handbook adds sandboxes for hands-on trials [S-L11-105].
- **Visual effect:** n/a.
- **Depends on (upstream):** rollout (DC-L11-08), versioning.
- **Affects (downstream):** adoption rates. "Communication/community" is cited as an adoption success factor by 59% [S-L11-030].
- **Token encoding:** the builder could auto-generate release notes from token and component diffs; DESIGN.md's CLI already has a `diff` command [S-L11-047].
- **Platform notes:** none.
- **Accessibility constraints:** none.
- **Default + heuristic:** Minimum viable set: release notes every release, a public roadmap, and a support channel [S-L11-030, S-L11-002].
- **Evidence:** [S-L11-030, S-L11-002, S-L11-105, S-L11-047]

---

## Part E. AI-era decisions and trends (2025-2026, verified 2026-09-23)

### DC-L11-23: Agent-readable distribution (how AI tools consume the system)
- **Block path:** Distribution > Agent context
- **Questions the designer answers:** Which AI tools will our teams use to generate UI? In what format do they need our system? Do we serve it live (MCP) or as files (DESIGN.md, llms.txt, rules files, registry)?
- **Options (all verified live):**
  - **Figma MCP server.** Remote at `mcp.figma.com/mcp` on all seats and plans; desktop server needs a Dev or Full seat. Write-to-canvas is remote-only and a free beta that will later be usage-based [S-L11-041]. Tools include `get_design_context`, `get_variable_defs`, `get_metadata`, `get_screenshot`, `search_design_system`, `get_libraries`, `get_code_connect_map`/`add_code_connect_map`, `use_figma`, `generate_figma_design`, and the prompt `create_design_system_rules`, which gives agents codebase-aware context [S-L11-043]. Figma argues MCP is "the unlock" for design systems and AI [S-L11-040].
  - **Storybook MCP** (`@storybook/addon-mcp`, docs show v10.6): development, docs and testing toolsets; the component manifest is off by default; docs toolset supports React, Angular (Vite), Vue 3 (Vite) [S-L11-044]. L00 confirms 10.3 added MCP for React and 10.6.0 is current stable (2 Sep 2026) [COMMUNITY-SIGNAL].
  - **shadcn registry + MCP:** registries declared in `components.json` (`"@acme": "https://acme.com/r/{name}.json"`) with a `registry.json` index; `shadcn mcp init --client claude` [S-L11-045]. v0 opens registry items through `/r/{name}.json` [S-L11-054].
  - **DESIGN.md** (Google Stitch, open-sourced 21 Apr 2026): YAML front matter (colors, typography, rounded, spacing, components with `{path.to.token}` references) plus 8 ordered prose sections (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts). CLI `lint` (11 rules including WCAG contrast), `diff`, and `export` to Tailwind or W3C DTCG. Apache-2.0, alpha [S-L11-046, S-L11-047].
  - **llms.txt:** Cloudscape publishes an llms.txt index plus per-page Markdown guidelines and JSON API definitions [S-L11-048]; the CMS Design System has llms.txt guidance [S-L11-050]; Supernova serves llms.txt [S-L11-049].
  - **Figma Make kits:** the DS as an npm package plus a `guidelines/` folder (Guidelines.md, setup.md, styles.md, tokens.md, components/). "Multiple short guidelines files are better than a few large files" [S-L11-051].
  - **Docs-platform MCPs:** zeroheight MCP (DS context, drift-detection audits, clients from Figma Make to Claude Code, v0, Lovable; only published content is exposed) [S-L11-104]; Supernova scoped MCP servers [S-L11-061].
- **Visual effect:** With context, generated UI uses real tokens and components. Without it, agents "reinvented existing components and hardcoded values" (community report) [COMMUNITY-SIGNAL], and 59% of teams report UI bypassing the design system [S-L11-031].
- **Depends on (upstream):** source of truth (DC-L11-16), docs structure (DC-L11-18).
- **Affects (downstream):** export formats the builder must emit; docs structure (short, structured files).
- **Token encoding:** the builder should emit DTCG JSON (canonical), DESIGN.md (front matter can be exported to DTCG [S-L11-047]), a shadcn-compatible registry (`registry.json` + `r/{name}.json`), and an llms.txt index [inferred from S-L11-045, S-L11-047, S-L11-048].
- **Platform notes:** Most agent tooling targets React and web today (v0, Lovable, Bolt, shadcn, Storybook manifest) [S-L11-044, S-L11-052, S-L11-053, S-L11-103]. Native agent context is a gap [inferred].
- **Accessibility constraints:** Structured docs plus linting cut accessibility violations per iteration from 5.1 to 0.6 in Sanity's evals [S-L11-108].
- **Default + heuristic:** Ship at least one live channel (MCP) and one file channel (DESIGN.md + DTCG). Keep guidelines as many short, structured files. Test with evals rather than hoping docs changes work [S-L11-108, S-L11-051].
- **Evidence:** [S-L11-040, S-L11-041, S-L11-043, S-L11-044, S-L11-045, S-L11-046, S-L11-047, S-L11-048, S-L11-049, S-L11-051, S-L11-054, S-L11-104, S-L11-108, S-L11-031]

### DC-L11-24: AI guardrails (enforcement, linting, evals)
- **Block path:** Governance > AI guardrails
- **Questions the designer answers:** How do we stop AI-generated UI from drifting off-system? How do we know our docs work for agents? What is allowed in "shadow AI"?
- **Options:** (a) Adherence scanning in the generator. Lovable scans connected projects for raw colors, custom components where system components exist, inline style overrides and token deviations, then attempts corrections [S-L11-053]. (b) Drift detection audits at the docs layer (zeroheight MCP) [S-L11-104]. (c) Conformance measurement (Knapsack now positions itself as AI conformance evaluation; its "~70% of AI styling decisions drift off-system" is a vendor claim) [S-L11-062]. (d) Linters and code chunks ("on-rails" solutions) plus eval harnesses (Sanity open-sourced one) [S-L11-108]. (e) Token lint: DESIGN.md `lint` [S-L11-047]; Polaris uses stylelint to disallow deprecated tokens [S-L11-100]. Survey context: 44% of organizations tolerate shadow AI; 50% say other teams' AI use creates real problems [S-L11-031].
- **Visual effect:** Enforcement is what keeps AI-built screens looking like the product [inferred].
- **Depends on (upstream):** posture (DC-L11-03), agent distribution (DC-L11-23).
- **Affects (downstream):** lint config export, CI checks, metrics (off-system rate).
- **Token encoding:** `lint.rules[] {id, severity}`, for example `no-raw-color`, `no-unknown-token`, `no-deprecated-token`, `contrast-min` [inferred].
- **Platform notes:** Web tooling is mature (stylelint, eslint); native needs custom rules [inferred].
- **Accessibility constraints:** Include contrast and ARIA lint rules [S-L11-047, S-L11-108].
- **Default + heuristic:** The builder should export lint rules alongside tokens, so every generated system arrives with its own guardrails [inferred].
- **Evidence:** [S-L11-053, S-L11-104, S-L11-062, S-L11-108, S-L11-047, S-L11-100, S-L11-031]

### DC-L11-25: Theming dimensions (modes, brands, density, platforms)
- **Block path:** Foundations > Theming scope
- **Questions the designer answers:** Do we need light and dark? Multiple brands or white-label? Density or breakpoint modes? Per-platform values?
- **Options:** zeroheight 2026, how tokens are structured for theming: visual modes (light/dark) 76%, brands 63%, breakpoints 38%, devices or platforms 24%. Token layers in use: primitives 90%, semantic 85%, component-level 52%. Library setup: single library 79%, cross-library aliasing 21% [S-L11-030]. Generator precedent: Radix exposes appearance, radius, scaling (90-110%) and panel background as theme axes [S-L11-068, S-L11-069]; shadcn create exposes style (density and shape personality: Nova compact, Maia soft and rounded, Lyra boxy and sharp, Mira dense) [S-L11-071]; Material Theme Builder exposes contrast level [S-L11-067].
- **Visual effect:** Each dimension multiplies the token values a designer must check. For example, 2 modes x 3 brands = 6 palettes to contrast-test [inferred].
- **Depends on (upstream):** scope (DC-L11-02), brand architecture (L06).
- **Affects (downstream):** token tiers and mode structure (L07), color ramps (L01), density scales (L03).
- **Token encoding:** DTCG plus modes. L07 owns the details; the builder stores `theming.dimensions = ["mode","brand","density"]` [inferred].
- **Platform notes:** Platform dimension overlaps with L10 (per-platform type and size values).
- **Accessibility constraints:** Every mode and brand combination must pass the contrast target (DC-L11-19); Material's contrast levels are one way to offer higher-contrast variants [S-L11-067].
- **Default + heuristic:** Light plus dark from day one, since 76% of systems do it. Add brand and density dimensions only when a real product needs them [S-L11-030].
- **Evidence:** [S-L11-030, S-L11-067, S-L11-068, S-L11-069, S-L11-071]

### E1. Trend facts table (verified live on 2026-09-23)

| Trend | Verified fact | Source |
|---|---|---|
| AI adoption in DS teams | 56% of DS teams use AI (10% built into processes, 46% experimenting), 44% not using. Use cases: code generation 71%, docs generation 60%, AI prototyping 50%, linting 28%, design generation 24%. Impact rated neutral by 52%. | [S-L11-030] |
| What works vs hype (survey) | State of AI in DS 2026 (n=123): 82% use AI in some form; 74% use Claude and 56% Figma Make; 63% most satisfied with AI for documentation; only 17% rate their docs "very AI-ready"; design generation net satisfaction -53; 67% say AI is "somewhat or way overhyped". | [S-L11-031] |
| Concerns | Top AI concern in the zeroheight report is design generation (61%), then code generation (35%). | [S-L11-030] |
| MCP as the channel | 48% already operate an MCP server. Figma, Storybook, shadcn, zeroheight, Supernova, Stitch, Token Designer/Bezel all ship MCP. | [S-L11-031, S-L11-043, S-L11-044, S-L11-045, S-L11-104, S-L11-061, S-L11-077, S-L11-081] |
| Docs for machines | Doc restructure raised agent success: Haiku 4.5 3%->47%, Sonnet 4.6 20%->90%, Opus 4.8 40%->100%; JSON beat Markdown; code chunks and linting helped further. | [S-L11-108] |
| File standards | DESIGN.md open-sourced 21 Apr 2026 (alpha, Apache-2.0); llms.txt used by Cloudscape (Oct 2025), CMS, Supernova. | [S-L11-046, S-L11-047, S-L11-048, S-L11-050, S-L11-049] |
| AI builders ingest systems | v0 Design Systems 2.0 (repo, Figma, Storybook, npm; saved as a "skill"); Lovable design-system projects (`design-system.json`, `system.md`, adherence scanning); Bolt Design System Agents (26 Mar 2026); Figma Make kits; Claude Design (17 Apr 2026, builds the team DS from codebase and design files); Stitch (18 Mar 2026, extracts DS from URL, DESIGN.md, MCP); Magic Patterns Design System Agent (10 Jun 2026). | [S-L11-052, S-L11-053, S-L11-103, S-L11-051, S-L11-055, S-L11-077, S-L11-080] |
| Figma Config 2026 | Figma Motion (timing and easing variables, animated components), generative plugins, custom shaders, agent skills + MCP (open beta from 24 Jun 2026), code layers (closed beta). New "materials" for systems to cover. | [S-L11-057, S-L11-058 snippet] |
| Practitioner stance | Brad Frost (2023): the design system "carries the burden of the boring" while humans keep judgment [S-L11-085]. Brad Frost (Dec 2025): "agentic design systems" means AI deliberately constrained to DS materials, as opposed to vibe coding. Community pushback: "agentic design system... really doesn't mean anything", since a DS is already usage documentation for a person or an agent. | [S-L11-086, COMMUNITY-SIGNAL] |

**What works (evidence-backed):** serving the system to agents through MCP or structured files; short, structured, machine-readable docs; code chunks and lint rules; evaluating agent output with evals; AI for documentation drafting [S-L11-108, S-L11-031, S-L11-051].
**What is hype or weak (evidence-backed):** unconstrained AI design generation (net satisfaction -53, the top concern at 61%); expecting prose docs alone to steer agents; "agentic design system" as a label with no new substance [S-L11-031, S-L11-030, S-L11-108, COMMUNITY-SIGNAL].

---

## Part F. Roles and skills

| Role | What they own | Core skills | Evidence |
|---|---|---|---|
| DS lead / product manager | Vision, roadmap, prioritization, value story, sponsor relations | Product management, stakeholder management, metrics and ROI storytelling | Missing in 44% of teams [S-L11-030]; Frost's "make it official", "who allocates time, budget, resources" [S-L11-002, S-L11-083] |
| DS designer (visual + interaction) | Foundations, tokens, Figma libraries, component design, audits | Systems thinking, Figma variables, modes and components, visual design, interaction states | NN/g minimum team [S-L11-006]; InVision [S-L11-105] |
| DS engineer | Component code, token pipeline, releases, testing, codemods | Component API design, a11y implementation, build and release tooling, token transforms | NN/g minimum team [S-L11-006]; Polaris codemods [S-L11-100] |
| Content designer / UX writer | Voice and tone, microcopy rules, component content guidance | Writing, content strategy, localization awareness | Missing in 22% [S-L11-030]; Carbon "Content" section [S-L11-090] |
| Accessibility specialist | Target, test matrix, audits, AT testing, a11y docs | WCAG 2.2, ARIA APG, screen readers, speech and magnification testing | Missing in 44% [S-L11-030]; GOV.UK AT testing [S-L11-093] |
| UX researcher | Discovery interviews, usability of components and docs | Interviewing, synthesis, testing "with and without the system" | Missing in 18% [S-L11-030]; Figma testing guidance [S-L11-010] |
| DesignOps / program manager | Process, tooling, rituals, cross-team frameworks | Program management, tooling curation, operations | Missing in 24% [S-L11-030]; NN/g roles [S-L11-097] |
| QA / business analyst (optional) | Implementation fidelity, market and localization context | Test design, domain knowledge | [S-L11-098] |

Staffing reality check: 28% of teams have 1-2 people and 61% have 5 or fewer [S-L11-030]. A builder aimed at these teams has to cover the missing roles with automation: content lint, contrast validation, docs generation, release notes [inferred].

---

## Part G. Competitor and reference products (24 reviewed)

| # | Product | Category | What it generates | Inputs it asks for | Gaps vs a decision-guiding builder | Evidence |
|---|---|---|---|---|---|---|
| 1 | **Figma** (variables, libraries, Make kits, AI brand-guidelines generator, MCP) | Design tool + AI | Variables, styles, components, libraries. Make generates brand guidelines (typography, color, components, usage, voice and tone, logo spacing, a11y notes) from a prose brand description. The MCP server serves context to agents. | Natural-language brand description; existing libraries and tokens; for Make kits, an npm package plus a guidelines folder | No guided decision flow or explanation of trade-offs; no governance, versioning or metrics setup (analytics only on Org/Enterprise); branching needs Org/Enterprise | [S-L11-079, S-L11-051, S-L11-043, S-L11-035, S-L11-010] |
| 2 | **Tokens Studio** | Token management | Token sets and themes; sync to GitHub; Style Dictionary exports; Figma/Penpot | Manually authored tokens | Assumes you already know your token decisions; no guidance on values, principles or governance | [S-L11-060] |
| 3 | **Supernova** | DS platform | Docs, token pipelines with automatic PRs, component health, adoption analytics, scoped MCP servers, llms.txt | Figma, Storybook, GitHub/GitLab, Tokens Studio | Hosts an existing system; does not help create the decisions | [S-L11-061, S-L11-049] |
| 4 | **zeroheight** | Docs platform | Documentation sites, measurement, MCP with drift detection | Figma, Storybook, code, authored docs | Documentation of decisions made elsewhere; no generation of foundations | [S-L11-104, S-L11-030] |
| 5 | **Knapsack** | Enterprise DS / AI conformance | Aggregates standards from GitHub, Figma, Jira, Storybook, Supernova; measures AI output conformance | Existing enterprise sources | Enterprise-only, sales-led; assumes a mature system | [S-L11-062] |
| 6 | **UXPin Merge** | Code-backed design | Prototypes with real React or Web components; built-in MUI, shadcn and others | Git repo, Storybook, npm | Designs *with* a system; does not define one | [S-L11-063] |
| 7 | **Specify** | Token pipeline | (discontinued) formerly 50+ token types to CSS/Tailwind/RN/Flutter parsers | Figma, Tokens Studio, JSON | Discontinued: market signal that pipeline-only tools struggle | [S-L11-064] |
| 8 | **Relume Style Guide Builder** | Web style guide (AI) | Color palette with shades, font pairing, button/form/card styles; export to Figma, Webflow, React (soon) | Brand colors and fonts or AI suggestion | Marketing-site scope; no product components, a11y target, modes or governance | [S-L11-065] |
| 9 | **Material Theme Builder** | Color/theme generator | M3 color scheme (tonal roles), custom colors, fonts; export to Figma, Compose, Views, Flutter, Web CSS, DSP | Source color or image, core colors, extended colors, fonts, contrast level | Material-only; the GitHub repo was archived 23 Jul 2026 (future unclear) | [S-L11-067] |
| 10 | **Radix Themes playground** | Theme configurator | Theme config for Radix Themes components | Accent, gray, appearance, radius (none..full), scaling (90-110%), panel background | Tied to Radix Themes; five axes only; no brand or principles input | [S-L11-068, S-L11-069] |
| 11 | **shadcn create / themes** | Project and theme generator | A rewritten shadcn project (Dec 2025) | Component library (Radix or Base UI), style (Vega/Nova/Maia/Lyra/Mira), base color, theme, icon library, fonts, radius, menu style | React/Tailwind only; no explanation of choices; no docs or governance | [S-L11-071] |
| 12 | **tweakcn** | shadcn theme editor (OSS) | CSS variables for shadcn/Tailwind v3/v4 (OKLCH/HSL); registry install | Colors, typography, radius, shadows; AI from text or image; presets | shadcn-only; visual tuning without rationale or a11y program | [S-L11-073] |
| 13 | **Realtime Colors** | Color + type previewer | Palette plus fonts previewed on a real site layout; exports CSS, Tailwind, SCSS, OKLCH etc.; contrast checker | 5 colors (text, background, primary, secondary, accent), heading/body fonts, type scale | No components, modes beyond light/dark, or system output | [S-L11-074] |
| 14 | **Eva Design colors** | Semantic palette generator (legacy) | Semantic palette (success, info, warning, danger) in 9 shades; JSON/Sketch | One brand color | Legacy; color only | [S-L11-075] (low-confidence fetch) |
| 15 | **Adobe Leonardo** | Accessible color (OSS) | Contrast-ratio-based ramps, adaptive light/dark themes, DTCG tokens, CSS/JSON | Key colors, background, target contrast ratios, WCAG2 or APCA | Color only; expert-oriented | [S-L11-082] |
| 16 | **Untitled UI** | Ready-made kit | Figma kit (10,000+ components/variants, 900+ styles/variables) and React library (React Aria, Tailwind v4.3) | None; you buy and customize ($129 Figma, $349 React single-user) | A finished system to adopt, not a builder; customization is manual | [S-L11-078] |
| 17 | **Google Stitch** | AI UI design | UI designs, prototypes, code; extracts a design system from a URL; DESIGN.md import and export; MCP + SDK | Prompt, images, URL, voice | Generates screens; the system is a by-product; no governance or versioning | [S-L11-077, S-L11-046] |
| 18 | **Claude Design** (Anthropic Labs) | AI visual creation | Builds a team design system by reading codebase and design files; prototypes, decks; handoff to Claude Code | Codebase, design files, prompts | Extracts rather than guides; research preview at launch (Apr 2026), beta since Sep 2026 [S-V1a-003]; limited explicit decision rationale | [S-L11-055, S-L11-056] |
| 19 | **Magic Patterns** | AI prototyping + DS agent | Design System Agent builds and iterates a DS from tokens, components and brand, mapped to code | GitHub repo, npm package, or URL (per product page snippet) | Needs existing sources; prototyping-focused | [S-L11-080] |
| 20 | **v0 Design Systems 2.0** | AI app builder | A starter app plus a saved "skill" that grounds generations in your system | GitHub repo, Figma frames, Storybook/doc links, archives, private npm | Consumes an existing system; does not create one | [S-L11-052, S-L11-054] |
| 21 | **Lovable design systems** | AI app builder | DS project with `design-system.json`, rendered docs, `system.md`; connected projects receive components and rules; adherence scanning | A Lovable project marked as DS (or npm wrapper on Enterprise) | Lovable-only; one DS per project; guidance is whatever you author | [S-L11-053] |
| 22 | **Bolt Design System Agents** | AI app builder | Apps built with your real components and tokens | Codebase components, npm packages, Storybook, specs, logos, fonts, brand guidelines | Consumes an existing system | [S-L11-103] |
| 23 | **Token Designer (now Bezel)** | AI token generator | Branded token system (color, type, spacing, radius), live component preview, AA/AAA checks, MCP to coding tools | Brand colors, fonts, radius, design preferences | Closest to Kunal's idea at the token layer; unclear depth on components, governance, multi-platform | [S-L11-081] |
| 24 | **Storybook** (docs + MCP) | Component workshop | Stories, docs, component manifest; MCP tools for agents | Your component code | Documents and tests code that already exists | [S-L11-044] |

**Pattern across competitors [inferred from the table]:** (1) *Theme generators* take 3-10 visual inputs and emit tokens for one stack. (2) *Platforms* host, document and deliver an existing system. (3) *AI builders* extract a system from an existing codebase or URL and use it to generate apps. The open space for Kunal's builder: a guided, explainable decision flow that starts before any system exists (principles, audience, platforms, accessibility target, theming dimensions, governance) and emits every consumer format at once (Figma variables, DTCG, CSS/Tailwind, DESIGN.md, registry, MCP-ready docs, lint rules, ADRs).

---

## Part H. Consolidated kickoff questionnaire

Each question lists why it matters and what it changes downstream. "Src" gives the source that asks this question, or [inferred] when the question is my synthesis. Phases follow Part A.

### H0. Sell and frame (before anything is built)
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 0.1 | Why do you want a design system? What problem hurts most today (inconsistency, speed, accessibility, rebrand, AI output drift)? | The problem sets the success metric and the first scope | Metrics (DC-20), pilot choice (DC-07), priorities | [S-L11-083] |
| 0.2 | What goals should the system accomplish in 12 months? | Gives the roadmap a finish line | Roadmap, maturity target (DC-21) | [S-L11-083, S-L11-084] |
| 0.3 | What happens if this fails? What would sink it? | Surfaces risks early (no mandate, no staff) | Governance and sponsorship plan | [S-L11-083, S-L11-084] |
| 0.4 | Who must be convinced, and who is doing the convincing? | Mandate is the top adoption lever: lack of mandate is the #1 barrier (73%) | Rollout (DC-08), comms (DC-22) | [S-L11-083, S-L11-030] |
| 0.5 | Build, adapt, or adopt? How distinct must the product look? | Sets the cost and how much the builder generates vs customizes | Starting point (DC-01) | [S-L11-006] |

### H1. Discovery and audience
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 1.1 | Who are the users of the system: designers, engineers, PMs, content, marketing, external partners, AI agents? | Each audience needs different docs and formats | Docs template (DC-18), agent exports (DC-23) | [S-L11-083, S-L11-088] |
| 1.2 | Who will be interviewed, and what themes came out (workflow pains, hopes, fears)? | Grounds the system in real needs | Principles, priorities | [S-L11-084, S-L11-105] |
| 1.3 | What does success look like in one year, from each stakeholder's view? | Defines "done" for the first version | Metrics (DC-20) | [S-L11-084] |
| 1.4 | Who attends the kickoff workshop, and who turns its outcomes into a plan? | Accountability | Team roles (DC-10) | [S-L11-083] |
| 1.5 | Which existing products and UI will you audit? Is this greenfield? | Greenfield skips the audit | Audit method (DC-04) | [S-L11-105] |
| 1.6 | What did the interface inventory find: counts of colors, type styles, button variants, duplicated patterns? | Quantifies consolidation and fuels buy-in | Ramps, scales, component list | [S-L11-001, S-L11-105] |

### H2. Scope: products, platforms, technology
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 2.1 | Which products will the system serve, and which will it explicitly not serve? | Prevents scope creep | Scope (DC-02) | [S-L11-083] |
| 2.2 | Which platforms: web app, marketing site, iOS, Android, desktop, email, embedded? | Each adds conventions, components and exporters | Platform packages (L10), exporters | [S-L11-083, S-L11-030] |
| 2.3 | Which frameworks and styling approach (React, Web Components, Angular, Vue, SwiftUI, Compose, Tailwind, CSS-in-JS)? | Determines component code output and token transforms | Code generation, token format (L07) | [S-L11-083, S-L11-030] |
| 2.4 | Which design tools are in use (Figma, Penpot, other)? Which plan (analytics and branching need Org/Enterprise)? | Tool capabilities bound the workflow | Library setup, analytics (DC-20) | [S-L11-083, S-L11-035, S-L11-010] |
| 2.5 | Where will the source of truth live: design tool, code, or a token platform? | Avoids design-code drift | Sync pipeline (DC-16) | [S-L11-030, COMMUNITY-SIGNAL] |
| 2.6 | Is there an existing component library or UI kit to build on (Radix, Base UI, MUI, shadcn, Material)? | Adapting is cheaper than creating | Starting point (DC-01) | [S-L11-006, S-L11-071] |
| 2.7 | Which pilot products will prove the system (score on the 8 criteria)? | Real content prevents abstract, unused components | Pilot (DC-07), first components | [S-L11-105] |
| 2.8 | Big-bang redesign or incremental rollout? | Changes planning, comms and versioning | Rollout (DC-08) | [S-L11-105] |

### H3. Brand and principles
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 3.1 | Where are brand identity guidelines managed, and what is the relationship between brand and UI components? | Brand constrains palette, type and imagery | Color (L01), type (L02), imagery (L05), brand lane (L06) | [S-L11-083] |
| 3.2 | What are your 3-5 principles, each with a do/don't example? | Tie-breakers for every later decision | Presets for density, radius, color strategy, motion | [S-L11-008, S-L11-083] |
| 3.3 | What should the product feel like? Which reference products do stakeholders agree on (20-second gut test)? | Aligns taste before building | Visual direction and personality mapping (L06) | [S-L11-001] |
| 3.4 | What are the brand colors? What are the neutral and utility (status) palettes? | Seeds color ramps | Color roles (L01) | [S-L11-083] |
| 3.5 | What typography system and typefaces (brand vs system fonts, licensing)? | Seeds the type scale | Typography (L02) | [S-L11-083] |
| 3.6 | Is there a voice and tone guide and a content strategy? | Consistent microcopy across components | Content guidelines, component copy | [S-L11-083] |

### H4. Accessibility and inclusion
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 4.1 | What conformance target (default WCAG 2.2 AA)? Any legal requirement (public sector, regional accessibility law)? | Bounds color, size and interaction choices everywhere | Contrast minimums, target sizes, focus styles | [S-L11-093] |
| 4.2 | What will the system guarantee vs what product teams must do? | Prevents a false sense of compliance | Published responsibility split | [S-L11-092, S-L11-094] |
| 4.3 | Which assistive technologies and browsers are in the test matrix? | Automated tools find only about 30% of issues | Test plan, Ready gate (DC-13) | [S-L11-093, S-L11-091] |
| 4.4 | Do you need higher-contrast themes, reduced motion, text scaling support? | Extra modes and tokens | Theming dimensions (DC-25), motion (L04) | [S-L11-067; inferred] |
| 4.5 | Who owns accessibility on the team (44% of teams lack a specialist)? | Ownership decides whether it happens | Roles (DC-10) | [S-L11-030] |

### H5. Internationalization and content
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 5.1 | Which languages and scripts? Any right-to-left (Arabic, Hebrew)? | RTL mirrors layouts and icons; some scripts need different fonts and line heights | Logical spacing tokens, mirrored icons, font stacks (L02, L05) | [S-L11-090 (Carbon RTL section); inferred] |
| 5.2 | How much text expansion must components tolerate (German, Finnish)? | Truncation and overflow rules | Component content guidance ("overflow content") | [S-L11-090] |
| 5.3 | Locale-specific formats (dates, numbers, currency, names, addresses)? | Pattern and input component design | Form patterns (L08) | [inferred] |
| 5.4 | Who writes component content guidance (labels, errors, empty states)? | 22% of teams lack a content designer | Content lint, docs | [S-L11-030] |
| 5.5 | Are there regulated content requirements (legal copy, disclosures)? | Adds fixed patterns | Pattern library | [inferred] |

### H6. Theming
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 6.1 | Light and dark (76% of systems)? System-following or user-chosen? | Doubles color decisions and contrast checks | Mode structure (L07), color (L01) | [S-L11-030] |
| 6.2 | Multiple brands or white-label clients (63%)? | Needs a brand tier and aliasing | Token tiers, library architecture | [S-L11-030, COMMUNITY-SIGNAL] |
| 6.3 | Density or size modes (compact, comfortable)? Breakpoint modes (38%)? | Adds spacing and size scales | Space and layout (L03) | [S-L11-030, S-L11-071] |
| 6.4 | Per-platform value differences (24%)? | Platform-specific type and size tokens | Platform lane (L10) | [S-L11-030] |
| 6.5 | Will product teams be allowed to theme or override? | Posture decision | Lint strictness, component APIs | [S-L11-019] |

### H7. Foundations (pointers into lanes L01-L05)
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 7.1 | Color: ramp method, semantic roles, status colors, data-viz palette? | Core of perceived brand | L01 | [S-L11-083] |
| 7.2 | Typography: scale ratio, sizes, weights, line heights, fluid or fixed? | Hierarchy and density | L02 | [S-L11-083] |
| 7.3 | Space, grid, breakpoints, touch targets? | Rhythm and responsiveness | L03 | [S-L11-008] |
| 7.4 | Shape, elevation, motion personality? Motion is now a Figma "material" (Config 2026) | Tactile feel | L04 | [S-L11-083, S-L11-057] |
| 7.5 | Icons: source, style, delivery, update process? Imagery and illustration? | Visual language consistency | L05 | [S-L11-083] |
| 7.6 | Naming convention for tokens and components (for example Category/Use/Variation)? | Shared vocabulary for humans and agents | Token names (L07) | [S-L11-008, S-L11-001] |

### H8. Components and patterns
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 8.1 | Which UI components are in version 1 (from the audit and pilot)? | Completeness is the #1 adoption factor (79%) | Component backlog (L08) | [S-L11-083, S-L11-030] |
| 8.2 | Do you use a methodology to organize components (atomic, other)? | Taxonomy and file structure | Library structure | [S-L11-083, S-L11-107] |
| 8.3 | Which page templates and workflows belong in the system? | Patterns beyond components | Pattern library | [S-L11-083] |
| 8.4 | What is the snowflake policy (what stays product-owned)? | Controls drift vs flexibility | Governance (DC-12), posture (DC-03) | [S-L11-003, S-L11-014] |
| 8.5 | What makes a component "Ready" (tests, docs, a11y, design-code parity)? | Quality bar | Lifecycle (DC-13) | [S-L11-025, S-L11-003] |

### H9. Team, governance, contribution
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 9.1 | Who are the makers, primary users and secondary users? Which teams won't use it? | Defines the customer | Team model, comms | [S-L11-083] |
| 9.2 | Team model: solitary, centralized, federated, hybrid? | Changes throughput and buy-in | DC-09 | [S-L11-005, S-L11-013] |
| 9.3 | Who is the primary owner? Who allocates time, budget and resources? | 61% of teams are understaffed | DC-10, roadmap | [S-L11-083, S-L11-030] |
| 9.4 | Who can contribute, and what (fixes, enhancements, new components)? | Only 36% are satisfied with their contribution process | DC-11 | [S-L11-083, S-L11-030] |
| 9.5 | What are the acceptance criteria for new additions (useful, unique, usable, consistent, versatile)? | Keeps the system lean | DC-11 | [S-L11-021] |
| 9.6 | How are decisions recorded (RFCs, ADRs)? | Explains "why things are the way they are" | DC-12 | [S-L11-095] |
| 9.7 | What rituals: critique, office hours, flow and system weeks? | Keeps the loop running | DC-12, DC-22 | [S-L11-024, S-L11-014] |

### H10. Versioning, release, deprecation
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 10.1 | How do components get into applications (packages, registry, copy-in)? | Distribution model | Exporters, registry (DC-23) | [S-L11-083, S-L11-045] |
| 10.2 | How is versioning handled (library-level vs per-component semver)? | Upgrade predictability | DC-14 | [S-L11-083, S-L11-028, S-L11-106] |
| 10.3 | How are dependencies managed, and who runs deployment? | Release reliability | Release process | [S-L11-083] |
| 10.4 | What is the deprecation policy (notice period, markers, codemods, migration guides)? | Protects consumers | DC-15 | [S-L11-100] |
| 10.5 | How do design libraries and code versions stay aligned? | 60% have no token automation | DC-16 | [S-L11-030] |

### H11. Documentation and distribution (including AI)
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 11.1 | What is the system's name, where do docs live, and are they public? | Discoverability and accountability | Docs platform (DC-17) | [S-L11-083, S-L11-002] |
| 11.2 | Which docs tool (Figma, Storybook, zeroheight, Supernova, custom)? | Authoring friction | DC-17 | [S-L11-030, S-L11-088] |
| 11.3 | What goes on each component page? | Consistency of guidance | DC-18 template | [S-L11-090, S-L11-089] |
| 11.4 | Which AI tools will teams use to generate UI (Figma Make, v0, Lovable, Bolt, Claude, Cursor, Stitch)? | Decides export formats | DC-23 | [S-L11-031, S-L11-052, S-L11-053, S-L11-103] |
| 11.5 | Which agent channels to ship (MCP, DESIGN.md, llms.txt, rules files, registry, Make kit)? | 59% report UI bypassing the DS | DC-23 | [S-L11-031, S-L11-047, S-L11-048, S-L11-051] |
| 11.6 | How will you check that agents follow the system (lint, adherence scans, evals)? | Docs alone don't steer agents | DC-24 | [S-L11-108, S-L11-053] |

### H12. Measurement
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 12.1 | What counts as "adopted" in design (for example DS layers / all layers on handoff pages)? | Makes adoption measurable | Metrics (DC-20) | [S-L11-038] |
| 12.2 | What counts as adopted in code (imports from the DS package vs local components)? | Code is the shipped truth | Scanner setup | [S-L11-037, S-L11-039] |
| 12.3 | Which quality signals: detach rates, a11y defects, bug volume, consistency? | Finds broken components | Roadmap | [S-L11-036, S-L11-030] |
| 12.4 | How and how often will you survey satisfaction? What value story does leadership need (speed, ROI)? | Buy-in satisfaction fell to 32% | Reporting | [S-L11-030, S-L11-099] |

### H13. Timeline and resourcing
| # | Question | Why it matters | What it changes downstream | Src |
|---|---|---|---|---|
| 13.1 | What is the timeline for version 1 and the pilot window (for example 3-4 weeks per pilot)? | Scopes version 1 | Pilot (DC-07) | [S-L11-105] |
| 13.2 | How many people, at what allocation? | 28% of teams have 1-2 people | Automation needs, scope | [S-L11-030] |
| 13.3 | How will the system be announced? | Launch moment or incremental occasions | Comms (DC-22) | [S-L11-083, S-L11-105] |
| 13.4 | How are system changes communicated to consumers after launch? | Only 39% are satisfied with change comms | Release notes, changelog | [S-L11-083, S-L11-030] |

---

## Reconciliation with `sources/COMMUNITY-SIGNAL.md` (L00)

- **zeroheight 2026 numbers:** L00 flagged that the AI numbers came only from a LinkedIn post and blog summary and asked lanes to re-check them on report.zeroheight.com. I did: report.zeroheight.com rendered via fetch and confirms 56% using AI (10% built in, 46% experimenting), n=147, fifth annual edition [S-L11-030]. One blog-snippet claim I could **not** match to the report page: "16% of design systems are maintained by a single person" and "only 23% agree they have adequate resources" [S-L11-029 snippet]. The report page shows team size 1-2 people = 28% and 61% understaffed. I did not use the 16% and 23% figures.
- **"Only 15% say AI lives up to the hype":** this appears in the blog snippet [S-L11-029] but not on the report page I read. The closest verified numbers are impact rated "highly" or "very highly" by 28% (22% + 6%) [S-L11-030] and 67% calling AI overhyped in the separate State of AI report [S-L11-031]. Treat the 15% as unverified.
- **Code as source of truth (community majority):** consistent with zeroheight's automation data (only 6% code-to-design, 5% bi-directional) [S-L11-030]. Reflected in DC-L11-16.
- **Pushback on "agentic design system":** included as a counterweight in E1 and DC-L11-23.
- **Sanity evals:** I fetched it independently [S-L11-108]; the numbers match L00's [S-L00-036].
- **Storybook MCP versions:** L00 says 10.3 introduced MCP for React and 10.6.0 is current. The docs page I read shows v10.6 [S-L11-044]. Consistent.
- **Disputed sources:** L00 flags Jakob Nielsen's personal commentary as disputed. I used only an NN/g article by Therese Fessenden and one by Kate Kaplan [S-L11-006, S-L11-097]; no Nielsen opinion is used.

---

## Open questions / gaps

1. **Nathan Curtis primary texts on contribution and roles were unreachable.** Medium returned Cloudflare 403 and eightshapes.com did not resolve. Contribution sizing is taken from a search snippet [S-L11-020]. Team models came through the Center Centre republication [S-L11-005].
2. **Dan Mall's book was not read directly.** Pilot and process claims come from Tier C book notes [S-L11-014], the publisher's chapter list [S-L11-015], and the pilot scorecard reproduced in the InVision handbook [S-L11-105].
3. **Carbon's contribution overview and PDLC pages** returned 404 or truncated content; Carbon's phases come from search snippets [S-L11-023].
4. **The zeroheight State of AI 2026 full report** is client-rendered. Only the landing-page summary was verified [S-L11-031]; the MCP (48%) and bypass (59%) numbers rest on that summary.
5. **Several competitor pages were client-rendered** (shadcn themes and create, Stitch app, Material Theme Builder web app, tweakcn site). I used changelogs, blogs or GitHub READMEs instead. The Eva Design summary is low-confidence [S-L11-075].
6. **Material Theme Builder's GitHub repo was archived on 23 Jul 2026** [S-L11-067]. Whether the tool moved elsewhere (for example into m3.material.io or a Figma plugin) was not verified.
7. **The legal accessibility landscape** (EU European Accessibility Act, ADA, Section 508 dates and scope) was not researched; it affects question 4.1.
8. **Pricing** for Supernova, zeroheight, Knapsack, Tokens Studio, v0, Lovable, Bolt and Claude Design was not captured.
9. **WebSearch budget ran out** late in the session (200 calls shared across agents), and Perplexity had no quota. Final checks relied on WebFetch of known URLs.
10. **No hands-on testing** of any competitor. All competitor descriptions come from official pages.

## Confidence

- **Confirmed (Tier A or B, read live today):** the interface inventory method and categories; the governance flow; the design-system questionnaire; team model definitions; GOV.UK contribution criteria and accessibility strategy (WCAG 2.2 AA, about 30% automated detection); Carbon's component page structure and a11y test status; Primer's lifecycle; Polaris deprecation rules; SemVer rules; all zeroheight 2026 report numbers quoted from report.zeroheight.com; Figma library analytics facts; the Pinterest adoption metric; the Figma MCP tool list; Storybook MCP; shadcn MCP and shadcn create; DESIGN.md spec and date; Cloudscape llms.txt; Make kit structure; v0, Lovable and Bolt DS features; Claude Design launch and DS onboarding; Stitch March 2026 features; Sanity eval numbers; competitor inputs and outputs as listed.
- **Partly confirmed:** Dan Mall's process claims (Tier C notes plus handbook excerpt); Kholmatova's parameters (the Smashing page confirms chapter 6 exists; the definitions come from a Tier C summary); Nathan Curtis's contribution sizing (snippet); the State of AI 2026 numbers (landing-page summary only); Eva Design (thin fetch).
- **Inferred (marked [inferred] in the text):** all "Default + heuristic" syntheses that combine sources; the builder encodings (`governance.*`, `component.status`, etc.); visual effects of process decisions; the competitor gap analysis and the "open space" statement.

---

## Cross-lane notes

- [L11 -> L07] Builder exports should include DTCG JSON (canonical), DESIGN.md (front matter can export to DTCG and Tailwind via its CLI), a shadcn-compatible registry (`registry.json` + `r/{name}.json`), and an llms.txt index. Please confirm DTCG `$deprecated` support and Figma's native DTCG import/export status (DC-L11-15, DC-L11-23). [S-L11-047, S-L11-045, S-L11-048]
- [L11 -> L07] zeroheight 2026: 60% of teams have no token automation; token layers are primitives 90%, semantic 85%, component 52%; theming by mode 76%, brand 63%, breakpoint 38%, platform 24%. Useful defaults for token-tier and mode decisions. [S-L11-030]
- [L11 -> L01] Accessible color generators to benchmark: Adobe Leonardo (contrast-ratio targets, WCAG2 or APCA, DTCG output) and Material Theme Builder (contrast levels; repo archived 23 Jul 2026). DESIGN.md lint checks WCAG contrast. [S-L11-082, S-L11-067, S-L11-047]
- [L11 -> L03/L04] Density and shape "styles" in shadcn create (Vega classic, Nova compact, Maia soft and rounded, Lyra boxy and sharp, Mira dense) and Radix scaling of 90-110% are real-world preset axes worth mirroring. [S-L11-071, S-L11-068]
- [L11 -> L04] Figma Config 2026 made motion a first-class DS material (timing and easing variables, animated components; open beta 24 Jun 2026). [S-L11-057]
- [L11 -> L08] Component doc page template (Carbon: Usage, Style, Code, Accessibility; GOV.UK: when to use, how it works, research, recent changes) plus a lifecycle field (experimental, ready, deprecated) should be attributes of every component in the ontology. [S-L11-090, S-L11-089, S-L11-025]
- [L11 -> L10] Agent tooling is web and React-centric (v0, Lovable, Bolt, shadcn, Storybook manifest). Native (SwiftUI, Compose) agent context is an open gap and a differentiation opportunity. [S-L11-044, S-L11-052, S-L11-053, S-L11-103]
- [L11 -> S1] The questionnaire in Part H (77 questions in 14 phase groups) is ready to seed the builder's onboarding flow. The 25 Decision Cards can map one-to-one to ADRs the builder emits. [inferred]
