class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f'There are {len(self.books)} books'

class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        f'book {self.name}'

book1 = Book("Harry Potter")
book2 = Book("Trial and justice")
