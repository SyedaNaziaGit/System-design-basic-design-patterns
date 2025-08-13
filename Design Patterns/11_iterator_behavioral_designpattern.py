'''
Let's say we have a custom collection (a BookCollection) that stores books, and we want to iterate over this 
collection. The Iterator Pattern will allow us to traverse the collection without exposing its underlying structure 
(like a list or dictionary).
'''
# Iterable collection class
class BookCollection:
    def __init__(self):
        self.books = []
        
    def add_book(self,book):
        self.books.append(book)
    
    def __iter__(self):
        return BookIterator(self.books)
# Iterator class
class BookIterator(BookCollection):
    def __init__(self,books):
        self.books = books
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index +=1
            return book
        else:
            raise StopIteration  # No more elements to iterate over
#Client Code
book_collection = BookCollection()
book_collection.add_book("The Great Gatsby")
book_collection.add_book("1984")
book_collection.add_book("To Kill a Mockingbird")
# Using the iterator to traverse the collection
for book in book_collection:
    print(book)

'''
Output:
The Great Gatsby
1984
To Kill a Mockingbird
'''