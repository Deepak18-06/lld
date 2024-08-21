class User:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
        self.subscribed_topics = set()
        self.asked_questions = []
        self.answered_questions = []