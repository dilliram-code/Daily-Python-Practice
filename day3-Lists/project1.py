# Mini Project: Student Management System (Using Lists)

# Features:

# Add new students
# View all students
# Update student marks
# Delete a student
# Search student by name
# Display class statistics (average, highest, lowest)
# Exit program

students = []                             # each student will be stored as [name, marks]

def add_students():
  name = input("Enter student's name: ").strip()
  marks = int(input("Enter student's marks: "))
  students.append([name, marks])
  print(f"{name} added successfully!")


# add_students()
# print(students)