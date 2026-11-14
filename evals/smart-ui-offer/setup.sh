#!/usr/bin/env bash
# Seed the workspace with the fixture system and a small app that has a support chat (runs before the agent; needs --scaffold).
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
cp -R "$here/system" ./opendesigner
cp -R "$here/app" ./app
