#!/bin/bash
VIDEOS=(
"QlntPA3gA5U"
"xRXpznNzeg0"
"fcAQ-zFXGXc"
"NtsvgxoS9do"
"SOi9SzIZruI"
"u0XdaETDMjg"
"gqRTUYwxmjM"
"bVsINPgyIPc"
"0vhi9YmF6Ss"
"kXvWXv7ePCc"
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
