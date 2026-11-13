#!/bin/sh
# Stakeholder research, coverage and the summary page, on a small example repo in a fresh scratch folder.
# Nothing outside the scratch folder is touched: HOME, OD_HOME and XDG_CONFIG_HOME point into it, git ignores your config.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
SCRIPTS="$HERE/../../skills/opendesigner/scripts"
T=$(mktemp -d)
export HOME="$T/home" OD_HOME="$T/home" XDG_CONFIG_HOME="$T/home/.config" GIT_CONFIG_GLOBAL=/dev/null
mkdir -p "$HOME" "$T/proj/.github" "$T/proj/brand" "$T/proj/docs"
cd "$T/proj"
# the example repo: who owns what, a README, a licence, a logo, terms (no real company)
printf '* @counterly/eng\n/src/ui/ @counterly/design\n/docs/legal/ @counterly/legal\n' > .github/CODEOWNERS
printf '# Counterly\nStock and prescriptions for small chemist shops.\n## Accessibility\nWe aim for WCAG 2.2 AA.\n## Support\nAsk in the help desk.\n' > README.md
echo '{"name":"counterly","license":"UNLICENSED"}' > package.json
echo '<svg/>' > brand/logo.svg; echo terms > docs/TERMS.md
git init -q . && git -c user.name=Demo -c user.email=demo@demo.example add -A && git -c user.name=Demo -c user.email=demo@demo.example commit -qm init
printf '[{"number":1,"title":"Contrast too low on stock list","labels":[{"name":"a11y"}]}]' > "$T/issues.json"
E() { python3 "$SCRIPTS/engine.py" "$@"; }
P() { python3 "$SCRIPTS/research.py" "$@"; }
step() { printf '\n== %s\n' "$*"; }
step "1. Sketch";              E sketch --name Counterly --audience dense --platforms web,android --feel calm,minimal | tail -1
step "2. Plan the research";   E research plan --brief "pharmacists in small chemist shops, 30 to 55, at a counter all day, on Android tablets" --tools web-search,browser | tail -2
step "3. Save findings";       E research add "$HERE/findings.json" | head -3
step "4. Coverage";            P coverage
step "5. Who has a say";       P stakeholders scan --issues "$T/issues.json"
step "6. Interviews";          P stakeholders interview --role legal --role accessibility | head -12
step "7. Answers";             P stakeholders none marketing --why "no marketing team yet"
P stakeholders answer product 4 --said-by "Head of product" --text "Android tablets first, then the web" --value android,web
P stakeholders answer engineering 2 --said-by "Lead engineer" --text "Android only this year" --value android
P stakeholders answer legal 2 --said-by "Compliance officer" --text "AA, it is in our contract" --value wcag22-aa --how email
P stakeholders answer accessibility 1 --said-by "Accessibility champion" --text "AA is our floor too" --value wcag22-aa
step "8. Agree and differ";    P stakeholders show | grep -A1 '^Conflict\|^Agreed'
step "9. Decide";              P stakeholders decide a11y-level
P stakeholders decide platforms || true
P stakeholders decide platforms --value android --quote "Android first; the web waits until next year"
step "10. Summary page";       P summary
step "11. Build, then review"; E build >/dev/null; E review | grep -i "stakeholder\|research\|Review:" || true
printf '\nOpen it: %s\n' "$T/proj/opendesigner/research/summary.html"
