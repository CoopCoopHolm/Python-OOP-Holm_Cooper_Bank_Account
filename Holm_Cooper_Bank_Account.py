class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.balance = balance
        self.int_rate = int_rate

    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def yield_interest(self):
        return self
    def display_BankAccount_balance(self):
        print (f"Balance: $ {self.balance}")
        return self
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self

coopcoopholm = BankAccount(0.3)
joedoe = BankAccount(0.1)

coopcoopholm.make_deposit(321654987).make_deposit(987654321).make_deposit(456789123).make_withdrawal(123456789).display_BankAccount_balance()

joedoe.make_deposit(13579).make_deposit(97531).make_withdrawal(123).make_withdrawal(321).make_withdrawal(987).make_withdrawal(789).display_BankAccount_balance()