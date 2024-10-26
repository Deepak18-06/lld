# task management
"""
Users create tasks add details 
Users assign task to other users
Task are of different type i.e bug
"""

class User:
    def __init__(self, name, email, password, role) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.created_boards = []
        self.assigned_boards = []
        self.assigned_task = []


class Task:
    def __init__(self, id, title, description, created_by, asssigned_to, board) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.created_by = created_by
        self.assigned_to = asssigned_to
        self.board = board

    

class Board:
    def __init__(self, id, title, description, created_by):
        self.id = id
        self.name = title
        self.description = description
        self.created_by = created_by
        self.tickets = []
        self.assigned_to = created_by

    def assign(self, user):
        self.unassigned()
        self.assigned_to = user

    def unassigned(self):
        user = self.assigned_to
        user.boardsremove(self)
        self.assigned_to = None

    def add_tickets(self, ticket):
        if ticket in self.tickets:
            return "Ticket already in board"
        self.add_tickets.append(ticket)

    def remove_ticket(self, ticket):
        if not ticket in self.tickets:    
            return "Ticket not in board"
        self.tickets.remove(ticket)


class Jira:
    def __init__(self, boards):
        self.boards = {}

    def add_board(self, board):
        self.boards[board.id] = board
    
    def get_board(self, board_id):
        board = self.boards.get(board_id)
    
    def update_board(self, board):
        existing_board = self.boards.get(board.id)
        if existing_board:
            existing_board.id = board.id
            existing_board.title = board.title
            existing_board.description = board.description
            existing_board.tickets = board.tickets

    def delete_board(self, board):
        self.boards.remove(board)

    def create_ticket(self, board_id, ticket):
        board = self.board.get(board_id)
        ticket = Task()
        board.tickets.append(ticket)

    def update_ticket():
        pass

    def get_ticket(self):
        pass

    def delete_ticket(self):
        pass
    



        