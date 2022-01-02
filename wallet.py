from Crypto import PublicKey
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import uuid
from Blockchainutils import BlockchainUtils
from transaction import Transaction

class Wallet():
    def __init__(self):
        # creates private RSA key 
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        datahash = BlockchainUtils.hash(data)
        signatureobject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureobject.sign(datahash)
        # the signature object interacts with the long hash key to create a new hex object
        return signature.hex()
    
    @staticmethod
    def signaturevalid(data,signature, publicKeyString):
        # back to bytes
        signature = bytes.fromhex(signature)
        # sha256object
        datahash = BlockchainUtils.hash(data)
        # the public key part of the keypair
        publicKey = RSA.importKey(publicKeyString)
        # some kind of signature object using the public key
        signatureSchemeObject = PKCS1_v1_5.new(publicKey)
        # use the public key object along with the hashed data and hex signature to verify if they match each other
        signatureValid = signatureSchemeObject.verify(datahash, signature)
        return signatureValid

    def publicKeyString(self):
        # pull out the public key from the key pair to insert into the above function
        publicKeyString = self.keyPair.publickey().exportKey('PEM').decode('utf-8')
        return publicKeyString
    def create_transaction(self, receiver, amount, type):
        # return an instance of newly created transaction, with whoever sent the transaction as the 'owner'
        transaction = Transaction(self.publicKeyString(), receiver, amount, type)
        signature = self.sign(transaction.toJson())
        # transaction takes the hex signature and adds it to its instance dictionary
        transaction.sign(signature)
        return transaction



# this is how it works
# t = 'hello i am a pizza what are you???'
# t1 = t.encode('utf-8')
# t2 = SHA256.new(t1)
# t3 = PKCS1_v1_5.new(RSA.generate(2048))
# print(t3.sign(t2).hex())