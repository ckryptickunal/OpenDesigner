---
type: source
title: "Styling – Sonner"
created: 2026-09-27
updated: 2026-09-27
video_id: sonner-styling
url: https://sonner.emilkowal.ski/styling
channel: Sonner docs (web)
published: Unknown
authority: non-negotiable
tags:
  - sonner
  - toast
  - styling
  - headless
  - tailwind
  - classnames
  - icons
  - react
---

# Styling – Sonner

## Metadata

- Page ID: `sonner-styling`
- Publisher: Sonner docs (web)
- Published: Unknown
- URL: https://sonner.emilkowal.ski/styling

## Summary

The Styling page explains how to style Sonner beyond its default theme and ranks the approaches. Headless (no default styles, full control of the JSX, which also suits Tailwind) is the recommended approach, because people usually either keep the defaults or go fully custom. It also suggests wrapping toast() in your own function with props that fit your codebase. For small changes, such as a background color, toastOptions.style styles every toast, and the same style option styles a single toast. Per-element classNames need !important (including Tailwind's ! prefix), and unstyled removes all styles but gets messy, so it is only a compromise for a few changes. Icons can be replaced globally with the icons prop, set per toast with icon, or removed with null. For a design system this sets the house policy for toasts: keep the defaults or go headless, and avoid piling up overrides. [inferred]

## Key Ideas

- Headless (no default styles, full JSX control) is the recommended way to style Sonner, including with Tailwind.
- People usually either keep the defaults or go fully custom, which is why headless is recommended.
- Wrap toast() in your own function whose props fit your codebase.
- For small changes such as a background color, toastOptions.style on the Toaster styles every toast the same way.
- The same style option on a single toast() call styles just that toast.
- Class-based styling is best done through headless; per-element classNames need !important to beat the defaults.
- Tailwind classes in classNames must use the important modifier, for example !text-red-900.
- unstyled removes all styles so classes work without !important, but headless gives more control and a nicer developer experience.
- classNames overrides get messy quickly and are only a compromise for a few changes.
- Default icons (success, info, warning, error, loading) are replaced with the icons prop, set per toast with icon, or removed with null.

## Entities

- [[entities/sonner|Sonner]] (library): The React toast library whose styling options this page documents.
- [[entities/tailwind-css|Tailwind CSS]] (library): A utility CSS framework; its classes work in classNames only when marked important.
- [[entities/headless-toast|Headless toast]] (concept): The recommended styling approach: no default styles and full control of the JSX.
- [[entities/toastoptions|toastOptions]] (concept): A Toaster prop that applies the same style or classNames to every toast.
- [[entities/aiforui-dev|aiforui.dev]] (product): A course promoted in the site-wide banner.

## Topics

- [[topics/toasts-and-notifications|Toasts and notifications]]: How to restyle Sonner toasts: headless, global styles, per-element classNames, unstyled and icon changes.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Explains style objects, classNames with !important, Tailwind's ! modifier, the unstyled prop and wrapping toast() in your own function.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Recommends headless because people usually either use the defaults or go fully custom, and shows abstracting toast() into your own function with props that fit the codebase.
- [[topics/icons-and-imagery|Icons and imagery]]: Default success, info, warning, error and loading icons can be swapped globally, per toast, or removed with null.

## Notable Claims

- Headless is the recommended styling approach because people usually either use the defaults or go fully custom. Evidence: Headless / TailwindCSS
- The toast() function can be abstracted to accept different props that better fit your codebase. Evidence: You can also abstract the toast() function
- Using the toastOptions prop gives every toast the same styling. Evidence: Global styles
- The preferred way to style toasts with classes is the headless approach. Evidence: Styling specific elements
- Classes applied to toast elements through classNames need !important to override the default styles. Evidence: You will need to use !important in order to override the default styles.
- The unstyled prop removes all styles so your own styles apply without !important, but headless gives more control and a nicer developer experience. Evidence: You can also use the unstyled prop
- Styling through classNames can get messy quickly but is a good compromise for a few changes. Evidence: This can get quite messy quickly
- Default icons can be changed with the icons prop, set per toast with icon, or removed by passing null. Evidence: Changing Icons

## Quotes

> people usually either use the defaults or go fully custom.
> You will need to use !important in order to override the default styles.
> using headless will provide more control and a nicer developer experience.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: The headless example was a live preview, and its code did not survive text extraction ('Cop y ied Code'), so this page does not show the headless call itself.
- Caveat: The background: 'red' and '!text-red-900' values are illustrations of the technique, not recommended colors.
- Caveat: A site-wide banner promotes the author's aiforui.dev course with a countdown: self-promotion, time-sensitive.
- Caveat: The page's publish date is unknown, so the API may have changed since it was fetched.

### Rules and practices

- **should** (components, react): Style toasts beyond the default theme with the headless approach: no default styles and full control of the JSX (this is also the route for Tailwind). Why: It is the recommended approach, as people usually either use the defaults or go fully custom. [This is the recommended approach as people usually either use the defaults or go fully custom.]
- **should** (process, react): Either keep Sonner's default look or go fully custom with headless; do not settle in between unless the change is small. [inferred] Why: People usually either use the defaults or go fully custom, and the in-between options get messy quickly. [people usually either use the defaults or go fully custom]
- **consider** (components, react): Wrap toast() in your own function that accepts the props your codebase needs, instead of calling Sonner directly everywhere. [inferred] Why: The page says you can abstract the toast() function to accept different props that fit your codebase's needs better. [You can also abstract the toast() function]
- **should** (components, react): For small changes such as the background color, set style in the Toaster's toastOptions so every toast gets the same styling. Why: toastOptions applies the same styling to every toast. Values: toastOptions={{ style: { background: 'red', }, }}. [If you only need to make smaller changes like changing the background color, you can use the toastOptions prop.]
- **consider** (components, react): To style one specific toast, pass style in that toast() call's options. Why: The same props used in toastOptions also work when calling toast. Values: toast('Hello World', { style: { background: 'red', }, }). [You can also use the same props when calling toast to style a specific toast.]
- **should** (components, react): Prefer the headless approach when styling toasts with classes. Why: The page calls headless the preferred way to style the toasts with classes. [The preferred way to style the toasts with classes is through the headless approach.]
- **must** (components, css): When you only need to change a few things with classes, target the toast's elements through toastOptions.classNames (toast, title, description, actionButton, cancelButton, closeButton) and mark those styles !important. Why: You will need to use !important in order to override the default styles. Values: toast, title, description, actionButton, cancelButton, closeButton, !important. [Styling specific elements]
- **must** (components, css): When using Tailwind classes in classNames, mark each one important with the ! prefix. Why: This makes sure the styles are applied correctly over the defaults. Values: '!text-red-900'. [you need to mark them as !important]
- **consider** (components, react): Use unstyled: true with classNames to drop all default styles and style without !important, only for a few changes; beyond that, switch to headless. Why: unstyled removes all styles, but at that point headless provides more control and a nicer developer experience; the approach gets messy quickly and is only a good compromise for a few changes. Values: unstyled: true. [You can also use the unstyled prop]
- **should** (components, react): Do not pile up many classNames or unstyled overrides; move to headless once the changes stop being small. Why: This can get quite messy quickly; it is only a good compromise as long as it is just a few changes. [This can get quite messy quickly]
- **consider** (components, react): Replace the default toast icons for the whole app with the Toaster's icons prop (success, info, warning, error, loading). Why: The icons prop changes the default icons. Values: success, info, warning, error, loading. [Changing Icons]
- **consider** (components, react): Set a different icon on a single toast with the icon option. Why: You can set an icon for each toast. Values: icon: <Icon />. [You can also set an icon for each toast]
- **consider** (components, react): Remove an icon by passing null: icon: null on one toast, or icons={{ success: null }} on the Toaster for every toast of that type. Why: Passing null removes the icon completely. Values: icon: null, icons={{ success: null, }}. [Or remove the icon completely by passing null]

### Decisions it informs

- How should toasts be styled to match the design system?
  - Keep the defaults: Sonner's default theme, with no styling work. When: When the default look fits; the page notes people usually either use the defaults or go fully custom.
  - Global styles (toastOptions.style): Every toast gets the same small change, such as a background color. When: For smaller changes like the background color.
  - Per-element classNames with !important: Classes on toast, title, description and the buttons override the defaults; Tailwind classes need the ! prefix. When: When only a few things need to change; it gets messy quickly.
  - unstyled with classNames: All default styles are removed, so classes apply without !important. When: A compromise for a few changes; headless gives more control.
  - Headless: No default styles and full control of the JSX, with Sonner's behaviour kept. When: When going fully custom, including with Tailwind; this is the recommended approach.
  - Recommendation: Headless, because people usually either keep the defaults or go fully custom, and headless gives more control and a nicer developer experience than stacking overrides.
- Which icons should toasts show?
  - Default icons: Sonner's built-in success, info, warning, error and loading icons. When: When no icons prop is set.
  - Custom icon set: The Toaster's icons prop swaps each default icon for your own components. When: When the design system has its own icons. [inferred]
  - Per-toast icon: A single toast shows a different icon through icon. When: When one toast needs a special icon.
  - No icon: Passing null removes the icon from one toast or from every toast of a type. When: When the icon should be removed completely.

### Process

1. Decide defaults or custom: If the default look fits, keep it. If not, the recommended path is headless: no default styles and full control of the JSX.
2. Abstract toast(): Wrap toast() in your own function whose props fit your codebase.
3. Small global tweak: For a small change such as the background, set style in the Toaster's toastOptions; use style in a toast() call for one toast.
4. Few element tweaks: Set toastOptions.classNames for toast, title, description, actionButton, cancelButton and closeButton with !important (Tailwind: the ! prefix), or use unstyled: true to drop the defaults. Switch to headless if the list grows.
5. Icons: Swap icons globally with the icons prop, per toast with icon, or remove them with null.

### Examples and visual references

- Global red background (Sonner docs, Global styles): Code only: <Toaster toastOptions={{ style: { background: 'red' } }} /> gives every toast the same background; 'red' is only an example value.
- Element class map (Sonner docs, Styling specific elements): Code only: classNames keys toast, title, description, actionButton, cancelButton and closeButton, each mapped to a class.
- Tailwind override (Sonner docs, Styling specific elements): Code only: classNames: { description: '!text-red-900' }, showing Tailwind's important modifier.
- Custom icon set (Sonner docs, Changing Icons): Code only: icons={{ success: <SuccessIcon />, info: <InfoIcon />, warning: <WarningIcon />, error: <ErrorIcon />, loading: <LoadingIcon /> }}.

<!-- /od:learn -->
