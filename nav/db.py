from encodings.punycode import T
import sqlite3
import os
import sys
from typing import Callable

# db tables
SHORTCUT_TABLE = "shortcuts"
FUZZY_TABLE = "fuzzy"

def db_path():
    return os.path.join(os.path.expanduser("~"), ".nav.db")

def connect_db():
    return sqlite3.connect(db_path())

def ensure_tables(db):
    db.execute(f"""
    CREATE TABLE IF NOT EXISTS {SHORTCUT_TABLE} (
        name TEXT PRIMARY KEY,
        path TEXT NOT NULL
    );
    """)
    db.commit()
    
def with_db_connection(function: Callable[[sqlite3.Connection], T]) -> T:
    with connect_db() as db:
        result = function(db)
        db.commit()
        return result