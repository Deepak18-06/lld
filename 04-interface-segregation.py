"""
A client should not be forced to implement interfaces it doesn't use.
"""

from abc import ABC, abstractmethod

# Violating ISP - forcing all animals to implement both fly and walk
class Animal(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def walk(self):
        pass

# Fixing it by segregating interfaces
class Walker(ABC):
    @abstractmethod
    def walk(self):
        pass

class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass

class Dog(Walker):
    def walk(self):
        return "Dog walking"

class Bird(Walker, Flyer):
    def walk(self):
        return "Bird walking"
    
    def fly(self):
        return "Bird flying"

dog = Dog()
bird = Bird()

print(dog.walk())  # Outputs: Dog walking
print(bird.walk())  # Outputs: Bird walking
print(bird.fly())   # Outputs: Bird flying
