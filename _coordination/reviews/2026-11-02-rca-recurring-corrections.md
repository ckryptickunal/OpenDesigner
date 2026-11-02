# RCA: why the same corrections keep coming back

Date: 2026-11-02. Inputs: the maritime B2B landing page notes (`learn/local-learnings/2026-11-03-b2b-landing-maritime.md`, 47 lessons over 9 rounds, still uncommitted on the maintainer's Mac), the 14 rows of `_coordination/OWNER-FEEDBACK.md` "2026-11-03: a private B2B landing page" (also uncommitted), earlier owner rows on type, and `skills/opendesigner/references/making.md` as it stood on main (f528ea6).

## 1. What keeps recurring

| Pattern | How many times | Examples |
|---|---|---|
| Building before showing shipped samples | asked 3 times in one project, plus lesson 27 | "Why are you not using Mobbin to benchmark other websites ... and then build?" |
| Copying a reference instead of learning from it | 2 rounds, plus earlier showcase and Helsing rounds | Edge ruler ticks from one reference; a whole page cloned from the parent site |
| Values drifting outside a design system | 5 drafts in a row | "Nothing looks aligned", "you have not made a design system" |
| Cutting substance when asked for brevity | 2 | "Less text" removed the facts that built trust |
| Changing what the owner had settled | 1, called out sharply | A type dial nobody asked for |
| Taste read from thumbnails or a still | 2 | Variants from Mobbin thumbnails; screenshots of a background tab |
| Type spacing faults (kerning, tracking) | across the site, videos and pages | Letters touching at -0.045em; kerning lost in a split-letter headline; "iOS kerning everywhere" |

## 2. Root causes

**RC1. The rules existed, but as advice, not as steps that block.** "Look at shipped work before you invent", "build the first draft on the tokens" and "list the places before you edit" were all already in `making.md`. Lesson 27 says so in its own words: "`making.md` section 1 already asks for this, but it wasn't done." A builder under pressure to show something skips any step that nothing checks. *Why it recurs:* nothing in the flow fails when the step is skipped, and the cost of skipping shows up only in the owner's next message.

**RC2. The guidance contradicted itself about references.** One line said "take structure and quality, never identity". Others said "rebuild its structure closely" (section 10) and "rebuild each screen from one strong reference ... follow its structure closely" (section 12). In the same project the owner asked to rebuild on the parent company's system, and the agent read "system" as "pages". Each reading was defensible from the text, so the agent picked the one that was easiest to build. *Why it recurs:* the exception (a named section, "our version of this") was not separated from the rule (a reference named for direction gives principles only).

**RC3. Short instructions were read literally.** "Less text" became fewer facts; "rounded" became 32 px; "inherit their system" became copy their layout; black-and-white for card backgrounds also went on the hero. `making.md` already had "taking a word to its extreme", but nothing tied a short instruction to a list the agent could check against (what must stay, which instances it covers).

**RC4. Judgement made from the wrong evidence.** Taste was read from Mobbin thumbnails, which carry layout but not motion, scale or depth. A screenshot of a background tab caught reveals halfway. Figures were judged by screenshot at two widths, so a label collision at 320 px slipped through. *Why it recurs:* a picture is the quickest evidence, and the guidance did not say which questions need a live measurement instead.

**RC5. Lessons sit in a queue that nothing drains.** The project notes and 14 owner rows were written down well, but locally and with status "open". The two strictest owner rules (no moving calls to action, known meaning colours) cannot become house standards, because `synthesis/standards.json` accepts only the listed outside sources and has no owner source. So each new session starts without them unless it happens to read that project's files.

**RC6. Rule-shaped faults had no automatic check.** Kerning and tracking faults are mechanical (px tracking, kerning switched off, capitals at 0, letters split into spans) but the only check was "tighter than -0.03em". Separately, `engine.py review` flagged OpenDesigner's own `tokens.css` when it was copied into an app. A check that cries wolf on its own output trains agents to add `od-ignore` and stop reading it.

## 3. What this change fixes

| Root cause | Fix in this change |
|---|---|
| RC1 | `making.md` section 1 now starts with ordered steps in the owner's words: samples board first, pick, then build; measure the reference live; content core before the first draft; motion plan for pages that persuade. Section 5 adds measuring figures with a script at every width, and waiting for reveals before judging a screenshot |
| RC2 | Section 1 says a reference gives principles, never its page, and that inheriting a parent system means its materials, not its compositions. The section 10 row and the section 12 rule now say when one reference may be followed closely (a named section the person asked for, or a screen pattern inside a product) and when it may not (a landing page or brand direction) |
| RC3 | Content core list ("less text" never cuts facts); options never change settled fonts, palette or corners; directions differ in structure, not palette |
| RC4 | Live measurement with `read_page.js` before building from a reference; figure audit by script at nine widths |
| RC5 | The no-moving-CTA and meaning-colour rules are in `making.md` section 11, which every build reads. Promoting them to house standards needs a decision (below) |
| RC6 | `preflight.py html` now checks kerning and tracking (checklist item 50, M51) against a new guide, `preflight/references/kerning.md`, with a scored eval page. `engine.py review` skips files carrying the engine's export header |

## 4. Not fixed here, and why

- **House standards from the owner.** Needs a decision: allow an `owner` source in `standards.json` (strength must, locked), so rules like no moving CTAs and known meaning colours are enforced by `engine.py review`, not just read.
- **Neutral defaults (#FFFFFF and #111111).** Needs a decision: OpenDesigner's default for everyone, or the owner's personal default kept in his project memory.
- **A blocking gate.** RC1 is only partly fixed by better wording. A real gate would be an `engine.py` step that records the picked samples and refuses to call a draft ready without them. Proposed, not built.
- **Project-specific lessons** left for their own changes: inheriting from a parent codebase (3), `od-reason` markers (6), feel words "precise" and "industrial" (8), the video provider change (10, 23), brand names on stock photos (18), palette from the hero photo (19), oklab gradients (20), the `pathLength` bug (22), "rounded" for enterprise (28), real vendor logos (40), tree figures (41), the mix-and-match lab template (46).
- **The local files.** The notes file and the 14 owner rows stay with the session that wrote them, to be committed there. This change repeats the two `making.md` section 11 rows word for word, so the two edits merge cleanly.

## 5. Kerning and tracking, specifically

Why type spacing keeps going wrong in every kind of project:
1. Tracking is set by eye per section, as a literal, instead of from the text style tokens the engine already writes in em per size.
2. Values are copied from mocks in the wrong unit: Figma's -2% is -0.02em, not `-2%` (a share of the space width in CSS) or `-2px`.
3. Motion splits words into letters, which drops pair kerning and ligatures, and many screen readers then spell the word out.
4. Faces are not fully loaded: a fallback or a synthesized bold has spacing the tracking was not tuned for, and a subset font can lose features.
5. Nothing checked any of it beyond "tighter than -0.03em".

The guide (`skills/opendesigner-preflight/references/kerning.md`) lists each mistake with its cause and fix, with sources (MDN, W3C SC 1.4.12, Adrian Roselli's split-text tests, fontTools, the CSS Working Group). The new checks catch the rule-shaped ones automatically; the guide's six-step check covers the rest at 200%.
