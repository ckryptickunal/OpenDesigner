---
type: source
title: "Other – Sonner"
created: 2026-09-27
updated: 2026-09-27
video_id: sonner-other
url: https://sonner.emilkowal.ski/other
channel: Sonner docs (web)
published: Unknown
authority: non-negotiable
tags:
  - sonner
  - toast
  - react
  - toast-lifecycle
  - dismiss
  - persist
  - astro
  - shadow-dom
---

# Other – Sonner

## Metadata

- Video ID: `sonner-other`
- Channel: Sonner docs (web)
- Published: Unknown
- URL: https://sonner.emilkowal.ski/other

## Summary

The Other page of the Sonner docs covers what you do with toasts after they appear. You can update a toast by calling toast() or a typed function such as toast.success() with its id, which changes only the properties you pass. The page separates onDismiss (the close button is clicked or the toast is swiped) from onAutoClose (the toast times out after its duration). It shows how to keep a toast forever with duration Infinity, dismiss one toast or all of them, read the visible toasts with the useSonner hook or toast.getActiveToasts(), and render links or components inside the title and description. It ends with fixes for Astro (import the stylesheet in a layout) and shadow DOM (copy Sonner's style tags into the shadow root). For a design system this defines the lifecycle rules of the house toast: update in place, persist on purpose, dismiss by id, and load the styles where the host needs them. [inferred]

## Key Ideas

- Update a toast in place by calling toast() again with its id; only the properties you pass change.
- Change a toast's type on update by calling toast.success(), toast.error() and so on with the same id.
- toast() returns the toast's id.
- onDismiss fires when the close button is clicked or the toast is swiped; onAutoClose fires when the toast disappears after its duration.
- A toast with duration Infinity never disappears on its own.
- toast.dismiss(id) removes one toast, and toast.dismiss() with no id removes them all.
- The useSonner hook returns all visible toasts, each with its id; outside React, toast.getActiveToasts() returns them.
- Titles and descriptions can render links or components when you pass a function instead of a string; headless gives more control.
- With Astro (including view transitions), import 'sonner/dist/styles.css' in a layout file.
- Sonner injects its styles into the document head, so shadow DOM needs them copied in by hand.

## Entities

- [[entities/sonner|Sonner]] (library): The React toast library whose update, dismiss and integration APIs this page documents.
- [[entities/usesonner|useSonner]] (concept): A React hook that returns all visible toasts.
- [[entities/toast-getactivetoasts|toast.getActiveToasts()]] (concept): A function that returns all toasts outside React.
- [[entities/astro|Astro]] (library): A web framework that needs Sonner's stylesheet imported in a layout, especially with view transitions.
- [[entities/shadow-dom|Shadow DOM]] (concept): An isolated DOM subtree that Sonner's head-injected styles do not reach.
- [[entities/animation-on-the-web-animations-dev|Animation on the Web (animations.dev)]] (product): The site linked in the custom-element example (link text 'Animation on the Web', https://animations.dev/); that it is the author's own course is [inferred].
- [[entities/aiforui-dev|aiforui.dev]] (product): A course promoted in the site-wide banner.

## Topics

- [[topics/toasts-and-notifications|Toasts and notifications]]: Covers updating, dismissing, persisting and reading toasts, close callbacks, custom elements, and Astro and shadow DOM integration.
- [[topics/gestures-and-drag|Gestures and drag]]: Swiping a toast dismisses it and fires onDismiss, like clicking the close button.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Shows the useSonner hook, toast.getActiveToasts() outside React, the Astro stylesheet import, and copying '[data-sonner-toaster]' style tags into a shadow root.

## Notable Claims

- Calling toast() with an existing toast's id updates that toast, changing only the properties passed. Evidence: Updating toasts
- Calling toast.success(), toast.error() and so on with an id changes the toast's type. Evidence: To change the type you can call toast.success() , toast.error() etc.
- onDismiss fires when the close button is clicked or the toast is swiped. Evidence: On Close Callback
- onAutoClose fires when the toast disappears automatically after its timeout (the duration prop). Evidence: On Close Callback
- Setting duration to Infinity keeps a toast on screen forever. Evidence: Persisting toasts
- toast() returns the id of the toast. Evidence: The toast() function returns the id of the toast.
- toast.dismiss() without an id dismisses all toasts. Evidence: You can also dismiss all toasts at once
- useSonner returns all visible toasts, and each includes its id. Evidence: useSonner
- toast.getActiveToasts() returns an array of all toasts and works outside React. Evidence: To get all toasts outside of React
- Passing a function instead of a string renders custom elements, for both the title and the description. Evidence: Rendering custom elements
- Sonner's styles are inserted into the document's head when the bundle loads, so they are not available in shadow DOM. Evidence: Shadow DOM support

## Quotes

> You then only change the properties you want to update.
> If you want a toast to never disappear, you can set the duration to Infinity
> Therefore these styles are not available in shadow DOM.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: The shadow DOM limitation is described as how things work 'at the moment', so it may change in later versions.
- Caveat: The custom-element example links to animations.dev ('Animation on the Web'), which is the author's own course [inferred]; treat it as self-promotion inside an otherwise neutral example.
- Caveat: The shadow DOM section links to more examples that are not in this text.
- Caveat: A site-wide banner promotes the author's aiforui.dev course with a countdown: self-promotion, time-sensitive.
- Caveat: The page's publish date is unknown, so the API may have changed since it was fetched.

### Rules and practices

- **should** (components, react): To change a toast that is already on screen, call toast() with its id and pass only the properties you want to change, instead of showing a new toast. [inferred] Why: Passing the id updates that toast, and only the properties you pass change; the rest stays the same. Values: toast('Toast has been updated', { id: toastId, }). [You then only change the properties you want to update.]
- **should** (components, react): Keep the id that toast() returns whenever you may need to update or dismiss that toast later. Why: The toast() function returns the id, and updating and dismissing both take it. Values: const toastId = toast('Sonner'). [The toast() function returns the id of the toast.]
- **should** (components, react): Change a toast's type on update by calling the typed function, such as toast.success() or toast.error(), with the same id. Why: This is how the docs change the type of an existing toast. Values: toast.success('Toast has been updated', { id: toastId, }). [To change the type you can call toast.success() , toast.error() etc.]
- **should** (components, react): Use onDismiss for user dismissal (the close button or a swipe) and onAutoClose for the toast timing out; do not treat them as the same event. Why: onDismiss fires when the close button is clicked or the toast is swiped, while onAutoClose fires when it disappears automatically after its duration. Values: onDismiss, onAutoClose. [On Close Callback]
- **consider** (components, react): To make a toast never disappear on its own, set its duration to Infinity. Why: The docs say that if you want a toast to never disappear, you can set the duration to Infinity. Values: duration: Infinity. [If you want a toast to never disappear, you can set the duration to Infinity]
- **should** (components, react): Remove a toast from code with toast.dismiss(id). Why: This is the documented way to remove a toast programmatically. Values: toast.dismiss(toastId). [To remove a toast programmatically use toast.dismiss(id)]
- **consider** (components, react): Call toast.dismiss() with no id to dismiss all toasts at once. Why: Without an id, dismiss removes every toast. Values: toast.dismiss(). [You can also dismiss all toasts at once by calling toast.dismiss() without an id.]
- **consider** (components, react): Inside React, read the visible toasts with the useSonner hook; each toast carries its id, so you can dismiss them one by one. Why: useSonner returns all visible toasts, each with its id, for example to delete them all. Values: const { toasts } = useSonner(), toasts.forEach((t) => toast.dismiss(t.id)). [You can use the useSonner hook to retrieve all visible toasts]
- **consider** (components, react): Outside React, get all toasts with toast.getActiveToasts(). Why: It returns an array of all toasts outside React. Values: toast.getActiveToasts(). [To get all toasts outside of React, you can use toast.getActiveToasts()]
- **consider** (content, react): To put a link or a component in a toast's title or description, pass a function that returns the JSX instead of a string. Why: Passing a function renders custom elements, for both the title and the description. Values: description: () => <button>This is a button element!</button>. [Rendering custom elements]
- **consider** (components, react): Use the headless approach when custom elements in the title and description do not give enough control. Why: The docs point to headless if you need more control. [If you need more control, see the headless approach.]
- **should** (platforms, web): In Astro projects that use view transitions, or that hit any other Sonner issue, import Sonner's stylesheet in a layout file. Why: The docs ask you to import Sonner's styles into a layout file if you use Astro with view transitions or run into any other Sonner issue with Astro. Values: import 'sonner/dist/styles.css'. [please import Sonner's styles into a layout file]
- **must** (platforms, web): When rendering Sonner inside shadow DOM, add Sonner's styles to the shadow root manually; one documented way is to copy the <style> elements in document.head whose text includes '[data-sonner-toaster]' into the shadow root. Why: Sonner's styles are inserted into the document's head when the bundle is loaded, so they are not available in shadow DOM; the docs say you need to add them to the shadow DOM manually. Values: [data-sonner-toaster], document.head.querySelectorAll('style'), shadow.append(styleEl). [To fix this you need to add the styles to the shadow DOM manually.]

### Decisions it informs

- Should a toast go away on its own or stay until it is dismissed?
  - Auto close: The toast disappears after its duration, and onAutoClose fires. When: The default behaviour.
  - Persist: With duration: Infinity the toast stays on screen until the user closes or swipes it (onDismiss) or code calls toast.dismiss(id). [inferred] When: When you want a toast to never disappear.
- When the status of an action changes, update the existing toast or show a new one?
  - Update in place: toast() or toast.success() with the same id changes only the passed properties or the type of the toast already on screen. When: When the toast refers to the same event, for example 'Toast has been updated'.
  - New toast: A separate toast is added to the pile. [inferred] When: When it is a different event. [inferred]

### Process

1. Keep the id: Store the id returned by toast(), for example const toastId = toast('Sonner').
2. Update: Call toast('...', { id: toastId }) to change only the properties you pass, or toast.success('...', { id: toastId }) to change the type.
3. React to closing: Pass onDismiss (close button or swipe) and onAutoClose (timed out after duration) callbacks where code must respond.
4. Dismiss: Call toast.dismiss(toastId) for one toast, or toast.dismiss() for all. Use useSonner() in React or toast.getActiveToasts() outside it to list the current toasts.
5. Fix styles in special hosts: In Astro, import 'sonner/dist/styles.css' in a layout file. In shadow DOM, loop over document.head style tags and append those containing '[data-sonner-toaster]' to the shadow root.

### Examples and visual references

- Close callbacks (Sonner docs, On Close Callback): Code only: toast('Event has been created', { onDismiss, onAutoClose }), where each callback logs the toast id with a different message.
- Link and button inside a toast (Sonner docs, Rendering custom elements): Code only: a title function rendering 'View' plus a link to 'Animation on the Web' (animations.dev) opening in a new tab, and a description function rendering a <button>.
- Remove all toasts with useSonner (Sonner docs, useSonner): Code only: removeAllToasts() loops over the hook's toasts and calls toast.dismiss(t.id) on each.
- Shadow DOM style copy (Sonner docs, Shadow DOM support): Code only: document.head.querySelectorAll('style').forEach(...) appends every style element whose text includes '[data-sonner-toaster]' to the shadow root.

### Numbers

- Infinity: duration value that keeps a toast on screen forever [Persisting toasts]

<!-- /od:learn -->
