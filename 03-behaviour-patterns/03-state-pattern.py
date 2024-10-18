'''
The State Pattern is a behavioral design pattern that allows an object to alter its behavior 
when its internal state changes. This pattern is particularly useful when an object's behavior 
depends on its state and when an object needs to change its behavior dynamically at runtime


State is the interface that defines the behavior associated with a particular state.
Context is the class whose behavior changes based on its internal state.
ConcreteStateA and ConcreteStateB are concrete state classes implementing specific
behaviors associated with different states.
When you run this code, it will output "Handling request in State A" indicating that 
the request is being handled according to the current state. To switch to a different 
state, you would uncomment the appropriate lines in the handle method of each concrete 
state class and call context.set_state() accordingly.
'''

class State:
    def handle(self):
        pass

class Context:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()

class ConcreteStateA(State):
    def handle(self):
        print("Handling request in State A")
        # Change state if necessary
        # context.set_state(ConcreteStateB())

class ConcreteStateB(State):
    def handle(self):
        print("Handling request in State B")
        # Change state if necessary
        # context.set_state(ConcreteStateA())

# Usage
if __name__ == "__main__":
    context = Context()

    # Set initial state
    context.set_state(ConcreteStateA())

    # Request handling
    context.request()
