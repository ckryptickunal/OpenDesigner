---
type: source
title: "Other – Vaul"
created: 2026-09-27
updated: 2026-09-27
video_id: vaul-other
url: https://vaul.emilkowal.ski/other
channel: Vaul docs (web)
published: Unknown
authority: good-to-have
tags:
  - vaul
  - drawer
  - non-modal
  - non-dismissible
  - family
  - react
---

# Other – Vaul

## Metadata

- Page ID: `vaul-other`
- Publisher: Vaul docs (web)
- Published: Unknown
- URL: https://vaul.emilkowal.ski/other

## Summary

This Vaul docs page collects other drawer configurations. A non-modal drawer (modal set to false) lets people interact with the background while it is open. A non-dismissible drawer (dismissible set to false) cannot be closed by clicking outside, pressing Escape or dragging down, and the page warns that opening its demo means refreshing to close it. A Dynamic Drawer demo recreates the Family drawer with Vaul. For a design system it shows two behaviour switches a drawer component can expose, and, through the demo's warning, what happens when every way to dismiss is removed.

## Key Ideas

- Setting modal to false lets people interact with the background while the drawer is open.
- Setting dismissible to false stops the drawer closing on an outside click, the Escape key or a downward drag.
- The non-dismissible demo can only be closed by refreshing the page.
- Vaul can recreate the Family drawer (the Dynamic Drawer demo).

## Entities

- [[entities/vaul|Vaul]] (library): Drawer component whose extra configurations this page shows.
- [[entities/family|Family]] (product): Product whose drawer the Dynamic Drawer demo recreates.
- [[entities/animations-on-the-web|Animations on the Web]] (product): Plugged on the page as where the Family drawer recreation is built together; a course [inferred].
- [[entities/aiforui-dev|aiforui.dev]] (product): Course advertised in the page banner; not part of the docs content.

## Topics

- [[topics/drawers-and-sheets|Drawers and sheets]]: Non-modal and non-dismissible drawers, plus a recreation of the Family drawer.
- [[topics/modals-and-popovers|Modals and popovers]]: modal false keeps the background interactive; dismissible false removes outside-click, Escape and drag-down dismissal.
- [[topics/accessibility|Accessibility]]: A non-dismissible drawer ignores the Escape key, outside clicks and drag-down, and its demo can only be closed by refreshing; the page does not frame this as accessibility [inferred].

## Notable Claims

- Setting modal to false allows interaction with the background while the drawer is open. Evidence: Non-modal
- Setting dismissible to false prevents closing by clicking outside, pressing Escape or dragging down. Evidence: Non-dismissible
- The non-dismissible demo can only be closed by refreshing the page. Evidence: Non-dismissible
- The Dynamic Drawer demo is a recreation of the Family drawer built with Vaul. Evidence: Dynamic Drawer

## Quotes

> Don't open this one or else you'll have to refresh the page to close it.

<!-- od:learn -->

## For OpenDesigner

- Authority: **good-to-have**
- Caveat: Every page carries a banner advertising the aiforui.dev course ('31 minutes left to join'); it is self-promotion and time-sensitive.
- Caveat: The Dynamic Drawer section plugs the Animations on the Web course, where the recreation is built.
- Caveat: Defaults for modal and dismissible are not stated on this page (the API page lists both as true).
- Caveat: The demos' code and visuals were not captured in the raw text.
- Caveat: Published date is unknown.
- Caveat: Not in this page: learn/sources.json records that the Vaul README says the library is unmaintained (checked 2026-09-24); flag that before recommending it as a dependency.

### Rules and practices

- **consider** (components, react): Set modal to false when people need to interact with the background while the drawer is open. Why: A non-modal drawer allows interaction with the background. Values: modal, false. [Non-modal]
- **consider** (components, react): Set dismissible to false to stop the drawer closing on an outside click, the Escape key or a downward drag. Why: The source says it prevents the user from closing the drawer in all three ways. Values: dismissible, false. [Non-dismissible]
- **should** (accessibility, all): If a drawer is non-dismissible, give it an explicit way to close [inferred]. Why: Without one, the source's non-dismissible demo can only be closed by refreshing the page. [Non-dismissible]

### Decisions it informs

- Should the page behind the drawer stay usable while the drawer is open?
  - Modal: The background is not interactive while the drawer is open [inferred]. When: Not stated on this page.
  - Non-modal (modal false): People can interact with the background while the drawer is open. When: When the background must stay usable.
- Can people close the drawer by clicking outside, pressing Escape or dragging down?
  - Dismissible: Outside click, Escape and drag-down close the drawer [inferred]. When: Not stated on this page.
  - Non-dismissible (dismissible false): None of the three close it; the demo can only be left by refreshing. When: When the drawer must not be closed by those actions.

### Examples and visual references

- Non-modal drawer demo (Vaul docs, Other): Drawer open while the background stays interactive; visuals were not captured in the raw text.
- Non-dismissible drawer demo (Vaul docs, Other): Drawer with no outside-click, Escape or drag-down dismissal; the page warns you must refresh to close it.
- Dynamic Drawer (Family): Recreation of the Family drawer using Vaul; no visual description in the raw text.

<!-- /od:learn -->
