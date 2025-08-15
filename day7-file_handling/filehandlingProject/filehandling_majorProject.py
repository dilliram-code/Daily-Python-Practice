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
            writer.writerow(["Timestamp, Category, Note"])

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
        next(reader) # skip header
        notes = list(reader)
        
        if notes:
            for idx, (timestamp, category, note) in enumerate(notes,1):
                print(f"{idx}.[{timestamp}] {category} {note}")
        else:
            print("Notes not found!")

view_notes()
