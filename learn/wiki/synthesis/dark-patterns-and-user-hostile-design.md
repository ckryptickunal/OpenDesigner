---
type: synthesis
title: Dark patterns and user-hostile design
created: 2026-09-27
updated: 2026-09-28
sources:
  - 9ypqs_2fAl8
  - ARq1bx3Sfg8
  - BUDipdbKK7Y
  - E7RzEZ8GlHE
  - YbLF42BaoZs
  - qK7WYCMvjUw
tags:
  - od-area-patterns
---

# Dark patterns and user-hostile design

## In short

Dark patterns are design choices that work against the people using a product: pressure, guilt, fake urgency, walls in front of content, and flows that are easy to join but hard to leave. Six sources now touch this. A comedy video by Kole Jain teaches by showing what not to do, making well-known apps deliberately infuriating, yet it still gives three of its annoying features a way to turn them off. Five Mobbin videos bring real practice: a paywall designer says spin-the-wheel offers do raise short-term revenue while more people learn to close paywalls and wait for an offer (the video's narrator adds that people stop believing fake urgency once every app uses it), and a streaks video shows how fear, guilt and attachment to a mascot are used to bring people back. OpenDesigner's research supplies the formal list of deceptive patterns and their legal anchors, and its planned question (Q-pattern-05, not built yet) defaults to writing the ban down and blocking what a tool can detect.

## House standards

No house standard comes from these sources, which are reference videos. These standards from the non-negotiable sources apply to anything that nags, blocks or pressures people:

- `STD-visual-details-33` (must): never trap the user; every screen answers where am I, where can I go, what is here, and how do I get out.
- `STD-accessibility-motion-24` (must): every screen and overlay has a way out; drawers close by outside click, Escape and drag by default, and one that must stay open gets an explicit close control.
- `STD-visual-details-39` (should): keep people in control by offering choices instead of forcing a single path.
- `STD-visual-details-41` (should): ask for private data at the moment it is needed, only for what is needed, and say why.
- `STD-visual-details-44` (should): decide what not to build, and spend people's time, attention and trust only on features that pay off.
- `STD-visual-details-45` (should): anticipate misuse and harm, add previews, confirmations and disclaimers, and cut a feature whose risk outweighs its value.
- `STD-when-to-animate-20` (should): tools people open with a clear goal need less friction, not added delight.

Also locked, as an OpenDesigner accessibility floor rather than an STD: every dialog has a way to dismiss it, and no consent box is pre-checked (`skills/opendesigner/references/guardrails.md`, section 4).

## What the sources teach

### Pressure tactics on paywalls

- **Spin-the-wheel offers.** A predetermined wheel animation lands on a discount the user "wins", on the idea that people who just won something are more likely to subscribe. The guest says it works when maximising a weekly price, but it may not suit a long-term business, and more users are getting comfortable closing paywalls because they expect an offer afterwards [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]) [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- **Fake urgency and last-minute discounts.** When every app uses fake urgency, users stop believing it. The guest avoids aggressive last-minute discounts (except perhaps on Black Friday) and offers a longer trial instead, to stay compliant; the narrator adds that this preserves trust [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]). An 80% discount right after onboarding can also cannibalise revenue [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- **Confusing trial switches.** In early 2026 Apple started rejecting paywalls that relied on free-trial toggles, because some were considered confusing or misleading [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- **Feeling tricked.** Blinkist users complained that they felt tricked into being charged after a free trial; a paywall showing a step-by-step trial timeline brought more trial sign-ups and fewer complaints [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]). Being clear about the charge was the fix, not a cost [inferred].

### Easy to join, hard to leave

- It takes fewer than five screens to subscribe to ClassPass and 17 screens to cancel [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Retention offers sit on the way out: an exit-intent sheet offering the monthly plan when someone closes a yearly offer [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]); a discounted win-back offer when a subscriber tries to cancel, which the guest thinks is fine, and a "before you go" paywall when someone is about to delete the app [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- On Android, the Moonly founder says alternative billing must go through Google's native SDK, whose interface is designed to scare users away and lacks Google Pay, which kills almost all conversions. This is his claim about a platform, not a tested finding [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

### Fear, guilt and attachment in engagement

- **Fear of loss.** Fear-based streak screens rely on loss aversion (losing $10 stings more than winning $10 feels good): the copy grows urgent, a clock counts down, and an angry owl creates guilt [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).
- **Attachment by design.** Mascots are designed to create attachment, not just to look cute; when a digital thing seems to need you (the Tamagotchi effect), the barrier to leaving feels higher [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).
- **Engagement is not wellbeing.** The video asks whether streaks build habits or just make people afraid to stop, says optimising for engagement differs from building a lasting habit, and reports that Duolingo kept more people going with flexibility (streak freezes) than with stricter rules [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]). It never uses the term "dark pattern"; filing it here is OpenDesigner's reading [inferred].

### What makes a product maddening (satire)

- The comedy video opens with the usual offenders: endless pop-ups, paywalls blocking content, and premium subscriptions that add nothing [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Shaming people about their usage.** A YouTube message says 342 videos is a lot, and the only choices are to subscribe to Premium or keep getting the notifications; the presenter grants it might help someone controlling their screen time, but mostly it made him angry. An Amazon pop-up after too much browsing tells people to buy a book instead [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Guilt about progress.** A fitness pop-up says you would need to run a marathon today to hit a goal of 10,000 steps a day for the week. He held back from adding more because the tone would slide from passive-aggressive to simply aggressive, and a button suggesting that the user lower their goal would make it even worse [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Lock-in and paid access.** Gmail and Google Drive stop working in any browser except Chrome, unless the user watches a minute-long ad [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **A blocking modal for a chore.** An optional Figma feature leaves new layers unnamed, and clicking anywhere except the name field brings up a modal that allows nothing else until the layer is named [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Walls in front of simple content.** A dinner recipe behind a paywall or an account requirement, like finance sites that charge to read articles [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Punishing a lapse.** Apple Books already shows a reading streak; in the joke version, breaking the streak makes the reader guess where they were in the book with a slider [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Costly or risky shortcuts.** Instacart borrows the drive-through habit of paying for the person behind you, on orders that are usually 20 or more items for over $100; a smart-home app lets neighbours pair with your outlets and bulbs, which he notes would be far worse for smart locks [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).

### Even a hostile feature needs a way out

- Three of the deliberately annoying features keep one piece of good UX: the Figma naming modal carries a notice explaining how to turn the feature off, the Apple Books punishment has a button that jumps to the actual page and another that turns the feature off, and the smart-home pairing can be switched off in settings. His reason is that being annoying is no excuse to ignore good UX [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- The usage-shaming message is the counter-example: its only choices are paying or more of the same notifications [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).

### Personalisation that goes too far

- Moonly personalised about 50 product images with each user's own face. Results were inconsistent and some were "cringe"; thousands of users avoided opening the app until the feature was removed, because people are sensitive to anything involving their own face [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]). The source reports it as a failed experiment; treating it as user-hostile is OpenDesigner's reading [inferred].

### Asking for help staying on the right side

- In a vendor demo, the brief asked an AI agent where an offers nudge belongs without feeling manipulative; after researching shipped apps, it placed the offer on the home screen right after onboarding, citing an app that shows its setup bonus there [S-L19-108] ([[sources/YbLF42BaoZs-i-gave-claude-600-000-ui-screens-then-this-happened|I Gave Claude 600,000 UI Screens… Then This Happened]]). The captions are unclear about the exact kind of offer, and the demo does not show the result.

### Some jokes turn out useful

- A driver's chattiness rating (3 out of 5, based on 134 reviews) shown while Uber finds a ride, and a one-click cart built from past orders with a running total, might actually be useful [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).

### Reading these sources

- The Kole Jain video is a comedy piece from July 2024: every feature is bad on purpose, and the app behaviours are imagined, except the Apple Books streak counter [S-L19-048]. The Mobbin videos are from 2026, promote Mobbin's library and tools, and report tactics they do not endorse; their figures are self-reported [S-L19-104] [S-L19-105] [S-L19-106] [S-L19-108] [S-L19-111].

## Where they agree and disagree

- **Satire and practice agree, for different reasons.** [S-L19-048] calls pressure maddening; the paywall guest admits a prize wheel works but has a hard time accepting it, says it may not suit a long-term business, and sees people learning to close paywalls to wait for an offer [S-L19-104] [S-L19-106]; the narrator adds that fake urgency stops being believed once every app uses it [S-L19-104]. Both are one voice each: [S-L19-104] and [S-L19-106] are the same interview.
- **Against the deceptive-pattern list.** DC-L13-15 lists the 16 types at deceptive.design and the EU DSA's examples. The recurring watch-time notification looks like nagging, the upgrade-only usage message like confirmshaming, the ad-gated Gmail and the recipe account wall like forced action [inferred mapping]. The ClassPass flow (under five screens to join, 17 to cancel) is exactly the DSA's "termination harder than subscribing" and DC-L13-15's "hard to cancel" lint [S-L19-104]. The prize wheel that always lands on a discount and fake urgency sit close to fake urgency and fake scarcity; the guilt mascot is close to confirmshaming [inferred mapping]. None of the videos uses these names.
- **What a lint can and cannot catch.** DC-L13-15 flags a countdown with no real deadline source. A streak countdown has a real deadline (the end of the day), so the lint would not catch the fear-based streak [S-L19-105]; that pressure is a tone and ethics question for review [inferred]. DC-L19-135 already proposes an off-switch check and three human-review items for the satire's patterns.
- **Win-back offers against the cancel lint.** Exit-intent sheets and win-back offers [S-L19-104] [S-L19-106] add a screen to leaving. Under DC-L13-15's rule, the whole cancel flow must still be no longer than sign-up [inferred].
- **Hidden or late close buttons.** Moonly's "soft" paywall shows its close button only after 5 seconds, and the host says a hard paywall won in the US [S-L19-111]. The way-out standards (`STD-visual-details-33`, `STD-accessibility-motion-24`) require a visible exit on every overlay, so OpenDesigner cannot recommend either [inferred application].
- **Streaks: flexibility, not punishment.** [S-L19-048] mocks punishing a broken streak; [S-L19-105] now reports Duolingo data where freezes and a lower bar beat stricter rules. Both support DC-L19-136's rule that a missed day is never punished, which until now rested only on the satire.
- **Mascots.** OpenDesigner's research uses a mascot for warmth in empty, error and success states and says not to rely on a character's expression to communicate status (DC-L06-12). [S-L19-105] shows the same device used to raise the cost of leaving; guilt from a mascot falls under DC-L19-37's rule to aim tone at the situation, never at the person [inferred].
- **The way out (agree, with a gap).** The satire's off switches agree with `STD-visual-details-39` and the escape-hatch standards. A notice saying how to turn a feature off is not a way out of the modal itself; the standards and the guardrails would still require a close control on the naming modal [inferred].
- **Usage information itself.** The presenter grants that a watch-time message could help someone managing screen time [S-L19-048]; the problem is the shaming tone and the pay-or-suffer exits, not the fact of showing usage [inferred].

## Decisions this informs

- **Q-pattern-05** (how firmly to stop design tricks): confirms `enforced`. Candidate checks from these sources, all [inferred]: a cancel flow longer than sign-up, counting win-back and exit-intent screens (DC-L13-15's hard-to-cancel rule, [S-L19-104]); a paywall or overlay whose close control is missing or delayed (`STD-accessibility-motion-24`, [S-L19-111]); a prize wheel with a fixed outcome, for human review [S-L19-104]; DC-L19-135's off-switch check and review items [S-L19-048]; and DC-L19-155's check for a free-trial toggle on an iOS paywall [S-L19-104].
- **Q-voice-02** (how tone changes for errors, success and first use): no guilt, sass or passive-aggression about the user's progress or usage (DC-L19-37) [S-L19-048] [S-L19-105].
- **Q-img-04** (illustrations or a mascot): a mascot may cheer people on, never guilt them [S-L19-105] [inferred].
- **Q-pattern-01** (which tasks open in a modal, panel or pop-up): a modal that blocks everything until a chore is done is the example of what not to do (DC-L19-114) [S-L19-048].
- **Proposed Q-pattern-12** (progress, streaks and rewards, DC-L19-136): a missed day is never punished, freezes or grace days are offered, and reminders can be switched off [S-L19-048] [S-L19-105].
- **Q-scope-06** (what the screens are for): `persuade` screens, subscription paywalls and any product with upgrade prompts are where this policy is tested most [inferred].

## Visual examples worth showing

- An anti-pattern gallery for Q-pattern-05: the 342-videos message whose only exits are subscribing or more notifications, the step-goal pop-up, the recipe behind an account wall, and the Apple Books guess-the-page slider [S-L19-048].
- A spin-the-wheel paywall beside the honest alternative, a step-by-step trial timeline (Blinkist) [S-L19-104].
- ClassPass as a count: under five screens to subscribe against 17 to cancel [S-L19-104].
- A fear-based streak screen (urgent copy, a countdown, a guilty mascot) beside an optimism-based one ("commit to my goal", collectible milestones) [S-L19-105].
- The Figma naming modal with its turn-off notice, beside a version that also has a close control [S-L19-048] [inferred for the second version].

## Open questions

- Where is the line between persuasion and pressure? Commitment copy, collectible milestones and a cheering mascot are presented as positive [S-L19-105], yet all aim to bring people back; no source draws the line.
- Moonly moved most US payments off Apple's in-app purchase to Stripe, partly because half of cancellations came within 3 minutes when cancelling was one tap [S-L19-111]. Does cancelling stay as easy after such a move? The source does not say.
- Device-based pricing (a higher price for newer phones on fast networks) is described without any discussion of fairness [S-L19-106].
- Can the builder check for an off switch or a cancel-flow length at all, given that it knows the design system but not every product flow? DC-L19-135 calls the off switch the simplest first lint; nobody has specified its input.
- The neighbouring advice is in the [[synthesis/modals-and-popovers|Modals and popovers synthesis]], the [[synthesis/paywalls-and-pricing-pages|Paywalls and pricing pages synthesis]] and the [[synthesis/retention-and-gamification|Retention and gamification synthesis]].