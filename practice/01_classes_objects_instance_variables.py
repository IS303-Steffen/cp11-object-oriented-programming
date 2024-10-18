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

# =======================================
# CLASSES AND OBJECT-ORIENTED PROGRAMMING
# =======================================

'''
OVERVIEW
--------
Remember how you could store multiple variables in a list or a dictionary?

Object-oriented Programming (OOP) is sort of like a mega-extension of that.
The idea is that you create "objects" that can hold multiple variables AND
multiple functions. Also remember how with custom functions, you defined that
function first before calling it? In OOP, first you define the structure of
what an object should be and then afterwards you can make as many "instances"
of that object as you want.

Like always, most programming concepts are hard to understand in the abstract
without practicing, so let's just jump into making objects. In Python, OOP is
implemented by the "class" keyword.

STRUCTURE - DEFINING A CLASS
----------------------------
class ClassName:

    def __init__(self, instance_variable_parameter):
        self.instance_variable = instance_variable_parameter    

TIP - CLASS NAMING CONVENTIONS
------------------------------
You can name classes whatever you want, but convention is to use PascalCase
for naming classes, For example MyFirstClass instead of my_first_class.

snake_case is the convention for variables and function names.

That way it is easier to tell classes apart from everything else.
'''

# 1. MAKING A DOG CLASS - CONSTRUCTOR
# Make a class named "Dog" and the constructor, meaning the __init__ function.
# The constructor should allow for name, breed, and sex to be passed in as 
# parameters. Make the default value of sex be "F". Create instance variables
# in "self" for each of the parameters. Also create an instance variable
# called last_food_eaten and just give it the value of "unknown"




'''
HOW TO MAKE AN OBJECT
---------------------

To make an object, you need to call the constructor method (function). By 
default, if you type the name of the Class, followed by parentheses, it will
automatically call the constructor (which is the __init__ function). You ignore
the first parameter (self), and pass in any other arguments to fill the other
parameters. __init__ will then automatically return an object of the class
to where you called the constructor in your code. Your object will contain
all the instance variables

SYNTAX
------

new_object = ClassName(instance_variable_parameters)
'''

# 2 CREATING INSTANCES OF THE DOG CLASS (DOG OBJECTS)
# Now create 2 instances of the Dog class, store them into variables.
# You can try printing out the Dog instances, but it won't be very useful yet.


'''
ACCESSING VARIABLES INSIDE OBJECTS
----------------------------------
When you store an object in a variable, you get access to its instance
variables by typing . and then the name of the variable.

For example: dog_1.name

Use . to access anything stored inside of an object.
'''

# 3. ACCESSING INSTANCE VARIABLES INSIDE AN INSTANCE/OBJECT
# Now, print out the name variable inside each of the 2 dog objects you've
# made. Feel free to print out any other variables too.



'''
UPDATING INSTANCE VARIABLES
---------------------------
After you've made an object, you can update its instance variables at any
time like you would any other variable. You can even add new variables
to the object any time you want. Just update or insert new things with .
just like with any other variable in python

object.existing_variable = "updated value"

object.new_variable = "value for a new variable"

'''

# 4. UPDATING INSTANCE VARIABLES
# Update the name value of one of your dog objects to something different
# and print it out.







