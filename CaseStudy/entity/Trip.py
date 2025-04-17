class Trip:
    def __init__(self, trip_id=None, vehicle_id=None, route_id=None, departure_date=None, arrival_date=None, status=None, trip_type=None, max_passengers=None):
        self.trip_id = trip_id
        self.vehicle_id = vehicle_id
        self.route_id = route_id
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.status = status
        self.trip_type = trip_type
        self.max_passengers = max_passengers

    def __str__(self):
        return f"Trip({self.trip_id}, {self.vehicle_id}, {self.route_id}, {self.departure_date}, {self.arrival_date}, {self.status}, {self.trip_type}, {self.max_passengers})"