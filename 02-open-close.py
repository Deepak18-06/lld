"""
Software entities (classes, modules, functions) should be open for extension but closed for modification.
"""

from abc import ABC, abstractmethod

# Base class for different types of discounts
class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass

class NoDiscount(Discount):
    def apply(self, price):
        return price

class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price - (price * self.percent / 100)

# Order class, now closed for modification but open for extension via discounts
class Order:
    def __init__(self, price, discount: Discount):
        self.price = price
        self.discount = discount

    def get_total(self):
        return self.discount.apply(self.price)

order = Order(100, PercentageDiscount(10))
print(order.get_total())  # Outputs 90.0
