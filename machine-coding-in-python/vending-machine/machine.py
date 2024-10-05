from abc import ABC, abstractmethod
from enum import Enum
from collections import defaultdict
from typing import Dict, List

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Note(Enum):
    ONE = 1
    FIVE = 5
    TEN = 10
    TWENTY = 20
    FIFTY = 50
    HUNDRED = 100

class Coin(Enum):
    PENNY = 0.01
    NICKEL = 0.05
    DIME = 0.1
    QUARTER = 0.25


class Inventory:
    def __init__(self):
        self.products = {}
    def add_product(self, product: Product, quantity: int):
        self.products[product] = quantity
        return True
    def remove_product(self, product: Product):
        if product in self.products:
            del self.products[product]

    def update_quantity(self, product, quantity):
        if product in self.products:
            self.products[product] = quantity

    def get_quantity(self, product):
        return self.products.get(product,0)
    
    def is_available(self, product):
        return self.get_quantity(product) == 0
    
from threading import Lock

class VendingMachine:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.inventory = Inventory()
            cls.idle_state = IdleState()

    @classmethod
    def get_instance(cls):
        return cls()

class VendingMachineState(ABC):
    def __init__(self, vending_machine: VendingMachine):
        self.vending_machine = vending_machine

    @abstractmethod
    def select_product(self, product):
        pass

    @abstractmethod
    def insert_coin(self, coin: Coin):
        pass

    @abstractmethod
    def insert_note(self, note: Note):
        pass

    @abstractmethod
    def dispense_product(self):
        pass

    @abstractmethod
    def return_change(self):
        pass

class IdleState(VendingMachine):
    def __init__(self, vending_machine: VendingMachine):
        self.vending_machine = vending_machine

    def select_product(self, product):
        pass
