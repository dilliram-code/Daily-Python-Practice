import os

NOTES = "my_notes.txt"


# create a file and write on it
def create_note():
    note = input("Enter you note: ")
    with open(NOTES, 'a') as f:
        f.write(note + '\n')
    print("Note saved!")


# create_note()

# view note


def view_note():
    if not os.path.exists(NOTES):
        print("No notes found!")
        return
    with open(NOTES, 'r') as f:
        notes = f.readlines()
        if notes:
            for idx, note in enumerate(notes, 1):
                print(f"{idx}.{note.strip()}")
        else:
            print("No note to display.")


# view_note()

# search notes


def search_notes():
    search_keyword = input("Enter the word to search:")
    found = False
    with open(NOTES, 'r') as f:
        for idx, line in enumerate(f, 1):
            if search_keyword.lower() in line.lower():
                print(f"{idx}.{line.strip()}")
                found = True
            if not found:
                print("No matching note found!")


# search_notes()

# delete notes


def delete_notes():
    view_note()
    try:
        note_number = int(input("Enter the note number: "))
        with open(NOTES, 'r') as f:
            notes = f.readlines()
            if 1 <= note_number <= len(notes):
                del notes[note_number - 1]
                print("Note Deleted!")
                with open(NOTES, 'w') as f:
                    f.writelines(notes)
            else:
                print("Invalid number!")
    except ValueError:
        print("Invalid input!")


# delete_notes()

# main function to start the program


def start_me():
    while True:
        print("\n =======Personal Note Keeper========")
        print("1. Create note.")
        print("2. View note.")
        print("3. Search note.")
        print("4. Delete note.")
        print("5. Exit.")

        choice = input("Choose a number: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            view_note()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_notes()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    start_me()
