# This tutorial is all about accessing the class variables using the instance method.
class Student:
    # Class variable
    school_name = 'ABC School '

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def insider(self):
        print("I am trying to acces the var of class", self.school_name)


# create first object
s1 = Student('Emma', 10)
print(s1.name, s1.roll_no, Student.school_name)
# access class variable

# create second object
s2 = Student('Jessa', 20)
# access class variable
print(s2.name, s2.roll_no, Student.school_name)

inside = Student('Rakul', 45)
inside.insider()
