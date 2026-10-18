# Feedback

Gaps, bugs, confusing steps and ideas found while using OpenDesigner. Each entry has a ready-to-file issue link. Nothing is posted unless you open the link and submit it yourself.

## F-001 · 2026-10-14 · bug
engine.py review flags CSS mask gradients ('mask: linear-gradient(90deg, transparent, #000 14%)') as hard-coded colours and suggests var(--ds-color-text-on-action). A mask's black is alpha, not a colour.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bbug%5D%20engine.py%20review%20flags%20CSS%20mask%20gradients%20%28%27mask%3A%20linear-gradient%2890de...&body=%2A%2AKind%3A%2A%2A%20bug%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0Aengine.py%20review%20flags%20CSS%20mask%20gradients%20%28%27mask%3A%20linear-gradient%2890deg%2C%20transparent%2C%20%23000%2014%25%29%27%29%20as%20hard-coded%20colours%20and%20suggests%20var%28--ds-color-text-on-action%29.%20A%20mask%27s%20black%20is%20alpha%2C%20not%20a%20colour.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=bug%2Cfrom-engine)

## F-002 · 2026-10-14 · gap
Photos are now allowed (Unsplash, hotlinked) but nothing in OpenDesigner helps source them: no licence check (search results mix free and Unsplash+ photos), no credit line, no check for real brand names in the background (this photo had a legible business sign behind a fence that I had to blur). opendesigner-illustrate covers open-licence SVG only.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20Photos%20are%20now%20allowed%20%28Unsplash%2C%20hotlinked%29%20but%20nothing%20in%20OpenDesign...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0APhotos%20are%20now%20allowed%20%28Unsplash%2C%20hotlinked%29%20but%20nothing%20in%20OpenDesigner%20helps%20source%20them%3A%20no%20licence%20check%20%28search%20results%20mix%20free%20and%20Unsplash%2B%20photos%29%2C%20no%20credit%20line%2C%20no%20check%20for%20real%20brand%20names%20in%20the%20background%20%28this%20photo%20had%20a%20legible%20business%20sign%20behind%20a%20fence%20that%20I%20had%20to%20blur%29.%20opendesigner-illustrate%20covers%20open-licence%20SVG%20only.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)
