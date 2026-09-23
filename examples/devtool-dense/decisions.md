# Decisions

Append-only, ADR-style (spec 7.9): one entry per decision, newest last. A later entry for the same path supersedes an earlier one; nothing is edited or deleted. set_by is chosen, confirmed_default, auto_default, assumed, delegated, reference or asset.

## D-0001 · init with defaults
- set_by: auto_default · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: Start of the design system; every default traces to references/levers.json.

## D-0002 · summary = "A dense, calm console for a fictional CI and observability tool: productive, compact, sharp, quiet."
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: the one-line brief
- previous value: ""

## D-0003 · context.product = "Build and run console for platform teams: pipelines, logs, traces."
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: product brief
- previous value: ""

## D-0004 · context.audience = "Engineers who keep it open all day on large desktop screens."
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: Q-aud-01 conversation
- previous value: ""

## D-0005 · context.surfaces = [{"name": "Pipelines table", "mode": "Operate"}, {"name": "Run detail and logs", "mode": "Read"}]
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: two main surfaces
- previous value: []

## D-0006 · context.memorable = "The run timeline: every step of a build on one line."
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: Q-brand-02
- previous value: ""

## D-0007 · context.scope = {"in": ["web app", "desktop shell"], "out": ["marketing site", "mobile apps"]}
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: scope agreed at the first gate
- previous value: {"in": [], "out": []}

## D-0008 · principles = ["The task comes first: chrome recedes, data leads.", "Dense, never cramped: visuals shrink, hit areas do not.", "Quiet motion: show state changes, skip choreography."]
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: ranked principles
- previous value: []

## D-0009 · answers.Q-aud-01 = "dense"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: people work all day in data-heavy tables
- also set: dials.density = 80 (from Q-aud-01)

## D-0010 · answers.Q-plat-01 = ["web", "desktop"]
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: browser plus an Electron-style desktop shell
- also set: raw.platforms = ["web", "desktop"] (from Q-plat-01)

## D-0011 · raw.inputs = ["pointer"]
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: pointer-first desktop tool; touch is out of scope, so the 24px WCAG 2.5.8 floor applies
- previous value: ["pointer", "touch"]

## D-0012 · dials.expression = 20
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: productive: no hero moments inside the product (DC-L06-03)

## D-0013 · dials.brandPresence = 55
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: own look on an open neutral face; platform chrome stays native

## D-0014 · dials.density = 85
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: compact band: 14px body, 32px default controls, compact spacing mode
- previous value: 80

## D-0015 · dials.energy = 20
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: calm: productive easing, no overshoot, durations x0.88

## D-0016 · dials.roundness = 30
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: 4px controls: crisp but not brutal (Fluent, Radix band)

## D-0017 · dials.depth = 22
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: ring plus faint shadow: separation without heavy shadows in dense layouts

## D-0018 · dials.colorfulness = 30
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: neutral scheme: color only where it means something (status, selection, the primary action)

## D-0019 · dials.warmth = 30
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: cool, formal neutrals: slate-leaning gray

## D-0020 · raw.brandColor = "#4a5cf0"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: the product's indigo; used as the accent hue

## D-0021 · raw.flags.brandExact = true
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: keep the exact indigo on the primary action even at low colorfulness (Carbon pattern)
- previous value: false

## D-0022 · raw.textFace = "Inter"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: open neutral face with tabular figures; OFL licence
- previous value: "system"

## D-0023 · raw.monoFace = "JetBrains Mono"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: logs and code; OFL licence
- previous value: "ui-monospace"

## D-0024 · raw.scripts = ["Latn"]
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: English-only product for now
- previous value: ["Latn"]

## D-0025 · hooks.H-logo.status = "have"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: SVG logo exists
- previous value: "pending"

## D-0026 · hooks.H-favicon.status = "have"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: derived from the logo SVG
- previous value: "pending"

## D-0027 · hooks.H-icons.status = "open-library"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: Lucide (ISC licence), 1.5px strokes at 16px match the formula
- previous value: "pending"

## D-0028 · hooks.H-type.status = "open-library"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: Inter and JetBrains Mono under the SIL OFL
- previous value: "pending"

## D-0029 · hooks.H-color.status = "have"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: the indigo is fixed
- previous value: "pending"

## D-0030 · hooks.H-illus.status = "not-needed"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: empty states use icon plus text
- previous value: "pending"

## D-0031 · hooks.H-photo.status = "not-needed"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: no photography in a console
- previous value: "pending"

## D-0032 · hooks.H-voice.status = "placeholder"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: draft voice from the dials until a writer reviews it
- previous value: "pending"
