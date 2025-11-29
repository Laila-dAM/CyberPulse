#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
SYS_LOG=$(journalctl -n 50 --no-pager --output=short-iso)
AUTH_LOG=$(journalctl -n 50 -u ssh --no-pager --output=short-iso)
KERNEL_LOG=$(journalctl -n 50 -k --no-pager --output=short-iso)

LOG_JSON=$(jq -n \
    --arg ts "$TIMESTAMP" \
    --argjson sys "$(echo "$SYS_LOG" | jq -R -s -c 'split("\n")[:-1]')" \
    --argjson auth "$(echo "$AUTH_LOG" | jq -R -s -c 'split("\n")[:-1]')" \
    --argjson kernel "$(echo "$KERNEL_LOG" | jq -R -s -c 'split("\n")[:-1]')" \
    '{timestamp: $ts, system_logs: $sys, auth_logs: $auth, kernel_logs: $kernel}'
)

echo "$LOG_JSON" > /tmp/cyberpulse_logs.json
