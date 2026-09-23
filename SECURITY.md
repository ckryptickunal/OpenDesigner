# Security policy

## Reporting a vulnerability

Please report security problems privately, not in a public issue.

1. Open the repository's **Security** tab.
2. Click **Report a vulnerability** (GitHub private vulnerability reporting).
3. Describe the problem, the affected files or versions, and how to reproduce it.

Only maintainers can see these reports. You should get a first reply within 7 days. We will agree a fix and a disclosure date with you, and credit you in the advisory unless you prefer not to be named.

## What counts

- Anything in `skills/` that could run unexpected code, read files outside the person's project, or make network calls (skills are meant to be offline and standard-library only).
- Prompt-injection paths: a reference file, URL or design file that could make a skill ignore its rules, leak data or write outside `./opendesigner/`.
- Workflow or CI configuration that could leak secrets or let untrusted pull requests run with write access.
- Committed secrets (API keys, tokens) anywhere in the repository or its history.

Design disagreements, wrong research values and accessibility bugs are not security issues. Use the normal issue forms for those.

## Secrets must never be committed

- `.env`, `.env.*`, `*.pem` and `*.key` are git-ignored. Keep keys in a local `.env` or your shell environment only.
- `tools/jev_nav.py find` reads `JEV_API_KEY` from the environment or a local `.env`. Nothing else in the repository needs a key.
- If you commit a secret by mistake: revoke or rotate it first, then report it privately as above. Deleting the file in a later commit does not remove it from git history.

## Supported versions

OpenDesigner has not had a tagged release yet. Security fixes land on `main`.
