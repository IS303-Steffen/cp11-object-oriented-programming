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


class Dog:
    species = "Canis lupus familiaris" # class variable

    def __init__(self, name, breed, sex = "F"):
        # Instance variables. Must use self. to be instance variables
        self.name = name
        self.breed = breed
        self.sex = sex
    
# You can access class variables as soon as the class is defined.
# you don't have to create a specific object to access them:

print(f"This is the class variable: {Dog.species}")

# create 2 dog objects:
dog_1 = Dog("Buddy", "Golden Retriever", "M")
dog_2 = Dog("Princess", "German Shepherd", "F")

# when you create an instance of a dog, you can access the class variable,
# even though it isn't an instance variable:
# try printing out dog_1.species
print(dog_1.species)

# think of it this way:
'''
    When you try to access a variable by doing instanceName.variableName:

    FIRST: python checks if that variable exists as an instance variable.
        If it can find the variable, it stops there.

    SECOND: if it didn't find an instance variable, THEN it checks for class variables.
'''

# what happens when you change the value of species in the dog_1 instance?
# change dog_1.species
dog_1.species = "Alien dog"
print(dog_1.species)
# will it change the class variable of Dog.species too?
# check Dog.species
print(Dog.species)
# what about dog_2.species
print(dog_2.species)

# now let's change Dog.species
Dog.species = "Actually a cat"

# what will happend to dog_1.species and dog_2.species?
print(dog_1.species)
print(dog_2.species)

dog_1.wow_new_instance_Variable = "wow"


'''
Summary: two main points:

    1. You can create new instance variables whenever. Be careful. 
    2. Python checks first if there is an instance variable with that name,
       then checks if there is a class variable.

'''

