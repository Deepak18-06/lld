'''
- Air Traffic Control -> send message to other planes that other planes are there
The Mediator Pattern is a behavioral design pattern that promotes loose coupling by encapsulating
the way objects interact with each other. Instead of objects directly communicating with each other,
they communicate through a mediator object. This centralizes communication and reduces dependencies 
between objects.


Mediator class manages communication between colleagues. It contains a list of colleagues and a method 
to send messages to other colleagues.
Colleague class represents individual colleagues. Each colleague has a name and a reference to the mediator. 
It also has methods to send and receive messages.
When a colleague sends a message, it goes through the mediator, which forwards it to all other colleagues 
except the sender.
'''

class Mediator:
    def __init__(self, colleagues):
        self.colleagues = colleagues

    def send_message(self, sender, message):
        for colleague in self.colleagues:
            if colleague != sender:
                colleague.receive_message(message)

class Colleague:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send_message(self, message):
        print(f"{self.name} sends message: {message}")
        self.mediator.send_message(self, message)

    def receive_message(self, message):
        print(f"{self.name} receives message: {message}")


if __name__ == "__main__":
    # Create mediator
    mediator = Mediator([])

    # Create colleagues
    colleague1 = Colleague("Colleague 1", mediator)
    colleague2 = Colleague("Colleague 2", mediator)
    colleague3 = Colleague("Colleague 3", mediator)

    # Add colleagues to mediator
    mediator.colleagues.extend([colleague1, colleague2, colleague3])

    # Sending message from colleague 1
    colleague1.send_message("Hello, everyone!")
