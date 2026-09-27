---
type: synthesis
title: Design systems and tokens
created: 2026-09-24
updated: 2026-09-27
sources:
  - ADaQuZS04Rc
  - AH_ugxmLeUM
  - HE4rLEQpiXY
  - 7sUUzOCv47U
  - adev-home
  - ek-building-an-animation-course
  - eks-skills-animate-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-audit
  - eks-skills-improve-animations-skill
  - eks-skills-improve-animations-plan-template
  - eks-skills-prototype-skill
  - eks-skills-review-animations-standards
  - eks-skills-ask-sonner-skill
  - sonner-styling
tags:
  - od-area-tokens
---

# Design systems and tokens

## In short

A design system is a small set of decisions (colors, spacing, type sizes, corner radius, motion) that you make once, give names to and reuse everywhere, so every new screen feels familiar and people learn to trust the product. The named values are called tokens: you write `var(--ease-out)` instead of typing `cubic-bezier(0.23, 1, 0.32, 1)` in twenty places. Emil Kowalski's rule, which is a locked house standard, is to build from the tokens a project already has and extend them, never to add a second parallel set and never to hand-type a value that only looks close. Kole Jain explains why it matters: consistency builds trust and speed, the system should be as big as the team needs and no bigger, and you break its rules only on purpose. The practitioner videos give almost no token values; the few they give (a 10px radius, a 1.27 type ratio) come from single videos and are opinions.

## House standards

These apply to every system OpenDesigner builds and cannot be traded away.

- **STD-visual-details-26** (must): build UI from the project's existing tokens (colors, radii, spacing, fonts, easing and duration variables) and extend them when something is missing; never add a parallel set, and never hand-type or approximate a value such as `cubic-bezier(0.4, 0, 0.2, 1)`.
- **STD-visual-details-27** (should): make every spacing, timing and alignment value a deliberate choice you can defend.
- **STD-visual-details-36** (must): things that look the same behave the same and live in the same place.
- **STD-visual-details-51** (should): make a component's default easing, timing and look excellent before adding options.
- **STD-visual-details-25** (must): when prototyping with no project to take tokens from, use a restrained default: neutral grays, one accent color and the system font stack.
- **STD-easing-duration-02** (must): use the strong custom curves `--ease-out: cubic-bezier(0.23, 1, 0.32, 1)` and `--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1)` instead of built-in easings; only the `ease` and `linear` keywords stay allowed.
- **STD-components-toasts-drawers-40** (must): define the drawer curve once as a token, `--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1)`.
- **STD-easing-duration-07** (must): time each UI animation within its element's budget (press 100-160ms, tooltips 125-200ms, dropdowns 150-250ms, modals and drawers 200-500ms on the web).
- **STD-springs-gestures-02** (should): describe springs by damping (or bounce) and response (or duration), not mass, stiffness and damping.
- **STD-process-review-taste-11** (must): before judging or designing motion, map the stack, where motion lives and the existing easing, duration and spring conventions.
- **STD-process-review-taste-10** (should): rate every motion finding HIGH, MEDIUM or LOW; token consolidation is LOW (polish).
- **STD-process-review-taste-20** (must): one fix plan per finding; merge two only when they share every file and the same fix, such as one easing-token swap across components.
- **STD-process-review-taste-49** (must): when a prototype variant is picked, integrate it following the project's conventions, including its token usage.
- **STD-process-review-taste-45** (must): the one exception to "use the project's tokens": the prototype variant picker keeps its own fixed styling and never takes the project's tokens, fonts or colors.
- **STD-components-toasts-drawers-24** (should): build the design system's toast headless with `toast.custom()`, wrapped in your own `toast()` function.

OpenDesigner's own accessibility floors also apply here, although they are not STDs: WCAG 2.2 AA contrast, 24px minimum targets, visible focus and reduced motion are locked (`skills/opendesigner/references/guardrails.md`).

## What the sources teach

### Why a system at all: trust and speed

- A design system is not decoration; it is how users build trust and speed with a product, and the need grows as products get more complex [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]). In Linear, buttons, spacing and text styles are exactly the same in a settings panel and when creating a view [S-L19-044].
- Consistent meaning is part of it: in macOS pop-ups the primary color always marks the non-destructive action, which Kole says he trusts to always be that way [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- The payoff is reuse: because button spacing, type scale and colors were held constant, a new modal is quick to build and every new screen feels familiar even when the content differs [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- A system is judged by the decisions you can stick to, not by how many components it has; "hundreds of components" is not the point [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- Building the system (rules, spacing, type scales, interaction patterns) is often more critical than the design itself, because defining them gives an architecture for expansion [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- Emil Kowalski developed the design system while on Vercel's design team; the animations.dev home page states this as his background, not as guidance [S-L19-002] ([[sources/adev-home-animations-dev|animations.dev]]).

### Size the system to the team

- The system has to reflect the values of the team. A lean startup may need something lightweight, flexible, quick to update and easy to scrap; Google's Material Design is massive and deeply defined because it serves dozens of products and billions of users [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]). The video does not pick one size for everyone [S-L19-054].
- A system is a shared language, not a way to make everything look the same. Mastery includes knowing when to bend a rule: break the system on purpose, never by accident [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).

### What becomes a token

- Kole's working definition of consistency: styles for colors, variables for measurements and components for UI elements [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]). Duplicate components that do the same job (a back and a skip button, two search bars) must match in size, corner radius and style [S-L19-045].
- Give all smaller components one shared corner radius; in his recipe-app fix that is 10px, and he calls it a step most designers miss [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]). The 10px is this app's value; the lasting lesson is one radius for the small parts, as the analysis notes.
- Derive font sizes from a ratio instead of eyeballing one page and building the style guide around it: Kole uses 1.27 (the square root of the golden ratio) from a 16px base [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]). See the [[synthesis/typography|Typography synthesis]] for the full method; it is his personal method, not a standard.
- Motion is part of the token set. The house skills turn three strong curves into tokens (`--ease-out`, `--ease-in-out`, `--ease-drawer`) because built-in CSS easings are too weak [S-L19-018] ([[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]])[S-L19-023][S-L19-033], and they keep curves and durations as shared tokens [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]). Every curve, duration and spring config comes from fixed tables; none is invented or approximated [S-L19-018].
- Emil keeps a larger library of 18 custom easing functions as named CSS custom properties on `:root` for his own animation work; the course article shows six of them (`--ease-breeze`, `--ease-silk`, `--ease-swift`, `--ease-nova`, `--ease-crisp`, `--ease-glide`) [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]). The page gives no reason for the format and does not say where each curve is used. All six shown have both control points below the diagonal, so they start slowly, like ease-in [inferred from the published values].

### Use what is there, extend it, never fork it

- Look first. Recon finds where motion lives (global CSS and tokens such as `--ease-*` and `--duration-*`, the Tailwind config, keyframe definitions) and the existing duration scales and spring configs [S-L19-027] ([[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]]). Opportunity hunts start the same way [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]), and so do prototypes (colors, radii, spacing, fonts, easing and duration variables) [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).
- Extend, don't fork: if `--ease-out` or a duration scale already exists, use it; adding a parallel system is called a defect [S-L19-018] ([[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]). Suggestions and plans must extend existing tokens, not invent parallel ones [S-L19-024][S-L19-027].
- New curves go into the repo's existing token file, and every fix plan names the repo's conventions (token names, file placement, prop patterns) with one exemplar file and line to imitate [S-L19-026] ([[sources/eks-skills-improve-animations-plan-template-emilkowalski-skills-skills-improve-animations-plan-template-md|emilkowalski/skills: skills/improve-animations/PLAN-TEMPLATE.md]]). The template's `src/styles/tokens.css` is a placeholder path, not a real file.
- Prototype variants are built from the project's own tokens so each could ship tomorrow; sharing tokens is not convergence [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]). With no project, use neutral grays, one accent and the system font stack [S-L19-031].
- Consolidate drift: several near-identical hand-typed cubic-beziers are a consolidation finding [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]), rated LOW (polish) [S-L19-027] ([[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]]). One component that is bouncier than the rest of a crisp app is also a finding, because motion personality must stay consistent across components [S-L19-025].
- One plan per finding; merge only when two findings touch the same files with the same fix, such as the same easing-token swap across components [S-L19-026] ([[sources/eks-skills-improve-animations-plan-template-emilkowalski-skills-skills-improve-animations-plan-template-md|emilkowalski/skills: skills/improve-animations/PLAN-TEMPLATE.md]]).

### A component inside the system: the toast

- For toasts, people usually either keep Sonner's defaults or go fully custom, so the docs recommend the headless route and show wrapping `toast()` in your own function whose props fit your codebase [S-L19-090] ([[sources/sonner-styling-styling-sonner|Styling – Sonner]]).
- The house skill calls this the recommended design-system toast: headless `toast.custom()` wrapped in your own `toast()`, which keeps Sonner's positioning, stacking and swipe [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]). Styling is a ladder (defaults, inline styles, classes with `!important`, headless); climb only as far as needed, and do not settle on the middle rungs [S-L19-022]. See the [[synthesis/toasts-and-notifications|Toasts and notifications synthesis]].

## Where they agree and disagree

**Between the sources**

- Kole and Emil describe the same habit from two ends: Kole's advice to make decisions you can stick to, and to use styles, variables and components, [S-L19-044][S-L19-045] are the design-side version of Emil's "extend the codebase's tokens, don't fork them" [S-L19-018] [inferred].
- Strictness looks different but does not really conflict. Emil's token rules are hard rules [S-L19-018]; Kole says to bend the system's rules only with intention [S-L19-054]. OpenDesigner's override path for standards (restate the rule once, then record the person's reason with `engine.py standard override`) is a way to break a rule with intention [inferred].
- Size: Kole's lean-startup system is "easy to scrap" [S-L19-054]; the house motion vocabulary is already small (three curves and a duration table) [S-L19-018], so it fits a lean system [inferred].
- Using shared tokens instead of hand-typed values is a must-level standard (STD-visual-details-26), but consolidating near-duplicates that already exist is a LOW-severity finding in an audit [S-L19-027]. The two fit together: the rule for new code is fixed, the urgency of fixing old drift is low [inferred].
- The six named course easings [S-L19-007] are a bonus library, not the rules; the skills name three curves for UI work [S-L19-018]. Because the six shown start slowly [inferred], they cannot be UI entrance curves under STD-easing-duration-03 (never ease-in on UI).
- The find-animation-opportunities skill says suggested curves come only from the shared vocabulary, yet its own example recipes use the `ease-out` and `ease` keywords; its analysis flags this as an internal tension [S-L19-024].
- No second source backs either practitioner number: Kole's 10px radius [S-L19-045] and his 1.27 ratio [S-L19-042] each come from one video, so treat them as opinion.

**With OpenDesigner's existing research**

- Tiers, DC-L07-01 and DC-L07-02: two tiers (primitive and semantic) by default, component tokens only when a brand must restyle one component or 3 or more components share a value (EightShapes' "start within, then promote"). This agrees with Kole's point that a system is about decisions, not hundreds of components [S-L19-044] and with sizing the system to the team [S-L19-054] [inferred]. The Q-token-01 default is `two-plus`.
- Coverage, DC-L07-07: the default is extended coverage, including motion, which agrees with Emil's motion tokens [S-L19-025].
- Naming, DC-L07-05 and DC-L07-06: a 2-4 letter prefix added only in platform output, kebab case in CSS. `engine.py` emits names such as `--ds-motion-easing-enter` (its `css_var` function adds the `ds` prefix). The house vocabulary uses unprefixed `--ease-out`, `--ease-in-out` and `--ease-drawer` [S-L19-018], and recon looks for `--ease-*` and `--duration-*` [S-L19-027]. In a project that already has `--ease-out`, a prefixed export would add a second set of curve tokens unless it maps onto the existing ones, which STD-visual-details-26 forbids [inferred]. `standards.json` records no conflict for this yet.
- Motion tokens, DC-L07-14, DC-L04-20 and DC-L04-21: 3-5 durations, 3-4 easings, and default curves of standard (0.2, 0, 0, 1), enter (0, 0, 0, 1) and exit (0.3, 0, 1, 1). These are not the house curves. `standards.json` already records the conflicts: `engine.py` builds `motion.easing.enter` and `motion.easing.exit` from other curves (the exit is an ease-in shape), the Energy dial swaps curves, and the Q-motion-03 default names the card's curves (STD-easing-duration-02, STD-easing-duration-03). It also records that the Energy dial stretches durations past the per-element budgets (STD-easing-duration-07). STD-components-toasts-drawers-40 notes the engine can create `motion.easing.drawer` with `engine.py set`.
- Springs, DC-L07-14 and DC-L04-28: DTCG has no spring type, so springs go in `$extensions`. STD-springs-gestures-02 asks for damping and response; `standards.json` records that the Q-motion-04 default stores stiffness instead.
- Lifecycle, DC-L07-23: a `$description` on every semantic token and one release of deprecation before deleting. Emil adds the audit habit of consolidating near-duplicate curves [S-L19-025]; no conflict.
- Governance, DC-L11-03 and the Q-gov-01 default: a strict core (tokens, primitives, accessibility behavior) with loose edges. This matches Kole's advice to break the system only with intention [S-L19-054] [inferred]. DC-L11-01's default for small teams (adapt an accessible base, invest in tokens and docs) matches the lean-startup advice [S-L19-054] [inferred].
- Build order, DC-L11-06: minimal foundations first, then components pulled from a real product. Kole's new modal built from existing parts [S-L19-044] is that reuse in action [inferred].

## Decisions this informs

- **Q-scope-02** (existing screens or a fresh start): with existing code, run recon and extend the tokens found (STD-visual-details-26) [S-L19-027][S-L19-024].
- **Q-scope-04** (team size and model): size the system to the team, lightweight for a lean startup, deeply defined for many products [S-L19-054].
- **Q-gov-01** (how strict): hold decisions everywhere [S-L19-044], break them only with intention [S-L19-054].
- **Q-token-01** (layers of named values): few decisions held consistently [S-L19-044], so no large component tier at launch [inferred; DC-L19-181].
- **Q-token-02** (naming rules): the house curve names `--ease-out`, `--ease-in-out`, `--ease-drawer` [S-L19-018][S-L19-023]; recon expects `--ease-*` and `--duration-*` [S-L19-027].
- **Q-token-03** (which values get a token): curves and durations as shared tokens [S-L19-025].
- **Q-token-07** (keeping the Figma library tidy): Kole's "styles for colors, variables for measurements, components for UI" [S-L19-045] is one video's opinion; keep DC-L07-21 (a color that changes by mode is a variable), as DC-L19-181 and DC-L19-173 do.
- **Q-token-05** (composite values, including motion): curves as cubic-bezier tokens [S-L19-033]; springs by damping and response (STD-springs-gestures-02).
- **Q-token-09** (descriptions and retiring tokens): consolidate near-identical hand-typed curves [S-L19-025]; one plan per finding [S-L19-026].
- **Q-motion-01** (motion personality): one personality held across components; a single bouncy component in a crisp app is a finding [S-L19-025].
- **Q-motion-02** (how many durations): per-element budgets rather than a free scale (STD-easing-duration-07).
- **Q-motion-03** (how curves are grouped): by what the motion does, defaulting to ease-out [S-L19-025].
- **Q-shape-01** and **Q-shape-02** (corner softness and radius steps): one shared radius for all smaller components [S-L19-045] (one video's opinion).
- **Q-type-09** (scale ratio): derive sizes from a ratio such as 1.27 [S-L19-042] (one video's personal method).
- **Q-state-06** (risky actions): in one video the primary color always marks the non-destructive action, as in macOS pop-ups [S-L19-044]; another Kole video fills the Delete button instead, and DC-L19-107 keeps both as options.
- **Q-form-04** and **Q-comp-01** (toasts and the component base): a headless design-system toast wrapped in your own `toast()` [S-L19-022][S-L19-090].
- **Q-dist-03** (catching rule breaks): `standards.json` gives STD-visual-details-26 a review pattern that flags a hand-typed `cubic-bezier(` inside a `transition` or `animation` declaration; near-duplicate curves are a consolidation finding [S-L19-025].

## Visual examples worth showing

- **Same parts in different places**: Linear's settings panel next to its view-creation screen, with identical buttons, spacing and text styles [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- **A convention you can trust**: a macOS confirmation pop-up with the primary color on the non-destructive action [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- **Recipe app before and after**: a back and a skip button drawn differently, and two unmatched search bars, then all small components at one 10px radius [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- **Lean versus massive**: a lightweight startup system beside Material Design, sized to the team [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- **Two type scales from 16px**: steps of 1.62 reaching about 110px next to steps of 1.27 [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]).
- **The house motion token block**: `--ease-out`, `--ease-in-out` and `--ease-drawer` as CSS custom properties, each with its curve plotted [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]])[S-L19-033].
- **Five near-matching curves become one token**: before and after code of hand-typed cubic-beziers consolidated into `var(--ease-out)` [S-L19-025] ([[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]).
- **The animations.dev easing library**: the `:root` block with six named curves, plotted to show their slow start [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- **Sonner's styling ladder**: the same toast with defaults, inline style, classes with `!important`, and headless [S-L19-022] ([[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]])[S-L19-090].
- **Variants that share tokens but not direction**: prototype variants on the project's own colors, radii and fonts, differing only on their named axis [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).

## Open questions

- When a project already defines `--ease-out` or a duration scale, should `engine.py export --format css` map OpenDesigner's motion tokens onto those names instead of emitting `--ds-motion-easing-*` [inferred]? DC-L19-189 (keep the project's names) and DC-L19-183 (unprefixed house aliases) propose yes; `standards.json` records no conflict for this yet, and the engine is unchanged.
- Should OpenDesigner's default easing tokens become the house trio (`--ease-out`, `--ease-in-out`, `--ease-drawer`)? DC-L19-85 proposes it for Q-motion-03; the conflicts with DC-L04-21, the Energy dial and the current Q-motion-03 default are recorded but not resolved.
- Kole's advice to give all smaller components one radius [S-L19-045] comes from one video. How does it sit with Q-shape-03's default of four radius roles? One role could cover every small part [inferred].
- How should `engine.py review` rate a hand-typed curve: as a must-level break of STD-visual-details-26, or as LOW polish as the audit severity says [S-L19-027]?
- Should the six named animations.dev easings [S-L19-007] be offered at all, and for what? The source does not say where they are used, and their slow start rules them out for UI entrances.
- How should a project record a rule it breaks on purpose [S-L19-054]? House standards have `engine.py standard override`. For a one-off raw value, `engine.py review` accepts an `od-ignore` comment on the line but records no reason; DC-L19-165 proposes that every exception carry a one-line reason.
