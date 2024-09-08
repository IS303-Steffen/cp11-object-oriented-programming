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

# To practice, make a Book class with the following requirements:

# Requirements:
'''
PART 1:

    Create a class named Book.
    The class should have the following instance variables:
        - title (The title of the book)
        - author (The author of the book)
        - total_pages (The number of pages in the book)
        - current_page (The page the reader is currently on, default to 1)

    Implement the `Book` class and create the __init__ constructor with the specified instance variables. 
    Then, create a 2 instances of the `Book` class (choose your own books, titles, and total_pages)

    Print out each book's title after you create them both.

PART 2:
    Add these methods to the Book class:
    - turn_page(self): Increases the `current_page` by 1. If the reader is on the last page and tries to turn the page,
            it should print a message "You've reached the end of the book!" and not increase the `current_page`.
    - current_status(self): Returns the current status in the format: "Reading '<title>' by <author>. Currently on page <current_page> of <total_pages>."

    Choose the 2nd of the books you wrote, print out the current_status, and then turn the page 50 times. then print out the current status again.

PART 3:
    Put both of the books you made into a list. Theen loop through the list and run the current_status() method on each.
    Then get rid of the first book from your list using the remove() function.
    Check if you can still print the title of the first book from the original variable.
'''

class Book:
    def __init__(self, title, author, total_pages, current_page = 1):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page
    
    def turn_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
        else:
            print("You've reached the end of the book!")
        
    
    def current_status(self):
        return(f"Reading {self.title} by {self.author}. Currently on page {self.current_page} of {self.total_pages}.")
    
book_1 = Book("Python Basics", "John Doe", 150)
book_2 = Book("Pride and Prejudice", "Jane Austen", 500)

print(book_1.title)
print(book_2.title)

print(book_2.current_status())

for _ in range(50):
    book_2.turn_page()

print(book_2.current_status())

list_of_books = [book_1, book_2]

for book in list_of_books:
    print(book.current_status())

list_of_books.remove(book_1)
print(book_1.author)
