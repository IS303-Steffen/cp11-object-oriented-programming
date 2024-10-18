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

# =======
# METHODS
# =======

'''
OVERVIEW
--------

Objects don't just store instance & class variables, they also store entire
functions. When a function is part of an object (e.g. defined in a Class) then
it is called a "Method". So all methods are functions, but not all functions 
are methods.

Anytime you make a method, the first parameter needs to be "self". "self" is a
representation of the object that is calling the method. That means self lets
you get access to all of the instance variables (and methods) attached to it
inside of the method. This is very powerful.

You've actually already made a method, __init__ also called the constructor or
the initializer. It is a special method that makes/initializes the object.
Every class you make in IS 303 will use the constructor. You can also add other
methods that do whatever you want with any of the instance/class variables
(or other parameters if you like).

You access methods inside objects the same way you access variables: with 
a period/dot .
'''

class Dog: # name of the class
    species = "Canis lupus familiaris"

    def __init__(self, name, breed, sex = "F"): # the constructor
        self.name = name # putting parameter into an instance variable
        self.breed = breed # putting parameter into an instance variable
        self.sex = sex # putting parameter into an instance variable
        self.last_food_eaten = "unknown" # instance variable, no parameter

    def doggy_description(self): # method is just a function inside a class
        if self.sex == 'M':
            message = (f"{self.name} is a {self.breed} and he is a good boy! "
                       f"The last food he ate was {self.last_food_eaten}.")
        else:
            message = (f"{self.name} is a {self.breed} and she is a good girl! "
                       f"The last food he ate was {self.last_food_eaten}.")

        return message
    
    def feed(self, food):
        self.last_food_eaten = food
        return f"{self.name} is eating {self.last_food_eaten}!"

dog_1 = Dog("Buddy", "Golden Retriever", "M") # creating a Dog object
dog_2 = Dog("Princess", "German Shepherd", "F") # creating another Dog object

# 1. CREATING A CUSTOM METHOD
# Alter the code above.
# In the Dog class, create a method called doggy_description. If the dog is 
# male, it should return "<dog name> is a <breed> and he is a good boy! The
# last food he ate was <last food eaten>". If the dog is female, return
# "<dog name> is a <breed> and she is a good girl! The last food she ate was
# <last food eaten>" call the doggy_description for both dog objects and print
# the result

print(dog_1.doggy_description())
print(dog_2.doggy_description())

# 2. CREATE A CUSTOM METHOD WITH EXTRA PARAMETER
# Create another method called "feed". Like all (default) methods, you need
# to put "self" as the first parameter. But include another parameter called
# "food". Use the self and food parameters to update the dog object's
# last_food_eaten instance variable to be equal to the food parameter.
# Additionally, return the message: "<dog name> is eating <food>!"
# call the method for each of the 2 dog objects.
# then call doggy_description for one of the dogs. Did the doggy_description
# change?

print(dog_1.feed("beef"))
print(dog_2.feed("chocolate (probably shouldn't eat that)"))

print(dog_1.doggy_description())