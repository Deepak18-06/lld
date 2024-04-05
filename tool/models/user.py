from enum import Enum

class Role(Enum):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'
    EXECUTIVE = 'EXECUTIVE'
    SALES_HEAD = 'SALES_HEAD'

class User:
    def __init__(self, name: str, phone: int, role: Role):
        self.name = name
        self.phone = phone
        self.role = role

