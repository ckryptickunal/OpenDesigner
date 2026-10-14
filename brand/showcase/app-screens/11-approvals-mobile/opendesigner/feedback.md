# Feedback

Gaps, bugs, confusing steps and ideas found while using OpenDesigner. Each entry has a ready-to-file issue link. Nothing is posted unless you open the link and submit it yourself.

## F-001 · 2026-10-14 · gap
Still no Apple HIG named type scale: I added overrides.font.size 11/13/15/22/34 by hand; the formula steps 14/20/24/29/35/42 cannot be removed, so validate warns '12 text sizes' for a screen that uses six.

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20Still%20no%20Apple%20HIG%20named%20type%20scale%3A%20I%20added%20overrides.font.size%2011/13...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0AStill%20no%20Apple%20HIG%20named%20type%20scale%3A%20I%20added%20overrides.font.size%2011/13/15/22/34%20by%20hand%3B%20the%20formula%20steps%2014/20/24/29/35/42%20cannot%20be%20removed%2C%20so%20validate%20warns%20%2712%20text%20sizes%27%20for%20a%20screen%20that%20uses%20six.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)

## F-002 · 2026-10-14 · gap
preflight.py has no ios medium (I ran --medium web on a phone screen), and still reports Google Fonts <link> faces as M9 'no @font-face' errors (false positive in the hero and footer).

[File this as an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new?title=%5Bgap%5D%20preflight.py%20has%20no%20ios%20medium%20%28I%20ran%20--medium%20web%20on%20a%20phone%20screen%29%2C...&body=%2A%2AKind%3A%2A%2A%20gap%0A%0A%2A%2AWhat%20happened%20or%20what%20is%20missing%3A%2A%2A%0Apreflight.py%20has%20no%20ios%20medium%20%28I%20ran%20--medium%20web%20on%20a%20phone%20screen%29%2C%20and%20still%20reports%20Google%20Fonts%20%3Clink%3E%20faces%20as%20M9%20%27no%20%40font-face%27%20errors%20%28false%20positive%20in%20the%20hero%20and%20footer%29.%0A%0A%2A%2AEngine%3A%2A%2A%201.0.0%20%28Python%203.10%29%0A%0A_Filed%20from%20%60engine.py%20feedback%60.%20Please%20remove%20anything%20private%20before%20submitting._&labels=gap%2Cfrom-engine)
