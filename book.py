class Book:
    def __init__(self, book_id, title, author, genre, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = True

    def borrow_book(self):
        self.available = False

    def return_book(self):
        self.available = True

    def get_status(self):
        if self.available:
            return "Available"
        return "Borrowed"

    def to_csv_row(self):
        return [
            self.book_id,
            self.title,
            self.author,
            self.genre,
            self.year,
            self.available
        ]

    def __str__(self):
        return (
            "ID: " + str(self.book_id) +
            " | Title: " + self.title +
            " | Author: " + self.author +
            " | Genre: " + self.genre +
            " | Year: " + str(self.year) +
            " | Status: " + self.get_status()
        )