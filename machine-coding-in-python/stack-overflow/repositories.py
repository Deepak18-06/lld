class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def find_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

class QuestionRepository:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_all_questions(self):
        return self.questions

    def find_question_by_id(self, question_id):
        for question in self.questions:
            if question.question_id == question_id:
                return question
        return None

class AnswerRepository:
    def __init__(self):
        self.answers = []

    def add_answer(self, answer):
        self.answers.append(answer)

    def get_all_answers(self, question):
        return [answer for answer in self.answers if answer.question == question]

    def find_answer_by_id(self, answer_id):
        for answer in self.answers:
            if answer.answer_id == answer_id:
                return answer
        return None  # Return None if the answer is not found


class CommentRepository:
    def __init__(self):
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments_for_target(self, target):
        return [comment for comment in self.comments if comment.target == target]
