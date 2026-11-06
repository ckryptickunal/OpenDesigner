---
title: Interface details that add up
seo_title: Interface details: type, numbers, edges, targets, contrast
description: Small interface details every OpenDesigner system follows, drawn and measured: letter spacing by size, tabular digits, soft edges, tap targets and contrast.
section: Craft
order: 3
updated: 2026-11-07
---

Most of these details go unnoticed one at a time. Together they decide whether an interface feels careful. *(STD-visual-details-50)*

Each rule is an OpenDesigner house standard or one of its [accessibility floors](/docs/accessibility/), with its source. The drawings use this site's own type and colors, and their measurements are real.

## Letter spacing and line height change with size

**Never use one letter spacing for every size, and set line height inversely to size.** *(STD-visual-details-05, STD-visual-details-06)* Capitals need more room, or they look cramped. *(STD-visual-details-04)*

| Text | Letter spacing | Line height |
|---|---|---|
| Large headings | tightened, for example -0.02em | tight, for example 1.05 |
| Body text | near 0 | looser, for example 1.5 |
| Small text | slightly more | |
| Small capital labels | +0.06em in OpenDesigner's tokens; capitals are never tightened | |

Build hierarchy from weight, size and line height together, not size alone. *(STD-visual-details-07)*

**Keep lines of body text to about 65 characters.** *(STD-visual-details-01)*

{{figure:craft-ui-type}}

Source: the apple-design skill in [emilkowalski/skills](https://github.com/emilkowalski/skills), and Emil Kowalski's essay [Agents with taste](https://emilkowal.ski/ui/agents-with-taste) for capitals and line length.

## Numbers that change in place

**Use tabular digits, `font-variant-numeric: tabular-nums`, for price columns and numbers that update, like timers and counters.** Every digit has the same width, so columns line up and a changing number doesn't shift. *(STD-visual-details-02)* When a number animates, use the NumberFlow library instead of re-rendering the text. *(STD-visual-details-59)*

{{figure:craft-ui-numbers}}

Source: Emil Kowalski's [Agents with taste](https://emilkowal.ski/ui/agents-with-taste) and the animation-vocabulary and pick-ui-library skills in emilkowalski/skills.

## Small habits in text

**Write the ellipsis as one character (…), never three periods.** *(STD-visual-details-03)* **Underline only links,** so an underline always means "you can click this". *(STD-visual-details-09)* **Emphasize interface text with weight, not italics.** *(STD-visual-details-08)*

{{figure:craft-ui-text}}

Source: Emil Kowalski's [Agents with taste](https://emilkowal.ski/ui/agents-with-taste).

## Soft edges, not hard lines

**Separate surfaces with a semi-transparent shadow rather than a solid, opaque border.** *(STD-visual-details-14)*

{{figure:craft-ui-edges}}

**Under a sticky header, fade the edge instead of drawing a permanent line,** and only where content passes under it. *(STD-visual-details-15)*

{{figure:craft-ui-scroll-edge}}

**Never place one light, see-through surface on another:** text on stacked translucent layers is hard to read. *(STD-visual-details-18)*

Source: the README and the apple-design skill in emilkowalski/skills.

## Targets and focus, measured

| Target | At least | Source |
|---|---|---|
| Touch, iOS | 44 × 44 pt | STD-mobile-touch-09 |
| Touch, Android | 48 dp | STD-mobile-touch-09 |
| Touch, web | 44 px | STD-mobile-touch-09 |
| Any web target, mouse or finger | 24 × 24 CSS px | Accessibility floor, WCAG 2.2 [2.5.8 Target Size (Minimum)](https://www.w3.org/TR/WCAG22/#target-size-minimum) |

**When the drawn control is smaller, grow its hit area,** with a pseudo-element on the web or hitSlop in React Native, never the drawing. *(STD-mobile-touch-09)*

**Every focusable element shows a focus ring,** 2 px wide, 2 px from the element, with at least 3:1 contrast against its surroundings: a floor from [2.4.7 Focus Visible](https://www.w3.org/TR/WCAG22/#focus-visible) and [1.4.11 Non-text Contrast](https://www.w3.org/TR/WCAG22/#non-text-contrast).

**Set the text in inputs to 16 px or more,** or iOS Safari zooms the page on focus and doesn't zoom back. Never turn off pinch zoom to stop it. *(STD-mobile-touch-11, STD-accessibility-motion-27)*

{{figure:craft-ui-targets}}

Source: the mobile-native, animate-expo and apple-design skills in emilkowalski/skills, and Emil Kowalski's [Agents with taste](https://emilkowal.ski/ui/agents-with-taste).

## Color: contrast and meaning

**Text on a fill needs at least 4.5:1 contrast, or 3:1 when it is large.** OpenDesigner uses the WCAG 2 formula and never rounds up, so 4.49:1 fails. An accessibility floor, from [1.4.3 Contrast (Minimum)](https://www.w3.org/TR/WCAG22/#contrast-minimum).

**Put color on solid layers, not see-through ones.** Over a translucent surface, use higher-contrast text, a slightly heavier weight and a little more letter spacing. *(STD-visual-details-21, STD-visual-details-13)*

{{figure:craft-ui-contrast}}

**Never pair pure white with pure black.** Use an off-black such as #111111 with white, or an off-white with black. *(STD-visual-details-66)*

**Keep the colors people already know:** green for success, red for errors, amber for pending, blue for information. *(STD-visual-details-65)*

Source: the apple-design skill in emilkowalski/skills, for translucent surfaces. The last two are OpenDesigner's own house rules.

## Build from the tokens

**Build from the project's existing [tokens](/docs/design-tokens/), the named values of the system, and extend them when something is missing.** Never hand-type or approximate a value, and never start a second, parallel set. *(STD-visual-details-26)*

**Make every spacing, timing and alignment value a choice you can defend.** *(STD-visual-details-27)* Jittery scrolling, misaligned icons or layouts that break on rotation read as carelessness. *(STD-visual-details-28)*

Source: the prototype, animate and review skills in emilkowalski/skills, and the apple-design skill.

## Where these rules come from

The [standards file](https://github.com/ckryptickunal/OpenDesigner/blob/main/skills/opendesigner/references/standards.md) lists each standard with its sources, and [Who OpenDesigner learns from](/docs/resources/) describes every source. OpenDesigner is not affiliated with or endorsed by the people it cites.
