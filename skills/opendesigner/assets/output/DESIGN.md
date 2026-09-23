---
# DESIGN.md front matter (Google's open DESIGN.md format; DTCG tokens in opendesigner/tokens/ are canonical)
name: {{name}}
generated-by: OpenDesigner {{version}}
colors:
  primary: "{{accent.9}}"
  on-primary: "{{on-accent}}"
  background: "{{neutral.1}}"
  surface: "{{neutral.2}}"
  text: "{{neutral.12}}"
  text-muted: "{{neutral.11}}"
  border: "{{neutral.6}}"
typography:
  body: { fontFamily: "{{textFace}}", fontSize: "{{baseSize}}px", lineHeight: "{{bodyLineHeight}}px" }
  heading: { fontFamily: "{{displayFace}}", fontWeight: {{headingWeight}} }
rounded:
  control: "{{radius.control}}px"
  container: "{{radius.container}}px"
spacing:
  unit: "{{spaceUnit}}px"
  scale: [{{space.steps}}]
components:
  button-primary: { background: "{colors.primary}", color: "{colors.on-primary}", rounded: "{rounded.control}" }
---

# {{name}} design system

## Overview
{{One paragraph: product, audience, the memorable thing, the chosen direction and its safe choices and risks.}}

## Colors
{{Accent and neutral ramps, roles, where the brand color appears (Q-color-02), contrast target, dark mode.}}

## Typography
{{Faces and their licences, base size, ratio, the scale table, line heights, numerals.}}

## Layout
{{Spacing unit and scale, density, breakpoints, containers, target sizes.}}

## Elevation & Depth
{{The depth model and each level; how dark mode raises surfaces.}}

## Shapes
{{Radius per role; nested radius rule; people stay round.}}

## Motion
{{Duration ladder, easing, exits shorter than entrances, reduced-motion behavior.}}

## Components
{{Base library, inventory, state rules (hover, focus, disabled, loading, error).}}

## Do's and Don'ts
- Do use tokens by name; don't hard-code values.
- {{Rules from the decisions, for example: one primary action per view.}}

## Assets
{{Each designer hook with its status (have, commissioning, placeholder) and owner.}}

## Decisions
{{The highest-impact decisions with their D-numbers; full log in decisions.md.}}
