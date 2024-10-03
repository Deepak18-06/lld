from models import User, Question, Answer, Comment, Vote
from repositories import UserRepository, QuestionRepository, AnswerRepository, CommentRepository

user_repo = UserRepository()
question_repo = QuestionRepository()
answer_repo = AnswerRepository()
comment_repo = CommentRepository()

# Controller for managing users
class UserController:
    def create_user(self, username):
        user = User(username)
        user_repo.add_user(user)
        return user

# Controller for questions
class QuestionController:
    def ask_question(self, title, body, tags, username):
        user = user_repo.find_user_by_username(username)
        if not user:
            return None, "User not found"
        question = Question(title, body, tags, user)
        question_repo.add_question(question)
        return question

    def get_all_questions(self):
        return question_repo.get_all_questions()

# Controller for answers
class AnswerController:
    def answer_question(self, question_id, body, username):
        user = user_repo.find_user_by_username(username)
        if not user:
            return None, "User not found"
        question = question_repo.find_question_by_id(question_id)
        if not question:
            return None, "Question not found"
        answer = Answer(body, user, question)
        answer_repo.add_answer(answer)
        question.answers.append(answer)
        return answer

# Controller for voting
class VoteController:
    def vote_question(self, question_id, username, vote_type):
        user = user_repo.find_user_by_username(username)
        if not user:
            return None, "User not found"
        question = question_repo.find_question_by_id(question_id)
        if not question:
            return None, "Question not found"
        if vote_type == 'upvote':
            question.votes += 1
            user.reputation += 10
        elif vote_type == 'downvote':
            question.votes -= 1
            user.reputation -= 2
        return question

    def vote_answer(self, answer_id, username, vote_type):
        user = user_repo.find_user_by_username(username)
        if not user:
            return None, "User not found"
        answer = answer_repo.find_answer_by_id(answer_id)
        if not answer:
            return None, "Answer not found"
        if vote_type == 'upvote':
            answer.votes += 1
            user.reputation += 10
        elif vote_type == 'downvote':
            answer.votes -= 1
            user.reputation -= 2
        return answer

# Controller for comments
class CommentController:
    def add_comment_to_question(self, question_id, body, username):
        user = user_repo.find_user_by_username(username)
        if not user:
            return None, "User not found"
        question = question_repo.find_question_by_id(question_id)
        if not question:
            return None, "Question not found"
        comment = Comment(body, user, question)
        comment_repo.add_comment(comment)
        return comment

    def add_comment_to_answer(self, answer_id, body, username):
        user = user_repo.find_user_by_username(username)
        if not user:
            return None, "User not found"
        answer = answer_repo.find_answer_by_id(answer_id)
        if not answer:
            return None, "Answer not found"
        comment = Comment(body, user, answer)
        comment_repo.add_comment(comment)
        return comment
