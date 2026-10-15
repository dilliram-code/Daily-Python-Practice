
import unittest

from student import Student


class TestStudentGrade(unittest.TestCase):
    """Test grade calculation and related behavior."""

    def setUp(self):
        # A fresh student is created before each test.
        self.student = Student("S101", "Ram", 20)

    def test_grade_a(self):
        self.student.add_marks("Math", 90)
        self.assertEqual(self.student.calculate_grade(), "A")

    def test_grade_b(self):
        self.student.add_marks("Math", 70)
        self.assertEqual(self.student.calculate_grade(), "B")

    def test_grade_c(self):
        self.student.add_marks("Math", 50)
        self.assertEqual(self.student.calculate_grade(), "C")

    def test_grade_f(self):
        self.student.add_marks("Math", 30)
        self.assertEqual(self.student.calculate_grade(), "F")

    def test_grade_at_boundary_80(self):
        self.student.add_marks("Math", 80)
        self.assertEqual(self.student.calculate_grade(), "A")

    def test_grade_at_boundary_60(self):
        self.student.add_marks("Math", 60)
        self.assertEqual(self.student.calculate_grade(), "B")

    def test_grade_at_boundary_40(self):
        self.student.add_marks("Math", 40)
        self.assertEqual(self.student.calculate_grade(), "C")

    def test_grade_below_40(self):
        self.student.add_marks("Math", 39)
        self.assertEqual(self.student.calculate_grade(), "F")

    def test_average_of_multiple_subjects(self):
        self.student.add_marks("Math", 80)
        self.student.add_marks("Physics", 60)

        self.assertEqual(self.student.calculate_average(), 70)
        self.assertEqual(self.student.calculate_grade(), "B")

    def test_no_marks_returns_zero_average(self):
        self.assertEqual(self.student.calculate_average(), 0.0)

    def test_no_marks_returns_f_grade(self):
        self.assertEqual(self.student.calculate_grade(), "F")

    def test_invalid_marks_raise_error(self):
        with self.assertRaises(ValueError):
            self.student.add_marks("Math", 101)

        with self.assertRaises(ValueError):
            self.student.add_marks("Math", -1)


if __name__ == "__main__":
    unittest.main()
