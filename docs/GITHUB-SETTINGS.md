# GitHub settings for the public launch

Everything here is for the maintainer to apply. GitHub's search reads the repository name, the About description and the topics, so these are worth getting right. All commands use the [GitHub CLI](https://cli.github.com/) and assume:

```bash
REPO=ckryptickunal/OpenDesigner
```

## Before making the repository public

1. **Revoke the keys that were once committed.** `_coordination/DECISIONS.md` (2026-09-23 18:45 IST) records that `.env` with two API keys was in the first commit. History was rewritten, but the keys must be revoked at their providers, and GitHub Support should be asked to purge the orphaned commit `1ac2ebe`, which GitHub still serves by SHA.
2. **Decide the licenses.** The defaults are MIT for code, skills and data, and CC BY 4.0 for written research and docs (`LICENSE`, `LICENSE-CONTENT`). Change them now if you want something else; it is much harder after outside contributions arrive.
3. **Check for other secrets** once more: `git log -p | grep -iE "api[_-]?key|secret|token" | head`.

## About description (315 characters)

```
Open-source AI design system builder. Load it into Claude, ChatGPT, Codex or Cursor: it interviews you, recommends sourced defaults and writes DTCG design tokens, CSS, Tailwind, Figma variables, DESIGN.md and a decision log, with WCAG 2.2 checks. Built on 352 cited Decision Cards and 25 benchmarked design systems.
```

It leads with the phrase people search for, names the hosts and formats people filter by, and ends with the proof. Update the card count when the research grows (`python3 tools/jev_nav.py check` prints it).

## Topics (20, the maximum)

```
design-system, design-systems, design-tokens, dtcg, design-system-generator, ai-design,
claude, claude-code, claude-skills, agent-skills, codex, chatgpt, mcp, figma,
tailwindcss, shadcn-ui, accessibility, wcag, ui-design, theming
```

## Homepage

Leave it empty until there is a site. A good first site is GitHub Pages serving `docs/` at `https://ckryptickunal.github.io/OpenDesigner/`; once it exists, set it with `gh repo edit "$REPO" --homepage <url>`. Do not point the homepage at the repo itself; it adds nothing.

## Social preview image

Upload `docs/assets/social-preview.png` (1280x640) under **Settings > General > Social preview**. GitHub has no API for this, so it is a manual step. The source is `docs/assets/social-preview.html`; re-render it if the tagline changes.

## Apply description, topics and features

```bash
gh repo edit "$REPO" \
  --description "Open-source AI design system builder. Load it into Claude, ChatGPT, Codex or Cursor: it interviews you, recommends sourced defaults and writes DTCG design tokens, CSS, Tailwind, Figma variables, DESIGN.md and a decision log, with WCAG 2.2 checks. Built on 352 cited Decision Cards and 25 benchmarked design systems." \
  --add-topic design-system,design-systems,design-tokens,dtcg,design-system-generator,ai-design,claude,claude-code,claude-skills,agent-skills,codex,chatgpt,mcp,figma,tailwindcss,shadcn-ui,accessibility,wcag,ui-design,theming \
  --enable-issues --enable-discussions --enable-wiki=false --enable-projects=false \
  --enable-squash-merge --enable-merge-commit=false --enable-rebase-merge=false \
  --delete-branch-on-merge
```

## Security features

```bash
# private vulnerability reporting (SECURITY.md and CODE_OF_CONDUCT.md point people here)
gh api -X PUT "repos/$REPO/private-vulnerability-reporting"

# secret scanning, then push protection (free on public repositories; run after going public)
gh repo edit "$REPO" --enable-secret-scanning
gh repo edit "$REPO" --enable-secret-scanning-push-protection

# Dependabot alerts
gh api -X PUT "repos/$REPO/vulnerability-alerts"
```

## Discussions categories

Enabling Discussions creates GitHub's defaults: Announcements, General, Ideas, Polls, Q&A and Show and tell. The issue forms link to **Q&A** (`/discussions/categories/q-a`) and **Show and tell** (`/discussions/categories/show-and-tell`), so keep those names. GitHub has no API for creating categories; add these two by hand under **Discussions > Categories**:

| Category | Format | Description |
|---|---|---|
| Research | Open-ended discussion | Sources, disagreements between systems, and ideas for new lanes |
| Host support | Open-ended discussion | Running OpenDesigner in a specific AI tool: what works, what does not |

Pin a welcome post in Announcements that links the README quickstart, CONTRIBUTING.md and the good first issues.

## Labels

The full set is in `.github/labels.yml`. To create or update them:

```bash
gh label create "good first issue" --color 7057ff --description "Small, well-scoped, with the files and sources named" --force -R "$REPO"
gh label create "help wanted" --color 008672 --description "Maintainers would welcome a contribution here" --force -R "$REPO"
gh label create "research" --color 1d76db --description "Lanes, Decision Cards, sources and traces" --force -R "$REPO"
gh label create "building-block" --color 0e8a16 --description "The ontology of design-system building blocks" --force -R "$REPO"
gh label create "skill" --color 5319e7 --description "Agent Skills and the interview flow" --force -R "$REPO"
gh label create "engine" --color b60205 --description "engine.py, generation, validation and exports" --force -R "$REPO"
gh label create "host-support" --color fbca04 --description "Making OpenDesigner work in another AI tool" --force -R "$REPO"
gh label create "accessibility" --color 006b75 --description "WCAG, contrast, focus, targets, motion and assistive tech" --force -R "$REPO"
gh label create "design" --color d93f0b --description "Visual templates, previews, examples and artboards" --force -R "$REPO"
gh label create "docs" --color 0075ca --description "README, docs/ and community files" --force -R "$REPO"
gh label create "tokens" --color c5def5 --description "DTCG tokens, naming, modes and exports" --force -R "$REPO"
gh label create "figma" --color f9d0c4 --description "Figma and Paper round trip" --force -R "$REPO"
gh label create "translation" --color bfdadc --description "Translating docs or the interview" --force -R "$REPO"
gh label create "example" --color c2e0c6 --description "Worked example design systems" --force -R "$REPO"
gh label create "ci" --color ededed --description "Workflows, checks and repo tooling" --force -R "$REPO"
gh label create "needs-source" --color e99695 --description "A claim needs a Tier A or B source" --force -R "$REPO"
gh label create "disputed" --color d876e3 --description "Sources disagree; settle with evidence (see GOVERNANCE.md)" --force -R "$REPO"
gh label create "verification" --color fef2c0 --description "Re-check a claim or value against a live source" --force -R "$REPO"
gh label create "bug" --color d73a4a --description "Something does not work as documented" --force -R "$REPO"
gh label create "enhancement" --color a2eeef --description "A new capability or an improvement" --force -R "$REPO"
gh label create "question" --color cc317c --description "A question; Discussions is usually faster" --force -R "$REPO"
gh label create "triage" --color ffffff --description "New; a maintainer has not looked at it yet" --force -R "$REPO"
```

GitHub's default labels (`documentation`, `duplicate`, `invalid`, `wontfix`) can stay alongside these.

## Protect main

After the first green CI run, require it on `main`:

```bash
gh api -X POST "repos/$REPO/rulesets" --input - <<'JSON'
{"name": "main", "target": "branch", "enforcement": "active",
 "conditions": {"ref_name": {"include": ["~DEFAULT_BRANCH"], "exclude": []}},
 "rules": [{"type": "deletion"}, {"type": "non_fast_forward"},
           {"type": "required_status_checks",
            "parameters": {"strict_required_status_checks_policy": false,
                           "required_status_checks": [{"context": "Checks (Python 3.11, no network)"}]}}]}
JSON
```

The coordination tool (`tools/od.py sync`) pushes straight to `main` from maintainer sessions. If that should keep working, add a bypass for the maintainer role in the ruleset, or have sessions open pull requests instead.

## Seed issues

`docs/SEED-ISSUES.md` holds 21 ready issues. Create them after the labels exist.

## Discovery beyond GitHub

GitHub search ranks on name, description, topics and README; Google needs links from other sites; AI assistants read `llms.txt`, the README and `AGENTS.md`. After launch:

- Submit the Claude plugin to the official marketplace (`claude-plugins-official`, by pull request) and list the skill on agentskills.io, once the manifests are in the repo.
- Post a Show and tell with a real before and after, and link the repo from the places people ask "how do I create a design system": design-system communities, the DTCG community group's implementations list, and relevant awesome lists.
- Keep the README answering the literal questions people type (see `docs/FAQ.md`), and keep `llms.txt` current when files move.

## A note on license detection

GitHub detects the license from root files named `LICENSE*`. With both `LICENSE` (MIT) and `LICENSE-CONTENT` (CC BY 4.0) at the root, the sidebar may list both, and the API may report the repository license as "Other". If you want the `license:mit` search filter to match, check the repository page after pushing, and if it shows "Other", move `LICENSE-CONTENT` to `docs/LICENSE-CONTENT` and update the links in `README.md`, `CONTRIBUTING.md` and `docs/FAQ.md`.
