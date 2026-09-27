---
type: source
title: "API Reference – Vaul"
created: 2026-09-27
updated: 2026-09-27
video_id: vaul-api
url: https://vaul.emilkowal.ski/api
channel: Vaul docs (web)
published: Unknown
authority: good-to-have
tags:
  - vaul
  - drawer
  - bottom-sheet
  - react
  - api
  - anatomy
  - snap-points
  - accessibility
---

# API Reference – Vaul

## Metadata

- Page ID: `vaul-api`
- Publisher: Vaul docs (web)
- Published: Unknown
- URL: https://vaul.emilkowal.ski/api

## Summary

The Vaul API reference lists the parts of a drawer and the props of each part. A drawer is assembled from Root, Trigger, Portal, Overlay, Content, Handle, Title, Description and Close. Root's defaults describe a drawer's out-of-the-box behaviour: modal, dismissible, opening from the bottom, handleOnly off (so, by the prop's name, a drag is not limited to the handle [inferred]), repositioning for inputs, and portalled into document.body. Extra Root props control snap points (snapPoints, activeSnapPoint, setActiveSnapPoint, fadeFromIndex, snapToSequentialPoint). For a design system this is a ready-made anatomy and a set of default behaviours for a drawer or bottom-sheet component, including optional accessible Title and Description text that is announced when the drawer opens.

## Key Ideas

- A drawer is built from separate parts that you import and compose: Root, Trigger, Portal, Overlay, Content, Handle, Title, Description, Close.
- Root holds all the parts and carries the behaviour props.
- By default a drawer is modal, dismissible and opens from the bottom.
- handleOnly defaults to false; read from the prop's name, a drag is not limited to the handle by default [inferred].
- Root also takes defaultOpen, open, onOpenChange and onAnimationEnd, with no default listed.
- By default the drawer repositions itself for inputs (repositionInputs is true).
- The Portal renders the overlay and content into the body; the default container is document.body.
- The Overlay covers the inert part of the view while the drawer is open.
- Title and Description are optional accessible text announced when the drawer opens.
- The Handle is an optional grip for dragging the drawer.
- Snap points are configured on Root with snapPoints, activeSnapPoint, setActiveSnapPoint, fadeFromIndex and snapToSequentialPoint.
- Trigger, Overlay, Content, Close, Title and Description each accept asChild, which defaults to false.

## Entities

- [[entities/vaul|Vaul]] (library): Drawer component whose parts and props this page documents.
- [[entities/drawer-root|Drawer.Root]] (concept): Container for all drawer parts; holds modal, direction, dismissible, handleOnly, repositionInputs and snap-point props.
- [[entities/drawer-overlay|Drawer.Overlay]] (concept): Layer covering the inert portion of the view while the drawer is open.
- [[entities/drawer-handle|Drawer.Handle]] (concept): Optional handle used to drag the drawer; takes no props.
- [[entities/drawer-title-and-drawer-description|Drawer.Title and Drawer.Description]] (concept): Optional accessible text announced when the drawer opens.
- [[entities/snap-points|Snap points]] (concept): Root props that let the drawer rest at defined points; listed as additional props.
- [[entities/aiforui-dev|aiforui.dev]] (product): Course advertised in the page banner; not part of the API content.

## Topics

- [[topics/drawers-and-sheets|Drawers and sheets]]: Full anatomy of a drawer component and the default behaviour of each prop: modal, dismissible, bottom direction, drag from anywhere, input repositioning.
- [[topics/ui-libraries|UI libraries]]: Vaul's component API: nine composable parts, Root props with defaults, and additional snap-point props.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: React compound-component anatomy (Drawer.Root, Drawer.Portal, Drawer.Content...) and prop types such as HTMLElement container and asChild booleans.
- [[topics/accessibility|Accessibility]]: Title and Description are optional accessible text announced when the drawer opens; the overlay covers the inert portion of the view while the drawer is open.
- [[topics/gestures-and-drag|Gestures and drag]]: An optional Handle drags the drawer; handleOnly defaults to false, which by its name decides whether only the handle starts a drag [inferred].

## Notable Claims

- Vaul's drawer is composed of Root, Trigger, Portal, Overlay, Content, Handle, Title, Description and Close. Evidence: Anatomy
- Root's modal prop defaults to true. Evidence: Root prop table: modal boolean true
- Root's container prop defaults to document.body. Evidence: Root prop table: container HTMLElement document.body
- Root's direction prop defaults to bottom. Evidence: Root prop table: direction directionType bottom
- Root's dismissible prop defaults to true and handleOnly defaults to false. Evidence: Root prop table
- Root's repositionInputs prop defaults to true. Evidence: Root prop table: repositionInputs boolean true
- Snap points are controlled by snapPoints, activeSnapPoint, setActiveSnapPoint, fadeFromIndex and snapToSequentialPoint. Evidence: Additional props for snap points
- Portal renders the overlay and content parts into the body and has no props. Evidence: Portal
- Title and Description are announced when the drawer is opened. Evidence: Title; Description
- Handle is optional, drags the drawer and has no props. Evidence: Handle
- Root also takes defaultOpen, open, onOpenChange and onAnimationEnd; the table lists no default for them. Evidence: Root prop table
- Trigger is the button that opens the drawer and Close is the button that closes it. Evidence: Trigger; Close
- Content contains the content rendered in the open drawer. Evidence: Content

## Quotes

> Import all parts and piece them together.
> A layer that covers the inert portion of the view when the drawer is open.
> An optional accessible title to be announced when the drawer is opened.

<!-- od:learn -->

## For OpenDesigner

- Authority: **good-to-have**
- Caveat: Every page carries a banner advertising the aiforui.dev course ('31 minutes left to join'); it is self-promotion and time-sensitive.
- Caveat: The prop table lists activeSnapPoint with type boolean while snapPoints is an array; the type may be a docs error [inferred].
- Caveat: The page lists asChild on several parts but does not explain what it does.
- Caveat: Published date is unknown.
- Caveat: Not in this page: learn/sources.json records that the Vaul README says the library is unmaintained (checked 2026-09-24); flag that before recommending it as a dependency.

### Rules and practices

- **should** (components, react): Build the drawer component from separate composable parts: Root, Trigger, Portal, Overlay, Content, Handle, Title, Description and Close. Why: The API is designed so you import all parts and piece them together. Values: Drawer.Root, Drawer.Trigger, Drawer.Portal, Drawer.Overlay, Drawer.Content, Drawer.Handle, Drawer.Title, Drawer.Description, Drawer.Close. [Anatomy]
- **should** (components, all): Make drawers modal by default. Why: Vaul's Root defaults modal to true. Values: modal, true. [Root prop table]
- **should** (components, all): Open drawers from the bottom edge by default. Why: Vaul's Root defaults direction to bottom. Values: direction, bottom. [Root prop table]
- **should** (components, all): Make drawers dismissible by default. Why: Vaul's Root defaults dismissible to true. Values: dismissible, true. [Root prop table]
- **should** (components, all): Keep handleOnly false by default, so a drag is not limited to the handle [inferred]. Why: Vaul's Root defaults handleOnly to false; the page does not define the prop beyond its name. Values: handleOnly, false. [handleOnly boolean]
- **should** (components, all): Reposition the drawer for inputs by default. Why: Vaul's Root defaults repositionInputs to true. Values: repositionInputs, true. [Root prop table]
- **should** (components, react): Portal the drawer's overlay and content into document.body by default. Why: Portal renders the overlay and content into the body, and Root's container defaults to document.body. Values: container, document.body. [Portal; Root prop table]
- **should** (components, all): Render an Overlay that covers the inert part of the view while the drawer is open. Why: The Overlay is the layer that covers the inert portion of the view when the drawer is open. [A layer that covers the inert portion of the view]
- **consider** (accessibility, all): Give the drawer a Title and Description so they are announced when it opens. Why: Title and Description are the optional accessible text announced when the drawer is opened. Values: Drawer.Title, Drawer.Description. [Title; Description]
- **consider** (components, all): Add a Handle when the drawer should show a grip for dragging. Why: The Handle is an optional part used to drag the drawer. Values: Drawer.Handle. [Handle]
- **consider** (components, react): Place a Close button inside the drawer's Content. Why: The anatomy puts Drawer.Close, the button that closes the drawer, inside Drawer.Content. Values: Drawer.Close, Drawer.Content. [Anatomy; Close]

### Decisions it informs

- Should a drag start anywhere on the drawer, or only on its handle?
  - Anywhere on the drawer (handleOnly false): The whole drawer can be dragged [inferred]. When: The default.
  - Handle only (handleOnly true): Only the handle starts a drag [inferred]. When: Not stated by the source.
  - Recommendation: No recommendation; the source's default is handleOnly false and it gives no reason.

### Process

1. Wrap in Root: Drawer.Root contains all the parts of the drawer and carries the behaviour props.
2. Add the Trigger: Drawer.Trigger is the button that opens the drawer.
3. Portal the layers: Inside Drawer.Portal place Drawer.Overlay and Drawer.Content.
4. Fill the Content: Inside Drawer.Content place Drawer.Handle, Drawer.Title, Drawer.Description and Drawer.Close alongside your content.

### Examples and visual references

- Anatomy snippet: a MyDrawer component nesting Root > Trigger, Portal > Overlay, Content > Handle, Title, Description, Close. (Vaul docs, API Reference): Code only; shows the nesting order of every drawer part.

<!-- /od:learn -->
