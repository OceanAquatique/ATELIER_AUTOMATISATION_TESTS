 
import sqlite3
import json
import datetime

DB = "runs.db"


def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        result TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_run(result):

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "INSERT INTO runs (timestamp, result) VALUES (?,?)",
        (datetime.datetime.now().isoformat(), json.dumps(result))
    )

    conn.commit()
    conn.close()


def list_runs():

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    rows = c.execute(
        "SELECT timestamp, result FROM runs ORDER BY id DESC LIMIT 20"
    ).fetchall()

    conn.close()

    return rows
