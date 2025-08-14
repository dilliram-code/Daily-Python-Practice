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
                print("No matching not found!")


# search_notes()
