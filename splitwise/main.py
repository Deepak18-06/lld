from models.group import Group
from models.user import User

user = User("deepak", "deepak@gmail.com")

group = Group(name="hey", members=[user], creater="user")
print(group.members.__class__)

def add(a: int, b: int) -> int:
    return a + b

result = add(3, 4)
print(result)

result = add("3", "4")
print(result)

