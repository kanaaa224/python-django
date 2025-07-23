import sqlite3

db = sqlite3.connect('db.sqlite3', isolation_level=None)

insert_sql = """
    INSERT INTO rooms (name, hotel_id)
    VALUES
        ('シングルルーム', 1), -- ホテルA のルーム
        ('ダブルルーム', 1),   -- ホテルA のルーム
        ('スイートルーム', 1), -- ホテルA のルーム
        ('ツインルーム', 2),   -- ホテルB のルーム
        ('和室', 3)           -- 旅館A   のルーム
"""

db.execute(insert_sql)
db.close()