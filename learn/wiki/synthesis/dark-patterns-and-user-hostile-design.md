---
type: synthesis
title: Dark patterns and user-hostile design
created: 2026-09-27
updated: 2026-09-27
sources:
  - BUDipdbKK7Y
tags:
  - od-area-patterns
---

# Dark patterns and user-hostile design

## In short

Dark patterns are design choices that work against the people using a product: pressure, guilt, walls in front of content, and features that cannot be switched off. The only source on this topic is a comedy video in which Kole Jain redesigns well-known apps to be deliberately infuriating, so it teaches by showing what not to do: usage-shaming messages that offer only an upgrade or more of the same, a modal that blocks everything until you finish a chore, a paywall in front of a simple recipe, and a punishment for breaking a reading streak. Even while being annoying, he gives three of his features a way to turn them off, because being annoying is no excuse to ignore good UX. This page rests on that single, satirical source, so its lessons are opinion until another source agrees. OpenDesigner's research supplies the formal list of deceptive patterns and their legal anchors, and the default of its planned question (Q-pattern-05, not built yet) is to write the ban down and block what a tool can detect.

## House standards

No house standard comes from this source, which is a reference video. These standards from the non-negotiable sources apply to anything that nags, blocks or pressures people:

- `STD-visual-details-33` (must): never trap the user; every screen answers where am I, where can I go, what is here, and how do I get out.
- `STD-accessibility-motion-24` (must): every screen and overlay has a way out; drawers close by outside click, Escape and drag by default, and one that must stay open gets an explicit close control.
- `STD-visual-details-39` (should): keep people in control by offering choices instead of forcing a single path.
- `STD-visual-details-44` (should): decide what not to build, and spend people's time, attention and trust only on features that pay off.
- `STD-visual-details-45` (should): anticipate misuse and harm, add previews, confirmations and disclaimers, and cut a feature whose risk outweighs its value.
- `STD-when-to-animate-20` (should): tools people open with a clear goal need less friction, not added delight.

Also locked, as an OpenDesigner accessibility floor rather than an STD: every dialog has a way to dismiss it, and no consent box is pre-checked (`skills/opendesigner/references/guardrails.md`, section 4).

## What the sources teach

### What makes a product maddening

- The video opens with the usual offenders: endless pop-ups, paywalls blocking content, and premium subscriptions that add nothing [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Shaming people about their usage.** A YouTube message says 342 videos is a lot, and the only choices are to subscribe to Premium or keep getting the notifications; the presenter grants it might help someone controlling their screen time, but mostly it made him angry. An Amazon pop-up after too much browsing tells people to buy a book instead [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Guilt about progress.** A fitness pop-up says you would need to run a marathon today to hit a goal of 10,000 steps a day for the week. He held back from adding more because the tone would slide from passive-aggressive to simply aggressive, and a button suggesting that the user lower their goal would make it even worse [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Lock-in and paid access.** Gmail and Google Drive stop working in any browser except Chrome, unless the user watches a minute-long ad [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **A blocking modal for a chore.** An optional Figma feature leaves new layers unnamed, and clicking anywhere except the name field brings up a modal that allows nothing else until the layer is named; he expects designers to despise it about a minute in [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Walls in front of simple content.** A dinner recipe behind a paywall or an account requirement, like finance sites that charge to read articles [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Punishing a lapse.** Apple Books already shows a reading streak; in the joke version, breaking the streak makes the reader guess where they were in the book with a slider [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- **Costly or risky shortcuts.** Instacart borrows the drive-through habit of paying for the person behind you, on orders that are usually 20 or more items for over $100; a smart-home app lets neighbours pair with your outlets and bulbs, which he notes would be far worse for smart locks [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).

### Even a hostile feature needs a way out

- Three of the deliberately annoying features keep one piece of good UX: the Figma naming modal carries a notice explaining how to turn the feature off, the Apple Books punishment has a button that jumps to the actual page and another that turns the feature off, and the smart-home pairing can be switched off in settings. His reason: "just because we're being annoying doesn't mean we should ignore good ux" [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- The usage-shaming message is the counter-example: its only choices are paying or more of the same notifications [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).

### Some jokes turn out useful

- A driver's chattiness rating (3 out of 5, based on 134 reviews) shown while Uber finds a ride would let riders plan the trip and not feel awkward in silent moments; he says it could actually be useful [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- A one-click random grocery cart is useless, but one based on past orders, with a cart total to help people stay on budget, might be useful [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).

### Reading this source

- It is a comedy piece: every feature is bad on purpose, the rules above are drawn from what the presenter frames as infuriating plus the few places he names good UX, and the mockups are known only from his narration. The app behaviours are imagined, except the Apple Books streak counter. The video dates from July 2024 and promotes the presenter's design community [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).

## Where they agree and disagree

With a single source, the comparisons are with OpenDesigner's research, the other learning-wiki cards and the house standards.

- **Against the deceptive-pattern list (agree).** DC-L13-15 lists the 16 types at deceptive.design and the EU DSA's examples, including repeated requests after a choice was made. The recurring watch-time notification that stops only if you pay looks like nagging, the usage message with an upgrade as its only exit looks like confirmshaming, and the ad-gated Gmail and the recipe account wall look like forced action [inferred mapping]. The video never uses these names.
- **What a tool can catch (a gap).** Q-pattern-05's default `enforced` blocks what a machine can detect (DC-L13-15: pre-checked opt-ins, unequal accept and decline, re-prompting after a dismissal, fake countdowns, confirmshaming wording, cancelling harder than signing up). Most of the video's patterns fall outside that list, so DC-L19-135 proposes an off-switch check as the simplest first lint and three human-review items: an upsell attached to a usage or guilt message, a wall in front of content promoted as free, and a lapse that removes progress. Q-pattern-05 is still planned, so the interview skips it today.
- **The way out (agree, with a gap).** The video's off switches agree with `STD-visual-details-39` and the escape-hatch standards (`STD-visual-details-33`, `STD-accessibility-motion-24`). A notice saying how to turn the feature off is not the same as a way out of the modal itself: the standards and the guardrails' "every dialog has a way to dismiss it" would still require a close control on the naming modal [inferred].
- **Tone (agree).** DC-L19-37 aims humour at the situation, never at the person, and asks usage and progress nudges to state facts neutrally and offer a real choice; that card draws its rule from this video's counter-examples. DC-L19-112 says never to shame people about their usage in a message whose only exits are an upsell or more of the same notifications.
- **Streaks (agree).** DC-L19-136 rejects punishing a broken streak and asks for an off switch on reminders and other engagement features, citing this video; the research lists addictive design among the patterns to watch (DC-L13-15).
- **Blocking modals (agree).** DC-L19-114 names the forced layer-naming modal as something to avoid when choosing between a popover, modal, sheet or new page.
- **Usage information itself (softer than the joke).** The presenter grants that a watch-time message could help someone managing their screen time [S-L19-048]; the problem he shows is the shaming tone and the pay-or-keep-suffering exits, not the fact of showing usage [inferred].
- **Useful personalisation (not covered).** No research card covers the chattiness rating or a cart built from past orders; they are ideas, not tested patterns [S-L19-048].

## Decisions this informs

- **Q-pattern-05** (how firmly to stop design tricks): confirms `enforced`; add the off-switch check and the human-review items from DC-L19-135 when the question is built [S-L19-048].
- **Q-pattern-01** (which tasks open in a modal, panel or pop-up): a modal that blocks everything until a chore is done is the example of what not to do (DC-L19-114) [S-L19-048].
- **Q-voice-02** (how tone changes for errors, success and first use): no guilt, sass or passive-aggression about the user's own progress or usage (DC-L19-37) [S-L19-048].
- **Proposed Q-pattern-12** (progress, streaks and rewards, DC-L19-136): a missed day is never punished, and reminders can be switched off [S-L19-048].
- **Q-scope-06** (what the screens are for): `persuade` screens, and any product with upgrade prompts, are where this policy is tested most [inferred].

## Visual examples worth showing

- An anti-pattern gallery for Q-pattern-05: the 342-videos message whose only exits are subscribing or more notifications, the step-goal pop-up with and without the button suggesting a lower goal, the recipe behind an account wall, and the Apple Books guess-the-page slider [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).
- The Figma naming modal with its turn-off notice, beside a version that also has a close control [S-L19-048] [inferred for the second version].
- The two ideas that turned useful: the chattiness rating with its review count, and a one-click cart built from past orders with a running total [S-L19-048].

## Open questions

- The only source is satire. Should the learning wiki add a straight source on deceptive patterns, so that DC-L13-15's research list has practitioner examples that are not jokes?
- Where is the line between a helpful usage reminder (screen time) and a shaming one? The video grants the first and mocks the second without saying where the line falls.
- Can the builder check for an off switch at all, given that it knows the design system but not every product feature? DC-L19-135 calls it the simplest first lint; nobody has specified the input it would read.
- Does a notice explaining how to turn a feature off ever satisfy the way-out standards on its own, or must every blocking surface also close? The neighbouring advice is in the [[synthesis/modals-and-popovers|Modals and popovers synthesis]], the [[synthesis/paywalls-and-pricing-pages|Paywalls and pricing pages synthesis]] and the [[synthesis/retention-and-gamification|Retention and gamification synthesis]].
