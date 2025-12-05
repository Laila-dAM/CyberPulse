#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
CPU_TEMP=$(sensors | grep 'Package id 0:' | awk '{print $4}' | tr -d '+°C')
GPU_TEMP=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits 2>/dev/null)

TEMP_JSON=$(jq -n \
    --arg ts "$TIMESTAMP" \
    --arg cpu "$CPU_TEMP" \
    --arg gpu "$GPU_TEMP" \
    '{timestamp: $ts, cpu_temperature: ($cpu|tonumber), gpu_temperature: ($gpu|tonumber)}'
)

echo "$TEMP_JSON" > /tmp/cyberpulse_temp.json
