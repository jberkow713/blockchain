import uuid
import time
import copy


class Transaction():

    def __init__(self, senderPublicKey, receiverPublicKey, amount, type_):
        self.senderPublicKey=senderPublicKey
        self.receiverPublicKey=receiverPublicKey
        self.amount = amount
        self.type = type_ 
        # generates random hex value for self.id, globally unique
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        return self.__dict__ 

    def sign(self, signature):
        self.signature=signature
    
    def payload(self):
        jsonRepr = copy.deepcopy(self.toJson())
        jsonRepr['signature']=''
        return jsonRepr

    def equals(self, transaction):
        if self.id == transaction.id:
            return True
        else:
            return False    



