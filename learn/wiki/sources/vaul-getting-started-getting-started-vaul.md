---
type: source
title: "Getting Started – Vaul"
created: 2026-09-27
updated: 2026-09-27
video_id: vaul-getting-started
url: https://vaul.emilkowal.ski/getting-started
channel: Vaul docs (web)
published: Unknown
authority: good-to-have
tags:
  - vaul
  - drawer
  - react
  - install
  - overlay
  - bottom-sheet
---

# Getting Started – Vaul

## Metadata

- Page ID: `vaul-getting-started`
- Publisher: Vaul docs (web)
- Published: Unknown
- URL: https://vaul.emilkowal.ski/getting-started

## Summary

The getting-started page introduces Vaul as a drawer component for React, installed with pnpm, npm or yarn. It gives a minimal client component that composes Root, Trigger, Portal, Overlay and Content, and notes the drawer can be placed anywhere in the app. The example's styling gives concrete starting values: an overlay styled fixed inset-0 bg-black/40, and content styled fixed bottom-0 left-0 right-0 h-fit on bg-gray-100 with a p-4 bg-white inner block (read as utility classes: a full-screen black overlay at 40% and a full-width bottom sheet as tall as its content [inferred]). For a design system it is the smallest working drawer, with a concrete overlay dim value and bottom-sheet layout to start from.

## Key Ideas

- Vaul is a drawer component for React.
- Install it with pnpm, npm or yarn (pnpm i vaul).
- The drawer component file is marked 'use client'.
- A minimal drawer composes Root, Trigger, Portal, Overlay and Content.
- The example overlay is styled fixed inset-0 bg-black/40, a full-screen black layer at 40% [inferred].
- The example content is styled bg-gray-100 h-fit fixed bottom-0 left-0 right-0 outline-none: pinned to the bottom, full width, as tall as its content [inferred].
- Vaul is imported as { Drawer } from 'vaul'.
- The drawer component can be placed anywhere in the app.

## Entities

- [[entities/vaul|Vaul]] (library): Drawer component for React introduced on this page.
- [[entities/react|React]] (library): Framework Vaul is built for.
- [[entities/pnpm-npm-yarn|pnpm / npm / yarn]] (tool): Package managers named for installing Vaul.
- [[entities/aiforui-dev|aiforui.dev]] (product): Course advertised in the page banner; not part of the docs content.

## Topics

- [[topics/drawers-and-sheets|Drawers and sheets]]: The smallest working drawer: a trigger, a dimmed overlay and bottom-pinned content.
- [[topics/ui-libraries|UI libraries]]: Vaul is installed as a package (pnpm i vaul) and imported as { Drawer } from 'vaul'.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: A 'use client' React component styled with utility classes: fixed inset-0 bg-black/40 overlay and fixed bottom-0 left-0 right-0 h-fit content.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: The example overlay behind the drawer is black at /40 (bg-black/40).

## Notable Claims

- Vaul is a drawer component for React. Evidence: Getting Started intro
- Vaul installs with pnpm, npm or yarn. Evidence: Installation
- The drawer component can be placed anywhere in the app. Evidence: Create a Drawer component

## Quotes

> Vaul is a drawer component for React.
> It can be placed anywhere in your app.

<!-- od:learn -->

## For OpenDesigner

- Authority: **good-to-have**
- Caveat: Every page carries a banner advertising the aiforui.dev course ('31 minutes left to join'); it is self-promotion and time-sensitive.
- Caveat: The styling uses utility class names without naming the CSS framework; they look like Tailwind CSS classes [inferred].
- Caveat: The example is a minimal starter, not a styling recommendation the page argues for; the colours and spacing are example values.
- Caveat: The page links to an article on how Vaul was built; that article is not part of this raw text.
- Caveat: Published date is unknown.
- Caveat: Not in this page: learn/sources.json records that the Vaul README says the library is unmaintained (checked 2026-09-24); flag that before recommending it as a dependency.

### Rules and practices

- **consider** (elevation, css): Style the overlay behind a drawer as fixed inset-0 bg-black/40, a fixed full-screen black layer at 40% [inferred]. Why: The starter example styles Drawer.Overlay this way. Values: fixed inset-0, bg-black/40. [Create a Drawer component (MyDrawer.tsx)]
- **consider** (layout, css): Style bottom-drawer content as fixed bottom-0 left-0 right-0 h-fit outline-none on bg-gray-100: pinned to the bottom edge, full width, as tall as its content [inferred]. Why: The starter example styles Drawer.Content this way. Values: fixed bottom-0 left-0 right-0, h-fit, outline-none, bg-gray-100. [Create a Drawer component (MyDrawer.tsx)]
- **consider** (layout, css): Put the drawer's content in a padded inner block (p-4 on white) inside Drawer.Content. Why: The starter example wraps its content this way. Values: p-4, bg-white. [Create a Drawer component (MyDrawer.tsx)]
- **consider** (tooling, react): Mark the drawer component file as a client component with 'use client'. Why: The starter MyDrawer.tsx begins with it; the source gives no further reason. Values: 'use client'. [MyDrawer.tsx]

### Process

1. Install: Install the package with pnpm, npm or yarn: pnpm i vaul.
2. Create the component: Create MyDrawer.tsx, mark it 'use client' and import { Drawer } from 'vaul'.
3. Compose the parts: Drawer.Root > Drawer.Trigger ('Open Drawer') and Drawer.Portal > Drawer.Overlay + Drawer.Content, with your content in an inner div.
4. Style overlay and content: Overlay: fixed inset-0 bg-black/40. Content: bg-gray-100 h-fit fixed bottom-0 left-0 right-0 outline-none. Inner block: p-4 bg-white.
5. Place it: Render the component anywhere in the app.

### Examples and visual references

- MyDrawer.tsx starter component (Vaul docs, Getting Started): Code only: an 'Open Drawer' trigger opens a bottom drawer on a gray-100 surface with a white padded content block, over a black overlay at /40.

### Numbers

- bg-black/40: Overlay colour behind the drawer in the starter example; close to the 'scrim-fluent' option of Q-depth-06 (black 40% in light mode) [inferred] [Drawer.Overlay className in MyDrawer.tsx]

<!-- /od:learn -->
