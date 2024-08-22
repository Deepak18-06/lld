# Encapsulation - refers to binding the data and methods into a class
class Car:
    #constructor
    def __init__(self, brand):
        self.brand = brand  #public variable
        self.__speed = 0    #private variable

    #methods
    def accelerate(self, increase):
        self.__speed += increase

    def getSpeed(self):
        return self.__speed
    
## -------------------------------------------------------------------------------------------------------------##
# Inheritence -> It allows one class (child class) to inherit attributes and methods from another 
# class (parent class). This promotes code reuse and the creation of a hierarchical relationship between classes.

class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting")

class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)     #Inherit from parent
        self.model = model

    def drive(self):
        print(f"Driving the {self.brand} {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.start()  # Output: Toyota vehicle is starting
my_car.drive()  # Output: Driving the Toyota Corolla


##---------------------------------------------------------------------------------------------##

# Polymorphism allows different classes to have methods with the same name, and the correct method 
# is called depending on the object type. It provides flexibility by allowing the same interface to 
# be used for different types of objects.
    
class Bird:

    def sound(self):
        return "Chirp"
    
class Dog:

    def sound(self):
        return "Bark"
    

# Polymorphism in action
def animal_sound(animal):
    print(animal.sound())

sparrow = Bird()
bulldog = Dog()

animal_sound(sparrow)  # Output: Chirp
animal_sound(bulldog)  # Output: Bark


##--------------------------------------------------------------------------------------------------------------------##

# Abstraction means hiding the implementation details and exposing only the functionality. It can be achieved using abstract 
# classes or interfaces, although Python’s way of handling abstraction is a bit different from languages like Java

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract method, must be implemented in subclass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
