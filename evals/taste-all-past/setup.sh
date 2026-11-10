#!/usr/bin/env bash
# Seed the workspace the way a person gets there: a sketched project, then the taste poll they took, imported with
# taste.py. Both use the engine staged beside this case, so the fixture always matches the skills under test.
# poll.txt is the poll page's own export line; its ratings are screen ids from the taste library, so no images are needed.
# Runs before the agent, outside its sandbox; needs --scaffold.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
scripts="$here/../../skills/opendesigner/scripts"
[ -f "$scripts/engine.py" ] || { echo "setup.sh: no engine at $scripts" >&2; exit 1; }
python3 "$scripts/engine.py" sketch --name "Ledgerline" --audience regular --platforms web --feel calm,minimal >/dev/null
python3 "$scripts/taste.py" import "$here/poll.txt" >/dev/null
