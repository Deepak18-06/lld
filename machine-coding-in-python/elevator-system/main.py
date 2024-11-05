import abc
from collections import deque
from typing import List

# Elevator States
class ElevatorState(abc.ABC):
    @abc.abstractmethod
    def process_request(self, elevator, request):
        pass

class IdleState(ElevatorState):
    def process_request(self, elevator, request):
        if elevator.can_accommodate(request):
            elevator.current_floor = request.floor
            elevator.passengers.append(request)
            elevator.state = MovingState()
        else:
            # Add request to the queue if the elevator is at capacity
            elevator.request_queue.append(request)

class MovingState(ElevatorState):
    def process_request(self, elevator, request):
        if elevator.current_floor < request.floor:
            elevator.current_floor += 1
        elif elevator.current_floor > request.floor:
            elevator.current_floor -= 1
        else:
            # Reached the requested floor, open the doors
            elevator.open_doors()
            elevator.state = OpenDoorState()

class OpenDoorState(ElevatorState):
    def process_request(self, elevator, request):
        # Open doors, wait, then close doors
        elevator.close_doors()
        elevator.state = IdleState()
        elevator.process_next_request()

# Elevator Request
class ElevatorRequest:
    def __init__(self, origin_floor: int, destination_floor: int):
        self.origin_floor = origin_floor
        self.destination_floor = destination_floor

# Elevator
class Elevator:
    def __init__(self, num_floors: int, capacity: int):
        self.num_floors = num_floors
        self.capacity = capacity
        self.current_floor = 1
        self.passengers: List[ElevatorRequest] = []
        self.request_queue: deque[ElevatorRequest] = deque()
        self.state: ElevatorState = IdleState()

    def can_accommodate(self, request: ElevatorRequest):
        return len(self.passengers) < self.capacity

    def add_request(self, request: ElevatorRequest):
        if self.can_accommodate(request):
            self.passengers.append(request)
            self.process_next_request()
        else:
            self.request_queue.append(request)

    def process_next_request(self):
        if self.passengers:
            request = self.passengers[0]
            self.state.process_request(self, request)
        elif self.request_queue:
            request = self.request_queue.popleft()
            self.state.process_request(self, request)

    def open_doors(self):
        # Open the doors and wait for passengers to board/exit
        pass

    def close_doors(self):
        # Close the doors and prepare to move
        pass

# Elevator Controller
class ElevatorController:
    def __init__(self, num_elevators: int, num_floors: int, elevator_capacity: int):
        self.elevators: List[Elevator] = [Elevator(num_floors, elevator_capacity) for _ in range(num_elevators)]

    def add_request(self, origin_floor: int, destination_floor: int):
        request = ElevatorRequest(origin_floor, destination_floor)
        # Find the nearest available elevator that can accommodate the request
        nearest_elevator = min(self.elevators, key=lambda e: abs(e.current_floor - origin_floor) and e.can_accommodate(request))
        nearest_elevator.add_request(request)

# Example usage
controller = ElevatorController(num_elevators=3, num_floors=10, elevator_capacity=4)
controller.add_request(3, 7)
controller.add_request(7, 2)
controller.add_request(5, 5)
controller.add_request(2, 9)