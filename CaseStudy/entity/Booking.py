class Booking:
    def __init__(self, booking_id=None, trip_id=None, passenger_id=None, booking_date=None, status=None):
        self.booking_id = booking_id
        self.trip_id = trip_id
        self.passenger_id = passenger_id
        self.booking_date = booking_date
        self.status = status

    def __str__(self):
        return f"Booking({self.booking_id}, {self.trip_id}, {self.passenger_id}, {self.booking_date}, {self.status})"
