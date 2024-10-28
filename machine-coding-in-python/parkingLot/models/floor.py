class Floor:
    def __init__(self,id, parking_lot):
        self.id = id
        self.parking_lot = parking_lot
        self.spots = {}

    def add_spot(self, spot):
        self.spots[spot.id] = spot

    def get_available_spots(self):
        return [spot for spot in self.spots if spot.available == True]