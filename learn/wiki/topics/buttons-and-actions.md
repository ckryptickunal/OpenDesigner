---
type: topic
title: Buttons and actions
created: 2026-09-24
updated: 2026-09-24
sources: []
tags: []
---

# Buttons and actions

## Overview

Swipes can replace a button (swipe to add a friend instead of a plus button) and a slider can replace a confirm button for irreversible actions.

## Source Mentions

- [[sources/14h1VnkQvIc-master-the-3-types-of-crazy-mobile-ui-swipe-interactions|Master the 3 Types of CRAZY Mobile UI Swipe Interactions]]: Swipes can replace a button (swipe to add a friend instead of a plus button) and a slider can replace a confirm button for irreversible actions.
- [[sources/66oOi9OLMCw-why-the-60-30-10-rule-is-ruining-your-ui-designs|Why the 60-30-10 Rule is RUINING Your UI Designs]]: Button importance maps to darkness, from ghost to black with white text; most multi-purpose buttons sit around 90 to 95% white; destructive actions should be red.
- [[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]]: In macOS pop-ups the primary color always marks the non-destructive action, and that consistency is what makes users trust it.
- [[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]: Buttons that do the same job must match in size, corner radius and style; gray a button out when pressed so people know it registered; in the example a button's color is dimmed while removing clutter.
- [[sources/BvbFPzLjWcU-redesigning-a-modern-skincare-ui-from-scratch-free-design-files|Redesigning A Modern Skincare UI from SCRATCH (+ free design files)]]: Hero gets a primary and a secondary call to action, plus an arrow-only button added mainly for looks.
- [[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]: Delete buttons use red rather than the brand color; hover is lighter or brighter, press darker, disabled desaturated, and a light gray button with white text reads as disabled on its own.
- [[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]: Sidebar links are ghost buttons; ghost buttons pair with a primary CTA; padding guideline is double the height for the width; every button needs default, hover, pressed and disabled states, sometimes loading.
- [[sources/Gfsd8NNuD9g-everything-you-need-to-know-about-mobile-app-uis-in-8-minutes-beginner-friendly|Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)]]: Actions are contextual: the nav bar hides in the note editor to reveal formatting and sharing, and template selection shows only a confirm button and an X; the plus button opens a menu or an input.
- [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]: Calls to action should be eye-catching and easy to find, and buttons should almost always have a small animation.
- [[sources/Lp6ey4AyDzA-8-web-design-hacks-to-actually-make-your-designs-better|8 Web Design Hacks To ACTUALLY Make Your Designs Better]]: Not all buttons need backgrounds; demote secondary buttons by removing the fill, using a border, or reducing opacity.
- [[sources/V3Omp1hm0Sg-i-redesigned-a-failing-tesla-wannabe-full-website-to-save-it|I Redesigned a Failing Tesla WANNABE Full Website To SAVE It]]: Without a CTA in the header, the CTA section matters more; the final CTA is a dealer search bar instead of a button; long specs sit behind a 'see more' button.
- [[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]: Buttons in the quick-save window show keyboard shortcut reminders; a floating action bar in the preview gives copy, find and delete; Apple's universal share button is common.
- [[sources/Yr2uIcFZDDQ-redesigning-a-finance-dashboard-ui-from-scratch-ft-dribbble|Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)]]: Replaces actions that do not fit (receive, direct deposit) with lock card, adds all-tasks, add-reminder, compare and full-screen controls, and swaps a slider for a dropdown.
- [[sources/ZsP20PN14O0-5-trendy-animations-to-steal-for-your-next-web-design|5 Trendy Animations to Steal for Your Next Web Design]]: Button hovers that change text and background color are common and look professional; a CTA that comes to the cursor is the best use of mouse effects.
- [[sources/adev-changelog-animations-dev|animations.dev]]: A 'Hold to Delete' button exercise combines a scale-down animation with a linear transition for the button color, practising clip-path.
- [[sources/eMMiLeo_UGI-the-4-levels-of-landing-page-ui-ux-design|The 4 Levels of Landing Page UI/UX Design]]: The top-nav and hero call to action should share a label when they go to the same place; level two swaps to white buttons, and level three weaves the blue back in while keeping the primary call to action, with an icon.
- [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]]: Buttons should scale down subtly (0.97) on :active so the interface feels responsive; a button toggling between two states can crossfade with 2px blur.
- [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]: Pressed buttons scale to 0.97 to feel responsive; small buttons get a 44px minimum hit area through a pseudo-element.
- [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]]: A subtle scale-down when pressing a button is cited as a purposeful animation that makes the interface feel alive and responsive.
- [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]: Pressables scale to 0.97 on press-in, commit on press-out, keep a 44x44pt / 48dp target via hitSlop, and use pressRetentionOffset.
- [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]]: Every pressable element scales to 0.97 on :active; destructive actions can use hold-to-confirm (2s linear press, 200ms release).
- [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]: Buttons respond on pointer-down with an instant scale(0.97) press state and commit on release, with ~10px hit padding.
- [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]: Buttons scale to 0.97 on press with a 160ms ease-out transform, and hold-to-delete uses a slow press and snappy release.
- [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]]: Buttons need press feedback (scale(0.97), 160ms ease-out), subtle enough for their tens-per-day frequency; destructive actions can use hold-to-confirm to prevent slips.
- [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]: Button press feedback runs 100-160ms; pressable elements with no press feedback are a finding.
- [[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]: Buttons get touch-action: manipulation, user-select: none, an :active press state, and hover styles only behind a capability media query.
- [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]: Every pressable element gets subtle scale(0.95–0.98) press feedback on :active.
- [[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]: Chips versus buttons (chips are thinner and rarely the primary color), card links versus explicit calls to action, outline buttons to rebalance hierarchy, and more actionable button labels.
- [[sources/goWOAFqJHpA-i-redesigned-spotify-wrapped-entirely-from-scratch|I Redesigned Spotify Wrapped Entirely From SCRATCH]]: Keep the share button always visible at the bottom, have it pause the video, and use one share button with three options instead of two competing buttons.
- [[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]: Instead of picking random hover and click colors at the last minute, slide the label up inside a mask on hover and shrink the button while it is pressed; horizontal or diagonal text movement is a variation.
- [[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]: A profile card with too many unaligned buttons is better fixed by lining buttons up on a manufactured edge than by hiding secondary actions in a menu; action-bar icons can be ambiguous until a tooltip appears.
- [[sources/pGYLZyBE32o-i-redesigned-google-s-ai-website-from-scratch-complete-transformation|I Redesigned Google's AI Website from SCRATCH (complete transformation)]]: A typeable search bar replaces a plain button as the hero CTA and is echoed in the final CTA; the Enterprise option becomes a tiny button on each plan.
- [[sources/sonner-toast-toast-sonner|Toast – Sonner]]: Action renders a primary button and cancel a secondary one; both close the toast on click, and event.preventDefault() keeps it open.
- [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]]: Hero buttons at 14px text and 38px tall via padding, nav button 28px with text-sm, no icon, pill shape, secondary button with a small shadow and an outer ring, and a span wrapper so ringed and plain buttons are the same height.
- See also: [[synthesis/buttons-and-actions|Buttons and actions synthesis]]
