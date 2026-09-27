---
type: source
title: Sonner
created: 2026-09-27
updated: 2026-09-27
video_id: sonner-home
url: https://sonner.emilkowal.ski/
channel: Sonner docs (web)
published: Unknown
authority: non-negotiable
tags:
  - sonner
  - toast
  - react
  - toast-types
  - toast-position
  - swipe-to-dismiss
  - rich-colors
---

# Sonner

## Metadata

- Video ID: `sonner-home`
- Channel: Sonner docs (web)
- Published: Unknown
- URL: https://sonner.emilkowal.ski/

## Summary

The Sonner homepage introduces Sonner as an opinionated toast component for React and demonstrates its main options. You install it with npm, render the Toaster at the root of the app, and call toast() with an optional options object as the second argument. The page shows the toast types (default, description, success, info, warning, error, action, promise, custom), the six toaster positions, the expand setting and visibleToasts, and extras such as rich colors, a close button and a headless mode. It also notes that the swipe direction changes depending on the position. For a design system this is the menu of toast variants and placement options the house toast is built from. [inferred]

## Key Ideas

- Sonner is an opinionated toast component for React.
- Render the Toaster in the root of the app, then call toast() wherever a message is needed.
- toast() takes the message first and an options object second.
- Toast types: default, description, success, info, warning, error, action, promise and custom.
- The toaster can sit in six positions: top-left, top-center, top-right, bottom-left, bottom-center, bottom-right.
- The direction you swipe a toast away changes with the toaster's position.
- The expand prop switches between the default and an expanded pile of toasts.
- visibleToasts controls how many toasts are visible.
- richColors adds type-specific rich colors for success, error, info and warning toasts.
- A close button and a headless mode are available.
- The page closes with a plug for the author's animations course.

## Entities

- [[entities/sonner|Sonner]] (library): The opinionated React toast component the page presents.
- [[entities/toaster|Toaster]] (concept): The component rendered at the root of the app that displays toasts; it takes position, expand and richColors props.
- [[entities/toast|toast()]] (concept): The function that renders a toast, with typed variants such as toast.success().
- [[entities/emil-kowalski|Emil Kowalski]] (person): Sonner's author: the page's media list has a profile picture with the alt text "Emil's profile picture", and the page promotes his animations course. The surname comes from the site's domain. [inferred]
- [[entities/react|React]] (library): The framework Sonner is built for.
- [[entities/npm|npm]] (tool): The package manager in the homepage install command.
- [[entities/animations-course|Animations course]] (product): The author's course on animations that feel right, promoted at the bottom of the page.
- [[entities/aiforui-dev|aiforui.dev]] (product): A course promoted in the site-wide banner.

## Topics

- [[topics/toasts-and-notifications|Toasts and notifications]]: Lists Sonner's toast types, positions, expand behaviour, rich colors, close button and headless mode.
- [[topics/ui-libraries|UI libraries]]: Presents Sonner as an opinionated, installable toast component for React.
- [[topics/gestures-and-drag|Gestures and drag]]: Notes that the swipe direction for dismissing a toast depends on the toaster's position.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Shows the React usage: <Toaster /> at the root and toast('My first toast') in a button onClick.

## Notable Claims

- Sonner is an opinionated toast component for React. Evidence: An opinionated toast component for React.
- toast() takes an options object as its second argument, and the type of toast can be customized. Evidence: pass an options object as the second argument
- Sonner offers default, description, success, info, warning, error, action, promise and custom toasts. Evidence: Default Description Success Info Warning Error Action Promise Custom
- The toaster can be placed top-left, top-center, top-right, bottom-left, bottom-center or bottom-right. Evidence: top-left top-center top-right bottom-left bottom-center bottom-right
- Swipe direction changes depending on the toaster's position. Evidence: Swipe direction changes depending on the position.
- The number of visible toasts can be changed with the visibleToasts prop. Evidence: You can change the amount of toasts visible through the visibleToasts prop.
- Rich colors are available for success, error, info and warning toasts through the richColors prop. Evidence: Rich Colors Success Rich Colors Error Rich Colors Info Rich Colors Warning

## Quotes

> An opinionated toast component for React.
> Render the toaster in the root of your app.
> Swipe direction changes depending on the position.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: A site-wide banner promotes the author's aiforui.dev course with a countdown ('31 minutes left to join'): self-promotion, time-sensitive.
- Caveat: The page ends with a plug for the author's animations course ('Check out my animations course'). This is promotion, not guidance.
- Caveat: The homepage demos are interactive buttons, so the text does not show what each toast looks like. Visual effects described here come from the labels and code.
- Caveat: The page's publish date is unknown, so the API may have changed since it was fetched.
- Caveat: The media list contains only the author's profile picture (alt text "Emil's profile picture"), which carries no design lesson.
- Caveat: The homepage says to render the toaster in the root of your app, while the Getting Started and Toaster pages say it can be placed anywhere; the root is where the examples put it, not a hard requirement.

### Rules and practices

- **should** (components, react): Use Sonner as the toast component in React projects. [inferred] Why: The page presents Sonner as an opinionated toast component for React, and the owner marked the Sonner docs as a non-negotiable source. [inferred] [An opinionated toast component for React.]
- **should** (tooling, react): Install Sonner with npm install sonner. Why: This is the install command on the homepage. Values: npm install sonner. [npm install sonner]
- **should** (components, react): Render the <Toaster /> component in the root of the app. Why: The usage section says to render the toaster in the root of your app. Values: <Toaster />. [Render the toaster in the root of your app.]
- **should** (components, react): Show a toast by calling toast() with the message, and pass extra options as an object in the second argument. Why: The page shows toast('My first toast') and says an options object can be passed as the second argument. Values: toast('My first toast'), toast('Event has been created'). [pass an options object as the second argument]
- **consider** (components, react): Pick each toast's type from Sonner's set: default, description, success, info, warning, error, action, promise or custom. Why: The page says you can customize the type of toast you render and lists these types. Values: Default, Description, Success, Info, Warning, Error, Action, Promise, Custom. [You can customize the type of toast you want to render]
- **consider** (layout, react): Set where toasts appear with the Toaster position prop, using one of top-left, top-center, top-right, bottom-left, bottom-center or bottom-right. Why: These are the positions the page offers; its example uses bottom-right. Values: top-left, top-center, top-right, bottom-left, bottom-center, bottom-right, <Toaster position="bottom-right" />. [top-left top-center top-right bottom-left bottom-center bottom-right]
- **consider** (patterns, react): When choosing the toaster position, account for the swipe direction, because it changes with the position. [inferred] Why: The page says swipe direction changes depending on the position. [Swipe direction changes depending on the position.]
- **consider** (components, react): Control whether the toast pile is expanded with the Toaster expand prop; expand={false} is the default option. Why: The page's Expand section offers Expand and Default, and shows <Toaster expand={false} />. Values: <Toaster expand={false} />. [Expand Default]
- **consider** (components, react): Change how many toasts are visible with the visibleToasts prop. Why: The page says the amount of visible toasts is set through visibleToasts. Values: visibleToasts. [You can change the amount of toasts visible through the visibleToasts prop.]
- **consider** (color, react): Add the richColors prop to the Toaster when success, error, info and warning toasts should use rich colors, and call the typed function such as toast.success(). Why: The Other section demonstrates rich-color success, error, info and warning toasts with toast.success() and <Toaster richColors />. Values: <Toaster richColors />, toast.success('Event has been created'). [Rich Colors Success]
- **consider** (components, react): Use the Close Button option to add a close button to toasts, and the Headless option to render your own markup. Why: Close Button and Headless are listed as options in the Other section; that headless means your own unstyled markup comes from the toast page. [inferred] [Close Button Headless]

### Decisions it informs

- Where on the screen should toasts appear?
  - top-left: Toasts appear in the top-left corner; the swipe direction adapts to this position. When: When the top-left corner suits the layout.
  - top-center: Toasts appear centred at the top; the swipe direction adapts to this position. When: When the top centre suits the layout.
  - top-right: Toasts appear in the top-right corner; the swipe direction adapts to this position. When: When the top-right corner suits the layout.
  - bottom-left: Toasts appear in the bottom-left corner; the swipe direction adapts to this position. When: When the bottom-left corner suits the layout.
  - bottom-center: Toasts appear centred at the bottom; the swipe direction adapts to this position. When: When the bottom centre suits the layout.
  - bottom-right: Toasts appear in the bottom-right corner; the swipe direction adapts to this position. When: The page's code example uses this position.
  - Recommendation: The page does not recommend one position; its example uses bottom-right, and it notes that the swipe direction follows whichever position you pick.
- Should the toast pile stay in its default state or be expanded?
  - Default: expand={false}: the pile is not expanded by default. When: The default choice.
  - Expand: The toasts are shown expanded [inferred from the demo label]; how many are visible is set with visibleToasts. When: When the toasts should be expanded without the user doing anything. [inferred]
- Should typed toasts (success, error, info, warning) use rich colors?
  - Default colors: Typed toasts use the standard toast styling. When: When no richColors prop is set.
  - Rich colors: Success, error, info and warning toasts get rich, type-specific colors. When: Set <Toaster richColors /> and call typed functions such as toast.success().

### Process

1. Install: Run npm install sonner.
2. Render the toaster: Import { Toaster, toast } from 'sonner' and render <Toaster /> in the root of the app.
3. Fire toasts: Call toast('...') from an event handler, choose a type, and pass an options object as the second argument when needed.
4. Configure the toaster: Set position, expand, visibleToasts and richColors on <Toaster /> to control placement, stacking and colors.

### Examples and visual references

- 'Give me a toast' button (Sonner homepage usage example): A button whose onClick calls toast('My first toast') next to a <Toaster /> in the same component.
- Type demos (Sonner homepage, Types section): Buttons for Default, Description, Success, Info, Warning, Error, Action, Promise and Custom, each rendering that kind of toast, for example toast('Event has been created').
- Position demos (Sonner homepage, Position section): Buttons for the six positions, updating <Toaster position="..." />, which show where toasts appear and how the swipe direction changes.
- Expand vs Default demo (Sonner homepage, Expand section): A switch between an expanded pile and the default pile, shown with <Toaster expand={false} />.
- Rich colors, close button and headless demos (Sonner homepage, Other section): Buttons for rich-color success, error, info and warning toasts (toast.success('Event has been created') with <Toaster richColors />), plus Close Button and Headless variants.

<!-- /od:learn -->
