---
type: source
title: "referodesign/refero_skill: skills/refero-design/references/craft-details.md"
created: 2026-10-07
updated: 2026-10-07
video_id: referodesign-refero-skil-skills-refero-design-references-craft-details
url: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/craft-details.md
channel: referodesign/refero_skill (GitHub, MIT)
published: commit a9b54a3
authority: reference
tags:
  - focus-visible
  - forms
  - autocomplete
  - cls
  - images
  - touch
  - performance
  - virtualization
  - semantic-html
  - url-state
  - anti-patterns
  - refero
---

# referodesign/refero_skill: skills/refero-design/references/craft-details.md

## Metadata

- Page ID: `referodesign-refero-skil-skills-refero-design-references-craft-details`
- Publisher: referodesign/refero_skill (GitHub, MIT)
- Published: commit a9b54a3
- URL: https://github.com/referodesign/refero_skill/blob/a9b54a3/skills/refero-design/references/craft-details.md

## Summary

This Refero guide collects web implementation details that separate polished products from rough ones, which it says most AI models miss. It covers focus states (:focus-visible, never bare outline: none, :focus-within for compound controls), form attributes (type, inputmode, autocomplete, spellcheck, clickable labels, placeholder format, submit states, inline errors, unsaved-changes warning), images (explicit dimensions, fetchpriority and lazy loading), touch details, performance patterns (virtualizing 50+ item lists, avoiding layout reads in render, uncontrolled inputs, preconnect and font preload), accessibility quick wins, URL state and destructive-action confirmation, plus short copy rules. It ends with an anti-pattern list for code review and a pre-ship checklist. For a design system it is a component-implementation checklist that keeps accessibility floors and interaction quality in shipped web code.

## Key Ideas

- Use :focus-visible so focus rings show for keyboard users, not on mouse clicks.
- Never remove the outline without a visible custom focus replacement.
- Use :focus-within to highlight a compound control when any child is focused.
- Correct input type, inputmode and autocomplete bring up the right mobile keyboard and help password managers.
- Never block paste in inputs.
- Images without width and height cause layout shift; load hero images eagerly and lower images lazily.
- touch-action: manipulation removes the mobile tap delay; overscroll-behavior: contain stops scroll chaining in modals.
- Autofocus only on desktop, at most one primary input per page, and only with a reason.
- Virtualize lists of 50+ items and avoid reading layout during render.
- Use semantic button and link elements, keyboard handlers for custom controls, and an unbroken heading order.
- Reflect filters, tabs and pagination in the URL and use real links so Cmd+click and back work.
- Destructive actions need a confirmation or an undo window.
- Flag transition: all, disabled zoom, div buttons, unlabelled inputs and icon buttons without aria-label in code review.

## Entities

- [[entities/virtua|virtua]] (library): List virtualization library shown in the VList example.
- [[entities/react-window|react-window]] (library): Alternative list virtualization library.
- [[entities/nuqs|nuqs]] (library): Library suggested for syncing state with URL query params.
- [[entities/next-js|Next.js]] (library): Image component example with priority and lazy loading.
- [[entities/resizeobserver|ResizeObserver]] (concept): Browser API recommended instead of reading offsetHeight in render.
- [[entities/cls|CLS]] (concept): Cumulative layout shift; images are named its number one cause.
- [[entities/intl-datetimeformat-intl-numberformat|Intl.DateTimeFormat / Intl.NumberFormat]] (concept): Recommended over hardcoded date and number formats.

## Topics

- [[topics/accessibility|Accessibility]]: :focus-visible focus rings, semantic elements, keyboard handlers for custom controls, heading hierarchy, aria-live announcements, labels, aria-label on icon buttons, and never disabling zoom.
- [[topics/forms-and-inputs|Forms and inputs]]: type/inputmode/autocomplete values, no paste blocking, spellcheck off for codes and emails, clickable labels with no dead zones, placeholders ending in an ellipsis, spinner on submit, inline errors focused on submit, unsaved-changes warning.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: CSS and JSX snippets for focus, touch, images, virtualization, ResizeObserver, uncontrolled inputs, preconnect and font preload, URL state with nuqs.
- [[topics/animation-performance|Animation performance]]: Flags transition: all as a performance killer and recommends virtualizing long lists and avoiding forced synchronous layout.
- [[topics/mobile-app-patterns|Mobile app patterns]]: Remove the 300ms tap delay, set tap highlight intentionally, contain overscroll in modals and sheets, avoid autofocus on mobile.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: URL reflects app state; use real links instead of onClick navigation so Cmd+click and middle-click work.
- [[topics/content-and-microcopy|Content and microcopy]]: Active voice, Title Case headings and buttons, numerals for counts, specific labels, errors with the fix, second person, & in tight spaces.
- [[topics/modals-and-popovers|Modals and popovers]]: overscroll-behavior: contain on modals, drawers and sheets; confirmation modal before destructive actions.
- [[topics/toasts-and-notifications|Toasts and notifications]]: Async messages such as toasts use role="status" aria-live="polite"; an undo toast can replace a confirmation for deletes.

## Notable Claims

- :focus triggers on any focus including mouse clicks, while :focus-visible only triggers for keyboard navigation. Evidence: The Rule: :focus-visible, Not :focus
- Removing outline on focus without a replacement breaks keyboard navigation. Evidence: Never Remove Focus Without Replacement
- Correct input types trigger the right keyboard on mobile, and meaningful names help password managers. Evidence: Input Types and Attributes
- Blocking paste is an accessibility violation and user hostile. Evidence: Never Block Paste
- Images are the number one cause of layout shift (CLS). Evidence: 3. Images
- touch-action: manipulation removes the 300ms tap delay on mobile. Evidence: Tap Delay Removal
- Reading offsetHeight in render forces synchronous layout recalculation. Evidence: Avoid Layout Reads in Render
- Controlled inputs re-render on every keystroke; uncontrolled inputs do not. Evidence: Uncontrolled Inputs When Possible
- onClick navigation breaks Cmd+click and middle-click. Evidence: Links Support Browser Features
- user-scalable=no or maximum-scale=1 disables zoom and is an accessibility violation. Evidence: 9. Anti-Patterns Checklist

## Quotes

> Images are the #1 cause of layout shift (CLS). Fix them.

> URL should reflect app state.

> These patterns are the difference between "works" and "feels right."

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Web and React specific; native platforms are not covered.
- Caveat: Library recommendations (virtua, react-window, nuqs, Next.js Image) are examples, not requirements.
- Caveat: The 300ms tap delay claim reflects older mobile browser behaviour; the source does not date it [inferred].
- Caveat: The Title Case rule here conflicts with sentence-case button examples in the same repo's copywriting guide [inferred].

### Rules and practices

- **must** (accessibility, css): Style focus rings with :focus-visible, not :focus, for example a 2px outline in the primary color with a 2px offset. Why: :focus also fires on mouse click, which is annoying; :focus-visible fires only for keyboard navigation. Values: outline: 2px solid var(--primary), outline-offset: 2px. [The Rule: :focus-visible, Not :focus]
- **must** (accessibility, css): Never set outline: none without a visible replacement such as a two-ring box-shadow on :focus-visible. Why: It breaks keyboard navigation. Values: box-shadow: 0 0 0 2px var(--bg), 0 0 0 4px var(--primary). [Never Remove Focus Without Replacement]
- **should** (components, css): Use :focus-within on compound controls, such as a search input with an icon, to highlight the wrapper. Why: Focus on any child should highlight the parent. Values: box-shadow: 0 0 0 3px var(--primary-tint). [Compound Controls: :focus-within]
- **must** (components, web): Set the correct input type, inputmode and autocomplete on every field (email, tel, url, numeric; current-password for login, new-password for signup; off for non-auth fields). Give fields meaningful name attributes. Why: Correct types trigger the right mobile keyboard, and meaningful names help password managers. Values: email, current-password, new-password, name, tel, street-address, cc-number, cc-exp, cc-csc, off. [Autocomplete Matters]
- **must** (accessibility, web): Never block paste in inputs. Why: It is an accessibility violation and user hostile. [Never Block Paste]
- **should** (components, web): Turn spellcheck off for emails, codes, usernames and URLs. Why: The source lists these fields for spellcheck off; it gives no further reason. Values: spellcheck="false". [Disable Spellcheck Where Appropriate]
- **should** (components, web): Make labels clickable and let a checkbox and its label share a single hit target with no dead zone between them. Why: Clickable labels and a shared checkbox hit target leave no dead zones between control and label. Values: gap: 8px. [Labels and Hit Targets]
- **consider** (content, web): End placeholders with an ellipsis and show the expected format. Why: Placeholders should show format. Values: name@company.com…, (555) 123-4567…, Search products…. [Placeholder Formatting]
- **should** (components, react): Keep the submit button enabled until the request starts, then disable it and show a spinner. Why: Shows submission state. [Submit Button States]
- **should** (components, react): Show errors inline, tie them to inputs with aria-invalid and aria-describedby, use role="alert", and focus the first error on submit. Why: The source shows this as the correct pattern without stating a reason. Values: aria-invalid, aria-describedby, role="alert". [Error Handling]
- **should** (patterns, web): Warn before the user leaves a page with unsaved changes. Why: Prevents lost work [inferred]. Values: beforeunload. [Unsaved Changes Warning]
- **must** (platforms, web): Always set width and height on images. Why: It reserves space and prevents layout shift. Values: width="400" height="300". [Always Set Dimensions]
- **should** (platforms, web): Load above-the-fold images with fetchpriority="high" (priority in Next.js) and lazy-load images below the fold. Why: Loading strategy by position. Values: fetchpriority="high", loading="lazy". [Loading Strategy]
- **should** (platforms, css): Set touch-action: manipulation to remove the mobile tap delay. Why: Removes the 300ms tap delay. Values: touch-action: manipulation, 300ms. [Tap Delay Removal]
- **consider** (platforms, css): Set the tap highlight color intentionally instead of just disabling it. Why: Set intentionally, don't just disable. Values: -webkit-tap-highlight-color: rgba(0, 0, 0, 0.1). [Tap Highlight]
- **should** (components, css): Set overscroll-behavior: contain on modals, drawers and sheets. Why: Prevents scroll chaining. Values: overscroll-behavior: contain. [Modal Scroll Lock]
- **should** (components, web): Autofocus only on desktop, on at most one primary input per page, and only when justified. Why: On mobile it opens the keyboard unexpectedly. [AutoFocus Rules]
- **should** (platforms, react): Virtualize lists with 50+ items, or use content-visibility: auto with contain-intrinsic-size for simpler cases. Why: Prevents jank. Values: 50+, content-visibility: auto, contain-intrinsic-size: 0 50px. [Virtualize Large Lists]
- **should** (platforms, react): Do not read layout (offsetHeight) during render; use ResizeObserver or CSS. Why: It forces synchronous layout recalculation. [Avoid Layout Reads in Render]
- **consider** (platforms, react): Prefer uncontrolled inputs and read the value on submit when possible. Why: Controlled inputs re-render on every keystroke. [Uncontrolled Inputs When Possible]
- **consider** (platforms, web): Preconnect to asset and font domains and preload critical fonts. Why: Performance pattern. Values: rel="preconnect", rel="preload", as="font", type="font/woff2". [Preconnect to CDNs]
- **must** (accessibility, web): Use <button> for actions and <a> for navigation instead of clickable div or span. Why: Semantic elements are a high-impact accessibility win. [Semantic Elements]
- **must** (accessibility, react): Give custom interactive elements role, tabIndex={0} and Enter/Space key handlers. Why: Interactive custom elements need keyboard support. Values: role="button", tabIndex={0}, Enter,  . [Keyboard Handlers]
- **must** (accessibility, web): Keep heading levels in order without skipping (h1, h2, h3). Why: Skipping levels is wrong. [Heading Hierarchy]
- **should** (layout, css): Set scroll-margin-top on anchor targets to the fixed header height plus a buffer. Why: Prevents the fixed header from covering anchor targets. Values: scroll-margin-top: 80px. [Scroll Margin for Anchors]
- **must** (accessibility, web): Announce async updates such as toasts and validation messages with role="status" aria-live="polite". Why: Async updates need announcements. Values: role="status", aria-live="polite". [Async Updates Need Announcements]
- **should** (patterns, web): Keep filters, tabs and pagination in the URL. Why: Users expect to bookmark, share and use the back button. [URL Reflects State]
- **must** (patterns, web): Use real links, not onClick handlers, for navigation. Why: onClick navigation breaks Cmd+click and middle-click. [Links Support Browser Features]
- **must** (patterns, all): Put a confirmation modal or an undo window in front of destructive actions. Why: Immediate destructive actions are an anti-pattern. Values: Undo (10s). [Destructive Actions Need Confirmation]
- **should** (content, all): Write copy in active voice and second person ("Your account"), use Title Case for headings and buttons, numerals for counts ("8 deployments"), specific labels ("Save API Key" not "Continue"), errors that include the fix, and & instead of "and" where space is tight. Why: Content copy rules that convert. [8. Content Copy Rules]
- **must** (accessibility, web): Never disable zoom with user-scalable=no or maximum-scale=1. Why: It is an accessibility violation. Values: user-scalable=no, maximum-scale=1. [9. Anti-Patterns Checklist]
- **must** (motion, css): Do not use transition: all. Why: It is a performance killer and unpredictable. Values: transition: all. [9. Anti-Patterns Checklist]
- **must** (accessibility, web): Give every icon-only button an aria-label and every input a label. Why: Missing labels are an accessibility fail. Values: aria-label. [9. Anti-Patterns Checklist]
- **should** (content, web): Format dates and numbers with Intl.DateTimeFormat and Intl.NumberFormat instead of hardcoding. Why: Hardcoded formats are an anti-pattern. Values: Intl.DateTimeFormat, Intl.NumberFormat. [9. Anti-Patterns Checklist]

### Decisions it informs

- When people delete something, should they confirm first or get an undo? (`Q-form-05`)
  - Confirmation modal: An extra step before the action runs. When: Destructive actions such as deleting an account.
  - Undo window: The action runs, and a toast offers "Undo (10s)". When: When the action can be reversed for a short time.
  - Immediate action: No safety net. When: Never for destructive actions.
  - Recommendation: Either a confirmation or an undo window; never immediate.
- Sentence case or Title Case for headings and buttons? (`Q-voice-03`)
  - Title Case: "Save Changes". When: The guide's recommendation.
  - Sentence case: "Save changes". When: Not this guide's choice.
  - Recommendation: Title Case for headings and buttons.
- Should the submit button ever be disabled? (`Q-form-02`)
  - Enabled until the request starts: Clickable while filling in; shows a spinner and disables during submission. When: The guide's pattern.
  - Recommendation: Enabled until the request starts, then disabled with a spinner.
- How should long lists render?
  - Virtualized list (virtua, react-window): Only visible rows render. When: 50+ items.
  - CSS content-visibility: auto: Browser skips off-screen rendering. When: Simpler cases.
  - Recommendation: Virtualize lists with 50+ items.

### Process

1. Review against the anti-patterns list: During code review flag disabled zoom, paste blocking, transition: all, bare outline: none, div navigation, div buttons, images without dimensions, unvirtualized 50+ lists, unlabelled inputs, icon buttons without aria-label, hardcoded formats and unjustified autoFocus.
2. Run the pre-ship checklist: Check focus, form attributes and labels, image dimensions and lazy loading, touch settings, list virtualization, semantic HTML and headings, URL state and links, and copy rules.

### Examples and visual references

- Two-ring custom focus: box-shadow: 0 0 0 2px var(--bg), 0 0 0 4px var(--primary) draws a background-colored gap and then a primary ring around the control.
- Search wrapper with :focus-within: The whole search field border turns primary with a 3px tinted halo when the inner input is focused.
- Undo toast: "Account deleted. Undo (10s)" instead of a confirm dialog.
- URL state: /products?category=shoes&sort=price&page=2 keeps filters, sort and page shareable.

### Numbers

- 2px: Focus outline width and offset. [outline: 2px solid var(--primary); outline-offset: 2px]
- 300ms: Mobile tap delay removed by touch-action: manipulation. [Remove 300ms tap delay on mobile]
- 50+: List length above which to virtualize. [Lists with 50+ items should be virtualized]
- 80px: Example scroll-margin-top for anchor targets under a fixed header. [scroll-margin-top: 80px]
- 10s: Example undo window after a destructive action. [Account deleted. Undo (10s)]
- 8px: Gap between checkbox and label in a shared hit target. [.checkbox-wrapper gap: 8px]

<!-- /od:learn -->
