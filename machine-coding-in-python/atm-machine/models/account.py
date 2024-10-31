class Account:
    def __init__(self, account_no, user, balance, branch, card):
        self.account_no = account_no
        self.user = user
        self.balance = balance
        self.branch = branch
        self.card = card

    def deposit(self, amount: int):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return False