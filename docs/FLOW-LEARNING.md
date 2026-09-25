# Learning where to shorten or extend the flow

Design proposal for review, September 25, 2026. Source: Kunal's September 25 voice note and public `ckryptickunal/OpenDesigner` at `30f0429`. This workstream is about adapting the *interview*, not persisting global preferences or building the tree.

## What exists

- `skills/opendesigner/SKILL.md` and `references/zoom.md` define sketch, broad, defined and detailed levels, asking fewer questions when prior words or files already answer them; a "just pick" route delegates optional choices.
- `references/questions.json` and `pacing.json` define IDs, stages, impact and the planned path. `engine.py` records answers, how they were set, and changes in the project's `state.json` and `decisions.md`.
- `journey.py` only logs after clear local consent (`profile.tracking=on`). It records shown, answered, skipped, changed, help, frustration and speed-mode events; `analyze()` at lines 760-831 suggests friction hotspots, defaults and speed-ups; `report()` writes a local `JOURNEY.md`. The engine does not turn those suggestions into automatic question routing.
- Anonymous reporting has its own separate sharing choice. The ChatGPT Project bundle explicitly omits `journey.py`, so the same loop is not available in every host.

## Missing behavior

The current report advises a maintainer to reword, split, or auto-apply a question. It cannot tell if a given person wants *this* explanation shorter or longer next time, and it should not silently rewrite the common interview from one session's sparse signals. Speed-mode means the person delegated; it is not evidence that a high-impact choice has a safe universal default. A quick finish is not proof the UI works for its users.

## Proposed experiment

Use a separate, reversible routing recommendation layered over the current question list. Inputs: the current project's answered/locked values; applicable skips; explicit requests ("faster", "show an example", "explain more"); and, only when consented, local friction counts. Outputs: suggest "keep", "shorten wording", "show one example", or "offer deeper explanation" with a reason and the question ID. Never silently skip an owner-input question, alter an answer, loosen accessibility checks, or auto-enable logging. Do not store free-text user answers in telemetry.

Before an algorithm, run observed trials with at least one designer, a frontend engineer and an individual polishing an existing app. For each question record whether it was needed, how many turns it took, requests for help, whether the person could explain the decision, and whether it stuck in a later session. Compare the same task with current wording and a candidate shorter or deeper version. A single signal calls for a candidate, not a universal rule. Proposed gate: two independent observations of the same friction before changing shared wording; one user's explicit in-session request may adapt *that session* at once.

## Code boundary and tests

A pure route-planning function can accept project state and a small set of consented events, return a reasoned suggestion, and never write. Keep the engine's deterministic token generation independent of question length. Test no-consent, one explicit speed request, repeated help, high-impact owner question, answered-by-repo, locked decision and conflicting signals. Require the person to see the unchanged decision and be able to ask for the full explanation at any time. In the journey report, describe the recommendation as a hypothesis rather than "auto-apply it" until user testing supports it.

Do not open a behavior-changing PR from these assumptions alone. A small first PR could clarify report wording and add tests for suggestions, with no automatic routing; collect trials before altering the shared flow.
