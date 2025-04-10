
INSERT_STUDENT = "INSERT INTO Student (StudentID, Name, Email, Age) VALUES (?, ?, ?, ?)"
GET_STUDENT_BY_ID = "SELECT * FROM Student WHERE StudentID = ?"
GET_ALL_STUDENTS = "SELECT * FROM Student"
UPDATE_STUDENT = "UPDATE Student SET Name = ?, Email = ?, Age = ? WHERE StudentID = ?"
DELETE_STUDENT = "DELETE FROM Student WHERE StudentID = ?"