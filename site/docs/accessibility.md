---
title: Accessibility floors
seo_title: Accessibility floors in OpenDesigner: WCAG 2.2 AA checks
description: The accessibility minimums every OpenDesigner system gets: WCAG 2.2 AA contrast, target sizes, focus rings and reduced motion, what is checked, and what is not.
section: Concepts
order: 5
updated: 2026-11-08
---

Every system OpenDesigner makes gets accessibility minimums, called floors. Text has enough contrast to read, controls are big enough to tap, keyboard users can see where they are, and motion calms down for people who ask for less. Fixed rules check them before the AI gives any opinion, and an error blocks the build.

## The floors

### Text contrast

- **Body text:** at least 4.5:1 against its background, from WCAG 2.2 [1.4.3 Contrast (Minimum)](https://www.w3.org/TR/WCAG22/#contrast-minimum).
- **Large text:** at least 3:1. Large means at least 18 point, or 14 point bold.

Every text and background pair in the system is checked, in every mode, and nothing is rounded up.

{{figure:accessibility-contrast}}

:::dev
The engine measures with the WCAG 2 formula, and 4.49:1 fails. In a test run, it checked 164 color pairs in every mode, across 12 mode combinations: light and dark, three densities, and standard and reduced motion.
:::

### Borders, focus rings and icons

Borders, focus rings and other parts that are not text need at least 3:1 contrast. See [1.4.11 Non-text Contrast](https://www.w3.org/TR/WCAG22/#non-text-contrast).

### Target sizes

Anything people tap or click must be big enough:

- **Web:** at least 24 by 24 CSS pixels, from [2.5.8 Target Size (Minimum)](https://www.w3.org/TR/WCAG22/#target-size-minimum).
- **iOS:** at least 44 points, from Apple's guidance.
- **Android:** at least 48 dp, from Android's guidance.

A compact density never shrinks these. When a control is drawn smaller, the engine notes that it needs padding to keep the tap area full size.

{{figure:accessibility-targets}}

### A visible focus ring

Every system gets one: a 2 px ring with a 2 px gap around the element. It never relies on color alone. See [2.4.7 Focus Visible](https://www.w3.org/TR/WCAG22/#focus-visible).

{{figure:accessibility-focus}}

### Reduced motion, and glass surfaces

Reduced motion is a mode that follows the device setting. OpenDesigner treats [2.3.3 Animation from Interactions](https://www.w3.org/TR/WCAG22/#animation-from-interactions) as required, even though WCAG lists it at level AAA.

If your system uses see-through glass, each glass surface gets a solid version for people who turn transparency off or ask for more contrast. A glass surface without one is an error.

:::dev
The CSS export also lets you switch reduced motion with a `data-motion` attribute. It swaps in the solid version, with no blur, when the browser reports `prefers-reduced-transparency` (Chrome and Edge today; Safari does not report it and Firefox only behind a setting) or `prefers-contrast: more` (every major browser).
:::

### Text that can grow

Text must scale to 200%, and containers must grow with it. See [1.4.4 Resize Text](https://www.w3.org/TR/WCAG22/#resize-text).

:::dev
The CSS export sets font sizes in rem, so browser text zoom works. The Swift export uses Dynamic Type text styles, so text follows the person's size setting.
:::

## Errors and warnings

The checks give the same result every time.

| Level | Comes from | Examples | Can you skip it? |
|---|---|---|---|
| **Error** | An accessibility rule | Targets under 24 px, fields with no label, meaning shown by color alone ([1.4.1 Use of Color](https://www.w3.org/TR/WCAG22/#use-of-color)), dialogs with no way out | Only with a written reason |
| **Warning** | Practitioner advice, labelled as guidance | Too many type sizes in one view, very bright colors in a very dense layout | Yes, with a reason |
| **Note** | Advice only | An APCA reading-contrast score next to the WCAG ratio | Nothing to skip |

WCAG 3 is still a draft, so WCAG 2.2 is the target the engine enforces.

## Your brand color and contrast

The brand color you typed stays exact. Main buttons get white or dark text on it, whichever reads. If neither reads, buttons with text use a nearby readable shade, and your exact color stays for the logo and large areas. You're told which in one line, and the overview page shows the result with its contrast ratio.

## The floors stay locked

The floors are set in the sketch and never skipped. They are locked unless you raise them, for example to a stricter AAA contrast target. When rules clash, the floors come first, ahead of your own explicit choices and any standard.

The note OpenDesigner offers to add to `AGENTS.md` tells coding agents the floors are part of the system.

## What the checks don't cover

The floors are a minimum. Passing them does not prove your app meets all of WCAG.

- Automated checks catch only part of WCAG. Many success criteria need a person to judge them, such as whether link text makes sense or the reading order is right.
- The engine checks the design system's values, not how your screens use them. A button can still be built without a label.
- People who use screen readers and other assistive technology should test your app. At deeper zoom levels, the interview asks which screen readers, control tools and text sizes you will test on each kind of device.

## Sources

- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- [WCAG overview from the W3C Web Accessibility Initiative](https://www.w3.org/WAI/standards-guidelines/wcag/)
