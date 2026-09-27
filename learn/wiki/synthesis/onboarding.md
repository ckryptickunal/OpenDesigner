---
type: synthesis
title: Onboarding
created: 2026-09-24
updated: 2026-09-27
sources:
  - 14h1VnkQvIc
  - 9WVt1CelBfg
  - Gfsd8NNuD9g
  - Ksx9C2-3yMo
  - Vy0KKvZJRH8
  - ek-building-an-animation-course
  - eks-skills-find-animation-opportunities-skill
  - ixUq4HM4FNg
  - jSxxAFxjxbU
  - tNMAFjzapOk
tags:
  - od-area-patterns
---
# Onboarding

## In short

Onboarding is how a new person gets from signing up to their first success with the product. The sources, mostly one practitioner (Kole Jain), prefer short, sequenced help to a long tour: point at the single most important action, show the product's value before asking for effort, and let empty screens teach. Ask only for what the product needs, when it needs it, and say why. Because people see it rarely, onboarding is one of the few places where the house standards allow delight and motion that explains how something works.

## House standards

- `STD-when-to-animate-09` (must): spend delight motion only on rare or first-time moments, and onboarding and first run are named examples.
- `STD-when-to-animate-10` (must): explanation motion, which shows how a feature works, is allowed only on marketing and onboarding surfaces.
- `STD-when-to-animate-08` (should): surfaces met occasionally get standard animation, not delight; the Expo table puts onboarding steps here.
- `STD-process-review-taste-67` (should): the first screen people land on after signing up sets the tone and shows the care they can expect from the rest of the product.
- `STD-visual-details-41` (should): ask for private data at the moment it is needed, only for what is needed, and say why.
- `STD-visual-details-39` (should): keep people in control by offering choices instead of one forced path.
- `STD-visual-details-33` (must): every screen answers "where am I, where can I go, what's here, how do I get out".
- `STD-springs-gestures-13` (must): never block input while a transition or stagger plays.
- `STD-when-to-animate-06` (must): never animate an action started from the keyboard; the change happens instantly.
- `STD-accessibility-motion-02` (must): under reduced motion, replace slides and springs with a short opacity cross-fade instead of removing all feedback.

## What the sources teach

### Sequence the help instead of explaining everything

- Start with a single tooltip on the most important action, then a second tooltip or a simple checklist in a corner once it is done. Avoid a modal that explains the whole product in six bullet points at first login, and avoid dropping first-time users onto a fully loaded dashboard [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]).
- On first login, a full-screen empty state can draw attention to the main "plus" action, with a simple popover explaining how the app works, instead of cards inviting people to add content [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]).
- Desktop apps should not skip onboarding either. A simple modal can teach a keyboard shortcut by asking the user to perform it (the modal closes when they do), backed by a shortcut cheat sheet [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).
- TikTok keeps onboarding to picking interests and the shortest tutorial, then learns from behaviour; only 30 to 50% of the first thousand videos rely on the onboarding answers [S-L19-077] ([[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok’s UX is so GOOD it should be ILLEGAL (seriously)]]).

### Show value before asking for effort

- In a gamified savings app, onboarding welcomes the user, asks them to connect a bank account with a reassuring message, shows swipeable insights into their past spending, and only then asks for a savings goal with a slider for the time period [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).
- A five-screen sign-up flow shows the small decisions hiding in onboarding: an escape link to log in for people who landed on sign-up by mistake, email verification that either blocks or gently reminds (the source says neither is wrong), and a team-size question that sends teams to an invite step and lets individuals skip it [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]).

### First impression, delight and motion

- After enrolling, students of an animation course land on a welcome page with a customisable "Motion Passport", which sets the tone and shows the care to expect [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- First-run and onboarding moments are eligible for delight (bounce, a generous stagger, a longer beat), and explanation motion is allowed there [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]).
- On mobile, onboarding is the best time to captivate: a clean, focused UI first, then an animation such as a swipe, then a small surprise. A screen sliding in from the left shows progress through the flow, and tools that slide up from the bottom read as temporary [S-L19-084] ([[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]).
- A step-by-step flow can use a "next" control that works by tap or swipe, with motion that follows the swipe and wraps into the next slide; swipe gestures should always have a visible button for people who do not know them [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]).

## Where they agree and disagree

- **Contextual help beats a tour.** [S-L19-053], [S-L19-056] and [S-L19-067] all favour small, in-context help; all three are Kole Jain videos, so this is one practitioner's view until the research backs it. The research agrees: no forced tour, contextual help and empty-state guidance first, everything skippable, and a warning lint for a tour with no skip control (DC-L13-11). The six-bullet welcome modal that [S-L19-056] rejects is the kind of up-front explanation the research also advises against.
- **Swipeable slide decks.** The circle-wrap slides in [S-L19-035] and the Craft example in [S-L19-084] look like the "deck-of-cards tutorial" that the research does not recommend because it makes the UI look more complicated than it is (DC-L13-11) [inferred mapping]. The sources praise these flows for how they feel, not for how much people learn.
- **Skip onboarding or not.** [S-L19-067] says desktop apps should not skip it, while the research's first recommendation is to avoid onboarding where the UI can explain itself (DC-L13-11). Teaching shortcuts in context, as [S-L19-067] does, is a form of contextual help, so the two fit together [inferred].
- **Ask for data only when it pays off.** [S-L19-078] (reassurance before the bank connection, then value before the savings goal) and [S-L19-077] (short interest pick, then learn) match the research case where a setup or personalization flow is warranted because the product needs data (DC-L13-11), and the house rule on private data (`STD-visual-details-41`).
- **Shortcut feedback without animation.** [S-L19-067] says every shortcut needs visible feedback, a micro-animation or at least a state change. The house standard forbids animating keyboard-initiated actions (`STD-when-to-animate-06`), so the state change should be instant [inferred].
- **How much motion.** Delight belongs to the first run (`STD-when-to-animate-09`), while repeated onboarding steps get standard motion (`STD-when-to-animate-08`). Sliding screens to show progress [S-L19-084] matches the research's shared-axis transition, which Material uses on the x axis for onboarding (DC-L04-23); under reduced motion that spatial slide should become a fade (DC-L04-23, `STD-accessibility-motion-02`).
- **Progressive disclosure.** [S-L19-056] calls onboarding a form of progressive disclosure: sequencing features rather than hiding them. The research's disclosure rules (at most two levels, never hover-only for essentials) apply to coachmarks too (DC-L13-03).

## Decisions this informs

- **Q-pattern-04** (empty screens and how first-time users learn): the sources support "onboarding-contextual" together with "empty-kinds"; "walkthrough" only for genuinely new, complex screens.
- **Q-pattern-03** (show everything or tuck extras away): onboarding sequences features [S-L19-056].
- **Q-motion-06** (screen changes): "shared-axis" x for onboarding steps.
- **Q-brand-04** and **Q-motion-01** (hero moments): the first run is a natural hero moment.
- **Q-voice-02** (tone for errors, success and first use).
- **Q-img-04** (illustrations or a mascot, and where they go): first-use empty states are a candidate place.
- **Q-plat-03** (input methods): desktop apps with keyboard shortcuts need a way to teach them [S-L19-067].

## Visual examples worth showing

- A tooltip pointing at the main action, followed by a small corner checklist, next to the rejected six-bullet welcome modal [S-L19-056].
- A full-screen first-use empty state with a popover on the plus button [S-L19-053].
- The savings-app onboarding: bank connection with reassurance, swipeable spending insights, and a goal screen with a time slider [S-L19-078].
- The branching five-screen sign-up, where teams get an invite step and individuals skip it [S-L19-043].
- A circle-wrap "next" button that works by tap or swipe [S-L19-035].
- A shortcut-teaching modal that closes when the user performs the shortcut [S-L19-067].
- The Motion Passport welcome page [S-L19-007].
- Craft's mobile onboarding: focused UI, swipe animation, then a surprise [S-L19-084].

## Open questions

- None of the sources measures whether its onboarding works (completion, activation, retention); see [[synthesis/a-b-testing-and-conversion|A/B testing and conversion synthesis]].
- How long should an onboarding checklist be, and when should it disappear? Not covered.
- Keyboard and screen-reader access to tooltips and coachmarks is not discussed by any source; the research asks for it (DC-L13-11).
- Where does "standard motion for onboarding steps" end and "first-run delight" begin? The standards name both, and a product needs a rule of thumb [inferred].
