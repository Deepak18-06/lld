class Publisher:
    def __init__(self, id, name, topic):
        self.id = id
        self.name = name
        self.topic = topic
        print(f"Publisher: {self.name} created with Topic: {self.topic.name}")

    def publish(self, message):
        self.topic.publish(message)


