---
type: synthesis
title: A/B testing and conversion
created: 2026-09-24
updated: 2026-09-28
sources:
  - 5JxUJ1fuyO8
  - 9ypqs_2fAl8
  - ARq1bx3Sfg8
  - E7RzEZ8GlHE
  - Qsq-Sj_rojU
  - qK7WYCMvjUw
tags:
  - od-area-patterns
---
# A/B testing and conversion

## In short

Conversion means the share of people who do the thing a screen is for, such as subscribing, signing up or buying. An A/B test shows two or more versions to real users and keeps the one that does better on a number chosen in advance. Five Mobbin videos now add self-reported test results from consumer apps, quoted without sample sizes: very different designs moved paywall results the most, changing only the words raised one app's conversion by 12%, and many winners went against common advice (a longer onboarding, more friction at sign-up, no free trial). They also warn that the number you choose matters: revenue per user can look good while most people cancel within a month, so retention and lifetime value should usually decide. The older freelancer video adds that small tests before launch cannot prove impact and that comparing analytics before and after a change is the minimum check, so treat every result here as an idea to test, not a rule.

## House standards

- `STD-when-to-animate-22` (should): decide deliberately whether an idea deserves building; when you build option A and option B to compare, validate them and ship the one that wins, not both.
- `STD-visual-details-37` (should): break a familiar pattern only when you can prove the new one is better, and test it rather than assume.
- `STD-visual-details-44` (should): decide what not to build, and spend people's time, attention and trust only on features that pay off.
- `STD-process-review-taste-34` (should): test designs with real people in the real context of use, not only on your own desk.

## What the sources teach

### Start from the business goal

- Behind "I need a website" there is usually a need for more customers, clients, sales or sign-ups; a site that looks good but serves no purpose still will not sell [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- Clients mostly judge a site on looks, while its users care about whether it works, so results depend more on UX than on UI; in the example, the fix for a store was better search and product categories, not a new look [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- A plain page can convert well if the information is clearly laid out and the next click is obvious, and page sections should be chosen for the goal they serve (testimonials for an agency, last year's impact for a nonprofit) [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- For subscription apps the business type decides the goal: a quick launch that wants as many users as possible can chase revenue per user (ARPU), while a long-term business should optimise lifetime value (LTV) and retention and balance churn [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).

### Choose the number before the test

- Revenue per user alone misleads: a three or four dollar ARPU can come from weekly plans whose churn is 90 to 95% a month. The guest also checks paywall percentage (the share of installs that see the paywall: above 80% is good, 90% or more is excellent), trial-to-paid conversion, LTV, retention on day 1, 7 and 30, and churn [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- The same guest wishes founders cared most about retention and LTV, because getting people to subscribe is easier than building something they keep paying for [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]). The highest-converting paywall is not always the one to ship [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- Engagement is not the same as the outcome people want: most evidence on streaks covers engagement and retention, not lasting habits, so a streak feature should not be judged only by those numbers when the goal is a habit [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).

### What to test first

- Test in this order: radically different designs first (a video paywall, a bullet list, a trial timeline, a long-form page), then personalisation (the user's name, their goals, imagery that matches them), then price packaging (how the plans sit in the footer and how prices read), and device-based pricing last because it is a lot of work for smaller gains [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]). The companion video repeats that design tests move the needle most and adds that there is no universal best paywall, only better experiments [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Moonly's founder calls pricing tests the most important experiment a product can run (40 in the past year), says images are the biggest paywall lever (one winning image gave a 2x uplift), and reports that changing only the paywall's title and subtitle, across eight variants, raised conversion by 12% [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- Test even the elements nobody would question: at Moonly every element, icon and piece of text earned its place by winning a test [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

### How to run tests

- Ship a simple base version first (for a paywall: a headline, a couple of bullet points and a continue button) and measure its base numbers before optimising placements [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]) [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Keep the current version as the control and design four to five challengers against it. Be patient: the guest says most clients beat the control in the first week, but two needed a second or third experiment to reach a statistically significant win [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- Small, almost daily improvements add up: Moonly reports paid-traffic conversion going from 10% in 2020 to 40%. It runs hundreds of tests a month and uses AI tools to match numbers across analytics sources and recommend ship, don't ship or collect more data [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- Before building a full app, test the market with a lean web funnel, which gives faster signals for less money [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- Do not copy another product's winner without testing it: the onboarding video notes that audiences differ in how much information density feels efficient [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]), and the paywall guest's tests of account-before-paywall were inconclusive across app categories [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).

### Results that went against common advice

- More friction can raise paid conversion: when Outsider required card details to start a trial, sign-ups dropped by more than half but conversion rose five times and paying customers more than doubled. An ugly, text-heavy paywall beat every design the guest made for one app [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).
- Splitting a sign-up form across several screens raised House's conversions by 15%, and some of the longest onboarding flows belong to successful apps [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- At Moonly, a paywall per feature lost every test (people thought they had to buy each feature), removing the free trial made the numbers stronger, a realistic paywall image beat the Disney-style 3D characters the team liked, and personalising images with the user's own face was removed after thousands avoided opening the app [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- At Duolingo, adding flexibility beat adding pressure: streak freezes and a one-lesson minimum kept more people going [S-L19-105] ([[sources/ARq1bx3Sfg8-the-psychology-behind-streaks|The Psychology Behind Streaks]]).

### Reported results at a glance

Every figure below is quoted by the video without sample size, test length or date, and most are single-company outcomes.

| Product | Change | Reported result | Source |
|---|---|---|---|
| Opal | Sold the outcome (years of life saved) before the paywall | Trial sign-ups 7% to 17% | [S-L19-104] |
| Blinkist | Trial timeline on the paywall | More trial sign-ups, fewer complaints, more push opt-ins (no figure) | [S-L19-104] |
| Tipstop | Same offer, free trial emphasised, discount badge | Direct conversions almost tripled | [S-L19-104] |
| Slopes | One "redeem your free week" action instead of a paywall | Trial starts +25% | [S-L19-104] |
| Outsider | Card required to start a trial | Sign-ups down by more than half, conversion five times higher | [S-L19-104] |
| Headspace | 7, 14 and 30-day trials | 14-day trial on the annual plan won | [S-L19-104] |
| Headspace | More than one goal allowed in onboarding | Free-trial conversion +10% | [S-L19-107] |
| Dollar Shave Club | Conversational quiz copy | Subscriptions +5% | [S-L19-107] |
| Grammarly | Plans recommended from quiz answers | Plan upgrades almost +20% | [S-L19-107] |
| Mural | Six-step checklist instead of pop-ups and banners | One-week retention +10% relative | [S-L19-107] |
| House | Sign-up form split across screens | Conversions +15% | [S-L19-107] |
| Duolingo | Up to two streak freezes equipped | Daily active learners +0.38% (over 200,000 a day) | [S-L19-105] |
| Duolingo | One lesson keeps the streak instead of the full daily goal | Over 40% more people kept a 7-day streak | [S-L19-105] |
| Moonly | Onboarding tailored to the ad people came from | Lifetime value doubled | [S-L19-111] |
| Moonly | Only the paywall's words changed | Conversion +12% | [S-L19-111] |
| Moonly | One-time offer, usually on day three, instead of a trial | Day 3 to 30 revenue about +15% | [S-L19-111] |

### Where conversion work pays off

- For a site that already gets heavy traffic, conversion rate optimisation is a better add-on than SEO, because a small gain at that scale is worth a lot [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- In a subscription app, the paywall is described as the only part of the app that makes money, so every touch point where it appears is worth testing [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]) [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).

### Measuring impact without a controlled test

- Compare the site's analytics before and after the new design ships; building the site yourself, or keeping view-only access, makes this possible [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- Do not treat a small pre-launch UX test as proof: the sample sizes you can gather are often too small to be significant [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- Report results as short case studies: the services provided, the problem, and the solution with numbers [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).

### Looks matter, but do not decide

- Attractive designs are perceived as easier to use (the aesthetic-usability effect) [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]), yet an ugly paywall can win, and polish is still expected to set apps apart as more people ship them [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]).

## Where they agree and disagree

- **Who is speaking.** Five of the six sources come from Mobbin's channel, which promotes its own library and tools. Two of them ([S-L19-104] and [S-L19-106]) are one interview with the same paywall consultant, and [S-L19-111] replays short clips of him, so their agreement is one voice, not three. All figures are self-reported.
- **Design first or pricing first.** The paywall consultant says design tests move results most [S-L19-104] [S-L19-106]; Moonly's founder calls pricing tests the most important and images the biggest lever [S-L19-111]. They run different products, and both say to test rather than assume, so the order is a starting point [inferred].
- **Test size.** [S-L19-038] warns that small tests prove nothing, and [S-L19-106] waits for a statistically significant win, even into a second or third experiment. OpenDesigner's research says A/B testing and analytics need large traffic, while usability testing with about five people per round finds problems (L13 research, Part D methods table; not a Decision Card). None of the sources says how to size or time a test.
- **Validate, then ship one.** The house standards (`STD-when-to-animate-22`, `STD-visual-details-37`) agree with every source here. Moonly's "every element earned its place by winning a test" [S-L19-111] is the same rule applied to a whole screen [inferred].
- **Which number.** DC-L19-137 proposes recording the one number each change should move (proposed Q-pattern-13), and DC-L19-166 judges the whole system by product results before and after. The new sources add a guard: pair the conversion number with retention or churn, because a win on ARPU can hide 90 to 95% monthly churn [S-L19-106] and engagement can rise without a lasting habit [S-L19-105] [inferred proposal].
- **Conversion against trust.** The paywall consultant says a spin-the-wheel offer works for short-term weekly revenue while more people learn to close paywalls and wait for an offer [S-L19-104] [S-L19-106]; the video's narrator adds that people stop believing fake urgency once every app uses it [S-L19-104]. OpenDesigner's research lists fake urgency, hard-to-cancel flows and confirmshaming among deceptive patterns and proposes linting what a tool can detect (DC-L13-15); DC-L19-137 adds that no variant may drop below the accessibility floors to win, and that a trick that wins is still a deceptive pattern.
- **Attractiveness.** The research treats the aesthetic-usability effect as perceived usability only, never as evidence of usability (L13 research, law table). The ugly paywall that won [S-L19-104] fits that caution: looks alone do not predict results [inferred].
- **Before and after is weaker than a controlled test.** Other things change over time too, so [S-L19-038]'s before-and-after comparison is the minimum, not proof [inferred].

## Decisions this informs

- **Q-scope-06** (what the screens are for): `persuade` screens, and subscription paywalls, are where testing matters most.
- **Q-scope-01** (marketing site in scope).
- **Q-pattern-05** (how firmly to stop design tricks): conversion work is where the policy is tested; spin-the-wheel offers (a short-term tactic, in the consultant's words) and fake urgency (which the narrator says stops working once every app uses it) are the examples [S-L19-104] [S-L19-106].
- **Proposed Q-pattern-13** (DC-L19-137, "Which number should this page move, and how will you check it?"): the sources suggest also recording the guard metric (retention or churn) and the business type (quick launch or long-term) that decides the main number [S-L19-106] [inferred].
- **Q-gov-05** (how you will know the system helped): DC-L19-166's product-results option.

## Visual examples worth showing

- A short case-study card: services, problem, and solution with numbers, using the boutique-store example (better search and new product categories) [S-L19-038].
- A before-and-after analytics comparison around a redesign's launch date, labelled as not a controlled test [S-L19-038] [inferred].
- A paywall test board: the current paywall as control beside four to five radically different challengers (video, bullet list, trial timeline, long form) [S-L19-106].
- A metrics panel for a paywall test: paywall percentage against the 80% and 90% marks, trial-to-paid, LTV, day 1, 7 and 30 retention and churn [S-L19-106].
- Moonly's paywall image test: Disney-style 3D characters against the realistic sunset image that won [S-L19-111].
- The reported-results table above, as a card grid where each result carries its "self-reported" caveat [inferred].

## Open questions

- How should OpenDesigner help people measure a design change: record the metric a decision is meant to move (DC-L19-137), or leave measurement out of scope?
- No source explains how to run a test well (sample size, test length, one change at a time); [S-L19-106] only says to wait for significance.
- Should the builder warn when a conversion-focused pattern (a prize wheel, a countdown, a preselected option, a louder "yes") matches the deceptive-pattern list (DC-L13-15)?
- Device-based pricing (a higher price for newer phones on fast networks) is described as a late lever [S-L19-106]; no source discusses whether it is fair.
- Nearly all results come from consumer subscription apps; none covers business software, marketplaces or content sites.