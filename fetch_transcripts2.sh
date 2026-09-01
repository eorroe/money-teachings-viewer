#!/bin/bash
VIDEOS=(
"S7bXNS2liJI"
"uyAH-lc6IU8"
"FBEV4da-v10"
"h3uVfD2EO-I"
"wlDV8ZT6Jyc"
"PL7CEY3ef3g"
"dq_0oYkl-S8"
"z4tv7GiE88c"
"2BLNa6591LM"
"XmQZc5R1EDo"
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
