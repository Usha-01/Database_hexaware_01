import pyodbc

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-LODD6GED;"
        "DATABASE=transport;"
        "Trusted_Connection=yes;"
    )
