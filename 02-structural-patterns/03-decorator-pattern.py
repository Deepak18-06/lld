"""
The Decorator Pattern is a structural design pattern that allows behavior to be added to individual objects, either statically 
or dynamically, without affecting the behavior of other objects from the same class. It is often used to 
adhere to the Open/Closed Principle by allowing extensions without modifying existing code.
"""


from abc import ABC, abstractmethod

# Component
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Simple Coffee"

# Decorator (abstract class)
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1.5

    def description(self):
        return self._coffee.description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5

    def description(self):
        return self._coffee.description() + ", Sugar"

class ChocolateDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", Chocolate"

# Usage Example:
simple_coffee = SimpleCoffee()
print(f"{simple_coffee.description()} : ${simple_coffee.cost()}")  # Outputs: Simple Coffee : $5

# Add Milk
coffee_with_milk = MilkDecorator(simple_coffee)
print(f"{coffee_with_milk.description()} : ${coffee_with_milk.cost()}")  # Outputs: Simple Coffee, Milk : $6.5

# Add Milk and Sugar
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(f"{coffee_with_milk_and_sugar.description()} : ${coffee_with_milk_and_sugar.cost()}")  # Outputs: Simple Coffee, Milk, Sugar : $7.0

# Add Milk, Sugar, and Chocolate
coffee_with_all = ChocolateDecorator(coffee_with_milk_and_sugar)
print(f"{coffee_with_all.description()} : ${coffee_with_all.cost()}")  # Outputs: Simple Coffee, Milk, Sugar, Chocolate : $9.0
