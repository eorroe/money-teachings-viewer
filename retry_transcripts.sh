#!/bin/bash
BASE_DIR="/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_90978114-17d8-479d-a0ec-f20352980e17"
PLAYLIST_FILE="$BASE_DIR/playlist-info.txt"
TRANS_DIR="$BASE_DIR/transcripts"
YTDLP="./yt-dlp"

mkdir -p "$TRANS_DIR"

# Missing IDs from first run
MISSING_IDS="3e7OxgPhxJg KPeslt6FvxI MVOb0l-lvk8 NtsvgxoS9do QlntPA3gA5U Tyjgg4gl4h4 UY4fdi72o2g WnRZi4e9XOM XlHBEwZOjJo fcAQ-zFXGXc h-X3h9L4gU8 hl2bjK8M5zw kLIQDt-066I lhkND-5yXio uDfu_yKEcLA uZ34hZGkYbc wGBI9GeUXds wkeACs3xXR0 xv8qaYubDw4"

while IFS= read -r line; do
    url="${line#*|||}"
    url="${url%%|||*}"
    title="${line%%|||*}"
    vid="${url##*v=}"
    
    # Check if this ID is in the missing list
    if ! echo "$MISSING_IDS" | grep -qw "$vid"; then
        continue
    fi
    
    echo "Retrying transcript for: $title"
    "$YTDLP" --skip-download --write-sub --write-auto-sub --sub-lang en --sub-format json3 --no-check-certificate --extractor-args "youtube:player_client=android" -o "$TRANS_DIR/%(title)s [%(id)s].%(ext)s" "$url"
    sleep 10
done < "$PLAYLIST_FILE"

echo "Retry complete"
