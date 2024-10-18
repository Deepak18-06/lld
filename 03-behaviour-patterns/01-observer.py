'''
The Observer Pattern is a behavioral design pattern that defines a one-to-many dependency between 
objects so that when one object changes state, all its dependents are notified and updated automatically.

'''


# Subject class
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

# Observer interface
class Observer:
    def update(self, subject):
        pass

# Concrete Observer classes
class ConcreteObserverA(Observer):
    def update(self, subject):
        print("ConcreteObserverA received update from Subject")

class ConcreteObserverB(Observer):
    def update(self, subject):
        print("ConcreteObserverB received update from Subject")

# Usage
if __name__ == "__main__":
    subject = Subject()

    # Attach observers
    observer1 = ConcreteObserverA()
    observer2 = ConcreteObserverB()

    subject.attach(observer1)
    subject.attach(observer2)

    # Notify observers
    subject.notify()
