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
      
# ----------------------------------------------------------
# Polymorphism: Bill System
# ----------------------------------------------------------

class Bill:
  '''Base Bill'''
  
  def __init__(self, patient_id):
    self.patient_id = patient_id
    self.items = []
  
  def add_item(self, desc, amount):
    self.items.append(desc, amount)

  def total(self):
    return sum(a for _, a in self.items)

  def show(self):
    for desc, amt in self.items:
      print(f"{desc}: Rs. {amt}")
    print("Total:", self.total())

class OutpatientBill(Bill):
    """Polymorphism: outpatient has fixed consultation"""

    def finalize(self):
        self.add_item("Consultation Fee", 500)

class InpatientBill(Bill):
    """Polymorphism: inpatient has daily room charges"""

    def __init__(self, patient_id, days):
        super().__init__(patient_id)
        self.days = days

    def finalize(self):
        self.add_item(f"Room Charge ({self.days} days)", self.days * 2000)

def main():
    hospital = Hospital("Nuwakot General Hospital")

    while True:
        print("\n--- HOSPITAL MANAGEMENT ---")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Book Appointment")
        print("4. Generate Bill")
        print("5. Show Doctors")
        print("6. Show Patients")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Doctor Name: ")
            phone = input("Phone: ")
            spec = input("Specialty: ")
            d = Doctor(name, phone, spec)
            hospital.add_doctor(d)
            print("Doctor added with ID:", d.id)

        elif choice == "2":
            name = input("Patient Name: ")
            phone = input("Phone: ")
            age = int(input("Age: "))
            p = Patient(name, phone, age)
            hospital.add_patient(p)
            print("Patient added with ID:", p.id)

        elif choice == "3":
            pid = input("Patient ID: ")
            did = input("Doctor ID: ")
            time_str = input("Appointment (YYYY-MM-DD HH:MM): ")
            try:
                time_slot = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            except:
                print("Invalid date format.")
                continue

            print(hospital.book_appointment(pid, did, time_slot))

        elif choice == "4":
            pid = input("Patient ID: ")
            print("1. Outpatient")
            print("2. Inpatient")
            typ = input("Type: ")

            if typ == "1":
                bill = OutpatientBill(pid)
                bill.finalize()
                bill.show()

            elif typ == "2":
                days = int(input("Days admitted: "))
                bill = InpatientBill(pid, days)
                bill.finalize()
                bill.show()

        elif choice == "5":
            hospital.list_doctors()

        elif choice == "6":
            hospital.list_patients()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()