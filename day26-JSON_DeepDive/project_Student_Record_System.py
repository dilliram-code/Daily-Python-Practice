'''--------Project: Studenet Record System (Beginner Level)--------'''

import json
import os

FILE_NAME = "students.json"

# load data from json file if exists
def load_data():
  if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as f:
      return json.load(f)
  return []                           # return empty list if file not found

# save data to JSON file
def save_data(data):
  with open(FILE_NAME, 'w') as f:
    json.dump(data, f, indent=2) 
  
# add a new student
def add_student():
  name = input("enter your name: ").strip()
  roll = int(input("enter your roll: ").strip())
  marks = float(input("enter your marks: ").strip())

  # a dict that stores above info
  student = {"name": name, "roll": roll, "marks": marks}
  students.append(student)                # students -> empty list initially
  save_data(students)                     # injects students into FILE_NAME 
  print("✅ student added successfully!")

# display all students
def show_students():
  if not students:
    print("No students record found!")
    return
  print("\n------------Students' Record-----------")
  for s in students:
    print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
  print()


# main_menu
students = load_data()                # load_data() -> a json file (or a list)
def menu():
  while True:
    print("""
          1. Add student
          2. Show students
          3. Exist
          """)  
    choice = input("enter your choice: ").strip()
    if choice == '1':
      add_student()
    elif choice == '2':
      show_students()
    elif choice == '3':
      print("Goodbye!")
      break
    else:
      print("Invalid choice! Try again.")


if __name__== "__main__":
  menu()