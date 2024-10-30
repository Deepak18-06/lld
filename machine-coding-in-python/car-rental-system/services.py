# services.py

from repositories import UserRepository
from models import User

class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo
    
    def register_user(self, name, email):
        if self.user_repo.get_user_by_email(email):
            raise Exception("User with this email already exists.")
        user = User(len(self.user_repo.users) + 1, name, email)
        self.user_repo.add_user(user)
        return user
    
    def get_user(self, email):
        user = self.user_repo.get_user_by_email(email)
        if not user:
            raise Exception("User not found.")
        return user
