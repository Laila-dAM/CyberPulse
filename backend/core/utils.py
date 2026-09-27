"""Utility functions for file handling, logging, and metric processing."""

import json
import logging
import os
from datetime import datetime, timezone


def load_json_file(file_path: str) -> dict:
    """Load a JSON file and return its contents."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json_file(file_path: str, data: dict) -> None:
    """Save data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def get_current_timestamp() -> str:
    """Return the current UTC timestamp in ISO format."""
    return datetime.now(timezone.utc).isoformat()


def ensure_directory(path: str) -> None:
    """Create a directory if it does not exist."""
    os.makedirs(path, exist_ok=True)


def setup_logger(
    name: str,
    log_file: str,
    level=logging.INFO,
) -> logging.Logger:
    """Configure and return a file logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def chunk_list(data: list, chunk_size: int) -> list:
    """Split a list into smaller chunks."""
    return [
        data[i:i + chunk_size]
        for i in range(0, len(data), chunk_size)
    ]


def filter_metrics(
    metrics: list,
    key: str,
    min_value: float = None,
    max_value: float = None,
) -> list:
    """Filter metrics using minimum and maximum values."""
    result = []

    for metric in metrics:
        value = metric.get(key)

        if value is None:
            continue

        if min_value is not None and value < min_value:
            continue

        if max_value is not None and value > max_value:
            continue

        result.append(metric)

    return result
