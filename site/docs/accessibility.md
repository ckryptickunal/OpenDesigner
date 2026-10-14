---
title: Accessibility floors
seo_title: Accessibility floors in OpenDesigner: WCAG 2.2 AA checks
description: The accessibility minimums every OpenDesigner system gets: WCAG 2.2 AA contrast, target sizes, focus rings and reduced motion, what is checked, and what is not.
section: Concepts
order: 5
updated: 2026-10-14
---

Every design system OpenDesigner makes gets a set of accessibility minimums, called floors. They are WCAG 2.2 AA text contrast, 3:1 contrast for borders and focus rings, minimum target sizes, a visible focus ring and a reduced-motion mode. Fixed rules check them before the AI gives any opinion, and an error blocks the build.

## The floors

### Text contrast

- **Body text:** at least 4.5:1 against its background. This is WCAG 2.2 success criterion [1.4.3 Contrast (Minimum)](https://www.w3.org/TR/WCAG22/#contrast-minimum).
- **Large text:** at least 3:1. WCAG defines large text as at least 18 point, or 14 point bold.

The engine measures with the WCAG 2 formula and never rounds up, so 4.49:1 fails. It checks the text and background pairs the system defines, in every mode. In a test run, it checked 164 color pairs in every mode, across 12 mode combinations: light and dark, three densities, and standard and reduced motion.

{{figure:accessibility-contrast}}

### Borders, focus rings and icons

Borders, focus rings and other parts that are not text need at least 3:1 contrast. See [1.4.11 Non-text Contrast](https://www.w3.org/TR/WCAG22/#non-text-contrast).

### Target sizes

Anything people tap or click must be big enough:

- **Web:** at least 24 by 24 CSS pixels, from [2.5.8 Target Size (Minimum)](https://www.w3.org/TR/WCAG22/#target-size-minimum).
- **iOS:** at least 44 points, from Apple's platform guidance.
- **Android:** at least 48 dp, from Android's platform guidance.

A compact density never shrinks these. When a control is drawn smaller than the target, the engine notes that it needs padding to keep the tap area full size.

{{figure:accessibility-targets}}

### A visible focus ring

Every system gets a focus ring, so keyboard users can see where they are: a 2 px ring with a 2 px gap around the element. It never relies on color alone. See [2.4.7 Focus Visible](https://www.w3.org/TR/WCAG22/#focus-visible).

{{figure:accessibility-focus}}

### Reduced motion, and glass surfaces

Reduced motion is a mode in the tokens. It follows the device setting, and the CSS export also lets you switch it with a `data-motion` attribute. OpenDesigner treats [2.3.3 Animation from Interactions](https://www.w3.org/TR/WCAG22/#animation-from-interactions) as required, even though WCAG lists it at level AAA. If your system uses see-through glass surfaces, each one gets a solid version for people who turn transparency off. The CSS export swaps it in, with no blur, when the browser reports that the person wants less transparency (`prefers-reduced-transparency`: Chrome and Edge today; Safari does not report it and Firefox only behind a setting) or more contrast (`prefers-contrast: more`, in every major browser). A glass surface without one is an error.

### Text that can grow

Text must scale to 200%, and containers must grow with it. The CSS export sets font sizes in rem, so browser text zoom works. See [1.4.4 Resize Text](https://www.w3.org/TR/WCAG22/#resize-text). The Swift export uses Dynamic Type text styles, so text follows the person's size setting.

## Errors and warnings

The checks give the same result every time.

- **Errors** break an accessibility rule and block the build. Examples: targets under 24 px, fields with no label, meaning shown by color alone (see [1.4.1 Use of Color](https://www.w3.org/TR/WCAG22/#use-of-color)), and dialogs with no way out. You can waive one only with a written reason.
- **Warnings** come from practitioner advice and are labelled as guidance. Examples: too many type sizes in one view, or very bright colors in a very dense layout. You can override a warning with a reason.
- **Notes** are advice only. For example, the engine reports an APCA reading-contrast score next to the WCAG ratio. WCAG 3 is still a draft, so WCAG 2.2 is the target it enforces.

## Your brand color and contrast

If your brand color passes contrast on the main buttons, the engine keeps it exact. If it doesn't, the engine changes it just enough to pass and tells you in one line. You can see the result, with its contrast ratio, on the overview page.

## The floors stay locked

The floors are set in the sketch and never skipped. They are locked unless you raise them. For example, you can set a stricter contrast target of AAA. When rules clash, the floors come first, ahead of your own explicit choices and any standard.

The note OpenDesigner offers to add to your `AGENTS.md` tells coding agents that the floors are part of the system.

## What the checks don't cover

The floors are a minimum. Passing them does not prove your app meets all of WCAG.

- Automated checks catch only part of WCAG. Many success criteria need a person to judge them, such as whether link text makes sense or whether the reading order is right.
- The engine checks the design system's values. It can't see how your screens use them. A button can still be built without a label.
- People who use screen readers and other assistive technology should test your app. At deeper zoom levels, the interview asks which screen readers, control tools and text sizes you will test on each kind of device.

## Sources

- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- [WCAG overview from the W3C Web Accessibility Initiative](https://www.w3.org/WAI/standards-guidelines/wcag/)
