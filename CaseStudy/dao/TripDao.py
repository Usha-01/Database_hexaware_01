import pyodbc
from entity.Trip import Trip
from util.db_connection import get_connection

class TripDAO:
    def create_trip(self, trip):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO trips (vehicle_id, route_id, departure_date, arrival_date, status, trip_type, max_passengers)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (trip.vehicle_id, trip.route_id, trip.departure_date, trip.arrival_date, trip.status, trip.trip_type, trip.max_passengers))
            conn.commit()
        except Exception as e:
            print("Error creating trip:", e)
        finally:
            conn.close()

    def get_trip_by_id(self, trip_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM trips WHERE trip_id = ?", (trip_id,))
            row = cursor.fetchone()
            if row:
                return Trip(*row)
            return None
        except Exception as e:
            print("Error fetching trip:", e)
        finally:
            conn.close()

    def update_trip(self, trip):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE trips SET vehicle_id = ?, route_id = ?, departure_date = ?, arrival_date = ?, status = ?, trip_type = ?, max_passengers = ?
                WHERE trip_id = ?
            """, (trip.vehicle_id, trip.route_id, trip.departure_date, trip.arrival_date, trip.status, trip.trip_type, trip.max_passengers, trip.trip_id))
            conn.commit()
        except Exception as e:
            print("Error updating trip:", e)
        finally:
            conn.close()

    def delete_trip(self, trip_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM trips WHERE trip_id = ?", (trip_id,))
            conn.commit()
        except Exception as e:
            print("Error deleting trip:", e)
        finally:
            conn.close()

    def get_all_trips(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM trips")
            rows = cursor.fetchall()
            return [Trip(*row) for row in rows]
        except Exception as e:
            print("Error retrieving trips:", e)
        finally:
            conn.close()
