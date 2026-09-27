---
type: source
title: "Toast – Sonner"
created: 2026-09-27
updated: 2026-09-27
video_id: sonner-toast
url: https://sonner.emilkowal.ski/toast
channel: Sonner docs (web)
published: Unknown
authority: non-negotiable
tags:
  - sonner
  - toast
  - react
  - toast-types
  - promise-toast
  - loading-state
  - toast-actions
  - api-defaults
---

# Toast – Sonner

## Metadata

- Video ID: `sonner-toast`
- Channel: Sonner docs (web)
- Published: Unknown
- URL: https://sonner.emilkowal.ski/toast

## Summary

The toast() page documents every way to render a Sonner toast and lists the per-toast options with their defaults. A plain string becomes the title, and an options object passed as the second argument overrides any options set on <Toaster />. The typed variants add meaning: success shows a checkmark icon, error shows an error icon, action and cancel render primary and secondary buttons that close the toast, promise toasts move from loading to a result automatically, loading toasts show a spinner, and custom and headless toasts let you supply your own JSX. The API reference lists the per-toast defaults, including duration 4000, position bottom-right, dismissible true, closeButton false and containerAriaLabel 'Notifications'. For a design system this is the catalogue of toast variants and the baseline values to lock. [inferred]

## Key Ideas

- Calling toast() with just a string makes that string the title.
- Options passed to toast() override the options set on <Toaster />.
- Success toasts show a checkmark icon in front of the message, and error toasts show an error icon.
- An action is a primary button: clicking it runs onClick and closes the toast, unless onClick calls event.preventDefault().
- A cancel is a secondary button that also runs onClick and closes the toast.
- Both action and cancel can be JSX, such as your own <Button>.
- A promise toast starts in a loading state and updates itself when the promise resolves or fails; its messages can be functions of the result or error.
- A loading toast shows a spinner and is for when you handle the states yourself instead of using a promise toast.
- Custom toasts take JSX as the first argument and keep the default styling.
- Headless toasts are unstyled custom JSX that keep the functionality and receive the Toast as an argument.
- Default per-toast values: duration 4000, position bottom-right, dismissible true, closeButton false, invert false, containerAriaLabel Notifications.

## Entities

- [[entities/sonner|Sonner]] (library): The React toast library whose toast() function this page documents.
- [[entities/toast|toast()]] (concept): The function that renders a toast, with success, error, action, cancel, promise, loading, custom and headless forms.
- [[entities/toaster|Toaster]] (concept): The container component whose options are overridden by per-toast options.
- [[entities/headless-toast|Headless toast]] (concept): An unstyled toast rendered from your own JSX that keeps Sonner's behaviour.
- [[entities/promise-toast|Promise toast]] (concept): A toast that starts loading and updates automatically when a promise resolves or fails.
- [[entities/aiforui-dev|aiforui.dev]] (product): A course promoted in the site-wide banner.

## Topics

- [[topics/toasts-and-notifications|Toasts and notifications]]: Documents every toast variant (success, error, action, cancel, promise, loading, custom, headless) and the per-toast API defaults.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: Promise toasts show loading and then success or error automatically; loading toasts show a spinner when you manage the states yourself.
- [[topics/buttons-and-actions|Buttons and actions]]: Action renders a primary button and cancel a secondary one; both close the toast on click, and event.preventDefault() keeps it open.
- [[topics/accessibility|Accessibility]]: The toast container has an aria label, containerAriaLabel, which defaults to 'Notifications'.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Shows JSX actions and cancels, per-toast style objects (actionButtonStyle, cancelButtonStyle) and the typed API table.

## Notable Claims

- When toast() is called with just a string, the string becomes the title. Evidence: Rendering the toast
- Options passed as the second argument to toast() override options passed to <Toaster />. Evidence: These will override the options passed to <Toaster />
- A success toast renders a checkmark icon in front of the message. Evidence: Renders a checkmark icon in front of the message.
- An error toast renders an error icon in front of the message. Evidence: Renders an error icon in front of the message.
- Clicking an action button closes the toast and runs its onClick callback; calling event.preventDefault() in onClick prevents the close. Evidence: Action
- Clicking a cancel button closes the toast and runs its onClick callback. Evidence: Cancel
- A promise toast starts in a loading state and updates automatically after the promise resolves or fails. Evidence: Promise
- A promise toast's success and error messages can be functions that use the promise's result or error, and can return an object of toast options. Evidence: You can pass a function to the success/error messages
- A loading toast renders a loading spinner and is useful when you handle the states yourself instead of using a promise toast. Evidence: Loading
- Passing JSX as the first argument renders a custom toast that keeps the default styling. Evidence: Custom
- A headless toast is unstyled, keeps the functionality, and its function receives the Toast as an argument. Evidence: Headless
- The default toast duration is 4000. Evidence: duration number 4000
- The default containerAriaLabel is 'Notifications'. Evidence: containerAriaLabel string Notifications

## Quotes

> You can call it with just a string, that will become the title.
> These will override the options passed to <Toaster /> if you have provided any.
> Starts in a loading state and will update automatically after the promise resolves or fails.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Most sections were live previews with preview/code tabs, and their code did not survive text extraction ('Cop y ied Code' artifacts). The exact call names for the success, error, promise, loading, custom and headless variants are not shown on this page.
- Caveat: The page does not state the unit for the duration default of 4000.
- Caveat: The page lists invert, testId and toasterId without describing their effect, so their behaviour here comes only from their names and the Toaster page.
- Caveat: A site-wide banner promotes the author's aiforui.dev course with a countdown: self-promotion, time-sensitive.
- Caveat: The page's publish date is unknown, so the API may have changed since it was fetched.

### Rules and practices

- **should** (components, react): Call toast() with just a string when the toast only needs a title. Why: A string passed on its own becomes the title. [Rendering the toast]
- **should** (components, react): Set shared toast options on <Toaster />, and pass per-toast options as an object in toast()'s second argument; per-toast options win. Why: Options given to toast() override the options passed to <Toaster />. [These will override the options passed to <Toaster />]
- **should** (components, react): Use the success toast for success messages so a checkmark icon appears in front of the message. Why: Success renders a checkmark icon in front of the message. [Renders a checkmark icon in front of the message.]
- **should** (components, react): Use the error toast for failures so an error icon appears in front of the message. Why: Error renders an error icon in front of the message. [Renders an error icon in front of the message.]
- **should** (components, react): Use the action option to put a primary button in the toast; clicking it closes the toast and runs the callback passed via onClick. Why: Action renders a primary button, and clicking it closes the toast and runs the callback passed via onClick. Values: action. [Renders a primary button, clicking it will close the toast and run the callback passed via onClick]
- **consider** (components, react): Call event.preventDefault() inside the action's onClick when the toast must stay open after the action is clicked. Why: By default clicking the action closes the toast; preventDefault stops that. Values: event.preventDefault(). [You can prevent the toast from closing by calling event.preventDefault()]
- **consider** (components, react): Pass your own JSX, such as a <Button> component, as the action when the default action button is not enough. Why: The docs show that you can render JSX as your action. Values: action: <Button onClick={() => console.log('Action!')}>Action</Button>. [You can also render jsx as your action.]
- **should** (components, react): Use the cancel option to put a secondary button in the toast; clicking it closes the toast and runs the callback passed via onClick. Why: Cancel renders a secondary button, and clicking it closes the toast and runs the callback passed via onClick. Values: cancel. [Renders a secondary button, clicking it will close the toast and run the callback passed via onClick]
- **consider** (components, react): Pass your own JSX as the cancel when the default cancel button is not enough. Why: The docs show that you can render JSX in the cancel option. Values: cancel: <Button onClick={() => console.log('Cancel!')}>Cancel</Button>. [You can also render jsx in the cancel option.]
- **should** (patterns, react): Use a promise toast for async work, so the toast starts loading and switches to success or error on its own when the promise settles. Why: A promise toast starts in a loading state and updates automatically after the promise resolves or fails. [Starts in a loading state and will update automatically after the promise resolves or fails.]
- **should** (content, react): Pass functions as a promise toast's success and error messages so the message includes the promise's result or error. Why: The docs say you can pass a function to the success/error messages to incorporate the result or error. [You can pass a function to the success/error messages]
- **consider** (components, react): Return an object of toast options from a promise toast's success or error function when the result toast needs more detail. Why: The docs say you can return an object with toast options if you need more detailed toasts. [If you need more detailed toasts, you can return an object with toast options.]
- **should** (patterns, react): Use a loading toast (spinner) only when you handle the loading, success and error states yourself; otherwise use a promise toast. Why: The loading toast is useful when you want to handle various states yourself instead of using a promise toast. [Useful when you want to handle various states yourself instead of using a promise toast.]
- **consider** (components, react): For custom content that keeps Sonner's default styling, pass JSX as the first argument instead of a string. Why: This renders a custom toast while keeping the default styling. [You can pass jsx as the first argument instead of a string to render a custom toast while maintaining default styling.]
- **consider** (components, react): For a fully custom look, use the headless toast: render your own unstyled JSX, which keeps the functionality and receives the Toast as an argument. Why: Headless renders an unstyled toast with custom JSX while keeping the functionality and giving access to all toast properties. [Use it to render an unstyled toast with custom jsx while maintaining the functionality.]
- **should** (motion, react): Set how long a toast stays on screen with the duration option; the default is 4000. Why: The API reference lists duration with a default of 4000. Values: 4000. [duration number 4000]
- **should** (accessibility, react): Give the toast container its accessible label through containerAriaLabel, which defaults to 'Notifications'. Why: The API reference lists containerAriaLabel with the default 'Notifications'. Values: Notifications. [containerAriaLabel string Notifications]
- **consider** (components, react): Show a close button on a toast with closeButton; it is off (false) by default. Why: The API reference lists closeButton with a default of false. Values: false. [closeButton boolean false]
- **consider** (components, react): Control whether a toast can be dismissed with dismissible, which defaults to true. Why: The API reference lists dismissible with a default of true. Values: true. [dismissible boolean true]
- **consider** (layout, react): Set a toast's position with the position option; the default is bottom-right. Why: The API reference lists position with a default of bottom-right. Values: bottom-right. [position string bottom-right]
- **consider** (components, react): Put secondary text in the description option (a ReactNode) and a custom icon in the icon option (a ReactNode). Why: The API reference lists description and icon as ReactNode options. Values: description, icon. [description ReactNode]
- **consider** (components, react): Style a toast's action and cancel buttons with actionButtonStyle and cancelButtonStyle objects; both default to {}. Why: The API reference lists both as objects with a default of {}. Values: actionButtonStyle, cancelButtonStyle, {}. [actionButtonStyle object {}]
- **consider** (components, react): Give a toast an id to refer to it later and a toasterId to send it to a specific Toaster; a testId option also exists, but this page does not describe it. [inferred] Why: The API reference lists id, testId and toasterId as string options; what toasterId does is explained on the Toaster page. Values: id, testId, toasterId. [toasterId string]
- **consider** (components, react): Attach onDismiss and onAutoClose callbacks to a toast when code must react to it closing. Why: The API reference lists onDismiss and onAutoClose as function options; the Other page explains when each fires. Values: onDismiss, onAutoClose. [onDismiss function]
- **consider** (color, react): Leave invert at its default of false unless a toast should be inverted. Why: The API reference lists invert with a default of false; the page does not describe the inverted look. Values: false. [invert boolean false]

### Decisions it informs

- For async work, should the toast follow the promise automatically or be driven by hand?
  - Promise toast: Starts in a loading state and switches to success or error automatically when the promise settles; messages can use the result or error. When: When the work is a promise.
  - Loading toast: Shows a spinner; your code updates the toast to each state itself. When: When you want to handle the various states yourself instead of using a promise toast.
  - Recommendation: Use the promise toast by default; the page positions the loading toast for cases where you handle the states yourself. [inferred]
- When a toast needs custom content, should it keep Sonner's styling or be fully custom?
  - Custom: Your JSX is rendered inside the toast with the default styling kept. When: When you need custom content but want the standard look.
  - Headless: An unstyled toast made from your own JSX that keeps the functionality and receives the Toast as an argument. When: When you need full control of the look.
- Should clicking a toast's action button close the toast?
  - Close on click (default): The onClick callback runs and the toast closes. When: Default behaviour.
  - Stay open: Calling event.preventDefault() in onClick keeps the toast on screen after the action runs. When: When the toast must remain visible after the action.

### Process

1. Pick the variant: Choose plain, success, error, action, cancel, promise, loading, custom or headless based on what the message needs.
2. Pass options: Add an options object as the second argument (description, icon, action, cancel, duration, position and so on); these override the <Toaster /> options.
3. Wire async feedback: For a promise, use the promise toast: it shows loading, then success or error. Pass functions for the success and error messages to include the result or error, and return an object of toast options for more detail.
4. Handle actions: Give action and cancel an onClick. Both close the toast after running; call event.preventDefault() in the action's onClick to keep it open.

### Examples and visual references

- Action toast with a JSX button (Sonner docs, Action section): Code only: toast('My action toast', { action: <Button onClick={() => console.log('Action!')}>Action</Button> }), showing a custom primary button inside a toast.
- Cancel toast with a JSX button (Sonner docs, Cancel section): Code only: toast('My cancel toast', { cancel: <Button onClick={() => console.log('Cancel!')}>Cancel</Button> }), showing a custom secondary button.
- Live 'Render toast' previews (Sonner docs, each variant section): Each section has a preview/code tab with a 'Render toast' button. The rendered visuals and most code were not captured in the text.

### Numbers

- 4000: Default toast duration (the unit is not stated on the page) [API Reference: duration number 4000]
- bottom-right: Default toast position [API Reference: position string bottom-right]
- Notifications: Default containerAriaLabel for the toast container [API Reference: containerAriaLabel string Notifications]
- false: Default for closeButton and invert [API Reference]
- true: Default for dismissible [API Reference]
- {}: Default for actionButtonStyle and cancelButtonStyle [API Reference]

<!-- /od:learn -->
