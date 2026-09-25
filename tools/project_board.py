#!/usr/bin/env python3
"""Read-only project status board from OpenDesigner files. No network or model inference.

Run: python3 tools/project_board.py <project-root> [--out <output.json>]
The default prints JSON to stdout. --out explicitly writes the selected destination.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "skills/opendesigner/references/questions.json"
HOOKS = ROOT / "skills/opendesigner/references/hooks.json"
# The first sketch is the only universal question set; later questions need applicability checks.
SKETCH = {"Q-scope-01", "Q-scope-06", "Q-aud-01", "Q-plat-01", "Q-brand-01", "Q-color-01", "Q-brand-03"}
OUTPUTS = (
    ("design-system", "DESIGN.md"), ("product", "PRODUCT.md"),
    ("component-preview", "opendesigner/preview.html"),
    ("tokens", "opendesigner/tokens"), ("exports", "opendesigner/build"),
)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def value(record):
    return record.get("value") if isinstance(record, dict) else record


def decisions(path):
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    result = []
    for block in re.split(r"(?=^## D-\d+ · )", text, flags=re.M):
        m = re.match(r"## (D-\d+) · (.+)", block)
        if not m:
            continue
        meta = re.search(r"^- set_by: (\S+) · locked: (\S+) · date: (\S+) · supersedes: (\S+) · source_ref: (\S+)", block, re.M)
        reason = re.search(r"^- reason: (.*)$", block, re.M)
        heading = m[2]
        path_key = heading.split(" = ", 1)[0]
        result.append({"id": m[1], "path": path_key, "set_by": meta[1] if meta else None,
                       "supersedes": meta[4] if meta else None,
                       "source_ref": meta[5] if meta else None,
                       "reason": reason[1] if reason else "not recorded"})
    return result


def board(project, questions=None, hooks=None):
    project = Path(project)
    state_path = project / "opendesigner/state.json"
    # Shipped examples keep state at their own root; user projects use opendesigner/.
    if not state_path.is_file():
        state_path = project / "state.json"
    if not state_path.is_file():
        raise ValueError(f"No project state at {state_path}")
    state_dir = state_path.parent
    state = read_json(state_path)
    qs = questions if questions is not None else read_json(QUESTIONS)["questions"]
    hs = hooks if hooks is not None else read_json(HOOKS)["hooks"]
    answers = state.get("answers") or {}
    inputs = []
    for q in qs:
        if q.get("id") == "Q-ref-01":
            continue  # optional reference, not a missing requirement
        qid = q["id"]
        entry = answers.get(qid)
        status = "recorded" if value(entry) is not None else "unrecorded"
        inputs.append({"id": qid, "area": q.get("area"), "prompt": q.get("ask"),
                       "status": status, "phase": "sketch" if qid in SKETCH else "later-or-conditional",
                       "decision": entry.get("decision") if isinstance(entry, dict) else None,
                       "set_by": entry.get("set_by") if isinstance(entry, dict) else None})
    assets = []
    for hook in hs:
        if hook.get("kind") != "asset":
            continue
        hid = hook["id"]
        record = (state.get("hooks") or {}).get(hid) or {}
        status = record.get("status", "pending")
        files = record.get("files") or []
        # A hook saying 'have' is a recorded choice, not proof that a file exists.
        assets.append({"id": hid, "name": hook["name"], "status": status,
                       "files_recorded": files, "file_presence_not_checked": bool(files),
                       "questions": hook.get("questions", [])})
    outputs = []
    for kind, path in OUTPUTS:
        target = project / path
        if state_dir == project and path.startswith("opendesigner/"):
            target = project / path.removeprefix("opendesigner/")
        outputs.append({"kind": kind, "path": str(target.relative_to(project)),
                        "status": "made" if target.is_file() or (target.is_dir() and any(target.iterdir())) else "missing"})
    history = decisions(state_dir / "decisions.md")
    return {"schema": "opendesigner-project-board/1", "project": state.get("name", "Untitled"),
            "source": "local project files; no external verification",
            "inputs": inputs, "assets": assets, "outputs": outputs, "decisions": history,
            "limits": ["An unrecorded question may already be answered in project context or may not apply; it is not automatically missing.",
                       "A recorded asset status is not proof that the referenced file exists.",
                       "No evidence-to-output link is inferred from free-text reasoning."]}


def markdown_board(data):
    """Compact text fallback. Full question and decision details remain in JSON."""
    inputs = data["inputs"]
    rows = [f"# {data['project']}: project status", "", "## Inputs"]
    for status, label in (("recorded", "Recorded answers"), ("unrecorded", "Unrecorded questions (not necessarily missing)")):
        matches = [x for x in inputs if x["status"] == status]
        rows.append(f"- {label}: {len(matches)}")
        if status == "unrecorded":
            rows.extend(f"  - {x['id']}: {x['prompt']}" for x in matches if x["phase"] == "sketch")
    rows += ["", "## Assets"]
    rows.extend(f"- {x['name']}: {x['status']}" for x in data["assets"])
    rows += ["", "## Outputs"]
    rows.extend(f"- {x['kind']}: {x['status']} ({x['path']})" for x in data["outputs"])
    rows += ["", f"## Recorded decisions: {len(data['decisions'])}",
             "See opendesigner/decisions.md for the original choices and reasons.",
             "", "This is a file inventory, not a user-tested design or a causal explanation."]
    return "\n".join(rows) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--out", type=Path, help="write the selected format here instead of stdout")
    parser.add_argument("--markdown", action="store_true", help="print a compact board for text-only hosts")
    args = parser.parse_args()
    data = board(args.project)
    content = markdown_board(data) if args.markdown else json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        args.out.write_text(content, encoding="utf-8")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
