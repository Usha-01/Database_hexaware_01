class Vehicle:
    def __init__(self, vehicle_id=None, model=None, capacity=None, type=None, status=None):
        self.vehicle_id = vehicle_id
        self.model = model
        self.capacity = capacity
        self.type = type
        self.status = status

    def __str__(self):
        return f"Vehicle({self.vehicle_id}, {self.model}, {self.capacity}, {self.type}, {self.status})"