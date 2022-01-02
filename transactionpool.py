class TransactionPool:

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def transactionExists(self, transaction):
        for TRANSACTION in self.transactions:
            if TRANSACTION.equals(transaction)==True:
                return True
        return False     
            
               