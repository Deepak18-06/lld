from enum import Enum
from models.user import User

class CabType(str, Enum):
    MINI = "mini"
    XL = "xl"
    BLACK = "black"

class Location:
    def __init__(self, lattitude: float, longitude: float) -> None:
        self.lattitude = lattitude
        self.longitude = longitude


class Cab:
    def __init__(self, driver: User, registration_no: str, location: Location, cab_type: CabType) -> None:
        self.id = None
        self.driver = driver
        self.registration_no = registration_no
        self.location = location
        self.is_available = False
        self.cab_type = cab_type