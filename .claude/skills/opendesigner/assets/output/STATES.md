# {{name}}: states

<!-- OpenDesigner output template: the state catalogue, kept at opendesigner/STATES.md. Offer it when someone builds a screen that
shows data, such as a list, a total, a count, a status, progress toward a limit, or what happened after an action. Adapt the lists
to the product; they are a place to start, not a rule. Placeholders look like {{this}}. -->

{{The owner}} agreed to this on {{YYYY-MM-DD}}. Check it before changing any screen that reports a state. Every screen gets its wording from this file and never makes up a state on its own.

## Rules

1. **Rows before screens.** Before building a screen that shows data, add a row in section 2 for each state it can be in. If a screen turns out to need a state with no row, write the row first, then build it.
2. **The words say it.** Each state has words. Color backs those words up and never carries the meaning by itself, so the screen means the same in grayscale and through a screen reader (an accessibility floor).
3. **Each tone has one meaning.** Use the system's status roles: `danger` for a failure, something invalid, or a limit already passed; `warning` for what needs a look; `info` for news that is not a problem; `success` for a good result (an action finished, a real gain), and never for "nothing changed"; no tone for everyday states. Among related states, only the most serious one uses `danger`. The brand accent never marks a state.
4. **State it in one place.** Each screen reports a state once. Nothing close by repeats it, and nothing contradicts it.
5. **The same wording and the same thresholds everywhere.** A state reads the same on every screen. Each threshold has one definition (section 1), and every screen uses it.
6. **Give the boundary a row of its own.** Reaching a limit is not passing it. For each threshold, write the rows for just under it, exactly on it and over it (section 3).
7. **Not known yet is different from empty.** While nothing has loaded, show that it is loading; after that, either the content or the empty state that was designed for it, and never a blank screen that fills in later. Every wait also has a failure row: what went wrong, and what the person can do.
8. **Empty, blocked and failed states point somewhere,** or their row explains why there is nowhere to go.
9. **When a state was never designed, fall back to the quietest true one:** plain words, no tone. Then add the missing row and design it.
10. **Optional (one project did this; check with the owner):** keep words and numbers in the ordinary text color, and let a small mark next to them carry the tone: a dot, an icon, a bar, a ring, or a pale tint behind a notice.

## 1. Thresholds and meanings (each defined once)

| Question | Answer | Where it is defined |
|---|---|---|
| What makes it "{{state name}}"? | {{the rule, with < and <= written out}} | {{constant or function, and file}} |
| For {{value}}, what do 0, empty and missing each mean? | {{answer}} | {{where}} |
| Why might {{name}} differ between two screens? | {{the question each one answers, and the words that tell them apart}} | {{where}} |

## 2. The matrix

A row for every state. Ids look like `<class>-<number>` and are never used twice. "Hidden" names what this state leaves out that a related state shows. "Next step" is `yes -> <destination>` or `no: <reason>`.

| Id | State | Trigger | Words | Tone | Where the tone shows | Hidden | Next step | Test |
|---|---|---|---|---|---|---|---|---|
| none-1 | {{state}} | {{exact rule}} | {{exact words, with {value} for a figure}} | {{none, info, success, warning or danger}} | {{dot, icon, bar, ring, tint, or none}} | {{what is left out, or "nothing"}} | {{yes -> ..., or no: reason}} | {{test name, or "by hand: step"}} |

*Example (generic):* `none-1 | First use | the list has never had an item | "No projects yet" | none | none | filters and sort | yes -> New project | states_none_1`.

Go through each class below. If the product has no such case, give the class one row with State `n/a` and the reason under Trigger.

| Class | Prompts |
|---|---|
| `none`: nothing there yet | first use; a search or filter with no matches; everything done; nothing in this period; sample data |
| `setup`: not set up | no target or limit set; a permission not granted; set up but no data yet |
| `limit`: progress toward a number | under; close; exactly on it; over; on course to go over |
| `time`: edges of time | the first day; the last day; a past or future period; the switch at local midnight |
| `load`: loading and stale | the first load; refreshing while old data is shown; stale (say how old); some data missing |
| `fail`: failures and gates | failed; cancelled; denied; offline; handing off to another app and coming back with each possible result |
| `hide`: hidden or left out | private values hidden; items not counted in a total; archived items |
| `edge`: extreme data | zero; a single item; thousands; huge and tiny values; negative values; an extremely long name; a missing name; right-to-left text |

## 3. Boundaries

| Threshold | Value | Below | At | Above | Where it is defined |
|---|---|---|---|---|---|
| {{name}} | {{value}} | {{row id}} | {{row id}} | {{row id}} | {{where}} |

## 4. Modes (check every row in each)

| Mode | What must hold | Result: seen, or "not seen" |
|---|---|---|
| Light and dark | text at 4.5:1 or more and marks at 3:1 or more against what is behind them | {{result}} |
| Largest text size | words wrap or shorten, and nothing overlaps or gets cut off | {{result}} |
| Reduced motion | nothing slides or bounces in; content simply appears | {{result}} |
| Screen reader | a state is announced by its words, never as "red dot" | {{result}} |

## 5. Contradictions settled

| Was | Now | Decided by | Fixed in |
|---|---|---|---|
| {{what two screens said}} | {{the one rule}} | {{the owner's words and date, or this file}} | {{screens or files}} |

## 6. Open questions for the owner

| # | Question | Recommendation | Default until answered | Blocks work? |
|---|---|---|---|---|
| 1 | {{question}} | {{recommendation}} | {{default}} | {{yes or no}} |

## Building from it

- For engineers, one option: give each screen a single function that chooses the state and returns all of its text for that state (label, figure, caption and tone), so two screens can never phrase one state two ways.
- Name one test after each row's id. Add a test that goes through every state and fails if one is missing its words, its tone or its screen-reader text. For each threshold, test a value just under it, one exactly on it and one just over it.
- Keep a hidden page or story that shows each component in every state next to each other, using the live screen's own code and tokens, in light and dark.
- If someone points out one wrong state, list all of that feature's states here before fixing the one they mentioned.
- A change to any wording, threshold or tone updates this file in the same change.
