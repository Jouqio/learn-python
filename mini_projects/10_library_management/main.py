"""Mini Project 10: Library Management"""
from datetime import date, timedelta


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed_by = None
        self.due_date = None

    def borrow(self, member_name, days=7):
        if self.borrowed_by is not None:
            raise ValueError(f"'{self.title}' is already borrowed.")
        self.borrowed_by = member_name
        self.due_date = date.today() + timedelta(days=days)

    def return_book(self):
        self.borrowed_by = None
        self.due_date = None


def main():
    book = Book("Cantik Itu Luka", "Eka Kurniawan")
    book.borrow("Putri")
    print(f"{book.title} borrowed by {book.borrowed_by}, due {book.due_date}")
    book.return_book()
    print(f"Returned. Borrowed by: {book.borrowed_by}")


if __name__ == "__main__":
    main()
