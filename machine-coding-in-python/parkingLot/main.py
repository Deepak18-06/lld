from enum import Enum
from abc import ABC, abstractmethod

class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Vehicle:
    def __init__(self, license_plate, size):
        self.license_plate = license_plate
        self.size = size

class ParkingSlot:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def can_fit_vehicle(self, vehicle):
        return vehicle.size.value <= self.size.value

    def park_vehicle(self, vehicle):
        if self.is_available() and self.can_fit_vehicle(vehicle):
            self.vehicle = vehicle
            return True
        return False

    def remove_vehicle(self):
        self.vehicle = None

class Floor:
    def __init__(self, floor_number, slots):
        self.floor_number = floor_number
        self.slots = slots

class ParkingLot:
    def __init__(self, floors):
        self.floors = floors

class ParkingStrategy(ABC):
    @abstractmethod
    def find_available_slot(self, parking_lot, vehicle):
        pass

class FirstAvailableStrategy(ParkingStrategy):
    def find_available_slot(self, parking_lot, vehicle):
        for floor in parking_lot.floors:
            for slot in floor.slots:
                if slot.is_available() and slot.can_fit_vehicle(vehicle):
                    return floor, slot
        return None, None

class BestFitStrategy(ParkingStrategy):
    def find_available_slot(self, parking_lot, vehicle):
        best_fit = None
        best_fit_floor = None
        for floor in parking_lot.floors:
            for slot in floor.slots:
                if slot.is_available() and slot.can_fit_vehicle(vehicle):
                    if best_fit is None or slot.size.value < best_fit.size.value:
                        best_fit = slot
                        best_fit_floor = floor
        return best_fit_floor, best_fit

class ParkingSystem:
    def __init__(self, parking_lot, strategy):
        self.parking_lot = parking_lot
        self.strategy = strategy

    def park_vehicle(self, vehicle):
        floor, slot = self.strategy.find_available_slot(self.parking_lot, vehicle)
        if floor and slot:
            slot.park_vehicle(vehicle)
            return f"Vehicle parked on floor {floor.floor_number}, slot {slot.id}"
        return "No available parking slot"

    def remove_vehicle(self, license_plate):
        for floor in self.parking_lot.floors:
            for slot in floor.slots:
                if slot.vehicle and slot.vehicle.license_plate == license_plate:
                    slot.remove_vehicle()
                    return f"Vehicle removed from floor {floor.floor_number}, slot {slot.id}"
        return "Vehicle not found"

# Example usage
def create_parking_lot():
    floors = [
        Floor(1, [ParkingSlot(f"1-{i}", VehicleSize(i % 3 + 1)) for i in range(10)]),
        Floor(2, [ParkingSlot(f"2-{i}", VehicleSize(i % 3 + 1)) for i in range(10)])
    ]
    return ParkingLot(floors)

parking_lot = create_parking_lot()
first_available_system = ParkingSystem(parking_lot, FirstAvailableStrategy())
best_fit_system = ParkingSystem(parking_lot, BestFitStrategy())

# Test parking
vehicle1 = Vehicle("ABC123", VehicleSize.SMALL)
vehicle2 = Vehicle("DEF456", VehicleSize.MEDIUM)
vehicle3 = Vehicle("GHI789", VehicleSize.LARGE)

print(first_available_system.park_vehicle(vehicle1))
print(best_fit_system.park_vehicle(vehicle2))
print(first_available_system.park_vehicle(vehicle3))

# Test removing
print(first_available_system.remove_vehicle("ABC123"))
print(best_fit_system.remove_vehicle("DEF456"))
print(first_available_system.remove_vehicle("NON-EXISTENT"))