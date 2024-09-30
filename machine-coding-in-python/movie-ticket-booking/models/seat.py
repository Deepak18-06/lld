class Row:
    def __init__(self, number: str):
        self.number = number
class Seat:
    def __init__(self, number: int, row: Row):
        self.row = row.number
        self.number = number
        self.is_booked = False

class Hall:
    def __init__(self, movie, seats):
        self.movie = movie
        self.seats = seats
    def get_available_seats(self):
        return [seat for seat in self.seats if seat.is_booked == False]
    