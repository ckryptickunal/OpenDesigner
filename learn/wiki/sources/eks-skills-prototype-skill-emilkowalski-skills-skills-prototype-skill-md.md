---
type: source
title: "emilkowalski/skills: skills/prototype/SKILL.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-prototype-skill
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/prototype/SKILL.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - prototyping
  - variants
  - divergence
  - design-exploration
  - visual-options
  - decision-making
  - presenting-designs
  - craft-bar
  - agent-skill
  - emil-kowalski
---

# emilkowalski/skills: skills/prototype/SKILL.md

## Metadata

- Page ID: `eks-skills-prototype-skill`
- Publisher: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/prototype/SKILL.md

## Summary

The prototype skill from Emil Kowalski's skills repository turns one described piece of UI into several genuinely different, fully working versions and shows them one at a time behind a fixed visual picker, so a person can flip through them live and promote the one that feels right. Its core idea is divergence: each variant must explore a different named axis (layout, density, personality, motion or interaction model) and be defensible as a shipping direction, while every variant still meets the craft bar (ease-out entrances, UI motion under 300ms, correct transform-origin, transform and opacity only, reduced motion handled). It sets a six-phase workflow (scope, recon, choose directions, build the harness, verify and hand off, promote), keeps all exploration away from production code, and requires an honest table of when each variant wins and what it costs before handing the choice to the person. For a design system this is a ready-made process for showing people a few visual options, built from the project's own tokens, and letting them choose instead of guessing for them [inferred].

## Key Ideas

- The value of a variant exploration is divergence: tints of one idea teach nothing, so each variant must be a different answer you could defend shipping.
- Every variant diverges on a named axis (layout, density, personality, motion, interaction model) that can be stated in a phrase before any code is written.
- Divergence never lowers the craft bar: each variant still uses ease-out entrances, sub-300ms UI motion, correct transform-origin, transform/opacity only and reduced-motion handling.
- Variants are built from the project's own tokens so each could ship tomorrow; sharing tokens is not convergence.
- Every variant fully works, with real interactions, real motion and realistic product-shaped content, never lorem ipsum or dead buttons.
- Exploration lives in an isolated prototype surface (a /prototypes route or a single HTML file) and never touches production code until one variant is picked.
- Three variants is the default, five is the cap; more dilutes the comparison, and two truly distinct directions beat three padded ones.
- Variants are named for their direction (Quiet, Editorial, Playful, Dense), never Option A/B/C.
- Judge one variant at a time, full size, in realistic surrounding context; thumbnails distort spacing and scale.
- Switching between variants is instant because flipping happens 100+ times a session, so by the frequency rule it gets no animation.
- The picker is neutral chrome copied verbatim, not a contestant, and never adapts to the project.
- Hand-off is an honest table of each variant's axis, when it is the right choice and what it costs, then the agent stops: the choice belongs to the person.
- The product's personality bounds how bold the boldest variant may go, and any recommendation should rest on personality and frequency of use, not aesthetics alone.
- After a pick, the winner is integrated following project conventions and the prototype surface is deleted; another round diverges around the direction the person leaned toward.
- This workflow matches OpenDesigner's need to let people pick among a few options from a visual sample rather than choosing for them [inferred].

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Author of the skills repository; the skill says its craft bar comes from his design engineering philosophy
- [[entities/emilkowalski-skills|emilkowalski/skills]] (product): MIT-licensed GitHub repository of agent skills; source of this SKILL.md at commit 85e8e23
- [[entities/prototype|prototype]] (tool): The agent skill described here: builds several genuinely different UI variants behind a visual picker; runs only when explicitly invoked
- [[entities/picker-md|PICKER.md]] (tool): Companion spec with the picker's exact markup, styles and behavior, copied verbatim
- [[entities/review-animations|review-animations]] (tool): Sibling skill that reviews existing UI; out of scope for prototype
- [[entities/improve-animations|improve-animations]] (tool): Sibling skill that plans fixes for existing UI; out of scope for prototype
- [[entities/pick-ui-library|pick-ui-library]] (tool): Sibling skill that chooses dependencies; out of scope for prototype
- [[entities/divergence|Divergence]] (concept): The whole value of the skill: each variant explores a genuinely different answer to the same brief
- [[entities/axis|Axis]] (concept): The named dimension a variant diverges on: layout, density, personality, motion or interaction model
- [[entities/prototype-surface|Prototype surface]] (concept): Isolated route or standalone HTML file where variants live; never imported into production and deleted after promotion
- [[entities/frequency-rule|Frequency rule]] (concept): Rule cited for why the variant swap, a 100+/session action, gets no animation; not defined in this file
- [[entities/tailwind|Tailwind]] (library): Named as one possible styling system to identify during recon
- [[entities/css-modules|CSS modules]] (tool): Named as one possible styling system to identify during recon

## Topics

- [[topics/prototyping|Prototyping]]: A six-phase workflow for building 3 (up to 5) genuinely different, fully working variants of one UI piece in an isolated surface, shown one at a time behind a fixed picker, then promoting the winner and deleting the prototype.
- [[topics/design-process|Design process]]: Scope to one piece and restate the brief in one sentence, do recon on stack, tokens, personality and context, choose named directions on distinct axes before coding, verify every variant, hand off with a tradeoff table, then promote or riff.
- [[topics/presenting-designs|Presenting designs]]: Show one variant at a time, full size, in realistic context, never as side-by-side thumbnails; present a table of axis, when it wins and its cost; never pre-pick a favorite; close with where the picker runs and the keys to flip.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Divergence without dropping craft; each variant defensible on its own; if two converge, cut one and say so; recommendations rest on the product's personality and frequency of use, not aesthetics alone.
- [[topics/motion-principles|Motion principles]]: Every variant meets the craft bar (ease-out entrances, never ease-in, sub-300ms UI motion, correct transform-origin, transform/opacity only, reduced motion handled), and switching variants gets no animation because it is a 100+/session action.
- [[topics/easing-and-timing|Easing and timing]]: Entrances use ease-out, never ease-in, and UI motion stays under 300ms in every variant.
- [[topics/reduced-motion|Reduced motion]]: Reduced-motion handling is part of the craft bar every variant must meet.
- [[topics/animation-performance|Animation performance]]: Variants animate only transform and opacity.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Variants use the project's existing colors, radii, spacing, fonts and easing/duration variables so each could ship tomorrow; sharing tokens is not convergence; with no project, a restrained default of neutral grays, one accent and the system font stack.
- [[topics/content-and-microcopy|Content and microcopy]]: Variants use realistic, product-shaped copy with plausible names and numbers, no lorem ipsum; variant names describe the direction (Quiet, Editorial, Playful, Dense), never Option A/B/C.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: In a project with a dev server, variants live on an isolated route such as /prototypes/<slug>, one file per variant plus a small harness file; with no project, a single self-contained HTML file with inline CSS/JS.
- [[topics/ai-assisted-design|AI-assisted design]]: An agent skill that runs only when explicitly invoked, has a fixed first reply, stays in scope (not review, fixes or dependency choice), verifies its own output with the browser and screenshots, and stops for the person's choice.

## Notable Claims

- Three tints of the same idea waste the picker because the user learns nothing by flipping between them. Evidence: Operating Posture
- A sloppy variant does not widen the exploration; it loses on execution and teaches nothing about the direction it represents. Evidence: Operating Posture: Divergence is not an excuse to drop the craft bar
- Sharing the project's tokens is not convergence. Evidence: Hard Rules 2
- The product's personality bounds how far the boldest variant may go. Evidence: Phase 2 — Recon: Personality
- More than 5 variants dilutes the comparison. Evidence: Phase 3 — Choose directions
- Two directions that differ only in accent color or copy are one direction. Evidence: Phase 3 — Choose directions
- Side-by-side thumbnails distort spacing and scale. Evidence: Phase 4 — Build the picker harness
- Flipping between variants is a 100+/session action, so by the frequency rule the variant swap gets no animation. Evidence: Phase 4: Switching is instant
- A picker with two truly distinct directions beats one padded to three. Evidence: Tone

## Quotes

> three tints of the same idea waste the picker
> never judge UI at postage-stamp size.
> a picker with two truly distinct directions beats one padded to three.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is an agent skill prompt, so parts of it are agent behaviour (explicit invocation only, stop and wait for the choice, delete the prototype after promotion) rather than visual design rules.
- Caveat: The fixed first reply ('my craft bar comes from Emil Kowalski's design engineering philosophy') is the skill's own branding; the rules record only that the first reply is fixed and says nothing else, not its wording.
- Caveat: Snapshot of the repository at commit 85e8e23; workflow details and sibling skill names may change later.
- Caveat: The craft bar items and the frequency rule are only named here; their full definitions presumably live in Emil Kowalski's other skills and essays [inferred].
- Caveat: The hand-off table shows only two example rows (Quiet, Editorial) although the default is three variants; the rows are illustrative.
- Caveat: The sibling skill pick-ui-library is referenced but not described in this source.
- Caveat: The isolated-route branch assumes a web framework with routing; the source does not cover native iOS or Android prototypes [inferred].

### Rules and practices

- **must** (process, all): Run the prototype workflow only when it is explicitly invoked; do not trigger it on your own. Why: The skill is marked disable-model-invocation and only runs when explicitly invoked. Values: disable-model-invocation: true. [Frontmatter description: Only runs when explicitly invoked]
- **must** (process, all): When the skill is first invoked without a specific question, reply only with its fixed one-line ready message, and give no other information until the user asks a question. Why: Stated in the skill's Initial Response section; no reason given. [Do not provide any other information until the user asks a question.]
- **must** (process, all): Keep a prototype run to divergence only: build versions of a described UI piece behind a picker, and do not review existing UI, plan fixes for it or choose dependencies in the same run. Why: Those jobs belong to review-animations, improve-animations and pick-ui-library. [A divergence skill. It does ONE thing]
- **must** (process, all): Make every variant a direction you could defend shipping on its own, exploring a genuinely different answer to the same brief. Why: The entire value is divergence; three tints of the same idea waste the picker because the user learns nothing by flipping between them. [Operating Posture]
- **must** (motion, all): Use ease-out on every variant's entrances, never ease-in. Why: Divergence is not an excuse to drop the craft bar; a sloppy variant just loses on execution and teaches nothing about its direction. Values: ease-out, never ease-in. [Operating Posture: right easing]
- **must** (motion, all): Keep every variant's UI motion under 300ms. Why: Part of the craft bar every variant must meet. Values: sub-300ms. [sub-300ms UI motion]
- **must** (motion, all): Set the correct transform-origin on every variant's animated elements. Why: Part of the craft bar every variant must meet. Values: transform-origin. [correct `transform-origin`]
- **must** (motion, all): Animate only transform and opacity in every variant. Why: Part of the craft bar every variant must meet. Values: transform, opacity. [Operating Posture: transform/opacity only]
- **must** (accessibility, all): Handle reduced motion in every variant. Why: Part of the craft bar every variant must meet. [Operating Posture: reduced-motion handled]
- **must** (process, all): Never touch production code during exploration; build every variant in an isolated prototype surface, and integrate into production only after the user picks, and only the picked variant. Why: Integration happens only at promotion, only for the variant the user picked. [Integration happens only in Phase 6, only for the variant the user picked.]
- **must** (process, all): Make variants diverge on a named axis (layout, density, personality, motion or interaction model), and be able to state each variant's axis in a phrase before building. Why: The entire value of the skill is divergence; three tints of the same idea waste the picker. Values: layout, density, personality, motion, interaction model. [Variants diverge on a named axis]
- **must** (tokens, all): Build every variant from the project's existing tokens (colors, radii, spacing, fonts, easing and duration variables) so each looks like it could ship in the product tomorrow. Why: Variants should feel native to the product; sharing the project's tokens is not convergence. [Variants use these — every variant should look like it could ship in this product tomorrow]
- **must** (content, all): Make every variant fully work: real interactions, real motion and realistic, product-shaped copy with plausible names and numbers. Why: Stated as Hard Rule 3 ('Every variant fully works'); no separate reason given. [Real interactions, real motion, realistic content]
- **must** (content, all): Never put lorem ipsum, dead buttons or 'imagine this part' placeholders in a variant. Why: Stated as Hard Rule 3 ('Every variant fully works'); no separate reason given. [No lorem ipsum, no dead buttons]
- **must** (tooling, web): Treat the picker as chrome, not a contestant: copy its markup, styles and behavior verbatim from PICKER.md and never adapt its look to the project. Why: Its look is not a design decision and never adapts to the project. [The picker is chrome, not a contestant]
- **must** (process, all): When a winner is promoted, delete the prototype surface unless the user asks to keep it. Why: Stated as Hard Rule 5 ('Clean up after the choice'); no further reason given. Values: keep <variant>, leave the picker. [delete the prototype surface unless the user asks to keep it]
- **must** (process, all): Explore one UI piece per run; if the description spans several components (for example 'the dashboard'), pick the single highest-leverage piece, say which and why, and offer the rest as follow-up runs. Why: One thing per run. [Phase 1 — Scope]
- **must** (process, all): Restate the brief in one sentence: what the thing is, where it will live and what it must do. Why: Stated in Phase 1 (Scope); no reason given. [Phase 1 — Scope]
- **must** (process, all): Before designing, identify the stack: framework, styling system (Tailwind, CSS modules, vanilla) and motion library, if any. Why: Map the ground the variants must stand on. Values: Tailwind, CSS modules, vanilla. [Phase 2 — Recon: Stack]
- **must** (process, all): Judge the product's personality (playful consumer app or crisp dashboard) and let it bound how far the boldest variant may go. Why: Personality bounds how bold a variant may be. [Phase 2 — Recon: Personality]
- **must** (process, all): Map where the piece renders: against what background, beside what neighbors and at what sizes. Why: Map the ground the variants must stand on. [Phase 2 — Recon: Context]
- **must** (tokens, all): With no project (an empty directory, or the user is just exploring), use the standalone branch and a restrained default look: neutral grays, one accent and the system font stack. Why: There are no project tokens to build on [inferred]. Values: neutral grays, one accent, system font stack. [choose a restrained default look: neutral grays, one accent, system font stack]
- **must** (process, all): Build 3 variants by default; go up to 5 only when the user asks or the design space is genuinely wide. Why: The source gives no reason for 3; more than 5 dilutes the comparison. Values: 3, 5. [Phase 3 — Choose directions]
- **must** (process, all): Never build more than 5 variants, even when asked for more (a request like '<description> x5' is capped at 5). Why: More than 5 dilutes the comparison. Values: 5, x5. [Phase 3; Invocation Variants: capped at 5]
- **must** (process, all): Before writing any code, list the set of variants with a name and an axis for each. Why: Directions are chosen before building. [Before writing any code, list the set: a name and an axis for each]
- **must** (content, all): Name each variant for its direction, such as 'Quiet', 'Editorial', 'Playful' or 'Dense', never 'Option A/B/C'. Why: Names describe the direction. Values: Quiet, Editorial, Playful, Dense. [Phase 3 — Choose directions]
- **must** (process, all): Do not count two directions that would differ only in accent color or copy as two: they are one direction, so replace one with a real alternative (a different layout, interaction model or motion story). Why: Differing only in accent color or copy is one direction, not two. [Phase 3 — Choose directions]
- **must** (process, all): Do not start building until every variant has a name and a stated axis and no two variants share an axis position. Why: This is the completion criterion for choosing directions. [Phase 3: Completion criterion]
- **must** (tooling, web): In a project with a dev server, build the harness as an isolated route or page (/prototypes/<slug> or the framework's equivalent), with one file per variant plus a small harness file. Why: Exploration stays isolated from production. Values: /prototypes/<slug>. [Phase 4 — Build the picker harness]
- **must** (tooling, all): Never import anything from the prototype surface into production code. Why: Exploration must not touch production. [Phase 4: Nothing imports from the prototype surface]
- **must** (tooling, web): With no project or a static context, build a single self-contained HTML file with inline CSS and JS that the user can open directly in a browser. Why: So the user can open it directly in a browser. [Phase 4: No project / static context]
- **must** (tooling, web): Load PICKER.md when building the harness and build exactly its markup, styles, keyboard wiring and placement. Why: The picker is specified, not designed. [Phase 4: load it now and build exactly that]
- **must** (process, all): Render one variant at a time, full size, in realistic surrounding context: a toast needs a page behind it, a card needs siblings, a button needs a form. Why: Side-by-side thumbnails distort spacing and scale; never judge UI at postage-stamp size. [one variant at a time, full size, in realistic surrounding context]
- **must** (process, all): Do not compare variants as side-by-side thumbnails; never judge UI at postage-stamp size. Why: Side-by-side thumbnails distort spacing and scale. [Phase 4: Side-by-side thumbnails distort spacing and scale]
- **must** (motion, all): Do not animate the switch between variants; switching is instant. Why: Flipping is a 100+/session action; by the frequency rule the variant swap gets no animation. Values: 100+/session. [by the frequency rule the variant swap gets no animation]
- **must** (process, all): Run the harness and confirm every variant renders, is reachable from the picker, responds to every interaction and leaves the console clean, flipping through all variants yourself before showing the user. Why: Verification before hand-off; no console errors is a completion criterion. [Phase 5 — Verify and hand off]
- **must** (process, all): If browser tooling is available, screenshot each variant. Why: Part of verification before hand-off. [Phase 5: screenshot each variant]
- **must** (process, all): Present the set as a table with columns #, Variant, Axis, When it's the right choice, and Its cost, then stop. Why: The choice belongs to the user. Values: #, Variant, Axis, When it's the right choice, Its cost. [Phase 5: stop — the choice belongs to the user]
- **must** (process, all): Close the hand-off with where the picker is running (URL or file path) and the keys to flip. Why: The user needs to reach and operate the picker. [Phase 5: Close with where the picker is running]
- **must** (content, all): Sell each variant honestly: one line on when it wins and one on what it costs, naming each tradeoff truthfully. Why: The table must name each variant's tradeoff honestly (completion criterion). [Sell each variant honestly — one line on when it wins, one on what it costs]
- **must** (process, all): Never pre-pick a favorite in the hand-off table. Why: The choice belongs to the user. [Never pre-pick a favorite in the table]
- **must** (process, all): If the user asks which variant you would choose, answer with a reason rooted in the product's personality and frequency of use, not aesthetics alone. Why: Stated in the Tone section; the source gives no further reason. [answer with a reason rooted in the product's personality and frequency of use, not aesthetics alone]
- **must** (process, all): If two variants converged while you built them, cut one and say so instead of padding the picker. Why: A picker with two truly distinct directions beats one padded to three. [If two variants converged while you built them, cut one and say so]
- **must** (process, all): When the user picks, integrate that variant where it belongs following the project's existing conventions (file layout, naming, token usage), then delete the prototype surface. Why: Promotion ends the exploration and cleans up after the choice. Values: keep <variant>. [Phase 6 — Promote on selection]
- **must** (process, all): If the user wants another round, keep the harness and choose directions again, diverging around the direction they gravitated to. Why: A new round refines toward what the user leaned toward. Values: riff <variant>. [Phase 6; Invocation Variants: riff]

### Decisions it informs

- How many variants should the exploration show?
  - 3 variants (default): A focused comparison of three distinct directions When: Every run unless the user asks for more or the design space is genuinely wide
  - Up to 5 variants: Wider exploration; more than 5 dilutes the comparison When: The user asks (for example '<description> x5') or the design space is genuinely wide
  - 2 variants: Two truly distinct directions When: Two of three converged while building; cut one and say so
  - Recommendation: Default to 3, cap at 5, and prefer two truly distinct directions over a set padded to three.
- What should each variant differ on?
  - Layout: A different arrangement of the same piece When: The structure of the piece is open [inferred]
  - Density: Tighter or roomier versions of the piece [inferred] When: How much fits on screen is in question [inferred]
  - Personality: A different character, for example quiet versus playful, bounded by the product's personality When: The tone of the piece is open [inferred]
  - Motion: A different motion story When: How the piece enters, responds or changes is in question [inferred]
  - Interaction model: A different way of operating the piece When: How people use the piece is in question [inferred]
  - Recommendation: Give each variant a named axis position that no other variant shares; directions differing only in accent color or copy count as one.
- Where should the variants be built?
  - Isolated route in the project: A /prototypes/<slug> page (or framework equivalent), one file per variant plus a small harness file, never imported by production When: There is a project with a dev server
  - Standalone HTML file: One self-contained file with inline CSS and JS that opens directly in a browser When: No project, an empty directory or a static context
  - Recommendation: Pick by what exists; either way keep exploration isolated from production code.
- How should people compare the variants?
  - One at a time, full size, in context: Each variant shown at real size with its surroundings (a page behind a toast, siblings beside a card, a form around a button), switched instantly When: Always
  - Side-by-side thumbnails: Distorts spacing and scale When: Never
  - Recommendation: One variant at a time, full size, in realistic context, with instant switching.
- What happens after the person has seen the variants?
  - keep <variant>: The variant is integrated following project conventions and the prototype surface is deleted When: The person has picked a winner
  - keep <variant>, leave the picker: The variant is promoted but the prototype surface stays When: The person wants to keep the exploration around
  - riff <variant>: A fresh set diverging around the named variant's direction, reusing the harness When: The person gravitated to a direction but wants another round
  - Recommendation: Wait for the person's choice; clean up after promotion unless they ask to keep the picker.

### Process

1. Scope: Take one UI piece per run; if the description spans several components, choose the highest-leverage one, say which and why, offer the rest as follow-ups, and restate the brief in one sentence (what it is, where it lives, what it must do).
2. Recon: Identify the stack (framework, styling system, motion library), the tokens (colors, radii, spacing, fonts, easing and duration variables), the personality (playful consumer or crisp dashboard) and the context (background, neighbors, sizes). With no project, use a restrained default: neutral grays, one accent, system font stack.
3. Choose directions: Plan 3 variants (up to 5), each with a direction name and a stated axis; replace any two that differ only in accent color or copy. Done when every variant has a name and axis and no two share an axis position.
4. Build the picker harness: In a project, an isolated /prototypes/<slug> route with one file per variant plus a harness file; otherwise a single self-contained HTML file. Add the PICKER.md picker verbatim, render one variant at a time full size in realistic context, and switch instantly.
5. Verify and hand off: Run it, flip through every variant, confirm interactions work and the console is clean, screenshot each if possible, then present the table (#, Variant, Axis, When it's the right choice, Its cost), say where the picker runs and which keys flip it, and stop.
6. Promote on selection: Integrate the picked variant using the project's conventions and delete the prototype surface (unless asked to keep it), or keep the harness and riff around the direction the person leaned toward.

### Examples and visual references

- Briefs suited to one run ('a toast', 'the pricing card', 'a hold-to-delete button'): Single UI pieces that can be explored as several directions in one run.
- Brief too broad for one run ('the dashboard'): Spans multiple components, so it is narrowed to the single highest-leverage piece with the rest offered as follow-ups.
- Quiet variant (Hand-off table example): Axis: minimal motion, borders over shadows; right when the product is a daily-use tool; cost: least memorable.
- Editorial variant (Hand-off table example): Axis: large type, generous whitespace; right when the moment deserves weight; cost: eats vertical space.
- Realistic surrounding context (Phase 4 examples): A toast is shown with a page behind it, a card with siblings, a button inside a form, so spacing and scale read correctly.

### Numbers

- 3: Default number of variants [Phase 3 — Choose directions]
- 5: Maximum number of variants; more dilutes the comparison [Phase 3; Invocation Variants: capped at 5]
- sub-300ms: UI motion budget every variant must meet [Operating Posture]
- 100+/session: How often a person flips between variants, the reason switching gets no animation [Phase 4]
- one sentence: Length of the restated brief [Phase 1 — Scope]

<!-- /od:learn -->
