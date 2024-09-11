from exceptions import InsufficientFundsException

class Account:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw amount must be a positive number")
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            raise InsufficientFundsException
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

