'''
Let's consider a real-world example of an online news portal with subscribers. When a news article is published on the portal, 
it needs to notify all its subscribers about the new article. This scenario fits well with the Observer Pattern.

Here's how the Observer Pattern can be applied to this example:

Subject (News Portal):

The news portal acts as the subject.
It maintains a list of subscribers (observers).
It provides methods to subscribe and unsubscribe from notifications.
When a new article is published, it notifies all subscribers.
Observer (Subscriber):

Subscribers register with the news portal to receive notifications.
They provide a method to receive and handle notifications (e.g., displaying the new article).

'''

# Subject (News Portal)
class NewsPortal:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, article):
        for subscriber in self._subscribers:
            subscriber.update(article)

# Observer (Subscriber)
class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, article):
        print(f"{self.name} received notification: New article - {article}")

# Usage
if __name__ == "__main__":
    # Create news portal
    news_portal = NewsPortal()

    # Create subscribers
    subscriber1 = Subscriber("John")
    subscriber2 = Subscriber("Alice")

    # Subscribe subscribers to the news portal
    news_portal.subscribe(subscriber1)
    news_portal.subscribe(subscriber2)

    # Publish a new article
    news_portal.notify_subscribers("10 Tips for a Healthy Lifestyle")
