import json
import pytest
from backend.utils.parser import parse_metric_output

def test_parse_valid_cpu():
    output = "cpu_usage: 45"
    parsed = parse_metric_output(output)
    assert parsed["cpu_usage"] == 45

def test_parse_valid_ram():
    output = "ram_usage: 3021"
    parsed = parse_metric_output(output)
    assert parsed["ram_usage"] == 3021

def test_parse_valid_disk():
    output = "disk_usage: 71"
    parsed = parse_metric_output(output)
    assert parsed["disk_usage"] == 71

def test_parse_valid_network():
    output = json.dumps({"rx": 1024, "tx": 2048})
    parsed = parse_metric_output(output)
    assert parsed["rx"] == 1024
    assert parsed["tx"] == 2048

def test_parse_valid_temp():
    output = "temp: 55"
    parsed = parse_metric_output(output)
    assert parsed["temp"] == 55

def test_parse_invalid():
    output = "invalid data"
    with pytest.raises(ValueError):
        parse_metric_output(output)
