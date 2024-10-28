from repository.parking_spot_repo import ParkingSpotRepo
from repository.parking_lot_repo import ParkingLotRepo

class ParkingSpotService:
    def __init__(self, parking_spot_repo: ParkingSpotRepo) -> None:
        self.parking_spot_repo = parking_spot_repo

    def add_parking(self):
        pass