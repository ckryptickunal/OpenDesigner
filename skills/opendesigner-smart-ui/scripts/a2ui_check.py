#!/usr/bin/env python3
"""Check Smart UI's A2UI output against the official A2UI v1.0 JSON Schemas (a host test, run by hand).

  gh api ... or git clone https://github.com/a2ui-project/a2ui, then:
  python3 a2ui_check.py --schemas <a2ui>/specification/v1_0/json --catalog opendesigner/smart-ui/catalog.json [answers...]

Checks: the catalog against catalog_definition.json; every message in each answer (and in the shared validator fixtures
that should pass) against agent_to_renderer.json; the renderer's action and error messages against
renderer_to_agent.json; <od-surface>'s capabilities against renderer_capabilities.json.
Needs the jsonschema and referencing packages, which the skill never installs. Writes nothing.
"""
import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import smartui  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--schemas", required=True)
    ap.add_argument("--catalog", default="opendesigner/smart-ui/catalog.json")
    ap.add_argument("answers", nargs="*")
    a = ap.parse_args(argv)
    try:
        import jsonschema
        from referencing import Registry, Resource
    except ImportError:
        print("Needs jsonschema and referencing (pip install jsonschema). The skill never installs them.")
        return 2
    d = pathlib.Path(a.schemas)
    # Python's re has no \p{XID_*} classes; this stand-in accepts every name Smart UI writes
    xid = "[" + "\\\\p{XID_Start}_][" + "\\\\p{XID_Continue}]*"
    docs = {f.name: json.loads(f.read_text().replace(xid, "[A-Za-z_]" + "\\\\w*"))
            for f in d.glob("*.json")}
    reg = Registry()
    for name, doc in docs.items():
        res = Resource.from_contents(doc)
        reg = reg.with_resource(doc.get("$id", name), res).with_resource(name, res)

    def check(schema_name, inst, label):
        v = jsonschema.Draft202012Validator(docs[schema_name], registry=reg)
        errs = sorted(v.iter_errors(inst), key=lambda e: list(e.path))
        print(f"{'ok  ' if not errs else 'FAIL'} {label}")
        for e in errs[:5]:
            print(f"     {'/'.join(map(str, e.absolute_path)) or '/'}: {e.message[:200]}")
        return not errs

    base = reg

    def run(cat, answers):
        nonlocal reg
        # agent_to_renderer.json checks each component against "catalog.json#/$defs/anyComponent": the catalog in use
        res = Resource.from_contents(cat)
        reg = base.with_resource("https://a2ui.org/specification/v1_0/catalog.json", res).with_resource("catalog.json", res)
        good = check("catalog_definition.json", cat, f"catalog {cat.get('catalogId')}")
        for label, ans in answers:
            for i, m in enumerate(smartui.normalize(ans) or []):
                good &= check("agent_to_renderer.json", m, f"{label} message {i}")
        return good

    cat = json.loads(pathlib.Path(a.catalog).read_text())
    answers = []
    import audit
    for name, comp in cat["components"].items():
        slug = smartui.od(comp).get("slug")
        f = audit.fixture_path(slug) if slug else None
        if f:
            answers.append((f"component {slug}", [{"version": "1.0", "createSurface": {"surfaceId": "s1", "catalogId": cat["catalogId"],
                                                   "components": [{**json.loads(f.read_text()), "id": "root", "component": name}]}}]))
    for f in a.answers:
        ans = smartui.extract_answer(pathlib.Path(f).read_text())
        if ans:
            answers.append((f, ans))
    ok = run(cat, answers)
    test_dir = HERE.parent / "assets/fixtures/validator"
    fx = json.loads((test_dir / "cases.json").read_text())["cases"]
    ok &= run(json.loads((test_dir / "catalog.json").read_text()),
              [(f"fixture {c['name']}", c["answer"]) for c in fx if not c["expect"] and isinstance(c["answer"], list) and not c["opts"].get("partial")])
    action = {"version": "1.0", "action": {"name": "book_flight", "surfaceId": "s1", "sourceComponentId": "root",
                                           "timestamp": "2026-11-13T10:00:00Z", "context": {"flight": "OV 214", "approved": True}}}
    ok &= check("renderer_to_agent.json", action, "od-surface action message")
    err = smartui.validate([{"version": "1.0", "createSurface": {"surfaceId": "s1", "components": [{"id": "root", "component": "Nope"}]}}], cat)["errors"][0]
    ok &= check("renderer_to_agent.json", {"version": "1.0", "error": {k: err[k] for k in ("code", "path", "message", "surfaceId")}}, "validator error message")
    ok &= check("renderer_capabilities.json", {"1.0": {"supportedCatalogIds": [cat["catalogId"]]}}, "od-surface capabilities")
    print("all conform" if ok else "some messages do not conform")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
