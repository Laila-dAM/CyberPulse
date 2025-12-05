#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
INTERFACE=$(ip route | grep '^default' | awk '{print $5}')
BYTES_RX=$(cat /sys/class/net/$INTERFACE/statistics/rx_bytes)
BYTES_TX=$(cat /sys/class/net/$INTERFACE/statistics/tx_bytes)
PACKETS_RX=$(cat /sys/class/net/$INTERFACE/statistics/rx_packets)
PACKETS_TX=$(cat /sys/class/net/$INTERFACE/statistics/tx_packets)

NETWORK_JSON=$(jq -n \
    --arg ts "$TIMESTAMP" \
    --arg iface "$INTERFACE" \
    --arg rx_bytes "$BYTES_RX" \
    --arg tx_bytes "$BYTES_TX" \
    --arg rx_packets "$PACKETS_RX" \
    --arg tx_packets "$PACKETS_TX" \
    '{timestamp: $ts, interface: $iface, rx_bytes: ($rx_bytes|tonumber), tx_bytes: ($tx_bytes|tonumber), rx_packets: ($rx_packets|tonumber), tx_packets: ($tx_packets|tonumber)}'
)

echo "$NETWORK_JSON" > /tmp/cyberpulse_network.json
