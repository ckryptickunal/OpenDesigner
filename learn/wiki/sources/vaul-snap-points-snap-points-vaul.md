---
type: source
title: "Snap Points – Vaul"
created: 2026-09-27
updated: 2026-09-27
video_id: vaul-snap-points
url: https://vaul.emilkowal.ski/snap-points
channel: Vaul docs (web)
published: Unknown
authority: good-to-have
tags:
  - vaul
  - drawer
  - snap-points
  - drag
  - velocity
  - fade
  - bottom-sheet
---

# Snap Points – Vaul

## Metadata

- Page ID: `vaul-snap-points`
- Publisher: Vaul docs (web)
- Published: Unknown
- URL: https://vaul.emilkowal.ski/snap-points

## Summary

This Vaul docs page explains snap points: a set of points the drawer can snap to while it is dragged, so a drawer can be partially open rather than only open or closed. Combining modal set to false with snap points lets people use the background while the drawer is open. snapToSequentialPoint turns off velocity-based snapping so a fast drag never skips a point, which the page calls useful when every point is equally important. fadeFromIndex sets the snap point from which the drawer starts fading; it defaults to the last point. For a design system these are the choices a multi-height sheet needs.

## Key Ideas

- Snap points are positions the drawer can snap to during a drag.
- With snap points a drawer can be partially open, not only open or closed.
- modal false combined with snap points keeps the background interactive while the drawer is open.
- By default snapping is velocity-based: a fast enough drag can skip a snap point.
- snapToSequentialPoint stops points being skipped even at high velocity.
- Sequential snapping suits drawers where each snap point is equally important.
- fadeFromIndex sets the snap point index where the drawer starts fading; the default is the last point.

## Entities

- [[entities/vaul|Vaul]] (library): Drawer component whose snap-point behaviour this page documents.
- [[entities/snap-points|Snap points]] (concept): Points a drawer can snap to during a drag, allowing a partially open state.
- [[entities/snaptosequentialpoint|snapToSequentialPoint]] (concept): Prop that disables velocity-based snapping so no point is skipped.
- [[entities/fadefromindex|fadeFromIndex]] (concept): Prop giving the snap point index from which the drawer starts fading.
- [[entities/aiforui-dev|aiforui.dev]] (product): Course advertised in the page banner; not part of the docs content.

## Topics

- [[topics/drawers-and-sheets|Drawers and sheets]]: Snap points let a drawer rest partially open; options for background interaction, sequential snapping and where fading starts.
- [[topics/gestures-and-drag|Gestures and drag]]: Velocity-based snapping can skip points on a fast drag; snapToSequentialPoint prevents that.
- [[topics/modals-and-popovers|Modals and popovers]]: modal false with snap points keeps the background interactive while the drawer is open.

## Notable Claims

- Snap points let a drawer be partially open instead of only open or closed. Evidence: Snap Points intro
- Combining modal={false} with snap points allows interaction with the background while the drawer is open. Evidence: Interact with background
- snapToSequentialPoint disables velocity-based snapping, so a snap point is not skipped even at high velocity. Evidence: Snap to sequential points
- fadeFromIndex defaults to the last snap point. Evidence: Custom fade index
- The custom fade index demo changes fadeFromIndex to the second point. Evidence: Custom fade index

## Quotes

> a drawer no longer only has to be open or closed
> a snap point won't be skipped even if the velocity is high enough.
> Useful if each snap point in a drawer is equally important.

<!-- od:learn -->

## For OpenDesigner

- Authority: **good-to-have**
- Caveat: Every page carries a banner advertising the aiforui.dev course ('31 minutes left to join'); it is self-promotion and time-sensitive.
- Caveat: The page does not say how snap point values are written (fractions or pixels) or what exactly fades.
- Caveat: The demos' code and visuals were not captured in the raw text.
- Caveat: Published date is unknown.
- Caveat: Not in this page: learn/sources.json records that the Vaul README says the library is unmaintained (checked 2026-09-24); flag that before recommending it as a dependency.

### Rules and practices

- **consider** (components, all): Use snap points when a drawer should be able to rest partially open, not only open or closed. Why: Snap points define where the drawer can stop during a drag, allowing a partially open state. [Snap Points intro]
- **consider** (components, react): Combine modal={false} with snap points when people need to use the background while the drawer is open. Why: The combination keeps the background interactive. Values: modal={false}. [Interact with background]
- **should** (components, react): Turn on snapToSequentialPoint when every snap point in the drawer is equally important. Why: It disables velocity-based snapping, so a fast drag cannot skip a point. Values: snapToSequentialPoint. [Snap to sequential points]
- **consider** (motion, react): Set fadeFromIndex to the snap point index from which the drawer should start fading; without it, fading starts from the last point. Why: fadeFromIndex defaults to the last point; the demo moves it to the second point. Values: fadeFromIndex. [Custom fade index]

### Decisions it informs

- Should the drawer only be open or closed, or also able to rest partially open?
  - Open or closed only: The drawer has two states. When: Not stated on this page.
  - Snap points: The drawer can snap to set points during a drag and rest partially open. When: When the drawer should be able to be partially open.
- Should a fast drag be able to skip snap points?
  - Velocity-based snapping: A fast enough drag can skip a snap point. When: The default behaviour.
  - Sequential snapping (snapToSequentialPoint): No snap point is skipped, even at high velocity. When: When each snap point in the drawer is equally important.
  - Recommendation: Sequential snapping when every snap point is equally important; otherwise the velocity-based default.
- From which snap point should the drawer start fading?
  - Last point: Fading starts from the last snap point. When: The default.
  - An earlier point (e.g. the second): Fading starts from the chosen earlier snap point. When: Shown in the demo; the page gives no rule for when.
- Should the background stay interactive while a drawer with snap points is open?
  - Modal: The background is not interactive [inferred]. When: Not stated on this page.
  - Non-modal (modal={false}) with snap points: People can interact with the background while the drawer is open. When: When the background must stay usable alongside a partially open drawer.

### Examples and visual references

- Snap points demo (Vaul docs, Snap Points): A drawer that snaps to set points while dragged; visuals and code were not captured in the raw text.
- Interact with background demo (Vaul docs, Snap Points): Snap-point drawer with modal={false}, leaving the background usable.
- Snap to sequential points demo (Vaul docs, Snap Points): A fast drag stops at each point in turn instead of skipping.
- Custom fade index demo (Vaul docs, Snap Points): fadeFromIndex moved from the last point to the second point.

<!-- /od:learn -->
