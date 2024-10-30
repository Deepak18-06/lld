# Car Rental system

## Requirements
- system should be able to register cars 
- cars should have type, availability, price 
- user should be able to search car on different criteria like availability, type, price


## Core Entities
- Users
    - id (pk)
    - name
    - email
    - phone
    - role (e.g., admin, customer)

- Vehicle_type
    - id(pk)
    - name
    - seats
    - reservation_price
    - reg_charge
    - fuel_type
    - transmission_type
    - mileage

- Vehicles
    - id(pk)
    - vehicle_type_id(fk)
    - is_booked
    - availability_status (available, booked, maintenance)

- Reservations
    - id(pk)
    - vehicle_id(fk)
    - user_id(fk)
    - reserved_from_time
    - reserved_to_time
    - reserved_at
    - status (e.g., confirmed, pending, canceled)

- Payments
    - reservation_id(fk)
    - payment_mode
    - status (e.g., success, failure, pending)
    - amount
    - payment_date

    - reservation_id
    - payment_mode
    - status
    - amount

## APIs
### Reserve a vehicle
```
POST: /api/v1/reservations
Headers: 
- Authorization: JWT OR SESSION_TOKEN

Body:
{
    "vehicle_id": <integer, required>,       // ID of the vehicle to be reserved
    "from_time": <timestamp, required>,      // Start date and time of reservation
    "to_time": <timestamp, required>         // End date and time of reservation
}

Response:
Status: 201 Created
Body:
{
    "reservation": {
        "id": <reservation_id>,
        "vehicle_id": <vehicle_id>,
        "from_time": <timestamp>,
        "to_time": <timestamp>,
        "status": "reserved",                 // Or other status if applicable
        "created_at": <timestamp>
    }
}

Errors:
- 400 Bad Request: Invalid or missing `vehicle_id`, `from_time`, or `to_time`
- 401 Unauthorized: Missing or invalid token
- 404 Not Found: Vehicle with specified `vehicle_id` not found
- 409 Conflict: Vehicle is already reserved for the specified time
```
-----------------------------------------------
### Get reservation details
```
GET: /api/v1/reservations/:reservation_id
Headers:
- Authorization: JWT or Session Token

Response:
Status: 200 OK
Body:
{
    "reservation": {
        "id": <reservation_id>,
        "vehicle_id": <vehicle_id>,
        "from_time": <timestamp>,
        "to_time": <timestamp>,
        "status": <string>,           // e.g., "reserved", "completed", "cancelled"
        "created_at": <timestamp>,
        "updated_at": <timestamp>
    }
}

Errors:
- 401 Unauthorized: Missing or invalid token
- 404 Not Found: Reservation with specified `reservation_id` not found

------------------------------------------------
```
### Update reservation details
```
PUT: /api/v1/reservations/:reservation_id
Headers:
- Authorization: JWT or Session Token

Body:
{
    "from_time": <timestamp, required>,     // New start time for the reservation
    "to_time": <timestamp, required>        // New end time for the reservation
}

Response:
Status: 200 OK
Body:
{
    "reservation": {
        "id": <reservation_id>,
        "vehicle_id": <vehicle_id>,
        "from_time": <timestamp>,
        "to_time": <timestamp>,
        "status": <string>,                  // e.g., "reserved", "completed", "cancelled"
        "updated_at": <timestamp>
    }
}

Errors:
- 400 Bad Request: Invalid or missing `from_time` or `to_time`
- 401 Unauthorized: Missing or invalid token
- 404 Not Found: Reservation with specified `reservation_id` not found
- 409 Conflict: Vehicle is already reserved during the new specified time

------------------------------------------------
```
### Cancel a reservation
```
PUT: /api/v1/reservations/:reservation_id
Headers:
- Authorization: JWT or Session Token

Body:
{
    "cancel": true                  // Boolean flag to indicate cancellation
}

Response:
Status: 200 OK
Body:
{
    "reservation": {
        "id": <reservation_id>,
        "vehicle_id": <vehicle_id>,
        "from_time": <timestamp>,
        "to_time": <timestamp>,
        "status": "cancelled",      // Updated status to reflect cancellation
        "updated_at": <timestamp>
    }
}

Errors:
- 400 Bad Request: Missing or invalid `cancel` field
- 401 Unauthorized: Missing or invalid token
- 404 Not Found: Reservation with specified `reservation_id` not found
- 409 Conflict: Reservation cannot be canceled due to business rules (e.g., already completed)

------------------------------------------------
```
### Search
```
GET: api/v1/search
Query Params: 
    - query: search term
    - from_time: timestamp
    - to_time: timestamp
    - type: vehicle type
    - min_price: minimum price
    - max_price: maximum price
    - seats: minimum seat requirement
    - fuel_type: vehicle fuel type (e.g., diesel, petrol)
    - transmission_type: transmission type (e.g., automatic, manual)
    - page: page number (for pagination)
    - page_size: number of results per page
Headers: JWT or Session Token

Response: 
    {
        "vehicles": [
            {
                "id": <vehicle_id>,
                "type": <type>,
                "price": <price>,
                "seats": <seats>,
                "availability": <availability>
            },
            ...
        ],
        "pagination": {
            "current_page": <page>,
            "total_pages": <total_pages>,
            "page_size": <page_size>
        }
    }
```
### Availability
```
GET: api/v1/vehicles/:vehicle_id/availability?from_time={}&to_time={}
Headers: JWT or Session Token

Response:
    {
        "vehicle_id": <vehicle_id>,
        "is_available": true/false,
        "message": <explanation if unavailable>
    }

-----------------------------------------------------------------------
```
### Payments
```
POST: api/v1/reservations/:reservation_id/payments
Headers: JWT or Session Token
Body:
{
    "amount": <decimal>,           // Required: Payment amount
    "payment_mode": <string>       // Required: e.g., 'credit_card', 'debit_card', 'paypal'
}

Response: 
Status: 201 Created
Body:
{
    "payment": {
        "reservation_id": <reservation_id>,
        "payment_id": <payment_id>,
        "status": <string, e.g., 'success' | 'failure' | 'pending'>,
        "transaction_id": <optional, string>,  // Unique transaction ID from provider
        "created_at": <timestamp>
    }
}

Errors:
- 400 Bad Request: Missing or invalid `amount` or `payment_mode`
- 404 Not Found: Invalid `reservation_id`
- 402 Payment Required: Insufficient funds or payment declined

```
### Get payment details
```
GET: api/v1/reservations/:reservation_id/payments/:payment_id
Headers: JWT or Session Token

Response: 
Status: 200 OK
Body:
{
    "payment": {
        "payment_id": <payment_id>,
        "reservation_id": <reservation_id>,
        "status": <string, e.g., 'success' | 'failure' | 'pending'>,
        "amount": <decimal>,
        "payment_mode": <string>,
        "transaction_id": <optional, string>,
        "created_at": <timestamp>
    }
}

Errors:
- 404 Not Found: Invalid `reservation_id` or `payment_id`
- 403 Forbidden: Unauthorized access

# Callback for using external payment process
POST: api/v1/payments/callback
Headers: None (or can be restricted based on gateway security)
Body: {
    "reservation_id": <>,
    "payment_id": <>,
    "status": "success/failure/pending",
    "transaction_details": { ... }
}

Response:
    {
        "status": "received"
    }

```
    