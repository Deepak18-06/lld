'''
The Chain of Responsibility pattern is a behavioral design pattern that allows you to pass 
requests along a chain of handlers. Each handler decides whether to process the request or 
pass it to the next handler in the chain. This pattern is useful when you have a series of 
handlers that can handle a request independently, and the client doesn't need to know which 
handler will process the request.

Handler is the base class for all handlers and defines the interface for handling requests. 
It also holds a reference to the next handler in the chain.
ConcreteHandlerA, ConcreteHandlerB, and ConcreteHandlerC are concrete handlers that implement 
the handling logic for specific types of requests. Each handler decides whether to handle the 
request or pass it to the next handler in the chain.

When you run this code, you'll see the output indicating which handler handles each request or 
if no handler is available for the request. This demonstrates how the Chain of Responsibility
pattern allows requests to be handled by different handlers in a chain.
'''

class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if self._successor:
            self._successor.handle_request(request)

class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == 'A':
            print("Handler A: Handling request")
        else:
            print("Handler A: Passing request to next handler")
            super().handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == 'B':
            print("Handler B: Handling request")
        else:
            print("Handler B: Passing request to next handler")
            super().handle_request(request)

class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request == 'C':
            print("Handler C: Handling request")
        else:
            print("Handler C: No handler available for this request")

if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB(handler_a)
    handler_c = ConcreteHandlerC(handler_b)

    # Make requests
    handler_c.handle_request('A')  # Handled by Handler A
    handler_c.handle_request('B')  # Handled by Handler B
    handler_c.handle_request('C')  # Handled by Handler C
    handler_c.handle_request('D')  # No handler available
