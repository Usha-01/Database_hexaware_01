from db_connection import get_connection

def get_transport():
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    query = "SELECT * FROM transport"
    cursor.execute(query)

    rows = cursor.fetchall()
    print("Passengers present here in the database:")
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    get_transport()

