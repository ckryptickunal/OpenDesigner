---
type: synthesis
title: A/B testing and conversion
created: 2026-09-24
updated: 2026-09-27
sources:
  - 5JxUJ1fuyO8
tags:
  - od-area-patterns
---
# A/B testing and conversion

## In short

Conversion means the share of visitors who do the thing a page is for, such as buying, signing up or getting in touch. The only source on this topic says a website's real job is usually more customers, sales or sign-ups, so design choices should be judged by what they do for that goal. For a site that already gets lots of visitors, improving conversion is worth more than attracting more of them. Check a redesign by comparing analytics before and after it ships, because small tests before launch rarely have enough people to prove anything. The house standards add that when you build two versions to compare, you should test them and ship the winner, and that a familiar pattern should only be broken with proof. This topic rests on one practitioner video, so treat its specific claims as opinion.

## House standards

- `STD-when-to-animate-22` (should): decide deliberately whether an idea deserves building; when you build option A and option B to compare, validate them and ship the one that wins, not both.
- `STD-visual-details-37` (should): break a familiar pattern only when you can prove the new one is better, and test it rather than assume.
- `STD-visual-details-44` (should): decide what not to build, and spend people's time, attention and trust only on features that pay off.

## What the sources teach

### Start from the business goal

- Behind "I need a website" there is usually a need for more customers, clients, sales or sign-ups; a site that looks good but serves no purpose still will not sell [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- Clients mostly judge a site on looks, while its users care about whether it works, so results depend more on UX than on UI; in the example, the fix for a store was better search and product categories, not a new look [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- A plain page can convert well if the information is clearly laid out and the next click is obvious, which is why the source says ClickFunnels-style pages work [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- Choose page sections for the goal they serve: testimonials to win clients for an agency, a list of last year's impact to win donations for a nonprofit [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).

### Where conversion work pays off

- For a site that already gets heavy traffic, conversion rate optimisation is a better add-on than SEO, because a small gain at that scale is worth a lot [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).

### Measuring impact

- Compare the site's analytics before and after the new design ships to see whether it had an effect; building the site yourself, or keeping view-only access, makes this possible [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- Do not treat a small pre-launch UX test as proof: the sample sizes you can gather are often too small to be significant [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).
- Report results as short case studies: the services provided, the problem, and the solution with numbers [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).

### Looks still matter

- Good looks and usability are not a trade-off: attractive designs are perceived as easier to use (the aesthetic-usability effect) [S-L19-038] ([[sources/5JxUJ1fuyO8-make-one-design-change-to-actually-land-clients-stop-struggling|Make ONE Design Change to Actually Land Clients (Stop Struggling)]]).

## Where they agree and disagree

- **Only one source.** Everything under "What the sources teach" comes from [S-L19-038]; no second practitioner source confirms or disputes it.
- **Test size.** OpenDesigner's research lists research methods by what they answer: A/B testing and analytics tell you which variant performs better and need large traffic, while qualitative usability testing with about five people per round is for finding problems (L13 research, Part D methods table; not a Decision Card). That supports [S-L19-038]'s warning: small tests find problems but do not prove impact [inferred].
- **Attractiveness.** The research rates the aesthetic-usability effect as being about perceived usability only: polish makes people tolerate small flaws and can hide problems during tests, so attractiveness is never evidence of usability (L13 research, law table). This agrees with [S-L19-038]'s wording ("perceived as easier to use") and adds a caution.
- **Validate, then ship one.** The house standards (`STD-when-to-animate-22`, `STD-visual-details-37`) agree with measuring before trusting a change; [S-L19-038]'s before-and-after comparison is a weaker check than a controlled A/B test, because other things change over time too [inferred].
- **Conversion pressure and design tricks.** The research's deceptive-pattern policy (fake urgency, confirmshaming, preselection, hard-to-cancel flows) names the places where conversion work tends to cross a line (DC-L13-15). [S-L19-038] does not discuss tricks.
- **Metrics in the research are about the system, not the product.** OpenDesigner's success-metric card measures design-system adoption, speed and satisfaction (DC-L11-20), not product conversion; no research card covers running product experiments. Two learning-wiki cards now propose ways to record product results: per design change (DC-L19-137) and for the system as a whole (DC-L19-166).
- **Other pages make untested claims.** The landing-page and pricing syntheses report conversion claims from practitioners without data; see [[synthesis/landing-pages|Landing pages synthesis]] and [[synthesis/paywalls-and-pricing-pages|Paywalls and pricing pages synthesis]].

## Decisions this informs

- **Q-scope-06** (what the screens are for): "persuade" screens are where conversion matters most.
- **Q-scope-01** (marketing site in scope).
- **Q-pattern-05** (how firmly to stop design tricks): conversion work is where the policy is tested.
- No current question asks how a design change will be measured; DC-L19-137 proposes one (Q-pattern-13) and DC-L19-166 an `outcomes` option for Q-gov-05. See the open questions.

## Visual examples worth showing

- A short case-study card: services, problem, and solution with numbers, using the source's boutique-store example (better search and new product categories) [S-L19-038].
- A before-and-after analytics comparison around a redesign's launch date, with a note that it is not a controlled test [S-L19-038] [inferred].

## Open questions

- How should OpenDesigner help people measure a design change: record the metric a decision is meant to move, or leave measurement out of scope?
- No source here covers how to run an A/B test (sample size, test length, one change at a time); the research method table only names the method.
- Should the builder warn when a conversion-focused pattern (urgency timers, preselected options, a louder "yes") matches the deceptive-pattern list (DC-L13-15)?
- The source's claims about what clients want and what sells come from one freelancer's experience; a second source would strengthen or correct them.
