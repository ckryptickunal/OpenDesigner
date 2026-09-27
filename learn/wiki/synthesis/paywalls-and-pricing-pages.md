---
type: synthesis
title: Paywalls and pricing pages
created: 2026-09-24
updated: 2026-09-27
sources:
  - BUDipdbKK7Y
  - PDcQJOPby1k
  - gKM6b2EnW1k
  - ld1zhQMXxXU
  - pGYLZyBE32o
tags:
  - od-area-patterns
---
# Paywalls and pricing pages

## In short

A pricing page helps people choose a plan and trust what they will pay. The sources agree on a few moves: offer fewer plans, make the monthly price bigger than the plan name, show the real discount and the real billing terms, and show what the next plan adds. Options that few visitors need, such as Enterprise, can shrink to a small button. Walls that block simple content, and upsells paired with guilt, are shown as what makes products maddening. All five sources are videos by one practitioner (Kole Jain), and none of them measures what these changes do to sales.

## House standards

- `STD-visual-details-02` (must): use tabular digits on price columns and numbers that change in place.
- `STD-visual-details-59` (must): when a price animates (for example on a monthly or yearly switch [inferred]), use NumberFlow instead of re-rendering the text.
- `STD-visual-details-29` (should): make the most important thing on the screen the most obvious.
- `STD-visual-details-35` (should): keep interface copy plain and concise.
- `STD-visual-details-44` (should): spend the user's time, attention and trust only on features that pay off.
- `STD-accessibility-motion-15` (must): put hover animations inside `@media (hover: hover) and (pointer: fine)`, which applies to hover reveals on upgrade prompts [inferred].

## What the sources teach

### Fewer, clearer plans

- Five plans is not ideal; drop at least one, and rename a very high-volume plan to Enterprise, because customers at that volume probably need more than a fixed plan [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- Merge landing pages that sell the same thing into one plans section built on the few points that matter (for an AI product: cost, a better model, document uploads). Put Enterprise behind a tiny button on every plan, because the creator estimates it is irrelevant to about 98% of visitors, and make the purchase call to action one of the cards, marked with a gradient stroke [S-L19-082] ([[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]).

### A pricing card with the right hierarchy

- Make the plan name smaller and the monthly cost larger, because people care about the cost, not the name, and drop elements that add nothing [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- Give each plan a name and a short description, use check marks instead of bullets, list a feature the plan lacks, make the button an outline button if it moves up the card, separate the price from the features with a light tint of the primary color instead of a divider line, and write an actionable button label [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).

### Honest numbers

- Show the actual discount; without it, discounted plans look cheaper than lower tiers and the order stops making sense. Show what the next plan includes that the current one does not, a pattern common on software pricing pages such as Resend and Supabase [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- Add a short note under the price with the real billing terms, so people do not feel misled when they find out what they actually pay [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- In the product's billing area, use tabs (billing, usage and more), show usage as a few small donut charts, and include the billing email and payment method [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).

### Upgrade prompts inside the product

- Hovering an upgrade prompt can reveal the higher plan's limits (an idea taken from Dub) with a slide-in where the old number disappears, instead of Dub's crossed-out text [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).

### Walls and upsells to avoid

- Do not put a paywall or an account wall in front of simple content such as a recipe, do not sell premium subscriptions that add nothing, and do not shame people about their usage and then offer only an upsell or more notifications [S-L19-048] ([[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]).

## Where they agree and disagree

- **Honesty is the common thread.** Showing the real discount and billing terms [S-L19-061] [S-L19-075] lines up with the research's deceptive-pattern list, which names hidden costs, hidden subscriptions, comparison prevention and confirmshaming, and names pricing pages as a place the policy applies (DC-L13-15) [inferred mapping]. The usage-shaming upsell in [S-L19-048] is close to confirmshaming and nagging in that list [inferred]. OpenDesigner's current default for Q-pattern-05 is "enforced".
- **Plan count.** "Five is too many" comes from one video [S-L19-061] and no Decision Card sets a number, so treat it as opinion. The L13 research's law table suggests an info-level lint for plan pickers with more than 3-4 tiers and no suggested plan or comparison, itself marked [inferred] there.
- **Making Enterprise small.** [S-L19-082] shrinks an option most visitors do not need; it stays visible on every plan, so it is not hidden in the deceptive-pattern sense [inferred]. The 98% figure is the creator's estimate, not data.
- **One highlighted choice.** [S-L19-075] tones the card button down to an outline, and [S-L19-082] turns the purchase action into a highlighted card. Both fit the research rule of at most one high-emphasis action per region (DC-L13-18) [inferred].
- **Hover reveals.** [S-L19-079] relies on hover, which touch screens do not have; the house rule gates hover motion to fine pointers (`STD-accessibility-motion-15`), so the plan limits also need to be readable without hover [inferred].
- **Gradients.** The gradient stroke on the purchase card [S-L19-082] is a brand moment; Q-color-25 defaults gradients to brand-only use.

## Decisions this informs

- **Q-pattern-05** (how firmly to stop design tricks): pricing and paywalls are where it matters most.
- **Q-type-06** (numbers font and tabular digits) and **Q-voice-05** (writing rules, including numbers).
- **Q-state-01** (button styles and how many main buttons per area): one highlighted plan or purchase card.
- **Q-color-25** (where gradients are allowed): gradient strokes on the purchase card [S-L19-082].
- **Q-scope-06** ("persuade" screens) and **Q-scope-01** (marketing site in scope).

## Visual examples worth showing

- A pricing card before and after: check marks, a missing feature listed, a name and description, billing text under the price, a tinted price area and an outline button [S-L19-075].
- A vibe-coded pricing page fixed: five plans cut down, plan names smaller, prices larger, the actual discount shown and the next plan's extras listed [S-L19-061].
- Merged AI plans where the purchase call to action is a card with a gradient stroke and Enterprise is a tiny button on each plan [S-L19-082].
- An upgrade prompt whose limits slide in on hover, next to the crossed-out-text version [S-L19-079].
- A billing and usage page with tabs and small donut charts [S-L19-061].
- The anti-pattern: a recipe behind a paywall or account wall [S-L19-048].

## Open questions

- None of the sources covers mobile app paywalls, free trials, or when to show a paywall in a flow.
- Monthly versus yearly switches, taxes, currencies and local prices are not covered.
- Cancelling a plan is not covered; the research treats "harder to cancel than to subscribe" as a deceptive pattern (DC-L13-15).
- No source reports conversion data, so none of these changes is proven to sell more; see [[synthesis/a-b-testing-and-conversion|A/B testing and conversion synthesis]].
