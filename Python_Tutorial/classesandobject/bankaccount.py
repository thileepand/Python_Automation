class BankAccount():
    def __init__(self):
        self.balance = 1500

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


minimum_balance= 1000

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        print ("Withdrawn amount ",amount)
        if self.balance - amount < self.minimum_balance:
            print("Sorry minimum balance should be maintained ", minimum_balance)
        else:
            BankAccount.withdraw(self, amount)
            print("Amount successfully withdrawn")
    def show_balance(self):
        print ("current balance ",self.balance)

min_x = MinimumBalanceAccount(minimum_balance)
min_x.withdraw(1000)
min_x.show_balance()
print ("__"*20)

min_y = MinimumBalanceAccount(minimum_balance)
min_y.withdraw(100)
min_y.deposit(2000)
min_y.show_balance()