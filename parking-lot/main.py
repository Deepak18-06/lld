"""
Requirements
- multiple levels each with certain number of spots
- the parking lot should support parking of different types of vehicles, like car, bike, truck etc
- each parking spot should be able to accomodate a specific type of vehicle
- system should assign parking to a vehicle on entry and free the slot on exit
- system should track the availability of spots and provide real-time info to customer
- the system should handle multple entry and exit points and support concurrent access
"""

from enum import Enum
import datetime
import math

class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3

class Vehicle:
    def __init__(self, vehicle_type: VehicleType):
        self.vehicle_type = vehicle_type

class PricingStrategy:
    def __init__(self):
        # Define hourly rates for different vehicle types
        self.prices = {
            VehicleType.CAR: 10,   # Car: $10 per hour
            VehicleType.BIKE: 5,   # Bike: $5 per hour
            VehicleType.TRUCK: 20  # Truck: $20 per hour
        }
    
    def calculate_price(self, vehicle_type: VehicleType, duration_in_hours: float):
        # Calculate total cost based on the vehicle type and parking duration
        rate_per_hour = self.prices.get(vehicle_type, 0)
        return rate_per_hour * duration_in_hours

class ParkingSlot:
    def __init__(self, slot_id, floor_number, slot_type: VehicleType):
        self.id = slot_id
        self.floor_no = floor_number
        self.slot_type = slot_type
        self.vehicle = None
        self.parking_time = None
        self.pricing_strategy = PricingStrategy()

    def isAvailable(self):
        return self.vehicle is None
    
    def park(self, vehicle: Vehicle):
        if self.isAvailable() and vehicle.vehicle_type == self.slot_type:
            self.vehicle = vehicle
            self.parking_time = datetime.datetime.now()
            print(f"Vehicle parked at slot {self.id} on floor {self.floor_no}.")
        else:
            print(f"Cannot park vehicle. Slot {self.id} is unavailable or vehicle type mismatch.")

    def unpark(self):
        if self.vehicle:
            # Calculate parking duration in hours
            parking_duration = (datetime.datetime.now() - self.parking_time).total_seconds() / 3600
            parking_duration = math.ceil(parking_duration)  # Round up to the nearest hour

            # Calculate parking cost based on the vehicle type and duration
            parking_cost = self.pricing_strategy.calculate_price(self.vehicle.vehicle_type, parking_duration)

            print(f"Slot {self.id} is now free. Vehicle was parked for {parking_duration} hours.")
            print(f"Total parking cost: ${parking_cost:.2f}")
            
            # Reset the slot to available
            self.vehicle = None
            self.parking_time = None
        else:
            print(f"Slot {self.id} is already empty.")

class Floor:
    def __init__(self, floor_id):
        self.id = floor_id
        self.slots = []

    def addSlot(self, slot: ParkingSlot):
        self.slots.append(slot)

    def removeSlot(self, slot: ParkingSlot):
        self.slots.remove(slot)

    def getAvailableSlot(self, vehicle_type: VehicleType):
        for slot in self.slots:
            if slot.isAvailable() and slot.slot_type == vehicle_type:
                return slot
        return None

class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.floors = []

    def addFloor(self, floor: Floor):
        self.floors.append(floor)

    def removeFloor(self, floor: Floor):
        self.floors.remove(floor)

    def findParkingSlot(self, vehicle: Vehicle):
        for floor in self.floors:
            slot = floor.getAvailableSlot(vehicle.vehicle_type)
            if slot:
                return slot
        return None

    def parkVehicle(self, vehicle: Vehicle):
        slot = self.findParkingSlot(vehicle)
        if slot:
            slot.park(vehicle)
        else:
            print("No available slot for this vehicle.")

    def unparkVehicle(self, slot_id, floor_id):
        for floor in self.floors:
            if floor.id == floor_id:
                for slot in floor.slots:
                    if slot.id == slot_id:
                        slot.unpark()
                        return
        print("Slot not found.")

# Example usage
car = Vehicle(VehicleType.CAR)
bike = Vehicle(VehicleType.BIKE)
truck = Vehicle(VehicleType.TRUCK)

lot = ParkingLot("Main Lot")

# Create floors and slots
floor1 = Floor(1)
floor1.addSlot(ParkingSlot(101, 1, VehicleType.CAR))
floor1.addSlot(ParkingSlot(102, 1, VehicleType.BIKE))

floor2 = Floor(2)
floor2.addSlot(ParkingSlot(201, 2, VehicleType.CAR))
floor2.addSlot(ParkingSlot(202, 2, VehicleType.TRUCK))

# Add floors to the parking lot
lot.addFloor(floor1)
lot.addFloor(floor2)

# Park vehicles
lot.parkVehicle(car)
lot.parkVehicle(bike)
lot.parkVehicle(truck)

# Simulate parking duration by adjusting `self.parking_time` manually for testing

# Unpark vehicles and calculate fees
lot.unparkVehicle(101, 1)
lot.unparkVehicle(102, 1)
lot.unparkVehicle(202, 2)
