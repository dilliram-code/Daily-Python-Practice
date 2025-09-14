
# Example of default value constructor
class Ascol:

    # This is the default value constructor
    def __init__(self, name, room_no=104, floor=1):
        self.name = name
        self.room_no = room_no
        self.floor = floor

    # Instance method: when it is called by the object
    # It will be bound to the object.
    def student_details(self):
        print(f"The room no. of the {self.name}'is {self.room_no} from {self.floor} floor")


# Object creation
# Since, I donot have passed any arguments except for name

student1 = Ascol("Karan")
student1.student_details()


# Let's pass the arguments
student2 = Ascol("Somnath", 107)
student2.student_details()
