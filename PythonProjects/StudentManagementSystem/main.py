
class Student:
    """Represent a student and their academic records."""

    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.__marks = {}  # Private attribute

    def add_marks(self, subject, marks):
        """Add marks for a subject."""
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        self.__marks[subject] = marks
        print(f"Marks added for {self.name}.")

    def calculate_average(self):
        """Calculate the average of recorded marks."""
        if not self.__marks:
            return 0

        return sum(self.__marks.values()) / len(self.__marks)

    def calculate_grade(self):
        """Calculate a grade based on average marks."""
        average = self.calculate_average()

        if average >= 80:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 40:
            return "C"
        else:
            return "F"

    def display_report(self):
        """Display the student's academic report."""
        print("\n--- Student Report ---")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

        if not self.__marks:
            print("No marks recorded.")
        else:
            print("Subject-wise marks:")

            for subject, marks in self.__marks.items():
                print(f"  {subject}: {marks}")

            print(f"Average: {self.calculate_average():.2f}")
            print(f"Grade: {self.calculate_grade()}")


class GraduateStudent(Student):
    """Represent a graduate student with a research topic."""

    def __init__(self, student_id, name, age, research_topic):
        super().__init__(student_id, name, age)
        self.research_topic = research_topic

    def display_report(self):
        """Extend the standard report with research information."""
        super().display_report()
        print(f"Research topic: {self.research_topic}")


class StudentManagementSystem:
    """Manage student registration and searches."""

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.student_id in self.students:
            print("Student ID already exists.")
            return

        self.students[student.student_id] = student
        print("Student registered successfully.")

    def display_all_students(self):
        if not self.students:
            print("No students registered.")
            return

        for student in self.students.values():
            print(
                f"ID: {student.student_id} | "
                f"Name: {student.name} | "
                f"Age: {student.age}"
            )

    def search_student(self, student_id):
        student = self.students.get(student_id)

        if student is None:
            print("Student not found.")
        else:
            student.display_report()

    def add_student_marks(self, student_id, subject, marks):
        student = self.students.get(student_id)

        if student is None:
            print("Student not found.")
            return

        student.add_marks(subject, marks)


def main():
    system = StudentManagementSystem()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Register regular student")
        print("2. Register graduate student")
        print("3. Display all students")
        print("4. Add subject marks")
        print("5. Search student and view report")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_id = input("Student ID: ").strip()
            name = input("Student name: ").strip()
            age = int(input("Student age: "))

            student = Student(student_id, name, age)
            system.add_student(student)

        elif choice == "2":
            student_id = input("Student ID: ").strip()
            name = input("Student name: ").strip()
            age = int(input("Student age: "))
            topic = input("Research topic: ").strip()

            student = GraduateStudent(
                student_id, name, age, topic
            )
            system.add_student(student)

        elif choice == "3":
            system.display_all_students()

        elif choice == "4":
            student_id = input("Student ID: ").strip()
            subject = input("Subject: ").strip()

            try:
                marks = float(input("Marks (0-100): "))
                system.add_student_marks(
                    student_id, subject, marks
                )
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            student_id = input("Student ID: ").strip()
            system.search_student(student_id)

        elif choice == "6":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
