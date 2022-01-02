from transaction import Transaction
from transactionpool import TransactionPool
from wallet import Wallet
from block import Block
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
    
    block = wallet.create_block(pool.transactions, 'lasthash', 1)
    validsignature = wallet.signaturevalid(block.payload(), block.signature, wallet.publicKeyString())

    print(validsignature)
    # pprint.pprint(block.toJson())

    # this is testing if the thing is valid for the trade purposes, it will not affect what is stored in the transactionpool
    # validsign = wallet.signaturevalid(transaction.payload(), transaction.signature, wallet.publicKeyString())
    # print(validsign)
    # validsign2 = wallet.signaturevalid(transaction.payload(), transaction.signature, fake_wallet.publicKeyString())
    # print(validsign2)
        
    # print(pool.transactions)
    
    


    

