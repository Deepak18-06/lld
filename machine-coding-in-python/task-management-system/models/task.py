class Task:
    next_id = 1
    def __init__(self, title, description, due_date, priority, status) -> None:
        self.id = Task.next_id
        Task.next_id += 1
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.create_by = None
        self.assigned_to = None
        self.assigned_by = None
        self.history = []
    
    def edit_title(self, title):
        self.title = title

    def edit_description(self, descrition):
        self.description = descrition

    def edit_due_date(self, date):
        self.due_date = date

    def set_priority(self, priority):
        self.priority = priority

    def set_status(self, status):
        self.status = status

    def assigned(self, user1, user2):
        self.assigned_by = user1
        self.assigned_to = user2

