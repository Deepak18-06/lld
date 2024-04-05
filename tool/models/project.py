
class Country:
    def __init__(self, name: str, code: str) -> None:
        self.name = name
        self.code = code
        self.states = []
class State:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.cities = []

class Location:
    def __init__(self, lat: float, long: float):
        self.lat: float = lat
        self.long: float = long
class City:
    def __init__(self, name: str, state: State, country: Country):
        self.name = name
        self.state = state
        self.country = country

class Address:
    def __init__(self, plot: str, street: str, city: City, state: State, country: Country, pinCode: int, location: Location):
        self.plot = plot
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.location = location
        self.pinCode = pinCode

class Project:
    def __init__(self, name, address: Address):
        self.name = name
        self.address = address