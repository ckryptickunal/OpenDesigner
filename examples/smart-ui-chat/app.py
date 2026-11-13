"""Orvell Travel's actions, for the live mode of the Smart UI demo (skills/opendesigner-smart-ui/scripts/live.py).

  python3 skills/opendesigner-smart-ui/scripts/live.py serve --app examples/smart-ui-chat/app.py --port 8000

The data is the demo's invented trip (turns.json). Read actions answer; book_flight and book_transfer change data, so
the model can only offer them as buttons the person confirms. Without a model key the page stays in recorded mode.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
T = json.loads((HERE / "turns.json").read_text())["turns"]
NAME = "Orvell Travel assistant"
CATALOG = HERE / "opendesigner" / "smart-ui" / "catalog.json"
TOKENS = HERE / "opendesigner" / "build" / "css" / "tokens.css"
WEB = HERE
STATIC = {"/devtool-dense/": HERE.parent / "devtool-dense", "/consumer-playful/": HERE.parent / "consumer-playful"}  # the system switch
SUGGESTIONS = [t["user"] for t in T if t.get("user")]
RECORDED = {t["user"]: t for t in T if t.get("user")}

FLIGHTS = T[0]["data"]["flights"]
FARES = {"OV214": [{"name": "Basic", "price": "€164", "bag": "Small bag only", "seat": "Random", "changes": "Not allowed", "refund": "No"},
                   {"name": "Standard", "price": "€212", "bag": "1 checked bag, 23 kg", "seat": "Choose your seat", "changes": "€45 fee", "refund": "No"},
                   {"name": "Flex", "price": "€289", "bag": "1 checked bag, 23 kg", "seat": "Choose your seat", "changes": "Free", "refund": "Up to 2 hours before"}]}


def search_flights(origin="BRS", destination="LIS", date="2026-12-04"):
    """Flights between two airports on a date, with times, duration, stops, airline and price per person."""
    return {"route": f"{origin} to {destination}", "date": date, "flights": FLIGHTS}


def get_fares(flight="OV214"):
    """The fares on one flight with what each includes: bags, seat, changes, refund."""
    return {"flight": flight, "fares": FARES.get(flight, FARES["OV214"])}


def flight_info(flight="OV214"):
    """One flight's details: times, terminal, check-in opening, bag drop."""
    return {"flight": flight, "depart": "08:40", "terminal": "Bristol, main terminal", "checkin_opens": "30 hours before: Wed 3 Dec, 02:40",
            "bag_drop_closes": "40 minutes before departure"}


def get_hotel():
    """The traveller's hotel: name, address, distance from the airport, reception hours."""
    return T[5]["data"]


def transfer_times(date="2026-12-04"):
    """Free airport transfer times after the flight lands, and the price."""
    return T[6]["data"]


def get_booking():
    """The traveller's hotel booking: dates, room, guests, breakfast, reference."""
    return T[7]["data"]


def book_flight(flight, fare):
    """Book a flight on a fare and charge the card on file. Changes data."""
    price = next((f["price"] for f in FARES.get(flight, []) if f["name"].lower() == str(fare).lower()), None)
    return {"booked": {"flight": flight, "fare": fare, "price": price, "reference": "OR-58214"}}


def book_transfer(time):
    """Book the airport transfer at a time and charge €38. Changes data."""
    return {"booked": {"transfer": time, "price": "€38", "reference": "TR-11902"}}


def _a(fn, changes=False, **params):
    return {"description": fn.__doc__.strip(), "changes": changes, "fn": fn, "params": params}


ACTIONS = {
    "search_flights": _a(search_flights, origin="airport code, default BRS", destination="airport code, default LIS", date="YYYY-MM-DD"),
    "get_fares": _a(get_fares, flight="a flight number such as OV214"),
    "flight_info": _a(flight_info, flight="a flight number such as OV214"),
    "get_hotel": _a(get_hotel),
    "transfer_times": _a(transfer_times, date="YYYY-MM-DD"),
    "get_booking": _a(get_booking),
    "book_flight": _a(book_flight, True, flight="flight number", fare="Basic, Standard or Flex"),
    "book_transfer": _a(book_transfer, True, time="a free time such as 13:15"),
}
