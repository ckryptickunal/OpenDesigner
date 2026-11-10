import json, subprocess, re, difflib
lines = dict(json.load(open("audio/lines.json")))
norm = lambda s: re.sub(r"[^a-z0-9 ]", "", s.lower().replace("-", " ")).split()
bad = 0
for vid, text in lines.items():
    subprocess.run(["npx","hyperframes","transcribe",f"audio/{vid}.wav","--json"],capture_output=True)
    d = json.load(open("audio/transcript.json")); w = d if isinstance(d, list) else d.get("words", d)
    heard = " ".join(x["text"] for x in w)
    r = difflib.SequenceMatcher(None, norm(text), norm(heard)).ratio()
    flag = "OK " if r > 0.8 else "BAD"; bad += r <= 0.8
    print(flag, vid, round(r,2), "|", heard)
print("lines below 0.8 match:", bad)
