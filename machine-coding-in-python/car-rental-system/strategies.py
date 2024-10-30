# strategies.py

from datetime import datetime
from repositories import VehicleRepository, ReservationRepository
from models import Reservation

class ReservationStrategy:
    def __init__(self, vehicle_repo, reservation_repo):
        self.vehicle_repo = vehicle_repo
        self.reservation_repo = reservation_repo
    
    def can_reserve(self, vehicle, from_time, to_time):
        # Check if the vehicle is available
        reservations = self.reservation_repo.get_reservations_for_vehicle(vehicle.id)
        for reservation in reservations:
            if not (to_time <= reservation.reserved_from_time or from_time >= reservation.reserved_to_time):
                return False  # Vehicle is already booked in this timeframe
        return True
    
    def reserve_vehicle(self, vehicle, user, from_time, to_time):
        if self.can_reserve(vehicle, from_time, to_time):
            reservation = Reservation(len(self.reservation_repo.reservations) + 1, vehicle, user, from_time, to_time)
            self.reservation_repo.add_reservation(reservation)
            vehicle.is_booked = True
            return reservation
        else:
            raise Exception("Vehicle is not available for the selected time.")
