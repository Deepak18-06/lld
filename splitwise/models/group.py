from models.user import User
from typing import List

class Group:
    def __init__(self, name: str, members: list[User], creater: User) -> None:
        self.name = name
        self.members: list[User]= members
        self.creater = creater
