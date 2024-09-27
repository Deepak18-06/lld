from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


# define the subject interface
class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


#implement concrete subjec
class Product(Subject):
    def __init__(self, name):
        self.name = name
        self.is_in_stock = False
        self._observers = []

    # Subscribe a user (observer) to notifications
    def subscribe(self, observer: Observer):
        self._observers.append(observer)
        print(f"{observer.name} has subscribed for {self.name} notifications.")

    # Unsubscribe a user (observer)
    def unsubscribe(self, observer: Observer):
        self._observers.remove(observer)
        print(f"{observer.name} has unsubscribed from {self.name} notifications.")

    # Notify all observers about product availability
    def notify_observers(self):
        for observer in self._observers:
            observer.update(f"{self.name} is now back in stock!")

    # Change the stock status and notify users
    def set_in_stock(self, in_stock):
        self.is_in_stock = in_stock
        if in_stock:
            print(f"{self.name} is now in stock.")
            self.notify_observers()
        else:
            print(f"{self.name} is out of stock.")


#implement concrete observer
class User(Observer):
    def __init__(self, name):
        self.name = name

    # Method that is called when the product is back in stock
    def update(self, message):
        print(f"Notification for {self.name}: {message}")


#usage
# Create a product that users can subscribe to
product = Product("Smartphone")

# Create users who want to be notified
user1 = User("Alice")
user2 = User("Bob")
user3 = User("Charlie")

# Users subscribe to the product's notifications
product.subscribe(user1)
product.subscribe(user2)

# Product becomes available
product.set_in_stock(True)

# Charlie subscribes after the product is in stock
product.subscribe(user3)

# Unsubscribe Alice
product.unsubscribe(user1)

# Product goes out of stock again
product.set_in_stock(False)

# Product is back in stock, notifying remaining observers (Bob and Charlie)
product.set_in_stock(True)


