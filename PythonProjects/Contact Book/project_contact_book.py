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
  contacts[name] = {"Phone:",phone, "Email:",email}
  print(f"Added {name}.")

def view_contact(contacts: Dict[str, Contact]) -> None:
  if not contacts:
    print("No contacts found!")
    return
  for name, info in sorted(contacts.items()):
    print(f"{name} - Phone: {info.get("phone", '')}, Email: {info.get("email", '')}")

def search_contact(contacts: Dict[str, Contact]) -> None:
  name = input("Enter your name: ")
  contact = contacts.get(name)
  if contact:
    print(f"{name} - Phone: {contact['phone']}, Email: {contact['email']}")
  else: 
    print("Not found!")

def update_contact(contacts: Dict[str, Contact]) -> None:
  name = input("enter your name: ").strip()
  if name not in contacts:
    print("Contacts not found!")
    return 
  phone = input(f"New phone (leave blank to keep {contacts[name]['phone']}): ").strip()
  email = input(f"New email (leave blank to keep {contacts[name]['email']}): ").strip()
  if phone:
    contacts[name]['phone'] = phone
  if email:
    contacts[name]['email'] = email
  print("Contact updated!")
def delete_contact(contacts: Dict[str, Contact]) -> None:
  name = input("enter the name to delete: ").strip()
  if name in contacts:
    del contacts[name]
    print("contact deleted!")
  else:
    print("contact not found!")

def menu() -> None:
  contacts: Dict[str, Contact] = {}
  options = {
    "1": ("Add contact", add_contact),
    "2": ("View contact", view_contact),
    "3": ("Search contact", search_contact),
    "4": ("Update contact", update_contact),
    "5": ("Delete contact", delete_contact),
    "0": ("Exit", None)
  }

  while True:
    for k, (desc, _) in options.items():
      print(f"{k}.{desc}")
    choice = input("Choose: ").strip()
    if choice == "0":
      print("goodbye!")
      break
    action = options.get(choice)
    if action:
      action[1](contacts)
    else:
      print("Invalid choice!")
      
if __name__ == "__main__":
  menu()