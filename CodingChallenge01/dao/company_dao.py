import pyodbc
from entity.company import Company
from util.db_connection import DBConnection


class CompanyDAO:

    @staticmethod
    def create_company(name, location):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Companies (company_name, location)
                VALUES (?, ?)
            """, (name, location))
            conn.commit()
            return True
        except Exception as e:
            print(f"❌ Error creating company: {e}")
            return False
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_company_by_id(company_id):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Companies WHERE company_id = ?", (company_id,))
            row = cursor.fetchone()
            if row:
                return Company(*row)
            return None
        except Exception as e:
            print(f"❌ Error reading company: {e}")
            return None
        finally:
            if conn:
                conn.close()

    @staticmethod
    def update_company(company_id, name, location):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Companies 
                SET company_name = ?, location = ?
                WHERE company_id = ?
            """, (name, location, company_id))
            conn.commit()
            return True
        except Exception as e:
            print(f"❌ Error updating company: {e}")
            return False
        finally:
            if conn:
                conn.close()

    @staticmethod
    def delete_company(company_id):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Companies WHERE company_id = ?", (company_id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"❌ Error deleting company: {e}")
            return False
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_all_companies():
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Companies")
            rows = cursor.fetchall()
            return [Company(*row) for row in rows]
        except Exception as e:
            print(f"❌ Error retrieving all companies: {e}")
            return []
        finally:
            if conn:
                conn.close()
