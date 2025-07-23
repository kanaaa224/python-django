import sqlite3

db = sqlite3.connect('db.sqlite3', isolation_level=None)

create_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(150) UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
"""

db.execute(create_sql)
db.close()