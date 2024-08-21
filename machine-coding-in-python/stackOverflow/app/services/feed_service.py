class FeedService:
    def __init__(self, user_service, topic_service):
        self.user_service = user_service
        self.topic_service = topic_service

    def show_feed(self, filter_topics=None, answered=None):
        current_user = self.user_service.get_current_user()
        questions = []
        for topic in current_user.subscribed_topics:
            questions.extend(topic.questions)
        if filter_topics:
            questions = [q for q in questions if q.topic.intersection(filter_topics)]
        if answered is not None:
            questions = [q for q in questions if (q.accepted_answer is not None) == answered]
        # Sort and display the questions and answers

    def show_profile(self, name):
        user = self.user_service.users[name]
        # Display user profile information, asked questions, and answered questions