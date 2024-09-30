from models.user import User
class Ticket:
    def __init__(self, id, assigned_to: User):
        self.id = id
        self.assigned_to = assigned_to