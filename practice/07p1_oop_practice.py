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
