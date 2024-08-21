class Answer:
    def __init__(self, text, answered_by):
        self.text = text
        self.answered_by = answered_by
        self.upvotes = set()