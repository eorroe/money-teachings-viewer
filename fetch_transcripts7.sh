#!/bin/bash
VIDEOS=(
"tjgqETnLM4Y"
"YobaEOZiP58"
"03OyVEQ_yb8"
"wkeACs3xXR0"
"lhkND-5yXio"
"JfIfLMXz7eU"
"YydySt8hCZg"
"L0IrzwvXwwI"
"L0i41L4AwjU"
"hl2bjK8M5zw"
)

for i in "${!VIDEOS[@]}"; do
  vid="${VIDEOS[$i]}"
  echo "Fetching $vid ($((i+1))/${#VIDEOS[@]})..."
  ./yt-dlp --skip-download --write-sub --write-auto-sub --sub-lang en-orig --sub-format json3 --no-check-certificate --extractor-args "youtube:player_client=android" --sleep-interval 3 --max-sleep-interval 10 "https://www.youtube.com/watch?v=$vid"
  if [ $? -eq 0 ]; then
    echo "Success: $vid"
  else
    echo "Failed: $vid"
  fi
  sleep 5
done
