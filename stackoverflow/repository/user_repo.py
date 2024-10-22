from models.user import User

class UserRepo:
    def __init__(self) -> None:
        self.users = {}

    def register_user(self, name, email):
        if self.users.get(email):
            raise Exception("user already exist with same email")
        self.users[email] = User(name, email)
        return self.users[email]
    
    def get_user(self, email):
        if not self.users.get(email):
            raise Exception("user with give email does not exist")
        return self.users.get(email)