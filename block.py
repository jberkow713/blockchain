
import time
import json
import copy

class Block():

    def __init__(self, transactions, lastHash, forger, blockCount):
        self.transactions = transactions
        self.lastHash = lastHash 
        self.forger = forger
        self.blockCount = blockCount
        self.timestamp = time.time()
        self.signature = ''

    @staticmethod
    def genesis():
        genesisBlock = Block([], 'genesisHash', 'genesis', 0)
        genesisBlock.timestamp = 0
        return genesisBlock    

    def toJson(self):
        d = {}
        d['lastHash']=self.lastHash
        d['forger']=self.forger
        d['blockCount']=self.blockCount
        d['timestamp']=self.timestamp
        d['signature']=self.signature
        jsontransactions = []
        for transaction in self.transactions:
            jsontransactions.append(transaction.toJson())
        d['transactions']=jsontransactions
        return d

    def payload(self):
        jsonrep = copy.deepcopy(self.toJson())
        jsonrep['signature']= ''
        return jsonrep

    def sign(self, signature):
        self.signature = signature              
