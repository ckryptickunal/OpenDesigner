---
type: source
title: "Inputs – Vaul"
created: 2026-09-27
updated: 2026-09-27
video_id: vaul-inputs
url: https://vaul.emilkowal.ski/inputs
channel: Vaul docs (web)
published: Unknown
authority: good-to-have
tags:
  - vaul
  - drawer
  - inputs
  - keyboard
  - mobile
  - forms
---

# Inputs – Vaul

## Metadata

- Page ID: `vaul-inputs`
- Publisher: Vaul docs (web)
- Published: Unknown
- URL: https://vaul.emilkowal.ski/inputs

## Summary

This Vaul docs page covers text inputs inside a drawer, which are traditionally hard to get right because the keyboard pushes the content up. Vaul fixes this by correcting the drawer's position when the keyboard opens. Setting repositionInputs to false turns the correction off and falls back to the browser's default behaviour. For a design system it names a failure mode for drawers that contain inputs (most likely on touch devices with an on-screen keyboard [inferred]) and the switch that turns Vaul's fix off.

## Key Ideas

- Inputs inside a drawer are traditionally tricky because the keyboard pushes the content up.
- Vaul corrects the drawer's position when the keyboard opens.
- repositionInputs set to false disables the repositioning.
- With repositioning off, the drawer falls back to the default browser behaviour.

## Entities

- [[entities/vaul|Vaul]] (library): Drawer component that repositions itself when the keyboard opens.
- [[entities/repositioninputs|repositionInputs]] (concept): Prop that turns the keyboard repositioning on or off.
- [[entities/aiforui-dev|aiforui.dev]] (product): Course advertised in the page banner; not part of the docs content.

## Topics

- [[topics/drawers-and-sheets|Drawers and sheets]]: Vaul corrects the drawer's position when the keyboard opens; repositionInputs false turns this off.
- [[topics/forms-and-inputs|Forms and inputs]]: Inputs inside drawers are tricky because the keyboard pushes content up; Vaul repositions the drawer.
- [[topics/mobile-app-patterns|Mobile app patterns]]: Keyboard handling for drawers that contain inputs; the page does not name mobile, but a keyboard that pushes content up points to on-screen keyboards [inferred].

## Notable Claims

- Inputs in drawers are tricky because the keyboard pushes the content up. Evidence: Inputs intro
- Vaul corrects the drawer's position when the keyboard is opened. Evidence: Inputs intro
- Setting repositionInputs to false disables repositioning and falls back to the default browser behaviour. Evidence: No repositioning

## Quotes

> Traditionally tricky to get right, because keyboard is pushing the content up.

<!-- od:learn -->

## For OpenDesigner

- Authority: **good-to-have**
- Caveat: Every page carries a banner advertising the aiforui.dev course ('31 minutes left to join'); it is self-promotion and time-sensitive.
- Caveat: The page does not explain how the repositioning works.
- Caveat: The demos' code and visuals were not captured in the raw text.
- Caveat: Published date is unknown.
- Caveat: Not in this page: learn/sources.json records that the Vaul README says the library is unmaintained (checked 2026-09-24); flag that before recommending it as a dependency.

### Rules and practices

- **should** (components, all): Keep the drawer's position corrected when the keyboard opens for an input inside it. Why: Otherwise the keyboard pushes the drawer's content up. Values: repositionInputs. [Inputs intro]
- **consider** (components, react): Turn repositioning off only when you want the browser's default keyboard behaviour. Why: Setting repositionInputs to false disables repositioning and falls back to default browser behaviour. Values: repositionInputs, false. [No repositioning]

### Decisions it informs

- When the keyboard opens for an input in a drawer, should the drawer reposition itself?
  - Reposition: The drawer's position is corrected when the keyboard opens. When: Inputs inside a drawer (the source's main setup).
  - Browser default (repositionInputs false): No repositioning; the default browser behaviour applies, where the keyboard can push content up [inferred]. When: When you want the default browser behaviour.
  - Recommendation: Reposition: the source presents it as Vaul's fix for content being pushed up by the keyboard.

### Examples and visual references

- Drawer with an input, repositioned for the keyboard (Vaul docs, Inputs): Demo behind an 'Open Drawer' button; visuals and code were not captured in the raw text.
- No repositioning demo (Vaul docs, Inputs): The same drawer with repositionInputs false, showing the default browser behaviour.

<!-- /od:learn -->
