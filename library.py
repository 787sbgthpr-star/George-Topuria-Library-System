import csv
import os
from datetime import datetime

from book import Book
from member import Member
from loan import Loan


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []
        self.load_all()

    def add_book(self, book):
        if self.find_book(book.book_id) is not None:
            raise ValueError("A book with this ID already exists.")
        self.books.append(book)

    def add_member(self, member):
        if self.find_member(member.member_id) is not None:
            raise ValueError("A member with this ID already exists.")
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

        if book is None:
            raise ValueError("Book not found.")

        if member is None:
            raise ValueError("Member not found.")

        if book.available == False:
            raise ValueError("Book is already borrowed.")

        loan_id = len(self.loans) + 1
        today = datetime.now().strftime("%Y-%m-%d")

        loan = Loan(loan_id, book_id, member_id, today)
        self.loans.append(loan)
        book.borrow_book()

    def return_book(self, book_id):
        book = self.find_book(book_id)

        if book is None:
            raise ValueError("Book not found.")

        for loan in self.loans:
            if str(loan.book_id) == str(book_id) and loan.is_active():
                today = datetime.now().strftime("%Y-%m-%d")
                loan.mark_returned(today)
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

    def load_books(self):
        if not os.path.exists("books.csv"):
            return

        with open("books.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) > 0:
                    book = Book(row[0], row[1], row[2], row[3], row[4])

                    if row[5] == "True":
                        book.available = True
                    else:
                        book.available = False

                    self.books.append(book)

    def load_members(self):
        if not os.path.exists("members.csv"):
            return

        with open("members.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) > 0:
                    member = Member(row[0], row[1], row[2])
                    self.members.append(member)

    def load_loans(self):
        if not os.path.exists("loans.csv"):
            return

        with open("loans.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) > 0:
                    loan = Loan(row[0], row[1], row[2], row[3])
                    loan.return_date = row[4]
                    self.loans.append(loan)

    def save_all(self):
        self.save_books()
        self.save_members()
        self.save_loans()

    def load_all(self):
        self.load_books()
        self.load_members()
        self.load_loans()