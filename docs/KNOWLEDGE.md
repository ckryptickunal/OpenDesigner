# How OpenDesigner learns

OpenDesigner's advice comes from sources someone trusts. This page sets the rules for three things:
- how a new source gets in;
- which source wins when two disagree;
- how a change reaches the skills and the design systems people have already made.

The same rules work at two levels:
- **The OpenDesigner repo** (house knowledge, for everyone). Maintainers add sources to `learn/sources.json`.
- **A person's own project** (project knowledge, for that one system). While they use OpenDesigner, a person can say "follow this", "this is non-negotiable for us" or "use this as a reference".

## 1. Three kinds of source

Every source has an **authority**. It decides what the knowledge is allowed to do.

| Authority | What it becomes | Who can change it |
|---|---|---|
| **Non-negotiable** | A **standard**. It is applied without asking, locked, written into DESIGN.md and checked by `engine.py validate` and `review` | Only the person, and only when they explicitly ask to improve, remove or change it. The agent restates the standard and its reason once, then records the change with the person's words |
| **Good to have** | A **recommended default**: the option OpenDesigner recommends first | The person, freely, like any other answer |
| **Reference** | **Learning material**: options and their visual effect, examples for visual samples, process steps, heuristics. It never becomes a default on its own | Not applicable. It informs choices; it does not make them |

When nobody says, a source is a reference. The agent asks one question when the difference matters: "Should I follow this as a rule, recommend it, or just learn from it?"

## 2. Which one wins

From highest to lowest. A higher rule wins, and the agent tells the person in one line when that happens.

1. **Accessibility floors** (`guardrails.md` section 4). Locked. They can only be raised.
2. **The person's explicit choice in this project.** This includes an explicit override of a standard.
3. **Project standards.** These come from sources the person marked non-negotiable for their project, such as their brand book or their company's UI rules.
4. **House standards.** These come from the OpenDesigner repo's non-negotiable sources (`synthesis/standards.json`).
5. **Recommended defaults** from good-to-have sources, the project's first, then the house's.
6. **Research defaults.** These are `levers.json` and the Decision Cards.
7. **Reference material.** It shapes the options, examples and explanations, never the default by itself.

A conflict is never settled silently.
- In the repo, it goes into the lane file ("Conflicts with existing research").
- In a project, the agent says it once, for example: "Your brand guide asks for ease-in exits; OpenDesigner's house standard is ease-out. Your guide wins in this project." It then records it.

## 3. How knowledge is used in a session

| Moment | What the skill does | Where it comes from |
|---|---|---|
| Start (`engine.py init`, `sketch`) | Applies every house standard that fits the project and maps to a token or setting, locked, with `set_by: standard`. It says so once, in the first result: "I applied OpenDesigner's house standards for motion and components; say if you want to change one" | `references/standards.json` |
| Which standards fit | A standard applies when one of its `applies_to` tags is one of the project's tags. The project's tags are its platforms (web gives web and css; ios gives ios and swift; android gives android and compose; desktop gives desktop, web and css) plus its recorded stack (`raw.stack`, such as react or react-native). The stack is read from the project's `package.json` first; the agent asks once only when that file does not settle it | `rules.md` section 3 |
| Each question | Recommends one option. The recommendation never contradicts a standard. Each option shows a visual sample of the same real screen, with **Now:** (what changes today) and **As it grows:** (what it means with more screens, people, platforms and content) | `questions.json` options, `synthesis/impact.json`, Decision Cards |
| A question a standard settles | Not asked, like a Planned one: the stage file says **Settled by:** STD-..., and `questions.json` has `settled_by`. An option that would break a standard is marked "(breaks STD-...)", is never recommended, and `engine.py pick` refuses it unless the person has overridden that standard | the standard's `settles` and `breaks_options` |
| Deciding without asking | Standards: apply, and mention once. Mechanical and low-impact questions: default, and list them at the next gate. "You pick": delegate, and give the reason | `rules.md` section 6, `learn/wiki/synthesis/decide-or-ask.md` |
| "Why?" | Cites the card or standard, and its source | `cards/*.json`, `standards.json` |
| Implementation | DESIGN.md lists the standards to follow. `engine.py review` flags code that breaks one (for example `transition: all`, or an enter animation from `scale(0)`) | `standards.json` → DESIGN.md, review checks |

## 4. A person adds a source while working

This happens when the person shares a link or file and says to follow it, or to learn from it.

1. **Authority.** If they did not say, ask the one question from section 1.
2. **Consent to read.** Show the URL and get a yes (`guardrails.md` section 2). Paid, logged-in and paywalled content stays out of scope.
3. **Read and extract.** Read it the way the repo does (`learn/README.md`, "The analysis schema"): rules with exact values, decisions, and examples. Show the person the extracted rules in plain words, 10 at most per message, and ask which to keep.
4. **Record.** One command records every kept rule, the same in every doc:
   ```
   engine.py standard add --rule "..." --why "..." --source <url, or "person, 2026-09-27"> [--path P --value V]... [--values '{...}'] [--review-pattern <regex> --review-message "..."] [--authority good-to-have] [--beats STD-a,STD-b]
   ```
   - **Non-negotiable:** the command as it is. It becomes a project standard, locked like a house standard. Repeat `--path` and `--value` once for each token the rule fixes. Add `--review-pattern` when code that breaks it can be found line by line. The source can be a link, a file name, or the person's own words with the date.
   - **Good to have:** the same command with `--authority good-to-have`. OpenDesigner recommends it first, and it stays unlocked.
   - **Reference:** record nothing. It shapes options, examples and explanations only. When the person picks a value from it, record that value with `engine.py set <path> <value> --set-by reference --source-ref <url>`.
5. **When it clashes with a house standard,** say so once, then follow the person's words:
   - **"It's our brand", "always", "non-negotiable for us":** a project standard that beats the house one. Add `--beats STD-...` to the command. The engine records "project wins", and it turns off those house standards' review checks and constraints for this project. `standard remove` turns them back on.
   - **"Just this value", "just here":** an override of the house standard, not a new rule: `engine.py standard override <id> --why "<their words>"`.
6. **Offer it upstream, once.** "Want to suggest this source to OpenDesigner for everyone?" Skip this for a local file or anything internal to their company. After a yes, run `engine.py feedback "source: <url> (<authority>, why)" --kind idea`. It is sent only with their OK (`improve.md`).

## 5. How the repo reacts to new knowledge

```
new link ─> learn/sources.json (authority) ─> fetch ─> analyse ─> verify ─> learn/analysis/
                                                                              │
             non-negotiable ─> synthesis/standards.json  (draft by theme, verify, merge, completeness critic)
             good-to-have   ─> recommended defaults       (Decision Card, "Maps to" a question)
             reference      ─> research/L19 Decision Cards, learn/wiki/synthesis/, synthesis/impact.json
                                                                              │
                 tools/build_data.py ─> skills/*/references/  ─> engine.py behaviour ─> tests ─> release
```

Rules for every change:
- **Standards are versioned.**
  - `synthesis/standards.json` has a `version` and a content hash. Changing a standard without bumping the version fails the build: `tools/build_data.py` (and its `--check`) and `tools/wiki.py standards` exit 1 until you run `python3 tools/wiki.py standards --bump "what changed"`.
  - The bump compares the file with the last commit, so it needs git. It refuses when nothing changed. A second bump before the commit amends the same version.
  - Each standard records the version it arrived in (`since`) and the version it last changed in (`changed`).
  - A removed standard moves to `retired`, with the reason. It never simply disappears.
  - `built_from` records the analyses the standards were built from. Only the learn-standards merge sets it (`wiki.py standards --built-from`), so `wiki.py next` can say when a house source changed since.
  - A standard may also carry `settles` (questions it answers), `breaks_options` (options that contradict it), `constraints` (values a token may not take, such as an accelerating curve) and `supersedes` (older Decision Cards it replaces). `wiki.py standards` checks that each names something real, and that no two standards set one token to different values.
- **Reference material can't change a default by itself.** It proposes a change in a Decision Card (Part B of the lane file). That change needs to be verified and then applied to the source files in `synthesis/`. Only then does the build pick it up.
- **Every claim traces to a source.**
  - Cards cite `S-L19-nnn` ids, and `jev_nav.py check` fails on a dangling one.
  - Standards cite analysis ids.
  - Analysis cites the raw text.
- **Third-party text stays out of git.** Only summaries, rules and at most 3 short quotes per source are committed.
- **The engine behind the wiki is tracked.**
  - `learn/openwiki.lock.json` pins the tested OpenWiki commit.
  - `tools/wiki.py upstream` shows new commits. Its `--upgrade` flag installs the new commit, runs OpenWiki's tests and ours, and moves the lock only if both pass.
  - A weekly CI job does the same check and opens an issue when OpenWiki moves.

## 6. How existing projects get new standards

A design system made with an older version keeps working. When the house standards change:
- `engine.py validate` reports, as an advisory, that the house standards moved since this system was made. It lists how many are new, changed or retired.
- `engine.py standards --update` applies the new and changed ones. Anything the person overrode stays overridden: their explicit choice outranks a standard (section 2). Retired standards are unlocked, not reverted. Then `engine.py build` rebuilds the tokens, exports and DESIGN.md.
- The extend skill runs `engine.py validate` first when it opens a project, so it notices. It tells the person in one line, then shows what changed, grouped by area.
- `engine.py set --force` is for values the person locked. It never changes a value a standard holds; that takes `standard override`.
- Project standards (section 4) belong to the person. House updates never touch them.

## 7. Who does what

| Task | Who | Tool |
|---|---|---|
| Add a house source, pick its authority | the repo owner | `tools/wiki.py add`, then the checklist in `learn/IMPROVING.md` section 4, "A new house source" |
| Analyse, verify, synthesise | lane L19 (any agent following `_coordination/lanes/L19-learning-wiki.md`) | `.claude/workflows/learn-analyze.js`, `tools/wiki.py` |
| Change a house standard | a maintainer, with a verified source | edit `synthesis/standards.json`, then `wiki.py standards --bump` |
| Add a project source or standard | the person, in their project | the skill (section 4), `engine.py standard add` (with `--beats` when it outranks a house standard) |
| Override a standard in a project | the person, explicitly | `engine.py standard override <id> --why "<their words>"` |
