import sqlite3

db = sqlite3.connect('db.sqlite3', isolation_level=None)

create_sql = """
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(200) NOT NULL,
        hotel_id INTEGER NOT NULL,
        FOREIGN KEY (hotel_id) REFERENCES hotels (id)
    );
"""

db.execute(create_sql)
db.close()