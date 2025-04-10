from db_connection import get_connection

def get_students():
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    query = "SELECT * FROM Students"
    cursor.execute(query)

    rows = cursor.fetchall()
    print("📋 Students in the database:")
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    get_students()

