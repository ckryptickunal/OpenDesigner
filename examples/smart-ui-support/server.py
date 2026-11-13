#!/usr/bin/env python3
"""Tallyhaus: a small billing app with an assistant, for the Smart UI example. Invented product, people and numbers.

  python3 examples/smart-ui-support/server.py [--port 8010] [--provider gemini|claude-cli|anthropic|recorded]

The API below is what a developer already has. Smart UI's scope step reads these routes (`smartui.py scope`), and the
assistant may call the GET ones to answer; the POST ones change data, so they only ever become buttons the person
confirms. The chat itself is POST /api/chat, served by the Smart UI reference server (skills/opendesigner-smart-ui/scripts/live.py).
Standard library only; loopback only.
"""
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DATA = json.loads((HERE / "data.json").read_text())

NAME = "Tallyhaus assistant"
CATALOG = HERE / "opendesigner" / "smart-ui" / "catalog.json"
TOKENS = HERE / "opendesigner" / "build" / "css" / "tokens.css"
WEB = HERE / "web"
ACTIONS = {}
SUGGESTIONS = ["Show my open invoices", "How has our API usage changed this year?", "Compare the plans",
               "What plan are we on?", "Where's the refund for invoice TH-1041?", "When is my next invoice due?"]


class App:
    """A tiny router in the style most Python web apps use. Each route is also an action the assistant knows about."""

    def _route(self, method, path, changes):
        def deco(fn):
            ACTIONS[fn.__name__] = {"description": (fn.__doc__ or "").strip(), "changes": changes, "fn": fn,
                                    "method": method, "path": path,
                                    "params": {k: v for k, v in getattr(fn, "params", {}).items()}}
            return fn
        return deco

    def get(self, path):
        return self._route("GET", path, False)

    def post(self, path):
        return self._route("POST", path, True)


app = App()


def params(**p):
    def deco(fn):
        fn.params = p
        return fn
    return deco


@app.get("/api/invoices")
@params(status="open, paid or all (default all)")
def list_invoices(status="all"):
    """The team's invoices, newest first, with number, date, amount, status and due date."""
    rows = [i for i in DATA["invoices"] if status == "all" or i["status"] == status]
    return {"invoices": rows, "currency": "EUR"}


@app.get("/api/invoices/<number>")
@params(number="an invoice number such as TH-1043")
def get_invoice(number):
    """One invoice with its lines and its PDF file name."""
    inv = next((i for i in DATA["invoices"] if i["number"].lower() == str(number).lower()), None)
    if not inv:
        raise LookupError(f"No invoice {number}")
    return {"invoice": inv}


@app.get("/api/usage")
@params(months="how many recent months, 1 to 12 (default 6)")
def get_usage(months=6):
    """API calls and active seats per month, most recent last."""
    m = max(1, min(12, int(months)))
    return {"usage": DATA["usage"][-m:], "limit_calls": DATA["subscription"]["calls_included"]}


@app.get("/api/plans")
def list_plans():
    """Every plan with its price per seat, included API calls, support level and features."""
    return {"plans": DATA["plans"], "current": DATA["subscription"]["plan"]}


@app.get("/api/subscription")
def get_subscription():
    """What the team is on now: plan, seats, price, renewal date, payment card."""
    return {"subscription": DATA["subscription"]}


@app.get("/api/refunds/<invoice>")
@params(invoice="the invoice number the refund is for")
def refund_status(invoice):
    """Where a refund is: its steps with dates, the amount, and when it should arrive."""
    r = next((x for x in DATA["refunds"] if x["invoice"].lower() == str(invoice).lower()), None)
    if not r:
        raise LookupError(f"No refund for {invoice}")
    return {"refund": r}


@app.post("/api/subscription/plan")
@params(plan="the plan to move to: Starter, Team or Scale")
def change_plan(plan):
    """Move the team to another plan from the next billing date. Changes the subscription."""
    p = next((x for x in DATA["plans"] if x["name"].lower() == str(plan).lower()), None)
    if not p:
        raise LookupError(f"No plan {plan}")
    sub = DATA["subscription"]
    return {"changed": {"from": sub["plan"], "to": p["name"], "seats": sub["seats"], "starts": sub["renews"],
                        "new_monthly": f"€{p['price_per_seat'] * sub['seats']}", "reference": "CH-20871"}}


@app.post("/api/invoices/<number>/pay")
@params(number="the invoice to pay now with the card on file")
def pay_invoice(number):
    """Pay one open invoice now with the card on file. Charges the card."""
    inv = next((i for i in DATA["invoices"] if i["number"].lower() == str(number).lower()), None)
    if not inv or inv["status"] != "open":
        raise LookupError(f"{number} is not an open invoice")
    return {"paid": {"invoice": inv["number"], "amount": inv["amount"], "card": DATA["subscription"]["card"],
                     "reference": "PY-55309", "at": datetime.date(2026, 11, 14).isoformat()}}


@app.post("/api/seats")
@params(add="how many seats to add, 1 to 50")
def add_seats(add):
    """Add seats to the plan now; the extra cost is prorated on the next invoice. Changes the subscription."""
    n = max(1, min(50, int(add)))
    sub = DATA["subscription"]
    p = next(x for x in DATA["plans"] if x["name"] == sub["plan"])
    return {"seats": {"from": sub["seats"], "to": sub["seats"] + n, "extra_monthly": f"€{p['price_per_seat'] * n}", "reference": "ST-30112"}}


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "skills" / "opendesigner-smart-ui" / "scripts"))
    import live
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8010)
    ap.add_argument("--provider", choices=["anthropic", "claude-cli", "gemini", "recorded"])
    a = ap.parse_args()
    live.serve(__file__, a.port, a.provider)
