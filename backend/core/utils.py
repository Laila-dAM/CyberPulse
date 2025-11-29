import os
import json
import logging
from datetime import datetime

def load_json_file(file_path: str) -> dict:
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r") as file:
        return json.load(file)

def save_json_file(file_path: str, data: dict) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def get_current_timestamp() -> str:
    return datetime.utcnow().isoformat()

def ensure_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger

def chunk_list(data: list, chunk_size: int) -> list:
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

def filter_metrics(metrics: list, key: str, min_value: float = None, max_value: float = None) -> list:
    result = []
    for m in metrics:
        value = m.get(key)
        if value is None:
            continue
        if min_value is not None and value < min_value:
            continue
        if max_value is not None and value > max_value:
            continue
        result.append(m)
    return result
