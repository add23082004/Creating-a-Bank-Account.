import random


class Account:
    next_account_number = random.randint(1, 1000)
    sum_to_deposit = 0
    sum_to_withdraw = 0
    account_number = 0

    @classmethod
    def generate_account_number(cls):
        account_number = str(cls.next_account_number)
        cls.next_account_number += random.randint(1, 10)
        return account_number

    def __init__(self, account_balance, account_holder):
        self.account_number = Account.generate_account_number()
        self.account_balance = float(account_balance)
        self.account_holder = str(account_holder)

    def deposit(self, sum_to_deposit):
        self.sum_to_deposit = sum_to_deposit
        self.account_balance += self.sum_to_deposit
        print(self.sum_to_deposit, '$ has been added to your bank account.\nNew balance:', self.account_balance, '$.')

    def withdraw(self, sum_to_withdraw):
        self.sum_to_withdraw = sum_to_withdraw
        if self.account_balance > self.sum_to_withdraw:
            self.account_balance -= self.sum_to_withdraw
            print('You have just retrieved', self.sum_to_withdraw, '$ from your bank account.\nNew balance:',
                  self.account_balance, '$.')

        elif self.account_balance == self.sum_to_withdraw:
            self.account_balance -= self.sum_to_withdraw
            print("You don't have anything left in your bank account.\nYou're broke !!!")

        else:
            print("You've just retrieved... HAHAHA.\nYou're broke remember go to work!!!!!")

    def check_balance(self):
        if self.account_balance > 0:
            print('Your current account balance is:', self.account_balance, '$.')

        else:
            print("You don't have anything left in your bank account.\nYou're broke !!!")


my_account1 = Account(342425.24, "Ibra")

print(my_account1.account_number)





