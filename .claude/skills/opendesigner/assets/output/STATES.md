# {{name}}: states

<!-- OpenDesigner output template: the state catalogue, kept at opendesigner/STATES.md. Copy it when the product has a screen
that shows data: a list, a total, a count, a status, progress against a limit, or the result of an action. Fill the rows before
you design or change that screen. It comes from one project's lessons (research/L21-design-playbook.md, DC-L19-125): treat its
lists as a starting point to test, not a rule. Placeholders look like {{this}}. -->

Agreed with {{the owner}} on {{YYYY-MM-DD}}. Read this before you change any screen that shows a state. Screens take their words from here; they never invent a state of their own.

## Rules

1. **List the states first.** No screen that shows data is designed or changed until each of its states is a row in section 2. If a state you need is missing, add the row, get it agreed, then build.
2. **Words carry the state.** Every state is said in words. Color agrees with the words and never speaks alone, so the screen reads the same in grayscale and to a screen reader (an accessibility floor).
3. **One job per tone.** Use the system's status roles: `danger` only for something that failed, is invalid or is already over; `warning` for something that needs attention; `info` for what is not a problem; `success` for something that went well (a completed action, a real improvement), never for "no change"; no tone for ordinary states. In a family of states, only the worst one gets `danger`. The brand accent is never a state color.
4. **Say it once per screen.** One place on each screen states the state. Nothing nearby repeats it or says the opposite.
5. **One set of words, one set of numbers.** The same state has the same words on every screen. Each threshold is defined once (section 1), and every screen reads that definition.
6. **The boundary gets its own row.** "Exactly at the limit" is not "over". For every threshold, write the rows below, at and above it (section 3).
7. **Unknown is not empty.** Show loading until the first answer arrives, then the content or the designed empty state; never empty first and content after. Every wait has a failure row that says what happened and what to do next.
8. **Every empty, blocked or failed state has a next step,** or its row says why it has none.
9. **A state nobody designed falls back to the calmest state that is true:** neutral words, no tone. Log it as a missing row and design it.
10. **Optional (one project's choice; confirm with the owner):** keep text and figures in the normal text color and put the tone only in a small mark beside the words: a dot, an icon, a bar, a ring, or a light tint behind a notice.

## 1. Thresholds and meanings (one source of truth each)

| Question | Answer | Where it is defined |
|---|---|---|
| When is it "{{state name}}"? | {{the rule, with < and <= spelled out}} | {{constant or function, and file}} |
| What do 0, empty and missing mean for {{value}}? | {{answer}} | {{where}} |
| Why do two screens show different numbers for {{name}}? | {{the different questions, and the words that say which}} | {{where}} |

## 2. The matrix

One row per state. The id is `<class>-<number>` and is never reused. "Hidden" is what this state leaves out that a neighbouring state shows. "Next step" is `yes -> <where it goes>` or `no: <reason>`.

| Id | State | Trigger | Words | Tone | Where the tone shows | Hidden | Next step | Test |
|---|---|---|---|---|---|---|---|---|
| none-1 | {{state}} | {{exact rule}} | {{exact words, with {value} for a figure}} | {{none, info, success, warning or danger}} | {{dot, icon, bar, ring, tint, or none}} | {{what is left out, or "nothing"}} | {{yes -> ..., or no: reason}} | {{test name, or "by hand: step"}} |

*Example (generic):* `none-1 | First use | the list has never had an item | "No projects yet" | none | none | filters and sort | yes -> New project | states_none_1`.

Classes to sweep. A class the product truly does not have gets one row with State `n/a` and the reason in Trigger.

| Class | Prompts |
|---|---|
| `none`: nothing there yet | first use; nothing matches a search or filter; all done; nothing this period; sample data |
| `setup`: not set up | no limit or target; a permission not given; set up and waiting for the first data |
| `limit`: progress against a number | under; near; exactly at; over; projected to go over |
| `time`: time edges | first day; last day; a past or future period; the change at local midnight |
| `load`: loading and stale | first load; refresh while old data shows; stale (say how old); partial data |
| `fail`: failure and gates | failed; cancelled; denied; offline; a hand-off to another app that comes back with each possible outcome |
| `hide`: hidden or left out | private values hidden; items left out of a total; archived items |
| `edge`: data extremes | zero; one item; thousands; very large and very small values; negative; a very long name; no name; right-to-left text |

## 3. Boundaries

| Threshold | Value | Below | At | Above | Where it is defined |
|---|---|---|---|---|---|
| {{name}} | {{value}} | {{row id}} | {{row id}} | {{row id}} | {{where}} |

## 4. Modes (every row is checked in each)

| Mode | What must hold | Result: seen, or "not seen" |
|---|---|---|
| Light and dark | text keeps 4.5:1 and marks keep 3:1 against their background | {{result}} |
| Largest text size | words wrap or shorten; nothing overlaps or clips | {{result}} |
| Reduced motion | nothing slides or bounces in; content appears in place | {{result}} |
| Screen reader | each state is read as its words, never as "red dot" | {{result}} |

## 5. Contradictions settled

| Was | Now | Decided by | Fixed in |
|---|---|---|---|
| {{what two screens said}} | {{the one rule}} | {{the owner's words and date, or this file}} | {{screens or files}} |

## 6. Open questions for the owner

| # | Question | Recommendation | Default until answered | Blocks work? |
|---|---|---|---|---|
| 1 | {{question}} | {{recommendation}} | {{default}} | {{yes or no}} |

## Building from it

- One function per screen picks the state and returns everything the screen says for it: the label, the figure, the caption and the tone. The screen draws that result and holds no state logic or state text of its own.
- Write one test per row, named with its id. Add one test that loops over every state and fails when a state lacks its words, its tone or its screen-reader text. For each threshold, test just below, exactly at and just above it.
- Keep one hidden page or story that draws each component in every state side by side, through the same code and tokens as the real screen, in light and dark.
- When someone flags one wrong state, list every state of that feature here before you fix the one they named.
- A change to a word, a threshold or a tone edits this file in the same change.
