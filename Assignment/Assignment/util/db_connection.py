import pyodbc

def get_connection():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=LAPTOP-LODD6GED;'
            'DATABASE=Student;'
            'Trusted_Connection=yes;'
        )
        print("Database connection successful.")
        return connection
    except Exception as e:
        print("Error while connecting to database:", e)
        return None
