#!/bin/bash
THRESHOLD=20
STATUS=$(acpi -b | grep -o "Discharging\|Charging\|Full")
LEVEL=$(acpi -b | grep -oP '\d+(?=%)')

if [[ "$STATUS" == "Discharging" && "$LEVEL" -le "$THRESHOLD" ]]; then
    dunstify -a "battery-notify" -u critical "Battery Low" "${LEVEL}% remaining"
fi
