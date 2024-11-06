# db/database.py

class Database:
    def __init__(self):
        self.theaters = []
        self.screens = []
        self.movies = []
        self.shows = []
        self.bookings = []
        self.users = []
    
    def add(self, collection_name, item):
        collection = getattr(self, collection_name)
        collection.append(item)
        return item

    def get_all(self, collection_name):
        return getattr(self, collection_name)
    
    def find_by_id(self, collection_name, item_id):
        collection = getattr(self, collection_name)
        return next((item for item in collection if item.id == item_id), None)

database = Database()


# models/theater.py

class Theater:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location
        self.screens = []

    def add_screen(self, screen):
        self.screens.append(screen)


# models/screen.py

class Screen:
    def __init__(self, id, theater_id, screen_number):
        self.id = id
        self.theater_id = theater_id
        self.screen_number = screen_number
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)


# models/movie.py

class Movie:
    def __init__(self, id, title, duration, genre, release_date):
        self.id = id
        self.title = title
        self.duration = duration
        self.genre = genre
        self.release_date = release_date


# models/show.py

class Show:
    def __init__(self, id, screen_id, movie_id, start_time, end_time):
        self.id = id
        self.screen_id = screen_id
        self.movie_id = movie_id
        self.start_time = start_time
        self.end_time = end_time
        self.booked_seats = []

    def get_available_seats(self, total_seats=100):
        return [seat for seat in range(1, total_seats + 1) if seat not in self.booked_seats]

    def book_seats(self, seats):
        self.booked_seats.extend(seats)


# models/booking.py

class Booking:
    def __init__(self, id, show_id, user_id, seats):
        self.id = id
        self.show_id = show_id
        self.user_id = user_id
        self.seats = seats
        self.status = "BOOKED"

    def cancel(self):
        self.status = "CANCELLED"

# repositories/movie_repository.py

class MovieRepository:
    def find_by_title(self, title):
        return [movie for movie in database.get_all("movies") if title.lower() in movie.title.lower()]
    
    def add_movie(self, movie):
        return database.add("movies", movie)
    
# repositories/booking_repository.py

class BookingRepository:
    def add_booking(self, booking):
        return database.add("bookings", booking)

    def find_by_id(self, booking_id):
        return database.find_by_id("bookings", booking_id)
    
class ShowRepository:
    def find_by_id(self, show_id):
        return database.find_by_id("shows", show_id)

    def add_show(self, show):
        return database.add("shows", show)


# services/movie_service.py

class MovieService:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def search_movies(self, title):
        return self.movie_repository.find_by_title(title)


# services/booking_service.py

class BookingService:
    def __init__(self, booking_repository, show_repository):
        self.booking_repository = booking_repository
        self.show_repository = show_repository

    def book_tickets(self, show_id, user_id, seats):
        show = self.show_repository.find_by_id(show_id)
        if not show:
            raise Exception("Show not found.")

        available_seats = show.get_available_seats()
        if all(seat in available_seats for seat in seats):
            booking = Booking(id=len(database.get_all("bookings")) + 1, show_id=show_id, user_id=user_id, seats=seats)
            self.booking_repository.add_booking(booking)
            show.book_seats(seats)
            return booking
        else:
            raise Exception("One or more selected seats are not available.")

    def cancel_booking(self, booking_id):
        booking = self.booking_repository.find_by_id(booking_id)
        if booking:
            booking.cancel()
            return booking
        else:
            raise Exception("Booking not found.")

    def __init__(self, booking_repository, show_repository):
        self.booking_repository = booking_repository
        self.show_repository = show_repository

    def book_tickets(self, show_id, user_id, seats):
        show = self.show_repository.find_by_id(show_id)
        available_seats = show.get_available_seats()

        if all(seat in available_seats for seat in seats):
            booking = Booking(id=len(database.get_all("bookings")) + 1, show_id=show_id, user_id=user_id, seats=seats)
            self.booking_repository.add_booking(booking)
            show.book_seats(seats)
            return booking
        else:
            raise Exception("One or more selected seats are not available.")

    def cancel_booking(self, booking_id):
        booking = self.booking_repository.find_by_id(booking_id)
        if booking:
            booking.cancel()
            return booking
        else:
            raise Exception("Booking not found.")


# main.py

# Setup Repositories
movie_repo = MovieRepository()
booking_repo = BookingRepository()
show_repo = ShowRepository()  # Initialize ShowRepository

# Setup Services
movie_service = MovieService(movie_repo)
booking_service = BookingService(booking_repo, show_repo)  # Pass show_repo here

# Adding movies (Admin Functionality)
movie1 = Movie(id=1, title="Inception", duration=148, genre="Sci-Fi", release_date="2010-07-16")
movie_repo.add_movie(movie1)

# Adding a show for the movie
show1 = Show(id=1, screen_id=1, movie_id=1, start_time="2024-11-06T14:00:00", end_time="2024-11-06T16:00:00")
show_repo.add_show(show1)  # Use show_repo to add the show

# Searching for a movie
print("Search for 'Inception':")
print(movie_service.search_movies("Inception"))

# Booking tickets (User Functionality)
print("\nBooking tickets for Show ID 1, User ID 1:")
booking = booking_service.book_tickets(show_id=1, user_id=1, seats=[5, 6, 7])
print(f"Booking Confirmed: {booking.__dict__}")

# Cancelling a booking
print("\nCancelling the booking:")
cancelled_booking = booking_service.cancel_booking(booking.id)
print(f"Booking Cancelled: {cancelled_booking.__dict__}")
