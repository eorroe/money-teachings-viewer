#!/bin/bash
mkdir -p transcripts
videos=(
  "https://www.youtube.com/watch?v=RiAN8TEx7ok"
  "https://www.youtube.com/watch?v=cGOI0G3sJi0"
  "https://www.youtube.com/watch?v=2fTh_oCx4bo"
  "https://www.youtube.com/watch?v=8iZayjBAe6c"
  "https://www.youtube.com/watch?v=J64jUY2zRoA"
  "https://www.youtube.com/watch?v=S0ohBcrcMMk"
  "https://www.youtube.com/watch?v=MIhK6ky9vOQ"
  "https://www.youtube.com/watch?v=tZ6tvHViwdU"
  "https://www.youtube.com/watch?v=xgXrFOMVXdQ"
)
for v in "${videos[@]}"; do
  echo "Downloading transcript for $v"
  ./yt-dlp --skip-download --write-sub --write-auto-sub --sub-lang en --sub-format json3 --no-check-certificate -o "transcripts/%(id)s.%(ext)s" "$v"
done
echo "Done"
