class Topic:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.subscribers = {}

    def subscribe(self, subscriber):
        self.subscribers[subscriber.id] = subscriber
        return True

    def unsubscribe(self, subscriber_id):
        del self.subscribers[subscriber_id]
        return False
    
    def print_subscribers(self):
        for key, val in self.subscribers.items():
            print(f"id: {key} | Name: {val.name}")

    def publish(self, message):
        for key, subscriber in self.subscribers.items():
            subscriber.update(message)