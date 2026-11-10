#!/usr/bin/env bash
# Seed the workspace: a sketched project and the measurements of an invented site (scan.json, css_scan.py --json output),
# so the case needs no network. Uses the engine staged beside this case. Runs before the agent; needs --scaffold.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
scripts="$here/../../skills/opendesigner/scripts"
[ -f "$scripts/engine.py" ] || { echo "setup.sh: no engine at $scripts" >&2; exit 1; }
python3 "$scripts/engine.py" sketch --name "Fieldnotes" --audience regular --platforms web --feel calm,minimal >/dev/null
cp "$here/scan.json" ./scan.json
