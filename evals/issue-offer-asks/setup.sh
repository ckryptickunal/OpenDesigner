#!/usr/bin/env bash
# Seed the workspace with a system whose feedback has a repeated problem and an open issue offer (runs before the agent,
# outside its sandbox; needs --scaffold). DESIGN.md and PRODUCT.md sit at the project root, as the engine writes them.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
cp -R "$here/system" ./opendesigner
mv ./opendesigner/DESIGN.md ./opendesigner/PRODUCT.md .
