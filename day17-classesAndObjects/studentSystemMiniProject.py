class Student:
  def __init__(self, name, roll, age, marks):
    self.name = name
    self.roll = roll
    self.age = age
    self.marks = marks
    
  def display(self):
    print(f"Name: {self.name}, Roll: {self.roll}, Age:  {self.age}")