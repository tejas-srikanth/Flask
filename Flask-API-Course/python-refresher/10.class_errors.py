class TooManyPagesReadError(Exception):
    pass

class Book:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr__(self):
        return (
            f"<Book {self.name}, {self.page_count} pages"
        )

    def read(self, pages):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(f"You were going to read {self.pages_read + pages} pages but there are only {self.page_count} pages in the book")
        else:
            self.pages_read += pages

py101 = Book("Python 101", 50)
try:
    py101.read(30)
    py101.read(10)
except TooManyPagesReadError as e:
    print(e)
else:
    print("All your pages are read")
finally:
    print("You have finished reading the book")