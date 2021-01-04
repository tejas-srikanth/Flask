class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}>"
    
    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPES[0], weight)
    
    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.TYPES[1], weight)
    
print(Book.paperback("Trial", 600))