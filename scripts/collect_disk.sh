#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
DISK_TOTAL=$(df -m / | awk 'NR==2 {print $2}')
DISK_USED=$(df -m / | awk 'NR==2 {print $3}')
DISK_USAGE_PERCENT=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

DISK_JSON=$(jq -n \
    --arg ts "$TIMESTAMP" \
    --arg total "$DISK_TOTAL" \
    --arg used "$DISK_USED" \
    --arg percent "$DISK_USAGE_PERCENT" \
    '{timestamp: $ts, total_mb: ($total|tonumber), used_mb: ($used|tonumber), usage_percent: ($percent|tonumber)}'
)

echo "$DISK_JSON" > /tmp/cyberpulse_disk.json
