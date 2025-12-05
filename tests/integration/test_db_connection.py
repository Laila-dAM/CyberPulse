import pytest
from backend.database import get_db_connection

def test_db_connection_returns_object():
    conn = get_db_connection()
    assert conn is not None

def test_db_simple_query():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1;")
    result = cursor.fetchone()
    assert result is not None
    assert result[0] == 1
    cursor.close()
    conn.close()

def test_db_multiple_connections():
    conn1 = get_db_connection()
    conn2 = get_db_connection()
    assert conn1 is not None
    assert conn2 is not None
    conn1.close()
    conn2.close()

def test_db_invalid_query_raises():
    conn = get_db_connection()
    cursor = conn.cursor()
    with pytest.raises(Exception):
        cursor.execute("SELECT * FROM invalid_table;")
    cursor.close()
    conn.close()
