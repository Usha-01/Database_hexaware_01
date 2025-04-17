import pyodbc
from util.db_connection import DBConnection
from entity.job_application import JobApplication

class JobApplicationDAO:
    @staticmethod
    @staticmethod
    def create_application(application):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            query = """
            INSERT INTO Applications (job_id, applicant_id, application_date, cover_letter)
            VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (application.job_id, application.applicant_id,
                                   application.application_date, application.cover_letter))
            conn.commit()
            print("Database connection successful.")
        except Exception as e:
            print(f"❌ Error creating job application: {e}")
        finally:
            conn.close()

    @staticmethod
    def get_all_applications():
        apps = []
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Applications")
            rows = cursor.fetchall()
            for row in rows:
                apps.append(JobApplication(*row))
        finally:
            cursor.close()
            conn.close()
        return apps

    @staticmethod
    def get_application_by_id(app_id):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Applications WHERE application_id = ?", (app_id,))
            row = cursor.fetchone()
            return JobApplication(*row) if row else None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_application_status(app_id, new_letter):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("UPDATE Applications SET cover_letter = ? WHERE application_id = ?", (new_letter, app_id))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_application(app_id):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM Applications WHERE application_id = ?", (app_id,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
