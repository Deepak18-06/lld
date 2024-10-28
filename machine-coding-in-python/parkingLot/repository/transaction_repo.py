class TransactionRepo:
    def __init__(self) -> None:
        self.transactions = {}

    def add_trasaction(self, transaction):
        self.transactions[transaction.id] = transaction

    def get_trasaction(self, id):
        return self.transactions.get(id)