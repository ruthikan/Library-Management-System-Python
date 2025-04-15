class Person:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def get_details(self,name,email):
        return f"Name : {self.name}, Email : {self.email}"

class User(Person):
    def __init__(self,name,email):
        super().__init__(name,email)
        self.borrowed_books=[]

    def borrow_book(self,book_title):
        self.borrowed_books.append(book_title)

    def return_book(self,book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
        else:
            print(f"❌ You haven't borrowed '{book_title}'.")

class Admin(Person):
    def __init__(self, name, email):
        super().__init__(name, email)