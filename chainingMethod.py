class User:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def make_withdrawal(self,amount):
        self.balance -= amount
        return self
    def make_deposit(self,amount):
        self.balance += amount
        return self
    def display_user_balance(self):
        print("User:",self.name, ",Balance: $"+ str(self.balance))
    def transfer_money(self,other_user,amount):
        self.balance -= amount
        other_user.balance += amount
        
Majd = User("Majd Abu Sada", 0)  
George = User("George",9000)  
Khader = User("Khader Khair", 8000)

Majd.make_deposit(10000).make_deposit(10000).make_deposit(10000).make_withdrawal(5000).display_user_balance()

George.make_deposit(15000).make_deposit(8000).make_withdrawal(2000).make_withdrawal(5000).display_user_balance()

Khader.make_deposit(6000).make_withdrawal(1500).make_withdrawal(3000).make_withdrawal(4500).display_user_balance()

Majd.transfer_money(Khader,3000)
Majd.display_user_balance()
Khader.display_user_balance()
