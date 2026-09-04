#!/bin/bash
BASE_DIR="/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_90978114-17d8-479d-a0ec-f20352980e17"
TRANS_DIR="$BASE_DIR/transcripts"

for f in "$TRANS_DIR"/*.json3; do
    if [ ! -f "$f" ]; then
        continue
    fi
    python3 -c "
import json, sys
with open(sys.argv[1], 'r', encoding='utf-8') as fp:
    data = json.load(fp)
events = data.get('events', [])
lines = []
for event in events:
    segs = event.get('segs', [])
    for seg in segs:
        text = seg.get('utf8', '')
        if text.strip():
            lines.append(text.strip())
print('\n'.join(lines))
" "$f" > "${f%.json3}.txt"
done

echo "Converted transcripts to plain text"
