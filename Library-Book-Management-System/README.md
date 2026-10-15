
# 📚 Library Book Management System

A beginner-friendly Library Book Management System built using Python and Object-Oriented Programming (OOP).

This project allows users to manage library books through a simple menu-driven program.

## ✨ Features

- ➕ Add new books to the library
- 📋 Display all books
- 🔍 Search for a book by its ID
- 📖 Borrow a book
- 📥 Return a book
- ✅ Check book availability
- 🚪 Exit the program

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** Object-Oriented Programming (OOP)
- **Data Storage:** Python list (in-memory)

## 🧠 OOP Concepts Practiced

- Classes and objects
- Constructors (`__init__`)
- Instance attributes and methods
- Lists of objects
- Functions and code reusability
- Conditional statements and loops
- Searching with `next()`
- Handling missing records with `None`

## ▶️ How to Run

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

   ```bash
   python library_management.py
   ```

   If your system uses `python3`, run:

   ```bash
   python3 library_management.py
   ```

## 📌 How It Works

Each book is represented by an object of the `library_Book` class.

Every book stores:
- Book title
- Author name
- Book ID
- Availability status

The program stores book objects in a list and uses a reusable `find_book()` function to search for books by ID.

## ⚠️ Limitations

- Book records are stored in memory and are lost when the program closes.
- Each book should have a unique ID.
- The program runs in the terminal and uses a text-based menu.

## 🚀 Future Improvements

- Prevent duplicate book IDs.
- Save book records to a file.
- Add a feature to delete books.
- Improve input validation and error handling.
- Add a graphical user interface (GUI).

## 👨‍💻 Author

Created as a Python OOP learning project.

---

⭐ If you find this project useful, feel free to explore and improve it!
