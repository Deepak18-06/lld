# Pub-Sub System

## Requirements
- It should allow user to publish messages on a specific topic
- A topic could be subscribe to one to more subcribers
- It should publish message from a topic to subsriber
- It should support multiple publisher and subscribers
- Message should be delivered to all subsribers in real time


## Classes
- Topic
    1. id(pk)
    2. name

- Publishers
    1. id(pk)
    2. name
    3. config
    4. topic_id(fk)

- Subcribers
    1. id(pk)
    2. name
    3. config
    4. topic_id(fk)

- Message
    1. id(fk)
    2. content
    3. topic_id(fk)


Relationships
- a topic have many publishers and a publisher belongs to a topic
- a topic has many subscribers and a subscriber belongs to a topic
- a topic has many messages and a message belongs to a topic