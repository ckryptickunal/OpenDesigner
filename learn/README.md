# The learning wiki

OpenDesigner learns from a short list of sources its owner trusts: YouTube channels, single videos, websites, docs and GitHub repos. This folder is that knowledge, kept on its own. It holds the sources, a structured reading of each one, a Markdown wiki that ties them together by concept, and the tools and workflows that keep it current. The app draws on it for three things:
- **House standards:** rules applied in every project.
- **Decision Cards:** better questions and options.
- **Impact notes:** what each choice changes now, and as the product grows.

## Start here

| You want to... | Read |
|---|---|
| Understand a concept, or see everything known about an area | [MAP.md](MAP.md): the knowledge by area, standard, card and question |
| Change or improve the app using what the wiki teaches | [IMPROVING.md](IMPROVING.md) |
| Know what each kind of source is allowed to change, and which wins | [../docs/KNOWLEDGE.md](../docs/KNOWLEDGE.md) |
| Add a source, or bring the wiki up to date | this page, from "Three kinds of source" down, and `python3 tools/wiki.py next` |

The extraction and ingest engine is [OpenWiki](https://github.com/ckryptickunal/OpenWiki) (the `openwiki` package). `tools/wiki.py` adds what OpenDesigner needs on top of it: authority levels, pages and GitHub files as sources, the analysis schema, checks, the citation trace, the Jev citation check and the map.

## What is in this folder

| Path | Committed | Holds |
|---|---|---|
| `MAP.md` | yes (generated: `wiki.py map`) | the index: every area, topic, standard theme, Decision Card and question, with links |
| `IMPROVING.md` | yes | how to turn the wiki into app changes |
| `sources.json`, `taxonomy.json` | yes | the source list with each source's authority, and the controlled topic names |
| `analysis/<id>.json` | yes | the structured reading of one source: summary, rules, decisions, process, examples, numbers, at most 3 quotes of 15 words or fewer |
| `wiki/sources/`, `topics/`, `entities/`, `index.md` | yes (generated: `wiki.py ingest`) | OpenWiki pages: one per source, per topic and per person, company or product |
| `wiki/synthesis/` | yes | cross-source topic pages, "Decide or ask", the house standards page, the citation check report |
| `wiki/synthesis/_cards/`, `_standards/` | yes | the Decision Cards by area (the source for `research/L19-learning-wiki.md`), and the standards drafts by theme |
| `sids.json`, `citation-check.json`, `citation-review.json`, `openwiki.lock.json` | yes | source id to `S-L19` citation id; Jev's verdicts (no source text); the review decisions that settle flagged items (`wiki.py review-log`, written by learn-escalate); the tested OpenWiki commit |
| `wiki/ingested.json` | yes (generated: `wiki.py ingest`) | what is in the wiki, and the hash of the analysis each page was built from. An edited analysis is re-ingested on the next `ingest` |
| `raw/` | **no** (git-ignored) | full transcripts and page text. Third-party content stays on the machine that fetched it; `wiki.py fetch` gets it again. `raw/_skipped.json` lists the pages fetch could not use on this machine |

What the wiki produces for the app lives where the app's build expects it:
- `synthesis/standards.json` and `synthesis/impact.json`;
- `research/L19-learning-wiki.md`;
- `traces/L19-trace.md`.

Every one of them is rebuilt from this folder by the workflows below, so this folder is the source of truth.

## Three kinds of source

Every source in `sources.json` has an `authority`. It decides what the knowledge is allowed to do.

| Authority | What it becomes | Can a project change it? |
|---|---|---|
| `non-negotiable` | **House standards** (`synthesis/standards.json`). Applied and locked in every project, written into DESIGN.md, checked by `engine.py validate` and `review` | Only when the person explicitly asks to improve, remove or change one. The change is recorded with their words as the reason |
| `good-to-have` | Recommended defaults: the option OpenDesigner recommends first | Yes, freely |
| `reference` | Learning material: Decision Cards (`research/L19-learning-wiki.md`), options and their visual effect, process steps, examples for visual samples | Not applicable. It informs choices; it does not make them |

Current sources:
- **Non-negotiable:** Emil Kowalski's site, the Sonner docs, animations.dev (public pages only; the course itself is paid), the `emilkowalski/skills` repo (MIT).
- **Good to have:** the Vaul docs. The Vaul README says the library is unmaintained, so OpenDesigner recommends its drawer craft but flags that status before suggesting it as a dependency.
- **Reference:** every video on Kole Jain's and Mobbin's channels, and Steve Schoger's "Designing with Claude Code".

## The pipeline

```
sources.json ─ fetch ─> raw/<folder>/<id>.txt (+ <id>.media.json for pages)
                             │
                   analyse (one agent per source reads it in full)
                             │
                   verify (a fresh agent tries to refute every rule, value and quote)
                             │
                   analysis/<id>.json ─ check ─ ingest ─> wiki/sources, topics, entities, index
                             │
                   synthesise ─> wiki/synthesis/*.md   (one page per topic, across sources)
                             ├─> synthesis/standards.json      (non-negotiable -> house standards)
                             └─> research/L19-learning-wiki.md (reference -> Decision Cards)
                                          │
                               tools/build_data.py, jev_nav.py export -> the skills' references/
```

### The saved workflows

Each step that needs judgement runs as a saved Claude Code workflow in `.claude/workflows/`. Any other agent can follow the same prompts by hand: read the file.

Every workflow takes `root`: the absolute path of the checkout it works in. Without it, the workflow stops at once with a message saying which args it needs; it never falls back to someone else's folder. `python3 tools/wiki.py next` prints the exact args for each step that is due.

| Workflow | Run it when | Args |
|---|---|---|
| `learn-analyze` | sources were fetched but not analysed | the output of `python3 tools/wiki.py pending --work-items`: `{"root": "<repo path>", "items": [...]}`. One item per video or article; the pages of one site, and the files of one folder of a GitHub repo, share an item, at most 5 files each |
| `learn-standards` | non-negotiable or good-to-have sources changed | `{"root": "<repo path>"}`, optionally `"themes": [...]`. It reads the house sources and their raw folders from `sources.json`, may add a theme when rules fit none, and ends with `wiki.py standards --built-from` |
| `learn-synthesis` | reference sources changed, or topic pages and cards need to catch up | `{"root": "<repo path>", "topics": [...], "cards": [...], "verify": [...], "process": true, "merge": true}`; all but `root` are optional |
| `learn-escalate` | `cite-check` flagged items | `{"root": "<repo path>"}`. It reads `wiki.py flagged --json`, where each item names its raw file |
| `learn-personas` | after any change to standards, skills text or the pipeline | `{"root": "<repo path>"}`, optionally `"only": ["student", ...]` |

## What to do next

`python3 tools/wiki.py next` checks the whole pipeline and prints each step that is out of date, in order, with the exact command or workflow args to run:
1. analysis files that fail `check`, each with its fix (an analysis whose authority changed is redone with learn-analyze, because the authority decides how completely rules are extracted);
2. sources nothing was fetched or learned from yet, including pages fetch had to skip;
3. fetched but not analysed; analysed but not in the wiki (or its page was built from an older analysis) or the trace;
4. standards built before a non-negotiable or good-to-have analysis changed, or edited without a version bump;
5. reference sources no card or topic page uses yet (with the learn-synthesis args for their areas);
6. rules whose text Jev has not checked, and flagged items waiting for learn-escalate;
7. skill files older than `synthesis/`, and an untested OpenWiki.

Last, as a note and not as work, it lists analysed sources whose raw text is not on this machine. That is normal in a fresh clone: `raw/` is git-ignored and the committed analyses are what the app uses. Fetch it again only to re-analyse or citation-check. `python3 tools/wiki.py status` counts the same way: analysed, in the wiki, and raw text here. Start every session in this folder with `next`.

## Add a source

```bash
python3 tools/wiki.py add https://www.youtube.com/@somechannel --authority reference
python3 tools/wiki.py add https://example.com/article --authority non-negotiable --name "Example"
.venv-wiki/bin/python tools/wiki.py fetch --only "Example"
python3 tools/wiki.py pending --work-items        # the args for the analysis workflow: {"root": ..., "items": [...]}
```

- `add` compares links without the scheme, `www.` or a trailing slash, so a page already on the list is refused, with the source that has it and its authority. It also refuses a name, raw folder or id prefix another source uses; pass a different `--name`. A GitHub repo is named after `owner/repo`. `add --help` lists the authorities.
- `fetch` exits 1 when a source ends up with no raw text (a page with too little text, a failed download) and records the skipped pages in `raw/_skipped.json`, which `next` reports. `fetch --only` with a name that matches nothing lists the valid names.
- `python3 tools/wiki.py remove "<name or link>"` takes a source, or one page of a multi-page source, off the list. What was learned from it stays until you delete its analysis files.
- A non-negotiable or good-to-have source is a house source: follow [IMPROVING.md](IMPROVING.md) section 4, "A new house source".

Then, in Claude Code, run the saved workflow `.claude/workflows/learn-analyze.js` with those args (or ask: "run the learn-analyze workflow on the pending sources"). Any other agent can follow the same two prompts by hand: they are in that file.

```bash
python3 tools/wiki.py check                         # schema and types, quote limits, authority, topic names, maps_to
.venv-wiki/bin/python tools/wiki.py ingest          # wiki pages and index; an edited analysis is re-ingested by itself
python3 tools/wiki.py trace                         # S-L19 ids in traces/L19-trace.md
python3 tools/wiki.py cite-check <ids>              # Jev checks every must/should rule against its source passage
python3 tools/wiki.py cite-check --standards        # and every house standard against the sources it cites
python3 tools/wiki.py flagged                       # what is left for review (learn-escalate)
python3 tools/wiki.py map                           # refresh MAP.md
```

`cite-check` follows TypeSafe's citation-check pattern. Code finds the passage the evidence points to. Jev judges whether it supports the rule, contradicts it, or says nothing about it. Any verdict other than "supports", and any below 0.8 confidence, is listed in `wiki/synthesis/citation-check.md` for a person or a reasoning model to review. Passages are not saved, because they are third-party text.

After new non-negotiable or reference material, run the `learn-standards` or `learn-synthesis` workflow (`python3 tools/wiki.py next` says which), then the repo checks in AGENTS.md.

## Setup

```bash
python3 -m venv .venv-wiki
.venv-wiki/bin/pip install "git+https://github.com/ckryptickunal/OpenWiki.git@$(python3 -c "import json;print(json.load(open('learn/openwiki.lock.json'))['commit'])")" pysocks pytest
```

- `YOUTUBE_API_KEY` in the environment lists channel videos. A single video works without it.
- YouTube blocks an IP after many caption requests. Wait an hour, or run `tor` and set `YOUTUBE_PROXY=socks5://127.0.0.1:9050`.
- No Gemini key is needed: the analysis is done by agents and passed to OpenWiki with `--analysis-file`. OpenWiki's own Gemini ingest still works if you prefer it, but its output lacks the rules, decisions and authority fields.
- `JEV_API_KEY` (TypeSafe) in the environment or `.env` enables `cite-check` and Jev ranking in `tools/jev_nav.py find`.

## Keeping up with OpenWiki

OpenWiki changes often. `openwiki.lock.json` records the commit this repo was last tested with.
- `.venv-wiki/bin/python tools/wiki.py upstream` lists new commits, and flags changes to the modules `tools/wiki.py` calls.
- `upstream --upgrade` installs the new commit and runs OpenWiki's tests and ours (`tools/test_wiki.py`, whose integration tests pin the contract: raw header parsing, ingest with analysis JSON, folder naming, lint). It moves the lock only when both suites pass. Otherwise it reinstalls the tested commit.
- `fetch` and `ingest` warn when the installed OpenWiki is not the locked one.
- The `OpenWiki upstream` GitHub workflow runs the same check every Monday. It opens an issue when OpenWiki has moved.

Example of why this matters: OpenWiki 0.2.0 started rewriting `/` in folder names (`raw/videos` became `raw_videos`, outside the git-ignored folder). `tools/wiki.py` now runs YouTube extraction with `raw/` as the root, and `test_safe_folder_name_contract` will fail if that behaviour changes again.


## The analysis schema

OpenWiki's fields (`summary`, `key_ideas`, `entities`, `topics`, `claims`, `quotes`, `tags`) plus:

| Field | What goes in it |
|---|---|
| `authority` | copied from `sources.json` |
| `rules` | `{rule, why, kind: do/dont, strength: must/should/consider, area, applies_to, values[], evidence}` |
| `decisions` | `{question, options[{name, effect, when}], recommendation, maps_to: Q-id or null, evidence}` |
| `process` | `{step, detail}`: how-to sequences (presenting a design, a case study, designing with an AI) |
| `examples` | `{what, where, visual_note}`: concrete products and visuals, the raw material for visual samples |
| `numbers` | `{value, context, evidence}` |
| `caveats` | sponsor segments, dated information, opinion versus fact |

Topic names come from `taxonomy.json` exactly, so each topic gets one wiki page. Everything must come from the source; anything an agent connects itself ends with `[inferred]`.

`wiki.py check` enforces the types and the allowed values:
- `numbers` and `caveats` are lists, even with one item, and each rule's `values` is a list of strings.
- A rule's `area` is one of color, typography, layout, shape, elevation, motion, iconography, components, patterns, content, accessibility, platforms, process, tokens or tooling.
- `kind` is `do` or `dont`.
- `applies_to` is one of the platform and stack tags that standards use: all, web, css, react, react-native, ios, swift, android, compose or desktop.
- A decision's `maps_to` is `null` or a question id that exists in `skills/opendesigner/references/questions.json`.
