# Demo: OpenDesigner's evals on Gemini

About five minutes, and about $0.10 of Gemini usage. You need macOS (Bash runs in `sandbox-exec`), Python 3.10+, the Claude CLI (for the Haiku judge), and a Gemini API key.

1. Make a clean scratch folder and point the usual config locations into it:
   ```bash
   export SCRATCH="$(mktemp -d)"; export HOME="$SCRATCH" OD_HOME="$SCRATCH/od" XDG_CONFIG_HOME="$SCRATCH/.config" GIT_CONFIG_GLOBAL=/dev/null
   ```
2. Give it a key. Either put `GEMINI_API_KEY=...` in the repo's `.env` (git-ignored), or `export GEMINI_API_KEY=...` in this shell. The runner never prints it.
3. See which cases would run (free):
   ```bash
   python3 tools/gemini_evals.py --list
   ```
4. Run one case once, with a 50-cent ceiling:
   ```bash
   python3 tools/gemini_evals.py --case contrast-floor --runs 1 --label demo --max-cost-usd 0.5
   ```
   You get one line per run, such as `contrast-floor run 1 score 1.00 STOP $0.04`. The transcript, the workspace and `result.json` are in `dist/gemini/runs/demo/contrast-floor/run-1/`.
5. Compare with the committed Claude baseline:
   ```bash
   python3 tools/gemini_evals.py regrade --label demo --compare evals/agent/results/2026-11-13-claude-sonnet-baseline.json
   ```
6. The drift test (about $0.40 and 10 minutes per page) builds a page on a finished example, then measures it. `measure` opens Chrome through the review skill's `capture.py`:
   ```bash
   python3 tools/gemini_evals.py drift --example devtool-dense --task pricing --runs 1 --label demo-drift --max-cost-usd 1
   python3 tools/gemini_evals.py measure --label demo-drift
   ```
   `dist/gemini/drift/demo-drift/devtool-dense/pricing-1/measure.json` holds what `engine.py review`, the static scan and the browser probe each found, and `review/shots/` holds the screenshots.

The offline tests need no key: `python3 tools/test_gemini_evals.py`.
