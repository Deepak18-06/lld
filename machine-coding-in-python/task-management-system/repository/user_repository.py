from models.user import User

class UserRepo:
    def __init__(self) -> None:
        self.users = {}

    def register_user(self, user: User) -> User:
        if self.users.get(user.email):
            raise Exception("User already exists with given email")
        user.id = user.email
        self.users[user.id] = user
        return user
    
    def get_user(self, user_id: str) -> User:
        if not self.users.get(user_id):
            raise Exception("User with given id does not exists")
        return self.users[user_id]