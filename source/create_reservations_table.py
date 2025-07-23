import sqlite3

db = sqlite3.connect('db.sqlite3', isolation_level=None)

create_sql = """
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_id INTEGER NOT NULL,
        price INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        reservation_date DATE DEFAULT CURRENT_DATE,
        stay_date DATE NOT NULL,
        FOREIGN KEY (room_id) REFERENCES rooms (id),
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
"""

db.execute(create_sql)
db.close()