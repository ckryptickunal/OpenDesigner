# Feedback

Gaps, bugs, confusing steps and ideas found while using OpenDesigner. Each entry has a ready-to-file issue link. Nothing is posted unless you open the link and submit it yourself.

## F-001 · 2026-10-14 · bug
engine.py review suggests wrong replacements for device geometry: 'border-radius: 46px -> use var(--ds-radius-overlay) (16px)' for a tablet corner, 'padding: 22px' (a bezel) flagged against the rem standard, 'inset 0 0 0 1px' (a hairline) -> 'use var(--ds-elevation-raised)'. It has no way to tell art and device geometry from UI.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bbug%5D%20engine.py%20review%20suggests%20wrong%20replacements%20for%20device%20geometry%3A%20%27bor...&body=%2A%2AKind%3A%2A%2A%20bug%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0Aengine.py%20review%20suggests%20wrong%20replacements%20for%20device%20geometry%3A%20%27border-radius%3A%2046px%20-%3E%20use%20var%28--ds-radius-overlay%29%20%2816px%29%27%20for%20a%20tablet%20corner%2C%20%27padding%3A%2022px%27%20%28a%20bezel%29%20flagged%20against%20the%20rem%20standard%2C%20%27inset%200%200%200%201px%27%20%28a%20hairline%29%20-%3E%20%27use%20var%28--ds-elevation-raised%29%27.%20It%20has%20no%20way%20to%20tell%20art%20and%20device%20geometry%20from%20UI.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=bug%2Cfrom-engine)
