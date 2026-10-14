
from student import Student, GraduateStudent
from student_manager import StudentManagementSystem


def main():
    system = StudentManagementSystem()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Register regular student")
        print("2. Register graduate student")
        print("3. Display all students")
        print("4. Add subject marks")
        print("5. View student report")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                student_id = input("Student ID: ").strip()
                name = input("Name: ").strip()
                age = int(input("Age: "))

                if not student_id or not name or age <= 0:
                    raise ValueError(
                        "ID and name are required; age must be positive."
                    )

                student = Student(student_id, name, age)
                system.add_student(student)
                print("Student registered successfully.")

            elif choice == "2":
                student_id = input("Student ID: ").strip()
                name = input("Name: ").strip()
                age = int(input("Age: "))
                topic = input("Research topic: ").strip()

                if not student_id or not name or age <= 0 or not topic:
                    raise ValueError("All fields must be valid.")

                student = GraduateStudent(
                    student_id, name, age, topic
                )
                system.add_student(student)
                print("Graduate student registered successfully.")

            elif choice == "3":
                system.display_all_students()

            elif choice == "4":
                student_id = input("Student ID: ").strip()
                subject = input("Subject: ").strip()
                marks = float(input("Marks (0-100): "))

                if not subject:
                    raise ValueError("Subject cannot be empty.")

                system.add_student_marks(
                    student_id, subject, marks
                )
                print("Marks recorded successfully.")

            elif choice == "5":
                student_id = input("Student ID: ").strip()
                system.display_student_report(student_id)

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid menu choice.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
