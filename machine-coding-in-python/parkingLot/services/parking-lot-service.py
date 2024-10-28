from repository.parking_spot_repo import ParkingSpotRepo
from repository.transaction_repo import TransactionRepo
from repository.vehicle_parking_spot_entry_repo import VehicleParkingSpotEntryRepo
from repository.vehicle_repo import VehicleRepo
from repository.parking_lot_repo import ParkingLotRepo
from models.floor import Floor
from models.parking_spot import ParkingSpot
from models.parking_lot import ParkingLot


class ParkingLotService:
    def __init__(self, parking_lot_repo: ParkingLotRepo) -> None:
        self.parking_lot_repo = parking_lot_repo

    def create_parking_lot(self, name):
        lot = ParkingLot(name)
        self.parking_lot_repo.add_parking_lot(lot)
        return lot
    
    def get_parking_lot(self, lot_id):
        self.parking_lot_repo.get(lot_id)

    def add_floor(self):
        pass