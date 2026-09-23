# Decisions

Append-only, ADR-style (spec 7.9): one entry per decision, newest last. A later entry for the same path supersedes an earlier one; nothing is edited or deleted. set_by is chosen, confirmed_default, auto_default, assumed, delegated, reference or asset.

## D-0001 · init with defaults
- set_by: auto_default · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: Start of the design system; every default traces to references/levers.json.

## D-0002 · summary = "A plain, high-contrast system for a fictional city benefits service: AAA text, generous targets, no motion."
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: the one-line brief
- previous value: ""

## D-0003 · context.product = "Apply for and track council benefits online."
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: product brief
- previous value: ""

## D-0004 · context.audience = "Everyone, including people with low vision, low literacy, old devices and assistive technology."
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: Q-aud-01
- previous value: ""

## D-0005 · context.surfaces = [{"name": "Application form", "mode": "Operate"}, {"name": "Guidance pages", "mode": "Read"}]
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: surfaces
- previous value: []

## D-0006 · context.memorable = "Nothing to learn: one question per page."
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: Q-brand-02
- previous value: ""

## D-0007 · context.constraints = ["Legal: public-sector accessibility regulations", "Works without JavaScript"]
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: constraints
- previous value: []

## D-0008 · principles = ["Start with user needs.", "Do less, but make it work for everyone.", "Plain over clever."]
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: ranked principles
- previous value: []

## D-0009 · answers.Q-aud-01 = "large"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: occasional, public users
- also set: dials.density = 15 (from Q-aud-01)

## D-0010 · answers.Q-plat-01 = ["web"]
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: web only
- also set: raw.platforms = ["web"] (from Q-plat-01)

## D-0011 · answers.Q-theme-01 = "light-only"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: one light theme keeps testing simple; forced colors still work
- also set: raw.flags.darkMode = false (from Q-theme-01)

## D-0012 · answers.Q-motion-01 = "none"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: no motion; state changes are instant
- also set: dials.energy = 0 (from Q-motion-01)
- also set: raw.flags.motionOff = true (from Q-motion-01)

## D-0013 · raw.inputs = ["touch", "pointer"]
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: phones and desktops
- previous value: ["pointer", "touch"]

## D-0014 · dials.expression = 10
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: plain: no hero moments, whitespace over containers

## D-0015 · dials.brandPresence = 85
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: one fixed look everywhere; no theming

## D-0016 · dials.density = 8
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: spacious: 19px body text
- previous value: 15

## D-0017 · dials.roundness = 0
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: square corners

## D-0018 · dials.depth = 5
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: borders only; no shadows

## D-0019 · dials.colorfulness = 35
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: restrained: color for actions, links and status only

## D-0020 · dials.warmth = 45
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: near-neutral gray; formal but not cold

## D-0021 · raw.brandColor = "#075c63"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: a deep teal of our own (not another service's identity); 7.7:1 with white

## D-0022 · raw.flags.brandExact = true
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: the teal is the button fill exactly; it already carries white text at AAA
- previous value: false

## D-0023 · raw.contrastTarget = "AAA"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: 7:1 text everywhere (WCAG 2.2 SC 1.4.6)
- previous value: "AA"

## D-0024 · raw.textFace = "Atkinson Hyperlegible"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: open face designed for low vision (OFL) instead of any proprietary government face
- previous value: "system"

## D-0025 · raw.spaceUnit = 5
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: 5px unit, a raw input: gives 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 100, 120
- previous value: 4

## D-0026 · raw.minTarget = 48
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: generous targets: every hit area at least 48px

## D-0027 · raw.focusWidth = 3
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: a thicker 3px focus ring

## D-0028 · hooks.H-logo.status = "have"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: council crest supplied by the council
- previous value: "pending"

## D-0029 · hooks.H-icons.status = "not-needed"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: text labels instead of icons
- previous value: "pending"

## D-0030 · hooks.H-illus.status = "not-needed"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: no illustration
- previous value: "pending"

## D-0031 · hooks.H-photo.status = "not-needed"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: no photography
- previous value: "pending"

## D-0032 · hooks.H-type.status = "open-library"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: Atkinson Hyperlegible under the SIL OFL
- previous value: "pending"

## D-0033 · hooks.H-voice.status = "have"
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: none · source_ref: none
- reason: plain-English content guide exists
- previous value: "pending"
