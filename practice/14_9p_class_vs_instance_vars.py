# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################


# PRACTICE (Class and instance variables interacting):
'''
1. Create an Account class with the following:
    - Class Variables:
        - total_money: This should be initialized to 0 (e.g. set it equal to 0 at first) and will keep track of the total amount of money in all the accounts.
    - Instance Variables:
        - account_holder: The name of the account holder.
        - balance: The current balance in the account, initialized based on the input but defaults to 0 if not provided.
    - Methods:
        - A method named deposit_or_withdraw(amount) which adds the amount to the account's balance and updates the total_money class variable.
                To withdraw, just pass a negative amount
        - A method named display_balance() that prints the account holder's name and current balance.     
'''
class Account:
    total_money = 0

    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

        Account.total_money += balance # this is updating the class variable

    def deposit_or_withdraw(self, amount):
        self.balance += amount
        Account.total_money += amount # this is updating the class variable

    def display_balance(self):
        print(f"{self.account_holder}'s currenct balance: {self.balance}")
    

print(Account.total_money) # at first it is zero
account_1 = Account("Steffen", 100)
account_2 = Account("Sarah", 500)
# we want this to equal the total of all the money, so 600
print(Account.total_money)

account_1.deposit_or_withdraw(1345.32)
account_1.display_balance()
account_2.deposit_or_withdraw(-100)
account_2.display_balance()

print(Account.total_money) # still shows the updated current amount





'''

2. Every time money is added or deducted, the total_money class variable should be updated accordingly
    This means whenever a new object is created (so in the constructor) as well as when an Account object calls the deposit_or_withdraw method.

3. Create 2 instances of the Account class, and deposit and withdraw on each at least once, and display their balances.

4. Finally, display the total money in the bank using the total_money class variable.
'''


