---
type: synthesis
title: Forms and inputs
created: 2026-09-24
updated: 2026-09-24
sources:
  - AH_ugxmLeUM
  - B7k5rOgmOGY
  - EcbgbKtOELY
  - HE4rLEQpiXY
  - If7iCPDy2vk
  - PDcQJOPby1k
  - ek-building-a-drawer-component
  - eks-skills-apple-design-skill
  - eks-skills-mobile-native-skill
  - eks-skills-pick-ui-library-skill
  - gKM6b2EnW1k
  - ld1zhQMXxXU
  - neE6wOuBIP8
  - vaul-api
  - vaul-inputs
tags:
  - od-area-components
---
# Forms and inputs

## In short

Forms are where people type and choose, so the labels must stay visible and the page must not jump or zoom while they work. Put each label above its field and use the placeholder for a realistic example, never as the label. On phones, input text is at least 16px so iOS does not zoom in, and each field asks for the right keyboard, such as numbers for a code. Check answers as people go rather than only when they press submit, and show a problem next to its field with a red border and a message. Show the common fields first and tuck advanced options away.

## House standards

- `STD-mobile-touch-11` (must): Form inputs at 16px or larger.
- `STD-accessibility-motion-27` (must): Never disable pinch zoom.
- `STD-mobile-touch-13` (should): Open the right software keyboard per field.
- `STD-visual-details-49` (must): Feedback on every action. (this includes validating form input inline rather than on submit)
- `STD-visual-details-31` (should): Show the common path first.
- `STD-visual-details-32` (should): Controls sit near what they change.
- `STD-visual-details-35` (should): Keep interface copy plain and concise.
- `STD-visual-details-41` (should): Ask for private data carefully.
- `STD-accessibility-motion-16` (must): Build overlays on accessible primitives. (selects included)
- `STD-visual-details-55` (must): Pick libraries from the curated list. (the curated list names input-otp for code inputs)
- `STD-components-toasts-drawers-45` (should): Keep drawer inputs above the keyboard.
- `STD-components-toasts-drawers-48` (should): Fixed-pixel snap points for inputs.
- `STD-mobile-touch-10` (must): Size full-height layouts with dvh and svh.
- `STD-mobile-touch-61` (must): Follow the keyboard frame by frame.

## What the sources teach

### Labels and placeholders

- Kole Jain calls a sign-up modal "awful" even though it looks fine, and its first problem is labels used as placeholders inside the inputs: halfway through typing, people forget what the field was. Move the labels above the inputs where they are always visible, and fill the placeholder with a realistic example of the expected entry [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- The same sign-up fix adds a "create account" subheading and a small link to log in instead, lays the modal out on a 4px grid (Kole Jain's personal rule for sign-up and log-in modals), and gives inputs an off-white fill with a 40%-opacity stroke [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).

### States

- Inputs need a focus state when someone clicks in, an error state with a red border and a message when something is wrong, and a warning state for optional issues. Inputs matter even more than buttons for answering what the person did [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- Color should carry meaning; a focus state on an input is one of the examples of color with a purpose [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- A checkbox's off state stays plain (a thin border, no color, no icon); fill, color and a checkmark belong only to the on state, because the change of color is the whole signal [S-L19-080] ([[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]).

### When to check answers

- Validate form input inline, not on submit [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]).

### Phones: zoom, keyboards and the viewport

- iOS Safari zooms the page when an input's text is under 16px and does not zoom back out, leaving a cropped layout. Set `input`, `textarea` and `select` to at least 16px, or apply the 16px only under `(pointer: coarse)` if desktop needs smaller text. Never switch off pinch zoom to hide the problem [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- Ask for the right keyboard: `inputmode="numeric"` for codes, `inputmode="decimal"` for amounts, `type="email"` and `type="tel"`, `autocapitalize="none"` and `autocorrect="off"` on usernames and codes, and `enterkeyhint` ("send", "search", "done") so the return key says what it does. Test with the keyboard open, and with `interactive-widget=resizes-content` in the viewport tag so Android resizes the layout like iOS [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- An input inside a drawer makes the browser scroll and hide content when the keyboard opens. Vaul switches that off and uses the Visual Viewport API to keep the drawer just above the keyboard, and a fixed-pixel snap point makes an input peek out by the same amount on every device [S-L19-005] ([[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]]). The docs expose this as `repositionInputs` [S-L19-096] ([[sources/vaul-inputs-inputs-vaul|Inputs – Vaul]]), on by default [S-L19-093] ([[sources/vaul-api-api-reference-vaul|API Reference – Vaul]]).

### Show less at once

- In a create form, collapse the advanced options by default and add missing ones (a custom domain switch, a description) in a layout that lets more fields slot in. When a side flyout holds only a few fields, a modal fits better [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- Start from what the person intends. For a rental search, build the search bar first (destination, travelers, dates) before any cards or icons, and reveal more only as it is needed; once browsing becomes the priority, shrink the search bar and let it animate open on click [S-L19-054] ([[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]]).
- A search bar can collapse into its magnifying-glass icon and expand on click, as Apple does [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).
- A screen of preset choices needs a search field for choices that are not listed and a skip button for people to whom none apply [S-L19-045] ([[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]]).

### Forms inside products

- User input is one of four building blocks of a dashboard, showing up in modals such as "create link" and in settings pages. Notion's settings modal is mostly lists with some inputs, and Vercel puts form inputs inside cards [S-L19-047] ([[sources/B7k5rOgmOGY-everything-you-need-to-know-to-build-a-dashboard-ui-in-8-minutes-beginner-friendly|EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)]]).
- Multi-step forms can keep people engaged with a smooth progress bar, as in Linear [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).

### Prompt boxes for AI products

- A good prompt box is a control panel, not just a field: previews for attached PDFs and images, large pastes collapsed into a compact block, mode chips, buttons for context and integrations, an advanced-mode toggle and a token-cost estimate above the input. Keep inline editing short, with a few quick selectors and shortcuts [S-L19-055] ([[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]]).

### Libraries

- For one-time password and verification code inputs, the curated pick is input-otp; dialogs, menus and selects come from base-ui [S-L19-029] ([[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]]).

## Where they agree and disagree

- **Labels.** Kole Jain's labels-above rule [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]) matches OpenDesigner's research exactly: DC-L13-05 rejects placeholder-as-label, and DC-L08-16 defaults to top labels.
- **When to validate.** The house standard, from the Apple-design skill [S-L19-020] ([[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]]), says validate inline rather than on submit (`STD-visual-details-49`). OpenDesigner's research does not agree with itself: DC-L13-06 recommends validating when the person leaves a field ("reward early, punish late"), which is Q-form-02's default, while DC-L08-17 defaults to validating on submit, with blur checks only for formats. Validation on blur is inline, so DC-L13-06 fits the standard; a submit-only form would not [inferred].
- **Error messages.** The red border plus a message [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]) fits DC-L13-07's inline pattern. DC-L13-07 also asks for an icon or text so the error does not rely on color alone; the message covers that.
- **Field style.** An off-white fill with a 40%-opacity stroke [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]) sits between Q-form-01's outlined default and its filled option. DC-L08-16 notes borders need 3:1 contrast, and a 40%-opacity stroke may not reach it [inferred].
- **Spacing.** Kole Jain's 4px grid [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]) matches the 4-based options in Q-space-01.
- **Disabling submit.** None of these sources covers it. DC-L08-10 says do not disable submit buttons; explain the problem instead.

## Decisions this informs

- **Q-form-01** (border or fill, label placement): labels on top, realistic placeholders.
- **Q-form-02** (when to check answers): inline, which rules out checking only on submit [inferred].
- **Q-form-03** (where errors show up): inline, next to the field, with a red border and a message.
- **Q-pattern-03** (show everything or tuck extras away): collapse advanced options.
- **Q-pattern-01** (modal, panel or pop-up): a modal for a short create form.
- **Q-type-08** (body text size): inputs need 16px on touch even if body text is smaller [inferred].
- **Q-space-01** (base spacing unit): a 4px grid for forms.
- **Q-state-03** (focus ring): every input needs a visible focus state; the sources give no ring values.
- **Q-ai-01** (how people spot and fix AI work): prompt-box controls and inline editing [S-L19-055] ([[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]]).

## Visual examples worth showing

- The sign-up modal before (labels inside the fields) and after (labels above, example placeholders, log-in link, 4px spacing) [S-L19-075] ([[sources/gKM6b2EnW1k-upgrading-9-crucial-ui-elements-free-figma-file-included|Upgrading 9 CRUCIAL UI Elements (free figma file included)]]).
- An input under 16px that zooms the iPhone page on focus next to a 16px one that does not [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- A row of phone keyboards: numeric, decimal, email, phone, and a return key labeled "send" [S-L19-028] ([[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]]).
- A drawer with an input kept above the keyboard, against the browser default [S-L19-096] ([[sources/vaul-inputs-inputs-vaul|Inputs – Vaul]]).
- One input in default, focus, error and warning states [S-L19-052] ([[sources/EcbgbKtOELY-every-ui-ux-concept-explained-in-under-10-minutes|Every UI/UX Concept Explained in Under 10 Minutes]]).
- A checkbox off and on, next to six chips that are all colored in their default state [S-L19-080] ([[sources/neE6wOuBIP8-the-secret-behind-weirdly-perfect-ui-designs|The secret behind weirdly perfect UI designs]]).
- A create-link modal with advanced options collapsed [S-L19-061] ([[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]]).
- An AI prompt box with attachment previews and mode chips [S-L19-055] ([[sources/If7iCPDy2vk-the-7-ui-components-to-design-like-unicorn-ai-startups|The 7 UI Components to Design Like Unicorn AI Startups]]).
- A Linear-style form progress bar drawing itself in [S-L19-079] ([[sources/ld1zhQMXxXU-11-micro-animations-that-will-instantly-level-up-your-ui-free-figma-file|11 Micro Animations That Will Instantly Level Up Your UI (free figma file)]]).

## Open questions

- Should blur-time validation cover every rule the client can check, or only formats as Q-form-02's default says? DC-L19-111 proposes every rule, to meet `STD-visual-details-49`.
- Does a 40%-opacity input stroke meet the 3:1 contrast DC-L08-16 asks for, and in which themes?
- How should required and optional fields be marked? None of these sources covers it.
- Are floating labels acceptable? None of these sources evaluates them.
- What should native iOS and Android forms follow, since the input rules here are web-only?
