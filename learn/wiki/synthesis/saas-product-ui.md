---
type: synthesis
title: SaaS product UI
created: 2026-09-24
updated: 2026-09-27
sources:
  - 66oOi9OLMCw
  - ADaQuZS04Rc
  - B7k5rOgmOGY
  - If7iCPDy2vk
  - PDcQJOPby1k
  - tNMAFjzapOk
tags:
  - od-area-patterns
---
# SaaS product UI

## In short

A SaaS product is a tool people work in every day, not a brochure. The sources say to design it as screens and sequences, to design every state people meet (empty, loading, success and error), and to hold a small set of decisions consistently so each new screen feels familiar. The sidebar is the product's spine, the main area shows what matters most, and overlays are picked by how big and how lasting the task is. Product UIs are mostly neutral, with several background layers and color kept for meaning. Small tells, such as emojis used as icons or the same KPI cards on every page, make a product look careless.

## House standards

- `STD-visual-details-36` (must): things that look the same behave the same and live in the same place.
- `STD-visual-details-49` (must): give feedback on every action as soon as possible: a loading state while a form submits, a success state after copying, visible status, warnings before problems, inline validation.
- `STD-visual-details-33` (must): every screen answers where am I, where can I go, what's here and how do I get out.
- `STD-visual-details-31` (should): show the common path first and put advanced options one level deeper.
- `STD-visual-details-40` (must): easy undo for slips; confirmation dialogs only for genuinely destructive, irreversible actions.
- `STD-visual-details-17` (should): darker, heavier materials separate structural regions such as sidebars.
- `STD-easing-duration-13` (must): a crisp, professional product gets fewer, subtler, faster animations.
- `STD-when-to-animate-05` (must), `STD-when-to-animate-06` (must) and `STD-when-to-animate-20` (should): no motion on actions seen 100+ times a day, never animate keyboard-initiated actions, and remove friction from everyday work tools instead of adding delight.
- `STD-visual-details-57` (must): never hand-roll standard components; build toasts with Sonner.
- `STD-visual-details-45` (should): in AI features, add previews, confirmations and disclaimers, and cut features whose risk outweighs their value.

## What the sources teach

### Think in flows and states, not pages

- UI design decorates one room; product design is the whole house. Design every state people meet (empty, loading, success, error), think in screens and sequences instead of website sections, and ask for every screen how the user got there and what they need next [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- After a create step, prompt the natural next step with an option to skip (Notion prompts for members after a new team space is created) [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- A design system is not hundreds of components but decisions you stick to: identical button spacing, type and colors across a settings panel and a create dialog, and a primary color that always means the same thing (in macOS dialogs it marks the non-destructive action) [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).
- In app menus, alignment and type differences can show what is clickable, what is not and what is a keyboard shortcut, as in Linear's menu [S-L19-084] ([[sources/tNMAFjzapOk-the-formula-behind-truly-captivating-ui-sections|The Formula Behind Truly Captivating UI Sections]]).

### The app shell

- The sidebar is the spine: profile at the top, links with a recognisable icon and a short title, grouped by relevance, rarely used links (settings, help) at the bottom, dropdowns as links grow, and a clear active state. The very top of the main area is for page actions such as "create" [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- Keep sidebar items to navigation, with no stats; replace a gradient initial-letter avatar with an account card whose links open in a popover; put billing, usage and future sections in tabs; collapse advanced form options by default [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- Choose the surface by the size and permanence of the task: a popover for simple non-blocking settings, a modal for complex work on the same page, a new page for permanent or large context, with a back button or breadcrumb [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).

### Mostly neutral, color for meaning

- The 60-30-10 rule does not fit product UI. Plan color in four layers: a neutral foundation, a functional accent, semantic colors and theming. A product needs about four background layers, one or two strokes and about three text colors before hover states. Semantic colors for success, failure and in-progress are always needed, even in a black-and-white brand like Vercel's [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- In dark mode, raised surfaces get lighter than what they sit on, and the steps between neutrals should be roughly doubled rather than mirrored from light mode [S-L19-039] ([[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]).
- Emojis used as interface icons are the most obvious tell of AI-built UI (Notion is a noted exception); use an interface icon set such as Phosphor or Lucide [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).

### Feedback and speed

- Toasts confirm changes made in a modal and surface warnings and errors that are easy to miss; lists need an empty state; selecting several items reveals bulk actions; optimistic UI updates the screen before the server confirms [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- A thoughtful empty state (Dub) has an animation, a message and a next step; a build status appears right after a deploy (Vercel); connecting an integration shows a loading state, then success or error [S-L19-044] ([[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]).

### AI products

- AI products share a set of components (the title says seven; the transcript does not number them): a prompt box (with attachment previews and context chips), generation history with search, a memory panel people can see and edit when the AI keeps memory, inline editing, visible steps (documents retrieved, sources cited), short looping loaders with streaming and shimmer skeletons, confidence indicators, and a dark "soft glass" look [S-L19-055] ([[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]]).

## Where they agree and disagree

- **States are part of the design.** [S-L19-044] and [S-L19-047] agree with the research: empty states need a message and an action (DC-L13-10), and waits need a loading ladder (DC-L13-01).
- **Toasts for errors.** [S-L19-047] uses toasts for warnings and errors. The research says toasts suit low-stakes confirmations and must never be the only channel for an error that blocks progress (DC-L13-09, DC-L08-18), and the current default of Q-form-04 is inline or banner first. The house standards fix how toasts are built (Sonner), not when to use them, so the research rule can stand [inferred].
- **The primary color is never the destructive action.** [S-L19-044]'s macOS observation matches the research: in Apple's rules a destructive button never gets the primary role (DC-L13-18).
- **Optimistic UI.** [S-L19-047] recommends it; the research lists it with a rollback when the request fails (DC-L13-01), and the house rule gives undo for slips (`STD-visual-details-40`).
- **Showing the AI's steps.** [S-L19-055] shows retrieved documents and cited sources step by step to make the AI feel like a collaborator. The research agrees about sources (place them next to the claim, show them in drill-down form) but advises against step-by-step reasoning shown as an explanation, because it is often unfaithful to what the model did (DC-L13-16). Retrieval steps and citations are fine; narrated reasoning is not [inferred].
- **Confidence labels.** [S-L19-055] and the research both suggest confidence ratings, which the research limits to high-stakes contexts (DC-L13-16).
- **Neutral budgets.** The counts of background layers, strokes and text colors come from one video [S-L19-039]; the research's status default of four statuses with icons (DC-L01-15) agrees on the semantic layer.
- **Motion.** [S-L19-044] praises Linear's subtle but meaningful status animations and [S-L19-047] calls dashboard motion tame and user focused, both matching `STD-easing-duration-13`.

## Decisions this informs

- **Q-scope-06** ("operate" screens) and **Q-layout-03** (working or data pages).
- **Q-layout-04** (navigation placement): the sidebar as the spine.
- **Q-dir-02** (density).
- **Q-color-14** (how stacked layers are shaded) and **Q-color-09** (gray temperature).
- **Q-color-15** (status colors) and **Q-color-16** (deriving dark mode: stretch the neutral steps [S-L19-039]).
- **Q-depth-01** (how cards stand out).
- **Q-pattern-01** (modal, panel or pop-up) and **Q-pattern-03** (progressive disclosure).
- **Q-state-06** (how risky actions look): the primary color stays on the safe action.
- **Q-form-04** (where "Saved" messages appear) and **Q-form-05** (undo or confirm).
- **Q-icon-01** (icon source): an interface icon set, not emojis.
- **Q-ai-01** (how AI work is labelled and corrected).
- **Q-motion-01** (motion style): productive.

## Visual examples worth showing

- Linear's clarity: hover context on issues, a guiding empty state for a new project, subtle status animation, and identical controls in settings and in the create-view dialog [S-L19-044].
- Notion's team-space flow that prompts for members with a skip option [S-L19-044].
- A vibe-coded URL shortener before and after: emojis swapped for an icon set, KPIs with micro charts, an account card with a popover, billing and usage tabs [S-L19-061].
- A link-tracking dashboard with a sidebar, a create modal followed by a confirming toast, and bulk actions on multi-select [S-L19-047].
- Vercel's near-monochrome palette that still shows build status in color, and Mercury's tinted sidebar [S-L19-039].
- A prompt box with attachment previews, a memory panel with storage, bulk delete and added facts, a research trail fading in step by step, and a confidence pill under each answer [S-L19-055].
- Linear's menu, where alignment and type separate clickable items from shortcuts [S-L19-084].

## Open questions

- None of the sources covers settings pages, permissions, roles or multi-workspace switching in depth.
- Keyboard use (command menus, shortcuts) appears only in passing here, although the house standards have firm rules on it.
- When should a product use toasts at all? The sources use them freely; the research is more cautious. See [[synthesis/feedback-empty-and-loading-states|Feedback, empty and loading states synthesis]].
- The dark "soft glass" look [S-L19-055] has not been checked against the house rules for text on translucent surfaces (`STD-visual-details-13`) and reduced transparency (`STD-accessibility-motion-11`).
