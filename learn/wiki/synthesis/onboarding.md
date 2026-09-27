---
type: synthesis
title: Onboarding
created: 2026-09-24
updated: 2026-09-28
sources:
  - 14h1VnkQvIc
  - 9WVt1CelBfg
  - 9ypqs_2fAl8
  - E7RzEZ8GlHE
  - Gfsd8NNuD9g
  - Ksx9C2-3yMo
  - Qsq-Sj_rojU
  - Vy0KKvZJRH8
  - YbLF42BaoZs
  - ek-building-an-animation-course
  - eks-skills-find-animation-opportunities-skill
  - ixUq4HM4FNg
  - jSxxAFxjxbU
  - qK7WYCMvjUw
  - tNMAFjzapOk
tags:
  - od-area-patterns
---
# Onboarding

## In short

Onboarding is how a new person gets from first opening a product to the moment they feel its value, often called the aha moment. A Mobbin study of 1,460 flows found that length is not the point: the average app has 25 onboarding screens, and some of the longest flows belong to successful apps; what the good ones share is reaching value quickly, whether through a long but delightful flow, a few personal questions, or simply getting out of the way. Sell the outcome instead of listing features, make any questions pay off visibly, and teach in context (one tooltip, a checklist, a hint in an empty screen) rather than with pop-ups and tours. Ask for an account, permissions and payment only when they are needed and after the value is clear. Because people see it rarely, onboarding is one of the few places where the house standards allow delight and motion that explains how something works.

## House standards

- `STD-when-to-animate-09` (must): spend delight motion only on rare or first-time moments, and onboarding and first run are named examples.
- `STD-when-to-animate-10` (must): explanation motion, which shows how a feature works, is allowed only on marketing and onboarding surfaces.
- `STD-when-to-animate-08` (should): surfaces met occasionally get standard animation, not delight; the Expo table puts onboarding steps here.
- `STD-process-review-taste-67` (should): the first screen people land on after signing up sets the tone and shows the care they can expect from the rest of the product.
- `STD-visual-details-41` (should): ask for private data at the moment it is needed, only for what is needed, and say why.
- `STD-visual-details-49` (must): give feedback as soon as possible and validate form input inline rather than on submit.
- `STD-visual-details-39` (should): keep people in control by offering choices instead of one forced path.
- `STD-visual-details-33` (must): every screen answers "where am I, where can I go, what's here, how do I get out".
- `STD-springs-gestures-61` (must): haptics and sound only for meaningful moments, at most one haptic per action, and never on an entrance the person did not cause.
- `STD-springs-gestures-13` (must): never block input while a transition or stagger plays.
- `STD-when-to-animate-06` (must): never animate an action started from the keyboard; the change happens instantly.
- `STD-accessibility-motion-02` (must): under reduced motion, replace slides and springs with a short opacity cross-fade instead of removing all feedback.

## What the sources teach

### Aim for the aha moment, not a screen count

- Good onboarding goes sign up, set up, then the aha moment where people feel the value: for Airbnb the first booking, for Netflix watching a show, for Mobbin saving a screen to a collection [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- The average app in the sample has 25 onboarding screens; the longest categories are finance, health and fitness, and education, and some of the longest flows belong to some of the most successful apps. Web onboarding is 21% shorter than iOS, which the video suggests may be because mobile adds permission and paywall screens [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- Moonly's onboarding is 30 screens, built around the user's problem rather than the product's features: a small insight first, then the feature that solves that problem. About 10 versions run at once, each matched to the ad and App Store page the person came from, and the founder says this doubled lifetime value [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- Some products may need no onboarding at all: an inspiration library, or an AI chat where the first prompt is the value, may do best letting people in fast [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]). TikTok keeps onboarding to picking interests and the shortest tutorial, then learns from behaviour; only 30 to 50% of the first thousand videos rely on the onboarding answers [S-L19-077] ([[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok’s UX is so GOOD it should be ILLEGAL (seriously)]]).
- Industry shapes the flow: a banking onboarding is not a generic one. In a vendor demo, an AI that first researched shipped finance apps produced a fintech onboarding that covered identity checks and compliance, where the unresearched draft looked fine but generic [S-L19-108] ([[sources/YbLF42BaoZs-i-gave-claude-600-000-ui-screens-then-this-happened|I Gave Claude 600,000 UI Screens… Then This Happened]]).

### Sell the outcome first

- The best welcome screens sell the outcome instead of listing features: Timehop shows the product in action, Runkeeper's opening animation explains the app without words, Elma lets people try the core experience before signing up, and Superhuman turns its sign-up screen into a pitch with customer logos beside the form [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- A human touch works too: a founder's note with a handwritten signature (One Year), a personal CEO note after account creation (Basecamp), a CEO video after a host's first listing (Airbnb) [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]). After enrolling, students of an animation course land on a welcome page with a customisable "Motion Passport", which sets the tone [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- In a gamified savings app, onboarding asks to connect a bank account with a reassuring message, shows swipeable insights into past spending, and only then asks for a savings goal [S-L19-078] ([[sources/jSxxAFxjxbU-i-spent-a-week-gamifying-apps-this-is-what-i-built|I spent a week gamifying apps. This is what I built]]).

### Personalise, then show what the answers unlocked

- Only 23% of apps personalise during onboarding, and 7% of AI apps; AI tools seem to learn from use instead [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- Make the questions worth the time: Tide asks two questions and customises recommendations as you watch; Headspace lets people pick more than one goal (+10% free-trial conversion); Dollar Shave Club made its quiz copy conversational (+5% subscriptions); Focus Flight lets people pick a map style so the app feels theirs [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- Then show what the answers unlocked: a personal plan with the date the goal will be reached, a home page already filled with matching courses (Brilliant), or one screen promising you will be able to communicate while travelling in France in 2 months (Speak) [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- Moonly uses onboarding answers to shape the first session, down to the home screen's quick-access buttons, and reports day-1 retention of 41% and day-7 of 37% [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

### Teach in context instead of explaining everything

- Start with a single tooltip on the most important action, then a second tooltip or a simple checklist in a corner once it is done. Avoid a modal that explains the whole product in six bullet points at first login, and avoid dropping first-time users onto a fully loaded dashboard [S-L19-056] ([[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]).
- Mural replaced pop-ups and banners with a clear six-step checklist and saw a 10% relative rise in one-week retention; a checklist stays after the first flow is dismissed [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- Do not front-load education: Cake Equity explains equity and vesting step by step with reassuring copy and tooltips that state each step's impact. Small aids remove reasons to get stuck: a progress indicator, helpful microcopy, a password field that ticks off each requirement as you type, and a small nudge in an empty screen instead of a tour [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- On first login, a full-screen empty state can draw attention to the main "plus" action, with a simple popover explaining how the app works [S-L19-053] ([[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]).
- Desktop apps should not skip onboarding either. A simple modal can teach a keyboard shortcut by asking the user to perform it (the modal closes when they do), backed by a shortcut cheat sheet [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).

### Accounts, sign-up and permissions

- When to ask for an account varies: first (the pattern the video describes), after trying the core experience (Duolingo puts 60 screens, including a first lesson, before sign-up), or after personalisation (Tide) [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- Ask why a login is needed before copying one: Moonly removed login entirely, because data already lived in the Apple keychain and email marketing was not paying off; only 12% of apps on Mobbin have no sign-up or login step anywhere [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- A five-screen sign-up shows the small decisions hiding in onboarding: an escape link to log in, email verification that either blocks or gently reminds (the source says neither is wrong), and a team-size question that sends teams to an invite step and lets individuals skip it [S-L19-043] ([[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]]).
- Splitting a sign-up form across several screens raised House's conversions by 15%; the video suggests friction added in one place can remove it in another [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- Many apps show their own screen explaining the benefit before the system notification prompt (Brilliant: reminders to make learning a habit), and Center also previews the notification; the video says this "apparently" improves accept rates a lot, without a figure [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).

### Paywalls at the end of onboarding

- The after-onboarding paywall is the most used: 78% of iOS apps on Mobbin show one; the paywall consultant prefers creating the account first, though his tests of the order were inconclusive [S-L19-106] ([[sources/E7RzEZ8GlHE-he-tested-4-700-paywalls-these-won|He Tested 4,700 Paywalls. These Won.]]).
- The paywall should feel like the natural end of onboarding: "your plan is ready", in the language of the outcome the person wants [S-L19-104] ([[sources/9ypqs_2fAl8-we-studied-2-995-paywalls-heres-what-actually-converts|We Studied 2,995 Paywalls. Here’s What Actually Converts.]]). Examples put a page of social proof first (Timely), recommend plans from quiz answers (Grammarly, almost +20% upgrades) or make the offer playful (Focus Flight's ticket that "prints" with a vibration) [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]). See the [[synthesis/paywalls-and-pricing-pages|Paywalls and pricing pages synthesis]].

### Keep long flows alive: delight and motion

- Long flows can feel short when something is always happening: Bump animates even its loading and verification steps, and one 61-screen flow lets people name a lovable virtual pet raccoon before a personal plan and a paywall [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).
- First-run and onboarding moments are eligible for delight (bounce, a generous stagger, a longer beat), and explanation motion is allowed there [S-L19-024] ([[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]).
- On mobile, onboarding is the best time to captivate: a clean, focused UI first, then an animation such as a swipe, then a small surprise. A screen sliding in from the left shows progress through the flow, and tools that slide up from the bottom read as temporary [S-L19-084] ([[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]).
- A step-by-step flow can use a "next" control that works by tap or swipe, with motion that follows the swipe; swipe gestures should always have a visible button for people who do not know them [S-L19-035] ([[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]).
- Culture matters: the onboarding video says people in Eastern markets tend to find information-heavy screens efficient rather than cluttered, so a successful flow cannot simply be copied; it gives no source for this [S-L19-107] ([[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]).

## Where they agree and disagree

- **Short or long.** The Kole Jain videos favour short, sequenced help [S-L19-053] [S-L19-056]; [S-L19-107] and [S-L19-111] say long flows work when each screen personalises or moves toward value. This fits OpenDesigner's research better than it first looks: DC-L13-11 advises against forced tours but says a setup and personalisation flow is warranted when the product needs data, and the long flows praised here are mostly that kind [inferred]. The link between long flows and success is observational; long flows belonging to successful apps does not show that length causes success.
- **Checklists over pop-ups (now two voices).** [S-L19-056] (Kole Jain) and [S-L19-107] (Mobbin, with Mural's figure) both prefer a checklist and in-context hints to pop-ups and tours. This supports DC-L19-129's proposed default (one tip on the main action, then a small checklist) and DC-L13-11's contextual help.
- **Does it need onboarding at all?** [S-L19-107]'s "let people in fast" for products whose first use is the value matches DC-L13-11's first option (a self-explaining UI, no onboarding). [S-L19-067] says desktop apps should not skip it; teaching shortcuts in context is itself contextual help, so the two fit [inferred].
- **Sign up first or value first.** [S-L19-107] describes sign up, set up, aha as the pattern, yet praises flows that put value before sign-up (Duolingo, Tide, Elma) and does not reconcile the two. [S-L19-078] shows value before asking for effort, and [S-L19-111] dropped login altogether. The house rule to ask for private data only when it is needed (`STD-visual-details-41`) favours asking for an account when the product actually needs one [inferred].
- **Permission primers.** [S-L19-107]'s benefit screen before the system prompt matches `STD-visual-details-41` (say why). DC-L13-15 treats asking again after a dismissal as nagging, so a primer asks once and a "not now" sticks [inferred]. The first version of DC-L19-135 noted that no source covered notification permission prompts; this one does, though without data.
- **Two paywall numbers that do not compare.** 22% of over 900 apps and websites show a paywall during onboarding [S-L19-107]; 78% of iOS apps on Mobbin show one after it [S-L19-106]. They count different things in different samples [inferred].
- **Fewer steps or split steps.** House's split sign-up [S-L19-107] adds screens, while `STD-visual-details-35` asks for fewer steps. It is one case result; fewer fields per screen may be what helped [inferred].
- **Swipeable slide decks.** The circle-wrap slides in [S-L19-035] and the Craft example in [S-L19-084] look like the "deck-of-cards tutorial" the research does not recommend (DC-L13-11) [inferred mapping]. The sources praise these flows for how they feel, not for how much people learn.
- **How much motion.** Delight belongs to the first run (`STD-when-to-animate-09`), while repeated onboarding steps get standard motion (`STD-when-to-animate-08`). Animated verification in onboarding [S-L19-107] fits the first case; the same states met daily in the product stay plain (`STD-when-to-animate-04`) [inferred]. Sliding screens to show progress [S-L19-084] matches the shared-axis transition, which becomes a fade under reduced motion (DC-L04-23, `STD-accessibility-motion-02`).
- **Shortcut feedback without animation.** [S-L19-067] says every shortcut needs visible feedback; the house standard forbids animating keyboard-initiated actions (`STD-when-to-animate-06`), so the state change should be instant [inferred].
- **Progressive disclosure.** [S-L19-056] calls onboarding a form of progressive disclosure: sequencing features rather than hiding them. The research's disclosure rules (at most two levels, never hover-only for essentials) apply to coachmarks too (DC-L13-03).
- **Who is speaking.** Most older sources are Kole Jain videos; the new ones are Mobbin videos that draw on Mobbin's library and promote it. The cited results (Headspace, Dollar Shave Club, Grammarly, Mural, House, Moonly) come without sample sizes.

## Decisions this informs

- **Q-pattern-04** (empty screens and how first-time users learn): `onboarding-none` suits products whose first use is the value [S-L19-107]; otherwise `onboarding-contextual` with a persistent checklist [S-L19-056] [S-L19-107], plus `empty-kinds`; `walkthrough` only for genuinely new, complex screens.
- **Proposed Q-pattern-07** (DC-L19-129, how first-time users learn) and its sign-up follow-up (proposed Q-pattern-15): "when to ask for an account", with DC-L19-156's options (`none`, `before-use`, `after-value`, `before-paywall`) plus `after-personalising`, and a permission primer in the setup checklist [S-L19-106] [S-L19-107] [S-L19-111] [inferred].
- **Q-form-02** (when forms check answers): a password field that ticks off requirements as people type [S-L19-107].
- **Q-voice-02** (tone for errors, success and first use) and **Q-voice-06** (per-component copy): conversational quiz questions and reassuring copy at each step [S-L19-107].
- **Q-pattern-03** (show everything or tuck extras away): onboarding sequences features [S-L19-056].
- **Q-motion-06** (screen changes): `shared-axis` x for onboarding steps.
- **Q-brand-04** and **Q-motion-01** (hero moments): the first run is a natural hero moment.
- **Q-motion-09** (haptics): at most one haptic, and only on the person's own action, such as the tap that claims an offer. A vibration that fires as an offer appears, like Focus Flight's printing ticket [S-L19-107], is an entrance the person did not cause, which `STD-springs-gestures-61` forbids (DC-L19-98) [inferred application].
- **Q-img-04** (illustrations or a mascot): a character in onboarding, such as the nameable raccoon [S-L19-107].
- **Q-plat-03** (input methods): desktop apps with keyboard shortcuts need a way to teach them [S-L19-067].
- **Q-scope-06** (what the screens are for): `persuade` and `experience` products tend to have longer, personalised flows [inferred].

## Visual examples worth showing

- Welcome screens that sell the outcome: Timehop's product in action, Superhuman's sign-up with logos beside the form [S-L19-107].
- A goal question with several answers allowed (Headspace), then the result screen: Speak's "in 2 months" promise with its small graph, or Brilliant's home already filled with matching courses [S-L19-107].
- Mural's six-step checklist beside the pop-ups it replaced, and a tooltip on the main action followed by a corner checklist beside the rejected six-bullet welcome modal [S-L19-107] [S-L19-056].
- A notification primer: Brilliant's benefit screen and Center's preview of the notification [S-L19-107].
- A password field ticking off requirements as you type [S-L19-107].
- Moonly's first home screen, with quick-access buttons chosen from onboarding answers [S-L19-111].
- A fintech onboarding drafted without research beside one grounded in real finance apps, with identity checks [S-L19-108].
- A full-screen first-use empty state with a popover on the plus button [S-L19-053]; the branching five-screen sign-up [S-L19-043]; a shortcut-teaching modal that closes when the user performs it [S-L19-067]; the Motion Passport welcome page [S-L19-007].

## Open questions

- How should OpenDesigner decide between a short and a long flow? The sources say "it depends on the product" [S-L19-107]; a rule of thumb (for example, only as long as the personalisation it pays for) would be [inferred].
- How long should a checklist be, and when should it disappear? Mural's has six steps and stays after dismissal [S-L19-107]; no source says when it goes away.
- Keyboard and screen-reader access to tooltips, coachmarks and checklists is not discussed by any source; the research asks for it (DC-L13-11).
- Where does "standard motion for onboarding steps" end and "first-run delight" begin? The standards name both, and a product needs a rule of thumb [inferred].
- The claim about information density in Eastern markets [S-L19-107] has no source; should OpenDesigner ask about the audience's region?