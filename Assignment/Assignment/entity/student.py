import re
from exception.exception import InvalidEmailException, DuplicateEntryException

class Student:
    def __init__(self, student_id, first_name=None, last_name=None, email=None, dob=None, phone=None):
        self.StudentID = student_id
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.DOB = dob
        self.Phone = phone

    @property
    def StudentID(self):
        return self._student_id

    @StudentID.setter
    def StudentID(self, value):
        if not isinstance(value, int):
            raise ValueError("Student ID must be an integer.")
        self._student_id = value

    @property
    def FirstName(self):
        return self._first_name

    @FirstName.setter
    def FirstName(self, value):
        if value is not None and not value.strip():
            raise ValueError("First name cannot be empty.")
        self._first_name = value.strip() if value else None

    @property
    def LastName(self):
        return self._last_name

    @LastName.setter
    def LastName(self, value):
        if value is not None and not value.strip():
            raise ValueError("Last name cannot be empty.")
        self._last_name = value.strip() if value else None

    @property
    def Email(self):
        return self._email

    @Email.setter
    def Email(self, value):
        if value is not None and not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise InvalidEmailException("Invalid email format.")
        self._email = value

    @property
    def DOB(self):
        return self._dob

    @DOB.setter
    def DOB(self, value):
        self._dob = value

    @property
    def Phone(self):
        return self._phone

    @Phone.setter
    def Phone(self, value):
        if value is not None and not value.strip().isdigit():
            raise ValueError("Phone number must contain only digits.")
        self._phone = value.strip() if value else None

    def create_student(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Students WHERE student_id = ?", (self.StudentID,))
            if cursor.fetchone():
                raise DuplicateEntryException("Student already exists.")

            cursor.execute(
                "INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number) VALUES (?, ?, ?, ?, ?, ?)",
                (self.StudentID, self.FirstName, self.LastName, self.DOB, self.Email, self.Phone)
            )
            connection.commit()
            print("✅ Student created successfully.")
        except (InvalidEmailException, DuplicateEntryException, ValueError) as e:
            print(f"❌ Validation error: {e}")
        except Exception as e:
            print(f"❌ Database error: {e}")

    def view_students(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Students")
            rows = cursor.fetchall()
            if not rows:
                print("No students found.")
                return
            print("\n--- All Students ---")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, DOB: {row[3]}, Email: {row[4]}, Phone: {row[5]}")
        except Exception as e:
            print(f"❌ Error fetching students: {e}")

    def update_student(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Students WHERE student_id = ?", (self.StudentID,))
            if not cursor.fetchone():
                print("❌ Student not found.")
                return

            cursor.execute("""
                UPDATE Students 
                SET first_name = ?, last_name = ?, date_of_birth = ?, email = ?, phone_number = ?
                WHERE student_id = ?
            """, (self.FirstName, self.LastName, self.DOB, self.Email, self.Phone, self.StudentID))
            connection.commit()
            print("✅ Student updated successfully.")
        except Exception as e:
            print(f"❌ Error updating student: {e}")

