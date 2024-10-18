"""
The Builder Pattern is a creational design pattern that helps construct complex objects step by step. 
It separates the construction of an object from its representation, allowing the same construction process 
to create different representations.

Key Concepts:
Builder: Provides a way to construct a complex object. It offers methods to configure the object step by step and a method to retrieve the final product.
Director: Often optional, but it can be used to control the building process and ensure that the steps are executed in a specific order.
Product: The final complex object that is being built.
"""

#product class

class Car:
    def __init__(self,engine=None, wheels=None, color=None):
        self.engine = engine
        self.wheels = wheels
        self.color = color

#Builder Class
class CarBuilder:
    def __init__(self) -> None:
        self.engine = None
        self.wheels = None
        self.color = None

    def set_engine(self, engine):
        self.engine = engine
        return self
    def set_wheels(self, wheels):
        self.wheels = wheels
        return self
    def set_color(self, color):
        self.color = color
        return self
    def build(self):
        return Car(self.engine, self.wheels, self.color)

builder = CarBuilder()
car = builder.set_engine("V8").set_wheels(4).set_color("red").build()
print(car)