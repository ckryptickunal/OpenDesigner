# Improving OpenDesigner with the learning wiki

The wiki is where OpenDesigner's taste comes from. This page is for anyone, a person or an agent, who wants to use it to change the app: a better question, a better default, a new check, a clearer explanation. [MAP.md](MAP.md) is the index. [../docs/KNOWLEDGE.md](../docs/KNOWLEDGE.md) sets what each kind of knowledge is allowed to change.

## 1. Before you change an area of the app

1. Open [MAP.md](MAP.md) and find the area ("Read by area").
2. Read its topic pages in [wiki/synthesis/](wiki/synthesis/). Each one covers:
   - what the sources teach;
   - where they disagree with each other and with the existing research;
   - which questions the topic informs.
3. Read the house standards themes for that area (`skills/opendesigner/references/standards/<theme>.md`). A change must never break a standard. Only the owner can change one, by the route in section 4.
4. In "Questions this knowledge touches", find the questions you plan to edit, and read their Decision Cards.

## 2. Ask the wiki a question

| You want | Do |
|---|---|
| The rule for something ("which easing for a closing modal?") | `python3 tools/jev_nav.py find "<question>"`. Jev ranks the house standards and every Decision Card |
| What the sources say on a concept | The topic page in `wiki/synthesis/`, then its sources in `wiki/sources/` |
| Why the app does X | `synthesis/standards.json` (the standard and its sources), or the card named in the stage file |
| The exact words of a source | The raw file in `raw/`. It stays local; fetch it again with `tools/wiki.py fetch` |
| Everything one source taught | `analysis/<id>.json` or its page in `wiki/sources/` |

## 3. Turn an insight into an app change

| Kind of change | Where you edit | Then run |
|---|---|---|
| **A question:** new option, better default, new heuristic or new question | `synthesis/QUESTIONNAIRE.md`, citing the card (`DC-L19-nn`) and its sources | `python3 tools/build_questionnaire.py`, `python3 tools/build_data.py`, the engine tests |
| **A "Now / As it grows" line** under an option | `synthesis/impact.json` | `python3 tools/build_data.py` |
| **Engine behaviour:** a new default value, a new token or a review check | `skills/opendesigner/scripts/engine.py` plus a test in `test_engine.py`. Cite the card or standard in a comment | `python3 skills/opendesigner/scripts/test_engine.py` |
| **Skill wording:** how the agent asks, decides or explains | `skills/*/SKILL.md` or `skills/opendesigner/references/*.md` (never the generated copies) | `python3 tools/sync_skills.py` |

In every case:
- **Log it.** Record the decision with `python3 tools/od.py log "..."`.
- **Where to start.** Part B of [../research/L19-learning-wiki.md](../research/L19-learning-wiki.md) lists every change the cards propose, with evidence. Part C lists where they disagree with older research. Both are good places to start.

Rules:
- **Reference material proposes; it doesn't decide.** A single video's number or "always/never" claim is opinion until another source or the existing research agrees. The card says which.
- **Never silently override older research.** If a card disagrees with an existing Decision Card, settle it openly: log the decision, and update or supersede the older card's default.
- **Every value traces to a source.** That means a card id, a standard id, or an `S-` id.

## 4. Change a house standard (maintainers only)

House standards come from sources the owner marked non-negotiable. To change one:
1. Change the source list or its authority in [sources.json](sources.json). If the source itself changed, fetch and analyse it again.
2. Re-run the standards synthesis: the saved workflow `.claude/workflows/learn-standards.js` with `{"root": "<repo path>"}`, or lane L19 step 6 by hand. It ends with `python3 tools/wiki.py standards --built-from`, which records the analyses the standards were built from.
3. Run `python3 tools/wiki.py standards --bump "what changed"`. It compares the file with the last commit (so it needs git), stamps `since` and `changed`, records the history, and moves removed rules to `retired`. It refuses when nothing changed, and a second bump before you commit amends the same version instead of adding one. Until the bump, `tools/build_data.py` refuses to build.
4. Run `python3 tools/wiki.py cite-check --standards` (it needs `JEV_API_KEY`), then `.claude/workflows/learn-escalate.js` with `{"root": "<repo path>"}` for anything flagged.
5. Run `python3 tools/build_data.py`, `python3 tools/sync_skills.py`, `python3 tools/wiki.py map` and every check in AGENTS.md ("Before you commit"). Existing projects pick up the change with `engine.py standards --update`, and their overrides stay (`docs/KNOWLEDGE.md` section 6).

A standard can also say what it does to the interview and to values (`docs/KNOWLEDGE.md` section 3). `wiki.py standards` checks each field:
- `settles`: the questions it answers, which the interview then skips.
- `breaks_options`: the options that would break it, which are never recommended.
- `constraints`: values a token may not take, such as an accelerating curve on `motion.easing.*`.
- `supersedes`: the older Decision Cards it replaces.

### A new house source

When a non-negotiable or good-to-have source joins the list, work through these steps in order:
1. **Add it.** `python3 tools/wiki.py add <url> --authority non-negotiable` (or `good-to-have`). Check the name, raw folder and id prefix it prints. `add` refuses one another source already uses.
2. **Scope and licence.** Public pages only: nothing paid, behind a login or paywalled. For a GitHub repo, add its licence (`"license"`) to the entry. Put any warning a project needs, such as an unmaintained library, in a `"note"`.
3. **Fetch.** `.venv-wiki/bin/python tools/wiki.py fetch --only "<name>"`. Exit 1 means nothing usable came back: fix the link, or take it off with `wiki.py remove`.
4. **Analyse.** Run the learn-analyze workflow with the output of `python3 tools/wiki.py pending --work-items`. For a house source the analysis must be complete, not a sample.
5. **Into the wiki.** `python3 tools/wiki.py check`, `.venv-wiki/bin/python tools/wiki.py ingest`, `python3 tools/wiki.py trace`.
6. **Standards.** Run the learn-standards workflow with `{"root": "<repo path>"}`. It reads the house sources and their raw folders from `sources.json`, so the workflow needs no edit. It may add a theme when the new rules fit none.
7. **Name the source where the prose lists them.** These are the "Current sources" in [README.md](README.md), the `policy` text in `synthesis/standards.json` (editing `policy` does not change the content hash), and the Tiers line at the top of `traces/L19-trace.md`.
8. **Version and check.** Follow steps 3 to 5 above: the bump, the citation check with learn-escalate, then the build and the checks. Add a CHANGELOG line, and log the decision with `python3 tools/od.py log "..."`.
9. **Try it.** Run the learn-personas workflow with `{"root": "<repo path>"}`, so the new rules are met the way a person meets them.

## 5. Keep the wiki fresh

- **New sources:** `python3 tools/wiki.py add <url> --authority ...`, then `python3 tools/wiki.py next` for each following step ([README.md](README.md)).
- **The pipeline's saved workflows** are in `.claude/workflows/`. The lane prompt (`_coordination/lanes/L19-learning-wiki.md`) has the same steps for any other agent.

| Workflow | What it does |
|---|---|
| `learn-analyze` | Analyses each fetched source, then has a fresh agent check the analysis against the source |
| `learn-standards` | Builds the house standards from the non-negotiable sources |
| `learn-synthesis` | Writes the topic pages, Decision Cards, decide-or-ask page and impact notes |
| `learn-escalate` | Reviews what the citation check flagged |
| `learn-personas` | Runs the end-to-end tests with simulated users |
- **OpenWiki,** the engine under the wiki, is pinned and checked weekly ([README.md](README.md), "Keeping up with OpenWiki").
