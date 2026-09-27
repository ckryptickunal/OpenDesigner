---
type: synthesis
title: Retention and gamification
created: 2026-09-24
updated: 2026-09-28
sources:
  - 9ypqs_2fAl8
  - ARq1bx3Sfg8
  - BUDipdbKK7Y
  - E7RzEZ8GlHE
  - Qsq-Sj_rojU
  - goWOAFqJHpA
  - ixUq4HM4FNg
  - jSxxAFxjxbU
  - kdRkuqu8apE
  - qK7WYCMvjUw
tags:
  - od-area-patterns
---
# Retention and gamification

## In short

Retention is about why people come back to a product. A Mobbin study of 859 streak designs sorts streaks by the feeling they use (fear of losing the streak, optimism about progress, attachment to a mascot, or a visible chain of days where a gap stands out) and reports Duolingo tests where flexibility beat pressure: streak freezes and a one-lesson minimum kept more people going. Other sources add one central currency with visible progress, a social layer, sharing personal insights, a metric the product names itself, and a first session shaped by the answers people gave in onboarding. They also warn that engagement is not the same as a lasting habit, and that guilt, punishment and pressure make products maddening; OpenDesigner's research lists those among deceptive patterns. The figures are quoted by the videos without study details, so treat them as reported, not proven.

## House standards

- `STD-when-to-animate-09` (must): delight motion is spent only on rare, high-emotion moments such as success, completion and celebration, never on components used many times a day.
- `STD-when-to-animate-04` (must): the more often people see an animation, the shorter and subtler it gets, down to none; a streak screen seen daily is not a rare moment [inferred application].
- `STD-springs-gestures-61` (must): haptics and sound only for meaningful moments (success, error, commit, snap), at most one haptic per action.
- `STD-accessibility-motion-20` (must): never make a haptic the only feedback; pair it with a visual change.
- `STD-visual-details-59` (must): animate counters (such as points, a streak count or a currency balance [inferred]) with NumberFlow.
- `STD-visual-details-47` (should): decide the emotion people should feel and reinforce it in every decision instead of tacking delight on top.
- `STD-visual-details-39` (should): offer choices instead of forcing one path.
- `STD-visual-details-44` (should): spend people's time, attention and trust only on features that pay off.
- `STD-visual-details-45` (should): anticipate misuse and harm, and cut a feature whose risk outweighs its value.

## What the sources teach

### What brings people back to a streak

- Every streak design answers one question: what makes the person come back tomorrow. The video finds four levers [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]):
  - **Fear of loss:** losses sting more than equal gains feel good, so the design shows what you could lose: urgent copy, a countdown clock, a mascot that makes you feel guilty.
  - **Optimism:** encouraging copy, a call to action reworded as a promise to yourself (Duolingo changed "continue" to "commit to my goal" and called it a massive win), and collectible badges and milestones (Opal).
  - **Attachment:** a mascot that cheers you on or grows alongside you; when a digital thing seems to need you (the Tamagotchi effect), leaving feels harder.
  - **Visual attention:** days shown as a visible chain, so a gap stands out at once (the Zeigarnik effect) and filling it feels satisfying.
- Simply seeing the streak number makes people more likely to keep going, and the longer a streak runs, the more it becomes part of a person's identity, which is why some give up entirely after breaking one [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).

### The habit loop

- Dopamine responds to the prediction of a reward, so a streak only has to make the brain feel something satisfying is about to happen. Each stage of the habit loop can be designed: a cue (a reminder showing the streak number), craving (Duolingo's jingle after each lesson), an easy response (auto-progressing to the next step) and the reward. Once the reward becomes predictable the signal weakens, so apps add surprises such as animations, milestone celebrations and bonus XP [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).

### Flexibility beats pressure

- The obvious fix for broken streaks is stricter rules; Duolingo found the opposite worked. Letting people equip up to two streak freezes raised daily active learners by 0.38% (over 200,000 more people a day), and letting one lesson keep the streak alive, instead of the full daily goal, meant over 40% more people kept a 7-day streak. More apps now design around recovery: repairs, freezes, pauses and grace days [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).
- A study of people building habits over months found that missing a day had almost no effect on whether the behaviour became automatic; what may matter most is whether people come back after breaking a streak [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).

### Engagement is not a habit

- Most evidence on streaks covers engagement and retention, not lasting change, and optimising for engagement is not the same as optimising for a habit. The presenter says that at some point keeping the streak alive mattered more than learning [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).

### The parts of a gamification system

- Gamification usually hinges on one central currency (Duolingo XP, Todoist Karma) earned by the core actions; it shows what you have done and what is left (Exercism); it often has a social side (leaderboards, public badges); and rewards only work when tied to real goals [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).
- Duolingo layers XP, gems, hearts, streaks and achievements. The worked example, a savings app, keeps a streak alive with the core action, scales rewards to the size of the goal, gives badges for milestones (30 days in a row), ranks people on a local leaderboard with Duolingo-style promotion and demotion zones, and pays the currency for finishing short finance quizzes [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).

### Prove value, then personalise the first session

- The savings app's onboarding shows insights into past spending before introducing any game mechanics, and reassures people before asking them to connect a bank account [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).
- Moonly uses onboarding answers to shape the first home screen (a daily guidance card, a personalised daily program, personal transits and customised quick-access buttons); the host calls the transits a perfect hook, and the founder reports day-1 retention of 41% and day-7 of 37% [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- Replacing pop-ups and banners with a clear six-step onboarding checklist raised Mural's one-week retention by 10% relative, and the checklist stays after the first flow is dismissed. A nameable virtual pet raccoon made one 61-screen onboarding fun [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).

### A metric of your own, recaps and highlights

- Some products coin their own metric (Duolingo's streaks, Oura's readiness score, Apple's closing rings). Once a user says "I closed my rings", the video asserts, they are very unlikely to switch; it gives no data [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- Packaging stats helps them stick: Runner's post-run highlights give a sense of accomplishment, and Origin's weekly recap is easy to understand [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).

### Sharing

- In a yearly recap, keep the share action always visible because sharing is why the product succeeds; use one share button with a few scopes; show the owner's name on shared content; add a short comparison with last year under a headline stat; and do not drop features people liked in earlier years [S-L19-076] ([[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]).
- Opal shows screen-time insights as a swipeable story; when personal data looks that good, people share it [S-L19-110] ([[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]).
- People share insights about themselves, not features: when someone takes a screenshot in Moonly, a ready-made flow shares it in one tap; the founder says 23% of users share and it brought millions of free views [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

### Paying subscribers: retention decides

- The paywall guest wishes founders cared most about retention and lifetime value, because building something people keep paying for is much harder than getting them to subscribe [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- A high revenue per user from weekly plans can hide 90 to 95% monthly churn, so a long-term business should optimise lifetime value and retention; a discounted offer can win back subscribers who are about to cancel [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).

### Removing friction

- TikTok's main screen offers one core action, a swipe up with a target covering almost the whole screen, plus autoplay and auto-snap, so moving on needs no decision. The video reports 53 minutes a day for the average American user and eight opens a day on average (2024 figures, stated without sources) [S-L19-077] ([[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok’s UX is so GOOD it should be ILLEGAL (seriously)]]).

### What to avoid

- Do not shame people about their usage and then offer only an upsell, do not write guilt-tripping progress pop-ups, do not pair a progress warning with a nudge to lower the goal, and do not punish a broken streak. Three of the deliberately annoying features in the video still come with a way to turn them off [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- Do not answer broken streaks with stricter rules or more pressure [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).

## Where they agree and disagree

- **Streaks: reward, never punish (now with data).** [S-L19-078] uses a streak as motivation, [S-L19-048] mocks punishing a broken one, and [S-L19-105] reports Duolingo results where freezes and a lower bar beat stricter rules. This confirms DC-L19-136's rule that a missed day is never punished, which until now was inferred from satire. The Duolingo figures come from the video, not a linked study.
- **Fear as a lever.** [S-L19-105] describes fear-based streaks (urgent copy, countdowns, a guilty mascot) without endorsing them, and questions whether streaks just make people afraid to stop. DC-L19-37 aims tone at the situation, never at the person, and DC-L13-15 lists confirmshaming and addictive design among the patterns to watch, so OpenDesigner would recommend the optimism and visual-attention levers, not fear [inferred].
- **Surprises and the motion budget.** [S-L19-105] says apps layer in animations and milestone celebrations once a streak becomes routine. Milestones fit the rare moments where the house standards allow delight (`STD-when-to-animate-09`), but a daily streak screen is seen often and should stay short (`STD-when-to-animate-04`) [inferred split]. DC-L19-83 narrows hero moments to rare ones such as first run, milestones and empty states, and celebrates the milestone while only confirming the daily completion [inferred there].
- **Sound.** Duolingo's jingle after each lesson builds craving [S-L19-105]; the house rule allows sound for success and completion (`STD-springs-gestures-61`), which matches Q-motion-08's `rare-events` option rather than the default `silent` [inferred].
- **Mascots.** The research uses a mascot for warmth in empty, error and success states (DC-L06-12); [S-L19-105] shows the same device designed to raise the barrier to leaving. The difference is whether the character cheers or guilts [inferred].
- **Engagement against the goal.** [S-L19-105] separates engagement from lasting habits, and the paywall guest separates first payment from retention [S-L19-104] [S-L19-106]. Both agree with `STD-visual-details-44`: spend attention and trust only on what pays off for people [inferred].
- **Compulsive use.** [S-L19-077] admires what it calls an addictive experience; its analysis notes that designing for compulsive use is an ethical choice the video does not weigh. The research notes that EU rules on dark patterns and addictive design are announced but not yet adopted (DC-L13-15).
- **Fewer choices.** [S-L19-077] says more options lead to worse decisions and removes them. OpenDesigner's research warns that choice overload averaged about zero across 50 studies and that Hick's law does not justify deleting options (L13 research, law table; not a Decision Card).
- **Progress displays.** Showing progress made and left [S-L19-078] and a visible chain of days [S-L19-105] match the goal-gradient effect in the research, which draws an ethics line at artificial progress that misstates the real work left (L13 research, law table) [inferred link].
- **Coined metrics.** The claim that a coined metric keeps users from switching [S-L19-110] is an assertion without data.
- **Why a gap in the chain pulls.** [S-L19-105] explains the visible chain with the Zeigarnik effect, which OpenDesigner's research marks as a failed replication; the related Ovsiankina tendency to resume unfinished tasks does hold, and the research forbids using either to justify nagging (L13 research, law table). The chain can stay; reminders cannot lean on Zeigarnik [inferred].
- **One channel.** Six of the ten sources are Mobbin videos and four are Kole Jain videos; [S-L19-104] and [S-L19-106] are the same interview.

## Decisions this informs

- **Proposed Q-pattern-12** (progress, streaks and rewards, DC-L19-136): add streak rules from [S-L19-105]: one unit of the core action keeps the streak, freezes or grace days are offered, and the main button uses commitment wording rather than guilt [inferred defaults].
- **Q-pattern-05** (how firmly to stop design tricks): guilt copy, nagging reminders and punishment mechanics fall under it.
- **Q-voice-02** (tone for errors, success and first use): encouraging copy rather than a guilt line [S-L19-105]. The button label itself ("commit to my goal" rather than "continue") is DC-L19-38's proposal under **Q-voice-06** `flow-vocab`.
- **Q-img-04** (illustrations or a mascot): a mascot that cheers people on or grows with them [S-L19-105]; Duolingo is the example in the option list.
- **Q-brand-04** and **Q-motion-01** (how lively; hero moments): milestones and completions are candidate hero moments.
- **Q-motion-08** (app sounds): `rare-events` fits a completion jingle [S-L19-105]; the default is `silent`.
- **Q-motion-09** (haptics): tie haptics to meaningful moments only.
- **Q-pattern-06** (one number to see without opening the app): a streak count is a cue that brings people back before they open the app [S-L19-105] [inferred application].
- **Q-scope-06** (`experience` screens, such as a yearly recap or a story-format insight).

## Visual examples worth showing

- A fear-based streak screen (urgent copy, a countdown, a guilty mascot) beside an optimism-based one ("commit to my goal", collectible milestones as in Opal) [S-L19-105].
- A visible chain of days with one gap, and the same chain with a streak freeze covering the gap [S-L19-105].
- A league leaderboard with promotion, neutral and demotion zones, a goals home with a sliding rewards strip, and spending analytics with overspending highlighted [S-L19-078].
- The redesigned Spotify Wrapped with one share button and three scopes [S-L19-076], and Opal's story-format insights [S-L19-110].
- Moonly's first home screen: a daily guidance card, a personal program, transits and quick-access buttons from onboarding answers [S-L19-111].
- Post-run highlights (Runner) and a weekly recap (Origin) [S-L19-110].
- An anti-pattern gallery: a usage-shaming message with an upsell, a step-goal guilt pop-up, and a streak punishment that makes readers guess their page [S-L19-048].

## Open questions

- The retention figures (Duolingo's 0.38% and over 40%, Moonly's 41% and 37%, Mural's 10%) are reported without test details; no source here gives a method.
- How many freezes, and how much grace, before a streak stops meaning anything? Duolingo allows two equipped at a time [S-L19-105]; no source says more.
- Which mechanics suit a work tool, where the house standards favour removing friction over adding delight (`STD-when-to-animate-20`), as opposed to a consumer app?
- When do surprise layers (animations, bonus XP) stop being delight and become engineered compulsion? [S-L19-105] raises the question without answering it.
- How often may reminders fire before they become nagging? The research makes repeated prompts after a dismissal a lint error (DC-L13-15), but no source sets a frequency.