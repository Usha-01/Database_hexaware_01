import pyodbc
from entity.Booking import Booking
from util.db_connection import get_connection
from ExceptionHandling.exception import BookingNotFoundException

class BookingDAO:
    def create_booking(self, booking):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO bookings (trip_id, passenger_id, booking_date, status)
                VALUES (?, ?, ?, ?)
            """, (booking.trip_id, booking.passenger_id, booking.booking_date, booking.status))
            conn.commit()
        except Exception as e:
            print("Error creating booking:", e)
        finally:
            conn.close()

    def get_booking_by_id(self, booking_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bookings WHERE booking_id = ?", (booking_id,))
            row = cursor.fetchone()
            if row:
                return Booking(*row)
            else:
                raise BookingNotFoundException(f"Booking with ID {booking_id} not found.")
        except BookingNotFoundException as e:
            raise e
        except Exception as e:
            print("Error fetching booking:", e)
        finally:
            conn.close()

    def update_booking(self, booking):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE bookings SET trip_id = ?, passenger_id = ?, booking_date = ?, status = ?
                WHERE booking_id = ?
            """, (booking.trip_id, booking.passenger_id, booking.booking_date, booking.status, booking.booking_id))
            if cursor.rowcount == 0:
                raise BookingNotFoundException(f"No booking found with ID {booking.booking_id} to update.")
            conn.commit()
        except BookingNotFoundException as e:
            raise e
        except Exception as e:
            print("Error updating booking:", e)
        finally:
            conn.close()

    def delete_booking(self, booking_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM bookings WHERE booking_id = ?", (booking_id,))
            if cursor.rowcount == 0:
                raise BookingNotFoundException(f"No booking found with ID {booking_id} to delete.")
            conn.commit()
        except BookingNotFoundException as e:
            raise e
        except Exception as e:
            print("Error deleting booking:", e)
        finally:
            conn.close()

    def get_all_bookings(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bookings")
            rows = cursor.fetchall()
            if not rows:
                raise BookingNotFoundException("No bookings found in the system.")
            bookings = [Booking(*row) for row in rows]
            return bookings
        except BookingNotFoundException as e:
            raise e
        except Exception as e:
            print("Error fetching all bookings:", e)
            return []
        finally:
            conn.close()
