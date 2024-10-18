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

# ========================
# HOW CLASS VARIABLES WORK
# ========================

'''
OVERVIEW
--------------
When you have an object, like dog_1, when you add a dot . and a variable name,
it will first check if that variable name exists as an instance variable. If it 
doesn't, it will then check if that variable name exists as a class variable. 
'''

class Dog:
    species = "Canis lupus familiaris" # this is a class variable

    def __init__(self, name, breed, sex = "F"):
        # all the below are instance variables
        self.name = name 
        self.breed = breed 
        self.sex = sex 
        self.last_food_eaten = "unknown" 

# 1. ACCESSING CLASS VARIABLES DIRECTLY
# You can access class variables as soon as a class is defined. You don't need
# to make an instance first. Print out the species class variable:


# Creating 2 dog objects.
dog_1 = Dog("Buddy", "Golden Retriever", "M")
dog_2 = Dog("Princess", "German Shepherd", "F")

# 2. ACCESSING CLASS VARIABLES THROUGH AN OBJECT
# when you create an instance of a dog, you can access the class variable,
# even though it isn't an instance variable:
# try printing out dog_1.species


# 3. "CHANGING" A CLASS VARIABLE THROUGH AN OBJECT
# Change dog_1.species to a new value. Then print out dog_1.species
# and Dog.species. What do you notice? Print out dog_2.species.


# 4. DIRECTLY CHANGING A CLASS VARIABLE
# Change Dog.species to a new value. Then print out dog_1.species and 
# dog_2.species. Try to think why you see the results you do.



'''
SUMMARY: WHAT IS GOING ON
-------------------------
1. You can create new instance variables whenever. Be careful. An instance
   variable can have the same name as a class variable. Avoid doing that.

2. When you access an object, like dog_1.species, FIRST it looks to see if
   there is an instance variable with that name. If so it stops there. If it
   doesn't find anything, THEN it checks if there is a class variable with that
   name and grabs it if so.

'''