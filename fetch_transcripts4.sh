#!/bin/bash
VIDEOS=(
"_2em2pshIgM"
"WnRZi4e9XOM"
"UD_q7h-m3tM"
"Fmfo20WhBnQ"
"KCMSmQUJmhw"
"wbW_tl9NgUc"
"w-hKAi0WABw"
"DEGFdgo2Ojs"
"6e8ZCARXQ1I"
"uZ34hZGkYbc"
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
