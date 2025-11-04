""" Contact Book — Beginner level 
Run: python contact_book_basic.py """

from typing import Dict

Contact = Dict[str, str]                # {"phone": "...", "email": "..."}

def add_contact(contacts: Dict[str, Contact]) -> None:
  name = input("Enter you name: ").strip()
  if not name:
    print("Name cannot be empty!")
    return
  if name in contacts:
    print("Contact already exists!")
    return
  phone = input("Enter your phone: ").strip()
  email = input("Enter your email: ").strip()
  contacts[name] = {"Phone:",name, "Email:",email}
  print(f"Added {name}.")

def view_contact(contacts: Dict[str, Contact]) -> None:
  if not contacts:
    print("No contacts found!")
    return
  for name, info in sorted(contacts.items()):
    print(f"{name} - Phone: {info.get("phone", '')}, Email: {info.get("email", '')}")
    
