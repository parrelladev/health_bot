import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "health_bot.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, telegram_id INTEGER UNIQUE)"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, user_id INTEGER, url TEXT)"
    )
    return conn
