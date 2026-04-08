class Book:
    def __init__(self, title: str, author: str, book_rating: float) -> None:
        self.title: str = title
        self.author: str = author
        self.book_rating: float = book_rating

    # Task C
    def __str__(self) -> str:
        return f"Book: {self.title} (Author: {self.author}, Rating: {self.book_rating})"

    # Task D
    def __repr__(self) -> str:
        return f"Book(title='{self.title}', author='{self.author}', book_rating={self.book_rating})"

    # Task E
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return (
            self.title == other.title and
            self.author == other.author and
            self.book_rating == other.book_rating
        )

    # Task F
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.book_rating < other.book_rating


# =========================
# Testing
# =========================

book1: Book = Book("Mile High", "Liz Tomforde", 4.5)

# Task A
print("A) Define the book class")
print("Title:", book1.title)
print("Author:", book1.author)
print("Book Rating:", book1.book_rating)

print("\n" + "-"*40 + "\n")

# Task B
print("B) Inspect internal structure")
print("Book dict:", book1.__dict__)

book1.__dict__["book_rating"] = 4.8
print("Updated book_rating:", book1.book_rating)
# The book1 object now has a rating of 4.8, which we will work with in the future

print("\n" + "-"*40 + "\n")

# Task C
print("C) Implement __str__")
print(book1)

print("\n" + "-"*40 + "\n")

# Task D
print("D) Implement __repr__")
print(repr(book1))

print("\n" + "-"*40 + "\n")

# Task E
print("E) Implement equality(__eq__)")
book2: Book = Book("Mile High", "Liz Tomforde", 4.8)
book3: Book = Book("Corrupt", "Penelope Douglas", 4.7)

print("book1 == book2:", book1 == book2)  # True
print("book1 == book3:", book1 == book3)  # False
print("book1 == 5:", book1 == 5)          # False

print("\n" + "-"*40 + "\n")

# Task F
print("F) Implement ordering(__lt__)")
book1_taskF: Book = Book("A", "Bob", 4.5)
book2_taskF: Book = Book("C", "Bob", 4.8)

print("book1 < book2:", book1_taskF < book2_taskF)  # True
print("book2 < book1:", book2_taskF < book1_taskF)  # False

try:
    print(book1 < 5)
except TypeError as e:
    print("Error:", e)

print("\n" + "-"*40 + "\n")

# Task G
print("G) Sorting")

books: list[Book] = [
    Book("Credence", "Penelope Douglas", 4.8),
    Book("Love", "Ana Hwan", 4.6),
    Book("On the waves of the tide", "Laura Pavlov", 4.9),
    Book("Judged", "John Marrs", 5.0)
]

books.sort()

for book in books:
    print(book)