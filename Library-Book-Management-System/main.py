
class Library_Book:
    def __init__(self, title, author, book_id, is_available=True):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = is_available

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Book ID: {self.book_id}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print("Book borrowed successfully!")
        else:
            print("Book is already issued!")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print("Book returned successfully!")
        else:
            print("Book is already available!")

    def check_status(self):
        if self.is_available:
            print(f"{self.title} is available!")
        else:
            print(f"{self.title} is not available!")


books = []


def book_creation():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = input("Enter book ID: ")

    if find_book(book_id) is not None:
        print("A book with this ID already exists!")
        return

    book = Library_Book(title, author, book_id)
    books.append(book)
    print("Book added successfully!")


def find_book(book_id):
    return next((book for book in books if book.book_id == book_id), None)


def search_and_perform(action):
    book_id = input("Enter Book ID: ")
    book = find_book(book_id)

    if book is None:
        print("Book not found!")
        return

    if action == "search":
        book.display()
    elif action == "borrow":
        book.borrow_book()
    elif action == "return":
        book.return_book()
    elif action == "status":
        book.check_status()


while True:
    user_input = input("""
Library Book Management System

1. Add Book
2. Display All Books
3. Search Book by ID
4. Borrow Book
5. Return Book
6. Check Book Status
e. Exit

Enter your choice: """).strip().lower()

    if user_input == "1":
        book_creation()

    elif user_input == "2":
        if not books:
            print("No books in the library.")
        else:
            for book in books:
                print()
                book.display()

    elif user_input == "3":
        search_and_perform("search")

    elif user_input == "4":
        search_and_perform("borrow")

    elif user_input == "5":
        search_and_perform("return")

    elif user_input == "6":
        search_and_perform("status")

    elif user_input == "e":
        print("Program exited!")
        break

    else:
        print("Invalid choice! Please try again.")
