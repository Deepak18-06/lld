from models.task import Task

class TaskRepo:
    def __init__(self) -> None:
        self.tasks = {}

    def create_task(self, task: Task):
        if self.tasks.get(task.id):
            raise Exception("task with given id already exists")
        self.tasks[task.id] = task
        return task
    
    def get_task(self, task_id):
        if not self.tasks.get(task_id):
            raise Exception("Task with given id does not exists")
        return self.tasks[task_id]