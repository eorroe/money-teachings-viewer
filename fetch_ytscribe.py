#!/usr/bin/env python3
import os
import re
from urllib.request import Request, urlopen
from urllib.error import URLError

videos = [
    ("RiAN8TEx7ok", "How to Make Money Without Working - Robert Kiyosaki"),
    ("cGOI0G3sJi0", "How to Find a GOOD Business Partner - Robert Kiyosaki"),
    ("2fTh_oCx4bo", 'Why "A" Students Work For "C" Students - Robert Kiyosaki'),
    ("8iZayjBAe6c", "3 Branding Tips to Get You to the Next Level - Robert Kiyosaki"),
    ("J64jUY2zRoA", "Don't Chase Money, Chase Education - Robert Kiyosaki"),
    ("S0ohBcrcMMk", "The #1 Most Important Skill You NEED To Be SUCCESSFUL - Robert Kiyosaki"),
    ("MIhK6ky9vOQ", "How to Get Rich In The Next Market Crash - Robert Kiyosaki"),
    ("tZ6tvHViwdU", "Learn To Invest Like Robert Kiyosaki - With ZERO Risk"),
    ("xgXrFOMVXdQ", "What Are You Investing For? Cash Flow or Capital Gains? - Robert Kiyosaki"),
]

os.makedirs("transcripts", exist_ok=True)

for vid_id, title in videos:
    url = f"https://ytscribe.com/v/{vid_id}"
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=60) as resp:
            data = resp.read().decode("utf-8", errors="ignore")
        m = re.search(r"Show full transcript</a>", data)
        if not m:
            print(f"NO_TRANSCRIPT_BUTTON: {vid_id}")
            continue
        transcript_text = data[m.start():]
        path = f"transcripts/{vid_id}.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(transcript_text)
        print(f"OK: {vid_id} -> {path}")
    except Exception as e:
        print(f"FAIL: {vid_id} -> {e}")
