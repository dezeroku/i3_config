#!/bin/sh

# This script should be added to crontab to run every 5min.
# Use it only if your computer is ACPI compatible and you have acpi installed.

# You can adjust low_battery value to display notification basing on the battery level.
low_battery=20;

percentage=$(acpi -b | awk '{print substr($4,0,2)}')

if [ $percentage -lt $low_battery ] && [ $percentage -ne 10 ]; then
    notify-send "Low battery" "You only got $percentage% left";
fi;
