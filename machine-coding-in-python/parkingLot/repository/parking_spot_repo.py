class ParkingSpotRepo:
    def __init__(self):
        self.parking_spots = {}

    def add_parking_spot(self, spot):
        self.parking_spots[spot.id] = spot

    def get_parking_spot(self, spot_id):
        return self.parking_spots[spot_id]
    
    def remove_parking_spot(self, spot_id):
        del self.parking_spots[spot_id]