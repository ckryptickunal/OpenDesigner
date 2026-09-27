---
type: synthesis
title: Paywalls and pricing pages
created: 2026-09-24
updated: 2026-09-28
sources:
  - 9ypqs_2fAl8
  - BUDipdbKK7Y
  - E7RzEZ8GlHE
  - PDcQJOPby1k
  - Qsq-Sj_rojU
  - gKM6b2EnW1k
  - ld1zhQMXxXU
  - pGYLZyBE32o
  - qK7WYCMvjUw
tags:
  - od-area-patterns
---
# Paywalls and pricing pages

## In short

A paywall is the screen that asks people to pay inside an app; a pricing page helps visitors to a website choose a plan. The newer sources, Mobbin interviews with a paywall designer and an app founder, treat the paywall as a flow rather than one screen: sell the outcome first, show it at the right moment, lower the fear of being charged (a trial timeline, a "cancel anytime" line, a longer trial), show two plans with yearly preselected, and test very different designs, because no paywall wins everywhere. For web pricing pages, Kole Jain's videos ask for fewer plans, a price larger than the plan name, and honest discounts and billing terms. A spin-the-wheel offer can raise short-term revenue, but the guest says people are learning to close paywalls and wait for an offer, the narrator adds that fake urgency stops being believed, and a flow that is easy to join but hard to cancel (ClassPass) is the example to avoid; OpenDesigner's research lists these as deceptive patterns. The numbers are self-reported case results, so treat them as ideas to test.

## House standards

- `STD-visual-details-02` (must): use tabular digits on price columns and numbers that change in place.
- `STD-visual-details-59` (must): when a price animates (for example on a monthly or yearly switch [inferred]), use NumberFlow instead of re-rendering the text.
- `STD-visual-details-29` (should): make the most important thing on the screen the most obvious.
- `STD-visual-details-35` (should): keep interface copy plain and concise.
- `STD-visual-details-44` (should): spend the user's time, attention and trust only on features that pay off.
- `STD-visual-details-33` (must) and `STD-accessibility-motion-24` (must): never trap the user; every overlay has a way out. A paywall therefore keeps a visible close control from the start [inferred application].
- `STD-visual-details-41` (should): ask for private data at the moment it is needed, only what is needed, and say why; this covers asking for card details to start a trial [inferred application].
- `STD-springs-gestures-61` (must) and `STD-accessibility-motion-20` (must): at most one haptic per action, for a meaningful moment, never on an entrance the person did not cause, always paired with a visual change. A one-time offer that vibrates as it appears breaks this; a haptic may answer only the person's own tap on it (DC-L19-98) [inferred application].
- `STD-visual-details-37` (should) and `STD-when-to-animate-22` (should): prove a new pattern by testing it, and ship the winner.
- `STD-accessibility-motion-15` (must): put hover animations inside `@media (hover: hover) and (pointer: fine)`, which applies to hover reveals on upgrade prompts [inferred].

## What the sources teach

### A paywall is a flow, not a screen

- Before asking for money, sell the outcome, so the paywall feels like the natural next step: Opal shows how many years of life people could get back, and its trial sign-ups rose from 7% to 17% [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- At the end of onboarding, make the paywall a natural segue: tell people their plan is ready and speak to the outcome they want (feeling like themselves in 4 weeks). Multi-page paywalls, where information unfolds gradually, almost always beat single-page ones in the guest's experience [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Onboarding flows that end in a paywall often show value or proof first: a full page of social proof (Timely), or a ready personal plan with a goal date [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- A first paywall only needs a headline describing the product, a couple of bullet points and a continue button; optimise later, once people are in the app [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).

### When and where it appears

- A well-designed paywall shown at the wrong moment is still a bad paywall. Touch points include the end of onboarding, a premium feature, the settings page, cancellation (a win-back offer) and a last-chance screen before someone deletes the app [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]) [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- The after-onboarding paywall is the most used: 78% of iOS apps on Mobbin show one [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]). In a separate count, 22% of over 900 apps and websites show a paywall during onboarding [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- At Moonly, a separate paywall for each feature lost every test, because people thought they had to buy each feature separately, so Moonly went back to one consistent paywall; the video then shows Orbit's paywall, which makes clear that paying today unlocks all features [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- Whether to create the account before or after the paywall has to be tested; the guest's results were inconclusive, though he prefers account first so the subscription is tied to a user ID [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- A soft paywall (closable) won across Moonly's tests, though its close button appears only after 5 seconds; the host says a hard paywall (no way past without paying) won in the US [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

### Lowering the fear of paying

- Blinkist users felt tricked into being charged after a trial; a step-by-step trial timeline brought more trial sign-ups, fewer complaints and more push notification opt-ins, because the app reminds people before the trial ends [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- A "no commitment, cancel anytime" subtitle under the button always seems to lift results a little. A call to action that names what the user is doing, instead of "Continue", is hit or miss. Most winning paywalls have a right chevron on the button, though the guest has not tested it on its own [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Emphasising the free trial, adding a discount badge and making the same offer easier to understand almost tripled Tipstop's direct conversions. Headspace tested 7, 14 and 30-day trials, and a 14-day trial on the annual plan won because it made the decision feel less risky [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Removing friction does not always help: when Outsider required card details to start a trial, sign-ups fell by more than half but conversion rose five times and paying customers more than doubled [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- The opposite view: Moonly removed its free trial because trial users got the most valuable feature free and felt they had 90% of the value. It shows a one-time offer instead, usually on day three, which lifted revenue between day 3 and day 30 by about 15%. On Mobbin, 59% of iOS paywall screens offer no free trial [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

### Plans, prices and packaging

- Preselect the yearly plan, which has the highest lifetime value, unless yearly does not suit the business; show only two plans (yearly plus weekly or monthly) to lower the mental effort, and put any others behind a "view all plans" button that opens a sheet [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]) [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- Price packaging is its own test: plans stacked or side by side, what goes in each, and whether both plans read as a weekly price with the real billed price as a subtitle [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- Price anchoring: Tide breaks the price into smaller weekly amounts, and Ahead compares the subscription with things people already buy, such as coffee or therapy [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]). A high-priced lifetime plan can raise perceived value and nudge people toward the annual plan even if it rarely sells; 4% of iOS apps on Mobbin offer one, usually at about twice the annual price [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- People compare prices with each other rather than with value, so Moonly kept the number and changed the unit ($8 a month became $8 a week). Weekly payments recover ad spend faster; the founder confirms those buyers churned harder [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- Leave device-based pricing (a higher price for a new phone on a fast network) until last: it is a lot of work for smaller gains [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).

### Framing, copy and imagery

- Common framing: social proof with real reviews and a five-star rating, and value framed around what each user cares about [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]). Moonly's founder recommends always adding social proof (downloads, reviews) and reports that changing only the title and subtitle raised conversion by 12% [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- After design, personalisation moves results most: the user's name, their goals, and imagery that reflects who they are [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]). Recommending plans from quiz answers raised Grammarly's plan upgrades by almost 20% [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- Imagery must fit who pays: Moonly's team loved Disney-style 3D characters, but its paying audience, mostly over 35, could not see themselves in them; the first realistic image won and gave a 2x uplift. Personalising images with the user's own face was removed [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

### Formats worth testing

- Test radically different designs first: a video paywall, a bullet list, a trial timeline or a long-form page [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- A table shows what people miss by not subscribing (the guest is a huge fan, though tables are harder to build in paywall tools); a video paywall shows the app in action with a short bullet list and simple social proof; Slopes replaced the paywall with a single "redeem your free week" action, a pay ramp that raised trial starts by 25% [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- A one-time offer that disappears once closed can use animation and a haptic to catch attention at the moment someone considers upgrading [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]); Focus Flight's offer is shaped like a flight ticket and the phone vibrates as it prints [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]). The house standard keeps the animation as a rare moment but rules out the attention haptic (see Q-motion-09 below).
- Polish (animation, custom characters, world building, as in Focus Town) is expected to set apps apart now that anyone can ship one, yet an ugly, text-heavy squeeze page beat every design the guest made for one app. There is no universal best paywall, only better experiments [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).

### Leaving, cancelling and win-backs

- When someone closes a yearly offer, an exit-intent sheet can offer the monthly plan; instead of an aggressive last-minute discount, offer a longer trial, which keeps you compliant and preserves trust [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- A steep discount is fine in a win-back offer for a subscriber about to cancel, but not right after onboarding, where an 80% discount can cannibalise revenue [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- ClassPass takes fewer than five screens to subscribe and 17 to cancel [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).

### Tactics the sources warn against

- Spin-the-wheel paywalls (a wheel with a fixed outcome that lands on a discount) work for maximising a weekly price, the guest says, but he has a hard time accepting them, says they may not suit a long-term business, and sees more people learning to close paywalls because they expect an offer next. The paywall video's narrator adds that people stop believing fake urgency once every app uses it [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]) [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- In early 2026 Apple began rejecting paywalls built on free-trial toggles because some were confusing or misleading [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Do not put a paywall or an account wall in front of simple content such as a recipe, do not sell premium subscriptions that add nothing, and do not shame people about their usage and then offer only an upsell or more notifications [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).

### Payments

- With Apple's native payments, half of Moonly's cancellations came within 3 minutes of purchase; adding Stripe as an alternative in the US, with a small discount, doubled lifetime value, and about 80% of US customers now use it. On Android the founder advises against alternative billing through Google's SDK, whose interface he says scares users away [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]). These depend on platform rules in 2026 and may date quickly. Where people pay, and what the store allows on a paywall, is DC-L19-155's decision.

### Pricing pages on the web

- Five plans is not ideal; drop at least one, and rename a very high-volume plan to Enterprise, because customers at that volume probably need more than a fixed plan [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- Merge landing pages that sell the same thing into one plans section built on the few points that matter (for an AI product: cost, a better model, document uploads). Put Enterprise behind a tiny button on every plan, because the creator estimates it is irrelevant to about 98% of visitors, and make the purchase call to action one of the cards, marked with a gradient stroke [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).
- Make the plan name smaller and the monthly cost larger, because people care about the cost, not the name [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- Give each plan a name and a short description, use check marks instead of bullets, list a feature the plan lacks, make the button an outline button if it moves up the card, separate the price from the features with a light tint of the primary color, and write an actionable button label [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- Show the actual discount, or discounted plans look cheaper than lower tiers; show what the next plan adds (as Resend and Supabase do) [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]). Add a short note under the price with the real billing terms, so people do not feel misled [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- In the product's billing area, use tabs (billing, usage and more), show usage as a few small donut charts, and include the billing email and payment method [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- Hovering an upgrade prompt can reveal the higher plan's limits (an idea taken from Dub) with a slide-in where the old number disappears, instead of Dub's crossed-out text [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).

## Where they agree and disagree

- **Who is speaking.** [S-L19-104] and [S-L19-106] are one interview with the same paywall consultant, and [S-L19-111] replays short clips of him, so their agreement on two plans, a yearly default and the "cancel anytime" line is one voice. The web pricing advice is one voice too (Kole Jain). All figures are self-reported by the videos.
- **One paywall or one per feature.** [S-L19-104] says paywalls at different touch points speak more to the user because they are more personal; [S-L19-111] found that per-feature paywalls lost every test. They can fit: show the paywall at the right moments, but make each one say that paying unlocks everything [inferred].
- **Trial or no trial.** [S-L19-104] favours longer trials and trial timelines (and mentions Moonly offering a trial only on its annual plan); [S-L19-111] reports Moonly removing its trial entirely. The answer depends on whether the trial gives away the product's main value [S-L19-111] [inferred generalisation].
- **Friction.** Requiring card details raised conversion for Outsider [S-L19-104]. The house rule on private data (`STD-visual-details-41`) still asks the paywall to say why the card is needed and when the first charge comes, which is what Blinkist's timeline does [inferred].
- **Plan count by surface.** Two plans on a mobile paywall [S-L19-104] [S-L19-106]; "five is too many" on a web pricing page [S-L19-061]; DC-L19-134 proposes three or four plans with one suggested for web pricing pages. These are different surfaces, not a contradiction [inferred]. DC-L19-134 also said no source covered mobile paywalls or free trials; these sources now do.
- **Honest numbers.** Showing both plans as a weekly price with the real billed price as a subtitle [S-L19-106] fits DC-L19-134's rule to show the real discount and billing terms, as long as the billed price is visible [inferred]. Moonly's unit change [S-L19-111] is a price change; shown plainly it is a pricing choice, but hiding the real total would drift toward the hidden costs DC-L13-15 lists [inferred].
- **Hard to cancel.** ClassPass (under five screens to join, 17 to cancel) [S-L19-104] is exactly what DC-L13-15's lint targets: a cancel flow with more steps than sign-up, also named in the EU DSA. Exit-intent sheets and win-back offers [S-L19-104] [S-L19-106] add a screen to leaving, so under that lint the whole cancel flow must still be no longer than sign-up [inferred].
- **Hard paywalls and late close buttons.** A hard paywall, or a close button hidden for 5 seconds [S-L19-111], conflicts with the way-out standards (`STD-visual-details-33`, `STD-accessibility-motion-24`); OpenDesigner can lock premium content, but the paywall screen itself keeps a visible exit [inferred application].
- **Pressure tactics.** Spin-the-wheel and fake urgency [S-L19-104] [S-L19-106] map to fake urgency and fake scarcity in DC-L13-15's list [inferred mapping], and the usage-shaming upsell [S-L19-048] is close to confirmshaming. OpenDesigner's current default for Q-pattern-05 is `enforced`.
- **Imagery.** Realistic images beat cartoon 3D for Moonly's over-35 payers [S-L19-111], while OpenDesigner's research lists dimensional 3D as a playful illustration style (DC-L06-12). The audience decides, and one app's result is not a rule [inferred].
- **One highlighted choice.** [S-L19-075] tones the card button down to an outline, and [S-L19-082] turns the purchase action into a highlighted card; both fit the research rule of at most one high-emphasis action per region (DC-L13-18) [inferred]. A preselected yearly plan [S-L19-104] is a default choice, not a pre-ticked consent box, so it is not the preselection DC-L13-15 flags, provided the other plan is equally easy to pick [inferred].
- **Hover reveals.** [S-L19-079] relies on hover, which touch screens do not have; the house rule gates hover motion to fine pointers (`STD-accessibility-motion-15`), so plan limits also need to be readable without hover [inferred].

## Decisions this informs

- **Q-pattern-05** (how firmly to stop design tricks): pricing, paywalls and cancel flows are where it matters most; candidate checks are a cancel flow longer than sign-up and a paywall without a visible close control [inferred], plus DC-L19-155's check for a free-trial toggle on an iOS paywall [S-L19-104].
- **Proposed Q-pattern-11** (DC-L19-134, how plans are shown): add a mobile paywall variant with two plans, yearly preselected and the rest behind a "view all plans" sheet [S-L19-104] [S-L19-106] [inferred option].
- **Q-pattern-01** (modal, panel or pop-up): "view all plans" and exit-intent offers open as sheets [S-L19-104].
- **Q-img-01** (photos) and **Q-img-06** (3D art): paywall imagery should match who pays [S-L19-111].
- **Q-motion-09** (haptics): no haptic to draw attention to an offer as it appears [S-L19-104] [S-L19-107]; at most one light haptic on the tap that claims it, paired with a visual change (DC-L19-98, `STD-springs-gestures-61`) [inferred application].
- **Q-type-06** (numbers font and tabular digits) and **Q-voice-05** (writing rules, including numbers).
- **Q-state-01** (button styles and how many main buttons per area): one highlighted plan or purchase card.
- **Q-color-25** (where gradients are allowed): gradient strokes on the purchase card [S-L19-082].
- **Q-scope-06** (`persuade` screens) and **Q-scope-01** (marketing site in scope).
- **Proposed Q-pattern-13** (DC-L19-137, which number a change should move): for paywalls, pick the metric by business type [S-L19-106].

## Visual examples worth showing

- Opal's outcome screen ("8 years of your life back") before its paywall [S-L19-104].
- Blinkist's step-by-step trial timeline paywall [S-L19-104].
- A paywall button with the "no commitment, cancel anytime" subtitle and a right chevron [S-L19-104].
- A two-plan footer with yearly preselected and a "view all plans" sheet, beside the weekly-price-with-real-price variant [S-L19-104] [S-L19-106].
- Price anchoring: Tide's weekly breakdown and Ahead's comparison with coffee or therapy [S-L19-104].
- Format gallery: a table paywall, a video paywall, a trial timeline and Slopes' single "redeem your free week" pay ramp [S-L19-104].
- Focus Flight's ticket-shaped one-time offer [S-L19-107].
- Moonly's Disney-style 3D paywall image beside the realistic one that won [S-L19-111].
- The anti-patterns: a spin-the-wheel paywall, and ClassPass's 5 screens to join against 17 to cancel [S-L19-104]; a recipe behind a paywall [S-L19-048].
- A web pricing card before and after: check marks, a missing feature listed, billing text under the price, a tinted price area and an outline button [S-L19-075]; a vibe-coded pricing page fixed [S-L19-061]; merged AI plans with a gradient-stroke purchase card [S-L19-082]; an upgrade prompt whose limits slide in on hover [S-L19-079].

## Open questions

- Monthly versus yearly switches on web pricing pages, taxes, currencies and local prices are still not covered.
- Where is the line between price anchoring (a lifetime plan that is not meant to sell, a weekly unit) and misleading framing? The sources present anchoring as normal practice; DC-L13-15 names comparison prevention and hidden costs but not anchoring.
- Device-based pricing is described without any discussion of fairness [S-L19-106].
- App-store rules change quickly (Apple's early-2026 rejection of trial toggles [S-L19-104], US payment alternatives [S-L19-111]); should OpenDesigner record platform rules with a date?
- The case results are single-company figures without test details; see [[synthesis/a-b-testing-and-conversion|A/B testing and conversion synthesis]].