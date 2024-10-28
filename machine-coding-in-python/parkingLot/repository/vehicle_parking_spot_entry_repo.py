class VehicleParkingSpotEntryRepo:
    def __init__(self):
        self.vehicle_parking_spots_entry = {}

    def get(self, id):
        return self.vehicle_parking_spots_entry.get(id)
    
    def add(self, entry):
        self.vehicle_parking_spots_entry[entry.id] = entry
