# Adaptee: Existing class with an incompatible interface

class SquarePeg:
    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width
    
# Target: Expected interface by the client
class RoundHole:
    def __init__(self, radius):
        self.radius = radius

    def fits(self, peg):
        return self.radius >= peg.get_radius()
    

# Adapter
class SquarePegAdapter:
    def __init__(self, square_peg):
        self.square_peg = square_peg
    
    # converts square peg width to an equivalent radius
    def get_radius(self):
        return self.square_peg.get_width() * (2 ** 0.5) / 2 # diagonal to radius
    

#Client Code
hole = RoundHole(5)
square_peg = SquarePeg(7)

adapter = SquarePegAdapter(square_peg)

if hole.fits(adapter):
    print("Square peg fits in round hole via the adapter")
else:
    print("Square peg doesn't fit in the round hole")