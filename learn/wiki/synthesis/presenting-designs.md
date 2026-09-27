---
type: synthesis
title: Presenting designs
created: 2026-09-24
updated: 2026-09-24
sources:
  - 7cTdCu8HMgM
  - ek-building-a-toast-component
  - eks-skills-prototype-picker
  - eks-skills-prototype-skill
  - t7mpEDXzjCg
tags:
  - od-area-process
---

# Presenting designs

## In short

The same design is judged differently depending on how it is shown, so the way you present it is part of the work. Who is looking decides the method. A portfolio or social post can use creative showcase shots; a client needs the design in a realistic setting and a working prototype; and a person choosing between options needs each one shown alone, full size, in context, with neutral tool chrome around it and no favorite picked for them. When you document decisions, show the screens large with the reason written next to each one. The rules for comparing options come from Emil Kowalski's prototype skill and are locked house standards; the showcase and client techniques come from Kole Jain's videos and are practitioner opinion.

## House standards

- `STD-process-review-taste-43` (must): show prototype variants one at a time, full size, in realistic surrounding context, never as side-by-side thumbnails.
- `STD-process-review-taste-44` (must): switching between variants is instant, with no transition.
- `STD-process-review-taste-45` (must): the variant picker is fixed chrome, built verbatim from its spec and never restyled with the project's tokens.
- `STD-process-review-taste-46` (must): the picker's keys, URL parameter and re-mount behavior follow a fixed contract.
- `STD-process-review-taste-47` (must): run and flip through every variant, and screenshot each one when possible, before showing them.
- `STD-process-review-taste-48` (must): hand off variants as a table (#, Variant, Axis, When it's the right choice, Its cost), never pre-pick a favorite, say where the picker runs and which keys flip it, then stop.
- `STD-process-review-taste-40` (must): every variant fully works, with realistic product-shaped copy and no lorem ipsum or dead buttons.
- `STD-process-review-taste-59` (must): teach motion with interactive demos people can touch, including bad-versus-good examples.
- `STD-process-review-taste-60` (should): documentation is part of the product, with interactive examples and ready-to-use code.
- `STD-process-review-taste-04` (must): report review findings as one table with Before, After and Why columns.
- `STD-visual-details-25` (must): when prototyping with no project tokens, use a restrained look: neutral grays, one accent and the system font stack.

## What the sources teach

### Match the method to the audience

- Presenting is "half a design": the same UI looks better when it is presented well. Creative showcase techniques suit portfolios and social media; in client meetings the goal changes from impressing people to building confidence in the product, so the design is shown where it will actually be used [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).

### Showcase shots for portfolios and social media

- Start with a plain, fairly bland background; it works for nearly any design because the design itself stands out. For a light-mode design, take the accent color and darken and desaturate it, then add a faint shadow; a bright background would compete with the UI. For a dark-mode design, large blurred circles of the accent behind the UI give a soft glow, and a glassy backdrop with a soft gradient stroke adds depth [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).
- To add interest, let the design or its pattern run off the frame ("exploding the image"), skew it slightly (the example uses 2° vertical and -14° horizontal) and pop one part out with an offset and a shadow [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]). The skew values are one example, not a standard.
- Several screens look better offset and slid off the page, or arranged in a collage that deliberately does not line up in a grid; stacking them is boring. Collages need large designs such as landing pages; a dashboard is better shown by zooming into one section and animating it lightly [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).
- Photos belong in a showcase only if they are relevant and don't distract, which mostly suits physical products [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).

### Client presentations: realistic context and working prototypes

- Put the design in a device mockup; even a plain computer frames it well. A lifestyle mockup, with the UI in use on an iPad or Apple Watch, goes further [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).
- The presenter does not think AI is good at thoughtful UIs but finds it good at mockup scenes: a prompt of about 30 words for the latest Apple device with a green screen, then the green is cut out and the design skewed in, gave a custom mockup in two minutes. Small details in the scene, such as a crack or a water stain, sell it [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).
- "Don't describe, show": a working prototype lets the client feel the experience and reveals hidden details such as swipe actions, a modal animating in, or the sequence when a link is deleted [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).

### Launching and documenting a component

- When Sonner launched, its announcement videos focused on the stacking animation, the feature people loved most [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- Its documentation is a custom site with live examples to play with and code to copy, built with care rather than as an afterthought, because good docs drastically lower the barrier to using a product [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).

### Showing options so a person can choose

- Show one variant at a time, full size, in realistic surroundings: a toast needs a page behind it, a card needs siblings, a button needs a form. Side-by-side thumbnails distort spacing and scale [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).
- Switching is instant, with no transition, because people flip between variants more than 100 times in a session [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).
- The switcher is a dark glass pill fixed at the bottom center of the screen. It is copied verbatim every time and never styled with the project's fonts, colors or theme, so it always reads as a tool and never as part of the design being judged. It moves to the top only when a variant uses the bottom center (a toast stack, a bottom sheet), and a replay button appears only when some variant has motion worth re-running [S-L19-030] ([[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]).
- The chosen variant survives a reload through a `?v=` URL parameter, and every switch re-mounts the variant so its entrance animation plays again [S-L19-030] ([[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]).
- The hand-off is a table of each variant's axis, when it is the right choice and what it costs, followed by where the picker runs and which keys flip it. The agent does not pick a favorite; if asked, it answers from the product's personality and how often the piece is used, not from looks alone [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).

### Documenting design decisions

- In a case study, show final designs as large as reasonably possible with text beside each one explaining why; squeezing many screens together hides the detail. Clickable tabs are one way to group screens [S-L19-083] ([[sources/t7mpEDXzjCg-make-a-perfect-ux-case-study-in-8-steps|Make A Perfect UX Case Study In 8 Steps]]).
- Keep the text short and use many images and GIFs. Charts need a title, axis titles and a legend, and circling and annotations help people read them [S-L19-083] ([[sources/t7mpEDXzjCg-make-a-perfect-ux-case-study-in-8-steps|Make A Perfect UX Case Study In 8 Steps]]).

## Where they agree and disagree

Between the sources:

- **Show, don't describe:** all agree. Client prototypes [S-L19-041], fully working variants [S-L19-031], interactive docs [S-L19-006] and the house rule on touchable demos (`STD-process-review-taste-59`) point the same way.
- **Real size and real context:** the case study shows final designs large [S-L19-083], client mockups show the design where it will be used [S-L19-041], and the prototype skill never shows thumbnails [S-L19-031].
- **Showcases break the comparison rules, on purpose:** collages, skews and off-frame crops [S-L19-041] shrink, rotate and cut designs, which `STD-process-review-taste-43` forbids when someone is judging options. A showcase sells finished work; a picker helps someone decide. Anything OpenDesigner shows for a decision follows the standard [inferred].
- **Where color may come from:** the showcase background is tinted from the design's own accent [S-L19-041], while the picker must never take the project's colors [S-L19-030]. One is a backdrop for a finished shot and the other is tool chrome, so both rules can hold [inferred].

Against OpenDesigner's existing research and files:

- **Side-by-side grids conflict with the house standard:** DC-L16-05 defaults to a "show 6" grid that renders the same sample once per variant, DC-L17-05 renders light and dark side by side, and DC-L16-06 wants every mode visible at once or one keystroke away. The option-gallery template shows 3 to 8 directions side by side, a conflict already recorded on `STD-process-review-taste-43` and `STD-process-review-taste-38`. Under the standards policy the house standard wins for comparing variants of one UI piece; the recorded note leaves open whether a gallery of whole design-system directions counts [inferred].
- **Recommending conflicts with not pre-picking:** OpenDesigner's `rules.md` rule 5 ("Recommend one with a short reason") and the gallery's "Recommended" badge pre-pick a favorite, which `STD-process-review-taste-48` forbids in a prototype hand-off. The conflict note on that standard scopes it to prototype hand-offs, not interview questions.
- **Rendered previews agree:** DC-L17-11 says decisions should be made on rendered components, with raster images only for labelled mood boards. That matches the prototype skill's fully working variants [S-L19-031]. AI mockup scenes [S-L19-041] are raster images for a client meeting, not for decisions [inferred]; when suggesting an AI image tool, the guardrails require a note on who owns AI-generated assets (`guardrails.md`, section 3).
- **Docs agree:** DC-L11-18's component page template (a live demo, usage, code and accessibility) matches Sonner's interactive docs with copyable code [S-L19-006].

## Decisions this informs

- **Q-pref-02** (planned, not asked yet: how to review AI changes and try other versions): the house standards favor one variant at a time behind a picker, which none of its options (`patches`, `staged`, `lock-shuffle`, `show-6`) names; `show-6` conflicts with `STD-process-review-taste-43` [inferred].
- **Q-dist-04** (where the docs live and what each component page shows): Sonner's custom docs site with live examples and copyable code [S-L19-006] backs `custom-site` or a template that includes a live demo.
- **Q-scope-06** (what the screens are for): a portfolio or showcase site is `experience`, which is where the showcase techniques of [S-L19-041] belong [inferred].

## Visual examples worth showing

- One dashboard presented eight ways, from a muted accent-tinted background to a skewed pop-out, a collage, a lifestyle mockup and a prototype; the video links its Figma files [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).
- A light-mode shot on a darkened, desaturated accent background beside a dark-mode shot with a blurred accent glow [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).
- The AI-generated MacBook Air scene on an orange faux leather chair, before and after the design is keyed into the green screen [S-L19-041] ([[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]]).
- The prototype picker: a dark glass pill at the bottom center with numbered variants, the sliding highlight and the replay button, shown over both a light and a dark page [S-L19-030] ([[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]]).
- A hand-off table with example rows such as "Quiet" (minimal motion, borders over shadows; right for a daily-use tool; cost: least memorable) and "Editorial" (large type, generous space; cost: uses vertical space) [S-L19-031] ([[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]]).
- Sonner's docs page, with Preview and Code tabs, a live "Render toast" button and a Copy Code link, as shown in the article's screenshot [S-L19-006] ([[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]]).
- A case-study final-design section with a large screen and its reasoning beside it, grouped by clickable tabs [S-L19-083] ([[sources/t7mpEDXzjCg-make-a-perfect-ux-case-study-in-8-steps|Make A Perfect UX Case Study In 8 Steps]]).

## Open questions

- Does the one-at-a-time rule (`STD-process-review-taste-43`) cover OpenDesigner's gallery of whole design-system directions, or only variants of one UI piece? The standard's own conflict note leaves this open.
- Should Q-pref-02 gain a "picker, one at a time" option, and should `show-6` be removed or limited to a quick first look?
- The showcase techniques were only described for web and dashboard designs. How should native mobile apps be shown to clients, beyond device and lifestyle mockups?
