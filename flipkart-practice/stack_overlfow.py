"""
user can post a question, 
user can answer a question
user can comment on question and answer
user can vote a question and answer
user can tag a question
user can serch of question based on keyword, tags
user 
"""

class User:
    def __init__(self) -> None:
        self.name
        self.email
        self.questions
        self.answers
        self.comments
        self.votes

        def ask_qeustion(self, question):
            self.questions.append(question)
        def answer_questoin():
            pass

class Vote:
    def __init__(self) -> None:
        self.value = 0

    def upvote(self):
        self.value += 1

    def downvote(self):
        self.value -= 1

class Question:
    def __init__(self) -> None:
        self.id 
        self.title 
        self.description 
        self.answers
        self.comments
        self.votes

class Anwser:
    def __init__(self) -> None:
        self.id
        self.title
        self.description
        self.question
        self.votes = []
        self.comments = []

class Comment:
    def __init__(self) -> None:
        self.id
        self.description
        self.votes = []




