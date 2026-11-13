# Demo: your system as built, adapt from a reference, the ledger and states

Five minutes, from a clean scratch folder. Every command is read-only for this repository: each writes only inside `$DEMO`.

## 0. A clean scratch folder

Run these from the repository's top folder.

```bash
export DEMO="$(mktemp -d)" HOME="$(mktemp -d)" && export OD_HOME="$HOME/.opendesigner" XDG_CONFIG_HOME="$HOME/.config" GIT_CONFIG_GLOBAL=/dev/null
```

```bash
export E="$PWD/skills/opendesigner/scripts/engine.py" REPO="$PWD"
```

## 1. The audit page on this repo's own website (about 5 seconds)

The website is built on the brand system in `brand/opendesigner/`. Copy that system so nothing in the repo changes, then check the site against it.

```bash
cp -R brand/opendesigner "$DEMO/brand" && python3 "$E" audit-page --dir "$DEMO/brand" --project site --out "$DEMO/audit.html" --open
```

What you should see: about 111 files, 2,776 token uses against 3,747 raw values, and about 36 things to decide. Open "What does not match", pick an option on "13 different buttons" and watch the right-hand preview change; the footer shows `OD:fix A-comp-button=system`. Pick "Keep as it is, on purpose" on any other and type a reason: the footer adds an `OD:waive` line.

## 2. Mark the demo figures as deliberate mistakes

```bash
python3 "$E" exempt site/figures --why "demo figures show mistakes on purpose" --dir "$DEMO/brand"
```

```bash
python3 "$E" review --dir "$DEMO/brand" --project site | grep "Left out on purpose"
```

Run step 1 again: the figures are gone from the findings and listed under "Kept on purpose, and the ledger".

## 3. A ledger round

A small project: the devtool-dense example as its system, in `opendesigner/`, with DESIGN.md at the top.

```bash
mkdir "$DEMO/app" && cp -R examples/devtool-dense "$DEMO/app/opendesigner" && cd "$DEMO/app" && mv opendesigner/DESIGN.md opendesigner/PRODUCT.md .
```

```bash
python3 "$E" ledger start "Settings page" --items comp.action.button,A-space-13px,empty-state
```

```bash
python3 "$E" review --strict | tail -1
```

The last line names 3 ledger items neither done nor waived, and the exit code is 1. Then:

```bash
python3 "$E" ledger done comp.action.button && python3 "$E" ledger broke A-space-13px --note "card padding jumped on mobile"
```

```bash
python3 "$E" ledger waive empty-state --why "no empty lists on this page" --by owner --quote "skip it for now"
```

```bash
python3 "$E" ledger close
```

`close` refuses: A-space-13px is broken. `ledger done A-space-13px`, then `ledger close` works, and `DESIGN.md` has an "Audit Ledger" table.

## 4. States: answers that now change tokens

```bash
python3 "$E" pick Q-state-08 skeleton-first --set-by assumed && python3 "$E" build >/dev/null && grep state-skeleton opendesigner/build/css/tokens.css
```

`pick` says "tokens: 6 values change". Open `opendesigner/overview.html#states` to see loading, empty, error and not found drawn with the system's tokens.

## 5. Adapt from a reference

Measure another example's page as the reference, then compare.

```bash
python3 "$REPO/skills/opendesigner-extract/scripts/css_scan.py" "$REPO/examples/consumer-playful/preview.html" --json > "$DEMO/ref.json"
```

```bash
python3 "$E" adapt "$DEMO/ref.json" --open
```

What you should see: your system and the adapted one side by side, a table of what changes (corners, control height, body size), and what stays (brand colour and fonts). Values you chose yourself start unticked. `state.json` is unchanged until you copy the `OD:accept` lines back.
