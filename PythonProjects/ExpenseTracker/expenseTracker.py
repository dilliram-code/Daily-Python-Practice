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
