# Report receiver (reference)

**In plain words:** a tiny web service that receives the anonymous journey reports people choose to share, checks each one, and stores it without anything that could identify the sender. It is a reference: nothing here is deployed, and hosting is the maintainers' decision.

- **Designers:** where opted-in usage reports would land, so the interview can be improved from real journeys.
- **Engineers:** a Cloudflare Worker (`worker.js`) plus D1, schema-validated POSTs of at most 16 KB, per-address rate limit, no IP or user-agent storage, a weekly 12-month cleanup, and an export-to-report script.

What people agree to, and what is and isn't sent, is in [docs/PRIVACY.md](../../docs/PRIVACY.md). The client side is `skills/opendesigner/scripts/journey.py` (`share`).

## Files
| File | What it does |
|---|---|
| `worker.js` | `POST /v1/reports`: rate limit, size limit (16 KB), JSON parse, schema check, store `{id, received_week, payload}`. A weekly cron deletes rows older than 52 weeks |
| `validate.js` | The same small JSON Schema check as `journey.py validate()` |
| `schema.sql` | The D1 table |
| `wrangler.toml.example` | Bindings: D1 `DB`, rate limiter `RATE_LIMITER` (20 a minute per address), the cron, and Workers Logs off |
| `aggregate_reports.py` | Stored reports into the aggregate journey report |

The schema is not copied: `worker.js` imports `skills/opendesigner/references/report.schema.json`, so the sender and receiver can't drift apart.

## What it keeps, and what it doesn't
- Keeps: the validated report, and the ISO week it arrived (for example `2026-W39`).
- Never stores: the IP address, the user agent, other headers, or the exact time. The IP is only the rate limiter's counter key, which Cloudflare holds for one minute.
- Refuses: anything over 16 KB, anything that isn't JSON, and anything that doesn't match the schema (an extra key, a question id that isn't one, a timing not rounded to 5 seconds, and so on).
- Workers Logs are on by default for new Workers; `wrangler.toml.example` turns them off. Leave Logpush off too.

Why 16 KB and not 8: a run through the sketch and broad levels is about 3 KB, but a full detailed run of all 192 questions measures about 14 KB. `journey.py` drops the per-question timings if a report would go over 16 KB.

## Setting it up (only when the maintainers decide to host it)
```
cd server/telemetry
cp wrangler.toml.example wrangler.toml
npx wrangler d1 create opendesigner-reports            put the database id it prints into wrangler.toml
npx wrangler d1 execute opendesigner-reports --remote --file schema.sql
npx wrangler deploy
```
Then publish the address in docs/PRIVACY.md and set it as the default in `journey.py` (phase B), or have people set `OPENDESIGNER_REPORTS_URL=https://<worker>/v1/reports`. Until then, `journey.py share` keeps reports in each person's `opendesigner/journey/outbox/` and says that nothing was sent.

The rate limiter and cron settings follow the Cloudflare docs checked on 2026-09-24 (the `[[ratelimits]]` period must be 10 or 60 seconds). The JSON import uses `with { type: "json" }`, the form Cloudflare's bundling docs show. The worker was exercised locally with Node 24 and mocked bindings (valid report stored, extra keys, bad ids, unrounded timings, oversize and non-JSON bodies refused, rate limit honored); it has not been run on Cloudflare.

## Turning stored reports into a report
```
npx wrangler d1 execute opendesigner-reports --remote --json --command "SELECT payload FROM reports" > reports.json
python3 server/telemetry/aggregate_reports.py reports.json --out journeys.md
```
The script re-checks every report against the schema, skips and counts any that fail, and counts a repeated report once. The shape of the `--json` export is not documented by Cloudflare [inferred]; the reader accepts either `[{"results": [{"payload": "..."}]}]` or a plain list of rows or reports.

## Retention
Raw reports: 12 months, then deleted by the weekly cron. The aggregate reports made from them hold only counts, rates and averages per question, and are kept.
