# L22: Making and reviewing pages (private, first-party project evidence)

## Lane overview

- **What this lane does.** OpenDesigner's process ends when the system is exported (`docs/HOW-IT-WORKS.md` sections 8 and 9). This lane covers what comes next: building pages with the system and going round after round with the person who decides. It reads the full decision trail of one build and turns what worked, and what did not, into nine Decision Cards, evidence on existing cards and standards, and a guide for agents (`skills/opendesigner/references/making.md`).
- **The source.** S-L22-01, "Decision trail of one B2B marketing-site build by several AI sessions under one owner's review (private, first-party project evidence, 2026)". It is not public and has no licence, so it cannot enter `learn/sources.json` (`learn/IMPROVING.md` section 4 asks for public pages only). It enters as this research lane instead. Every file opened is in `traces/L22-trace.md`.
- **What the trail holds.** 1,133 ledger events at the cut-off (the evening of the last working day), over two weeks and 8 working days: 291 decisions (260 made by the owner, with the owner's words quoted), 262 work records, 259 stored subagent reports, 109 checks and 39 findings about the design tool. A reader's digest of the trail counts 137 corrections by the owner and 35 acceptances, and puts 153 of the owner's 260 decisions (59%) as corrections of something already shown. The subagent reports were not re-read for this lane.
- **What the project did not do.** It set out to build its design system with OpenDesigner. One sketch-level build ran in a sandbox on the first day and fed the first proposal page [S-L22-01: E-260929-f807]. It was never promoted to the project, and the built draft took no values from it: the draft's style sheet still says it will be regenerated from the token build later. No research summary and no structure step were produced; `engine.py review` never ran on the draft; the planned accessibility and performance passes did not happen. The owner asked for a built draft on the first day, the draft was deployed for the owner's team that evening, and it became the product. Values lived in three separate style kits [S-L22-01: digest, planned process]. So this lane is evidence of what happens when making outruns the system, and of what held the work together anyway. It is not evidence that the engine's outputs work on a real page.
- **How it is cited.** By the ledger's own ids: D- is a decision, E- a work record or hand-off, V- a check, F- a finding. "audit" is the cohesion audit of one page and its measurement files. "notes" are the builder's private notes on the owner's standing preferences. "session record" is the builder's own record of the last working day, for the few points the ledger does not hold. "digest" is a reader's count over the whole trail. "project files" means the state of the project folder on the last day. Identifying details of the project (its name, brand, customers, copy and the references it studied) are left out on purpose.
- **Authority.** Reference material, treated like Tier C (`_coordination/SCHEMA.md`). It shapes options, evidence and agent behavior. It never sets a default value by itself (`docs/KNOWLEDGE.md` sections 1 and 2). Every number below is one project's evidence: a starting point to test, not a rule. One owner's taste is evidence about that owner, not about design.
- **The main finding.** Most of what this project learned the hard way was already a house standard. STD-process-review-taste-37 to -49 say how options are named, limited, built, isolated, compared one at a time, verified and cleaned up. They are filed under a theme that reads as motion only, and nothing in the skills sends an agent that is building a page to them. The guide added here is that route (Part C). Nine lessons had no card, so they get one each (Part A). The ninth lists the builder's own recurring mistakes.
- **What changed in OpenDesigner.** Agent instructions, one output template and one section of the how-it-works page (Part C). No house standard, no `synthesis/standards.json` entry, no question, no default and no engine code changed. Where the project's practice differs from a standard, Part D sets out both positions for the maintainer to decide; none of them is applied.
- **Relation to lane L21.** L21 (pull request 52, not merged when this was written) brings a design playbook from a different project. Both lanes reach some of the same conclusions from separate evidence: one example in feedback stands for a class, and a builder whose inventions are rejected should follow a reference. This lane does not edit `rules.md` or `guardrails.md`, where L21 writes those points, and cites none of its card ids. Both lanes add rows to the same table in the extend skill, at different places. Part B says where the two agree.

## Part A: Decision Cards

### DC-L22-01: Pace of the work: approval gates, or a built draft the owner reacts to
- **Block path:** Builder > Process > Pace of making (after the system exists; `references/making.md` sections 1, 2 and 9)
- **Questions the designer answers:** Do you want to approve a plan step by step, or decide by looking at something built? When may building start? When you ask for more options, should the builder invent them or rebuild shipped work? When does exploring outside the system stop?
- **Options:**
  - **Gates first:** brief, research, system, structure, build and checks, each approved before the next. The builder proposed six gated phases on the first day. The owner never accepted the proposal, and asked the same day for a built draft to review [S-L22-01: D-260929-4e36, D-260929-7ed0]. All later work ran as review rounds on built pages.
  - **What became of the plan.** None of the six gates was ever recorded. The research summary and the structure step were never produced, the one sketch build stayed in its sandbox, and the draft became the product: it was deployed for the owner's team on the first evening [S-L22-01: D-260929-7ed0, D-260929-1ec6, E-260929-f807; project files]. One section the owner approved was reopened five days later, and the record could not say what the approval had covered [S-L22-01: D-261006-b6cb, D-261011-778c].
  - **Draft first:** build early and let the owner react. It found this owner's taste quickly: ideas the owner had asked for were judged and reverted within minutes of being seen [S-L22-01: D-260930-2f26, D-260930-bbe3, D-261005-3d62], and a switch on the real page was answered in 9 to 46 minutes [S-L22-01: D-260929-ff85, D-261012-93d3, D-261012-926e]. Its costs in this project: structure was never settled, so dedicated pages were first made as copies of home-page sections and took three passes [S-L22-01: D-260929-6fb2]; the draft took no values from the sketch build, so values lived in three separate style kits; and one page ended with four design languages (DC-L22-03).
  - **Draft first, with the system as the only source of values and a debt list:** building may start as soon as a sketch-level token build exists (`zoom.md`, level 0), and the draft reads its values from that build's export instead of keeping a style file of its own; every value comes from the tokens or is listed as debt; the page's materials are fixed before the second section; a cohesion check runs before the page is called done [inferred from the costs above: a sketch build existed here, and nothing bound the draft to it].
  - **Invent, or rebuild shipped work.** Whole rounds of the builder's own options were removed. All five standing versions of one section went; they had been drawn loosely "after" named references instead of rebuilt from them [S-L22-01: E-261012-103d, D-261012-01ef]. A rebuild in this sense takes a section's structure with the person's own words and assets. In this project the rebuilds also borrowed each reference's type and color on private review pages before being brought into the brand; OpenDesigner's identity firewall stops at structure (`guardrails.md` section 1), and this lane does not propose changing that. Five of six directions for another section went too [S-L22-01: D-261011-5bec]. Nine variations of the one survivor drew the reply that the builder had only repeated it, and five were removed; five "new ideas" that reused the house assets were removed outright [S-L22-01: D-261011-b965, D-261012-20ba]. Twenty study builds for one section, the builder's own designs made after looking at 24 shipped examples, were all discarded after three passes in 33 minutes [S-L22-01: E-260930-d5bf, D-260930-2d81, D-260930-48bb]. The owner then named the method: rebuild real, shipped sections from a library, and set the system aside while experimenting [S-L22-01: D-261012-2926]. The builder planned to bring only the pick back into the system; the owner instead had all eight rebuilds aligned to the brand first, and cut them to two about five hours after first seeing them [S-L22-01: E-261012-ebce, D-261012-e3ca, D-261012-6cb4]. Rebuilds were cut hard (six of eight, and two of three), but the pages the owner kept working on were built on one of them [S-L22-01: D-261012-6cb4, D-261012-f9ac].
  - **What the owner says, and what the owner picks on seeing it.** A reader's digest counts ten cases where a stated preference was reversed on sight, some within minutes: a light ground asked for, and the all-light page it produced found dull 78 minutes later; a slow hover asked for and sped up two minutes later; every animation on phones asked to be removed, and 40 minutes later only the scroll effects had been meant [S-L22-01: digest, pattern 16; D-260929-dec7, D-260929-be0f, D-261005-3d62, D-260929-15e1, D-260929-8591]. Analysis did no better at predicting the choice: an audit of a set of product screens by several reviewers (ten, by the digest's count) recommended one shared layout, one shared story and a floor on text size, and the owner reversed all three, the last about 28 hours after the audit was handed over [S-L22-01: D-261011-13ef, D-261011-3c17, D-261011-2e86; digest, pattern 15]. Measurements of faults, and of whether stated rules were kept, were welcome every time [S-L22-01: digest, pattern 15].
  - **Research before, or after each rejection.** The planned research summary was never written. References were fetched after each rejection instead, and about 35 builds were discarded in two days: 25 of 28 directions for one section and 10 of 16 for another [S-L22-01: digest, pattern 2].
  - **Options from what is already in the repo:** rejected when options were asked for. Ten backgrounds picked from existing files were all refused; ten new ones produced a pick in three minutes [S-L22-01: D-261012-60ce, D-261012-9a48].
- **Visual effect:** none directly. Draft first gives something to react to on day one. Without the safeguards it also gives a page whose sections do not match (DC-L22-03).
- **Depends on (upstream):** the brief (what the page must make someone do), the person's references and how shipped products are studied (DC-L19-178), an exported system.
- **Affects (downstream):** when building starts, the debt list, how options are produced (DC-L22-02), the cohesion check (DC-L22-03).
- **Token encoding:** none (process decision).
- **Platform notes:** none.
- **Accessibility constraints:** a draft is not exempt from the accessibility floors (`guardrails.md` section 4).
- **Default + heuristic:** When the person wants to see something built, build the draft on a sketch-level token build and keep three things: every value from the tokens or on the debt list, the page's materials fixed before the second section, and a cohesion check before "done" [inferred]. A stated preference is something to test: build the smallest real version and keep the version before one switch away [inferred]. Heuristic: study shipped examples before inventing options (DC-L19-178); when invented options are rejected, rebuild a few shipped examples on a review page [S-L22-01: D-261012-2926]. "More like this one" asks for new ideas, not near-copies [S-L22-01: D-261011-b965].
- **Evidence:** [S-L22-01: D-260929-4e36, D-260929-7ed0, D-260929-1ec6, E-260929-f807, E-261012-103d, E-260930-d5bf, E-261012-ebce, D-260929-15e1, D-260929-8591, D-261006-b6cb, D-261011-778c, D-260929-6fb2, D-260929-dec7, D-260929-be0f, D-261011-13ef, D-261011-3c17, D-261011-2e86, D-260929-ff85, D-260930-2d81, D-260930-48bb, D-260930-2f26, D-260930-bbe3, D-261005-3d62, D-261011-5bec, D-261011-b965, D-261012-20ba, D-261012-2926, D-261012-e3ca, D-261012-6cb4, D-261012-01ef, D-261012-f9ac, D-261012-60ce, D-261012-9a48, D-261012-93d3, D-261012-926e; digest, patterns 2, 15 and 16; project files]. Compared against DC-L19-178.
- **Maps to:**
  - `references/making.md` sections 1, 2 and 9. Applied.
  - `docs/HOW-IT-WORKS.md` section 9, "Making and reviewing pages". Applied.
  - DC-L19-178: evidence that its "research shipped products first" default also holds for sections of a marketing page, not only for flows with domain rules. The faithful rebuild with the system set aside goes past what that card says (study, report, then build with the system's tokens), and came from the owner. For L20.
- **Impact now / as it grows:**
  - *Gates first:* now, nothing to look at for days. As it grows, fewer rebuilt pages, if the person can judge a plan.
  - *Draft first:* now, fast reactions. As it grows, debt nobody listed.
  - *Draft first with safeguards:* now, a short list to keep. As it grows, the draft can become the product.

### DC-L22-02: Comparing options on a built page: switches, a kept baseline, and boiling down
- **Block path:** Builder > Review > Options on a built page (`references/making.md` section 3; STD-process-review-taste-37 to -49)
- **Questions the designer answers:** How do you want to compare options for a page that already exists? What is the baseline? What if several questions are open at once? What happens to the options after you decide?
- **Options:**
  - **A picker of variants of one piece,** one at a time and full size: the house standard (STD-process-review-taste-43, -45, -46) and DC-L19-174's default.
  - **Several named switches on the real page, one per open question, with the current version kept as an option.** This project's working form. Pickers on the real page date from the first day: a section on two grounds, and four layouts for another [S-L22-01: D-260929-93ee, D-260929-ff85, D-260929-e075]. Later came three versions of six screens on one page with feature switches [S-L22-01: D-261010-0eb5], then switches for a section's drawing, the page's background, the heading style and a layout [S-L22-01: D-261012-3775, D-261012-93d3, D-261012-e73f], and last a switch between the current page and two whole-page directions for the owner's team, kept beside four other open options [S-L22-01: D-261012-f886, D-261012-4ed1, E-261012-d7e0]. Of the 35 acceptances in the trail, a reader's count puts 12 behind a switch or side-by-side variants on the real page [S-L22-01: digest of acceptances].
  - **A written description with small maps:** not enough to decide from. Given a report that described five directions, the owner chose two and asked to see both built before deciding [S-L22-01: D-261012-f886].
  - **What went wrong with switches in this project:**
    - Review controls were left on the page after the pick, twice [S-L22-01: D-260929-e075, D-260929-2286].
    - A fold-away control had to be added once a page carried several rows of options; the owner had said they were in the way [S-L22-01: E-261012-f5e4; session record].
    - A switch changed one section when the owner wanted to judge the whole page [S-L22-01: D-261012-5e45].
    - An option restyled a page the owner had already approved, and had to be reverted [S-L22-01: D-261012-9698].
    - Options were shown after the builder had looked only at small full-page thumbnails; buttons were broken [S-L22-01: E-261012-6b76; notes].
  - **After the decision:** remove the switch, keep the choice, record it [S-L22-01: D-261012-926e, D-261012-4ed1]. This owner wanted rejected options kept out of the product but not deleted [S-L22-01: D-261011-5bec; notes], and a second version kept beside the pick [S-L22-01: D-261006-7c4d].
- **Visual effect:** none on the product. On the review page: the real page, with a small control at one edge.
- **Depends on (upstream):** how variants are generated and compared (DC-L19-174), the size at which layouts are judged (DC-L19-56), the prototype standards.
- **Affects (downstream):** how many combinations must be checked before a hand-off (STD-process-review-taste-47), what is cleaned up after a pick (STD-process-review-taste-49), the debt list.
- **Token encoding:** none. Review controls are outside the system and never take its tokens (STD-process-review-taste-45).
- **Platform notes:** web: each switch has an address in the URL, so one combination can be shared and tested. A review route is kept out of the sitemap and the deploy [S-L22-01: D-261004-4127].
- **Accessibility constraints:** the controls are reachable by keyboard. STD-process-review-taste-46 fixes the keys and ignores them while the person is typing in a field.
- **Default + heuristic:** For one piece, the house standards hold as written: three options by default, one at a time, full size, in the real page. Where several questions are open on one page, give each its own switch and keep the current version as an option [inferred from this project's accepted rounds]. Heuristic: count the combinations before adding a switch, because every one must be flipped through before the hand-off (STD-process-review-taste-47); boil down as soon as a question is answered [inferred].
- **Evidence:** [S-L22-01: D-260929-93ee, D-260929-ff85, E-261012-d7e0, D-261010-0eb5, D-261012-3775, D-261012-93d3, D-261012-e73f, D-261012-f886, D-261012-4ed1, D-261012-926e, D-260929-e075, D-260929-2286, E-261012-f5e4, D-261012-5e45, D-261012-9698, E-261012-6b76, D-261011-5bec, D-261006-7c4d, D-261004-4127; digest of acceptances; notes; session record]. Compared against DC-L19-174, DC-L19-56 and STD-process-review-taste-37 to -49.
- **Maps to:**
  - `references/making.md` section 3. Applied.
  - STD-process-review-taste-45 and -46 (the picker): a form with several switches and a fold-away control is proposed in Part D3. Not applied.
- **Impact now / as it grows:**
  - *One picker per piece:* now, simple. As it grows, slow when sections must be judged together.
  - *Several switches:* now, fast decisions on the real page. As it grows, combinations multiply, so boiling down is part of the method.

### DC-L22-03: What stays the same between sections, and the audit when it did not
- **Block path:** Patterns > Page composition > Cohesion across sections (`references/making.md` section 4; `assets/output/COHESION-AUDIT.md`)
- **Questions the designer answers:** Sections may differ in layout. What may not differ? Who checks, and when? When a page stops looking like one page, how do we find out why before changing anything?
- **Options:**
  - **No constants:** each section follows its own reference. In this project several rounds each built one section to a strong reference. For one section the owner asked for the system to be set aside while experimenting, and that section was brought back into the brand the same night [S-L22-01: D-261012-2926, D-261012-e3ca]. The sections built to references in later rounds were not reconciled with the rest of the page until the owner said it did not hang together [inferred from the audit].
  - **Page materials fixed before the second section:** type families and their jobs, one heading style, which corner rule belongs to which kind of thing, how a box is drawn, where content starts and ends, one dark text color and one accent, how photographs are treated, how a stepping section is controlled [inferred from the audit's columns and its findings on photographs and colors].
  - **An audit after the fact.** The same eight questions were asked of all eleven sections and measured on the rendered page [S-L22-01: V-261012-1e2d; audit]. It found:
    - four design languages on one page;
    - seven type families, with two neighboring sections sharing none for their small text;
    - three corner rules: one section had 20 boxes, all square, with no shadows; the next had four different curves and 18 shadows;
    - five ways to draw a box;
    - content starting and ending in four different places;
    - three near-blacks and three blues;
    - headings that matched in style but not in placement.
  - **Complaints matched to causes.** The owner called three sections "bland" or "narrow". The audit traced "bland" mostly to contrast in how much there was to look at, after three dense sections. For one of the sections it also named that section's own photograph treatment as the main reason [S-L22-01: audit, findings 6 and 7].
  - **Directions, not one fix.** The report offered five: the least effort, the most adaptable, and three led by a section the owner liked. The owner answered the report point by point within 37 minutes, chose two directions and had both built as a switch [S-L22-01: D-261012-f886, D-261012-4ed1].
  - **Page rules broken again by sections built later.** A rule against small labels above headings was set on the first day and broken on two later occasions, by pages and a section built afterwards: four removal decisions in all [S-L22-01: D-260929-9658, D-260929-7ad9, D-260929-8d02, D-261012-93d3]. A section heading was shrunk to save room, and another arrived in its reference's heavy capitals [S-L22-01: D-260929-35fd, E-261012-754c].
  - **Restyle is not resize.** Cards and type grew a little in each restyle until the owner said so [S-L22-01: E-261012-f5e4; notes].
  - **A light section does not become a dark one by swapping colors.** Dark versions of three sections the owner was content with were withdrawn [S-L22-01: D-261012-a482, D-261012-832c]. Icon discs that had been inverted mechanically for a dark ground went back to their light-ground color at the owner's word [S-L22-01: D-260929-fefd].
- **Visual effect:** with constants, sections can vary in layout and still read as one page. Without them the reader meets a new idea of "card", "label" and "edge" in every section.
- **Depends on (upstream):** the system's type, shape, depth and color decisions; variety between sections (DC-L19-50); how sections are separated (DC-L19-53); the interface inventory (DC-L11-04).
- **Affects (downstream):** every section built later, `engine.py review` (it reports values that are not tokens, and cannot count families or box styles per page), the debt list.
- **Token encoding:** none new. The audit reports rendered values next to the tokens they should have been.
- **Platform notes:** the audit measures the rendered page in a browser. It is not part of the engine, whose scripts have no browser.
- **Accessibility constraints:** none new. A page that keeps one heading style and one text color is easier to check for contrast and heading order.
- **Default + heuristic:** Vary layout, hold materials [inferred; a companion to DC-L19-50, which asks for varied layouts and limits how far a section may break the grid, and says nothing about type, corners or boxes]. Fix the materials before the second section is built. When the person says the page does not hang together, audit before restyling: the same questions for every section, measured, with each complaint matched to a cause, and at least a least-effort and a most-adaptable direction [inferred from one accepted audit]. A restyle does not change sizes [S-L22-01: E-261012-f5e4; notes]. The counts above are one page's measurements, not limits.
- **Evidence:** [S-L22-01: V-261012-1e2d, D-261012-f886, D-261012-4ed1, D-261012-2926, D-261012-e3ca, D-260929-9658, D-260929-7ad9, D-260929-8d02, D-261012-93d3, D-260929-35fd, E-261012-754c, E-261012-f5e4, D-261012-a482, D-261012-832c, D-260929-fefd; audit; notes]. Compared against DC-L19-50, DC-L19-53 and DC-L11-04.
- **Maps to:**
  - `references/making.md` section 4 and `assets/output/COHESION-AUDIT.md`. Applied.
  - DC-L19-50: proposes "vary layout, hold materials" as its companion limit. For L20 and Part D4. Not applied.
- **Impact now / as it grows:**
  - *No constants:* now, each section looks its best alone. As it grows, each round adds a design language.
  - *Materials first:* now, a short list to agree. As it grows, new sections fit without an audit.
  - *Audit after the fact:* now, a day's work. As it grows, the only way back once the debt exists.

### DC-L22-04: Finished interface shown inside a page
- **Block path:** Imagery > Product views > Live product views inside a page (`references/making.md` section 6)
- **Questions the designer answers:** When a page shows the product, is it a picture, a simplified mock-up or a real interface running inside the page? How small may its text get? What keeps the page's styles and the interface's styles apart? What does a phone show?
- **Options:**
  - **An abstract animated diagram:** rejected. The owner expected screens that look like the product and sent examples [S-L22-01: D-261005-7494].
  - **A simplified mock-up, large and fully readable:** rejected as looking like a mock-up, not a real product. The builder had been holding every label to an 11 px floor [S-L22-01: D-261011-2e86, F-261010-3f5c].
  - **A complete interface at real size, shown scaled like a screenshot:** this project's accepted form, built on a fixed canvas and shown at about 73%. Real density; small detail may fall below reading size; a few large elements carry the story [S-L22-01: D-261011-2e86]. A review that reads type sizes from tokens can pass while such text renders at 8 to 10 px. Which parts must stay readable has to be decided and measured as rendered [S-L22-01: F-261010-3f5c, F-261011-b5ef].
  - **One shared shell and one shared story for every screen:** rejected twice. Six screens on one shell read as one app, and five of six told the same story, which narrowed what the site seemed to sell [S-L22-01: D-261011-13ef, D-261011-3c17, D-261011-e685].
  - **Two style worlds in one page.** The page's short class names, bare element rules and click handlers reached into the embedded interface, and the interface's generic state classes were matched by page rules [S-L22-01: F-261010-7866, F-261011-3f97]. Later, one page rule aimed at every icon stroke changed the color of every icon inside the screens, in two of three page options; the fix was to scope the rule and compare the screens with the untouched page [S-L22-01: E-261012-10ad, V-261012-5819]. A page rule for a section named like a button wrapper restyled the header's button [S-L22-01: E-261012-6b76].
  - **On a phone:** shrunk to under a third of its size it could not be read. The accepted form shows part of the screen at a readable size and moves the view to follow the story [S-L22-01: D-261011-3706].
  - **Cost of loading:** six live screens made the page slow and blank at first. Loading each one when needed, and painting only the one that shows, took the time to interactive from 549 ms to 32 ms on the test machine [S-L22-01: D-261011-ae93, V-261011-3c26].
  - **Every page that shows the same screens changes in the same pass.** The owner had to ask twice in 17 minutes [S-L22-01: D-261011-a5b7, D-261012-c30e].
- **Visual effect:** a real interface at real density reads as a product that exists. A large simplified one reads as an illustration of a product.
- **Depends on (upstream):** whether marketing pages show the product at all (DC-L19-131, DC-L19-72), how a screenshot is framed (DC-L19-73), sample content (DC-L19-35).
- **Affects (downstream):** page weight, the phone layout, every page that reuses the same views, the checks in DC-L22-05.
- **Token encoding:** none new. The embedded interface may carry its own small set of interface tokens; the page's tokens must not reach into it. Whether a system needs a named product-view layer is an open question [S-L22-01: F-261010-6bc8].
- **Platform notes:** web: prefix every class inside the embed, state classes included; write its resets so that each weighs one element (wrap only the scoping part in `:where`), which beats the page's element rules and still loses to the embed's own classes; scope page rules that target bare elements or attributes [S-L22-01: F-261010-7866, F-261011-3f97].
- **Accessibility constraints:** text that falls below reading size inside a scaled view is decoration, so the same information is also given in the page's own text [inferred]. Movement inside the view follows the reduced-motion setting.
- **Default + heuristic:** Whether to show the product rests on DC-L19-131, which says to use the real product; here the views were built for the page with invented data, so this card is about that form only. How: build the view at real size and show it scaled; name the parts that must stay readable and measure them as rendered; keep the two style worlds apart in both directions; after any page-wide restyle, compare the view with the version before; on a phone, crop and move the view instead of shrinking it [inferred from this project's accepted rounds]. Heuristic: if a page rule has no class in its selector, assume it reaches into the embed.
- **Evidence:** [S-L22-01: D-261005-7494, D-261011-2e86, D-261011-13ef, D-261011-3c17, D-261011-e685, D-261011-3706, D-261011-ae93, V-261011-3c26, D-261011-a5b7, D-261012-c30e, E-261012-10ad, V-261012-5819, E-261012-6b76, F-261010-3f5c, F-261010-6bc8, F-261010-7866, F-261011-3f97, F-261011-b5ef]. Compared against DC-L19-131, DC-L19-72, DC-L19-73 and DC-L19-35.
- **Maps to:**
  - `references/making.md` section 6. Applied.
  - `engine.py review`: a rendered-size check is proposed in Part D5. Not applied.
- **Impact now / as it grows:**
  - *A picture:* now, cheapest, and nothing can leak. As it grows, it goes stale with the product.
  - *A live view:* now, the strongest proof, with real cost in weight and isolation. As it grows, every page-wide change must be checked against it.

### DC-L22-05: Where a built page is checked before it is shown
- **Block path:** Builder > Verification > Checking the rendered page (`references/making.md` section 5)
- **Questions the designer answers:** In which browser and at what window size do you look at the work? Which sizes does the builder check before showing you anything? What does it do when you report something it cannot see?
- **Options:**
  - **The usual breakpoints in one browser engine:** this project's starting practice. A reader's digest counts 19 occurrences of checking where it was convenient, 18 of them corrections by the owner. Ten of the 109 recorded checks say that the owner's browser or a real device was not checked, and one of the 109 is the owner's own look [S-L22-01: digest, pattern 3].
    - The phone width was not opened before the first review; the owner found it broken and it took five rounds in 40 minutes [S-L22-01: D-260929-a70e, D-260929-15e1, D-260929-8591].
    - Six screens were checked in one engine only, with no phone [S-L22-01: V-261011-c460].
    - A fix that set a gap without the row it needed left the layout as it was, and the owner had to ask a second time; a look at the result would have shown it [S-L22-01: D-260929-295d, D-260929-e353] [inferred for the last clause].
  - **Add the owner's own window.** The builder tested at 1440 to 1515 px while the owner reviews in a window 1800 px wide, in a different browser engine [S-L22-01: notes; V-261012-5819].
  - **Add the widths between the breakpoints.** A tablet rule squeezed one layout at widths nobody had opened; on a tablet a held section overlapped the next one [S-L22-01: V-261012-898b, D-261005-e5ae].
  - **Add a pass with no hover.** A list that changed its picture on hover did nothing on a phone until the owner pointed it out [S-L22-01: D-261012-0509].
  - **Look at your own screenshots.** The owner asked for it in so many words after a round that was visibly broken [S-L22-01: D-261012-f9ac].
  - **Compare with the version before** for everything the change was not meant to touch. This is how a color leak into embedded screens was confirmed fixed [S-L22-01: V-261012-5819].
  - **Record the real window for motion.** A recording at full pixel density showed a patterned card being redrawn on 68 of 131 frames, which no still could show [S-L22-01: D-261012-eb40]. Record only the test window: a recording of a screen region once caught the owner's other windows [S-L22-01: notes].
  - **When a reported fault cannot be reproduced:** say so. A flicker the owner reported did not appear in any recording; it was handed over as open and not as fixed [S-L22-01: E-261012-a6a8]. An earlier flicker fix was real, but it was not the fault the owner meant, and a second cause was found only after a second report [S-L22-01: D-261012-5c86, D-261012-eb40].
  - **Check a measurement before it carries a recommendation.** The builder measured an existing moving strip as static, recommended replacing it, and was overruled. The measurement was wrong: it had been taken in a background tab where the page's animations had not started [S-L22-01: D-260929-21c4, V-261004-61f2].
- **Visual effect:** none. Fewer rounds are spent on faults the builder could have seen.
- **Depends on (upstream):** the breakpoint set (DC-L03-14), the size at which layouts are judged (DC-L19-56), which device counts as proof (DC-L19-153), what the builder's checks cannot judge (DC-L19-167).
- **Affects (downstream):** the closing report (what was checked and what was not), the check-by-hand list.
- **Token encoding:** none.
- **Platform notes:** web. A full-page screenshot taken under touch emulation can drop the touch state, so it may show the mouse layout [S-L22-01: session record]. A headless build of a browser engine may not draw background blur, so its cost there stays unmeasured [S-L22-01: V-261011-3c26].
- **Accessibility constraints:** the no-hover pass is also the keyboard and switch pass: nothing needed is reachable only by hover (DC-L19-143). Hover styles sit behind a fine-pointer query (STD-accessibility-motion-15).
- **Default + heuristic:** Rests on DC-L19-56, DC-L19-153 and DC-L19-167, which stand. This project adds four habits, each [inferred] from its rework: ask once what the person reviews in and test there; test between the breakpoints; test with no hover; compare with the version before. Heuristic: if the builder has not looked at a screenshot of the change at the person's window size, it has not been checked.
- **Evidence:** [S-L22-01: D-260929-a70e, D-260929-15e1, D-260929-8591, V-261011-c460, D-260929-295d, D-260929-e353, V-261012-898b, D-261005-e5ae, D-261012-0509, D-261012-f9ac, V-261012-5819, D-261012-eb40, E-261012-a6a8, D-261012-5c86, D-260929-21c4, V-261004-61f2, V-261011-3c26; notes; session record]. Compared against DC-L19-56, DC-L19-153, DC-L19-167 and DC-L03-14.
- **Maps to:**
  - `references/making.md` section 5. Applied.
  - DC-L19-56: proposes adding "and in the person's own window" to its default. For L20. Not applied.
- **Impact now / as it grows:**
  - *Usual breakpoints only:* now, quick. As it grows, the person becomes the tester.
  - *The person's window, the gaps, no hover, a comparison:* now, a few more minutes a round. As it grows, the rounds are about design.

### DC-L22-06: Sections that hold the page while they step
- **Block path:** Patterns > Scroll > Held sections and what moves them on (`references/making.md` section 7)
- **Questions the designer answers:** May a section stay in place while its steps play? What moves it on: scrolling, a clock, or either? How much of the page's scroll may held sections take? What happens on a phone, and with reduced motion?
- **Options:**
  - **Not held; the steps change on a timer:** the phone form the owner asked for in place of the first held section, later given to tablets too [S-L22-01: D-260929-c28e, D-261005-e5ae].
  - **Held, moved on by scroll:** asked for by the owner twice, first for a product walk-through and later for a diagram [S-L22-01: D-260929-e412, D-261012-e73f].
  - **Moved on by a clock:** the owner's first choice for the diagram, kept as the other option when scroll was added [S-L22-01: D-261012-32db, D-261012-e73f]. On phones, steps play only while in view [S-L22-01: D-261005-34ef].
  - **The cost of holding.** Two held sections took 12,252 of the page's 20,158 px of scroll, 61%, each with a different control. Everything else on the page, including all its proof, shared the rest. With one of four drawings picked, the share was about 54% [S-L22-01: V-261012-1e2d; audit, finding 9]. The owner agreed to shorten both a little; one was put back to its earlier step length the same afternoon while a flicker report was being chased [S-L22-01: D-261012-f886, E-261012-10ad].
  - **Movement on a phone.** The owner first asked for animations, motion, scroll and hover effects to be removed on phones. Forty minutes later the owner said only the scroll effects had been meant, and the in-view motion came back [S-L22-01: D-260929-15e1, D-260929-8591]. A view that eased by a fixed share per frame looked irregular to the owner. Driven by elapsed time, its movement from frame to frame measured even; the owner had not yet confirmed it on a phone when this was written [S-L22-01: D-261012-0509, V-261012-f73b].
  - **Changing step.** Two layers fading at once let the page show through halfway. Fading only the arriving layer over the held one fixed it [S-L22-01: D-261012-5c86]. A finely patterned surface that moved by part of a pixel shimmered; it now moves by whole device pixels [S-L22-01: D-261012-eb40].
  - **Pace of a step.** A lead-in sped up by cutting its steps read as "fast-forwarded"; one continuous eased motion did not. Each step stays up long enough to be read [S-L22-01: D-261011-d92e, D-261011-3706].
- **Visual effect:** a held section makes one thing the center of the page for a while. Two of them make most of the page a walk-through.
- **Depends on (upstream):** how lively marketing pages may be (DC-L19-84), reduced motion, the phone layout.
- **Affects (downstream):** the page's length, where the proof sits, the control pattern, performance.
- **Token encoding:** durations and easings come from the motion tokens. The length of a scroll step is a layout value: record it as a decision.
- **Platform notes:** web: never size a held section with `100vh`. STD-mobile-touch-10 gives `svh` for marketing first screens and warns that `dvh` there shifts the layout while scrolling.
- **Accessibility constraints:** with reduced motion on, every step is shown without movement and nothing advances by itself. A clock pauses while the section is out of view and when the person takes over [inferred].
- **Default + heuristic:** DC-L19-84 stands: few moving parts on a site meant to convert, a scroll story only where the page exists to be experienced. This project is one case of a site meant to convert whose owner still wanted two held sections; the cost was measurable, and the owner agreed to shorten both a little once the share was shown. Heuristic: for each held section, report its share of the page's whole scroll, and use one control pattern for all of them [inferred].
- **Evidence:** [S-L22-01: D-260929-e412, D-260929-c28e, D-260929-15e1, D-260929-8591, D-261005-e5ae, D-261005-34ef, D-261011-d92e, D-261011-3706, D-261012-32db, D-261012-e73f, D-261012-5c86, D-261012-eb40, D-261012-f886, D-261012-0509, E-261012-10ad, V-261012-1e2d, V-261012-f73b; audit]. Compared against DC-L19-84.
- **Maps to:**
  - `references/making.md` section 7. Applied.
  - DC-L19-84: evidence on the cost of `scroll-story` on a site meant to convert. For L20.
- **Impact now / as it grows:**
  - *Not held:* now, plain. As it grows, nothing to maintain.
  - *Held sections:* now, a strong center. As it grows, each one lengthens the page and adds a control to keep the same.

### DC-L22-07: Figures drawn as graphics on a marketing page
- **Block path:** Imagery > Data graphics > Proof figures on marketing pages (`references/making.md` section 8)
- **Questions the designer answers:** Does a proof figure stand alone, or get a drawing? What may the drawing show? In whose visual language is it drawn? How do several of them move?
- **Options:**
  - **The figure alone, in a plain box:** this project's original form. When a dark restyle of it was shown, the owner asked for the original back; five hours later the owner chose the drawn version below [S-L22-01: D-261012-a482, D-261012-4ed1].
  - **An abstract line diagram beside the figure:** rejected as looking cheap [S-L22-01: notes]. It had been drawn from a screenshot of a reference instead of a visit to it [S-L22-01: E-261012-2cec, E-261012-3557].
  - **A small piece of the product, drawn in the product screens' own language:** accepted. The owner named the method: use what made the screens work [S-L22-01: D-261012-4ed1; notes].
  - **Only what the words state.** Each drawing shows the claim in the copy and nothing more: no invented axes, series or trends [S-L22-01: E-261012-2cec].
  - **A set on one grid.** Cards of different heights looked ragged until every column started and ended on the same lines [S-L22-01: E-261012-4df5].
  - **Movement.** The owner pointed out that four of the six drawings moved the same way, left to right, and that two looked alike [S-L22-01: session record]. Each now builds in the way that explains its own figure, on its own clock [S-L22-01: E-261012-4df5].
  - **Labels at reading size.** A scale the owner could not read was redrawn [S-L22-01: session record]. Of two earlier charts the owner said they should be detailed or they should be clear [S-L22-01: D-261005-808d].
  - **Color that carries meaning stays.** A restyle to brand colors only had removed the meaning from a risk display; meaning colors came back [S-L22-01: D-261005-808d].
  - **On a small screen:** two cards in a row while they stay readable, not one wide card per row [S-L22-01: D-261012-0509].
- **Visual effect:** a figure with a drawing in the product's language reads as proof from the product. A generic infographic beside real product views reads as decoration.
- **Depends on (upstream):** chart scope and anatomy (DC-L05-22, DC-L05-24), chart accessibility (DC-L05-25), the product views on the same page (DC-L22-04).
- **Affects (downstream):** the proof section's layout, motion, and the copy, because the drawing may not say more than the words.
- **Token encoding:** none new here. Charts made of counted marks (one dot or block for each unit) have no tokens yet [S-L22-01: F-261011-95d9].
- **Platform notes:** none.
- **Accessibility constraints:** the figure and its meaning are in text; the drawing is not the only carrier (DC-L05-25). Movement follows the reduced-motion setting.
- **Default + heuristic:** The figure alone is a sound start. Add a drawing only when it shows what the words state, in the product's own chart language when the page shows the product [inferred from one accepted and one rejected round]. Heuristic: if the drawing needs an axis the copy does not give, it is claiming something nobody checked.
- **Evidence:** [S-L22-01: D-261012-a482, D-261012-4ed1, D-261012-0509, D-261005-808d, E-261012-2cec, E-261012-3557, E-261012-4df5, F-261011-95d9; notes; session record]. Compared against DC-L05-22, DC-L05-24 and DC-L05-25.
- **Maps to:**
  - `references/making.md` section 8. Applied.
  - Chart tokens for counted marks: for the chart lane. Not applied.
- **Impact now / as it grows:**
  - *The figure alone:* now, honest and quiet. As it grows, nothing to keep in step with the copy.
  - *A drawing:* now, more to look at. As it grows, every change to a claim changes a drawing.

### DC-L22-08: How far a note reaches
- **Block path:** Builder > Feedback > Scope of a change (`references/making.md` section 2)
- **Questions the designer answers:** When you point at one thing, does the builder change only that, everything of the same kind, or everything that looks alike? May it change anything you did not mention? When should it ask before acting?
- **Options:**
  - **Too little.** The owner then has to say it again. A reader's digest counts about 30 decisions that are repeats of an earlier note. Icons for one family of cards took 13 decisions in 24 minutes: the first note was applied to every related link, and the owner then asked for icons on more groups of cards, one group at a time [S-L22-01: D-260929-0dc9; digest, pattern 5]. A bar had to be asked for again because the first change was so small that it still read as a hairline [S-L22-01: D-260929-a888]. One marker rule was broken four times across six screens before it was fixed in one sweep [S-L22-01: D-261011-1284].
  - **Everything that looks alike.** The opposite failure. A reader's digest counts 15 changes that went wider than the note or that nobody had asked for [S-L22-01: digest, pattern 4]. A stroke asked for on one kind of card was applied to every framed surface, and its leftovers took two more rounds to remove [S-L22-01: D-260929-6030, D-260929-b149, D-260929-8a66]. A sweep that added an icon to every row was cut back to the five rows that needed one [S-L22-01: D-261011-6d49]. A second button was changed when the request named one [S-L22-01: D-260930-90b0].
  - **The thing named and its true siblings, counted.** For a rule that had been broken four times, the builder wrote the rule in one line and a small script that listed every case before and after. The sweep overshot once, with too many icons, and was cut back [S-L22-01: D-261011-1284, V-261011-d623, D-261011-6d49]. A second rule got its script the first time it was stated [S-L22-01: D-261011-53e7, V-261011-f383]. Neither rule came up again in the day of record that remained.
  - **Changes nobody asked for:** a new button, a banner, a disclaimer line, a regraded photograph and a restyle of an approved page each cost a round [S-L22-01: D-260929-38f8, D-261011-aad2, D-260929-9124, D-261012-e35c, D-261012-9698].
  - **Asking, or acting.** Asking whether related pages should follow a change, and then holding one such page back, each drew a rebuke, 17 minutes apart [S-L22-01: D-261011-a5b7, D-261012-c30e]. A real fork, put with a recommendation and a visible alternative, was answered in 10 minutes; a numbered report was answered point by point in 37 [S-L22-01: D-261011-e685, D-261012-f886]. Questions and builder decisions that were only logged never closed: 7 questions stayed open for two weeks and 28 of the builder's decisions were still waiting at the end [S-L22-01: digest, pattern 6].
- **Visual effect:** none directly. A product where one rule holds everywhere, and nothing changed that the person did not expect.
- **Depends on (upstream):** the decision log (what is already decided), "Decide or ask" (`rules.md` section 6).
- **Affects (downstream):** every round of feedback, the debt list, the closing report.
- **Token encoding:** none. When a note is really a rule ("all bars are this thick"), record it as a decision or a project standard so later pages keep it.
- **Platform notes:** none.
- **Accessibility constraints:** a sweep never removes an accessibility floor (`guardrails.md` section 4).
- **Default + heuristic:** A note changes the thing named and every other instance of the same kind, and nothing of another kind [inferred: the digest counts about 30 decisions that repeat an earlier note, and 15 changes that went too wide]. Say in one line what you will apply it to. Where instances can be counted, count them before and after. Act on what follows from the request and report it; ask only for a real fork, with your pick and a visible alternative; put waiting decisions in one numbered list the person can answer in one message [inferred]. Lane L21 proposes "one example stands for a class" from a different project; this card adds the opposite failure and the count.
- **Evidence:** [S-L22-01: D-260929-0dc9, D-260929-a888, D-261011-1284, D-260929-6030, D-260929-b149, D-260929-8a66, D-261011-6d49, D-260930-90b0, V-261011-d623, D-261011-53e7, V-261011-f383, D-260929-38f8, D-261011-aad2, D-260929-9124, D-261012-e35c, D-261012-9698, D-261011-a5b7, D-261012-c30e, D-261011-e685, D-261012-f886; digest, patterns 4, 5 and 6]. Compared against `rules.md` section 6.
- **Maps to:**
  - `references/making.md` section 2. Applied.
  - `rules.md` section 6, "Decide or ask": evidence that its table also holds while building, with "what follows from the request" as a kind of mechanical decision. For L20.
- **Impact now / as it grows:**
  - *Only the thing pointed at:* now, safe. As it grows, the person repeats every note on every page.
  - *The same kind, counted:* now, one line to say what it covers. As it grows, rules hold on pages built later.

### DC-L22-09: The builder's recurring mistakes, and what a repeated note means
- **Block path:** Builder > Feedback > Learning from the person's replies (`references/making.md` section 10)
- **Questions the designer answers:** When you have to say something twice, what should the builder change: the thing, or the way it reads your notes? Which mistakes should it check itself for before it shows you anything? Where are your standing rules kept, so work built later keeps them?
- **Options:** the mistakes an AI builder made most often in this project, each with what the owner's reply showed.
  - **Doubling down on what was liked.** The owner liked one of six directions and asked for more iterations in its direction, and for more inventive ways to show it. The builder made nine variations of that one. The reply: the builder had been told one thing and doubled down on it without thinking; what was wanted was entirely new ideas [S-L22-01: D-261011-5bec, D-261011-b965].
  - **Reaching for what is at hand.** The "new ideas" that followed reused the same film and style, and every one was removed. Ten background options taken from existing files were all refused. One photograph was used again and again on a page, once mirrored [S-L22-01: D-261012-20ba, D-261012-2926, D-261012-60ce, D-261012-f5d4; notes].
  - **Too narrow, and too wide:** DC-L22-08.
  - **Taking a word to its extreme.** A stated preference for a light ground was applied to almost every section, and the page was called dull 78 minutes later; this is the same case as in DC-L22-01, seen from the builder's side [S-L22-01: D-260929-dec7, D-260929-be0f]. After two notes that pointed back at the existing site, the next draft was called a copy of it [S-L22-01: D-260929-be0f, D-260929-2bc5, D-260929-616e] [inferred link]. A request for sharp corners was built as fully square and corrected to a very small curve [S-L22-01: D-261011-ba1e]. A request for a faster lead-in was built by cutting steps, and read as fast-forwarded [S-L22-01: D-261011-2ee2, D-261011-d92e]. A request to make one screen's field obvious was answered with a banner that was removed [S-L22-01: D-261011-e685, D-261011-aad2].
  - **A timid fix.** A bar was thickened so little that it still read as a hairline; the owner's next note opened by saying it was a repeat [S-L22-01: D-260929-a888].
  - **Forgetting a standing rule on later work.** A rule against small labels above headings was broken on two later occasions, by pages and a section built afterwards [S-L22-01: D-260929-9658, D-260929-7ad9, D-260929-8d02, D-261012-93d3].
  - **A fix that did not hold.** A button that read as disabled was reported, fixed, and reported again 11 minutes later, this time with the words that the same should be done for all similar buttons [S-L22-01: D-260929-1754, D-260929-e2b9].
  - **Changing what was protected.** A stroke the owner had said not to change was changed by a page-wide pass 30 minutes later [S-L22-01: D-260929-3218, D-260929-93ee]. Two screens were rebuilt unasked. The owner's word to keep them as they were was then read as keeping the rebuilt ones, and the owner had to ask again for the originals [S-L22-01: E-261005-3914, D-261005-24fb, D-261005-d153].
  - **Growing with each pass.** Cards and type grew in each restyle [S-L22-01: E-261012-f5e4; notes]. A screen called unprofessional was rebuilt with more nested boxes and came back as cluttered [S-L22-01: D-261011-50fe, D-261011-9baf].
  - **Following a reference loosely after the method was named.** Six hours after the owner said to rebuild shipped work, the builder drew another section loosely "after" references instead of rebuilding them. The five standing versions were removed four hours later, with the instruction to use the library thoroughly [S-L22-01: D-261012-2926, E-261012-103d, D-261012-01ef].
  - **Arguing from analysis where the person judges by eye.** The builder swapped in a lighter accent on dark grounds on the strength of a contrast measurement; the owner asked for the brand's own accent back everywhere [S-L22-01: D-260929-25c7, D-260930-33c7]. This is a hard case, not a plain mistake: contrast floors stay locked (`guardrails.md` section 4), so the right move is to show both versions and say which one meets the floor, not to decide silently either way.
  - **Fixing a different fault, and calling it done.** A flicker fix was real, but was not the fault the owner meant [S-L22-01: D-261012-5c86, D-261012-eb40].
  - **Stating what was not checked.** A strip was reported as static from a test in a background tab [S-L22-01: V-261004-61f2]. The builder told the owner that a set of cards used the same typefaces as the product screens; the audit showed they did not, and said so [S-L22-01: audit, finding 1].
  - **What ended the repeats.** At the fourth repeat of one rule the owner asked why it had to be repeated and said to apply it everywhere it was relevant. The builder then wrote the rule in one line and a small script that counted every case before and after. The sweep overshot once and was cut back; after that the rule did not come up again in the day of record that remained [S-L22-01: D-261011-1284, V-261011-d623, D-261011-6d49].
- **Visual effect:** none directly. Fewer rounds are spent on the same note.
- **Depends on (upstream):** how far a note reaches (DC-L22-08), where decisions and project standards are recorded.
- **Affects (downstream):** every round of feedback, the list of standing rules, the checks run before a showing.
- **Token encoding:** none. A note that turns out to be a rule is recorded as a decision or a project standard (`engine.py standard add`).
- **Platform notes:** none.
- **Accessibility constraints:** none new.
- **Default + heuristic:** A repeated note is a signal about how the builder reads, not only about the thing. On a second mention: stop, re-read both messages, name what was misread (too narrow, too wide, too literal, or the wrong thing), say the rule back in one line, apply it to every instance, and record it so later work keeps it. On a third: write a check that finds every case [inferred from one rule where this was done]. "I like this one, show me more" asks for new ideas at the same level, not variations of it [S-L22-01: D-261011-b965]. Before showing work, check it against the list of mistakes in `making.md` section 10.
- **Evidence:** [S-L22-01: D-261011-5bec, D-261011-b965, D-261012-20ba, D-261012-2926, D-261012-60ce, D-261012-f5d4, D-260929-dec7, D-260929-be0f, D-260929-2bc5, D-260929-616e, D-261011-ba1e, D-261011-2ee2, D-261011-d92e, D-261011-aad2, D-261011-e685, D-260929-a888, D-260929-9658, D-260929-7ad9, D-260929-8d02, D-261012-93d3, D-260929-1754, D-260929-e2b9, D-260929-3218, D-260929-93ee, E-261005-3914, D-261005-24fb, D-261005-d153, E-261012-f5e4, D-261011-50fe, D-261011-9baf, E-261012-103d, D-261012-01ef, D-260929-25c7, D-260930-33c7, D-261012-5c86, D-261012-eb40, V-261004-61f2, D-261011-1284, V-261011-d623, D-261011-6d49; audit; notes]. Compared against `rules.md` section 7.
- **Maps to:**
  - `references/making.md` section 10. Applied.
  - `rules.md` section 7 (vague taste words): evidence that a taste word taken to its extreme is as wrong as one ignored. For L20.
- **Impact now / as it grows:**
  - *Patch each note:* now, quick. As it grows, the person says everything twice and stops trusting the builder.
  - *Treat the second mention as a rule:* now, one line to say back. As it grows, the list of standing rules does the remembering.

## Part B: Evidence on existing cards and standards

One project's evidence, added as a second source where a card or a standard already covers the lesson. "Supports" means the project ran into the cost the card or standard warns of. Nothing in this table changes a default.

| Card or standard | What it says | What this project adds | Reading |
|---|---|---|---|
| STD-process-review-taste-38 (three variants by default, five at most) | Never more than five | Rounds of 6, 9 and 8 options were built for one section. The owner cut them to one, four and two, and 28 directions in all left 3, none chosen [S-L22-01: D-261011-5bec, D-261011-b965, D-261012-6cb4; digest, numbers] | Supports the cap. See Part D2 for the one exception the owner asked for |
| STD-process-review-taste-37 (variants diverge on a named axis) | Each variant is a direction you could defend shipping | Nine near-copies of a liked option, and five ideas in the house style, were rejected in turn [S-L22-01: D-261011-b965, D-261012-20ba] | Supports |
| STD-process-review-taste-41 (keep exploration out of production) | An isolated route, never production code | The owner asked for it three times, unprompted, and praised review pages being left out of the sitemap [S-L22-01: D-260929-1fca, D-260930-2d81, D-261004-4127] | Supports |
| STD-process-review-taste-42 (one piece per prototype run) | Explore one piece at a time | By one afternoon a page carried eight rows of review options; a fold-away control had to be added and the owner cut them to five [S-L22-01: E-261012-f5e4, D-261012-4ed1; digest, numbers] | Supports. The standard has no form for judging sections together: Part D3 |
| STD-process-review-taste-43 (one at a time, full size) | Never side-by-side thumbnails | The builder itself reviewed a round on small full-page thumbnails and showed the owner broken buttons [S-L22-01: E-261012-6b76; notes] | Supports, and extends it to the builder's own check |
| STD-process-review-taste-47 (verify every variant before hand-off) | Flip through every one yourself | A color leak sat in two of three page options and was found by the owner [S-L22-01: E-261012-10ad; session record] | Supports |
| STD-process-review-taste-49 (promote the pick, then clean up) | Delete the prototype surface unless they ask to keep it | Pickers were left on the page twice; this owner also asked for rejected options to be kept [S-L22-01: D-260929-e075, D-260929-2286, D-261006-7c4d] | Supports. Ask once whether options are kept |
| STD-process-review-taste-29 and -33 (feel cannot be judged from code; real hardware) | Emulation never counts as verified | Ten of 109 recorded checks say the owner's browser or a real device was not checked; three of those ten were still recorded as confirmed [S-L22-01: digest, numbers] | Supports |
| DC-L19-143 (hover is an extra), with STD-accessibility-motion-15 (gate hover to fine pointers) | Hover can only add, never hold something people need (the card); hover styles sit behind a fine-pointer query (the standard) | A list that changed its picture on hover had no phone behavior until the owner said so [S-L22-01: D-261012-0509] | Supports |
| DC-L19-178 (research shipped products before drafting a flow) | Study shipped products first, for flows with domain rules | The same held for sections of a marketing page: eight review rounds were lost to invented options; references were fetched only after each rejection [S-L22-01: digest, pattern 2] | Supports, and widens it (DC-L22-01) |
| DC-L19-50 (variety between sections) | No two sections of one page share a layout (a warning, not a block); break the grid only in small ways | Variety without constants gave four design languages on one page [S-L22-01: V-261012-1e2d] | Qualifies: vary layout, hold materials (DC-L22-03, Part D4) |
| DC-L19-53 (how long pages separate their sections) | Space by default; a frame of lines only as a deliberate style | The owner asked for page-wide guide lines as an option, then for them to sit behind content and for more vertical space when they are on [S-L22-01: D-261012-93d3, E-261012-f5e4; session record] | Supports "a deliberate style", with two conditions |
| DC-L19-56 (how a layout is judged) | Full size, in a real frame, at a 1920 px desktop fold and a phone | The owner reviews in an 1800 px window and in a narrow desktop window of about 516 px, in a browser the builder was not testing in [S-L22-01: notes] | Qualifies: add the person's own window (DC-L22-05) |
| DC-L19-84 (how lively marketing pages may be) | Few moving parts on a site meant to convert | Two held sections took 61% of one page's scroll [S-L22-01: V-261012-1e2d] | Supports the default with a number (DC-L22-06) |
| DC-L19-131, DC-L19-72, DC-L19-73 (show the real product; how screenshots are framed) | Use the real product, cropped to what the text describes | Abstract diagrams and large simplified mock-ups were both rejected; a complete interface at real size, scaled, was accepted. It was built for the page with invented data, not captured from the product [S-L22-01: D-261005-7494, D-261011-2e86] | Supports the direction (the more real, the better received); the purpose-built view is a different form (DC-L22-04) |
| DC-L19-35 (sample content in previews) | Realistic copy built from the person's own product description | Demo content is positioning: five of six screens told one industry's story until the owner spread them across the industries the site names [S-L22-01: D-261011-3c17, D-261011-e685] | Supports, and adds "spread across the customers served". On a public page the companies and people named in a demo were invented, which that card does not cover |
| DC-L19-167 and DC-L19-153 (what checks cannot judge; which device counts) | Nothing that depends on feel is reported as verified | A flicker the owner saw could not be reproduced by the builder and was handed over as open [S-L22-01: E-261012-a6a8] | Supports |
| DC-L11-04 (audit method) | The inventory's main value is shared vocabulary | The cohesion audit opened by reading the owner's own section numbers back; the answers came by finding number [S-L22-01: D-261012-f886; audit] | Supports |
| DC-L01-18 (dark mode mapping) | How light values map to dark | Three light sections restyled dark with the page were withdrawn; icon discs inverted mechanically went back to their light-ground color [S-L22-01: D-261012-a482, D-261012-832c, D-260929-fefd] | One owner's picks: a section is designed for its ground |
| `rules.md` section 6 (decide or ask) | Mechanical decisions are made silently; taste is asked | 28 decisions the builders logged as "proposed" were never accepted or rejected in two weeks; forks put with a recommendation were answered in minutes [S-L22-01: digest, numbers and pattern 6] | Supports. A decision that is only logged is not asked (DC-L22-08) |
| `rules.md` section 7 (vague taste words) | Turn a taste word into precise visual keywords, and say how you read it | A request for sharp corners was built as absolutely square and corrected to a very small curve; a request to make one field obvious was answered with a banner that was removed [S-L22-01: D-261011-ba1e, D-261011-e685, D-261011-aad2] | Supports |
| `guardrails.md` section 5 (honesty) | Don't claim you checked something you did not run | "Verified" was written into the project's own instructions before the check existed; a builder's claim about its own work was wrong and corrected in the audit [S-L22-01: digest, pattern 13; audit] | Supports |

**Where this lane and lane L21 agree.** L21's playbook comes from a mobile app; this trail comes from a marketing site. Both found that a note on one example stands for a class, and that a builder whose inventions are rejected twice should follow a reference. L21 also separates what was written from what was verified, which this trail supports (ten recorded checks say the owner's browser was not checked). Two projects is still a small sample, but they are independent.

## Part C: What changed in OpenDesigner

| File | Change | Why |
|---|---|---|
| `skills/opendesigner/references/making.md` (new) | A guide in ten sections: before you build, one round, showing options, one page not several, checking as rendered, finished interface inside a page, held sections and movement, figures as graphics, debt, and the mistakes builders make with what a repeated note means | Nothing told an agent how to build and review pages once the system exists. It routes to STD-process-review-taste-37 to -49 and the cards above, and adds what this lane found |
| `skills/opendesigner/assets/output/COHESION-AUDIT.md` (new) | A template for the audit in DC-L22-03: sections, eight questions, findings, complaints and causes, directions, recommendation, questions, corrections | The audit was the one report the owner answered point by point |
| `skills/opendesigner/SKILL.md` | One row in "Files in this skill"; a short section, "Building pages with the system" | So the main skill knows the guide exists |
| `tools/build_data.py`, `chatgpt-project/knowledge/01-protocol.md` (generated) | The guide and the audit template are added to the ChatGPT bundle's protocol file | The bundle includes SKILL.md, which now points to both |
| `skills/opendesigner-extend/SKILL.md` | Two rows in "Classify the request" (a page built with the system; a page that does not hang together); one line in section 5 | The extend skill is where pages are built after the system exists |
| `docs/HOW-IT-WORKS.md` | A subsection under section 9, "Making and reviewing pages" | The readable process stopped at export |
| `tools/build_dist.py` | `references/making.md` added to the files bundled into the sub-skills' zips | The extend skill points to it, and on claude.ai each skill installs alone |
| `synthesis/cards.json`, `skills/opendesigner/references/cards/L22.json`, `data/cards/L22.json` (generated) | Nine cards indexed | So "why?" lookups from the guide resolve |

Not changed: `synthesis/standards.json`, `synthesis/QUESTIONNAIRE.md`, any default, `engine.py`, `rules.md`, `guardrails.md`.

## Part D: Proposed for the maintainer to decide

Each item gives both positions and a recommendation. None is applied.

### D1. Should the prototype standards be presented as rules for any built option, not only for motion?
- **Today:** STD-process-review-taste-37 to -49 sit in the theme "Process, review and taste", whose summary reads "How motion is built, reviewed, audited, prototyped...". Their text speaks of prototype variants of "one UI piece".
- **This project:** every one of them applied to pages and sections, and was rediscovered at cost because nothing pointed there (Part B).
- **Recommendation:** keep the rules as they are and widen the theme's summary and the standards index line to say they cover any built option. The new guide already routes there.
- **If accepted:** a wording change in `synthesis/standards.json` (a version bump, maintainers only).

### D2. More than five options, when the round is a set of rebuilt references?
- **Standard:** three by default, five at most, never more (STD-process-review-taste-38).
- **This project:** the owner asked for many references to be rebuilt, saw eight, had all eight restyled in the brand, and cut them to two about five hours later. The owner did not ask for fewer.
- **Recommendation:** keep five as the cap for options the builder designs. Allow a wider first round only when every option is a faithful rebuild of a named shipped example and the person asked for breadth, and cut to three or fewer before any option is refined.
- **If accepted:** an exception clause on STD-process-review-taste-38.

### D3. A picker with several switches, and a way to fold it away?
- **Standard:** one piece per prototype run (STD-process-review-taste-42), and the picker is fixed chrome with one row of variants (STD-process-review-taste-45, -46).
- **This project:** sections had to be judged together, so several questions were open at once; the controls covered the page until they could be folded away.
- **Recommendation:** extend the picker spec with an optional form: several named rows, one per question, each with its own URL key, and a fold control. Keep one row as the default and say that every added row multiplies the checks. Until this is decided, the guide keeps one question at a time as the rule and describes several switches only for the case where the person asks to judge sections together.
- **If accepted:** a change to the picker spec and to STD-process-review-taste-45 and -46.

### D4. A limit on what may vary between sections?
- **Card:** DC-L19-50 says no two sections of one page share a layout, as a warning, and limits how far a section may break the grid. It says nothing about type, corners, boxes or edges.
- **This project:** layout variety was welcome; variety in type, corners, boxes and edges was what the owner called a mismatch.
- **Recommendation:** adopt "vary layout, hold materials" as DC-L19-50's companion, and let `engine.py review` warn when a page uses more type families or corner values than the system defines. The thresholds need a second project.
- **If accepted:** a line on DC-L19-50 for L20, and a review check.

### D5. Should review measure the rendered page?
- **Today:** `engine.py review` reads code. Skill scripts are standard-library Python with no browser.
- **This project:** several faults were visible only as rendered: text at 8 to 10 px inside a scaled view, a color leak into embedded screens, a layout squeezed between breakpoints. The builder found the first and third itself; the owner found the second.
- **Recommendation:** keep the engine as it is. Treat rendered checks as the builder's own work with whatever browser tool the host has, as the guide now says, and add them to the check-by-hand list review prints.
- **If accepted:** two lines in review's closing list.

### D6. May a draft come before the interview?
- **Specification:** the process has three gates before foundations are built on (`docs/HOW-IT-WORKS.md`, "The process at a glance").
- **This project:** the owner asked for a built draft on day one and never used a gate. A sketch build existed in a sandbox, and the draft was never bound to it.
- **Recommendation:** say plainly that a draft may come before the deeper questions, never before the sketch-level token build, and that the draft reads its values from that build. The guide says so; the specification does not yet.
- **If accepted:** one paragraph in `docs/SPEC.md` section 3 and `zoom.md`.

## Open questions / gaps

- **One project, one owner.** Every count here comes from a single build with a single decider who judges by seeing. A person who prefers to approve plans may need none of DC-L22-01's draft-first safeguards.
- **The engine's outputs were not tested.** The one sketch build was never used by the draft, so this lane says nothing about whether tokens, DESIGN.md or `engine.py review` hold up on a real page.
- **No accessibility or performance pass ran** in the source project beyond one contrast calculation and one load-time fix, so the guide's checks in those areas rest on existing cards, not on this evidence.
- **The digest is one reader's count.** The 137 corrections, 35 acceptances and the pattern totals were counted by one reader from the ledger and were spot-checked, not recounted. The 260 subagent reports were not re-read.
- **Some of the owner's words are not in the ledger.** For at least six corrections the owner's words survive only in the builder's private notes; five corrections of the last day have a work record and no decision.
- **Still open in the source project:** the choice between the two cohesion directions, one flicker report that could not be reproduced, and the section the most rounds were spent on, which has no chosen direction after 28 built options.
- **Not covered:** native apps, design-canvas work, and teams with a designer in the loop.

## Confidence

- **High** that the events happened as described: every id cited was read in the ledger, and the audit's numbers were measured on the rendered page.
- **Medium** that the nine defaults carry to other marketing-site builds. Each is marked [inferred] or rests on an existing card or standard.
- **Low** that any count (61%, seven families, three options surviving) is a threshold. They are one project's measurements.

## Source key

| S-id | Source | Tier | Access |
|---|---|---|---|
| S-L22-01 | Decision trail of one B2B marketing-site build by several AI sessions under one owner's review: an append-only ledger of decisions, work, checks and findings; the generated views of it; the design record; a cohesion audit with its measurements; the builder's private notes (private, first-party project evidence, 2026) | Treated like C | Private. Cited by ledger id. Rows in `traces/L22-trace.md` |
