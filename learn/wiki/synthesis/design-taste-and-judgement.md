---
type: synthesis
title: Design taste and judgement
created: 2026-09-24
updated: 2026-09-28
sources:
  - 6CC8lLnqa28
  - 9WVt1CelBfg
  - AH_ugxmLeUM
  - BvbFPzLjWcU
  - EHwZzWd-OnQ
  - EcbgbKtOELY
  - HE4rLEQpiXY
  - Lp6ey4AyDzA
  - RCneB_MQ7qs
  - SfX43uIubj4
  - V3Omp1hm0Sg
  - VPeTgU7la34
  - Yr2uIcFZDDQ
  - ZsP20PN14O0
  - adev-changelog
  - adev-home
  - eMMiLeo_UGI
  - ek-7-practical-animation-tips
  - ek-agents-with-taste
  - ek-building-a-drawer-component
  - ek-building-a-toast-component
  - ek-building-an-animation-course
  - ek-developing-taste
  - ek-friction-as-a-feature
  - ek-the-magic-of-clip-path
  - ek-train-your-judgement
  - ek-you-dont-need-animations
  - eks-readme
  - eks-skills-apple-design-skill
  - eks-skills-emil-design-eng-skill
  - eks-skills-find-animation-opportunities-skill
  - eks-skills-prototype-skill
  - eks-skills-review-animations-skill
  - eks-skills-review-animations-standards
  - kdRkuqu8apE
  - neE6wOuBIP8
  - pGYLZyBE32o
  - tNMAFjzapOk
  - ulSOdTgoGeY
tags:
  - od-area-process
---

# Design taste and judgement

## In short

Taste is not personal preference: it is a trained ability to see what makes a design better, and with practice you can say why. Emil Kowalski's sources, which are locked house standards here, teach it by looking at great work, comparing two versions side by side and writing down why one feels better, and they say that small details nobody consciously notices add up to software that feels right. Kole Jain's videos agree that function comes before looks and that restraint usually wins, but they also warn that a design can follow every rule and still feel boring or soulless, so one well-chosen distinctive touch matters. Galleries such as Dribbble are useful for ideas but often reward looks over sense, and a Mobbin review of 2,108 dashboards found that the memorable ones were not the prettiest but the ones that knew what to leave out. Judgement matters more now that AI can build anything quickly, because someone still has to decide what is good enough to ship.

## House standards

- `STD-process-review-taste-51` (should): train taste on the best work: build a curated list of respected tastemakers (and the people they admire) and study their designs, apps and books.
- `STD-process-review-taste-52` (should): explain why something feels great or wrong and name the pattern behind it, instead of labelling it good or bad.
- `STD-process-review-taste-53` (should): practise by making things, ask the right person for critique, and keep going when early work falls short.
- `STD-process-review-taste-54` (should): train motion judgement with side-by-side pairs: pick the better one and write down why before reading an expert's breakdown.
- `STD-process-review-taste-50` (should): a product that merely works is not finished; go the extra mile.
- `STD-process-review-taste-01` (must): never ship motion, AI-written or not, just because it runs.
- `STD-visual-details-50` (should): polish the small details users will not consciously notice, such as native-feeling behavior.
- `STD-visual-details-51` (should): make the default design and motion of a component excellent before adding options.
- `STD-visual-details-27` (should): make every spacing, timing and alignment value a deliberate choice you can defend.
- `STD-visual-details-29` and `STD-visual-details-30` (should): make the most important thing the most obvious, and aim for simplicity, not minimalism: strip what is unnecessary and make every element earn its place.
- `STD-visual-details-44` (should): decide what not to build, and spend the user's time, attention and trust only on what pays off.
- `STD-visual-details-37` (should): break a familiar pattern only when you can prove the new one is better.
- `STD-visual-details-47` (should): decide the emotion people should feel and reinforce it in every decision.
- `STD-when-to-animate-03` and `STD-when-to-animate-16` (must): every animation needs a named purpose ("it looks cool" is not one), and expect to reject most candidates when looking for places to add motion.
- `STD-easing-duration-13` (must): motion fits the product's personality: a crisp dashboard gets fewer, subtler, faster animations than a playful consumer app.
- `STD-process-review-taste-37` (must): prototype variants must each be a direction you could defend shipping.

## What the sources teach

### Taste is trained, and it can be explained

- Taste is a trained instinct for recognising what elevates a design, not personal preference. Train it in three steps: surround yourself with great work from a curated list of tastemakers, work out why something feels great instead of calling it good or bad, and practise the craft with critique from the right person. Early work falling short of your own standard is expected (the "taste gap") [S-L19-008] ([[sources/ek-developing-taste-developing-taste|Developing Taste]]).
- Almost every taste decision has a logical reason. An element should grow from `scale(0.95)`, not `scale(0)`, because nothing in the real world appears from nothing; with experience you can say why, not just feel it [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]).
- Judgement is the ability to spot what is wrong, name it and fix it. It is trained with pairs of animations side by side: interact with both, pick one, write down why, then read the expert's breakdown [S-L19-011] ([[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]]). The course frames the problem as the feeling that "it just doesn't feel right and you can't tell why" [S-L19-002] ([[sources/adev-home-animations-dev|animations.dev (home)]]), and runs more than 25 such exercises [S-L19-001] ([[sources/adev-changelog-animations-dev|animations.dev (changelog)]]).
- Animation skill is learnable, not magic [S-L19-003] ([[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]). The right judgement is the biggest differentiator when software is abundant [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- Taste changes quickly while you learn: the presenter's portfolio from about three years earlier had huge animations and giant text, and his current one is more refined, with smaller animations [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]).
- Some judgement stays approximate. Hierarchy is "not an exact science", and a different layout can still be right if the key ideas hold [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]); arranging decorative elements involves "a lot of eyeballing" [S-L19-063] ([[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]); and even Emil's review standards say the balance of opacity and height in an entering list has no formula and needs trial and error [S-L19-033] ([[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]).

### Small details add up

- Beauty is an underused lever in software. Small details users never notice (pausing a toast's timer while its tab is hidden, filling the gaps between expanded toasts so the pointer never loses its hover state) add up, and the fewer details users notice, the more intuitive the experience [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- Invisible details feel invisible because they match what people already expect; when they are missing, the component feels off [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]). Small, unnoticed details still add up to an experience that feels more polished [S-L19-010] ([[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]).
- Small ingredients compound until an interface is either amazing or just not that great [S-L19-014] ([[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]]). Taste is trained, unseen details compound, and beauty is leverage [S-L19-023] ([[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]).
- Craft means every spacing, timing and alignment value is a deliberate choice you can defend, and delight comes from getting the other principles right first [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- The difference between a good landing page and a great one is almost never one big change; it is many small details. A page that looks like a template is one where nobody made any design decisions [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).

### Function first, then looks

- Strong designers focus on making things work for the user rather than making them look good. They respect conventions users already expect, add something unique through micro-interactions and features, and break the system's rules only on purpose [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- Busy, varied Dribbble layouts look appealing but hurt usability; usability is at the heart of everything, and simplicity has value [S-L19-040] ([[sources/6CC8lLnqa28-6-things-you-probably-need-to-hear-as-a-web-designer|6 Things You Probably Need to Hear (as a web designer)]]). Interesting layouts can be taken too far, and Dribbble shots often favor looks over usability, as some of the presenter's own choices do [S-L19-049] ([[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]).
- A dashboard that looks amazing on Dribbble can fall apart once you check whether each element and action actually means something [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- Interfaces that feel "weirdly perfect" are built to be scanned, not read: they line content up on shared edges, tell items apart with avatars, chips and icons, and keep defaults gray so only what matters gets color. The polish comes from scannability, not prettiness [S-L19-080] ([[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]).
- Beginner mistakes include skipping flow planning, overusing shadows, glows and gradients, cramped or uneven spacing, inconsistent components, poor icons, redundant elements, missing feedback and over-designed charts [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).

### Knowing what to leave out

- After going through 2,108 dashboards, Mobbin's presenter found that clear hierarchy, good spacing and useful charts make a dashboard fine but not memorable. The ones worth a screenshot "weren't the prettiest ones": they knew what to leave out. His gut check is to ask "Would I screenshot this, and why?" [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- The standouts "weren't templates": someone asked how to make the data make sense to users instantly. Examples include key insights placed beside a line chart, a heat map where darker squares mean busier hours, and an analytics dashboard that stands out simply by being clean when most look busy [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- Small, specific touches also show that someone made decisions: a birthday cake inside Cake's ownership donut chart, and a game in Mercury where an empty table would sit once all bills are paid [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- These patterns are the presenter's opinion from browsing screenshots. The video's one usage figure, that AI dashboards get about twice the saves and exports on Mobbin, shows what designers collect, not what users prefer [S-L19-110].

### Restraint

- Restraint is the defining trait of good motion work: reject most candidates, never animate because it looks cool, and treat finding nothing to add as a good result [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]). Deciding when not to animate is part of the craft; think about what the user is trying to do and how often they will see it [S-L19-012] ([[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]).
- Motion must match the component's personality; when unsure, review it in slow motion and with fresh eyes, or delete it [S-L19-032] ([[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]]).
- Keep effects subtle: preloaders short, loops simple and slow, and mouse-following effects sparing, so they add to the design instead of coming across as flashy [S-L19-069] ([[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]).
- Subtle, muted colors rather than all-or-nothing color are a sign of a more experienced designer; gradients and shadows that aren't working should go [S-L19-057] ([[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]).
- Good UI comes from structure, rhythm and "just the right surprise". Chaotic designs compete for attention; motion and ornament for their own sake make a section feel crammed rather than crafted [S-L19-084] ([[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]).
- Use the common layouts but add one distinctive touch; simple and well put together beats flashy [S-L19-066] ([[sources/VPeTgU7la34-7-modern-ui-layouts-from-50-top-software-companies-free-figma-file|7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)]]).

### Not boring, not soulless

- A good design and an interesting design are different: a site can follow every principle and still be boring. Interesting sites have more variety in layouts, colors and sizes, and more originality [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]).
- A clean, functional site can still feel soulless if it does not relate to the people it is for. The fix is a feeling that fits the brand, not a formula or a more modern look [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]).
- The skill is knowing when decoration turns into clutter and matching the vibe to the product; stripping every extra element from a busy page can leave it feeling empty rather than clear [S-L19-063] ([[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]).
- Bento layouts and 3D animation were everywhere by late 2024, and less common effects make a site feel more original; the presenter calls his own roundup "satirical" [S-L19-050] ([[sources/EHwZzWd-OnQ-7-ui-design-trends-that-are-criminally-slept-on-dont-miss-these|7 ui design trends that are CRIMINALLY slept on (don’t miss these)]]).
- Copying the Tesla-style stack of full-screen images is, in one presenter's opinion, "kind of lazy"; he prefers Rivian's site and treats tasteful hover animations as a source of premium feel [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]).
- A critique of AI company sites calls out lopsided layouts, too many tabs, tiny text and redundant pages, and rejects its own ideas when they look messy against the brand's clean style [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).

### Judging options

- When comparing variants, each must be defensible on its own; if two converge, cut one and say so; and any recommendation rests on the product's personality and how often the piece is used, not on looks alone [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).
- Friction used to force judgement about what was worth building; without it, output feels meaningless and undesigned [S-L19-009] ([[sources/ek-friction-as-a-feature-friction-as-a-feature|Friction as a Feature]]).

## Where they agree and disagree

Between the sources:

- **Taste can be learned:** Emil's sources say so directly [S-L19-008] [S-L19-003] [S-L19-011], and Kole's changing portfolio shows it [S-L19-043].
- **Explain it, or eyeball it:** Emil holds that almost every taste decision has a nameable reason [S-L19-004] and that every value should be defensible [S-L19-020]. Kole admits much is eyeballed [S-L19-063] and that hierarchy is not exact [S-L19-052], and one of Emil's own sources says one motion balance has no formula [S-L19-033]. Both can hold: the reason can be named even when the exact value is found by trying [inferred].
- **Restraint versus interest:** restraint runs through [S-L19-024] [S-L19-012] [S-L19-069] [S-L19-057] [S-L19-084], while [S-L19-085] [S-L19-062] [S-L19-050] push for variety and originality. They meet in "one distinctive touch" [S-L19-066] and "just the right surprise" [S-L19-084].
- **Dribbble:** used for inspiration in several videos, but warned against as a guide to usability [S-L19-040] [S-L19-049] [S-L19-068].
- **Pretty is not the point:** Mobbin's dashboards worth a screenshot were not the prettiest but knew what to leave out [S-L19-110]; Kole's "weirdly perfect" interfaces owe their polish to scannability, not prettiness [S-L19-080]; and a Dribbble dashboard falls apart once each element is checked for meaning [S-L19-068].
- **Templates show:** "you can tell these weren't templates" [S-L19-110] matches the landing-page video's point that a page looks like a template when nobody made any design decisions [S-L19-072], and the advice to add one distinctive touch to common layouts [S-L19-066].
- **A gut check that asks why:** the screenshot test is a gut check, but it ends in "and why?" [S-L19-110], so it still asks for a reason, as `STD-process-review-taste-52` does [inferred].
- **Delight in a data screen:** the cake in a donut chart and the game after all bills are paid [S-L19-110] are delight inside data screens; the video does not say how either moves. Wherever they animate, `STD-when-to-animate-09` would limit them to rare or first-time moments such as success states, and `STD-when-to-animate-11` keeps decorative motion off charts people are reading [inferred].
- **Hover and button motion:** Kole wants small hover interactions on almost everything on a simple site [S-L19-063], sees tasteful hovers as premium [S-L19-065] and says buttons should almost always have a small animation [S-L19-054]. `STD-when-to-animate-07` says anything seen tens of times a day, including hover and press feedback, should be removed or reduced to near-imperceptible motion. A marketing site visited occasionally is a different frequency tier from an app used daily, so the two can coexist, but in product UI the standard wins [inferred].

Against OpenDesigner's existing research:

- **Name the principle:** DC-L15-11's "coach" mode ties every message to a named principle so people learn the vocabulary, the same move as `STD-process-review-taste-52` and [S-L19-011].
- **Spend boldness in one place:** DC-L17-06 keeps most of a product conventional and concentrates distinctiveness in two or three places, which matches [S-L19-066] and [S-L19-054]. DC-L13-17 likewise defaults to conventional behavior with a custom look.
- **Taste rules warn, accessibility rules fail:** DC-L17-07 lints for generic looks with waivers; taste rules only warn, while accessibility rules block. That fits the practitioner opinions here, which are advice rather than hard rules [inferred].
- **Looks are not usability:** OpenDesigner's guardrails (section 7) forbid automating "treating attractiveness as usability", which agrees with [S-L19-080]'s point that polish comes from scannability, not prettiness [inferred].
- **Principles as words:** DC-L11-05 warns against principles built on words any product could claim ("simple", "beautiful"), in line with Emil's point that taste should be explained, not labelled [inferred].
- **Leaving things out on dashboards:** DC-L19-48 ranks every module before placing it, and the finance redesign cuts what adds no value [S-L19-068]. Mobbin's "knew what to leave out" [S-L19-110] reaches the same place from a different direction: from what people remember rather than from a priority audit [inferred].
- **Charts chosen for the data:** DC-L19-122 keeps a fixed chart set by default, with the heuristic "if the chart needs its caption to be read, fix the chart". Mobbin's standouts go further, picking a visual that fits the data, such as a live map with one dot per visitor or an hours heat map [S-L19-110]. The two fit together: the fixed set covers most cases, and a fitted visual is an exception worth recording with its reason (DC-L19-165) [inferred].

## Decisions this informs

- **Q-pref-01** (planned, not asked yet: how strict the critique is): naming the principle behind each note [S-L19-008] [S-L19-011] backs `coach`.
- **Q-brand-07** (principles that break ties): decide the emotion first (`STD-visual-details-47`); break the system's rules only on purpose [S-L19-054].
- **Q-plat-10** (usual behavior, own look, or something new): conventions plus one distinctive touch [S-L19-054] [S-L19-066] back `custom-skin`.
- **Q-brand-04** (how lively) and **Q-motion-01** (how motion feels): the restraint sources favor `hero-moments` or `productive` over `expressive` for Q-brand-04, and `productive` or `two-mode` over `springs` for Q-motion-01; delight is kept for rare moments (`STD-when-to-animate-09`) [inferred].
- **Q-dir-01** (overall look): "simple and well put together beats flashy" [S-L19-066]; a `maximal` look needs a reason tied to the brand's feeling [S-L19-062] [inferred].
- **Q-ref-01** (a reference you like): point to work by respected tastemakers and say why it feels great [S-L19-008]; prefer references that make sense over gallery shots that only look good [S-L19-068] [S-L19-110].
- **Q-viz-01** (which charts): the default `core-6` covers most needs; a chart built for how users will read that data instantly [S-L19-110] is an exception to record with its reason [inferred].
- **Q-pattern-04** (what an empty screen shows): the source contrasts Mercury's game with an empty table once everything is done [S-L19-110], a "user-cleared" case of `empty-kinds`.
- **Q-pref-01** (planned: how strict the critique is): "Would I screenshot this, and why?" [S-L19-110] could be one of the `coach` prompts at the end of a screen review [inferred].

## Visual examples worth showing

- A pair of animations side by side for one exercise, such as a toast with two easings or a menu opened and closed rapidly [S-L19-011] ([[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]]). The captured text has the prompts but not the author's verdicts.
- An element entering from `scale(0)` beside the same element entering from `scale(0.95)` [S-L19-004] ([[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]).
- Sonner's invisible details: a toast that stays put while its tab is hidden, and the gaps between expanded toasts filled (shown as dark bars) so hovering over a gap keeps the stack open [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- A store receipt held together by two edges, and a checklist improved with avatars, due-date groups and chips instead of more white space [S-L19-080] ([[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]).
- A crammed landing page beside a restrained, grid-driven one [S-L19-084] ([[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]).
- The same site as "good" and as "interesting": varied columns, broken boxes, treated photos and size contrast [S-L19-085] ([[sources/ulSOdTgoGeY-awful-to-amazing-web-designs-easily|Awful To AMAZING Web Designs Easily]]).
- A restaurant-software site with no images beside its redesign built from one moody image [S-L19-062] ([[sources/RCneB_MQ7qs-the-one-thing-vibe-coding-cant-fix-about-your-website|The one thing vibe coding CAN’T fix about your website]]).
- A Dribbble-style finance dashboard beside a version where every card has a purpose and a priority [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- The presenter's old, everything-moving portfolio beside his current one [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]).
- A plain line chart beside the same chart with key insights next to it, and a busy analytics dashboard beside a very clean one [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- An ownership donut chart with a birthday cake inside it, and a paid-up bills screen showing a game instead of an empty table [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).

## Open questions

- The "Train your judgement" exercises were captured without their answers. A re-capture that includes the breakdowns would turn the training dimensions into checkable rules [S-L19-011].
- How should OpenDesigner help a person build their own list of tastemakers (`STD-process-review-taste-51`) during a short interview?
- Where exactly is the line between a marketing site's occasional hovers and product UI's frequent ones, for `STD-when-to-animate-07`?
- Can "interesting" be measured at all, for example as layout variety across sections, or does it stay a human judgement?
- The screenshot gut check [S-L19-110] comes from one person browsing a reference library. Would the answer to "and why?" match what users of the product remember, and how could OpenDesigner find out?
