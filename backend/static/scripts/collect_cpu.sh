#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

CPU_JSON=$(jq -n \
    --arg ts "$TIMESTAMP" \
    --arg cpu "$CPU_USAGE" \
    '{timestamp: $ts, cpu: $cpu|tonumber}'
)

echo "$CPU_JSON" > /tmp/cyberpulse_cpu.json
