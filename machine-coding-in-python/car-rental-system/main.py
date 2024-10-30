# main.py

from datetime import datetime, timedelta
from models import VehicleType, Vehicle
from repositories import VehicleRepository, ReservationRepository, PaymentRepository, UserRepository
from strategies import ReservationStrategy
from services import UserService

def main():
    # Initialize repositories
    vehicle_repo = VehicleRepository()
    reservation_repo = ReservationRepository()
    payment_repo = PaymentRepository()
    user_repo = UserRepository()

    # Initialize services
    user_service = UserService(user_repo)

    # Create vehicle types
    sedan = VehicleType(1, "Sedan", 5, 20, 5)
    suv = VehicleType(2, "SUV", 7, 30, 10)

    # Add vehicles
    vehicle_repo.add_vehicle(Vehicle(1, sedan))
    vehicle_repo.add_vehicle(Vehicle(2, suv))

    # Register a user
    user = user_service.register_user("John Doe", "john@example.com")
    print(f"User registered: {user.name} with email {user.email}")

    # Initialize reservation strategy
    reservation_strategy = ReservationStrategy(vehicle_repo, reservation_repo)

    # Attempt to reserve a vehicle
    from_time = datetime.now() + timedelta(days=1)  # Reserve for tomorrow
    to_time = from_time + timedelta(days=1)  # 1-day reservation

    try:
        reserved_vehicle = reservation_strategy.reserve_vehicle(vehicle_repo.get_available_vehicles()[0], user, from_time, to_time)
        print(f"Reservation successful: {reserved_vehicle.id} from {reserved_vehicle.reserved_from_time} to {reserved_vehicle.reserved_to_time}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
