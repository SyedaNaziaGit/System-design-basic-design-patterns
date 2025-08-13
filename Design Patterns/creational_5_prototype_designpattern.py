'''
Let’s say we have a Book class, and we want to clone the book object instead of creating new book instances from
scratch every time.
'''
import copy
# Prototype class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    # The clone method (deep copy in Python)
    def clone(self):
        return copy.deepcopy(self)
# Client code
book1 = Book("1984", "George Orwell")
# Cloning the book
book2 = book1.clone()
# Changing the title of the cloned book
book2.title = "Animal Farm"
print(book1)  # Output: Book: 1984 by George Orwell
print(book2)  # Output: Book: Animal Farm by George Orwell
