class bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited:",amount)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdrawn:",amount)
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("Balance:",self.balance)
class user(bank):
    pass

b=user(10000)
b.check_balance()
b.deposit(2000)
b.check_balance()
b.withdraw(12000)
b.check_balance()
b.deposit(20000)
b.check_balance()