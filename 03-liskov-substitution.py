"""
Subtypes should be replaceable by their base types without altering the correctness of the program.
"""
class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying"

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich cannot fly")

# Ostrich violates LSP because it cannot fly, breaking the "fly" behavior
# Fix it by abstracting flight ability
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        return "Flying"

class Ostrich(Bird):
    def move(self):
        return "Running"

def move_bird(bird: Bird):
    return bird.move()

sparrow = Sparrow()
ostrich = Ostrich()

print(move_bird(sparrow))  # Outputs: Flying
print(move_bird(ostrich))  # Outputs: Running
