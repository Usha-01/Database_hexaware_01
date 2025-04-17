class Route:
    def __init__(self, route_id=None, start_destination=None, end_destination=None, distance=None):
        self.route_id = route_id
        self.start_destination = start_destination
        self.end_destination = end_destination
        self.distance = distance

    def __str__(self):
        return f"Route({self.route_id}, {self.start_destination}, {self.end_destination}, {self.distance})"