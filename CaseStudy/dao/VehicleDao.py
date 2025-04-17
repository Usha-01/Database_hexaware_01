import pyodbc
from entity.Vehicle import Vehicle
from util.db_connection import get_connection



class VehicleDAO:
    def create_vehicle(self, vehicle):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO vehicles (model, capacity, type, status)
                VALUES (?, ?, ?, ?)
            """, (vehicle.model, vehicle.capacity, vehicle.type, vehicle.status))
            conn.commit()
        except Exception as e:
            print("Error creating vehicle:", e)
        finally:
            conn.close()

    def get_vehicle_by_id(self, vehicle_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vehicles WHERE vehicle_id = ?", (vehicle_id,))
            row = cursor.fetchone()
            if row:
                return Vehicle(*row)
            return None
        except Exception as e:
            print("Error fetching vehicle:", e)
        finally:
            conn.close()

    def update_vehicle(self, vehicle):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE vehicles SET model = ?, capacity = ?, type = ?, status = ?
                WHERE vehicle_id = ?
            """, (vehicle.model, vehicle.capacity, vehicle.type, vehicle.status, vehicle.vehicle_id))
            conn.commit()
        except Exception as e:
            print("Error updating vehicle:", e)
        finally:
            conn.close()

    def delete_vehicle(self, vehicle_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM vehicles WHERE vehicle_id = ?", (vehicle_id,))
            conn.commit()
        except Exception as e:
            print("Error deleting vehicle:", e)
        finally:
            conn.close()

    def get_all_vehicles(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vehicles")
            rows = cursor.fetchall()
            return [Vehicle(*row) for row in rows]
        except Exception as e:
            print("Error fetching all vehicles:", e)
        finally:
            conn.close()
