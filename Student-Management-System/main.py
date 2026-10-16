class Student:
    def __init__(self, student_name, student_id, marks):
        self.student_name = student_name
        self.ID = student_id
        self.marks = marks

    def display(self):
        print(f"Name: {self.student_name} | ID: {self.ID} | Marks: {self.marks}")

    def check_status(self):
        if self.marks >= 50:
            print(f"{self.student_name} has passed!")
        else:
            print(f"{self.student_name} has failed!")


students = []


def add_student():
    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()

    for existing_student in students:
        if existing_student.ID == student_id:
            print(f"Student ID {student_id} is already registered.")
            return

    try:
        marks = int(input("Enter student marks (0-100): "))
    except ValueError:
        print("Please enter a valid whole number for marks.")
        return

    if not 0 <= marks <= 100:
        print("Invalid marks! Marks must be between 0 and 100.")
        return

    student = Student(name, student_id, marks)
    students.append(student)
    print("Student added successfully!")


def search_student():
    search_id = input("Enter student ID to search: ").strip()
    student = next(
        (student for student in students if student.ID == search_id),
        None
    )

    if student is not None:
        student.display()
    else:
        print("Student not found!")


def display_all_students():
    if not students:
        print("No students are registered.")
        return

    for student in students:
        student.display()


def check_student_status():
    search_id = input("Enter student ID to check: ").strip()
    student = next(
        (student for student in students if student.ID == search_id),
        None
    )

    if student is not None:
        student.check_status()
    else:
        print("Student not found!")

def update_marks():
    search_id = input("Enter the student id you want to update marks for: ")
    student = next((s for s in students if student.ID == search_id),None)

    if student is not None:
        
        try:
            marks = int(input("Enter student marks (0-100): "))
        except ValueError:
            print("Please enter a valid whole number for marks.")
            return

        if not 0 <= marks <= 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            return
        student.marks = marks        
        print(f"{student.ID}: Marks updated successfully!")
    else:
        print("Student not Found!")
    
while True:
    print(
        "\nStudent Management System"
        "\n1. Add a student"
        "\n2. Search for a student"
        "\n3. Display all students"
        "\n4. Check pass/fail status"
        "\n5. Exit"
        "\n6. Update students marks"
        )

    user_input = input("Enter your choice: ").strip()

    if user_input == "1":
        add_student()
    elif user_input == "2":
        search_student()
    elif user_input == "3":
        display_all_students()
    elif user_input == "4":
        check_student_status()
    elif user_input == "5":
        print("Program exited.")
        break
    elif user_input == "6":
        update_marks()
    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
