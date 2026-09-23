# Repo plan: turning the research into the OpenDesigner product

Written 2026-09-23 by the orchestrator. Every repo-building agent follows this layout so their pieces fit. Source: `research/L18-ai-first-distribution.md` Part I (recommended architecture), `_coordination/BRIEF.md`, `synthesis/*`.

## Target layout
```
OpenDesigner/
├── README.md                  R1  humans first: what it is, 60-second quickstart per host, how it works, examples, research, contributing
├── AGENTS.md                  R3  canonical agent entry (<200 lines); replaces the current research-only AGENTS.md
├── CLAUDE.md, GEMINI.md       R3  "@AGENTS.md" plus host notes
├── plugin.json                R3  Agent Plugins 1.0 manifest (Codex, ChatGPT, Cursor, VS Code, Copilot, Kiro)
├── .claude-plugin/            R3  plugin.json + marketplace.json (the repo doubles as a Claude marketplace)
├── skills/                    R3  SOURCE OF TRUTH, Agent Skills format, portable frontmatter only
│   ├── opendesigner/          router skill: interview flow, depth modes, pacing, visual ladder, output contract
│   │   ├── SKILL.md           (<500 lines)
│   │   ├── references/stages/ one file per questionnaire stage, built from synthesis/questionnaire.json
│   │   ├── references/        rules.md (interview rules), hooks.md (designer hooks), guardrails.md
│   │   ├── assets/templates/  visual templates (.html, JSON-fed): palette, type scale, spacing ruler, radius, elevation, motion, component sheet, option gallery
│   │   ├── assets/output/     DESIGN.md, decisions.md, state.json templates
│   │   └── scripts/engine.py  R2  state, ramps, scales, contrast, validate, export (stdlib only, no network)
│   ├── opendesigner-extract/  reference intake (repo CSS, URL, screenshot, Figma variables), never copies identity
│   ├── opendesigner-extend/   later-session protocol: read DESIGN.md + tokens + decisions before changing anything
│   └── opendesigner-export/   DTCG, CSS variables, Tailwind, Figma (use_figma), Paper
├── .agents/skills/, .claude/skills/   R3  GENERATED copies of skills/ (tools/sync_skills.py; CI checks drift)
├── data/                      R3  chunked knowledge built from synthesis/ by tools/build_data.py (ontology, graph, levers, questions per stage, hooks, pacing)
├── examples/                  R2  complete worked examples, each with DESIGN.md, decisions.md, tokens/, css/, preview.html
├── chatgpt-project/           R3  instructions.md + at most 5 knowledge files, for ChatGPT Projects
├── docs/                      R1  SPEC.md (from S1d), HOW-IT-WORKS.md, RESEARCH.md (map of the research), FAQ.md
├── research/, benchmarks/, sources/, traces/, synthesis/   unchanged: the evidence base
├── _coordination/, tools/od.py, tools/jev_nav.py           unchanged: multi-session collaboration
├── .github/                   R1  issue forms, PR template, FUNDING.yml, workflows/ci.yml, labels
├── CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, SUPPORT.md, GOVERNANCE.md, CITATION.cff, CHANGELOG.md   R1
└── LICENSE (MIT, code) + LICENSE-CONTENT (CC BY 4.0, research and docs)   R1  [default; Kunal can change before going public]
```
Phase 2 (`server/`, a stateless MCP server with MCP Apps views reusing the templates) is roadmap only in this pass.

## Owners in this pass
| Id | Owner | Builds |
|---|---|---|
| S1d | subagent | `synthesis/OPENDESIGNER-SPEC.md` (copied to `docs/SPEC.md` by R1) |
| R1 | subagent | README, docs/, community health files, .github/, licenses, social preview image, `docs/SEED-ISSUES.md` (the orchestrator creates the issues) |
| R2 | subagent | `skills/opendesigner/scripts/engine.py` + tests, exporters, `examples/` |
| R3 | subagent | skills/ (except engine.py), data/ + `tools/build_data.py`, templates, manifests, `tools/sync_skills.py`, chatgpt-project/, new AGENTS.md/CLAUDE.md/GEMINI.md |
| R4 | subagent | `docs/SPONSORSHIP.md` (verified funding options) |
| D1 | orchestrator | writes `design/` artifacts into Paper (and Figma after sign-in) |

## Engine contract (R2 implements, R3's skills call it)
Run from the user's project; state lives in `./opendesigner/` unless `--dir` is given.
```
python3 <skill>/scripts/engine.py init [--dir D] [--from examples/<name>/state.json]   create state.json with defaults
python3 <skill>/scripts/engine.py set <dotted.path> <json-value>                       record one decision (appends to decisions.md with --why "reason")
python3 <skill>/scripts/engine.py generate                                           state.json + levers.json -> tokens/ (DTCG 2025.10 + resolver)
python3 <skill>/scripts/engine.py validate [--json]                                  contrast, targets, lint; exit 1 on errors; report cites the rule
python3 <skill>/scripts/engine.py export --format css|tailwind|figma|paper|swift|compose|dtcg
python3 <skill>/scripts/engine.py design-md                                          render DESIGN.md from state + tokens + decisions
python3 <skill>/scripts/engine.py preview [--open]                                   render preview.html (specimen of every token and a few components)
```
`state.json` holds the person's answers keyed by questionnaire question id, the dial values (0-100), raw inputs (brand color, typefaces, base sizes, platforms, devices), and asset-hook status (have / commissioning / using tool / skipped). The engine reads `levers.json` from the skill's own `references/` folder so the skill works offline and self-contained.

`FUNDING.yml` is owned by R4 (not R1).

## Shared conventions
- Python 3.10+, standard library only, no network in anything that ships inside `skills/`.
- Every value the engine produces traces to `synthesis/levers.json` or a Decision Card; keep `[inferred]` honesty in docs.
- DTCG 2025.10 is the canonical token format; DESIGN.md is the readable view.
- Reference intake copies structure and quality, never another brand's identity (hard rule).
- Plain language for engineers in every user-facing file. No marketing fluff, no emoji walls, no trophy badges.
- Don't edit another owner's files. Log product decisions with `python3 tools/od.py log`. Never commit secrets.
