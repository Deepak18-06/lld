from users.user import User

class UserService:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def signup(self, name, profession):
        user = User(name, profession)
        self.users[name] = user
        return user

    def login(self, name):
        self.current_user = self.users[name]

    def logout(self):
        self.current_user = None

    def get_current_user(self):
        return self.current_user
