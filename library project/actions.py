from books import Book
from datetime import datetime

# Decorator to log actions
def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        action_name = func.__name__.replace('_', ' ').title()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"📋 [{timestamp}] Action Performed: {action_name}")
        return result
    return wrapper

class ExtendedLibrary:
    def __init__(self):
        self.books = [Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
        Book("The Lord of the Rings", "J.R.R. Tolkien"),
        Book("Pride and Prejudice", "Jane Austen"),
        Book("The Alchemist", "Paulo Coelho"),
        Book("The Da Vinci Code", "Dan Brown"),
        Book("The Hobbit", "J.R.R. Tolkien"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("1984", "George Orwell"),
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("The Catcher in the Rye", "J.D. Salinger")]


    @log_action
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    @log_action
    def list_books(self):
        return self.books

    @log_action
    def borrow_book(self, title, user):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                user.borrow_book(book.title)
                return f"✅ '{book.title}' borrowed by {user.name}"
        return "❌ Book not available or already borrowed."

    @log_action
    def return_book(self, title, user):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                user.return_book(book.title)
                return f"✅ '{book.title}' returned by {user.name}"
        return "❌ Book not found or not borrowed."
