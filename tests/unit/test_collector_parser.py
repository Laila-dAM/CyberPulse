import json

import pytest

from backend.services.collector_parser import (
    parse_cpu_output,
    parse_ram_output,
    parse_disk_output,
    parse_network_output,
    parse_temperature_output,
    parse_logs_output,
)


def test_parse_valid_cpu():
    assert parse_cpu_output("45") == 45


def test_parse_valid_ram():
    assert parse_ram_output("3021") == 3021


def test_parse_valid_disk():
    assert parse_disk_output("71") == 71


def test_parse_valid_network():
    assert parse_network_output("1024") == 1024


def test_parse_valid_temp():
    assert parse_temperature_output("55") == 55


def test_parse_logs():
    assert parse_logs_output("system started") == "system started"


def test_parse_invalid_cpu():
    assert parse_cpu_output("invalid data") == 0.0


def test_parse_invalid_ram():
    assert parse_ram_output("invalid data") == 0.0


def test_parse_invalid_disk():
    assert parse_disk_output("invalid data") == 0.0


def test_parse_invalid_network():
    assert parse_network_output("invalid data") == 0.0


def test_parse_invalid_temperature():
    assert parse_temperature_output("invalid data") == 0.0