from Blockchainutils import BlockchainUtils
from block import Block
from accountmodel import accountmodel
from transaction import Transaction

class Blockchain():

    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = accountmodel()

    def add_block(self, block):
        self.executeTransactions(block.transactions)
        self.blocks.append(block)

    def to_json(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data['Blocks']=jsonBlocks
        return data

    def blockCountValid(self, block):
        # make the number equal to correct number in list, blocks go in in order, so the last value
        # should equal length of the list -1, which is equivalent to last block value

        if self.blocks[-1].blockCount == block.blockCount -1:
            return True            
        else:
            return False

    def lastHashValid(self, block):
        latestHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        if latestHash == block.lastHash:
            return True
        else:
            return False
    
    def VERIFY(self, block):
        # takes in block , 
        if self.blockCountValid(block)==False:
            print('block count not valid')
            return
        if self.lastHashValid(block)==False:
            print('hash not valid')
            return
        if self.blockCountValid(block)==True and self.lastHashValid(block) == True:
            self.add_block(block)
            return
    
    def transactionCovered(self, transaction):
        
        if transaction.type_ == 'Exchange':
            return True
        
        senderbalance = self.accountModel.get_balance(transaction.senderPublicKey)
        if senderbalance >=transaction.amount:
            return True
        else:
            return False
    
    def getCoveredTransactionSet(self, transactions):
        covered_transactions = []
        for transaction in transactions:
            if self.transactionCovered(transaction) == True:
                covered_transactions.append(transaction)
            else:
                print('transaction is not covered by sender')
                print(transaction.type_)
        return covered_transactions  

    def executeTransaction(self, transaction):
        sender = transaction.senderPublicKey
        receiver = transaction.receiverPublicKey
        amount = transaction.amount
        self.accountModel.update_balance(sender,-amount)
        self.accountModel.update_balance(receiver, amount)

    def executeTransactions(self, transactions):
        for transaction in transactions:
            self.executeTransaction(transaction)                  
    

