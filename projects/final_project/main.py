"""
Final Project: Student Management System
A console CRUD application combining variables, functions, OOP, file
handling, JSON persistence, and exception handling.
"""
from src.repositories.json_repository import JSONStudentRepository
from src.services.student_service import StudentService
from src.utils.validators import ValidationError

MENU = """
=== Student Management System ===
1. Add student
2. View all students
3. Search student by name
4. Update student
5. Delete student
6. Exit
"""


def print_students(students):
    if not students:
        print("No students found.")
        return
    for s in students:
        print(f"[{s.student_id}] {s.name} - {s.major} - GPA {s.gpa}")


def main():
    service = StudentService(JSONStudentRepository())

    while True:
        print(MENU)
        choice = input("Choose an option (1-6): ").strip()
        try:
            if choice == "1":
                name = input("Name: ")
                major = input("Major: ")
                gpa = input("GPA (0.0-4.0): ")
                student = service.add_student(name, major, gpa)
                print(f"Added: {student}")
            elif choice == "2":
                print_students(service.list_students())
            elif choice == "3":
                name = input("Name to search: ")
                result = service.find_student(name)
                print(result if result else "Not found.")
            elif choice == "4":
                student_id = int(input("Student ID to update: "))
                gpa = input("New GPA (leave blank to skip): ")
                fields = {}
                if gpa.strip():
                    fields["gpa"] = gpa
                student = service.update_student(student_id, **fields)
                print(f"Updated: {student}")
            elif choice == "5":
                student_id = int(input("Student ID to delete: "))
                deleted = service.delete_student(student_id)
                print("Deleted." if deleted else "Student not found.")
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid option, please choose 1-6.")
        except ValidationError as exc:
            print(f"Validation error: {exc}")
        except ValueError:
            print("Please enter a valid number where required.")


if __name__ == "__main__":
    main()
