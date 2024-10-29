from services.pub_sub_service import PubSubService
from models.message import Message
from models.publisher import Publisher
from models.subscriber import Subscriber
from models.topic import Topic

redis = PubSubService("redis")

# Defining Topics
movies_release = Topic(1,"Movie released")
news = Topic(2,"News")

redis.add_topic(movies_release)
redis.add_topic(news)

# Defining Publishers
pub1 = Publisher(1,"pub1", movies_release)
pub2 = Publisher(2,"pub2", news)

# Defining Subscribers
sub1 = Subscriber(1, "sub1")
sub2 = Subscriber(2, "sub2")

redis.subscribe(news.id, sub1)
redis.subscribe(movies_release.id, sub2)
redis.get_topics()
redis.get_topic_subscribers(news.id)


message = Message(1,"Hi")
pub2.publish(message)

