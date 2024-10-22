class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.tasks = []

    def add_task(self, task):
        self.tasks = task

    def assigne_task(self, task, user):
        user.add_task(task)
    