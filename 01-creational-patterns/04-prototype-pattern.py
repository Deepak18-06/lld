"""
The Prototype Pattern is a creational design pattern used to create objects by copying an existing object, 
known as the prototype, rather than creating a new instance from scratch. It allows you to create new objects 
by cloning a prototype, which is particularly useful when creating objects is costly or complex.

Key Concepts:
Prototype: An existing object that is cloned to create new objects.
Client: The code that creates new objects by asking the prototype to clone itself.
Cloning: The process of making an exact copy of the prototype object.
When to Use:
When object creation is expensive (e.g., requires database access or heavy computation).
When instances of a class have only a few different combinations of state and these states need to be duplicated frequently.
When you want to avoid subclasses of an object creator (as in the Factory Method) and prefer copying an existing object.
"""

import copy

# Prototype class
class Shape:
    def __init__(self, type) -> None:
        self.type = type

    def clone(self):
        return copy.copy(self)
    
    def draw(self):
        raise NotImplementedError("Subclass must implement 'draw' method")
    
# Concrete prototypes
class Circle(Shape):
    def __init__(self) -> None:
        super().__init__("Circle")
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def __init__(self) -> None:
        super().__init__("Square")
    def draw(self):
        print("Drawing a Square")

circle = Circle()
square = Square()
circle.draw()
square.draw()

#cloning the existing instance
another_circle = circle.clone()
another_square = square.clone()
another_circle.draw()
another_square.draw()