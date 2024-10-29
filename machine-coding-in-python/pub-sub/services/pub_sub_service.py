from models.topic import Topic
from models.message import Message
from models.publisher import Publisher
from models.subscriber import Subscriber


class PubSubService:
    def __init__(self, name):
        self.name = name
        self.topics = {}

    def get_topics(self):
        for id, topic in self.topics.items():
            print(f"ID: {id} => Topic: {topic.name}")

    def get_topic_subscribers(self, topid_id):
        print(f"topic: { self.topics[topid_id].name } has subscribers { len(self.topics[topid_id].subscribers)}", end='\n')
        return self.topics[topid_id].print_subscribers()

    def add_topic(self, topic):
        self.topics[topic.id] = topic
        print(f"Topic: {topic.name} created")
        return True

    def subscribe(self, topic_id, subscriber):
        topic = self.topics[topic_id]
        topic.subscribe(subscriber)
        print(f"Subscriber: {subscriber.name} added to Topic: {topic.name}")

    def unsubscribe(self, topic_id, subscriber_id):
        topic = self.topics[topic_id]
        topic.unsubscribe(subscriber_id)

        