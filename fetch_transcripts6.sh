#!/bin/bash
VIDEOS=(
"kLIQDt-066I"
"7zOShRrwf08"
"bp6ew3yFLhM"
"MVOb0l-lvk8"
"KPeslt6FvxI"
"tmwx0cj3mk8"
"UY4fdi72o2g"
"dM5hZs5QOWc"
"ho7PrUY3EeA"
"kX__kP0QUMg"
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
