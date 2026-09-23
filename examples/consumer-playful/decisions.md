# Decisions

Append-only, ADR-style (spec 7.9): one entry per decision, newest last. A later entry for the same path supersedes an earlier one; nothing is edited or deleted. set_by is chosen, confirmed_default, auto_default, assumed, delegated, reference or asset.

## D-0001 · init with defaults
- set_by: auto_default · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: Start of the design system; every default traces to references/levers.json.

## D-0002 · summary = "An expressive, rounded, colorful system for a fictional habit app shared between friends."
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: the one-line brief
- previous value: ""

## D-0003 · context.product = "A habit tracker where friends cheer each other on."
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: product brief
- previous value: ""

## D-0004 · context.audience = "Casual users on phones, a few minutes a day, many first-time visitors."
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: Q-aud-01 conversation
- previous value: ""

## D-0005 · answers.Q-scope-06 = ["Today feed:experience", "Onboarding and store pages:persuade", "Settings:operate"]
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: surfaces and their modes
- also set: context.surfaces = [{"name": "Today feed", "mode": "Experience"}, {"name": "Onboarding and store pages", "mode": "Persuade"}, {"name": "Settings", "mode": "Operate"}] (from Q-scope-06)
- also set: raw.productType = "marketing" (from Q-scope-06)
- also set: raw.marketingSurfaces = true (from Q-scope-06)

## D-0006 · context.memorable = "The streak celebration."
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: Q-brand-02
- previous value: ""

## D-0007 · context.scope = {"in": ["iOS app", "Android app", "web app", "marketing pages"], "out": ["watch", "TV"]}
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: scope
- previous value: {"in": [], "out": []}

## D-0008 · principles = ["Celebrate progress, never shame a miss.", "Big, friendly targets for thumbs.", "One joyful moment per screen, not ten."]
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: ranked principles
- previous value: []

## D-0009 · macros = ["playful", "friendly"]
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: Q-brand-01: playful and friendly; explicit dials below win where set
- previous value: []

## D-0010 · answers.Q-aud-01 = "large"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: occasional, mobile users
- also set: dials.density = 15 (from Q-aud-01)

## D-0011 · answers.Q-plat-01 = ["ios", "android", "web"]
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: phone-first with a web companion
- also set: raw.platforms = ["ios", "android", "web"] (from Q-plat-01)

## D-0012 · raw.inputs = ["touch", "pointer"]
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: touch first
- previous value: ["pointer", "touch"]

## D-0013 · dials.expression = 82
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: expressive: hero moments, visible containers, springs throughout

## D-0014 · dials.brandPresence = 70
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: brand-led surfaces; navigation and sheets stay native

## D-0015 · dials.density = 25
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: spacious: 16px body, 48px default controls
- previous value: 15

## D-0016 · dials.energy = 80
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: energetic: springy (damping 0.76), durations x1.12, heavier headings

## D-0017 · dials.roundness = 97
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: pill controls, 24px cards

## D-0018 · dials.depth = 62
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: soft shadow ladder for cards and sheets

## D-0019 · dials.colorfulness = 85
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: expressive scheme with three accents and tinted containers

## D-0020 · dials.warmth = 78
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: warm neutrals and sentence case

## D-0021 · raw.brandColor = "#ff5a36"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: coral: warm and energetic

## D-0022 · raw.textFace = "Nunito"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: rounded open face (OFL) matching Roundness 81+
- previous value: "system"

## D-0023 · raw.productType = "content"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: a content app: 16px body in the comfortable band
- previous value: "marketing"

## D-0024 · raw.marketingSurfaces = true
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: store pages and onboarding need display sizes
- previous value: true

## D-0025 · hooks.H-logo.status = "have"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: wordmark and symbol exist
- previous value: "pending"

## D-0026 · hooks.H-appicon.status = "commissioning"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: designer brief sent for layered 1024px icon
- previous value: "pending"

## D-0027 · hooks.H-illus.status = "commissioning"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: character illustrations for empty and success states
- previous value: "pending"

## D-0028 · hooks.H-motion.status = "commissioning"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: Lottie streak celebration
- previous value: "pending"

## D-0029 · hooks.H-icons.status = "open-library"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: Phosphor (MIT), rounded weight
- previous value: "pending"

## D-0030 · hooks.H-type.status = "open-library"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: Nunito under the SIL OFL
- previous value: "pending"

## D-0031 · hooks.H-voice.status = "placeholder"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: draft: casual, encouraging, contractions
- previous value: "pending"

## D-0032 · answers.Q-color-04 = "three"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: friends' streaks use three accents around the coral
- also set: raw.accentCount = 3 (from Q-color-04)
- also set: raw.accentHarmony = "triadic" (from Q-color-04)

## D-0033 · answers.Q-color-20 = "overlay"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: state layers keep hover and press visible on every colorful fill
- also set: raw.stateMethod = "overlay" (from Q-color-20)

## D-0034 · answers.Q-depth-04 = "control-layer"
- set_by: chosen · locked: no · date: 2026-09-24 · supersedes: none · source_ref: none
- reason: glass only on the iOS tab bar and toolbars, never on content
- also set: raw.glass = true (from Q-depth-04)
