from person import User, Admin
from actions import ExtendedLibrary

library = ExtendedLibrary()

user_ruthika = User("Ruthika", "ruthika@example.com")
admin_rahul = Admin("Rahul", "rahul@library.com")

def display_books():
    print("\n📚 Available Books:")
    for idx, book in enumerate(library.list_books(), 1):
        print(f"{idx}. {book}")
    print()

def user_menu(user):
    while True:
        print(f"\n👤 Welcome, {user.name}")
        print("1. View Available Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("👉 Enter your choice: ")

        if choice == '1':
            display_books()

        elif choice == '2':
            title = input("Enter book title to borrow: ")
            result = library.borrow_book(title, user)
            print(result)

        elif choice == '3':
            title = input("Enter book title to return: ")
            result = library.return_book(title, user)
            print(result)

        elif choice == '4':
            print("👋 Exiting User Menu...")
            break

        else:
            print("⚠️ Invalid choice. Try again.")

def admin_menu(admin):
    while True:
        print(f"\n🛠️ Admin Panel - {admin.name}")
        print("1. View Available Books")
        print("2. Add New Book")
        print("3. Exit")
        choice = input("👉 Enter your choice: ")

        if choice == '1':
            display_books()

        elif choice == '2':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(title, author)
            print(f"✅ Book '{title}' by {author} added.")

        elif choice == '3':
            print("👋 Exiting Admin Panel...")
            break

        else:
            print("⚠️ Invalid choice. Try again.")

def main():
    print("📖 Welcome to the Library Management System\n")
    while True:
        print("1. Log in as User")
        print("2. Log in as Admin")
        print("3. Exit")
        role = input("👉 Choose your role: ")

        if role == '1':
            user_menu(user_ruthika)
        elif role == '2':
            admin_menu(admin_rahul)
        elif role == '3':
            print("👋 Goodbye! Have a great day!")
            break
        else:
            print("⚠️ Invalid input. Try again.\n")

if __name__ == "__main__":
    main()
