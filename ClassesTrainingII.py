class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.accounts = {}
    def add_account(self,account_name, balance, int_rate):
        self.accounts[account_name] = BankAccount(balance , int_rate)
    def make_deposit(self,amount,account_name):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else: 
            print("account does not exist")
        return self
    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self
    def display_account_info(self,account_name):
        print(f"Account: {account_name}")
        self.accounts[account_name].account_info()
        return self
    
        
class BankAccount:
    def __init__(self,balance = 0,int_rate=0.01):
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if self.balance-amount < 0:
            print("no funds to deposit")
        else:
            self.balance -= amount
        return self
    def account_info(self):
        print(f"Your account balance is {self.balance}")
        return self
    
Majd = User("Majd", "Abusadamajd@gmail.com")
Majd.add_account("saving", 0, 0.05)
Majd.make_deposit(1000,"saving")
Majd.display_account_info("saving")
Majd.add_account("current",1000,0.1)
Majd.make_deposit(1,"current")
Majd.display_account_info("current")

