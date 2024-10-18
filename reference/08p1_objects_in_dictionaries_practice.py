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

person_dictionary = {person_1.name : person_1, person_2.name : person_2, person_3.name : person_3}

# 1.2: ACCESSING OBJECTS, RUNNING MEETHODS
# Using the dictionary, individually access each of the objects and
# run their print_info method

person_dictionary["Alice"].print_info()
person_dictionary["Bob"].print_info()
person_dictionary["Charlie"].print_info()

# 1.3: ACCESSING OBJECTS IN A LOOP
# Loop through the dictionary of people and run the print_info method on each.

for person_name in person_dictionary:
    person_dictionary[person_name].print_info()