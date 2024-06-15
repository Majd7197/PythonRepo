class BankAccount:
    def __init__(self,int_rate,balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self
    def display_info(self):
        print(self.balance)
class RetirementAccount(BankAccount):
    def __init__(self,int_rate, is_roth,balance=0):
        super().__init__(int_rate,balance)
        self.is_roth = is_roth
    def depositt(self,amount):
        super().deposit(amount)
        return self
    def display_info(self):
        return super().display_info()
first_account = RetirementAccount(0.05,True)
first_account.deposit(100).display_info()