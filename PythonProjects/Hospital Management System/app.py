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

class Hospital:
  def __init__(self, name):
    self.name = name  
    self.doctors = {}
    self.patients = {}
    self.appointments = []

  def add_doctor(self, doctor):
    self.doctors[doctor.id] = doctor

  def add_patient(self,patient):
    self.patients[patient.id] = patient
    
  def book_appointment(self, patient_id, doctor_id, time_slot):
    doctor = self.doctors.get(doctor_id)
    patient = self.patients.get(patient_id)

    if not doctor or not patient:
      return "Doctor or Patient not found!"
  
    # check availability
    if not doctor.is_available(time_slot):
      return "Doctor is not available at this time."
    
    # book it
    doctor.add_appointment(time_slot)
    self.appointments.append(patient_id, doctor_id, time_slot)
    return "Appointment booked successfully!"
  
  def list_doctors(self):
    for doc in self.doctors.values():
      print(f"{doc.id} | {doc.name} | {doc.speciality} ")
  
  def list_patients(self):
    for pat in self.patients.values():
      print(f"{pat.id} | {pat.name} | Age {pat.age}")

# Polymorphism: Bill System
class Bill:
  '''Base Bill'''
  
  def __init__(self, patient_id):
    self.patient_id = patient_id
    self.items = []
  
  def add_item(self, desc, amount):
    self.items.append(desc, amount)


person1 = Person("Dilli", "9803773533")
print(person1)