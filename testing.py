from Blockchainutils import BlockchainUtils
from transaction import Transaction
from transactionpool import TransactionPool
from wallet import Wallet
from block import Block
from blockchain import Blockchain
import pprint

if __name__ == '__main__':
    
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    TYPE = 'TRANSFER'
    # transaction information gets instantiated, 
    pool = TransactionPool()
    wallet =  Wallet()
    fake_wallet = Wallet()
    
    transaction = wallet.create_transaction(receiver, amount, TYPE)

    if pool.transactionExists(transaction)==False:
        pool.add_transaction(transaction)
    
    blockchain = Blockchain()
    # in creating a new block, we take the hash from the previous block and hash it
    # creates simple loop to test functionality using last blocks count and hash as verification
    for _ in range(3):

        lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
        blockCount = blockchain.blocks[-1].blockCount+1

        block = wallet.create_block(pool.transactions, lastHash, blockCount)
        
        blockchain.VERIFY(block)
        
        
      
    
    pprint.pprint(blockchain.to_json())
    # pprint.pprint(block.toJson())

    
    
    


    

