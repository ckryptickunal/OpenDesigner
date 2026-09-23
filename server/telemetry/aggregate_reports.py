#!/usr/bin/env python3
"""Turn stored reports into one aggregate journey report (for maintainers).

    npx wrangler d1 execute opendesigner-reports --remote --json --command "SELECT payload FROM reports" > reports.json
    python3 server/telemetry/aggregate_reports.py reports.json --out journeys.md      (or --out journeys.json)

It accepts the D1 export, a list of reports, single report files, or folders of them. Every report is checked
against skills/opendesigner/references/report.schema.json again; any that fail are skipped and counted.
This is `journey.py aggregate` with the report source spelled out. Standard library only.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "skills", "opendesigner", "scripts"))
import journey  # noqa: E402

if __name__ == "__main__":
    sys.exit(journey.main(["aggregate", *sys.argv[1:]]))
