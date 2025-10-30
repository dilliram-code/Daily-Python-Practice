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

add_students()

def view_students():
  if not students:
    print("No students available.\n")
    return
  print("-------Student Marks-----\n")
  for i,(name, marks) in enumerate(students, start=1):
    print(f"{i}.Name: {name}, Marks: {marks}")
  print()

view_students()

def update_students():
  name = input("Enter the name of student: ").strip()
  for student in students:
    if student[0].lower() == name.lower():
      new_marks = float(input("Enter new marks: "))
      student[1] = new_marks
      print(f"{name}'s marks updated.\n")
      return
  print("Student not found!")

update_students()

def delete_students():
  name = input("Enter student's name: ").strip()
  for student in students:
    if student[0].lower() == name.lower():
      students.remove(student)
      print(f"{name} deleted successfully!")
      return
  print("Student not found!")

# delete_students()

def search_student():
  name = input("Enter name of student: ").strip()
  found = False
  for student in students:
    if name.lower() in student[0].lower():
      print(f"Found: {student[0]} - {student[1]}")
      found = True
  if not found:
    print("Student not found!\n")

search_student()



