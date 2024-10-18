"""
The Iterator Pattern is a behavioral design pattern that provides a way to access elements of a collection (like a list or a tree) 
sequentially without exposing the underlying representation. The pattern is useful for traversing collections in a uniform way, 
regardless of the specific type of collection used.

Key Concepts:
Iterator: An object that encapsulates the traversal of a collection and provides access to the elements one at a time.
Aggregate (Collection): The collection object that holds the data elements. It provides a method to return an iterator object.
Client: The code that uses the iterator to traverse the collection.
When to Use:
When you need to traverse a collection of objects without exposing the collection's underlying structure.
When the collection needs different ways to traverse through its elements.
When you want a uniform way of accessing elements in different types of collections (e.g., arrays, lists, trees).
"""

# Item (Object to iterate over)
class Book:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

# Iterator
class BookIterator:
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration

# Collection (Aggregate)
class BookCollection:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def __iter__(self):
        return BookIterator(self._books)

# Usage
if __name__ == "__main__":
    book_collection = BookCollection()
    book_collection.add_book(Book("The Catcher in the Rye"))
    book_collection.add_book(Book("To Kill a Mockingbird"))
    book_collection.add_book(Book("1984"))

    # Using the iterator to traverse the collection
    for book in book_collection:
        print("Book:", book.get_title())
