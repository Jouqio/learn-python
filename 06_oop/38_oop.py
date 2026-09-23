"""
Topic: OOP Introduction
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Object-Oriented Programming organizes code around objects that combine data (attributes) and behavior (methods).

# ============================================
# 2. EXAMPLE
# ============================================

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author}"

book = Book("Laskar Pelangi", "Andrea Hirata")
print(book.describe())

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a simple class with 2 attributes and 1 method.
# EXERCISE 2 (easy): Create two instances of the same class with different data.
# EXERCISE 3 (easy): Explain (via prints) the difference between a class and an object/instance.
# EXERCISE 4 (medium): Add a method that changes one of the object's attributes.
# EXERCISE 5 (medium): List 3 real-world examples that would make good classes.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Design a `Product` class with name, price, and stock, plus a method `is_in_stock()`.


# ============================================
# 5. SUMMARY
# ============================================
# OOP groups related data and behavior together, making complex programs easier to model and maintain.
