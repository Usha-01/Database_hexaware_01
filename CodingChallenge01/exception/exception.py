class InvalidEmailFormatException(Exception):

    def __init__(self, message="Invalid email format. Email must contain '@' and a valid domain."):
        super().__init__(message)


class NegativeSalaryException(Exception):

    def __init__(self, message="Salary must be a non-negative value."):
        super().__init__(message)


class DatabaseConnectionException(Exception):

    def __init__(self, message="Failed to connect to the database."):
        super().__init__(message)

# exception/exception.py

class DatabaseException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class SQLQueryException(Exception):

    def __init__(self, message="An error occurred while executing the SQL query."):
        super().__init__(message)
