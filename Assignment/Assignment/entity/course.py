class Course:
    def __init__(self, course_id, name, credits, teacher_id):
        self.CourseID = course_id
        self.Name = name
        self.Credits = credits
        self.TeacherID = teacher_id

    def create_course(self, conn):
        try:
            if self.Credits <= 0:
                raise ValueError("Credits must be greater than 0.")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Courses VALUES (?, ?, ?, ?)", (
                self.CourseID, self.Name, self.Credits, self.TeacherID))
            conn.commit()
            print("✅ Course created successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def read_course(self, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Courses WHERE course_id=?", (self.CourseID,))
            row = cursor.fetchone()
            if row:
                print(f"📄 Course Info: {row}")
            else:
                print("❌ Course not found.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def update_course(self, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Courses SET course_name=?, credits=?, teacher_id=?
                WHERE course_id=?
            """, (self.Name, self.Credits, self.TeacherID, self.CourseID))
            conn.commit()
            print("✅ Course updated successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")


