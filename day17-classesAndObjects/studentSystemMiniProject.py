class Student:
  def __init__(self, name, roll, age, marks):
    self.name = name
    self.roll = roll
    self.age = age
    self.marks = marks
    
  def display(self):
    print(f"Name: {self.name}, Roll: {self.roll}, Age:  {self.age}")
    
class Classroom:
  def __init__(self, course_name):
    self.course_name = course_name
    self.students = []
    
  def add_student(self, student):
    self.students.append(student)
  
  def showAll(self):
    print(f"Class: {self.course_name}")
    for s in self.students:
      s.display()

