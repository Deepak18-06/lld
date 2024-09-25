'''
The Strategy Pattern is a behavioral design pattern that allows you to define a family of algorithms, 
encapsulate each one, and make them interchangeable. It lets the algorithm vary independently from the 
clients that use it


PaymentStrategy is the strategy interface that declares a method for paying.
CreditCardPayment, PayPalPayment, and GooglePayPayment are concrete strategy classes implementing 
specific payment methods.
ShoppingCart is the context class that takes a payment strategy and uses it to pay during checkout.
'''


# Define the strategy interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# Define concrete strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal")

class GooglePayPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Google Pay")

# Context class
class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)

# Usage
if __name__ == "__main__":
    # Creating context with different payment strategies
    cart1 = ShoppingCart(CreditCardPayment())
    cart2 = ShoppingCart(PayPalPayment())
    cart3 = ShoppingCart(GooglePayPayment())

    # Checkout with different amounts
    cart1.checkout(100)
    cart2.checkout(200)
    cart3.checkout(300)
