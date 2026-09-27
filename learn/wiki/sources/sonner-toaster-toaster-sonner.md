---
type: source
title: "Toaster – Sonner"
created: 2026-09-27
updated: 2026-09-27
video_id: sonner-toaster
url: https://sonner.emilkowal.ski/toaster
channel: Sonner docs (web)
published: Unknown
authority: non-negotiable
tags:
  - sonner
  - toaster
  - react
  - toast-position
  - toast-offset
  - dark-mode
  - next-themes
  - api-defaults
---

# Toaster – Sonner

## Metadata

- Video ID: `sonner-toaster`
- Channel: Sonner docs (web)
- Published: Unknown
- URL: https://sonner.emilkowal.ski/toaster

## Summary

The Toaster page documents the component that renders all toasts and can be placed anywhere in the app. It explains that toasts expand on hover, that expand makes that the default, and that visibleToasts changes how many are shown (default 3). It covers the six positions, multiple toasters routed with id and toasterId, and spacing from the screen edge: offset defaults to 32px on desktop and mobileOffset to 16px below a 600px screen width. It also shows how to make the toaster follow the app's light or dark theme through next-themes. The API table lists the container defaults: theme light, richColors false, expand false, visibleToasts 3, position bottom-right, closeButton false, gap 14, dir ltr and hotkey ⌥/alt + T.

## Key Ideas

- Toaster renders every toast and can be placed anywhere in the app.
- Hovering one toast expands the pile; expand makes the expanded state the default.
- Three toasts are visible by default; visibleToasts changes that number.
- Six positions are available, and bottom-right is the default.
- Several toasters can coexist when you need a clear separation; each has an id and toasts pick one with toasterId.
- Toasts sit 32px from the screen edge on desktop and 16px on mobile by default.
- mobileOffset applies when the screen is narrower than 600px.
- offset and mobileOffset accept a number, a string such as 10vh, or an object of individual sides.
- The toaster's theme defaults to light; pass the resolved app theme (for example from next-themes) to follow dark mode.
- Swipe directions are derived from the position unless swipeDirections is set.
- Other container defaults: gap 14, dir ltr, hotkey ⌥/alt + T, richColors false, closeButton false, invert false.

## Entities

- [[entities/sonner|Sonner]] (library): The React toast library whose Toaster component this page documents.
- [[entities/toaster|Toaster]] (concept): The component that renders all toasts and holds container settings such as position, offsets and theme.
- [[entities/next-themes|next-themes]] (library): A theme provider whose resolvedTheme is passed to Toaster so toasts follow the app theme.
- [[entities/react|React]] (library): The framework Sonner is built for.
- [[entities/aiforui-dev|aiforui.dev]] (product): A course promoted in the site-wide banner.

## Topics

- [[topics/toasts-and-notifications|Toasts and notifications]]: Documents the Toaster container: expand on hover, visible count, positions, multiple toasters, offsets, theme and all container defaults.
- [[topics/spacing-and-layout|Spacing and layout]]: Toasts sit 32px from the screen edge on desktop and 16px on mobile, with mobile applying below a 600px screen width; offsets can be set per side.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: The toaster's theme defaults to light; pass resolvedTheme from a theme provider such as next-themes so toasts follow the app theme.
- [[topics/gestures-and-drag|Gestures and drag]]: Swipe directions default to being based on the position and can be set with swipeDirections.
- [[topics/accessibility|Accessibility]]: The API lists a keyboard hotkey (default ⌥/alt + T) and a dir setting (default ltr).
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Shows the React props, a 'use client' Toaster wrapper using next-themes, and offsets as numbers, strings or per-side objects.

## Notable Claims

- Toaster renders all the toasts and can be placed anywhere in the app. Evidence: This component renders all the toasts
- Hovering one of the toasts expands them; setting expand to true makes that the default behaviour. Evidence: When you hover on one of the toasts, they will expand.
- By default 3 toasts are visible. Evidence: 9 toasts will be visible instead of the default, which is 3.
- The available positions are top-left, top-center, top-right, bottom-left, bottom-center and bottom-right. Evidence: Available positions
- Multiple toasters can be rendered, and a toast can be pointed to a specific toaster. Evidence: Multiple Toasters
- The default desktop offset is 32px and the default mobile offset is 16px. Evidence: Customizing offsets
- mobileOffset is applied when the screen width is less than 600px. Evidence: mobileOffset will be applied when the screen width is less than 600px
- The toaster's theme can adapt to the app's theme by passing a theme prop from a theme provider such as next-themes. Evidence: Dynamic theme
- The theme prop defaults to light. Evidence: theme string light
- swipeDirections defaults to being based on position. Evidence: swipeDirections [] based on position
- The default gap is 14. Evidence: gap number 14

## Quotes

> This component renders all the toasts, you can place it anywhere in your app.
> When you hover on one of the toasts, they will expand.
> mobileOffset will be applied when the screen width is less than 600px

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: The API table lists toastOptions with a default of 4000, which looks like a documentation slip, since toastOptions is an object and 4000 is the toast duration default. [inferred]
- Caveat: The page does not state the unit for gap (14), and it does not say what the hotkey does.
- Caveat: The page says you can see examples on the homepage, but those interactive demos are not in this text.
- Caveat: A site-wide banner promotes the author's aiforui.dev course with a countdown: self-promotion, time-sensitive.
- Caveat: The page's publish date is unknown, so the API may have changed since it was fetched.

### Rules and practices

- **should** (components, react): Render the <Toaster /> component to display toasts; it can be placed anywhere in the app. Why: This component renders all the toasts. [This component renders all the toasts, you can place it anywhere in your app.]
- **consider** (components, react): Toasts expand when the user hovers one of them; set the expand prop to true to make the expanded state the default (expand is false by default). Why: When you hover on one of the toasts they expand, and setting expand to true makes that the default behaviour; the API table lists expand as false by default. Values: expand, false. [You can make that the default behavior by setting the expand prop to true]
- **should** (components, react): Visible toasts default to 3; change the count with the visibleToasts prop (the example uses 9). Why: The default number of visible toasts is 3; visibleToasts customizes it. Values: 3, <Toaster expand visibleToasts={9} />. [9 toasts will be visible instead of the default, which is 3.]
- **should** (layout, react): Place toasts with the position prop, choosing top-left, top-center, top-right, bottom-left, bottom-center or bottom-right; the default is bottom-right. Why: Position changes where all toasts are rendered; the API table lists bottom-right as the default. Values: top-left, top-center, top-right, bottom-left, bottom-center, bottom-right, <Toaster position="top-center" />. [Changes the place where all toasts will be rendered.]
- **consider** (components, react): Render more than one Toaster only when you need a clear separation; give each an id and send each toast to one with toasterId. Why: Multiple toasters are for when you need this clear separation, and they let you point a toast to a specific toaster. Values: <Toaster id="global" position="top-right" />, <Toaster id="canvas" position="bottom-left" />, toast('Global toast', { toasterId: 'global' }), toast('Canvas toast', { toasterId: 'canvas' }). [Multiple Toasters]
- **should** (layout, react): Offsets default to 32px on desktop and 16px on mobile; change them with the offset and mobileOffset props. Why: The docs give a default desktop offset of 32px and a default mobile offset of 16px, both customizable through offset and mobileOffset. Values: 32px, 16px. [Default desktop offset is 32px and default mobile offset is 16px]
- **should** (layout, web): Set mobile spacing with mobileOffset, which applies when the screen width is less than 600px. Why: mobileOffset is applied below a 600px screen width. Values: 600px. [mobileOffset will be applied when the screen width is less than 600px]
- **consider** (layout, react): Give offset a number for the same spacing on all sides, a string such as "10vh" for relative units, or an object to set individual sides. Why: The page shows all three forms of offset. Values: <Toaster offset={16} />, <Toaster offset="10vh" />, <Toaster offset={{ bottom: '24px', right: "16px", left: "16px" }} />. [Customizing offsets]
- **consider** (layout, react): To change only some mobile sides, pass mobileOffset an object with just those sides; the rest keep their default values. Why: The example sets only bottom and says the rest use default values. Values: <Toaster mobileOffset={{ bottom: '16px' }} />. [mobile offset will be 16px from the bottom, default values for the rest]
- **should** (color, react): Make the toaster follow the app's theme by wrapping it in a 'use client' component that passes the theme provider's resolvedTheme (for example from next-themes) to the theme prop. Why: This makes the toaster's theme adapt to the app's theme; theme otherwise defaults to light, so dark-mode apps would show light toasts. [inferred] Values: 'use client', theme={resolvedTheme as ToasterProps['theme']}, light. [Dynamic theme]
- **consider** (patterns, react): Let swipe directions follow the toaster's position (the default), and set swipeDirections only to override them. Why: The API table lists swipeDirections with a default that is based on position. Values: swipeDirections. [swipeDirections [] based on position]
- **consider** (color, react): Turn on richColors on the Toaster when typed toasts should use rich colors; it is false by default. Why: The API table lists richColors as a boolean defaulting to false. Values: false. [richColors boolean false]
- **consider** (components, react): Turn on closeButton on the Toaster to show close buttons; it is false by default. Why: The API table lists closeButton as a boolean defaulting to false. Values: false. [closeButton boolean false]
- **consider** (accessibility, react): Set the dir prop for right-to-left interfaces; it defaults to ltr. [inferred] Why: The API table lists dir as a string defaulting to ltr. Values: ltr. [dir string ltr]
- **consider** (accessibility, react): Set the toaster's keyboard shortcut with the hotkey prop; the default is ⌥/alt + T. Why: The API table lists hotkey with the default ⌥/alt + T. Values: ⌥/alt + T. [hotkey string ⌥/alt + T]
- **consider** (layout, react): Space the toasts with the gap prop, which defaults to 14. [inferred] Why: The API table lists gap as a number defaulting to 14; the page does not describe what it spaces or its unit. Values: 14. [gap number 14]
- **consider** (components, react): Set shared per-toast defaults through toastOptions and default icons through icons on the Toaster. Why: The API table lists toastOptions and icons as Toaster props. Values: toastOptions, icons. [toastOptions object]
- **consider** (color, react): Leave invert at its default of false unless toasts should be inverted. Why: The API table lists invert as a boolean defaulting to false; the page does not describe the inverted look. Values: false. [invert boolean false]

### Decisions it informs

- Should the toast pile expand only on hover, or stay expanded?
  - Expand on hover (default): The toasts expand when the user hovers one of them. When: Default: expand is false.
  - Always expanded: The expanded state becomes the default; combine with visibleToasts to show more than 3. When: When every visible toast should be expanded without hovering.
- Where should the toaster sit on screen?
  - top-left: All toasts render at the top left. When: When the layout calls for it.
  - top-center: All toasts render centred at the top. When: The page's code example uses this position.
  - top-right: All toasts render at the top right. When: When the layout calls for it; the multiple-toasters example puts its 'global' toaster here.
  - bottom-left: All toasts render at the bottom left. When: When the layout calls for it; the multiple-toasters example puts its 'canvas' toaster here.
  - bottom-center: All toasts render centred at the bottom. When: When the layout calls for it.
  - bottom-right: All toasts render at the bottom right. When: The default.
- One toaster for the whole app, or several?
  - One toaster: All toasts appear in a single place. When: When no separation between kinds of toasts is needed. [inferred]
  - Multiple toasters: Each Toaster has an id and position, and toasts are routed with toasterId, for example a 'global' toaster top-right and a 'canvas' toaster bottom-left. When: When you need this clear separation.
  - Recommendation: Render multiple toasters only if you need the clear separation.
- Should toasts use a fixed theme or follow the app's theme?
  - Fixed light (default): The toaster uses the light theme regardless of the app. When: Default when no theme prop is passed.
  - Follow the app theme: The toaster adapts to the app's theme using the resolved theme from a provider such as next-themes. When: When the app has a theme provider.
- Should toasts show a close button?
  - No close button (default): Toasts render without a close button; closeButton is false. When: Default when closeButton is not set.
  - Close button: Every toast from this Toaster shows a close button. When: Set closeButton on the Toaster; clicking it fires onDismiss (Other page). [inferred]

### Process

1. Mount the toaster: Render <Toaster /> anywhere in the app; it renders all toasts.
2. Set placement and spacing: Choose a position, and adjust offset (default 32px) and mobileOffset (default 16px, applied below 600px) as a number, a string or a per-side object if the defaults do not fit.
3. Wire the theme: Create a 'use client' Toaster wrapper that reads resolvedTheme from useTheme() (next-themes) and passes it to Sonner's Toaster as theme={resolvedTheme as ToasterProps['theme']}.
4. Separate toasters if needed: Render additional <Toaster id="..." position="..." /> instances and pass toasterId in toast() options to route each toast.

### Examples and visual references

- Global and canvas toasters (Sonner docs, Multiple Toasters): A 'global' toaster top-right and a 'canvas' toaster bottom-left, with buttons that send toasts to each through toasterId.
- Offset variations (Sonner docs, Customizing offsets): offset={16} (16px on all sides), offset="10vh" (10vh on all sides), a per-side object of 24px bottom and 16px right and left, and mobileOffset={{ bottom: '16px' }}.
- Theme-aware Toaster wrapper (Sonner docs, Dynamic theme (next-themes)): A client component that imports Toaster as SonnerToaster and ToasterProps from 'sonner', and useTheme from 'next-themes', then passes resolvedTheme to the theme prop.
- Expanded pile with 9 visible toasts (Sonner docs, Expand): <Toaster expand visibleToasts={9} /> shows 9 toasts instead of the default 3.

### Numbers

- 3: Default number of visible toasts (visibleToasts) [the default, which is 3]
- 9: Example visibleToasts value [9 toasts will be visible instead of the default]
- 32px: Default desktop offset from the screen edge [Default desktop offset is 32px]
- 16px: Default mobile offset from the screen edge [default mobile offset is 16px]
- 600px: Screen width below which mobileOffset applies [less than 600px]
- 10vh: Example string offset applied to all sides [all sides will have 10vh offset]
- 24px: Example bottom offset in a per-side offset object [24px from the bottom, 16px from the right and left]
- 14: Default gap (unit not stated) [API Reference: gap number 14]
- ⌥/alt + T: Default toaster hotkey [API Reference: hotkey]
- light: Default toaster theme [API Reference: theme string light]
- ltr: Default dir [API Reference: dir string ltr]
- bottom-right: Default toaster position [API Reference: position string bottom-right]

<!-- /od:learn -->
