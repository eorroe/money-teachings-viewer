#!/bin/bash
VIDEOS=(
"wGBI9GeUXds"
"W2Jvk13OQCM"
"W_ljqClCcPw"
"XMsU4bjCqig"
"XlHBEwZOjJo"
"xv8qaYubDw4"
"h-X3h9L4gU8"
"jMbuhTaS8WE"
"VD6xP7rtCwI"
"SlcdA1llGlM"
)

mkdir -p ./transcripts

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
