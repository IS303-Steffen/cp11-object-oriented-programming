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

# ===============
# CLASS VARIABLES
# ===============

'''
OVERVIEW
--------
When you make an instance variable, it can have a unique value for every
instance that you make. You can also make class variables. These are
variables with a single value that applies to all instances. You
create them below the class name, NOT in the constructor. 

We won't use them much in this class, but you absolutely should know what they
are.
'''

class Dog: # name of the class
    species = "Canis lupus familiaris"

    def __init__(self, name, breed, sex = "F"): # the constructor
        self.name = name # putting parameter into an instance variable
        self.breed = breed # putting parameter into an instance variable
        self.sex = sex # putting parameter into an instance variable
        self.last_food_eaten = "unknown" # instance variable, no parameter

dog_1 = Dog("Buddy", "Golden Retriever", "M") # creating a Dog object
dog_2 = Dog("Princess", "German Shepherd", "F") # creating another Dog object

# 1. DOG CLASS VARIABLES
# Alter the code above to create a class variable called "species" with the
# value of "Canis lupus familiaris". Then try printing it out for the two Dog
# instances you already made. You can also print it out by just specifying the
# Dog class, like Dog.species

print(dog_1.species)
print(dog_2.species)
print(Dog.species)

