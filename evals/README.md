# Evals

How OpenDesigner tests itself. The results are published on the site at [/docs/evals/](https://opendesigner.dev/docs/evals/), built from the `latest.json` files below, so the page shows the last real run with its date and commit.

| Kind | What it tests | Run it | Cost | Results |
|---|---|---|---|---|
| Agent evals | An AI agent does a small task with OpenDesigner loaded and without it (`claude plugin eval`). Checks score the files it wrote and what it said | `python3 tools/agent_evals.py` | Real model usage on your account (the last full run is on the site) | `evals/agent/latest.json` |
| Design evals | The engine builds a system from each brief in `design/briefs.json`, twice. No AI | `python3 tools/design_evals.py` | Free, about 2 minutes | `evals/design/latest.json` |
| Checker evals | Our checkers (layout, preflight, review, dates, names) on pages with planted mistakes and on clean pages | `python3 tools/checker_evals.py` | Free | `evals/checkers/latest.json` |

The CI workflow (`.github/workflows/ci.yml`) is set up to run the design evals on every push and pull request (`--check --no-save`), but GitHub has no runs of it recorded yet (`docs/FIELD-PLAN.md`), so run them yourself before a merge. The agent evals are not in CI. They cost model usage and need a credential, so a maintainer runs them and commits the summary with `--save`.

## Agent eval cases

Each folder here with a `prompt.md` is one case:
- **`prompt.md`**: the task in the person's words, with frontmatter for `description`, `tags`, `max_turns`, `timeout_seconds` and `allowed_tools`.
- **`graders/`**: one file per check. Prefer the free, exact graders: `regex` on the reply or on a file the agent wrote, `file_exists`, and `tool_used` (with `arm: with-only` for "used the OpenDesigner skill", which can't pass without the plugin). Use an `llm` grader only for a rule that needs judgment, and keep it short and specific.
- **`case.yaml`** (optional): `context.add_dirs` for read-only fixtures such as a page to review or an existing system.

`claude plugin eval` refuses a plugin folder with more than 20,000 entries, and this repo is bigger than that. So `tools/agent_evals.py` first copies the plugin as a person installs it (the manifest and `skills/`), plus these cases, into `dist/eval-plugin/`, and runs there. Raw runs and the HTML report stay in `dist/eval-plugin/evals/results/`. They are git-ignored.

To add a case:
1. Copy the closest folder and write the new prompt the way a real person would ask.
2. Write graders that would fail on a plausible wrong answer. A check that always passes measures nothing.
3. Run it once with each arm: `python3 tools/agent_evals.py --case '<name>' --runs 1`.
4. Read the report. If a grader failed on a good answer, fix the grader, not the prompt.
5. Open a pull request with the case. A maintainer runs the full suite.

## Rules

- **Report what happened.** A failing check stays on the site until the product improves. Never tune a check until it passes.
- **Pin the models** (`--model`, `--judge-model`) so scores compare over time, and say which you used.
- **Fixtures use invented brands** and `.example` domains.
- **Share results**, including bad ones, with the [eval report](https://github.com/ckryptickunal/OpenDesigner/issues/new?template=eval-result.yml) issue form.
