import json, base64, os, subprocess, sys, urllib.request
key = os.environ["GEMINI_API_KEY"]
model = os.environ.get("TTS_MODEL", "gemini-3.8-flash-tts")
prefix = os.environ.get("TTS_PREFIX", "")
voice = sys.argv[1] if len(sys.argv) > 1 else "Charon"
only = sys.argv[2:]  # optional ids
style = ("Read this as the narrator of a premium product film: calm, confident and warm, "
         "unhurried but crisp, with a slight smile. No dramatic pauses. Line: ")
for vid, text in json.load(open("audio/lines.json")):
    if only and vid not in only: continue
    body = {"contents": [{"parts": [{"text": prefix + text}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
              "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}}}}
    req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}",
        data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    d = json.load(urllib.request.urlopen(req, timeout=120))
    part = d["candidates"][0]["content"]["parts"][0]["inlineData"]
    blob = base64.b64decode(part["data"])
    mime = part.get("mimeType", "")
    # The API may return a whole WAV file (header plus trailing metadata), not raw PCM.
    # Decoding a container as raw samples plays its metadata as a burst of white noise.
    if blob[:4] == b"RIFF" or "wav" in mime:
        raw = f"audio/{vid}.src.wav"; open(raw, "wb").write(blob); src = ["-i", raw]
    else:
        rate = int(mime.split("rate=")[1].split(";")[0]) if "rate=" in mime else 24000
        raw = f"audio/{vid}.pcm"; open(raw, "wb").write(blob); src = ["-f", "s16le", "-ar", str(rate), "-ac", "1", "-i", raw]
    # trim leading/trailing silence, normalise loudness
    subprocess.run(["ffmpeg","-v","error","-y",*src,
        "-af","silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,loudnorm=I=-16:TP=-1.5",
        "-ar","48000",f"audio/{os.environ.get('TTS_TAG','')}{vid}.wav"], check=True)
    os.remove(raw)
    dur = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"audio/{os.environ.get('TTS_TAG','')}{vid}.wav"],capture_output=True,text=True).stdout.strip()
    print(vid, dur)
