# V1b verification: standards, platform values, benchmark defaults, studies and funding

Verifier V1b, fresh context, 2026-09-24 (01:35-01:56 IST). Every claim below was located in the repo, then checked against the live official page (or the platform's own source code where the page renders only with JavaScript). Sources are logged as `S-V1b-001` to `S-V1b-091` in [`traces/V1-trace.md`](../traces/V1-trace.md). Nothing in the research, spec or docs was edited; this file lists the fixes for the owners to make.

## Result

| Verdict | Count |
|---|---|
| Confirmed | 69 |
| Partly right | 8 |
| Wrong | 4 |
| Unverifiable | 2 |
| **Total claims checked** | **83** |

"Confirmed" means the official source says the same thing today. "Partly right" means the core is right but a detail, date or attribution is off. Line numbers are from the working tree on 2026-09-24.

How the checks were made:
- Apple HIG pages were read through their DocC JSON (`developer.apple.com/tutorials/data/design/...json`).
- Material pages were read in a browser tab. Compose values were cross-checked in the androidx source.
- WCAG, DTCG, Sanity and several funding pages were parsed from raw HTML. The WebFetch summarizer got two facts wrong: it said DTCG shadows have no `inset`, and it garbled Sanity's accessibility numbers. Numbers were therefore always taken from the raw page.
- Perplexity was unavailable (quota error, S-V1b-028).

## Claims checked

### Design tokens (DTCG)

| # | Claim (as written) | Where | Verdict | Correct statement or note | Source |
|---|---|---|---|---|---|
| 1 | DTCG Format 2025.10 is the stable version, published 28 Oct 2025 | docs/FAQ.md:68; synthesis/OPENDESIGNER-SPEC.md:517; docs/SPEC.md:519; research/L05-icons-imagery-dataviz.md:228; README.md:147 | confirmed | "Final Community Group Report, 28 October 2025". It is a Community Group report, not a W3C Standard, which the repo's wording respects | S-V1b-002 |
| 2 | The Color and Resolver modules are also 2025.10 (same date). Modes live in the Resolver (sets, modifiers, contexts, resolution order), not in the Format module | research/L01-color.md:485, :576; synthesis/OPENDESIGNER-SPEC.md:517; docs/FAQ.md:68 | confirmed | Both are Final CG Reports of 28 Oct 2025 | S-V1b-003, S-V1b-004 |
| 3 | A color `$value` is an object {colorSpace, components, alpha?, hex?} with 14 color spaces. A plain hex string is not valid | research/L01-color.md:20, :114, :489 | confirmed | | S-V1b-003 |
| 4 | Composite types: typography = fontFamily, fontSize, fontWeight, letterSpacing, lineHeight (a number multiplier). There is a gradient composite and shadow has an optional `inset`. Dimension units are px and rem only; fontWeight is 1-1000 | research/L02-typography.md:22, :133, :531; research/L01-color.md:469; research/L04-shape-depth-motion.md:672; research/L03-space-layout.md:508 | confirmed | | S-V1b-002 |
| 5 | DTCG has no spring type, in either 2025.10 or the Sept 2026 draft | research/L04-shape-depth-motion.md:12, :479, :606, :693 | confirmed | The draft checked is the 8 Sep 2026 Draft CG Report | S-V1b-002, S-V1b-090 |
| 6 | "The Sept 2026 draft keeps this and adds that px equals Android dp and iOS pt, and translators SHOULD convert" | research/L03-space-layout.md:508 | partly right | The px = dp / pt note and the SHOULD-convert sentence are already in the 2025.10 Final report. The draft keeps them; it does not add them | S-V1b-002, S-V1b-090 |
| 7 | "open Issue 102 on lineHeight type" | research/L02-typography.md:582 | partly right | Issue 102 in 2025.10 is "Typography type feedback", which covers the whole typography type, not lineHeight alone | S-V1b-002 |

### Accessibility (WCAG, APCA)

| # | Claim | Where | Verdict | Correct statement or note | Source |
|---|---|---|---|---|---|
| 8 | WCAG 3 is still a Working Draft (10 Sep 2026). Its contrast method is to be determined and APCA is not named | research/L01-color.md:20; synthesis/LEVERS.md:249; docs/FAQ.md:187; synthesis/OPENDESIGNER-SPEC.md:695 | confirmed | "W3C Working Draft 10 September 2026"; "The contrast algorithm used in WCAG 3 is yet to be determined". APCA appears 0 times in the draft | S-V1b-005 |
| 9 | 2.4.11 Focus Not Obscured (Minimum) is AA; 2.4.12 is AAA | research/L04-shape-depth-motion.md:16, :192, :671; research/L10-platforms.md:253 | confirmed | | S-V1b-006 |
| 10 | 2.4.13 Focus Appearance is AAA: a 2 CSS px perimeter and a 3:1 change | research/L04-shape-depth-motion.md:16; research/L08-components-patterns.md:238; research/L01-color.md:313 | confirmed | | S-V1b-006 |
| 11 | 2.5.8 Target Size (Minimum) is AA: 24x24 CSS px, with a spacing exception based on a 24 px circle | synthesis/LEVERS.md:355; research/L03-space-layout.md:268, :285; research/L08-components-patterns.md:176; docs/FAQ.md:184; docs/HOW-IT-WORKS.md:157 | confirmed | | S-V1b-006 |
| 12 | 2.5.5 Target Size (Enhanced) is AAA: 44x44 CSS px | research/L03-space-layout.md:269; research/L08-components-patterns.md:176 | confirmed | | S-V1b-006 |
| 13 | 1.4.11 Non-text Contrast is AA at 3:1, and inactive components are exempt | synthesis/LEVERS.md:247; research/L01-color.md:313, :421; research/L08-components-patterns.md:225 | confirmed | | S-V1b-006 |
| 14 | 1.4.3 requires 4.5:1, or 3:1 for large text (18pt, or 14pt bold, about 24px / 18.66px). Ratios are not rounded, so 4.499:1 fails | synthesis/LEVERS.md:247; research/L01-color.md:412 | confirmed | | S-V1b-006, S-V1b-007 |
| 15 | 2.3.3 is AAA; 3.3.7 Redundant Entry is A; 3.3.8 Accessible Authentication is AA; 3.2.6 Consistent Help is A; 3.3.4 is AA; 3.1.5 is AAA | research/L04-shape-depth-motion.md:16; research/L13-ux-laws-heuristics.md:231, :283, :338, :428; research/L08-component-catalog.md:252 | confirmed | L13 tags 3.3.4 and 3.1.5 as [inferred]. S-V1b-006 can replace those tags | S-V1b-006 |
| 16 | APCA levels: Lc 90 preferred body, 75 minimum body, 60 other text, 45 large text, 30 placeholder and disabled, 15 non-text | synthesis/LEVERS.md:249; research/L01-color.md:414 | confirmed | These come from the method's author (Tier B), not a W3C standard, as the repo says | S-V1b-084, S-V1b-085 |

### Apple

| # | Claim | Where | Verdict | Correct statement or note | Source |
|---|---|---|---|---|---|
| 17 | Control sizes, default / minimum: iOS 44x44 / 28x28 pt; macOS 28 / 20; tvOS 66 / 56; visionOS 60 / 28; watchOS 44 / 28 | research/L03-space-layout.md:266; benchmarks/L09-benchmark-matrix.md:380 | confirmed | | S-V1b-008 |
| 18 | Targets of "at least 44pt on iOS", and 60pt on visionOS | synthesis/LEVERS.md:355; docs/FAQ.md:184; docs/HOW-IT-WORKS.md:157 | confirmed | The Buttons page says "a button needs a hit region of at least 44x44 pt — in visionOS, 60x60 pt". The Accessibility page calls 44 the default and 28 the minimum control size | S-V1b-010, S-V1b-008 |
| 19 | tvOS targets: 66 default, 56 minimum; LEVERS gives "56-66 for remote and gaze" | research/L03-space-layout.md:266; synthesis/LEVERS.md:355 | confirmed | visionOS's 60 falls inside that range | S-V1b-008 |
| 20 | Text sizes, default / minimum: iOS 17/11, macOS 13/10, tvOS 29/23, visionOS 17/12, watchOS 16/12 | research/L02-typography.md:200, :205, :405; synthesis/LEVERS.md:260 | confirmed | | S-V1b-008, S-V1b-009 |
| 21 | Dynamic Type has 7 standard and 5 accessibility sizes. Body goes 14 / 17 / 23 / 53 and Large Title 31 / 34 / 40 / 60; "Dynamic Type (12 sizes)" | research/L02-typography.md:419, :423; benchmarks/L09-benchmark-matrix.md:316 | confirmed | | S-V1b-009 |
| 22 | iOS 26.1 added a Clear or Tinted Liquid Glass option ("press-reported") | research/L04-shape-depth-motion.md:14, :304, :650, :678; benchmarks/L09-benchmark-matrix.md:652 | confirmed | Apple's own "About iOS 26 Updates" page now states it: "choose between the default clear look or a new tinted look which increases opacity". The "press-reported" caveat can go | S-V1b-021 |
| 23 | iOS 27 adds a transparency slider "from ultraclear to fully tinted", plus "more uniform refraction and improved contrast" | research/L04-shape-depth-motion.md:304; benchmarks/L09-benchmark-matrix.md:14; research/L03-space-layout.md:399 | confirmed | | S-V1b-018, S-V1b-019 |
| 24 | The `UIDesignRequiresCompatibility` opt-out is ignored when building for iOS, iPadOS, Mac Catalyst, macOS or tvOS 27 | research/L10-platforms.md:12, :19, :96 | confirmed | Quoted verbatim from Apple's documentation | S-V1b-016 |
| 25 | All six OS 27 releases shipped on 14 Sep 2026 | benchmarks/L09-benchmark-matrix.md:14, :28, :62 | confirmed | | S-V1b-018 |
| 26 | Apple's HIG moves brand color into the content layer (Branding page, updated Sep 2026) | research/L06-brand-voice.md:639; research/L10-platforms.md:123; synthesis/LEVERS.md:56 | confirmed | Change log, 9 Sep 2026: "Refined guidance for using brand color". The page says to consider "moving it into the content layer, where it scrolls beneath Liquid Glass controls" | S-V1b-012, S-V1b-088 |
| 27 | Liquid Glass stays out of the content layer; add a 35% dark dimming layer under clear glass over bright content; Liquid Glass "has no inherent color" | research/L04-shape-depth-motion.md:303, :316; research/L01-color.md:397; synthesis/LEVERS.md:292 | confirmed | | S-V1b-013 |
| 28 | The HIG Materials change log still ends at 2025-09-09 | research/L04-shape-depth-motion.md:650 | confirmed | | S-V1b-013 |
| 29 | HIG dates: latest What's New entry 2026-09-18; WWDC 2026-06-08; Liquid Glass added 2025-06-09 | benchmarks/L09-benchmark-matrix.md:62 | confirmed | | S-V1b-088, S-V1b-014 |

### Material and Android

| # | Claim | Where | Verdict | Correct statement or note | Source |
|---|---|---|---|---|---|
| 30 | M3 type scale: Display L/M/S 57/64, 45/52, 36/44; Body Large 16/24; Body Medium 14/20 | research/L02-typography.md:49, :62; benchmarks/L09-benchmark-matrix.md:155 | confirmed | | S-V1b-025 |
| 31 | Material uses the Major Second scale (1.125) with a base of 14, the smallest ratio in the benchmark | research/L02-typography.md:63, :215; synthesis/LEVERS.md:443; synthesis/OPENDESIGNER-SPEC.md:691; docs/SPEC.md:693 | confirmed | | S-V1b-024 |
| 32 | "14 x 1.125^n rounds to 16, 22, 28, 32, 36, 45, 57 ... exactly Material's sizes" | research/L02-typography.md:19, :215 | **wrong** | 14 x 1.125^12 = 57.54, which rounds to 58. The formula gives 16, 22, 28, 32, 36, 45 and 58. Material's 57 is off-formula by 1, like its 24. LEVERS.md:444 already says this | S-V1b-025 + arithmetic |
| 33 | Breakpoints were renamed from "window size classes" in May 2026, with five ranges: <600, 600-839, 840-1199, 1200-1599 and 1600+ dp | research/L10-platforms.md:36, :227; research/L03-space-layout.md:21, :302, :578; research/L14-device-practices.md:63 | confirmed | The page says "A breakpoint (previously window size class)" and lists these ranges. It prints no date. The May date is supported by the I/O 2026 post (19 May 2026), which lists updated Breakpoints guidance, and by the Wayback Machine, whose first capture of /breakpoints is 21 May 2026. The old URL returned 404 by July | S-V1b-027, S-V1b-086, S-V1b-030 |
| 34 | System spacing tokens `md.sys.measurement.space0` to `space900` (0-72dp), with space100 = 8dp, in Compose only | research/L03-space-layout.md:21, :29, :592; benchmarks/L09-benchmark-matrix.md:187 | confirmed | There are 18 tokens: 0, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 32, 36, 40, 48, 56, 64, 72. The availability table marks Jetpack Compose "Available" and MDC-Android and Web "Unavailable" | S-V1b-033, S-V1b-034 |
| 35 | Springs. Standard spatial: 0.9 damping at 1400 / 700 / 300 stiffness. Expressive spatial: 0.6/800, 0.8/380, 0.8/200. Effects: 1.0 at 3800 / 1600 / 800 | research/L04-shape-depth-motion.md:11, :418, :419; synthesis/LEVERS.md:85, :300, :326; benchmarks/L09-benchmark-matrix.md:283, :670 | confirmed | Values taken from androidx `StandardMotionTokens` and `ExpressiveMotionTokens` | S-V1b-026 |
| 36 | M3 shape scale: 0, 4, 8, 12, 16, 20, 28, 32, 48, full. Expressive adds 20 / 32 / 48 | benchmarks/L09-benchmark-matrix.md:219, :670 | confirmed | | S-V1b-089 |
| 37 | Compose Material3 1.4.0 is stable and 1.5.0-alpha28 is current; the Expressive APIs are graduating in the 1.5.0 alphas | benchmarks/L09-benchmark-matrix.md:61, :651; research/L10-platforms.md:35; research/L03-space-layout.md:183 | partly right | 1.4.0 (24 Sep 2025) is stable and the Expressive APIs are graduating in the 1.5.0 alphas. But the latest alpha is now **1.5.0-alpha29** (23 Sep 2026) | S-V1b-035 |
| 38 | M3 Expressive launched 2025-05-13; the I/O 2026 update was 2026-05-19; Material Android is Compose-first | benchmarks/L09-benchmark-matrix.md:13, :61 | confirmed | The 13 May 2025 date comes from press reports (Tier B) | S-V1b-087, S-V1b-086 |
| 39 | Android 15 enforces edge-to-edge for apps targeting SDK 35. At SDK 36 the opt-out is disabled on Android 16 | research/L03-space-layout.md:409, :594; research/L10-platforms.md:12, :20, :244 | confirmed | | S-V1b-036, S-V1b-037 |
| 40 | At SDK 36, orientation, resizability and aspect-ratio locks are ignored on screens with smallest width 600dp or more. The opt-out ends at API 37 (Android 17) | research/L03-space-layout.md:411, :594; research/L10-platforms.md:12, :75, :235 | confirmed | | S-V1b-036, S-V1b-038 |
| 41 | Android 16 turns on predictive back by default | research/L10-platforms.md:12 | confirmed | Applies to apps targeting API 36 | S-V1b-036 |

### Other design systems and guidelines

| # | Claim | Where | Verdict | Correct statement or note | Source |
|---|---|---|---|---|---|
| 42 | GOV.UK Frontend 6.0.0 (2026-02-09) sets body text to 19px (19/25) at every breakpoint and removes size 14 | benchmarks/L09-benchmark-matrix.md:15, :668; synthesis/LEVERS.md:333 | confirmed | The latest release is v6.5.1 (14 Sep 2026) | S-V1b-039, S-V1b-040, S-V1b-041 |
| 43 | Carbon v12 radius tokens: 0 / 2 / 4 / 8 / 16 / 24 / max (999999px), behind `enable-v12-release`. Inputs and tags go to 4px (small tags 2px); menus 8 / 4 | research/L04-shape-depth-motion.md:34, :44, :80, :128, :648; benchmarks/L09-benchmark-matrix.md:19, :222; synthesis/LEVERS.md:105 | confirmed | | S-V1b-042, S-V1b-043, S-V1b-045 |
| 44 | "radius tokens ... in its v12 beta (Sept 2026)" and "IBM Carbon v12 (in beta, ...)" | research/L04-shape-depth-motion.md:10, :34 | partly right | There is no v12 beta release. v12 behavior ships inside v11 releases behind the `enable-v12-release` flag. The latest release is v11.117.0 (23 Sep 2026), and npm's `beta` tag is a stale 0.1.0. Write "behind the v12 feature flag (unreleased)", as L04:648 and L09:19 already do | S-V1b-044, S-V1b-046 |
| 45 | NHTSA's voluntary 2013 guidelines: glances away of 2 s or less, 12 s or less in total, and a 1.5 s occlusion test | research/L14-device-practices.md:23, :92, :140, :224 | confirmed | | S-V1b-047 |
| 46 | L09 spacing: 17 of 22 published scales contain 4, 8, 12, 16, 24, 32, 40, 48, 64 | benchmarks/L09-benchmark-matrix.md:213, :669; synthesis/QUESTIONNAIRE.md:1916 | confirmed | A recount of L09's own table gives 17 of 22. Spot-checked rows for Material, Carbon, Atlassian (8px base), Tailwind and Ant against their sources; all match | S-V1b-034, S-V1b-043, S-V1b-080, S-V1b-081, S-V1b-073 |
| 47 | "Fluent (no 64), Blade (no 64) and Ant (no 40 or 64) miss only upper steps" | benchmarks/L09-benchmark-matrix.md:213 | partly right | Fluent 2's spacing ramp stops at 32 px (`xxxl`), so it lacks 40, 48 and 64, not only 64. The 17-of-22 count does not change | S-V1b-074 |
| 48 | "a 4px base with the ladder 4 ... 64 plus 0 and 2, in 17 of 22 systems" | synthesis/ONTOLOGY.md:674 | **wrong** | 17 of 22 contain the 4-64 ladder, but only 13 of the 22 declare a 4px base. Material, Carbon, Atlassian, USWDS and Airbnb are 8-based; Spectrum and Mantine have no single base; GOV.UK uses 5 and Encore 16. Several scales (for example SLDS and Radix) have no 0 or 2 step | L09 table M5; S-V1b-080, S-V1b-043, S-V1b-034 |
| 49 | The median default control radius is 6px | benchmarks/L09-benchmark-matrix.md:245, :451; synthesis/LEVERS.md:21, :102; docs/GLOSSARY.md:161, :1870; docs/SPEC.md:681 | confirmed | A recount of L09 table M6 gives 23 values (SLDS counted once per theme) with a median of 6, and 16 of 23 at 4, 6 or 8. Spot-check: Ant 6, Primer 6, Atlassian 6, Fluent 4 and USWDS 4 all match their sources | S-V1b-073, S-V1b-078, S-V1b-079, S-V1b-074, S-V1b-077 |
| 50 | Light and dark ship together in 21 of 25 systems | benchmarks/L09-benchmark-matrix.md:341, :450; synthesis/ONTOLOGY.md:471; synthesis/QUESTIONNAIRE.md:936 | confirmed (spot-check, not a full recount) | Primer and Fluent ship dark themes. GOV.UK Frontend and USWDS have no `prefers-color-scheme` code [inferred from absence] | S-V1b-078, S-V1b-074, S-V1b-083 |

### Studies and surveys

| # | Claim | Where | Verdict | Correct statement or note | Source |
|---|---|---|---|---|---|
| 51 | The zeroheight Design Systems Report 2026 has n=147 | research/L17-how-systems-get-made.md:184, :945 | confirmed | | S-V1b-048 |
| 52 | 61% of teams are understaffed | research/L11-process-governance.md:13; research/L17-how-systems-get-made.md:184 | confirmed | 39% have enough people and 61% do not. A separate claim at L17:19 and L11:430, "61% have five or fewer people", is also right (28% + 33%) | S-V1b-048 |
| 53 | Satisfaction with leadership buy-in fell from 42% to 32% | research/L11-process-governance.md:13, :594 | confirmed | | S-V1b-048 |
| 54 | Lack of mandate (73%) is the biggest barrier to adoption | research/L11-process-governance.md:14, :477 | confirmed | Strictly, it is the top reason people give for their system *not* being well adopted | S-V1b-048 |
| 55 | 56% name resourcing as their top challenge | research/L11-process-governance.md:13 | confirmed | | S-V1b-048 |
| 56 | Team sizes: "1-2 people 28%, 3-5 33%, 6-10 25%, 10+ 12%" | research/L17-how-systems-get-made.md:184 | **wrong** | The report gives 10-15 people 6%, 16-20 4% and 20+ 4%, so more than 10 people is **14%**, not 12% | S-V1b-048 |
| 57 | 48% of teams already run an MCP server | research/L11-process-governance.md:15, :405 | confirmed | This figure is from zeroheight's separate *State of AI in Design Systems 2026* (123 respondents), not the n=147 report. The repo cites it correctly (S-L11-031) | S-V1b-049 |
| 58 | Sanity's evals: Sonnet 4.6 went from 20% to 90%, Haiku from 3% to 47% and Opus from 40% to 100%. Accessibility violations per iteration fell from 5.1 to 0.6 | research/L11-process-governance.md:368, :406; research/L08-components-patterns.md:398 | confirmed | | S-V1b-050 |
| 59 | "JSON-structured docs plus 3 MCP tools took Sonnet 4.6 from 20% to 90% task success; retrievable code examples helped most, lint less" | research/L18-ai-first-distribution.md:188 | partly right | The 20% to 90% came from the new JSON docs alone ("New Sanity UI + docs"). Adding code chunks raised Sonnet to 93%, and chunks plus lints to 100%. The ranking of the tools is right: chunks best, lint "spotty", the wizard worst | S-V1b-050 |
| 60 | The Zeigarnik effect failed a 2025 meta-analysis of 59 studies, but people do tend to resume unfinished tasks | research/L13-ux-laws-heuristics.md:17, :69 | partly right | Ghibellini and Meier, *Humanities and Social Sciences Communications*, 1 Jul 2025, analyzed **59 publications**. 39 of them studied the Zeigarnik effect (38 alone, 1 with both effects) and 21 the Ovsiankina effect. The findings are as stated. The evidence can now cite the article itself rather than a snippet and Wikipedia | S-V1b-053 |

### Funding (docs/SPONSORSHIP.md)

| # | Claim | Where | Verdict | Correct statement or note | Source |
|---|---|---|---|---|---|
| 61 | GitHub Sponsors supports India. It takes 0% from personal accounts and up to 6% from organizations (invoicing saves 3%). Payment goes through Stripe Connect to a bank; W-8BEN and 2FA are needed; payouts come within 30 days after month end | docs/SPONSORSHIP.md:31, :50, :149 | confirmed | Two details to add: the first payout comes 60 days after the first sponsorship, and Stripe Connect payouts go out on the 22nd "regardless of the amount of the balance" | S-V1b-054, S-V1b-055, S-V1b-057, S-V1b-058 |
| 62 | FOSS United grants go up to ₹15L, with a median of ₹3-7L over a year. It says "we do not fund ideas", looks at the person first, asks about users, and takes applications as funding.json | docs/SPONSORSHIP.md:17, :32, :70 | confirmed | | S-V1b-059 |
| 63 | FOSS United's 2026 fellowships ran from ₹16.5k to ₹6L, including a ₹1.8L fellowship for design work | docs/SPONSORSHIP.md:32, :71 | confirmed | The ₹1.8L fellowship is for "improving design across the open source ecosystem" | S-V1b-060 |
| 64 | FOSS United fellowships have "no formal call; use the general form" | docs/SPONSORSHIP.md:71 | unverifiable | The fellowship page lists grantees but shows no application route or call | S-V1b-060 |
| 65 | Cline runs a $1M program that pays $1k-$10k in credits, reviewed on a rolling basis | docs/SPONSORSHIP.md:33, :107 | confirmed | The blog also says "Solo developers, small teams ... are exactly the kinds of projects we want to support", which settles the open item at SPONSORSHIP.md:240 | S-V1b-063, S-V1b-062 |
| 66 | OpenAI Codex for Open Source gives 6 months of ChatGPT Pro with Codex, API credits and conditional Codex Security. It says "apply anyway and explain why", and it is open | docs/SPONSORSHIP.md:33, :90 | confirmed | | S-V1b-064 |
| 67 | Vercel OSP gives $3,600 in credits over 3 years plus a starter pack. It is closed now; windows open four times a year; the summer window ended 13 Sep; the Spring 2026 cohort included agent-skill repos | docs/SPONSORSHIP.md:34, :95 | confirmed | The $3,600 is spread over 3 years. "Four times a year" is how often applications open, not a quarterly credit | S-V1b-065, S-V1b-066, S-V1b-068 |
| 68 | Emergent Ventures is rolling, open to individuals, has "dedicated support" for India-focused projects, and states no amount | docs/SPONSORSHIP.md:35, :137, :238 | confirmed | The same line covers Africa and the Caribbean, and Ukraine | S-V1b-069 |
| 69 | Emergent Ventures lets applicants choose India "in the region menu" | docs/SPONSORSHIP.md:224 | unverifiable | The application form was not opened, because that would mean entering data | n/a |
| 70 | Claude for Open Source gives 6 months of Claude Max 20x. Its tracks include 100+ merged PRs to other people's repos and 20+ outside contributors in 12 months; there is a 10,000-recipient cap | docs/SPONSORSHIP.md:39, :91, :177 | confirmed | | S-V1b-070, S-V1b-071 |
| 71 | FLOSS/fund excludes very new projects and gives a $10k minimum, then multiples of $25k, up to $100k a year, reviewed quarterly | docs/SPONSORSHIP.md:17, :38, :73 | confirmed | | S-V1b-072 |
| 72 | "The repo is private, has 0 stars" | docs/SPONSORSHIP.md:17 | **wrong** | The repo is **public** (still 0 stars) as of 24 Sep 2026 | S-V1b-001 |

### Numbers the README and docs present as fact (checked against the repo's own files)

| # | Claim | Where | Verdict | Correct statement or note | Source |
|---|---|---|---|---|---|
| 73 | 352 Decision Cards, 18 research lanes and 2,740 logged sources | README.md:71, :176-178; docs/FAQ.md:16 | confirmed | `jev_nav.py` reports 352 cards and 2,740 source ids; 18 lanes are done | S-V1b-091 |
| 74 | 25 systems benchmarked, with 12 dimension tables | README.md:179 | confirmed | Tables M1-M12; 25 files in `benchmarks/systems/` | S-V1b-091 |
| 75 | 192 questions on 27 screens, ordered by a graph of 352 decisions and 465 dependencies | README.md:180; docs/HOW-IT-WORKS.md:38, :67 | confirmed | S00 (the reference panel) is not a screen, so S01-S27 make 27 screens | S-V1b-091 |
| 76 | The ontology has 271 nodes in 10 layers | README.md:100; docs/HOW-IT-WORKS.md:42 | confirmed | | S-V1b-091 |
| 77 | 207 design-system blocks, classed 135 generatable, 31 tool-assisted, 29 owner input, 7 designer-owned, 5 extractable | docs/HOW-IT-WORKS.md:44-52; research/L17-how-systems-get-made.md:14 | partly right | L17 counted 207 blocks from ONTOLOGY.md on 23 Sep. Today `synthesis/ontology.json` has **211** non-builder leaf blocks. Its own `provenance` tags give 156 generatable, 30 designer-owned, 23 tool-assisted and 2 extractable, with no owner-input class. The two classifications disagree | S-V1b-091 |
| 78 | 14 asset hooks | README.md:101; docs/HOW-IT-WORKS.md:93 | confirmed | `hooks.json` has 14 asset hooks and 5 tool hooks | S-V1b-091 |
| 79 | 393 glossary terms, 25 passing tests and 8 visual templates | README.md:202, :204, :205 | confirmed | The tests were run: 25 pass | S-V1b-091 |
| 80 | The dials were tested on 13 systems and match 6 outright: Apple HIG, Fluent 2, Primer, GOV.UK, shadcn/ui and Blade | README.md:141; docs/HOW-IT-WORKS.md:112 | confirmed | These 6 have grade A in the LEVERS recipe table | S-V1b-091 |
| 81 | Personality shapes 15 decisions and platforms shape 12 | docs/HOW-IT-WORKS.md:71; docs/FAQ.md:120 | confirmed | These are the graph's out-degrees | S-V1b-091 |
| 82 | The Quick, Standard and Expert tags cover 10, 92 and 191 questions | docs/HOW-IT-WORKS.md:67 | confirmed | Cumulative: 10; 10 + 82 = 92; 92 + 99 = 191; one question is tagged "Any" | S-V1b-091 |
| 83 | Material spacing: new component token naming (padding, gap, margin, with positional words) | research/L03-space-layout.md:592 | confirmed | | S-V1b-034 |

## Corrections to make, by file

The owners of each file should make these edits. Generated copies (`data/`, `skills/*/references/`, `.claude/`, `.agents/`) follow from the sources after `python3 tools/build_data.py`.

**research/L02-typography.md**
- :19 and :215: replace "rounds to 16, 22, 28, 32, 36, 45, 57 ... exactly Material's sizes". The correct text is: 14 x 1.125^n rounds to 16, 22, 28, 32, 36, 45 and 58. Material's 57 (and 24) are off-formula by 1.
- :582: Issue 102 is "Typography type feedback" on the whole composite, not a lineHeight issue.

**research/L03-space-layout.md**
- :508: the px = dp / pt equivalence and the SHOULD-convert sentence are already in 2025.10. The Sept 2026 draft keeps them.

**research/L04-shape-depth-motion.md**
- :10 and :34: change "v12 beta" / "in beta" to "behind the `enable-v12-release` flag (unreleased; latest release v11.117.0)".
- :14, :304, :650 and :678: the iOS 26.1 Clear/Tinted option is now confirmed on Apple's own page (support.apple.com/en-us/123075). Drop "press-reported".

**benchmarks/L09-benchmark-matrix.md**
- :61 and :651: the current alpha is 1.5.0-alpha29 (2026-09-23).
- :213: Fluent 2 lacks 40, 48 and 64, not only 64.

**research/L13-ux-laws-heuristics.md**
- :17 and :69: "59 studies" should be "59 publications (39 on the Zeigarnik effect, 21 on Ovsiankina)". Cite the article (nature.com/articles/s41599-025-05000-w, 1 Jul 2025).
- :338 and :428: the [inferred] tags on 3.3.4 (AA) and 3.1.5 (AAA) can cite the WCAG 2.2 Recommendation.

**research/L17-how-systems-get-made.md**
- :184: "10+ 12%" should be "more than 10 people: 14% (10-15 6%, 16-20 4%, 20+ 4%)".
- :14 (and the classification section): re-count against the current `ontology.json` (211 non-builder leaves), or state the date and source of the 207 count.

**research/L18-ai-first-distribution.md**
- :188: say that the JSON docs alone took Sonnet 4.6 from 20% to 90%, that chunks raised it to 93%, and that chunks plus lints raised it to 100%.

**research/L11-process-governance.md** (optional)
- :14: "lack of mandate (73%)" is the top reason systems are *not* well adopted. It is fine as written, but "barrier" could be made that specific.

**synthesis/ONTOLOGY.md**
- :674: replace "a 4px base ... plus 0 and 2, in 17 of 22 systems" with: "the ladder 4, 8, 12, 16, 24, 32, 40, 48, 64 appears in 17 of 22 published scales; 13 of 22 use a 4px base".

**docs/HOW-IT-WORKS.md**
- :44-52: the 207 and 135/31/29/7/5 counts come from L17's classification and do not match `ontology.json`'s own `provenance` tags (211 leaves: 156/30/23/2, no owner-input class). Say which classification the docs use, or reconcile the two. README.md:100 lists the same five classes.

**docs/SPONSORSHIP.md**
- :17: the repo is public now. Keep "0 stars".
- :31 / :50: add that the first GitHub Sponsors payout comes 60 days after the first sponsorship, and that Stripe Connect payouts go out on the 22nd whatever the balance.
- :231: resolved. There is no minimum payout for Stripe Connect (Additional Terms 3.3).
- :240: resolved. Cline's blog names solo developers as a target.

## Unverifiable, and left to V1a

- **Unverifiable here:**
  - The route for FOSS United fellowships (no call or form shown on the fellowship page).
  - Emergent Ventures' region menu (the form was not opened).
  - Vercel's next window date (still not published).
  - The size of an Emergent Ventures grant (still not stated).
- **Material height classes:** the 480 / 900 dp values (L10:227, L03:302) were not visible in the text of the breakpoints page. They were not re-checked.
- **Tool and host claims in the docs, left to V1a (platforms and tools):**
  - Custom GPT retirement on 11 Dec 2026 (docs/FAQ.md:96).
  - Claude Design's launch (docs/FAQ.md:130).
  - Figma's DTCG import limits (docs/FAQ.md:74).
  - "roughly 46 clients" that read Agent Skills (synthesis/OPENDESIGNER-SPEC.md:29).
  - The Android 48dp target and the 76dp target in cars (synthesis/LEVERS.md:355).
