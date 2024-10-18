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
# EXTRA OOP PRACTICE
# ==================

'''
NOTE
----
I very likely won't go over this example in class. Use it to practice on your
own. It is a longer practice question and it uses datetime objects:

    from datetime import datetime, timedelta
    
which we haven't gone over in detail. It might be good practice for learning
a new skill that you haven't been shown explicit examples of, which is good
practice for learning new programming techniques in the real world.
'''

# 1. PRACTICE
# Event Organizer Class
# You are tasked with creating a Python class named Event that manages events.
# Each event will have a name, a date and time, participants, and a location.
# Your class should allow for adding and removing participants, updating the
# event details, and displaying the Event's current information.


# PART 1: 
# Create the Event class with the following methods:
#   - Constructor (__init__): Initializes an event with a name, date_and_time,
#       location, and list_of_participants. Don't include list_of_participants
#       as a parameter, just make it equal to an empty list inside the
#       constructor.
#
#   - display_event: Prints the event's details, including the name, date,
#       location, and a list of participants. Ensure the list of participants
#       looks nice when printing it. If you have time, try out the .strftime
#       datetime function, like date_and_time.strftime.('%B %d, %Y at %H:%M')
#
# Then, create 2 Event objects.
# - For the date, use python's datetime. That means you should include
#       "from datetime import datetime" at the top of your code. You can make a
#        datetime object like this: datetime(year, month, day, hour, minute)
# - You don't need to add any participants yet.
# - run display_event() on each object.

from datetime import datetime, timedelta
import random

class Event:
    def __init__(self, name, date_and_time, location):
        self.name = name
        self.date_and_time = date_and_time
        self.location = location
        self.participants = []

    def display_event(self):
        print(f"Event Name: {self.name}")
        print(f"Date: {self.date_and_time.strftime('%B %d, %Y at %I:%M %p')}")
        print(f"Location: {self.location}")
        print("Participants:")
        for participant in self.participants:
            print(f"\t{participant}")


    def add_participant(self, name):
        if name not in self.participants:
            self.participants.append(name)
        else:
            print(f"{name} is already registered for the event.")

    def shift_day(self, num_days):
        self.date_and_time += timedelta(days=num_days)

# Create 2 Event objects
event1 = Event("Code Workshop", datetime(2024, 3, 15, 14, 30), "Community Center")
event2 = Event("Python Meetup", datetime(2024, 4, 20, 18, 00), "Tech Hub")

# Display events
event1.display_event()
print()
event2.display_event()

# PART 2:
# Add this new method:
# - add_participant: Adds a new participant to the event's list of
#       participants. Participants are just represented by their names. Make it
#       so that it won't add a participant twice (you can print a message if
#       the participant is already in the event)
#
# Make up a list of 5 names. Randomly choose 3 to be a part of each of the 2
# event objects you made. Run display_event again on each object.

names = ["Alice", "Bob", "Charlie", "Dana", "Eli"]

# Randomly choose 3 names for each event (for example)
random_names_event1 = random.sample(names, 3)
random_names_event2 = random.sample(names, 3)

for name in random_names_event1:
    event1.add_participant(name)

for name in random_names_event2:
    event2.add_participant(name)

print()
event1.display_event()
print()
event2.display_event()

# PART 3:
# Add this new method:
#   - shift_day: takes a number (or negative number) as a parameter and
#       increases (or decreases) the day of the event. Note, this means using
#       the timedelta class from datetime (which we haven't practiced much).

# Change the date of your event to be 10 days later by using the shift_day
# method. Run display_event again on that object to show the change.

event1.shift_day(10)

print("\nNotice it has shifted 10 days in the future:\n")
event1.display_event()