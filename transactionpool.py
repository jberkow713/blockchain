from transaction import Transaction

class TransactionPool:

    def __init__(self):
        self.transactions = []
   

    def transactionExists(self, transaction):
        for TRANSACTION in self.transactions:
            if TRANSACTION.equals(transaction)==True:
                return True
        return False

    def add_transaction(self, transaction):
        if self.transactionExists(transaction)==False:
            self.transactions.append(transaction)
    
    def remove_from_pool(self, transactions):
        new_transactions = []
        for transaction in transactions:
            if self.transactionExists(transaction)==False:
                new_transactions.append(transaction)
        self.transactions=new_transactions        

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction.toJson())              
               