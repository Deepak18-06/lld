from models.user import User
from models.task import Task
from repository.task_repository import TaskRepo
from repository.user_repository import UserRepo


class TaskService:
    def __init__(self, user_repo: UserRepo, task_repo: TaskRepo):
        self.user_repo = user_repo
        self.task_repo = task_repo

    def create_task(self, title, description):
        pass

    def update_task(self, task):
        pass
