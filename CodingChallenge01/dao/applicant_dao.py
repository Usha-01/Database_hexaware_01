import re
from util.db_connection import DBConnection
from entity.applicant import Applicant
from exception.exception import InvalidEmailFormatException


class ApplicantDAO:

    @staticmethod
    def _validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise InvalidEmailFormatException()

    @staticmethod

    def create_applicant(applicant: Applicant):
        conn = None  # Ensure conn is defined even if an exception occurs before it's assigned
        try:
            ApplicantDAO._validate_email(applicant.email)
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Applicants (first_name, last_name, email, phone, resume)
                VALUES (?, ?, ?, ?, ?)""",
                           (applicant.first_name, applicant.last_name,
                            applicant.email, applicant.phone, applicant.resume)
                           )
            conn.commit()
            print("✅ Applicant created successfully.")
        except InvalidEmailFormatException as e:
            print("❌ Invalid email format. Email must contain '@' and a valid domain.")
        except Exception as e:
            print("❌ Error creating applicant:", e)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_applicant_by_id(applicant_id):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Applicants WHERE applicant_id = ?", (applicant_id,))
            row = cursor.fetchone()
            if row:
                return Applicant(*row)
            return None
        except Exception as e:
            print("❌ Error reading applicant:", e)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def update_applicant(applicant_id, first_name, last_name, email, phone, resume):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Applicants
                SET first_name = ?, last_name = ?, email = ?, phone = ?, resume = ?
                WHERE applicant_id = ?
            """, (first_name, last_name, email, phone, resume, applicant_id))
            conn.commit()
            print("✅ Applicant updated successfully.")
        except Exception as e:
            print(f"❌ Error updating applicant: {e}")
        finally:
            if conn:
                conn.close()

    @staticmethod
    def delete_applicant(applicant_id):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Applicants WHERE applicant_id = ?", (applicant_id,))
            conn.commit()
            print("🗑️ Applicant deleted successfully.")
        except Exception as e:
            print("❌ Error deleting applicant:", e)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_all_applicants():
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Applicants")
            rows = cursor.fetchall()
            return [Applicant(*row) for row in rows]
        except Exception as e:
            print("❌ Error retrieving all applicants:", e)
            return []
        finally:
            if conn:
                conn.close()
