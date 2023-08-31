class Account:
    sum_to_deposit = 0
    sum_to_withdraw = 0

    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = int(account_number)
        self.account_balance = float(account_balance)
        self.account_holder = str(account_holder)
        print("Welcome to your bank account.")

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


my_account = Account(12, 342425.24, "Ibra")
my_account.withdraw(25432)
my_account.deposit(245654)
my_account.check_balance()


