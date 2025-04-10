from db_connection import get_connection

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    with open('init_schema.sql', 'r') as file:
        sql_script = file.read()
        for stmt in sql_script.strip().split(';'):
            if stmt.strip():
                cursor.execute(stmt)
    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized successfully.")
