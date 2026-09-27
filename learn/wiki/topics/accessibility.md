---
type: topic
title: Accessibility
created: 2026-09-24
updated: 2026-09-24
sources: []
tags: []
---

# Accessibility

## Overview

Colored cards and brand colors with white text often fail WCAG contrast checks; lighten backgrounds with black text, darken the brand color, or pick a complementary color that passes.

## Source Mentions

- [[sources/EOcY3hPMQkk-the-7-color-mistakes-that-ruin-your-ui-designs|The 7 Color Mistakes that RUIN your UI Designs]]: Colored cards and brand colors with white text often fail WCAG contrast checks; lighten backgrounds with black text, darken the brand color, or pick a complementary color that passes.
- [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]: Add a circle behind a save icon placed on bright listing images to guarantee contrast.
- [[sources/adev-changelog-animations-dev|animations.dev]]: The course site itself moved to more distinct, yellow focus states and added English captions to all videos.
- [[sources/adev-home-animations-dev|animations.dev]]: Accessibility is one of the Module 4 topics for taking animations from good to great; animation-accessibility is one of the AI skills.
- [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]]: Small buttons need a 44px minimum hit area; underlines are reserved for links so they stay a reliable affordance.
- [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]: Building on Radix's Dialog primitive gives the drawer accessibility and focus management.
- [[sources/ek-the-magic-of-clip-path-the-magic-of-clip-path|The Magic of Clip Path]]: The duplicated tab overlay is marked aria-hidden with tabIndex -1 buttons, and a real implementation should use an accessible primitive such as Radix Tabs.
- [[sources/eks-skills-animate-expo-skill-emilkowalski-skills-skills-animate-expo-skill-md|emilkowalski/skills: skills/animate-expo/SKILL.md]]: Reduced motion support, minimum touch targets, haptics never the only feedback, and no hardcoded heights, because a height measured at default type size is wrong at 200% text size.
- [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]: Components respond to prefers-reduced-motion, prefers-reduced-transparency and prefers-contrast: more, respect the user's text size with rem/em spacing, and keep text legible over translucent surfaces.
- [[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]]: Alt+T hotkey focuses the toaster area; the container ARIA label defaults to 'Notifications'; dir supports text direction; dismissible controls whether the user can close a toast.
- [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]]: Motion sickness risk and reduced motion, plus gating hover animations behind (hover: hover) and (pointer: fine) for touch devices.
- [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]]: Motion without prefers-reduced-motion handling and ungated :hover motion (touch fires false hovers) are findings.
- [[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]: Never disable zoom with user-scalable=no or maximum-scale=1; keep content text selectable; keep press feedback for touch users after removing the tap highlight.
- [[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]: base-ui is the pick because it handles accessibility, focus trapping and dismissal; a div-based dropdown or dialog with manual focus handling is a mismatch to catch.
- [[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]: The picker is a nav with aria-label, decorative spans are aria-hidden, the icon replay button has an aria-label, exactly one item carries aria-current="true", focus-visible shows a 2px outline with 2px offset, and key handling ignores form fields, contenteditable and modifier keys.
- [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]]: Reduced-motion handling and hover gating behind (hover: hover) and (pointer: fine) are review criteria and an approval condition.
- [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]]: Reduced-motion media query and hover gating behind (hover: hover) and (pointer: fine) because touch fires false hovers.
- [[sources/sonner-toast-toast-sonner|Toast – Sonner]]: The toast container has an aria label, containerAriaLabel, which defaults to 'Notifications'.
- [[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]]: The API lists a keyboard hotkey (default ⌥/alt + T) and a dir setting (default ltr).
- [[sources/vaul-api-api-reference-vaul|API Reference – Vaul]]: Title and Description are optional accessible text announced when the drawer opens; the overlay covers the inert portion of the view while the drawer is open.
- [[sources/vaul-other-other-vaul|Other – Vaul]]: A non-dismissible drawer ignores the Escape key, outside clicks and drag-down, and its demo can only be closed by refreshing; the page does not frame this as accessibility [inferred].
- [[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]]: Contrast on the generated chips needed fixing during the Figma pass.
- See also: [[synthesis/accessibility|Accessibility synthesis]]
