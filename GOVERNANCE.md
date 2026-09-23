# Governance

## Who decides

OpenDesigner is maintained by **Kunal Bairwa** ([@ckryptickunal](https://github.com/ckryptickunal)), who has final say on scope, releases and licensing. Contributors who make sustained, high-quality contributions can be invited to become maintainers with merge rights for the areas they know.

## How decisions are recorded

Every coordination or product decision is written down with its reason in [`_coordination/DECISIONS.md`](_coordination/DECISIONS.md), an append-only log. Add entries with:

```bash
OD_SESSION="Your name" python3 tools/od.py log "decision and why"
```

Entries are never edited or deleted. A decision that is reversed gets a new entry that says so and why. Pull requests that change a product decision should add a log entry in the same PR.

Who owns which piece of work is on [`_coordination/BOARD.md`](_coordination/BOARD.md). The product brief everyone designs against is [`_coordination/BRIEF.md`](_coordination/BRIEF.md).

## How research disputes are settled

Research questions are settled by evidence, not by votes or seniority.

1. **Primary beats secondary.** A system's own docs, source code or a W3C spec (Tier A) outrank practitioner writing (Tier B), which outranks community opinion (Tier C). The tiers are defined in [`_coordination/SCHEMA.md`](_coordination/SCHEMA.md).
2. **Newer beats older on fast-moving topics** (Figma features, token specs, OS design languages), unless the older source is cited as history.
3. **Measured beats asserted.** A study or a shipped value outranks a rule of thumb.
4. **Shipped code beats prose** when a system's docs and its published tokens disagree, and the disagreement is recorded.
5. **When sources genuinely conflict,** both stay in the card, the chosen value is marked, and the reason is written down. Conflicts that change the product go into the questionnaire as a real choice for the person instead of being averaged away.
6. **Inference is labelled.** Anything a contributor concluded rather than read is marked `[inferred]` and can be overturned by any sourced claim.

Open a [research correction](.github/ISSUE_TEMPLATE/research-correction.yml) issue to dispute a value. A maintainer merges the correction once the source checks out.

## Product principles that are not up for a vote

These come from the brief and bound every change:

- The model interviews the person and teaches as it goes; it does not replace the designer. Blocks it cannot make well (logo, custom icons, illustration, photography, brand typeface) get a "do you have this?" hook with honest fallbacks.
- Reference intake copies structure and quality, never another brand's identity.
- Everything is traceable: every value to a source or a formula, every decision to a log entry.
- It works in any capable AI host, with a plain-text fallback wherever visuals are not available.

## Changes to this document

Changes to governance are proposed by pull request and need the lead maintainer's approval.
