class User():
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self,balance):
        self.account_balance += balance

khader = User("Khader","kdoor@hotmail.com")
print(khader.account_balance)
khader.make_deposit(400)
print(khader.account_balance)
print(khader.name)