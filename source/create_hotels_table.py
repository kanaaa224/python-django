import sqlite3

db = sqlite3.connect('db.sqlite3', isolation_level=None)

create_sql = """
    CREATE TABLE IF NOT EXISTS hotels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(200) NOT NULL,
        prefecture VARCHAR(200) NOT NULL
    );
"""

db.execute(create_sql)
db.close()