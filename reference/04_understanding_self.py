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

# ==================
# UNDERSTANDING SELF
# ==================

'''
WHAT IS SELF??
--------------
The "self" parameter you see in every method in your class is a representation
of the object that is being created, or was already created. In the case of
this example, it represents the specific Dog object that you are working with

You can technically rename it to be any other name, but I highly recommend just
keeping it called self. Every method you write will, by default, recognize the 
first parameter as being a representation of the object itself, and convention
is to call that parameter "self", so I highly recommend to just call it "self".


IS SELF PASSED IN AS AN ARGUMENT?
---------------------------------
When you run code like this:

dog_object.doggy_description()

dog_object is automatically used as the first argument, even though you don't
type it in the parentheses.

It is functionally identical to calling the method this way:

Dog.doggy_description(dog_object)
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

# 1. HOW SELF IS PASSED AS AN ARGUMENT
# Call feed() using dog_1, just like you did in the last module.
# Notice how dog_1 becomes "self" when feed() is called.
# To make it clearer what is happening, you can also call methods like this:
#       Dog.feed(dog_object, "beef").
# The point is to see that self is just a representation of the object you are
# working with.

print(dog_1.feed("beef"))
print(Dog.feed(dog_1, "beef")) # this is exactly the same as the above line


'''
WHICH WAY SHOULD I CALL METHODS?
--------------------------------

Every time in this class, and 98% of the time in the real world, you should
just call functions the first way.

There are advantages to using the first way that will make sense as we learn
about other concepts like inheritance.

I'm only showing this other way so you can see that the object is in fact being
passed in as an argument, even though it doesn't look like it does with normal
functions.
'''