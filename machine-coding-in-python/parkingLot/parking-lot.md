# Parking Lot

## Requirements
- Parking lot should have multiple floors
- Parking lot should have multple spots on each floor
- Each spot should have a vehicle type to park
- Each spot should have price associated with spot
- Price should be price per hour


### Vehicle
- id(pk)
- license_no
- type(fk)
- name
- color

### VehicleType
- id
- type
- max_length
- max_breadth

a parking_spot belongs to floor and floor has many parking_slots

### parking_spot
- id(pk)
- parking_floor_id(fk)
- vehicle_type_id(fk)
- is_available
- price_per_hour

a vehicle can be parked many time and a parking spot can be used many times by cars

### vehicle_parking_spot
- id
- vehicle_id
- parking_spot_id
- parked_at
- unparked_at

### trasaction
- id (PK)
- vehicle_parking_spot_id (FK)
- total_price
- payment_mode
- payment_status
- paid_at (timestamp)
- currency (optional)



a parking lot has many parking_floors, and a parking floor belongs to parking_lot
### parking_floor
- id(pk)
- parking_lot_id(fk)

### parking_lot
- id
- name
