import datetime
import uuid
class Book():
    def __init__(self, book_id, name, author, total_copies, available_copies):
        self.name = name
        self.author = author
        self.book_id = book_id
        self.no_copies = total_copies
        self.available_copies = available_copies
    def checkout_copy(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    def return_copy(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
class Member():
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    def borrow_book(self, book_id):
        self.books.append(book_id)
    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
class Transaction():
    def __init__(self, member_id, book_id):
        self.transaction_id = str(uuid.uuid4())
        self.member_id = member_id
        self.book_id = book_id
        self.checkout_date = datetime.datetime.now()
        self.return_date = None
    def mark_return(self):
        self.return_date = datetime.datetime.now()
    def is_returned(self):
        return self.return_date is not None
class Library():
    def __init_(self):
        self.books = {}       # book_id -> Book
        self.members = {}     # member_id -> Member
        self.transactions = {}  # transaction_id -> Transaction
    # book
    def add_book(self, book_id, title, author, total_copies=1):
        if book_id in self.books:
            existing_book = self.books[book_id]
            existing_book