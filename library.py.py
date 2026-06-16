import csv
import os
from datetime import datetime

from book import Book
from member import Member
from loan import Loan

class Library:
def **init**(self):
self.books = []
self.members = []
self.loans = []

```
def add_book(self, book):
    self.books.append(book)

def add_member(self, member):
    self.members.append(member)

def find_book(self, book_id):
    for book in self.books:
        if str(book.book_id) == str(book_id):
            return book
    return None

def find_member(self, member_id):
    for member in self.members:
        if str(member.member_id) == str(member_id):
            return member
    return None

def borrow_book(self, book_id, member_id):
    book = self.find_book(book_id)
    member = self.find_member(member_id)

    if not book:
        raise ValueError("Book not found.")

    if not member:
        raise ValueError("Member not found.")

    if not book.is_available:
        raise ValueError("Book is already borrowed.")

    loan = Loan(
        len(self.loans) + 1,
        book_id,
        member_id,
        datetime.now().strftime("%Y-%m-%d")
    )

    self.loans.append(loan)
    book.borrow()

def return_book(self, book_id):
    book = self.find_book(book_id)

    if not book:
        raise ValueError("Book not found.")

    for loan in self.loans:
        if loan.book_id == book_id and loan.is_active():
            loan.mark_returned(
                datetime.now().strftime("%Y-%m-%d")
            )
            book.return_book()
            return

    raise ValueError("No active loan found.")

def save_books(self):
    with open("books.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for book in self.books:
            writer.writerow(book.to_csv_row())

def save_members(self):
    with open("members.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for member in self.members:
            writer.writerow(member.to_csv_row())

def save_loans(self):
    with open("loans.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for loan in self.loans:
            writer.writerow(loan.to_csv_row())

def save_all(self):
    self.save_books()
    self.save_members()
    self.save_loans()
```
