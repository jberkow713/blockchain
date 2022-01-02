from Crypto import PublicKey
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import uuid

from Blockchainutils import BlockchainUtils

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
        signature = bytes.fromhex(signature)
        datahash = BlockchainUtils.hash(data)
        publicKey = RSA.importKey(publicKeyString)
        signatureSchemeObject = PKCS1_v1_5.new(publicKey)
        signatureValid = signatureSchemeObject.verify(datahash, signature)
        return signatureValid

    def publicKeyString(self):
        publicKeyString = self.keyPair.publickey().exportKey('PEM').decode('utf-8')
        return publicKeyString

# this is how it works

# t = 'hello i am a pizza what are you???'
# t1 = t.encode('utf-8')
# t2 = SHA256.new(t1)
# t3 = PKCS1_v1_5.new(RSA.generate(2048))
# print(t3.sign(t2).hex())