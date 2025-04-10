from exception.exception import InvalidAmountException

class Payment:
    def __init__(self, student_id, amount, date):
        self.StudentID = student_id
        self.Amount = amount
        self.PaymentDate = date

    def make_payment(self, conn):
        try:
            if self.Amount <= 0:
                raise InvalidAmountException("Amount must be greater than 0.")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Payments (student_id, amount, payment_date) VALUES (?, ?, ?)",
                           (self.StudentID, self.Amount, self.PaymentDate))
            conn.commit()
            print("✅ Payment made successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def read_payment(self, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Payments")
            rows = cursor.fetchall()
            if rows:
                print("\n--- Payment List ---")
                for row in rows:
                    print(f"Student ID: {row[1]}, Amount: {row[2]:.2f}, Date: {row[3]}")
            else:
                print("❌ No payment records found.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def update_payment(self, conn, new_amount, new_date):
        try:
            if new_amount <= 0:
                raise InvalidAmountException("Amount must be greater than 0.")
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Payments 
                SET amount = ?, payment_date = ? 
                WHERE student_id = ? AND payment_date = ?
            """, (new_amount, new_date, self.StudentID, self.PaymentDate))
            if cursor.rowcount == 0:
                print("❌ No matching payment found to update.")
            else:
                conn.commit()
                print("✅ Payment updated successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")
