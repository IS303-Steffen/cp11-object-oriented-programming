import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# =================
# MORE OOP PRACTICE
# =================


# 1. PRACTICE: CLASS AND INSTANCE VARIABLES INTERACTING
# Create an Account class with the following:
# - Class Variables:
#     - total_money: This should be initialized to 0 (e.g. set it equal to 0
#       at first) and will keep track of the total amount of money in all the
#       accounts.
# - Instance Variables:
#     - account_holder: The name of the account holder, a parameter.
#     - balance: The current balance in the account, initialized based on the
#                parameter but defaults to 0 if not provided.
# - Methods:
#     - deposit_or_withdraw:
#           includes an `amount` parameter which you will add to the account's
#           balance instance variable. The method should also update the
#           total_money class variable. To withdraw, just pass a negative
#           amount
#     - display_balance:
#           that prints the account holder's name and current balance.
#
# Every time money is added or deducted, the total_money class variable should
# be updated accordingly. This means whenever a new object is created
# (so in the constructor) as well as when an Account object calls the
# deposit_or_withdraw method.
#
# Create 2 instances of the Account class, and deposit and withdraw on each at
# least once, and display their balances. Between each transaction, display the
# total money in the bank using the total_money class variable


class Account: # name of the class is Account
    total_money = 0 # this is a class variable

    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder # these are the instance variables
        self.balance = balance

        Account.total_money = Account.total_money + balance # this updates the class variable

    def deposit_or_withdraw(self, amount):
        self.balance = self.balance + amount

        Account.total_money = Account.total_money + amount

    def display_balance(self):
        print(f"Account holder: {self.account_holder} has a current balance of: {self.balance}")



print(Account.total_money)
acc1 = Account("Jacob", 5000)
print(Account.total_money)
acc1.deposit_or_withdraw(30)
print(Account.total_money)
acc1.deposit_or_withdraw(-30)
print(Account.total_money)


acc2 = Account("Jane", 10000)
acc2.deposit_or_withdraw(60)
print(Account.total_money)
acc2.deposit_or_withdraw(-70)
print(Account.total_money)

acc1.display_balance()
acc2.display_balance()
