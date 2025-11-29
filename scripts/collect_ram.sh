#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
RAM_TOTAL=$(free -m | awk '/Mem:/ {print $2}')
RAM_USED=$(free -m | awk '/Mem:/ {print $3}')
RAM_USAGE_PERCENT=$(awk "BEGIN {printf \"%.2f\", ($RAM_USED/$RAM_TOTAL)*100}")

RAM_JSON=$(jq -n \
    --arg ts "$TIMESTAMP" \
    --arg total "$RAM_TOTAL" \
    --arg used "$RAM_USED" \
    --arg percent "$RAM_USAGE_PERCENT" \
    '{timestamp: $ts, total_mb: ($total|tonumber), used_mb: ($used|tonumber), usage_percent: ($percent|tonumber)}'
)

echo "$RAM_JSON" > /tmp/cyberpulse_ram.json
