'''------------------------Library Management Project-------------------'''

from typing import List, Optional
import datetime

class Book:
  def __init__(self, book_id: int, title: str, author: str):
    self.book_id = book_id
    self.title = title
    self.author = author
    self.is_borrowed = False
    self.borrowed_by = None         # Name of borrower
    self.borrowed_date: Optional[datetime.date] = None
  
  def __str__(self):
    status = f"Borrowed by {self.borrowed_by}" if self.is_borrowed else "Available"
    return f"[{self.book_id}] {self.title} by {self.author} - {status}" 
  
class Library:
  def __init__(self):
    self.books: List[Book] = []
    self.next_id = 1                # simple auto-incrementing id

  def add_books(self, title: str, author:str):
    book = Book(self.next_id, title, author)
    self.books.append(book)
    self.next_id += 1
    print(f"Added book: {book}")  
  
  def find_book_by_id(self, book_id: int) -> Optional[Book]:
        for b in self.books:
            if b.book_id == book_id:
                return b
        return None
  
  def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for b in self.books:
            print(b)
  def borrow_book(self, book_id: int, borrower_name: str):
        book = self.find_book_by_id(book_id)
        if book is None:
            print("Book not found.")
            return
        if book.is_borrowed:
            print("Book is already borrowed.")
            return
        book.is_borrowed = True
        book.borrowed_by = borrower_name
        book.borrow_date = datetime.date.today()
        print(f"{borrower_name} borrowed '{book.title}' on {book.borrow_date}")
  
  def return_book(self, book_id: int):
        book = self.find_book_by_id(book_id)
        if book is None:
            print("Book not found.")
            return
        if not book.is_borrowed:
            print("Book is not borrowed.")
            return
        # reset borrowing info
        print(f"{book.borrowed_by} returned '{book.title}'")
        book.is_borrowed = False
        book.borrowed_by = None
        book.borrow_date = None

def main():
  lib = Library()

  # Seed sample books
  lib.add_book("The Alchemist", "Paulo Coelho")
  lib.add_book("Atomic Habits", "James Clear")
  lib.add_book("Introduction to Algorithms", "Cormen et al.")
  while True:
        print("\nOptions: list / add / borrow / return / quit")
        choice = input("Enter command: ").strip().lower()
        if choice == "list":
            lib.list_books()
        elif choice == "add":
            t = input("Title: ").strip()
            a = input("Author: ").strip()
            if t and a:
                lib.add_book(t, a)
            else:
                print("Invalid input.")
        elif choice == "borrow":
            try:
                bid = int(input("Book ID to borrow: ").strip())
                name = input("Borrower name: ").strip()
                lib.borrow_book(bid, name)
            except ValueError:
                print("Please enter a valid numeric Book ID.")
        elif choice == "return":
            try:
                bid = int(input("Book ID to return: ").strip())
                lib.return_book(bid)
            except ValueError:
                print("Please enter a valid numeric Book ID.")
        elif choice == "quit":
            print("Goodbye.")
            break
        else:
            print("Unknown command.")
