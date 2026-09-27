---
type: source
title: "emilkowalski/skills: skills/ask-sonner/SKILL.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-ask-sonner-skill
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/ask-sonner/SKILL.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - sonner
  - toast
  - notifications
  - react
  - nextjs
  - headless
  - styling
  - theming
  - troubleshooting
  - agent-skill
---

# emilkowalski/skills: skills/ask-sonner/SKILL.md

## Metadata

- Video ID: `eks-skills-ask-sonner-skill`
- Channel: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/ask-sonner/SKILL.md

## Summary

This is Emil Kowalski's ask-sonner agent skill: a working guide to Sonner, his React toast library, covering setup, which toast() call to use, common recipes, styling and troubleshooting. Setup is exactly two pieces: one <Toaster /> mounted once near the root, and toast() called only from client code. It gives a styling escalation ladder (defaults, inline styles, classes with !important, then headless toast.custom()) and recommends the headless rung, wrapped in your own toast() abstraction, for a design-system toast. A troubleshooting table maps the usual failures (toasts missing, doubled, unstyled, behind modals, ignoring dark mode, never closing) to their causes and fixes. For a design system it defines how a toast component should be wired, themed and customised without fighting the library.

## Key Ideas

- A toast system needs one Toaster mounted once at the root and a toast() function called from client code; nothing else.
- A second mounted Toaster duplicates every toast, so the Toaster must never be per-page or conditional.
- toast() does nothing on the server: a server action returns its result and the client shows the toast.
- Pick the call by intent: plain, typed status, loading updated by id, promise-driven, with an action button, custom JSX in the default shell, or fully headless.
- Updating a toast means calling toast() again with the same id; only the props you pass change, and a typed call switches the type.
- Styling is a ladder: defaults, inline styles, classes on parts, then headless. Climb only as far as needed; jumping straight to the top rung is fine, lingering in the middle is not.
- For a design-system toast, go headless with toast.custom() and wrap it in your own toast() abstraction, keeping Sonner's positioning, stacking and swipe.
- Classes on toast parts need !important because Sonner's injected styles win the cascade; needing many of them is the signal to go headless.
- The toast theme defaults to light and does not follow the OS; it must be set to 'system' or fed the app's resolved theme.
- There is no single 'closed' callback: onDismiss covers the close button and swipes, onAutoClose covers the timeout.
- Toasts hidden behind modals come from stacking contexts or z-index; the fix is mounting the Toaster at the document root outside dialogs and portals.
- Lost styles in Astro, view transitions or Shadow DOM are fixed by importing the stylesheet explicitly or copying the style tag into the shadow root.
- With several toasters, untargeted toasts render in every one; give each Toaster an id and target it with toasterId.
- Mobile needs a smaller edge distance: offset defaults to 32px and mobileOffset to 16px below 600px.

## Entities

- [[entities/sonner|Sonner]] (library): Emil Kowalski's React toast library that the skill teaches.
- [[entities/emil-kowalski|Emil Kowalski]] (person): Author of Sonner and of this skill.
- [[entities/ask-sonner|ask-sonner]] (product): The agent skill in emilkowalski/skills (MIT) at commit 85e8e23 that this file is.
- [[entities/next-js|Next.js]] (product): React framework; the Toaster goes in layout.tsx and works inside server components.
- [[entities/next-themes|next-themes]] (library): Theme provider whose resolvedTheme is passed to <Toaster theme>.
- [[entities/tailwind-css|Tailwind CSS]] (library): Utility classes on toast parts need the ! (important) prefix, e.g. !text-red-900.
- [[entities/astro|Astro]] (product): Framework where Sonner's injected stylesheet can be lost, fixed by importing sonner/dist/styles.css.
- [[entities/react-strictmode|React StrictMode]] (concept): Its development double-invoke of effects can fire a toast twice.
- [[entities/shadow-dom|Shadow DOM]] (concept): Sonner's styles land in document.head, so they must be copied into the shadow root.
- [[entities/headless-toast|Headless toast]] (concept): toast.custom() with your own JSX while Sonner keeps positioning, stacking and swipe.

## Topics

- [[topics/toasts-and-notifications|Toasts and notifications]]: Complete guide to wiring, calling, updating, persisting, dismissing, styling and debugging toasts.
- [[topics/ui-libraries|UI libraries]]: How to adopt Sonner well: one Toaster, toast() from client code, and a headless wrapper for a design-system toast.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: The recommended design-system toast is headless (toast.custom()) wrapped in your own toast() abstraction.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Server vs client calls, StrictMode double-invoke, the CSS cascade and !important, stacking contexts, stylesheet loss in Astro, view transitions and Shadow DOM.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: theme defaults to 'light' and ignores the OS; set 'system' or pass the resolved theme from next-themes.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: Loading toasts updated by id, toast.promise for loading to success or error, and promises that never settle leaving a toast stuck.
- [[topics/modals-and-popovers|Modals and popovers]]: Toasts behind modals or overlays are caused by stacking contexts or z-index; mount the Toaster outside dialog and portal containers.
- [[topics/gestures-and-drag|Gestures and drag]]: Swipe-to-dismiss directions derive from position and are overridden with swipeDirections; swipes fire onDismiss.
- [[topics/spacing-and-layout|Spacing and layout]]: offset (default 32px) and mobileOffset (below 600px, default 16px) keep toasts off the screen edge.

## Notable Claims

- A second mounted Toaster duplicates every toast. Evidence: a second mounted Toaster duplicates every toast
- In Next.js the Toaster works inside server components when placed in layout.tsx. Evidence: in Next.js: `layout.tsx` — it works inside server components
- toast() is a plain function needing no hook or provider, but it does nothing on the server. Evidence: It's a plain function, no hook or provider needed, but it does nothing on the server
- Calling toast() again with the same id changes only the props you pass; toast.success(…, { id }) changes the type. Evidence: call `toast()` again with the same `id`; only the props you pass change
- Without toasterId, every toaster renders the toast. Evidence: Without `toasterId`, every toaster renders the toast
- onDismiss and onAutoClose are separate; there is no single closed callback. Evidence: They are separate; there is no single "closed" callback
- Sonner's injected styles win the cascade, so classes on toast parts need !important. Evidence: Sonner's injected styles win the cascade, so every class needs `!important`
- Headless toast.custom() keeps Sonner's positioning, stacking and swipe. Evidence: keeping Sonner's positioning, stacking, and swipe
- unstyled: true is a halfway house; headless gives more control for the same effort. Evidence: `unstyled: true` exists as a halfway house
- The theme defaults to 'light' and does not track the OS. Evidence: `theme` defaults to `'light'` and does not track the OS
- Under React StrictMode, a toast fired in an effect can appear twice because of the development double-invoke. Evidence: `toast()` fired in an effect under React StrictMode's dev double-invoke
- In Astro and with view transitions, Sonner's injected stylesheet can be lost, leaving toasts unstyled. Evidence: Toasts render completely unstyled
- Inside Shadow DOM, toasts are unstyled because styles land in document.head, not the shadow root. Evidence: Unstyled inside Shadow DOM
- Toasts sit behind a modal or are clipped when an ancestor creates a stacking context (transform, filter, overflow) or an overlay out-z-indexes the toaster. Evidence: Toast behind a modal/overlay, or clipped
- Success and error toasts look gray rather than green and red by default. Evidence: Success/error look gray, not green/red
- A toast never closes when duration is Infinity, dismissible is false, or a toast.promise promise never settles. Evidence: Toast never closes
- toast.promise needs a promise, or a function returning one, that actually resolves or rejects. Evidence: `toast.promise` stuck on loading
- Swipe-to-dismiss directions derive from position. Evidence: Directions derive from `position`
- offset defaults to 32px on desktop and mobileOffset to 16px below 600px. Evidence: Toasts too close to the screen edge on mobile

## Quotes

> Never render it per-page or conditionally; a second mounted Toaster duplicates every toast.
> If you're marking more than a few things important, stop — go headless.
> Climb only as far as the change requires

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is an agent skill prompt, pinned to commit 85e8e23 of emilkowalski/skills; Sonner's API and defaults can change.
- Caveat: The skill tells the agent to open with a fixed line and say nothing more until asked; that line is self-description, not design guidance.
- Caveat: Framework-specific fixes (Next.js layout.tsx, next-themes, Astro, Tailwind ! prefix) apply only to those stacks.
- Caveat: React-only: rules about Toaster, toast() and hooks do not transfer as code to iOS, Android or desktop toolkits.

### Rules and practices

- **must** (components, react): Mount one <Toaster /> once, as close to the root as possible (several toasters are a separate recipe, each with its own id). Why: Setup is two pieces, and only two; a second mounted Toaster duplicates every toast. Values: <Toaster />. [One `<Toaster />`, mounted once**, as close to the root as possible]
- **must** (tooling, react): In Next.js, put the Toaster in layout.tsx. Why: It belongs as close to the root as possible and works inside server components. Values: layout.tsx. [in Next.js: `layout.tsx`]
- **must** (components, react): Never render the Toaster per page or conditionally. Why: A second mounted Toaster duplicates every toast, and an unmounted one means toasts never appear. [Never render it per-page or conditionally]
- **must** (components, react): Call toast() only from client code (event handlers, effects, callbacks); it is a plain function, so no hook or provider is needed. Why: It is a plain function that does nothing on the server. [`toast()` called from client code]
- **must** (components, react): Do not call toast() inside a server action; return the result and call toast() in the client code that receives it. Why: toast() is client-only and does nothing on the server. [in a server action, return the result]
- **should** (tooling, react): Import Toaster once, in the layout, and import toast wherever client code needs it. Why: Setup is exactly these two imports. Values: import { Toaster } from 'sonner', import { toast } from 'sonner'. [once, in layout]
- **should** (components, react): For a plain message use toast('Title') and add { description } for a second line. Why: This is the call the source maps to a plain message. Values: toast('Title'), { description }. [Plain message]
- **should** (components, react): For success, error, info or warning messages use the typed calls toast.success, toast.error, toast.info and toast.warning. Why: They carry the matching status icon. Values: toast.success('…'), toast.error('…'). [Success / error / info / warning icon]
- **should** (components, react): When you manage the async state yourself, show toast.loading('…') and then update that toast by its id. Why: It shows a spinner and changes in place when updated by id. Values: toast.loading('…'). [Spinner while you manage state yourself]
- **should** (components, react): When the loading, success and error states are tied to one promise, use toast.promise(promise, { loading, success, error }), passing functions to success and error to use the resolved value or the error. Why: success and error accept functions receiving the resolved value or error. Values: toast.promise(promise, { loading, success, error }). [Loading → success/error tied to a promise]
- **should** (components, react): Give a toast a button that does something with { action: { label, onClick } }, use cancel for the secondary button, and call event.preventDefault() in onClick to keep the toast open. Why: The action closes the toast unless onClick calls event.preventDefault(); cancel is the secondary variant. Values: { action: { label, onClick } }, event.preventDefault(). [Button that does something]
- **consider** (components, react): Put custom JSX inside the default toast shell with toast(<jsx />). Why: This keeps Sonner's default shell around your content. Values: toast(<jsx />). [Custom JSX, default toast shell]
- **should** (components, react): For custom JSX with no default styles at all, use toast.custom((t) => <jsx />) and use t's id to dismiss it. Why: It is headless, and t gives you the id to dismiss. Values: toast.custom((t) => <jsx />). [Custom JSX, no styles at all]
- **should** (components, react): Update a toast by calling toast() again with the same id, passing only the props that change; switch its type with a typed call such as toast.success(…, { id }). Why: Only the props you pass change, and a typed call changes the type; this is how loading to success works without toast.promise. Values: const id = toast.loading('Uploading…');, toast.success('Uploaded', { id });. [call `toast()` again with the same `id`; only the props you pass change]
- **consider** (components, react): Persist a toast with { duration: Infinity }. Why: This is the source's recipe for persisting. Values: { duration: Infinity }. [**Persist** — `{ duration: Infinity }`]
- **consider** (components, react): Dismiss one toast with toast.dismiss(id) and all toasts with toast.dismiss(). Why: This is the source's dismiss recipe. Values: toast.dismiss(id), toast.dismiss(). [`toast.dismiss(id)`, or `toast.dismiss()` for all]
- **consider** (components, react): Read active toasts with useSonner() in React and toast.getActiveToasts() outside it. Why: This is the source's recipe for reading active toasts. Values: useSonner(), toast.getActiveToasts(). [Read active toasts]
- **consider** (content, react): To put links or components in a toast's title or description, pass a function that returns the JSX. Why: The source gives this as the way to render links or components in the text. Values: toast(() => <a href="…">View</a>). [Links or components in the text]
- **must** (components, react): With more than one Toaster, give each an id and target it with toasterId in every toast() call. Why: Without toasterId, every toaster renders the toast. Values: toast('…', { toasterId: 'canvas' }). [Without `toasterId`, every toaster renders the toast]
- **should** (components, react): Handle onDismiss and onAutoClose separately, and wire both when you need to react to every way a toast closes. Why: onDismiss fires on close button or swipe and onAutoClose on timeout; there is no single closed callback [wiring both is inferred]. Values: onDismiss, onAutoClose. [They are separate; there is no single "closed" callback]
- **must** (process, react): Climb the styling ladder (defaults, inline style, classNames, headless) only as far as the change requires; jumping straight to headless is fine. Why: Jumping to the top rung too early is fine (it is the recommended end state), but lingering in the middle rungs is not. [Climb only as far as the change requires]
- **must** (process, react): Do not settle on the middle styling rungs (inline styles or !important classes) as the long-term setup. Why: The top rung is the recommended end state; lingering in the middle is not fine. [lingering in the middle is not]
- **should** (color, react): Start from the defaults, adding richColors on the Toaster for colorful success and error, and invert to flip toasts against the theme. Why: This is rung 1 of the ladder. Values: richColors, invert. [plus `richColors` on the Toaster for colorful success/error, `invert` to flip against the theme]
- **consider** (components, react): For small tweaks, use toastOptions={{ style: {…} }} on the Toaster for all toasts, or style on a single toast() call. Why: This is rung 2, inline tweaks. Values: toastOptions={{ style: {…} }}, style. [**Inline tweaks**]
- **must** (components, css): When styling toast parts with classNames (toast, title, description, actionButton, cancelButton, closeButton), mark every class !important; in Tailwind use the ! prefix. Why: Sonner's injected styles win the cascade. Values: !important, !text-red-900. [Sonner's injected styles win the cascade]
- **must** (components, css): Once more than a few classes need !important, stop and go headless. Why: That is the signal the middle rung is being over-used. [If you're marking more than a few things important, stop]
- **should** (components, react): Build the design-system toast headless with toast.custom() and your own JSX, and wrap it in your own toast() abstraction. Why: Headless keeps Sonner's positioning, stacking and swipe, and it is the recommended approach for a design-system toast. Values: toast.custom(). [The recommended approach for a design-system toast: wrap it in your own `toast()` abstraction]
- **should** (components, react): Prefer headless toast.custom() over unstyled: true. Why: unstyled is a halfway house; headless gives more control for the same effort. Values: unstyled: true. [halfway house]
- **consider** (components, react): Swap icons per type with the Toaster's icons prop, per toast with icon, and remove one with null. Why: These are the three icon controls the source lists. Values: icons, icon, null. [swap defaults per-type with the Toaster's `icons` prop, per-toast with `icon`, remove with `null`]
- **must** (color, react): Set the Toaster theme to 'system' or pass your theme provider's resolved theme, e.g. <Toaster theme={resolvedTheme} /> from next-themes. Why: theme defaults to 'light' and does not track the OS, so dark mode is otherwise ignored. Values: theme="system", <Toaster theme={resolvedTheme} />. [does not track the OS]
- **should** (process, react): If a toast never appears, check that a Toaster is mounted at the root and not unmounted by a conditional render or per-page placement, and that toast() runs on the client. Why: Missing or unmounted Toasters and server-side calls are the listed causes. [Toast never appears]
- **must** (components, react): Do not mount a Toaster in both the layout and a page; keep one. Why: Two mounted Toasters make the same toast appear twice. [Two Toasters mounted (layout **and** page)]
- **should** (components, react): Fire toasts from event handlers rather than effects, or pass a stable id when a toast must fire from an effect. Why: React StrictMode's dev double-invoke runs effects twice; a stable id makes the second call update rather than duplicate. Values: stable id. [React StrictMode's dev double-invoke]
- **should** (tooling, web): When toasts render completely unstyled (common in Astro and with view transitions), import the stylesheet explicitly in a layout. Why: Sonner's injected stylesheet was lost. Values: import 'sonner/dist/styles.css'. [Toasts render completely unstyled]
- **should** (tooling, web): Inside Shadow DOM, copy the style tag whose text includes [data-sonner-toaster] into the shadow root. Why: Sonner's styles land in document.head, not the shadow root. Values: [data-sonner-toaster]. [Unstyled inside Shadow DOM]
- **should** (elevation, web): Mount the Toaster at the document root, outside any dialog or portal container, so toasts are not hidden behind modals or clipped. Why: An ancestor with transform, filter or overflow creates a stacking context, or the overlay out-z-indexes the toaster. Values: transform, filter, overflow. [Move `<Toaster />` to the document root, outside any dialog/portal container]
- **should** (elevation, css): Do not place the Toaster inside an element that uses transform, filter or overflow [inferred]. Why: Those create a stacking context that hides or clips toasts [phrased as a don't: inferred from the cause column]. Values: transform, filter, overflow. [An ancestor creates a stacking context]
- **should** (color, react): Add richColors to the Toaster when success and error must look green and red. Why: Gray success and error toasts are the default. Values: richColors. [Success/error look gray, not green/red]
- **should** (process, react): If a toast never closes, check for duration: Infinity, dismissible: false, or a toast.promise whose promise never settles. Why: Each makes the toast stay; an unsettled promise leaves the loading toast waiting forever. Values: duration: Infinity, dismissible: false. [Toast never closes]
- **must** (components, react): Pass toast.promise a promise, or a function returning one, that actually resolves or rejects. Why: Otherwise toast.promise stays stuck on loading. [`toast.promise` stuck on loading]
- **should** (motion, react): If swipe-to-dismiss goes the wrong way or does not work, override swipeDirections on the Toaster. Why: Swipe directions derive from position. Values: swipeDirections. [Directions derive from `position`]
- **should** (layout, web): Keep toasts off the screen edge with offset on desktop (default 32px) and mobileOffset below 600px (default 16px), as numbers, CSS strings or per-side objects. Why: These are the settings for toasts that sit too close to the edge on mobile. Values: 32px, 16px, <600px. [Toasts too close to the screen edge on mobile]
- **should** (process, all): Answer Sonner tasks from the skill first, and read API.md when an exact prop name, type or default is needed. Why: The skill says to answer from this file first and keep full prop tables in API.md. Values: API.md. [answer from this file first]
- **should** (components, css): When Tailwind or CSS classes on toasts have no effect, mark them !important or move to unstyled or headless. Why: Sonner's default styles override the classes. Values: !important, unstyled. [Default styles override them. Mark them `!important`, or use `unstyled` / headless]

### Decisions it informs

- How should the design system's toast be styled on top of Sonner?
  - Defaults: Sonner's look, with richColors for colorful success and error and invert to flip against the theme. When: No custom look is needed [inferred].
  - Inline tweaks: style objects via toastOptions for all toasts, or style per call. When: A few small changes [inferred].
  - Classes on parts: classNames on toast, title, description and buttons, each needing !important. When: Only a few classes; if many need !important, go headless.
  - unstyled: true: Default styles removed; a halfway house. When: Not preferred: headless gives more control for the same effort.
  - Headless toast.custom(): Your own JSX; Sonner keeps positioning, stacking and swipe. When: A design-system toast, wrapped in your own toast() abstraction.
  - Recommendation: Headless toast.custom() wrapped in your own toast() abstraction. It is the recommended end state for a design-system toast, and lingering on the middle rungs is discouraged.
- Which toast call fits the message?
  - toast('Title'): Plain message, with an optional description line. When: Plain information.
  - toast.success / .error / .info / .warning: Status toast with its icon. When: The message has a status.
  - toast.loading then update by id: Spinner that changes into the result in place. When: You manage the async state yourself.
  - toast.promise: Loading that turns into success or error when the promise settles. When: The states are tied to one promise.
  - action / cancel: Primary and secondary buttons on the toast. When: The toast offers something to do.
  - toast(<jsx />): Custom content in the default shell. When: Custom content, default look.
  - toast.custom((t) => <jsx />): Headless: no styles at all. When: Fully custom look.
  - Recommendation: Match the call to the intent using the source's table.
- How should a loading toast become a success or error toast?
  - toast.promise: Sonner moves from loading to success or error when the promise resolves or rejects. When: The states are tied to one promise.
  - toast.loading plus update by id: You call toast.success(…, { id }) or toast.error with the same id when done. When: You manage the state yourself.
- How should toasts follow light and dark mode?
  - Default 'light': Toasts stay light and ignore the OS. When: Light-only apps [inferred].
  - theme="system": Toasts follow the OS setting. When: The app follows the OS.
  - Resolved theme from a provider: <Toaster theme={resolvedTheme} /> matches the app's own theme switch. When: The app has a theme provider such as next-themes.
  - Recommendation: Set theme="system" or pass the resolved theme, because the default ignores dark mode.
- With more than one toaster, where does each toast go?
  - Untargeted: Every toaster renders the toast. When: Not intended with several toasters.
  - Targeted by toasterId: Each Toaster has an id and toasts go only to the one named. When: Several toasters, e.g. one for a canvas (the source's example id).
  - Recommendation: Give each Toaster an id and pass toasterId.

### Process

1. Mount the Toaster once: Render one <Toaster /> as close to the root as possible (Next.js: layout.tsx), never per page or conditionally.
2. Call toast() from the client: Call toast() from event handlers, effects or callbacks; for server actions, return the result and toast on the client.
3. Pick the call by intent: Use the table: plain, typed status, loading plus update, promise, action, custom JSX in the shell, or headless.
4. Wire state changes by id: Update, persist (duration: Infinity) and dismiss toasts through their id; read active toasts with useSonner() or toast.getActiveToasts().
5. Set the theme: Pass theme="system" or the resolved theme from your provider, since the default is light.
6. Climb the styling ladder: Defaults, then inline style, then classNames with !important, then headless toast.custom() wrapped in your own toast() for a design-system toast; stop at the rung the change needs, but never settle in the middle.
7. Troubleshoot by symptom: Match the symptom (missing, doubled, unstyled, behind a modal, dark mode ignored, gray status, never closes, stuck loading, wrong swipe, every toaster, too close to the edge) to its listed cause and fix.
8. Look up exact props in API.md: Answer from the skill first and read API.md for an exact prop name, type or default.

### Examples and visual references

- Loading to success upload flow without toast.promise (Sonner): const id = toast.loading('Uploading…'); then toast.success('Uploaded', { id }); the same toast changes from a spinner to a success message in place.
- Link inside a toast (Sonner): toast(() => <a href="…">View</a>) renders a clickable link as the toast title.
- Second toaster for a canvas (Sonner): toast('…', { toasterId: 'canvas' }) sends the toast only to the Toaster with id 'canvas'.
- Toaster following the app theme (next-themes): <Toaster theme={resolvedTheme} /> keeps toasts in step with the app's light or dark theme.
- Tailwind class on a toast part (Tailwind CSS): !text-red-900 shows the ! prefix needed to beat Sonner's injected styles.
- Restoring lost styles (Astro, view transitions): import 'sonner/dist/styles.css' in a layout brings back the stylesheet when toasts render completely unstyled.

### Numbers

- 32px: Default desktop offset of toasts from the screen edge [`offset` (desktop, default 32px)]
- 16px: Default mobileOffset [`mobileOffset` (<600px, default 16px)]
- <600px: Screen width at which mobileOffset applies [`mobileOffset` (<600px, default 16px)]

<!-- /od:learn -->
