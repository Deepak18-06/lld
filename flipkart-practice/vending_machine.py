"""
multple products with diffrenet prices and quantities
should accept cash payments only
dispense selected product
tract available products

product 
- name 
- price
- quantity

VendingMachine
- id
- product list
- current_balance
- display(products)
- selectProduct()
- acceptPayment()
- dispense(product)

GET /vending-machine/products
response {
[{...product1}, {...product2}
]
}

POST /vending-machine/select-product
request {
product_id = 1
}
response {
price: 1.5
product_id:
}

POST /vending-machine/pay

request {
"amount" : 3
"payment_method": "Card"
}

{
"message": "Payment successful"
"change": "0.0"
}

POST dispense
"""


class Product:
    def __init__(self, name, quantity, price) -> None:
        self.name = name
        self.price = price


class Inventory:
    def __init__(self) -> None:
        self.products = {}

    def add_product(self,product):
        pass
    def remove_product(self, product):
        pass
    def update_quanitiy(self, product, quantity):
        pass
    def is_available(self, product):
        pass


class VendingMachineState(ABC):
    def __init__(self, machine):
        self.vending_machine = machine

    @abstractmethod
    def select_product(self, product):
        pass
    @abstractmethod
    def inserver_coin(self, coint):
        pass

    def insert_not(self):
        pass

    def dispense_product():
        pass

    def return_change(self):
        pass

class IdleState(VendingMachineState):

    def __init__(self, machine):
        super().__init__(machine)

    def select_product(self, product):
        #logic of selecting product
        pass

    def insert_coint(self, coin):
        print("please select a product first")

    def dispense_product():
        print("please select product and make payment")

    def return_change(self):
        print("no change to return")


class ReadyState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def select_product(self, product: Product):
        print("Product already selected. Please make payment.")

    def insert_coin(self, coin: Coin):
        self.vending_machine.add_coin(coin)
        print(f"Coin inserted: {coin.name}")
        self.check_payment_status()

    def insert_note(self, note: Note):
        self.vending_machine.add_note(note)
        print(f"Note inserted: {note.name}")
        self.check_payment_status()

    def dispense_product(self):
        print("Please make payment first.")

    def return_change(self):
        change = self.vending_machine.total_payment - self.vending_machine.selected_product.price
        if change > 0:
            print(f"Change returned: ${change:.2f}")
            self.vending_machine.reset_payment()
        else:
            print("No change to return.")
        self.vending_machine.set_state(self.vending_machine.idle_state)

    def check_payment_status(self):
        if self.vending_machine.total_payment >= self.vending_machine.selected_product.price:
            self.vending_machine.set_state(self.vending_machine.dispense_state)


from vending_machine_state import VendingMachineState
from product import Product
from coin import Coin
from note import Note

class ReturnChangeState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def select_product(self, product: Product):
        print("Please collect the change first.")

    def insert_coin(self, coin: Coin):
        print("Please collect the change first.")

    def insert_note(self, note: Note):
        print("Please collect the change first.")

    def dispense_product(self):
        print("Product already dispensed. Please collect the change.")

    def return_change(self):
        change = self.vending_machine.total_payment - self.vending_machine.selected_product.price
        if change > 0:
            print(f"Change returned: ${change:.2f}")
            self.vending_machine.reset_payment()
        else:
            print("No change to return.")
        self.vending_machine.reset_selected_product()
        self.vending_machine.set_state(self.vending_machine.idle_state)


from vending_machine_state import VendingMachineState
from product import Product
from coin import Coin
from note import Note

class DispenseState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def select_product(self, product: Product):
        print("Product already selected. Please collect the dispensed product.")

    def insert_coin(self, coin: Coin):
        print("Payment already made. Please collect the dispensed product.")

    def insert_note(self, note: Note):
        print("Payment already made. Please collect the dispensed product.")

    def dispense_product(self):
        self.vending_machine.set_state(self.vending_machine.ready_state)
        product = self.vending_machine.selected_product
        self.vending_machine.inventory.update_quantity(product, self.vending_machine.inventory.get_quantity(product) - 1)
        print(f"Product dispensed: {product.name}")
        self.vending_machine.set_state(self.vending_machine.return_change_state)

    def return_change(self):
        print("Please collect the dispensed product first.")



from threading import Lock
from inventory import Inventory
from idle_state import IdleState
from ready_state import ReadyState
from dispense_state import DispenseState
from return_change_state import ReturnChangeState
from vending_machine_state import VendingMachineState
from product import Product
from coin import Coin
from note import Note

class VendingMachine:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.inventory = Inventory()
                cls._instance.idle_state = IdleState(cls._instance)
                cls._instance.ready_state = ReadyState(cls._instance)
                cls._instance.dispense_state = DispenseState(cls._instance)
                cls._instance.return_change_state = ReturnChangeState(cls._instance)
                cls._instance.current_state = cls._instance.idle_state
                cls._instance.selected_product = None
                cls._instance.total_payment = 0.0
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def select_product(self, product: Product):
        self.current_state.select_product(product)

    def insert_coin(self, coin: Coin):
        self.current_state.insert_coin(coin)

    def insert_note(self, note: Note):
        self.current_state.insert_note(note)

    def dispense_product(self):
        self.current_state.dispense_product()

    def return_change(self):
        self.current_state.return_change()

    def set_state(self, state: VendingMachineState):
        self.current_state = state

    def add_coin(self, coin: Coin):
        self.total_payment += coin.value

    def add_note(self, note: Note):
        self.total_payment += note.value

    def reset_payment(self):
        self.total_payment = 0.0

    def reset_selected_product(self):
        self.selected_product = None



from vending_machine import VendingMachine
from product import Product
from coin import Coin
from note import Note

class VendingMachineDemo:
    @staticmethod
    def run():
        vending_machine = VendingMachine.get_instance()

        # Add products to the inventory
        coke = Product("Coke", 1.5)
        pepsi = Product("Pepsi", 1.5)
        water = Product("Water", 1.0)

        vending_machine.inventory.add_product(coke, 5)
        vending_machine.inventory.add_product(pepsi, 3)
        vending_machine.inventory.add_product(water, 2)

        # Select a product
        vending_machine.select_product(coke)

        # Insert coins
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)

        # Insert a note
        vending_machine.insert_note(Note.FIVE)

        # Dispense the product
        vending_machine.dispense_product()

        # Return change
        vending_machine.return_change()

        # Select another product
        vending_machine.select_product(pepsi)

        # Insert insufficient payment
        vending_machine.insert_coin(Coin.QUARTER)

        # Try to dispense the product
        vending_machine.dispense_product()

        # Insert more coins
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)

        # Dispense the product
        vending_machine.dispense_product()

        # Return change
        vending_machine.return_change()

if __name__ == "__main__":
    VendingMachineDemo.run()


