import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parents[1].parent / "cyberpulse.db"


def get_db_connection():
    return sqlite3.connect(DATABASE_PATH)