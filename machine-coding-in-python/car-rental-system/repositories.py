# repositories.py

from models import Vehicle, Reservation, Payment, User

class VehicleRepository:
    def __init__(self):
        self.vehicles = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    
    def get_available_vehicles(self):
        return [v for v in self.vehicles if not v.is_booked]

class ReservationRepository:
    def __init__(self):
        self.reservations = []
    
    def add_reservation(self, reservation):
        self.reservations.append(reservation)
    
    def get_reservations_for_vehicle(self, vehicle_id):
        return [r for r in self.reservations if r.vehicle.id == vehicle_id]
    
    def get_reservations_for_user(self, user_id):
        return [r for r in self.reservations if r.user.id == user_id]

class PaymentRepository:
    def __init__(self):
        self.payments = []
    
    def add_payment(self, payment):
        self.payments.append(payment)

class UserRepository:
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None
