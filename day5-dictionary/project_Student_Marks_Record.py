'''--------------------Students Marks Record-----------------'''

# using if else conditionals

marks = {}

while True:
  print('''
      1. Add student
      2. View student
      3. Exit
      ''')
  
  choice = input("Enter your choice (1/2/3): ")
  if choice == '1':
    name = input("enter you name:").strip()
    mark = int(input("enter your marks:").strip())
    marks[name]=mark
    print("✅ marks added!")
  elif choice == '2':
    if not marks:
      print("❌ No record found!")
      break
    else:
      for name, mark in marks.items():
        print(f"Name: {name} - Marks: {mark}")
  elif choice == '3':
    print("Goodbye👋!")
    break
  else:
    print("Invalid input! Try again.")

