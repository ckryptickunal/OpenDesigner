# OpenDesigner: public problem and user-feedback corpus

**Researched:** 2026-09-25. **Scope:** Public feedback on AI-assisted UI/design generation, especially distinctive visual direction, design-system consistency, source references, and human control. This is *market/problem evidence*, not feedback from OpenDesigner users. [OpenDesigner](https://github.com/ckryptickunal/OpenDesigner) is the project anchor. Entries are dated by the original post/issue, not discovery date. Links point to the original discussion or issue. Quotes are short verbatim excerpts unless labeled paraphrase. An author's complaint is evidence of that experience, not a measured prevalence claim. Some posts are themselves promotional or advice-seeking; this is flagged when relevant.

## Quick read

- **Generic defaults are the loudest complaint.** Builders identify repeated rounded cards, gradients, stock fonts, Tailwind/shadcn defaults and interchangeable landing-page sections. This supports showing alternatives and recording the human's visual choices, rather than assuming one house style.
- **A screenshot or adjective is not enough.** Several builders say the tools lose layout, copy, colours or the subtler character of a reference. Preserve reference-to-decision links and have the user review interpretations before generating assets.
- **Consistency fails across pages and iterations.** Button typography, spacing and colour drift; a local change can propagate unexpectedly. Separate approved project rules from exploratory variants, and make changes auditable.
- **The gap is not just first-pass aesthetics.** Navigation, breakpoints, loading states and accessibility require testing and human review. A status board should show what has actually been checked, not mark generated UI as finished.
- **There is a counterpoint.** Some people regard a generic component language as useful for speed; distinctiveness should be a user choice, not imposed. See OD-03.

## Source records

Schema for agents: each `OD-NN` block has `theme`, `date`, `audience`, `type`, `evidence`, `source`, and `OpenDesigner relevance`. A post can appear in only one block even if it informs multiple themes. `type` is `firsthand`, `discussion`, or `feature-request`. Relevance is a design hypothesis, not a claim that OpenDesigner already solves it.

### Generic visual defaults and distinctiveness

#### OD-01
- theme: Generic defaults
- date: 2025-08-26
- audience: Indie builders using Bolt / vibe coding
- type: firsthand
- evidence: "One thing I find really frustrating about AI app builders like Bolt is how generic their UIs tend to look ... you can spot an AI-generated landing page or UI from a mile away."
- source: [r/vibecoding, "UI made by vibecoding is so generic"](https://www.reddit.com/r/vibecoding/comments/1n0fh3n/ui_made_by_vibecoding_is_so_generic/)
- OpenDesigner relevance: Ask for examples and preferred distinctions before defaulting to a standard landing-page arrangement.

#### OD-02
- theme: Generic defaults
- date: 2025-03-31
- audience: Lovable user making a landing page
- type: firsthand
- evidence: "no matter what I do, the results always end up looking like the typical, cookie-cutter Tailwind CSS designs"; style adjectives changed only minor details.
- source: [r/lovable, "How do you get Lovable to design a unique UI"](https://www.reddit.com/r/lovable/comments/1jntlvm/how_do_you_get_lovable_to_design_a_unique_ui/)
- OpenDesigner relevance: A taste interview needs specific visual references and explicit choices, not only adjectives.

#### OD-03
- theme: Generic defaults / counterpoint
- date: 2025-08-05
- audience: Frontend developers
- type: discussion
- evidence: A commenter calls Radix/shadcn plus Tailwind the generic "AI style," but adds that a shared UI language "is an okay thing for the world" in some cases. Another names generic shadcn/Tailwind layouts.
- source: [r/Frontend, "What defines the AI-generated style in frontend?"](https://www.reddit.com/r/Frontend/comments/1mihgav/what_defines_the_aigenerated_style_in_frontend/)
- OpenDesigner relevance: Let the user choose familiar patterns intentionally; don't equate conventional with broken.

#### OD-04
- theme: Generic defaults
- date: 2025-08-31
- audience: Lovable user
- type: firsthand
- evidence: "Every time I build something in lovable the site has exactly the same design ... now all vibe coded apps look the same." The author also worries that changing it may disrupt the project.
- source: [r/lovable, "Generic AI Slop design"](https://www.reddit.com/r/lovable/comments/1n4olsd/generic_ai_slop_design/)
- OpenDesigner relevance: Differentiate a visual-direction decision from a risky codebase rewrite; show a preview and scope of changes.

#### OD-05
- theme: Generic defaults / colour
- date: 2025-06-26
- audience: Claude UI users
- type: discussion
- evidence: The poster asks why Claude 3.7+ makes "every UI and UX design purple"; one commenter says they saw the same issue.
- source: [r/ClaudeAI, purple UI question](https://www.reddit.com/r/ClaudeAI/comments/1lkxwmk/why_does_claude_37_seem_to_have_such_a_thing_for/)
- OpenDesigner relevance: Make colour direction an explicit approved system, not a model default. This thread is small, not a prevalence estimate.

#### OD-06
- theme: Generic defaults
- date: 2025-11-29
- audience: Claude Code frontend users
- type: discussion
- evidence: A user experimenting with Claude skills reports "when you ask claude to generate UI, it defaults to the same patterns every time." The post suggests a skill-based fix and is partly solution advocacy.
- source: [r/ClaudeAI, generic UI patterns](https://www.reddit.com/r/ClaudeAI/comments/1p9srou/finally_figured_out_why_claudes_ui_generations/)
- OpenDesigner relevance: Compare human-selected patterns against the model's default patterns; do not treat the author's proposed fix as independently validated.

#### OD-07
- theme: Generic defaults / section structure
- date: 2026-03-21
- audience: Indie travel-site builder using Lovable / Framer
- type: firsthand
- evidence: For a "How it works" section, the tools keep returning "3–4 boxes" with "icon + title + short text," which the builder calls "boring and forgettable."
- source: [r/vibecoding, non-generic UI sections](https://www.reddit.com/r/vibecoding/comments/1rzoter/how_do_you_prompt_ai_to_generate_nongeneric_ui/)
- OpenDesigner relevance: Explore component and storytelling forms before selecting the default card-grid pattern.

#### OD-08
- theme: Generic defaults
- date: 2026-02-16
- audience: Builder of a resume-to-personal-site generator
- type: firsthand
- evidence: "every page the AI creates looks flat, text-heavy, and very generic" despite trying prompts, design tokens, seed variation, and template components.
- source: [r/vibecoding, generic website generator](https://www.reddit.com/r/vibecoding/comments/1r5zx6j/aigenerated_websites_always_look_generic_how_do/)
- OpenDesigner relevance: Tokens alone may not establish visual hierarchy or personality; test output against example pages.

#### OD-09
- theme: Generic defaults
- date: 2025-11-24
- audience: Indie SaaS builders
- type: discussion
- evidence: Poster describes the recurring "rounded buttons, same spacing, same shadows, same purple/blue vibe." This is an open-ended discussion prompt, not a controlled study.
- source: [r/lovable, same-template SaaS UI](https://www.reddit.com/r/lovable/comments/1p5fz8d/why_does_every_ai_saas_ui_look_like_the_same/)
- OpenDesigner relevance: Record the choices behind a spacing, colour, and component system so they do not collapse into defaults.

#### OD-10
- theme: Generic defaults / visual hierarchy
- date: Date not independently verified; HN page displayed "6 months ago" at retrieval
- audience: Founder using Cursor, Claude, Figma
- type: discussion
- evidence: The commenter complains that gradients, rounded cards, shadows, and presets compete, with "No taste. No hierarchy." The same commenter promotes a tool they built, so treat as interested testimony.
- source: [Hacker News, AI beige slop discussion](https://news.ycombinator.com/item?id=46956964)
- OpenDesigner relevance: Critique hierarchy with the user and identify the one primary purpose of each screen before generating it.

### Reference fidelity and human taste

#### OD-11
- theme: Reference fidelity
- date: 2025-04-25
- audience: Frontend builder using Lovable, Cursor, Bolt
- type: firsthand
- evidence: With a UI image attached, the AI "either misinterprets the layout or totally ignores the subtle design vibes" the builder referenced.
- source: [r/Frontend, image-to-UI intent](https://www.reddit.com/r/Frontend/comments/1k7mh0z/anyone_else_feel_like_aiassisted_ui_tools_still/)
- OpenDesigner relevance: Ask what in a reference matters, preserve that mapping, and review the interpretation before implementation.

#### OD-12
- theme: Reference fidelity
- date: 2025-09-16
- audience: Frontend developer testing Figma MCP, v0 and Figma-to-code plugins
- type: firsthand
- evidence: The author says basic screens were not reproduced; "Colors manage to be wrong, they can’t even implement the copy correctly."
- source: [r/Frontend, Figma-to-code frustration](https://www.reddit.com/r/Frontend/comments/1nickcg/have_you_tried_any_figmatocode_tools_and_got/)
- OpenDesigner relevance: Compare generated assets to source text, colour and layout; include explicit review checks.

#### OD-13
- theme: Reference fidelity / visual hierarchy
- date: 2025-04-25
- audience: Frontend developer in the OD-11 discussion
- type: firsthand comment
- evidence: Asked for Swiss style with specified elements; the commenter says tools returned wrong elements and "terrible UX and hierarchy," like generic WordPress templates.
- source: [r/Frontend, image-to-UI intent and comments](https://www.reddit.com/r/Frontend/comments/1k7mh0z/anyone_else_feel_like_aiassisted_ui_tools_still/)
- OpenDesigner relevance: Test whether stated visual language and hierarchy actually survive generation, rather than checking only build success.

#### OD-14
- theme: Reference fidelity / consistency
- date: 2024-10-12
- audience: Designer requesting Bolt feature
- type: feature-request
- evidence: "Bolt currently relies on existing design libraries or makes its own design choices"; uploaded reference images can be misread, and manually adjusting generated design is time-consuming. The request asks to integrate a custom guide covering type, colours, buttons and layout.
- source: [stackblitz/bolt.new issue #494, Custom Style Guide Integration](https://github.com/stackblitz/bolt.new/issues/494)
- OpenDesigner relevance: A persistent, human-approved style guide and trace from reference to rule are a directly articulated need; this is a request, not proof of Bolt's current behavior.

#### OD-15
- theme: Reference fidelity / integration
- date: 2025-09-19
- audience: Lovable user
- type: firsthand
- evidence: The user reports generic templates, clashing colours and sections that do not fit; even screenshot cloning returns a "weird knockoff version."
- source: [r/lovable, UI prompting difficulty](https://www.reddit.com/r/lovable/comments/1nl4xfb/is_there_an_idiotfriendly_way_to_prompt_loveable/)
- OpenDesigner relevance: Keep a coherent page direction and ask for human judgment on colour/section fit before treating assets as complete.

### Design-system continuity and safe iteration

#### OD-16
- theme: Cross-page consistency
- date: 2025-06-11
- audience: Lovable user building a multi-page site
- type: firsthand
- evidence: A new page's CTA had the wrong font weight; "Once I’ve established how a button or card should look, I want that to just stick across the whole site unless I say otherwise."
- source: [r/lovable, keeping things consistent](https://www.reddit.com/r/lovable/comments/1l8uhrh/anyone_have_tips_for_keeping_things_consistent_in/)
- OpenDesigner relevance: Store approved component rules once, apply them across pages, and flag drift.

#### OD-17
- theme: Iteration safety
- date: 2025-03-31
- audience: Lovable user
- type: firsthand
- evidence: A navigation styling update caused unintended changes elsewhere; the author describes "a lot of circular prompting" and asks for a whole-UI review.
- source: [r/lovable, UI inconsistencies after adjustment](https://www.reddit.com/r/lovable/comments/1jo2gx7/prompt_to_fix_ui_inconsistencies_on_lovable/)
- OpenDesigner relevance: Show what changed and which project rules/assets each change affects; support scoped review before propagating.

#### OD-18
- theme: Cross-page consistency
- date: 2026-03-09
- audience: Frontend developers evaluating generated UI
- type: discussion
- evidence: A poster asks if generated layouts remain consistent in a multi-page app across spacing, typography hierarchy, component reuse, colour and interaction patterns; "the consistency starts to break."
- source: [r/Frontend, design consistency question](https://www.reddit.com/r/Frontend/comments/1rouppw/do_aigenerated_uis_actually_maintain_design/)
- OpenDesigner relevance: Track these systems explicitly at product level, not as unrelated page outputs. This is an observation and question, not a benchmark.

#### OD-19
- theme: Agent-readable design rules
- date: 2026-04-15
- audience: React/Tailwind/shadcn developer with an existing custom system
- type: firsthand need
- evidence: The user wants an agent-readable `design-system.md` and text wireframes so an agent can implement their existing components and layouts without Figma files.
- source: [r/Frontend, structuring design-system.md](https://www.reddit.com/r/Frontend/comments/1slxwjt/need_advice_how_to_structure_a_designsystemmd/)
- OpenDesigner relevance: Human-readable and machine-readable system outputs are complementary, but must distinguish existing rules from suggestions.

#### OD-20
- theme: Structural design rules
- date: Date not independently verified; HN page displayed "7 months ago" at retrieval
- audience: Frontend engineer discussing v0
- type: discussion
- evidence: A commenter argues UI should use component hierarchies with pre-defined design guidelines, with colours, margins and radii defined outside raw model-generated code.
- source: [Hacker News, discussion of v0 as a coding agent](https://news.ycombinator.com/item?id=46535691)
- OpenDesigner relevance: Separate chosen design tokens/components from generated layout and implementation. This is a proposed architecture, not firsthand failure evidence.

### Evaluation beyond looks

#### OD-21
- theme: UX / quality review
- date: 2026-02-01
- audience: Claude Code user building frontend products
- type: firsthand
- evidence: Backend is close to one-shot, but frontend takes "a disproportionate amount of time correcting small but numerous UI issues," including spacing, colour, animation, navigation, loading and disabled states, even with project instruction files.
- source: [r/ClaudeAI, consistently good UI question](https://www.reddit.com/r/ClaudeAI/comments/1qsxdn7/how_do_you_get_claude_code_to_consistently_nail/)
- OpenDesigner relevance: Treat interaction states and flows as testable assets, with owner review and clear incomplete status.

#### OD-22
- theme: UX / responsive review
- date: 2026-04-22
- audience: Newer frontend builder using Cursor and Claude Code
- type: firsthand
- evidence: Reports janky modals, mobile breakpoints and subtle interactions; agent self-review "mostly useless" for spotting its own errors.
- source: [r/Frontend, generic AI look and hidden defects](https://www.reddit.com/r/Frontend/comments/1ssqj99/how_do_you_avoid_the_generic_ai_slop_look_when/)
- OpenDesigner relevance: Include preview/test evidence and human review in completion criteria; model self-approval is insufficient.

#### OD-23
- theme: Accessibility
- date: 2025-08-05
- audience: Frontend commenters evaluating AI-generated UI
- type: discussion
- evidence: A commenter identifies "A11y issues" as part of the AI-generated UI tell. The thread does not specify a test or example.
- source: [r/Frontend, AI-generated style discussion](https://www.reddit.com/r/Frontend/comments/1mihgav/what_defines_the_aigenerated_style_in_frontend/)
- OpenDesigner relevance: Put accessibility on the review checklist; do not overclaim this one brief comment as a quantified problem.

## Interpretation for a product backlog (hypotheses, not user requests)

| Evidence cluster | Useful experiment | How to judge it |
| --- | --- | --- |
| OD-01–10 | Ask users to choose/avoid concrete examples and name screen hierarchy before proposing UI | Blind compare distinctiveness and task clarity against a prompt-only baseline |
| OD-11–15 | Explicit reference annotations: "keep this layout / colour / type / feeling" with user approval | Compare output to source elements and count corrections |
| OD-16–20 | Approved design-system record with component/token provenance and a change-impact preview | Track cross-page drift and unintended edits over iterations |
| OD-21–23 | Quality board of interactions, states, responsive checks and human sign-off | Test on multiple viewport sizes and assistive checks; mark unchecked work honestly |

## Method and limits

Searched public web indexes for Reddit discussions in r/Frontend, r/lovable, r/vibecoding and r/ClaudeAI, HN discussions, GitHub issues of Bolt, and the OpenDesigner repo; opened each included source page. The linked [last30days-skill](https://github.com/mvanhorn/last30days-skill) was considered as a search lead, but this corpus uses directly checked public pages rather than claiming results from a tool not run. Searches of X and v0/Lovable GitHub issues did not produce sufficiently verifiable and relevant direct reports for inclusion; no claim of exhaustive coverage. Reddit posters are anonymous and some advice/complaint threads may include self-promotion. HN relative dates were left unconverted rather than guessing exact dates. Do not quote the synthesis as if it were OpenDesigner customer feedback. This is a snapshot, not a continuously refreshed feed.
