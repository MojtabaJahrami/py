class Student:
    def __init__(self, id, national_id, name, last_name):
        self.id = id
        self.national_id = national_id
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f"Student(id={self.id}, national_id={self.national_id}, name={self.name}, last_name={self.last_name})"

students = []

def add_student():
    id = input("Enter student id: ")
    national_id = input("Enter national id: ")
    name = input("Enter student name: ")
    last_name = input("Enter student last name: ")

    student = Student(id, national_id, name, last_name)
    students.append(student)

def find_student():
    search_type = input("Enter 1 for searching by national id,\n Enter 2 for searching by student id,\n Enter 3 for searching by name,\n Enter 4 for searching by last name: ")
    if search_type == '1':
        national_id = input("Enter national id: ")
        for student in students:
            if student.national_id == national_id:
                print(student)
                return
        print("No student found.")
    elif search_type == '2':
        id = input("Enter student id: ")
        for student in students:
            if student.id == id:
                print(student)
                return
        print("No student found.")
    elif search_type == '3':
        name = input("Enter student name: ")
        for student in students:
            if student.name == name:
                print(student)
                return
        print("No student found.")
    elif search_type == '4':
        last_name = input("Enter student last name: ")
        for student in students:
            if student.last_name == last_name:
                print(student)
                return
        print("No student found.")

def list_students():
    for student in students:
        print(student)

def menu():
    while True:
        print("\n1- Add student")
        print("2- Find student")
        print("3- List all students")
        print("4- Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            find_student()
        elif choice == '3':
            list_students()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

menu()
