class Subscriber:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def update(self, message):
        print(f"Subscriber: {self.name} got message: {message.get_content()}")
    