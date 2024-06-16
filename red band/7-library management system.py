from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available
        self.borrowed_times = 0
        self.due_date = None

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowing_history = []

class Librarian:
    def __init__(self, name, librarian_id, permissions):
        self.name = name
        self.librarian_id = librarian_id
        self.permissions = permissions

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.librarians = []

    def add_book(self, book):
        self.books.append(book)

    def search_books(self, title=None, author=None, ISBN=None):
        results = []
        for book in self.books:
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (ISBN and ISBN == book.ISBN):
                results.append(book)
        return results

    def add_user(self, user):
        self.users.append(user)

    def borrow_book(self, user_id, ISBN):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.ISBN == ISBN), None)
        if user and book and book.available:
            book.available = False
            book.borrowed_times += 1
            book.due_date = datetime.now() + timedelta(days=14)
            user.borrowing_history.append((book, datetime.now()))
            print(f"Book '{book.title}' borrowed by {user.name}")
        else:
            print("Book not available or user not found")

    def return_book(self, user_id, ISBN):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.ISBN == ISBN), None)
        if user and book and not book.available:
            book.available = True
            book.due_date = None
            print(f"Book '{book.title}' returned by {user.name}")
        else:
            print("Book not found or not borrowed")

    def track_overdue_books(self):
        overdue_books = []
        for book in self.books:
            if not book.available and book.due_date and datetime.now() > book.due_date:
                overdue_books.append(book)
        return overdue_books

    def generate_popularity_report(self):
        sorted_books = sorted(self.books, key=lambda b: b.borrowed_times, reverse=True)
        report = [(book.title, book.borrowed_times) for book in sorted_books]
        return report

# Example usage
library = Library()

# Adding books
library.add_book(Book("1984", "George Orwell", "1234567890"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "1234567891"))

# Adding users
library.add_user(User("Alice", 1))
library.add_user(User("Bob", 2))

# Adding a librarian
library.librarians.append(Librarian("Mr. Smith", 101, ["add_book", "remove_book", "manage_users"]))

# Searching for a book
books_found = library.search_books(title="1984")
for book in books_found:
    print(f"Found book: {book.title} by {book.author}")

# Borrowing a book
library.borrow_book(1, "1234567890")

# Returning a book
library.return_book(1, "1234567890")

# Tracking overdue books
overdue_books = library.track_overdue_books()
for book in overdue_books:
    print(f"Overdue book: {book.title}")

# Generating popularity report
popularity_report = library.generate_popularity_report()
print("Book popularity report:")
for title, times in popularity_report:
    print(f"{title}: borrowed {times} times")
