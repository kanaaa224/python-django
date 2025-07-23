from django.db import connection

def dict_fetch_all(cursor):
    columns = [col[0] for col in cursor.description]

    return [
        dict(zip(columns, row))

        for row in cursor.fetchall()
    ]

class UserManager:
    @classmethod
    def create_user(cls, username, hashed_password):
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO users (username, password)
                VALUES (%s, %s)
            """, [username, hashed_password])

            return True

    @classmethod
    def get_user_by_username(cls, username):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, username, password
                FROM users
                WHERE username = %s
            """, [username])

            results = dict_fetch_all(cursor)

            return results[0] if results else None