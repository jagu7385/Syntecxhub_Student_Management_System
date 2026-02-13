import json
import os


# Student Class
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grade": self.grade
        }



# Student Manager Class
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    # Load students from file
    def load_students(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    return [Student(**student) for student in data]
            except json.JSONDecodeError:
                return []
        return []

    # Save students to file
    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    # Add new student
    def add_student(self, name, student_id, grade):
        if self.find_student(student_id):
            print("❌ Error: Student ID must be unique.")
            return
        new_student = Student(name, student_id, grade)
        self.students.append(new_student)
        self.save_students()
        print("✅ Student added successfully.")

    # Find student by ID
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    # Update student
    def update_student(self, student_id, new_name, new_grade):
        student = self.find_student(student_id)
        if student:
            student.name = new_name
            student.grade = new_grade
            self.save_students()
            print("✅ Student updated successfully.")
        else:
            print("❌ Student not found.")

    # Delete student
    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            self.save_students()
            print("✅ Student deleted successfully.")
        else:
            print("❌ Student not found.")

    # List all students
    def list_students(self):
        if not self.students:
            print("⚠️ No student records found.")
            return

        print("\n" + "-" * 50)
        print(f"{'ID':<10}{'Name':<20}{'Grade':<10}")
        print("-" * 50)

        for student in self.students:
            print(f"{student.student_id:<10}{student.name:<20}{student.grade:<10}")

        print("-" * 50)



# CLI Menu
def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            grade = input("Enter grade: ")
            manager.add_student(name, student_id, grade)

        elif choice == "2":
            student_id = input("Enter student ID to update: ")
            new_name = input("Enter new name: ")
            new_grade = input("Enter new grade: ")
            manager.update_student(student_id, new_name, new_grade)

        elif choice == "3":
            student_id = input("Enter student ID to delete: ")
            manager.delete_student(student_id)

        elif choice == "4":
            manager.list_students()

        elif choice == "5":
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
