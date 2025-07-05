from db import connect_db, ensure_tables, with_db_connection, SHORTCUT_TABLE
import os

def add_shortcut(path, name):
    db = connect_db()
    ensure_tables(db)
    abs_path = os.path.abspath(path)
    db.execute(f"REPLACE INTO {SHORTCUT_TABLE} (name, path) VALUES (?, ?)", (name, abs_path))
    db.commit()
    db.close()

def add_shortcut2(path, name):
    result = with_db_connection(lambda db:
        db.execute(f"REPLACE INTO {SHORTCUT_TABLE} (name, path) VALUES (?, ?)", (name, path))
    )
    return result
    
def remove_shortcut(name):
    db = connect_db()
    db.execute(f"DELETE FROM {SHORTCUT_TABLE} WHERE name = ?", (name,))
    db.commit()
    db.close()

def list_shortcuts():
    db = connect_db()
    shortcuts = db.execute(f"SELECT name, path FROM {SHORTCUT_TABLE}").fetchall()
    for name, path in shortcuts:
        print(f"{name}: {path}")
    db.close()

def resolve_path(name):
    db = connect_db()
    shortcut = db.execute(f"SELECT path FROM {SHORTCUT_TABLE} WHERE name = ?", (name,)).fetchone()
    db.close()
    return shortcut[0] if shortcut else None