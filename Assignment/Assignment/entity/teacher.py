from exception.exception import DuplicateEntryException, InvalidEmailException
import re

class Teacher:
    def __init__(self, teacher_id, first_name=None, last_name=None, email=None):
        self.TeacherID = teacher_id
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email

    @property
    def TeacherID(self):
        return self._teacher_id

    @TeacherID.setter
    def TeacherID(self, value):
        if not isinstance(value, int):
            raise ValueError("Teacher ID must be an integer.")
        self._teacher_id = value

    @property
    def FirstName(self):
        return self._first_name

    @FirstName.setter
    def FirstName(self, value):
        self._first_name = value

    @property
    def LastName(self):
        return self._last_name

    @LastName.setter
    def LastName(self, value):
        self._last_name = value

    @property
    def Email(self):
        return self._email

    @Email.setter
    def Email(self, value):
        if value is not None and not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise InvalidEmailException("Invalid email format.")
        self._email = value

    def create_teacher(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Teachers WHERE teacher_id=?", (self.TeacherID,))
            if cursor.fetchone():
                raise DuplicateEntryException("Teacher already exists.")
            cursor.execute(
                "INSERT INTO Teachers (teacher_id, first_name, last_name, email) VALUES (?, ?, ?, ?)",
                (self.TeacherID, self.FirstName, self.LastName, self.Email)
            )
            connection.commit()
            print("✅ Teacher created successfully.")
        except (InvalidEmailException, DuplicateEntryException, ValueError) as e:
            print(f"❌ Validation error: {e}")
        except Exception as e:
            print(f"❌ Database error: {e}")

    def read_teacher(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Teachers WHERE teacher_id=?", (self.TeacherID,))
            row = cursor.fetchone()
            if row:
                print(f"📘 Teacher Details: ID={row[0]}, Name={row[1]} {row[2]}, Email={row[3]}")
            else:
                print("❌ Teacher not found.")
        except Exception as e:
            print(f"❌ Error while reading teacher: {e}")

    def update_teacher(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Teachers WHERE teacher_id=?", (self.TeacherID,))
            if not cursor.fetchone():
                print("❌ Teacher not found.")
                return
            cursor.execute(
                "UPDATE Teachers SET first_name=?, last_name=?, email=? WHERE teacher_id=?",
                (self.FirstName, self.LastName, self.Email, self.TeacherID)
            )
            connection.commit()
            print("✅ Teacher updated successfully.")
        except (InvalidEmailException, ValueError) as e:
            print(f"❌ Validation error: {e}")
        except Exception as e:
            print(f"❌ Error while updating teacher: {e}")


