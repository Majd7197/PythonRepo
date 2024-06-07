class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount()	
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    def display_user_balance(self):
        print("User:",self.name, ",Balance: $"+ str(self.account.balance))
    def transfer_money(self,other_user,amount):
        self.balance -= amount
        other_user.balance += amount
    def example_method(self):
        pass;
        
        
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
    
# Create an instance of User
Majd = User("Majd Abusada", "majd@gmail.com")
Majd.make_deposit(100)
Majd.account.display_account_info()