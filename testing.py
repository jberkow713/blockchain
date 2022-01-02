from transaction import Transaction
from wallet import Wallet
if __name__ == '__main__':
    
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    TYPE = 'TRANSFER'
    # transaction information gets instantiated, 
    transaction = Transaction(sender, receiver, amount, TYPE)
    # wallet object is instantiated
    wallet = Wallet()
    # wallet object then takes the transaction dictionary, converts it using sha and pkcs1_v5
    signature = wallet.sign(transaction.toJson())
    # and then stores this signature in the transaction signature attribute
    if wallet.signaturevalid(transaction.toJson(), signature, wallet.publicKeyString())==True:
        print('valid')
        transaction.sign(signature)
    

