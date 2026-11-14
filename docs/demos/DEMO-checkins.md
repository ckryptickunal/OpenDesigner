# Demo: check-ins, the one-time offer, and the shorter review

About five minutes, from a clean scratch folder. Run the commands from the repository's top folder. Nothing in this repository changes: each command writes only inside `$DEMO` and the scratch home folder.

## 0. A clean scratch folder

```bash
export DEMO="$(mktemp -d)" HOME="$(mktemp -d)" && export OD_HOME="$HOME/.opendesigner" XDG_CONFIG_HOME="$HOME/.config" GIT_CONFIG_GLOBAL=/dev/null
```

```bash
export E="$PWD/skills/opendesigner/scripts/engine.py" REPO="$PWD"
```

A small project: the devtool-dense example as its system, DESIGN.md at the top, and one stylesheet.

```bash
mkdir -p "$DEMO/app/src" && cp -R examples/devtool-dense "$DEMO/app/opendesigner" && cd "$DEMO/app" && mv opendesigner/DESIGN.md opendesigner/PRODUCT.md . && printf '.a{padding:13px;color:#f3f4f6}\n' > src/app.css
```

## 1. The first check-in

```bash
python3 "$E" checkin
```

You see five lines: decisions so far, the ledger, whether DESIGN.md matches, review's count, and one next step. It records the check-in, so the next one counts from here.

## 2. A check-in after five decisions

```bash
for v in 31 32 33 34 35; do python3 "$E" set dials.roundness $v --set-by assumed --why demo | grep -A6 Check-in; done
```

The first four decisions print no check-in. The fifth ends with one, and with a line telling the agent to pass it on in two or three sentences and ask at most one question.

## 3. What the session-start hook prints

```bash
python3 -B "$E" --dir opendesigner status --hook
```

The Now line, then the check-in. The hook scans no code, so it stays fast, and it writes nothing in the project.

## 4. The one-time offer in a project with no design system

```bash
mkdir "$DEMO/plain" && printf 'body{margin:0}\n' > "$DEMO/plain/style.css"
```

```bash
python3 -B "$E" checkin --offer --project "$DEMO/plain"; python3 -B "$E" checkin --offer --project "$DEMO/plain" | wc -c
```

The first run prints one note for the agent. The second prints nothing (0 bytes): the offer is remembered in `$OD_HOME/checkins.json`, never in the project.

## 5. Turning it off

```bash
python3 "$E" checkin --every 10 && python3 "$E" checkin --off && python3 "$E" checkin --offers off
```

`--on` brings check-ins back; `OD_CHECKINS=off` silences everything for one shell.

## 6. The shorter review

```bash
python3 "$E" --dir "$REPO/brand/opendesigner" review --project "$REPO/site" | head -16
```

Review leads with the 10 biggest groups of findings (same value, same fix). `--all` prints every line, as before.
