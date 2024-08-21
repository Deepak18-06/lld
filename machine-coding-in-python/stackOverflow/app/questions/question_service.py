from questions.question import Question
from questions.answer import Answer

class QuestionService:
    def __init__(self, user_service):
        self.user_service = user_service

    def ask_question(self, question_text, topics):
        current_user = self.user_service.get_current_user()
        question = Question(question_text, topics, current_user)
        current_user.asked_questions.append(question)
        # Add code to update topics_map and Topic objects
        return question

    def answer_question(self, question, answer_text):
        current_user = self.user_service.get_current_user()
        if question.topic.issubset(current_user.subscribed_topics):
            answer = Answer(answer_text, current_user)
            question.answers.append(answer)
            current_user.answered_questions.append(question)
        else:
            print(f"{current_user.name} cannot answer {question.text} as they are not subscribed to the required topics.")

    def accept_answer(self, question, answer):
        current_user = self.user_service.get_current_user()
        if question in current_user.asked_questions:
            question.accepted_answer = answer
        else:
            print(f"{current_user.name} cannot accept an answer for {question.text} as they did not ask the question.")

    def upvote_answer(self, answer):
        current_user = self.user_service.get_current_user()
        if answer.question.topic.issubset(current_user.subscribed_topics):
            answer.upvotes.add(current_user)
        else:
            print(f"{current_user.name} cannot upvote answers for {answer.question.text} as they are not subscribed to the required topics.")