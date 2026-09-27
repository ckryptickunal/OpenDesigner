---
type: topic
title: Feedback, empty and loading states
created: 2026-09-24
updated: 2026-09-28
sources: []
tags: []
---

# Feedback, empty and loading states

## Overview

Real apps need empty, loading, success and error states; examples from Dub (empty state with animation, message and next step), Vercel (build status notification) and a Notion integration with loading then success or error.

## Source Mentions

- [[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]: Real apps need empty, loading, success and error states; examples from Dub (empty state with animation, message and next step), Vercel (build status notification) and a Notion integration with loading then success or error.
- [[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]: A short delay with no feedback looks like the tap failed; gray the button out on press and add a loading wheel for long waits.
- [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]: Think about the empty state for a list with no data to display; use toasts for confirmation, warning and error feedback.
- [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]: Every interaction needs a response: loading spinners while data fetches, success messages when an action completes, micro animations on scroll or swipe.
- [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]: Two empty states: first use, which highlights the main plus action with a full-screen state and an instructional popover; and no search results, which needs imagery, an acknowledgement, suggestions and an exit action.
- [[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]]: Short looping loaders, streaming output word by word, skeleton placeholders with shimmer, step-by-step research trails and confidence labels all give feedback during waits.
- [[sources/NtZeYmTMuo4-animated-dashboard-sidebar-tutorial-in-figma-free-design-files|Animated Dashboard Sidebar Tutorial in Figma (+ free design files)]]: Shows a focus state, a loading dialogue with a spinning icon and a success state with a check mark.
- [[sources/SfX43uIubj4-4-ui-design-hacks-to-kill-boring-designs|4 UI Design Hacks to KILL boring designs]]: 404 pages are the ultimate place to be quirky: a quiz, a movie character, a mini game that redirects, or personal text with smooth animation.
- [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]: A simple empty state invites the first action; optimistic UI shows a save as done straight away; every shortcut needs a visible state change.
- [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]: Preloaders add a premium feel and cover loading of heavy media, but must stay short so people are not kept waiting.
- [[sources/d4MF6pdAZNw-developing-premium-load-animations-html-css-js-part-2|Developing Premium Load animations (HTML, CSS & JS): Part 2]]: A branded loading screen: a black full-screen overlay where the logo and wordmark fade in, then the screen slides up to reveal the page.
- [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]: Submitting a form should show a loading state and copy-to-clipboard should show a success state; a faster-spinning spinner makes loading feel faster.
- [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]: The promise API shows one toast that moves through loading, success and error states from a single call.
- [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]: A faster-spinning spinner makes the app seem to load faster at the same load time.
- [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]: Skeleton or shimmer placeholders with a moving sheen while content loads; shake signals rejected input.
- [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]: Feedback comes in four kinds (status, completion, warning, error); confirm meaningful actions, expose ongoing status, warn before problems; sound and haptics only for meaningful moments.
- [[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]: toast.loading shows a spinner and is updated by id; toast.promise moves from loading to success or error when the promise settles.
- [[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]: Loading toasts updated by id, toast.promise for loading to success or error, and promises that never settle leaving a toast stuck.
- [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]: Faster-spinning spinners make loading feel faster; transitions prevent jarring appear/disappear changes.
- [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]: Empty states and success or completion moments are rare, high-emotion places where the delight budget may be spent.
- [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]: Faster spinners make loading feel faster for the same actual time.
- [[sources/ixUq4HM4FNg-tiktoks-ux-is-so-good-it-should-be-illegal-seriously|TikTok’s UX is so GOOD it should be ILLEGAL (seriously)]]: Defines user feedback as an immediate response to any action, and extends it to social feedback (likes, comments, shares) for creators.
- [[sources/nl8OFGdx75w-prototyping-professional-load-animations-in-figma-part-1|Prototyping Professional Load Animations in Figma: Part 1]]: A loading screen with a centred logo slides up to reveal the page, with the content underneath rising with it and the nav fading in afterwards.
- [[sources/sonner-toast-toast-sonner|Toast – Sonner]]: Promise toasts show loading and then success or error automatically; loading toasts show a spinner when you manage the states yourself.
- [[sources/Qsq-Sj_rojU-i-studied-1-460-onboarding-flows-here-s-what-i-found|I Studied 1,460 Onboarding Flows. Here's What I Found.]]: Replace blank empty states with a small nudge, and give loading and verification states smooth animation so long flows stay engaging.
- [[sources/kdRkuqu8apE-i-studied-2-108-dashboards-to-see-what-sticks|I Studied 2,108 Dashboards To See What Sticks]]: Mercury shows a game instead of an empty table after all bills are paid, as an example of a non-template empty state.
- See also: [[synthesis/feedback-empty-and-loading-states|Feedback, empty and loading states synthesis]]
