class UserRepository:
    users = []

    @classmethod
    def add_user(cls, user):
        cls.users.append(user)

    @classmethod
    def get_user_by_id(cls, user_id):
        for user in cls.users:
            if user.user_id == user_id:
                return user
        return None
