---
type: topic
title: Modals and popovers
created: 2026-09-24
updated: 2026-09-24
sources: []
tags: []
---

# Modals and popovers

## Overview

Swipe gestures are a quick, often intuitive way to dismiss popovers and pages, which is why Apple uses them widely.

## Source Mentions

- [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]: Swipe gestures are a quick, often intuitive way to dismiss popovers and pages, which is why Apple uses them widely.
- [[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]: A new 'create listing' modal is quick to build from existing parts (template selectors, title, description and tag fields, actions at the bottom) and feels familiar next to the other modals.
- [[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]: Popovers suit simple, non-blocking context such as display settings; modals suit more complex, blocking context that should stay on the same page, such as creating a link; very large or permanent context gets a new page.
- [[sources/BUDipdbKK7Y-i-made-the-most-unhinged-ui-upgrades-downgrades|I Made The Most UNHINGED UI Upgrades (downgrades?)]]: A forced layer-naming modal that blocks all other actions is used as an example of an infuriating pattern; a notice explaining how to turn it off is added as the one piece of good UX.
- [[sources/Ksx9C2-3yMo-the-3-dashboard-ui-flaws-that-give-away-you-ve-never-built-one|The 3 dashboard UI flaws that give away you've NEVER built one]]: Put infrequent features like sharing into a popover rather than a permanent panel or a new page; put the popover's primary action (a search box) at the top and reveal secondary actions on hover.
- [[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]: In a delete modal, the delete button gets the primary fill (preferably red) and cancel gets no background, a border or reduced opacity.
- [[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]: A sparse create-link flyout becomes a modal; account links are tucked into a popover opened on click.
- [[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]: An add-on's details open in a lightbox card with a full-size photo, a text overlay, a gradient for legibility and a close X.
- [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]: Popovers and new windows are part of feeling native; onboarding is a modal, and a settings popover holds the shortcut cheat sheet, panel side and light/dark setting.
- [[sources/adev-home-animations-dev|animations.dev]]: Module 3 builds a Feedback popover across 3 exercises.
- [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]: Popovers and dropdowns should scale in from their trigger using transform-origin; tooltips need an initial delay, then open instantly and without animation for neighbouring triggers.
- [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]: Popovers should scale from the trigger by setting transform-origin; modals and drawers animate in 200-300ms; he used his skill to have Claude Code improve a dialog animation.
- [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]: The author prefers a drawer to a modal on mobile, and builds the drawer on Radix's Dialog primitive.
- [[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]]: Exercises compare dialog entrance animations and popover animations triggered by a button.
- [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]: Tooltips get a slight initial delay to prevent accidental activation, then open with no delay and no animation while another is open; a 180ms dropdown feels more responsive than a 400ms one.
- [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]: Popover/dropdown/menu/select at 200ms from scale(0.95) out of the trigger; tooltip at 125ms from scale(0.97) with instant neighbours; modal centered at 250ms from scale(0.96) with a matching backdrop fade.
- [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]]: Popovers, dropdowns, menus and tooltips scale from their trigger via transform-origin; modals are exempt and stay centered; per-type durations.
- [[sources/eks-skills-animation-vocabulary-skill-emilkowalski-skills-skills-animation-vocabulary-skill-md|emilkowalski/skills: skills/animation-vocabulary/SKILL.md]]: Origin-aware animation: a popover grows from the button that opened it instead of from its own center, which is the default in CSS; this is the skill's first worked example.
- [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]: Popovers and menus originate from their trigger via transform-origin; modal tasks pair the surface with a dimming scrim while non-blocking panels use translucency without a scrim; confirmation dialogs are only for destructive, irreversible actions.
- [[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]]: Toasts behind modals or overlays are caused by stacking contexts or z-index; mount the Toaster outside dialog and portal containers.
- [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]: Popovers and tooltips scale from their trigger via var(--transform-origin); modals stay centered; tooltip delay then instant subsequent tooltips.
- [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]: Panels, popovers and menus scale in from a transform-origin at their trigger (Base UI var(--transform-origin)); modals are exempt and stay centered; tooltips and small popovers take 125-200ms.
- [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]: Popovers, dropdowns and tooltips scale from their trigger via transform-origin; modals are exempt and stay centered; tooltip durations 125-200ms and only the first tooltip in a toolbar gets delay plus animation.
- [[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]]: transform-origin: center on a modal is correct and must be rejected as a finding; wrong origin elsewhere is MEDIUM.
- [[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]: base-ui is the pick for dialogs, popovers, menus and selects, replacing div-based versions with manual focus handling because it handles accessibility, focus trapping and dismissal.
- [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]]: Popovers, dropdowns and tooltips scale from their trigger; modals are exempt and stay centered.
- [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]: Popovers scale from the trigger via var(--transform-origin); modals stay centered; tooltips and small popovers run 125–200ms and later tooltips can be instant.
- [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]: Delayed tooltips pop up to explain what an icon does, only after the pointer rests on it for a full second, and hide on mouse leave.
- [[sources/vaul-other-other-vaul|Other – Vaul]]: modal false keeps the background interactive; dismissible false removes outside-click, Escape and drag-down dismissal.
- [[sources/vaul-snap-points-snap-points-vaul|Snap Points – Vaul]]: modal false with snap points keeps the background interactive while the drawer is open.
- See also: [[synthesis/modals-and-popovers|Modals and popovers synthesis]]
