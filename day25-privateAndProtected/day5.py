# This program is about the name mangling in which
# we can access the private variabl by name mangling

class Ascol:

    # constructor
    def __init__(self, level, roll_no):
        self.level = level
        self.__roll_no = roll_no

    @staticmethod
    def faculty(name):
        print("The faculty is ", name)


# create an object of the class
student1 = Ascol("Bachelor", 9080909)

student1.faculty("CBZ")


# Name mangling
# print(student1.__roll_no)
# Definitely, the code above will throw an error since it
# is trying to access the private attribute of the class
# from outside of the class

# However, we can access the private attribute from outside
# of the class by using the name mangling

print("The roll no. of the student1 is ", student1._Ascol__roll_no)
