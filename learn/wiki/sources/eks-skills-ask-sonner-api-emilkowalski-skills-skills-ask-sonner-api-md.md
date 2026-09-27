---
type: source
title: "emilkowalski/skills: skills/ask-sonner/API.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-ask-sonner-api
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/ask-sonner/API.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - sonner
  - toast
  - notifications
  - react
  - api-reference
  - defaults
  - headless
  - swipe-to-dismiss
  - accessibility
  - theming
---

# emilkowalski/skills: skills/ask-sonner/API.md

## Metadata

- Page ID: `eks-skills-ask-sonner-api`
- Publisher: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/ask-sonner/API.md

## Summary

This is the exact API reference for Sonner, the React toast library, taken from the ask-sonner skill in the emilkowalski/skills repository. It lists every prop of the <Toaster /> component and every option of the toast() function, with types and defaults, plus the helper functions for typed, loading, promise, custom and dismissed toasts. The defaults form a concrete, value-level spec for a notification component: 3 visible toasts, bottom-right placement, a 32px screen offset (16px under 600px wide), a 14 gap when expanded, 4000 ms auto-close, an Alt+T hotkey and a 'Notifications' ARIA label. It also defines the override model (per-toast options beat Toaster-wide toastOptions) and how update-by-id, headless rendering and multiple toasters work. For a design system it gives the exact knobs a toast component should expose and the default values to start from.

## Key Ideas

- Options passed to a single toast() call override the same options set on the Toaster through toastOptions.
- The <Toaster /> holds global behavior: theme, position, offsets, number of visible toasts, gap, hotkey, icons and default toast options.
- toast() returns the toast's id, and calling toast() again with the same id updates that toast instead of adding a new one.
- A toast auto-closes after 4000 ms by default; duration Infinity keeps it on screen.
- By default toasts expand on hover; expand: true shows them expanded by default.
- Only 3 toasts are visible at once by default.
- Offsets differ by screen size: 32px from the edges normally, 16px when the screen is narrower than 600px, and each side can be set separately.
- Swipe-to-dismiss directions follow the toaster's position unless swipeDirections overrides them.
- Keyboard and ARIA hooks come with defaults: the ⌥/alt + T hotkey focuses the toaster area and the container's ARIA label is 'Notifications'.
- Status toasts (success, error, info, warning) get matching icons; richColors makes success and error more colorful.
- Clicking the action button closes the toast unless its onClick calls event.preventDefault(); clicking the secondary cancel button closes the toast.
- Class names on toast parts need !important unless the toast is unstyled.
- toast.custom() is headless: your JSX with Sonner's behavior.
- onDismiss (close button or swipe) and onAutoClose (duration ran out) are separate callbacks.
- Several toasters can coexist: each gets an id, and toasterId sends a toast to one of them.
- toast(message, options) takes a string, JSX, or a function returning JSX as the message, and returns the toast's id.
- Setting an icon to null removes it, per type in the Toaster's icons object or per toast with icon.

## Entities

- [[entities/sonner|Sonner]] (library): React toast library whose props, options and defaults this reference lists.
- [[entities/emil-kowalski|Emil Kowalski]] (person): Owner of the emilkowalski/skills repository this file comes from; author of Sonner [inferred: stated in the sibling ask-sonner SKILL.md, not in this file].
- [[entities/toaster|<Toaster />]] (concept): The single mounted component that sets global toast behavior and renders toasts.
- [[entities/toast|toast()]] (concept): The function that creates, types, updates and dismisses toasts and returns a toast id.
- [[entities/usesonner|useSonner()]] (concept): React hook that returns the list of active toasts.
- [[entities/emilkowalski-skills|emilkowalski/skills]] (product): MIT-licensed GitHub repository of agent skills; this is skills/ask-sonner/API.md at commit 85e8e23.

## Topics

- [[topics/toasts-and-notifications|Toasts and notifications]]: Full prop and option list for a toast system, with defaults for count, placement, offsets, gap, duration, dismissal, actions and callbacks.
- [[topics/ui-libraries|UI libraries]]: Reference API of Sonner, the React toast library, including headless rendering via toast.custom().
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: React props and functions, class names per toast part that need !important unless unstyled, inline style objects, data-testid output for e2e tests, and toast.getActiveToasts() for code outside React.
- [[topics/accessibility|Accessibility]]: Alt+T hotkey focuses the toaster area; the container ARIA label defaults to 'Notifications'; dir supports text direction; dismissible controls whether the user can close a toast.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: theme accepts 'light', 'dark' or 'system' and defaults to 'light'; invert gives dark toasts in light mode and the reverse.
- [[topics/gestures-and-drag|Gestures and drag]]: Swipe-to-dismiss directions default to ones based on position and can be overridden with swipeDirections; onDismiss fires when a toast is swiped away.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: toast.loading shows a spinner and is updated by id; toast.promise moves from loading to success or error when the promise settles.
- [[topics/spacing-and-layout|Spacing and layout]]: Six positions, a 32px edge offset, a 16px mobile offset under 600px, per-side offset objects, and a 14 gap between expanded toasts.

## Notable Claims

- Options passed to toast() override the same options set via the Toaster's toastOptions. Evidence: Options passed to `toast()` override the same options set via the Toaster's `toastOptions`
- The Toaster's theme defaults to 'light'. Evidence: `theme` | `string` | `'light'`
- By default toasts are collapsed and expand on hover; expand: true keeps them expanded. Evidence: Toasts expanded by default (otherwise they expand on hover)
- Three toasts are visible by default. Evidence: `visibleToasts` | `number` | `3`
- The default position is bottom-right, out of six positions. Evidence: `top-left`, `top-center`, `top-right`, `bottom-left`, `bottom-center`, `bottom-right`
- The default offset from screen edges is 32px, and the object form sets each side separately. Evidence: Offset from screen edges. Object form is per-side
- mobileOffset applies when the screen is narrower than 600px and defaults to 16px. Evidence: Offset when screen width < 600px
- Allowed swipe-to-dismiss directions are based on position by default. Evidence: `swipeDirections` | `array` | based on position
- The keyboard shortcut Alt+T focuses the toaster area by default. Evidence: Keyboard shortcut that focuses the toaster area
- The gap between expanded toasts defaults to 14. Evidence: Gap between toasts when expanded
- Setting an icon to null removes it, either in the Toaster's icons object or in a toast's icon option. Evidence: `null` removes one
- Toasts auto-close after 4000 milliseconds by default and Infinity keeps them on screen. Evidence: Milliseconds before auto-close. `Infinity` persists the toast.
- With dismissible: false the user cannot dismiss the toast. Evidence: If `false`, the user cannot dismiss the toast.
- Clicking the action button closes the toast unless onClick calls event.preventDefault(). Evidence: Primary button; clicking closes the toast unless
- Calling toast() again with the same custom id updates the existing toast. Evidence: calling `toast()` again with the same id updates the existing toast
- classNames on toast parts need !important unless the toast is unstyled. Evidence: Needs `!important` unless `unstyled`.
- onDismiss fires on the close button or a swipe; onAutoClose fires when the duration runs out. Evidence: Fires when the close button is clicked or the toast is swiped away.
- The container's ARIA label defaults to 'Notifications'. Evidence: ARIA label for the toast container.
- toast.dismiss() without an id dismisses all toasts. Evidence: Dismiss one toast, or all when called without an id.
- toast.getActiveToasts() works outside React. Evidence: All active toasts, usable outside React.
- toast.custom() renders your JSX with Sonner's behavior (headless). Evidence: Headless toast — your JSX, Sonner's behavior.
- toast() accepts a string, JSX, or a function returning JSX as its message and returns the toast's id. Evidence: message is a string, JSX, or a function returning JSX. Returns the toast's id
- A single toast can set its own position through toast()'s position option, which defaults to 'bottom-right'. Evidence: Position of this toast.
- toast.promise's success and error accept strings, JSX, functions of the result, or objects of toast options. Evidence: `success`/`error` accept strings, JSX, functions of the result, or objects of toast options
- useSonner() is a React hook that returns { toasts }. Evidence: React hook returning `{ toasts }`

## Quotes

> Options passed to `toast()` override the same options set via the Toaster's `toastOptions`.
> Headless toast — your JSX, Sonner's behavior.
> calling `toast()` again with the same id updates the existing toast.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is a library reference pinned to commit 85e8e23 of emilkowalski/skills; defaults and prop names can change in later Sonner versions.
- Caveat: It documents React-specific APIs; the values carry over to other platforms only as design defaults, not as code.
- Caveat: The source lists defaults without saying why they were chosen; rules that adopt them as house defaults are marked [inferred].
- Caveat: Units are given as written: offsets are CSS strings ('32px', '16px') while gap is a bare number (14).

### Rules and practices

- **should** (components, react): Put app-wide toast defaults in the Toaster's toastOptions and override them per toast() call; per-call options win over toastOptions. Why: Options passed to toast() override the same options set via the Toaster's toastOptions. Values: toastOptions. [Options passed to `toast()` override the same options set via the Toaster's `toastOptions`]
- **consider** (color, react): Set the Toaster's theme to 'light', 'dark' or 'system'; it defaults to 'light'. Why: The API reference lists theme as 'light', 'dark' or 'system' with 'light' as the default; it states no recommendation (the dark-mode fix is a rule in the sibling SKILL.md). Values: 'light', 'dark', 'system', default 'light'. [`theme` | `string` | `'light'` | `'light'`, `'dark'`, or `'system'`]
- **consider** (color, react): Turn on richColors when success and error toasts must read as colored states rather than neutral ones. Why: richColors makes error and success states more colorful; it is off by default. Values: richColors: false (default). [Makes error and success states more colorful.]
- **consider** (components, react): Set expand on the Toaster to show toasts expanded by default; left at its default (false), toasts expand on hover. Why: The API reference documents expand as a boolean defaulting to false: toasts expanded by default, otherwise they expand on hover. It states no recommendation. Values: expand: false (default). [Toasts expanded by default (otherwise they expand on hover)]
- **should** (components, all): Show at most 3 toasts at once by default (visibleToasts). Why: Sonner's documented default amount of visible toasts is 3 [inferred: adopted as house default]. Values: visibleToasts: 3. [Amount of visible toasts.]
- **should** (layout, web): Place toasts bottom-right by default, choosing only from top-left, top-center, top-right, bottom-left, bottom-center or bottom-right. Why: bottom-right is the documented default position and these are the six supported positions [inferred: adopted as house default]. Values: 'bottom-right', top-left, top-center, top-right, bottom-left, bottom-center. [`position` | `string` | `'bottom-right'`]
- **should** (layout, web): Offset the toaster 32px from the screen edges on desktop. Why: The default offset from screen edges is '32px' [inferred: adopted as house default]. Values: offset: '32px'. [Offset from screen edges.]
- **should** (layout, web): Use a smaller 16px edge offset when the screen is narrower than 600px (mobileOffset). Why: mobileOffset is the offset used when screen width < 600px and defaults to '16px' [inferred: adopted as house default]. Values: mobileOffset: '16px', < 600px. [Offset when screen width < 600px.]
- **consider** (layout, react): When one edge needs a different distance, pass the offset as a per-side object instead of a single value. Why: The object form of offset is per-side. Values: { bottom: '24px', right: '16px' }. [Object form is per-side]
- **should** (motion, react): Let swipe-to-dismiss directions follow the toaster position, and set swipeDirections only when they must differ. Why: swipeDirections defaults to directions based on position [inferred: adopted as house default]. Values: swipeDirections: based on position. [Allowed swipe-to-dismiss directions.]
- **consider** (accessibility, react): Set dir to match the app's text direction (default 'ltr') [inferred]. Why: dir controls text directionality and defaults to 'ltr'. Values: dir: 'ltr'. [Text directionality.]
- **should** (accessibility, web): Keep a keyboard shortcut that moves focus to the toaster area, Alt+T by default. Why: hotkey is the keyboard shortcut that focuses the toaster area, default ⌥/alt + T [keeping it enabled is inferred]. Values: ⌥/alt + T. [Keyboard shortcut that focuses the toaster area.]
- **consider** (color, react): Use invert (Toaster-wide or per toast) to show dark toasts in light mode and light toasts in dark mode. Why: invert gives dark toasts in light mode and vice versa; default false. Values: invert: false (default). [Dark toasts in light mode and vice versa.]
- **should** (layout, react): Space expanded toasts with a gap of 14 by default. Why: gap is the gap between toasts when expanded and defaults to 14 [inferred: adopted as house default]. Values: gap: 14. [Gap between toasts when expanded.]
- **consider** (components, react): Replace status icons for the whole system through the Toaster's icons object (success, info, warning, error, loading), and use null to remove one. Why: icons replaces default icons per type; null removes one. Values: { success, info, warning, error, loading }, null. [Replace default icons]
- **consider** (components, react): Add a close button to all toasts with closeButton on the Toaster, or to one toast with closeButton in toast(); it is off by default. Why: closeButton adds a close button and defaults to false at both levels. Values: closeButton: false (default). [Adds a close button to all toasts.]
- **should** (motion, all): Auto-close toasts after 4000 ms by default. Why: duration is the milliseconds before auto-close and defaults to 4000 [inferred: adopted as house default]. Values: duration: 4000. [Milliseconds before auto-close.]
- **consider** (components, react): Use duration: Infinity to keep a toast on screen until it is dismissed. Why: Infinity persists the toast. Values: Infinity. [`Infinity` persists the toast.]
- **should** (accessibility, react): Leave toasts dismissible by the user; set dismissible: false only when the user must not be able to close it. Why: dismissible defaults to true; if false, the user cannot dismiss the toast [inferred: keeping the default as house default]. Values: dismissible: true (default). [If `false`, the user cannot dismiss the toast.]
- **consider** (components, react): Pass icon: null on a toast to remove its default icon, or a ReactNode to replace it. Why: icon renders in front of the text; null removes the default. Values: icon: null. [Icon in front of the text]
- **consider** (components, react): Give a toast a primary action via action ({ label, onClick } or a ReactNode); clicking it closes the toast, so call event.preventDefault() in onClick when the toast must stay open. Why: Clicking the action closes the toast unless onClick calls event.preventDefault(). Values: { label, onClick }, event.preventDefault(). [Primary button; clicking closes the toast unless `onClick` calls `event.preventDefault()`]
- **consider** (components, react): Use cancel ({ label, onClick } or a ReactNode) for the secondary button; clicking it closes the toast. Why: cancel is the secondary button and clicking it closes the toast. Values: { label, onClick }. [Secondary button; clicking closes the toast.]
- **consider** (components, react): Style the action and cancel buttons through actionButtonStyle and cancelButtonStyle objects. Why: These options hold styles for the action and cancel buttons; both default to {}. Values: actionButtonStyle: {}, cancelButtonStyle: {}. [Styles for the action button.]
- **should** (components, react): Give a toast a custom id when it will be updated later, and call toast() again with that id to update it instead of adding a new toast. Why: Calling toast() again with the same id updates the existing toast. Values: id. [Custom id; calling `toast()` again with the same id updates the existing toast.]
- **consider** (tooling, react): Set testId on toasts that end-to-end tests need to find; it renders as data-testid. Why: testId is rendered as data-testid for e2e tests. Values: data-testid. [Rendered as `data-testid` for e2e tests.]
- **should** (components, react): When more than one Toaster exists, give each an id and send each toast to one with toasterId. Why: The Toaster id is targeted by toast()'s toasterId option. Values: id, toasterId. [Toaster id, targeted by `toast()`'s `toasterId` option.]
- **must** (components, css): Style individual toast parts with classNames (toast, title, description, actionButton, cancelButton, closeButton) and mark those classes !important unless the toast is unstyled. Why: classNames need !important unless unstyled. Values: { toast, title, description, actionButton, cancelButton, closeButton }, !important. [Needs `!important` unless `unstyled`.]
- **consider** (components, react): Use unstyled: true to remove all default toast styles when the design system supplies its own. Why: unstyled removes all default styles; default false. Values: unstyled: false (default). [Removes all default styles.]
- **should** (components, react): Handle manual closes in onDismiss and timeouts in onAutoClose; they are different events. Why: onDismiss fires on the close button or a swipe; onAutoClose fires when the toast closes after duration. Values: onDismiss, onAutoClose. [Fires when the toast closes automatically after `duration`.]
- **should** (accessibility, web): Keep an ARIA label on the toast container, 'Notifications' by default, and localise it with containerAriaLabel. Why: containerAriaLabel is the ARIA label for the toast container and defaults to 'Notifications' [keeping and localising it is inferred]. Values: 'Notifications'. [ARIA label for the toast container.]
- **should** (components, react): Use toast.success, toast.error, toast.info and toast.warning for status messages so each gets its matching icon. Why: These are typed toasts with a matching icon. Values: toast.success, toast.error, toast.info, toast.warning. [Typed toast with matching icon.]
- **consider** (components, react): Use toast.loading for a spinner toast and update it later by its id. Why: toast.loading is a toast with a spinner that you update by id. Values: toast.loading. [Toast with a spinner; update it by id.]
- **should** (components, react): Use toast.promise(promise, { loading, success, error }) for async work, where success and error can be strings, JSX, functions of the result, or objects of toast options. Why: It shows a loading toast that resolves with the promise. Values: { loading, success, error }. [Loading toast that resolves with the promise]
- **consider** (components, react): Use toast.custom((t) => jsx) when the toast's look must be fully your own but the behavior should stay Sonner's. Why: toast.custom is a headless toast: your JSX, Sonner's behavior. Values: toast.custom((t) => jsx, opts?). [Headless toast — your JSX, Sonner's behavior.]
- **consider** (components, react): Dismiss one toast with toast.dismiss(id) and all toasts with toast.dismiss() without an id. Why: toast.dismiss dismisses one toast, or all when called without an id. Values: toast.dismiss(id?). [Dismiss one toast, or all when called without an id.]
- **consider** (components, react): Read active toasts with useSonner() inside React and toast.getActiveToasts() outside React. Why: useSonner returns { toasts }; getActiveToasts is usable outside React. Values: useSonner(), toast.getActiveToasts(). [All active toasts, usable outside React.]
- **consider** (content, react): Pass a description (ReactNode or a function returning JSX) for a second line under the title. Why: description renders underneath the title and accepts a function returning JSX. Values: description. [Renders underneath the title]
- **consider** (layout, react): Override one toast's placement with toast()'s position option (default 'bottom-right') when it must differ from the Toaster. Why: position is also a per-toast option: the position of this toast. Values: position: 'bottom-right'. [Position of this toast.]
- **consider** (components, react): Use style on a toast() call (or in toastOptions) for inline styles on the toast. Why: style holds inline styles for the toast. Values: style. [Inline styles for the toast.]
- **consider** (components, react): Pass the toast message as a string, JSX, or a function returning JSX, and keep the id toast() returns when the toast will be updated or dismissed later. Why: toast(message, options) accepts those message forms and returns the toast's id; updates and toast.dismiss(id) work by id. Values: toast(message, options). [message is a string, JSX, or a function returning JSX. Returns the toast's id]
- **consider** (content, react): Use toast.promise's success and error as functions of the result (or objects of toast options) when the result toast needs the resolved value or extra options. Why: success/error accept strings, JSX, functions of the result, or objects of toast options. Values: success, error. [`success`/`error` accept strings, JSX, functions of the result, or objects of toast options]

### Decisions it informs

- Where on the screen should toasts appear?
  - bottom-right: Toasts appear in the bottom-right corner; this is the default. When: Default.
  - bottom-center: Toasts appear centered at the bottom. When: When a centered placement is wanted [inferred].
  - bottom-left: Toasts appear in the bottom-left corner. When: When the bottom-right is occupied [inferred].
  - top-left: Toasts appear in the top-left corner. When: When toasts should sit at the top [inferred].
  - top-center: Toasts appear centered at the top. When: When toasts should sit at the top [inferred].
  - top-right: Toasts appear in the top-right corner. When: When toasts should sit at the top [inferred].
  - Recommendation: The source recommends no position; its default is 'bottom-right'. Swipe directions default to ones based on position.
- Should the toast pile be collapsed until hovered, or always expanded?
  - Collapsed, expand on hover: Toasts stack and expand when the pointer hovers them. When: Default (expand: false).
  - Always expanded: Toasts are expanded by default, separated by the gap (14 by default). When: When every toast must be readable without hovering [inferred].
  - Recommendation: The default is collapsed with expand on hover.
- Should success and error toasts use neutral styling or rich colors?
  - Neutral (default): Status toasts keep the base look and differ by their matching icon. When: Default (richColors: false).
  - richColors: Error and success states become more colorful. When: When status must read by color as well as icon [inferred].
- Which color theme should toasts use?
  - 'light': Light toasts; the default. When: Light-only apps [inferred].
  - 'dark': Dark toasts. When: Dark-only apps [inferred].
  - 'system': Toasts follow the system setting. When: Apps that follow the device's light or dark mode [inferred].
  - invert: Dark toasts in light mode and light toasts in dark mode. When: When toasts should contrast with the page [inferred].
- How long should a toast stay, and can the user close it?
  - Auto-close after 4000 ms: The toast disappears after four seconds. When: Default.
  - Persist (duration: Infinity): The toast stays until it is dismissed. When: When the message must stay until acted on or dismissed [inferred].
  - Not dismissible (dismissible: false): The user cannot dismiss the toast. When: Only when the user must not close it.
  - Close button (closeButton: true): A visible close button on each toast. When: When an explicit close control is wanted [inferred].
  - Recommendation: Defaults are duration 4000, dismissible true and no close button.
- How much styling control does the toast need?
  - Default styles: Sonner's look, tuned with style, invert and richColors. When: No custom look needed [inferred].
  - classNames per part: Your classes on toast, title, description and buttons; they need !important. When: Small visual changes [inferred].
  - unstyled: true: All default styles removed. When: Your own styles on the default structure [inferred].
  - toast.custom(): Your JSX, Sonner's behavior (headless). When: A fully custom toast [inferred].

### Examples and visual references

- Per-side offset object (Sonner <Toaster /> offset prop): { bottom: '24px', right: '16px' } sets the bottom and right distances separately instead of one value for every edge.
- Typed toasts with matching icons (Sonner toast.success / .error / .info / .warning): Each status call renders its own icon in front of the text; richColors additionally tints success and error.
- Loading toast updated by id (Sonner toast.loading): A spinner toast that is later updated in place by calling toast() with the same id, instead of stacking a second toast.

### Numbers

- 3: Default number of visible toasts (visibleToasts) [Amount of visible toasts.]
- '32px': Default offset of the toaster from screen edges [Offset from screen edges.]
- { bottom: '24px', right: '16px' }: Example of a per-side offset object [Object form is per-side]
- '16px': Default mobileOffset [Offset when screen width < 600px.]
- 600px: Screen width below which mobileOffset applies [Offset when screen width < 600px.]
- 14: Default gap between toasts when expanded [Gap between toasts when expanded.]
- 4000: Default duration in milliseconds before a toast auto-closes [Milliseconds before auto-close.]
- Infinity: Duration value that keeps a toast on screen [`Infinity` persists the toast.]
- ⌥/alt + T: Default hotkey that focuses the toaster area [Keyboard shortcut that focuses the toaster area.]
- 'Notifications': Default ARIA label for the toast container [ARIA label for the toast container.]
- 6: Number of supported positions (top-left, top-center, top-right, bottom-left, bottom-center, bottom-right) [inferred count] [`top-left`, `top-center`, `top-right`]

<!-- /od:learn -->
