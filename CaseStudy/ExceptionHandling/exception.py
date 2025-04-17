

class BookingNotFoundException(Exception):
    def __init__(self, message="Booking with the given ID does not exist."):
        super().__init__(message)


class InvalidEmailException(Exception):
    def __init__(self, message="Email is invalid. It must contain '@'."):
        super().__init__(message)