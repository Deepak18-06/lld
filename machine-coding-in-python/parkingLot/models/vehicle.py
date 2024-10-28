from models.vehicleType import VehicleType

class Vehicle:
    def __init__(self,type: VehicleType, license_no: str, name='', color=''):
        self.id = license_no
        self.type = type
        self.license_no = license_no
        self.name = name
        self.color = color

    def set_type(self, type: VehicleType):
        self.type = type

    def get_type(self):
        return self.type

    def get_license_no(self):
        return self.license_no
    
    def get_color(self):
        return self.color
    
    def get_name(self):
        return self.name
    