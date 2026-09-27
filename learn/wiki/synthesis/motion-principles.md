---
type: synthesis
title: Motion principles
created: 2026-09-24
updated: 2026-09-28
sources:
  - adev-changelog
  - adev-home
  - ek-7-practical-animation-tips
  - ek-agents-with-taste
  - ek-building-a-toast-component
  - ek-building-an-animation-course
  - ek-train-your-judgement
  - ek-you-dont-need-animations
  - eks-readme
  - eks-skills-animate-expo-skill
  - eks-skills-animate-skill
  - eks-skills-animation-vocabulary-skill
  - eks-skills-apple-design-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-improve-animations-audit
  - eks-skills-improve-animations-plan-template
  - eks-skills-improve-animations-skill
  - eks-skills-pick-ui-library-skill
  - eks-skills-prototype-skill
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
  - 14h1VnkQvIc
  - 6CC8lLnqa28
  - B7k5rOgmOGY
  - EHwZzWd-OnQ
  - HE4rLEQpiXY
  - RCneB_MQ7qs
  - SfX43uIubj4
  - VPeTgU7la34
  - ZsP20PN14O0
  - eMMiLeo_UGI
  - tNMAFjzapOk
  - ulSOdTgoGeY
  - vaul-default
tags:
  - od-area-motion
---
# Motion principles

## In short

Motion is part of how an interface answers people, but every animation has to earn its place. Before picking a curve or a duration, ask two questions: how often will people see this, and what job does the motion do? Things people use all day, or trigger from the keyboard, should not animate at all, while rare moments such as a first run can carry more personality. When something does move, it should be quick, start from where it really is, be interruptible, and leave the way it came. The practitioner videos also favour subtle, purposeful motion over flashy effects, but they decorate marketing pages far more freely than the house standards allow inside product UI.

## House standards

- `STD-when-to-animate-01`: decide whether to animate (how often it is seen) and name its purpose before choosing any tool, easing or duration; if either check fails, ship no animation.
- `STD-when-to-animate-03`: every animation names one purpose: feedback, spatial consistency, state indication, preventing a jarring change, explanation, or delight (delight only for rare or first-time moments).
- `STD-when-to-animate-04`: the more often something is seen (100+ a day, tens a day, occasionally, rarely), the shorter and subtler its motion, down to none.
- `STD-when-to-animate-05`: nothing seen or triggered 100+ times a day animates (launchers, command palettes, keyboard shortcuts, core navigation).
- `STD-when-to-animate-06`: actions started from the keyboard never animate.
- `STD-when-to-animate-07`: things seen tens of times a day (hover effects, list navigation, frequent toggles) lose their animation or shrink it to near-imperceptible.
- `STD-when-to-animate-08` and `STD-when-to-animate-09`: occasional surfaces (modals, drawers, toasts) get standard motion; delight motion is spent only on rare, high-emotion moments.
- `STD-when-to-animate-10` and `STD-when-to-animate-11`: explanatory motion belongs on marketing and onboarding surfaces, and decorative motion stays off functional data.
- `STD-when-to-animate-15` and `STD-when-to-animate-16`: when the gate fails, say so and offer a non-motion alternative; expect to reject most motion ideas (5-7 suggestions at most for a whole app).
- `STD-easing-duration-13`: the product's personality sets how much motion there is; a crisp dashboard gets fewer, faster animations than a playful consumer app.
- `STD-enter-exit-origin-01`: never enter from or exit to scale(0); start at scale 0.9-0.97 with opacity 0.
- `STD-enter-exit-origin-06`: an element leaves along the same path it entered, and its swipe-to-dismiss direction matches.
- `STD-enter-exit-origin-27`: scroll-triggered reveals only on marketing surfaces, never on daily-use UI.
- `STD-springs-gestures-12` and `STD-springs-gestures-13`: every animation can be grabbed and reversed mid-flight, and no transition locks out input.
- `STD-springs-gestures-42`: intermediate frames point toward the outcome.
- `STD-accessibility-motion-01`: the reduced-motion version ships in the same change as the animation.
- `STD-process-review-taste-01`: motion that merely runs is not done; sluggish or wrong-origin motion is a defect.

## What the sources teach

### Gate first: how often, and what for

- Emil Kowalski puts a gate in front of every animation: estimate how often it will be seen, name its purpose, and ship nothing if either check fails [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]] [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]] [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]. His example is Raycast: opened hundreds of times a day, it has no open animation, and he calls that the right experience [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]].
- The opportunity-finding skill lists six valid purposes (feedback, spatial consistency, state indication, preventing a jarring change, explanation, delight) and says daily use argues for less motion [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]. The audit and review checklists use the same list without delight [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]] [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]].
- The Expo skill applies the same gate to mobile apps as the first steps of a fixed build order: frequency, purpose, cheapest tool, cheap properties, spring or timing, thread, press, haptics, reduced motion [S-L19-016] [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]].
- Keyboard-initiated actions and anything used 100+ times a day never animate [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]. In audits, frequency sets how severe a motion problem is, and deleting the animation is often the strongest fix [S-L19-027] [[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]] [S-L19-032] [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]].
- The practitioner videos reach a similar test in plainer words: an animation should add clarity or functionality, and the presenter's old portfolio, whose animations served no purpose, is shown as the bad example [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]. Another video says every animation should support clarity and that complex animation added for its own sake makes navigation harder [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]].

### The context sets the amount

- Dashboards: animation stays tame and user-focused because people want a snappy, fast tool; creative motion is kept for chart hover states [S-L19-047] [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]. The house keeps decorative motion off functional charts (`STD-when-to-animate-11`), so of that chart motion only hover states that help reading, such as a value bubble or dimming the other bars, fit [inferred].
- Websites: heavy 3D and animation are memorable but optional, and should go when they slow loading or make navigation harder; the amount follows the site's goal (a conversion page versus an awareness piece with scrollytelling) [S-L19-040] [[sources/6CC8lLnqa28-6-things-you-probably-need-to-hear-as-a-web-designer|6 Things You Probably Need to Hear (as a web designer)]].
- Software marketing sites are moving from heavy graphics to simple, tasteful animation that has to be executed well [S-L19-066] [[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]], and web animation should be subtle and classy rather than big or flashy [S-L19-069] [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]].
- Emil's rule is that product UI motion must be fast, with marketing sites as the exception [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]; the course guideline says nothing should run longer than 1s unless it is illustrative [S-L19-001] [[sources/adev-changelog-animations-dev|animations.dev]]. Motion should match the product's personality [S-L19-027] [[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]] [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]].
- A landing-page ladder shows the same growth: no animation, then simple load animations, then smooth transitions, then high-quality details [S-L19-072] [[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]].

### Motion as brand and storytelling (marketing pages)

- Pick a few motion themes and repeat them across the site instead of one-off effects, and use motion to lead the eye to each section's focal point [S-L19-062] [[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]].
- "Just because things don't have to move, doesn't mean they shouldn't": give decorative elements entrances that suit what they are, and put parallax on elements in spacious margins [S-L19-063] [[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]. Text swapping, animated display text, morphing images and scroll-driven diagrams bring otherwise static pages to life [S-L19-050] [[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]].
- Staggered slide-up entrances and photos that zoom slightly make a site feel alive, with a warning that marquee text costs usability [S-L19-085] [[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]].
- One video sorts web animation into five kinds: entrance, hover or click, scroll, looped and mouse-driven [S-L19-069] [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]].
- Direction carries meaning: tools that slide up from the bottom read as temporary, and screens sliding in from the left show progress through onboarding [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]].

### Motion that behaves like real things

- Entering elements should grow from about scale(0.95), never from scale(0): even a deflated balloon keeps a visible shape [S-L19-004] [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]. The seven practical tips add origin-aware popovers and fast-or-no animation [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]].
- An interface feels alive when motion starts from the current on-screen value, inherits the user's velocity, projects momentum forward and can be grabbed at any instant; panels leave along the path they came in, and in-between frames hint at the outcome [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]].
- Sonner moved from CSS keyframes to transitions because keyframes cannot be interrupted: toasts added quickly jumped to their new positions instead of flowing [S-L19-006] [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]].
- In the video on swipe interactions, transitions follow the swipe direction and keep continuity, for example an image that zooms in to become the next page's hero instead of a plain page slide [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]].
- The vocabulary skill names the classic principles worth knowing: purposeful animation, anticipation, follow-through, squash and stretch, perceived performance, frequency of use and spatial consistency [S-L19-019] [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]].

### Judgement is trained, and feel is checked

- The judgement exercises cover element size, entry animations, intentionality, frequency of use, removing elements, interruptions, stagger and layered motion [S-L19-011] [[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]].
- Motion can be mechanically correct and still feel wrong, so every fix plan ends with a feel check in slow motion [S-L19-026] [[sources/eks-skills-improve-animations-plan-template-emilkowalski-skills-skills-improve-animations-plan-template-md|emilkowalski/skills: skills/improve-animations/PLAN-TEMPLATE.md]]. Every prototype variant must meet the same craft bar [S-L19-031] [[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]].
- Motion has to be felt to be understood, so the course teaches through interactive bad-versus-good demos [S-L19-007] [[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]] [S-L19-001] [[sources/adev-changelog-animations-dev|animations.dev]], with theory lessons on easing, springs, timing, purpose and taste [S-L19-002] [[sources/adev-home-animations-dev|animations.dev]].
- The skills exist to build, review and audit motion, find where it genuinely helps, and decide what not to animate [S-L19-014] [[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]]. A motion library is only worth adding for springs, layout animations, exit animations or gesture-driven values [S-L19-029] [[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]].
- Vaul exposes a `--initial-transform` variable to adjust a drawer's entrance when the drawer does not touch the screen edge [S-L19-094] [[sources/vaul-default-default-vaul|Default – Vaul]].

## Where they agree and disagree

- **Agreement on purpose.** The videos' tests ("add clarity or functionality" [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]], "support clarity" [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]) match the purpose gate in `STD-when-to-animate-03` in spirit, although no video uses frequency of use as a test [inferred].
- **Disagreement on how much.** Adding motion to things that don't have to move, and small hover interactions on "pretty much everything" [S-L19-063] [[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]], and "buttons should almost always have a small animation" [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]], go further than `STD-when-to-animate-07`, which removes or shrinks motion people see tens of times a day. The hover tip comes from a landing page and portfolio examples; the button tip is given as a general rule that "context matters" qualifies. Inside product UI the standard wins [inferred]. The one button animation both sides endorse is press feedback (`STD-mobile-touch-05`) [inferred].
- **Scroll motion.** Parallax and scroll-driven diagrams [S-L19-063] [[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]] [S-L19-050] [[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]] are allowed only on marketing pages (`STD-enter-exit-origin-27`), and parallax is removed under reduced motion (`STD-accessibility-motion-02`). One video also warns against scrolljacking [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]].
- **Direction semantics.** The rule that bottom means temporary and a screen sliding in from the left means progress [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]] comes from a single video, so treat it as practitioner opinion. It is consistent with `STD-enter-exit-origin-06` and with the shared-axis pattern in DC-L04-23 (onboarding on the x axis) [inferred].
- **OpenDesigner's personality framing.** DC-L04-19 and DC-L06-10 treat motion as a personality choice (productive versus expressive, with 1-3 hero moments per flow). That agrees with `STD-easing-duration-13`, but the house gate puts frequency first, and the standards now supersede both cards: `STD-when-to-animate-09` replaces DC-L04-19 and `STD-when-to-animate-05` replaces DC-L06-10. standards.json still records that Q-motion-01's advice to use expressive motion for page transitions and the primary action conflicts with `STD-when-to-animate-05` and `STD-when-to-animate-09`. DC-L19-82 proposes crisp motion by default and playful motion only for playful products.
- **Blocking input.** DC-L04-24 allows blocking input during transitions shorter than about 100ms [inferred in the card]; `STD-springs-gestures-13`, which never locks input, now supersedes it. The Q-motion-02 stage default still allows about 100ms, which standards.json records as a conflict.
- **Platforms.** DC-L10-14, where the operating system owns how screens come and go and the brand owns how things react inside a screen, agrees with the native-stack standards (`STD-mobile-touch-42`), and Q-motion-09's `one-language` option is now marked as breaking that standard. Its note that in-content brand motion runs "as springs" goes further than `STD-springs-gestures-01`, which keeps springs for motion a finger drives. DC-L14-08's per-device motion budgets (TV, watch, car, headset) are not covered by these sources: that is a gap, not a conflict.
- **Tabs and fades.** Q-motion-06's `fade-through` option (for unrelated destinations such as tabs) is now marked as breaking `STD-when-to-animate-05` and `STD-when-to-animate-14`, and its plain `fade` as breaking `STD-enter-exit-origin-02` (no opacity-only entrances); standards.json still records the stage default, all four patterns plus stagger, as a conflict.

## Decisions this informs

- **Q-motion-01** (motion feel): even the `two-mode` default has to leave high-frequency surfaces still; `productive` suits work tools; `none` keeps press feedback and quick fades by its own description, though the engine then makes the feedback transition instant [inferred from engine.py], short of the 100-160ms press in `STD-mobile-touch-05`; `springs` (springs throughout) is marked as breaking `STD-springs-gestures-01`; expressive motion goes only to rare moments (`STD-when-to-animate-09`).
- **Q-brand-04** (liveliness): decides where the small delight budget is spent, never on everyday controls.
- **Q-aud-02** (stakes): high-trust and work tools get fewer, crisper animations [S-L19-047] [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]], as `STD-easing-duration-13` requires.
- **Q-motion-06** (transition patterns): the named patterns still pass the gate; tab switches get no animation (`STD-when-to-animate-14`), so `fade-through` is marked as breaking it.
- **Q-pattern-04** (empty states and onboarding): onboarding and first run are where explanation and delight motion are allowed (`STD-when-to-animate-09`, `STD-when-to-animate-10`) [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]].
- **Q-motion-09** (system versus brand motion on iOS and Android): the OS owns screen transitions and the brand owns in-screen reactions (DC-L10-14), on springs only where a finger drives them (`STD-springs-gestures-01`); `one-language` breaks `STD-mobile-touch-42`.
- **Q-motion-07** (reduced motion): settled by `STD-accessibility-motion-02`, so the interview skips it; each animation ships with its reduced version (`STD-accessibility-motion-01`).

## Visual examples worth showing

- A launcher that opens instantly next to one that animates open, to show why Raycast has no animation [S-L19-012] [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]].
- The "Options" demo: the same element entering from scale(0) and from scale(0.93) [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]], with the balloon explanation [S-L19-004] [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]].
- Quickly added toasts: keyframes that jump versus transitions that flow into their new positions [S-L19-006] [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]].
- An image that zooms into the next page's hero compared with a plain page slide [S-L19-035] [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]].
- A hero-to-section transition where the hero slides away and its text blurs while the next section slides over it [S-L19-062] [[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]].
- Onboarding with editing tools sliding up from the bottom (temporary) and screens moving sideways (progress) [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]].
- A frequency ladder built from `STD-when-to-animate-04`: 100+ a day, tens a day, occasional, rare, each with example components and the motion each tier allows.

## Open questions

- OpenDesigner asks no question that separates marketing surfaces from product UI, yet most video advice only fits marketing pages [inferred]. Should the builder ask which surfaces are marketing?
- How should the gate appear in DESIGN.md? standards.json notes that the generated Motion section says how long things move but not when nothing should move (`STD-when-to-animate-01` conflicts), and that the question DC-L19-81 proposes for the gate (Q-motion-11) is not built.
- Should the direction semantics from [S-L19-084] [[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]] become a guideline? Only one source states them.
- Per-device motion budgets (DC-L14-08) have no support in these sources; they stay on OpenDesigner's own research.
