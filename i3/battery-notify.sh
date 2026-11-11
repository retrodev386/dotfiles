#!/usr/bin/env bash
# Eye-friendly cyberpunk battery block for i3blocks
BATT=$(acpi -b 2>/dev/null | head -n 1)

# Theme colours
CYAN="#69A9B5"
LAVENDER="#A99BB5"
AMBER="#C2A36B"
PINK="#C75B8F"
DIM="#766C80"

if [ -z "$BATT" ]; then
    printf "BAT N/A\nBAT N/A\n%s\n" "$DIM"
    exit 0
fi

PCT=$(printf '%s\n' "$BATT" |
    grep -o '[0-9]\+%' |
    head -n 1 |
    tr -d '%')

STATUS=$(printf '%s\n' "$BATT" |
    awk -F': ' '{print $2}' |
    awk -F', ' '{print $1}')

TIME=$(printf '%s\n' "$BATT" |
    grep -o '[0-9][0-9]:[0-9][0-9]:[0-9][0-9]' |
    head -n 1)

# Protect comparisons if acpi returns unexpected output
case "$PCT" in
    ''|*[!0-9]*) PCT=0 ;;
esac

case "$STATUS" in
    Charging)
        LABEL="BAT+"
        COLOR="$CYAN"
        ;;
    Full)
        LABEL="FULL"
        COLOR="$CYAN"
        ;;
    "Not charging")
        LABEL="BAT"
        COLOR="$AMBER"
        ;;
    Discharging)
        LABEL="BAT"
        if [ "$PCT" -gt 50 ]; then
            COLOR="$LAVENDER"
        elif [ "$PCT" -gt 20 ]; then
            COLOR="$AMBER"
        else
            COLOR="$PINK"
        fi
        ;;
    *)
        LABEL="BAT"
        COLOR="$DIM"
        ;;
esac

# Convert 04:32:15 to 4:32
if [ -n "$TIME" ]; then
    SHORT_TIME=$(printf '%s\n' "$TIME" |
        sed 's/^0//; s/:[0-9][0-9]$//')
fi

if [ "$STATUS" = "Discharging" ] && [ -n "$SHORT_TIME" ]; then
    FULL_TEXT="$LABEL ${PCT}%  ${SHORT_TIME}"
else
    FULL_TEXT="$LABEL ${PCT}%"
fi

# i3blocks protocol:
# line 1 = full text
# line 2 = short text
# line 3 = colour
printf "%s\n%s\n%s\n" "$FULL_TEXT" "$LABEL ${PCT}%" "$COLOR"
