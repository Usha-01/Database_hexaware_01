class Passenger:
    def __init__(self, passenger_id=None, first_name=None, gender=None, age=None, email=None, phone_number=None):
        self.passenger_id = passenger_id
        self.first_name = first_name
        self.gender = gender
        self.age = age
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"Passenger({self.passenger_id}, {self.first_name}, {self.gender}, {self.age}, {self.email}, {self.phone_number})"