#!/bin/bash

SCRIPTS=("collect_cpu.sh" "collect_ram.sh" "collect_disk.sh" "collect_network.sh" "collect_temp.sh" "collect_logs.sh")
OUTPUT_DIR="/tmp/cyberpulse_metrics"
mkdir -p "$OUTPUT_DIR"

for SCRIPT in "${SCRIPTS[@]}"; do
    bash "./$SCRIPT"
    FILE_NAME=$(basename "$SCRIPT" .sh)
    if [ -f "/tmp/cyberpulse_$FILE_NAME.json" ]; then
        mv "/tmp/cyberpulse_$FILE_NAME.json" "$OUTPUT_DIR/$FILE_NAME.json"
    fi
done

METRICS_JSON=$(jq -n \
    --slurpfile cpu "$OUTPUT_DIR/collect_cpu.json" \
    --slurpfile ram "$OUTPUT_DIR/collect_ram.json" \
    --slurpfile disk "$OUTPUT_DIR/collect_disk.json" \
    --slurpfile network "$OUTPUT_DIR/collect_network.json" \
    --slurpfile temp "$OUTPUT_DIR/collect_temp.json" \
    --slurpfile logs "$OUTPUT_DIR/collect_logs.json" \
    '{cpu: $cpu[0], ram: $ram[0], disk: $disk[0], network: $network[0], temperature: $temp[0], logs: $logs[0]}'
)

echo "$METRICS_JSON" > "$OUTPUT_DIR/cyberpulse_master.json"
