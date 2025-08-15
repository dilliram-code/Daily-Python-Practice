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

backup_note()