
whole_library = {}


class Library(object):
    def __init__(self, num_shelves):
        self.num_shelves = num_shelves
        for shelf in range(1, self.num_shelves + 1):
            whole_library[shelf] = []

    def report(self):
        for books in whole_library.itervalues():
            for book in books:
                print book + '\t'


class Shelf(object):
    def __init__(self, shelf_num):
        self.shelf_num = shelf_num

    def which_books(self):
        for book in whole_library[self.shelf_num]:
            print book


class Book(object):
    def __init__(self, name):
        self.name = name

    def enshelf(self, shelf_num):
        whole_library[shelf_num] = whole_library[shelf_num] + [self.name]

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
