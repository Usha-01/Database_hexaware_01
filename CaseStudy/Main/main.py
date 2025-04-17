from dao.VehicleDao import VehicleDAO
from dao.RouteDao import RouteDAO
from dao.TripDao import TripDAO
from dao.PassengerDao import PassengerDAO
from dao.BookingDao import BookingDAO
from entity.Vehicle import Vehicle
from entity.Route import Route
from entity.Trip import Trip
from entity.Passenger import Passenger
from entity.Booking import Booking
from ExceptionHandling.exception import InvalidEmailException
from ExceptionHandling.exception import BookingNotFoundException

def main():
    menu_options = {
        '1': vehicle_menu,
        '2': route_menu,
        '3': trip_menu,
        '4': passenger_menu,
        '5': booking_menu,
        '6': exit_program
    }

    while True:
        print("\n=== Transport Management System ===")
        print("1. Vehicle Management")
        print("2. Route Management")
        print("3. Trip Management")
        print("4. Passenger Management")
        print("5. Booking Management")
        print("6. Exit")

        choice = input("Enter your choice: ")
        menu_function = menu_options.get(choice)
        if menu_function:
            menu_function()
        else:
           print("Invalid choice. Please try again.")

def exit_program():
    print("Thank you for using the Transport Management System. Goodbye!")
    exit()

def vehicle_menu():
    dao = VehicleDAO()
    while True:
        print("\n--- Vehicle Menu ---")
        print("1. Add Vehicle")
        print("2. View Vehicle by ID")
        print("3. Update Vehicle")
        print("4. Delete Vehicle")
        print("5. View All Vehicles")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            model = input("Enter vehicle model: ")
            capacity = int(input("Enter vehicle capacity: "))
            vehicle_type = input("Enter vehicle type: ")
            status = input("Enter vehicle status: ")
            vehicle = Vehicle(model=model, capacity=capacity, type=vehicle_type, status=status)
            dao.create_vehicle(vehicle)
            print("Vehicle added successfully!")
        elif choice == '2':
            vehicle_id = int(input("Enter vehicle ID: "))
            vehicle = dao.get_vehicle_by_id(vehicle_id)
            print(vehicle)
        elif choice == '3':
            vehicle_id = int(input("Enter vehicle ID to update: "))
            model = input("Enter new model: ")
            capacity = int(input("Enter new capacity: "))
            vehicle_type = input("Enter new type: ")
            status = input("Enter new status: ")
            updated_vehicle = Vehicle(vehicle_id=vehicle_id, model=model, capacity=capacity, type=vehicle_type, status=status)
            dao.update_vehicle(updated_vehicle)
            print("Vehicle updated successfully!")
        elif choice == '4':
            vehicle_id = int(input("Enter vehicle ID to delete: "))
            dao.delete_vehicle(vehicle_id)
            print("Vehicle deleted successfully!")
        elif choice == '5':
            vehicles = dao.get_all_vehicles()
            for vehicle in vehicles:
                print(vehicle)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def route_menu():
    dao = RouteDAO()
    while True:
        print("\n--- Route Menu ---")
        print("1. Add Route")
        print("2. View Route by ID")
        print("3. Update Route")
        print("4. Delete Route")
        print("5. View All Routes")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            start_destination = input("Enter start destination: ")
            end_destination = input("Enter end destination: ")
            distance = float(input("Enter distance: "))
            route = Route(start_destination=start_destination, end_destination=end_destination, distance=distance)
            dao.create_route(route)
            print("Route added successfully!")
        elif choice == '2':
            route_id = int(input("Enter route ID: "))
            route = dao.get_route_by_id(route_id)
            print(route)
        elif choice == '3':
            route_id = int(input("Enter route ID to update: "))
            start_destination = input("Enter new start destination: ")
            end_destination = input("Enter new end destination: ")
            distance = float(input("Enter new distance: "))
            updated_route = Route(route_id=route_id, start_destination=start_destination, end_destination=end_destination, distance=distance)
            dao.update_route(updated_route)
            print("Route updated successfully!")
        elif choice == '4':
            route_id = int(input("Enter route ID to delete: "))
            dao.delete_route(route_id)
            print("Route deleted successfully!")
        elif choice == '5':
            routes = dao.get_all_routes()
            for route in routes:
                print(route)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def trip_menu():
    dao = TripDAO()
    while True:
        print("\n--- Trip Menu ---")
        print("1. Add Trip")
        print("2. View Trip by ID")
        print("3. Update Trip")
        print("4. Delete Trip")
        print("5. View All Trips")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle_id = int(input("Enter vehicle ID: "))
            route_id = int(input("Enter route ID: "))
            departure_date = input("Enter departure date (YYYY-MM-DD): ")
            arrival_date = input("Enter arrival date (YYYY-MM-DD): ")
            status = input("Enter trip status: ")
            trip_type = input("Enter trip type: ")
            max_passengers = int(input("Enter max passengers: "))
            trip = Trip(vehicle_id=vehicle_id, route_id=route_id, departure_date=departure_date, arrival_date=arrival_date, status=status, trip_type=trip_type, max_passengers=max_passengers)
            dao.create_trip(trip)
            print("Trip added successfully!")
        elif choice == '2':
            trip_id = int(input("Enter trip ID: "))
            trip = dao.get_trip_by_id(trip_id)
            print(trip)
        elif choice == '3':
            trip_id = int(input("Enter trip ID to update: "))
            vehicle_id = int(input("Enter new vehicle ID: "))
            route_id = int(input("Enter new route ID: "))
            departure_date = input("Enter new departure date (YYYY-MM-DD): ")
            arrival_date = input("Enter new arrival date (YYYY-MM-DD): ")
            status = input("Enter new status: ")
            trip_type = input("Enter new trip type: ")
            max_passengers = int(input("Enter new max passengers: "))
            updated_trip = Trip(trip_id=trip_id, vehicle_id=vehicle_id, route_id=route_id, departure_date=departure_date, arrival_date=arrival_date, status=status, trip_type=trip_type, max_passengers=max_passengers)
            dao.update_trip(updated_trip)
            print("Trip updated successfully!")
        elif choice == '4':
            trip_id = int(input("Enter trip ID to delete: "))
            dao.delete_trip(trip_id)
            print("Trip deleted successfully!")
        elif choice == '5':
            trips = dao.get_all_trips()
            for trip in trips:
                print(trip)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


def passenger_menu():
    dao = PassengerDAO()
    while True:
        print("\n--- Passenger Menu ---")
        print("1. Add Passenger")
        print("2. View Passenger by ID")
        print("3. Update Passenger")
        print("4. Delete Passenger")
        print("5. View All Passengers")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            gender = input("Enter gender: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            passenger = Passenger(first_name=first_name, gender=gender, age=age, email=email, phone_number=phone_number)
            try:
                dao.create_passenger(passenger)
                print("Passenger added successfully!")
            except InvalidEmailException as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == '2':
            passenger_id = int(input("Enter passenger ID: "))
            passenger = dao.get_passenger_by_id(passenger_id)
            print(passenger)

        elif choice == '3':
            passenger_id = int(input("Enter passenger ID to update: "))
            first_name = input("Enter new first name: ")
            gender = input("Enter new gender: ")
            age = int(input("Enter new age: "))
            email = input("Enter new email: ")
            phone_number = input("Enter new phone number: ")
            updated_passenger = Passenger(passenger_id=passenger_id, first_name=first_name, gender=gender, age=age, email=email, phone_number=phone_number)
            try:
                dao.update_passenger(updated_passenger)
                print("Passenger updated successfully!")
            except InvalidEmailException as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == '4':
            passenger_id = int(input("Enter passenger ID to delete: "))
            dao.delete_passenger(passenger_id)
            print("Passenger deleted successfully!")

        elif choice == "5":
            try:
                passengers = dao.get_all_passengers()
                if not passengers:
                    print("No passengers found.")
                else:
                    for p in passengers:
                        print(
                            f"ID: {p.passenger_id}, Name: {p.first_name}, Gender: {p.gender}, Age: {p.age}, Email: {p.email}, Phone: {p.phone_number}")
            except Exception as e:
                print("An error occurred while fetching passengers:", e)

        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def booking_menu():
    dao = BookingDAO()
    while True:
        print("\n--- Booking Menu ---")
        print("1. Add Booking")
        print("2. View Booking by ID")
        print("3. Update Booking")
        print("4. Delete Booking")
        print("5. View All Bookings")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            trip_id = int(input("Enter trip ID: "))
            passenger_id = int(input("Enter passenger ID: "))
            booking_date = input("Enter booking date (YYYY-MM-DD): ")
            status = input("Enter booking status: ")
            booking = Booking(trip_id=trip_id, passenger_id=passenger_id, booking_date=booking_date, status=status)
            dao.create_booking(booking)
            print("Booking added successfully!")

        elif choice == '2':
            booking_id = int(input("Enter booking ID: "))
            try:
                booking = dao.get_booking_by_id(booking_id)
                print(booking)
            except BookingNotFoundException as e:
                print(f"Error: {e}")

        elif choice == '3':
            booking_id = int(input("Enter booking ID to update: "))
            trip_id = int(input("Enter new trip ID: "))
            passenger_id = int(input("Enter new passenger ID: "))
            booking_date = input("Enter new booking date (YYYY-MM-DD): ")
            status = input("Enter new status: ")
            updated_booking = Booking(booking_id=booking_id, trip_id=trip_id, passenger_id=passenger_id, booking_date=booking_date, status=status)
            try:
                dao.update_booking(updated_booking)
                print("Booking updated successfully!")
            except BookingNotFoundException as e:
                print(f"Error: {e}")

        elif choice == '4':
            booking_id = int(input("Enter booking ID to delete: "))
            try:
                dao.delete_booking(booking_id)
                print("Booking deleted successfully!")
            except BookingNotFoundException as e:
                print(f"Error: {e}")

        elif choice == '5':
            try:
                bookings = dao.get_all_bookings()
                for booking in bookings:
                    print(booking)
            except BookingNotFoundException as e:
                print(f"Error: {e}")

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
