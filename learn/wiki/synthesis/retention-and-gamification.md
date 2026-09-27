---
type: synthesis
title: Retention and gamification
created: 2026-09-24
updated: 2026-09-27
sources:
  - BUDipdbKK7Y
  - goWOAFqJHpA
  - ixUq4HM4FNg
  - jSxxAFxjxbU
tags:
  - od-area-patterns
---
# Retention and gamification

## In short

Retention is about why people come back to a product. The main source on gamification says it works when it is built around one central currency, shows progress made and progress left, adds a social layer such as leaderboards, and ties rewards to goals people really have; it also says to prove the product's value before adding any game. Sharing can be its own reason to return, as the Spotify Wrapped redesign shows. The other side matters as much: guilt messages, punishments for a broken streak and designing for compulsive use are presented as what makes products maddening, and OpenDesigner's research lists them among deceptive patterns. All four sources are videos by one practitioner (Kole Jain), without retention data.

## House standards

- `STD-when-to-animate-09` (must): delight motion is spent only on rare, high-emotion moments such as success, completion and celebration, never on components used many times a day.
- `STD-springs-gestures-61` (must): haptics and sound only for meaningful moments (success, error, commit, snap), at most one haptic per action.
- `STD-visual-details-59` (must): animate counters (such as points or a currency balance [inferred]) with NumberFlow.
- `STD-visual-details-47` (should): decide the emotion people should feel and reinforce it in every decision instead of tacking delight on top.
- `STD-visual-details-39` (should): offer choices instead of forcing one path.
- `STD-visual-details-44` (should): spend people's time, attention and trust only on features that pay off.
- `STD-visual-details-45` (should): anticipate misuse and harm, and cut a feature whose risk outweighs its value.

## What the sources teach

### The parts of a gamification system

- Gamification usually hinges on one central currency (Duolingo XP, Todoist Karma) earned by the core actions; it shows what you have done and what is left (Exercism); it often has a social side (leaderboards, public badges); and rewards only work when tied to real goals [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).
- Duolingo layers XP, gems, hearts, streaks and achievements. The worked example, a savings app, keeps a streak alive with the core action, scales rewards to the size of the goal, gives badges for milestones (30 days in a row), ranks people on a local leaderboard with Duolingo-style promotion and demotion zones, and pays the currency for finishing short finance quizzes [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).

### Prove value before the game

- The savings app's onboarding shows insights into past spending before introducing any game mechanics, and reassures people before asking them to connect a bank account [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).

### Sharing and recaps

- In a yearly recap, keep the share action always visible because sharing is why the product succeeds; use one share button with a few scopes rather than two similar buttons; show the owner's name on shared content; add a short comparison with last year under a headline stat; prefer a few familiar categories over hyper-specific AI labels; and do not drop features people liked in earlier years [S-L19-076] ([[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]).

### Removing friction

- TikTok's main screen offers one core action, a swipe up with a target covering almost the whole screen, plus autoplay and auto-snap, so moving on needs no decision. The video reports 53 minutes a day for the average American user and eight opens a day on average (2024 figures, stated without sources) [S-L19-077] ([[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok’s UX is so GOOD it should be ILLEGAL (seriously)]]).

### What to avoid

- Do not shame people about their usage and then offer only an upsell, do not write guilt-tripping progress pop-ups, do not pair a progress warning with a nudge to lower the goal, and do not punish a broken streak. Three of the deliberately annoying features in the video (the forced layer-naming modal, the streak punishment and neighbour control of smart-home devices) still come with a way to turn them off [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).

## Where they agree and disagree

- **Streaks: reward, never punish.** [S-L19-078] uses a streak as motivation, and [S-L19-048] mocks punishing a broken one. Together they suggest a streak should reward keeping going and never penalise a lapse [inferred].
- **Compulsive use.** [S-L19-077] admires what it calls an addictive experience; its analysis notes that designing for compulsive use is an ethical choice the video does not weigh. The research lists nagging and confirmshaming among 16 deceptive patterns, lists addictive design separately, and notes that EU rules on dark patterns and addictive design are announced but not yet adopted (DC-L13-15).
- **Fewer choices.** [S-L19-077] says more options lead to worse decisions and removes them. OpenDesigner's research warns that choice overload averaged about zero across 50 studies and that Hick's law does not justify deleting options (L13 research, law table; not a Decision Card). The video's analysis also notes it describes Fitts's law while naming Hick's. Removing options may work for TikTok only because its algorithm learns what people want from their behaviour, which the video credits for its success [inferred]; it is not a general rule.
- **Progress displays.** Showing progress made and left [S-L19-078] matches the goal-gradient effect in the research, which also draws an ethics line at artificial progress that misstates the real work left (L13 research, law table) [inferred link].
- **Celebration budget.** Milestones and badges are rare moments where the house standards allow delight (`STD-when-to-animate-09`), and the research default of calm motion with a few hero moments (one or two in DC-L06-03, one to three per flow in DC-L04-19) fits them [inferred]. DC-L19-83 narrows those hero moments to rare ones such as first run, success and empty states.
- **An escape hatch.** [S-L19-048] keeps a way out in three of its satirical features, which matches the house rule to offer choices instead of one forced path (`STD-visual-details-39`).

## Decisions this informs

- **Q-pattern-05** (how firmly to stop design tricks): guilt copy, nagging reminders and punishment mechanics fall under it.
- **Q-brand-04** and **Q-motion-01** (how lively; hero moments): milestones and completions are candidate hero moments.
- **Q-motion-08** (app sounds): "rare-events" fits celebrations; the default is "silent".
- **Q-motion-09** (haptics): tie haptics to meaningful moments only.
- **Q-voice-02** (tone for errors, success and first use): celebration and lapse messages set the tone.
- **Q-img-04** (illustrations or a mascot): a mascot in empty, loading and success states is one option (Duolingo is the example in the option list).
- **Q-pattern-06** (one number to see without opening the app): a streak or goal progress is a candidate [inferred].
- **Q-scope-06** ("experience" screens, such as a yearly recap).

## Visual examples worth showing

- A league leaderboard with promotion, neutral and demotion zones, a goals home with a sliding rewards strip, and spending analytics with overspending highlighted [S-L19-078].
- The redesigned Spotify Wrapped: four named chapters with a bottom chapter chip, a "view summary" dashboard per chapter, and one share button with three scopes [S-L19-076].
- TikTok's full-screen feed with a bottom nav bar and action icons in the right thumb's reach [S-L19-077].
- An anti-pattern gallery: a usage-shaming message with an upsell, a step-goal guilt pop-up, and a streak punishment that makes readers guess their page [S-L19-048].

## Open questions

- None of the sources reports retention data, so no mechanic here is shown to work.
- Which mechanics suit a work tool, where the house standards favour removing friction over adding delight (`STD-when-to-animate-20`), as opposed to a consumer app?
- How should a streak handle a missed day (a freeze, a grace period)? Not covered.
- How often may reminders and notifications fire before they become nagging? The research makes repeated prompts after a dismissal a lint error (DC-L13-15), but no source here sets a frequency.
