#!/bin/bash
VIDEOS=(
"u3MxJW0k_wU"
"uDfu_yKEcLA"
"3e7OxgPhxJg"
"MAVD06YakZ4"
"Z-M9SLVL6Cc"
"WAC4hMAb_0s"
"W4_kxlRzdMc"
"0mzpmx2eCHQ"
"X6WhjVND0RQ"
"6ixipm18cs4"
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
