
class StudentManagementSystem:
    """Manage student registration and academic records."""

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        """Register a student using their ID."""
        if student.student_id in self.students:
            raise ValueError("Student ID already exists.")

        self.students[student.student_id] = student

    def get_student(self, student_id):
        """Return a student or None if not found."""
        return self.students.get(student_id)

    def display_all_students(self):
        """Display the registered students."""
        if not self.students:
            print("No students registered.")
            return

        for student in self.students.values():
            print(
                f"ID: {student.student_id} | "
                f"Name: {student.name} | "
                f"Age: {student.age}"
            )

    def add_student_marks(self, student_id, subject, marks):
        """Find a student and add their subject marks."""
        student = self.get_student(student_id)

        if student is None:
            raise ValueError("Student not found.")

        student.add_marks(subject, marks)

    def display_student_report(self, student_id):
        """Display the report of a particular student."""
        student = self.get_student(student_id)

        if student is None:
            raise ValueError("Student not found.")

        student.display_report()
