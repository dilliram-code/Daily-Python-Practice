tasks = []


def show_menu():
    print("\n======== To-Do-List =========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
 

while True:
    show_menu()
    choice = input("Enter your choice.")

    if choice == "1":
        task = input("Enter task.")
        tasks.append(task)
        print("Task added!")
