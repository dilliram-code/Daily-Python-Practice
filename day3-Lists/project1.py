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

def view_students():
  if not students:
    print("No students available.\n")
    return
  print("-------Student Marks-----\n")
  for i,(name, marks) in enumerate(students, start=1):
    print(f"{i}.Name: {name}, Marks: {marks}")
  print()

# view_students()

def update_students():
  name = input("Enter the name of student: ").strip()
  for student in students:
    if student[0].lower() == name.lower():
      new_marks = float(input("Enter new marks: "))
      student[1] = new_marks
      print(f"{name}'s marks updated.\n")
      return
  print("Student not found!")

# update_students()

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

# search_student()

def show_statistics():
  if not students:
    print("No students to analyse.\n")
    return
  marks = [m for _, m in students]    # stores marks only skipping names
  avg = sum(marks)/len(marks)
  highest = max(marks)
  lowest = min(marks)

  print("\n----------Student statistics-------")
  print(f"The average marks: {avg:.2f}")
  print(f"The highest marks: {highest}")
  print(f"The lowest marks: {lowest}\n")

# show_statistics()

# main Menu loop
def main():
  while True:
    print("\n=============Student Management System==========")
    print("""
          1. Add student
          2. View student
          3. Update student
          4. Delete student
          5. Search student
          6. Show statistics
          7. Exit
          """)
    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
      add_students()
    elif choice == 2:
      view_students()
    elif choice == 3: 
      update_students()
    elif choice == 4:
      delete_students()
    elif choice == 5:
      search_student()
    elif choice == 6:
      show_statistics()
    elif choice == 7:
      print("Exiting the program? Good bye!")
      break
    else:
      print("Invalid inpu, please try again!")

# call the main function:
if __name__ == '__main__':
  main()