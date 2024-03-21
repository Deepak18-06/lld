class Question:
    def __init__(self, text, topics, asked_by):
        self.text = text
        self.topic = set(topics)
        self.asked_by = asked_by
        self.answers = []
        self.accepted_answer = None