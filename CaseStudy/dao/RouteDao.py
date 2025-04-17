import pyodbc
from entity.Route import Route
from util.db_connection import get_connection

class RouteDAO:
    def create_route(self, route):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO routess (start_destination, end_destination, distance)
                VALUES (?, ?, ?)
            """, (route.start_destination, route.end_destination, route.distance))
            conn.commit()
        except Exception as e:
            print("Error creating route:", e)
        finally:
            conn.close()

    def get_route_by_id(self, route_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM routess WHERE route_id = ?", (route_id,))
            row = cursor.fetchone()
            if row:
                return Route(*row)
            return None
        except Exception as e:
            print("Error fetching route:", e)
        finally:
            conn.close()

    def update_route(self, route):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE routess SET start_destination = ?, end_destination = ?, distance = ?
                WHERE route_id = ?
            """, (route.start_destination, route.end_destination, route.distance, route.route_id))
            conn.commit()
        except Exception as e:
            print("Error updating route:", e)
        finally:
            conn.close()

    def delete_route(self, route_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM routess WHERE route_id = ?", (route_id,))
            conn.commit()
        except Exception as e:
            print("Error deleting route:", e)
        finally:
            conn.close()

    def get_all_routes(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM routess")
            rows = cursor.fetchall()
            return [Route(*row) for row in rows]
        except Exception as e:
            print("Error retrieving routes:", e)
        finally:
            conn.close()
