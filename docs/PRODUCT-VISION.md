# OpenDesigner: product vision

Draft for Kunal's review, September 25, 2026. This replaces the earlier field-plan hypothesis with the founder's stated purpose. It is direction, not a claim that every capability has shipped. Source: Kunal's September 25 voice note at 2:32 PM IST; implementation references are to public `ckryptickunal/OpenDesigner` at `30f0429`.

## Why this exists

AI can improve at code while still missing the human side of design. It cannot reliably predict how a person will interact with a product or what using it will feel like. OpenDesigner is an open-source way to keep the person who knows the users involved as an AI-assisted product takes shape. It should help people make and improve interfaces, not claim to replace the judgment of designers, users, or product owners.

The working promise is: inspect the product and its existing design, offer research-backed choices people can see and challenge, ask for the decisions and assets that need a human, then write a usable design system that can be revisited as the project changes. A generated preview is a proposal to test, not evidence that users understand or like it. Accessibility checks establish floors; they cannot substitute for watching someone use the product.

## Who it is for

- Designers who use AI tools to make projects and want the mechanical system work handled without giving away direction and taste.
- Front-end engineers, especially on larger projects, who need consistent decisions across surfaces and future sessions.
- Individuals who have already built a project and want to polish its interface and make it more useful to people, rather than start from scratch.

These are use cases, not proven segments or a ranked market. The earlier field-plan assumption that a small Next.js/Tailwind team is the primary audience is a test candidate, not the founder's stated limit. Do not collapse the product to that one segment without observed user evidence.

## Product principles

1. **Human judgment stays visible.** The person decides product direction, identity, trade-offs, interaction expectations, and whether a suggested design actually works for users. Label defaults and assumptions as such. Do not present generated work as designer-approved.
2. **Work with what exists.** Read the project's files, code and references before asking. Let a later session extend and review earlier decisions instead of resetting them.
3. **Separate kinds of learning.** A preference about how a person wants to work across projects is not a design choice for every project. Keep project-specific decisions, assets and tested adaptations local; make any reusable preference explicit, reviewable and reversible before applying it elsewhere. Never silently promote private project context into a global profile.
4. **Adapt the path using evidence.** After testing, shorten repeated friction and extend steps where people need explanation or examples. A request to move faster is not proof that a high-stakes decision can be skipped. Preserve the human checkpoints and accessibility floors.
5. **Show the trail.** Give people a readable view of what was gathered, what was inferred or reasoned, what they chose, and what examples or outputs resulted. Let them correct the link between evidence and conclusion. The tree is for understanding and review, not a pretend transcript of hidden model reasoning.
6. **Be honest about maturity.** The repository is in progress. Engine tests, three sample systems, templates and exports show implementation, not production use, host reliability or user satisfaction.

## What exists today, and what is still proposed

The public repo contains a Python design-system engine (`skills/opendesigner/scripts/engine.py`), source-backed questions and decisions, DTCG token generation, CSS/Tailwind/Figma exports, eight visual templates, examples, and an opt-in local journey tracker (`journey.py`). It keeps a per-project `opendesigner/state.json` and append-only `decisions.md`. The optional tracker can summarize friction, but does not itself change the interview. There is no tested cross-project preference scope or user-facing evidence-to-decision tree. The ChatGPT bundle has no journey tracker. These are proposals for research and implementation, not current features.

## Near-term test

Watch people from each intended use case work on their own or a permission-cleared sample project. Record where the flow asks too much, where it skips needed context, whether the person can explain a decision, and whether they keep and use the output in a second session. Compare the local project, host, and any proposed reusable preferences without sending project data anywhere without separate consent. Prioritize recurring observed failures over adding another exporter.

## Boundary

OpenDesigner helps create a design system and improve a UI; it cannot certify a product as user-centered by generating tokens or a preview. The person checks the result with actual users. This document does not assert demand, adoption, revenue, or completion. Keep the repo's specific implementation status and roadmap separate from the founder's intended outcome.
