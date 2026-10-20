#!/usr/bin/env bash
# Seed the workspace with the case's fixture system (runs before the agent, outside its sandbox; needs --scaffold).
set -euo pipefail
cp -R "$(cd "$(dirname "$0")" && pwd)/system" ./opendesigner
