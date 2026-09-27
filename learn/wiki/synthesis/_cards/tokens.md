---
type: synthesis
title: "L19 Decision Cards: tokens (stages 05, 24)"
tags:
  - decision-cards
  - tokens
---

# L19 Decision Cards: tokens (stages 05, 24)

Lane: L19 (learning wiki). Area: tokens, covering the topics Design systems and tokens, and Web implementation (CSS and React) (OpenDesigner stages 05 where the system lives, and 24 tokens and encoding). Cards DC-L19-181 to DC-L19-190. Written 2026-09-24.

Built from every verified analysis tagged with these two topics in `learn/analysis/` (42 sources), checked against the raw text in `learn/raw/` where a card relies on a detail, and compared with the existing cards DC-L07-01 to DC-L07-28, DC-L03-26, DC-L04-21, DC-L04-22, DC-L04-28, DC-L08-03, DC-L09-08, DC-L10-08, DC-L10-18, DC-L10-22, DC-L11-01, DC-L11-16, DC-L11-23 and DC-L16-02, with `questions.json`, the stage 05 and 24 files, `pacing.json`, `synthesis/standards.json`, and `engine.py` where a card says what the engine does today.

How to read the authority: Emil Kowalski's sources are house standards (STD ids, locked). Vaul is a recommended default. Kole Jain and Steve Schoger videos are trusted practitioner opinion; a number or an always/never rule from a single video is labelled as opinion unless another source or existing research agrees. My own connections are marked [inferred]. Engine facts marked "checked" were read in `skills/opendesigner/scripts/engine.py` on 2026-09-24.

Sources read but not cited here: [S-L19-042] (its fluid type and ratio are covered by DC-L19-31 and the typography cards), [S-L19-002] (course outline and background only), the motion and build sources [S-L19-010], [S-L19-019], [S-L19-069] and [S-L19-071], which hold no token or delivery decision that the motion cards do not own, and [S-L19-030], [S-L19-087], [S-L19-088] and [S-L19-093] (the prototype picker, Sonner setup and Vaul's part list, which the component and process cards own).

## Sources used

- [S-L19-001] [[sources/adev-changelog-animations-dev|animations.dev]] (non-negotiable)
- [S-L19-003] [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]] (non-negotiable)
- [S-L19-004] [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]] (non-negotiable)
- [S-L19-005] [[sources/ek-building-a-drawer-component-building-a-drawer-component|Building a drawer component]] (non-negotiable)
- [S-L19-006] [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]] (non-negotiable)
- [S-L19-007] [[sources/ek-building-an-animation-course-building-an-animation-course|Building an animation course]] (non-negotiable)
- [S-L19-013] [[sources/eks-performance-cheatsheet-emilkowalski-skills-performance-cheatsheet-md|emilkowalski/skills: performance-cheatsheet.md]] (non-negotiable)
- [S-L19-017] [[sources/eks-skills-animate-recipes-emilkowalski-skills-skills-animate-recipes-md|emilkowalski/skills: skills/animate/RECIPES.md]] (non-negotiable)
- [S-L19-018] [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]] (non-negotiable)
- [S-L19-020] [[sources/eks-skills-apple-design-skill-emilkowalski-skills-skills-apple-design-skill-md|emilkowalski/skills: skills/apple-design/SKILL.md]] (non-negotiable)
- [S-L19-021] [[sources/eks-skills-ask-sonner-api-emilkowalski-skills-skills-ask-sonner-api-md|emilkowalski/skills: skills/ask-sonner/API.md]] (non-negotiable)
- [S-L19-022] [[sources/eks-skills-ask-sonner-skill-emilkowalski-skills-skills-ask-sonner-skill-md|emilkowalski/skills: skills/ask-sonner/SKILL.md]] (non-negotiable)
- [S-L19-023] [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] (non-negotiable)
- [S-L19-024] [[sources/eks-skills-find-animation-opportunities-skill-emilkowalski-skills-skills-find-animation-opportunities-skill-md|emilkowalski/skills: skills/find-animation-opportunities/SKILL.md]] (non-negotiable)
- [S-L19-025] [[sources/eks-skills-improve-animations-audit-emilkowalski-skills-skills-improve-animations-audit-md|emilkowalski/skills: skills/improve-animations/AUDIT.md]] (non-negotiable)
- [S-L19-026] [[sources/eks-skills-improve-animations-plan-template-emilkowalski-skills-skills-improve-animations-plan-template-md|emilkowalski/skills: skills/improve-animations/PLAN-TEMPLATE.md]] (non-negotiable)
- [S-L19-027] [[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]] (non-negotiable)
- [S-L19-028] [[sources/eks-skills-mobile-native-skill-emilkowalski-skills-skills-mobile-native-skill-md|emilkowalski/skills: skills/mobile-native/SKILL.md]] (non-negotiable)
- [S-L19-029] [[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]] (non-negotiable)
- [S-L19-031] [[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]] (non-negotiable)
- [S-L19-032] [[sources/eks-skills-review-animations-skill-emilkowalski-skills-skills-review-animations-skill-md|emilkowalski/skills: skills/review-animations/SKILL.md]] (non-negotiable)
- [S-L19-033] [[sources/eks-skills-review-animations-standards-emilkowalski-skills-skills-review-animations-standards-md|emilkowalski/skills: skills/review-animations/STANDARDS.md]] (non-negotiable)
- [S-L19-089] [[sources/sonner-other-other-sonner|Other – Sonner]] (non-negotiable)
- [S-L19-090] [[sources/sonner-styling-styling-sonner|Styling – Sonner]] (non-negotiable)
- [S-L19-091] [[sources/sonner-toast-toast-sonner|Toast – Sonner]] (non-negotiable)
- [S-L19-092] [[sources/sonner-toaster-toaster-sonner|Toaster – Sonner]] (non-negotiable)
- [S-L19-094] [[sources/vaul-default-default-vaul|Default – Vaul]] (good-to-have)
- [S-L19-095] [[sources/vaul-getting-started-getting-started-vaul|Getting Started – Vaul]] (good-to-have)
- [S-L19-044] [[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]] (reference)
- [S-L19-045] [[sources/AH_ugxmLeUM-7-ui-ux-mistakes-that-scream-youre-a-beginner|7 UI/UX mistakes that SCREAM you’re a beginner]] (reference)
- [S-L19-054] [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]] (reference)
- [S-L19-103] [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]] (reference)

Synthesis pages these cards build on: [[synthesis/design-systems-and-tokens|Design systems and tokens synthesis]] and [[synthesis/web-implementation-css-and-react|Web implementation (CSS and React) synthesis]].

## Decision Cards

### DC-L19-181: How much system to define first, and what counts as progress
- **Block path:** Tokens > Architecture > System size and first commitments
- **Questions the designer answers:** Should this system be light and easy to throw away, or deeply defined for many products? Which few decisions must hold on every screen from day one? Do we measure progress by how many components exist, or by how many decisions hold everywhere?
- **Options:**
  - **Lean core: a few decisions you stick to.** In Linear, buttons, spacing and text styles are exactly the same in a settings panel and when creating a view; in Kole's own example, holding button spacing, the type scale and the color scheme constant makes a new modal quick to build and familiar [S-L19-044]. A lean startup needs something light, flexible, quick to update and easy to scrap [S-L19-054]. The house motion vocabulary is this size: three named curves and a duration table [S-L19-018]. One video adds one shared corner radius for all small components (10px in its example) [S-L19-045]; the 10px is opinion from one video, the "one radius for the small parts" lesson is the point.
  - **Deeply defined.** Material Design is massive and deeply defined because it serves dozens of products and billions of users [S-L19-054]. In token terms this is a component tier for every part (DC-L07-02, option 2) [inferred].
  - **Count of components as the goal.** Rejected: a system is not about having hundreds of components [S-L19-044].
  - **How the core is held in the design file.** Kole: styles for colors, variables for measurements, components for UI elements [S-L19-045] (one video, June 2025). This differs from DC-L07-21, which makes every single value that changes by mode, colors included, a variable so light and dark can switch; styles stay for bundles such as text styles and shadows.
- **Visual effect:** Lean core: every new screen looks like it belongs, with few distinct paddings, radii and type sizes on show [S-L19-044]. Deeply defined: the same consistency across many products, but a change takes longer to reach the screen [inferred]. Component count as the goal: many parts that each look slightly different, which Kole calls amateur when duplicates differ [S-L19-045].
- **Depends on (upstream):** Q-scope-04 (team size and model), Q-scope-01 (which surfaces), Q-scope-02 (existing screens), DC-L11-01 (adopt, adapt or create).
- **Affects (downstream):** Q-token-01 (tier depth, whether component tokens exist at launch), Q-token-03 (coverage), which tokens are locked (`engine.py set --lock`), Q-gov-01 (how strict), what DESIGN.md reports as done.
- **Token encoding:** none new (process decision). The core commitments are ordinary semantic tokens that carry the engine's lock, for example the control padding, the `text.*` scale, the small-component radius and the surface and action colors [inferred].
- **Platform notes:** The sources give none.
- **Accessibility constraints:** However lean, the locked floors are part of the core from day one: WCAG 2.2 AA contrast, 24px minimum targets, visible focus and reduced motion (OpenDesigner guardrails).
- **Default + heuristic:** Default: a lean core. Confirms Q-token-01 `two-plus` (DC-L07-01) with component tokens added only when a brand must restyle one component or 3 or more components share a value (DC-L07-02). Confirms Q-token-03 `extended`: "lean" means few hand-made decisions, not few token categories, because the engine generates the extra categories from the same few inputs and they stay quick to update [inferred]. One exception, owned by the motion cards: motion gets per-component recipe tokens from the start, because each component has its own duration budget (DC-L19-99). Heuristic: let Q-scope-04 set the depth. `size-1-2`, `size-3-5` or `model-solitary` gets the lean core; `size-10plus`, `model-federated`, or several products sharing the system gets component tokens for the parts brands restyle [inferred from S-L19-054 and DC-L11-01]. No question asks how many products share the system; Q-scope-01 counts surfaces (app, marketing site, docs), which is only a stand-in [inferred]. Count progress in decisions held, not components built [S-L19-044], and break a rule only on purpose, never by accident [S-L19-054]. For the Figma split, keep DC-L07-21: a color that changes between light and dark must be a variable; Kole's "styles for colors" is a one-video opinion (DC-L19-173 says the same). This card is the token-depth side of DC-L19-164 (how much system the team needs, and where to stop zooming); the two agree.
- **Evidence:** [S-L19-018] [S-L19-044] [S-L19-045] [S-L19-054]; compared with DC-L07-01, DC-L07-02, DC-L07-07, DC-L07-21, DC-L11-01, DC-L11-09, DC-L19-99, DC-L19-164, DC-L19-173.
- **Maps to:**
  - Q-scope-04: new effect. Today it decides DC-L11-09 and DC-L11-10 and changes DC-L11-01, DC-L11-11 and DC-L11-12, all process and governance cards; add that it sets how deep Q-token-01 goes (lean core or component tier).
  - Q-token-01: confirms default `two-plus`; new heuristic "depth follows team size and number of products".
  - Q-token-03: confirms default `extended`; new Use/avoid line "lean means few hand-made decisions, not fewer token kinds".
  - Q-token-07 `vars-styles`: flag, no change: Kole's styles-for-colors [S-L19-045] differs from DC-L07-21; keep variables for any value that changes by mode.
  - Visual sample: Linear's settings panel beside its view-creation screen with identical buttons, spacing and text styles [S-L19-044]; a new modal assembled only from existing parts [S-L19-044].
- **Impact now / as it grows:**
  - Lean core: now, a handful of decisions and a fast first build. As it grows, local values need a promotion path to shared tokens once 3 or more components use them (DC-L07-02), and on-purpose exceptions need a written reason.
  - Deeply defined: now, slower to set up and more to review. As it grows, it pays back across many products, but it is no longer easy to scrap [S-L19-054].
  - Component count as the goal: now, it looks productive. As it grows, parts drift apart because no shared decisions hold them together [S-L19-044] [inferred].
- **Standards:** STD-visual-details-27 (every value a deliberate choice), STD-visual-details-36 (same look, same behaviour), STD-visual-details-51 (excellent defaults before options).

### DC-L19-182: Spacing on the web grows with the reader's text size (rem, not px)
- **Block path:** Tokens > Types > Dimension > Web output unit for spacing and sizes
- **Questions the designer answers:** When someone sets a larger default text size in their browser, should padding, gaps and control heights grow with the text or stay fixed? Which values should stay in pixels? Does anything change for people who never touch that setting?
- **Options:**
  - **rem (or em) for spacing on the web.** The house rule: respect the user's text-size setting and scale layout with the text, writing spacing in rem or em, not fixed px, so a larger font does not break the layout [S-L19-020] (STD-accessibility-motion-13, must). Carbon, Atlassian and Primer publish rem next to px, and Tailwind's spacing base is 0.25rem (DC-L03-26).
  - **px spacing, rem type only.** What the engine exports today: in the CSS export only `font.size.*` becomes rem, while `space.*`, control heights and target sizes stay px (checked; the conflict is recorded on STD-accessibility-motion-13). The Tailwind export goes one step further: it sets Tailwind's spacing multiplier to `--spacing: 4px` (the base unit in px, checked), replacing Tailwind's own rem-based 0.25rem (DC-L03-26), so every `p-*` and `gap-*` class becomes fixed; this part is not recorded in `standards.json`. DC-L03-26 cites a practitioner view that padding should stay px because growing spacing squeezes content, and Q-token-04 keeps "spacing scales with text size" as a toggle that is off by default. Both differ from the house standard.
  - **em inside a component.** Spacing tied to the component's own font size, which the standard also allows [S-L19-020]; for example the gap between a button's icon and label follows the label [inferred].
  - **What stays px.** The standard's review check matches only margin, padding and gap (its `review.pattern` in `standards.json`), so borders, focus rings, shadow offsets and radii can stay px, and 1px hairlines stay crisp [inferred from the review pattern].
- **Visual effect:** At the default text size nothing changes: 1rem is 16px. With a larger default text size, rem spacing keeps the proportions, so cards and buttons get roomier along with their text. With px spacing, bigger text is squeezed inside the same padding and fixed-height controls can clip their labels [inferred]. Browser zoom scales px and rem alike; only the text-size setting shows the difference [inferred].
- **Depends on (upstream):** Q-plat-01 (web is shipped), Q-space-01 (base unit), Q-token-04 (source units).
- **Affects (downstream):** every `space.*`, `size.control.*` and `size.target.*` token in the CSS export and in Tailwind's `--spacing-*` (which point at the CSS variables), container padding, the review lint's spacing message. Breakpoints are already rem in the Tailwind export, but the CSS export's `size.breakpoint.*` variables are px (checked).
- **Token encoding:** The source stays px, `{"$type": "dimension", "$value": {"value": 16, "unit": "px"}}`, so Figma import stays lossless (DC-L07-11). Only the web transform changes: `--ds-space-400: 1rem` instead of `16px`, dividing by 16 as the platform pipelines assume (DC-L10-22).
- **Platform notes:** Web only for the unit. The same standard asks native apps to respect Dynamic Type by scaling layout with text [S-L19-020] but names no mechanism for native spacing [inferred: on iOS this would be a scaled metric]. DC-L10-08's Android rule (spacing in dp, only text in sp) is not contradicted by these sources. Figma keeps px.
- **Accessibility constraints:** WCAG 1.4.4 Resize Text (200%) and 1.4.10 Reflow at 320 CSS px (DC-L03-26). A 24px minimum target written as plain 1.5rem would fall below 24 CSS px for someone who sets a default text size smaller than 16px, so write the floor as `max(24px, 1.5rem)`: it grows with larger text and never drops under the locked 24px floor [inferred].
- **Default + heuristic:** Default on the web: spacing and control heights in rem (px divided by 16); target-size floors as `max(<px>, <rem>)`; borders, rings, shadow offsets and radii in px; source values stay px. The standard names spacing only; extending it to control heights and target sizes is [inferred] from its "scale layout with the text". Differs from DC-L03-26 and the current Q-token-04 default: the toggle "spacing scales with text size, off by default" goes away on the web, because the house standard is must-level. The layout cards already write spacing in rem on the web (DC-L19-41, DC-L19-43, DC-L19-47), so this card agrees with them. Heuristic [inferred]: if the value makes room for text (padding, gap, control height), it is rem; if it draws a line, it is px; if it is a locked minimum, it is `max()` of both.
- **Evidence:** [S-L19-020]; compared with DC-L03-26, DC-L07-11, DC-L10-08, DC-L10-22.
- **Maps to:**
  - Q-token-04: new default "px in the source; rem on the web for type, spacing, control heights and breakpoints; `max(px, rem)` for target-size floors; px for borders, rings, shadows and radii". Remove "spacing scales with text size is an explicit toggle, off by default" for web output. New Use/avoid line: "avoid px margin, padding and gap on the web (STD-accessibility-motion-13)".
  - Engine (proposed): the CSS export's `css_dim` rem conversion should cover `space.*` and `size.control.*`, not only `font.size.*`, and write `size.target.*` as `max(24px, 1.5rem)` and so on; the Tailwind export should write `--spacing` as the base unit divided by 16 in rem (0.25rem for a 4px unit) instead of px.
  - Visual sample: the same card at the default text size and at a 200% default text size, once with px padding and once with rem padding.
- **Impact now / as it grows:**
  - rem: now, one transform change and no visible difference at the default size. As it grows, every new component inherits text scaling, and testing at 200% text finds fewer broken layouts.
  - px: now, nothing to change. As it grows, each component needs its own fix when text-size bugs are reported, and the review check flags every px padding.
- **Standards:** STD-accessibility-motion-13, STD-visual-details-27.

### DC-L19-183: Names for motion tokens that code, agents and the house skills share
- **Block path:** Tokens > Naming > Motion token names
- **Questions the designer answers:** Should a curve's name say its job (for things entering or leaving, for things moving on screen, for drawers) or its character (silk, breeze)? What names should the CSS export write, so a coding agent that looks for `--ease-*` finds them? Does the web need the same names as the other platforms?
- **Options:**
  - **Job names from the house vocabulary.** `--ease-out` (entering and exiting), `--ease-in-out` (moving or morphing on screen) and `--ease-drawer` (drawers and sheets) [S-L19-018] [S-L19-023] [S-L19-025] [S-L19-033]; suggestions must use this shared vocabulary [S-L19-024]; recipes consume `var(--ease-out)` [S-L19-017]; press feedback reuses the same token rather than forking a curve [S-L19-028]. Before any motion work, recon looks for `--ease-*` and `--duration-*` [S-L19-027].
  - **Role names (the engine and DC-L04-21).** DTCG `motion.easing.standard`, `enter`, `exit` and `linear`, exported as `--ds-motion-easing-enter` in CSS and `--ease-standard`, `--ease-enter`, `--ease-exit`, `--ease-linear` in the Tailwind `@theme` (checked). Carbon, Primer and Windows group curves this way (DC-L04-21).
  - **Character names.** The animations.dev library keeps 18 custom curves on `:root` with names such as `--ease-breeze` and `--ease-silk` [S-L19-007]. The six it shows all start slowly by their control points [inferred], which the names do not reveal, and the source says nothing about where each is used.
  - **Intensity names.** Fluent's min, mid and max (DC-L04-21).
- **Visual effect:** None on screen by itself. Job names make a wrong curve visible in code review: an entrance written with an exit-only or ease-in curve reads as wrong from its name [inferred].
- **Depends on (upstream):** Q-motion-03 (how curves are grouped), Q-token-02 (grammar and prefix), DC-L19-189 (existing tokens in the repo).
- **Affects (downstream):** the CSS and Tailwind exports, the DESIGN.md motion section, component recipes, the review lint (STD-visual-details-26 flags a hand-typed `cubic-bezier(` in a transition), and whether agents extend the system or add a parallel set.
- **Token encoding:** DTCG paths named by job, `$type: cubicBezier`: `motion.easing.out` = [0.23, 1, 0.32, 1], `motion.easing.in-out` = [0.77, 0, 0.175, 1], `motion.easing.drawer` = [0.32, 0.72, 0, 1] (values from STD-easing-duration-02 and STD-components-toasts-drawers-40) [inferred path names]. The CSS export writes unprefixed aliases next to the prefixed tokens, for example `--ease-out: var(--ds-motion-easing-out)`, plus `--duration-*` aliases for the duration steps [inferred].
- **Platform notes:** React Native uses constants with the same jobs: `EASE_OUT`, `EASE_IN_OUT` and `EASE_SHEET` for the drawer curve (values in STD-easing-duration-02 and STD-components-toasts-drawers-40). The sources give no Swift or Compose names.
- **Accessibility constraints:** None directly. The reduced-motion mode must still switch the aliased values (the engine switches motion by `[data-motion]` and `prefers-reduced-motion`, checked).
- **Default + heuristic:** Default: name curves by job and export the house names `--ease-out`, `--ease-in-out` and `--ease-drawer` (and `--duration-*`) as unprefixed aliases, so an agent following the house skills finds and extends them instead of adding its own [S-L19-018] [S-L19-027]. Differs from DC-L04-21 and the Q-motion-03 option `role-based` (standard, enter, exit): the house vocabulary has no separate exit curve, because exits use ease-out too (STD-easing-duration-01, STD-easing-duration-03); the value conflicts are already recorded on STD-easing-duration-02, the naming conflict is not. Differs from DC-L07-05 (prefix only in platform output) for these aliases only. Character-named curves stay out of the UI token set [inferred]. Heuristic: if a person or agent cannot tell from a curve's name whether it is for entering, moving or a drawer, rename it.
- **Evidence:** [S-L19-007] [S-L19-017] [S-L19-018] [S-L19-023] [S-L19-024] [S-L19-025] [S-L19-027] [S-L19-028] [S-L19-033]; compared with DC-L04-21, DC-L07-04, DC-L07-05, DC-L07-14, DC-L19-85.
- **Maps to:**
  - Q-token-02: new option `motion-names`: "motion tokens use the house names (`--ease-out`, `--ease-in-out`, `--ease-drawer`, `--duration-*`) as unprefixed CSS aliases"; new default for motion tokens.
  - Q-motion-03: owned by DC-L19-85 (new default "by job", `role-based` reworded to the jobs), which uses the same token paths as this card; no separate option is proposed here.
  - Engine (proposed): add the aliases to the CSS export and rename the Tailwind `--ease-enter`/`--ease-exit` pair.
  - Visual sample: the `:root` block with the three curves, each plotted [S-L19-025].
- **Impact now / as it grows:**
  - Job names: now, agents and people pick the right curve by name. As it grows, new curves slot in by job, and one edit changes every use.
  - Role names: now, fine inside OpenDesigner. As it grows, each agent session that looks for `--ease-out` and does not find it risks adding a parallel set [inferred].
  - Character names: now, expressive. As it grows, nobody knows which curve to use, and near-duplicates pile up as consolidation findings [S-L19-025].
- **Standards:** STD-visual-details-26, STD-easing-duration-01, STD-easing-duration-02, STD-easing-duration-03, STD-components-toasts-drawers-40, STD-process-review-taste-11.

### DC-L19-184: Which framework defaults stay switched on next to the system (Tailwind theme)
- **Block path:** Tokens > Delivery > Web > Framework default theme
- **Questions the designer answers:** When the system ships as Tailwind utilities, which of Tailwind's own built-in values should still exist? Should anyone still be able to type `ease-in`? Should `hover:` mean "only on a device with a mouse"?
- **Options:**
  - **Reset colors, text sizes, radii, shadows and breakpoints only (the engine today).** `exports.tailwindReset` switches those namespaces off, breakpoints only when the system defines them (checked). Tailwind's easing defaults stay: `ease-in` is cubic-bezier(0.4, 0, 1, 1), `ease-out` is (0, 0, 0.2, 1) and `ease-in-out` is (0.4, 0, 0.2, 1) [inferred; checked against Tailwind's transition-timing-function docs on 2026-09-24]. That `ease-in-out` is the exact curve the house names as one never to hand-type or approximate [S-L19-018], built-in curves are too weak [S-L19-018], and ease-in is never allowed on UI (STD-easing-duration-03).
  - **Reset easing too, and point Tailwind's names at the system.** `--ease-*: initial`, then `--ease-out`, `--ease-in-out` and `--ease-drawer` defined from the system tokens, so Tailwind's own `ease-out` and `ease-in-out` classes give the strong curves and `ease-in` no longer exists [inferred]. The bare `transition` class does not read `--ease-*`: it uses `--default-transition-timing-function`, which is cubic-bezier(0.4, 0, 0.2, 1) with a 150ms `--default-transition-duration` [inferred; checked against Tailwind's transition-property docs on 2026-09-27]. The reset leaves it alone, so it must be set to the house ease-out as well.
  - **No reset.** Tailwind's palette, radii and curves sit beside the system's: a parallel set (STD-visual-details-26).
  - **Hover gating.** Tailwind v4's `hover:` already compiles to `@media (hover: hover)`; v3 needs `future.hoverOnlyWhenSupported` [S-L19-028]. The standard asks for both `(hover: hover)` and `(pointer: fine)` (STD-accessibility-motion-15), so a custom `hover` variant that adds `(pointer: fine)` closes the gap [inferred].
  - **Prompting in Tailwind's names.** Schoger instructs Claude Code in Tailwind's default vocabulary (gray 950 at 10%, text-sm, 5XL) [S-L19-103]. After a reset those names are gone, so prompts must use the system's names [inferred].
- **Visual effect:** With the easing reset and the default timing function set, every `transition` and `ease-*` class an engineer or agent types moves on the strong house curves, so menus and popovers feel snappy instead of generic [S-L19-018]. Without them, some components glide on Tailwind's softer defaults and a few start slowly with `ease-in` [inferred].
- **Depends on (upstream):** Q-tool-02 (`utilities`), Q-token-08 (`web-delivery`), Q-plat-08 (framework), DC-L19-183 (motion names).
- **Affects (downstream):** the Tailwind `@theme` export, which utility classes exist, editor autocomplete, the DESIGN.md list of classes, the review lint, the hover rules in the preview.
- **Token encoding:** no new tokens; export lines such as `@theme { --ease-*: initial; --ease-out: var(--ds-motion-easing-out); --ease-in-out: var(--ds-motion-easing-in-out); --ease-drawer: var(--ds-motion-easing-drawer); --default-transition-timing-function: var(--ds-motion-easing-out); }` [inferred].
- **Platform notes:** Web with Tailwind only. v3 and v4 differ for hover [S-L19-028]; the `@theme` reset syntax is v4.
- **Accessibility constraints:** Hover styles gated on both media features, with `:active` press feedback left ungated (STD-accessibility-motion-15). Reduced motion keeps working because the aliases point at the moded CSS variables (checked: durations follow the reduced-motion mode).
- **Default + heuristic:** Default when Q-tool-02 includes `utilities`: reset every Tailwind namespace the system defines, easing included, redefine `--ease-out`, `--ease-in-out` and `--ease-drawer` from the system tokens, point `--default-transition-timing-function` at the house ease-out, add a hover variant gated on `(hover: hover) and (pointer: fine)`, and list the system's class names in DESIGN.md so prompts use them. Heuristic: any built-in utility value the system does not own is a parallel token; switch it off or point it at a system token.
- **Evidence:** [S-L19-018] [S-L19-028] [S-L19-103]; compared with DC-L09-08, DC-L10-18, and the Q-tool-02 default. `standards.json` records no conflict for the easing reset yet.
- **Maps to:**
  - Q-tool-02, option `utilities`: new default note "Tailwind's own easing, color, type, radius and shadow values are switched off; `ease-out` and `ease-in-out` point at the house curves, and so does the bare `transition` class; `hover:` is gated on a fine pointer".
  - Q-token-08, option `web-delivery`: new Use/avoid line "avoid leaving framework defaults that duplicate system tokens".
  - Engine (proposed): add `--ease-*: initial` and `--default-transition-timing-function` to the `tailwindReset` block, and a gated hover variant; add a conflict note to STD-easing-duration-02 or STD-visual-details-26.
  - Visual sample: the same dropdown on Tailwind's default `ease-in-out` and on the house `--ease-out`, side by side at 10% speed.
- **Impact now / as it grows:**
  - Full reset: now, a few extra lines and one class (`ease-in`) that disappears. As it grows, every engineer and agent gets the house curves by default, with nothing to catch in review.
  - Partial reset (today): now, nothing changes. As it grows, weak and ease-in curves keep appearing through ordinary class names and must be caught one by one [inferred].
- **Standards:** STD-visual-details-26, STD-easing-duration-02, STD-easing-duration-03, STD-accessibility-motion-15.

### DC-L19-185: How the system's look reaches library components (the styling ladder)
- **Block path:** Components > Implementation > Styling third-party components
- **Questions the designer answers:** When a component comes from a library (a toast, a drawer, a menu), does it keep the library's look or take ours? If ours, do we override its styles or render our own markup on top of its behaviour? Do product teams call the library directly, or our wrapper?
- **Options:** Sonner's ladder, from least to most control [S-L19-022] [S-L19-090]:
  - **Library defaults**, tuned with its own switches (`richColors` for green and red status, `invert`) [S-L19-022].
  - **Global style options**: `toastOptions.style` for every toast, `style` for one; options on a single call win over global ones [S-L19-090] [S-L19-021].
  - **Classes on parts**, each needing `!important` (Tailwind's `!` prefix) because the library's injected styles win the cascade; fine for a few changes [S-L19-090] [S-L19-022].
  - **`unstyled: true`**: a halfway house that gets messy quickly [S-L19-022] [S-L19-090].
  - **Headless, wrapped**: your own JSX on the library's behaviour (`toast.custom()` keeps positioning, stacking and swipe), wrapped in your own `toast()` whose props fit the codebase. The docs recommend it because people usually either keep the defaults or go fully custom [S-L19-090] [S-L19-091], and the house skill calls it the design-system toast [S-L19-022].
  - **Unstyled primitives by design**: base-ui for dialogs, popovers, menus and selects [S-L19-029]; Vaul's parts are styled by the app, for example an overlay of `fixed inset-0 bg-black/40` [S-L19-095]. The system supplies all the styling.
- **Visual effect:** Defaults show the library's own look (Sonner's toasts are light unless told the theme [S-L19-092]). The middle rungs are a fair compromise for a few changes but get messy quickly [S-L19-090]; as overrides pile up they tend to break in small ways [inferred]. Headless and unstyled primitives look exactly like the rest of the system because they use its tokens [inferred].
- **Depends on (upstream):** Q-comp-01 (component base), Q-tool-02 (how engineers use the system), Q-plat-08 (React), Q-form-04 (whether toasts are used).
- **Affects (downstream):** toast, drawer, menu and dialog components; their component tokens; the wrapper API; library upgrades; DESIGN.md usage notes.
- **Token encoding:** no new semantic tokens; the wrapper reads the system's surface, text, radius and elevation tokens. Library settings that are values can become component tokens, for example `toast.offset.desktop` = 32px, `toast.offset.mobile` = 16px and `toast.gap` = 14 (Sonner's defaults) [S-L19-021] [S-L19-092]; the names are [inferred] and match DC-L19-113.
- **Platform notes:** Web and React. When Sonner's injected stylesheet is lost (Astro, view transitions) import `sonner/dist/styles.css`; inside Shadow DOM, copy the `[data-sonner-toaster]` style tag into the shadow root [S-L19-022] [S-L19-089].
- **Accessibility constraints:** Headless keeps the library's behaviour, so keep Sonner's container label, Alt+T hotkey and dismissible default (STD-accessibility-motion-23); your own JSX must still meet contrast and visible focus. Dialogs, popovers and menus stay on an accessible primitive that handles focus trapping and dismissal (STD-accessibility-motion-16).
- **Default + heuristic:** Default: every design-system component that wraps a behaviour library is headless (or built on an unstyled primitive) and exposed through the system's own function or component, so product code never imports the library directly [inferred from S-L19-090's wrapper advice]. Keep library defaults only where the look already fits, for example an internal tool. Heuristic: once more than a few classes need `!important`, go headless [S-L19-022]; never settle on the middle rungs.
- **Evidence:** [S-L19-021] [S-L19-022] [S-L19-029] [S-L19-089] [S-L19-090] [S-L19-091] [S-L19-092] [S-L19-095]; compared with DC-L08-03, DC-L09-08, DC-L19-101 (which library supplies each part) and DC-L19-113 (toast placement and tokens).
- **Maps to:**
  - Q-comp-01, option `headless`: confirms, and adds "behaviour libraries such as Sonner are used headless and wrapped in the system's own function".
  - Q-tool-02: new heuristic "product teams import the system's wrappers, never the library directly" for `npm` and `copy-in`.
  - No new question: this is an automatic default when Q-comp-01 is `headless` or `copy-in-styled`.
  - Visual sample: one toast at four rungs (defaults, inline style, classes with `!important`, headless) [S-L19-022].
- **Impact now / as it grows:**
  - Headless and wrapped: now, more JSX to write once. As it grows, library upgrades do not change the look, and the library can be swapped behind the wrapper [inferred].
  - Defaults: now, no work. As it grows, the library's look drifts from the brand and overrides pile up.
  - Middle rungs: now, quick fixes. As it grows, `!important` classes multiply until someone rewrites them headless anyway [inferred from S-L19-090, which calls this route messy beyond a few changes].
- **Standards:** STD-components-toasts-drawers-24, STD-components-toasts-drawers-25, STD-components-toasts-drawers-34, STD-visual-details-55, STD-visual-details-57, STD-accessibility-motion-16, STD-accessibility-motion-23.

### DC-L19-186: Which values are CSS variables, and at what scope
- **Block path:** Tokens > Delivery > Web > Variable scope and state hooks
- **Questions the designer answers:** Which values live as CSS variables on the page root, which are set per component by the component library, and which must never be CSS variables at all? How does the CSS know a component's state (opening, closing, open instantly)?
- **Options:**
  - **Theme tokens on `:root`.** Named custom properties on `:root`, as in Emil's easing library [S-L19-007]; components use them through `var(--ease-out)` [S-L19-017]. Modes switch with an attribute on the root (the engine uses `[data-theme]`, `[data-density]` and `[data-motion]`, checked).
  - **Variables the component library sets, used as given.** Base UI's `--transform-origin` and Radix's `--radix-dropdown-menu-content-transform-origin` make popovers grow from their trigger [S-L19-003] [S-L19-017] [S-L19-032]; Vaul's `--initial-transform` adjusts a side drawer that does not touch the screen edge [S-L19-094]. The names differ per library [S-L19-003] (the audit writes the Base UI one [S-L19-025]), so they belong to the chosen base [inferred].
  - **Component-internal computed variables.** Sonner builds its stack transform in CSS from `--toasts-before`, `--lift-amount` and `--offset` [S-L19-006]. They change when the stack changes, not every frame [inferred].
  - **Per-frame values: never an inherited variable on a parent.** Variables are inherited, so changing one restyles every child; a drawer's drag lagged past about 20 list items until the transform was set on the element itself [S-L19-005]; in React, write per-frame values to `ref.current.style` [S-L19-013].
  - **State as data attributes.** Sonner styles state through `data-mounted`, `data-expanded` and `data-front` [S-L19-006]; the recipes use `[data-starting-style]`, `[data-ending-style]`, `[data-instant]`, `[data-closed]` and `[data-visible]`, with `@starting-style` first and a `data-mounted` flag as fallback [S-L19-017] [S-L19-003].
- **Visual effect:** None when right. When wrong: dropped frames while dragging a long drawer [S-L19-005], and popovers that grow from their own center instead of the button that opened them [S-L19-003].
- **Depends on (upstream):** Q-token-08 (`web-delivery`), Q-comp-01 (the base library decides the variable and attribute names), DC-L10-18.
- **Affects (downstream):** the CSS export, component recipes, DESIGN.md usage notes, the review lint (STD-performance-properties-11 already flags drag offsets written to `--swipe` or `--drag` variables).
- **Token encoding:** Only theme-level values are DTCG tokens (emitted on `:root`). Library variables and state attributes are not tokens; they are documented in each component's notes [inferred]. Example: `.popover { transform-origin: var(--transform-origin); transition: transform 200ms var(--ease-out), opacity 200ms var(--ease-out); }` [S-L19-017].
- **Platform notes:** Web only. The attribute names assume a library that sets them (Base UI is named only for `--transform-origin`) [S-L19-017].
- **Accessibility constraints:** `[data-instant]` removes the animation only for neighbouring tooltips; the first still waits (STD-enter-exit-origin-10). Reduced-motion blocks apply to state transitions too (STD-accessibility-motion-01).
- **Default + heuristic:** Default: tokens and modes as `:root` custom properties (confirms DC-L10-18); components consume the base library's variables and data attributes instead of computing origin or state themselves; values that change every frame are written inline on the moving element. Heuristic: if it changes every frame, it is not a variable; if it changes per theme, it is a `:root` token; if the library measures it, use the library's variable.
- **Evidence:** [S-L19-003] [S-L19-005] [S-L19-006] [S-L19-007] [S-L19-013] [S-L19-017] [S-L19-025] [S-L19-032] [S-L19-094]; compared with DC-L10-18.
- **Maps to:**
  - Q-token-08, option `web-delivery`: keep the current text (custom properties for semantics, media queries for preferences, container queries for components) and add "custom properties sit on `:root` for tokens and modes; component state uses the base library's variables and data attributes; per-frame values are inline transforms"; new Use/avoid line "avoid CSS variables for values that change every frame (STD-performance-properties-11)".
  - Q-comp-01: new note "the chosen base decides the transform-origin variable and state attribute names; keep them inside the wrapper" [inferred].
  - Visual samples: a drawer with 20+ items dragged with a variable and with an inline transform [S-L19-005]; a popover growing from its center and from its trigger [S-L19-003].
- **Impact now / as it grows:**
  - Scoped as above: now, the recipes are correct from the start. As it grows, switching base library (Radix to Base UI) changes only the names inside the wrappers [inferred].
  - Everything as variables: now, it feels tidy. As it grows, drag performance falls as lists grow [S-L19-005].
- **Standards:** STD-performance-properties-11, STD-enter-exit-origin-03, STD-enter-exit-origin-06, STD-enter-exit-origin-10, STD-enter-exit-origin-40, STD-visual-details-26.

### DC-L19-187: Component variant axes named once for Figma, tokens and code
- **Block path:** Components > API > Variant axes and their code encoding
- **Questions the designer answers:** What are each component's variant axes (size, intent, state)? Are they spelled the same in Figma, in token names and in code props? How does a chosen variant become classes in code?
- **Options:**
  - **A typed variant API (cva)** for components with real variants, named in the source as size, intent and state [S-L19-029]; must-level when a component has variants (STD-visual-details-62).
  - **Ad hoc conditional classes (clsx)** for one-off conditions; the two compose [S-L19-029]. Template-literal ternaries three conditions deep are banned (STD-visual-details-62).
  - **Figma variants for state, size and type** (DC-L07-22); the third item of that list is "type" where the code source says "intent".
  - **Token modifiers**: variant (primary, secondary, success, error), state (hover, press, focus, disabled) and scale (DC-L07-04, EightShapes).
  - **State from the library as data attributes** instead of a state prop, where the base library sets them [S-L19-006] [S-L19-017].
- **Visual effect:** Indirect: the same size or intent looks and behaves the same in every component (STD-visual-details-36); mismatched axes show up as a "medium" button next to a "medium" input of a different height [inferred].
- **Depends on (upstream):** Q-token-02 (grammar), Q-comp-01 (base), Q-token-01 (whether component tokens exist), Q-tool-04 (Code Connect property maps).
- **Affects (downstream):** component token paths, Figma variant properties, code props, cva configurations, Code Connect mappings, DESIGN.md component tables.
- **Token encoding:** component tokens keyed by the same axis values, for example `button.height.sm|md|lg` and `button.bg.{intent}.{state}`, and a cva config with `variants: { size, intent }` whose keys match [inferred names].
- **Platform notes:** the curated list names cva for variant-driven Tailwind styling, in a React-centric list [S-L19-029]; the sources give nothing for SwiftUI or Compose.
- **Accessibility constraints:** the state axis always includes focus-visible and disabled (visible focus is a locked floor); the smallest size still meets the 24px target floor.
- **Default + heuristic:** Default: three axes spelled `size`, `intent` and `state` in Figma variant properties, component token paths and code props; states the base library sets stay data attributes. Differs from DC-L07-22 in one word: "intent" instead of "type", following the code source [S-L19-029] and avoiding a clash with the HTML `type` attribute on buttons [inferred]; DC-L07-04 already warns against `type` as a name part because it is a homonym. Heuristic: a condition that appears in more than one component, or needs a Figma variant, is an axis; anything else is clsx.
- **Evidence:** [S-L19-006] [S-L19-017] [S-L19-029]; compared with DC-L07-04, DC-L07-22, DC-L07-24, DC-L08-04.
- **Maps to:**
  - Q-token-02: new option `variant-axes`: "component variants use `size`, `intent` and `state`, spelled the same in Figma, tokens and code".
  - Q-tool-04: Code Connect prop maps become one-to-one when the axes match [inferred].
  - Q-comp-01 (with Tailwind): code encoding default "cva for variant-shaped components, clsx for ad hoc classes" (STD-visual-details-62).
- **Impact now / as it grows:**
  - Shared axes: now, one naming decision. As it grows, new components, Code Connect maps and agent-written code line up without translation tables [inferred].
  - Separate names per tool: now, no work. As it grows, every handoff needs a mapping, and mismatched sizes creep in.
- **Standards:** STD-visual-details-62, STD-visual-details-36.

### DC-L19-188: What each token and rule tells an agent: the use, the exact value and the reason
- **Block path:** Tokens > Governance > Descriptions and agent rules
- **Questions the designer answers:** Does each token say only what it is, or also when to use it, when not to, and why? Do the rules we hand to AI coding tools carry their reasons? Are values given exactly, or "about right"?
- **Options:**
  - **Describe what it is.** The engine's motion descriptions today are one-liners such as "Entering: decelerate." (checked).
  - **Describe use and reason, strictly.** Emil packages taste as one strict rule file per aspect of the interface, each rule stating why it has to be done that way, so the agent does not guess or invent its own rules [S-L19-004]; his course ships its principles as a rules file and a SKILL.md for coding agents [S-L19-001] [S-L19-007]. The audit gives reasons in plain words, for example ease-in delays the exact moment the user is watching [S-L19-025].
  - **Exact values only.** Take curves, durations and springs from the tables and never approximate [S-L19-018]; copy values exactly [S-L19-025]; plans cite exact values, file and line, and one exemplar to imitate [S-L19-026].
  - **Docs that machines can read.** A "copy as markdown" button so content can be fed to LLMs [S-L19-001]; interactive examples with ready-to-use code [S-L19-006].
- **Visual effect:** None on screen. Agents given the rules with reasons produce clearly better results [S-L19-004], which shows as fewer invented values and fewer parallel tokens [inferred].
- **Depends on (upstream):** Q-scope-03 (`ai-agents`), Q-token-09 (descriptions), Q-dist-02 (how agents read the system).
- **Affects (downstream):** `$description` on every semantic token, DESIGN.md, the AGENTS.md snippet, rules files, review messages.
- **Token encoding:** `$description` in one or two plain sentences with use, avoid and reason, for example on `motion.easing.out`: "Anything entering or leaving the screen. Never use ease-in on UI: it starts slowly and delays the moment the user is watching." (reason from [S-L19-025]) [inferred wording].
- **Platform notes:** none.
- **Accessibility constraints:** floor rules carry their reason too, for example 16px inputs so iOS does not zoom the page (STD-accessibility-motion-27).
- **Default + heuristic:** Default: every semantic token and every house rule written into DESIGN.md carries its use and its reason, with exact values. Extends DC-L07-23 (a description of intended use) with the reason. The engine gap is already recorded: DESIGN.md writes each standard's rule and values but leaves out its "why" (conflict note on STD-process-review-taste-55). Heuristic: a rule without a reason gets reinvented; a description an agent can act on says when to use it, when not to, and why.
- **Evidence:** [S-L19-001] [S-L19-004] [S-L19-006] [S-L19-007] [S-L19-018] [S-L19-025] [S-L19-026]; compared with DC-L07-23, DC-L07-24, DC-L11-23, DC-L19-171.
- **Maps to:**
  - Q-token-09, option `descriptions`: new wording "a short note on each semantic token with its use, what to avoid, and why"; new Use/avoid line "avoid descriptions that only restate the name".
  - Q-dist-02 (planned; the interview skips it until built), option `rules`: rules are strict and each states its reason (STD-process-review-taste-55). This agrees with DC-L19-171, which adds the option `aspect-files` (one rule file per aspect, each rule with its reason); no second change is proposed here.
  - Engine: write the standards' "why" into DESIGN.md (the recorded conflict).
  - Visual sample: a token detail card showing the same curve with a bare description and with use plus reason.
- **Impact now / as it grows:**
  - Use plus reason: now, longer descriptions to write once (the engine can generate most). As it grows, each new agent session starts with the same rules and reasons, so fewer tokens are forked or misused [inferred].
  - What-it-is only: now, compact. As it grows, agents and new teammates re-derive rules and invent near-duplicates [S-L19-025].
- **Standards:** STD-process-review-taste-55, STD-visual-details-26, STD-easing-duration-17.

### DC-L19-189: When the codebase already has tokens: map onto them, extend, never fork
- **Block path:** Tokens > Architecture > Source of truth > Existing tokens in the repo
- **Questions the designer answers:** Does the project already have tokens or CSS variables (colors, radii, spacing, fonts, easing, durations)? Should OpenDesigner's output adopt those names, replace them, or sit beside them? What happens to near-duplicates it finds?
- **Options:**
  - **Map and extend (the house rule).** Recon first: where tokens live (global CSS with `--ease-*` and `--duration-*`, the Tailwind config, keyframes) and the existing duration scales and spring configs [S-L19-027] [S-L19-024] [S-L19-031]. Build from them and extend what is missing; a parallel system is a defect [S-L19-018]; new curves go into the repo's existing token file [S-L19-026]; do not fork a new curve for press feedback [S-L19-028]. The same applies to libraries: read `package.json`, use what is installed, and do not replace a competitor unless asked [S-L19-029]. Schoger did the design-side version, switching the page's grays from slate to neutral to match the grays in the product screenshot on the page [S-L19-103].
  - **Replace through a migration.** The builder's model becomes the master (the Q-tool-01 default, DC-L16-02) and old tokens are deprecated for one release before removal (DC-L07-23). Only when the person asks for it [inferred from STD-visual-details-56's "unless asked"].
  - **Side by side.** The builder emits its own `--ds-*` set next to the existing one: the parallel set the standard forbids (STD-visual-details-26).
  - **Consolidate what is there.** Several near-identical hand-typed curves are a consolidation finding [S-L19-025], rated LOW (polish) [S-L19-027]; one plan per finding, merged only when the files and the fix are the same, such as one easing-token swap across components [S-L19-026].
  - **No project at all.** When prototyping with nothing to draw tokens from: neutral grays, one accent and the system font stack [S-L19-031] (STD-visual-details-25, a prototyping rule).
- **Visual effect:** Map and extend: new screens look like the product people already use; prototype variants look as if they could ship in the product tomorrow [S-L19-031]. Side by side: two almost-equal grays or curves, which shows as small, hard-to-name inconsistencies [inferred].
- **Depends on (upstream):** Q-scope-02 (existing screens), Q-scope-05 (start from an existing product; adopt, adapt or create), Q-ref-01 `code`, Q-tool-01.
- **Affects (downstream):** the Q-tool-01 default, export names (prefix and aliases), the token file location, the Tailwind config, review findings, the opendesigner-extract skill.
- **Token encoding:** existing names are kept as each matching token's code name, so the export writes the project's own variables (for example the DTCG token `motion.easing.out` exported as the project's existing `--ease-out`) [inferred; DC-L16-02 already gives every token a code syntax].
- **Platform notes:** Mostly web in these sources. In Figma, existing variables play the same role (DC-L07-08).
- **Accessibility constraints:** An existing token that fails a locked floor (for example text below AA contrast) is not adopted as is; the floor wins and the change is reported [inferred from the guardrails].
- **Default + heuristic:** Default: when Q-scope-02 is not `greenfield`, or recon finds tokens, OpenDesigner reads the existing tokens as its starting values, keeps their names as code names, and only extends. Differs from DC-L16-02 and the Q-tool-01 default `builder` in one respect: the builder's model can stay the master, but its export must write the project's existing names instead of a second prefixed set. Heuristic: before adding any token, search for one that already does the job; three near-matches means one token.
- **Evidence:** [S-L19-018] [S-L19-024] [S-L19-025] [S-L19-026] [S-L19-027] [S-L19-028] [S-L19-029] [S-L19-031] [S-L19-103]; compared with DC-L07-08, DC-L07-23, DC-L11-01, DC-L11-16, DC-L16-02.
- **Maps to:**
  - Q-tool-01: new heuristic "if the repo already has tokens, the export keeps their names and extends them; replacing them is an explicit migration".
  - Q-scope-02 and Q-scope-05 (`existing-product`, `adapt`): recon runs first, and the found tokens pre-fill the answers.
  - Q-token-02, option `prefix`: "never rename a project's existing tokens to add a prefix".
  - Q-dist-03 (planned): near-duplicate curves and durations reported as LOW consolidation findings [S-L19-027].
  - Visual sample: five near-matching hand-typed curves becoming one `var(--ease-out)` [S-L19-025].
- **Impact now / as it grows:**
  - Map and extend: now, a slower first run because recon comes first. As it grows, one set of tokens to maintain, and every agent finds and reuses it.
  - Replace: now, clean names. As it grows, a migration with a deprecation window and codemods.
  - Side by side: now, the fastest start. As it grows, two systems drift apart and every review has to pick one.
- **Standards:** STD-visual-details-26, STD-visual-details-56, STD-visual-details-25, STD-process-review-taste-11, STD-process-review-taste-10, STD-process-review-taste-49.

### DC-L19-190: How spring tokens are stored
- **Block path:** Tokens > Types > Motion > Spring encoding
- **Questions the designer answers:** Are springs stored as the two numbers designers reason with (how much it overshoots, and how quickly it arrives) or as physics numbers (stiffness, mass)? What does each platform receive? What does the web get when it cannot run a spring?
- **Options:**
  - **Damping ratio and response (the house standard).** Apple replaced mass, stiffness and damping with these two designer-friendly numbers; 1.0 means no bounce, lower is bouncier; response is how quickly the value reaches the target, in seconds, and is not a duration [S-L19-020]. Apple's values: move or reposition 1.0 and 0.4, rotation 0.8 and 0.4, drawer or sheet 0.8 and 0.3 [S-L19-020]. On the web, Motion's `bounce` and `duration` map closely to damping and response [S-L19-020]; the house skills write it as `{ type: "spring", duration: 0.5, bounce: 0.2 }` [S-L19-018] [S-L19-023] [S-L19-025] [S-L19-033], with bounce kept to 0.1-0.3 [S-L19-018].
  - **Damping ratio and stiffness (the engine and Q-token-05 today).** The engine stores `dampingRatio`, `stiffness` and `mass` and derives Apple's duration and bounce (checked); Q-token-05's option text stores `{dampingRatio, stiffness}`; the M3 export does the same (DC-L04-22).
  - **Mass, stiffness and damping.** Only when more control is needed [S-L19-018] [S-L19-023].
  - **Web fallback.** A CSS `linear()` sample of the spring (Atlassian; the engine writes one), or a cubic-bezier (DC-L04-22).
- **Visual effect:** The same motion when converted correctly. What changes is what a designer can tune by eye: bounce 0.2 reads as a slight overshoot, response 0.3 as snappy; stiffness 700 means nothing until it is plotted [inferred].
- **Depends on (upstream):** Q-motion-01 (personality), Q-motion-04 (springs or not), Q-token-05, Q-token-08 (pipeline outputs).
- **Affects (downstream):** `motion.spring.*` tokens, Figma's spring bounce field (DC-L07-14), SwiftUI, Compose and Motion code, the CSS fallback.
- **Token encoding:** a `transition` token with its fallback curve, and the spring in `$extensions`: `{"spring": {"dampingRatio": 0.8, "response": 0.3}}` for a sheet [S-L19-020]. Stiffness is derived for platforms that need it: stiffness = (2π / response)² with mass 1 [inferred; the engine already uses the inverse, response = 2π / √stiffness]. Bounce = 1 − dampingRatio for ratios up to 1 [inferred; the engine uses the same mapping].
- **Platform notes:** SwiftUI takes duration and bounce, Compose takes dampingRatio and stiffness (DC-L04-22), Motion takes bounce and duration [S-L19-020], and a React Native sheet uses `{ duration: 300, dampingRatio: 0.8 }` (STD-components-toasts-drawers-40). So the stored pair converts to every target, with Compose needing the derived stiffness.
- **Accessibility constraints:** Reduced motion removes springs and overshoot and keeps a short fade (STD-accessibility-motion-02).
- **Default + heuristic:** Default: store `dampingRatio` and `response` (in seconds) as the source values; derive stiffness for Compose and a `linear()` sample for CSS. Most UI starts at damping 1.0; bounce only when the gesture carried momentum [S-L19-020]. Differs from the Q-token-05 option text and the Q-motion-04 default, which store stiffness (the Q-motion-04 conflict is recorded on STD-springs-gestures-02; Q-token-05's is not). Heuristic: if a designer cannot predict the feel from the two stored numbers, store different numbers.
- **Evidence:** [S-L19-018] [S-L19-020] [S-L19-023] [S-L19-025] [S-L19-033]; compared with DC-L04-22, DC-L04-28, DC-L07-14, DC-L09-06, DC-L19-88, DC-L19-99.
- **Maps to:**
  - Q-token-05, option `motion`: change "springs as `{dampingRatio, stiffness}` in `$extensions`" to "springs as `{dampingRatio, response}` in `$extensions`, stiffness derived per platform, with a `linear()` or bezier fallback". This is the storage side of DC-L19-88 (the presets) and DC-L19-99 (the `$extensions` shape), which store the same pair.
  - Q-motion-04: owned by DC-L19-88 (new default: damping ratio and response with four presets); this card agrees and proposes nothing further there.
  - Engine (proposed): make `dampingRatio` and `response` the stored spring fields and derive `stiffness`.
  - Visual sample: Apple's sheet spring (0.8, 0.3) next to its move spring (1.0, 0.4), plotted over time.
- **Impact now / as it grows:**
  - Damping and response: now, one conversion function. As it grows, designers tune springs on every platform with the same two numbers.
  - Damping and stiffness: now, matches Compose and M3 directly. As it grows, every design review needs a plot to know what a stiffness value feels like [inferred].
- **Standards:** STD-springs-gestures-02, STD-components-toasts-drawers-40, STD-accessibility-motion-02.

## Proposed questionnaire changes

| Q-id | Change | Evidence |
|---|---|---|
| Q-token-04 | New default: px in the source; rem on the web for type, spacing, control heights and breakpoints; `max(px, rem)` for target-size floors; px for borders, rings, shadows and radii. Remove the "spacing scales with text size, off by default" toggle for web output. Engine: extend the rem conversion beyond `font.size.*`, and write Tailwind's `--spacing` in rem instead of px. | DC-L19-182; [S-L19-020]; STD-accessibility-motion-13 |
| Q-token-02 | New option `motion-names` (unprefixed `--ease-out`, `--ease-in-out`, `--ease-drawer`, `--duration-*` aliases) as the motion default; new option `variant-axes` (`size`, `intent`, `state` spelled the same everywhere); `prefix` never renames a project's existing tokens. | DC-L19-183, DC-L19-187, DC-L19-189; [S-L19-018] [S-L19-027] [S-L19-029] |
| Q-tool-02 | `utilities`: switch off Tailwind's own easing (and every namespace the system owns), point `ease-out`/`ease-in-out` and the bare `transition` class's default timing function at the house curves, gate `hover:` on a fine pointer. New heuristic: product teams import the system's wrappers, not the library. | DC-L19-184, DC-L19-185; [S-L19-018] [S-L19-028] [S-L19-090] |
| Q-token-08 | `web-delivery`: `:root` variables for tokens and modes, the base library's variables and data attributes for state, inline transforms for per-frame values; avoid framework defaults that duplicate tokens. | DC-L19-184, DC-L19-186; [S-L19-003] [S-L19-005] [S-L19-017] |
| Q-token-05 | `motion`: springs stored as `{dampingRatio, response}`, stiffness derived. | DC-L19-190; [S-L19-020]; STD-springs-gestures-02 |
| Q-token-09 | `descriptions`: use, what to avoid, and why; exact values. | DC-L19-188; [S-L19-004] [S-L19-025] |
| Q-tool-01 | New heuristic: with existing repo tokens, keep their names and extend; replacing them is an explicit migration. | DC-L19-189; [S-L19-018] [S-L19-027] [S-L19-029] |
| Q-token-01 | Confirms `two-plus`; new heuristic: depth follows team size and number of products (from Q-scope-04). | DC-L19-181; [S-L19-044] [S-L19-054] |
| Q-token-03 | Confirms `extended`; "lean" means few hand-made decisions, not fewer token kinds. | DC-L19-181; [S-L19-054] |
| Q-token-07 | `vars-styles`: no change; Kole's "styles for colors" flagged as one-video opinion that differs from DC-L07-21. | DC-L19-181; [S-L19-045] |
| Q-scope-04 | New effect on Q-token-01 depth. | DC-L19-181; [S-L19-054] |
| Q-comp-01 | `headless`: behaviour libraries used headless and wrapped; the base decides origin variable names; cva for variant-shaped components with Tailwind. | DC-L19-185, DC-L19-186, DC-L19-187; [S-L19-022] [S-L19-029] |
| Q-dist-02 (planned) | `rules`: each rule states its reason; agrees with DC-L19-171's `aspect-files` option. | DC-L19-188; [S-L19-004] |
| Q-motion-03, Q-motion-04 | No change from these cards: DC-L19-85 (curves by job) and DC-L19-88 (damping and response presets) own them, and DC-L19-183 and DC-L19-190 agree. | DC-L19-183, DC-L19-190 |

No new interview question is proposed: the delivery area already has 18 zoom-3 questions (`pacing.json`), and every change above is a new default, option or automatic output.

## Open questions / gaps

- The Tailwind easing values and the bare `transition` class's default timing function in DC-L19-184 come from Tailwind's own documentation, not from an L19 source; they were checked on 2026-09-24 and 2026-09-27 and can change with a Tailwind release.
- No source says how native apps should scale spacing with Dynamic Type; DC-L19-182 only settles the web.
- Whether radii should follow rem is untested; DC-L19-182 keeps them px because the standard's check covers only margin, padding and gap.
- Should the engine's reduced-motion and theme attributes (`[data-motion]`, `[data-theme]`) also be documented as the "state attributes" of the page, next to the component ones? Not covered by the sources.
- How `engine.py review` should rate a hand-typed curve (must-level break of STD-visual-details-26, or LOW polish per [S-L19-027]) is still open, as the tokens synthesis notes.
- Vaul is recorded as unmaintained (`learn/sources.json`), so DC-L19-185 and DC-L19-186 use it as a craft reference for `--initial-transform` and unstyled parts, not as a recommended dependency.

## Confidence

- Confirmed against source text: the easing library on `:root` [S-L19-007]; "styles for colors, variables for measurements" [S-L19-045]; lean versus massive systems [S-L19-054] and "decisions you can stick to" [S-L19-044]; rem or em spacing [S-L19-020]; the recon targets `--ease-*` and `--duration-*` and LOW severity for consolidation [S-L19-027]; consolidation of near-identical curves [S-L19-025]; the headless recommendation and the wrapper advice [S-L19-090]; the transform-origin variables [S-L19-003]; `--initial-transform` [S-L19-094]; data attributes and stack variables [S-L19-006]; the inherited-variable drag lag [S-L19-005]; cva and clsx for size, intent and state, and the `package.json` check [S-L19-029]; Apple's spring table [S-L19-020]; rule files with reasons [S-L19-004]; the "copy as markdown" button and rules file [S-L19-001].
- Checked in `engine.py`: rem only for `font.size.*` in the CSS export; Tailwind's `--spacing` written in px; `--ds-` prefixed CSS names; the Tailwind `--ease-standard/enter/exit/linear` aliases; `tailwindReset` covering colors, text, radii, shadows and breakpoints only; springs stored with stiffness and derived Apple values; mode switching by `[data-theme]`, `[data-density]` and `[data-motion]`.
- Inferred and marked: the depth-by-team-size mapping, the "what stays px" split, the alias names, the "intent" over "type" reason, the wrapper-for-every-behaviour-library default, the stiffness and bounce conversions, and the reconciliations flagged in each Default.
- Adversarial check, 2026-09-27 (every cited source reopened in `learn/analysis/` and `learn/raw/`, every Q-id, DC id and STD id resolved). Corrected: DC-L19-182's claim that a 1.5rem target never drops below 24px (false when someone sets a smaller default text size; now `max(24px, 1.5rem)`), and its control-height and target extension is now marked inferred; DC-L19-184 missed that Tailwind's bare `transition` class uses `--default-transition-timing-function`, which the `--ease-*` reset does not touch; DC-L19-181's Linear wording (the source says "creating a view", not a dialog), its account of what Q-scope-04 changes, and its use of Q-scope-01 surfaces as a product count; DC-L19-185's middle-rung effects, which go beyond the Sonner page and are now inferred; DC-L19-186's citation for per-library variable names; DC-L19-187's "fourth" item (it is the third) and cva's scope; DC-L19-189's misquote of the prototype skill and the prototyping scope of STD-visual-details-25; DC-L19-190's attribution of the Motion-to-Apple mapping (it is [S-L19-020]). Cross-links added where these cards overlap newer cards: DC-L19-85 and DC-L19-88 own Q-motion-03 and Q-motion-04, DC-L19-99 gives motion a component tier from the start, DC-L19-164 is the process side of DC-L19-181, DC-L19-171 shares Q-dist-02 (planned) with DC-L19-188, and DC-L19-113 names the toast tokens. No card contradicts a house standard, and none was withdrawn.
