from backend.core.database import engine


def get_db_connection():
    return engine.raw_connection()
