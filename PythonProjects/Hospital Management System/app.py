'''---------------------Hospital Management System---------------------'''

import uuid
from datetime import datetime, timedelta

def generate_id(prefix=""):
  return prefix + uuid.uuid4().hex[:6]

# print(generate_id())              # debugging line

class Person:
  def __init__(self, name, phone):
    self.id = generate_id("U-")
    self.name = name
    self.phone = phone
  
  def __str__(self):
    return f"{self.name} ({self.phone})"

person1 = Person("Dilli", "9803773533")
print(person1)