---
title: Interface details that add up
seo_title: Interface details: type, numbers, edges, targets, contrast
description: Small interface details every OpenDesigner system follows, drawn and measured: letter spacing by size, tabular digits, soft edges, tap targets and contrast.
section: Craft
order: 3
updated: 2026-10-15
---

Most of these details go unnoticed one at a time. Together they decide whether an interface feels careful. When something works exactly as people expect, they carry on without a second thought, and in the aggregate the small details become visible. *(STD-visual-details-50)*

Each rule below is an OpenDesigner house standard or one of its [accessibility floors](/docs/accessibility/), with its source named. The drawings use this site's own type and colors, and the measurements in them are real.

## Letter spacing and line height change with size

**Never use one letter spacing for every size.** Tighten large headings, for example to -0.02em. Give small text slightly more space, and leave body text near 0. Letters look further apart as text grows. *(STD-visual-details-05)*

**Give capitals more room.** Uppercase labels need looser letter spacing than the same words in sentence case, or they look cramped. *(STD-visual-details-04)*

**Set line height inversely to size.** Keep it tight on large headings, for example 1.05, and looser on body text, for example 1.5. *(STD-visual-details-06)* Build hierarchy from weight, size and line height together, not from size alone. *(STD-visual-details-07)*

**Keep lines of body text to about 65 characters,** so they stay comfortable to read. *(STD-visual-details-01)*

{{figure:craft-ui-type}}

Source: the apple-design skill in [emilkowalski/skills](https://github.com/emilkowalski/skills), and Emil Kowalski's essay [Agents with taste](https://emilkowal.ski/ui/agents-with-taste) for capitals and line length.

## Numbers that change in place

**Use tabular digits for price columns and for numbers that update, like timers and counters.** Tabular digits all have the same width. In CSS that is `font-variant-numeric: tabular-nums`. Columns then line up, and a changing number does not shift as it updates. *(STD-visual-details-02)*

{{figure:craft-ui-numbers}}

When a number animates, such as a counter or a price, use the NumberFlow library instead of re-rendering the text. *(STD-visual-details-59)*

Source: Emil Kowalski's [Agents with taste](https://emilkowal.ski/ui/agents-with-taste) and the animation-vocabulary and pick-ui-library skills in emilkowalski/skills.

## Small habits in text

**Write the ellipsis as one character (…), never as three periods.** *(STD-visual-details-03)*

**Underline only links.** Emphasize other text with weight or color. Then an underline always means "you can click this". *(STD-visual-details-09)*

**Emphasize interface text with weight, not italics.** Italics belong to citations and stress in long prose; in an interface they read like print. *(STD-visual-details-08)*

{{figure:craft-ui-text}}

Source: Emil Kowalski's [Agents with taste](https://emilkowal.ski/ui/agents-with-taste).

## Soft edges, not hard lines

**Separate surfaces with a semi-transparent shadow rather than a solid, opaque border.** A solid border where a shadow belongs is one of the small mistakes that add up to an interface that is not great. *(STD-visual-details-14)*

{{figure:craft-ui-edges}}

**Under a sticky header, fade the edge instead of drawing a permanent line.** Show a short blur or gradient only where content actually passes under the header. *(STD-visual-details-15)*

{{figure:craft-ui-scroll-edge}}

**Never place one light, see-through surface on another.** Text on stacked translucent layers becomes hard to read. *(STD-visual-details-18)*

Source: the README and the apple-design skill in emilkowalski/skills.

## Targets and focus, measured

**Make every touch target at least 44 by 44 points on iOS, 48 dp on Android and 44 px on the touch web.** When the drawn control is smaller, grow its hit area with a pseudo-element on the web, or hitSlop in React Native, never by growing the drawing. *(STD-mobile-touch-09)*

**No web target, for a mouse or a finger, is smaller than 24 by 24 CSS pixels.** This is an accessibility floor, from WCAG 2.2 [2.5.8 Target Size (Minimum)](https://www.w3.org/TR/WCAG22/#target-size-minimum).

**Every focusable element shows a focus ring:** 2 px wide, 2 px from the element, with at least 3:1 contrast against what is around it. This is also a floor, from [2.4.7 Focus Visible](https://www.w3.org/TR/WCAG22/#focus-visible) and [1.4.11 Non-text Contrast](https://www.w3.org/TR/WCAG22/#non-text-contrast).

**Set the text in inputs to 16 px or more.** Below that, iOS Safari zooms the page when the field gets focus and does not zoom back out. Never turn off pinch zoom to stop it. *(STD-mobile-touch-11, STD-accessibility-motion-27)*

{{figure:craft-ui-targets}}

Source: the mobile-native, animate-expo and apple-design skills in emilkowalski/skills, and Emil Kowalski's [Agents with taste](https://emilkowal.ski/ui/agents-with-taste).

## Text on colored fills

**Text on a fill needs at least 4.5:1 contrast, or 3:1 when it is large.** OpenDesigner measures with the WCAG 2 formula and never rounds up, so 4.49:1 fails. This is an accessibility floor, from [1.4.3 Contrast (Minimum)](https://www.w3.org/TR/WCAG22/#contrast-minimum).

**Put color on solid layers, not on see-through ones.** Over a translucent surface, use higher-contrast text, a slightly heavier weight and a little more letter spacing. *(STD-visual-details-21, STD-visual-details-13)*

{{figure:craft-ui-contrast}}

Source: the apple-design skill in emilkowalski/skills, for the rules on translucent surfaces.

## Build from the tokens

Tokens are the named values of a design system, such as a color or a spacing step. See [Design tokens](/docs/design-tokens/).

**Build from the project's existing tokens, and extend them when something is missing.** Never hand-type or approximate a value, and never start a second, parallel set. *(STD-visual-details-26)*

**Make every spacing, timing and alignment value a choice you can defend.** *(STD-visual-details-27)* Do not ship jittery scrolling, misaligned icons or layouts that break when the device rotates; they read as carelessness. *(STD-visual-details-28)*

Source: the prototype, animate and review skills in emilkowalski/skills, and the apple-design skill.

## Where these rules come from

The house standards and their sources are listed in the [standards file](https://github.com/ckryptickunal/OpenDesigner/blob/main/skills/opendesigner/references/standards.md), and the floors on the [Accessibility floors](/docs/accessibility/) page. [Who OpenDesigner learns from](/docs/resources/) describes every source. OpenDesigner is not affiliated with or endorsed by the people it cites.
