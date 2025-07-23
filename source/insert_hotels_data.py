import sqlite3

db = sqlite3.connect('db.sqlite3', isolation_level=None)

insert_sql = """
    INSERT INTO hotels (name, prefecture)
    VALUES
        ('ホテルA', '東京都'),
        ('ホテルB', '群馬県'),
        ('旅館A', '埼玉県')
"""

db.execute(insert_sql)
db.close()