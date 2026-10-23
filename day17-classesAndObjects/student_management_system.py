
class Student:
    # Class variable: shared by all student objects
    school_name = "ABC Secondary School"
    total_students = 0

    def __init__(self, name, age, marks):
        # Instance variables: unique to each student
        self.name = name
        self.age = age
        self.marks = marks

        # Update the shared student count
        Student.total_students += 1

    # 1. INSTANCE METHOD
    def display_info(self):
        """Display information about an individual student."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"School: {self.school_name}")
        print(f"Grade: {self.calculate_grade()}")

    # 2. CLASS METHOD
    @classmethod
    def change_school(cls, new_school):
        """Change the school name for the entire class."""
        cls.school_name = new_school
        print(f"School changed to: {cls.school_name}")

    @classmethod
    def get_total_students(cls):
        """Return the total number of students created."""
        return cls.total_students

    # 3. STATIC METHOD
    @staticmethod
    def is_valid_marks(marks):
        """Check whether marks are within the valid range."""
        return 0 <= marks <= 100

    # Another instance method
    def calculate_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "Fail"


# -------------------------------
# MAIN PROGRAM
# -------------------------------

# Create student objects
student1 = Student("Ram", 20, 85)
student2 = Student("Sita", 19, 72)
student3 = Student("Hari", 21, 35)

# Use instance methods
print("=== STUDENT DETAILS ===")
student1.display_info()

print("\n=== ANOTHER STUDENT ===")
student2.display_info()

# Use the static method
print("\n=== MARKS VALIDATION ===")
print(Student.is_valid_marks(85))   # True
print(Student.is_valid_marks(120))  # False

# Use the class method
print("\n=== SCHOOL INFORMATION ===")
Student.change_school("Modern Secondary School")

# Existing objects also see the updated class variable
print(student1.school_name)
print(student2.school_name)

# Get total number of students
print("\nTotal students:", Student.get_total_students())
