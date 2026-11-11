#!/bin/bash
i3lock \
  --nofork \
  --image="$HOME/.config/i3/wallpapers/grub-login-halloween-rice.png" \
  --fill \
  --pass-media-keys --pass-volume-keys \
  \
  --clock --indicator \
  --radius=120 --ring-width=8 \
  --ind-pos="x+w/2:y+h/2" \
  \
  --time-str="%H:%M" --date-str="%A, %d %B" \
  --time-pos="x+w/2:y+h/2+14" --date-pos="x+w/2:y+h/2+44" \
  --time-font="Share Tech Mono" --date-font="Share Tech Mono" \
  --time-size=52 --date-size=16 \
  --time-color=f0405cff --date-color=b8bfd8ff \
  \
  --greeter-text="[ retro-ned // locked ]" \
  --greeter-font="Share Tech Mono" --greeter-size=14 \
  --greeter-color=b8bfd8cc \
  --greeter-pos="x+w/2:y+h-80" \
  \
  --inside-color=0b0c1cdd --ring-color=f0405cff \
  --insidever-color=0b0c1cdd --ringver-color=4a64a8ff \
  --insidewrong-color=14172edd --ringwrong-color=f0405cff \
  --line-uses-inside --separator-color=00000000 \
  --keyhl-color=4a64a8ff --bshl-color=b8bfd8ff \
  \
  --verif-text="unlocking" --wrong-text="denied" --noinput-text="empty" \
  --verif-font="Share Tech Mono" --wrong-font="Share Tech Mono" \
  --verif-size=14 --wrong-size=14 \
  --verif-color=b8bfd8ff --wrong-color=f0405cff \
  --verif-pos="x+w/2:y+h/2-30" --wrong-pos="x+w/2:y+h/2-30" \
  \
  --layout-color=b8bfd8ff --layout-font="Share Tech Mono" --layout-size=12 \
  --layout-pos="x+w/2:y+h/2+80" \
  --show-failed-attempts
