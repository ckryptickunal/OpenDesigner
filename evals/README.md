# Evals

How OpenDesigner tests itself. The results are published on the site at [/docs/evals/](https://opendesigner.dev/docs/evals/), built from the `latest.json` files below, so the page shows the last real run with its date and commit.

| Kind | What it tests | Run it | Cost | Results |
|---|---|---|---|---|
| Agent evals | An AI agent does a small task with OpenDesigner loaded and without it (`claude plugin eval`). Checks score the files it wrote and what it said | `python3 tools/agent_evals.py` | Real model usage on your account (the last full run is on the site) | `evals/agent/latest.json` |
| Design evals | The engine builds a system from each brief in `design/briefs.json`, twice. No AI | `python3 tools/design_evals.py` | Free, about 2 minutes | `evals/design/latest.json` |
| Agent evals on Gemini | The same cases and graders, run by a Gemini model through `tools/gemini_evals.py` (its own small agent loop with the same tools), so OpenDesigner is tested outside Claude. `drift` and `measure` give the model a finished example system and three build tasks, then measure the pages with `engine.py review` and the review skill's probe | `python3 tools/gemini_evals.py --runs 3 --save` | Gemini API usage on the key in `.env` (a ceiling per run, `--max-cost-usd`); the llm graders use Haiku, as the Claude runs do | `evals/agent/results/<date>-gemini-*.json` |
| Checker evals | Our checkers (layout, preflight, review, dates, names) on pages with planted mistakes and on clean pages | `python3 tools/checker_evals.py` | Free | `evals/checkers/latest.json` |

The CI workflow (`.github/workflows/ci.yml`) is set up to run the design evals on every push and pull request (`--check --no-save`), but GitHub has no runs of it recorded yet (`docs/FIELD-PLAN.md`), so run them yourself before a merge. The agent evals are not in CI. They cost model usage and need a credential, so a maintainer runs them and commits the summary with `--save`.

## Agent eval cases

Each folder here with a `prompt.md` is one case:
- **`prompt.md`**: the task in the person's words, with frontmatter for `description`, `tags`, `max_turns`, `timeout_seconds` and `allowed_tools`.
- **`graders/`**: one file per check. Prefer the free, exact graders: `regex` on the reply or on a file the agent wrote, `file_exists`, and `tool_used` (with `arm: with-only` for "used the OpenDesigner skill", which can't pass without the plugin). Use an `llm` grader only for a rule that needs judgment, and keep it short and specific.
- **`case.yaml`** (optional): `context.add_dirs` for read-only fixtures such as a page to review or an existing system.

`claude plugin eval` refuses a plugin folder with more than 20,000 entries, and this repo is bigger than that. So `tools/agent_evals.py` first copies the plugin as a person installs it (the manifest, `skills/` and `hooks/`), plus these cases, into `dist/eval-plugin/`, and runs there. Raw runs and the HTML report stay in `dist/eval-plugin/evals/results/`. They are git-ignored.

To add a case:
1. Copy the closest folder and write the new prompt the way a real person would ask.
2. Write graders that would fail on a plausible wrong answer. A check that always passes measures nothing.
3. Run it once with each arm: `python3 tools/agent_evals.py --case '<name>' --runs 1`. To run several, give a comma list (`--case 'export*,extend*'` or `--tag smoke,guardrail`), and add `--list` first to see which cases match without spending anything. A filter that matches nothing stops with the list of cases instead of reporting a score of 0.
4. Read the report. If a grader failed on a good answer, fix the grader, not the prompt.
5. Open a pull request with the case. A maintainer runs the full suite.

## Rules

- **Report what happened.** A failing check stays on the site until the product improves. Never tune a check until it passes.
- **Pin the models** (`--model`, `--judge-model`) so scores compare over time, and say which you used.
- **Fixtures use invented brands** and `.example` domains.
- **Share results**, including bad ones, with the [eval report](https://github.com/ckryptickunal/OpenDesigner/issues/new?template=eval-result.yml) issue form.

## Gemini runs

`tools/gemini_evals.py` runs the cases above with a Gemini model (default `gemini-3.1-pro-preview`), to see how another model follows the skills. What differs from a Claude run:
- **The harness is ours, not Claude Code.** A small loop gives the model the tools the case allows, shaped like Claude Code's (Read, Glob, Grep, Bash, Write, Edit, Skill, AskUserQuestion), lists the skills the way Claude Code does, and runs the plugin's start-of-session hook. A low score can be the loop's fault, so read the transcript before you blame the skill.
- **Bash runs in a macOS sandbox:** no network, writes only inside the run's folder, no `.env` or other credentials.
- **Only the "with" arm runs** (OpenDesigner loaded). Compare its score with the Claude summary's `score` column, not with the delta.
- **The key** comes from `GEMINI_API_KEY` in `.env` and is never printed or saved. One call at a time, a backoff on 429, and a cost ceiling per run (`--max-cost-usd`, default $20) checked before every call.
- Transcripts stay in `dist/gemini/` (git-ignored). Only the summary is committed.
