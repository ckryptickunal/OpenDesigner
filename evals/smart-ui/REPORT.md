# Smart UI evals

Made by `python3 tools/smartui_evals.py --report` from `evals/smart-ui/results/`. The cases: `cases.json` (20 that need a part, 5 that should stay text). The data in them is invented.

## The selector alone (no model)

Run 2026-11-13. Recall at 3 (the expected part is among the three sent to the model): **100.0%**. Held back on text-only questions: **100.0%**.

## Models

| Model | Date | Runs | Picked the right part | Valid first time | Held back on text-only | Over-triggered | Rendered | Floor findings |
|---|---|---|---|---|---|---|---|---|
| claude-sonnet-5-5 | 2026-11-13 | 75 (3 per case) | 80.0% | 98.0% | 100.0% | 0.0% | 48 | 0 |
| gemini-3.1-pro-preview | 2026-11-13 | 75 (3 per case) | 95.0% | 93.0% | 100.0% | 0.0% | 53 | 0 |

### What went wrong: claude-sonnet-5-5

- `bars-spend` run 1: showed text, wanted BarChart, LineChart, DataTable
- `bars-spend` run 2: showed text, wanted BarChart, LineChart, DataTable
- `bars-spend` run 3: showed text, wanted BarChart, LineChart, DataTable
- `donut-categories` run 1: showed text, wanted DonutBreakdown, DataTable, BarChart
- `donut-categories` run 2: showed text, wanted DonutBreakdown, DataTable, BarChart
- `donut-categories` run 3: showed text, wanted DonutBreakdown, DataTable, BarChart
- `receipt-seat` run 1: showed text, wanted Receipt, ProgressStatus
- `receipt-seat` run 2: showed text, wanted Receipt, ProgressStatus
- `receipt-seat` run 3: showed text, wanted Receipt, ProgressStatus
- `error-search` run 1: showed text, wanted ErrorRetry
- `error-search` run 2: showed text, wanted ErrorRetry
- `location-hotel` run 3: invalid: length /0/createSurface/components/0/distance text is 48 characters, the most is 40
- `file-invoice` run 3: showed ApprovalPrompt, wanted FileCard

### What went wrong: gemini-3.1-pro-preview

- `facts-hotel` run 2: invalid: root  one component needs id "root"
- `bars-spend` run 1: invalid: required /0/createSurface/components/0/months/0/forecast forecast is required; required /0/createSurface/components/0/months/1/forecast forecast is required
- `bars-spend` run 2: invalid: required /0/createSurface/components/0/months/0/forecast forecast is required; required /0/createSurface/components/0/months/1/forecast forecast is required
- `bars-spend` run 3: invalid: required /0/createSurface/components/0/budget budget is required
- `donut-categories` run 1: showed text, wanted DonutBreakdown, DataTable, BarChart
- `donut-categories` run 2: showed text, wanted DonutBreakdown, DataTable, BarChart
- `donut-categories` run 3: showed text, wanted DonutBreakdown, DataTable, BarChart

## The live path (examples/smart-ui-support)

A real model routes to the app's read actions, answers, and the answer is validated against the data it got, with one repair round. Cases come from `live-cases.json`: 20 that need a part (some are follow-ups that need the conversation, five are changes that must end in an approval prompt) and 5 that should stay text.

| Run | Model | Date | Runs | Selector recall | Right part | Valid first time | Valid after one repair | Held back (text-only) | Approval shown for changes | Changes the model ran | Rendered | Floor findings |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| live-claude-round1 | claude-sonnet-5-5 | 2026-11-14 | 75 | 60.0% | 68.3% | 75.6% | 100.0% | 100.0% | 100.0% | 0 | 41 | 0 |
| live-claude-round2 | claude-sonnet-5-5 | 2026-11-14 | 75 | 85.0% | 80.0% | 93.9% | 98.0% | 100.0% | 80.0% | 0 | 48 | 0 |
| live-gemini-round1 | gemini-3.1-pro-preview | 2026-11-14 | 75 | 60.0% | 65.0% | 79.5% | 100.0% | 100.0% | 86.7% | 0 | 39 | 0 |
| live-gemini-round2 | gemini-3.1-pro-preview | 2026-11-14 | 75 | 80.0% | 88.3% | 84.9% | 100.0% | 100.0% | 93.3% | 0 | 53 | 0 |

## Earlier rounds of the recorded-data path

| Round | Model | Right part | Valid first time | Held back |
|---|---|---|---|---|
| claude-round1 | claude-sonnet-5-5 | 33.3% | 37.3% | 100.0% |
| claude-round2 | claude-sonnet-5-5 | 80.0% | 98.0% | 100.0% |
| gemini-round1 | gemini-3.1-pro-preview | 95.0% | 93.0% | 100.0% |

## Not measured

- On the recorded-data path, a failed answer is not sent back to the model; the live path does one repair round.
- Round 2 of the live path ran while the billing catalog was regenerated once (optional fields, list item names); later cases used the new one.
- The selector's 100% on the recorded-data cases is on the same cases used to tune it; the live cases were written before its last changes.
- Streaming: every reply is scored whole.
- Copy quality inside the parts, and whether a person would prefer the part to text.
