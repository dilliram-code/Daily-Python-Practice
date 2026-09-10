import os 
import shutil

EXTENSION_MAP = {
  "PDFs": [".pdf"],
  "IMAGEs" : [".png", ".jpeg", ".jpg"],
  "TEXTs" : [".txt"]
}

def get_destination_folder(filename):
  ext = os.path.splitext(filename)[1].lower()
  for folder, extensions in EXTENSION_MAP:
    if ext in extensions:
      return folder
  return "Others"