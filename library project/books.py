class Book:
    def __init__(self,title,author,is_borrowed=False):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed

    def __str__(self):
        status="Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def list_books(self):
        return self.books

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                return f"✅ '{book.title}' has been borrowed."
        return "❌ Book not available or already borrowed."

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                return f"✅ '{book.title}' has been returned."
        return "❌ Book not found or not borrowed."