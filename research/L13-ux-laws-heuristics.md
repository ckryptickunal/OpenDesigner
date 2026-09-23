# L13: UX laws, heuristics, interaction principles, core UX practices

## Lane overview

Status: done (2026-09-23). Sources are logged in `traces/L13-trace.md` (S-L13-001 to S-L13-110).

**What this lane gives the builder.** Tokens and components decide how a product looks. The laws and heuristics in this file decide whether it works. For the builder, they become a third layer that sits on top of tokens and components: **behavior rules**. A behavior rule links a principle (for example Fitts's law) to a concrete check (for example "no interactive target below 24x24 CSS px") and to a place in the system where it applies (token, component, pattern, content or flow). Part E proposes a schema for these rules.

**How this file is organized**
- Part A: all 30 laws currently on lawsofux.com. A compact table gives definition, origin and evidence strength. A mapping table then gives law, design-system rule, builder guardrail, and what stays a human call.
- Part B: the classic heuristic sets (Nielsen's 10, Norman, Shneiderman's 8, Tognazzini's First Principles), the response-time limits, and a crosswalk showing where they agree.
- Part C: 18 Decision Cards for the core UX practices a system should encode (loading ladder, navigation, progressive disclosure, scanning, forms, validation, errors, undo vs confirm, feedback channels, empty states, onboarding, microinteractions, plain language, inclusive design, deceptive patterns, AI interfaces, convention vs novelty, primary action emphasis).
- Part D: UX research methods at summary level (L11 owns process).
- Part E: the automation boundary, meaning what the builder can enforce and what must stay human judgment, plus a rule schema.

**Top findings**
1. **Three popular "laws" are shaky, and one is routinely misused.** The Zeigarnik effect did not survive a 2025 meta-analysis of 59 publications (39 on the Zeigarnik effect) [S-V1b-053]: there is no memory advantage for unfinished tasks, though people do tend to resume them [S-L13-040, S-L13-044]. Choice overload averaged "virtually zero" across 50 papers in 2010 [S-L13-045], and it only shows up reliably under four conditions: complex sets, hard tasks, unclear preferences, and effort-minimizing goals [S-L13-046]. Parkinson's law began as a humorous essay [S-L13-020]. Miller's 7±2 is real memory research, but using it to cap menus at seven items is a misuse, because menus rely on recognition, not recall [S-L13-048, S-L13-002].
2. **Hick's law does not justify deleting menu items.** Novices scanning an unfamiliar list pay a linear visual-search cost. Only experts who already know where an item is pay the logarithmic Hick-Hyman cost [S-L13-050]. So the fix for novices is grouping, ordering and labeling, not cutting items.
3. **Response-time thresholds fit together into one ladder** that the builder can ship as tokens: 16 ms per frame, 50 ms to acknowledge input, 100 ms to feel instant, 200 ms for a "good" INP, 400 ms (the Doherty threshold), 1 s before focus breaks, 10 s before attention is lost. Each band maps to a feedback pattern: nothing, then spinner or skeleton, then percent-done progress [S-L13-031, S-L13-032, S-L13-033, S-L13-038, S-L13-051, S-L13-052, S-L13-003].
4. **The heuristic sets agree on seven things** (Part B6): visible status and feedback, consistency and conventions, error prevention, easy reversal and user control, recognition over recall, plain language, and minimalism. These are the builder's core rule set, and most of them can be partly checked by a machine.
5. **AI interfaces now have usable guidance.** Style citations distinctly and place them next to the claims they support. Do not show step-by-step "reasoning" displays, because they are often unfaithful to what the model actually computed. Put disclaimers near the input box and pair them with an action. Avoid anthropomorphic wording. Do not autoscroll streamed answers [S-L13-083, S-L13-084, S-L13-085]. Microsoft's 18 HAX guidelines and the Shape of AI pattern library give the builder a taxonomy for AI components [S-L13-089, S-L13-088].

**Evidence-strength scale used in this file**
- **R (research-backed):** replicated lab or field evidence, and it transfers to UI directly.
- **R- (research-backed at origin, extrapolated to UI):** solid in its home field (memory, perception, motivation). The UI application is an inference.
- **C (contested):** failed replications, or a meta-analysis that finds a near-zero mean effect.
- **H (heuristic):** a practitioner rule or aphorism with no experimental test behind it. Useful, but it is judgment.
- **P (pop / analogy):** satire, or an economic or philosophical observation borrowed by analogy.

---

## Part A. The Laws of UX (30 laws, verified against lawsofux.com on 2026-09-23)

The current lawsofux.com home page lists exactly 30 laws, with no categories [S-L13-001]. This is the same set as the lane brief. The five Gestalt laws (Common Region, Proximity, Prägnanz, Similarity, Uniform Connectedness) get one line each here. **L15 owns them in depth.**

### A1. Compact table

| # | Law | One-line definition | Origin | Evidence | Misapplication flag |
|---|---|---|---|---|---|
| 1 | Aesthetic-Usability Effect | People perceive attractive designs as more usable [S-L13-001] | Kurosu and Kashimura, Hitachi, 1995: 26 ATM layouts, 252 participants. Appeal correlated more with *perceived* than with *actual* usability [S-L13-010, S-L13-053] | R- | It is about perception only. Users tolerate *minor* issues, not major ones, and polish can hide problems during usability tests [S-L13-053] |
| 2 | Choice Overload | People get overwhelmed by many options [S-L13-001] | Toffler, *Future Shock*, 1970 [S-L13-011]; popular "jam study" lineage [inferred] | **C** | 2010 meta-analysis: mean effect "virtually zero" (50 papers, 5,036 participants) [S-L13-045]. 2015 meta-analysis (99 observations, N=7,202): the effect is significant only with its moderators: set complexity, task difficulty, preference uncertainty, effort-minimizing goal [S-L13-046]. Do not use it to cap catalogs or search results |
| 3 | Chunking | Break information into meaningful groups [S-L13-026] | Miller 1956 [S-L13-026] | R | Chunk size does not matter. The number of chunks does [S-L13-048] |
| 4 | Cognitive Bias | Systematic errors in judgment [S-L13-025] | Tversky and Kahneman, 1972 [S-L13-025] | R (as a field) | An umbrella term, not a design rule. The same biases power defaults and dark patterns (DC-L13-15) [inferred] |
| 5 | Cognitive Load | Mental resources needed to use an interface [S-L13-017] | Sweller, cognitive load theory, 1988. Intrinsic vs extraneous load [S-L13-017] | R- (instructional design) | Designers can only remove *extraneous* load. Intrinsic task complexity remains (see Tesler) [S-L13-017, S-L13-007] |
| 6 | Doherty Threshold | Productivity soars when response time is under 400 ms [S-L13-003] | Doherty and Thadani, IBM, 1982. Replaced a 2 s standard [S-L13-003] | H (dated) | Mainframe-era productivity data. Modern budgets are tighter: 100 ms for response (RAIL), 200 ms for a "good" INP [S-L13-052, S-L13-051]. Its takeaway that "strategic delays can enhance perceived value" is a persuasion tactic, not a latency rule [S-L13-003] |
| 7 | Fitts's Law | Time to acquire a target depends on distance and size [S-L13-004] | Fitts 1954. T = a + b·log2(2D/w) [S-L13-004, S-L13-054] | **R** | Screen-edge "infinite targets" help mouse users but *hurt* touch users [S-L13-054] |
| 8 | Flow | Full immersion with energized focus [S-L13-023] | Csikszentmihalyi 1975 [S-L13-023] | R- | Hard to operationalize. Treat it as "don't interrupt, match challenge to skill" [S-L13-023] |
| 9 | Goal-Gradient Effect | Effort increases as the goal gets closer [S-L13-012] | Hull 1932/1934 (rats). Kivetz, Urminsky and Zheng 2006 field data: café card buyers speed up near the reward; a 12-stamp card with 2 bonus stamps was completed faster than a 10-stamp card [S-L13-012, S-L13-058] | R | "Artificial progress" is an ethics line: pre-filled progress that misstates the real work left drifts toward manipulation [inferred] |
| 10 | Hick's Law | Decision time grows with the number and complexity of choices [S-L13-005] | Hick and Hyman 1952. RT = a + b·log2(n) [S-L13-005, S-L13-103] | R (narrow) | Holds when choices are equally likely and known [S-L13-103]. For novices scanning a menu, search time is **linear**; only experts pay the log cost [S-L13-050]. Do not use it as a reason to delete navigation |
| 11 | Jakob's Law | Users prefer your product to work like the others they already know [S-L13-006] | Nielsen (NN/g), 2017 wording [S-L13-055] | H | The law itself is uncontroversial. Nielsen personally is a disputed voice in the community right now (COMMUNITY-SIGNAL). Cite NN/g research, not personal opinion posts |
| 12 | Law of Common Region | Elements inside a shared boundary are seen as a group [S-L13-027] | Gestalt tradition [S-L13-027] (Palmer 1992 [inferred]) | R | See L15 |
| 13 | Law of Proximity | Near things are seen as a group [S-L13-028] | Gestalt [S-L13-028] | R | See L15 |
| 14 | Law of Prägnanz | Ambiguous images are read as the simplest form [S-L13-001] | Gestalt (Wertheimer [inferred]) | R | See L15 |
| 15 | Law of Similarity | Similar elements are seen as a group even when separated [S-L13-001] | Gestalt | R | See L15 |
| 16 | Law of Uniform Connectedness | Visually connected elements are seen as more related [S-L13-001] | Gestalt (Palmer and Rock 1994 [inferred]) | R | See L15 |
| 17 | Mental Model | A compressed model of what we think we know about a system [S-L13-022] | Craik 1943 [S-L13-022] | R- | Needs research to find the users' model. The builder cannot infer it [S-L13-022] |
| 18 | Miller's Law | People hold about 7±2 items in working memory [S-L13-002] | Miller 1956 [S-L13-002] | R (memory) / **misapplied** | Later work puts capacity nearer 4±1 chunks (Cowan 2001) [S-L13-047], or 3 to 6 [S-L13-048]. The lawsofux page itself warns against using seven to justify design limits [S-L13-002]. **The classic misuse is capping navigation at seven items** [S-L13-048] |
| 19 | Occam's Razor | Among equal hypotheses, prefer the one with the fewest assumptions [S-L13-021] | William of Ockham, c. 1287-1347 [S-L13-021] | P | A philosophical principle used by analogy for "remove until function suffers" [S-L13-021] |
| 20 | Paradox of the Active User | Users skip manuals and start using the product right away [S-L13-018] | Carroll and Rosson 1987 [S-L13-018] | R- (observational) | Supports contextual help over manuals and tours [S-L13-018, S-L13-070] |
| 21 | Pareto Principle | About 80% of effects come from 20% of causes [S-L13-019] | Pareto (Italian land ownership) [S-L13-019] | P | 80/20 is a rough regularity, not a constant [inferred] |
| 22 | Parkinson's Law | Work expands to fill the time available [S-L13-020] | Parkinson, humorous *Economist* essay, 1955 [S-L13-020] | **P** | Satire. Its UI takeaway (autofill, fewer steps) stands on other evidence [S-L13-020] |
| 23 | Peak-End Rule | Experiences are judged by their peak and their end [S-L13-009] | Kahneman et al. 1993 [S-L13-009] | R | 2022 meta-analysis: 174 effect sizes, large peak-end effect r=0.581, robust duration neglect [S-L13-061]. But the overall average predicts about as well [S-L13-059]. So design the whole journey, then polish the peaks and ends |
| 24 | Postel's Law | Be liberal in what you accept, conservative in what you send [S-L13-008] | Jon Postel, TCP robustness principle [S-L13-008] | H (disputed at origin) | The IETF's RFC 9413 (2023) argues that tolerance entrenches errors in protocols [S-L13-056]. For UI input it still holds, within security bounds [inferred] |
| 25 | Selective Attention | People attend to the stimuli related to their goals [S-L13-024] | Cherry 1953, Broadbent 1958, Treisman 1960 [S-L13-024] | R | Includes banner blindness and change blindness [S-L13-024] |
| 26 | Serial Position Effect | People best remember the first and last items in a series [S-L13-015] | Ebbinghaus [S-L13-015] | R- | Strong for list *recall*. Applying it to *navigation choice* is an extrapolation [inferred] |
| 27 | Tesler's Law | Every system has complexity that cannot be reduced [S-L13-007] | Larry Tesler, Xerox PARC, mid-1980s; popularized by Saffer [S-L13-007] | H | "Who carries the complexity?" is a design question, not a measurement [S-L13-007] |
| 28 | Von Restorff Effect | The item that differs from the rest is remembered [S-L13-014] | von Restorff 1933 [S-L13-014] | R | Restraint is part of the law: too many salient items compete and can look like ads. Do not rely on color alone [S-L13-014] |
| 29 | Working Memory | A system that temporarily holds and manipulates information for a task [S-L13-016] | Miller, Galanter and Pribram (1960s); Atkinson and Shiffrin 1968 [S-L13-016] | R | lawsofux says "4-7 chunks", fading after 20-30 s [S-L13-016]. Capacity figures vary by study [S-L13-047] |
| 30 | Zeigarnik Effect | Unfinished tasks are remembered better than finished ones [S-L13-013] | Zeigarnik, 1920s [S-L13-013] | **C (failed replication)** | Ghibellini and Meier 2025 (*Humanities and Social Sciences Communications*, 1 Jul 2025, 59 publications: 39 on the Zeigarnik effect, 21 on Ovsiankina [S-V1b-053]): no memory advantage. The **Ovsiankina** tendency to *resume* interrupted tasks does hold [S-L13-040, S-L13-044]. Justify "resume" patterns with Ovsiankina, and never use either effect to justify nagging |

**Tally:** R 15 (five of them Gestalt), R- 6, H 4 (Doherty, Jakob, Postel, Tesler), P 3 (Occam, Pareto, Parkinson), C 2 (Choice Overload, Zeigarnik). Miller counts as R for the memory finding but is flagged as misapplied. Hick counts as R in a narrow sense but is flagged. The tally is my own classification using the scale above [inferred]. Per-law evidence is cited in the table.

### A2. Law to design-system rule to builder guardrail

Key: **Default** means the builder ships it pre-set. **Lint** means an automated check with error or warning severity. **Human** means it stays a judgment call, which the builder can prompt for but should not decide.

| Law | Design-system rule | Builder: automatic | Stays human |
|---|---|---|---|
| Fitts's | Minimum target size and spacing. Primary action close to the fields or content it acts on. Icon plus label beats icon alone. Hit area never shrinks with density. Values live in L03 DC-L03-12 (web 24px AA, iOS 44pt, Android 48dp) [S-L13-054, S-L13-004] | Default: `size.target.min` token fixed across density modes. Lint (error): interactive element hit area < 24x24 CSS px with no spacing exception (WCAG 2.5.8) [S-L13-098]. Lint (warn): primary submit placed far from the last field, for example top of page [S-L13-054]. Lint (warn): edge-anchored small targets on touch layouts [S-L13-054] | Exact placement of primary actions across layouts. Trade-offs in dense pro tools |
| Hick's | Recommend or default one option in selection sets. Group and label long lists. Progressive disclosure for rare options. Search and typeahead for long known-item lists [S-L13-005, S-L13-050, S-L13-103] | Lint (warn): a flat, ungrouped list or menu above roughly 10-12 items with no search, sections or typeahead [inferred threshold]. Default: Select or Combobox switches to searchable above N options (configurable) [inferred] | Which items to promote or demote. Whether to cut features. **The builder must not auto-delete options to "satisfy Hick"** |
| Miller's / Working Memory / Chunking | Recognition over recall. Keep context visible across steps. Chunk long strings. **No seven-item cap** [S-L13-002, S-L13-016, S-L13-048] | Default: input masks or grouping for OTP, phone, card and IBAN-like formats [inferred]. Lint (warn): form re-asks information already given in the session (WCAG 3.3.7 Redundant Entry, Level A) [S-L13-098]. Lint (warn): placeholder used as the only label [S-L13-066]. **Explicitly do not ship a "max 7 nav items" rule** | How to chunk domain content |
| Doherty / response-time limits | Latency budget and loading-feedback ladder (DC-L13-01). Motion must never delay acknowledgment [S-L13-003, S-L13-031, S-L13-051] | Default: duration tokens for feedback thresholds (Part B5). Default: Button has a `loading` state that blocks repeat submits [S-L13-038, S-L13-106]. Lint (warn): standard UI transitions > 500 ms (L04 F1: systems pack most tokens into 50-400 ms) [inferred threshold] | Perceived-performance strategy (optimistic UI, prefetch). Whether a deliberate delay is honest |
| Jakob's | Follow platform and web conventions unless the benefit is proven. Offer a transition path on redesigns [S-L13-006, S-L13-055] | Default: platform presets (L10). Lint (warn): overriding standard platform behavior such as back gesture, standard shortcuts (Ctrl/Cmd+S), link vs button semantics [S-L13-036]. Info: a "convention deviation" note is required in component docs [inferred] | When novelty is worth the learning cost (DC-L13-17) |
| Aesthetic-Usability | Visual polish raises tolerance for small flaws only. Never treat attractiveness as evidence of usability [S-L13-053] | Info: usability test templates remind facilitators to separate aesthetic comments from task success [S-L13-053] | Brand expression (L06) |
| Choice Overload | For decisions with many comparable options: comparison views, a recommended option, filters [S-L13-011, S-L13-046] | Lint (info): pricing or plan pickers with more than 3-4 tiers and no "recommended" marker or comparison table [inferred] | Assortment size. Whether moderators (complexity, uncertainty) apply |
| Cognitive Load | Cut extraneous load: fewer simultaneous styles, consistent components, no decorative noise [S-L13-017] | Lint (warn): more than N distinct text styles, or more than N accent colors, on one screen [inferred]. Default: density presets (L03 DC-L03-10) | What counts as necessary information |
| Tesler's | The system absorbs complexity: smart defaults, inference, autofill. Don't oversimplify to the point of abstraction [S-L13-007, S-L13-005] | Default: `autocomplete` attributes on standard inputs (name, email, address, one-time code) [inferred]. Questionnaire item: "Where does irreducible complexity live: user, system, or admin?" | The allocation decision itself |
| Postel's | Accept flexible input (spaces in phone numbers, pasted formatting, varied date formats) and normalize it. Output one canonical format [S-L13-008] | Default: input components trim whitespace and normalize known formats [inferred]. Lint (warn): validation pattern rejects common separators [inferred] | Security-sensitive validation, where strictness wins [S-L13-056] |
| Von Restorff | One primary (high-emphasis) action per region. Emphasis is scarce. Never color alone [S-L13-014] | Lint (warn): more than one filled or primary button in the same action group or dialog [inferred from S-L13-014]. Lint (error): state or meaning shown by color only (WCAG 1.4.1) [inferred from S-L13-014] | Which action deserves emphasis |
| Serial Position | Put key items at the start and end of nav bars and toolbars. Bury rarely used items in the middle or overflow [S-L13-015] | Suggestion only: ordering hints in nav config [inferred] | Final ordering, backed by analytics or tree tests |
| Selective Attention | Do not style real content like ads. Limit competing attention-grabbers. Announce dynamic changes, because of change blindness [S-L13-024] | Lint (warn): more than one page-level banner visible at once [inferred]. Default: live-region announcements on toast, inline alert and async form errors [inferred] | Campaign and marketing placements |
| Goal-Gradient | Multi-step flows show progress ("Step 2 of 4") [S-L13-012, S-L13-058] | Default: Stepper shows position and total. Lint (warn): 3+ step flow with no progress indicator [inferred] | Whether any "head-start" progress is honest |
| Peak-End | Design the ends: success, completion, error and empty states. Celebrate sparingly at real peaks [S-L13-009, S-L13-061] | Lint (warn): a flow or pattern shipped without success, error and empty variants [inferred] | Tone and degree of celebration (L06 voice) |
| Zeigarnik (via Ovsiankina) | "Resume where you left off", visible drafts and incomplete-task lists. Never nagging [S-L13-044, S-L13-071] | Default: draft autosave in long forms [inferred, supports Tognazzini "never lose work" S-L13-038]. Lint (error): repeated prompts after a choice was made (DSA Art. 25 example) [S-L13-108] | Frequency of reminders |
| Paradox of the Active User | Contextual help (inline hints, toggletips, empty-state guidance) over manuals and forced tours [S-L13-018, S-L13-070] | Lint (warn): onboarding tour with no skip control [S-L13-070] | Whether onboarding is needed at all (DC-L13-11) |
| Mental Model | Use the users' vocabulary and match their model of objects and actions [S-L13-022] | Questionnaire: capture domain glossary; content lint flags internal jargon from a team-supplied list [inferred] | The model itself (requires research, Part D) |
| Occam's Razor / Pareto | Prune variants and tokens that nothing uses. Put effort into the most-used components [S-L13-021, S-L13-019] | Report: unused tokens and variants; component usage ranking (L11 adoption metrics) [inferred] | What to cut |
| Parkinson's | Shorten tasks with autofill, sensible defaults and saved data [S-L13-020] | Covered by the Tesler and Postel defaults | n/a |
| Flow | No interruptions mid-task (modals, nags). Keyboard shortcuts for experts. Clear feedback [S-L13-023] | Lint (warn): modal or interstitial on page load or mid-task that the user did not trigger [inferred] | Challenge-skill balance (games, learning products) |
| Cognitive Bias | Use defaults to help, never to deceive [S-L13-025, S-L13-071] | Deceptive-pattern lints (DC-L13-15) | Ethical review |
| Gestalt five (Proximity, Similarity, Common Region, Connectedness, Prägnanz) | Spacing encodes grouping: space inside a group is smaller than space between groups. Same function, same look. Containers group. **L15 owns these** [S-L13-027, S-L13-028] | Lint (warn): intra-group gap >= inter-group gap, for example label-to-field gap >= field-to-field gap [inferred]. Lint (warn): interactive and static text share identical styling [inferred] | Composition |

---

## Part B. Heuristic frameworks and interaction principles

### B1. Nielsen's 10 usability heuristics (current NN/g wording)

The article was published on 24 Apr 1994 and last reviewed on 30 Jan 2024. The heuristics date from 1994, with language refinements in 2020 [S-L13-030]. The titles below are verbatim, and the gist is paraphrased from NN/g.

| # | Heuristic | Gist (NN/g) | Design-system encoding | Builder: automatic | Stays human |
|---|---|---|---|---|---|
| 1 | Visibility of system status | Keep users informed with appropriate feedback in reasonable time [S-L13-030] | Loading ladder (DC-L13-01); every async component has loading, success and error states; selected and current states in nav | Lint: async component with no loading or error state; nav with no "current" state [inferred] | Which status matters to users |
| 2 | Match between the system and the real world | Speak the users' language, not internal jargon [S-L13-030] | Content guidelines, domain glossary, reading-level targets (DC-L13-13) | Content lint: jargon list, reading-grade estimate [inferred] | Vocabulary choices |
| 3 | User control and freedom | A clearly marked "emergency exit" to leave unwanted actions [S-L13-030] | Undo, cancel, back; Escape closes dialogs (APG, L08); undo preferred over confirm (DC-L13-08) | Lint: dialog without a dismiss path; destructive action with neither undo nor confirmation [inferred] | Which actions get undo |
| 4 | Consistency and standards | Same words and actions mean the same thing; follow platform and industry conventions [S-L13-030] | Tokens, one component per job, platform presets | Lint: duplicate components doing the same job, off-token values (L07/L11 lint) [inferred] | Deliberate exceptions |
| 5 | Error prevention | Prevent problems before they happen [S-L13-030] | Constraints (input types, pickers, disabled-with-reason), confirmation for high-stakes irreversible actions | Default: typed inputs (`type=email`, `inputmode`) [inferred]; WCAG 3.3.4 for legal and financial data [inferred] | Risk assessment per action |
| 6 | Recognition rather than recall | Make elements, actions and options visible [S-L13-030] | Persistent labels, recent items, visible navigation, breadcrumbs | Lint: placeholder-only label [S-L13-066]; icon-only button with no visible label or tooltip in primary nav [inferred] | How much to show vs hide |
| 7 | Flexibility and efficiency of use | Shortcuts, hidden from novices, speed up experts [S-L13-030] | Keyboard shortcuts, command palette, bulk actions, customization | Default: shortcut registry that refuses to override OS or browser standards [S-L13-036] | Which shortcuts |
| 8 | Aesthetic and minimalist design | No irrelevant or rarely needed information [S-L13-030] | Progressive disclosure (DC-L13-03), density, variant pruning | Report: unused variants and tokens [inferred] | What is "rarely needed" |
| 9 | Help users recognize, diagnose and recover from errors | Plain language, no error codes, precise problem, constructive solution [S-L13-030] | Error-message template (DC-L13-07) | Lint: error string with no remedy, or that exposes a raw code only [inferred] | Wording |
| 10 | Help and documentation | Best if no explanation is needed; otherwise provide it [S-L13-030] | Contextual help components (toggletip, inline hint, empty-state guidance); help in a consistent place (WCAG 3.2.6, Level A) [S-L13-098] | Lint: help entry point moves between pages [inferred from S-L13-098] | Help content |

### B2. Norman's principles (The Design of Everyday Things, revised edition 2013)

Norman's revised edition keeps the original science and adds one concept, **signifiers**. Chapter 4 covers constraints, discoverability and feedback [S-L13-035]. The list below uses the book's terms. The design-system translation is my inference unless tagged otherwise.

| Principle | Meaning | Design-system rule | Builder |
|---|---|---|---|
| Discoverability | Users can work out what actions are possible and how to do them [S-L13-035] | Visible affordances for primary tasks; hidden gestures only as accelerators. NN/g data: hidden mobile nav was used by 44% of users on one site, visible or combo nav by 89% on another [S-L13-097] | Lint (warn): primary navigation hidden behind a menu icon on wide layouts [inferred] |
| Affordance | The relationship between object and person that determines possible actions [S-L13-035] | Interactive elements look interactive (buttons look pressable, links look like links) | Lint: link style reused on non-interactive text [inferred] |
| Signifier (added 2013) | A perceivable cue that shows where and how to act [S-L13-035] | Hover, focus and pressed states; drag handles; chevrons for disclosure; the cursor. Figma lists five core button states (default, hover, active, focus, disabled) plus loading, success, error and selected [S-L13-106] | Lint: interactive component missing a focus or hover state [inferred] |
| Mapping | Controls laid out to match their effect [S-L13-035] | Control placement mirrors the object (align/justify icons, spatial sliders); related controls close together (Fitts) | Human |
| Feedback | Communicate the result of an action, promptly [S-L13-035] | Response-time ladder (B5); microinteraction feedback (DC-L13-12) | Default: pressed and loading states |
| Constraints | Limit possible actions to prevent errors [S-L13-035] | Input types, masks, disabled-with-explanation, pickers instead of free text where the domain is closed | Default: typed inputs [inferred] |
| Conceptual model | A simplified explanation of how the system works, which the design should convey [S-L13-035] | Consistent object-action grammar across screens | Human (research) |

### B3. Shneiderman's Eight Golden Rules

Source: Designing the User Interface, 6th edition (May 2016), section 3.3.4, as listed on the author's own page [S-L13-037].

| # | Rule (verbatim title) | Design-system rule [inferred mapping] |
|---|---|---|
| 1 | Strive for consistency | Identical terms in prompts, menus and help; tokens; one pattern per job [S-L13-037] |
| 2 | Seek universal usability | Novice-to-expert range, disabilities, international users: accessibility, i18n, density modes [S-L13-037] |
| 3 | Offer informative feedback | Feedback for every action, scaled to frequency and importance [S-L13-037] |
| 4 | Design dialogs to yield closure | Flows have a clear beginning, middle and end, with success states (links to Peak-End) [S-L13-037] |
| 5 | Prevent errors | With "simple, constructive, and specific instructions for recovery" [S-L13-037] |
| 6 | Permit easy reversal of actions | Undo reduces anxiety and encourages exploration [S-L13-037] |
| 7 | Keep users in control | No unwanted surprises (no autoplay, no unrequested modals) [S-L13-037] |
| 8 | Reduce short-term memory load | No remembering across displays (links to WCAG 3.3.7) [S-L13-037, S-L13-098] |

### B4. Tognazzini's First Principles of Interaction Design (revised and expanded, 5 Mar 2014)

There are 19 principles [S-L13-038]: Aesthetics, Anticipation, Autonomy, Color, Consistency, Defaults, Discoverability, Efficiency of the User, Explorable Interfaces, Fitts's Law, Human-Interface Objects, Latency Reduction, Learnability, Metaphors, Protect Users' Work, Readability, Simplicity, State, Visible Navigation.

The ones that give the builder concrete, checkable rules (verbatim quotes from the source) [S-L13-038]:
- **Latency Reduction:** "Acknowledge all button clicks by visual or aural feedback within 50 milliseconds". "Trap multiple clicks of the same button or object". Builder: pressed-state feedback within one frame of input; loading state disables repeat submission.
- **Protect Users' Work:** "Ensure that users never lose their work". Builder: draft autosave defaults; preserve input on error (NN/g error guideline 10 agrees [S-L13-064]).
- **Defaults:** "Defaults within fields should be easy to 'blow away'". Builder: pre-filled values are selected on focus, or clear with one action [inferred implementation].
- **Discoverability:** "If the user cannot find it, it does not exist". Builder: discoverability lint (B2).
- **Color:** use secondary cues alongside color for color-blind users [S-L13-038]. Builder: no color-only states (WCAG 1.4.1).
- **Aesthetics:** fashion must not trump usability [S-L13-038]. The Liquid Glass legibility backlash, and Apple's two rounds of fixes (iOS 26.1 Clear/Tinted option; iOS 27 transparency slider), is a live 2025-26 example (COMMUNITY-SIGNAL section e).
- **Visible Navigation** and **State** (remember location, history and preferences; preserve work across sessions) [S-L13-038].

### B5. Response-time limits, reconciled into one ladder

| Threshold | Meaning | Source | Feedback pattern | Token (proposed) |
|---|---|---|---|---|
| 16 ms (10 ms target) | One frame at 60 fps; animation work per frame | RAIL [S-L13-052] | Animations must hold frame rate | n/a (performance budget) |
| 50 ms | Acknowledge input (pressed state); process input events within 50 ms | Tognazzini [S-L13-038]; RAIL [S-L13-052] | Pressed or active state, instant | `feedback.acknowledge.max = 50ms` |
| 100 ms | Feels instantaneous | Nielsen [S-L13-031]; RAIL [S-L13-052] | Show the result directly; no indicator | `feedback.instant.max = 100ms` |
| 200 ms | INP "good" at the 75th percentile (500 ms = poor) | web.dev [S-L13-051] | Web interaction budget | `perf.inp.good = 200ms` |
| 400 ms | Doherty threshold | Doherty and Thadani 1982 [S-L13-003] | Upper bound for standard UI transitions (matches M3 medium4 = 400 ms in L04 F1) [inferred link] | n/a (motion tokens in L04) |
| 1 s | Flow of thought stays uninterrupted; users notice the delay | Nielsen [S-L13-031] | Show an indicator for anything longer than about 1 s [S-L13-032] | `feedback.indicator.delay = 1000ms` [inferred value; some teams show it at 300-500 ms to avoid flashes, not sourced] |
| 1-10 s | Wait | NN/g [S-L13-032, S-L13-033] | Full page: skeleton screen. Module: spinner or looped indicator. Always with a text label ("Loading comments...") [S-L13-032] | `feedback.determinate.threshold = 10000ms` |
| > 10 s | Attention lost | Nielsen [S-L13-031] | Percent-done progress bar with explanatory text; allow background or cancel [S-L13-031, S-L13-032] | as above |

Rules that go with the ladder: never use a static "Loading..." label alone [S-L13-032]. Skeletons complement performance work; they don't replace it [S-L13-033]. Animated (pulsing or shimmer) skeletons carry accessibility concerns, so respect reduced motion [S-L13-033] (L04 DC-L04-25 owns reduced motion).

### B6. Crosswalk: where the frameworks agree (the builder's core rule set)

| Consensus principle | Nielsen | Norman | Shneiderman | Tognazzini | Laws of UX | Machine-checkable? |
|---|---|---|---|---|---|---|
| Visible status and feedback | H1 | Feedback | Rule 3 | Latency Reduction | Doherty | Mostly: required states, timing tokens |
| Consistency and conventions | H4 | Conceptual model | Rule 1 | Consistency | Jakob's | Mostly: token and component lint |
| Error prevention | H5 | Constraints | Rule 5 | Protect Users' Work | Postel's | Partly: input types, confirm or undo presence |
| Reversal and user control | H3 | n/a | Rules 6, 7 | Autonomy, Explorable Interfaces | n/a | Partly: dismiss paths, undo presence |
| Recognition over recall | H6 | Discoverability, Signifiers | Rule 8 | Visible Navigation, State | Miller's, Working Memory | Partly: label lint, redundant entry |
| Plain language and real-world match | H2, H9 | Mapping | n/a | Metaphors, Readability | Mental Model | Partly: reading grade, jargon list |
| Minimalism and progressive disclosure | H8 | n/a | n/a | Simplicity | Hick's, Occam's, Cognitive Load | Weakly: variant and style counts |
| Efficiency for experts | H7 | n/a | Rule 2 | Efficiency of the User, Fitts's Law | Fitts's | Partly: target sizes, shortcut registry |

Sources: [S-L13-030, S-L13-035, S-L13-037, S-L13-038, S-L13-001]. The groupings are my synthesis [inferred].

---

## Part C. Decision Cards: core UX practices a design system should encode

Note on cross-lane evidence: some cards cite L08's source ids (for example [S-L08-039]) for component facts L08 already verified. I read those rows in `traces/L08-trace.md` and did not reopen the pages.

### DC-L13-01: Loading and wait-feedback ladder
- **Block path:** Patterns > Feedback > Loading and latency
- **Questions the designer answers:** How fast must the UI acknowledge a tap or click? After how long does a loading indicator appear? Skeleton or spinner? What happens when a wait passes 10 seconds?
- **Options:**
  - *NN/g threshold ladder:* no indicator under 1 s; looped indicator for 2-10 s; percent-done progress for 10 s and more [S-L13-032, S-L13-031].
  - *Skeleton-first* for full-page or region loads under 10 s; spinners for individual modules [S-L13-033].
  - *Inline loading in the trigger:* Apple HIG puts an activity indicator inside the button [S-L08-039]; Carbon ships an Inline loading component [S-L08-009]; M3's loading indicator is for waits under 5 s [S-L08-038].
  - *Optimistic UI:* show the expected result immediately and roll back on failure [inferred].
- **Visual effect:** skeletons make the page feel structured and faster. Spinners feel generic and give no duration. Optimistic UI feels instant, but a failed action produces a visible rollback. Inline loading keeps the user's eyes where they acted [inferred].
- **Depends on (upstream):** motion system and reduced-motion policy (L04), API latency profile, performance budget.
- **Affects (downstream):** Button (loading state, double-submit trap), Skeleton, Spinner or loading indicator, Progress bar, Toast, data tables, the empty state (loading is not empty; DC-L13-10).
- **Token encoding:** DTCG `$type: duration`: `feedback.acknowledge.max = 50ms`, `feedback.instant.max = 100ms`, `feedback.indicator.delay = 1000ms`, `feedback.determinate.threshold = 10000ms`. DTCG has no "threshold" or rule type, so store the rule itself in `$extensions` (Part E) [inferred].
- **Platform notes:** Web: INP "good" is at most 200 ms at the 75th percentile [S-L13-051]; RAIL says respond within 100 ms and handle input within 50 ms [S-L13-052]. iOS: indicator inside the button [S-L08-039]. Android: M3 loading indicator replaces most indeterminate circular progress [S-L08-038].
- **Accessibility constraints:** Animated skeletons raise accessibility concerns, so honor reduced motion [S-L13-033]. Announce busy and done states to screen readers, for example with `aria-busy` and a polite live region [inferred].
- **Default + heuristic:** Acknowledge within 50 ms [S-L13-038]. No indicator under about 1 s. Skeleton for page or region loads of 1-10 s; spinner for a module or inline action. Over 10 s: determinate progress, explanatory text, and a way to cancel or background it. Every indicator carries a text label, never "Loading..." alone [S-L13-032]. Button loading state disables repeat clicks [S-L13-038].
- **Evidence:** [S-L13-003, S-L13-031, S-L13-032, S-L13-033, S-L13-038, S-L13-051, S-L13-052, S-L08-009, S-L08-038, S-L08-039]

### DC-L13-02: Global navigation model and item count
- **Block path:** Patterns > Navigation > Global navigation
- **Questions the designer answers:** How many top-level destinations are there? Is navigation always visible or hidden behind a menu? How deep does the hierarchy go? Do we cap the number of items?
- **Options:**
  - *Visible bar:* bottom tab bar (3-5 destinations on compact screens, per L03), top nav, rail, or sidebar.
  - *Hidden:* a hamburger or drawer.
  - *Combo:* the top items visible, the rest under "More".
- **Visual effect:** visible navigation claims space but tells users what the product does at a glance. Hidden navigation looks clean and hides scope. In an NN/g mobile study of 179 users, a hidden-nav site had 44% navigation use and a 33 s time-to-navigation; a visible or combo site had 89% and 24 s [S-L13-097].
- **Depends on (upstream):** content inventory and IA research (card sort, tree test; Part D), platform (L10), breakpoints (L03).
- **Affects (downstream):** Nav bar, Rail, Sidebar, Breadcrumbs, Tabs, overflow menus, search placement.
- **Token encoding:** not a token. It is a pattern config, for example `nav.visibleItems.compact = 5` as a platform constraint [inferred].
- **Platform notes:** Material swaps the bottom bar for a rail or drawer by breakpoint. Apple converts the tab bar to a sidebar. See L03 and L10. On mouse-driven desktops, screen-edge targets are easy to hit; on touch they are not [S-L13-054].
- **Accessibility constraints:** WCAG 3.2.6 Consistent Help (A) and consistent navigation placement [S-L13-098]. The nav landmark and current-page state must be exposed [inferred].
- **Default + heuristic:** Keep primary navigation visible whenever width allows. **Do not cap at seven items**: that is the Miller misuse [S-L13-048]. Keep disclosure to two levels at most [S-L13-063]. For long lists, group into labeled categories [S-L13-103] and add search, because novices scan linearly [S-L13-050]. Put the most important items at the ends [S-L13-015] and validate labels with a tree test [S-L13-095].
- **Evidence:** [S-L13-015, S-L13-048, S-L13-050, S-L13-054, S-L13-063, S-L13-095, S-L13-097, S-L13-098, S-L13-103]

### DC-L13-03: Progressive disclosure strategy
- **Block path:** Patterns > Information density > Disclosure
- **Questions the designer answers:** Which options are needed by most users, most of the time? Where do advanced options live? Is the task linear (wizard) or free-form?
- **Options:**
  - *Everything visible.*
  - *Progressive disclosure:* primary options up front, advanced ones behind a clearly labeled trigger ("More options", accordion, "Advanced" panel) [S-L13-063].
  - *Staged disclosure:* a wizard or stepper. Good for independent steps, bad when steps depend on each other [S-L13-063].
  - *Contextual reveal:* on hover or selection (a discoverability risk: "If the user cannot find it, it does not exist" [S-L13-038]).
  - *Basic/Advanced mode switch* [inferred].
- **Visual effect:** progressive disclosure gives calmer, shorter screens. Everything-visible reads as powerful but dense. Wizards feel guided but slow for experts [inferred].
- **Depends on (upstream):** task-frequency data (Pareto [S-L13-019]), audience expertise (novice vs expert, H7 [S-L13-030]).
- **Affects (downstream):** Accordion, Disclosure, Popover, Stepper, settings pages, filter panels, AI chat answers (NN/g recommends expand/collapse instead of generating new messages [S-L13-083]).
- **Token encoding:** none. It is a pattern rule.
- **Platform notes:** mobile favors staged disclosure (one thing per screen). Desktop favors panels and accordions [inferred].
- **Accessibility constraints:** disclosure triggers need an expanded or collapsed state (APG accordion and disclosure; L08) [inferred from L08]. Hover-only reveal fails keyboard and touch users [inferred].
- **Default + heuristic:** Progressive disclosure with **at most two levels** [S-L13-063], and a trigger label that says what is behind it. Use staged disclosure only for independent steps [S-L13-063]. Never hover-only for anything essential.
- **Evidence:** [S-L13-019, S-L13-030, S-L13-038, S-L13-063, S-L13-083]

### DC-L13-04: Content hierarchy for scanning
- **Block path:** Foundations > Content > Scannability (type styles in L02, layout in L03)
- **Questions the designer answers:** Will people read or scan this page? How do headings, bold text and lists get used? Where does the key information go?
- **Options:**
  - *Layer-cake:* headings and subheadings carry the page; users scan the headings and skip the body [S-L13-062].
  - *Front-loaded (inverted pyramid):* key points in the first two paragraphs [S-L13-062].
  - *Spotted:* make links, numbers and keywords stand out for users who hunt for them [S-L13-062].
  - The **F-pattern is a failure mode, not a layout goal.** It appears with unformatted text, efficiency-seeking users and moderate interest, and NN/g calls it "bad for users and businesses" [S-L13-062].
- **Visual effect:** layer-cake pages look structured, with frequent, distinct headings. Unformatted walls of text push users into the F-pattern [S-L13-062].
- **Depends on (upstream):** type scale and heading styles (L02), spacing (L03).
- **Affects (downstream):** heading components, prose styles, lists, link styles, cards, docs templates, empty states.
- **Token encoding:** type role tokens (L02) plus content rules in `$extensions` [inferred].
- **Platform notes:** same on all platforms. Mobile shortens the lines and raises heading frequency [inferred].
- **Accessibility constraints:** real heading structure and descriptive link text (WCAG 1.3.1, 2.4.6, 2.4.4) [inferred; SC numbers not re-verified in this lane].
- **Default + heuristic:** A heading for every section. Front-load the first two paragraphs. Bold key terms sparingly. Use bullets for lists of three or more items, and information-rich link text [S-L13-062]. Builder lint: skipped heading levels, paragraphs over N lines without a heading, and link text like "click here" [inferred].
- **Evidence:** [S-L13-062]

### DC-L13-05: Form field labeling and required-field marking
- **Block path:** Patterns > Forms > Field anatomy
- **Questions the designer answers:** Where do labels go? Can placeholder text stand in for a label? How are required and optional fields marked? Where do hints go?
- **Options:**
  - *Persistent label outside the field* (above or beside) with a hint below the label [S-L13-066].
  - *Floating label* (a label that animates from placeholder position) [inferred; not evaluated in a source I opened].
  - *Placeholder as label:* **reject.** It causes seven problems, including memory strain, no way to check entries, and harder error correction [S-L13-066].
  - *Required marking:* an asterisk at the start of the label, with a legend (NN/g recommends marking all required fields), or "Required" in words. Marking optional fields as well helps [S-L13-068].
- **Visual effect:** persistent labels make taller but calmer forms. Placeholder-only forms look minimal but become opaque once filled [S-L13-066].
- **Depends on (upstream):** type roles (L02), spacing (L03, with label-to-field gap smaller than field-to-field gap, per Proximity), color for required and error states (L01).
- **Affects (downstream):** Text field, Select, Combobox, Checkbox and Radio groups (fieldset and legend), Form layout, Field (Fluent and shadcn both ship a Field wrapper [S-L08-010, S-L08-018]).
- **Token encoding:** `space.field.label-gap`, `space.field.stack` (label gap smaller than stack gap), `color.text.required`, type role `label` [inferred names].
- **Platform notes:** iOS grouped forms often put labels inline, to the left [inferred]. Web defaults to labels above the field.
- **Accessibility constraints:** WCAG 3.3.2 Labels or Instructions and 1.3.5 Identify Input Purpose [inferred]. 3.3.7 Redundant Entry (A) and 3.3.8 Accessible Authentication (AA; do not block paste or password managers) [S-L13-098]. The required state must be exposed to assistive tech, not just shown as an asterisk [S-L13-068].
- **Default + heuristic:** A visible label above every field, a hint under the label, the asterisk at the label start plus a legend, and `autocomplete` attributes on personal-data fields. Builder lint (error): field with no programmatic label. Builder lint (warn): placeholder-only label.
- **Evidence:** [S-L13-066, S-L13-068, S-L13-098, S-L08-010, S-L08-018]

### DC-L13-06: Validation timing
- **Block path:** Patterns > Forms > Validation
- **Questions the designer answers:** When do we check input: while typing, when leaving the field, or on submit? When does an error disappear? Do we show "valid" confirmation? Can a user override a validator?
- **Options:**
  - *On submit only:* fine for short forms [S-L13-100]. But 31% of e-commerce sites have no inline validation at all [S-L13-065].
  - *Late validation (on blur):* performs better than keystroke validation for most inputs [S-L13-100].
  - *Reward early, punish late:* when fixing an invalid field, confirm the fix immediately; for a valid field being edited, wait until blur to flag new errors [S-L13-100].
  - *Live keystroke validation:* only for things like password-strength meters [S-L13-099].
  - *Just-in-time:* an explicit "Validate" or "Check" button for complex inputs [S-L13-100].
  - *Positive inline validation:* checkmarks for correct entries [S-L13-065].
- **Visual effect:** premature errors feel hostile ("Why are you telling me my email address is wrong, I haven't had a chance to fill it all out yet!", a Baymard test participant) [S-L13-065]. Positive validation feels encouraging [S-L13-065].
- **Depends on (upstream):** DC-L13-05 (field anatomy), DC-L13-07 (error pattern), form length.
- **Affects (downstream):** Text field error slot, Form, Error summary, Stepper.
- **Token encoding:** none. It is a component prop, for example `validateOn: "blur" | "submit" | "change"` plus `revalidateOn: "change"` [inferred API].
- **Platform notes:** same across platforms. Keyboards on mobile make premature errors more costly [inferred].
- **Accessibility constraints:** errors identified in text and announced (WCAG 3.3.1 and 3.3.3) [inferred]. Validation must not move focus unexpectedly while the user types [inferred].
- **Default + heuristic:** Validate on blur, or when the input reaches its complete length (ZIP, phone) [S-L13-065]. Clear the error on the keystroke that fixes it [S-L13-065]. Never flag an empty field the user has not left [S-L13-064]. For long forms, use one thing per page and validate on submit [S-L13-100]. Give heuristic validators (addresses, names) an override [S-L13-100].
- **Evidence:** [S-L13-064, S-L13-065, S-L13-099, S-L13-100]

### DC-L13-07: Error message pattern
- **Block path:** Patterns > Feedback > Errors
- **Questions the designer answers:** Where does an error appear? How loud is it relative to severity? What does the message say? Is the user's input kept?
- **Options:**
  - *Inline field error* (next to the source).
  - *Error summary* at the top of the form.
  - *Section or page banner.*
  - *Blocking dialog.*
  - *Full error page* for catastrophic failures.
  - NN/g: match prominence to severity, and put the message near the source [S-L13-064].
- **Visual effect:** inline errors keep context. Banners signal system-level problems. Dialogs interrupt [inferred].
- **Depends on (upstream):** status colors (L01 DC-L01-15), icons (L05), voice and tone (L06), DC-L13-06.
- **Affects (downstream):** Field error slot, Inline alert, Banner or Message bar, Toast (not for form errors [inferred]), Error page template.
- **Token encoding:** `color.feedback.error.{fg,bg,border}`, `icon.status.error`, and a content template `{problem}{cause?}{remedy}` stored as documentation or `$extensions` [inferred].
- **Platform notes:** OS alert conventions differ (L10).
- **Accessibility constraints:** redundant, non-color indicators (icon plus text) [S-L13-064]; WCAG 1.4.1 Use of Color [inferred]; errors announced to screen readers [inferred].
- **Default + heuristic:** The NN/g 13 guidelines [S-L13-064], which match Nielsen H9 [S-L13-030] and Shneiderman rule 5 [S-L13-037]. Shown close to the source. Visible without relying on color. Human-readable, precise, constructive and blame-free. Input preserved, with a quick fix where possible. Template: "what happened, then how to fix it". Builder lint: message with no remedy; raw error code with no explanation; color-only error state.
- **Evidence:** [S-L13-030, S-L13-037, S-L13-064]

### DC-L13-08: Destructive and irreversible actions: undo vs confirm
- **Block path:** Patterns > Error prevention > Destructive actions
- **Questions the designer answers:** Can this action be reversed? How costly is a mistake? Should we offer undo, ask for confirmation, or both?
- **Options:**
  - *Undo:* a toast or snackbar with "Undo", plus soft delete or trash. NN/g calls undo the superior approach [S-L13-067]. Shneiderman rule 6: permit easy reversal [S-L13-037].
  - *Confirmation dialog* with specific verb labels ("Delete file" / "Keep file"), reserved for serious, irreversible or costly actions, because overuse breeds habituation [S-L13-067]. Primer ships a ConfirmationDialog [S-L08-012].
  - *Type-to-confirm* for catastrophic actions [inferred; common practice, not verified here].
  - *No protection:* only for trivial actions.
- **Visual effect:** undo keeps flow fast and calm. Frequent confirmations feel bureaucratic and stop being read [S-L13-067].
- **Depends on (upstream):** data model support for soft delete and versioning (engineering), DC-L13-09 (feedback channel).
- **Affects (downstream):** Toast or Snackbar (with action), Dialog, Button (destructive variant), Menu (destructive items), trash patterns.
- **Token encoding:** `color.action.destructive.*` (L01). Toast auto-dismiss duration as `$type: duration`; long enough to read and act, and pausable (WCAG 2.2.1) [inferred].
- **Platform notes:** Apple HIG: never give the primary role to a destructive button [S-L08-039]. Button order in dialogs differs by platform (L10).
- **Accessibility constraints:** WCAG 3.3.4 Error Prevention (Legal, Financial, Data): reversible, checked or confirmed; level AA [S-V1b-006]. Focus must return to the invoker after a dialog closes (APG, L08).
- **Default + heuristic:** If it is reversible, use undo and do not confirm. If it is irreversible and costly, confirm with verb labels, with Cancel as the safe default [inferred]. If it is catastrophic, use type-to-confirm. Builder lint (warn): delete action with neither undo nor confirmation; generic "Yes/No" or "OK" labels in a destructive dialog [S-L13-067].
- **Evidence:** [S-L13-037, S-L13-067, S-L08-012, S-L08-039]

### DC-L13-09: Feedback channel selection (inline, toast, banner, dialog)
- **Block path:** Patterns > Feedback > Messaging
- **Questions the designer answers:** Which component carries which message? How long does it stay? Does it need an action? What if several messages appear at once?
- **Options (real systems):**
  - *Inline message or status in place* (field, section, button success state [S-L13-106]).
  - *Toast or snackbar:* transient and low-stakes. Spectrum ships Toast [S-L08-015]; Atlassian ships Flag [S-L08-011]. Primer deliberately has **no** Toast [S-L08-012].
  - *Banner or message bar:* persistent, page or system level. Fluent Message bar [S-L08-010]; Spectrum InlineAlert [S-L08-015].
  - *Modal dialog:* a blocking decision.
- **Visual effect:** inline feedback is quiet and precise. Toasts are ambient and easy to miss. Banners are loud and persistent. Dialogs stop the user [inferred].
- **Depends on (upstream):** DC-L13-07, DC-L13-08, motion (L04), elevation (L04).
- **Affects (downstream):** Toast, Banner, Inline alert, Dialog, live-region infrastructure.
- **Token encoding:** `duration.toast.default`, z-index or layer tokens (L04), status color roles (L01) [inferred names].
- **Platform notes:** Android snackbars, iOS banners and alerts; the web needs custom live regions [inferred].
- **Accessibility constraints:** messages announced via live regions [inferred]. Timed messages carrying actions must give enough time or be pausable (WCAG 2.2.1) [inferred]. Change blindness means changes elsewhere on screen must be announced or signaled [S-L13-024].
- **Default + heuristic:** Put the message where the cause is [S-L13-064]. Use toast only for low-stakes confirmations, and toast plus Undo for reversible actions. Never make a toast the only channel for an error that blocks progress [inferred]. At most one page-level banner at a time (Selective Attention [S-L13-024]). Use a dialog only for decisions that must block.
- **Evidence:** [S-L13-024, S-L13-064, S-L13-106, S-L08-010, S-L08-011, S-L08-012, S-L08-015]

### DC-L13-10: Empty states
- **Block path:** Patterns > States > Empty
- **Questions the designer answers:** What does each collection show when it has no data? Is the space empty because it is new, because the user cleared it, because a filter matched nothing, or because of an error? What single action should we offer?
- **Options (types):**
  - *First use* (nothing created yet).
  - *User-cleared* (for example inbox zero).
  - *No results* (search or filter).
  - *No permission, or error.*
  - *Loading*, which is **not** an empty state: it belongs to DC-L13-01.
  - Real components: Primer Blankslate [S-L08-012], Spectrum IllustratedMessage [S-L08-015], shadcn Empty [S-L08-018].
- **Visual effect:** a designed empty state (message, explanation, action, optional illustration) teaches and invites. A blank area looks broken [S-L13-069].
- **Depends on (upstream):** illustration style (L05), voice (L06), DC-L13-01.
- **Affects (downstream):** tables, lists, dashboards, search results, inboxes, cards, charts (L05 data viz).
- **Token encoding:** spot-illustration size tokens (L05); spacing (L03); no new token types.
- **Platform notes:** same pattern everywhere; mobile uses smaller illustrations [inferred].
- **Accessibility constraints:** the status message must be real text, not only an image [inferred].
- **Default + heuristic:** NN/g's three guidelines: communicate system status, increase learnability with "pull revelation" help, and give a direct pathway (a CTA) [S-L13-069]. For no-results, the CTA is "Clear filters" or a search suggestion [inferred]. Builder lint (warn): collection component with no empty variant, or an empty variant with no action.
- **Evidence:** [S-L13-069, S-L08-012, S-L08-015, S-L08-018]

### DC-L13-11: Onboarding approach
- **Block path:** Patterns > Guidance > Onboarding
- **Questions the designer answers:** Does the product need onboarding at all? Is the interaction model new to users? Do we need setup data or personalization first?
- **Options:**
  - *None:* a self-evident UI. NN/g's first recommendation is to avoid onboarding where possible [S-L13-070].
  - *Contextual help and instructional overlays* at the moment of need: "nice-to-have, not need-to-have" [S-L13-070].
  - *Empty-state guidance* (DC-L13-10).
  - *Interactive walkthrough:* for genuinely new, complex interfaces [S-L13-070].
  - *Deck-of-cards tutorial:* **not recommended**, because it makes the UI look more complicated than it is [S-L13-070].
  - *Setup and personalization flow:* warranted when data is needed [S-L13-070].
  - Atlassian now lists an onboarding component as deprecated [S-L08-011].
- **Visual effect:** tours add friction up front. Contextual tips feel lighter but are easy to miss [inferred].
- **Depends on (upstream):** novelty of the interaction model (DC-L13-17), Paradox of the Active User [S-L13-018].
- **Affects (downstream):** Popover or Coachmark, Toggletip, Empty state, Checklist, Dialog.
- **Token encoding:** none.
- **Platform notes:** app-store listings, not first launch, are the place to promote features to new users [S-L13-070].
- **Accessibility constraints:** coachmarks must be keyboard-reachable and dismissible; focus management as for dialogs [inferred].
- **Default + heuristic:** No forced tour. Use contextual help and empty states. Everything skippable [S-L13-070]. Builder lint (warn): tour with no skip control.
- **Evidence:** [S-L13-018, S-L13-070, S-L08-011]

### DC-L13-12: Microinteraction specification model
- **Block path:** Components > Behavior > Interaction spec
- **Questions the designer answers:** How do we document what a component *does*, not only how it looks? What starts the interaction, what are its rules, what feedback does it give, and how does it behave over time?
- **Options:**
  - *State list only:* Figma variants for default, hover, active, focus, disabled, plus loading, success, error and selected [S-L13-106].
  - *Saffer spec:* **trigger, rules, feedback, loops and modes** (Microinteractions, O'Reilly 2013) [S-L13-079]. NN/g defines a microinteraction as a trigger-feedback pair, where the trigger can be a user action or a system-state change [S-L13-074].
  - *State machine / statechart in code:* Ark UI is "state machine powered" [S-L08-031].
  - The five dimensions of interaction design (words, visuals, physical objects and space, time, behavior; Crampton Smith plus Silver) are a checklist for what the spec must cover [S-L13-107].
- **Visual effect:** well-specified microinteractions show up as consistent press, hover, success and failure feedback across the product [inferred].
- **Depends on (upstream):** motion tokens (L04 F1, F2, F3), haptics (L04), response-time ladder (B5).
- **Affects (downstream):** every interactive component's docs; Code Connect or MCP descriptions (L07); AI-readable component specs.
- **Token encoding:** motion and haptic tokens (L04). The spec itself as structured docs: `trigger`, `rules`, `feedback`, `loops`, `modes` [inferred schema].
- **Platform notes:** haptic feedback is native on iOS and Android and absent on the web (L04).
- **Accessibility constraints:** feedback must not rely on motion or sound alone; honor reduced motion (L04 DC-L04-25) [inferred].
- **Default + heuristic:** Each interactive component documents Saffer's four parts plus its state list. In code, those parts come from a state machine. NN/g lists three functions for microinteractions (system status, error prevention and undo, brand expression); check each one against those [S-L13-074].
- **Evidence:** [S-L13-074, S-L13-079, S-L13-106, S-L13-107, S-L08-031]

### DC-L13-13: Readability and plain-language targets
- **Block path:** Foundations > Content > Readability (L06 owns voice and tone)
- **Questions the designer answers:** Who reads our UI text (general public vs specialists)? What reading level do we target? How long can button labels be?
- **Options (reading-grade targets):**
  - *6th-8th grade* for general audiences.
  - *10th-12th grade* for specialists.
  - Beyond 12th grade takes too much effort even for highly educated readers. Experts prefer plain language too [S-L13-091].
  - *Command labels:* 2-4 words, verb first; describe the resulting state (show "Pause" while playing); ellipsis when more input follows; avoid branded terms [S-L13-036].
- **Visual effect:** shorter strings shrink components, cause fewer truncations and read faster [inferred].
- **Depends on (upstream):** audience definition (questionnaire), brand voice (L06), localization (text expansion) [inferred].
- **Affects (downstream):** all UI strings, error templates (DC-L13-07), empty states, AI disclaimers (DC-L13-16), docs.
- **Token encoding:** none. Content rules live as lint configuration (`content.readingGrade.max`, `button.label.maxWords = 4`) [inferred].
- **Platform notes:** platform-specific verbs ("Tap" vs "Click") should be avoided in shared strings [inferred].
- **Accessibility constraints:** WCAG 3.1.5 Reading Level is AAA [S-V1b-006]. Plain language also serves cognitive accessibility [inferred].
- **Default + heuristic:** Target 6th-8th grade for consumer products and 10th-12th for expert tools [S-L13-091]. Button labels 2-4 words, verb first [S-L13-036]. Builder lint: readability score over the target; button label over 4 words; terms from the team's internal-jargon list.
- **Evidence:** [S-L13-036, S-L13-091]

### DC-L13-14: Inclusive design stance
- **Block path:** Principles > Inclusion
- **Questions the designer answers:** Is accessibility a compliance floor or a design driver? Which permanent, temporary and situational constraints do our users face (one hand, glare, noise, low bandwidth, older eyes)? What can users adjust themselves?
- **Options:**
  - *Compliance-only:* WCAG 2.2 AA [S-L13-098].
  - *Inclusive design:* Microsoft's three principles are Recognize exclusion; Learn from diversity; Solve for one, extend to many [S-L13-072]. The **persona spectrum** runs from permanent (one arm, 26,000 people per year in the US) to temporary (arm injury, 13 million) to situational (new parent holding a child, 8 million) [S-L13-076].
  - *Universal usability* (Shneiderman rule 2) [S-L13-037].
  - *User-adjustable settings:* text size, density, contrast themes, reduced motion [inferred; L01, L02, L03, L04 own them].
- **Visual effect:** inclusive defaults tend toward larger targets, higher contrast and clearer labels. They read as calmer and more legible [inferred].
- **Depends on (upstream):** audience research; legal context (WCAG level referenced by regulation).
- **Affects (downstream):** target sizes (L03), contrast themes (L01), type scaling (L02), motion (L04), captions and media, content (DC-L13-13).
- **Token encoding:** accessibility modes as token modes (contrast, density, motion) (L07) [inferred].
- **Platform notes:** OS settings (Dynamic Type, font scale, Reduce Motion, Increase Contrast) must flow into tokens (L10).
- **Accessibility constraints:** WCAG 2.2 new criteria: 2.4.11 Focus Not Obscured (AA), 2.5.7 Dragging Movements (AA), 2.5.8 Target Size (AA), 3.2.6 Consistent Help (A), 3.3.7 Redundant Entry (A), 3.3.8 Accessible Authentication (AA). 4.1.1 Parsing was removed [S-L13-098].
- **Default + heuristic:** WCAG 2.2 AA as the floor. The questionnaire asks about situational constraints and turns them on (larger targets, contrast theme, captions). Tognazzini: test readability with older users [S-L13-038].
- **Evidence:** [S-L13-037, S-L13-038, S-L13-072, S-L13-076, S-L13-098]

### DC-L13-15: Deceptive-pattern policy
- **Block path:** Principles > Ethics > Deceptive patterns
- **Questions the designer answers:** Which persuasion techniques are off-limits? Do we enforce the policy in the builder or leave it to review? Which laws apply (EU, US)?
- **Options:**
  - *No policy.*
  - *Documented policy:* the 16 types at deceptive.design are sneaking, forced action, hard to cancel, preselection, obstruction, hidden subscription, hidden costs, trick wording, visual interference, fake social proof, fake urgency, nagging, fake scarcity, disguised ads, confirmshaming and comparison prevention. Addictive design and currency confusion are listed separately [S-L13-071].
  - *Enforced lint* for the detectable subset.
  - Legal anchors: EU DSA Art. 25 bans deceptive or manipulative interfaces and names three examples: undue prominence of one choice, repeated requests after a choice was made, and termination harder than subscribing [S-L13-108]. The EU Digital Fairness Act (dark patterns, addictive design) is announced but not adopted, expected Q4 2026 [S-L13-110].
- **Visual effect:** ethical defaults give equal visual weight to accept and decline, unchecked opt-ins, and neutral decline copy [inferred].
- **Depends on (upstream):** DC-L13-18 (emphasis rules), content rules (L06).
- **Affects (downstream):** consent dialogs, checkout, subscription and cancellation flows, pricing pages, countdown and timer components, notification prompts.
- **Token encoding:** none. Lint rules in `$extensions` or config [inferred].
- **Platform notes:** app-store review rules also police some patterns [inferred; not verified here].
- **Accessibility constraints:** visual interference often overlaps with contrast failures (low-contrast decline links) [inferred].
- **Default + heuristic:** Enforce what a machine can detect:
  - pre-checked marketing or consent checkboxes (Preselection);
  - accept and reject with unequal emphasis in consent dialogs (DSA prominence);
  - re-prompting after a dismissal (Nagging, and the DSA repeated-requests example);
  - a countdown component with no real deadline source (Fake urgency);
  - decline copy that matches confirmshaming phrase patterns;
  - a cancel flow with more steps than the signup flow (Hard to cancel).

  Leave the rest to human ethics review. Evidence: [S-L13-071, S-L13-108]; the implementation is [inferred].
- **Evidence:** [S-L13-071, S-L13-108, S-L13-110]

### DC-L13-16: AI interface patterns
- **Block path:** Patterns > AI > Generative and agentic features
- **Questions the designer answers:** How is AI-generated content identified? How are sources and uncertainty shown? What controls does the user get (stop, regenerate, edit, undo, dismiss)? Where do disclaimers go? How human-like is the voice?
- **Options:**
  - *Taxonomies:* Microsoft HAX 18 guidelines (CHI 2019), for example G1 "Make clear what the system can do", G2 "how well", G8 efficient dismissal, G9 efficient correction, G11 "why the system did what it did", G17 global controls, G18 notify about changes [S-L13-089]. They are grouped into four phases: Initially, During interaction, When wrong, Over time [S-L13-082]. Shape of AI's six categories are Wayfinders, Inputs, Tuners, Governors, Trust builders and Identifiers [S-L13-088].
  - *Identification:* Carbon ships an AI label component [S-L08-009]. Shape of AI "Identifiers" covers avatar, color, iconography, name and personality [S-L13-088].
  - *Sources:* style citations distinctly, place them next to the claim, and avoid vague labels like "Source" [S-L13-085]. Show them in drill-down form and show the count of supporting sources [S-L13-084].
  - *Uncertainty:* first-person hedges ("I'm not completely sure, but..."), confidence ratings (numeric or High/Medium/Low) in high-stakes domains, multiple responses with inconsistencies flagged [S-L13-084].
  - *Reasoning displays:* **avoid** step-by-step explanations, because they are "often unfaithful to the model's actual computation" [S-L13-085].
  - *Chat UI:* suggested prompts as buttons; progressive disclosure instead of new messages; **don't autoscroll** to the end of streamed responses; resizable window; save and share; voice input [S-L13-083].
  - Current component sets: Spectrum 2 v1.7.0 has a first preview of AI components [S-L08-027]. shadcn ships AI chat items (Message, Bubble, Attachment, Message Scroller) [S-L08-018].
- **Visual effect:** clear identifiers and distinct citation styling make AI output read as "assistive, check me". Anthropomorphic, human-sounding explanations lead users to overestimate capability [S-L13-085].
- **Depends on (upstream):** brand identity for AI (L06), color and iconography (L01, L05), DC-L13-13 (plain language), DC-L13-15 (ethics).
- **Affects (downstream):** AI label, chat message, citation chip, confidence badge, prompt suggestions, stop and regenerate controls, feedback (thumbs) controls, disclaimers, agent action plans and confirmations (Shape of AI Governors: action plan, draft mode, verification, cost estimates [S-L13-088]).
- **Token encoding:** `color.ai.*` or an `ai` accent role, `icon.ai`, and motion for streaming or "thinking" indicators (L04) [inferred names].
- **Platform notes:** Apple, Google and Microsoft each run their own AI identity conventions. L10 should verify them [inferred].
- **Accessibility constraints:** streamed text must not flood screen readers; announce at completion or in chunks [inferred]. Don't autoscroll [S-L13-083].
- **Default + heuristic:** Label AI content. Put citations next to claims and style them distinctly. Use no reasoning traces as "explanation". Express uncertainty in high-stakes contexts. Put the disclaimer near the input and pair it with an action ("double-check responses") instead of in the footer [S-L13-085]. Provide stop, regenerate, edit and copy controls and a way to give feedback (HAX G9, G15 [S-L13-089]). Use a neutral, non-anthropomorphic voice [S-L13-085]. Show contextual warnings, not repeated generic ones [S-L13-084].
- **Evidence:** [S-L13-082, S-L13-083, S-L13-084, S-L13-085, S-L13-088, S-L13-089, S-L08-009, S-L08-018, S-L08-027]

### DC-L13-17: Convention vs novelty (the Jakob's-law dial)
- **Block path:** Principles > Familiarity
- **Questions the designer answers:** Where do we follow platform and web conventions exactly? Where is a novel interaction worth the learning cost? How do we move existing users through a redesign?
- **Options:**
  - *Platform-native:* follow HIG, Material or Fluent behavior and look (L10).
  - *Conventional behavior with a custom skin:* brand visuals, standard interaction.
  - *Novel interaction model:* only for the product's core differentiator.
- **Visual effect:** native feels trustworthy and instantly usable but generic. A custom skin carries the brand. Novel interaction feels distinctive and costs learnability [inferred].
- **Depends on (upstream):** brand ambition (L06), platform strategy (L10).
- **Affects (downstream):** every component's interaction contract; keyboard shortcuts; gestures; icons (magnifier = search, and so on).
- **Token encoding:** none; platform presets (L10).
- **Platform notes:** M3 Expressive is effectively Android/Compose-only today, and iOS developers push back on porting its look (COMMUNITY-SIGNAL section d). That is a Jakob's-law signal: users expect their own platform's idiom.
- **Accessibility constraints:** keep standard semantics and keyboard behavior (APG, L08) even when the visuals are custom [inferred].
- **Default + heuristic:** Use conventional behavior with a custom skin. Don't override standard shortcuts [S-L13-036]. Be novel only where it is the differentiator, and test it. On a redesign, give users temporary access to the old version [S-L13-006]. Consistency and standards (H4) is the matching heuristic [S-L13-030].
- **Evidence:** [S-L13-006, S-L13-030, S-L13-036, S-L13-055]

### DC-L13-18: Primary action emphasis and placement
- **Block path:** Components > Actions > Emphasis hierarchy (L08 owns button variants)
- **Questions the designer answers:** How many high-emphasis actions can one view hold? Where does the primary action sit relative to the content? How are destructive and cancel actions styled and ordered?
- **Options:**
  - *One primary per view or region:* Von Restorff; restraint prevents competing emphasis [S-L13-014].
  - *One primary per section* in long pages [inferred].
  - *No primary:* all actions equal (toolbars) [inferred].
  - Apple: style, not size, marks the preferred choice, and a destructive button never gets the primary role [S-L08-039]. Sheets put Cancel at the leading edge and Done at the trailing edge [S-L08-040].
- **Visual effect:** a single filled button gives an obvious next step. Several filled buttons flatten the hierarchy and look like ads or noise [S-L13-014].
- **Depends on (upstream):** button emphasis variants (L08), color roles (L01), target size (L03).
- **Affects (downstream):** Button groups, dialogs, forms, cards, toolbars, empty-state CTAs.
- **Token encoding:** button emphasis tokens, for example `button.primary.*`, `button.secondary.*`, `button.destructive.*` (L08, L01).
- **Platform notes:** dialog button order differs by OS (L10) [inferred].
- **Accessibility constraints:** emphasis must not rely on color alone; filled vs outline shape carries it too [S-L13-014]. Target size per L03.
- **Default + heuristic:** At most one high-emphasis action per region. Place the primary after the last field, in reading order, near the content it acts on (Fitts) [S-L13-054]. Label key actions with text and an icon, not an icon alone [S-L13-054]. Builder lint (warn): two or more primary buttons in one group or dialog.
- **Evidence:** [S-L13-014, S-L13-054, S-L08-039, S-L08-040]

---

## Part D. UX research practices used when building a design system (summary; L11 owns process)

NN/g classifies methods on three dimensions: attitudinal vs behavioral, qualitative vs quantitative, and context of use. It also maps them to three phases: strategize, design, and launch and assess [S-L13-092].

| Method | Answers | Phase | Sample size (NN/g) | Use in design-system work | Evidence |
|---|---|---|---|---|---|
| Heuristic evaluation | Which known principles does this UI violate? | Design, audit | 3-5 independent evaluators, 1-2 h each, then consolidate | Audit existing product UIs before building the system; review new components against B1 | [S-L13-093] |
| Usability testing (qualitative) | Where do people struggle, and why? | Design | About 5 per round finds about 85% of problems; prefer three rounds of 5 over one of 15; 3-4 per group when user groups differ | Test patterns (forms, navigation, empty states) in context, not isolated components | [S-L13-096] |
| Usability benchmarking (quantitative) | How good is it, in numbers? | Launch and assess | About 20+ | Before/after metrics for system adoption | [S-L13-096, S-L13-092] |
| Card sorting | How do users group and name content? | Design (generative) | Qualitative: at least 15. Quantitative: 30-50. Hybrid sorts are discouraged | Nav categories, docs-site IA, component taxonomy names | [S-L13-094] |
| Tree testing | Can users find things in a proposed hierarchy? | Design (evaluative) | Few for qualitative, more for quantitative | Validate nav labels. Metrics: success, directness, time. Use instead of closed card sorts | [S-L13-095, S-L13-094] |
| A/B testing, analytics | Which variant performs better at scale? | Launch and assess | Large traffic | Validate a pattern change (for example validation timing) with real conversion data | [S-L13-092] |
| Interviews, field studies, diary studies, surveys | Needs, context, mental models | Strategize | n/a in this lane | Capture the users' domain vocabulary and mental model (A2 "Mental Model") | [S-L13-092] |

**Builder implication.** The builder cannot run research. It can ship templates (heuristic-evaluation checklist from B1, a test script per pattern, a tree-test export of the nav config), and it can record research evidence against decisions [inferred].

---

## Part E. The automation boundary

### E1. What the builder should enforce, warn about, default, or leave to people

| Level | Behavior | Examples (source principle) |
|---|---|---|
| **1. Default** (pre-set, editable) | Ships in every generated system | `size.target.min` fixed across densities (Fitts, WCAG 2.5.8); feedback duration tokens (B5); Button `loading` state that traps repeat clicks (Tognazzini); `autocomplete` on standard inputs (Tesler, Parkinson); input normalization (Postel); Stepper with position and total (Goal-gradient); scaffolded empty, error and success variants (Peak-End, DC-L13-10); live-region announcements (Selective Attention); draft autosave (Protect Users' Work) |
| **2. Lint error** (blocks publish unless overridden with a written reason) | Clear, checkable violations of a Tier A rule | Target below 24x24 CSS px without a spacing exception [S-L13-098]; field with no programmatic label; meaning shown by color only; dialog with no dismiss path; pre-checked consent or marketing opt-in [S-L13-071]; re-prompting after a user dismissed a choice [S-L13-108] |
| **3. Warning** | Likely problems that depend on context | Placeholder-only label [S-L13-066]; two or more primary buttons in a group [S-L13-014]; flat ungrouped list over about 10-12 items with no search [inferred threshold]; more than 2 disclosure levels [S-L13-063]; tour with no skip [S-L13-070]; reading grade over target [S-L13-091]; button label over 4 words [S-L13-036]; standard transition over 500 ms [inferred]; primary action far from the last field [S-L13-054]; collection with no empty state [S-L13-069]; delete with neither undo nor confirm [S-L13-067]; hidden primary nav on wide layouts [S-L13-097] |
| **4. Human judgment** (the builder asks, records the answer, does not decide) | Needs research, taste or ethics | IA and labels; which features to promote or hide; which actions get undo vs confirm; novelty vs convention; tone and celebration; the users' mental model; assortment size; whether any "progress head start" or persuasive default is honest |

### E2. Rules the builder must NOT automate (common misapplications)
- **No "max 7 navigation items" rule.** It is Miller's misuse, and menus rely on recognition [S-L13-048, S-L13-002].
- **No automatic deletion of options to "satisfy Hick's law."** Novices search linearly, so grouping and search fix the real problem [S-L13-050, S-L13-103].
- **No nag or reminder features justified by the Zeigarnik effect.** The memory claim failed replication, and nagging is a deceptive pattern [S-L13-040, S-L13-071].
- **No "strategic delay" feature justified by the Doherty threshold.** Deliberate slowness to seem valuable is a persuasion tactic [S-L13-003].
- **No use of attractiveness scores as a usability signal** [S-L13-053].
- **No hard caps on catalog or result counts justified by choice overload.** The effect depends on its moderators [S-L13-045, S-L13-046].

### E3. Proposed behavior-rule schema (for S1 ontology and the builder)

DTCG 2025.10 has no type for rules, so behavior rules need their own model. They can reference tokens and live in `$extensions` or in a sibling file [inferred].

```json
{
  "id": "target-size-min",
  "principle": ["fitts-law", "wcag-2.5.8"],
  "evidence": "R",
  "scope": "component",
  "appliesTo": ["Button", "IconButton", "Link", "Checkbox", "Tab"],
  "check": { "kind": "static-geometry", "metric": "hitArea", "min": "{size.target.min}" },
  "severity": "error",
  "overridable": true,
  "overrideRequires": "rationale",
  "exceptions": ["inline-text-link", "spacing-equivalent", "user-agent-control", "essential"],
  "sources": ["S-L13-098", "S-L13-054", "S-L03-035"]
}
```

Fields [inferred design]:
- `evidence` uses the R, R-, C, H, P scale from the overview, so the UI can show users how solid a rule is.
- `scope` is one of token, component, pattern, content or flow.
- `check.kind` is one of static-geometry, token-reference, content-text, structure (for example "has empty variant"), flow (for example "cancel steps <= signup steps") or runtime.
- `severity` maps to the E1 levels.
- The exceptions list mirrors the WCAG 2.5.8 exceptions that L03 recorded.

Why a machine-readable form matters: Sanity's published evals found that linting and structured, JSON-shaped docs cut accessibility violations per iteration from 5.1 to 0.6 when agents built with a design system (COMMUNITY-SIGNAL section a, [S-L00-036]). Behavior rules expressed this way can be enforced for human and agent authors alike [inferred].

---

## Cross-lane notes
- [L13 -> L03] Fitts's law values stay in DC-L03-12. L13 adds NN/g's caveat that screen-edge targets help mouse users but hurt touch users [S-L13-054], plus the rule "hit area never shrinks with density" as a lint (E1).
- [L13 -> L04] The response-time ladder (B5) sets the ceiling for feedback. Acknowledge input within 50 ms and never let an animation delay it. The Doherty threshold of 400 ms matches M3 medium4 as a practical ceiling for standard transitions. Animated skeletons fall under reduced motion (DC-L04-25).
- [L13 -> L08] Components need these behavior requirements: Button `loading` state that traps repeat submits; destructive dialogs with verb labels and Cancel as the safe default; Toast with an Undo action and pausable timing; an empty variant on every collection; Field with a persistent label, hint and error slot (no placeholder-as-label); Stepper with position and total; Skeleton; AI label, citation and confidence components (DC-L13-16). Primer's deliberate lack of a Toast is a useful counter-example for DC-L13-09.
- [L13 -> L06] Content rules: reading-grade targets (6-8 consumer, 10-12 expert) [S-L13-091]; command labels 2-4 words, verb first [S-L13-036]; error template "what happened, then how to fix it" [S-L13-064]; confirmshaming and trick-wording bans [S-L13-071]; non-anthropomorphic AI voice [S-L13-085].
- [L13 -> L15] The five Gestalt laws (Proximity, Similarity, Common Region, Uniform Connectedness, Prägnanz) are listed here with one line each; L15 owns them. The proposed lint is "space inside a group is smaller than space between groups".
- [L13 -> L14] Device notes for L14: edge targets are worse on touch [S-L13-054]; hidden mobile navigation lowered navigation use (44% vs 89% across two sites) [S-L13-097]; onboarding promotion belongs in store listings, not first launch [S-L13-070].
- [L13 -> L11] Research methods summary (Part D). Heuristic evaluation with 3-5 evaluators is a cheap governance gate for new components [S-L13-093]. Jakob Nielsen personally is disputed in the community, but NN/g articles remain Tier B (COMMUNITY-SIGNAL).
- [L13 -> L07] Behavior rules need a home outside DTCG `$type`s: the E3 schema in `$extensions` or a sibling `rules.json`. Feedback thresholds are ordinary duration tokens.
- [L13 -> L01] Von Restorff and WCAG 1.4.1: emphasis color is scarce (one primary per region) and never carries meaning alone.
- [L13 -> L05] Empty-state illustrations and AI identifiers (Shape of AI: avatar, color, iconography [S-L13-088]) need spot-illustration and AI icon slots.
- [L13 -> S1] Add a "Behavior rules" layer to the ontology, parallel to tokens and components (E3). The questionnaire should ask: audience reading level, novice vs expert mix, situational constraints (persona spectrum), undo capability of the data model, convention vs novelty stance, AI features present, and jurisdictions (EU DSA and DFA).
- [L13 -> V1] Figma's "Button states" resource-library article claims all states need 4.5:1 contrast and focus rings need 3px [S-L13-106]. Both contradict WCAG: disabled or inactive components are exempt from 1.4.3, and 2.4.13 (AAA) specifies a 2 CSS px perimeter. Do not import those two values.

## Open questions / gaps
- **Primary sources not read directly:** the Ghibellini and Meier 2025 paper (nature.com redirected to a login; findings corroborated by a search snippet from the publisher listing and by Wikipedia), Scheibehenne et al. 2010 (search snippet only), Cowan 2001 (search snippet only), the Doherty and Thadani 1982 IBM paper (only via lawsofux), and Saffer's book (via the publisher blurb on Goodreads; microinteractions.com now redirects to an unrelated domain).
- **Google PAIR People + AI Guidebook** did not render (JavaScript), so it is not covered. The HAX four-phase grouping is confirmed by the Microsoft Research page, but I did not re-verify which guideline numbers fall in which phase.
- **Some thresholds are my inferences, not sourced:** the about 10-12 item flat-list warning, the 500 ms transition warning, the 3-4 pricing-tier hint, and the style-count limits. The builder should expose them as configurable, and V1 should treat them as inferred.
- **Not verified in this lane:** WCAG SC numbers other than the 2.2 additions (1.3.1, 1.3.5, 1.4.1, 2.2.1, 2.4.4, 2.4.6, 3.1.5, 3.3.1-3.3.4 are cited from knowledge and tagged [inferred]); top-aligned vs left-aligned label evidence; floating labels; type-to-confirm conventions; platform dialog button order (L10).
- **Evidence on Serial Position for navigation choice** (as opposed to list recall) was not found.
- **Perplexity was unavailable** (HTTP 401, quota), so every check went through WebSearch and WebFetch.
- **Baymard:** only the inline-validation article was read. Baymard's checkout and form-field research (field counts, label placement) is paywalled and not covered.
- **NN/g AI guidance moves fast.** The three articles used are dated 2025-02, 2025-12 and 2026-04. Recheck them before the builder ships AI patterns.

## Confidence
- **High (Tier A or B source read live today):** the list of 30 laws and their definitions and origins as stated by lawsofux.com; Nielsen's 10 heuristics wording and dates; Shneiderman's 8; Tognazzini's 19 principles and the verbatim 50 ms rule; Norman's revised-edition addition of signifiers; the response-time limits and NN/g loading guidance; INP and RAIL thresholds; the WCAG 2.2 new criteria; NN/g form, error, confirmation, empty-state, onboarding, scanning, plain-language and AI guidance; Baymard's 31%/4% inline-validation figures; Chernev 2015 meta-analysis moderators; Kivetz 2006 findings; Cockburn and Gutwin 2007 menu model; the deceptive.design taxonomy; DSA Art. 25 text; DFA status; Microsoft inclusive principles and persona spectrum numbers; Shape of AI categories; HAX guideline titles.
- **Medium (corroborated secondary):** the Zeigarnik meta-analysis result (publisher snippet plus Wikipedia); the Scheibehenne 2010 near-zero mean; Cowan 4±1; the peak-end meta-analysis numbers (EconPapers abstract plus snippet; "average predicts as well" is snippet-only); Saffer's four parts.
- **Inferred (tagged in text):** evidence-strength classifications (my scale), all builder guardrails and thresholds not attributed to a source, token names, the rule schema, and the mapping of principles to components.
