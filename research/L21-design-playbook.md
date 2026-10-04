# L21: Design playbook lessons (private, first-party project evidence)

## Lane overview

- **What this lane does.** It brings four groups of lessons from a private design playbook into OpenDesigner. The owner approved the groups from a gap report: keeping a decided design from being undone, states beyond the happy path, honest checks, and reading the owner's feedback together with safe round trips to a design canvas.
- **The source.** S-L21-01, "Design playbook: lessons from one mobile app built by many AI sessions under design rules (private, first-party project evidence, 2026)". It is not public and has no licence, so it cannot enter `learn/sources.json` (`learn/IMPROVING.md` section 4 asks for public pages only). It enters as this research lane instead. Every file opened is in `traces/L21-trace.md`.
- **How it is cited.** By chapter rule number (02.14 means chapter 02, rule 14 of its "rules in one screen"), template or case-study number, and the item ids the playbook attaches to each principle (for example gov-18). The playbook's own caveats apply: no person read its chapters line by line, and numbers inside its reasons were not re-derived from the original records [S-L21-01: README].
- **Authority.** Reference material, treated like Tier C (`_coordination/SCHEMA.md`). It shapes options, evidence and agent behaviour. It never sets a default value by itself (`docs/KNOWLEDGE.md` sections 1 and 2). Every number below is one project's evidence: a starting point to test, not a rule.
- **What changed in OpenDesigner.** Agent instructions, output templates and `engine.py review` checks (Part C). No house standard, no `synthesis/standards.json` entry and no default token value changed. Where the playbook disagrees with OpenDesigner, Part D sets out both positions for the owner to decide; none of them is applied.
- **New cards versus evidence.** Where a pending card already covers a lesson (DC-L19-125, -165, -167, -176), the playbook is added as evidence there (Part B), so lane L20 sees a second source. Four lessons had no card, so they get one each (Part A).

## Part A: Decision Cards

### DC-L21-01: Keeping a decided design system from being undone
- **Block path:** Governance > AI guardrails > Protecting decided design across sessions (Stage 25; `engine.py review`, `assets/output/AGENTS-snippet.md`, DESIGN.md "Removed on Purpose")
- **Questions the designer answers:** When several AI sessions or people change the product, what stops one of them from undoing a decision by accident? Where is something removed on purpose remembered? What has to pass before a merge or pull request?
- **Options:**
  - **Prose only:** decisions written in DESIGN.md and decisions.md, plus a short agent note. In the source project, rules that lived only in documents were broken again by the next session that had not read them, and a removed control survived for hours after its removal [S-L21-01: 02.15, assistant-2-07, summaries-2-11].
  - **One instruction file that every session reads first,** with a table that routes each area to the document that decides it, a never-list, the merge rules and the command to run before a pull request. Each never-list entry names a verb and a concrete object and says "as part of other work", so a change the owner asks for is not blocked [S-L21-01: 02.2, 02.4, gov-01, gov-03, gov-05]. The source file was about 60 lines in six sections; that length is one project's observation, not a tested rule [S-L21-01: gov-01].
  - **A registry of removed things:** what was removed, what replaced it, why (the owner's words or "not recorded"), when, and how a return is noticed. A row is added the same day, because removals leave no trace in code and a well-meaning session re-adds them first [S-L21-01: 02.4, gov-06, seed-15; template 18 section 5].
  - **A guard that runs anywhere:** one fast check per way the design was or could be undone: the files that carry the system exist, decision documents keep their rules, decided values hold, removed or banned patterns stay absent. It prints one fixed success line, lists every problem in one run and names the likely fix. An exception is allowed only on its own line, with a marker and a reason [S-L21-01: 02.14, 02.16, 02.18, tooling-01, tooling-03, gov-11, gov-18; template 02].
  - **Plan for the three accidental reverts:** a stale branch merged over the design, a merge conflict resolved toward the older side, and a well-meant tidy-up. A check for one does not cover the others [S-L21-01: 02.3, gov-09]. For conflicts: keep the design side and re-apply the other change on top [S-L21-01: 02.20, gov-23].
  - **Reach every branch:** the lock protects only the branches that hold it. In the source project, a build from a branch without the design work showed none of it [S-L21-01: case study 02].
  - **Code-owner review** of design files on the repository host [S-L21-01: seed-13]. That is a host setting outside OpenDesigner; it is mentioned, not built.
- **Visual effect:** none directly. Decided screens keep their look as more sessions and people work on them [inferred].
- **Depends on (upstream):** strictness (Q-gov-01), contribution model (Q-gov-03), how exceptions are recorded (DC-L19-165), decision records (DC-L11-12).
- **Affects (downstream):** the agent note (`AGENTS-snippet.md`), DESIGN.md ("Removed on Purpose", "For Agents"), `engine.py review` (guard checks and a closing line), the new `engine.py removed` command and the `removed` list in state.json, and the extend skill's start-up, removal and merge rules.
- **Token encoding:** none. State: `removed[] {id, what, instead, why, date, pattern, status, decision}`. Each removal is also an append-only decisions.md entry `removed.R-nn = "<what>"`, recorded as locked [inferred design for OpenDesigner].
- **Platform notes:** the checks are text searches, so they run where no compiler does [S-L21-01: tooling-01]. OpenDesigner's review already reads CSS, JSX, Tailwind, Swift and Compose, so a removal pattern can target any of them.
- **Accessibility constraints:** the accessibility floors stay locked whatever the registry says. A removal never takes away a focus ring, a label or a reduced-motion path [inferred].
- **Default + heuristic:** Default, applied in this lane with the owner's approval: the agent note routes each area to its file, states the order in which sources win, holds a never-list and the merge rule, and asks for `engine.py review --strict` before a pull request. DESIGN.md lists what was removed. Review checks that the system's files exist, that the tokens on disk are what state.json generates, that every locked decision in state.json still matches the append-only decisions.md (which survives a merge that took the older side of state.json), that removed patterns stay absent, and that every `od-ignore` carries a reason; it ends with one fixed line, `Review: ok` or `Review: N to fix`. Heuristic: turn every regression the owner catches into a check the same day [S-L21-01: 02.15]. What a text search cannot see becomes a check by hand on each screen [S-L21-01: template 18 section 5.2].
- **Evidence:** [S-L21-01: 02.2, 02.3, 02.4, 02.14, 02.15, 02.16, 02.18, 02.20, gov-01, gov-03, gov-05, gov-06, gov-09, gov-11, gov-18, gov-23, seed-13, seed-15, tooling-01, tooling-03, assistant-2-07, summaries-2-11; templates 01, 02, 18; case study 02]. Compared against DC-L11-12, DC-L11-15, DC-L11-24 and DC-L19-165.
- **Maps to:**
  - `engine.py review` (no Q-id): guard checks (required files, tokens in step, locked decisions, removed patterns), reasoned and bare `od-ignore`, one closing line. Applied in this lane.
  - `engine.py removed add|list|restore` (no Q-id) and DESIGN.md "Removed on Purpose". Applied.
  - `assets/output/AGENTS-snippet.md` and the extend skill sections 1, 2, 3 and 5. Applied.
  - Q-gov-01 and Q-gov-03: a heuristic for lane L20 to consider: "a removal is recorded the day it happens, with what replaced it", and "a strict project runs `engine.py review --strict` before every merge" [inferred].
- **Impact now / as it grows:**
  - *Prose only:* now, nothing to set up. As it grows, every new session is a new chance to undo a decision.
  - *Agent note with routing and a never-list:* now, one longer note. As it grows, a fresh session knows where each answer lives before it edits.
  - *Removed registry:* now, one command per removal. As it grows, the record of what was taken out and why, which code alone never keeps.
  - *Guard checks in review:* now, a few more lines of output. As it grows, a stale branch or an older-side merge shows up before it ships.

### DC-L21-02: What the builder may call checked: written, built, verified
- **Block path:** Builder > Guidance > Reporting what was checked (every skill's closing report; `guardrails.md` section 5; the extend skill's change note)
- **Questions the designer answers:** When the AI says a change is done, what has actually run? What should a report say first? What is left for a person to check by hand, and on what?
- **Options:**
  - **"Done":** a bare status word. In the source project "done" hid that nothing had run; many commits landed before any compiler saw them [S-L21-01: 13.2, CORE-PRINCIPLES mistake 6]. The count is one project's.
  - **Three separate states:** written (the file changed), built (it compiled or ran), verified (a build, a test run, a screenshot pass or a device check). Never write "builds", "works", "tests pass" or "done" for what did not run; write "not verified" [S-L21-01: 13.2, 13.4].
  - **What was checked, first:** open every report with what was and was not verified, piece by piece, and close with the riskiest unverified items and the command that checks each [S-L21-01: 13.3, 15.7].
  - **A fixed report order:** result and checks; what changed for the person; what is not verified; decisions for the owner; numbered checks on a real device; commands; skipped items with reasons [S-L21-01: 15.10]. A Deviation line whenever the work departs from a brief or a design document [S-L21-01: 15.17]; every skip with its reason [S-L21-01: 15.18].
  - **A check-by-hand list, ordered by risk:** each step names the screen, one action, the expected result and what must not happen; anything nobody has seen running is marked "not seen yet" [S-L21-01: 13.15; template 13 rules R3, R4, R9, R14].
  - **Unrun sweeps are guesses:** a bug sweep that could not run is a set of hypotheses; fix only what is certain [S-L21-01: 13.20; case study 16].
- **Visual effect:** none directly. People trust a report that says what it did not check, and the first real run becomes a short list instead of a surprise [S-L21-01: case study 16] [inferred for "trust"].
- **Depends on (upstream):** which checks exist (`engine.py validate`, `review`), the hand checks DC-L19-167 names, the review report format (DC-L19-176).
- **Affects (downstream):** the closing summary in every skill, the extend skill's change note, the AGENTS note ("report written, built and verified separately").
- **Token encoding:** none (process decision).
- **Platform notes:** the playbook's toolchain advice (parse checks, fetching a compiler into scratch space) is left out: OpenDesigner's own checks run on standard-library Python everywhere. What carries over is the wording rule and the order.
- **Accessibility constraints:** the check-by-hand list includes the reduced-motion toggle, the largest text size and a screen reader whenever the change touches them (Q-gov-07, STD-process-review-taste-19).
- **Default + heuristic:** Default, applied in this lane: written, built and verified are reported separately; a report follows the fixed order in `guardrails.md` section 5; work that moves, answers a touch or can only be judged on a real screen ends with a numbered check-by-hand list, riskiest first. Heuristic: if a claim cannot point to something that ran in this session, it says "not verified" [S-L21-01: 13.2] [inferred wording].
- **Evidence:** [S-L21-01: 13.2, 13.3, 13.4, 13.15, 13.20, 15.7, 15.10, 15.17, 15.18; template 13; case study 16; CORE-PRINCIPLES mistake 6]. Compared against DC-L19-167 and DC-L19-176.
- **Maps to:**
  - `guardrails.md` section 5, the main skill's Finish step 3, the extend skill's change note (section 6). Applied.
  - `engine.py review` (no Q-id): its closing line gives reports one exact line to quote. Applied (DC-L21-01).
  - Q-gov-07: supports DC-L19-167's proposed `feel-checks` option; adds "ordered by risk, with what must not happen" as its heuristic, for L20 [S-L21-01: 13.15].
- **Impact now / as it grows:**
  - *"Done":* now, the shortest report. As it grows, unrun work piles up unseen.
  - *Three states and a fixed order:* now, a few more lines per report. As it grows, every report reads the same way, so gaps stand out.
  - *Check-by-hand list:* now, a few minutes of a person's time. As it grows, the only route for motion, gestures and real screens.

### DC-L21-03: Reading the owner's feedback on built screens, and keeping open questions alive
- **Block path:** Builder > Guidance > Feedback on what was built (`rules.md` section 7; the extend skill's request table; decisions.md "Open items")
- **Questions the designer answers:** When the person says a built screen "looks dull" or marks a screenshot, how does the AI turn that into a scoped change? How does it avoid fixing only the one screen they named? Where do unanswered questions live between sessions? How are the AI's own judgment calls recorded?
- **Options:**
  - **Literal reading:** change exactly the words of the comment on the screen named. In the source project, comments named a symptom or one example, not the fix; literal fixes were sent back [S-L21-01: 01.8, seed-03; case study 10].
  - **Split, read for intent, answer every part:** split each message into decision, reason, bug and numbered asks, and answer by number; state your reading of an odd term first [S-L21-01: 01.6, summaries-2-03, summaries-2-01].
  - **One example is a class:** fix it, build one shared mechanism, sweep the product with a look-for list and a leave-alone list [S-L21-01: 01.23, motion-pers-31].
  - **A worksheet per message:** the quote, the literal ask, the intent, what is already decided, the smallest change, what not to change, how to verify, what to ask, the outcome [S-L21-01: template 16 section 1]. Reading patterns: an adjective about the look usually points at a gap next to something the owner likes; "at most" is a ceiling, not a target; a whole-product taste word needs a written test before any change [S-L21-01: template 16 section 2].
  - **Stop rule:** after two rejected attempts on one intent, add no new device; undo what the attempts added that the reference lacks, then copy the reference's mechanism [S-L21-01: template 16 section 3; case study 10].
  - **Still open:** a reply that mixes approval with a condition, or a question that was brushed aside, stays open [S-L21-01: 01.7, seed-10].
  - **One numbered list of open questions that survives sessions,** each with a default and whether it blocks, repeated until answered and never deleted without an answer [S-L21-01: 01.16, assistant-2-06, gov-76].
  - **A judgment ledger:** when the owner delegates, record each call, its alternative and how to undo it [S-L21-01: 01.13, 01.17, owner-messages-04, ux-adoption-86].
- **Visual effect:** none directly. Fewer reworks: the change matches what the person meant, and the same complaint does not return on the next screen [inferred].
- **Depends on (upstream):** the decide-or-ask rules (`rules.md` section 6), the decision log, "Removed on Purpose" (DC-L21-01).
- **Affects (downstream):** `rules.md` section 7, the extend skill's request table and start-up, the decisions.md "Open items" template, the extend change note.
- **Token encoding:** none (process decision). The open-questions list lives in decisions.md "Open items" entries as `Q<n> · question · recommend · default · blocks` [inferred format].
- **Platform notes:** the same everywhere.
- **Accessibility constraints:** a vague request never lowers a floor; "make it lighter" that would break contrast is answered with the nearest option that passes [inferred].
- **Default + heuristic:** Default, applied in this lane: `rules.md` section 7 gives the eight-step method for feedback on built screens, the open-questions list in decisions.md, and `--why` text that says what was chosen over what and how to undo it. Heuristic: if the comment names one screen, ask where else the same pattern lives before you fix it [S-L21-01: 01.23].
- **Evidence:** [S-L21-01: 01.6, 01.7, 01.8, 01.13, 01.16, 01.17, 01.23, seed-03, seed-10, summaries-2-01, summaries-2-03, motion-pers-31, assistant-2-06, gov-76, owner-messages-04, ux-adoption-86; template 16; case study 10]. Compared against `rules.md` section 7 as it stood (vague taste words become 3 to 5 visual keywords) and `learn/wiki/synthesis/decide-or-ask.md`.
- **Maps to:**
  - `rules.md` section 7 ("When you decide for the person", "Open questions last across sessions", "Feedback on what was built"). Applied.
  - The extend skill (a feedback row in section 2, open questions at start-up, an "Open questions" line in the change note) and `assets/output/decisions.md`. Applied.
  - Q-pref-01 (planned): the `coach` mode could use the same split-and-answer format [inferred]; for L20.
- **Impact now / as it grows:**
  - *Literal:* now, quick. As it grows, the same complaint comes back screen by screen.
  - *Intent and class:* now, a short plan before each change. As it grows, one fix covers every screen with the pattern.
  - *Open-questions list:* now, a few lines per session. As it grows, nothing the person was asked is lost between sessions.

### DC-L21-04: Writing to a design canvas without losing anyone's work
- **Block path:** Delivery > Output > Round trips to Figma and Paper (Stage 26; `opendesigner-export`)
- **Questions the designer answers:** When the AI writes to a shared design file, what stops it from overwriting a designer's edits? How do we know a change to one shared piece did not alter other frames? How are comments answered?
- **Options:**
  - **Write from memory:** regenerate the file from the AI's last copy. The playbook's publish protocol exists because the live canvas changes faster than any copy [S-L21-01: 14.1, gov-44; case study 06].
  - **Read just before every write, merge into what you read, publish only the changed boards, to the same place** [S-L21-01: 14.2, summaries-2-78, gov-45]. In the source project the host refused a publish until the session had read the latest version [S-L21-01: template 15 part 6].
  - **Never overwrite a board someone is editing:** publish yours beside it, tell them, redraw after they save [S-L21-01: 14.4, assistant-1-76, seed-105].
  - **Prove untouched boards unchanged:** render before and after, write the list of boards expected to change first, and report how many changed as expected and how many did not [S-L21-01: 14.3; template 15 part 7].
  - **Close each comment in its own thread:** change, reply in the thread, resolve after the change is pushed, one line in chat [S-L21-01: 14.7, summaries-2-79].
  - **Tie each copy to a named version** of the board, with the export date [S-L21-01: case study 06; 14.25].
- **Visual effect:** none in the product. Designers keep their edits, and every frame that changed was meant to [inferred].
- **Depends on (upstream):** where the master copy lives (Q-tool-01), what the Figma copy contains (DC-L19-173), the identity firewall for references (DC-L17-03).
- **Affects (downstream):** the export skill's Figma and Paper flows, the export summary, `guardrails.md` section 6.
- **Token encoding:** none (process decision).
- **Platform notes:** Figma's desktop MCP reads only; writes go through the remote MCP's `use_figma`. Paper's MCP runs inside Paper Desktop. A byte-for-byte image comparison needs saved screenshots; when only a visual comparison is possible, the report says so [inferred].
- **Accessibility constraints:** a proposal frame placed beside the designer's keeps the system's contrast and focus floors [inferred].
- **Default + heuristic:** Default, applied in this lane: the export skill's "Before every write" steps: read just before writing, turn edits and comments into decisions first, write only what changed, never overwrite a frame being edited (put a proposal beside it), compare untouched frames before and after, answer each comment in its thread, record the write with the file's version. Heuristic: if you did not read a frame in this session, you may not write to it [S-L21-01: 14.2].
- **Evidence:** [S-L21-01: 14.1, 14.2, 14.3, 14.4, 14.7, 14.25, gov-44, gov-45, summaries-2-78, summaries-2-79, assistant-1-76, seed-105; template 15 parts 6 and 7; case study 06]. Compared against DC-L19-173 and the export skill's existing round-trip steps.
- **Maps to:**
  - `opendesigner-export/SKILL.md`, "Before every write to Figma or Paper", and `guardrails.md` section 6. Applied.
  - Q-dist-01 (planned) `design-push`: add "read before every write; proposals beside edited frames" as its heuristic, for L20 [inferred].
- **Impact now / as it grows:**
  - *Write from memory:* now, fastest. As it grows, a designer's edits vanish and trust in the file goes with them.
  - *Read, write only what changed, compare:* now, a few extra reads and screenshots per write. As it grows, the file can be shared by people and agents at once.

## Part B: Evidence on existing cards

| Card | What the playbook adds | Status after this lane |
|---|---|---|
| DC-L19-165 (exceptions need a reason) | A second source. An exception lives only on its own line, as one fixed marker plus a reason; a marker without a reason fails the check; the markers are counted, and a growing count means the rule needs a conversation with the owner [S-L21-01: 02.16, gov-18, tooling-06; template 02 section 4.4]. | The engine part is applied: `od-ignore: <why>` lines are listed as kept on purpose, a bare `od-ignore` counts as a finding (it fails `--strict`), and a reason that repeats three times prompts a question to the owner. Not applied: the card's line that "a reason never waives a house standard". Review still skips an `od-ignore` line for standards too, as before, but now lists it with its reason (STD-process-review-taste-22 asks that a documented tradeoff be noted, not re-reported). See open question 2. The Q-gov-03 heuristic stays pending for L20. |
| DC-L11-24 (AI guardrails) | Evidence that enforcement has to run where the agents work: a text-only check that needs no compiler, run before every install and pull request, with the exact success line quoted in reports [S-L21-01: 02.14, tooling-01, tooling-03]. | Applied inside `engine.py review` (guard checks and the closing line) rather than as a separate script, so OpenDesigner keeps one command. |
| DC-L11-15 (deprecation) | The design-side twin of token deprecation: a removed control, label or treatment needs a record with its replacement and reason, because nothing in code marks its absence [S-L21-01: 02.4, gov-06]. | Applied as the removed registry. Token deprecation itself is unchanged. |
| DC-L19-125 (which states every screen ships with) | A second source, and a wider state set for screens that show data. See "Extending DC-L19-125" below. | The state catalogue template is applied (`assets/output/STATES.md`, kept in a project as `opendesigner/STATES.md`), with skill wording in the main and extend skills. The card's lint warning and its component-sheet state switcher stay pending for L20; the extension below widens what the switcher should show. |
| DC-L19-167 (what the builder's checks cannot judge) | A second source for "never call a device-only result verified" and for a closing list of hand checks: numbered, ordered by risk, each with the expected result and what must not happen, "not seen yet" on anything nobody watched run [S-L21-01: 13.15; template 13 rules R3, R4, R9, R14]. A sweep you could not run is a set of guesses [S-L21-01: 13.20; case study 16]. | Applied as agent wording (`guardrails.md` section 5, the extend change note). The card's engine part, a closing "check by hand" list printed by `engine.py review` from what changed, stays pending for L20. |
| DC-L19-173 (what the Figma copy contains) | Adjacent, not the same question: DC-L19-173 is about what the copy holds, the playbook about writing to it safely. The write-safety lessons became DC-L21-04 [S-L21-01: 14.2, 14.3, 14.4]. One overlap: build boards from one shared mock-up whose new inputs default to the old look, so a change to a shared piece cannot silently alter other boards [S-L21-01: 14.12, canvas-04]. | Unchanged; L20 may cite DC-L21-04 when it adopts the card's `design-push` heuristic. |
| DC-L19-176 (how a review is reported) | One fixed success line, every problem listed in one run, and a failure message that names the fix [S-L21-01: 02.14, tooling-03]. | The closing verdict line is applied (`Review: ok` / `Review: N to fix`). The Before/After/Why table the card proposes is not done; it stays pending for L20. |

### Extending DC-L19-125: states beyond empty, loading, success and error

DC-L19-125 covers four states for every screen and flow. The playbook adds evidence that screens which show a value need many more, and a way to keep them consistent:
- **Write a state matrix before designing a screen that shows a value:** one row per state, with its words, its tone, where the tone shows, what is hidden, the next step and its test [S-L21-01: 06.1, owner-messages-45, seed-47; template 07 parts 3 and 4]. In the source project, fixing states one screen at a time left contradictions between screens; one matrix settled them, with 17 rows of "was / now" changes [S-L21-01: CORE-PRINCIPLES mistake 5; case study 08]. The count is one project's.
- **List the classes to sweep,** not only the happy path: nothing there yet, not set up, progress against a number (under, near, exactly at, over, projected over), time edges, loading and stale, failure and gates, hidden or left out, and data extremes [S-L21-01: template 07 section 4.1]. "Exactly at" is its own row, separate from below and above [S-L21-01: 06.14; template 07 rule S6].
- **One catalogue, one function per screen:** keep one written catalogue of states, and for each screen one function that picks the state and returns everything the screen says for it; the screen holds no state text of its own; test every state by its id and test that two screens give one state the same words [S-L21-01: 06.7, copy-states-ux-28, git-5-07, git-6-24, tests-lock-44].
- **Words carry the state;** color agrees and never speaks alone [S-L21-01: 06.4, copy-states-ux-30]. This matches OpenDesigner's floor ("never carry meaning by color alone", `guardrails.md` section 4). The playbook goes further, putting the tone only in a small mark and keeping text in the normal text color [S-L21-01: 06.4, gov-15]. That stronger form is one project's choice, so the template offers it as an option to confirm, not a default.
- **When one state is flagged, design them all:** list every state of that feature before fixing the one named [S-L21-01: 06.2, canvas-45]. A state nobody designed falls back to the calmest state that is true [S-L21-01: copy-states-ux-29].

Proposed for L20, extending the card's "Maps to" (not applied here):
- **Stage 23 "Show" state switcher:** besides ideal, empty, loading, success and error, offer the data states that need their own look: near the limit, exactly at, over, stale, failed with a next step, and hidden values. Draw them through the same tokens as the real component, in light and dark [S-L21-01: gov-66, summaries-2-100] [inferred mapping to the component sheet].
- **Q-dist-03 `lint-rules`:** the card's proposed warning stays; add "a threshold with no row exactly at it" as a manual review item, since code cannot see it [inferred].
- **New heuristic for Q-pattern-04 and the stage 23 patterns:** "for any screen that shows a value, write its states in `opendesigner/STATES.md` first" [S-L21-01: 06.1].

## Part C: What changed in OpenDesigner

| Change | Files | Backed by |
|---|---|---|
| Review guard checks: required files, tokens in step with state.json, locked decisions against decisions.md, removed patterns, reasoned and bare `od-ignore`, one closing line | `skills/opendesigner/scripts/engine.py` (`review_guard`, `ignore_reason`, `cmd_review`), tests in `test_engine.py` (`KeepDecidedSystem`) | DC-L21-01, DC-L19-165, DC-L19-176 |
| The removed-on-purpose registry: `engine.py removed add|list|restore`, a "Removed on Purpose" section in DESIGN.md and a line in "For Agents" | `engine.py` (`cmd_removed`, `render_design_md`), `assets/output/DESIGN.md`, `assets/output/state.json` | DC-L21-01 |
| Agent note: routing table, source order, never-list, merge rule, review before a pull request, stop and ask | `skills/opendesigner/assets/output/AGENTS-snippet.md` | DC-L21-01 |
| Skill wording: record removals, keep the note on the branch new work starts from, offer review in CI after a yes; extend start-up reads guard lines, removal row, merge rule, reasoned exceptions, review before a pull request | `skills/opendesigner/SKILL.md`, `skills/opendesigner-extend/SKILL.md` | DC-L21-01, DC-L19-165 |
| The state catalogue: a template with ten rules, a thresholds table, the state matrix with eight classes, boundary rows, modes, settled contradictions, open questions and how to build and test from it; skill wording to write states before building a screen that shows data | `skills/opendesigner/assets/output/STATES.md`, `skills/opendesigner/SKILL.md` ("DESIGN.md stays alive"), `skills/opendesigner-extend/SKILL.md` section 2 | DC-L19-125 (extended) |
| Honest reports: written, built and verified kept apart; a fixed report order; a check-by-hand list ordered by risk; unrun sweeps named as guesses | `skills/opendesigner/references/guardrails.md` section 5, `skills/opendesigner/SKILL.md` (Finish step 3), `skills/opendesigner-extend/SKILL.md` section 6 | DC-L21-02, DC-L19-167 |
| Feedback on built screens: an eight-step method, judgment calls written with how to undo them, one numbered open-questions list that every session carries forward | `skills/opendesigner/references/rules.md` section 7, `skills/opendesigner/assets/output/decisions.md`, `skills/opendesigner-extend/SKILL.md` sections 1, 2 and 6 | DC-L21-03 |
| Safe canvas round trips: read just before every write, edits and comments first, write only what changed, proposals beside frames being edited, compare untouched frames, answer each comment in its thread, record the version | `skills/opendesigner-export/SKILL.md` ("Before every write to Figma or Paper"), `skills/opendesigner/references/guardrails.md` section 6 | DC-L21-04 |
