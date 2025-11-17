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

lib = Library()
lib.add_books("The alchemist", "Poulo Coelho")
