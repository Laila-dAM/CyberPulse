"""Utilities for parsing collector output into metrics."""

import json
from datetime import datetime, timezone
from typing import Any, Dict

from backend.models.metric import Metric


def parse_cpu_output(output: str) -> float:
    """Parse CPU usage output."""
    try:
        return float(output.strip())
    except ValueError:
        return 0.0


def parse_ram_output(output: str) -> float:
    """Parse RAM usage output."""
    try:
        return float(output.strip())
    except ValueError:
        return 0.0


def parse_disk_output(output: str) -> float:
    """Parse disk usage output."""
    try:
        return float(output.strip())
    except ValueError:
        return 0.0


def parse_network_output(output: str) -> float:
    """Parse network usage output."""
    try:
        return float(output.strip())
    except ValueError:
        return 0.0


def parse_temperature_output(output: str) -> float:
    """Parse temperature output."""
    try:
        return float(output.strip())
    except ValueError:
        return 0.0


def parse_logs_output(output: str) -> str:
    """Parse log output."""
    return output.strip()


def parse_collector_output(raw_outputs: Dict[str, str]) -> Metric:
    """Convert collector output into a metric model."""
    return Metric(
        timestamp=datetime.now(timezone.utc),
        cpu=parse_cpu_output(raw_outputs.get("cpu", "0")),
        ram=parse_ram_output(raw_outputs.get("ram", "0")),
        disk=parse_disk_output(raw_outputs.get("disk", "0")),
        network=parse_network_output(raw_outputs.get("network", "0")),
        temperature=parse_temperature_output(
            raw_outputs.get("temperature", "0")
        ),
    )


def parse_json_metrics(json_string: str) -> Metric:
    """Parse JSON metrics and convert them into a metric model."""
    try:
        data: Dict[str, Any] = json.loads(json_string)
    except json.JSONDecodeError:
        data = {}

    return parse_collector_output(data)
