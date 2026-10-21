#!/usr/bin/env bash
# Seed the workspace with the messy app (runs before the agent, outside its sandbox; needs --scaffold).
set -euo pipefail
cp -R "$(cd "$(dirname "$0")" && pwd)/app/." ./
