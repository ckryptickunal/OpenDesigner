---
type: synthesis
title: Design process
created: 2026-09-24
updated: 2026-09-24
sources:
  - 2rtsoM2Dqrs
  - 59XWYgN00nQ
  - 5JxUJ1fuyO8
  - 6CC8lLnqa28
  - 7sUUzOCv47U
  - 9WVt1CelBfg
  - ADaQuZS04Rc
  - AH_ugxmLeUM
  - A_Ozpb0XDuw
  - BvbFPzLjWcU
  - HE4rLEQpiXY
  - Lp6ey4AyDzA
  - RCneB_MQ7qs
  - V3Omp1hm0Sg
  - VPeTgU7la34
  - Vy0KKvZJRH8
  - Yr2uIcFZDDQ
  - ek-agents-with-taste
  - ek-building-a-drawer-component
  - ek-building-an-animation-course
  - ek-developing-taste
  - ek-friction-as-a-feature
  - ek-train-your-judgement
  - ek-you-dont-need-animations
  - eks-skills-apple-design-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-plan-template
  - eks-skills-improve-animations-skill
  - eks-skills-mobile-native-skill
  - eks-skills-prototype-skill
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
  - goWOAFqJHpA
  - jSxxAFxjxbU
  - lkKGQVHrXzE
  - pGYLZyBE32o
  - t7mpEDXzjCg
  - ulSOdTgoGeY
  - xHD01_Onac0
tags:
  - od-area-process
---

# Design process

## In short

Good design work follows a rough order: understand the problem and the person first, gather references, plan the structure (flows, wireframes, content) before any styling, then build section by section, and only add motion once the layout already works. Along the way you try several options, look again with fresh eyes the next day, and check the result on the real screen or device, not a zoomed-out canvas. Emil Kowalski's sources add a strict review habit for motion (slow motion, frame by frame, real hardware, a clear approve or block) and a disciplined way to audit a codebase and hand fixes to other agents; those are locked house standards. Kole Jain's redesign videos and Steve Schoger's Claude Code session show the same order in practice and are practitioner opinion. Two of Kole Jain's videos say work takes longer than expected [S-L19-036] [S-L19-078], and Emil Kowalski's sources say "it works" is not the end (`STD-process-review-taste-50`).

## House standards

- `STD-when-to-animate-01` (must): decide whether something should animate at all (how often it is seen, what its purpose is) before choosing any tool, easing or duration.
- `STD-when-to-animate-22` (should): judge whether an idea deserves to be built before building it; build A and B to compare, ship only the winner.
- `STD-visual-details-44` (should): decide what not to build.
- `STD-visual-details-47` and `STD-visual-details-48` (should): decide the emotion people should feel and reinforce it in every decision, and reason with Apple's eight principles (purpose, agency, responsibility, familiarity, flexibility, simplicity, craft, delight).
- `STD-visual-details-37` (should): break a familiar pattern only when you can prove the new one is better, and test it.
- `STD-process-review-taste-11` (must): before judging or designing motion, map the stack, existing conventions, the product's personality and how often each surface is seen.
- `STD-process-review-taste-64` (should): talk an animation through before coding it, then code, improve and iterate.
- `STD-process-review-taste-35`, `STD-process-review-taste-36` and `STD-process-review-taste-34` (should): prototype interactively, design motion together with the visuals, and test with real people in the real context.
- `STD-easing-duration-17` (must): choose every curve and duration deliberately and say which and why.
- `STD-process-review-taste-30`, `STD-process-review-taste-31` and `STD-process-review-taste-32` (should): review motion in slow motion and frame by frame, look again the next day, and feel-check by using it the way users do.
- `STD-process-review-taste-33` (must): judge touch and gesture feel on real hardware; a simulator or shrunken window never counts as verified.
- `STD-mobile-touch-70` (must): apply each mobile fix only where its reason applies.
- `STD-process-review-taste-04` and `STD-process-review-taste-05` (must): report findings as one Before, After and Why table and end a motion review with Block or Approve.
- `STD-process-review-taste-12` to `STD-process-review-taste-21` (mostly must): the audit workflow: sweep every seam, stay read-only, let the person pick findings, write one self-contained plan per finding from the fixed template, execute in isolation and reconcile.
- `STD-process-review-taste-50` (should): a product that merely works is not finished.
- `STD-process-review-taste-63` and `STD-process-review-taste-66` (should): keep a product alive with updates and a changelog, and don't tease unfinished work.

## What the sources teach

### Start from the problem and the person

- Look past the request for a website to the business need, usually more customers or sales, and design for the site's users rather than the client's taste [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- Start from what the user came to do: for a rental search, build the search bar first, and add listings and filters only when a second intent (browsing) calls for them. Decide what content to show and structure it so imperfect real content still works, and add motion only where it adds clarity [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- For a desktop app, first work out how and where the user will actually reach it (a shortcut while working in other apps, a quick-capture window), then design the main window, and ask what minimum UI lets the content shine before adding color or effects [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).
- Write a full brief before designing, keep it in mind throughout, and use realistic content, never lorem ipsum [S-L19-037] ([[sources/59XWYgN00nQ-create-a-portfolio-with-no-experience-or-clients-needed|Create A Portfolio With No Experience (or clients) Needed]]).
- A UX case study shows the whole research loop: collect data, group it in an affinity map into a problem statement, build a persona, map the flow, sketch lo-fi wireframes, test them with a couple of people, tweak and retest, then design and reflect [S-L19-083] ([[sources/t7mpEDXzjCg-make-a-perfect-ux-case-study-in-8-steps|Make A Perfect UX Case Study In 8 Steps]]).
- Before animating, name the purpose, weigh how often people will see it and what they are trying to do, and only then check the speed [S-L19-012] ([[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]).
- Keep a judgement step that decides what is worth building at all, since AI no longer makes building expensive enough to force that choice [S-L19-009] ([[sources/ek-friction-as-a-feature-friction-as-a-feature|Friction as a Feature]]).

### Gather references, then plan structure before pixels

- Design is iterative: early designs will be weak, quantity breeds quality, and when stuck you move on and come back. Gather inspiration and a mood board before opening Figma, and explore options instead of taking the first idea [S-L19-040] ([[sources/6CC8lLnqa28-6-things-you-probably-need-to-hear-as-a-web-designer|6 Things You Probably Need to Hear (as a web designer)]]).
- Pull a site you like apart into zones, spacing, text length and hierarchy before designing; to learn, copy a design exactly rather than redesigning it [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]).
- Plan the user flow first, even as boxes on paper, and check each screen for gaps such as a missing search bar or skip button. Improve an existing UI one mistake at a time rather than restarting [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- Start a website with a wireframe, and make it varied; a boring wireframe usually leads to a boring site [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]).
- Design an app in screens and sequences, not sections: for every screen ask how the user got there and what they need next, design every state (empty, loading, success, error), and pull out components so the system stays consistent [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- One redesign runs diagnosis, a visual identity deck from one moody image, a "Frankensteined" wireframe assembled from sections of other sites (keeping only the structure), section-by-section visuals, then animation [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]).
- Other redesigns follow the same pattern: diagnose the current site, gather inspiration from competitors, Dribbble and past work, restructure the content, then rebuild section by section and compare with the original [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]); critique element by element, gather real assets, fix the layout before anything else and size the design to a real browser (about 1920 by 1,000 pixels) [S-L19-049] ([[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]); gather inspiration, plan a page roadmap, borrow and adapt layouts and search for assets before starting [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- A dashboard redesign starts with the hierarchy: check what falls below the fold, cut what adds no value, audit and merge cards, rank each module high, mid or low priority, then assemble the grid [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- For a product people have used for years, critique what was lost, and evolve the layout rather than replacing it [S-L19-076] ([[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]).
- Study many real sites to see which sections recur and why, make your own interpretation, and design every tab of a tabbed section before handing off [S-L19-066] ([[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]).
- Replace "eyeball one page, then build a style guide" with a systematic type scale, rank every text element by importance before styling, and review designs on the screens they are meant for [S-L19-042] ([[sources/7sUUzOCv47U-mathematically-perfect-typography-for-web-design|Mathematically Perfect Typography for Web Design]]).

### Build and iterate

- Try several layouts for a key section (about four for one call to action) and keep changing it until it feels right; a section should already look good before any animation is added [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- Work top to bottom one section at a time, try a value and adjust it ("Goldilocks" it), apply a finished treatment to every section, and recreate the original to compare before and after [S-L19-103] ([[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]).
- The AI-assisted version: reference image, prompt, generate, check responsiveness, import into Figma, polish fonts, alignment and color, then reuse the screen as the reference for the next ones [S-L19-086] ([[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]).
- An end-to-end no-code build: a reference site, a logo SVG from Figma, a 3D model and animation, a video export, the page in Figma, the build in Wix Studio, then a review with a list of fixes [S-L19-046] ([[sources/A_Ozpb0XDuw-how-hard-is-it-to-really-make-a-no-code-3d-animated-website|How hard is it to REALLY make a no-code 3D animated website?]]).
- Research first, then a case study, a domain, a feature plan, a logo, wireframed onboarding and a palette; look again the next day and make bigger changes if needed (here a switch to dark mode). The main screens took three days against an estimate of four to six hours [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).
- Look honestly at gradients and shadows and remove them if they aren't working; preview on the real screen [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).

### Review, test and verify

- Emil's working method: answer the framework questions before coding, review again the next day, use slow motion and frame-by-frame inspection, test on real devices, and report findings as Before, After and Why tables [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]). The review standards repeat the debugging method: slow motion, frame by frame, real devices and fresh eyes [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]).
- A repeatable motion review has standards, escalation triggers, a remedial order (starting with deleting the animation), tiered output and explicit approval criteria [S-L19-032] ([[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]]).
- Prototype interactively, design interaction and visuals together, test with real people in real context and review motion in slow motion [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- Debug a drawer on a real phone connected by cable with Safari's devtools, loading the dev server by IP address; open-sourcing a component brings more feedback [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]).
- For mobile web fixes: match the symptom, apply the fix only where its reason applies, ship the baseline first, test on an older real phone with the keyboard open and in landscape, and report what still needs a device [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- Train judgement with a loop: compare two variants, use them, pick one, write down why, then compare with an expert breakdown [S-L19-011] ([[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]]). Surround yourself with great work, work out why you like it, practise and ask the right person for critique [S-L19-008] ([[sources/ek-developing-taste-developing-taste|Developing Taste]]).
- To turn judgement into rules: step back, ask why you made each decision, say it, make it a strict rule, then give the packaged rules to agents [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]).

### Audit a codebase and hand the fixes off

- Finding motion opportunities runs recon, a sweep, a gate and a report, with a frequency map, file and line evidence for every candidate, and a report listing opportunities, rejected candidates and a verdict [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]).
- Improving existing motion runs recon, a parallel audit, vetting, prioritizing by leverage, letting the person choose, writing plans, executing and reconciling [S-L19-027] ([[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]]). Each plan has a fixed structure (status, commit, severity, category, scope, problem, target, conventions, steps, boundaries, verification) and an index [S-L19-026] ([[sources/eks-skills-improve-animations-plan-template-emilkowalski-skills-skills-improve-animations-plan-template-md|emilkowalski/skills: skills/improve-animations/PLAN-TEMPLATE.md]]).
- A prototype run scopes one piece, restates the brief in one sentence, does recon, names directions on distinct axes before coding, verifies every variant, hands off with a trade-off table, then promotes or riffs [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).

### Ship, and keep it alive

- Don't tease a project before it is done; a presale with a public deadline gives outside motivation. Treat the product as living, with free updates, refreshed sections and a changelog, and go the extra mile rather than ship something mediocre [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).

## Where they agree and disagree

Between the sources:

- **Structure before styling, styling before motion:** flows and wireframes first [S-L19-045] [S-L19-085] [S-L19-083] [S-L19-054] [S-L19-062]; layout that works before animation [S-L19-082]; whether to animate before how [S-L19-012].
- **Fresh eyes the next day:** Emil's sources [S-L19-023] [S-L19-033] and Kole's gamified app [S-L19-078].
- **Check on the real thing:** real screen sizes [S-L19-042] [S-L19-057], real phones [S-L19-005] [S-L19-028], real people [S-L19-020].
- **Simulators:** the drawer essay offers Xcode Simulator as a close replica [S-L19-005], but `STD-process-review-taste-33`, built from that essay and newer skills, says a simulator never counts as verified for feel. The standard wins.
- **Copying references:** copy a design exactly to learn [S-L19-043]; keep only a reference's wireframe and bring your own identity [S-L19-062]. The first is practice; for real work OpenDesigner's identity firewall applies [inferred].
- **Evolve or rebuild:** fix one mistake at a time [S-L19-045] and evolve a familiar layout [S-L19-076], while several redesigns rebuild a site section by section [S-L19-065] [S-L19-082]. The choice seems to follow how familiar users are with the current design [inferred].
- **Small tests:** testing wireframes with a couple of people [S-L19-083] spots confusion, but tests that small cannot prove a business result [S-L19-038] [inferred].
- **Time:** work takes far longer than estimated: four screens took three days instead of four to six hours [S-L19-078], and the pricing video says things generally take longer than you think [S-L19-036]. Both are one creator's experience, not measured data.

Against OpenDesigner's existing research:

- **Build order:** DC-L11-06 defaults to minimal foundations first (color roles, type scale, spacing, radius), then components from a pilot, then back-filling foundations. [S-L19-042] argues for the scale first, and [S-L19-044] extracts components from designed flows; DC-L11-06's default combines the two [inferred].
- **Size the system to the team:** [S-L19-054] says a lean startup needs a light system that is easy to scrap and a many-product company a deep one. DC-L11-01 likewise recommends that small teams adapt an existing base rather than create from scratch.
- **Audits at page scale:** DC-L11-04 (an interface inventory with keep, merge or kill decisions) is the system-scale version of the element-by-element critiques in [S-L19-049] [S-L19-068] [S-L19-065] [inferred].
- **References:** DC-L17-03 defaults to reinterpreting a reference (take its lessons, rebuild in your own world), which is what the Frankensteined wireframe does [S-L19-062]. DC-L17-02 starts an existing product with an audit and otherwise from a brief, matching [S-L19-037].
- **Gates:** DC-L17-12 sets approval gates at structure, direction and assets; [S-L19-062] settles the visual identity before any section is designed, and the prototype skill stops for the person's choice [S-L19-031] [inferred].
- **Convention first:** DC-L13-17 defaults to conventional behavior with a custom look and novelty only where it sets the product apart, which [S-L19-054] [S-L19-076] and `STD-visual-details-37` all support.
- **Principles as tie-breakers:** DC-L11-05 wants three to five testable principles; [S-L19-054] says the system should reflect the team's values, and `STD-visual-details-48` names Apple's eight [inferred].

## Decisions this informs

- **Q-scope-05** (where to start: product, UI kit, reference or brief): the redesign videos start from an existing product with a critique [S-L19-049] [S-L19-068]; [S-L19-062] shows a reference used as `reinterpret`; [S-L19-037] starts from a `brief`.
- **Q-scope-02** (existing screens or a fresh start): element-by-element critique is a `manual-inventory` at page scale [inferred].
- **Q-gov-02** (build order): scale first [S-L19-042] points to `foundations-first`; extracting components from flows [S-L19-044] to `pilot-driven`.
- **Q-scope-04** (team size and model): size the system to the team [S-L19-054].
- **Q-brand-07** (tie-breaking principles): the system reflects the team's values [S-L19-054]; decide the emotion first (`STD-visual-details-47`).
- **Q-plat-10** (usual behavior, own look, or something new): evolve familiar layouts [S-L19-076] and follow conventions [S-L19-054], which backs the default `custom-skin`.
- **Q-gov-05** (what hurts, and how to measure): find the real problem first and measure before and after [S-L19-038].
- **Q-pref-02** (planned: reviewing AI changes): Before, After and Why tables [S-L19-023] back `patches`.

## Visual examples worth showing

- A user flow sketched as boxes on paper, catching a missing search bar and skip button before any screen is designed [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).
- A wireframe assembled from other sites' sections, then two different visual identities dropped into the same layout [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]).
- The finance dashboard redesign as a strip: the fold line, 12 cards audited and merged, modules tagged high, mid and low, and the final grid [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- A rental flow that begins with only a search bar and grows listings and filters as a second intent appears [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- Four versions of one call-to-action section, three rejected with the reason for each [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- A gamified app's first-day light screens beside the next-day dark redesign [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).
- The case-study research loop from Google Form to affinity map, persona, flow, lo-fi sketches and the tested final design [S-L19-083] ([[sources/t7mpEDXzjCg-make-a-perfect-ux-case-study-in-8-steps|Make A Perfect UX Case Study In 8 Steps]]).
- A Mac quick-capture window that appears from a shortcut, collapses into a toast on Enter and slides away [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).

## Open questions

- OpenDesigner's interview usually happens in one session. How can it build in "look again the next day" (`STD-process-review-taste-31`), for example by suggesting a later `engine.py review`?
- `STD-process-review-taste-34` asks for testing with real people in context, which the builder cannot do itself. Should the handoff include a short test plan?
- Q-gov-02 has no single default option in `questions.json`; its stage file gives DC-L11-06's mixed default (minimal foundations first, then pilot-driven components, incremental rollout). Should scale-first or flows-first be the recommendation for a new product?
- How should estimates be set when both the creator's own project [S-L19-078] and his pricing advice [S-L19-036] say work runs long?
