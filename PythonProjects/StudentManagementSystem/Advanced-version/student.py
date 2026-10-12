
class Student:
    """Represent a student and their academic records."""

    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.__marks = {}

    def add_marks(self, subject, marks):
        """Add or update marks for a subject."""
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")

        self.__marks[subject] = marks

    def calculate_average(self):
        """Return the average of recorded marks."""
        if not self.__marks:
            return 0.0

        return sum(self.__marks.values()) / len(self.__marks)

    def calculate_grade(self):
        """Return a grade based on average marks."""
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
            return

        for subject, marks in self.__marks.items():
            print(f"{subject}: {marks}")

        print(f"Average: {self.calculate_average():.2f}")
        print(f"Grade: {self.calculate_grade()}")


class GraduateStudent(Student):
    """Represent a student conducting graduate research."""

    def __init__(self, student_id, name, age, research_topic):
        super().__init__(student_id, name, age)
        self.research_topic = research_topic

    def display_report(self):
        """Display academic and research information."""
        super().display_report()
        print(f"Research topic: {self.research_topic}")
