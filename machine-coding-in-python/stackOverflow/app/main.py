from users.user_service import UserService
from questions.question_service import QuestionService
from topics.topic_service import TopicService
from services.feed_service import FeedService

# Create instances of the services
user_service = UserService()
question_service = QuestionService(user_service)
topic_service = TopicService()
feed_service = FeedService(user_service, topic_service)

# Demo
user_service.signup('Sachin', 'Developer')
user_service.login('Sachin')
topic_service.subscribe(user_service.get_current_user(), 'java', 'hadoop', 'jdk')
q1 = question_service.ask_question("What are new open source jdks?", ['java', 'jdk'])
q2 = question_service.ask_question("Does Hadoop work on JDK 11?", ['hadoop', 'jdk'])
feed_service.show_feed()
feed_service.show_feed(filter_topics=['java'])
feed_service.show_feed(filter_topics=['jdk'])
feed_service.show_feed(answered=True)
user_service.logout()

user_service.signup('Kalyan', 'Developer')
user_service.login('Kalyan')
topic_service.subscribe(user_service.get_current_user(), 'apache', 'hadoop')
feed_service.show_feed()
q3 = question_service.ask_question("Does Apache Spark support streaming of data from hdfs?", ['apache', 'hadoop'])
question_service.answer_question(q2, "Yeah Hadoop 3 and above supports it.")
feed_service.show_feed()
user_service.logout()

user_service.signup('Lokesh', 'Developer')
user_service.login('Lokesh')
topic_service.subscribe(user_service.get_current_user(), 'apache', 'hadoop', 'java')
feed_service.show_feed()
feed_service.show_profile('Kalyan')
question_service.answer_question(q2, "Yeah, Hadoop 3 and above supports it.") # Should not be able to answer
if q2.answers:
    question_service.upvote_answer(q2.answers[0])
else:
    print("No answers available for upvoting.")
# question_service.upvote_answer(q2.answers[0])
user_service.logout()

user_service.login('Sachin')
feed_service.show_feed()
feed_service.show_profile('Kalyan')
feed_service.show_profile('Sachin')
# question_service.accept_answer(q2, q2.answers[0])
if q2.answers:
    question_service.accept_answer(q2, q2.answers[0])
else:
    print("No answers available to accept.")
feed_service.show_profile('Kalyan')
feed_service.show_feed(answered=True)
user_service.logout()