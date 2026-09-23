"""
Topic: Inner (Nested) Classes
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# A class defined inside another class is useful for tightly-coupled helper structures.

# ============================================
# 2. EXAMPLE
# ============================================

class Library:
    class Book:
        def __init__(self, title):
            self.title = title

    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Library.Book(title))

lib = Library()
lib.add_book("Bumi Manusia")
print(lib.books[0].title)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Define a simple inner class inside an outer class.
# EXERCISE 2 (easy): Create an instance of the inner class through the outer class.
# EXERCISE 3 (easy): Explain a real scenario where an inner class makes sense (e.g. Node inside LinkedList).
# EXERCISE 4 (medium): Add a method to the outer class that creates and returns inner class instances.
# EXERCISE 5 (medium): Compare defining the same structure as a separate top-level class instead.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Design a `LinkedList` class with an inner `Node` class, supporting an `append(value)` method.


# ============================================
# 5. SUMMARY
# ============================================
# Inner classes group tightly related helper structures inside the class that owns them.
