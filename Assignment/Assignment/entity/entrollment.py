class Enrollment:
    def __init__(self, student_id, course_id, date):
        self.StudentID = student_id
        self.CourseID = course_id
        self.EnrollmentDate = date

    def enroll_student(self, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Enrollments VALUES (?, ?, ?)", (
                self.StudentID, self.CourseID, self.EnrollmentDate))
            conn.commit()
            print("✅ Student enrolled successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def read_enrollment(self, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Enrollments WHERE student_id=? AND course_id=?", (
                self.StudentID, self.CourseID))
            row = cursor.fetchone()
            if row:
                print(f"📄 Enrollment Info: {row}")
            else:
                print("❌ Enrollment not found.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def update_enrollment(self, conn, new_date):
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Enrollments SET enrollment_date=? WHERE student_id=? AND course_id=?
            """, (new_date, self.StudentID, self.CourseID))
            conn.commit()
            print("✅ Enrollment updated successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")


