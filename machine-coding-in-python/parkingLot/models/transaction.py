class Transaction:
    def __init__(self, id, vehicle_parking_spot_entry, total_price, payment_mode, payment_status, paid_at, currency=None):
        self.id = id
        self.vehicle_parking_spot_entry = vehicle_parking_spot_entry
        self.total_price = total_price
        self.payment_mode = payment_mode
        self.payment_status = payment_status
        self.paid_at = paid_at
        self.currency = currency

        