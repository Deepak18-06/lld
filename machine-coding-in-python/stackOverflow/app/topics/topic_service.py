from topics.topic import Topic

class TopicService:
    def __init__(self):
        self.topics_map = {}

    def subscribe(self, current_user, *topics):
        for topic in topics:
            topic_obj = self.topics_map.get(topic, Topic(topic))
            current_user.subscribed_topics.add(topic_obj)
            self.topics_map[topic] = topic_obj

    def unsubscribe(self, current_user, topic):
        current_user.subscribed_topics.remove(topic)
        # Remove the topic from topics_map if no user is subscribed to it