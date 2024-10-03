from controllers import UserController, QuestionController, AnswerController, VoteController, CommentController

user_controller = UserController()
question_controller = QuestionController()
answer_controller = AnswerController()
vote_controller = VoteController()
comment_controller = CommentController()

def run_app():
    # Create some users
    user1 = user_controller.create_user("Alice")
    user2 = user_controller.create_user("Bob")

    # Alice asks a question
    question = question_controller.ask_question("What is Python?", "Can someone explain Python?", ["Python", "Programming"], "Alice")

    # Bob answers the question
    answer = answer_controller.answer_question(question.question_id, "Python is a programming language.", "Bob")

    # Alice upvotes Bob's answer
    vote_controller.vote_answer(answer.answer_id, "Alice", "upvote")

    # Print the current state
    print(f"Question: {question.title} by {question.user.username}")
    print(f"Answer: {answer.body} by {answer.user.username}, Votes: {answer.votes}")

if __name__ == "__main__":
    run_app()
