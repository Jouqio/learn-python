"""
Topic: Magic (Dunder) Methods
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Magic methods like __str__, __eq__, and __len__ let custom objects work with built-in functions and operators.

# ============================================
# 2. EXAMPLE
# ============================================

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1, p2 = Point(1, 2), Point(1, 2)
print(p1, p1 == p2)

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Implement __str__ for a class so print() shows something readable.
# EXERCISE 2 (easy): Implement __eq__ to compare two objects by value.
# EXERCISE 3 (easy): Implement __len__ so len() works on a custom object.
# EXERCISE 4 (medium): Implement __add__ so two objects can be combined with +.
# EXERCISE 5 (medium): Implement __repr__ and explain how it differs from __str__.
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Design a `Vector` class supporting __add__, __sub__, __str__, and __eq__ for 2D vector math.


# ============================================
# 5. SUMMARY
# ============================================
# Magic methods let your custom classes integrate naturally with Python's built-in syntax and functions.
