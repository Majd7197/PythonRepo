class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance:$"+str(self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
        return self

Majd_acc = BankAccount(0.01, 500)  
George_acc = BankAccount(0.05)  
Majd_acc.deposit(500).deposit(300).deposit(440).withdraw(555).yield_interest().display_account_info()
George_acc.deposit(6000).deposit(440).withdraw(4000).withdraw(100).withdraw(550).withdraw(2000).yield_interest().display_account_info()

