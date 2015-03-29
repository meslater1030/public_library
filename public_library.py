
whole_library = {}

# Library object


class Library(object):
    # the library creates space for its shelves on initialization
    def __init__(self, num_shelves):
        self.num_shelves = num_shelves
        for shelf in range(1, self.num_shelves + 1):
            whole_library[shelf] = []

    # reports on all books in the library
    def report(self):
        for books in whole_library.itervalues():
            for book in books:
                print book + '\t'

# Shelf object


class Shelf(object):
    # the shelf knows which shelf it is
    def __init__(self, shelf_num):
        self.shelf_num = shelf_num

    # this function prints out the books located on this shelf
    def which_books(self):
        for book in whole_library[self.shelf_num]:
            print book

# Book object


class Book(object):
    # the book knows which book it is
    def __init__(self, name):
        self.name = name

    # this function puts the book on a shelf
    def enshelf(self, shelf_num):
        whole_library[shelf_num] = whole_library[shelf_num] + [self.name]

    # this function finds the book and removes it from its shelf
    def unshelf(self):
        try:
            for shelf, books in whole_library.iteritems():
                for book in books:
                    if self.name == book:
                        whole_library[shelf].remove(book)
        except TypeError:
            pass

this_library = Library(6)
this_library.report()
shelf3 = Shelf(3)
shelf3.which_books()
this_book = Book('The Pearl')
this_book.enshelf(2)
shelf2 = Shelf(2)
shelf2.which_books()
this_book.unshelf()
this_book.enshelf(3)
shelf3.which_books()
