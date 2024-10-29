from repository.parking_spot_repo import ParkingSpotRepo
from repository.parking_lot_repo import ParkingLotRepo

class ParkingSpotService:
    def __init__(self, parking_spot_repo: ParkingSpotRepo, parking_lot_repo) -> None:
        self.parking_spot_repo = parking_spot_repo
        self.parking_lot_repo = parking_lot_repo

    def add_parking_spot(self, spot, floor_id):
        pass