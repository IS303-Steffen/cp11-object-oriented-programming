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


'''
Object-oriented programming is implemented in python by using the "class" keyword

The structure is:

class ClassName:
    any_class_variables = "value of class variable"

    def __init__(self, instance_variable_parameter):
        self.instance_variable = instance_variable_parameter

    def any_other_method_you_want(self):
        any code you want

####
You create an object of your class by doing

new_object = ClassName(instance_variable_parameters)
'''

# Follow-along Practice
'''
Together, let's make our first class.

Class name: Dog

Class variable: species
    - make it have the value of "Canis lupus familiaris"

Constructor:
    this is a special method. Method is a function that is part of a class
    The constructor MUST be called __init__. it should also have "self" as the first
    parameter

    Instance Variables: all of the variables that you want to be unique to each object
    name
    breed
    sex

        make it so you pass in parameters for all of the instance variables. Make it so the 
        default value for sex is "F"
            
Other Methods

    Make a method called doggy_description. Its only parameter should be self

    If they are male, return "{dog name} is a {breed} and he is a good boy!"

    if they are female, return "{dog name} is a {breed} and she is a good girl!"
'''

# Start the class here
class Dog:
    # Add any class variables
    species = "Canis lupus familiaris"

    # Add Constructor. must be called __init__
    def __init__(self, name, breed, sex = "F"):
        # Instance variables. Must use self.Name to be instance variables
        self.name = name
        self.breed = breed
        self.sex = sex
    
    # Method. Same thing as a function, but in a class.
    # Note passing "self" in gives us access to all the instance variables.
    def doggy_description(self):
        if self.sex == 'M':
            message = self.name + " is a " + self.breed + " and he is a good boy!"
        else:
            message = self.name + " is a " + self.breed + " and she is a good girl!"

        return message


# Get access to class variable by typing ClassName.class_variable
# Print out the species class variable
    
print(Dog.species)

# Create 2 dog variables and store them in 2 separate variables
# this is called "instantiation". You are creating 2 dog objects, or 2 "instances" of a dog.
# this calls the __init__ constructor method.
dog_1 = Dog("Buddy", "Golden Retriever", "M")
dog_2 = Dog("Princess", "German Shepherd", "F")

# try printing out the variables you just made. Its not very useful yet.
print(dog_1)
print(dog_2)

# Now try printing out each dog's name. You can access instance variables
# by referencing the variable the object is stored in, then using .
# like dog_1.variable_name

print(dog_1.name)
print(dog_2.name)

# You can also alter any variables stored in a class. Alter the first dog's name, then print it out again
dog_1.name = "Henry"
print(dog_1.name)

# methods are accessed in the same way as variables.
# you call methods by typing the instance of the class (like dog1) then . then the method name:
# so instance.methodName()
# print out the 

print(dog_1.doggy_description())
print(dog_2.doggy_description())

# try putting the 

