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
    forger = Wallet()

    Exchange_transaction = Exchange.create_transaction(Alice.publicKeyString(), 10, 'Exchange')
    pool.add_transaction(Exchange_transaction)
    covered_transactions = blockchain.getCoveredTransactionSet(pool.transactions)

    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    BlockCount = blockchain.blocks[-1].blockCount+1
    BlockOne = forger.create_block(covered_transactions, lastHash, BlockCount)
    blockchain.add_block(BlockOne)
    pool.remove_from_pool(covered_transactions)

    transaction = Alice.create_transaction(Bob.publicKeyString(), 5, 'transfer')
    pool.add_transaction(transaction)
    covered_transactions = blockchain.getCoveredTransactionSet(pool.transactions)
    
    
    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    BlockCount = blockchain.blocks[-1].blockCount+1
    BlockTwo = forger.create_block(covered_transactions, lastHash, BlockCount)
    blockchain.add_block(BlockTwo)
    

    pprint.pprint(blockchain.to_json())
      
    
    

    
    
    


    

