# models.py

from datetime import datetime
from typing import List

class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name


class Account:
    def __init__(self, account_no: int, user: User, balance: float = 0.0):
        self.account_no = account_no
        self.user = user
        self.balance = balance
        self.transactions: List[Transaction] = []


class Transaction:
    def __init__(self, transaction_type: str, amount: float, timestamp: datetime):
        self.transaction_type = transaction_type  # e.g., 'deposit', 'withdrawal'
        self.amount = amount
        self.timestamp = timestamp

# repositories.py
from typing import Dict, Optional

class AccountRepository:
    def __init__(self):
        self.accounts: Dict[int, Account] = {}  # Using account_no as key
    
    def create_account(self, account_no: int, user: User, initial_balance: float = 0.0) -> Account:
        account = Account(account_no, user, initial_balance)
        self.accounts[account_no] = account
        return account

    def find_account_by_no(self, account_no: int) -> Optional[Account]:
        return self.accounts.get(account_no)
    
    def update_balance(self, account_no: int, new_balance: float) -> None:
        account = self.find_account_by_no(account_no)
        if account:
            account.balance = new_balance

# strategies.py
from datetime import datetime

class TransactionStrategy:
    def execute(self, account: Account, amount: float) -> None:
        raise NotImplementedError

class DepositStrategy(TransactionStrategy):
    def execute(self, account: Account, amount: float) -> None:
        account.balance += amount
        transaction = Transaction("deposit", amount, datetime.now())
        account.transactions.append(transaction)

class WithdrawalStrategy(TransactionStrategy):
    def execute(self, account: Account, amount: float) -> None:
        if account.balance >= amount:
            account.balance -= amount
            transaction = Transaction("withdrawal", amount, datetime.now())
            account.transactions.append(transaction)
        else:
            raise ValueError("Insufficient funds for withdrawal")


# services

class AccountService:
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo
        self.deposit_strategy = DepositStrategy()
        self.withdrawal_strategy = WithdrawalStrategy()

    def deposit(self, account_no: int, amount: float) -> str:
        account = self.account_repo.find_account_by_no(account_no)
        if account:
            self.deposit_strategy.execute(account, amount)
            self.account_repo.update_balance(account_no, account.balance)
            return f"Deposited {amount} successfully. New balance: {account.balance}"
        return "Account not found"

    def withdraw(self, account_no: int, amount: float) -> str:
        account = self.account_repo.find_account_by_no(account_no)
        if account:
            try:
                self.withdrawal_strategy.execute(account, amount)
                self.account_repo.update_balance(account_no, account.balance)
                return f"Withdrew {amount} successfully. New balance: {account.balance}"
            except ValueError as e:
                return str(e)
        return "Account not found"

    def get_balance(self, account_no: int) -> str:
        account = self.account_repo.find_account_by_no(account_no)
        if account:
            return f"Account balance: {account.balance}"
        return "Account not found"

# main

def main():
    # Initialize repository and services
    account_repo = AccountRepository()
    account_service = AccountService(account_repo)
    
    # Create user and account
    user = User(user_id=1, name="John Doe")
    account = account_repo.create_account(account_no=123456, user=user, initial_balance=1000.0)
    
    # Test operations
    print(account_service.get_balance(account.account_no))
    print(account_service.deposit(account.account_no, 500))
    print(account_service.withdraw(account.account_no, 200))
    print(account_service.get_balance(account.account_no))
    
    # Attempt an overdraw
    print(account_service.withdraw(account.account_no, 2000))

if __name__ == "__main__":
    main()
