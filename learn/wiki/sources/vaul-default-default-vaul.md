---
type: source
title: "Default – Vaul"
created: 2026-09-27
updated: 2026-09-27
video_id: vaul-default
url: https://vaul.emilkowal.ski/default
channel: Vaul docs (web)
published: Unknown
authority: good-to-have
tags:
  - vaul
  - drawer
  - side-drawer
  - nested-drawers
  - scrollable
  - controlled
  - react
---

# Default – Vaul

## Metadata

- Video ID: `vaul-default`
- Channel: Vaul docs (web)
- Published: Unknown
- URL: https://vaul.emilkowal.ski/default

## Summary

This Vaul docs page shows the basic drawer setups: the default bottom drawer, a side drawer, nested drawers, a scrollable drawer and a controlled drawer. A side drawer is made by setting direction to "right" or "left", and the --initial-transform CSS variable adjusts its animation, which is useful when the drawer does not touch the screen edge. The scrollable drawer's behaviour mimics Apple's Sheet component. A controlled drawer uses the open prop to open or close programmatically, and onOpenChange lets it react to Escape and outside clicks. For a design system it lists the drawer variants a drawer component can offer, and a CSS variable for adjusting the animation of drawers that do not touch the screen edge.

## Key Ideas

- The default drawer is the most basic setup.
- Setting direction to "right" or "left" turns the drawer into a side drawer.
- The --initial-transform CSS variable adjusts the drawer's animation.
- --initial-transform is useful when the drawer does not touch the edge of the screen.
- Drawers can be nested inside each other.
- A scrollable drawer can mimic the behaviour of Apple's Sheet component.
- The open prop opens or closes the drawer programmatically.
- onOpenChange is called when the open state changes, so a controlled drawer can react to Escape and outside clicks.

## Entities

- [[entities/vaul|Vaul]] (library): Drawer component whose basic setups this page demonstrates.
- [[entities/apple-sheet|Apple Sheet]] (product): Apple's Sheet component, whose behaviour the scrollable drawer mimics.
- [[entities/initial-transform|--initial-transform]] (concept): CSS variable that adjusts the drawer's animation, for drawers that do not touch the screen edge.
- [[entities/onopenchange|onOpenChange]] (concept): Callback fired when the drawer's open state changes; used to react to Escape and outside clicks when controlled.
- [[entities/aiforui-dev|aiforui.dev]] (product): Course advertised in the page banner; not part of the docs content.

## Topics

- [[topics/drawers-and-sheets|Drawers and sheets]]: Variants of a drawer: default bottom, side (right or left), nested, scrollable like Apple's Sheet, and controlled.
- [[topics/motion-principles|Motion principles]]: The --initial-transform CSS variable adjusts the drawer's animation, useful when the drawer does not touch the screen edge.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: The direction prop, the --initial-transform CSS variable, and the controlled open / onOpenChange pattern.

## Notable Claims

- Setting the direction prop to "right" or "left" changes the drawer's position. Evidence: Side drawer
- The --initial-transform CSS variable adjusts the drawer's animation and is useful when the drawer does not touch the edge of the screen. Evidence: Side drawer
- Vaul drawers can be nested inside each other. Evidence: Nested Drawers
- The scrollable drawer's behaviour mimics Apple's Sheet component. Evidence: Scrollable
- onOpenChange is called when the open state changes and lets a controlled drawer react to Escape and outside clicks. Evidence: Controlled
- The open prop opens or closes the drawer programmatically. Evidence: Controlled

## Quotes

> The behavior here mimics Apple's Sheet component.
> The most basic setup for a drawer.

<!-- od:learn -->

## For OpenDesigner

- Authority: **good-to-have**
- Caveat: Every page carries a banner advertising the aiforui.dev course ('31 minutes left to join'); it is self-promotion and time-sensitive.
- Caveat: The demos' code and visuals were not captured in the raw text; only the prose under each heading is available.
- Caveat: The page does not give values for --initial-transform or say when to prefer a side drawer.
- Caveat: Published date is unknown.
- Caveat: Not in this page: learn/sources.json records that the Vaul README says the library is unmaintained (checked 2026-09-24); flag that before recommending it as a dependency.

### Rules and practices

- **consider** (components, react): Make a side drawer by setting direction to "right" or "left". Why: The direction prop changes the position of the drawer. Values: direction, "right", "left". [Side drawer]
- **should** (motion, css): When a drawer does not touch the edge of the screen, adjust its animation with the --initial-transform CSS variable. Why: The variable adjusts the animation, which the source calls useful when the drawer does not touch the screen edge. Values: --initial-transform. [Side drawer]
- **consider** (components, all): For a scrollable drawer, consider mimicking the behaviour of Apple's Sheet component, as Vaul's scrollable demo does. Why: The source's scrollable drawer mimics Apple's Sheet. [Scrollable]
- **should** (components, react): When you control the drawer with the open prop and need to react to Escape or outside clicks, also pass onOpenChange. Why: onOpenChange is called when the open state changes, which the source says is useful for reacting to esc/outside clicks when controlled. Values: open, onOpenChange. [Controlled]
- **consider** (components, react): To open a drawer from inside another drawer, nest one drawer inside the other. Why: The source shows nesting drawers inside each other as a supported setup. [Nested Drawers]

### Decisions it informs

- Which edge should the drawer slide in from?
  - Bottom: The default drawer. When: The default setup.
  - Right: A side drawer on the right. When: Not stated by the source.
  - Left: A side drawer on the left. When: Not stated by the source.
- Should the app control when the drawer opens and closes?
  - Uncontrolled: The drawer manages its own open state [inferred]. When: When code does not need to open or close the drawer [inferred].
  - Controlled (open + onOpenChange): Code opens or closes the drawer and can react to Escape and outside clicks. When: When you need to open or close the drawer programmatically.

### Examples and visual references

- Default drawer demo (Vaul docs, Default): An 'Open Drawer' button opening the most basic drawer; visuals and code were not captured in the raw text.
- Side drawer demo (Vaul docs, Default): A drawer opened from the side that does not touch the screen edge, which is why the page points to --initial-transform.
- Nested drawers demo (Vaul docs, Default): A drawer opened from inside another drawer.
- Scrollable drawer demo (Vaul docs, Default): A drawer with scrolling content that behaves like Apple's Sheet.
- Controlled drawer demo (Vaul docs, Default): A drawer opened and closed through the open prop.

<!-- /od:learn -->
