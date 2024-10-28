from models.vehicle import Vehicle
from models.vehicleType import VehicleType

class ParkingSpot:
    def __init__(self, id, spot_type: VehicleType, floor, price_per_hour):
        self.id = id
        self.spot_type = spot_type
        self.available = False
        self.floor = floor
        self.price_per_hour = price_per_hour

    def get_spot_type(self):
        return self.spot_type
    
    def is_available(self):
        return self.available
    
    def update_available(self, val: bool):
        self.available = val

    def get_floor(self):
        return self.floor
    
    def get_price_per_hour(self):
        return self.price_per_hour
    
    