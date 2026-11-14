#!/usr/bin/env python3
"""Fernhollow: a council service with an assistant, for the Smart UI example. Invented council, people, places and numbers.

  python3 examples/smart-ui-fernhollow/server.py [--port 8020] [--provider gemini|claude-cli|anthropic|recorded]

The API below is what the council's developers already have. Smart UI's scope step reads these routes (`smartui.py scope`),
and the assistant may call the GET ones to answer; the POST ones change something (a payment, a booking, a renewal), so they
only ever become buttons the resident confirms. The chat itself is POST /api/chat, served by the Smart UI reference server
(skills/opendesigner-smart-ui/scripts/live.py). Standard library only; loopback only. Today is 2026-11-14.
"""
import datetime
import functools
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DATA = json.loads((HERE / "data.json").read_text())
TODAY = datetime.date.fromisoformat(DATA["today"])

NAME = "Fernhollow assistant"
CATALOG = HERE / "opendesigner" / "smart-ui" / "catalog.json"
TOKENS = HERE / "opendesigner" / "build" / "css" / "tokens.css"
WEB = HERE / "web"
ACTIONS = {}
SUGGESTIONS = ["Renew my parking permit", "Do I have any fines?", "When is the Hollow Lane office open?",
               "Book an appointment to show my documents", "Where is my application?", "Can I get a visitor permit?"]


def _words(v):
    """Every date the API returns also comes in words (2026-11-30 -> 30 November 2026), so answers can say it the way residents do."""
    if isinstance(v, dict):
        out = {}
        for k, x in v.items():
            out[k] = _words(x)
            if isinstance(x, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", x):
                d = datetime.date.fromisoformat(x)
                out[f"{k}_in_words"] = f"{d.strftime('%A')} {d.day} {d.strftime('%B %Y')}"
        return out
    return [_words(x) for x in v] if isinstance(v, list) else v


def in_words(fn):
    @functools.wraps(fn)
    def run(*a, **kw):
        return _words(fn(*a, **kw))
    return run


class App:
    """A tiny router in the style most Python web apps use. Each route is also an action the assistant knows about."""

    def _route(self, method, path, changes):
        def deco(fn):
            ACTIONS[fn.__name__] = {"description": (fn.__doc__ or "").strip(), "changes": changes, "fn": in_words(fn),
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


def _reg(v):
    return str(v or "").replace(" ", "").upper()


def _office(office):
    key = str(office or "").lower().replace(" office", "").replace(" library desk", "").replace(" community hub", "").strip().replace(" ", "-")
    return next((o for o in DATA["offices"] if o["id"] == key or o["name"].lower() == str(office).lower()), None)


def _application(reference):
    return next((x for x in DATA["applications"] if x["reference"].lower() == str(reference).lower()), None)


def _due(f):
    """What paying a fine today costs: the lower amount while the 14-day discount lasts, else the full amount."""
    if f["status"] != "Unpaid":
        return "Nothing, it is paid"
    return f["discounted_amount"] if TODAY <= datetime.date.fromisoformat(f["discount_until"]) else f["amount"]


def _not_found(what, message, what_to_do):
    return {"error": {"code": "not_found", "what": what, "message": message, "what_to_do": what_to_do}}


# ------------------------------------------------------------------------------------------------ parking permit

@app.get("/api/account/permit")
def get_permit():
    """The signed-in resident's current parking permit: permit number, zone, vehicle registration, start and expiry dates, and the price paid."""
    p = DATA["permit"]
    days = (datetime.date.fromisoformat(p["expires"]) - TODAY).days
    return {"permit": p, "days_left": days, "resident": DATA["resident"]["name"]}


@app.get("/api/account/permit/quote")
def renewal_quote():
    """What renewing the resident's parking permit would cost: the lengths on offer with price and new dates, and what stays the same."""
    return {"renewal": DATA["renewal"], "current_expiry": DATA["permit"]["expires"], "card": DATA["resident"]["card"]}


@app.post("/api/account/permit/renew")
@params(length="12 months or 6 months")
def renew_permit(length="12 months"):
    """Renew the resident's parking permit for 6 or 12 months and charge the card on file. Takes a payment."""
    opt = next((o for o in DATA["renewal"]["options"] if o["length"].split()[0] == str(length).split()[0]), None)
    if not opt:
        return {"error": {"code": "bad_length", "message": f"A permit can be renewed for 6 or 12 months, not {length}."}}
    p = DATA["permit"]
    return {"renewed": {"permit": p["number"], "zone": p["zone"], "vehicle": p["vehicle"], "length": opt["length"],
                        "valid_from": opt["from"], "valid_to": opt["to"], "paid": opt["price"], "card": DATA["resident"]["card"],
                        "reference": "PRM-448213", "receipt_sent_to": "the email address on your account"}}


# ------------------------------------------------------------------------------------------------ fines

@app.get("/api/fines")
@params(vehicle="a vehicle registration such as AB12 CDE (default: the resident's permit vehicle)")
def list_fines(vehicle=""):
    """Every penalty charge notice (parking fine) for one vehicle, newest first: reference, date, place, amount, whether it is paid, and what paying today would cost (the lower amount while the 14-day discount lasts)."""
    reg = _reg(vehicle or DATA["permit"]["vehicle"])
    rows = [{**{k: f[k] for k in ("reference", "date", "location", "amount", "status")}, "to_pay_now": _due(f)}
            for f in DATA["fines"] if _reg(f["vehicle"]) == reg]
    return {"vehicle": vehicle or DATA["permit"]["vehicle"], "fines": rows, "unpaid": sum(1 for f in rows if f["status"] == "Unpaid")}


@app.get("/api/fines/<reference>")
@params(reference="the 10-character reference on the notice, such as FH40018273", vehicle="the vehicle registration on the notice")
def get_fine(reference, vehicle=""):
    """A summary of one penalty charge notice (parking fine), found by its reference and the vehicle registration: what happened, when and where, the amount, the lower amount if paid within 14 days and its last day, and whether it is paid."""
    f = next((x for x in DATA["fines"] if x["reference"].lower() == str(reference).strip().lower()), None)
    if not f or (vehicle and _reg(vehicle) != _reg(f["vehicle"])):
        return _not_found("penalty charge notice", f"We can't find a penalty charge notice {reference}" + (f" for {vehicle}" if vehicle else "") + ".",
                          "Check the reference on the notice: it starts with FH and has 8 numbers. Then check the registration.")
    return {"fine": f, "to_pay_now": _due(f)}


@app.post("/api/fines/<reference>/pay")
@params(reference="the penalty charge notice to pay now with the card on file")
def pay_fine(reference):
    """Pay one unpaid penalty charge notice now with the card on file, at the lower amount while the 14-day discount lasts. Takes a payment."""
    f = next((x for x in DATA["fines"] if x["reference"].lower() == str(reference).strip().lower()), None)
    if not f or f["status"] != "Unpaid":
        return _not_found("unpaid penalty charge notice", f"{reference} is not an unpaid penalty charge notice.", "Ask to see your fines to check the reference.")
    amount = f["discounted_amount"] if TODAY <= datetime.date.fromisoformat(f["discount_until"]) else f["amount"]
    return {"paid": {"notice": f["reference"], "amount": amount, "card": DATA["resident"]["card"], "reference": "PAY-771905",
                     "on": TODAY.isoformat(), "note": "Paying closes the notice. You can no longer challenge it."}}


# ------------------------------------------------------------------------------------------------ appointments

@app.get("/api/offices/<office>/slots")
@params(office="hollow-lane, marsh-road or eastgate", service="what the appointment is for, such as Show documents for a parking permit")
def available_slots(office, service="Show documents for a parking permit"):
    """Free appointment slots this week at one council office for one service: day, date and time of each, or none and the next free day."""
    o = _office(office)
    if not o:
        return _not_found("office", f"There is no office called {office}.", "The offices are Hollow Lane, Marsh Road library desk and Eastgate community hub.")
    if service not in o["services"]:
        return {"office": o["name"], "service": service, "slots": [], "note": f"{o['name']} does not offer {service.lower()}."}
    slots = DATA["slots"].get(o["id"], [])
    week = [TODAY + datetime.timedelta(days=2 + i) for i in range(5)]  # the next working week, Monday to Friday
    out = {"office": o["name"], "address": o["address"], "service": service, "week": "Monday 16 to Friday 20 November",
           "days": [f"{d.strftime('%A')} {d.day} {d.strftime('%B')}" for d in week], "slots": slots}
    if not slots:
        out["next_free"] = DATA["next_free"].get(o["id"], "Not known yet")
    return out


@app.post("/api/appointments")
@params(office="hollow-lane, marsh-road or eastgate", slot="the slot id, such as HL-1116-1000", service="what the appointment is for")
def book_appointment(office, slot, service="Show documents for a parking permit"):
    """Book one free slot at a council office for the resident. Makes a booking; a confirmation email follows."""
    o = _office(office)
    s = next((x for x in DATA["slots"].get(o["id"], []) if x["id"] == slot), None) if o else None
    if not s:
        return _not_found("slot", f"Slot {slot} is not free at {office}.", "Ask for the free times again; someone may have booked it.")
    return {"booked": {"office": o["name"], "address": o["address"], "day": s["day"], "time": s["time"], "service": service,
                       "reference": "APT-30917", "bring": "The paper documents you want to show, and this reference."}}


# ------------------------------------------------------------------------------------------------ applications and documents

@app.get("/api/applications/<reference>")
@params(reference="an application reference such as RP-2026-0418 (the resident has one open)")
def application_status(reference="RP-2026-0418"):
    """Where an application is: its steps (submitted, checked, decision, permit sent) with dates, the current step and what it is waiting for."""
    a = _application(reference)
    if not a:
        return _not_found("application", f"We can't find an application {reference}.", "The reference is on the email we sent when you applied. It starts with RP-.")
    return {"application": {k: a[k] for k in ("reference", "what", "submitted", "current_step", "waiting_for", "steps")}}


@app.get("/api/applications/<reference>/documents")
@params(reference="an application reference such as RP-2026-0418")
def list_documents(reference="RP-2026-0418"):
    """The documents an application needs, which are already uploaded and which are still needed, with examples of what counts and the file types accepted."""
    a = _application(reference)
    if not a:
        return _not_found("application", f"We can't find an application {reference}.", "The reference is on the email we sent when you applied. It starts with RP-.")
    return {"application": a["reference"], "documents": a["documents"], "accepted_files": a["accepted_files"]}


@app.post("/api/applications/<reference>/documents")
@params(reference="the application the document is for", document="which document, such as Vehicle registration document (V5C)",
        file="the file the resident chose on their own device")
def upload_document(reference, document, file=""):
    """Add a document the resident chose on their own device to an application. The assistant may offer this as a button; it never picks or sends a file itself. Changes the application."""
    a = _application(reference)
    if not a:
        return _not_found("application", f"We can't find an application {reference}.", "Check the reference on your email.")
    if not file:
        return {"error": {"code": "no_file", "message": "Choose the file first. It stays on your device until you send it.",
                          "accepted_files": a["accepted_files"]}}
    return {"uploaded": {"application": a["reference"], "document": document, "file": file, "on": TODAY.isoformat(),
                         "next": "We check it within 2 working days, then make a decision."}}


# ------------------------------------------------------------------------------------------------ offices

@app.get("/api/offices")
def list_offices():
    """Every council office with its address, opening hours, whether it is open today, step-free access and hearing loop notes, and any closures."""
    return {"offices": [{k: o[k] for k in ("name", "address", "hours", "open_today", "access", "closures")} for o in DATA["offices"]],
            "today": "Saturday 14 November"}


@app.get("/api/offices/<office>")
@params(office="hollow-lane, marsh-road or eastgate")
def office_details(office):
    """A summary of one council office: address, opening hours, whether it is open today, access (step-free entrance, hearing loop, toilets), closures and phone."""
    o = _office(office)
    if not o:
        return _not_found("office", f"There is no office called {office}.", "The offices are Hollow Lane, Marsh Road library desk and Eastgate community hub.")
    return {"office": {k: v for k, v in o.items() if k != "id"}, "today": "Saturday 14 November"}


# ------------------------------------------------------------------------------------------------ eligibility

@app.get("/api/permits/pricing")
def permit_prices():
    """The kinds of parking permit side by side: who can get each, the price, the electric vehicle and blue badge prices, and how long each lasts."""
    return {"permit_types": DATA["permit_types"]}


@app.get("/api/eligibility")
@params(permit="resident or visitor", zone="the address zone, such as Zone C (default: the resident's zone)",
        vehicle="petrol car, diesel car, electric car, motorcycle, van, van over 3.5 tonnes, lorry or minibus",
        blue_badge="yes or no (default: what the account says)")
def check_eligibility(permit="resident", zone="", vehicle="petrol car", blue_badge=""):
    """A summary of whether someone can get a resident or visitor parking permit, from their address zone and vehicle type, with the rules that decided it and the price."""
    r = DATA["rules"]
    kind = "visitor" if "visit" in str(permit).lower() else "resident"
    zone = zone or DATA["resident"]["zone"]
    zone = zone if zone.lower().startswith("zone") else f"Zone {zone.strip().upper()}"
    badge = (str(blue_badge).lower() in ("yes", "true", "1")) if blue_badge != "" else DATA["resident"]["blue_badge"]
    rule = r[kind]
    reasons, ok = [], True
    if zone not in r["zones"]:
        ok = False
        reasons.append(f"{zone} is outside the permit zones (Zones A to E).")
    else:
        reasons.append(f"{zone} is a permit zone.")
    if str(vehicle).lower() in rule["not_eligible_vehicles"]:
        ok = False
        reasons.append(f"A {vehicle} can't have a {kind} permit.")
    if kind == "resident":
        reasons.append("One resident permit per vehicle, and up to 2 per household. Your household has 1 permit and 1 application.")
        price = rule["blue_badge_price"] if badge else rule["electric_price"] if "electric" in str(vehicle).lower() else rule["price"]
    else:
        reasons.append(f"Up to {rule['days_per_year']} visitor days a year for each household.")
        price = rule["blue_badge_price"] if badge else rule["price"]
    if badge:
        reasons.append("Blue badge holders pay nothing.")
    return {"permit": f"{kind.title()} permit", "zone": zone, "vehicle": vehicle, "eligible": "Yes" if ok else "No",
            "reasons": reasons, "price": price if ok else "Not available"}


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "skills" / "opendesigner-smart-ui" / "scripts"))
    import live
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8020)
    ap.add_argument("--provider", choices=["anthropic", "claude-cli", "gemini", "recorded"])
    a = ap.parse_args()
    live.serve(__file__, a.port, a.provider)
