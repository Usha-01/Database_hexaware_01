import pyodbc
from ExceptionHandling.exception import InvalidEmailException
from entity.Passenger import Passenger
from util.db_connection import get_connection


class PassengerDAO:

    def create_passenger(self, passenger):
        # Validate email
        if '@' not in passenger.email:
            raise InvalidEmailException(f"Invalid email format: {passenger.email}")

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO passengers (first_name, gender, age, email, phone_number)
                VALUES (?, ?, ?, ?, ?)
            """, (passenger.first_name, passenger.gender, passenger.age, passenger.email, passenger.phone_number))
            conn.commit()
        except pyodbc.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()

    def update_passenger(self, passenger):
        # Validate email
        if '@' not in passenger.email:
            raise InvalidEmailException(f"Invalid email format: {passenger.email}")

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE passengers 
                SET first_name = ?, gender = ?, age = ?, email = ?, phone_number = ?
                WHERE passenger_id = ?
            """, (passenger.first_name, passenger.gender, passenger.age,
                  passenger.email, passenger.phone_number, passenger.passenger_id))
            if cursor.rowcount == 0:
                raise PassengerNotFoundException(f"No passenger found with ID {passenger.passenger_id} to update.")
            conn.commit()
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error while updating passenger: {e}")
        finally:
            if conn:
                conn.close()

    def get_passenger_by_id(self, passenger_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM passengers WHERE passenger_id = ?", (passenger_id,))
            row = cursor.fetchone()
            if row:
                return Passenger(
                    passenger_id=row[0],  # Assuming passenger_id is the first column
                    first_name=row[1],     # Assuming first_name is the second column
                    gender=row[2],         # Assuming gender is the third column
                    age=row[3],            # Assuming age is the fourth column
                    email=row[4],          # Assuming email is the fifth column
                    phone_number=row[5]    # Assuming phone_number is the sixth column
                )
            return None
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Error fetching passenger: {e}")
        finally:
            if conn:
                conn.close()

    def delete_passenger(self, passenger_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM passengers WHERE passenger_id = ?", (passenger_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise PassengerNotFoundException(f"No passenger found with ID {passenger_id} to delete.")
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Error deleting passenger: {e}")
        finally:
            if conn:
                conn.close()

    def get_all_passengers(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM passengers")
            rows = cursor.fetchall()
            passengers = []
            for row in rows:
                try:
                    passenger = Passenger(
                        passenger_id=row[0],
                        first_name=row[1],
                        gender=row[2],
                        age=row[3],
                        email=row[4],
                        phone_number=row[5]
                    )
                    passengers.append(passenger)
                except ValueError as ve:
                    print(f"Skipping passenger with ID {row[0]} due to validation error: {ve}")
            return passengers
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Error retrieving all passengers: {e}")
        finally:
            if conn:
                conn.close()
