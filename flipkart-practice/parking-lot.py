"""
- drivers should be able to part a car on available space
- and unpark car. and make the space avaiable again
- multple floors in parking lot
- every floor with some parking slots
- there would a payment strategy
- slot can be of type

"""
class VehicleType:
    CAR=1
    BIKE=2
    TRUCK=3

class Slot:
    def __init__(self, id, floor_no, fits) -> None:
        self.id = id
        self.floor_no = floor_no
        self.fits = fits

class Floor:
    def __init__(self, id, number, buidling) -> None:
        self.id = id
        self.number = number
        self.building = buidling
        self.slots = list(Slot)

class ParkingLot:
    def __init__(self, name) -> None:
        self.floors = list(Floor)
        self.name = name


class SlotRepo:
    def __init__(self) -> None:
        self.slots = {}

    def add_slot(self, building, floor, slot_id):
        slot = Slot()
        self.slots[slot_id] = slot

    def get_slot(self, id):
        return self.slots[id]
    
    def update(self):
        pass

    
class FloorRepo:
    def __init__(self) -> None:
        self.floors = {}

    def add_floor(self, floor_no, building):
        floor = Floor(floor_no, buidling=building)
        self.floors.add(floor)

    def get_floor(self, id):
        return self.floors[id]
    
    def update(self):
        pass

    def delete(self):
        pass

class ParkingLotRepo:
    def __init__(self) -> None:
        self.parking_lots = {}

    def add_parking_lot(self, id, name):
        lot = ParkingLot()
        self.parking_lots[id] = lot

    def update(self):
        pass

    def delete(self):
        pass


class ParkingStrategy(ABC):
    @abstractmethod
    def park(self):
        pass

class NearestParkingStrategy(ParkingStrategy):
    def park(self):
        #logic goes here
        pass


class FairCalculationStrategy(ABC):
    @abstractmethod
    def calculate(self):
        pass

class HourlyFailCalculationStrategy(FairCalculationStrategy):
    @abstractmethod
    def calculate(self):
        #logic goes here
        pass

class ParkingServer:
    def __init__(self, parkinglotrepo, faircalcuationStrategy, parking_strategy) -> None:
        self.parkinglotrepo = parkinglotrepo
        self.faircalcuationStrategy = faircalcuationStrategy
        self.parking_strategy = parking_strategy

    def park(self, vehicle_id):
        slot = self.parking_strategy(vehicle_id)
        
    def unpark(self):
        pass


