# Demo: research the repo does itself

Under five minutes. It shows stakeholder research, the coverage check and the summary page on a small example repo, in a fresh scratch folder that nothing else touches.

1. From a clone of this repo, run:

   ```bash
   sh demos/research/run.sh
   ```

2. Read the output, step by step:
   - **4. Coverage** lists the seven research areas. Platform conventions and accessibility are covered by findings from pages that were opened ([findings.json](findings.json)). Content and voice is missing, and analytics is "not yet" because the product is not live.
   - **5. Who has a say** reads CODEOWNERS, the README, the licence, the logo and one exported issue. Every role starts as "not asked": a file in the repo says a role exists, never what it thinks.
   - **8. Agree and differ** shows product and engineering disagreeing on platforms, each with who said it.
   - **9. Decide** records the agreed accessibility level with `set_by research`. It refuses to settle the platform conflict until the owner's own words are given, then records `set_by chosen` and keeps both views.
3. Open the page it prints at the end (`summary.html`) in a browser. Try it at phone width and in dark mode.

One run's full output is in [example-output.txt](example-output.txt). Screenshots of the page at 1440 and 375 px, before and after its design review, are in [shots/](shots/).

The findings cite four pages opened on 2026-11-13 (Android Developers and W3C) and the owner's line from the sketch. The stakeholders, their names and their answers are invented for the demo.
