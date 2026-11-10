# Extractor test: three tools on one site

The scripts behind `research/L17-how-systems-get-made.md` Part F2b (issue #11). They score extractors against two references:

- **What the page renders.** `truth.js` records the computed colours, font sizes, spacing (padding, margin, gap), radii and box shadows of every visible element.
- **The published tokens.** `key.py` resolves the design system's published CSS variables to px and hex.

Results for primer.style on 2026-11-10: `scores-primer-2026-11-10.json`.

## Rerun

Everything goes in one work folder (`$W` below), outside the repo. Run the tools one at a time; each opens one headless Chrome. You need Python 3.10+, Playwright for Python (it uses the installed Chrome, `channel="chrome"`), Node 18+, and network access to the site.

1. **Answer key.** Download the published CSS into `$W/out/key/`, keeping its folders. For Primer, these files from `https://cdn.jsdelivr.net/npm/@primer/primitives@11.10.0/dist/css/`: `base/size/size.css`, `base/typography/typography.css`, `functional/size/border.css`, `functional/size/radius.css`, `functional/size/size.css`, `functional/spacing/space.css`, `functional/themes/light.css` and `functional/typography/typography.css`. Then run:
   `python3 key.py $W/out/key $W/out/key/answer.json`
2. **What the page renders.** `python3 capture.py <url> truth.js $W/out/truth/rendered.json`. Add a colour as a fourth argument (for example `'#0377ff'`) to count the `:focus` rules that resolve to it and how many match an element on the page (issue #110).
3. **OpenDesigner.**
   - `python3 capture.py <url> ../../skills/opendesigner-extract/scripts/read_page.js $W/out/ours/page.json`
   - `python3 ../../skills/opendesigner-extract/scripts/css_scan.py --from-json $W/out/ours/page.json --json > $W/out/ours/scan.json`
4. **Dembrandt** (`npm install --ignore-scripts dembrandt`; its optional `onnxruntime-node`, 283 MB, isn't needed).
   - Start the installed Chrome with `--headless=new --remote-debugging-port=9333 --user-data-dir=<a new empty folder>`.
   - Run `BROWSER_CDP_ENDPOINT=http://127.0.0.1:9333 DEMBRANDT_ENFORCE_ROBOTS=1 DEMBRANDT_NO_HEADED_FALLBACK=1 node <dembrandt>/dist/index.js <url> --browser chromium --json-only > $W/out/dembrandt/tokens.json`.
   - Don't pass `--key`. Without it, nothing is synced to Dembrandt's cloud.
5. **Project Wallace** (`npm install --ignore-scripts @projectwallace/css-analyzer`).
   - Save the page's linked stylesheets and inline `<style>` blocks as one file.
   - Run `node wallace.mjs <css-analyzer>/dist/index.js <that file> $W/out/wallace/values.json`.
6. **Score.** `python3 score.py $W` prints each tool's numbers and writes `$W/out/scores.json`.

## How a value is scored

- **Rendered:** the probe found it on the page. Lengths count within 0.06 px; colours count as the exact hex, with alpha.
- **Found:** the share of the page's rendered token values (rendered and in the key) that the tool reported.
- **Unreadable:** a CSS variable with no fallback has no number, so it doesn't count as reported.
- **Shadows:** compared layer by layer: offset, blur, spread, colour and inset.

Check robots.txt and the site's terms before pointing this at another site. Dembrandt asks for the same.
