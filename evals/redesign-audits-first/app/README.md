# Brindlewick Dispatch

Internal dispatch console for Brindlewick Freight (brindlewick.example). Dispatchers use it all day to track shipments, reassign drivers and handle delays.

## Run it

Open `index.html` in a browser, or:

```
python3 -m http.server 8080
```

## Pages

- `index.html`: dashboard (today's numbers, delayed shipments, activity)
- `shipments.html`: all shipments, with search and status filters
- `settings.html`: account and notification settings

## Notes

- `css/main.css` is the current stylesheet. `css/legacy.css` is from the first version and some pages still need it.
- No build step. Plain HTML, CSS and a little JavaScript.
- Data is hard-coded for now. The API comes later.
