from repository.UserRepository import UserRepository

class UserService:
    @classmethod
    def add_user(cls, user):
        UserRepository.add_user(user)
