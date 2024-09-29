from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List

# Product-related classes
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.products: Dict[str, List[Product]] = {}

    def add_product(self, product: Product, quantity: int):
        if product.name not in self.products:
            self.products[product.name] = []
        self.products[product.name].extend([product] * quantity)

    def remove_product(self, product_name: str) -> Product:
        if product_name in self.products and self.products[product_name]:
            return self.products[product_name].pop()
        raise ValueError(f"Product {product_name} is out of stock")

    def get_available_products(self) -> Dict[str, int]:
        return {name: len(products) for name, products in self.products.items()}

# Payment-related classes
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CashPayment(PaymentMethod):
    def process_payment(self, amount: float) -> bool:
        # Simulate cash payment processing
        print(f"Processing cash payment of ${amount:.2f}")
        return True

class CardPayment(PaymentMethod):
    def process_payment(self, amount: float) -> bool:
        # Simulate card payment processing
        print(f"Processing card payment of ${amount:.2f}")
        return True

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def make_payment(self, amount: float) -> bool:
        return self.payment_method.process_payment(amount)

# State-related classes
class State(ABC):
    @abstractmethod
    def insert_money(self, machine: 'VendingMachine', amount: float) -> None:
        pass

    @abstractmethod
    def select_product(self, machine: 'VendingMachine', product_name: str) -> None:
        pass

    @abstractmethod
    def dispense_product(self, machine: 'VendingMachine') -> None:
        pass

class IdleState(State):
    def insert_money(self, machine: 'VendingMachine', amount: float) -> None:
        machine.add_payment(amount)
        machine.set_state(machine.has_money_state)

    def select_product(self, machine: 'VendingMachine', product_name: str) -> None:
        print("Please insert money first")

    def dispense_product(self, machine: 'VendingMachine') -> None:
        print("Please insert money and select a product first")

class HasMoneyState(State):
    def insert_money(self, machine: 'VendingMachine', amount: float) -> None:
        machine.add_payment(amount)

    def select_product(self, machine: 'VendingMachine', product_name: str) -> None:
        if machine.select_product(product_name):
            machine.set_state(machine.dispense_state)
        else:
            print(f"Unable to select {product_name}")

    def dispense_product(self, machine: 'VendingMachine') -> None:
        print("Please select a product first")

class DispenseState(State):
    def insert_money(self, machine: 'VendingMachine', amount: float) -> None:
        print("Product dispensing in progress, please wait")

    def select_product(self, machine: 'VendingMachine', product_name: str) -> None:
        print("Product dispensing in progress, please wait")

    def dispense_product(self, machine: 'VendingMachine') -> None:
        machine.dispense_product()
        if machine.payment_amount > 0:
            machine.set_state(machine.has_money_state)
        else:
            machine.set_state(machine.idle_state)

# Main VendingMachine class
class VendingMachine:
    def __init__(self, inventory: Inventory, payment_processor: PaymentProcessor):
        self.inventory = inventory
        self.payment_processor = payment_processor
        self.payment_amount = 0
        self.selected_product = None

        # Initialize states
        self.idle_state = IdleState()
        self.has_money_state = HasMoneyState()
        self.dispense_state = DispenseState()
        self.state = self.idle_state

    def set_state(self, state: State) -> None:
        self.state = state

    def insert_money(self, amount: float) -> None:
        self.state.insert_money(self, amount)

    def select_product(self, product_name: str) -> bool:
        available_products = self.inventory.get_available_products()
        if product_name in available_products and available_products[product_name] > 0:
            product = self.inventory.products[product_name][0]
            if self.payment_amount >= product.price:
                self.selected_product = product_name
                return True
        return False

    def dispense_product(self) -> None:
        if self.selected_product:
            product = self.inventory.remove_product(self.selected_product)
            print(f"Dispensing {product.name}")
            self.payment_amount -= product.price
            self.selected_product = None
            if self.payment_amount > 0:
                print(f"Returning change: ${self.payment_amount:.2f}")
                self.payment_amount = 0

    def add_payment(self, amount: float) -> None:
        if self.payment_processor.make_payment(amount):
            self.payment_amount += amount
            print(f"Current balance: ${self.payment_amount:.2f}")

    def display_products(self) -> None:
        print("Available products:")
        for name, quantity in self.inventory.get_available_products().items():
            product = self.inventory.products[name][0]
            print(f"{name}: ${product.price:.2f} ({quantity} available)")

# Factory for creating VendingMachine instances
class VendingMachineFactory:
    @staticmethod
    def create_vending_machine(payment_method: PaymentMethod) -> VendingMachine:
        inventory = Inventory()
        inventory.add_product(Product("Cola", 1.50), 5)
        inventory.add_product(Product("Chips", 1.00), 5)
        inventory.add_product(Product("Candy", 0.75), 5)

        payment_processor = PaymentProcessor(payment_method)
        return VendingMachine(inventory, payment_processor)

# Usage example
if __name__ == "__main__":
    cash_machine = VendingMachineFactory.create_vending_machine(CashPayment())
    cash_machine.display_products()
    cash_machine.insert_money(2.00)
    cash_machine.select_product("Cola")
    cash_machine.state.dispense_product(cash_machine)

    print("\nTesting with card payment:")
    card_machine = VendingMachineFactory.create_vending_machine(CardPayment())
    card_machine.display_products()
    card_machine.insert_money(5.00)
    card_machine.select_product("Chips")
    card_machine.state.dispense_product(card_machine)
    card_machine.select_product("Candy")
    card_machine.state.dispense_product(card_machine)