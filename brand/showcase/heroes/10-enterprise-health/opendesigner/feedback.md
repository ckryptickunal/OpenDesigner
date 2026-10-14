# Feedback

Gaps, bugs, confusing steps and ideas found while using OpenDesigner. Each entry has a ready-to-file issue link. Nothing is posted unless you open the link and submit it yourself.

## F-001 · 2026-10-14 · bug
raw.secondaryColors ['#1F5FD1'] was silently ignored: at colorfulness 40 color.accentCount is 1, so no accent2 ramp was generated and set printed no warning. Setting a secondary color should raise accentCount or say it was dropped.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bbug%5D%20raw.secondaryColors%20%5B%27%231F5FD1%27%5D%20was%20silently%20ignored%3A%20at%20colorfulness%20...&body=%2A%2AKind%3A%2A%2A%20bug%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0Araw.secondaryColors%20%5B%27%231F5FD1%27%5D%20was%20silently%20ignored%3A%20at%20colorfulness%2040%20color.accentCount%20is%201%2C%20so%20no%20accent2%20ramp%20was%20generated%20and%20set%20printed%20no%20warning.%20Setting%20a%20secondary%20color%20should%20raise%20accentCount%20or%20say%20it%20was%20dropped.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=bug%2Cfrom-engine)

## F-002 · 2026-10-14 · confusing
Preflight and the engine disagree on small text: the generated scale's smallest step is 13px (body-sm, label-sm), but preflight.py M8 warns on anything under 14px for web. Dense product fragments (table metadata, chips) also want a 12px caption step the scale doesn't have; I lifted everything to 13px.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bconfusing%5D%20Preflight%20and%20the%20engine%20disagree%20on%20small%20text%3A%20the%20generated%20scale%27s...&body=%2A%2AKind%3A%2A%2A%20confusing%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0APreflight%20and%20the%20engine%20disagree%20on%20small%20text%3A%20the%20generated%20scale%27s%20smallest%20step%20is%2013px%20%28body-sm%2C%20label-sm%29%2C%20but%20preflight.py%20M8%20warns%20on%20anything%20under%2014px%20for%20web.%20Dense%20product%20fragments%20%28table%20metadata%2C%20chips%29%20also%20want%20a%2012px%20caption%20step%20the%20scale%20doesn%27t%20have%3B%20I%20lifted%20everything%20to%2013px.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=confusing%2Cfrom-engine)
