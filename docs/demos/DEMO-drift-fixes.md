# Demo: what review now catches, and the owner's words

About five minutes, from a clean scratch folder. Run the commands from the repository's top folder. Nothing in this repository changes.

## 0. A clean scratch folder and a page with the mistakes a second model made

```bash
export DEMO="$(mktemp -d)" HOME="$(mktemp -d)" && export OD_HOME="$HOME/.opendesigner" XDG_CONFIG_HOME="$HOME/.config" GIT_CONFIG_GLOBAL=/dev/null
```

```bash
export E="$PWD/skills/opendesigner/scripts/engine.py" && mkdir "$DEMO/app" && cp -R examples/devtool-dense "$DEMO/app/opendesigner" && cd "$DEMO/app" && mv opendesigner/DESIGN.md opendesigner/PRODUCT.md .
```

```bash
printf '<style>\n.t{color:var(--ds-color-text-fg-primary)}\n.b{font-family:"Inter",sans-serif}\n.h{font-weight:800}\n.k{padding:13px} /* od-ignore: the print grid needs it */\n</style>\n' > page.html
```

The page uses a token name that does not exist, a typed font stack, a weight the system does not have, and an `od-ignore` the agent wrote itself.

## 1. Review

```bash
python3 "$E" review --project . | head -20
```

You should see:
- one use of a token name that does not exist, with the nearest real name (`var(--ds-color-text-primary)`);
- the font stack and the weight under hard-coded values;
- "1 od-ignore line the owner has not approved", and how to ask.

Before this change, review found nothing in this page.

## 2. The owner approves the exception

```bash
python3 "$E" keep "the print grid needs it"; python3 "$E" keep "the print grid needs it" --quote "yes, keep that one"
```

The first is refused: only the owner's words approve it. After the second, review no longer counts the line as open, and DESIGN.md lists it under waivers.

## 3. Hand-off and the commit check take the owner's words

```bash
python3 "$E" handoff yes; python3 "$E" handoff yes --quote "yes, write the note"
```

The first writes nothing and says why; the second writes AGENTS.md and CLAUDE.md. `guard install` works the same way.

## 4. The session-start hook

```bash
python3 -B "$E" --dir opendesigner status --hook
```

One wait per line, no log question (the sketch is done), the full path of `rules.md`, and the build loop: a ledger round, `engine.py review`, `opendesigner-review` and screenshots.

## 5. For Agents in DESIGN.md

```bash
python3 "$E" design-md >/dev/null && sed -n '/^## For Agents/,$p' DESIGN.md | grep -E "Every build|Plain CSS|text-fg-primary"
```

Each Tailwind class sits beside its plain CSS name, with the note that classes need a Tailwind build.
