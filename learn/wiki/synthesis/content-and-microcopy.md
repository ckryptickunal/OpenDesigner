---
type: synthesis
title: Content and microcopy
created: 2026-09-24
updated: 2026-09-28
sources:
  - 9WVt1CelBfg
  - 59XWYgN00nQ
  - BUDipdbKK7Y
  - SfX43uIubj4
  - HE4rLEQpiXY
  - ToJiXPTNnLY
  - Yr2uIcFZDDQ
  - eMMiLeo_UGI
  - eks-skills-apple-design-skill
  - V3Omp1hm0Sg
  - eks-skills-prototype-skill
  - goWOAFqJHpA
  - gKM6b2EnW1k
  - pGYLZyBE32o
  - 9ypqs_2fAl8
  - ARq1bx3Sfg8
  - YbLF42BaoZs
  - Qsq-Sj_rojU
  - qK7WYCMvjUw
tags:
  - od-area-content
---

# Content and microcopy

## In short

Words make up most of a screen, so they deserve the same care as the visuals. Keep copy short, plain and specific: say how the product helps, put a label on every number, and name things after what they contain. Design with realistic content, never placeholder Latin, and test it with messy real content such as very long names. At the moments people decide, such as a sign-up screen, a paywall or a streak, small wording changes can change results: sell the outcome, reassure people they can cancel, and never shame or scare them. Emil Kowalski's rules here are house standards; the rest comes from Kole Jain's redesign videos and Mobbin's studies, where each number is one company's reported result, not a law.

## House standards

- **STD-visual-details-35** (should): keep interface copy concise: plain language, no jargon and fewer steps.
- **STD-visual-details-34** (should): name navigation items for their contents (for example "Progress", "Library"), not with vague umbrellas such as "Home".
- **STD-visual-details-03** (must): write the single ellipsis character (…) in markup and UI strings, never three periods.
- **STD-process-review-taste-40** (must): every prototype variant fully works, with realistic, product-shaped copy and plausible names and numbers; no lorem ipsum, dead buttons or "imagine this part" placeholders.
- **STD-process-review-taste-37** (must): prototype variants are named for their direction (for example Quiet, Editorial, Playful, Dense), never Option A/B/C.
- **STD-process-review-taste-48** (must): hand off prototype variants with one honest line on when each wins and one on what it costs, without pre-picking a favourite.
- **STD-process-review-taste-67** (should): the first screen people see after signing up is part of the product's packaging; it sets the tone and shows the care to expect.

Two of these are now checked by `engine.py review` (standards version 2, checked on 2026-09-28): STD-visual-details-03 flags three periods in UI text, and STD-process-review-taste-40 flags "lorem ipsum" and buttons whose handler does nothing.

## What the sources teach

### Short, direct copy

- By Kole's estimate text is about 80% of most websites, and plain paragraphs are neither fun nor interesting, which is why he animates key words and rewrites corporate lines [S-L19-063] ([[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]).
- Short hero copy communicates fastest. The landing page he takes apart uses a seven-word heading and a 14-word subtext [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]); the counts come from that one site.
- Cut vague, long blocks of text, because no one stops to read them, and don't repeat the company name when it is already on screen [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]). Headlines should get shorter and punchier as a page matures [S-L19-072]; Kole borrows the punchy headline style of the Chrome site for a Gemini redesign [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- Remove text that repeats an image or stats shown higher up, and cut the page to the length it needs [S-L19-065] ([[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]). Replace long accordion text with pictures and short paraphrased copy that links to the full specs, and tuck long but important text behind a "see more" control [S-L19-065].
- A portfolio intro should state your name and what you do, with no fluff [S-L19-064] ([[sources/ToJiXPTNnLY-professional-portfolio-breakdown-why-is-theirs-so-much-better|Professional Portfolio Breakdown — Why Is Theirs So Much Better?]]).
- Be concise: plain language, no jargon, fewer steps [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).

### Sell the outcome, not only the features

- The copy step from Kole's level three to level four is moving from what the product does to how it helps: collecting and analysing data quickly becomes turning that data into decisions [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).
- The strongest onboarding welcome screens sell the outcome instead of listing features, for example by showing the product in action (Timehop). Sometimes this is only a copy tweak: Superhuman turns a plain sign-up screen into a pitch, with customer logos beside the form as social proof [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- A paywall at the end of onboarding should read as its natural last step: tell people their plan is ready and speak to the outcome they want, such as feeling like themselves in 4 weeks [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Value framing matches the words to what each audience cares about, so the studied paywalls each sell a different future. Price anchoring is framing too: Tide breaks the price into weekly amounts, and Ahead compares its subscription with coffee or therapy [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Merge landing pages that sell the same thing into one page built on the few points they share (for Gemini's paid tiers: the cost, a better AI and document uploads) [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- Products that handle people's data need a privacy section on their landing page [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).

### Words at the moment people decide

- A "no commitment, cancel anytime" subtitle under the paywall button always seems to do well and bumps conversion up a little, in paywall designer Jonathan Parra's experience [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]). A later Mobbin episode replays a clip of an earlier guest making the same claim [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]); the wording matches, so it is most likely the same person, not a second opinion [inferred].
- Button labels: Jonathan finds a call to action that names what the user is doing, instead of a plain "Continue", hit or miss, so he keeps testing it [S-L19-104]. Duolingo's team changed "continue" to "commit to my goal" and called it a massive win, and the streaks video says more apps now reframe calls to action as a promise you make to yourself [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).
- Paywall headlines: Moonly tested eight title and subtitle variants, and changing only the words raised conversion by 12% [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- Social proof: Moonly's founder recommends always adding it, such as download counts and reviews [S-L19-111]; the paywall study names real reviews with a five-star rating as one of the most common framing techniques [S-L19-104].
- Offer extras only when they help: Moonly's AI assistant recommends an add-on only when that specific one can really help the user at that moment [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

### Tone in onboarding and first use

- Write quiz questions conversationally: Dollar Shave Club made its quiz copy more conversational, which alone led to a 5% increase in subscriptions [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- Explain as people go instead of front-loading everything: Cake Equity makes equity and vesting approachable with copy that reassures people from time to time and tooltips that state the impact of each step. Small guidance such as a line of microcopy or a progress indicator removes reasons to get stuck [S-L19-107].
- A human touch: One Year's onboarding includes a founder's note with a handwritten signature, and Basecamp shows a personal note from its CEO after account creation, which makes the product feel made with intention [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).

### Friendly, human voice

- Write friendly, natural copy instead of corporate jargon: a site that says it "sweats the details" beats "we take pride in our attention to detail", and Basecamp's whole site is written in easy, natural language [S-L19-063] ([[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]).
- A 404 page is the ultimate place to be quirky, because the visitor does not belong there; it can reuse the site's personal copy [S-L19-063] ([[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]).
- On a portfolio, an honest about page and a line of personality make you memorable, even when some visitors disagree [S-L19-064] ([[sources/ToJiXPTNnLY-professional-portfolio-breakdown-why-is-theirs-so-much-better|Professional Portfolio Breakdown — Why Is Theirs So Much Better?]]).

### Honesty, and never shaming or scaring the user

- State real billing terms on a pricing card so people do not feel misled when they find out what they actually pay (his example: it is really $20 a month) [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- In prototypes, sell each variant honestly: one line on when it wins, one on what it costs [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).
- Do not shame people about their usage: Kole's joke redesigns show a usage message about 342 watched videos whose only choices are an upsell or more notifications, and a fitness message saying you would need to run a marathon today to hit your goal. The first mostly made him angry, and he held back from adding more to the second because it would go from passive-aggressive to plain aggressive [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- Streak copy can lean on fear or on optimism. Fear-based streak screens make the copy more urgent, start a countdown and show a mascot that makes you feel guilty; optimism-based ones use positive, encouraging copy [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]). The video describes both rather than endorsing fear, and asks whether streaks build habits or just make people afraid to stop [S-L19-105].
- Pressure wears out: when every app uses fake urgency, users eventually stop believing it [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]). In a Mobbin demo, the brief asked where an offers nudge could go without feeling manipulative, and the AI agent put it on the home page right after onboarding, citing an app that does the same [S-L19-108] ([[sources/YbLF42BaoZs-i-gave-claude-600-000-ui-screens-then-this-happened|I Gave Claude 600,000 UI Screens… Then This Happened]]).
- People prefer a few familiar categories to strange, hyper-specific AI-generated labels; Spotify's AI genre names were not well received [S-L19-076] ([[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]).

### Labels, names and numbers

- Name navigation items for what they contain ("Progress", "Library"), not with a vague "Home"; direct, specific labels create predictability [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]). If a control needs a label to explain it, its placement and mapping are weak [S-L19-020].
- Label every chart and number; without labels the numbers mean nothing [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]). Show the figures that matter for the real object, such as a minimum payment and a due date on a credit card instead of a monthly fee, and retitle a card when its content changes [S-L19-068].
- Don't label a screen with what it obviously is, such as a "financial dashboard" heading [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]). Replace an unclear icon with a labelled button such as "all activities" [S-L19-068].
- Add context to a big number: a comparison with last year (for example a 120% increase) or a friendly line such as "you two just met" when the artist is new [S-L19-076] ([[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]).
- When two buttons go to the same place, give them the same label; matching labels build the right mental model [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).
- Make a pricing card's button label more actionable, and give each plan a name and a short description [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]). On repeated cards the whole card can be the link, but keep an explicit button when there is a specific action such as "Try it out" [S-L19-075].
- Forms: put labels above the inputs where they stay visible, because a label used as placeholder text disappears while typing; fill the empty input with a realistic example instead; add a "Create account" subheading so a sign-up is not mistaken for a login [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- Tab bars need text labels when the icons are obscure (Apple Music) and can skip them when the icons are familiar (Instagram); labels must be dark enough to read [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- Name prototype variants for their direction, never Option A/B/C [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).

### Real content, not placeholders

- Make every design as realistic as possible, with absolutely no lorem ipsum, and start from a written brief [S-L19-037] ([[sources/59XWYgN00nQ-create-a-portfolio-with-no-experience-or-clients-needed|Create A Portfolio With No Experience (or clients) Needed]]).
- Prototype variants use realistic, product-shaped copy with plausible names and numbers [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).
- Choose what a card shows from how people use it (location, rating and price on a listing card, the long description on the page it opens), then test the layout with imperfect content such as a very long destination name, and truncate it [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- Research real products before writing: an AI connected to a library of shipped app screens can distill how the best apps in a category differ in copy, and suggest copy tailored to your users that cites where each idea came from [S-L19-108] ([[sources/YbLF42BaoZs-i-gave-claude-600-000-ui-screens-then-this-happened|I Gave Claude 600,000 UI Screens… Then This Happened]]). This is Mobbin demonstrating its own paid product.

## Where they agree and disagree

**Between the sources**

- All of them want less text: short hero copy [S-L19-043][S-L19-072][S-L19-082], no repeated or padded text [S-L19-065][S-L19-072], concise intros [S-L19-064] and plain language [S-L19-020][S-L19-063].
- "Sell the outcome" runs from marketing into the product: how the product helps on a landing page [S-L19-072], outcome-first welcome screens [S-L19-107] and outcome-first paywalls [S-L19-104].
- Realistic content is shared ground: Kole's portfolio advice [S-L19-037] and Emil's prototype rule [S-L19-031] both ban lorem ipsum. Kole adds a stress test with messy real content [S-L19-054], which goes a step beyond "plausible" copy [inferred].
- Same words or specific words? Kole gives two buttons that go to the same place the same label [S-L19-072], while the Mobbin sources replace a generic "Continue" with a label that names the action or a commitment [S-L19-104][S-L19-105]. Both can hold: the same destination gets the same words, and a decisive step gets its own verb [inferred].
- Length on conversion screens is something to test, not a rule. The paywall study reports an ugly, compact, text-heavy squeeze page that beat almost every polished paywall for one app, and says there is no universal best paywall, only better experiments [S-L19-104]. That sits beside Kole's steady push for less text [S-L19-072][S-L19-065]. A longer tested variant can carry more information, but its wording still has to stay plain and concise under STD-visual-details-35 [inferred].
- Honesty means different things. Honesty about yourself or your product is praised: a brutally honest portfolio note [S-L19-064], honest billing text [S-L19-075], honest trade-off lines [S-L19-031], and reassurance that people can cancel [S-L19-104]. A "brutally honest" judgement of the user's own behaviour is the anti-pattern [S-L19-048]. The line seems to be whose behaviour the copy judges [inferred].
- Reassurance beats pressure in every source that weighs the two: fake urgency stops working once everyone uses it [S-L19-104], fear and guilt streak copy is described without being recommended [S-L19-105], and usage shaming makes people angry [S-L19-048]. "Commit to my goal" is filed under optimism in its source [S-L19-105]; whether commitment wording turns into pressure depends on what happens when someone does not commit [inferred].
- Personality versus restraint: Kole wants a quirky 404 [S-L19-063] and personality on a portfolio [S-L19-064], but his joke redesigns show sass aimed at users backfiring [S-L19-048]. Playfulness works when it is aimed at the situation, not at the person [inferred].
- The measured copy wins (5% more subscriptions from a conversational quiz [S-L19-107], 12% more conversion from paywall wording [S-L19-111], Duolingo's "massive win" [S-L19-105]) are single-company reports with no sample sizes or test details, as each analysis's caveats say. They are ideas to test, not defaults.
- The "cancel anytime" subtitle appears in two videos [S-L19-104][S-L19-111], but the second replays an earlier guest's clip, so it counts as one voice [inferred].

**With OpenDesigner's existing research**

- Voice, DC-L06-18: 3-4 traits, each with a "but not", and plain language without jargon as an accessibility constraint. This agrees with friendly, non-corporate copy [S-L19-063] and STD-visual-details-35 [S-L19-020].
- Tone, DC-L06-19: errors are serious, respectful and matter-of-fact, and "once may amuse, but a dozen times may annoy". A quirky 404 [S-L19-063] conflicts with the "errors serious" default unless a 404 is treated as a rare, low-stakes moment; DC-L19-37 proposes exactly that, with a plain way back, and aims humour at the situation, never at the person. The shaming messages [S-L19-048] and the guilt-inducing streak mascot [S-L19-105] are what these cards guard against [inferred]. DC-L06-19 has no separate first-use row, but conversational wording in a first-use quiz [S-L19-107] fits the first-use tone that Q-voice-02 asks about [inferred].
- Microcopy, DC-L06-22: verb-first buttons, consistent flow vocabulary (Get Started, Continue or Next, Done) and empty states with a next step. Verb-first buttons agree with matching labels for the same destination [S-L19-072] and actionable button labels [S-L19-075] [inferred]. The consistent "Continue" is where the Mobbin sources push back: at a paywall or a goal screen they test a specific or commitment label instead [S-L19-104][S-L19-105]. DC-L19-38 proposes that exception for goal, plan and trial steps only.
- Readability, DC-L13-13: 6th-8th grade for consumers, 10th-12th for experts, button labels of 2-4 words, verb first, naming the result. None of these sources gives a reading grade; the seven-word example [S-L19-043] is a headline, not a button. "Commit to my goal" is four words, verb first, and names what the tap means, so it fits the card [inferred].
- Deceptive patterns, DC-L13-15: its enforced lint covers fake urgency, confirmshaming and a cancel flow with more steps than sign-up. The paywall study's warning about fake urgency [S-L19-104] and the urgent-copy-plus-countdown streak screen [S-L19-105] are the patterns it targets [inferred]; ClassPass, which takes fewer than five screens to subscribe and 17 to cancel [S-L19-104], is its "hard to cancel" case.
- Marketing copy, DC-L19-36: short, outcome-first headlines, first built from Kole's videos and now extended from landing pages to welcome, onboarding and paywall screens with the Mobbin sources [S-L19-107][S-L19-104][S-L19-111]. It treats copy length on conversion screens as something to test.
- Onboarding, DC-L19-129: it already says to reassure people before asking for data (a message before connecting a bank), which agrees with reassuring copy and tooltips [S-L19-107]. The card predates the Mobbin onboarding study and does not cite it (checked 2026-09-28).
- Paywalls and upsells, DC-L19-135: it rests mainly on the satire video [S-L19-048] and cites none of the new Mobbin paywall sources yet (checked 2026-09-28). Their practitioner advice (a reassuring subtitle, social proof, value framing, no fake urgency) [S-L19-104][S-L19-111] fits its default that an upgrade prompt says what the next plan adds [inferred].
- Streaks, DC-L19-136: it rejects punishing a broken streak [S-L19-048]; the streaks video agrees that flexibility beat pressure at Duolingo [S-L19-105], though that finding is about the mechanics, not the wording.
- Numbers, sample content and punctuation: DC-L19-33 (a label and context for every key number), DC-L19-35 (realistic sample content with a long-string case) and DC-L19-39 (typographic punctuation, with the ellipsis locked) already turn this page's older sources into proposals.
- Form labels, DC-L13-05: placeholder-as-label is rejected, with a visible label above every field. This agrees with Kole [S-L19-075]; Q-form-01 offers `label-top`.
- Error messages, DC-L13-07: blame-free, "what happened, then how to fix it". This agrees in spirit with avoiding guilt-tripping copy [S-L19-048] [inferred].
- Icon labels, DC-L05-07: label everything in navigation and allow icon-only only for about a dozen universal actions. Kole accepts icon-only tab bars when the icons are familiar [S-L19-075]; the Q-icon-05 default (`labels-default`) follows the card.
- Terminology, DC-L06-23: a word list from day one. Kole's preference for a few familiar category names over invented ones [S-L19-076] points the same way [inferred].
- Capitalisation, DC-L06-20 (sentence case by default): no source here speaks to case.
- STD-process-review-taste-40 in OpenDesigner itself: `engine.py`, the other scripts and the visual templates in `skills/opendesigner/assets/templates/` contain no lorem ipsum (text search re-run on 2026-09-28), and `engine.py review` now flags it in a person's code.

## Decisions this informs

- **Q-voice-01** (voice guide or 3-4 traits): friendly and natural, not corporate [S-L19-063]; honest with a line of personality [S-L19-064]; plain language without jargon [S-L19-020]; a human touch such as a founder's note [S-L19-107].
- **Q-voice-02** (tone for errors, success and first use): never shame people about usage [S-L19-048]; a quirky 404 [S-L19-063]; warm comparison lines for good news [S-L19-076]; conversational, reassuring first-use copy [S-L19-107]; encouraging rather than urgent streak copy [S-L19-105].
- **Q-voice-03** (sentence or title case): no source in this set addresses it; the default stays with DC-L06-20.
- **Q-voice-04** (reading level): short, plain copy [S-L19-020][S-L19-043][S-L19-072]; the sources give no grade numbers; "commit to my goal" [S-L19-105] fits the `labels-2-4` option [inferred].
- **Q-voice-05** (writing rules): the ellipsis character (STD-visual-details-03); every number gets a label and context [S-L19-068][S-L19-076].
- **Q-voice-06** (rules and word lists per component): specific navigation labels (STD-visual-details-34) [S-L19-020]; matching labels for the same destination [S-L19-072]; actionable button labels, plan names, "Create account" subheadings [S-L19-075]; familiar category names [S-L19-076]; labelled buttons instead of unclear icons [S-L19-068]. The `flow-vocab` option ("the same step words everywhere") needs an exception for decisive steps if the specific-label findings are adopted [S-L19-104][S-L19-105].
- **Q-pattern-04** (empty screens and first-time learning): `onboarding-contextual` matches reassuring copy, tooltips and microcopy at each step [S-L19-107].
- **Q-pattern-05** (how firmly to stop design tricks; planned, default `enforced`): fake urgency [S-L19-104] and guilt-driven streak copy [S-L19-105] are the kind of copy it would catch.
- **Q-form-01** (field style and label position): labels above inputs, realistic example text inside [S-L19-075].
- **Q-icon-05** (when icons get words): tab-bar labels depend on how obscure the icons are, and must be dark enough to read [S-L19-075].
- **Q-scope-05** (where to start): starting from a written brief keeps the content realistic [S-L19-037]; research how shipped apps in the same industry handle the flow, including its copy, before designing it [S-L19-108].

## Visual examples worth showing

- **A short hero**: a seven-word heading over a 14-word subtext, from Kole's landing-page teardown [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]).
- **"What it does" versus "how it helps"**: the same analytics feature written both ways, from his level three and level four pages [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).
- **"Continue" versus "Commit to my goal"**: the same button with Duolingo's two labels [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).
- **Fear versus optimism**: a streak screen with urgent copy, a countdown and a guilty mascot next to one with encouraging copy and collectible milestones, shown as a "don't" and a "do" [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).
- **A reassuring paywall button**: Jonathan's main button with a "no commitment, cancel anytime" subtitle and a right chevron [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- **An end-of-onboarding paywall**: "your plan is ready" with the outcome the person asked for [S-L19-104], and price framing as weekly amounts (Tide) or against coffee and therapy (Ahead) [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- **A sign-up screen as a pitch**: Superhuman's form with customer logos beside it [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- **Reassuring copy and tooltips**: Cake Equity's equity and vesting steps, each explaining its impact, and One Year's handwritten founder's note [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- **Matching button labels**: a nav button and a hero button with the same label, against a version where they differ [S-L19-072] ([[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]).
- **Corporate versus friendly**: "we take pride in our attention to detail" next to "we sweat the details" [S-L19-063] ([[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]).
- **Sign-up form before and after**: labels as placeholders, then labels above the inputs, example text inside and a "Create account" subheading [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- **Pricing card upgrade**: plan name and description, check marks, an honest billing note and an actionable button [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- **Numbers with and without labels**: an unlabeled chart next to the labelled one, and a credit-card widget showing minimum payment and due date [S-L19-068] ([[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]).
- **A stat with context**: a top-artist figure with "120% increase from last year", or "you two just met" for a new artist [S-L19-076] ([[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]).
- **Specific versus generic navigation labels**: "Progress" and "Library" against "Home" [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).
- **Long-name stress test**: a listing card with a very long destination name, shown overflowing and then truncated [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- **What not to write**: the 342-videos usage message and the marathon step-goal message, shown as a "don't" pair [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Copy and graphics as one idea**: a privacy section headed "unparalleled privacy" drawn with two lines that are deliberately not parallel [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- **Variant naming**: a prototype picker reading Quiet, Editorial, Playful, Dense instead of Option A, B, C [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).

## Open questions

- Should a 404 page be playful, as Kole argues [S-L19-063], when DC-L06-19 makes errors serious by default? DC-L19-37 proposes treating "you are lost" pages differently from errors that cost people work; Q-voice-02 has no such option yet.
- Icon-only tab bars: follow Kole's "only if the icons are familiar" [S-L19-075] or keep DC-L05-07's "label everything in navigation"?
- Is there a word budget for headlines? The only numbers (7 and 14 words) come from one example page [S-L19-043]; DC-L13-13 sets limits for buttons only, and DC-L19-36 proposes one idea per headline, sized to two or three lines at the heading measure rather than to a word count.
- Does "say how it helps" [S-L19-072] apply to everyday product copy? The Mobbin studies apply it to welcome screens and paywalls [S-L19-107][S-L19-104], but nothing here covers ordinary working screens.
- What should a good progress or usage nudge say? The sources show the bad versions [S-L19-048] and describe optimism-based streak copy as positive and encouraging [S-L19-105], but give no worked example beyond one button label.
- Should Q-voice-06 `flow-vocab` allow a specific or commitment label at decisive steps, and who decides when "Continue" becomes a promise?
- Should Q-pattern-05's enforced lint flag urgent copy paired with a countdown on streak and paywall screens [S-L19-105][S-L19-104], or only countdowns with no real deadline, as DC-L13-15 lists?
- Should a pricing or paywall component ship with a required billing-terms slot [S-L19-075] and a reassurance subtitle slot [S-L19-104], filled only when the statement is true [inferred]?
- The measured copy wins come from single companies without sample sizes [S-L19-107][S-L19-111][S-L19-105]. Should DESIGN.md present them as test suggestions rather than defaults?
- Should OpenDesigner's previews include a long-name or long-string case in the component sheet, so layouts are tested with imperfect content [S-L19-054], as DC-L19-35 proposes?
- Capitalisation, contractions, pronouns and reading grade are not covered by these sources and rest on the L06 and L13 research alone.
