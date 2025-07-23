from django.db import models
from django.db import connection

def dict_fetch_all(cursor):
    columns = [col[0] for col in cursor.description]

    return [
        dict(zip(columns, row))

        for row in cursor.fetchall()
    ]

class ReservationManager:
    @classmethod
    def create_reservation(cls, room_id, price, user_id, stay_date):
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO reservations (
                room_id, price, user_id, stay_date)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, [room_id, price, user_id, stay_date])

            return cursor.fetchone()[0]

    @classmethod
    def get_reservations_by_user_id(cls, user_id):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT r.id, r.stay_date,
                h.name as hotel_name
                FROM reservations r
                JOIN rooms rm ON r.room_id = rm.id
                JOIN hotels h ON rm.hotel_id = h.id
                WHERE r.user_id = %s
                ORDER BY r.stay_date DESC
            """, [user_id])

            return dict_fetch_all(cursor)

    @classmethod
    def get_reservation_by_id(cls, reservation_id):
        with connection.cursor() as cursor:
            query = """
                SELECT r.id, r.price, r.reservation_date, r.stay_date, r.user_id,
                rm.id as room_id, rm.name as room_name,
                h.id as hotel_id, h.name as hotel_name, h.prefecture
                FROM reservations r
                JOIN rooms rm ON r.room_id = rm.id
                JOIN hotels h ON rm.hotel_id = h.id
                WHERE r.id = %s
            """
            cursor.execute(query, [reservation_id])

            result = dict_fetch_all(cursor)

            return result[0] if result else None

    @classmethod
    def delete_reservation(cls, reservation_id):
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM reservations
                WHERE id = %s
                RETURNING id
            """, [reservation_id])

            result = cursor.fetchone()

            return result[0] if result else None