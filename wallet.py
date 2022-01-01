from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from Blockchainutils import BlockchainUtils

class Wallet():
    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        datahash = BlockchainUtils.hash(data)
        signatureobject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureobject.sign(datahash)
        return signature.hex()


