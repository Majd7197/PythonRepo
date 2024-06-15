class BankAccount:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.balance = 0
    def make_deposit(self,amount):
        self.balance += amount
        return self
    def account_info(self):
        print(f"Account balance is {self.balance}")
        return self
        
        
majd = BankAccount("Majd", "abusadamajd@gmail.com")
majd.make_deposit(2000)
print(majd.balance)
print(majd.name)
majd.account_info().make_deposit(300).account_info()
