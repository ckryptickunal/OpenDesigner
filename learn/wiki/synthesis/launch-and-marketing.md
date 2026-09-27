---
type: synthesis
title: Launch and marketing
created: 2026-09-27
updated: 2026-09-28
sources:
  - ek-building-a-toast-component
  - ek-building-an-animation-course
  - qK7WYCMvjUw
tags:
  - od-area-process
---

# Launch and marketing

## In short

Launch and marketing here means how a product gets finished, introduced, found and talked about. Two sources cover it from opposite ends: Emil Kowalski's look back at building his animation course, a maker who relies on word of mouth, and a Mobbin interview with the founder of Moonly, an astrology app that grows through ads and tests almost everything. Emil's lessons are to finish before announcing (a presale with a public deadline helped him, teasing did not), to invest in packaging such as the logo and the first screen after sign-up, to keep the product alive with updates and a changelog, and to make something good enough that people spread it; several of these are house standards because the owner marked his source non-negotiable. Moonly's founder adds that App Store featuring now brings the wrong visitors to niche apps, that each ad should lead to a matching store page and onboarding, that people share insights about themselves rather than features, and that a lean web funnel should test the market before the full app is built. Each point rests on one maker's or one app's experience, so the marketing claims are opinion until another source agrees.

## House standards

Emil Kowalski's source is non-negotiable, and these house standards come from it:

- `STD-process-review-taste-66` (should): do not publicly tease a project before it is done; if you need outside pressure to finish, commit to something concrete such as a public deadline.
- `STD-process-review-taste-50` (should): a product that merely works is not finished; invest in its look and feel, good defaults and good animations, and go the extra mile rather than ship something mediocre.
- `STD-process-review-taste-67` (should): the first screen people land on after signing up is part of the packaging; design it to set the tone and show the care they can expect from the rest of the product.
- `STD-process-review-taste-63` (should): keep shipping updates, refresh existing parts as you learn better ways, and record every update on a changelog page.
- `STD-process-review-taste-59` (must): when teaching or explaining motion, let people play with interactive demos, including bad-versus-good examples, rather than text alone.
- `STD-process-review-taste-62` (should): save work in built-in editors and exercises automatically, so stopping midway loses nothing.
- `STD-process-review-taste-55` (should): package taste for coding agents as written rule files, one per aspect of the interface, each rule strict and with its reason.
- `STD-process-review-taste-56` (should): whoever ships animation code understands how it works, even when a model wrote it.

Also relevant to launch material, from other non-negotiable sources: `STD-when-to-animate-11` (must) keeps decorative motion such as animated illustrations on marketing pages and illustrations, and `STD-accessibility-motion-02` (must) keeps a gentle cross-fade under reduced motion. `STD-when-to-animate-22` (should), decide whether an idea deserves to be built before building it, is the standard closest to Moonly's web-funnel advice [inferred]. Emil's source also feeds `STD-easing-duration-01`, `STD-easing-duration-03`, `STD-mobile-touch-05`, `STD-accessibility-motion-17` and `STD-process-review-taste-01`, which belong to the [[synthesis/easing-and-timing|Easing and timing synthesis]] and the [[synthesis/micro-interactions|Micro-interactions synthesis]]. The Moonly interview is a reference source and adds no standards.

## What the sources teach

### Finish before you announce

- Teasing a project can drain the will to finish it: talking about ui.land already felt rewarding enough, and the project teased in December 2021 launched only in January 2023 [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- What helped most was opening a presale for the course when it had no content yet, with a public deadline. People had already paid, so he had to deliver, which is good outside motivation "as long as you can handle the pressure" [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]). The presale opened in January 2024, and the announcement was made before any work on the course began [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).

### Check the market before the full build

- Moonly's founder recommends starting with a web funnel: it gives more freedom and instant signals from the market, and one person can build it with AI agents or with one front-end developer. He advises moving slowly and cheaply, because the common mistake is spending millions on a product before learning that the market for it does not exist; in 2026, he says, positive unit economics are very hard to reach in an app [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

### Packaging makes the first impression

- People love beautiful things: the content is the main value, but the look and feel, which he counts as packaging, creates the first impression [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- The logo came from how people describe good animation: buttery smooth became a butter cube, designed with Nev Flynn and reused across the site in several forms. As enrolment nears its close, the cube melts a little more each hour through animated SVG paths [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- The hero's illustrations animate on hover and some respond to clicks. A course student animated them, so the hero also shows what the course enables [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- Onboarding is packaging too: after enrolling, people land on a welcome page with a customisable Motion Passport, which sets the tone and shows the care to expect [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- The idea can extend to physical goods, such as a sticker pack for early students or keycaps; both are plans, not shipped [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).

### Getting found: ads, store pages and featuring

- Being featured on the App Store "worked greatly 15 years ago", but today it tends to bring irrelevant traffic with worse conversion, and the store's algorithms may then rank the app lower in search. Featuring can still work for universal apps such as calculators or flashlights, but is not particularly useful for niche apps [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- Moonly's own attribution engine links each ad to a custom App Store product page, then to a matching onboarding flow and app experience. Someone who searches for a specific feature sees a fully customised page and screenshot set; a generic search shows the standard page. About 10 onboarding flows run in production, each built around one user job, and customising them doubled customer lifetime value, which let the company double its ad spend in a single month [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]). How those flows are built is covered in the [[synthesis/onboarding|Onboarding synthesis]].
- Email has not paid off for Moonly: despite years of effort and strong open rates, sending more than a million emails over months cost a significant amount without making email marketing work efficiently, one reason the app dropped its login screen [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

### A product built for how people use it

- The course runs on a platform made for the subject: interactive demos in every lesson, because people have to feel the difference between good and bad; a built-in code editor, so there is no repository to clone or environment to set up; automatic saving; and every solution as both a video and a written version, across more than 50 exercises. Students single out the demos and the editor [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]). How these teach is covered in the [[synthesis/design-process|Design process synthesis]].

### Keep it alive after launch

- Every enrolment includes free updates, so the course is a living thing that evolves rather than a snapshot in time. Updates can be new lessons (the Animations and AI lesson came from them) or refreshed ones (he fully refreshed the theory module as he learned to teach better), and a changelog page records them all [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- One update gave students a SKILL.md file for coding agents, holding the course's knowledge, free as part of the ongoing updates [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).

### Sharing: let quality spread it, or build the share moment in

- If you make great things and make sure a few people see them, word spreads, because people like sharing what they like; he calls this organic marketing the best kind and says it happened to Sonner, Vaul and the course [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- He has built his career on that premise: make things he would be proud of, go the extra mile, and accept that it won't always work, since there is no point in making something mediocre [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- When enrolment opens, people talk about the course, and when someone asks whether it is worth it, others answer with positive reviews; his example is a reply thread under Ryan Florence's post about enrolling. The aim is a product people cannot stop talking about, which he calls a win for everyone: students get value, he helps more people, and the course gets more exposure [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- People who are curious can join a waitlist that gives a few preview lessons at once and tips by email every two weeks [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- Moonly designs the share moment instead: "People don't share features, they share insights about themselves." When someone takes a screenshot in the app, a ready-made flow lets them share it in one tap; 23% of users share something, which brought millions of free views [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

### Reading these sources

- Much of Emil's page is testimonials and promotion for the course and a newer one; the praise is other people's opinion, and the enrolment figures and like counts are snapshots. The page has no publish date; its embedded posts run to January 2026 [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- The Moonly interview is Mobbin channel content that ends with a plug for the channel. Its figures are self-reported by the founder, come from one bootstrapped astrology app, and describe store and payment rules as of 2026, which may change [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).

## Where they agree and disagree

Between the two sources:

- **Word of mouth, left to quality or built in:** Emil counts on making something good and letting people share what they like [S-L19-007]; Moonly builds a one-tap share flow around the moment someone screenshots an insight about themselves [S-L19-111]. Both rely on people passing the product on; they differ in whether the product prompts it [inferred].
- **The right audience over the biggest one:** Emil wants a few of the right people to see the work [S-L19-007]; Moonly warns that broad featuring brings irrelevant visitors who can hurt a niche app's search ranking [S-L19-111] [inferred].
- **Paid or organic:** Moonly grows through ads, with a store page and an onboarding flow for each [S-L19-111]; Emil names no paid channel and calls organic marketing the best kind [S-L19-007]. They sell different things, a subscription app and a course by an author with an audience, so neither result carries over to the other without a test [inferred].
- **Commit before building:** Emil opened a paid presale with a public deadline before the course had any content [S-L19-007]; Moonly recommends a lean web funnel before the full app [S-L19-111]. Both put something in front of real buyers before the expensive part, though Emil's stated reason is his own motivation and Moonly's is market risk [inferred]. Neither is a teaser in the sense of `STD-process-review-taste-66`, which is about announcing unfinished work for attention [inferred].
- **Email:** Emil keeps a waitlist that sends tips every two weeks [S-L19-007]; Moonly has not made email marketing work efficiently, even after more than a million emails [S-L19-111]. One is a small list of people who asked, the other mass email to app users [inferred].

Against OpenDesigner's research, the other learning-wiki cards and the house standards:

- **Changelogs (agree).** DC-L11-22 finds release notes the most common way design-system teams announce changes (56% of teams), lists changelogs among Brad Frost's rituals, and sets a minimum of release notes every release, a roadmap and a support channel. DC-L19-169 turns Emil's changelog page into Q-gov-06's default wording. DC-L11-22 also reports that only 39% of teams are satisfied with how changes are communicated, so a changelog alone may not be enough [inferred].
- **Teasing versus a public roadmap (a tension).** DC-L11-22's minimum includes a public roadmap, which announces unfinished work. `STD-process-review-taste-66` advises against teasing, but its reason is the maker's motivation, and it allows committing to something concrete such as a public deadline; a dated roadmap for a system's users is closer to that commitment than to a teaser [inferred].
- **A launch moment (partly agree).** DC-L11-08 defaults a design system to an incremental rollout and notes that this has no launch moment, so teams must create occasions to introduce it. A presale with a public deadline is one such occasion for a product [inferred].
- **The first screen after sign-up (agree).** DC-L19-129 and DC-L13-11 advise against a forced tour; the Motion Passport is not a tour but a welcome page that sets the tone, which DC-L19-129 adopts through `STD-process-review-taste-67`. DC-L19-130 lists the welcome page among the few moments that may get celebratory treatment. Moonly's first screen is personalised from onboarding answers instead [S-L19-111], a different kind of care for the same moment [inferred].
- **Launch material around the signature motion (agree).** DC-L19-170 notes that Sonner's launch was built around its signature motion [S-L19-006], which fits Emil's account of word of mouth spreading Sonner [S-L19-007].
- **Show the real product (agree).** DC-L19-131 defaults marketing visuals to the real product. Moonly's custom store pages show a screenshot set matched to the feature someone searched for [S-L19-111], the same idea tuned to each visitor [inferred].
- **Rule files for agents (agree).** Shipping a SKILL.md as an update matches DC-L19-171 and `STD-process-review-taste-55`.
- **Measuring success (partly covered).** Emil judges success by enrolments and by what people say, with no analytics [S-L19-007]. Moonly measures conversion on paid traffic (10% in 2020, 40% now), lifetime value and share rate [S-L19-111]. DC-L19-137 and DC-L19-166 propose recording what a change should move; DC-L19-179 covers store pages, featuring and share moments as design choices, but no card proposes how to measure store traffic, featuring or word of mouth.

## Decisions this informs

- **Q-gov-06** (how people hear about each change): `release-notes`, published as a changelog page (DC-L19-169) [S-L19-007].
- **Q-pattern-04** (how first-time users learn the product): the first screen after sign-up is designed to set the tone, not left to chance (DC-L19-129, which proposes splitting this into Q-pattern-07) [S-L19-007]; Moonly tailors the onboarding to the ad a person came from [S-L19-111].
- **Q-brand-04** (how lively it feels): the welcome page and the hero's hover and click details are the kind of rare moment `hero-moments` allows (DC-L19-130) [S-L19-007].
- **Q-scope-01** (what the system covers): when `marketing` is in scope, packaging (a logo used in several forms, an interactive hero) is part of the work [S-L19-007] [inferred]; for an app, so are store product pages with a screenshot set per searched feature, which no option names today [S-L19-111] [inferred]. DC-L19-179 proposes a `launch-assets` option for store pages, share images and launch posts.
- **Q-brand-03** (logo): OpenDesigner asks for a logo and never invents one; the butter cube shows the kind of brief a designer might work from, a mark drawn from the quality people associate with the work [S-L19-007] [inferred].
- **Q-dist-02** (how AI tools read the system; planned): a rule file for agents can ship to existing users as an update [S-L19-007].
- **Q-dist-04** (docs): interactive demos and a changelog page (DC-L19-169) [S-L19-007].
- **Q-gov-05** (how to measure whether it helped): name the number each change should move (DC-L19-137, DC-L19-166); for an app that acquires users through ads, Moonly's measures are conversion on paid traffic, lifetime value and share rate [S-L19-111].

## Visual examples worth showing

- The butter-cube logo melting a little more each hour as enrolment closes, drawn with animated SVG paths [S-L19-007] ([[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]]).
- Hero illustrations that animate on hover and respond to clicks [S-L19-007].
- The Motion Passport welcome page after enrolment [S-L19-007].
- A timeline contrasting the ui.land teaser (December 2021) and its launch (January 2023) with the course's presale and public deadline [S-L19-007].
- A reply thread in which other people answer whether the course is worth it, the source's example of word of mouth [S-L19-007].
- The chain from an ad to a custom App Store product page to a matching onboarding flow, beside the standard page a generic search shows [S-L19-111] ([[sources/qK7WYCMvjUw-he-spent-1m-on-a-b-tests-here-s-what-won|He Spent $1M on A/B Tests. Here's What Won.]]).
- A screenshot that opens a one-tap share flow for a personal insight [S-L19-111]. The source describes the flow but not its screens, so a sample would be a reconstruction.

## Open questions

- Is word of mouth the best marketing? Emil says so from projects that spread [S-L19-007], and Moonly shows sharing can be designed in [S-L19-111], but neither measures how long word of mouth took or reports a case where it did not work.
- Should OpenDesigner's governance advice say which wins when a public roadmap (DC-L11-22) meets the advice not to tease unfinished work? DC-L19-179 proposes a Q-gov-06 note treating a dated roadmap as a commitment rather than a tease [inferred]; the sources do not settle it.
- Does committing to a public deadline translate to a design system inside a company, for example a dated pilot, or is it only for products people pay for?
- How should a launch be measured? OpenDesigner has no question yet on what a launch should move (DC-L19-137, DC-L19-166).
- Should the `marketing` scope include store product pages and share images, and should they follow the same system as the site? DC-L19-179 proposes covering them with templates built from the same tokens once the person names a launch, a store listing or sharing; no source discusses them as design-system surfaces, so that proposal is [inferred].
- Moonly's warning about App Store featuring comes from one niche iOS app in 2026. Does it hold for other stores and categories?
