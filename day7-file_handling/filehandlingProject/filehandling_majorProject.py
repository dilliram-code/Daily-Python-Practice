import os
import csv
from datetime import datetime
import shutil

NOTES = "notes.csv"
BACKUP_NOTES = "backup_notes.csv"

# initiate the note


def initiate_note():
    if not os.path.exists(NOTES):
        with open(NOTES, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Category", "Note"])

# initiate_note()

# Keep backup of the note


def backup_note():
    shutil.copy(NOTES, BACKUP_NOTES)
    print("Back up created!")

# backup_note()

# create_note


def create_note():
    category = input(
        "Enter your category (like: work, pesonal, ideas):").strip()
    note = input("Enter your note: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(NOTES, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, category, note])
        print("note created!")
    backup_note()
    print("Note saved!")


# create_note()

# read note
def view_notes():
    with open(NOTES, 'r', newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        notes = [row for row in reader if row]  # ignore blank rows
        # notes = list(reader)

        if notes:
            for idx, (timestamp, category, note) in enumerate(notes, 1):
                print(f"{idx}.[{timestamp}] ({category}) {note}")
        else:
            print("Notes not found!")


# view_notes()


def searh_notes():
    choice = input(
        "Search by (1) term or (2) by category. Enter 1 or 2 ").strip()
    term = input("Enter the term:").strip()
    term = term.lower()
    found = False

    with open(NOTES, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip the header

        for idx, (timestamp, category, note) in enumerate(reader, 1):
            if ((choice == "1" and term in note.lower()) or (choice == "2" and term in category.lower())):
                print(f"{idx}.[{timestamp}]({category}){note}")
                found = True
    if not found:
        print("No matching note found!")

# searh_notes()

# delete notes


def delete_notes():
    view_notes()
    try:
        note_number = input("Enter the note number to be deleted:")
        note_number = int(note_number)
        with open(NOTES, 'r') as f:
            reader = list(csv.reader(f))

            if (note_number < 1) or (note_number >= len(reader)):
                return
        deleted_note = reader.pop(note_number)
        with open(NOTES, "w") as f:
            writer = csv.writer(f)
            writer.writerows(reader)
        backup_note()
        print("Deleted note: ", deleted_note)

    except:
        print("Invalid input!")
# delete_notes()

# program controller


def start_me():
    initiate_note()
    while True:
        print("\n Personal Note Keeper for daily life!")
        print("Enter 1 to create note.")
        print("Enter 2 to view note.")
        print("Enter 3 to search note.")
        print("Enter 4 to delete note.")
        print("Enter 5 to quit.")
        choose_number = input("Enter a number:").strip()

        if choose_number == "1":
            create_note()
        elif choose_number == "2":
            view_notes()
        elif choose_number == "3":
            searh_notes()
        elif choose_number == "4":
            delete_notes()
        elif choose_number == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input! Try again!")


if __name__ == "__main__":
    start_me()
