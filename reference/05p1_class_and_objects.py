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

# ================
# # OOP PRACTICE 1
# ================

# 1. PRACTICE
# Make a Book class with the following requirements:

# PART 1:
# Create a class named Book.
#
# The class should have the following instance variables:
#
# - title (The title of the book)
# - author (The author of the book)
# - total_pages (The number of pages in the book)
# - current_page (The page the reader is currently on, default to 1)
#
# Implement the `Book` class and create the __init__ constructor with the
# specified instance variables. Then, create a 2 instances of the `Book` class
# (choose your own books, titles, and total_pages) Print out each book's title
# after you create them both.

class Book:
    def __init__(self, title, author, total_pages, current_page = 1):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page
    
    def read(self, num_pages):
        if self.current_page == self.total_pages:
            print(f"You've already reached the end of {self.title}!")
        elif self.current_page + num_pages <= self.total_pages:
            self.current_page += num_pages
        else:
            self.current_page = self.total_pages
            
    def current_status(self):
        return(f"Reading {self.title} by {self.author}. Currently on page {self.current_page} of {self.total_pages}.")
    
book_1 = Book("Mistborn", "Brandon Sanderson", 450)
book_2 = Book("Pride and Prejudice", "Jane Austen", 500)

print(book_1.title)
print(book_2.title)

# PART 2:
# Add these methods to the Book class:
#
# - read(self, num_pages): Increases the `current_page` by the number in
#       `num_pages`. Make it unable to go past the total_pages amount.
#       If current_page is already at the last page at the book, just print
#       out "You've already reached the end of <book title>!"
#
# - current_status(self): Returns the current status in the format:
#       "Reading '<title>' by <author>. Currently on page <current_page> of
#       <total_pages>."
#
# Choose the 2nd of the books you wrote, print out the current_status
# and then read 72 pages. Then print out the current status again.

print(book_2.current_status())

book_2.read(72)
print(book_2.current_status())


# PART 3:
# Put both of the books you made into a list. Then loop through the list and
# run the current_status() method on each. Then get rid of the first book from
# your list using the remove() function. Check if you can still print the title
# of the first book from the original variable.

list_of_books = [book_1, book_2]

for book in list_of_books:
    print(book.current_status())

list_of_books.remove(book_1)
print(book_1.author)
