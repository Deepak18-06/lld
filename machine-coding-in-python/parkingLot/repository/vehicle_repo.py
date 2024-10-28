from models.vehicle import Vehicle
class VehicleRepo:
    def __init__(self):
        self.vehicles = {}

    def vehicle_exist(self, vehicle_id):
        if self.vehicles.get(vehicle_id):
            return True
        return False

    def add_vehicle(self, vehicle: Vehicle):
        if self.vehicles.get(vehicle.id):
            return "Vehicle with same id already Exists"
        self.vehicles[vehicle.id] = vehicle

    def update_vehicle(self, vehicle: Vehicle):
        if self.vehicles.get(vehicle.id):
            self.vehicles[vehicle.id] = vehicle
            return self.vehicles[vehicle.id]
        return "Vehicle not found"
    
    def get_vehicle(self, vehicle_id):
        if self.vehicles.get(vehicle_id):
            return self.vehicles.get(vehicle_id)
        return "Vehicle not found"
    
    def delete_vehicle(self, vehicle_id):
        if self.vehicle_exist:
            del self.vehicles[vehicle_id]
        return "Vehicle does not exists"