'''
Single responsibility
Open close
Liskov substitution
Interface segregation
Dependency Inversion
'''

from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name: str, quantity: int, price: float):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.prices[i] * self.quantities[i]
        return total
        
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass
class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass



class SMSAuth(Authorizer):
    verified = False

    def verify(self, code):
        print(f"verifying sms code: {code}")
        self.verified = True
    
    def is_authorized(self) -> bool:
        return self.verified

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception(f"sms authentication on verified")
        print("Processing debit payment mode")
        print(f"Verifying security code: {self.security_code}")
        order.status = 'paid'

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        
    def pay(self, order):
        print("Processing credit payment mode")
        print(f"Verifying security code: {self.security_code}")
        order.status = 'paid'

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email = email
        
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Sms authentication not done")
        print("Processing paypal payment mode")
        print(f"Verifying email: {self.email}")
        order.status = 'paid'

    
        
order = Order()
order.add_item("keyboar", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = SMSAuth()
processor = DebitPaymentProcessor('w3432', authorizer)
authorizer.verify(34532)
processor.pay(order)