# L17: How design systems get made today (manual and AI), which blocks need a designer, and the process the builder should run

Lane: L17. Author: orchestrator subagent L17, with four helper subagents (H1 NN/g, H2 AI workflows and extractors, H3 designsystems.surf and manual workflows, H4 designer-hook formats and fallbacks). Written 2026-09-23.
Trace: `traces/L17-trace.md`. Helper rows are re-logged there with their reserved id ranges.
Status: see `## Open questions / gaps` and `## Confidence` at the end.

Related lanes this file links to rather than repeats: L11 (lifecycle, 24 competitors, 77-question kickoff questionnaire), L16 (43 tools, interaction models, round trip), L06 (brand inputs, lever matrix), L05 (icons, imagery, data viz), L07 (tokens, Figma), and the S1 synthesis files (`synthesis/ONTOLOGY.md`, `synthesis/LEVERS.md`).

## Lane overview

PLACEHOLDER_OVERVIEW

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
