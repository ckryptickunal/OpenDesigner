# A project board for inputs, work, and assets

Design proposal for review, September 25, 2026. Source: Kunal's September 25 voice note and public `ckryptickunal/OpenDesigner` at `30f0429`. This workstream covers a user-facing explanation surface, not hidden model reasoning.

## What exists

- `skills/opendesigner/references/graph.json` maps research Decision Cards and downstream dependencies. It is a static design-knowledge graph, not a live record of one person's project.
- `engine.py:3651-3669` appends project decisions with path, value, reason, source reference and supersession to `opendesigner/decisions.md`. `state.json` has `references`, `answers`, and `hooks`; the generator writes `DESIGN.md` and a preview. Provenance is distributed across files.
- `skills/opendesigner-extract` measures candidate properties from supplied references, marks confidence and asks for acceptance. `examples/` contains three worked outputs, but those are repo examples, not evidence that a new project produced a specific example.
- `docs/HOW-IT-WORKS.md` has a Mermaid *process* flowchart. The eight shipped HTML templates visualize design choices. Neither is a per-project tree of what was gathered, interpreted, chosen, and built.

## Honest shape

The tree should expose **recorded evidence and decisions**, not manufacture a transcript of the model's private thoughts. "Reasoned" means the short rationale that was actually written for a suggestion or decision, with an explicit label when inferred. Never claim that a source supports a value unless a link or file reference was recorded. Missing provenance is "source not recorded", not a filled-in citation.

Kunal clarified that this should be a **board**: all needed inputs with their status, all assets made from them, what is done and missing, and concise links from what was told to components, a design system, type scale, and color system. A minimum read-only board for one project:

```text
INPUTS [needed / received / pending / declined]
  Person said: "calm" (received) · logo (pending) · repo CSS (received)
WORK [proposed / chosen / built / needs review]
  Color system: muted accent suggested -> D-0012 chosen -> tokens built
  Type scale: default proposed -> awaiting review
ASSETS [made / supplied / missing]
  Color tokens + preview: made from D-0012 · logo: missing
```

A DAG is more accurate internally because one input may support several choices and one choice may change several assets. Render it as a compact status board with grouped cards and expandable "why / made from" links; never duplicate the underlying node. The board needs an explicit input inventory from required questions and hooks so missing inputs appear, not only the inputs already recorded. Nodes need stable IDs, types (`required-input`, `person-input`, `reference`, `recommendation`, `decision`, `component`, `system`, `asset`), source/provenance, status (`needed`, `received`, `declined`, `proposed`, `chosen`, `built`, `needs-review`, `missing`, `superseded`, `unlinked`), and a time or build revision when available. Show the difference between a founder/example fixture in this repo and an example created for the current project. Keep evidence local; never send the tree or referenced content to a server by default.

## First implementation slice

Build a read-only board exporter from required inputs (`questions.json` and hook catalog), project state, `decisions.md`, reference records and generated-file manifest into `opendesigner/board.json`, plus a Markdown board when HTML is unavailable. Include needed, received and missing inputs, then work and assets grouped by color, type, components and whole system. Start with a single worked example fixture and mark links the existing files cannot prove as "unlinked". Resist brittle parsing of free-form reasons into fake semantic edges. If a link is not explicitly recorded, show a flat parent group rather than guessing. A static HTML board can follow once the data contract is tested; it must be keyboard navigable, show status without relying on color alone, and give a plain-text path to every card. Keep user project facts out of committed repo fixtures unless fictional.

Tests: a project with no references; an accepted and ignored reference; a changed decision whose prior version remains visible; two outputs depending on one decision; missing source; and a real generated preview versus a shipped gallery example. Ensure the tree reflects a changed project without stale nodes, never modifies decisions, and does not disclose local content through network calls.

## Decision needed

Resolved: Kunal wants a status board for one project, including every needed input, received and missing material, made assets, and concise provenance for each system part. Remaining choice: decide in usability tests how much detail stays visible on the board versus opening a card. Do not wait for that choice to build a read-only data prototype.
