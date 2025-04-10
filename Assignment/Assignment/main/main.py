from util.db_connection import get_connection
from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher
from entity.entrollment import Enrollment
from entity.payment import Payment

def main():
    conn = get_connection()
    if not conn:
        print("❌ Failed to connect to the database.")
        return

    while True:
        print("\n--- Student Information System ---")
        print("1. Student")
        print("2. Course")
        print("3. Teacher")
        print("4. Enrollment")
        print("5. Payment")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            student_menu(conn)
        elif choice == "2":
            course_menu(conn)
        elif choice == "3":
            teacher_menu(conn)
        elif choice == "4":
            enrollment_menu(conn)
        elif choice == "5":
            payment_menu(conn)
        elif choice == "6":
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# --- Student Menu ---
def student_menu(conn):
    while True:
        print("\n--- Student Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                sid = int(input("Student ID: "))
                fname = input("First Name: ")
                lname = input("Last Name: ")
                email = input("Email: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                phone = input("Phone Number: ")
                Student(sid, fname, lname, email, dob, phone).create_student(conn)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Students")
                rows = cursor.fetchall()
                if not rows:
                    print("⚠️ No students found.")
                else:
                    print("\n--- Student List ---")
                    for row in rows:
                        print(f"ID: {row.student_id}, Name: {row.first_name} {row.last_name}, Email: {row.email}, DOB: {row.date_of_birth}, Phone: {row.phone_number}")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "3":
            try:
                sid = int(input("Student ID: "))
                fname = input("New First Name: ")
                lname = input("New Last Name: ")
                email = input("New Email: ")
                dob = input("New DOB (YYYY-MM-DD): ")
                phone = input("New Phone Number: ")
                Student(sid, fname, lname, email, dob, phone).update_student(conn)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "4":
            break

# --- Course Menu ---
def course_menu(conn):
    while True:
        print("\n--- Course Menu ---")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Update Course")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                cid = int(input("Course ID: "))
                name = input("Course Name: ")
                credits = int(input("Credits: "))
                tid = int(input("Teacher ID: "))
                Course(cid, name, credits, tid).create_course(conn)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Courses")
                rows = cursor.fetchall()
                if not rows:
                    print("⚠️ No courses found.")
                else:
                    print("\n--- Course List ---")
                    for row in rows:
                        print(f"ID: {row.course_id}, Name: {row.course_name}, Credits: {row.credits}, Teacher ID: {row.teacher_id}")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "3":
            try:
                cid = int(input("Course ID: "))
                name = input("New Course Name: ")
                credits = int(input("New Credits: "))
                tid = int(input("New Teacher ID: "))
                Course(cid, name, credits, tid).update_course(conn)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "4":
            break

# --- Teacher Menu ---
def teacher_menu(conn):
    while True:
        print("\n--- Teacher Menu ---")
        print("1. Add Teacher")
        print("2. View Teachers")
        print("3. Update Teacher")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                tid = int(input("Teacher ID: "))
                fname = input("First Name: ")
                lname = input("Last Name: ")
                email = input("Email: ")
                Teacher(tid, fname, lname, email).create_teacher(conn)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Teachers")
                rows = cursor.fetchall()
                if not rows:
                    print("⚠️ No teachers found.")
                else:
                    print("\n--- Teacher List ---")
                    for row in rows:
                        print(f"ID: {row.teacher_id}, Name: {row.first_name} {row.last_name}, Email: {row.email}")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "3":
            try:
                tid = int(input("Teacher ID: "))
                fname = input("New First Name: ")
                lname = input("New Last Name: ")
                email = input("New Email: ")
                Teacher(tid, fname, lname, email).update_teacher(conn)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "4":
            break

# --- Enrollment Menu ---
def enrollment_menu(conn):
    while True:
        print("\n--- Enrollment Menu ---")
        print("1. Enroll Student")
        print("2. View Enrollments")
        print("3. Update Enrollment")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                sid = int(input("Student ID: "))
                cid = int(input("Course ID: "))
                enroll_date = input("Enrollment Date (YYYY-MM-DD): ")
                Enrollment(sid, cid, enroll_date).enroll_student(conn)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Enrollments")
                rows = cursor.fetchall()
                if not rows:
                    print("⚠️ No enrollments found.")
                else:
                    print("\n--- Enrollment List ---")
                    for row in rows:
                        print(f"Student ID: {row.student_id}, Course ID: {row.course_id}, Date: {row.enrollment_date}")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "3":
            try:
                sid = int(input("Student ID: "))
                cid = int(input("New Course ID: "))
                enroll_date = input("New Enrollment Date (YYYY-MM-DD): ")
                Enrollment(sid, cid, enroll_date).update_enrollment(conn)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "4":
            break

# --- Payment Menu ---
def payment_menu(conn):
    while True:
        print("\n--- Payment Menu ---")
        print("1. Make Payment")
        print("2. View Payments")
        print("3. Update Payment")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                sid = int(input("Student ID: "))
                amount = float(input("Amount: "))
                pay_date = input("Payment Date (YYYY-MM-DD): ")
                Payment(sid, amount, pay_date).make_payment(conn)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            try:
                Payment(None, None, None).read_payment(conn)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "3":
            try:
                sid = int(input("Student ID: "))
                old_date = input("Old Payment Date (YYYY-MM-DD): ")
                new_amount = float(input("New Amount: "))
                new_date = input("New Payment Date (YYYY-MM-DD): ")
                Payment(sid, 0, old_date).update_payment(conn, new_amount, new_date)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "4":
            break

if __name__ == "__main__":
    main()
