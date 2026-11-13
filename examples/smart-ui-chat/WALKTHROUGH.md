# Smart UI: a live walkthrough

Four parts, about fifteen minutes. Run every command from the repository root. Screenshots are in `walkthrough/`.

## 1. The demo, on two systems

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```
Open http://127.0.0.1:8000/examples/smart-ui-chat/ and follow [DEMO.md](DEMO.md) steps 2 and 3.

| Orvell Travel, its own system | The same answer in Devtool Dense |
|---|---|
| ![Flights in Orvell Travel](walkthrough/1-orvell-flights.jpg) | ![The same flights in Devtool Dense](walkthrough/2-devtool-dense-flights.jpg) |

Points to make:
- The answer is the same JSON in both. Only `tokens.css` changed.
- A booking asks first (![approval](walkthrough/3-approval.jpg)) and the receipt follows only after the person presses it.
- On a phone the parts stack, and the text-only version is there for hosts that show no interface (![phone](walkthrough/4-receipt-phone.jpg)).

## 2. Adding it to an existing project

Make a small stand-in for "your app": a Next.js project with an assistant panel and two API routes.
```bash
P=$(mktemp -d)/acme-trips && mkdir -p $P/app/api/bookings $P/app/api/flights $P/components
echo '{"dependencies": {"next": "15.0.0", "ai": "5.0.0"}}' > $P/package.json
echo 'export async function POST(r) { return Response.json({}) }' > $P/app/api/bookings/route.ts
echo 'export async function GET(r) { return Response.json([]) }' > $P/app/api/flights/route.ts
echo 'export function AssistantPanel() { return null }' > $P/components/AssistantPanel.tsx
```

Give it a design system (the five-question sketch), then let Smart UI read the repo:
```bash
python3 skills/opendesigner/scripts/engine.py --dir $P/opendesigner sketch --name "Acme Trips" --audience regular --platforms web --feel friendly,calm
python3 skills/opendesigner/scripts/engine.py --dir $P/opendesigner pick Q-scope-01 "A travel booking app with an assistant" --set-by assumed --why "walkthrough"
python3 skills/opendesigner/scripts/engine.py --dir $P/opendesigner build
python3 skills/opendesigner-smart-ui/scripts/smartui.py scope --project $P --write
```
It finds Next.js, the Vercel AI SDK, `components/AssistantPanel.tsx`, the POST route that changes data (so it adds an approval, a receipt and an error part for it) and the travel intents. Anything it can't find is listed as "not known".

Confirm the parts and write the catalog:
```bash
cd $P
python3 $OLDPWD/skills/opendesigner-smart-ui/scripts/smartui.py confirm FlightResults,Comparison,ApprovalPrompt,Receipt,ErrorRetry
python3 $OLDPWD/skills/opendesigner-smart-ui/scripts/smartui.py catalog --allow-images images.unsplash.com
python3 $OLDPWD/skills/opendesigner-smart-ui/scripts/smartui.py prompt --for "Flights from Bristol to Lisbon on 4 December"
cd $OLDPWD
```
The prompt holds the rules and only the parts that fit this message. In the app, that text goes into the system prompt before each model call. Section 4 shows how the answer comes back.

## 3. How it works inside

| Piece | File | What to show |
|---|---|---|
| Slot marks | `skills/opendesigner/scripts/slots.py` | `python3 skills/opendesigner/scripts/slots.py show skills/opendesigner/assets/library/components/kpi-strip/component.html`: the parts of a library component that hold data, marked in its HTML |
| Catalog | `smartui.py catalog` | `examples/smart-ui-chat/opendesigner/smart-ui/catalog.json`: A2UI v1.0; looks only from the system's token names; no colour, size or style property exists |
| Selector | `smartui.py prompt --json` | `python3 skills/opendesigner-smart-ui/scripts/smartui.py prompt --catalog examples/smart-ui-chat/opendesigner/smart-ui/catalog.json --for "When does check-in open?" --json`: `"ui": false` |
| Validator | `smartui.py validate`, `od-validate.js` | The broken answer below |
| Renderer | `od-surface.js` | Fills each part's own markup with text only; styling from `tokens.css` alone |

What happens when a model sends something off-system:
```bash
python3 -c "import json;print(json.dumps(json.load(open('examples/smart-ui-chat/turns.json'))['broken']['answer']))" > /tmp/broken.json
python3 skills/opendesigner-smart-ui/scripts/smartui.py validate /tmp/broken.json --catalog examples/smart-ui-chat/opendesigner/smart-ui/catalog.json
python3 skills/opendesigner-smart-ui/scripts/smartui.py validate /tmp/broken.json --catalog examples/smart-ui-chat/opendesigner/smart-ui/catalog.json --a2ui
```
The first lists each rule broken with a fix; the second prints the A2UI error messages that go back to the model. In the browser the same answer draws nothing (![refused](walkthrough/5-refused.jpg)).

The same rules run in Python and JavaScript; 47 shared cases keep them equal:
```bash
python3 skills/opendesigner-smart-ui/scripts/test_smartui.py
```

## 4. Where it fits

**A plain HTML page** (no build): the demo itself. `examples/smart-ui-chat/chat.js` is about 100 lines: it sets `catalog`, calls `process()`, and listens for `od-action` and `od-error`.

**A React app:**
```jsx
import { useEffect, useRef } from "react";
import "./smart-ui/od-surface.js";             // copied from skills/opendesigner-smart-ui/assets/
import catalog from "../opendesigner/smart-ui/catalog.json";

export function Answer({ messages, data, onAction }) {
  const ref = useRef(null);
  useEffect(() => {
    const s = ref.current;
    s.catalog = catalog;
    s.source = data;
    s.reset();
    s.process(messages);
    const h = (e) => onAction(e.detail);
    s.addEventListener("od-action", h);
    return () => s.removeEventListener("od-action", h);
  }, [messages, data]);
  return <od-surface ref={ref} />;
}
```
Load `tokens.css`, `od-surface.css` and `opendesigner/smart-ui/od-components.js` once in the page head.

**Inside Claude or ChatGPT (MCP Apps):** the OpenDesigner MCP server's `show_ui` tool takes the same answer, checks it, and shows it in a `ui://opendesigner/surface` view drawn with the project's tokens. To see the view without a host:
```bash
cd examples/smart-ui-chat
python3 -c "import json;print(json.dumps(json.load(open('turns.json'))['turns'][0]['answer']))" > /tmp/flights.json
python3 ../../skills/opendesigner-smart-ui/scripts/smartui.py view --answer /tmp/flights.json --write /tmp/surface.html && open /tmp/surface.html
cd ../..
python3 server/mcp/test_smartui_view.py
```
The test loads the view in a page that speaks the MCP Apps protocol: initialize, draw the tool result, report its size, and turn a pressed button into a chat message. It has not been tried in Claude Desktop, claude.ai or ChatGPT yet.
