#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
RAM=$(free -m | awk 'NR==2{printf "%.0f", $3*1024*1024}')
DISK=$(df -h / | awk 'NR==2 {print $3}')
NETWORK=$(cat /proc/net/dev | awk '/eth0/ {print $2}')
TEMP=$(sensors | awk '/Package id 0:/ {print $4}' | tr -d '+°C')
LOGS=$(tail -n 50 /var/log/syslog | base64)

METRIC_JSON=$(jq -n \
    --arg ts "$TIMESTAMP" \
    --arg cpu "$CPU" \
    --arg ram "$RAM" \
    --arg disk "$DISK" \
    --arg network "$NETWORK" \
    --arg temp "$TEMP" \
    --arg logs "$LOGS" \
    '{timestamp: $ts, cpu: $cpu|tonumber, ram: $ram|tonumber, disk: $disk, network: $network|tonumber, temperature: $temp, logs: $logs}'
)

echo "$METRIC_JSON" > /tmp/cyberpulse_metrics.json
