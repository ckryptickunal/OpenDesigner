---
type: source
title: "Getting Started – Sonner"
created: 2026-09-27
updated: 2026-09-27
video_id: sonner-getting-started
url: https://sonner.emilkowal.ski/getting-started
channel: Sonner docs (web)
published: Unknown
authority: non-negotiable
tags:
  - sonner
  - toast
  - react
  - setup
  - installation
  - nextjs-layout
---

# Getting Started – Sonner

## Metadata

- Video ID: `sonner-getting-started`
- Channel: Sonner docs (web)
- Published: Unknown
- URL: https://sonner.emilkowal.ski/getting-started

## Summary

The Getting Started page of the Sonner docs shows the three steps to put toasts into a React app. You install the sonner package, add the Toaster component once to your app, and call the toast() function from any event handler to show a toast. The page stresses that Toaster can be placed anywhere, even in a server component such as the root layout.tsx. For a design system this fixes the setup pattern for toasts: a Toaster mounted in the root layout and a single function call for every message. [inferred]

## Key Ideas

- Sonner is a toast component for React.
- Install it from the command line as the sonner package.
- Toasts need a Toaster component rendered in the app.
- Toaster can live anywhere, including a server component such as layout.tsx.
- The example mounts Toaster inside body, after the page children, in the root layout.
- A toast is shown by calling toast() with a string, for example from a button's onClick.
- Toaster and toast are named imports from 'sonner'.
- Every toast option is documented on the separate toast() page.

## Entities

- [[entities/sonner|Sonner]] (library): The toast component for React that this page sets up.
- [[entities/toaster|Toaster]] (concept): Sonner's component that must be added to the app so toasts can render.
- [[entities/toast|toast()]] (concept): Sonner's function that renders a toast when called.
- [[entities/react|React]] (library): The UI framework Sonner is built for.
- [[entities/pnpm|pnpm]] (tool): The package manager used in the install command.
- [[entities/aiforui-dev|aiforui.dev]] (product): A course promoted in the site-wide banner at the top of the page.

## Topics

- [[topics/toasts-and-notifications|Toasts and notifications]]: How to install Sonner, mount the Toaster and render a first toast.
- [[topics/ui-libraries|UI libraries]]: Sonner is presented as a ready-made toast component for React, installed as a package.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Shows the React code: Toaster in the root layout.tsx and toast('Toast') in a button onClick.

## Notable Claims

- Sonner is a toast component for React. Evidence: Sonner is a toast component for React.
- The Toaster component can be placed anywhere in the app, even in server components such as layout.tsx. Evidence: It can be placed anywhere, even in server components such as layout.tsx
- Calling toast() with a string renders a toast. Evidence: Render a toast
- All toast options are documented on the toast page. Evidence: For all options, view the toast page

## Quotes

> Sonner is a toast component for React.
> It can be placed anywhere, even in server components such as layout.tsx

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: A site-wide banner promotes the author's aiforui.dev course with a countdown ('31 minutes left to join'). This is self-promotion and time-sensitive, not documentation.
- Caveat: The page's publish date is unknown, so the API it shows may have changed since it was fetched.
- Caveat: This page installs with pnpm i sonner, while the Sonner homepage uses npm install sonner.
- Caveat: The page links to a write-up on how Sonner was built, but that write-up is not part of this text.

### Rules and practices

- **should** (tooling, react): Install the sonner package from the command line; this page's command is pnpm i sonner. Why: Installation is the first documented step: install the component from your command line. Values: pnpm i sonner. [Install the component from your command line.]
- **must** (components, react): Add the <Toaster /> component to the app before calling toast(); the example mounts it inside <body>, after {children}, in the root layout.tsx. Why: Getting Started lists adding Toaster to your app as a setup step, before rendering a toast. Values: <Toaster />, layout.tsx. [Add Toaster to your app]
- **consider** (components, react): It is fine to render <Toaster /> inside a server component such as layout.tsx; it does not have to sit in a particular place. Why: The docs say it can be placed anywhere, even in server components. Values: layout.tsx. [It can be placed anywhere, even in server components such as layout.tsx]
- **should** (tooling, react): Import Toaster and toast as named imports from the 'sonner' package. Why: This is how the page's code examples import the component and the function. Values: import { Toaster } from 'sonner', import { toast } from 'sonner'. [import { Toaster } from 'sonner']
- **should** (components, react): Show a toast by calling toast() with the message string from an event handler, for example a button's onClick. Why: This is the documented way to render a toast. Values: toast('Toast'), onClick={() => toast('Toast')}. [Render a toast]

### Process

1. Install: Run pnpm i sonner from the command line.
2. Add Toaster to your app: Import { Toaster } from 'sonner' and render <Toaster /> in the app, for example inside <body> after {children} in the root layout.tsx. A server component is fine.
3. Render a toast: Import { toast } from 'sonner' and call toast('...') from an event handler such as a button's onClick. See the toast page for all options.

### Examples and visual references

- Root layout with Toaster (layout.tsx (RootLayout)): Code only: <html lang="en"><body>{children}<Toaster /></body></html>, showing Toaster mounted once at the root, after the page content.
- Button that renders a toast (MyToast component): Code only: a button labelled 'Render Toast' whose onClick calls toast('Toast').

<!-- /od:learn -->
