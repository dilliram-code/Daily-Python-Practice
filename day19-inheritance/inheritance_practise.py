from abc import ABC, abstractmethod
from typing import List

# -------------------------
# Base / Abstract class
# -------------------------
class Person(ABC):
    """
    Abstract base class that represents a generic person.
    Subclasses must implement get_role().
    """
    species = "Homo sapiens"               # class variable shared by subclasses

    def __init__(self, name: str, age: int, **kwargs):
        # required attributes
        self.name = name
        self.age = age

        # "protected" attribute (convention with single underscore)
        self._id = kwargs.pop("id", None)

        # "private" attribute (name-mangled to _Person__secret)
        self.__secret = kwargs.pop("secret", None)

        # NOTE: do NOT call super().__init__(**kwargs) here because object.__init__
        # does not accept arbitrary kwargs. Instead, each intermediate class
        # should consume its own kwargs and forward remaining ones.

    @abstractmethod
    def get_role(self) -> str:
        """Every concrete subclass must return its role name."""
        raise NotImplementedError

    def greet(self) -> str:
        return f"Hi, I'm {self.name} ({self.get_role()})"

    @classmethod
    def species_info(cls) -> str:
        return f"{cls.__name__} belongs to {cls.species}"

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    def reveal_secret(self):
        # private attributes are name-mangled to _Person__secret
        return getattr(self, "_Person__secret", None)

# -------------------------
# Single & multilevel inheritance
# -------------------------
class Employee(Person):
    def __init__(self, salary: float = 0.0, **kwargs):
        self.salary = salary
        # forward remaining keywords (name, age, id, secret) to Person
        super().__init__(**kwargs)

    def get_role(self) -> str:
        return "Employee"

    def work(self) -> str:
        return f"{self.name} (Employee) is working and earns {self.salary}"

class Teacher(Employee):
    def __init__(self, subject: str = "General", **kwargs):
        self.subject = subject
        super().__init__(**kwargs)

    def get_role(self) -> str:
        return "Teacher"

    # method overriding: Teacher provides its own implementation of work()
    def work(self) -> str:
        return f"{self.name} is teaching {self.subject}"

# -------------------------
# Another subclass of Person
# -------------------------
class Student(Person):
    def __init__(self, grade: str = "N/A", **kwargs):
        self.grade = grade
        super().__init__(**kwargs)

    def get_role(self) -> str:
        return "Student"

    def study(self) -> str:
        return f"{self.name} is studying for {self.grade}"

    # overriding greet() to demonstrate polymorphism
    def greet(self) -> str:
        return f"Hey — I'm {self.name}, a {self.grade} student."

# -------------------------
# Multiple inheritance (cooperative)
# -------------------------
class TeachingAssistant(Teacher, Student):
    """
    Demonstrates multiple inheritance. We rely on cooperative __init__ calls
    (each class consumes its kwargs then calls super().__init__(**kwargs)).
    MRO ensures Person.__init__ runs once.
    """

    def get_role(self) -> str:
        return "Teaching Assistant"

    def assist(self) -> str:
        return f"{self.name} assists in {self.subject} while studying {self.grade}"

# -------------------------
# Composition example
# -------------------------
class Course:
    def __init__(self, title: str, teacher: Teacher, students: List[Student]):
        self.title = title
        self.teacher = teacher    # composition: Course has-a Teacher
        self.students = students  # Course has-a list of Students

    def course_summary(self) -> str:
        student_names = ", ".join(s.name for s in self.students)
        return f"Course '{self.title}' taught by {self.teacher.name}. Students: {student_names}"

# -------------------------
# Polymorphism / duck typing helper
# -------------------------
def person_activity(people: List[Person]):
    """
    Demonstrates polymorphism and duck typing:
    - calls greet() on any Person
    - calls work(), study(), assist() only if the object provides them
    """
    for p in people:
        print(p.greet())

        # polymorphic behavior: we don't care about concrete type,
        # just what methods an object supports (duck typing)
        if hasattr(p, "work"):
            print("  ->", p.work())
        if hasattr(p, "study"):
            print("  ->", p.study())
        if hasattr(p, "assist"):
            print("  ->", p.assist())

        print()

# -------------------------
# Demo / Run
# -------------------------
if __name__ == "__main__":
    # create instances (use keyword args to cooperate across MRO)
    teacher = Teacher(name="Mr. Smith", age=40, salary=3200.0, subject="Physics", id=1, secret="loves tea")
    student = Student(name="Jane Doe", age=20, grade="BSc", id=2, secret="practices violin")
    ta = TeachingAssistant(name="Sam Lee", age=24, salary=1500.0, subject="Math", grade="MSc", id=3, secret="loves pizza")

    # show MRO for multiple inheritance clarity
    print("TeachingAssistant MRO:", [c.__name__ for c in TeachingAssistant.__mro__])
    print()

    # classmethod & staticmethod demo
    print(Person.species_info())
    print("Is 17 adult?", Person.is_adult(17))
    print("Is 21 adult?", Person.is_adult(21))
    print()

    # encapsulation: reveal private attribute (name-mangled)
    print("Teacher's hidden secret (via Person logic):", teacher.reveal_secret())
    print("Student secret:", student.reveal_secret())
    print("TA secret:", ta.reveal_secret())
    print()

    # polymorphism / duck typing demo
    all_people = [teacher, student, ta]
    person_activity(all_people)

    # composition
    course = Course("Calculus 101", teacher=teacher, students=[student, ta])
    print(course.course_summary())
    print()

    # show that overriding works
    print("teacher.work() ->", teacher.work())
    print("student.study() ->", student.study())
    print("ta.assist() ->", ta.assist())
