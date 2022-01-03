class accountmodel():

    def __init__(self):
        self.accounts = []
        self.balances = {}

    def add_account(self,publicKeyString):
        if not publicKeyString in self.accounts:
            self.accounts.append(publicKeyString)
            self.balances[publicKeyString]=0
    def get_balance(self, publicKeyString):
        if publicKeyString not in self.accounts:
            self.add_account(publicKeyString)
        return self.balances[publicKeyString]
    def update_balance(self, publicKeyString, amount):
        if publicKeyString not in self.accounts:
            self.add_account(publicKeyString)
        
        self.balances[publicKeyString]+=amount

