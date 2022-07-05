class Account:
    def __init__(self, name, passwords):
        self.balance = 0
        self.name = name
        self.passwords = passwords

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount > 0:
            self.balance -= amount

    def transfer(self, acc_number, amount, password):
        self.withdraw(amount)
        acc_number.deposit(amount)
