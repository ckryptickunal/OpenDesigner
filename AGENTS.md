# OpenDesigner: instructions for AI agents

OpenDesigner is an open-source, AI-first resource for creating design systems, designs and visuals. People load it into their own AI (Claude, ChatGPT, Codex, and others); the model interviews them, recommends best practices, shows and asks for examples, and slows down on the decisions that shape everything downstream. Read `_coordination/BRIEF.md` for the full product brief.

This repository currently holds the research that OpenDesigner is built from, plus the coordination system for the many agents building it.

## Layout
| Path | What it holds |
|---|---|
| `_coordination/` | `BRIEF.md` (what and why), `PROTOCOL.md` (how parallel sessions collaborate), `BOARD.md` (who owns which lane), `SCHEMA.md` (source tiers, Decision Card format), `DECISIONS.md` (decision log), `sessions/` (heartbeats), `inbox/` (messages between sessions), `lanes/` (ready prompts for new sessions) |
| `research/` | One file per research lane, written as Decision Cards (`### DC-Lxx-nn:`) |
| `benchmarks/` | Teardown of 25 famous design systems with real values |
| `sources/` | Community signal from /last30days and the registry of vetted sources |
| `traces/` | Append-only log of every source each lane opened |
| `synthesis/` | Combined outputs: ontology, questionnaire, dials and formulas (levers), decision graph, builder spec |
| `design/` | Tokens and artboards written to Figma and Paper for review |
| `tools/` | `od.py` (coordination), `jev_nav.py` (research navigation, Jev search, card export, decision graph, citation check) |

## If you are contributing
Follow `_coordination/PROTOCOL.md`. In short: pick a session name, `python3 tools/od.py status`, claim a lane, log every source, cite every claim with a source id or mark it `[inferred]`, post heartbeats, and sync with `python3 tools/od.py sync -m "..."`. Never commit `.env` or other secrets.

## Useful commands
```
python3 tools/od.py status
python3 tools/jev_nav.py status
python3 tools/jev_nav.py find "how many steps should a color ramp have"
python3 tools/jev_nav.py check
```
`jev_nav.py find` uses TypeSafe's Jev model when `JEV_API_KEY` is set (environment or a local, git-ignored `.env`); otherwise it falls back to keyword search.
