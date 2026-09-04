#!/bin/bash
BASE_DIR="/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_90978114-17d8-479d-a0ec-f20352980e17"
PLAYLIST_FILE="$BASE_DIR/playlist-info.txt"
TRANS_DIR="$BASE_DIR/transcripts"
YTDLP="./yt-dlp"

mkdir -p "$TRANS_DIR"

count=0
while IFS= read -r line; do
    # Extract URL (middle field between ||| delimiters)
    rest="${line#*|||}"
    url="${rest%%|||*}"
    title="${line%%|||*}"
    
    if [ -z "$url" ] || ! echo "$url" | grep -q "^https://www.youtube.com/watch"; then
        continue
    fi
    count=$((count + 1))
    echo "Downloading transcript for video $count: $title"
    "$YTDLP" --skip-download --write-sub --write-auto-sub --sub-lang en --sub-format json3 --no-check-certificate --extractor-args "youtube:player_client=android" -o "$TRANS_DIR/%(title)s [%(id)s].%(ext)s" "$url"
    sleep 2
done < "$PLAYLIST_FILE"

echo "Downloaded $count transcripts"
