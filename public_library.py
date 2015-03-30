# Library object
class Library:
    def __init__(self):
        self.shelves = {}

    def addShelf(self, shelf):
        self.shelves[shelf.num] = shelf

    # reports on all books in the library
    def report(self):
        if self.shelves:
            print('All books in the Library:')
            for shelf_num in self.shelves:
                shelf = self.shelves[shelf_num]
                shelf.report()
        else:
            print('Library has no shelves yet')

# Shelf object


class Shelf:
    # the shelf knows which shelf it is
    def __init__(self, num):
        self.num = num
        self.books = {}

    def addBook(self, book):
        self.books[book.name] = book

    def removeBook(self, book):
        del self.books[book.name]

    # this function prints out the books located on this shelf
    def report(self):
        if self.books:
            print("Shelf {0} books:".format(self.num))
            for book_name in self.books:
                print("\t{0}".format(book_name))
        else:
            print("Shelf {0} has no books.".format(self.num))

# Book object


class Book:
    # the book knows which book it is
    def __init__(self, name):
        self.name = name

    # this function puts the book on a shelf
    def enshelf(self, shelf):
        self.current_shelf = shelf
        shelf.addBook(self)

    # this function finds the book and removes it from its shelf
    def unshelf(self):
        if self.current_shelf:
            self.current_shelf.removeBook(self)
            self.current_shelf = None

this_library = Library()
this_library.report()

shelf1 = Shelf(1)
shelf2 = Shelf(2)
shelf3 = Shelf(3)
shelf3.report()

this_library.addShelf(shelf1)
this_library.addShelf(shelf2)
this_library.addShelf(shelf3)

this_book = Book('The Pearl')
this_book.enshelf(shelf2)

shelf2.report()
this_book.unshelf()

this_book.enshelf(shelf3)
shelf3.report()

this_library.report()
