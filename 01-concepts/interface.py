from abc import ABC, abstractmethod

# Interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def eat(self):
        pass

# Concrete classes implementing the interface
class Dog(Animal):
    def speak(self):
        return "Woof"

    def eat(self):
        return "Eating bones"

class Cat(Animal):
    def speak(self):
        return "Meow"

    def eat(self):
        return "Eating fish"

# Function that accepts objects implementing the Animal interface
def describe_animal(animal):
    print(f"The animal says: {animal.speak()}")
    print(f"The animal is eating: {animal.eat()}")

# Usage
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    describe_animal(dog)
    print()
    describe_animal(cat)
