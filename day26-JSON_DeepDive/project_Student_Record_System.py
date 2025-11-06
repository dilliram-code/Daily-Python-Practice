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