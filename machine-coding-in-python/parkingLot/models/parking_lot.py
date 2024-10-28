class ParkingLot:
    def __init__(self, name) -> None:
        self.name = name
        self.floors = {}

    def add_floor(self, floor):
        self.floors[floor.id] = floor

    def get_available_spots(self):
        available_spots = {}
        for id, floor in self.floors:
            available_spots[id] = floor.get_available_spots()
        return available_spots