"""
The Factory Pattern is a creational design pattern that provides an interface for creating objects in a 
superclass, but allows subclasses to alter the type of objects that will be created. The goal is to delegate 
the responsibility of object creation to a separate class or method.

This pattern is useful when the exact type of object to be created is determined at runtime, or when you want 
to encapsulate the logic of object creation in one place.

Example: Shape Factory
Consider a scenario where you need to create different shapes (Circle, Square, Rectangle) without directly instantiating them. 
You can use the Factory Pattern to centralize the object creation logic.
"""

from abc import ABC, abstractmethod

# Step 1: Define the common interface (Shape)
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Step 2: Implement concrete classes for each shape
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

# Step 3: Create the Factory class that will create the objects
class ShapeFactory:
    def create_shape(self, shape_type: str) -> Shape:
        if shape_type == 'Circle':
            return Circle()
        elif shape_type == 'Square':
            return Square()
        elif shape_type == 'Rectangle':
            return Rectangle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Step 4: Use the factory to create objects
factory = ShapeFactory()

# Create a Circle
shape1 = factory.create_shape('Circle')
print(shape1.draw())  # Outputs: Drawing a Circle

# Create a Square
shape2 = factory.create_shape('Square')
print(shape2.draw())  # Outputs: Drawing a Square

# Create a Rectangle
shape3 = factory.create_shape('Rectangle')
print(shape3.draw())  # Outputs: Drawing a Rectangle
