from enum import Enum

class VehicalType(str, Enum):
    FOUR_WHEELER = "FOUR_WHEELER"
    TWO_WHEELER = "TWO_WHEELER"
    THREE_WHEELER = "THREE_WHEELER"
class Vehical:
    def __init__(self, registration_number: str, type: VehicalType):
        self.registration_number = registration_number
        self.type = type
        self.seats = None
        