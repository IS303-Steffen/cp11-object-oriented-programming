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

# 1. PRACTICE: USING OBJECTS INSIDE DICTIONARIES
# You are given the following Person class and 3 Person objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person_1 = Person("Alice", 30)
person_2 = Person("Bob", 25)
person_3 = Person("Charlie", 35)

# 1.1: STORE OBJECTS IN A DICTIONARY
# Create a dictionary to store the person objects.
# Use the person's name as the key, and the entire object as the value



# 1.2: ACCESSING OBJECTS, RUNNING MEETHODS
# Using the dictionary, individually access each of the objects and
# run their print_info method


# 1.3: ACCESSING OBJECTS IN A LOOP
# Loop through the dictionary of people and run the print_info method on each.

