from Blockchainutils import BlockchainUtils
from transaction import Transaction
from transactionpool import TransactionPool
from wallet import Wallet
from block import Block
from blockchain import Blockchain
from accountmodel import accountmodel
import pprint

if __name__ == '__main__':
    
    blockchain = Blockchain()
    pool = TransactionPool()

    Alice = Wallet()
    Bob = Wallet()
    Exchange = Wallet()

    Exchange_transaction = Exchange.create_transaction(Alice.publicKeyString(), 10, 'Exchange')
    transaction = Alice.create_transaction(Bob.publicKeyString(), 5, 'transfer')

    pool.add_transaction(Exchange_transaction)
    pool.add_transaction(transaction)
    # pool.show_transactions()

    covered_transactions = blockchain.getCoveredTransactionSet(pool.transactions)
    print(covered_transactions)
      
    
    

    
    
    


    

