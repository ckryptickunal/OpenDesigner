# Feedback

Gaps, bugs, confusing steps and ideas found while using OpenDesigner. Each entry has a ready-to-file issue link. Nothing is posted unless you open the link and submit it yourself.

## F-001 · 2026-10-14 · gap
No component tokens for switches, badges, status dots or setting rows (only component.toast exists). The 32x18 switch, 20px badge and 60px setting row are invented by hand, and engine.py review then reports them as hard-coded sizes it cannot tell apart from real token misses.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20No%20component%20tokens%20for%20switches%2C%20badges%2C%20status%20dots%20or%20setting%20rows%20...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0ANo%20component%20tokens%20for%20switches%2C%20badges%2C%20status%20dots%20or%20setting%20rows%20%28only%20component.toast%20exists%29.%20The%2032x18%20switch%2C%2020px%20badge%20and%2060px%20setting%20row%20are%20invented%20by%20hand%2C%20and%20engine.py%20review%20then%20reports%20them%20as%20hard-coded%20sizes%20it%20cannot%20tell%20apart%20from%20real%20token%20misses.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)

## F-002 · 2026-10-14 · bug
Near-black primary next to a plum accent needs color.bg.inverse aliased as the primary by hand (raw.primaryActionColor with a near-black seed produces a mid-tone of its hue). Same bug as recorded in 04-sounding.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bbug%5D%20Near-black%20primary%20next%20to%20a%20plum%20accent%20needs%20color.bg.inverse%20aliase...&body=%2A%2AKind%3A%2A%2A%20bug%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0ANear-black%20primary%20next%20to%20a%20plum%20accent%20needs%20color.bg.inverse%20aliased%20as%20the%20primary%20by%20hand%20%28raw.primaryActionColor%20with%20a%20near-black%20seed%20produces%20a%20mid-tone%20of%20its%20hue%29.%20Same%20bug%20as%20recorded%20in%2004-sounding.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=bug%2Cfrom-engine)
