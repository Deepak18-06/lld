import uuid
from datetime import datetime

class User:
    def __init__(self, username):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.reputation = 0

class Question:
    def __init__(self, title, body, tags, user):
        self.question_id = str(uuid.uuid4())
        self.title = title
        self.body = body
        self.tags = tags
        self.user = user
        self.answers = []
        self.votes = 0
        self.creation_date = datetime.now()

class Answer:
    def __init__(self, body, user, question):
        self.answer_id = str(uuid.uuid4())
        self.body = body
        self.user = user
        self.votes = 0
        self.question = question
        self.creation_date = datetime.now()

class Comment:
    def __init__(self, body, user, target):
        self.comment_id = str(uuid.uuid4())
        self.body = body
        self.user = user
        self.target = target  # Can be a Question or Answer
        self.creation_date = datetime.now()

class Vote:
    def __init__(self, user, target, vote_type):
        self.vote_id = str(uuid.uuid4())
        self.user = user
        self.target = target  # Can be a Question or Answer
        self.vote_type = vote_type  # 'upvote' or 'downvote'
