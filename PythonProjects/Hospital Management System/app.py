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

class Doctor(Person):
  '''Doctor inherits from Person'''
  def __init__(self, name, phone, speciality):
    super().__init__(name, phone)
    self.speciality = speciality
    self.role = "Doctor"  
    self.shedule = []
  
  def is_available(self, time_slot):
    return self.time_slot not in self.shedule

  def add_appointment(self, time_slot):
    self.shedule.append(time_slot)

class Patient(Person):  
  '''Patient inherits from Person + has encapsulated report'''
  def __init__(self, name, phone, age):
    super().__init__(name, phone)
    self.age = age
    self.role = "Patient"
    self._report = None       # ENCAPSULATION

    # Encapsulation: report accessible only through methods

  # This method is often called setter
  def self_report(self, text):
    self._report = text

  # This method is often called getter
  def get_report(self):
    if self._report:  
      return self._report
    return "No medical report found!"


person1 = Person("Dilli", "9803773533")
print(person1)