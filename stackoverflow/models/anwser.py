class Answer:
    def __init__(self, title, description, question, user_id) -> None:
        self.title = title
        self.description = description
        self.question = question
        self.user_id = user_id

    def set_description(self, description):
        self.description = description