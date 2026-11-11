# !bin/sh
# usage: brightness.sh up|down

case "$1" in
    up) brightnessctl set +5% >/dev/null;;
    down) brightnessctl set 5%- >/dev/null;;
esac

cur=$(brightnessctl get)
max=$(brightnessctl max)
pct=$((cur * 100 / max))

notify-send -t 1500 "☀️ Brightness" "${pct}%"
