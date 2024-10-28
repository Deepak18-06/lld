class ParkingLotRepo:
    def __init__(self) -> None:
        self.parking_lots = {}

    def add_parking_lot(self, lot):
        self.parking_lots[lot.id] = lot

    def get_parking_lot(self, lot_id):
        return self.parking_lots[lot_id]