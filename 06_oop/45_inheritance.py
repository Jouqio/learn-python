"""
Topic: Inheritance
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
"""

# ============================================
# 1. CONCEPT
# ============================================
# Inheritance lets a subclass reuse and extend a parent class's attributes and methods.

# ============================================
# 2. EXAMPLE
# ============================================

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

print(Animal("Generic").speak())
print(Dog("Rex").speak())

# ============================================
# 3. PRACTICE
# ============================================
# EXERCISE 1 (easy): Create a base class and a subclass that overrides one method.
# EXERCISE 2 (easy): Use super().__init__() to call the parent constructor.
# EXERCISE 3 (easy): Add a new method to the subclass that the parent doesn't have.
# EXERCISE 4 (medium): Create a second subclass and show polymorphic behavior by looping over a list of both.
# EXERCISE 5 (medium): Check inheritance relationships using isinstance() and issubclass().
#
# Write your solutions below this line.


# ============================================
# 4. CHALLENGE
# ============================================
# Design a `Shape` base class with subclasses `Circle` and `Square`, each implementing `area()` differently.


# ============================================
# 5. SUMMARY
# ============================================
# Inheritance promotes code reuse by letting subclasses build on shared parent behavior.
