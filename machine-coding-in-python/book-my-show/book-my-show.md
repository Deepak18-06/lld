# BookMyShow

## Functional Requirements
- theater mangement
- show management
- use management
- user can book a ticket for a movie
- user can search on basis of title, date, time

## Core Entities
- Theaters
    - theater_id (PK)
    - name
    - location
- Screens
    - screen_id (PK)
    - theater_id (FK to Theaters)
    - screen_number

- Movies
    - movie_id (PK)
    - title
    - duration
    - genre
    - release_date

- Shows
    - show_id (PK)
    - screen_id (FK to Screens)
    - movie_id (FK to Movies)
    - start_time
    - end_time

- Bookings
    - booking_id (PK)
    - show_id (FK to Shows)
    - user_id (FK to Users)
    - status (Booked, Cancelled)
    - seats (stores booked seat numbers as an array or JSON)

- Users
    - user_id (PK)
    - name
    - email

- Admins
    - admin_id (PK)
    - name
    - email

## API
```json
Authentication
POST /login - User/Admin login
User APIs

Movie Search
GET /movies?title={title}
Description: Search for movies by title.
Response: List of movies matching the title.

Show Times for a Movie
GET /movies/{movie_id}/shows
Description: List all shows for a specific movie.
Response: List of shows with screen and theater details.

Book Tickets
POST /bookings
Request Body: { "show_id": 123, "user_id": 456, "seats": [5, 6, 7] }
Response: Booking confirmation with booking details.

Cancel Booking
DELETE /bookings/{booking_id}
Response: Confirmation of cancellation.


Admin APIs

Add a New Movie
POST /admin/movies
Request Body: { "title": "Movie Name", "duration": "120", "genre": "Action", "release_date": "2024-12-12" }
Response: Movie added confirmation.

Schedule a Show for a Movie
POST /admin/shows
Request Body: { "movie_id": 123, "screen_id": 456, "start_time": "2024-11-06T14:00:00", "end_time": "2024-11-06T16:00:00" }
Response: Show scheduled confirmation.

```
