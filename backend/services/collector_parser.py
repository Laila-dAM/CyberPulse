import json
from typing import Dict, Any
from backend.models.metric import Metric
from datetime import datetime

def parse_cpu_output(output: str) -> float:
    try:
        return float(output.strip())
    except ValueError:
        return 0.0

def parse_ram_output(output: str) -> float:
    try:
        return float(output.strip())
    except ValueError:
        return 0.0

def parse_disk_output(output: str) -> float:
    try:
        return float(output.strip())
    except ValueError:
        return 0.0

def parse_network_output(output: str) -> float:
    try:
        return float(output.strip())
    except ValueError:
        return 0.0

def parse_temperature_output(output: str) -> float:
    try:
        return float(output.strip())
    except ValueError:
        return 0.0

def parse_logs_output(output: str) -> str:
    return output.strip()

def parse_collector_output(raw_outputs: Dict[str, str]) -> Metric:
    return Metric(
        timestamp=datetime.utcnow(),
        cpu=parse_cpu_output(raw_outputs.get("cpu", "0")),
        ram=parse_ram_output(raw_outputs.get("ram", "0")),
        disk=parse_disk_output(raw_outputs.get("disk", "0")),
        network=parse_network_output(raw_outputs.get("network", "0")),
        temperature=parse_temperature_output(raw_outputs.get("temperature", "0")),
        logs=parse_logs_output(raw_outputs.get("logs", ""))
    )

def parse_json_metrics(json_string: str) -> Metric:
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError:
        data = {}
    return parse_collector_output(data)
