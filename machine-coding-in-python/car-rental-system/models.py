# models.py

from datetime import datetime

class VehicleType:
    def __init__(self, id, name, seats, reservation_price, reg_charge):
        self.id = id
        self.name = name
        self.seats = seats
        self.reservation_price = reservation_price
        self.reg_charge = reg_charge

class Vehicle:
    def __init__(self, id, vehicle_type, is_booked=False):
        self.id = id
        self.vehicle_type = vehicle_type
        self.is_booked = is_booked

class Reservation:
    def __init__(self, id, vehicle, user, reserved_from_time, reserved_to_time, status="Confirmed"):
        self.id = id
        self.vehicle = vehicle
        self.user = user  
        self.reserved_from_time = reserved_from_time
        self.reserved_to_time = reserved_to_time
        self.status = status

class Payment:
    def __init__(self, reservation, payment_mode, amount, status="Pending"):
        self.reservation = reservation
        self.payment_mode = payment_mode
        self.amount = amount
        self.status = status

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
