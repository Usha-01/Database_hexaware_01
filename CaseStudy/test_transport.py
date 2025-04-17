import pytest
from entity.Vehicle import Vehicle
from entity.Booking import Booking


class MockVehicleDAO:
    def __init__(self):
        self.vehicles = {
            1: Vehicle(vehicle_id=1, model='Tata Bus 101', capacity=45.00, type='Bus', status='Available'),
            2: Vehicle(vehicle_id=2, model='Eicher Starline', capacity=40.00, type='Bus', status='In Maintenance'),
            3: Vehicle(vehicle_id=3, model='Volvo AC Coach', capacity=50.00, type='Bus', status='Available'),
            4: Vehicle(vehicle_id=4, model='Mahindra Tourister', capacity=30.00, type='Van', status='Available'),
            5: Vehicle(vehicle_id=5, model='Ashok Leyland Lynx', capacity=55.00, type='Bus', status='Available'),
        }

    def get_vehicle_by_id(self, vehicle_id):
        return self.vehicles.get(vehicle_id)  # Returns None if not found

class MockBookingDAO:
    def __init__(self):
        self.bookings = {
            1: Booking(booking_id=1, trip_id=1, passenger_id=1, booking_date='2025-04-16 10:00:00', status='Confirmed'),
            2: Booking(booking_id=2, trip_id=1, passenger_id=2, booking_date='2025-04-16 10:15:00', status='Confirmed'),
            3: Booking(booking_id=3, trip_id=2, passenger_id=3, booking_date='2025-04-17 09:00:00', status='Pending'),
            4: Booking(booking_id=4, trip_id=3, passenger_id=4, booking_date='2025-04-18 08:30:00', status='Confirmed'),
            5: Booking(booking_id=5, trip_id=5, passenger_id=5, booking_date='2025-04-18 11:45:00', status='Confirmed'),
        }

    def get_booking_by_id(self, booking_id):
        return self.bookings.get(booking_id)  # Returns None if not found

# --------------------------
# Test Cases
# --------------------------

def test_vehicle_exists_by_id():
    dao = MockVehicleDAO()
    vehicle = dao.get_vehicle_by_id(3)
    assert vehicle is not None
    assert vehicle.model == "Volvo AC Coach"
    assert vehicle.capacity == 50.00

def test_booking_exists_by_id():
    dao = MockBookingDAO()
    booking = dao.get_booking_by_id(5)
    assert booking is not None
    assert booking.trip_id == 5
    assert booking.passenger_id == 5
    assert booking.status == "Confirmed"

def test_vehicle_not_found_returns_none():
    dao = MockVehicleDAO()
    vehicle = dao.get_vehicle_by_id(99)  # ID not present
    assert vehicle is None

def test_booking_not_found_returns_none():
    dao = MockBookingDAO()
    booking = dao.get_booking_by_id(100)  # ID not present
    assert booking is None
