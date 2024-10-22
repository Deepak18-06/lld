class Question:
    def __init__(self, title, description, tags=[]) -> None:
        self.title = title
        self.description = description
        self.tags = tags
        self.answers = []

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        if tag not in self.tags:
            raise Exception("Question not tagged with this tag")
        self.tag.remove(tag)

    def remove_answer(self, answer):
        if answer not in self.answers:
            raise Exception("Tag does not exists")
        self.answers.remove(answer)

    def add_answer(self, answer):
        if answer in self.answers:
            raise Exception("Answer already exists")
        self.answers.append(answer)
