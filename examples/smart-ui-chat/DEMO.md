# Smart UI demo: under five minutes

A travel assistant whose answers show as interface built from its own design system, then from a second system, with no change to the answers.

## 1. Open it (1 minute)
From the repository root:
```bash
python3 -m http.server 8000 --bind 127.0.0.1
```
Open http://127.0.0.1:8000/examples/smart-ui-chat/ (browsers block the page's modules on `file://`, so it needs the small server).

## 2. Play it (2 minutes)
1. The first answer is a list of flights. Under it: "Checked before it showed: no errors."
2. Press **Compare the fares on the 08:40**, then **Choose** on Standard. A booking prompt appears. Nothing is booked yet.
3. Press **Book for €212**. The button shows it is working, then a receipt appears.
4. Press **When does check-in open?** The answer is a sentence and nothing else: a short fact stays text.
5. Press **Send a broken answer**. Nothing is drawn. The list shows what the validator sent back for the model to fix: an unknown property, an image from an outside site, HTML in the text, and a style key.

## 3. Swap the system (1 minute)
- **System** menu: pick Devtool Dense, then Consumer Playful. The same answers redraw in the other system's colours, type, spacing and corners. Nothing in the answers changed.
- **Dark**: the same answers in dark mode.
- **Text only**: what a host that shows no interface gets.

## 4. Check it yourself (1 minute)
```bash
python3 examples/smart-ui-chat/check_demo.py
```
It plays every step above in two systems at 1440 and 375 px, fails on any console error, any answer that didn't pass its checks, or a broken answer that drew anything, and saves screenshots in `examples/smart-ui-chat/shots/`.

## What is real and what isn't
- **Real:** the validator, the renderer, the catalog (`opendesigner/smart-ui/`, made by `smartui.py catalog` from this folder's own system), and the travel system itself (made by the OpenDesigner engine).
- **Recorded:** the assistant. The answers in `turns.json` were written by hand, so the demo needs no model or API key. A live assistant sends the same kind of messages; the evals in `evals/smart-ui/` measure how Claude and Gemini do.
- **Invented:** Orvell Travel, the people, the flights and the hotel.
